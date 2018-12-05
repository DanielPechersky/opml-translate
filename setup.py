import setuptools

with open("README.md", 'r') as f:
    long_description = f.read()

setuptools.setup(
    name="opml-translate",
    version="0.1.0",
    author="Daniel Pechersky",
    author_email="danny.pechersky@gmail.com",
    description="Translates OPML files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)