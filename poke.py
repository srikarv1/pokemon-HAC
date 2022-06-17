import csv
import numpy as np 
import pandas as pd
import scipy.cluster


def load_data(filepath):
    return_list = []
    with open(filepath, 'r') as csvfile:
        pokemon_dict = csv.DictReader(csvfile)
        for row in pokemon_dict:
            return_list.append(dict(row))
    for i in return_list:
        i.pop('Generation', None)
        i.pop('Legendary', None)
    for i in return_list:
        i['#'] = int(i['#'])
        i['Total'] = int(i['Total'])
        i['HP'] = int(i['HP'])
        i['Attack'] = int(i['Attack'])
        i['Defense'] = int(i['Defense'])
        i['Sp. Atk'] = int(i['Sp. Atk'])
        i['Sp. Def'] = int(i['Sp. Def'])
        i['Speed'] = int(i['Speed'])
    return return_list


def calculate_x_y(stats):
    atk_stats = int(stats['Attack']) + \
        int(stats['Sp. Atk']) + int(stats['Speed'])
    def_stats = int(stats['Defense']) + \
        int(stats['Sp. Def']) + int(stats['HP'])
    return (atk_stats, def_stats)


def hac(dataset):
    dataset = np.array(dataset)
    return scipy.cluster.hierarchy.linkage(dataset)

if __name__=="__main__":
    result =[]
    tempdata = load_data("Pokemon.csv")
    for i in tempdata:
        result.append(calculate_x_y(i))
    print(hac(result))
    # first column and second column represents the indices of clusters 
    # third column represents distance between these clusters
    # last column represents the number of original observations in the cluster  
