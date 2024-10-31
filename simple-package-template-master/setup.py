from setuptools import setup, find_packages

setup(
    name="combinação_fotos",  
    version="0.0.1",           
    author="Nanda",         
    author_email="fernandacrosa57@gmail.com",  
    description="A criação de pacotes em Python permite combinar duas imagens, utilizando uma delas como base para a paisagem e a outra para as cores, gerando uma nova imagem que mescla elementos de ambas, resultando em uma composição única e criativa.",
    long_description=open('README.md').read(),  
    long_description_content_type="text/markdown",
    url="", 
    packages=find_packages(),  
    classifiers=[              
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',  
)
