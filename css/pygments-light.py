#
#   This file is part of m.css.
#
#   Copyright © 2017, 2018, 2019 Vladimír Vondruš <mosra@centrum.cz>
#
#   Permission is hereby granted, free of charge, to any person obtaining a
#   copy of this software and associated documentation files (the "Software"),
#   to deal in the Software without restriction, including without limitation
#   the rights to use, copy, modify, merge, publish, distribute, sublicense,
#   and/or sell copies of the Software, and to permit persons to whom the
#   Software is furnished to do so, subject to the following conditions:
#
#   The above copyright notice and this permission notice shall be included
#   in all copies or substantial portions of the Software.
#
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
#   THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#   FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#   DEALINGS IN THE SOFTWARE.
#

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
    Literal, Number, Operator, Other, Punctuation, Text, Generic, \
    Whitespace

class LightStyle(Style):
    background_color = None
    highlight_color = '#e0dbcb'
    default_style = ""

    styles = {
        # C++
        Comment:                '#258d85',
        Comment.Preproc:        '#ce5c00',
        Comment.PreprocFile:    '#00b200',
        Keyword:                'bold #9a9a00',
        Name:                   '#031227',
        String:                 '#00b200',
        String.Char:            '#00b200',
        Number:                 '#4fa7ff',
        Operator:               '#a7a797',
        Punctuation:            "#a7a797",

        # CMake
        Name.Builtin:           'bold #000000',
        Name.Variable:          '#4fa7ff',

        # reST, HTML
        Name.Tag:               'bold #333333',
        Name.Attribute:         'bold #333333',
        Name.Class:             'bold #333333',
        Operator.Word:          'bold #333333',
        Generic.Heading:        'bold #000000',
        Generic.Emph:           'italic #414141',
        Generic.Strong:         'bold #414141',

        # Diffs
        Generic.Subheading:     '#afd7e7',
        Generic.Inserted:       '#afffaf',
        Generic.Deleted:        '#ffafaf'
    }
