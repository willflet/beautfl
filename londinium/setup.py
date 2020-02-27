from setuptools import setup, find_packages

setup(
    name="londinium",
    version="0.1",
    packages=find_packages(),

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=['docutils>=0.3'],

    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst'],
    },

    # metadata to display on PyPI
    author="William Fletcher",
    description="",
    classifiers=["License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)"],
    keywords="London transport underground tube bus TfL",

    # could also include long_description, download_url, classifiers, etc.
)
