                                #### LUXURY WATCHES EXAMPLE - CLASS/STATIC METHODS ####

class Watch:
    __watches_created = 0

    def __init__(self):
        Watch.__watches_created += 1
        self.engraving = ''

    # engraving rules
    #it should not be longer than 40 characters;
    #it should consist of alphanumerical characters, so no space characters are allowed;
    #if the text does not comply with restrictions, an exception should be raised;

    @classmethod
    def with_engraving(cls, txt):
        print('Alternative constructor called...')
        if Watch.validate_engraving(txt):
            _watch = cls()
            _watch.engraving = txt
            return _watch
        else:
            raise Exception('The text does not follow the requirements. Please enter a valid engraving string.')

    @classmethod
    def get_watches_created(cls):
        return f'Watches created: {cls.__watches_created}'

    @staticmethod
    def validate_engraving(txt):
        if len(txt) < 41 and ' ' not in txt:
            return True
        else:
            return False

watches = []
w1 = Watch()
print(Watch.get_watches_created())
w2 = Watch.with_engraving('ILoveYou')
print(Watch.get_watches_created())

