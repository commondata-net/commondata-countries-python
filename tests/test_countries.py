import pytest

from commondata_countries import Country, CountryData


@pytest.fixture
def country_data():
    return CountryData()


def test_list_all_countries(country_data):
    countries = country_data.all()
    assert isinstance(countries, list)
    assert len(countries) > 0
    assert isinstance(countries[0], Country)


def test_lookup_by_iso_alpha2(country_data):
    country = country_data["US"]
    assert country.name == "United States of America"
    assert country.iso_alpha2 == "US"


def test_lookup_by_iso_alpha3(country_data):
    country = country_data["CAN"]
    assert country.name == "Canada"
    assert country.iso_alpha3 == "CAN"


def test_lookup_by_iso_numeric(country_data):
    country = country_data["124"]
    assert country.name == "Canada"
    assert country.iso_numeric == 124


def test_lookup_by_iso_numeric_int(country_data):
    country = country_data[124]
    assert country.name == "Canada"
    assert country.iso_numeric == 124


def test_lookup_by_name(country_data):
    country = country_data["Mexico"]
    assert country.iso_alpha2 == "MX"


def test_fuzzy_lookup(country_data):
    country = country_data["Untied America"]
    assert country.name == "United States of America"


def test_iterate_countries(country_data):
    countries = list(country_data)
    assert len(countries) == len(country_data.all())
    assert isinstance(countries[0], Country)


def test_repr_country(country_data):
    country = country_data["United States of America"]
    assert (
        str(country)
        == "Country(name='United States of America', iso_alpha2='US', iso_alpha3='USA', iso_numeric=840)"
    )


def test_invalid_lookup(country_data):
    with pytest.raises(KeyError):
        country_data["UnknownCountry"]
