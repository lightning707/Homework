country_dict = {}


def make_country(name, capital):
    country_dict.update({name : capital})
    print(country_dict)


make_country('Ukraine', 'Kyiv')
make_country('France', 'Paris')
