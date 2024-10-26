from setuptools import setup, find_packages

setup(
    name="custom_path",  # Nome do pacote
    version="1.0.1",
    description="A package to manage custom paths and directories.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Guilherme Mello",
    author_email="guilhermesamello@gmail.com",
    url="https://github.com/gmellotec/custom_path.git",  # URL do repositório
    packages=find_packages(),  # Encontra pacotes automaticamente
    install_requires=[],  # Adicione dependências, se necessário
)