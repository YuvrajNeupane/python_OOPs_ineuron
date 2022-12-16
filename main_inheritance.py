class car:
    def __init__(self, body, engin, tyre):
        self.body = body
        self.engin = engin
        self.tyre = tyre

    def milage(self):
        print('milage og this car.')

c = car('solid', 'v6', 'radial')
print(c)
print(c.body, c.engin, c.tyre )

class tata(car):
    pass 

t = tata('soft', 'v7', 'radial1')
print(t.body, t.engin, t.tyre)
print(t.milage())