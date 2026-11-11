class Scene:
    def __init__(self, tekst:str, valg:list):
        self._tekst = tekst
        self._valg = valg
    
    def start_scene(self):
        print(self._tekst)
        
        n = 1
        
        for valg in self.valg:
            print("Hva gjør du?")
            print(f"Valg {n}: {valg}")
            n += 1

class Vaapen:
    def __init__(self, navn:str, skade:int):
        self._navn = navn
        self._skade = skade

scene1 = Scene(
    "Du går langs den knasende grusveien og går rundt det høye fjellets hjørne. Å nei! Rundt hjørnet og inn i en fjellsprekk ser du en kræsjet vogn, det skinner av gull og du hører en kvinne rope etter hjelp.",
    [
        "Hjelp kvinnen som sitter fast i vognen.",
        "Ta gullet som ligger der, lett tilgjengelig (1000)."
    ]
)