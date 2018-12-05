import setuptools

requirements = [
    'translate',
    'click',
    'click-log',
]

setuptools.setup(
    name="opml-translate",
    version="0.1.0",

    packages=setuptools.find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'opml-trans=opml_translate.command_line:translate_command'
        ],
    },

    author="Daniel Pechersky",
    author_email="danny.pechersky@gmail.com",
    description="Translates OPML files",
    url="",
)