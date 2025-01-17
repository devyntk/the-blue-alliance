#! /bin/bash

# This is a simple wrapper around invoking a user script via ipython
# Invoke like: ./ops/shell/run_user_script.sh print_event.py -- 2019wat
# Pass arguments to the script after a `--` to signal what gets passed

SCRIPT="$1"

# Shift past this script's args and the --
shift # script name
shift # the --

ipython --config ops/shell/ipython_config.py \
    --TerminalIPythonApp.display_banner=False \
    "ops/shell/user_scripts/$SCRIPT" "$@"
