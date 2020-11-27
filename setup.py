import io
import setuptools
import os
import re
import sys
with open("README.md", "r") as fh:
    long_description = fh.read()

current_dir = os.path.abspath(os.path.dirname(__file__))

def get_version():
    version_file = os.path.join(current_dir, "retinaface", "__init__.py")
    with io.open(version_file, encoding="utf-8") as f:
        return re.search(r'^__version__ = [\'"]([^\'"]*)[\'"]', f.read(), re.M).group(1)

version = get_version()
    
setuptools.setup(
    name="Pytorch-detection", # Replace with your own username
    version="0.0.1",
    author="Hoang Phuong",
    author_email="hphuongdhsp@gmail.com",
    license='MIT',
    description = "A small example package for face recognition",
    long_description = long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hphuongdhsp/retinaface",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords='face detection, retinaface',
    install_requires=open('requirements.txt').readlines(),
    python_requires='>=3.6',
)