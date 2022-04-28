

# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * Keys
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
K_ACCESS_TIME = "K_ACCESS_TIME"
K_BLOCKS_ALLOCATED = "K_BLOCKS_ALLOCATED"
K_CHANGED_TIME = "K_CHANGED_TIME"
K_DIR = "K_DIR"
K_EXTENSION = "K_EXTENSION"
K_FILENAME = "K_FILENAME"
K_FILETYPE = "K_FILETYPE"
K_FT_CODE = "K_FT_CODE"
K_FT_DATA = "K_FT_DATA"
K_FT_DOCS = "K_FT_DOCS"
K_FT_PICS = "K_FT_PICS"
K_FT_SNDS = "K_FT_SNDS"
K_FT_TEXT = "K_FT_TEXT"
K_FT_UNKNOWN = "K_FT_UNKNOWN"
K_FT_VIDS = "K_FT_VIDS"
K_GID = "K_GID"
K_I_CAN_EXECUTE = "K_I_CAN_EXECUTE"
K_I_CAN_READ = "K_I_CAN_READ"
K_I_CAN_WRITE = "K_I_CAN_WRITE"
K_IS_A_DIR = "K_IS_A_DIR"
K_IS_A_FILE = "K_IS_A_FILE"
K_IS_A_KNOWN_FILE_TYPE = "K_IS_A_KNOWN_FILE_TYPE"
K_IS_A_SYMLINK = "K_IS_A_SYMLINK"
K_JUST_FILENAME = "K_JUST_FILENAME"
K_MODE = "K_MODE"
K_MODIFY_TIME = "K_MODIFY_TIME"
K_NUMS = "K_NUMS"
K_PATH = "K_PATH"
K_SIZE = "K_SIZE"
K_UID = "K_UID"


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * File Entry Vars
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
SHORT_ENTRY_TUP = (
    (K_PATH, ""),
    (K_DIR, ""),
    (K_FILENAME, ""),
    (K_JUST_FILENAME, ""),
    (K_EXTENSION, ""),
    (K_NUMS, 0),
)
def E_SHORT_ENTRY():
  return dict((x, y) for x, y in SHORT_ENTRY_TUP)


ENTRY_TUP = (
    (K_ACCESS_TIME, 0),
    (K_BLOCKS_ALLOCATED, 0),
    (K_CHANGED_TIME, 0),
    (K_DIR, ""),
    (K_EXTENSION, ""),
    (K_FILENAME, ""),
    (K_FILETYPE, K_FT_UNKNOWN),
    (K_GID, 0),
    (K_I_CAN_EXECUTE, False),
    (K_I_CAN_READ, False),
    (K_I_CAN_WRITE, False),
    (K_IS_A_DIR, False),
    (K_IS_A_FILE, False),
    (K_IS_A_KNOWN_FILE_TYPE, False),
    (K_IS_A_SYMLINK, False),
    (K_JUST_FILENAME, False),
    (K_MODE, -1),
    (K_MODIFY_TIME, 0),
    (K_NUMS, 0),
    (K_PATH, ""),
    (K_SIZE, 0),
    (K_UID, 0),
)
def E_ENTRY():
  return dict((x, y) for x, y in ENTRY_TUP)


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * Sanity Checks
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
DIR_BLACK_LIST = "[a-zA-Z0-9./]+"
DIRWHITELIST = "[^a-zA-Z0-9./]+"
FILEBLACKLIST = "[a-zA-Z0-9.]+"
FILEWHITELIST = "[^a-zA-Z0-9.]+"


ILLEGALPATHS = [  # list of absolute paths to be completely ignored if used
  "/",  # do not operate on / ever
]

