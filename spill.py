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

class Scene:
    def __init__(self, tekst:str, valg:list):
        self._tekst = tekst
        self._valg = valg
    
    def start_scene(self):
        print(self._tekst)
        
        n = 1
        
        for valg in self._valg:
            print(f"Valg {n}: {valg}")
            n += 1
            
        valgt = input(f"Hva gjør du? (tall fra 1-{(n-1)}): ")

class Vaapen:
    def __init__(self, navn:str, skade:int):
        self._navn = navn
        self._skade = skade
    
    def __str__(self):
        print("Våpen:", self._navn)
        print("Skade:", self._skade)

ridder = Spiller(100, 0, 10, ["gammelt sverd"], "gammelt sverd")
print(ridder)
