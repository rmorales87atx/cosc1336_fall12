"""
Some utility functions for console I/O.
Complete documentation for this module is available online:
http://squailboont.info/py/io_util.pdf

Copyright © 2012, Robert James Morales
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:

   1. Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.

   2. Redistributions in binary form must reproduce the above
      copyright notice, this list of conditions and the following
      disclaimer in the documentation and/or other materials provided
      with the distribution.

   3. Neither the name of the copyright holder nor the names of its
      contributors may be used to endorse or promote products derived
      from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL COPYRIGHT
HOLDERS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

from sys import stdout
from warnings import warn

def get_bool(prompt, true_values = ('y', 'yes', '1'), \
             false_values = ('n', 'no', '0')):
    """
    Receives input from the user and converts to a True/False value
    based on the values provided in 'true_values' and 'false_values'.
    """

    # validate that both true & false sets are unique from each other
    # by intersecting them; the intersection should return an empty set
    t_f_matches = set(true_values) & set(false_values)
    if len(t_f_matches) == 0:
        raise ValueError("`true_values` and `false_values` contain similar elements: " + str(t_f_matches))

    try:
        result = None

        while (result is None) or (result not in true_values) or \
              (result not in false_values):
            # convert input to lower case, since Python has no
            # equivalent to stricmp()
            result = input(prompt).lower()

            if result in true_values:
                return True
            elif result in false_values:
                return False
    except (EOFError, KeyboardInterrupt, ValueError):
        return None

def get_number(as_type, prompt, limit = None):
    """
    Receives input from the user and returns a numeric type if successful.
    """

    if as_type not in (int, float):
        raise ValueError("`as_type` must be int or float")

    # limit must either be None or a tuple type
    if limit is not None and type(limit) is not tuple:
        raise TypeError("`limit` must be a tuple")

    # if limit is a tuple, the following must be validated:
    # - contans only 2 values (len == 2)
    # - first value is greater than the second value; in this case
    #   we can simply swap the values and move on
    if type(limit) is tuple:
        if len(limit) != 2:
            raise ValueError("`limit` must be a tuple with two numeric values")

        begin, end = limit

        if type(begin) not in (int, float):
            raise ValueError("`limit` contains non-numeric value {0} in position 0".format(str(type(begin))))
        if type(end) not in (int, float):
            raise ValueError("`limit` contains non-numeric value {0} in position 1".format(str(type(end))))        

        if end <= begin:
            warn("range corrected to {1} <= x < {0}; received: {0} <= x < {1}".format(begin, end))
            begin,end = end,begin

    # validation of `limit` is complete

    try:
        if limit is not None:
            # input validation
            value = None

            while (value is None) or (not begin <= value < end):
                try:
                    value = as_type(input(prompt))
                except ValueError:
                    value = None # allow loop to continue
                except (EOFError, KeyboardInterrupt):
                    return None # exit due to interrupt

            return value
        else:
            # no validation, just convert input
            return as_type(input(prompt))
    except (EOFError, KeyboardInterrupt, ValueError):
        return None

def get_int(prompt, limit = None):
    """
    Alias for get_number(int, prompt, limit)
    """

    return get_number(int, prompt, limit)

def get_float(prompt, limit = None):
    """
    Alias for get_number(float, prompt, limit)
    """

    return get_number(float, prompt, limit)

def get_str(prompt, values=None):
    """
    Receives input from the user and returns it as-is.
    """

    try:
        if values is not None:
            result = None

            while (result is None) or (result not in values):
                result = input(prompt)

            return result
        else:
            return input(prompt)
    except (EOFError, KeyboardInterrupt):
        return None

def get_file_lines(filename, encoding=None):
    """
    This generator function opens the specified text file and removes
    the newline characters from each line of the file.
    """

    with open(filename, 'r', encoding=encoding) as file:
        for line in file:
            yield line.rstrip()
