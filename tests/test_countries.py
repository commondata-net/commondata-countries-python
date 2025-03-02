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
    assert country.label == "United States of America"
    assert country.iso_alpha2 == "US"


def test_lookup_by_iso_alpha3(country_data):
    country = country_data["CAN"]
    assert country.label == "Canada"
    assert country.iso_alpha3 == "CAN"


def test_lookup_by_iso_numeric(country_data):
    country = country_data["124"]
    assert country.label == "Canada"
    assert country.iso_numeric == 124


def test_lookup_by_iso_numeric_int(country_data):
    country = country_data[124]
    assert country.label == "Canada"
    assert country.iso_numeric == 124


def test_lookup_by_name(country_data):
    country = country_data["Mexico"]
    assert country.iso_alpha2 == "MX"


def test_fuzzy_lookup(country_data):
    country = country_data["Untied America"]
    assert country.label == "United States of America"


def test_fuzzy_lookup_with_search(country_data):
    countries = country_data.search("States America")
    assert len(countries) > 0
    assert countries[0].label == "United States of America"


def test_synonym_lookup(country_data):
    country = country_data["Untied States"]
    assert country.label == "United States of America"


def test_iterate_countries(country_data):
    countries = list(country_data)
    assert len(countries) == len(country_data.all())
    assert isinstance(countries[0], Country)


def test_repr_country(country_data):
    country = country_data["United States of America"]
    assert (
        str(country)
        == "Country(label='United States of America', iso_alpha2='US', iso_alpha3='USA', iso_numeric=840)"
    )


def test_invalid_lookup(country_data):
    with pytest.raises(KeyError):
        country_data["UnknownCountry"]


def test_deserialize_country(country_data):
    country = country_data["United States of America"]
    assert isinstance(country.to_dict(), dict)
    assert country.to_dict() == {
        "label": "United States of America",
        "iso_alpha2": "US",
        "iso_alpha3": "USA",
        "iso_numeric": 840,
    }


def test_search_countries(country_data):
    countries = country_data.search("united states")
    assert len(countries) > 1
    assert "United States of America" in [c.label for c in countries]
    assert len(countries) == len(set(map(lambda c: c.iso_alpha3, countries)))


def test_get_country(country_data):
    country = country_data.get("US")
    assert country.label == "United States of America"


def test_get_fail(country_data):
    country = country_data.get("UnknownCountry")
    assert country is None


def test_search_fail(country_data):
    countries = country_data.search("UnknownCountry")
    assert len(countries) == 0
