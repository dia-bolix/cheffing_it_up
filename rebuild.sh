#!/bin/bash
# This runs on the production server: fetches new code,
# Installs needed packages, and restarts the server.

touch rebuild
echo "Rebuilding"

echo "Pulling code from master"
git pull origin master

echo "Activating virtual environment"
source ~/.virtualenvs/my-virtualenv/bin/activate

echo "CD into directory"
cd ~/cheffing_it_up

echo "Installing packages"
pip install -r requirements.txt

echo "Going to reboot the webserver"
pa_reload_webapp.py alstonS.pythonanywhere.com

touch reboot
echo "Finished rebuild."
