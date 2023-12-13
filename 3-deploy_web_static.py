#!/usr/bin/python3
# a Fabric script (based on the file 2-do_deploy_web_static.py) 

from fabric.api import local, run, put, env
from datetime import datetime
import os

env.hosts = ['54.82.179.171', '100.25.132.241']

