class Transform:

    def __init__(self, **kwargs):
        
        if "translation" in kwargs:
            self.translation = kwargs["translation"]
        else:
            self.translation = (0, 0)
            
        self.rotation = 0
        self.scale = (1, 1)

NullTransform = Transform()
