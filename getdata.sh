#!/bin/bash

rsync -avz -r -e "sshpass -p wq101 ssh" wq101@139.196.204.22:~/merge.csv.gz .
