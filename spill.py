class Menneske: 
    """
    Klasse for å lage menneske-objekt.
    
    Parametere:
    liv (int): Menneskets livspoeng.
    angst (int): Menneskets angstpoeng.
    aktivt_vaapen (str): Menneskets aktive våpen.
    """
   def __init__(self, liv:int, angst:int, aktivt_vaapen):
        self._liv = liv 
        self._angst = angst 
        self._aktivt_vaapen = aktivt_vaapen 

   def __str__(self): 
        return f"Liv er {self._liv}, angst er {self._angst} og aktivt våpen er {self._aktivt_vaapen}."

   def angrip(self, person, skade:int,): 
        person._liv -= skade

class Spiller(Menneske): 
        """
        Klasse for å lage spiller-objekt.
        """
        def __init__(self, liv:int, angst:int, gull:int, sekk:list, aktivt_vaapen):
            super().__init__(liv, angst, aktivt_vaapen)
            self._sekk = sekk
            self._gull = gull 
         
        def __str__(self): 
              return f"Liv er {self._liv}, angst er {self._angst} gull er {self._gull}. Aktivt våpen er {self._aktivt_vaapen}."

        def oppdater_gull(self, gull):
            self._gull += gull
            
        def oppdater_liv(self, liv):
            self._liv += liv

        def oppdater_angst(self, angst):
            self._angst += angst

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
    """
    Klasse for å lage våpen-objekt
    """
    def __init__(self, navn:str, skade:int):
        self._navn = navn
        self._skade = skade
    
    def __str__(self):
        print(f"Våpen: {self._navn}, skade: {self._skade}")

# Våpen-objekter
gammelt_sverd = Vaapen("gammelt sverd", 20)
liten_kniv = Vaapen("liten kniv", 10)

# Menneske-objekter og spiller-objekt
ridder = Spiller(100, 0, 10, [gammelt_sverd], gammelt_sverd)
rover = Menneske(50, 0, liten_kniv)
gaatemester = Menneske(75, 0, "ingeting")

print(ridder)
print(gammelt_sverd)

print(rover)
print(liten_kniv)

print(gaatemester)