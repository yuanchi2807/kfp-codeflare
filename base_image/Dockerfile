FROM python:3.9.9-slim-bullseye
ENV TZ=US \
    DEBIAN_FRONTEND=noninteractive
USER root
WORKDIR /HAP
RUN apt-get update
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get install -y vim
RUN apt-get install -y sudo
RUN apt-get install -y build-essential
RUN apt-get install -y bash

ENV PYTHONPATH "$PYTHONPATH:/HAP"

RUN useradd -ms /bin/bash hap
RUN usermod -aG sudo hap
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

RUN chown -R hap:hap /HAP
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install --upgrade kubernetes
RUN pip install --upgrade openshift

COPY codeflare-deployment_1.yml /HAP
COPY codeflare-deployment_2.yml /HAP
COPY codeflare-deployment_3.yml /HAP
COPY test.py /HAP

RUN chgrp -R 0 /HAP && \
    chmod -R g=u /HAP

WORKDIR /HAP
CMD ["/bin/bash"]
# CMD [ "python", "/HAP/test.py"]