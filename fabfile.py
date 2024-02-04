#!/usr/bin/python3
"""this is a fabric script that creates a tgxz file"""
from fabric import task
import os
import tarfile
from datetime import datetime

@task
def do_pack():
    """this creates a pack"""
    src_dir = "web_static/"
    dest_dir = "web_static/versions"

    if not os.path.exists(src_dir):
        raise Exception(f"The source doesnt exitsts")
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    file_name = f"web_static_{timestamp}.tgz"

    archive_path = os.path.join(dest_dir, file_name)

    with tarfile.open(os.path.join(dest_dir, file_name), "w:gz") as tar:
        tar.add(src_dir, arcname=os.path.basename(src_dir))

    return archive_path if os.path.exists(archive_path) else None
