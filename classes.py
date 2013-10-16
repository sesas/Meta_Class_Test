
class OtherRandomClass(object):
    def __str__(self):
        return 'OtherRandomClass()'
        
class OtherRandomClassAbstract(object):
    def __str__(self):
        return 'OtherRandomClassAbstract()'
    
    class Meta:
        abstract = True
    pass

class Model(object):

    def __str__(self):
        return 'Model()'
    
    class Meta:
        abstract = False
    pass

class Field(object):
    def __init__(self, *args, **kwargs):
        super(Field, self).__init__()

    def __str__(self):
        return 'Field()'
    
    class Meta:
        abstract = False
    pass

class CharField(Field):

    def __init__(self, *args, **kwargs):
        super(CharField, self).__init__(*args, **kwargs)
    
    def __str__(self):
        return 'CharField()'
    pass

class ForeignKey(Field):
    def __init__(self, *args, **kwargs):
        super(ForeignKey, self).__init__(*args, **kwargs)
    
    def __str__(self):
        return 'ForeignKey()'
    pass

class SomeModel(Model):
    field_name = CharField(max_length=100)
    field_name2 = ForeignKey(Model, related_name='related_name')
    
    def __str__(self):
        return 'SomeModel()'
    pass


if __name__ == '__main__':
    print Model()
    print Field()
    print CharField()
    print SomeModel()
    print OtherRandomClass()
    print OtherRandomClassAbstract()
    print ForeignKey()
