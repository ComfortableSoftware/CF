

#
#
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
# * start of CF.setup.py
# * #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
#
#


from setuptools import find_packages
from setuptools import setup


setup(
  author="GaelicGrime",
  author_email="will.angus.blaylock@gmail.com",
  license="GPLv3",
  name="CS-CF",
  url="https://github.com/ComfortableSoftware/commonFunctions_py",
  version="0.11.0a1",
  package_dir={"CF": "CF"},
  package_data={
      "CF": [
          "../doc/*",
          "CLASSES_D/*",
          "CONST_D/*",
          "DEFS_D/*",
          "DOCS_D/*",
          "KEYS_D/*",
          "SUBM_D/*",
      ]
  },
  packages=find_packages(),
  install_requires=[
  ],
  extras_require={
      "hashing": ["hashlib"],
      "pickling": ["pickle"],
      "databases": ["mysql"],
      "time-date-stuff": [
          "datedelta",
          "datetime",
          "dateutil",
          "time",
      ],
      "debugging": [
          "inspect",
      ],
  }
)
