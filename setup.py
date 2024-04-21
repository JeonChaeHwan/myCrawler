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
    with open('README.md', encoding='utf-8') as f:
        long_description = f.read()
    long_description = long_description,
    long_description_content_type = 'text/markdonw',
)
