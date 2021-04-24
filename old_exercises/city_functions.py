def city_country(city, country, population=0):
    """Generate a city/country combo"""
    if population:
        city_country = f"{city}, {country} - {population}"
    else:
        city_country = f"{city}, {country}"
    return city_country.title()
