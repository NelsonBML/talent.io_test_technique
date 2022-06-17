
import random


def volleyball_simulator(p1, p2):    
    set_1(p1, p2) 
    set_2(p1, p2)
    set_3(p1, p2)
    set_4(p1, p2)
    #if team_1_sets == 3 or team_2_sets == 3:
    #    print ('Game Ends')
    #    exit()
    set_5(p1, p2)


def sets_score(p1, p2):
    server = 0
    team_1 = 0
    team_2 = 0  
    team_1_sets = 0
    team_2_sets = 0 
    score_list = []
    final_list = []
    #sets = str(set_1) + str(set_2) + str(set_3)
    while True:
        if server == 0:
            #print ("Team 1 serves!")
            if random.random() < p1:
                #print ("Team 1 wins the serve!")
                team_1+= 1
            else:
                server = 1
        else:
            #print ("Team 2 serves!")
            if random.random() < p2:
               #print ("Team 2 wins the serve!")
                team_2+= 1
                score_list.append(str(team_1) + "-" + str(team_2))
                final_list.append(str(score_list))
                print(final_list)
            else:
                server = 0

        if team_1 >= 25 or team_2 >= 25:
            if abs(team_1 - team_2) >= 2:
                break;
        
    #print ("team 1 : " + str(team_1))
    #print ("team 2 : " + str(team_2))
    print(str(team_1) + '-' + str(team_2))
    if team_1 > team_2:
        team_1_sets+= 1
        print('Team 1 wins the set!')
        #print('TEAM 1', team_1_sets)
        return team_1
        
    else:
        team_2_sets+=1
        print('Team 2 wins the set!')
        #print('TEAM 2', team_2_sets)
        return team_2
    

def sets_score_5(p1, p2):
    server = 0
    team_1 = 0
    team_2 = 0
    score_list = []
    final_list = []
    while True:
        if server == 0:
            if random.random() < p1:
                team_1+= 1
            else:
                server = 1
        else:
            if random.random() < p2:
                team_2+= 1
                score_list.append(str(team_1) + "-" + str(team_2))
                final_list.append(str(score_list))
                print(final_list)
                
            else:
                server = 0

        if team_1 >= 15 or team_2 >= 15:
            if abs(team_1 - team_2) >= 2:
                break;
        
 
    #print ("team 1 : " + str(team_1))
    #print ("team 2 : " + str(team_2))
    print(str(team_1) + '-' + str(team_2))
    if team_1 > team_2:
        print('Team 1 wins the set!')
        return team_1
        
    else:
         print('Team 2 wins the set!')
         return team_2
    

def set_1(p1, p2):

    print ("Set 1")
    sets_score(p1, p2)

def set_2(p1, p2):

    print ("Set 2")
    server = 1
    sets_score(p2, p1)
        

def set_3(p1, p2):

    print ("Set 3")
    sets_score(p1, p2)

def set_4(p1, p2):

    print ("Set 4")
    sets_score(p1, p2)

def set_5(p1, p2):

    print ("Set 5")
    sets_score_5(p1, p2)
        

volleyball_simulator(0.7, 0.7)