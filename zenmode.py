#!/usr/bin/env python3
import sys
import termios
import tty
import subprocess
import time
import os

def getch():
    """Detect ANY key including ESC"""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setcbreak(sys.stdin)
        ch = sys.stdin.read(1)
        if ch == '\x1b':  # ESC detected
            # Consume escape sequence but return ESC
            sys.stdin.read(2)  # Skip [A, [B, etc.
            return 'ESC'
        return ch if ch else ''
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

print("🔥 ZENMODE - ANY KEY (incl ESC) → LOCK & EXIT!")
print("Press Ctrl+C to stop")

try:
    while True:
        key = getch()
        if key:  # Any non-empty key
            print(f"\n🎯 Key '{key}' → LOCKING & EXITING!")
            
            xdo_path = os.path.expanduser("~/xdoo/Lockscreen/xdo")
            subprocess.run([xdo_path])
            
            print("🔒 Locked! EXITING...")
            sys.exit(0)
        
        time.sleep(0.01)  # Small poll delay
        
except KeyboardInterrupt:
    print("\nZenmode stopped.")
