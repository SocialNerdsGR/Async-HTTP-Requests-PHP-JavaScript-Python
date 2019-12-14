FROM node:12-stretch

# Add user.
RUN adduser serveruser

RUN apt-get update && apt-get install -y --no-install-recommends git

WORKDIR /home/serveruser/app

USER serveruser

CMD ["tail", "-f", "/dev/null"]
