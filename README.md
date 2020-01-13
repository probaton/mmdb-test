# The Mock Movie Database Test Suite
This project consists of two parts. One is an exceedingly simple REST API for the Mock Movie Database, a fictional competitor to IMDb.com. The other is an API test suite for that same API. 

## Requirements
- Python 3 (and matching Pip version)
- Bash
- A Linux environment (there is a very real chance it will work just fine on Mac, but that has not been tested)

## Getting Started
### Setting up the virtual environment
To ensure a consistent development environment, start a new virtual environment with `virtualenv`.

First, install `virtualenv`.
```
sudo pip install virtualenv
```
Initiate a new environment in the home directory of this project
```
virtualenv -p python3 venv
```
Activate the virtual environment
```
source venv/bin/activate
```

### Starting the API
Install dependencies
```
pip install -r api/requirements.txt
```
Run the API
```
python api/mmdb.py
```

