FROM jupyter/pyspark-notebook:lab-4.0.2

USER root

# Cài Python 3.10 và đặt làm mặc định
RUN apt-get update && \
    apt-get install -y software-properties-common curl && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y python3.10 python3.10-dev python3.10-distutils python3.10-venv && \
    curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10 && \
    ln -sf /usr/bin/python3.10 /usr/bin/python && \
    ln -sf /usr/local/bin/pip /usr/bin/pip && \
    python --version && \
    pip install --upgrade pip && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Cài các thư viện cần thiết cho Spark và ML
RUN pip install --no-cache-dir pandas numpy matplotlib pyspark tensorflow keras scikit-learn

USER $NB_UID
WORKDIR /home/jovyan/work
