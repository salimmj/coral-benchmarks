# for each model in the set of projects, run an inference task and collect timing data and save to csv 
import json

import pandas as pd

from os import listdir
from os.path import isdir

from image_classification.classify_image import *

LIST_OF_PROJECTS = {
        'image_classification': inference_model_on_image,
        }

def run_full_experiment():
    # for each project
    results = []
    for p in LIST_OF_PROJECTS:
        meta_path = '/'.join([p, 'metadata.json'])
        models_path = '/'.join([p, 'models'])
        data_path = '/'.join([p, 'data'])
        metadata = json.loads(open(meta_path).read())
        models = listdir(models_path) 
        for m in models:
            model_path = '/'.join([models_path, m])
            if not isdir(model_path):
                continue
            quant = 'quant' in m 
            model_files = list(filter(lambda x: '.tflite' in x, listdir(model_path)))
            for mfile in model_files:
                edgetpu = 'edgetpu' in mfile
                for image in listdir(data_path):
                    results.append([p, m, quant, edgetpu, *LIST_OF_PROJECTS[p](mfile, '/'.join([p, 'data', image]))])
    return results

if __name__=='__main__':
    df = pd.DataFrame(run_full_experiment(), columns=['project', 'model', 'quant', 'edgetpu']) 
    df.to_csv('results.csv', index=False)
