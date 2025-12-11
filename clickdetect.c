// clickdetect.c - Detects ANY mouse click
#include <X11/Xlib.h>
#include <X11/Xutil.h>
#include <stdio.h>
#include <unistd.h>

int main() {
    Display *d = XOpenDisplay(NULL);
    if (!d) return 1;
    
    Window root = DefaultRootWindow(d);
    XGrabButton(d, AnyButton, AnyModifier, root, True, 
                ButtonPressMask, GrabModeAsync, GrabModeAsync, None, None);
    
    XEvent ev;
    XNextEvent(d, &ev);
    
    if (ev.type == ButtonPress) {
        printf("CLICK DETECTED\n");
        XCloseDisplay(d);
        return 0;
    }
    XCloseDisplay(d);
    return 1;
}
