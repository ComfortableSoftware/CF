

import inspect as INS
from inspect import (
    isfunction,
#    ismethod,
    ismodule,
)
import typing as TYPING
from typing import types as TTYPES


from CF.SUBM_D import _00_VALS_IN as CF_V


locals().update(CF_V.ALL_THE_VALS)
V = None


"""

bool
dict
float
function
int
list
module
str
tuple

class03_C {INS.getmembers(class03_C.C_03, isfunction)}
class03_C.__new__ {INS.getmembers(class03_C.__new__)}
getfullargspec(class03_C)  {INS.getfullargspec(class03_C)}

"""


ALL_THE_VALS = {
    "OBJECT_BOOL_IN_NONE": "OBJECT_BOOL_IN_NONE",
    "OBJECT_DICT_IN_DICT": "OBJECT_DICT_IN_DICT",
    "OBJECT_DICT_IN_FUNC": "OBJECT_DICT_IN_FUNC",
    "OBJECT_DICT_IN_LIST": "OBJECT_DICT_IN_LIST",
    "OBJECT_DICT_IN_MODL": "OBJECT_DICT_IN_MODL",
    "OBJECT_DICT_IN_NONE": "OBJECT_DICT_IN_NONE",
    "OBJECT_DICT_IN_TUPL": "OBJECT_DICT_IN_TUPL",
    "OBJECT_FLT_IN_NONE": "OBJECT_FLT_IN_NONE",
    "OBJECT_FUNC_IN_DICT": "OBJECT_FUNC_IN_DICT",
    "OBJECT_FUNC_IN_FUNC": "OBJECT_FUNC_IN_FUNC",
    "OBJECT_FUNC_IN_LIST": "OBJECT_FUNC_IN_LIST",
    "OBJECT_FUNC_IN_MODL": "OBJECT_FUNC_IN_MODL",
    "OBJECT_FUNC_IN_NONE": "OBJECT_FUNC_IN_NONE",
    "OBJECT_FUNC_IN_TUPL": "OBJECT_FUNC_IN_TUPL",
    "OBJECT_INT_IN_NONE": "OBJECT_INT_IN_NONE",
    "OBJECT_LIST_IN_DICT": "OBJECT_LIST_IN_DICT",
    "OBJECT_LIST_IN_FUNC": "OBJECT_LIST_IN_FUNC",
    "OBJECT_LIST_IN_LIST": "OBJECT_LIST_IN_LIST",
    "OBJECT_LIST_IN_MODL": "OBJECT_LIST_IN_MODL",
    "OBJECT_LIST_IN_NONE": "OBJECT_LIST_IN_NONE",
    "OBJECT_LIST_IN_TUPL": "OBJECT_LIST_IN_TUPL",
    "OBJECT_MODL_IN_DICT": "OBJECT_MODL_IN_DICT",
    "OBJECT_MODL_IN_FUNC": "OBJECT_MODL_IN_FUNC",
    "OBJECT_MODL_IN_LIST": "OBJECT_MODL_IN_LIST",
    "OBJECT_MODL_IN_MODL": "OBJECT_MODL_IN_MODL",
    "OBJECT_MODL_IN_NONE": "OBJECT_MODL_IN_NONE",
    "OBJECT_MODL_IN_TUPL": "OBJECT_MODL_IN_TUPL",
    "OBJECT_NONE_IN_DICT": "OBJECT_NONE_IN_DICT",
    "OBJECT_NONE_IN_FUNC": "OBJECT_NONE_IN_FUNC",
    "OBJECT_NONE_IN_LIST": "OBJECT_NONE_IN_LIST",
    "OBJECT_NONE_IN_MODL": "OBJECT_NONE_IN_MODL",
    "OBJECT_NONE_IN_NONE": "OBJECT_NONE_IN_NONE",
    "OBJECT_NONE_IN_TUPL": "OBJECT_NONE_IN_TUPL",
    "OBJECT_STR_IN_NONE": "OBJECT_STR_IN_NONE",
    "OBJECT_TUPL_IN_DICT": "OBJECT_TUPL_IN_DICT",
    "OBJECT_TUPL_IN_FUNC": "OBJECT_TUPL_IN_FUNC",
    "OBJECT_TUPL_IN_LIST": "OBJECT_TUPL_IN_LIST",
    "OBJECT_TUPL_IN_MODL": "OBJECT_TUPL_IN_MODL",
    "OBJECT_TUPL_IN_NONE": "OBJECT_TUPL_IN_NONE",
    "OBJECT_TUPL_IN_TUPL": "OBJECT_TUPL_IN_TUPL",
    "STR_ASSIGN": "STR_ASSIGN",
    "STR_END": "STR_END",
    "STR_FINAL": "STR_FINAL",
    "TYPE_BOOL": "TYPE_BOOL",
    "TYPE_DICT": "TYPE_DICT",
    "TYPE_FLT": "TYPE_FLT",
    "TYPE_FUNC": "TYPE_FUNC",
    "TYPE_INT": "TYPE_INT",
    "TYPE_LIST": "TYPE_LIST",
    "TYPE_MODL": "TYPE_MODL",
    "TYPE_STR": "TYPE_STR",
    "TYPE_TUPL": "TYPE_TUPL",
    "TYPE_UNK"; "TYPE_UNK",
}
locals().update(ALL_THE_VALS)


