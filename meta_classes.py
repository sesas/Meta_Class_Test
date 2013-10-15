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
            yield cls_name, getattr(module, cls_name)

def make_resource(cls_name, cls):
    class _cls_Resource(resources.ModelResource):
        __name__ = '{name}Resource'.format(name=cls_name)
        make_resource.__class__.__name__ = __name__
        model = cls

    return _cls_Resource

if __name__ == '__main__':
    a = list(yield_module_classes(classes))
    b = a[0]
    c = a[-1][1]()
    
    for cls_name, cls in a:
        obj = cls()
        print (is_model(cls), is_abstract(cls), cls,
               obj.__class__.__name__, type(obj).__name__)

    d = make_resource(*b)
    print d, issubclass(d, resources.Resource)

    pass
