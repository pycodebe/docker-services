FROM continuumio/miniconda3

ARG USERNAME=docker
ARG USERID=1000
ARG CONDA_DIR=/opt/conda
ARG ENV_NAME=text_mining

RUN useradd --create-home -s /bin/bash --no-user-group -u ${USERID} ${USERNAME} && \
    chown ${USERNAME} ${CONDA_DIR} -R && \
    adduser ${USERNAME} sudo && \
    echo "$USERNAME ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

USER ${USERNAME}
WORKDIR /home/${USERNAME}

RUN mkdir staticfiles && \
    chown ${USERNAME} staticfiles

COPY . .

RUN conda env create --file ./environment.yml --force && \
    conda init bash &&  \
    echo "conda activate text_mining" >> /home/${USERNAME}/.bashrc && \ 
    . /home/${USERNAME}/.bashrc

EXPOSE 8002

ENTRYPOINT ["conda", "run", "-n", "text_mining", "./entrypoint.sh"]