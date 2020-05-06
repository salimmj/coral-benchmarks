
s = \
"""Mobilenet_V1_0.25_128_quant	paper, tflite&pb	0.5 Mb	39.5%	64.4%	0.8 ms	2 ms
Mobilenet_V1_0.25_160_quant	paper, tflite&pb	0.5 Mb	42.8%	68.1%	1.3 ms	2.4 ms
Mobilenet_V1_0.25_192_quant	paper, tflite&pb	0.5 Mb	45.7%	70.8%	1.8 ms	2.6 ms
Mobilenet_V1_0.25_224_quant	paper, tflite&pb	0.5 Mb	48.2%	72.8%	2.3 ms	2.9 ms
Mobilenet_V1_0.50_128_quant	paper, tflite&pb	1.4 Mb	54.9%	78.1%	1.7 ms	2.6 ms
Mobilenet_V1_0.50_160_quant	paper, tflite&pb	1.4 Mb	57.2%	80.5%	2.6 ms	2.9 ms
Mobilenet_V1_0.50_192_quant	paper, tflite&pb	1.4 Mb	59.9%	82.1%	3.6 ms	3.3 ms
Mobilenet_V1_0.50_224_quant	paper, tflite&pb	1.4 Mb	61.2%	83.2%	4.7 ms	3.6 ms
Mobilenet_V1_0.75_128_quant	paper, tflite&pb	2.6 Mb	55.9%	79.1%	3.1 ms	3.2 ms
Mobilenet_V1_0.75_160_quant	paper, tflite&pb	2.6 Mb	62.4%	83.7%	4.7 ms	3.8 ms
Mobilenet_V1_0.75_192_quant	paper, tflite&pb	2.6 Mb	66.1%	86.2%	6.4 ms	4.2 ms
Mobilenet_V1_0.75_224_quant	paper, tflite&pb	2.6 Mb	66.9%	86.9%	8.5 ms	4.8 ms
Mobilenet_V1_1.0_128_quant	paper, tflite&pb	4.3 Mb	63.3%	84.1%	4.8 ms	3.8 ms
Mobilenet_V1_1.0_160_quant	paper, tflite&pb	4.3 Mb	66.9%	86.7%	7.3 ms	4.6 ms
Mobilenet_V1_1.0_192_quant	paper, tflite&pb	4.3 Mb	69.1%	88.1%	9.9 ms	5.2 ms
Mobilenet_V1_1.0_224_quant	paper, tflite&pb	4.3 Mb	70.0%	89.0%	13 ms	6.0 ms
Mobilenet_V2_1.0_224_quant	paper, tflite&pb	3.4 Mb	70.8%	89.9%	12 ms	6.9 ms
Inception_V1_quant	paper, tflite&pb	6.4 Mb	70.1%	89.8%	39 ms	36 ms
Inception_V2_quant	paper, tflite&pb	11 Mb	73.5%	91.4%	59 ms	18 ms
Inception_V3_quant	paper,tflite&pb	23 Mb	77.5%	93.7%	148 ms	74 ms
Inception_V4_quant	paper, tflite&pb	41 Mb	79.5%	93.9%	268 ms	155 ms
DenseNet	paper, tflite&pb	43.6 Mb	64.2%	85.6%	195 ms	60 ms	1656 ms
SqueezeNet	paper, tflite&pb	5.0 Mb	49.0%	72.9%	36 ms	9.5 ms	18.5 ms
NASNet mobile	paper, tflite&pb	21.4 Mb	73.9%	91.5%	56 ms	---	102 ms
NASNet large	paper, tflite&pb	355.3 Mb	82.6%	96.1%	1170 ms	---	648 ms
ResNet_V2_101	paper, tflite&pb	178.3 Mb	76.8%	93.6%	526 ms	92 ms	1572 ms
Inception_V3	paper, tflite&pb	95.3 Mb	77.9%	93.8%	249 ms	56 ms	148 ms
Inception_V4	paper, tflite&pb	170.7 Mb	80.1%	95.1%	486 ms	93 ms	291 ms
Inception_ResNet_V2	paper, tflite&pb	121.0 Mb	77.5%	94.0%	422 ms	100 ms	201 ms
Mobilenet_V1_0.25_128	paper, tflite&pb	1.9 Mb	41.4%	66.2%	1.2 ms	1.6 ms	3 ms
Mobilenet_V1_0.25_160	paper, tflite&pb	1.9 Mb	45.4%	70.2%	1.7 ms	1.7 ms	3.2 ms
Mobilenet_V1_0.25_192	paper, tflite&pb	1.9 Mb	47.1%	72.0%	2.4 ms	1.8 ms	3.0 ms
Mobilenet_V1_0.25_224	paper, tflite&pb	1.9 Mb	49.7%	74.1%	3.3 ms	1.8 ms	3.6 ms
Mobilenet_V1_0.50_128	paper, tflite&pb	5.3 Mb	56.2%	79.3%	3.0 ms	1.7 ms	3.2 ms
Mobilenet_V1_0.50_160	paper, tflite&pb	5.3 Mb	59.0%	81.8%	4.4 ms	2.0 ms	4.0 ms
Mobilenet_V1_0.50_192	paper, tflite&pb	5.3 Mb	61.7%	83.5%	6.0 ms	2.5 ms	4.8 ms
Mobilenet_V1_0.50_224	paper, tflite&pb	5.3 Mb	63.2%	84.9%	7.9 ms	2.8 ms	6.1 ms
Mobilenet_V1_0.75_128	paper, tflite&pb	10.3 Mb	62.0%	83.8%	5.5 ms	2.6 ms	5.1 ms
Mobilenet_V1_0.75_160	paper, tflite&pb	10.3 Mb	65.2%	85.9%	8.2 ms	3.1 ms	6.3 ms
Mobilenet_V1_0.75_192	paper, tflite&pb	10.3 Mb	67.1%	87.2%	11.0 ms	4.5 ms	7.2 ms
Mobilenet_V1_0.75_224	paper, tflite&pb	10.3 Mb	68.3%	88.1%	14.6 ms	4.9 ms	9.9 ms
Mobilenet_V1_1.0_128	paper, tflite&pb	16.9 Mb	65.2%	85.7%	9.0 ms	4.4 ms	6.3 ms
Mobilenet_V1_1.0_160	paper, tflite&pb	16.9 Mb	68.0%	87.7%	13.4 ms	5.0 ms	8.4 ms
Mobilenet_V1_1.0_192	paper, tflite&pb	16.9 Mb	69.9%	89.1%	18.1 ms	6.3 ms	10.6 ms
Mobilenet_V1_1.0_224	paper, tflite&pb	16.9 Mb	71.0%	89.9%	24.0 ms	6.5 ms	13.8 ms
Mobilenet_V2_1.0_224	paper, tflite&pb	14.0 Mb	71.8%	90.6%	17.5 ms	6.2 ms	11.23 ms"""


