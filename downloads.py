# downloads models 
from os.path import isdir, isfile
from subprocess import call

import json 

project_dirs = ['image_classification', 'object_detection']

for p_dir in project_dirs:
    if not isdir(p_dir):
        print('{}: Directory not found'.format(p_dir))
        continue
    metadata_path = '/'.join([p_dir, 'metadata.json'])
    if not isfile(metadata_path):
        print('{}: File not found'.format(metadata_path))
        continue
    with open(metadata_path) as f:
        metadata = json.loads(f.read())
        print('{}: contains {} models'.format(p_dir, len(metadata)))
        for model in metadata:
            name = model['name']
            modelname = name.lower()
            modeldir = '/'.join([p_dir, 'models', modelname])
            if not isdir(modeldir):
                if 'url' in  model:
                    print('Downloading {}'.format(name))
                    tar_path = '/'.join([p_dir, 'models', model['url'].split('/')[-1]])
                    print(tar_path)
                    print(modeldir)
                    if isfile(tar_path):
                        call(['rm', tar_path])
                    call(['wget', model['url'], '-O', tar_path])
                    call(['mkdir {} && cd {} && tar -xf {}'.format(modeldir ,modeldir, '../'+model['url'].split('/')[-1])], shell=True)
                    call(['rm', tar_path])
                else:
                    print('{} not found and url unavailable'.format(name))
        print('{}: all models are installed'.format(p_dir)) 
