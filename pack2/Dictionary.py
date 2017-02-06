# -*-coding:Latin-1 -*

class Dictionary:
    
    
    def __init__(self, *dictionnary, **data):
        self.keys = []
        self.map = {}
        dictionnary = list(dictionnary)
        if len(dictionnary) >0:
            self.keys = list(dictionnary[0].keys)
            self.map = dict(dictionnary[0].map)
        if len(data) > 0:
            for (key, value) in data.items():
                self.add(key, value)
        
       
    def get(self, key):
        return self.map.get(key)
     
    def add(self, key, value):
        
        if not key in self.map:
            self.keys.insert(len(self.keys),key)
            
        self.map[key] = value
        
    def remove(self, key):
        if key in self.map:
            del(self.map[key])
            self.keys.remove(key)
            
    def __repr__(self):
        return "\t" + str(self.keys) + ";\n\t " + str(self.map)
       
    def __getitem__(self, item):
        if item in self.map:
            return self.map[item]
        return None
    
    def __setitem__(self, key, value):
        self.add(key, value)
    
    def __delitem__(self, item):
        self.remove(item)
        
    def __contains__(self, item):
        return item in self.keys
    
    def __len__(self):
        return len(self.keys)
    
    def sort(self, **parameters):
        if len(parameters) > 0:
            self.keys.sort(**parameters)
        else:
            self.keys.sort()
            
    def sorted(self, **parameters):
        res = Dictionary(self)
        if len(parameters) > 0:
            res.keys.sort(**parameters)
        else:
            res.keys.sort()
        return res
    
    def reverse(self):
        newKey=[]
        for i in range(len(self.keys), 0, -1):
            newKey.append(self.keys[i-1])
        self.keys = newKey
            
    def getKeys(self):
        return self.keys
    
    def values(self):
        return self.map.values()
    
    def __iter__(self):
        return DictionnaryIter(self)
    
    def items(self):
        for key in self.keys:
            yield (key, self.map.get(key))
            
    def __add__(self, dico):
        res = Dictionary(self)
        for key, value in dico.items():
            res.add(key, value)
        return res
    
class DictionnaryIter:
    
    def __init__(self, dico):
        self.listeToProvide = dico.keys
        self.position = 0
        
    def __next__(self):
        if self.position == len(self.listeToProvide):
            raise StopIteration
        self.position +=1
        return self.listeToProvide[self.position -1]
    
    
  #     __getitem__, __setitem__ et __delitem__
 #   def __str__(self): 
 #       return "{'keys': " + str(self.keys) + " 'map': " + str(self.map)
 
