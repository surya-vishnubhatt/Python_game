from entity import Entity
def find_highest_in_file(file):
    file_in = open(file)
    list_1 =[]
    highest = 0
    for line in file_in:
        try:
            int_val = int(line)
            list_1.append(int_val)
        except:
            return False
    for i in range(len(list_1)-1):
        if list_1[i]>=list_1[i+1]:
            highest = list_1[i]
        elif list_1[i] < list_1[i+1]:
            highest = list_1[i+1]
    return highest

def find_matches(file1, file2, str_val, boolVar):
    file1 = open(file1)
    file2=open(file2,"w")
    count = 0
    for line in file1:
            if boolVar == True:
                if str_val in line:
                    count = count + 1
                    file2.write(line)
            elif boolVar == False:
                if str_val not in line:
                    count = count + 1
                    file2.write(line)
    return count

def draw_entity(e,b):
    boolVar = True
    try:
        for i in range(e.top_left_y, e.top_left_y+ e.height):
            for j in range(e.top_left_x, e.top_left_x + e.width):
                b[i][j] = e.icon
        boolVar = True
    except:
        boolVar = False
    return boolVar
            
            
            
            
           
            
                
        
    
        
        
        
    
