

from CF.SUBM_D import (
    _00_VALS_IN as CF_V,
    _01_OPTIONS_KEYS as OPTIONS_KEYS,
)
import argparse as AP
import sys


V = None
locals().update(OPTIONS_KEYS.ALL_THE_OPTION_KEYS)
locals().update(CF_V.ALL_THE_VALS)


ARGV = sys.argv
ARGS = None
PARSER = None


# parser = argparse.ArgumentParser()
# command_group = parser.add_mutually_exclusive_group()
# command_group.add_argument('-run', help='run it', action='store_true')
# command_group.add_argument('-stop', help='stop it', action='store_true')


ARG_PARSER_TUP = (
    (K_PROG, None),
    (K_USAGE, None),
    (K_DESCRIPTION, None),
    (K_EPILOG, None),
    (K_PARENTS, []),
    (K_FORMATTER_CLASS, AP.HelpFormatter),
    (K_PREFIX_CHARS, "-"),
    (K_FROMFILE_PREFIX_CHARS, None),
    (K_ARGUMENT_DEFAULT, None),
    (K_CONFLICT_HANDLER, "error"),
    (K_ADD_HELP, True),
    (K_ALLOW_ABBREV, True),
    (K_EXIT_ON_ERROR, True),
)
def E_ARG_PARSER():
  return dict((x, y) for x, y in ARG_PARSER_TUP)


ADD_ARGS_TUP = (
    (K_OPTION_STRINGS, ""),  # "-b" or ["-b", "-bigOne"] dest= must be set if this is used
    (K_DEST, None),
    (K_NARGS, None),
    (K_CONST, None),
    (K_DEFAULT, None),
    (K_TYPE, None),
    (K_CHOICES, None),
    (K_REQUIRED, False),
    (K_HELP, None),
)
def E_ADD_ARGS():
  return dict((x, y) for x, y in ADD_ARGS_TUP)


ALL_THE_KEYS = {}
ALL_THE_KEYS.update(OPTIONS_KEYS.ALL_THE_OPTION_KEYS)


ALL_THE_OPTIONS_DATA = {
    "ARGV": ARGV,
    "ARGS": ARGS,
    "PARSER": PARSER,
    "E_ARG_PARSER": E_ARG_PARSER,
    "E_ADD_ARGS": E_ADD_ARGS,
}
ALL_THE_OPTIONS_DATA.update(OPTIONS_KEYS.ALL_THE_OPTION_KEYS)






#
