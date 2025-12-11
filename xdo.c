// xdo.c - Your custom Ctrl+Alt+L sender (no sudo needed)
#include <X11/Xlib.h>
#include <X11/XKBlib.h>  // <-- ADD THIS
#include <X11/extensions/XTest.h>
#include <unistd.h>

int main() {
    Display *d = XOpenDisplay(NULL);
    if (!d) return 1;
    
    KeyCode ctrl = XKeysymToKeycode(d, XStringToKeysym("Control_L"));
    KeyCode alt = XKeysymToKeycode(d, XStringToKeysym("Alt_L"));
    KeyCode lkey = XKeysymToKeycode(d, XStringToKeysym("l"));
    
    // Press Ctrl+Alt+L
    XTestFakeKeyEvent(d, ctrl, True, 0);
    XTestFakeKeyEvent(d, alt, True, 0);
    XTestFakeKeyEvent(d, lkey, True, 0);
    usleep(50000);  // 50ms
    // Release
    XTestFakeKeyEvent(d, lkey, False, 0);
    XTestFakeKeyEvent(d, alt, False, 0);
    XTestFakeKeyEvent(d, ctrl, False, 0);
    
    XCloseDisplay(d);
    return 0;
}

