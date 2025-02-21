# commondata-countries

Work with [ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1) [alpha2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2), [alpha3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) and [numeric](https://en.wikipedia.org/wiki/ISO_3166-1_numeric) standard country data

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
