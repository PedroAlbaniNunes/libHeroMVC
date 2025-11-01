from setuptools import setup, find_packages

# Lendo o README.md para o PyPI
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="libHeroMVCPHANunes",  # ⚡ Nome com hífen para o PyPI
    version="0.1.11",
    description="Biblioteca de criação e leitura de heróis e times de heróis.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Pedro Henrique Albani Nunes",
    author_email="albanipedroprofissional@gmail.com",
    url="https://github.com/PedroAlbaniNunes/libHeroMVC",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)