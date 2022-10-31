

from CF.SUBM_D import _01_DIALOG_VARS as V


V.V = V
locals().update(V.CF_V.ALL_THE_VALS)


def doA2BtnDialog(*,
    noLabel_="no",
    question_=None,
    yesLabel_="yes",
):
  if (
      (question_ == "")
  ):
    question_ = "Yes or No"
  _result_ = V.SP.run(
      V.YES_NO(question_)
  )
  if (
      (_result_.returncode == 0)
  ):
    return True
  elif (
      (_result_.returncode == 1)
  ):
    return False
  return None


def doA3BtnDialog(*,
    cancelLabel_="cancel",
    noLabel_="no",
    question_=None,
    yesLabel_="yes",
):
  _result_ = V.SP.run(V.YES_NO(question_))
  if (
      (_result_.returncode == 0)
  ):
    return True
  elif (
      (_result_.returncode == 1)
  ):
    return False
  return None




#
