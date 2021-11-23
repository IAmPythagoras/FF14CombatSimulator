class Spell:
    #This class will Is any Spell, it will have some subclasses to take Job similar spell, etc.


    def __init__(self, Potency, ManaCost, CastTime, RecastTime, Effect, Requirement):
        self.Potency = Potency
        self.ManaCost = ManaCost
        self.CastTime = CastTime
        self.RecastTime = RecastTime
        self.Effect = Effect
        self.Requirement = Requirement

    def Cast(self, player, Enemy):
        #This function will cast the spell given by the Fight, it will apply whatever effects it has and do its potency

        
