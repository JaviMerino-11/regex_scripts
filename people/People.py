import re


class People(object):
    def __init__(self):
        self.name = input('Introduce the name: ')
        self.first_surname = input('Introduce the first surname: ')
        self.last_surname = input('Introduce the last surname: ')

    def show_profile(self):
        search_name = '^\D[A-Z\sa-z]+$'
        search_first_surname = '^\D[A-Z\sa-z]+$'
        search_last_surname = '^\D([A-Z\sa-z]+)${0,1}'

        if re.search(search_name, self.name) is not None and re.search(search_first_surname,
                                                                       self.first_surname) is not None or re.search(
            search_last_surname, self.last_surname) is '':
            print('\nName: %s\nSurname: %s %s' % (self.name, self.first_surname, self.last_surname))
        else:
            print('\nFormate not allowed')
