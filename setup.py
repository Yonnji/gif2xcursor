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

from setuptools import setup


setup(
    name='gif2xcursor',
    version='0.0.1',
    description='Animated GIF to XCursor file converter',
    long_description='Converts animated GIF to XCursor files',
    url='https://kitsune.one/',
    download_url='https://kitsune.one/',
    author='Yonnji',
    license='GPL3',
    packages=(
        'gif2xcursor',
    ),
    entry_points={
        'console_scripts': (
            'gif2xcursor=gif2xcursor.gif2xcursor:main',
        ),
    },
    install_requires=(
        'Pillow >= 9.1.0',
    )
)
