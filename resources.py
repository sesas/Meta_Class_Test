
class Resource(object):
    def __str__(self):
        return 'Resource()'
    
    class Meta:
        pass

class ModelResource(Resource):
    def __str__(self):
        return "ModelResource()"

if __name__ == '__main__':
    print Resource()
    print ModelResource()
