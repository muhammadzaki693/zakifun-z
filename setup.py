import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zakifun-z_zakirhamadan53", # Replace with your own username
    version="0.0.1",
    author="zakirhamadan53",
    author_email="rzaki9353@gmail.com",
    description="A small package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/muhammadzaki693/zakifun-z",
    project_urls={
        "Bug Tracker": "https://github.com/muhammadzaki693/zakifun-z/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.x',
)