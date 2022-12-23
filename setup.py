import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="create-py-app",
    version="0.1.3",
    author="Hideaki Yoshida",
    author_email="",
    description="A tool for creating a simple python framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hyoshida123/create-py-app",
    packages=setuptools.find_packages(),
    install_requires=["pyyaml"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": ["create-py-app=create_py_app.main:main"],
    },
)
