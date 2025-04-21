
class Garbage(object):
    # Singleton instances
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Garbage, cls).__new__(cls)
        return cls.instance
    
    def __str__(self):
        return "###Garbage###"
    
    def __repr__(self):
        return "Garbage()"