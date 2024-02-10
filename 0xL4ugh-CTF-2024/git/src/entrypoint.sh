#!/bin/bash

# Define colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# ASCII banner
BANNER="
 ${RED}_____ _ _  ___  ___                   ${NC}
${RED}|  __ (_) | |  \/  |                   ${NC}
${GREEN}| |  \/_| |_| .  . | ___  _____      __ ${NC}
${GREEN}| | __| | __| |\/| |/ _ \/ _ \ \ /\ / / ${NC}
${YELLOW}| |_\ \ | |_| |  | |  __/ (_) \ V  V /  ${NC}
 ${YELLOW}\____/_|\__\_|  |_/\___|\___/ \_/\_/   ${NC}
"
echo -e "$BANNER"
echo -e "${YELLOW}[+] Welcome challenger to the epic GIT Madness, can you read${NC} ${RED}/flag.txt?${NC}"

python3 challenge.py