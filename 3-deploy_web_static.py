#!/usr/bin/python3
"""this module creates a tr in pakgs"""
from fabric.decorators import task
from fabric.api import local, run, env
import os
import tarfile
from datetime import datetime


env.hosts = ['54.160.110.173', '54.236.33.222']
env.key_filename = '~/.ssh/id_rsa'
env.user = 'ubuntu'


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


@task
def do_deploy(archive_path):
    """Deploy the project."""
    if archive_path is None:
        return False

    for host in env.hosts:
        local(f'scp -i {env.key_filename} {archive_path} \
              {env.user}@{host}:/tmp/')

    extract_path = "/data/web_static/releases/"
    with tarfile.open(archive_path, "r:gz") as file:
        file.extractall(path=extract_path)

    run(f'rm /tmp/{os.path.basename(archive_path)}')
    run(f'rm -rf /data/web_static/current')
    run(f'ln -s {extract_path}{os.path.basename(archive_path)[:-4]} \
        /data/web_static/current')

    return True


@task
def deploy():
    """Create and distribute an archive to web servers."""
    archive_path = do_pack()

    if archive_path is None:
        return False

    return do_deploy(archive_path)
