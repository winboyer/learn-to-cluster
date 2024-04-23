import os
import numpy as np

feat_num = 12967
filepath = '/root/jinyfeng/projects/learn-to-cluster/data/labels/feat_face_ms1mv3_r50_v1.meta'
filew = open(filepath, 'w')
for idx in range(feat_num):
    filew.write('-1 \n')

filew.close()

