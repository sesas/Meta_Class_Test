import inspect

import classes
from classes import Model

def is_model(cls):
    return issubclass(cls, Model)

def is_abstract(cls):
    """A model is abstract when it's Meta class has abstract==True"""
    if hasattr(cls, 'Meta') and hasattr(cls.Meta, 'abstract'):
        return cls.Meta.abstract
    else:
        return False

def yield_module_classes(module):
    for classes in dir(module):
        if not classes.startswith('_'):
            yield getattr(module, classes)

if __name__ == '__main__':
    a = list(yield_module_classes(classes))
    b = a[0]

    for cls in a:
        print is_model(cls), is_abstract(cls), cls
    pass
