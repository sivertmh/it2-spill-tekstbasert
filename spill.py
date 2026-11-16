class Menneske: 
   def __init__(self, liv:int, angst:int, aktivt_vaapen:str):
      self._liv = liv 
      self._angst = angst 
      self._aktivt_vaapen = aktivt_vaapen 

   def __str__(self): 
     return f"liv er {self._liv}, angst er {self._angst}"

   def angrep(self, person, skade:int,): 
       person._liv -= skade 
     


class Spiller(Menneske): 
        def __init__(self, liv:int, angst:int, gull:int, sekk:list, aktivt_vaapen:str):
         super().__init__(liv, angst, aktivt_vaapen)
         self._sekk = sekk
         self._gull = gull 
         
        def __str__(self): 
              return f"liv er {self._liv}, angst er {self._angst} gull er {self._gull}"

        def oppdater_gull(self, gull):
            self._gull += gull 

         
    
        

        def bytt_vaapen(self, vaapen):
         self._aktivt_vaapen = vaapen 
           
ridder = Spiller(100, 0, 10, ["gammelt sverd"], "gammelt sverd")
print(ridder)