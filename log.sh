#!/bin/bash

LOG_DIR="/var/log"

echo "Listing .log files in $LOG_DIR:"
ls -1 "$LOG_DIR"/*.log 2>/dev/null

COUNT=$(ls -1 "$LOG_DIR"/*.log 2>/dev/null | wc -l)

echo "Total .log files found: $COUNT"
