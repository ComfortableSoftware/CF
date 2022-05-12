

from CF.CONST_D import _00_VALS as CF_V
import argparse as AP
import sys


V = None
# ARGV = argv
ARGS = None
PARSER = None




ARG_PARSER_TUP = (
    ("prog", None),
    ("usage", None),
    ("description", None),
    ("epilog", None),
    ("parents", []),
    ("formatter_class", AP.HelpFormatter),
    ("prefix_chars", "-"),
    ("fromfile_prefix_chars", None),
    ("argument_default", None),
    ("conflict_handler", "error"),
    ("add_help", True),
    ("allow_abbrev", True),
    ("exit_on_error", True),
)
def E_ARG_PARSER():
  return dict((x, y) for x, y in ARG_PARSER_TUP)


ADD_ARGS_TUP = (
    ("option_strings", ""),  # "-b" or ["-b", "-bigOne"] dest= must be set if this is used
    ("dest", None),
    ("nargs", None),
    ("const", None),
    ("default", None),
    ("type", None),
    ("choices", None),
    ("required", False),
    ("help", None),
    ("metavar", None),
)
def E_ADD_ARGS():
  return dict((x, y) for x, y in ADD_ARGS_TUP)







#
