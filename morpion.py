J1_choice = 0
J2_choice = 0
rounds_x2 = 0
numbr = ("   1    2    3     ")
wall = ("|----|----|----|   ")
basic_content = ['1','2','3','4','5','6','7','8','9']
content = ['1','2','3','4','5','6','7','8','9']

J1 = input("Nom du J1: ")
J2 = input("Nom du J2: ")


def disp_terrain():

    #print(numbr)
    print(wall)
    print("| ",content[0],"| ",content[1],"| ",content[2],"|  ")
    print(wall)
    print("| ",content[3],"| ",content[4],"| ",content[5],"|  ")
    print(wall)
    print("| ",content[6],"| ",content[7],"| ",content[8],"|  ")
    print(wall)
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

def is_gamefinished():

    #HORIZONTAL
    if (content[0] == content[1] and content[1] == content[2]):
        disp_terrain()

        if (content[0] == "X"):
            print(J1,"a gagné !")
        else:
            print(J2,"a gagné !")
        return 1

    elif (content[3] == content[4] and content[4] == content[5]):
        disp_terrain()
        
        if (content[3] == "X"):
            print(J1,"a gagné !")
        else:
            print(J2,"a gagné !")
        return 1

    elif (content[6] == content[7] and content[7] == content[8]):
        disp_terrain()
        
        if (content[6] == "X"):
            print(J1,"a gagné !")
        else:
            print(J2,"a gagné !")
        return 1

    #VERTICAL
    elif (content[0] == content[3] and content[3] == content[6]):
        disp_terrain()
        
        if (content[0] == "X"):
            print(J1,"a gagné !")
        else:
            print(J2,"a gagné !")
        return 1

    elif (content[1] == content[4] and content[4] == content[7]):
        disp_terrain()
        
        if (content[1] == "X"):
            print(J1,"a gagné !")
        else:
            print(J2,"a gagné !")
        return 1

    elif (content[2] == content[5] and content[5] == content[8]):
        disp_terrain()
        
        if (content[2] == "X"):
            print(J1,"a gagné !")
        else:
            print(J2,"a gagné !")
        return 1

    #DIAGONALE
    elif (content[0] == content[4] and content[4] == content[8]):
        disp_terrain()
        
        if (content[0] == "X"):
            print(J1,"a gagné !")
        else:
            print(J2,"a gagné !")
        return 1

    elif (content[6] == content[4] and content[4] == content[2]):
        disp_terrain()
        
        if (content[6] == "X"):
            print(J1,"a gagné !")
        else:
            print(J2,"a gagné !")
        return 1

    elif (rounds_x2 != 0):

        for a in range(0,9,1):
            if (content[a] == basic_content[a]):

                return 0
        disp_terrain()
        print("EX - AEQUO !")
        return 1 
        
    
    return 0

def is_already_used(choice : int):

    if (content[choice-1] == "X" or content[choice-1] == "O"):
        return 1

    return 0

def select_slot(player : int):

    if (player == 1):
        
        print(J1,end = "")
        J1_choice = int(input("! Quelle case allez vous occuper ? -> "))

        while (is_already_used(J1_choice) == 1):

            print("La case est déja occupée !")        
            J1_choice = int(input("! Quelle case allez vous occuper ? -> "))

        content[J1_choice-1] = "X"

    elif (player == 2):
        
        print(J2,end = "")
        J2_choice = int(input("! Quelle case allez vous occuper ? -> "))

        while (is_already_used(J2_choice) == 1):

            print("La case est déja occupée !")          
            J2_choice = int(input("! Quelle case allez vous occuper ? -> "))

        content[J2_choice-1] = "O"


while (is_gamefinished() == 0):

    disp_terrain()
    select_slot(1)
    rounds_x2 = rounds_x2 + 1

    if (is_gamefinished() == 0):
        disp_terrain()
        select_slot(2)
        rounds_x2 = rounds_x2 + 1

print("")
print("Merci d'avoir joué - [by Mashiro]")