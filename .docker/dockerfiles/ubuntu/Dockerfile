FROM ubuntu:24.04

RUN apt-get update -y \
    && apt-get install -qy \
    openssh-server \
    sshpass \
    sudo \
    && rm -rf /var/lib/apt/lists/*

# Remove the default ubuntu user added on 24.04. See https://askubuntu.com/questions/1513927/ubuntu-24-04-docker-images-now-includes-user-ubuntu-with-uid-gid-1000
RUN touch /var/mail/ubuntu && chown ubuntu /var/mail/ubuntu && userdel -r ubuntu

RUN useradd -rm -d /home/ubuntu -s /bin/bash -g root -G sudo -u 1000 deploy
RUN echo 'deploy:deploy' | chpasswd

RUN service ssh start

USER deploy

EXPOSE 22

CMD ["/usr/sbin/sshd","-D"]


