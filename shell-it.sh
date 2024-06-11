#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

showHelp() {
    echo -e "${GREEN}Usage: $0 [DIRECTORY]${NC}"
    echo
    echo "Lists .sh scripts in the specified DIRECTORY (or the current directory if none is specified)"
    echo "and allows the user to select and run one of the scripts."
    echo
    echo "Options:"
    echo "  --help    Show this help message and exit"
}

if [[ "$1" == "--help" ]]; then
    showHelp
    exit 0
fi

# Defaults to pwd if no path is provided.
if [ -z "$1" ]; then
    target_dir=$(pwd)
else
    target_dir="$1"
fi

files_array=()
counter=1

# Make key-value array for each .sh file.
for file in "$target_dir"/*.sh; do
    if [ -e "$file" ]; then
        # .sh-it ignores itself.
        if [ "$(basename "$file")" != "sh-it.sh" ]; then
            files_array+=("$(basename "$file")")
            counter=$((counter + 1))
        fi
    fi
done

if [ ${#files_array[@]} -eq 0 ]; then
    echo -e "${RED}No .sh files found in ${target_dir}.${NC}"
else
    echo -e "${GREEN}Listing scripts in ${target_dir}:${NC}";
    for i in "${!files_array[@]}"; do
        echo "$((i + 1)): ${files_array[$i]}"
    done

    while true; do
        read -p "Enter number from 1 to ${#files_array[@]}: " usr_select
        if [[ "$usr_select" =~ ^[0-9]+$ ]] && [ "$usr_select" -ge 1 ] && [ "$usr_select" -le ${#files_array[@]} ]; then
            script_to_run="${files_array[$((usr_select - 1))]}"
            echo -e "${GREEN}Running script: $(basename "$script_to_run")${NC}"
            bash "$script_to_run"
            break
        else
            echo -e "${RED}Invalid input, enter value from 1 to ${#files_array[@]}.${NC}"
        fi
    done
fi
