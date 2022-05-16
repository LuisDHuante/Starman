#!/bin/bash

if pgrep -x "python3" > /dev/null
then
    echo "Running"
else
    python3 ~/Starman/00_Crawler/crawl.py &
    disown
    echo "Stopped"
fi
