FROM php:7.3-fpm

ARG UID=1000
ARG GID=1000

# Add user.
RUN sed -i -e"s/^user\s=\swww-data/user = serveruser/" /usr/local/etc/php-fpm.d/www.conf && \
  sed -i -e"s/^group\s=\swww-data/group = serveruser/" /usr/local/etc/php-fpm.d/www.conf && \
  sed -i -e"s/^;php_admin_value\[memory_limit\]\s=\s32M/php_admin_value[memory_limit] = 256M\nphp_admin_value[max_input_vars] = 5000/" /usr/local/etc/php-fpm.d/www.conf && \
  echo "\ncatch_workers_output = yes\nphp_admin_value[error_log] = /var/log/fpm-php.www.log\nphp_admin_flag[log_errors] = on\n" >> /usr/local/etc/php-fpm.d/www.conf && \
  touch /usr/local/etc/php/php.ini && echo "memory_limit = 256M\n" >> /usr/local/etc/php/php.ini && \
  touch /var/log/fpm-php.www.log && chmod 777 /var/log/fpm-php.www.log && \
  groupadd -r serveruser -g $GID && useradd -ms /bin/bash serveruser -u $UID -g $GID

RUN apt-get update && apt-get install -y --no-install-recommends git unzip

# Install composer.
RUN cd ~
RUN curl -sS https://getcomposer.org/installer -o composer-setup.php
RUN php composer-setup.php --install-dir=/usr/local/bin --filename=composer
RUN rm -rf composer-setup.php

WORKDIR /home/serveruser/app

USER serveruser

CMD ["tail", "-f", "/dev/null"]
