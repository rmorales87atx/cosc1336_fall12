# WARNING: Do not attempt to edit this file if Unicode characters
#          aren't working correctly in your text editor.
"""
╔════════════════════════════════════════════════════════════════════════╗
║ Copyright © 2012, Robert James Morales                                 ║
║ All rights reserved.                                                   ║
║                                                                        ║
║ Redistribution and use in source and binary forms, with or without     ║
║ modification, are permitted provided that the following conditions     ║
║ are met:                                                               ║
║                                                                        ║
║    1. Redistributions of source code must retain the above copyright   ║
║       notice, this list of conditions and the following disclaimer.    ║
║                                                                        ║
║    2. Redistributions in binary form must reproduce the above          ║
║       copyright notice, this list of conditions and the following      ║
║       disclaimer in the documentation and/or other materials provided  ║
║       with the distribution.                                           ║
║                                                                        ║
║    3. Neither the name of the copyright holder nor the names of its    ║
║       contributors may be used to endorse or promote products derived  ║
║       from this software without specific prior written permission.    ║
║                                                                        ║
║ THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS    ║
║ "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT      ║
║ LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR  ║
║ A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL COPYRIGHT       ║
║ HOLDERS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,       ║
║ EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,    ║
║ PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR     ║
║ PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY    ║
║ OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT           ║
║ (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE  ║
║ OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.   ║
╚════════════════════════════════════════════════════════════════════════╝
"""

from sys import stdout

def print_table(items, options = {}):
    """
    Prints a table using Unicode box-drawing characters.

    For detailed usage instructions see the documentation
    online @ http://squailboont.info/py/table_printer.pdf
    """

    if len(items) == 0:
        return

    def get_option(name, default):
        """
        Internal function used to access the 'options' dictionary.
        Returns the option's value if it is in the dictionary;
        otherwise the default value is returned.
        """
        value = options.get(name)
        return value if value != None else default

    # Read and validate all options from the table,
    # if there were any specified

    no_header = get_option("no_header", default=False)
    no_divider = get_option("no_divider", default=False)
    uniform_col_width = get_option("uniform_col_width", default=False)
    right_align_numbers = get_option("right_align_numbers", default=False)
    default_align = get_option("default_align", default='<')
    col_align = get_option("col_align", default={})
    row_align = get_option("row_align", default={})
    cell_align = get_option("cell_align", default={})

    if default_align not in ('<', '^', '>'):
        raise ValueError("default_align must be one of: '<', '^', '>'")

    # if the 'items' table is actually a dictionary, convert it to
    # the form expected

    if type(items) is dict:
        temp = []
        for key, value in items.items():
            temp += [(str(key), str(value))]
        items = temp
        no_header = True

    # determine lengths of all the items,
    # and the number of columns per row

    num_rows = len(items)
    num_columns = 0
    max_width = 0
    col_width = {}

    for rx, row in enumerate(items):
        cx = 0
        for cx, col in enumerate(row):
            width = len(str(col))
            cur_width = col_width.get(cx) or 0
            max_width = max(width, max_width)

            if not uniform_col_width:
                col_width[cx] = max(cur_width, width)

        num_columns = max(num_columns, cx+1)

    if uniform_col_width:
        col_width = [max_width] * num_columns

    # function used to print table and row borders
    def print_border(rx):
        """ internal function """

        left = ''
        right = ''
        filler = ''
        intersect = ''

        if rx == "top":
            left,filler,intersect,right = ('╔', '═', '╦', '╗')
        elif rx == "bottom":
            left,filler,intersect,right = ('╚', '═', '╩', '╝')
        elif (not no_header) and rx == 0:
            left,filler,intersect,right = ('╠', '═', '╬', '╣')
        else:
            left,filler,intersect,right = ('╟', '─', '╫', '╢')

        space = ""
        for ix in range(num_columns):
            space += filler * (col_width[ix] + 2)
            if (ix + 1) < num_columns:
                space += intersect

        print(left + space + right)

    # print the table's top border

    print_border("top")

    # iterate through the items and print each row
    #
    # -- TODO --
    # someday i'd like to be able to handle the case of a row
    # not having values for every column...

    for rx, row in enumerate(items):
        for cx, col in enumerate(row):
            cell = (rx+1, cx+1)
            width = col_width[cx]
            align = cell_align.get(cell) or \
                    row_align.get(rx+1) or \
                    col_align.get(cx+1)

            if align not in ('<', '>', '^'):
                align = default_align

            print('║', format(col, align+str(width)), '', end="")

        print('║')

        # print a row divider if we're not at the last row
        if (not no_divider) and (rx + 1) < num_rows:
            print_border(rx)

    # we're done, print the table's bottom border

    print_border("bottom")

if __name__ == "__main__":
    from random import random
    test = [ ("key", "value"), ('', "dfgdfgdfgdfgfsg"), ("two", random()), ("three", "sdfdfgrghedfgwe47rywherfuwe8rfurft") ]
    opts = {
        'default_align': '<',
        'cell_align': {(1,1): '^', (1,2): '^'}
    }
    print_table(test, opts)
