#!/usr/bin/env python3

import json

def print_file(file_name):

    file = open(file_name, "r")

    for line in file:
        print(line)

    file.close()


def read_file(file_name):

    raw_data = list()

    file = open(file_name, "r")

    for line in file:
        raw_data.append(line.replace('\n', ''))

    file.close()

    return raw_data


def generar_linea(lista, separador=';'):

    if lista is None:
        return None

    values = lista[0]

    for i in range(1, len(lista)):
        values = values + separador + lista[i]

    return values


def create_csv_file(file_name, names, data):

    file = open(file_name, "w")

    file.write(generar_linea(names))

    for line in data:
        file.write(generar_linea(line.split(',')))

    file.close()


def create_json_file(file_name, names, raw_data):

    file = open(file_name, "w")
    data = []
    template_position = list()

    for name in names:
        template_position.append(name)

    for linea in raw_data:
        template = dict()
        values = linea.split(',')
        for i in range(len(values)):
            template[template_position[i]] = values[i]

        data.append(template)

    file.write(json.dumps(data))

    file.close()


if __name__ == "__main__":

    names = ["id", "clump_thickness", "unif_cell_size", "unif_cell_shape", "marg_adhesion", "single_epith_cell_size", "bare_nuclei", "bland_chrom", "norm_nucleoli", "mitoses", "class"]
    data = read_file("./data/breast-cancer-wisconsin.data")
    create_csv_file("output.csv", names, data)
    create_json_file("output.json", names, data)
