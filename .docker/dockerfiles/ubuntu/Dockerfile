FROM ubuntu:22.04

RUN apt-get update -y \
    && apt-get install -qy \
    openssh-server \
    sshpass \
    sudo \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -rm -d /home/ubuntu -s /bin/bash -g root -G sudo -u 1000 test

RUN  echo 'test:test' | chpasswd

RUN service ssh start

EXPOSE 22

CMD ["/usr/sbin/sshd","-D"]


