from subprocess import call 
from os import listdir
from os.path import isdir

projects = ['image_classification']

for p in projects:
    models_dir = '/'.join([p, 'models'])
    model_dirs = listdir(models_dir)
    for m in model_dirs:
        m_path = '/'.join([models_dir, m])
        if not isdir(m_path):
            continue
        tflite_file = list(filter(lambda x: 'edgetpu' not in x and '.tflite' in x and 'quant' in x, listdir(m_path)))
        if len(tflite_file)>1:
            print('{}: Multiple tflite files'.format(m))
        elif len(tflite_file)==0:
            continue
        tflite_path = '/'.join([m_path, tflite_file[0]])
        call('pwd')
        call("edgetpu_compiler {} -o {}".format(tflite_path, m_path), shell=True)
