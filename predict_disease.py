# Import Dependencies
import csv
import pandas as pd
import numpy as np
from collections import defaultdict
import seaborn as sns
import matplotlib.pyplot as plt
disease_list = []
disease_symptom_dict = defaultdict(list)
disease_symptom_count = {}
count = 0

df = pd.read_excel('./data/raw_data.xlsx')
data = df.fillna(method='ffill')
print(data.tail())


print(list(data))

print(data.count())


# Process Disease and Symptom Names
def data_process(data):
    data_list = []
    data_name = data.replace('^','_').split('_')
    print(data)
    n = 1
    for names in data_name:
        if (n % 2 == 0):
            data_list.append(names)
        n += 1
    return data_list




for idx, row in data.iterrows():
    
    # Get the Disease Names
    if (row['Disease'] !="\xc2\xa0") and (row['Disease'] != ""):
        disease = row['Disease']
        disease_list = data_process(data=disease)
        count = row['Count of Disease Occurrence']

    # Get the Symptoms Corresponding to Diseases
    if (row['Symptom'] !="\xc2\xa0") and (row['Symptom'] != ""):
        symptom = row['Symptom']
        symptom_list = data_process(data=symptom)
        for d in disease_list:
            for s in symptom_list:
                disease_symptom_dict[d].append(s)
            disease_symptom_count[d] = count


detected_symptoms_disease = pd.DataFrame(list(disease_symptom_dict.items()), columns=['Disease','Symptom'])

