

from CF.SUBM_D import (
    _00_VALS_IN as CF_V
)
import subprocess as SP


V = None
locals().update(CF_V.ALL_THE_VALS)


def runIt(commandsToRun_, *, **KWArgs_={}):
  if (
      ("capture_output" not in KWArgs_)
  ):
    KWArgs_["capture_output"] = True

  if (
      ("text" not in KWArgs_)
  ):
    KWArgs_["text"] = True

  SP.run(commandsToRun_, **KWArgs_)






#
