#!/usr/bin/python3
# Fabfile to generate a .tgz archive from the contents of web_static.
import os.path
from datetime import datetime
from fabric.api import local, lcd

def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    dt = datetime.utcnow()
    archive_file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                                 dt.month,
                                                                 dt.day,
                                                                 dt.hour,
                                                                 dt.minute,
                                                                 dt.second)
    if os.path.isdir("versions") is False:
        local("mkdir -p versions")

    with lcd("web_static"):
        result = local("tar -cvzf {} .".format(archive_file), capture=True)

    if result.failed:
        return None

    return archive_file
