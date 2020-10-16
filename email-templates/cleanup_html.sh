#!/bin/bash

echo "[+] Deleting HTML files recursively..."
find . -name "*.html" -exec rm {} \;