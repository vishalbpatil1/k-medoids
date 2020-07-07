from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="k_Medoids",
    version="1.0.0",
    description="A Python package to get k_Medoids clustring .",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/vishalbpatil1/k-medoids",
    author="Vishal Patil",
    author_email="vishalbpatil1@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["k_medoids"],
    include_package_data=True,
    install_requires=["numpy","sklearn"],
)