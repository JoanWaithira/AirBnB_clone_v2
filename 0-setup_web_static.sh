#!/usr/bin/env bash
# a Bash script that sets up your web servers for the deployment of web_static

sudo apt-get update
sudo apt-get -y install nginx

sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

sudo rm -rf /data/web_static/current
sudo ln -s /data/web_static/releases/test /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/
config_content="
server {
    listen 80;
    server_name _;

    location /hbnb_static {
        alias /data/web_static/current;
    }

    location /redirect_me {
        return 301 http://www.youtube.com;
    }

    error_page 404 /404.html;
    location = /404.html {
        root /usr/share/nginx/html;
        internal;
    }

    add_header X-Served-By $HOSTNAME;
}
"

sudo echo "$config_content" | sudo tee /etc/nginx/sites-available/default

sudo service nginx restart

exit 0
