#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
echo "alias mem=\"python $DIR/mymem.py\"" >> ~/.bashrc
echo "memfile=$DIR/gsobol.mem" > ~/.config/mymem.config
