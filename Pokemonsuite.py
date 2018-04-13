# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 17:21:21 2016

@author: Antoine
"""

import random
import numpy as np

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
        
    def creation__de__pokemon():
        print("")
        print("Choisissez le nom du pokemon !")
        print("")
        nom=input()
        print("")
        PV=random.randint(1,100)
        spd=random.randint(1,100)
        atk=random.randint(1,100)
        deff=random.randint(1,100)
        attaque,c=[["",0,0,0],["",0,0,0],["",0,0,0],["",0,0,0]],1
        while c<5:
            c=c-1
            print("Choisissez le nom de l attaque "+str(c+1)+" !")
            print("")
            nomattaque=input()
            nomattaque=list(nomattaque)
            attaque[c][0]=nomattaque
            print("")
            print("Choisissez la puissance de l attaque "+str(c+1)+" !")
            print("")
            degatsattaque=input()
            attaque[c][1]=degatsattaque
            print("")
            print("Choisissez la precision de l attaque "+str(c+1)+" !")
            print("")
            precisionattaque=input()
            attaque[c][2]=precisionattaque
            print("")
            print("Choisissez le numero du type de l attaque "+str(c+1)+" !")
            print("")
            typeattaque=input()
            attaque[c][3]=typeattaque
            print("")
            print("Choisissez le numero du type du pokemon .")
            print("")
            TYpe=input()
            print("")
            c=c+2
        nom=Pokemon(nom,PV,atk,spd,deff,attaque,TYpe,1)
        print(nom.__dict__.values())
        
class Dresseur(object):
    
    def __init__(self,nomdudresseur="",listedepokemon=[],Type=0):
        self.nomdudresseur=nomdudresseur
        self.listedepokemon=listedepokemon
        self.Type=Type
        #Le Type differente les PNJ des PJ , O pour le PJ 1 pour le PNJ.
    
    def choisir_pokemon(self):
        if self.Type==0:
            print("")
            print("Choisissez le numero du pokemon pour le combat !")
            print("")
            x=input()
            x=int(x)
            while x not in [1,2,3,4,5]:
                print("")
                print("Choisissez le numero du pokemon pour le combat")
                print("SVP")
                print("")
                x=input()
                x=int(x)
            x=x-1
            pokechoisie=self.listedepokemon[x]
            x=x+1
        else:
            x=random.randint(0,4)
            pokechoisie=self.listedepokemon[x]
        print("")
        return pokechoisie,x
    
    def creation__d__ennemi():
        L,c=[],1
        print("")
        print("Choisissez le Type d ennemi !")
        print("")
        x=input()
        x=int(x)
        while x not in [0,1]:
            print("")
            print("Choisissez le Type d ennemi !")
            print("SVP")
            print("")
            x=input()
            x=int(x)
        print("")
        print("Choisissez le nom de l ennemi !")
        print("")
        y=input()
        while c<6:
            print("")
            print("Choisissez le pokemon numero "+str(c)+" de l ennemi !")
            print("")
            z=input()
            z=int(z)
            while z not in range(0,len(P)):
                print("")
                print("Choisissez le pokemon numero "+str(c)+" de l ennemi !")
                print("SVP")
                print("")
                z=input()
                z=int(z)
            L,c=L+[P[z]],c+1
        ennemi=Dresseur(y,L,x)
        print("")
        return ennemi
        
    def defier(self,ennemi):
        c,P1,P2=0,self.listedepokemon,ennemi.listedepokemon
        while P1!=[] or P2!=[]:
            if P1!=[]:
                print("Le dresseur choisi son pokemon.")
                print("Le dresseur a encore "+str(len(P1))+" pokemon pour combatre !")
                print("Liste des pokemons du dresseur : "+str(P1)+" !")
                print("")
                D=self.choisir_pokemon()
                dpok=D[0]
                d=D[1]
                print("L'ennemi choisi son pokemon.")
                print("Le dresseur a encore "+str(len(P2))+" pokemon pour combatre !")
                print("Liste des pokemons du dresseur : "+str(P2)+" !")
                print("")
                E=self.choisir_pokemon()
                epok=E[0]
                e=E[1]
                C=KOMBAT(dpok,epok,self,ennemi)
                if C==1:
                    P1=P1.remove(P1[d])
                    D=self.choisir_pokemon()
                    dpok=D[0]
                    d=D[1]
                else:
                    P2=P2.remove(P2[e])
                    E=self.choisir_pokemon()
                    epok=E[0]
                    e=E[1]
            else:
                return "Le dresseur n a plus de pokemon vivant."
            if P2!=[]:
                print("Le dresseur choisi son pokemon.")
                print("Le dresseur a encore "+str(len(P2))+" pokemon pour combatre !")
                print("Liste des pokemons du dresseur : "+str(P2)+" !")
                print("")
                D=self.choisir_pokemon()
                dpok=D[0]
                d=D[1]
                print("L'ennemi choisi son pokemon.")
                print("Le dresseur a encore "+str(len(P1))+" pokemon pour combatre !")
                print("Liste des pokemons du dresseur : "+str(P1)+" !")
                print("")
                E=self.choisir_pokemon()
                epok=E[0]
                e=E[1]
                C=KOMBAT(dpok,epok,self,ennemi)
                if C==1:
                    P1=P1.remove(P1[d])
                    D=self.choisir_pokemon()
                    dpok=D[0]
                    d=D[1]
                else:
                    P2=P2.remove(P2[e])
                    E=self.choisir_pokemon()
                    epok=E[0]
                    e=E[1]
            else:
                return "L ennemi n a plus de pokemon vivant."
        return "Nop"

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
       
def creation__de__liste(pok1,pok2,pok3,pok4,pok5):
    L=[pok1,pok2,pok3,pok4,pok5]
    return L

def KOMBAT(pok1,pok2,dres1,dres2):
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
                    atk=random.randint(0,3)
                else :
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
                    atk=random.randint(0,3)
                else :
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
                    return str(pok1.nompokemon)+" est MORT victoire de "+str(pok2.nompokemon)+" !"
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
                    atk=random.randint(0,3)
                else :
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
                    atk=random.randint(0,3)
                else :
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
                    return str(pok2.nompokemon)+" est MORT victoire de "+str(pok1.nompokemon)+" !"
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

def stat(x):
    Stat=int(2*x+21)+110
    return Stat
    
if __name__ == '__main__':
    
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
    
    P=[Pikachu,Arceus,Magicarpe,Miaouss,MegaMewtwoX,Munja,Leviator,Dracaufeu,Rayquaza,Tortank,Roucool,Taupiqueur,Voltali,Aquali,Mentali]
    
    Ash1=Dresseur("Ash1",[Arceus,Arceus,Arceus,Arceus,Arceus],0)
    Ash2=Dresseur("Ash2",[Magicarpe,Magicarpe,Magicarpe,Magicarpe,Magicarpe],1)
    Moutou=Dresseur("Montagnard Moutou",[Voltali,Aquali,Mentali,Taupiqueur,Roucool],0)
    Jaffres=Dresseur("Pecheur Jaffres",[Leviator,Tortank,Rayquaza,Magicarpe,Magicarpe],0)
    Sutter=Dresseur("Montagnard Sutter",[Voltali,Aquali,Mentali],0)
    
    print(Pikachu.__dict__.keys())
    print(Miaouss.__dict__.values())
    print(Ash1.__dict__.values())