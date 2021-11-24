class FailedToCast(Exception):#Exception called if a spell fails to cast
    pass

class Spell:
    #This class will Is any Spell, it will have some subclasses to take Job similar spell, etc.


    def __init__(self, GCD, Potency, ManaCost, CastTime, RecastTime, Effect, Requirement):
        self.GCD = GCD #True if GCD
        self.Potency = Potency
        self.ManaCost = ManaCost
        self.CastTime = CastTime
        self.RecastTime = RecastTime
        self.Effect = Effect
        self.Requirement = Requirement

    def Cast(self, player, Enemy):
        #This function will cast the spell given by the Fight, it will apply whatever effects it has and do its potency

        tempSpell = Spell(self.Potency, self.ManaCost, self.CastTime, 
        self.RecastTime, self.Effect, self.Requirement)
        #Creating a tempSpell which will have its values changed according that what effect
        #the player and the enemy have

        #Will apply each effect the player currently has on the spell

        for Effect in player.EffectList:
            Effect(tempSpell)#Changes tempSpell
        for Effect in Enemy.EffectList:
            Effect(tempSpell)#Changes tempSpell


        #Checks if we meet the spell requirement

        for Requirement in self.Requirement:
            if(not Requirement(self, player)) :
                raise FailedToCast("Failed to cast the spell")

        #Then we will apply whatever effect the spell has on the player or the enemy

        for Effect in self.Effect:
            Effect(player, Enemy)#Put effects on Player and/or Enemy
            #This will include substracting the mana (it has been verified before that the mana was enough)
            #One of these effects will also do the damage


        #At this point the spell is changed in such a way that it can be casted accordingly

class BLMSpell(Spell):
    #This class will be all BlackMage Ability

    def __init__(self, GCD, Potency, ManaCost, CastTime, RecastTime, Effect, Requirement, IsFire, IsIce):
        super().__init__(GCD, Potency, ManaCost, CastTime, RecastTime, Effect, Requirement)#Calls constructor of Spell

        #BLM specific part

        self.IsFire = IsFire
        self.IsIce = IsIce
