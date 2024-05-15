#!/usr/bin/bash

cd ../../helix
ln -Ts $PWD/runtime ~/.config/helix/runtime
cd ~
echo "created runtime at ~/.config/helix/runtime"
