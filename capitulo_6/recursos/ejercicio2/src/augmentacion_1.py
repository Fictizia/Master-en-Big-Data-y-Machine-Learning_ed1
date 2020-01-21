#/bin/env python3
# ==============================================================================
# Copyright (c) Moises Martinez by Fictizia. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

import imageio
from imgaug import augmenters as iaa
import numpy
import os

numpy.random.bit_generator = numpy.random._bit_generator

class Augmentations:

    def __init__(self, rotations = [15], scales=[25]):

        self.__output = '../data_augmented/'
        self.__filters = dict()

        for value in rotations:
             self.__filters['rotation_' + str(value)] = iaa.Affine(rotate=value)

        for value in scales:
             self.__filters['scale_' + str(value)] = iaa.Affine(scale=value)
    
        self.__filters['grey'] = iaa.Grayscale(alpha=1.0)
        self.__filters['half_grey'] = iaa.Grayscale(alpha=0.5)
        self.__filters['flip_h'] = iaa.Fliplr(1.0)
        self.__filters['flip_v'] = iaa.Flipud(1.0)

    @property
    def output_folder(self):
        return self.__output

    def get_filters(self):
        return self.__filters.items()

folder = '../data/'

rots = Augmentations([15, 30, 45, 60, 75, 90], [0.25, 0.50, 0.75])

for base, dirs, files in os.walk(folder):
    for file in files:
        image = imageio.imread(base + file)

        name = file.split('.')[0]
        ext = file.split('.')[1]

        for id, filter in rots.get_filters():
            image_augmented = filter.augment_images([image])[0]
            imageio.imwrite(rots.output_folder + name + '_' + id + '.' + ext, image_augmented)

exit(1)
