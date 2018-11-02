import setuptools

with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="YamlDB",
    version="0.0.1_a",
    author="RedstonedLife",
    author_email="tal.baskin1@gmail.com",
    description="A small database module using Yaml",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RedstonedLife/YamlDB",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
