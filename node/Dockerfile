FROM node:12-stretch

ARG UID=1000

# Add user.
RUN adduser serveruser -u $UID

RUN apt-get update && apt-get install -y --no-install-recommends git

WORKDIR /home/serveruser/app

USER serveruser

CMD ["tail", "-f", "/dev/null"]
