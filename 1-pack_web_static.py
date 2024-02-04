#!/usr/bin/python3
"""this module creates a tr in pakgs"""
from fabric.decorators import task
import os
import tarfile
from datetime import datetime


@task
def do_pack():
    """Create a .tgz archive from the contents of the web_static folder."""
    src_dir = "web_static/"
    dest_dir = "versions/"

    if not os.path.exists(src_dir):
        raise Exception("The source folder 'web_static/' doesn't exist.")

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = f"web_static_{timestamp}.tgz"

    archive_path = os.path.join(dest_dir, file_name)

    with tarfile.open(archive_path, "w:gz") as tar:
        tar.add(src_dir, arcname=os.path.basename(src_dir))

    print(f"TGZ archive created: {archive_path}")
    return archive_path if os.path.exists(archive_path) else None
