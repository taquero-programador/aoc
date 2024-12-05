#!/bin/bash

cat input.txt | grep -Eio 'mul\([[:digit:]]{1,3}\,[[:digit:]]{1,3}\)' | grep -Eio '[[:digit:]]{1,3}\,[[:digit:]]{1,3}' > output.txt

python 03.py
