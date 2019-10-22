#!/usr/bin/env python3
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf

tf.logging.set_verbosity(tf.logging.INFO)


PATH_DATA = './data/breast-cancer-wisconsin.data'
PATH_MODEL = './models/'
NAMES = ["id", "clump_thickness", "unif_cell_size", "unif_cell_shape", "marg_adhesion", "single_epith_cell_size", "bare_nuclei", "bland_chrom", "norm_nucleoli", "mitoses", "class"]
FIELD_DEFAULTS = [[0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], ['']]
LABELS = ['2', '4']

TRAINING_MODEL_NAME = 'breast-cancer-trained'
MODEL_NAME = 'breast-cancer'

SIGNATURE_NAME = 'predict'
OUTPUT_KEYS = ["class_ids", "classes", "logistic", "logits", "probabilities"]

def _parse_line(line):

    fields = tf.decode_csv(line, constant.FIELD_DEFAULTS, field_delim=',', na_value='?')
    features = dict(zip(constant.NAMES, fields))
    class_label = features.pop(constant.NAMES[-1])
    features.pop(constant.NAMES[0])

    return features, class_label


def retrieve_data_from_file(file_name):

    return tf.data.TextLineDataset(file_name).map(_parse_line), {}


def define_feature_columns(training_data):

    features = training_data.make_one_shot_iterator().get_next()[0]

    return [tf.feature_column.numeric_column(
        key=key,
        shape=1,
        default_value=None,
        dtype=features[key].dtype
     ) for key in features.keys()]


def my_input_fn(data_set, buffer_size, batch_size):

    data_set = data_set.shuffle(buffer_size=buffer_size)
    data_set = data_set.batch(batch_size) 
    iterator = data_set.make_one_shot_iterator()
    batch_features, batch_labels = iterator.get_next()

    return batch_features, batch_labels


if __name__ == "__main__":

    training_data, test_data = retrieve_data_from_file(constant.PATH_DATA)

    classifier = tf.estimator.DNNClassifier(
        feature_columns=define_feature_columns(training_data),
        hidden_units=[25, 35, 25],
        n_classes=len(constant.LABELS),
        model_dir= '/tmp/' + constant.TRAINING_MODEL_NAME,
        label_vocabulary=constant.LABELS,
    )

    classifier.train(
        input_fn=lambda: my_input_fn(training_data, 256, 100),
        steps=50
    )

    feature_spec = {}

    for column in define_feature_columns(training_data):
        feature_spec[column.key] = tf.placeholder(
            dtype=column.dtype,
            shape=column.shape,
            name=column.key)

    classifier.export_saved_model(
        export_dir_base=constant.PATH_MODEL + constant.MODEL_NAME,
        serving_input_receiver_fn=tf.estimator.export.build_raw_serving_input_receiver_fn(feature_spec),
        assets_extra=None,
        as_text=False,
        checkpoint_path=None
    )
