# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 09:51:01 2016

@author: Antoine
"""
import random

import Pokemon as POKE

#On créer la classe Dresseur.
class Dresseur(object):
    
    def __init__(self,nomdudresseur="",listedepokemon=[],Type=0):
        self.nomdudresseur=nomdudresseur
        self.listedepokemon=listedepokemon
        self.Type=Type
        #Le Type differente les PNJ des PJ , O pour le PJ 1 pour le PNJ.
    
    def choisir_pokemon(self):
        #Si le dresseur est un humain.
        if self.Type==0:
            print("")
            print("Choisissez le numero du pokemon pour le combat !")
            print("")
            x=input()
            x=int(x)
            #Si le numéro rentré ne corespond pas à un pokémon de la liste car on est limité à 5 pokémons par équipe.
            while x not in range(1,len(self.listedepokemon)+1):
                print("")
                print("Choisissez le numero du pokemon pour le combat")
                print("SVP")
                print("")
                x=input()
                x=int(x)
            x=x-1
            pokechoisie=self.listedepokemon[x]
            x=x+1
        #Si le dresseur est une IA.
        else:
            x=random.randint(0,len(self.listedepokemon)-1)
            pokechoisie=self.listedepokemon[x]
        print("")
        return pokechoisie,x
        
    def defier(self,ennemi):
        c,P1,P2=0,self.listedepokemon,ennemi.listedepokemon
        if P1==[]:
            return str(self.nomdudresseur)+" n a plus de pokemon vivant."
        if P2==[]:
            return str(ennemi.nomdudresseur)+" n a plus de pokemon vivant."
        #Initialisation du combat.
        print(str(self.nomdudresseur)+" choisi son pokemon.")
        print(str(self.nomdudresseur)+" a encore "+str(len(P1))+" pokemon pour combatre !")
        print("Liste des pokemons de "+str(self.nomdudresseur)+" : "+str(P1)+" !")
        print("")
        #On récupere le nom et son numéro dans la liste du pokémon choisie pour le dresseur.
        D=self.choisir_pokemon()
        dpok=D[0]
        d=D[1]
        print(str(ennemi.nomdudresseur)+" choisi son pokemon.")
        print(str(ennemi.nomdudresseur)+" a encore "+str(len(P2))+" pokemon pour combatre !")
        print("Liste des pokemons de "+str(ennemi.nomdudresseur)+" : "+str(P2)+" !")
        print("")
        #On récupere le nom et son numéro dans la liste du pokémon choisie pour l'ennemi.
        E=ennemi.choisir_pokemon()
        epok=E[0]
        e=E[1]
        #Début du combat.
        while P1!=[] or P2!=[]:
            C=POKE.KOMBAT(dpok,epok,self,ennemi)
            #Si le pokémon du dresseur est mort.
            if C==1:
                P1.remove(P1[d])
                if P1==[]:
                    return str(self.nomdudresseur)+" n a plus de pokemon vivant."
                print(str(self.nomdudresseur)+" choisi son pokemon.")
                print(str(self.nomdudresseur)+" a encore "+str(len(P1))+" pokemon pour combatre !")
                print("Liste des pokemons de "+str(self.nomdudresseur)+" : "+str(P1)+" !")
                print("")
                D=self.choisir_pokemon()
                dpok=D[0]
                d=D[1]
            #Si le pokémon de l'ennemi est mort.
            else:
                P2.remove(P2[e])
                if P2==[]:
                    return str(ennemi.nomdudresseur)+" n a plus de pokemon vivant."
                print(str(ennemi.nomdudresseur)+" choisi son pokemon.")
                print(str(ennemi.nomdudresseur)+" a encore "+str(len(P2))+" pokemon pour combatre !")
                print("Liste des pokemons de "+str(ennemi.nomdudresseur)+" : "+str(P2)+" !")
                print("")
                E=ennemi.choisir_pokemon()
                epok=E[0]
                e=E[1]
                
        