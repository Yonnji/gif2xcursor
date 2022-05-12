Animated GIF to XCursor converter
=================================

Tool for converting animated GIF to XCursor files.

Works on square animated GIFs only.


Requirements
------------

* Python
* Pillow (will be autoinstalled)
* xcursorgen


Installation
------------

```
pip install .
```


Usage
-----

```
gif2xcursor image.gif <x> <y>
```

Where
* "image.gif" is a path to animated GIF file
* x - hotspot X position
* y - hotspot Y position

It will create a file name "image.xcursor".
You need to put this file into new cursor theme or 
replace a single cursor file in your current theme.

You can switch cursor themes using "GNOME Tweaks".
