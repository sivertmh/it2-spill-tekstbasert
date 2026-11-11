class Menneske: 
   def __init__(self, liv:int, angst:int, gull:int):
      self._liv = liv 
      self._angst = angst 
      self._gull = gull 

   def __str__(self): 
     return f"liv er {self._liv}, angst er {self._angst}, gull er {self._gull}"

   def angrep(self, person, skade:int,): 
       person._liv -= skade 
     


   class Spiller: 
        def __init__(self, liv:int, angst:int, gull:int, sekk:list):
         super().__init__(liv, angst, gull)
         self._sekk = sekk 
      

        def status_liv(self):
           return self._liv