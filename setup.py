

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
	author_email="gaelicgrime@justpagans.org",
	license="BSD",
	name="CF",
	url="https://github.com/ComfortableSoftware-DEV/CF_commonFunctions_py",
	version="0.8.0",
	package_dir={"CF": "CF"},
	package_data={
			"CF": [
					".FM/*",
					"CLASSES_D/*",
					"CONST_D/*",
					"DEFS_D/*",
					"DOCS_D/*",
					"KEYS_D/*",
					"SUBM_D/*",
			]
	},
	packages=["CF"],
	install_requires=[
	],
	extras_require={
			"hashing": ["hashlib"],
			"pickling": ["pickle"],
			"timestuff": [
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
