A minimalistic python program that tracks cryptocurrency prices
across some exchanges and compare them in order to find arbitrage
opportunities.

# Setup
```
pip install -r requirement.text
```
(Runs on Python 3)

# Usage

## Data Collection
Each time the `main.py` script is called, all the exchanges registered
in the app are queried and the results are saved in a plain-text data base.
A different file is associated to each particular exchange-market-order
type combination.

You might want to set up a cron job to do this regularly, eg.:
```
0 10 * * *  /usr/bin/python path/to/main.py  # runs once a day at 10am
```

## Finding Arbitrage Opportunities

Simply run `arbtunities.py` to check for current arbitrage opportunities.

# Testing API connection
Api wrappers can be tested by simply:
```
pytest
```
# TODO
- Write a script to analyze historical arbitrage opportunities
- Migrate data to SQLite or similar
