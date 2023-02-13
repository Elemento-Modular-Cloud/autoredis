import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="AutoRedis",
    version="0.1.0",
    author="Elemento s.r.l.",
    author_email="fvalle@elemento.cloud",
    description="Redis on steroids",
    license="GPL",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Elemento-Modular-Cloud/autoredis",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL License",
        "Operating System :: OS Independent",
    ],
    install_requires = ["redis", 
        "docker"],
    python_requires='>=3.9',
)