#!/usr/bin/python3
"""this creates fabfile for tar"""
import os.path
from datetime import datetime
from fabric.api import local

def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    timestamp = datetime.now().strftime("%Y%m%D%H%M%S")
    file = f"versions/web_static_{timestamp}"
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local(f"tar -cvzf {file} web_static").failed is True:
        return None
    return file
