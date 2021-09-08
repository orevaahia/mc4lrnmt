# Decoding params

decode_from_file=$1             # path to source file to be evaluated
decode_to_file=$2               # path to save translated file
reference=$3                    # path to target reference file
PROBLEM=translate_enyo_sub4k
hparams_set=sparse_transformer_magnitude_pruning_tpu
USER_DIR=user_dir/              # modify with path to the user_dir used to generate your data         
DATA_DIR=$PWD/data/t2t_data     # modify with your data path
train_steps=6000
target_sparsity=0.00            # Percentage sparsity
OUTPUT_DIR="/tmp/training/directory" # modify with path to save model checkpoints
cloud_tpu_name='tpu-vm' 



python -m state_of_sparsity.sparse_transformer.decoder \
--t2t_usr_dir $USER_DIR \
--hparams_set $hparams_set \
--output_dir $OUTPUT_DIR \
--model sparse_transformer \
--problem $problem \
--data_dir $DATA_DIR \
--decode_from_file $decode_from_file \
--decode_to_file $decode_to_file \
--decode_hparams "beam_size=5,alpha=0.6" \
--hparams "symbol_modality_num_shards=1"


t2t-bleu --translation $decode_to_file --reference $reference