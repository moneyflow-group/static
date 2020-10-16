#!/bin/bash

echo "[+] Running MJML server..."
docker run --rm -p 80:80 --name "mjml-server" -d alokinplc/mjmlserver

echo "[+] Processing MJML files, with .xml file extension..."
FILES=$(find . -name "*.mjml")
for file in $FILES; do
    INPUT=$file
    OUTPUT=$(echo $INPUT | sed s/mjml/html/)
    http localhost <$INPUT >$OUTPUT
done

echo "[+] Stopping MJML server..."
docker stop "mjml-server"
