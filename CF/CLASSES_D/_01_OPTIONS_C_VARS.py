

from sys import argv
import argparse as AP


OPTIONS = {
}


OPTIONS_HELP_DICT = {
}


OPTIONS_DICT = {
}


"""
class ArgumentParser(_AttributeHolder, _ActionsContainer)
      ArgumentParser(prog=None, usage=None, description=None, epilog=None, parents=[], formatter_class=&lt;class 'argparse.HelpFormatter'&gt;, prefix_chars='-', fromfile_prefix_chars=None, argument_default=None, conflict_handler='error', add_help=True, allow_abbrev=True, exit_on_error=True)

Object for parsing command line strings into Python objects.

Keyword Arguments:
    - prog -- The name of the program (default:
        ``os.path.basename(sys.argv[0])``)
    - usage -- A usage message (default: auto-generated from arguments)
    - description -- A description of what the program does
    - epilog -- Text following the argument descriptions
    - parents -- Parsers whose arguments should be copied into this one
    - formatter_class -- HelpFormatter class for printing help messages
    - prefix_chars -- Characters that prefix optional arguments
    - fromfile_prefix_chars -- Characters that prefix files containing
        additional arguments
    - argument_default -- The default value for all arguments
    - conflict_handler -- String indicating how to handle conflicts
    - add_help -- Add a -h/-help option
    - allow_abbrev -- Allow long options to be abbreviated unambiguously
    - exit_on_error -- Determines whether or not ArgumentParser exits with
        error info when an error occurs
"""
