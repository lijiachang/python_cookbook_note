import types


def __init__(self, name, shares, price):
    self.name = name
    self.shares = shares
    self.price = price


def cost(self):
    return self.shares * self.price


cls_dict = {
    '__init__': __init__,
    'cost': cost
}


class Base:
    pass


Spam = types.new_class('Spam', (Base,), {'debut': True, 'type_check': True}, lambda ns: ns.update(cls_dict))
