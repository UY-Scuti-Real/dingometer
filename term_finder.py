"""
Date: 2019-10-24
Author: Richard A
finds & returns a list of objects
"""
import os

term_to_find = None
inclusions = []
exclusions = []
_root_directory = __file__.split("dingometer\\")[-1]


class _line:
    def __init__(self, path_str, line_number, line_string):
        self.__dict__.update(locals())




def get_file_paths_to_check(root_directory):
    file_set = set()
    for current_path,\
            current_path_dirs,\
            current_path_files in os.walk(root_directory):

        addable_files = _remove_irrelevant_strings(
            current_path_files, inclusions, exclusions
        )

        for file in addable_files:
            file_set.add(os.join(current_path, addable_files))


def find_term_in_dir(term, root_directory):
    pass

print(get_file_paths_to_check(_root_directory))
