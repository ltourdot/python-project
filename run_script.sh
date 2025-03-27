#!/bin/bash
echo "✅ Geany actually ran this!" > /tmp/test.txt
/usr/bin/xterm -hold -e "cat /tmp/test.txt"
