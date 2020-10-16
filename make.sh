#!/bin/bash
# My first script
dir=$1
echo "[*] start making fils"
if [ ! -d /Users/mbpro/Desktop/hackerank/$dir ]; then
  mkdir -p /Users/mbpro/Desktop/hackerank/$dir;
  echo >/Users/mbpro/Desktop/hackerank/$dir/input.txt
  echo >/Users/mbpro/Desktop/hackerank/$dir/output.txt
  echo "sys.stdin = open('input.txt', 'r')
        sys.stdout = open('output.txt', 'w')" >/Users/mbpro/Desktop/hackerank/$dir/run.py
  echo "[*] done with success"
fi
