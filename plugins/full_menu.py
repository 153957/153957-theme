# encoding: utf-8

# Copyright 2017 - Arne de Laat - 153957

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

""" Add full menu to gallery
"""

import os
import operator
from collections import OrderedDict

from sigal import signals


def full_tree(gallery):
    """full menu tree"""

    sorted_tree = sorted(gallery.albums.items(), key=operator.itemgetter(0))
    print(sorted_tree)

    gallery.full_tree = OrderedDict()

    for name, album in sorted_tree:
        if name == '.':
            continue
        ancestors = album.path.split('/')[:-1]
        print(ancestors)
        current_ancestor = gallery.full_tree
        for ancestor in ancestors:
            current_ancestor = current_ancestor[ancestor]['subalbums']
        current_ancestor[album.name] = {
            'self': album,
            'subalbums': OrderedDict()
        }


def path_to_root(album):
    """url path back to gallery root"""

    path_to_root = os.path.relpath('.', album.path)
    if path_to_root == '.':
        path_to_root = ''
    else:
        path_to_root += '/'

    album.path_to_root = path_to_root


def path_from_root(album):
    """url from gallery root"""

    album.path_from_root = album.path


def register(settings):
    signals.gallery_initialized.connect(full_tree)
    signals.album_initialized.connect(path_to_root)
    signals.album_initialized.connect(path_from_root)
