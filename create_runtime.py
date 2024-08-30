#!/usr/bin/env python3

import os
from pathlib import Path

def create_runtime_symlink():
    home_dir = Path.home()
    helix_dir = home_dir / '.helix'
    runtime_dir = helix_dir / 'runtime'
    config_dir = home_dir / '.config' / 'helix'
    config_runtime_dir = config_dir / 'runtime'

    if not runtime_dir.exists():
        print(f"[ERR] '{runtime_dir}' does not exist.")
        return
    if not config_dir.exists():
        try:
            config_dir.mkdir(parents=True, exist_ok=True)
        except OSError as e:
            print(f"[ERR] Failed to create directory '{config_dir}': {e}")
            return

    try:
        os.chdir(home_dir)
        
        config_runtime_dir.symlink_to(runtime_dir.resolve(), target_is_directory=True)
        
        print(f"[status] Created runtime symlink at '{config_runtime_dir}'")
    except OSError as e:
        print(f"[error] Failed to create symlink: {e}")

if __name__ == "__main__":
    create_runtime_symlink()
