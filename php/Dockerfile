FROM php:7.3-fpm

# Add user.
RUN adduser serveruser

RUN apt-get update && apt-get install -y --no-install-recommends git unzip

# Install composer.
RUN cd ~
RUN curl -sS https://getcomposer.org/installer -o composer-setup.php
RUN php composer-setup.php --install-dir=/usr/local/bin --filename=composer
RUN rm -rf composer-setup.php

WORKDIR /home/serveruser/app

USER serveruser

CMD ["tail", "-f", "/dev/null"]
