import re


class People(object):
    def __init__(self):
        self.name: str = input('Introduce the name: ')
        self.first_surname: str = input('Introduce the first surname: ')
        self.last_surname: str = input('Introduce the last surname: ')
        self.full_name = self.name + ' ' + self.first_surname + ' ' + self.last_surname

    def show_personal_data(self):
        profile_pattern = re.compile(
            "(?P<name>([A-ZÀ-ÿ][a-z\s]*)+) (?P<first_surname>([A-ZÀ-ÿ][a-z\s]*)+) (?P<last_surname>([A-ZÀ-ÿ][a-z\s]*)?)")

        match_name = re.match(profile_pattern, self.full_name)

        if match_name:
            print('Name: %s\nSurname: %s %s' % (
                match_name.group('name'), match_name.group('first_surname'), match_name.group('last_surname')))
        else:
            print('Formate Not Allowed. Check conditions')
