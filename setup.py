import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.1"

REPO_NAME = "chicken-disease-classification"
AUTHOR_USER_NAME = "RAHUL"
SRC_REPO = "chickenClassifier"
AUTHOR_EMAIL = "prajapatirahul6796@gmail.com"


setuptools.setup(
    name= SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    description="A small python packagefor Classifier app",
    long_description=long_description,
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
    )

