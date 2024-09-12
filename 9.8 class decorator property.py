class Person:
    first_name = property()

    @first_name.getter
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expect a string')
        self._first_name = value


person = Person()
person.first_name = 'li'
print(person.first_name)