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
    """
    Klasse for å lage scene-objekter.
    
    Parametre:
        tekst (str): Scenebeskrivelse
        valg (list): En liste så mange todimensjonelle ordbøker som det er 
    """
    def __init__(self, tekst:str, valg:list):
        """Konstruktør"""
        self._tekst = tekst
        self._valg = valg
    
    def start_scene(self):
        """
        Metode som viser spilleren beskrivelsen for denne scenen, spør spiller om valg og endrer gull, liv eller angst om oppgitt i utfallet for scenen.
        """
        print(self._tekst)
        
        # For-løkke som vil vise spilleren valgene for scenen.
        n = 1
        for valg in self._valg:
            print("\n" + f"Valg {n}: {valg["tekst"]}")
            n += 1
        
        # Spiller må velge tall som tilsvarer ett av valgene til scenen. 
        # Tar valgt minus 1 for å få en fungerende indeks.
        valgt = int(input("\n" + f"Hva gjør du? (heltall 1-{(n-1)}): ")) - 1
        
        # Utfallet tilhørende spillerens valg.
        utfall = self._valg[valgt]["utfall"]
        
        # Skriver ut tekstresultat for utfallet.
        print(utfall["tekst"] + "\n")

        # Om ulike verdier ikke er None i den todimensjonelle ordboken som spiller valgte.
        # Dette gjelder altså gull, liv og angst.
        
        if utfall["gull"]:
            # Oppdaterer ridderens (spillerens) gull med utfall fra scene som parameter.
            ridder.oppdater_gull(utfall["gull"])   
            
        if utfall["liv"]:
            # Oppdaterer ridderens (spillerens) liv med utfall fra scene som parameter.
            ridder.oppdater_liv(utfall["liv"])

        if utfall["angst"]:
            # Oppdaterer ridderens (spillerens) angst med utfall fra scene som parameter.
            ridder.oppdater_angst(utfall["angst"])  
     
class Vaapen:
    def __init__(self, navn:str, skade:int):
        self._navn = navn
        self._skade = skade
    
    def __str__(self):
        print("Våpen:", self._navn)
        print("Skade:", self._skade)

ridder = Spiller(100, 0, 10, ["gammelt sverd"], "gammelt sverd")

# Et scene-objekt består av en scenebeskrivelse først, så kommer en liste med en eller flere todimensjonale ordbøker som inneholder spillerens valgmuligheter.
scene1 = Scene(
    "Du går langs den knasende grusveien og går rundt det høye fjellets hjørne. Å nei! Rundt hjørnet og inn i en fjellsprekk ser du en kræsjet vogn, det skinner av gull og du hører en kvinne rope etter hjelp.",
    [
        {
        "tekst": "Redd kvinnen som sitter fast i vognen.", 
        "utfall": {
            "tekst": "Du hjelper kvinnen ut fra vognens vrak. Hun er veldig takknemlig for at du reddet henne og kommer til å huske det for alltid. Hun gir deg snap'en sin og 250 gull.", 
            "gull":250,
            "liv": None,
            "angst": None
            }
        },
        {
        "tekst": "Ta gullet som ligger der, lett tilgjengelig (1000).", 
        "utfall": {
            "tekst": "Du tar plukker opp gull rundt omkring med lyden av en skrikende kvinne som ser på deg, hun kommer til å huske fjeset ditt. Du blir ferdig med plukkingen og har nå 1000 gull.",
            "gull": 1000,
            "liv": None,
            "angst": None
            }
        }
    ]
)

scene2 = Scene(
    "Du går til bygda for å fullføre ditt oppdrag du fikk fra den allmektige kongen i bygda møter du en røver han kommer bort til deg med en kniv og sier 'gi meg 200 gull!'.",
    [
        {
        "tekst": "Overgi gullet ditt.", 
        "utfall": {
            "tekst": "Du mistet 200 gull og røveren stakk avgårde (-200 gull).",
            "gull": -200,
            "liv": None,
            "angst": None
            }
        },
        {
        "tekst": "Slåss mot røveren med ditt gamle sverd.", 
        "utfall": {
            "tekst": "Du mistet 25 liv, men du klarte å drepe ham (-25 liv).",
            "gull": None,
            "liv": -25,
            "angst": None
            }
        }
    ]
)

scene3 = Scene(
    "Du har hentet alt du trenger fra bygda og er på vei ut, ved porten står en gåtemester. Han sier før du kan gå ut må du svare på mine gåter. Hva blir våtere jo mer den tørker?",
    [
        {
           "tekst": "Håndkle.",
           "utfall": {
               "tekst": "Du svarte riktig. Derfor ble du glad og fikk slippe ut gjennom porten.",
                "gull": None,
                "liv": -25,
                "angst": None
           },
        },
        {
           "tekst": "Vann.",
           "utfall": {
                "tekst": "Du svarte feil og ble flau. Derfor fikk du mer angst (+20 angst).",
                "gull": None,
                "liv": None,
                "angst": 20,
            }
        }
    ]
)

scene1.start_scene()
scene2.start_scene()
scene3.start_scene()
