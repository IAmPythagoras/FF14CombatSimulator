class Fight:

    #This class will be the environment in which the fight happens. It will hold a list of players, an enemy, etc.
    # It will be called upon for when we want to start the simulation



    def __init__(self, PlayerList, Enemy):
        self.PlayerList = PlayerList
        self.Enemy = Enemy


    def SimulateFight(self, TimeUnit, TimeLimit):
        #This function will Simulate the fight given the enemy and player list of this Fight
        #It will increment in TimeUnit up to a maximum of TimeLimit (there can be other reasons the Fight ends)
        #It will check weither a player can cast its NextSpell, and if it can it will call the relevant functions
        #However, no direct computation is done in this function, it simply orchestrates the whole thing

        TimeStamp = 0   #Keep track of the time
        while(TimeStamp <= TimeLimit):

            for player in self.PlayerList:
                #Will check if a player is in a locked state. If it is not, it will cast whatever is in the player.NextSpell

                if (player.IsCasting or player.AnimationLocked):
                    #If here, then the player can cast its next Spell

                    player.NextSpell.Cast(player, self.Enemy)#This function will cast the next spell onto the enemy (all relevant computation is done in Spell)
                    #The state of the player will be updated by Cast()


                else:
                    #If is locked, then we will simply update the player's state
                    player.UpdateState(TimeUnit)    #Will update the state of the player accordingly


            #Will then let the enemy add the Dots damage

            for DOT in self.Enemy.DOTList:

                if(DOT.Check()) : 
                    DOT.Cast()#If the DOT can be applied in this time frame, then the DOT will be casted and the potency will be added

            
            #update timestamp

            TimeStamp += TimeUnit
            







