import os
import numpy as np
import shutil

cluster_file = './data/work_dir/cfg_test_gcne_facefeat/feat_face_ms1mv3_r50_gcne_k_160_th_0.0_ig_0.8/tau_0.6_pred_labels.txt'
filename_list = '/root/jinyfeng/projects/insightface/recognition/arcface_torch/face_feat0.log'

result_path = '/root/jinyfeng/datas/20230801_faces_v2_2619id_cluster_result_v2'
img_folder = '/root/jinyfeng/datas/20230801_faces_v2_2619id'

cluster_result_read = open(cluster_file, 'r')
cluster_result_lines = cluster_result_read.readlines()
filename_list_read = open(filename_list, 'r')
filename_lines = filename_list_read.readlines()

line_num=0
for idx_str in cluster_result_lines:
    idx_str = idx_str.strip('\n')
    subfolder = os.path.join(result_path, idx_str)
    if not os.path.exists(subfolder):
        os.makedirs(subfolder)
    filename = filename_lines[line_num]
#     print('filename========', filename)
    sub_str = '.jpg'
    flag = (sub_str in filename)
#     print('flag=======', flag)
    while not flag:
        line_num+=1
        filename = filename_lines[line_num]
#         print('filename========', filename)
        flag = (sub_str in filename)
#         print('flag=======', flag)
    
    filename = filename.split(' ')[1]
    print('idx_str, filename========', idx_str, filename)
    
    ori_path = os.path.join(img_folder, filename)
    dst_path = os.path.join(subfolder, filename)
    shutil.copy(ori_path, dst_path)
    
    line_num+=1


cluster_result_read.close()
filename_list_read.close()
    
    

