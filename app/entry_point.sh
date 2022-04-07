#! /bin/sh

pwd
echo "Starting services in /etc/service"
exec /usr/bin/supervisord -c /etc/supervisord.conf

# echo "inf loop"
# while true; do sleep 1000; done
# echo "inf loop end"
