#!/usr/bin/env python3

# Copyright (c) 2022 Yonnji Nyyoka.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import os
import subprocess
import sys

from PIL import Image, GifImagePlugin


def main():
    if len(sys.argv) < 4:
        print('Usage: {} <image.gif> <x> <y>'.format(sys.argv[0]))
        return

    image = Image.open(sys.argv[1])
    basepath = sys.argv[1].replace('.gif', '')

    if not image.is_animated:
        print('Animated GIF is required')
        return

    if image.width != image.height:
        print('Square image is required')
        return

    assets = []
    xfilepath = '{}.xcursorgen'.format(basepath)
    assets.append(xfilepath)
    with open(xfilepath, 'w') as f:
        for frame in range(0, image.n_frames):
            image.seek(frame)

            ifilepath = '{}_{}.png'.format(basepath, frame)
            assets.append(ifilepath)
            image.save(ifilepath)

            f.write('{width} {x} {y} {filepath} {duration}\n'.format(**{
                'width': image.width,
                'x': sys.argv[2],
                'y': sys.argv[3],
                'duration': image.info['duration'],
                'filepath': ifilepath,
            }))

    subprocess.run(['xcursorgen', xfilepath, '{}.xcursor'.format(basepath)])

    for filepath in assets:
        os.remove(filepath)


if __name__ == '__main__':
    main()
