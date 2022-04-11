#! /bin/sh

echo "Starting services in /etc/service"
exec /usr/bin/supervisord -c /etc/supervisord.conf
