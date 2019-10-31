"""
Date: 2019-10-24
Author: Richard A
finds & returns a list of objects
"""
import os
from strings import filter_strings


# classes --------------------------------------------------------------------
class file_details:
    def __init__(self, file_path: str, lines_in_file: int, term_objs_in_file: list):
        self.__dict__.update(locals())
        self.terms_in_file = len(term_objs_in_file)
        self.score = self._get_file_score()

    def _get_file_score(self):
        return self.lines_in_file/self.terms_in_file

    def __repr__(self):
        out_string = f"File: {self.file_path}\tscore: {self.score}\n"
        for task in self.term_objs_in_file:
            sub_string = "--------\n"+repr(task)+"\n"
            out_string += sub_string
        return out_string



class term_obj:
    def __init__(self, path_str, line_number, line_string):
        # the "local" namespace is just the variables passed to the __init__
        # function, and the "__dict__"
        self.__dict__.update(locals())


    def __repr__(self):
        return f"line contents:\n\tPath:\t{self.path_str}\
\n\tLnNo:\t{self.line_number}\n\tLine:\t{self.line_string}"


# functions ------------------------------------------------------------------


def get_file_paths_to_check(root_directory, inclusions, exclusions):
    """
    when passed a root directory get all the files of a desired type
    """
    file_set = set()
    for current_path,\
            current_path_dirs,\
            current_path_files in os.walk(root_directory):

        # all of the module creating, sub-module adding, etc was just for
        # this one line:
        addable_files = filter_strings(
            current_path_files, inclusions, exclusions
        )

        for file in addable_files:
            file_set.add(os.path.join(current_path, file))
    return file_set


def _assess_file_from_lines(term, lines_list, file_name):
    term_obj_list = []
    for index, line in enumerate(lines_list):
        if term in line:
            new_term_obj = term_obj(file_name, index+1, line)
            term_obj_list.append(new_term_obj)
    return term_obj_list


def assess_paths(term, path_list, local_returns=None):
    # complete_terms_list = []
    file_details_list = []
    file_score_dict = {}
    for path in path_list:
        with open(path) as fp:
            text = fp.read()
            if "\n" in text:
                lines = text.splitlines()
            else:
                continue
        term_obj_list = _assess_file_from_lines(term, lines, path)
        if len(term_obj_list) > 0:
            new_file_details = file_details(path, len(lines), term_obj_list)
            file_details_list.append(new_file_details)
    return file_details_list
