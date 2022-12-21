import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="create_py_app",
    version="0.1.0",
    author="Hideaki Yoshida",
    author_email="",
    description="A tool for creating a simple python framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hyoshida123/create-py-app",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    entry_points={
        "console_scripts": ["create_py_app=create_py_app.main:main"],
    },
)
