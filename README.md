# pgadmin4_desktop_mode - Start pgadmin4 in desktop mode

Sometimes the desktop mode is the way to go:
 - you can easily access your own files
 - if there is only one user you don't need any user management ...

This package requires pgadmin4 and provides a very simplistic starter for the
desktop mode. pgadmin4 listens on localhost using a port number, which is computed
from the login name. That's currently sufficient for our internal needs. If you
need more, feel free to submit a pull request.

How to use "pgadmin4_desktop_mode":

 1. prepare a virtual env
   > python3 -m venv pgadmin && . pgadmin/bin/activate && \\\
     python -m pip install -U pip && python -m pip install -U setuptools

 2. install pgadmin in desktop mode
   > python -m pip install pgadmin4_desktop_mode

 3. start pgadmin
   > pgadmin4_desktop_mode
