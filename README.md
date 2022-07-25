# domino
W celu uruchomienia programu należy wywołać plik `domino.py`.

Następnie należy postępować zgodnie z komunikatami wyświetlanymi w konsoli.

Aby uruchomić testy należy skonfigurować środowisko wirtualne. W tym celu należy w folderze z projektem skorzystać z następujących poleceń:

`pip install virtualenv`

`python -m venv env`

`env\Scripts\activate`

`pip install pytest`

Następnie w celu przetestowania algorytmu należy skorzystać z polecenia:

`python -m pytest tests/test_algorithm.py`

Aby przetestować odwrócony algorytm należy użyć polecenia:

`python -m pytest tests/test_inverted_algorithm.py`