ILLEGALWILDCARDS = [  # list all of the portions of a filename which will result in an error [0:] based
  "/bin/",  # illegal wildcards, these are most often /path/ and will be [0:] based
  "/boot/",  # illegal wildcards, these are most often /path/ and will be [0:] based
  "/dev/",  # illegal wildcards, these are most often /path/ and will be [0:] based
  "/efi/",  # illegal wildcards, these are most often /path/ and will be [0:] based
  "/etc/",  # illegal wildcards, these are most often /path/ and will be [0:] based
  "/home/",  # illegal wildcards, these are most often /path/ and will be [0:] based
  "/lib/",  # illegal wildcards, these are most often /path/ and will be [0:] based
  "/lib64/",  # illegal wildcards, these are most often /path/ and will be [0:] based
  "/media/",  # illegal wildcards, these are most often /path/ and will be [0:] based
  "/opt/",  # illegal wildcards, these are most often /path/ and will be [0:] based
  "/proc/",  # illegal wildcards, these are most often /path/ and will be [0:] based
  "/root/",  # illegal wildcards, these are most often /path/ and will be [0:] based
  "/run/",  # illegal wildcards, these are most often /path/ and will be [0:] based
  "/sbin/",  # illegal wildcards, these are most often /path/ and will be [0:] based
  "/srv/",  # illegal wildcards, these are most often /path/ and will be [0:] based
  "/sys/",  # illegal wildcards, these are most often /path/ and will be [0:] based
  "/tmp/",  # illegal wildcards, these are most often /path/ and will be [0:] based
  "/usr/",  # illegal wildcards, these are most often /path/ and will be [0:] based
  "/var/",  # illegal wildcards, these are most often /path/ and will be [0:] based
]


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * File Extension Vars
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
FTL_CODE = [
    ".c",
    ".coffee",
    ".pl",
    ".py",
    ".sh",
    ".zsh",
]

FTL_DATA = [
    ".cson",
    ".csv",
    ".db",
    ".json",
    ".kml",
    ".kmz",
]
FTL_TEXT_DATA = [
    ".cson",
    ".csv",
    ".json",
    ".kml",
]

FTL_DOCS = [
    ".md",
    ".pdf",
]
FTL_TEXT_DOCS = [
    ".md",
]

FTL_PICS = [
    ".bmp",
    ".gif",
    ".jpeg",
    ".jpg",
    ".png",
    ".webp",
]

FTL_SNDS = [
    ".au",
    ".mp3",
    ".wav",
]

FTL_TEXT = [
]
FTL_TEXT.extend(FTL_CODE)

FTL_VIDS = [
    ".avi",
    ".divx",
    ".flv",
    ".m2ts",
    ".m4a",
    ".m4v",
    ".mkv",
    ".mov",
    ".mp4",
    ".mpeg",
    ".mpg",
    ".webm",
    ".wmv",
]

# LEAVE AT BOTTOM OF FILE TYPES
FTL_MEDIA = []
FTL_MEDIA.extend(FTL_PICS)
FTL_MEDIA.extend(FTL_VIDS)
# FTL_MEDIA.extend(FTL_SNDS)

FTL_ALL_KNOWN = []
FTL_ALL_KNOWN.extend(FTL_CODE)
FTL_ALL_KNOWN.extend(FTL_DOCS)
FTL_ALL_KNOWN.extend(FTL_PICS)
FTL_ALL_KNOWN.extend(FTL_TEXT)
FTL_ALL_KNOWN.extend(FTL_VIDS)


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * Ignore File Lists
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
IL_PYTHON = [
    "__enter__.py",
    "__exit__.py",
    "__init__.py",
    "__main__.py",
]

IL_MEDIA = [
    "thumbs.db",
    "__UNRENAME__.zsh"
]


# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * File Modes
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
U_R = lambda __MODE__: __MODE__ and 0o400
U_W = lambda __MODE__: __MODE__ and 0o200
U_X = lambda __MODE__: __MODE__ and 0o100
G_R = lambda __MODE__: __MODE__ and 0o040
G_W = lambda __MODE__: __MODE__ and 0o020
G_X = lambda __MODE__: __MODE__ and 0o010
A_R = lambda __MODE__: __MODE__ and 0o004
A_W = lambda __MODE__: __MODE__ and 0o002
A_X = lambda __MODE__: __MODE__ and 0o001




#
