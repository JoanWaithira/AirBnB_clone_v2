#!/usr/bin/python3
# A fabric script that generates a .tgz archive from the content

from datetime import datetime
from fabric.api import local
import os.path


def do_pack():
    """
    Making an archive on the web static folder
    """
    local("mkdir -p versions")

    now = datetime.utcnow()
    archive_name = "web_static_{}{}{}{}{}{}.tgz".format(
        now.year, now.month, now.day, now.hour, now.minute, now.second
    )
    result = local("tar -cvzf versions/{} web_static".format(archive_name))
    if result.failed:
        return None
    else:
        archive_size = os.path.getsize(file)
        print(f"web_static packed: {file} -> {archive_size} Bytes")
        return file
