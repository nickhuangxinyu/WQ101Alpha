#!/bin/bash

rsync -avz -r -e "sshpass -p wq101 ssh" wq101@101.132.173.17:~/merge.csv.gz .
