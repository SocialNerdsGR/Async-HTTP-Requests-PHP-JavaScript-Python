FROM ubuntu:18.04

# Get user id and group id from arguments.
ARG UID
ARG GID

RUN \
  # Create user.
  groupadd -r serveruser -g $GID && useradd -ms /bin/bash serveruser -u $UID -g $GID && \
  # Install some packages.
  apt-get update && apt-get install -y --no-install-recommends \
  git python3-minimal python3-setuptools python3-pip && \
  pip3 install --user --upgrade setuptools && \
  pip3 install wheel requests aiohttp && \
  # Change permissions.
  chown -R serveruser:serveruser /home/serveruser

WORKDIR /home/serveruser/app

USER serveruser

CMD ["tail", "-f", "/dev/null"]