t = """<a href="https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_2018_08_02/mobilenet_v1_0.25_128_quant.tgz">tflite&amp;pb</a>
<a href="https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_2018_08_02/mobilenet_v1_0.25_160_quant.tgz">tflite&amp;pb</a>
<a href="https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_2018_08_02/mobilenet_v1_0.25_192_quant.tgz">tflite&amp;pb</a>
<a href="https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_2018_08_02/mobilenet_v1_0.25_224_quant.tgz">tflite&amp;pb</a>
<a href="https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_2018_08_02/mobilenet_v1_0.5_128_quant.tgz">tflite&amp;pb</a>
<a href="https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_2018_08_02/mobilenet_v1_0.5_160_quant.tgz">tflite&amp;pb</a>
<a href="https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_2018_08_02/mobilenet_v1_0.5_192_quant.tgz">tflite&amp;pb</a>
<a href="https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_2018_08_02/mobilenet_v1_0.5_224_quant.tgz">tflite&amp;pb</a>
<a href="https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_2018_08_02/mobilenet_v1_0.75_128_quant.tgz">tflite&amp;pb</a>
<a href="https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_2018_08_02/mobilenet_v1_0.75_160_quant.tgz">tflite&amp;pb</a>
<a href="https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_2018_08_02/mobilenet_v1_0.75_192_quant.tgz">tflite&amp;pb</a>
<a href="https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_2018_08_02/mobilenet_v1_0.75_224_quant.tgz">tflite&amp;pb</a>
<a href="https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_2018_08_02/mobilenet_v1_1.0_128_quant.tgz">tflite&amp;pb</a>
<a href="https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_2018_08_02/mobilenet_v1_1.0_160_quant.tgz">tflite&amp;pb</a>
<a href="https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_2018_08_02/mobilenet_v1_1.0_192_quant.tgz">tflite&amp;pb</a>
<a href="https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_2018_08_02/mobilenet_v1_1.0_224_quant.tgz">tflite&amp;pb</a>
<a href="https://storage.googleapis.com/download.tensorflow.org/models/tflite_11_05_08/mobilenet_v2_1.0_224_quant.tgz">tflite&amp;pb</a>
<a href="https://storage.googleapis.com/download.tensorflow.org/models/inception_v1_224_quant_20181026.tgz">tflite&amp;pb</a>
<a href="https://storage.googleapis.com/download.tensorflow.org/models/inception_v2_224_quant_20181026.tgz">tflite&amp;pb</a>
<a href="https://storage.googleapis.com/download.tensorflow.org/models/tflite_11_05_08/inception_v3_quant.tgz">tflite&amp;pb</a>
<a href="https://storage.googleapis.com/download.tensorflow.org/models/inception_v4_299_quant_20181026.tgz">tflite&amp;pb</a>
<a href="https://storage.googleapis.com/download.tensorflow.org/models/tflite/model_zoo/upload_20180427/densenet_2018_04_27.tgz">tflite&amp;pb</a>
<a href="https://storage.googleapis.com/download.tensorflow.org/models/tflite/model_zoo/upload_20180427/squeezenet_2018_04_27.tgz">tflite&amp;pb</a>
<a href="https://storage.googleapis.com/download.tensorflow.org/models/tflite/model_zoo/upload_20180427/nasnet_mobile_2018_04_27.tgz">tflite&amp;pb</a>
<a href="https://storage.googleapis.com/download.tensorflow.org/models/tflite/model_zoo/upload_20180427/nasnet_large_2018_04_27.tgz">tflite&amp;pb</a>
<a href="https://storage.googleapis.com/download.tensorflow.org/models/tflite_11_05_08/resnet_v2_101.tgz">tflite&amp;pb</a>
<a href="https://storage.googleapis.com/download.tensorflow.org/models/tflite/model_zoo/upload_20180427/inception_v3_2018_04_27.tgz">tflite&amp;pb</a>
<a href="https://storage.googleapis.com/download.tensorflow.org/models/tflite/model_zoo/upload_20180427/inception_v4_2018_04_27.tgz">tflite&amp;pb</a>
<a href="https://storage.googleapis.com/download.tensorflow.org/models/tflite/model_zoo/upload_20180427/inception_resnet_v2_2018_04_27.tgz">tflite&amp;pb</a>
<a href="https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_2018_02_22/mobilenet_v1_0.25_128.tgz">tflite&amp;pb</a>
<a href="https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_2018_02_22/mobilenet_v1_0.25_160.tgz">tflite&amp;pb</a>
<a href="https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_2018_02_22/mobilenet_v1_0.25_192.tgz">tflite&amp;pb</a>
<a href="https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_2018_02_22/mobilenet_v1_0.25_224.tgz">tflite&amp;pb</a>
<a href="https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_2018_02_22/mobilenet_v1_0.5_128.tgz">tflite&amp;pb</a>
<a href="https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_2018_02_22/mobilenet_v1_0.5_160.tgz">tflite&amp;pb</a>
<a href="https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_2018_02_22/mobilenet_v1_0.5_192.tgz">tflite&amp;pb</a>
<a href="https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_2018_02_22/mobilenet_v1_0.5_224.tgz">tflite&amp;pb</a>
<a href="https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_2018_02_22/mobilenet_v1_0.75_128.tgz">tflite&amp;pb</a>
<a href="https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_2018_02_22/mobilenet_v1_0.75_160.tgz">tflite&amp;pb</a>
<a href="https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_2018_02_22/mobilenet_v1_0.75_192.tgz">tflite&amp;pb</a>
<a href="https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_2018_02_22/mobilenet_v1_0.75_224.tgz">tflite&amp;pb</a>
<a href="https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_2018_02_22/mobilenet_v1_1.0_128.tgz">tflite&amp;pb</a>
<a href="https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_2018_02_22/mobilenet_v1_1.0_160.tgz">tflite&amp;pb</a>
<a href="https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_2018_02_22/mobilenet_v1_1.0_192.tgz">tflite&amp;pb</a>
<a href="https://storage.googleapis.com/download.tensorflow.org/models/mobilenet_v1_2018_02_22/mobilenet_v1_1.0_224.tgz">tflite&amp;pb</a>"""

t = t.split('\n')
links = []
for tt in t:
    tt = tt.replace('<a href="','').replace('">tflite&amp;pb</a>','')
    links.append(tt)

import json
meta = []
lines = []
s = s.split('\n')
for i in s:
    lines.append(i.split('\t'))

# print(links)
for l in lines:
    j = {}
    j['name'] = l[0]
    j['dataset'] = 'bird_images'
    j['tflite'] = True
    j['coral'] = False
    j['quantized'] = 'quant' in l[0]
    j['model_size'] = l[3]
    j['top_1'] = l[4]
    j['top_5'] = l[5]
    for ll in links:
        if l[0].lower().replace('.50','.5') in ll:
            j['url'] = ll
            break
        else:
            j['url'] = l[0]
    if j['url'] == l[0]: print(l[0])

    meta.append(j)

print(json.dumps(meta))
