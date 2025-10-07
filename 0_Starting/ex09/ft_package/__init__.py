# __init__.py

# __init__.py = rend mon dossier importable + contient le code
# setup.py = decrit mon package, dit a pip comment installer mon package
# python3 -m build = construit ton .tar.gz et .whl dans le dossier dist/
# pip install ./dist/... = installe mon package, le rend disponible globalement

from .count import count_in_list

__all__ = ["count_in_list"]
