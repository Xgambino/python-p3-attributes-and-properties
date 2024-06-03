APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]


class Dog:
    '''A dog.'''
    species = "Canis lupus familiaries"
    approved_breeds = APPROVED_BREEDS

    def __init__(self, name = None, breed = None):
        '''Create a new dog.'''
        if name is None:
            name = "DefaultName"
        if not isinstance(name, str) or not (1 <= len(name) <= 25):
            print("Name must be string between 1 and 25 characters.")
            self.name = None
        else:
            self.name = name

        if breed and breed not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
            self.breed = None
        elif breed:
            self.breed = breed
        else:
            self.breed = None