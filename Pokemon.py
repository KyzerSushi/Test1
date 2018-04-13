# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 17:21:21 2016

@author: Antoine
"""

import random
import numpy as np

import dresseur as DRE

#Création de la classe pokémon
class Pokemon(object):
    
    def __init__(self,nompokemon="",PV=0,ATK=0,deff=0,spd=0,attaque=[["",0,0,0],["",0,0,0],["",0,0,0],["",0,0,0]],TYpe=0,ko=0):
        self.nompokemon=nompokemon
        self.PV=PV
        self.ATK=ATK
        self.deff=deff
        self.spd=spd
        self.attaque=attaque
        self.TYpe=TYpe
        self.ko=ko
        #On définit les differentes statistiques du pokémon attaque est une liste contenant les 4 attaques connus par le Pokémon.
        #attaque[0] est le nom de l'attaque ,attaque[1] est le dégat de l'attaque ,attaque[2] est la puissance de l'attaque enfin attaque[3] est le type de l'attaque.
        
    def __repr__(self):
        return "{}".format(self.nompokemon)

#On créer la matrice TYPE qui définit les coefficient modificateur pour les types.
ACIER=[0.5,1,1,0.5,0.5,0.5,2,1,1,1,1,1,2,1,1,1,1]
COMBAT=[2,1,1,1,1,1,2,0.5,2,1,0.5,0.5,2,0.5,0,2,0.5]
DRAGON=[0.5,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
EAU=[1,1,0.5,0.5,1,2,1,1,1,0.5,1,1,2,2,1,1,1]
ELECTR=[1,1,0.5,2,0.5,1,1,1,1,0.5,1,1,1,0,1,1,2]
FEU=[2,1,0.5,0.5,1,0.5,2,2,1,2,1,1,0.5,1,1,1,1]
GLACE=[0.5,1,2,0.5,1,0.5,0.5,1,1,2,1,1,1,2,1,1,2]
INSECT=[0.5,0.5,1,1,1,0.5,1,1,1,2,0.5,2,1,1,0.5,2,0.5]
NORMAL=[0.5,1,1,1,1,1,1,1,1,1,1,1,0.5,1,0,1,1]
PLANTE=[0.5,1,0.5,2,1,0.5,1,0.5,1,0.5,0.5,1,2,2,1,1,0.5]
POISON=[0,1,1,1,1,1,1,1,1,2,0.5,1,1,0.5,1,1,1]
PSY=[0.5,2,1,1,1,1,1,1,1,1,2,0.5,1,1,1,0,1]
ROCHE=[0.5,0.5,1,1,1,2,2,2,1,1,1,1,1,0.5,1,1,2]
SOL=[2,1,1,0.5,2,2,1,1,1,0.5,2,1,2,1,1,1,0]
SPECTR=[0.5,1,1,1,1,1,1,1,0,1,1,2,1,1,2,0.5,1]
TENEBR=[0.5,0.5,1,1,1,1,1,1,1,1,1,2,1,1,2,0.5,1]
VOL=[0.5,2,1,1,0.5,1,1,2,1,2,1,1,0.5,1,1,1,1]
TYPE=np.array([ACIER]+[COMBAT]+[DRAGON]+[EAU]+[ELECTR]+[FEU]+[GLACE]+[INSECT]+[NORMAL]+[PLANTE]+[POISON]+[PSY]+[ROCHE]+[SOL]+[SPECTR]+[TENEBR]+[VOL])

#On deffinit le programme KOMBAT qui gère le combat entre 2 pokémons.
def KOMBAT(pok1,pok2,dres1,dres2):
    #On stock les PV des 2 pokemons avec PV1 et PV2 , si les 2 dresseurs impliqués sont des IA ou des humains avec t et T ,c est un conteur de tour et C et en sortie pour deffinir quel pokémon a gagner.
    PV1,PV2,t,T,c,C=pok1.PV,pok2.PV,dres1.Type,dres2.Type,1,0
    #Débute du combat.
    print("Debut du combat !")
    while PV1>0 or PV2>0:
        print("")
        if pok1.spd>=pok2.spd:
            print("Debut du tour "+str(c)+" !")
            print("")
            #Le pokémon 1 est le plus rapide il attaque donc en premier.
            if PV1>0:
                #Le pokémon 1 attaque.
                if t==1 :
                    #Le dresseur est une IA son attaque est donc aléatoire.
                    atk=random.randint(0,3)
                else :
                    #Le dresseur est un humain il choisie donc son attaque.
                    print("Choix de l attaque de "+str(pok1.nompokemon)+" : "+str(pok1.attaque)+" !")
                    print("")
                    atk=input()
                    atk=int(atk)
                    print("")
                    atk=atk-1
                    if atk not in [0,1,2,3]:
                        print("Choix de l attaque "+str(pok1.nompokemon)+" : "+str(pok1.attaque)+" !")
                        print("")
                        atk=input()
                        atk=int(atk)
                        print("")
                        atk=atk-1
                esquive=random.randint(0,100)
                #Le pokémon 2 arrive à esquiver .
                if pok1.attaque[atk][2]<esquive:
                    print(str(pok1.nompokemon)+" utilise "+str(pok1.attaque[atk][0])+" sur "+str(pok2.nompokemon))
                    print(str(pok2.nompokemon)+" esquive l attaque.")
                #Le pokémon 2 n'arrive pas à esquiver.
                else:
                    A=(((42*pok1.ATK*pok1.attaque[atk][1])//(pok2.deff*50))+2)*TYPE[pok1.attaque[atk][3]][pok2.TYpe]
                    print(str(pok1.nompokemon)+" utilise "+str(pok1.attaque[atk][0])+" sur "+str(pok2.nompokemon))
                    critique=random.randint(1,100)
                    if critique<=5 :
                        A=A*2
                        print("C est un CRITIQUE !!!")
                    if TYPE[pok1.attaque[atk][3]][pok2.TYpe]==2 :
                        print("C est super efficace !!!")
                    if TYPE[pok1.attaque[atk][3]][pok2.TYpe]==0 or TYPE[pok1.attaque[atk][3]][pok2.TYpe]==0.5 :
                        print("Ce n est pas tres efficace !!!")
                    PV2=PV2-A
                    if PV2<0:
                        PV2=0
                    print(str(pok2.nompokemon)+" subit "+str(A)+" PV")
                    print(str(pok2.nompokemon)+" passe a "+str(PV2)+" PV")
                    print("")
            else:
                #Le pokémon 1 est mort.
                print(str(pok1.nompokemon)+" est MORT victoire de "+str(pok2.nompokemon)+" !")
                print("")
                print("Fin du combat !")
                C=1
                return C
            if PV2>0:
                #Le pokémon 2 attaque.
                if T==1 :
                    #Le dresseur est une IA son attaque est donc aléatoire.
                    atk=random.randint(0,3)
                else :
                    #Le dresseur est un humain il choisie donc son attaque.
                    print("Choix de l attaque "+str(pok2.nompokemon)+" : "+str(pok2.attaque)+" !")
                    print("")
                    atk=input()
                    atk=int(atk)
                    print("")
                    atk=atk-1
                    if atk not in [0,1,2,3]:
                        print("Choix de l attaque "+str(pok2.nompokemon)+" : "+str(pok2.attaque)+" !")
                        print("")
                        atk=input()
                        atk=int(atk)
                        print("")
                        atk=atk-1
                esquive=random.randint(0,100)
                #Le pokémon 1 arrive à esquiver.
                if pok2.attaque[atk][2]<esquive:
                    print(str(pok2.nompokemon)+" utilise "+str(pok2.attaque[atk][0])+" sur "+str(pok1.nompokemon))
                    print(str(pok1.nompokemon)+" esquive l attaque.")
                #Le pokémon 1 n'arrive pas à esquiver.
                else:
                    A=(((42*pok2.ATK*pok2.attaque[atk][1])//(pok1.deff*50))+2)*TYPE[pok2.attaque[atk][3]][pok1.TYpe]
                    print(str(pok2.nompokemon)+" utilise "+str(pok2.attaque[atk][0])+" sur "+str(pok1.nompokemon))
                    critique=random.randint(1,100)
                    if critique<=5 :
                        A=A*2
                        print("C est un CRITIQUE !!!")
                    if TYPE[pok2.attaque[atk][3]][pok1.TYpe]==2 :
                        print("C est super efficace !!!")
                    if TYPE[pok2.attaque[atk][3]][pok1.TYpe]==0 or TYPE[pok2.attaque[atk][3]][pok1.TYpe]==0.5 :
                        print("Ce n est pas tres efficace !!!")
                    PV1=PV1-A
                    if PV1<0:
                        PV1=0
                    print(str(pok1.nompokemon)+" subit "+str(A)+" PV")
                    print(str(pok1.nompokemon)+" passe a "+str(PV1)+" PV")
                    print("")
                if PV1==0:
                    print(str(pok1.nompokemon)+" est MORT victoire de "+str(pok2.nompokemon)+" !")
                    print("")
                    print("Fin du combat !")
                    C=1
                    return C
            else:
                #Le pokémon 2 est mort.
                print(str(pok2.nompokemon)+" est MORT victoire de "+str(pok1.nompokemon)+" !")
                print("")
                print("Fin du combat !")
                C=2
                return C
            print("")
            print("Fin du tour "+str(c)+" !")
            c=c+1
        #Le pokémon 2 est le plus rapide il attaque donc en premier.
        else:
            print("Debut du tour "+str(c)+" !")
            print("")
            if PV2>0:
                #Le pokémon 2 attaque.
                if T==1 :
                    #Le dresseur est une IA son attaque est donc aléatoire.
                    atk=random.randint(0,3)
                else :
                    #Le dresseur est un humain il choisie donc son attaque.
                    print("Choix de l attaque "+str(pok2.nompokemon)+" : "+str(pok2.attaque)+" !")
                    print("")
                    atk=input()
                    atk=int(atk)
                    print("")
                    atk=atk-1
                    if atk not in [0,1,2,3]:
                        print("Choix de l attaque "+str(pok2.nompokemon)+" : "+str(pok2.attaque)+" !")
                        print("")
                        atk=input()
                        atk=int(atk)
                        print("")
                        atk=atk-1
                esquive=random.randint(0,100)
                #Le pokémon 1 arrive à esquiver.
                if pok2.attaque[atk][2]<esquive:
                    print(str(pok2.nompokemon)+" utilise "+str(pok2.attaque[atk][0])+" sur "+str(pok1.nompokemon))
                    print(str(pok1.nompokemon)+" esquive l attaque.")
                #Le pokémon 1 n'arrive pas à esquiver.
                else:
                    A=(((42*pok2.ATK*pok2.attaque[atk][1])//(pok1.deff*50))+2)*TYPE[pok2.attaque[atk][3]][pok1.TYpe]
                    print(str(pok2.nompokemon)+" utilise "+str(pok2.attaque[atk][0])+" sur "+str(pok1.nompokemon))
                    critique=random.randint(1,100)
                    if critique<=5 :
                        A=A*2
                        print("C est un CRITIQUE !!!")
                    if TYPE[pok2.attaque[atk][3]][pok1.TYpe]==2 :
                        print("C est super efficace !!!")
                    if TYPE[pok2.attaque[atk][3]][pok1.TYpe]==0 or TYPE[pok2.attaque[atk][3]][pok1.TYpe]==0.5 :
                        print("Ce n est pas tres efficace !!!")
                    PV1=PV1-A
                    if PV1<0:
                        PV1=0
                    print(str(pok1.nompokemon)+" subit "+str(A)+" PV")    
                    print(str(pok1.nompokemon)+" passe a "+str(PV1)+" PV")
                    print("")
            else:
                #Le pokémon 2 est mort.
                print(str(pok2.nompokemon)+" est MORT victoire de "+str(pok1.nompokemon)+" !")
                print("")
                print("Fin du combat !")
                C=2
                return C
            if PV1>0:
                #Le pokémon 1 attaque.
                if t==1 :
                    #Le dresseur est une IA son attaque est donc aléatoire.
                    atk=random.randint(0,3)
                else :
                    #Le dresseur est un humain il choisie donc son attaque.
                    print("Choix de l attaque "+str(pok1.nompokemon)+" : "+str(pok1.attaque)+" !")
                    print("")
                    atk=input()
                    atk=int(atk)
                    print("")
                    atk=atk-1
                    if atk not in [0,1,2,3]:
                        print("Choix de l attaque "+str(pok1.nompokemon)+" : "+str(pok1.attaque)+" !")
                        print("")
                        atk=input()
                        atk=int(atk)
                        print("")
                        atk=atk-1
                esquive=random.randint(0,100)
                #Le pokémon 2 arrive à esquiver .
                if pok1.attaque[atk][2]<esquive:
                    print(str(pok1.nompokemon)+" utilise "+str(pok1.attaque[atk][0])+" sur "+str(pok2.nompokemon))
                    print(str(pok2.nompokemon)+" esquive l attaque.")
                #Le pokémon 2 n'arrive pas à esquiver.
                else:
                    A=(((42*pok1.ATK*pok1.attaque[atk][1])//(pok2.deff*50))+2)*TYPE[pok1.attaque[atk][3]][pok2.TYpe]
                    print(str(pok1.nompokemon)+" utilise "+str(pok1.attaque[atk][0])+" sur "+str(pok2.nompokemon))
                    critique=random.randint(1,100)
                    if critique<=5 :
                        A=A*2
                        print("C est un CRITIQUE !!!")
                    if TYPE[pok1.attaque[atk][3]][pok2.TYpe]==2 :
                        print("C est super efficace !!!")
                    if TYPE[pok1.attaque[atk][3]][pok2.TYpe]==0 or TYPE[pok1.attaque[atk][3]][pok2.TYpe]==0.5 :
                        print("Ce n est pas tres efficace !!!")
                    PV2=PV2-A
                    if PV2<0:
                        PV2=0
                    print(str(pok2.nompokemon)+" subit "+str(A)+" PV")
                    print(str(pok2.nompokemon)+" passe a "+str(PV2)+" PV")
                    print("")
                if PV2==0:
                    print(str(pok2.nompokemon)+" est MORT victoire de "+str(pok1.nompokemon)+" !")
                    print("")
                    print("Fin du combat !")
                    C=2
                    return C
            else:
                #Le pokémon 1 est mort.
                print(str(pok1.nompokemon)+" est MORT victoire de "+str(pok2.nompokemon)+" !")
                print("")
                print("Fin du combat !")
                C=1
                return C
            print("")
            print("Fin du tour "+str(c)+" !")
            c=c+1
    return "Retourne au centre Pokemon"

#programme qui permet de calculer les statistiques réelles de chaque pokémon en partant du principe qu'ils sont tous niveau 100.
def stat(x):
    Stat=int(2*x+21)+110
    return Stat
    
if __name__ == '__main__':
    
    #On créer plusieurs pokémons.
    Pikachu=Pokemon("Pikachu",stat(35),stat(55),stat(40),stat(90),[["Eclair",40,100,4],["Poing eclair",75,100,4],["Tonnerre",95,100,4],["Fatal foudre",120,70,4]],4,1)
    Arceus=Pokemon("Arceus",stat(120),stat(120),stat(120),stat(120),[["Ultralaser",150,90,8],["Pique",140,90,16],["Surf",95,100,3],["Constriction",10,100,8]],8,1)
    Magicarpe=Pokemon("Magicarpe",stat(20),stat(10),stat(55),stat(80),[["Pistolet a O",40,100,3],["Ecume",20,100,3],["Constriction",10,100,8],["Trempette",0,100,8]],3,1)
    Miaouss=Pokemon("Miaouss",stat(40),stat(45),stat(35),stat(90),[["Charge",50,100,8],["Ecrasement",65,100,8],["Torgnoles",15,85,8],["Griffe",40,100,8]],8,1)
    MegaMewtwoX=Pokemon("Mega Mewtwo X",stat(106),stat(190),stat(100),stat(130),[["Ultralaser",150,90,8],["Pique",140,90,16],["Surf",95,100,3],["Constriction",10,100,8]],11,1)
    Munja=Pokemon("Munja",stat(1),stat(90),stat(45),stat(40),[["Double dard",25,100,11],["Dard nuee",14,85,11],["Secretion",10,95,11],["Vampirisme",20,100,11]],11,1)
    Leviator=Pokemon("Leviator",stat(95),stat(125),stat(79),stat(81),[["Hydrocanon",120,80,3],["Surf",95,100,3],["Pince masse",90,90,3],["Tornade",40,100,16]],3,1)
    Dracaufeu=Pokemon("Dracaufeu",stat(78),stat(84),stat(78),stat(100),[["Lance flamme",95,100,5],["Danseflamme",35,85,5],["Poing de feu",75,100,5],["Deflagration",120,85,5]],5,1)
    Rayquaza=Pokemon("Rayquaza",stat(105),stat(150),stat(90),stat(95),[["Dracogriffe",80,100,2],["Lance flamme",95,100,5],["Tonnerre",95,100,4],["Surf",95,100,3]],2,1)
    Tortank=Pokemon("Tortank",stat(79),stat(83),stat(100),stat(78),[["Hydrocanon",120,80,3],["Surf",95,100,3],["Pince masse",90,90,3],["Coud krane",100,100,8]],3,1)
    Roucool=Pokemon("Roucool",stat(40),stat(45),stat(40),stat(56),[["Vol",90,95,16],["Bec vrille",80,100,16],["Picpic",35,100,16],["Tornade",40,100,16]],16,1)
    Taupiqueur=Pokemon("Taupiqueur",stat(10),stat(55),stat(25),stat(95),[["Tunnel",80,100,13],["Seisme",100,100,13],["Jet de sable",0,100,13],["Jet pierres",50,90,16]],16,1)
    Voltali=Pokemon("Voltali",stat(65),stat(65),stat(60),stat(130),[["Double pied",60,95,1],["vitesse extreme",80,100,8],["Tonnerre",95,100,4],["Fatal foudre",120,70,4]],4,1)
    Aquali=Pokemon("Aquali",stat(130),stat(65),stat(60),stat(65),[["Hydrocanon",120,80,3],["Surf",95,100,3],["Laser glace",95,100,6],["Plaquage",85,100,8]],3,1)
    Mentali=Pokemon("Mentali",stat(65),stat(65),stat(60),stat(110),[["Psyko",90,100,11],["Ball Ombre",80,90,14],["Machouille",80,100,15],["vitesse extreme",80,100,8]],11,1)
    
    #On créer plusieurs dresseurs.
    Ash1=DRE.Dresseur("Ash1",[Arceus,Arceus,Arceus,Arceus,Arceus],1)
    Ash2=DRE.Dresseur("Ash2",[Magicarpe,Magicarpe,Magicarpe,Magicarpe,Magicarpe],1)
    Moutou=DRE.Dresseur("Montagnard Moutou",[Voltali,Aquali,Mentali,Taupiqueur,Roucool],1)
    Jaffres=DRE.Dresseur("Pecheur Jaffres",[Leviator,Tortank,Rayquaza,Magicarpe,Magicarpe],1)
    Sutter=DRE.Dresseur("Montagnard Sutter",[Voltali,Aquali,Mentali],0)
    Terry=DRE.Dresseur("Montagnard Terry",[Magicarpe,Aquali],1)
    Tom=DRE.Dresseur("Campagnard Tom",[Rayquaza],1)
    
    print(Pikachu.__dict__.keys())
    print(Miaouss.__dict__.values())
    print(Jaffres.__dict__.values())