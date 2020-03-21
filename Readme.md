# Flat scraper

Flat scraper is a Python program used for collecting, storing and presenting data from flat offers.

Program contains HTTP scraper for collecting data from Otodom and Gumtree pages based on author preferences.
Collected data is stored in MongoDB in two separate collections. Flask app is used for representing stored
flat offer data.

![screenshot](https://github.com/szoz/flat-scraper/raw/master/example.jpg "Card screenshot")

## Installation

Use the package manager [pipenv](https://pipenv.pypa.io/en/stable/) to install dependencies.

```bash
pipenv install
```

## Usage

### Collect data

```bash
pipenv run python main.py
```

### Present data

```bash
pipenv run python app.py
```





## License
[MIT](https://choosealicense.com/licenses/mit/)