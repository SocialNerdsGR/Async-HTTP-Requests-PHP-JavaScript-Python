FROM ubuntu:18.04

RUN \
  # Create user.
  adduser serveruser && \
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
