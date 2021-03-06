from setuptools import setup
import os
import re


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

def read(*names, **kwargs):
    with open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8")
    ) as fp:
        return fp.read()

def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


classifiers = [
    "Development Status :: 4 - Beta",
    "Environment :: X11 Applications :: Qt",
    "Intended Audience :: Education",
    "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3.4"
]

setup(
    name='poliBeePsync',
    version = find_version("polibeepsync/__init__.py"),
    url = "http://www.davideolianas.com/polibeepsync",
    author= "Davide Olianas",
    author_email= "ubuntupk@gmail.com",
    license = 'GPLv3+',
    install_requires = [
        "requests",
        "appdirs",
        "PySide2",
        "beautifulsoup4",
        "pyparsing",
        "signalslot"
    ],
    packages = ['polibeepsync'],
    description = "Sync files from https://beep.metid.polimi.it "
                 "(for students of Politecnico di Milano)",
    long_description = long_description,
    classifiers = classifiers,
    dependency_links = ['http://github.com/davethecipo/signalslot/tarball'
                        '/py34#egg=signalslot-0.10.0'],
    entry_points = {
    'console_scripts': [
        'polibeepsync=polibeepsync.qtgui:main',
    ],
    'gui_scripts': [
        'polibeepsync-gui=polibeepsync.qtgui:main'
    ]
}
)
