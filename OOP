class bateau:
    
    mat=1
    giletDeSauvetage=2
    matelot=5
    nourriture=True

    def securite(self):
        if self.matelot>self.giletDeSauvetage:
            print("danger")
        else:
            print("Sécurité assurée")

    def Provisions(self):
        if self.nourriture==True:
            print("Encore des réserves")
        
    def __init__(self):
        self.nom=None

class Multicoque(bateau):

    coques=3
    safran=2
    
    def __init__(self):
        self.nom = "Trimaran"
    
    def Nom(self):
        print(self.nom)


class Monocoque(bateau):

    derive=1
    voile=3
    surfaceParVoile=10
    
    def SurfaceVoile(self):
        return self.voile*self.surfaceParVoile
    
    def vitesseBateau(self):
        surfaceVoile=self.SurfaceVoile()
        return surfaceVoile*1.5





