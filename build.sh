#!/bin/bash
set -e
clear
rm -rf build
mkdir -p build
echo "==========Building=========="
javac src/Main.java -d build
echo "==========Running==========="
cd build && java Main
echo "==========Done=============="
