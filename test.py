class Foo:
    def __init__(self, value):
        self.v1 = value
        
class Bar:
    def __init__(self, value):
        self.v2 = value
        # Contains a reference to Baz!
        self.baz = Baz(3)
        
class Baz:
    def __init__(self, value):
        self.v3 = value
    
class FBB:
    def __init__(self):
        self.v = 0
        self.foo = Foo(1)
        self.bar = Bar(2)
        
def full_vars(obj):
    return {k: full_vars(v) if hasattr(v, '__dict__') else v for k, v in vars(obj).items()}
        
fbb = FBB()
print(full_vars(fbb))
