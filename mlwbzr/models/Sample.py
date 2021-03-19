class Sample():
    def __init__(self, **kwargs): 
        for key in kwargs:
            setattr(self, key, kwargs[key]) 
    
    @staticmethod
    def fromjson(data):
        return Sample(**data[-1])

    @staticmethod
    def fromjsonlist(data):
        samples = []
        for d in data:
            samples.append(Sample(**d))
        return samples
