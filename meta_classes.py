import pprint
import inspect

import classes
from classes import Model

import resources

def is_model(cls):
    return issubclass(cls, Model)

def is_abstract(cls):
    """A model is abstract when it's Meta class has abstract==True"""
    if hasattr(cls, 'Meta') and hasattr(cls.Meta, 'abstract'):
        return cls.Meta.abstract
    else:
        return False

def yield_module_classes(module):
    for cls_name in dir(module):
        if not cls_name.startswith('_'):
            yield getattr(module, cls_name)

def make_resource(cls):
    
    class _cls_Resource(resources.ModelResource):
        
##        make_resource.__class__.__name__ = __name__
        model = cls
##
##        def __str__(self):
##            return self.__class_name+'()'

    _class_name = '{name}Resource'.format(name=cls.__name__)
    _cls_Resource.__name__ = _class_name
    
    for attr in dir(cls):
        print attr
    return _cls_Resource

if __name__ == '__main__':
    a = list(yield_module_classes(classes))
    b = a[0]
    c = a[-1]()
    
    for cls in a:
        obj = cls()
        print (is_model(cls), is_abstract(cls), cls, cls.__name__, 
               obj.__class__.__name__, type(obj).__name__)

    e = a[-1]
    d = make_resource(e)
    print d, issubclass(d, resources.Resource), d()

    pass
