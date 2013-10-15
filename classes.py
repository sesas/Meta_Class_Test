

class Model():

    def __str__(self):
        return 'Model()'
    
    class Meta:
        abstract = True
    pass

class Field():
    def __str__(self):
        return 'Field()'
    
    class Meta:
        abstract = True
    pass

class CharField(Field):
    
    def __str__(self):
        return 'CharField()'
    pass

class SomeModel(Model):
    
    def __str__(self):
        return 'SomeModel()'
    pass


if __name__ == '__main__':
    print Model()
    print Field()
    print CharField()
    print SomeModel()
