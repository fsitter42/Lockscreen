*fsitter42*

**INSTRUCTIONS**

if the Makefile doesnt work use:

	gcc -o xdo xdo.c -lX11 -lXtst -lXext

to compile the xdo substitude.

then run the python script with:

	python3 zenmode.py

additionally fill your screen with black via this bash alias:

	zenmode() {
		flatpak run app.zen_browser.zen https://www.whitescreen.online/black-screen/ &
	}

Dont forget to set start screensafer to never and update the path in zenmode.py
