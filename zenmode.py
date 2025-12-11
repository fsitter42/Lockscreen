#!/usr/bin/env python3
import sys
import termios
import tty
import subprocess
import time
import os

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setcbreak(sys.stdin)
        ch = sys.stdin.read(1)[0]
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

print("🔥 ZENMODE FULLY AUTOMATIC - Python + xdo!")
print("Press Ctrl+C to stop")

try:
    while True:
        key = getch()
        print(f"\n🎯 Key '{key}' → Calling xdo...")
        
        # FIXED: Full path + os.path.expanduser
        xdo_path = os.path.expanduser("~/xdoo/Lockscreen/xdo")
        subprocess.run([xdo_path])
        
        print("🔒 Locked! Ready...")
        time.sleep(0.1)
        
except KeyboardInterrupt:
    print("\nZenmode stopped.")

