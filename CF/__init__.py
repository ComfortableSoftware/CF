#!/usr/bin/env /usr/bin/python


from CF.SUBM_D import _00_OS as CF_OS


__all__ = []


def __main__():

  __modulesList__ = CF_OS.globFilePiecesNumsList(CF_OS.DIR_NAME(__file__) + "/*")
  for __thisEntry__ in __modulesList__:
    __thisFile__ = __thisEntry__[2]
    if (
        (__thisFile__ != "__init__.py")
    ):
      __all__.append(__thisFile__)


__main__()
