

from CF.CONST_D import _00_VALS as CF_V
import argparse as AP
import sys
import _01_OPTIONS_KEYS as K


V = None


ARGV = sys.argv
ARGS = None
PARSER = None


# parser = argparse.ArgumentParser()
# command_group = parser.add_mutually_exclusive_group()
# command_group.add_argument('-run', help='run it', action='store_true')
# command_group.add_argument('-stop', help='stop it', action='store_true')


ARG_PARSER_TUP = (
    (K.K_PROG, None),
    (K.K_USAGE, None),
    (K.K_DESCRIPTION, None),
    (K.K_EPILOG, None),
    (K.K_PARENTS, []),
    (K.K_FORMATTER_CLASS, AP.HelpFormatter),
    (K.K_PREFIX_CHARS, "-"),
    (K.K_FROMFILE_PREFIX_CHARS, None),
    (K.K_ARGUMENT_DEFAULT, None),
    (K.K_CONFLICT_HANDLER, "error"),
    (K.K_ADD_HELP, True),
    (K.K_ALLOW_ABBREV, True),
    (K.K_EXIT_ON_ERROR, True),
)
def E_ARG_PARSER():
  return dict((x, y) for x, y in ARG_PARSER_TUP)


ADD_ARGS_TUP = (
    (K.K_OPTION_STRINGS, ""),  # "-b" or ["-b", "-bigOne"] dest= must be set if this is used
    (K.K_DEST, None),
    (K.K_NARGS, None),
    (K.K_CONST, None),
    (K.K_DEFAULT, None),
    (K.K_TYPE, None),
    (K.K_CHOICES, None),
    (K.K_REQUIRED, False),
    (K.K_HELP, None),
)
def E_ADD_ARGS():
  return dict((x, y) for x, y in ADD_ARGS_TUP)







#