TYPES_DICT = {
    bool: TYPE_BOOL,
    dict: TYPE_DICT,
    float: TYPE_FLT,
    TTYPES.FunctionType: TYPE_FUNC,
    int: TYPE_INT,
    list: TYPE_LIST,
    TTYPES.ModuleType: TYPE_MODL,
    str: TYPE_STR,
    tuple: TYPE_TUPL,
}


ALL_THE_DICTS = [
    OBJECT_DICT_IN_DICT,
    OBJECT_DICT_IN_FUNC,
    OBJECT_DICT_IN_LIST,
    OBJECT_DICT_IN_MODL,
    OBJECT_DICT_IN_NONE,
    OBJECT_DICT_IN_TUPL,
]


ALL_THE_FUNCS = [
    OBJECT_FUNC_IN_DICT,
    OBJECT_FUNC_IN_FUNC,
    OBJECT_FUNC_IN_LIST,
    OBJECT_FUNC_IN_MODL,
    OBJECT_FUNC_IN_NONE,
    OBJECT_FUNC_IN_TUPL,
]


ALL_THE_LISTS = [
    OBJECT_LIST_IN_DICT,
    OBJECT_LIST_IN_FUNC,
    OBJECT_LIST_IN_LIST,
    OBJECT_LIST_IN_MODL,
    OBJECT_LIST_IN_NONE,
    OBJECT_LIST_IN_TUPL,
]


ALL_THE_MODLS = [
    OBJECT_MODL_IN_DICT,
    OBJECT_MODL_IN_FUNC,
    OBJECT_MODL_IN_LIST,
    OBJECT_MODL_IN_MODL,
    OBJECT_MODL_IN_NONE,
    OBJECT_MODL_IN_TUPL,
]


ALL_THE_NONES = [
    OBJECT_NONE_IN_DICT,
    OBJECT_NONE_IN_FUNC,
    OBJECT_NONE_IN_LIST,
    OBJECT_NONE_IN_MODL,
    OBJECT_NONE_IN_NONE,
    OBJECT_NONE_IN_TUPL,
]


