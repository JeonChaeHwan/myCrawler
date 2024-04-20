import setuptools
setuptools.setup(
    name = "myCawler",
    packages=["myweb"],
    version="0.0.1",
    description="oss easily myCrawler",
    author = "ChaeHwanJeon",
    url ="https://github.com/JeonChaeHwan/webcrawler",
    download_url="https://github.com/JeonChaeHwan/webcrawler",
    install_requires = ["bs4", "requests"],
    classifiers = [
        "Programming Language :: Python :: 3",
    ]
)
