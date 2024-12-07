#!/bin/bash

grep -Eio 'mul\([[:digit:]]{1,3}\,[[:digit:]]{1,3}\)' input.txt | grep -Eio '[[:digit:]]{1,3}\,[[:digit:]]{1,3}' > output.txt

python 03.py
