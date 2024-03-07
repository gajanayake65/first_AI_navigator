import math
from itertools import permutations
class pointers:
    def __init__(self,x,y):
        self.x=x
        self.y=y
#create a dict
coordinataes_dict={}
#add value to dict
coordinataes_dict["O"]=pointers(0,0)
coordinataes_dict["A"]=pointers(3,4)
coordinataes_dict["B"]=pointers(6,7)
coordinataes_dict["C"]=pointers(3,10)

print("coordinataes_dict: ")
for key, point in coordinataes_dict.items():
    
    print(key)
##################### make a permutation ##############################################

#######################################################################################
now=input("Where are you now?")
distination=input("where you need to go?")
if now in coordinataes_dict : 
    if distination in coordinataes_dict:
        print("ok,I'll check")
        #get data for calculation
        value_x_now = coordinataes_dict[now].x
        value_y_now = coordinataes_dict[now].y
        ############################################################### make a Permutation ##################################################
        element=['O','A','B','C']
        permutations_list=list(permutations(element))
        filtered_permutations=[perm for perm in permutations_list if perm[0]==now and perm[3]==distination]
        print("Roads are:")
        for perm in filtered_permutations:
            print(perm)
        print(f"There are roads that you can go {now} to {distination}")
        if filtered_permutations:
            tuple_1=filtered_permutations[0]
            tuple_2=filtered_permutations[1]
            # accses data with tuple_1
            #values of X
            #now x has
            ###################################  x ########################################################
            second_x=tuple_1[1]
            third_x =tuple_1[2]
            if second_x in coordinataes_dict:
                value_x_sec=coordinataes_dict[second_x].x
            if third_x in coordinataes_dict:
                value_x_third=coordinataes_dict[third_x].x
            # distination x value
            value_x_dis=coordinataes_dict[distination].x
            ################################################################################################

            ################################### y ##########################################################
            
            if second_x in coordinataes_dict:
                value_y_sec=coordinataes_dict[second_x].y
            if third_x in coordinataes_dict:
                value_y_third=coordinataes_dict[third_x].y
            # distination x value
            value_y_dis=coordinataes_dict[distination].y
            ###############################################################################################
            #calculation part#
            #1st
            L1=((value_x_now-value_x_sec)**2)+((value_y_now-value_y_sec)**2)
            L1N=math.sqrt(L1)
            #2nd
            L2=((value_x_third-value_x_sec)**2)+((value_y_third-value_y_sec)**2)
            L2N=math.sqrt(L2)
            #3rd
            L3=((value_x_dis-value_x_third)**2)+((value_y_dis-value_y_third)**2)
            L3N=math.sqrt(L3)
            # toltal
            total=L1N+L2N+L3N
            ##############################@@@@@@@@@@@@@@@@@##########################################



            second_x_2=tuple_2[1]
            third_x_2 =tuple_2[2]
            if second_x_2 in coordinataes_dict:
                value_x_sec_2=coordinataes_dict[second_x_2].x
            if third_x_2 in coordinataes_dict:
                value_x_third_2=coordinataes_dict[third_x_2].x
           
            ################################################################################################

            ################################### y ##########################################################
            
            if second_x_2 in coordinataes_dict:
                value_y_sec_2=coordinataes_dict[second_x_2].y
            if third_x_2 in coordinataes_dict:
                value_y_third_2=coordinataes_dict[third_x_2].y
           
            #calculation part#
            #1st
            L1_2=((value_x_now-value_x_sec_2)**2)+((value_y_now-value_y_sec_2)**2)
            L1N_2=math.sqrt(L1_2)
            #2nd
            L2_2=((value_x_third_2-value_x_sec_2)**2)+((value_y_third_2-value_y_sec_2)**2)
            L2N_2=math.sqrt(L2_2)
            #3rd
            L3_2=((value_x_dis-value_x_third_2)**2)+((value_y_dis-value_y_third_2)**2)
            L3N_2=math.sqrt(L3_2)
            # toltal
            total1=L1N_2+L2N_2+L3N_2

            if total<total1:
                print(f"{tuple_1} road is shortest one,If you use this road you have to walk {total}m")
            else:
                print(f"{tuple_2} road is shortest one,If you use this road you have to walk {total1}m")

else:
    print("Your track couldn't found")

    

        
        
        ##############################################################  end it  ##############################################################    

