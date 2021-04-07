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
def describe_city(name, country='china'):
    """List the name of a city and the country it's in."""
    if country == 'usa' or country == 'united states':
        print(f"{name.title()} is a city in the {country.title()}.")
    else:
        print(f"{name.title()} is a city in {country.title()}.")
describe_city('beijing')
describe_city(name='detroit', country='united states')
describe_city(country='brazil', name='Rio')
