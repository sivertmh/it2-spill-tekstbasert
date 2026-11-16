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
