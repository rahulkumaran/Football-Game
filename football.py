# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 20:09:53 2016

@author: Rahul
"""

team_a ={'Messi' : '10' , 'Ronaldo' : '9' , 'Suarez' : '9' , 'Ney' : '11', 'Silva' : '12' , 'Neuer' : '1' ,
         'Rahul' : '8' , 'Ataur' : '19' , 'Utah' : '32' , 'Ishq' : '90' , 
         'Olala' : '123'}
team_b ={'Okau' : '23' , 'Bravo' : '1' , 'Kompany' : '89' , 'Dennis' : '324',
         'ok' : '1' , 'df' : '12343' , 'hj' : '9002' , 'kl' : '433424',
         'man' : '231' , 'fds' : '3435462656'}
         
print "The match is between team_a vs team_b"

l =[]

class football:
    
    """
    profile_name : string
    time_on_field : float
    goals : integer
    in_the_match : 'Yes'/ 'No'
    tired : 'Yes' / 'No'
    """
    
    
    def __init__(self,player_name,minutes_played,goals_scored):
        self.name = player_name
        self.time_on_field = minutes_played
        self.goals = goals_scored
        self.in_the_match = 'No'
        self.tired = 'Yes'
        
        
    def dist(self):
        dis_of_player = self.time_on_field* 0.672
        print "The player has covered",dis_of_player,"km"
        
        
    def goal_scored(self):
        if self.name in team_a:
            print self.name,"with jersey number",team_a[self.name],"played the game"


        else:
            print self.name,"didn't play the match"

            
    def celebration(self):
        if self.name == 'Ronaldo':
           if self.goals > 0 :
             print self.name,"celebrated by doing 'CALMA CALMA'"
             
           else:
               print self.name,"didn't score a goal"
               
        if self.name == 'Messi' :
            if self.goals > 0:
                print self.name,"celebrated in a very calm way"
            else :
                print self.name,"didn't score a goal"
                
        else:
            print "Nobody cares about how others celebrate as long as someone dabs"

                
    def scoring_now(self):
        if self.goals == 0:
            self.goals = self.goals + 1
        if self.goals == 1:
            self.goals = self.goals + 1
        if self.name == 'Messi' or 'Ronaldo' :
           if self.goals == 2:
              self.goals = self.goals + 1
              print self.name,"has scored",self.goals,"which can be considered as scoring a hat-trick"

              
    def goal_scored_against(self):
        print self.name,"scored a goal past the player with jersey number",team_b[self.name]


    def isTired(self):
        if self.time_on_field > 60 :
            self.Tired = 'Yes'
        if self.Tired == 'Yes':
                print "Drink Red Bull or some other energy drink bruuhh!"
                
        else:
                print "Go ahead and fuck everyone's case and lemme know when you're tired mann!"
              
                
    def match_heroes(self):
        if self.goals >= 2:
            print l.append(self.name),"are the players who scored either 2 or more goals"
    

    def perf(self) :
       if self.goals == 0:
           print "Poor performance given by",self.name