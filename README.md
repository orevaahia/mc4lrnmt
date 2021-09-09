# The Low-Resource Double Bind: An Empirical Study of Pruning for Low-Resource Machine Translation

Link to paper: (https://openreview.net/pdf?id=qw1qqFlw6O2)

This code is built based on the Tensor2Tensor implementation: (https://github.com/tensorflow/tensor2tensor) and https://github.com/google-research/google-research/tree/master/state_of_sparsity

## Running the Code:
We run all our experiments on Cloud TPU v2-8


### Data Preparation

To create a dataset in the right format, follow instructions here (https://github.com/tensorflow/tensor2tensor/blob/master/tensor2tensor/data_generators/README.md). An example of data generator script when using custom data is found here (). 

```
pip install -r requirements.txt
cd scripts 
bash data_gen.sh
```

The above commands will:
1. Install all requirements
2. Change your present working directory to the directory containing all scripts.
3. Generate the data after modifying the data_gen.sh script with the right paths. 


Run the train.sh and decode.sh script to train the model and evaluate afterwards. 

```
bash train.sh
bash decode.sh
```

More details on how to train and evaluate a transformer model with tensor2tensor can be found here (https://github.com/tensorflow/tensor2tensor)
