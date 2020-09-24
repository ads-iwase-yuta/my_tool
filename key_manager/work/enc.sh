#!/bin/bash
read -sp "type your secret text to save: " pass && \
echo "" && \
echo "$pass" > planetext && \
openssl aes-256-cbc -e -in planetext -out encrypted && \
shred -u planetext