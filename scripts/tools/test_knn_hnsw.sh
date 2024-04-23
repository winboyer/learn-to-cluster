export CUDA_VISIBLE_DEVICES=0
export PYTHONPATH=.

python tools/test_knn.py \
    --name part1_test \
    --knn_method hnsw
