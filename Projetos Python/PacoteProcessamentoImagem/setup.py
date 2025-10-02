from setuptools import setup, find_packages

setup(
    name="image_palette_processor",
    version="0.1.0",
    description="Pacote simples para transferir paletas de cores e mesclar imagens",
    author="Seu Nome",
    packages=find_packages(),
    install_requires=["pillow", "numpy"],
)
