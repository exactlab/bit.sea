class Layer():
    def __init__(self,top, bottom):
        self.top = top
        self.bottom = bottom
    def __str__(self):
        return "Layer %d-%d m" %(self.top, self.bottom)

class matchup():
    def __init__(self,Model,Ref):
        self.Model = Model
        self.Ref   = Ref
        
    def correlation(self):
        return self.Model +1
    def rms(self):
        return self.Ref + 1


class FloatMatchup(matchup):
    def __init__(self, Model=None, Ref=None, Depth=None, Lon=None, Lat=None):        
        if Model is None:
            self.Model = np.array([],np.float32)
            self.Ref   = np.array([],np.float32)
            self.Depth = np.array([],np.float32)
            self.Lon   = np.array([],np.float32)
            self.Lat   = np.array([],np.float32)
        else:
            self.Model = Model
            self.Ref   = Ref
            self.Depth = Depth
            self.Lon   = Lon
            self.Lat   = Lat
        
    def subset(self,layer):
        ii = (self.Depth <= layer.bottom) & (self.Depth >= layer.top)        
        return FloatMatchup(self.Model[ii], self.Ref[ii], self.Depth[ii], self.Lon[ii], self.Lat[ii])

    
    def extend(self,fm):
        self.Model = np.concatenate((self.Model, fm.Model))
        self.Ref   = np.concatenate((self.Ref,   fm.Ref))
        self.Depth = np.concatenate((self.Depth, fm.Ref))
        self.Lon   = np.concatenate((self.Lon,   fm.Lon))
        self.Lat   = np.concatenate((self.Lat,   fm.Lat))

class SingleFloatMatchup():
    def __init__(self, Model, Ref, Depth, biofloatObj):
        self.Model = Model
        self.Ref   = Ref
        self.Depth = Depth
        self.Float = biofloatObj
        self.Lon   = np.ones_like(Model)*self.Float.lon
        self.Lat   = np.ones_like(Model)*self.Float.lat
        
    def plot(self):
        return 1

            

if __name__ == '__main__':
    import numpy as np
    Depth = np.arange(10.)/10
    a=FloatMatchup(np.arange(10),np.arange(10)+1,Depth,Depth,Depth  )
    L=Layer(0.3, 0.8)
    b = a.subset(L)