#!/usr/bin/env bash
# this sets server for deploayment
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

echo "<!DOCTYPE html>
        <html lang="en">
	    <head>This is the head</head>
        <body> This is the test html</body>
        </html>