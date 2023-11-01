from ifield import ICommonField
from faker import Faker
from random import randint

fake_en = Faker()


class IncrementalField(ICommonField):

    def __init__(self, name, blank=0, format_fn=None, start=1, step=1):
        super().__init__(name, blank, format_fn)
        self.start = start
        self.step = step
        self.current = start - step

    @property
    def value(self):
        self.current = self.current + self.step
        return self.format_value(self.current)


class FirstNameField(ICommonField):

    def __init__(self, name, blank=0, format_fn=None):
        super().__init__(name, blank, format_fn)

    @property
    def value(self):
        return self.format_value(fake_en.first_name)


class LastNameField(ICommonField):

    def __init__(self, name, blank=0, format_fn=None):
        super().__init__(name, blank, format_fn)

    @property
    def value(self):
        return self.format_value(fake_en.last_name)


class FullNameField(ICommonField):

    def __init__(self, name, blank=0, format_fn=None):
        super().__init__(name, blank, format_fn)

    @property
    def value(self):
        return self.format_value(fake_en.first_name + ' ' + fake_en.last_name)


class AvatarField(ICommonField):

    def __init__(self, name, blank=0, format_fn=None):
        super().__init__(name, blank, format_fn)

    @property
    def value(self):
        return self.format_value(fake_en.image_url())


class NumberField(ICommonField):

    def __init__(self, name, blank=0, format_fn=None, minimum=0, maximum=100, decimal=0):
        super().__init__(name, blank, format_fn)
        self.min = minimum
        self.max = maximum
        self.decimal = decimal

    @property
    def value(self):
        return self.format_value(randint(self.min, self.max))

# num = NumberField("number")
# for _ in range(10):
#     print(num.value)
