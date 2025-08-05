#!/bin/bash

source="/home/kali/Documents/origen"
dest="/home/kali/Documents/backup"

date=$(date +"%Y-%m-%d_%H-%M-%S")
backup_name="backup_$date.tar.gz"

tar -czf "$dest/$backup_name" "$source"

echo "backup realizado: $backup_name"
