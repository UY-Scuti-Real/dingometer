#!/usr/bin/env python3
"""
Author: Richard A 
Date: 2019-10-07

Usage:
Run this module, first positional argument is the path to be searched. If no
argument is present, the script will assume the current directory is the
root directory of the package.

This package goes through the source directory file by file and finds all
the "DING"s,  and produces a file containing:

1) The relative path of the file it is in
2) The line it is on
3) the contents of that line


"""
import os
import sys
import term_finder



# returns current working directory as str
def _get_current_working_directory():
    """
    returns the current working directory

    This is a 1 line function, but it exists incase 
    I have to mess around with it later. 
    """
    return os.getcwd()

DIRECTORY = _get_current_working_directory()
FILE_EXTENSIONS = [".py", ".c", ".h"]

# returns the directory passed to the program
def _get_passed_directory():
    """
    should only be called if len(sys.argv) > 1.  
    """
    return sys.argv[1]


# sets global directory, extensions from sys args
def _set_dir_exts_from_args():
    """
    updates the global variables. Of course, globals are undesirable but given
    these variables are used everywhere, they should remain in the global name
    space.
    """
    global DIRECTORY, FILE_EXTENSIONS
    # Richard's patented method for python case statements
    # search_directory = argv_len_switcher[argv_len_case]()
    argv_len = len(sys.argv)
    if (argv_len > 1):
        DIRECTORY = _get_passed_directory()
    if (argv_len > 2):
        _extensions = []
        for file_extension_arg in sys.argv[2:]:
            _extensions.append(file_extension_arg)
        FILE_EXTENSIONS = _extensions


def main():
    """
    Main function of the package is used to do the thing
    """
    term = "DING"
    # print(DIRECTORY)
    paths = term_finder.get_file_paths_to_check(DIRECTORY, FILE_EXTENSIONS, [])
    # print(paths)
    file_details_list = term_finder.assess_paths(term, paths)
    print(file_details_list)


if __name__ == "__main__":
    _set_dir_exts_from_args()
    main()
