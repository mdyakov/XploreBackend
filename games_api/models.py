class Game(object):
    def __init__(self, id, name, background_image, released, rating, stores):
        self.name = name
        self.background_image = background_image
        self.released = released
        self.rating = rating
        self.stores = stores


class Store(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name