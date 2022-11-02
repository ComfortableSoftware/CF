

from CF.SUBM_D import _01_DIALOG_VARS as V


V.V = V
locals().update(V.CF_V.ALL_THE_VALS)
locals().update(V.ALL_THE_KEYS)


def checkProgressBar(*,
    dialogPath_,
):
  # Returns _result_
  pass


def closeProgressbar(*,
    dialogPath_
):
  # Returns _result_
  pass


def doA2BtnDialog(*,
    noLabel_="no",
    question_=None,
    title_="Answer me do‼",
    yesLabel_="yes",
):
  # Returns _result_
  # 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱
  return None
  # ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1


def doA3BtnDialog(*,
    cancelLabel_="cancel",
    noLabel_="no",
    question_=None,
    title_="Answer me do‼",
    yesLabel_="yes",
):
  # returns _result_.
  # 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱
  return None
  # ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1


def doACalendar (*,
    default_,  # Defaults to today
    format_="ddd MMM d yyyy",  # QT style
    text_,
    title_="Select a date",
):
  pass


def doAChecklist (*,
    checkList_,  # [(index (hidden), text, on/off/"" (set state)/hidden) …] returns with stdout == index index … of any items that were clicked on or defaulted on and not offed
    text_,
    title_="Click all that apply:",
):
  pass


def doACombobox (*
    default_,  #
    itemList_,  # ["item 1", "item 2", …] returns
    text_,
    title_="Select one:",
):
  pass


def doADetailedErrorDialog(*,
    details_,
    text_,
    title_="Something went wrong",
    where_,
):
  pass


def doADetailedWarningDialog(*,
    details_,
    text_=,
    title_="Something is fishy",
    where_,
):
  pass


def doAMenu (*,
    default_,  # No default unless you enter it
    items_,  # [("index (hidden)" "description)") …]
    text_,
    title_="Select your choice.",
):
  pass


def doAMessageBox(*,
    okLabel_="OK",
    text_,
    title_="Message for you",
):
  pass


def doAnErrorDialog(*,
    text_,
    title_="Something went wrong",
    where_,
):
  pass


def doAnInputbox(*,
    default_="",
    text_,
    title_="Input a line",
):
  pass


def doAPassivepopup (*,
    text_,
    timeout_="10",
    title_="An annoying popup",
):
  pass


def doARadiolist (*,
    items_,  # [(index description on/off/"")]  Last one listed as "on" will be the default selection
    text_,
    title_="Pick one",
):
  pass


def doATextbox(*,
    filename_,
    height_=300,
    title_="Heard you liked some reading yo‼",
    width_=700,
):
  pass


def doATextInputBox(*,
    default_="",
    filename_,
    height_=300,
    text_,
    title_="Heard you liked some reading/typing yo‼",
    width_=700,
):
  pass


def doAWarningDialog(*,
    text_,
    title_="Something is fishy",
    where_,
):
  pass


def doGetExistingDirectory (*
    title_="Select a directory",
    startDir_=".",
):
  pass


def doGetOpenFilename (*,
    title_="Pick a file",
    startDir_,
    filter_="",  # "mime/type mime/type …" or "name (*.ext *.ext …)" or "name (filename.ext …)"
):
  pass


def doGetSaveFilename (*,
    title_="Pick a file",
    startDir_,
    filter_="",  # "mime/type mime/type …" or "name (*.ext *.ext …)" or "name (filename.ext …)"
):
  pass


def enterANewPassword (*,
    text_,
    title_="Enter a new password",
):
  pass


def inputAPassword (*,
    text_,
    title_="Your password, enter it",
):
  pass


def setProgressVals(*,
    autoClose_=True,
    dialogPath_,
    maximum_=None,
    showCancelButton_=None,
    textLabel_=None,
    value_=None,
):
  # Returns _result_
  pass


def startAProgressBar(*,
    autoClose=True,  # Auto closes when 100% is reached.
    numOfSteps_==100,
    showCancelButton_=True,
    text_="Progress:",
    title_="Getting things done",
    value=0,
):
  # 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱ 0⟱
  ## Returns _result_
  _commands_ = [
      "kdialog",
      "--title",
      f"""{title_}""",
      "--progressbar",
      f"""{text_}""",
      f"""{numOfSteps_}""",
  ]
  _result1_ V.runIt(_commands_)
  _result1_ = V.parseResult(
      _result1_,
      startingProgressbar=True,
  )
  # 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱
  if (
      (_result1_[K_RETURN_CODE] != 0)
  ):
    V.runError("starting a progress bar", _result1_)
  # ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1
  _commands_ = [
      "qdbus",
      f"""{_result1_[K_SERVICE_NAME]}""",
      f"""{_result1_[K_SERVICE_PATH]}""",
      V.SM_PROGRESSBAR_SHOW_CANCEL_BUTTON,
      f"""{showCancelButton_}""".lower(),
  ]
  _result2_ = V.runIt(_commands_)
  _result2_ = V.parseResult(_result2_)
  # 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱
  if (
      (_result2_[K_RETURN_CODE] != 0)
  ):
    V.runError("setting the cancel button on a progress bar", _result2_)
  # ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1
  _commands_ = [
      "qdbus",
      f"""{_result1_[K_SERVICE_NAME]}""",
      f"""{_result1_[K_SERVICE_PATH]}""",
      V.SM_PROGRESSBAR_AUTOCLOSE,
      f"""{autoClose_}""".lower(),
  ]
  _result3_ = V.runIt(_commands_)
  _result3_ = V.parseResult(_result2_)
  # 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱ 1⟱
  if (
      (_result3_[K_RETURN_CODE] != 0)
  ):
    V.runError("setting the auto close on a progress bar", _result3_)
  # ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1 ⟰1
  return _result1_
  # ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0 ⟰0


def updateAProgressbar (*,
    dialogPath_,
    maximum_=None,
    value=None,
    autoClose_=None,
    showCancelButton_=None,
):
  pass





#
