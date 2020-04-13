import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mapquest",
    version="0.0.1",
    author="Mohammed Boukhlouf",
    author_email="mohammed.boukhlouf@outlook.com",
    description="An api wrapper for MapQuest",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/M-Boukhlouf/mapquest",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)