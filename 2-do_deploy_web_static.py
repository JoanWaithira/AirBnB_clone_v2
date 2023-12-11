#!/usr/bin/python3i
# distributes an archive to your web servers, using the function do_deploy


from fabric.api import run, put, env
from os.path import exists
from datetime import datetime

env.hosts = ['54.82.179.171', '100.25.132.241']


def do_deploy(archive_path):
    """
    Distributes an archive to a web server
    """
    if exists(archive_path) is False:
        return False
    try:
        put(archive_path, '/tmp/')
        archive_filename = archive_path.split('/')[-1]
        release_path = '/data/web_static/releases/{}'.format(
                archive_filename.split('.')[0])
        run('mkdir -p {}'.format(release_path))
        run('tar -xzf /tmp/{} -C {}'.format(archive_filename, release_path))
        run('mv {}/web_static/* {}'.format(release_path, release_path))
        run('rm -rf {}/web_static'.format(release_path))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(release_path))
        print('New version deployed!')
        return True
    except:
        return False
