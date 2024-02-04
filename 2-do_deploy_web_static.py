#!/usr/bin/python3
"""this module creates a tr in pakgs"""
from fabric.decorators import task
from fabric.api import local, run, env
import os
import tarfile


env.hosts = ['54.160.110.173', '54.236.33.222']
env.key_filename = '~/.ssh/id_rsa'
env.user = 'ubuntu'


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
