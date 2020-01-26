import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="flask_restplus_monkeypatch",
    version="0.0.1",
    author="Austin Plunkett",
    author_email="austin.plunkett+flask_restplus_monkeypatch@gmail.com",
    description="Apply some necessary patches to the RESTPlus package for Flask.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bitbucket.org/austinjp/flask_restplus_monkeypatch",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)

