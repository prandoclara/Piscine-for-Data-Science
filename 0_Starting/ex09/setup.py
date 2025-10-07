from setuptools import setup, find_packages

"""
Résumé du processus de création du package ft_package (Piscine Python 42)

1/ Structure du projet :
ex09/
│
├── ft_package/
│   ├── __init__.py       # rend le dossier importable et expose count_in_list
│   └── count.py          # contient la fonction principale
│
├── setup.py              # décrit le package pour pip
├── README.md             # (optionnel) petite description
├── venv/                 # environnement virtuel local
└── dist/                 # fichiers générés (.tar.gz et .whl)

2/ Contenu principal :
- ft_package/__init__.py :
    from .count import count_in_list
- ft_package/count.py :
    définit la fonction count_in_list(lst, item)
    → retourne le nombre d'occurrences de item dans lst

3/ Build du package :
    python3 -m venv venv
    source venv/bin/activate
    pip install build
    python3 -m build

    # Résultat → dist/ft_package-0.0.1.tar.gz
    # et ft_package-0.0.1-py3-none-any.whl

4/ Installation du package :
    pip install ./dist/ft_package-0.0.1.tar.gz
       ou
    pip install ./dist/ft_package-0.0.1-py3-none-any.whl

5/ Test dans un autre dossier :
    mkdir ../test_package && cd ../test_package
    python3 -m venv venv && source venv/bin/activate
    pip install ../ex09/dist/ft_package-0.0.1.tar.gz
    python3
      >>> from ft_package import count_in_list
      >>> print(count_in_list(["toto","tata","toto"], "toto"))  # 2
      >>> print(count_in_list(["toto","tata","toto"], "tutu"))  # 0

6/ Vérification :
    pip list | grep ft_package
    pip show ft_package

Ce package est maintenant installable et utilisable comme un vrai module pip ✅
"""

setup(
    name="ft_package",
    version="0.0.1",
    author="clara",
    author_email="clara@student.42.fr",
    description="A simple example package with a count_in_list function",
    packages=find_packages(),
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
