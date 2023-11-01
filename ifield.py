from abc import ABC, abstractmethod


class ICommonField(ABC):

    def __init__(self, name, blank=0, format_fn=None):
        self.name = name
        self.blank = blank
        self.format = format_fn

    @property
    @abstractmethod
    def value(self):
        pass

    def format_value(self, value):
        if self.format:
            formatter = eval(self.format)
            return formatter(value)
        return value
