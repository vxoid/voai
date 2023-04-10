from setuptools import setup, find_packages
import sys

classifiers = [
  "Operating System :: OS Independent",
  "License :: OSI Approved :: Apache Software License",
  "Programming Language :: Python :: 3",
]

CURRENT_VERSION = sys.version_info[:2]
REQUIRED_VERSION = (3, 7)

if CURRENT_VERSION < REQUIRED_VERSION:
    sys.stderr.write(
        f"""Current python version ({CURRENT_VERSION[0]}.{CURRENT_VERSION[1]}) is lower than required ({REQUIRED_VERSION[0]}.{REQUIRED_VERSION[1]})
        """
    )

setup(
    name="voai",
    version="0.0.2",
    description="A tool designed for working with 🧑‍💻ChatGPT API🧑‍💻",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/CURVoid/voai",
    author="VOID",
    license="APACHE 2.0", 
    keywords=["chatgpt", "gpt", "chat", "voai", "openai", "ai"],
    package_dir={"": "voai"},
    py_modules=["voai"], # Files in voai dir
    install_requires=["requests==2.22.0"],
    classifiers=classifiers,
)