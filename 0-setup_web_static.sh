#!/usr/bin/env bash
# a Bash script that sets up my web servers for the deployment of web_static

if ! command -v nginx &> /dev/null; then
	sudo apt-get update
	sudo apt install -y nginx
fi

if [ ! -d "/data/web_static/shared/" ]; then
	sudo mkdir -p "/data/web_static/shared/"
fi

if [ ! -d "/data/web_static/releases/test/" ]; then
	sudo mkdir -p "/data/web_static/releases/test/"
fi

echo '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
ubuntu@89-web-01:~/$ curl localhost/hbnb_static/index.html
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>' > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of
# /data/web_static/current/ to hbnb_static
# (ex: https://www.nguweneza.tech/hbnb_static).
sed -i '/^server {/a \
	location /hbnb_static/ {\
		alias /data/web_static/current/;\
	}' /etc/nginx/site-available/default

sudo service nginx restart
