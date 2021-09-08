

USER_DIR=user_dir/              # modify with path to the user_dir used to generate your data
PROBLEM=translate_enyo_sub4k    # modify with name of problem specific to data generator      
hparams_set=sparse_transformer_magnitude_pruning_tpu
DATA_DIR=$PWD/data/t2t_data     # modify with your data path
train_steps=6000
target_sparsity=0.00            # Percentage sparsity
OUTPUT_DIR="/tmp/training/directory" # modify with path to save model checkpoints
cloud_tpu_name='tpu-vm'  


echo "Started training ..."
python -m state_of_sparsity.sparse_transformer.trainer \
  --t2t_usr_dir $USER_DIR \
  --model sparse_transformer \
  --problem $problem  \
  --hparams_set $hparams_set\
  --data_dir $DATA_DIR\
  --output_dir $OUTPUT_DIR \
  --train_steps $train_steps\
  --use_tpu True \
  --eval_steps $eval_steps \
  --cloud_tpu_name $cloud_tpu_name- \
  --target_sparsity $target_sparsity \
  --begin_pruning_step 5900 \
  --end_pruning_step 6000 \
  --pruning_frequency 500 \
  --decode_hparams "batch_size=256"


