class Player:

    #This class will contain any relevant information to the player. It will be the mother of all other Player

    def __init__(self, GCDTimer, ActionSet, PrePullSet, EffectList):

        self.GCDTimer = GCDTimer    #How long a GCD is
        self.ActionSet = ActionSet  #Known Action List
        self.EffectList = EffectList    #Normally Empty, can has some effects initially
        self.PrePullSet = PrePullSet    #Prepull action list
        self.EffectCDList = []          #List of Effect for which we have to check if the have ended
        self.DOTList = []
        self.NextSpell = 0
        self.CastingSpell = []
        self.CastingTarget = []

        self.TrueLock = False   #Used to know when a player has finished all of its ActionSet
        self.Casting = False    #used to know if an action is possible
        self.oGCDLock = False   #If animation locked by oGCD
        self.GCDLock = False    #If have to wait for another GCD
        self.CastingLockTimer = 0
        self.oGCDLockTimer = 0
        self.GCDLockTimer = 0

        self.Mana = 10000
        self.HP = 1000  #Could be changed
        
        self.TotalPotency = 0

    def updateTimer(self, time):
        #print("Updated Timer : " + str(self.oGCDLockTimer))
        #print(str(self.GCDLock) + str(self.oGCDLock) + str(self.Casting))
        if (self.GCDLockTimer > 0) : self.GCDLockTimer = max(0, self.GCDLockTimer-time)
        if (self.oGCDLockTimer > 0) : self.oGCDLockTimer = max(0, self.oGCDLockTimer-time)
        if (self.CastingLockTimer > 0) : self.CastingLockTimer = max(0, self.CastingLockTimer-time)

    def updateLock(self):
        if (self.GCDLockTimer <= 0):
            self.GCDLockTimer = 0
            self.GCDLock = False
        
        if (self.oGCDLockTimer <= 0):
            self.oGCDLockTimer = 0
            self.oGCDLock = False
        
        if(self.Casting and self.CastingLockTimer <=0):
            self.CastingSpell.CastFinal(self, self.CastingTarget)

        if (self.CastingLockTimer <= 0):
            self.CastingLockTimer = 0
            self.Casting = False
            

class BlackMage(Player):
    #This class will be blackmage object and will be the one used to simulate a black mage

    def __init__(self, GCDTimer, ActionSet, PrePullSet, EffectList):
        super().__init__(GCDTimer, ActionSet, PrePullSet, EffectList)

        #Special
        self.AstralFireStack = 0
        self.UmbralIceStack = 0
        self.Enochian = False
        self.PolyglotStack = 0
        self.AFUITimer = 0
        self.UmbralHeartStack = 0

        #Prock
        self.T3Prock = False
        self.F3Prock = False

        #Ability Effect
        self.SharpCastStack = 0
        self.TripleCastStack = 0
        self.SwiftCastStack = 0
        self.T3Timer = 0
        self.F3Timer = 0
        self.LeyLinesTimer = 0

        #Ability CD
        self.LeyLinesCD = 0
        self.SharpCastCD = 0
        self.TripleCastCD = 0
        self.SwiftCastCD = 0
        self.EnochianCD = 0
        self.ManaFrontCD = 0
        self.TransposeCD = 0
    
    def updateCD(self, time):
        if (self.LeyLinesCD > 0) : self.LeyLinesCD = max(0,self.LeyLinesCD - time)
        if (self.SharpCastCD > 0) :self.SharpCastCD = max(0,self.SharpCastCD - time)
        if (self.TripleCastCD > 0) :self.TripleCastCD = max(0,self.TripleCastCD - time)
        if (self.SwiftCastCD > 0) :self.SwiftCastCD = max(0,self.SwiftCastCD - time)
        if (self.EnochianCD > 0) :self.EnochianCD = max(0,self.EnochianCD - time)
        if (self.ManaFrontCD > 0) :self.ManaFrontCD = max(0,self.ManaFrontCD - time)
        if (self.TransposeCD > 0) :self.TransposeCD = max(0,self.TransposeCD - time)

    def updateTimer(self, time):
        super().updateTimer(time)
        if (self.LeyLinesTimer > 0) : self.LeyLinesTimer = max(0,self.LeyLinesTimer - time)
        if (self.T3Timer > 0) : self.T3Timer = max(0,self.T3Timer - time)
        if (self.AFUITimer > 0) : self.AFUITimer = max(0, self.AFUITimer-time)

