FROM ubuntu:bionic

# Install the basics
RUN apt-get -y update --fix-missing
RUN apt-get install -y \
	curl \
    wget \
	emacs \
	htop \
	python3 \
	python3-pip python3-dev \
	git 

RUN pip3 install --upgrade pip

# Installs cloudml-hypertune for hyperparameter tuning.
RUN pip install cloudml-hypertune

# Installs google cloud sdk, this is mostly for using gsutil to export model.
RUN wget -nv \
    https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.tar.gz && \
    mkdir /root/tools && \
    tar xvzf google-cloud-sdk.tar.gz -C /root/tools && \
    rm google-cloud-sdk.tar.gz && \
    /root/tools/google-cloud-sdk/install.sh --usage-reporting=false \
        --path-update=false --bash-completion=false \
        --disable-installation-options && \
    rm -rf /root/.config/* && \
    ln -s /root/.config /config && \
    # Remove the backup directory that gcloud creates
    rm -rf /root/tools/google-cloud-sdk/.install/.backup

# Path configuration
ENV PATH $PATH:/root/tools/google-cloud-sdk/bin
# Make sure gsutil will use the default service account
RUN echo '[GoogleCompute]\nservice_account = default' > /etc/boto.cfg

# Add the source-code
RUN mkdir /home/state_of_sparsity
WORKDIR /home/state_of_sparsity
COPY . .

# Install the dependencies
RUN pip3 install -r requirements.txt

# Set the python path
RUN export PYTHONPATH=$PYTHONPATH:$PWD

# Sets up the entry point to invoke the trainer.
ENTRYPOINT ["python3", "sparse_transformer/trainer.py"]


