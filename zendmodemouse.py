#!/usr/bin/env python3
import sys, termios, tty, subprocess, time, os

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setcbreak(sys.stdin)
        ch = sys.stdin.read(1)
        if ch == '\x1b':
            sys.stdin.read(2)
            return 'ESC'
        return ch if ch else ''
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

print("🔥 ZENMODE - Keys OR Click → LOCK & EXIT!")
print("Ctrl+C to stop")

try:
    while True:
        key = getch()
        if key:
            print(f"\n🎯 KEY '{key}' → LOCKING!")
            break
        
        try:
            result = subprocess.run(['~/xdoo/Lockscreen/clickdetect'], capture_output=True, timeout=0.1)
            if result.returncode == 0:
                print("\n🎯 CLICK → LOCKING!")
                break
        except: pass
        
        time.sleep(0.05)
except KeyboardInterrupt:
    print("\nZenmode stopped.")

xdo_path = os.path.expanduser("~/xdoo/Lockscreen/xdo")
subprocess.run([xdo_path])
print("🔒 Locked & EXITING!")
sys.exit(0)
