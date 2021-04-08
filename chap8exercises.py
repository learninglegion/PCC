#8.1
# def display_message():
#     """Print one sentence about the material."""
#     print("I'm learning about functions. They're neat.")
# display_message()

#8.2
# def favorite_book(title):
#     """Print the title of one of my favorite books."""
#     print(f"One of my favorite books is {title.title()}.")
# favorite_book('the wastelands')

#8.3
# def make_shirt(size, text):
#     """Get parameters for a shirt to make."""
#     print(f"Ayo we need a {size} shirt with '{text.title()}' on it ASAP!")
# #make_shirt('medium', 'you can certainly try.')
# make_shirt(size='medium', text='you can certainly try.')

#8.4
# def make_shirt(size='large', text='I love Python.'):
#     """Get parameters for a shirt to make."""
#     print(f"Ayo we need a {size} shirt with '{text}' on it ASAP!")
# make_shirt()
# make_shirt(size='medium', text='You can certainly try.')

#8.5
# def describe_city(name, country='china'):
#     """List the name of a city and the country it's in."""
#     if country == 'usa' or country == 'united states':
#         print(f"{name.title()} is a city in the {country.title()}.")
#     else:
#         print(f"{name.title()} is a city in {country.title()}.")
# describe_city('beijing')
# describe_city(name='detroit', country='united states')
# describe_city(country='brazil', name='Rio')

#8.6
# def city_country(city, country):
#     """Write a city and country."""
#     location = f"{city}, {country}"
#     return location.title()
# print(city_country('evansville', 'USA'))
# place = city_country('indianapolis', 'USA')
# print(place)
# place = city_country('vincennes', 'USA')
# print(place)

#8.7
# def make_album(name, album):
#     """Describe a music album."""
#     record = {'artist_name': name.title(), 'artist_album': album.title()}
#     return record
# mjk = make_album('tool', 'lateralis')
# bh = make_album('a perfect circle', '13th step')
# tr = make_album('nin', 'broken')
# print(mjk)
# print(bh)
# print(tr)

#8.8
def make_album(name, album):
    """Describe a music album."""
    record = {'artist_name': name.title(), 'artist_album': album.title()}
    return record
while True:
    print("\nName some of your favorite musical artists and albums.")
    print("(Type 'q' to quit entering info.)\n")
    given_name = input("First, give me the name of a band or artist: ")
    if given_name == 'q':
        break
    given_album = input("Now give me the name of one of their albums: ")
    if given_album == 'q':
        break
    cd = make_album(given_name, given_album)
    print(cd)
    
