#!/bin/bash

# GET ALL MOUNTABLE DRIVES AND SAVE TO FILE
sudo blkid | sudo grep -l /dev/sd* > available_drives.md 

# GET FILE WITH LIST OF AVAILABLE DRIVES
DRIVE_FILE="./available_drives.md"
# CREATE LIST OF DRIVES
DRIVE_LIST=$(cat $DRIVE_FILE)

if [ ! -f ./mnt ]
then
    sudo mkdir ./mnt
fi

for DRIVE in $DRIVE_LIST
do
sudo mount -o ro $DRIVE ./mnt
done
