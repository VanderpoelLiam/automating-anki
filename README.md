# automating_anki
Anki flashcard generation

## Prerequisites
Install [pipx](https://github.com/pypa/pipx):
```
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```

Install [Poetry](https://python-poetry.org/)
```
pipx install poetry
```

Install [pyenv](https://github.com/pyenv/pyenv):
```
curl https://pyenv.run | bash
```

## Installation
Setup the Python 3.10.12 environment with:
```
pyenv install 3.10.12
pyenv virtualenv 3.10.12 automating_anki
pyenv local automating_anki
```

Setup Poetry:
```
poetry install
```

Install pre-commit
```
poetry run pre-commit install
```

## Usage
To run the flashcard creation tool, run:
```
poetry run main
```

TODO: Explain that need to have anki install on the machine and running before can run the tool. Also that you need to install AnkiConnect anki addon.
