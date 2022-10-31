

from CF.SUBM_D import (
    _00_VALS_IN as CF_V
)
import subprocess as SP


V = None
locals().update(CF_V.ALL_THE_VALS)


YES_NO = lambda __TEXT__: [
    "kdialog",
    "--yesno",
    f"""{__TEXT__}""",
]






#