ALL_THE_TUPLS = [
    OBJECT_TUPL_IN_DICT,
    OBJECT_TUPL_IN_FUNC,
    OBJECT_TUPL_IN_LIST,
    OBJECT_TUPL_IN_MODL,
    OBJECT_TUPL_IN_NONE,
    OBJECT_TUPL_IN_TUPL,
]


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * Start of fixKeys
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def fixKeys(nameToFix_):
  # fold here ⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1
  # 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱
  if (
      (isinstance(nameToFix_, str) is True)
  ):
    return f"""{DBLQT}{nameToFix_}{DBLQT}"""
  # ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱ ⟰1⟱
  else:
    return f"""{nameToFix_}"""
  # ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1
  # fold here ⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * End of fixKeys
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * Start of returnContainerValsDict
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def returnContainerValsDict(*,
    containerType_,
    indentIn_,
    nameIn_,
):
  # fold here ⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1
  if (
      (containerType_ == OBJECT_DICT_IN_DICT)
  ):
    _strAssign_ = f"""{NINDENT_IN(indentIn_)}(dict){fixKeys(nameIn_)}: {OBRCE}{NEWLINE}"""
    _strEnd_ = f""",{NEWLINE}"""
    _strFinal_ = f"""{NTAB(indentIn_)}{CBRCE},{NEWLINE}{NINDENT_OUT(indentIn_)}{NEWLINE}"""
    return {
        STR_ASSIGN: _strAssign_,
        STR_END: _strEnd_,
        STR_FINAL: _strFinal_,
    }

  if (
      (containerType_ == OBJECT_DICT_IN_FUNC)
  ):
    _strAssign_ = f"""{NINDENT_IN(indentIn_)}(dict){fixKeys(nameIn_)} = {OBRCE}{NEWLINE}"""
    _strEnd_ = f""",{NEWLINE}"""
    _strFinal_ = f"""{NTAB(indentIn_)}{CBRCE}{NEWLINE}{NINDENT_OUT(indentIn_)}{NEWLINE}"""
    return {
        STR_ASSIGN: _strAssign_,
        STR_END: _strEnd_,
        STR_FINAL: _strFinal_,
    }

  if (
      (containerType_ == OBJECT_DICT_IN_LIST)
  ):
    _strAssign_ = f"""{NINDENT_IN(indentIn_)}(dict){OBRCE}{NEWLINE}"""
    _strEnd_ = f""",{NEWLINE}"""
    _strFinal_ = f"""{NTAB(indentIn_)}{CBRCE},{NEWLINE}{NINDENT_OUT(indentIn_)}{NEWLINE}"""
    return {
        STR_ASSIGN: _strAssign_,
        STR_END: _strEnd_,
        STR_FINAL: _strFinal_,
    }

  if (
      (containerType_ == OBJECT_DICT_IN_MODL)
  ):
    _strAssign_ = f"""{NINDENT_IN(indentIn_)}(dict){fixKeys(nameIn_)} = {OBRCE}{NEWLINE}"""
    _strEnd_ = f""",{NEWLINE}"""
    _strFinal_ = f"""{NTAB(indentIn_)}{CBRCE}{NEWLINE}{NINDENT_OUT(indentIn_)}{NEWLINE}"""
    return {
        STR_ASSIGN: _strAssign_,
        STR_END: _strEnd_,
        STR_FINAL: _strFinal_,
    }

  if (
      (containerType_ == OBJECT_DICT_IN_NONE)
  ):
    _strAssign_ = f"""{NINDENT_IN(indentIn_)}(dict){fixKeys(nameIn_)} = {OBRCE}{NEWLINE}"""
    _strEnd_ = f""",{NEWLINE}"""
    _strFinal_ = f"""{NTAB(indentIn_)}{CBRCE}{NEWLINE}{NINDENT_OUT(indentIn_)}{NEWLINE}"""
    return {
        STR_ASSIGN: _strAssign_,
        STR_END: _strEnd_,
        STR_FINAL: _strFinal_,
    }

  if (
      (containerType_ == OBJECT_DICT_IN_TUPL)
  ):
    _strAssign_ = f"""{NINDENT_IN(indentIn_)}(dict){OBRCE}{NEWLINE}"""
    _strEnd_ = f""",{NEWLINE}"""
    _strFinal_ = f"""{NTAB(indentIn_)}{CBRCE},{NEWLINE}{NINDENT_OUT(indentIn_)}{NEWLINE}"""
    return {
        STR_ASSIGN: _strAssign_,
        STR_END: _strEnd_,
        STR_FINAL: _strFinal_,
    }
  return {
      STR_ASSIGN: None,
      STR_END: None,
      STR_FINAL: None,
  }
  # fold here ⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * End of returnContainerValsDict
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * Start of returnContainerValsFunc
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def returnContainerValsFunc(*,
    containerType_,
    indentIn_,
    nameIn_,
):
  # fold here ⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1
  if (
      (containerType_ == OBJECT_FUNC_IN_DICT)
  ):
    _strAssign_ = f"""{NINDENT_IN(indentIn_)}(func){nameIn_}(<params follow>):{NEWLINE}"""
    _strEnd_ = f""""""
    _strFinal_ = f"""{NEWLINE}{NINDENT_OUT(indentIn_)}{NEWLINE}"""
    return {
        STR_ASSIGN: _strAssign_,
        STR_END: _strEnd_,
        STR_FINAL: _strFinal_,
    }

  if (
      (containerType_ == OBJECT_FUNC_IN_FUNC)
  ):
    _strAssign_ = f"""{NINDENT_IN(indentIn_)}(func){nameIn_}(<params follow>):{NEWLINE}"""
    _strEnd_ = f""""""
    _strFinal_ = f"""{NEWLINE}{NINDENT_OUT(indentIn_)}{NEWLINE}"""
    return {
        STR_ASSIGN: _strAssign_,
        STR_END: _strEnd_,
        STR_FINAL: _strFinal_,
    }

  if (
      (containerType_ == OBJECT_FUNC_IN_LIST)
  ):
    _strAssign_ = f"""{NINDENT_IN(indentIn_)}(func){nameIn_}(<params follow>):{NEWLINE}"""
    _strEnd_ = f""""""
    _strFinal_ = f"""{NEWLINE}{NINDENT_OUT(indentIn_)}{NEWLINE}"""
    return {
        STR_ASSIGN: _strAssign_,
        STR_END: _strEnd_,
        STR_FINAL: _strFinal_,
    }

  if (
      (containerType_ == OBJECT_FUNC_IN_MODL)
  ):
    _strAssign_ = f"""{NINDENT_IN(indentIn_)}(func){nameIn_}(<params follow>):{NEWLINE}"""
    _strEnd_ = f""""""
    _strFinal_ = f"""{NEWLINE}{NINDENT_OUT(indentIn_)}{NEWLINE}"""
    return {
        STR_ASSIGN: _strAssign_,
        STR_END: _strEnd_,
        STR_FINAL: _strFinal_,
    }

  if (
      (containerType_ == OBJECT_FUNC_IN_NONE)
  ):
    _strAssign_ = f"""{NINDENT_IN(indentIn_)}(func){nameIn_}(<params follow>):{NEWLINE}"""
    _strEnd_ = f""""""
    _strFinal_ = f"""{NEWLINE}{NINDENT_OUT(indentIn_)}{NEWLINE}"""
    return {
        STR_ASSIGN: _strAssign_,
        STR_END: _strEnd_,
        STR_FINAL: _strFinal_,
    }

  if (
      (containerType_ == OBJECT_FUNC_IN_TUPL)
  ):
    _strAssign_ = f"""{NINDENT_IN(indentIn_)}(func){nameIn_}(<params follow>):{NEWLINE}"""
    _strEnd_ = f""""""
    _strFinal_ = f"""{NEWLINE}{NINDENT_OUT(indentIn_)}{NEWLINE}"""
    return {
        STR_ASSIGN: _strAssign_,
        STR_END: _strEnd_,
        STR_FINAL: _strFinal_,
    }
  return {
      STR_ASSIGN: None,
      STR_END: None,
      STR_FINAL: None,
  }
  # fold here ⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * End of returnContainerValsFunc
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * Start of returnContainerValsList
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
def returnContainerValsList(*,
    containerType_,
    indentIn_,
    nameIn_,
):
  # fold here ⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1⟱1
  if (
      (containerType_ == OBJECT_LIST_IN_DICT)
  ):
    _strAssign_ = f"""{NINDENT_IN(indentIn_)}(list){fixKeys(nameIn_)}: {OBRKT}{NEWLINE}"""
    _strEnd_ = f""",{NEWLINE}"""
    _strFinal_ = f"""{NEWLINE}{NTAB(indentIn_)}{CBRKT},{NEWLINE}{NINDENT_OUT(indentIn_)}{NEWLINE}"""
    return {
        STR_ASSIGN: _strAssign_,
        STR_END: _strEnd_,
        STR_FINAL: _strFinal_,
    }

  if (
      (containerType_ == OBJECT_LIST_IN_FUNC)
  ):
    _strAssign_ = f"""{NINDENT_IN(indentIn_)}(list){nameIn_} = {OBRKT}{NEWLINE}"""
    _strEnd_ = f""",{NEWLINE}"""
    _strFinal_ = f"""{NEWLINE}{NTAB(indentIn_)}{CBRKT}{NEWLINE}{NINDENT_OUT(indentIn_)}{NEWLINE}"""
    return {
        STR_ASSIGN: _strAssign_,
        STR_END: _strEnd_,
        STR_FINAL: _strFinal_,
    }

  if (
      (containerType_ == OBJECT_LIST_IN_LIST)
  ):
    _strAssign_ = f"""{NINDENT_IN(indentIn_)}(list){OBRKT}{NEWLINE}"""
    _strEnd_ = f""""""
    _strFinal_ = f"""{NEWLINE}{NTAB(indentIn_)}{CBRKT},{NEWLINE}{NINDENT_OUT(indentIn_)}{NEWLINE}"""
    return {
        STR_ASSIGN: _strAssign_,
        STR_END: _strEnd_,
        STR_FINAL: _strFinal_,
    }

  if (
      (containerType_ == OBJECT_LIST_IN_MODL)
  ):
    _strAssign_ = f"""{NINDENT_IN(indentIn_)}(list){nameIn_} = {OBRKT}{NEWLINE}"""
    _strEnd_ = f""",{NEWLINE}"""
    _strFinal_ = f"""{NEWLINE}{NTAB(indentIn_)}{CBRKT}{NEWLINE}{NINDENT_OUT(indentIn_)}{NEWLINE}"""
    return {
        STR_ASSIGN: _strAssign_,
        STR_END: _strEnd_,
        STR_FINAL: _strFinal_,
    }

  if (
      (containerType_ == OBJECT_LIST_IN_NONE)
  ):
    _strAssign_ = f"""{NINDENT_IN(indentIn_)}(list){nameIn_} = {OBRKT}{NEWLINE}"""
    _strEnd_ = f""",{NEWLINE}"""
    _strFinal_ = f"""{NEWLINE}{NTAB(indentIn_)}{CBRKT}{NEWLINE}{NINDENT_OUT(indentIn_)}{NEWLINE}"""
    return {
        STR_ASSIGN: _strAssign_,
        STR_END: _strEnd_,
        STR_FINAL: _strFinal_,
    }

  if (
      (containerType_ == OBJECT_LIST_IN_TUPL)
  ):
    _strAssign_ = f"""{NINDENT_IN(indentIn_)}(list){OBRKT}{NEWLINE}"""
    _strEnd_ = f""",{NEWLINE}"""
    _strFinal_ = f"""{NEWLINE}{NTAB(indentIn_)}{CBRKT},{NEWLINE}{NINDENT_OUT(indentIn_)}{NEWLINE}"""
    return {
        STR_ASSIGN: _strAssign_,
        STR_END: _strEnd_,
        STR_FINAL: _strFinal_,
    }

  return {
      STR_ASSIGN: None,
      STR_END: None,
      STR_FINAL: None,
  }
  # fold here ⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1⟰1
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * End of returnContainerValsList
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

















#
