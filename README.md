# commondata-countries

A Python package for managing country data.

## Installation

```bash
pip install commondata-countries
```

## Usage

**Iterate over all countries:**

```python
from commondata_countries import CountryData

countries = CountryData()

for country in countries:
    print(country.name)
```

**List all countries:**

```python
from commondata_countries import CountryData

countries = CountryData()

print(countries.all())
```

**Lookup a country**

```python
from commondata_countries import CountryData

countries = CountryData()

# Lookup by name (case insensitive, fuzzy search)
country = countries["Untied States of America"]

# Lookup by ISO Alpha-2
country = countries["US"]

# Lookup by ISO Alpha-3
country = countries["USA"]

# Lookup by ISO Numeric
country = countries[840]

print(country)
> Country(name='United States of America', iso_alpha2='US', iso_alpha3='USA', iso_numeric=840)
```
