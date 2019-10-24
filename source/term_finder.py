"""
Date: 2019-10-24
Author: Richard A
finds & returns a list of objects
"""
import os

term_to_find = None
_root_directory = __file__.split("dingometer\\")[-1]
_files_to_search = set()

_strip_mode_map = {
    "both": _strip_mode_both,
    "include": _strip_mode_include,
    "exclude": _strip_mode_exclude
}


class _line:
    def __init__(self, path_str, line_number, line_string):
        self.__dict__.update(locals())


def _strip_mode_both(string_to_check, inclusions, exclusions):
    if *exclusions not in string_to_check:
        if *inclusions in string_to_check:
            return True
    else:
        return False


def _strip_mode_include(string_to_check, inclusions, exclusions):
    if *inclusions in string_to_check:
        return True
    else:
        return False


def _strip_mode_exclude(string_to_check, inclusions, exclusions):
    if *exclusions not in string_to_check:
        return True
    else:
        return False


def _get_valid_strip_mode(mode_field):
    if type(mode_field) == str and mode_field in _strip_mode_map:
        return mode_map[mode_field]
    elif type(mode_field) == __func__:
        # test function to make sure the format is correct-ish
        mode_field("arb_string", [], [])
        return mode_field
    else:
        raise TypeError("mode field not valid, specify in-build or pass\
                         function")


def _strip_irrelevant_string(
        input_list, inclusions=[], exclusions=[], mode="both"
):
    """
    takes a list of strings and removes entries as specified by inclusions,
    exclusions and mode.

    built-in modes:
    "both", "include", "exclude"

    "both" requires the string to have the inclusions and not have the
    exclustions

    "include" will include all the strings that contain any inclusions,
    regardless of exclusion presence

    "exclude" will exclude all that contain exclusions, but include
    everthing else.

    mode functions can be passed. mode functions requires the following args:
    string_to_check: str, inclusions: list, exclusions: list

    must return True if the string is to be kept, and false if not.
    """
    check_function = _get_valid_strip_mode(mode)

    output_list = []
    for file_name in input_list:
        if *exclusions not in file_name:
            if *inclusions in file_name:
                output_list.append()


def find_term_in_dir(term, root_directory):
    for current_path,\
            current_path_dirs,\
            current_path_files in os.walk(root_directory):
        pass
