#export CUDA_VISIBLE_DEVICES=0
export PYTHONPATH=.

python tools/test_knn.py \
    --name feat_face_ms1mv3_r50 \
    --test_all True \
    --knn_method faiss
