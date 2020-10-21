#!/bin/bash

# Create email fixture json from MJML files.
#
# This script will start a local mjml-server as a docker instance that accept MJML files and outputs HTML files.
# Aftwards it will traverse the directories and find HTML files which will be used to generate a new default_email_templates.json
#
# This is all slightly convuluted, but it beats doing it manually.
#

echo "[+] Running MJML server..."
docker run --rm -p 80:80 --name "mjml-server" -d alokinplc/mjmlserver

# Wait for MJML server to boot
sleep 2

echo "[+] Compiling MJML to HTML..."
FILES=$(find . -name "*.mjml")
for file in $FILES; do
    INPUT=$file
    OUTPUT=$(echo $INPUT | sed s/mjml/html/)
    # echo "   $INPUT --> $OUTPUT"
    http localhost <$INPUT >$OUTPUT
done

echo "[+] Stopping MJML server..."
docker stop "mjml-server"

echo "[+] Done!"