# Scraping Service With Python

This project is a scraping service written in Python. It provides a set of functions and utilities to scrape data from websites and extract relevant information. The project includes a requirement.txt file that lists the required dependencies to run the scraping service.

## Installation

Install Project
Clone the repository:

```bash
  git clone https://github.com/Medicify/scraping-service.git
```

Import the .sql to mysql database

### Navigate to the project directory:

```bash
 cd scraping-service
```

### Create a virtual environment (optional but recommended):

```bash
 python -m venv venv
```

### Activate the virtual environment:

- On Windows

```bash
 venv\Scripts\activate

```

- On macOS and Linux:

```bash
source venv/bin/activate

```

### Install the project dependencies:

```bash
 pip install -r requirements.txt

```

### Start scraping

```bash
 python main.py

```

### deploy to cloud function

```bash
ADD: def main(request): #like this, because cloud function need to pass request argument to entry point function

REMOVE:
if __name__=="__main__":
    main()
# cloud function has own runtime

```

## Documentation

[Documentation](https://www.python.org/doc/)

## Cloud Computing Team C23-PS135

Bangkit Academy 2023 batch 1
