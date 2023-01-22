#!/bin/bash
set -e
clear
cd src && python3 -m interpreter "$@"