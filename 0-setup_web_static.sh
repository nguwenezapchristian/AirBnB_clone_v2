#!/usr/bin/env bash
# This script sets up directories and deploys a simple HTML page

# Define directories
directories=(
    "/data/"
    "/data/web_static/"
    "/data/web_static/releases/"
    "/data/web_static/shared/"
    "/data/web_static/releases/test/"
)

for dir in "${directories[@]}"; do
    if [ ! -d "$dir" ]; then
        mkdir -p "$dir"
    fi
done

html_content='<!DOCTYPE html>
<html lang="en">
<head></head>
<body>
    Holberton School
</body>
</html>'

echo "$html_content" > "/data/web_static/releases/test/index.html"

ln -sfT "/data/web_static/releases/test/" "/data/web_static/current"

chown -R ubuntu:ubuntu /data/
