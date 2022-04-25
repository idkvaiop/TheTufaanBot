#!/bin/bash
clear
echo "
 
╭━━━━┳╮╱╭┳━━━┳━━━┳━━━┳━╮╱╭┳━━╮╭━━━┳━━━━╮
┃╭╮╭╮┃┃╱┃┃╭━━┫╭━╮┃╭━╮┃┃╰╮┃┃╭╮┃┃╭━╮┃╭╮╭╮┃
╰╯┃┃╰┫┃╱┃┃╰━━┫┃╱┃┃┃╱┃┃╭╮╰╯┃╰╯╰┫┃╱┃┣╯┃┃╰╯
╱╱┃┃╱┃┃╱┃┃╭━━┫╰━╯┃╰━╯┃┃╰╮┃┃╭━╮┃┃╱┃┃╱┃┃
╱╱┃┃╱┃╰━╯┃┃╱╱┃╭━╮┃╭━╮┃┃╱┃┃┃╰━╯┃╰━╯┃╱┃┃
╱╱╰╯╱╰━━━┻╯╱╱╰╯╱╰┻╯╱╰┻╯╱╰━┻━━━┻━━━╯╱╰╯
"
# Termux session string generator for TufaanBot
echo Starting dependency installation in 5 seconds...
sleep 5
apt-get update
apt-get upgrade -y
pkg upgrade -y
pkg install python wget -y
wget https://raw.githubusercontent.com/AKHIL-SI/TheTufaanBot/master//userbot-setup.py
pip install telethon
python userbot-setup.py
