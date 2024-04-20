import setuptools
setuptools.setup(
    name = "mycrawlers",
    packages=["mycrawlers"],
    version="0.0.1",
    description="oss easily myCrawler",
    author = "ChaeHwanJeon",
    url ="https://github.com/JeonChaeHwan/myCrawler",
    download_url="https://github.com/JeonChaeHwan/myCrawler/",
    install_requires = ["bs4", "requests"],
    classifiers = [
        "Programming Language :: Python :: 3",
    ]
)
