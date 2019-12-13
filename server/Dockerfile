FROM ubuntu:18.04

RUN \
  # Create user.
  useradd -m serveruser && \
  # Install some packages.
  apt-get update && apt-get install -y --no-install-recommends \
  gcc libc6-dev make \
  python3-minimal python3-dev python3-setuptools python3-pip && \
  pip3 install wheel && \
  pip3 install uvloop ujson sanic

RUN mkdir /home/serveruser/app

COPY server.py /home/serveruser/app/

WORKDIR /home/serveruser/app

USER serveruser

CMD ["python3", "server.py"]
