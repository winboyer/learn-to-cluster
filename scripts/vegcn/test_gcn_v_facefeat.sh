config=vegcn/configs/cfg_test_gcnv_facefeat.py
load_from=data/pretrained_models/pretrained_gcn_v_ms1m.pth

export CUDA_VISIBLE_DEVICES=1
export PYTHONPATH=.

python vegcn/main.py \
    --config $config \
    --phase 'test' \
    --load_from $load_from \
    --save_output \
    --eval_interim \
    --force
