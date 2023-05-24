import setuptools

with open("README.md", "r", encoding="utf-8") as fhand:
    long_description = fhand.read()

setuptools.setup(
    name="root_exporter",
    version="0.0.1",
    author="Anima N K",
    author_email="nk.anima@gmail.com",
    description=("Pass .root file path and get the trees exported in .csv format."),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="to be filled",
    project_urls={
        "Bug Tracker": "to be filled",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["uproot","awkward","progress"],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "rootexport = exporter.cli:main",
        ]
    }
)