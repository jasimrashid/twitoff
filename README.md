# Twitoff

## Installation

Download the repo and navigate there from the command line:

``` sh
git clone https://github.com/jasimrashid/twitoff.git
cd twitoff

```

## Setup
```sh
pipenv install
pipenv shell
```

Setup the database:
```
# Windows users can omit the "FLASK_APP=web_app" part...

FLASK_APP=web_app flask db init #> generates app/migrations dir

# run both when changing the schema:
FLASK_APP=web_app flask db migrate #> creates the db (with "alembic_version" table)
FLASK_APP=web_app flask db upgrade #> creates the specified tables
```

## Usage

Setup and activate a virtual environment
```sh
FLASK_APP=web_app flask run
```