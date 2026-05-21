#!/usr/bin/env bash
if [ -z "$1" ]; then
    echo "[Error] Backup directory path is required."
    echo ""
    echo "Usage: ./02_restore.sh [backup_directory_path]"
    echo "Example: ./02_restore.sh \"$HOME/Library/Application Support/Antigravity IDE/migration_backups/20260520_094630\""
    echo ""
    exit 1
fi

echo "Restoring backup from: $1"
python3 -m src.main --restore "$1"
