import copy 

steps = 0

s = [[1,2,3],[8,0,4],[7,6,5]]

g = [[2,0,3],[1,8,4],[7,6,5]]

visited = []

def compare(curr):
    return curr == g
    
def blankTile(s):
    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j] == 0:
                return [i,j]
    return -1

def up(curr):
    
    i,j = blankTile(curr)
    
    if(i==0):
        
        return curr
    
    temp = copy.deepcopy(curr)
     
    temp[i-1][j],temp[i][j] = temp[i][j],temp[i-1][j]
    
    return temp
    

def down(curr):
    
    i,j = blankTile(curr)
    
    if (i == len(curr)-1):
        
        return curr
    
    temp = copy.deepcopy(curr)
     
    temp[i][j],temp[i+1][j] = temp[i+1][j],temp[i][j]
    
    return temp
    

def left(curr):
    
    i,j = blankTile(curr)
    
    if (j == 0):
        
        return curr
    
    temp = copy.deepcopy(curr)
    
    temp[i][j],temp[i][j-1] = temp[i][j-1],temp[i][j]
    
    return temp


def right(curr):
    
    i,j = blankTile(curr)
    
    if (j == len(curr[0])-1):
        
        return curr
    
    temp = copy.deepcopy(curr)
    
    temp[i][j],temp[i][j+1] = temp[i][j+1],temp[i][j]
    
    return temp


def heuristic(s):
    
    h_val = 0
    
    for i in range(len(s)):
        
        for j in range(len(s[0])):
            
            if s[i][j] != g[i][j] :
                
                h_val +=1 
    
    return h_val
    

def getStates(curr):
    
    states = []
    
    states.append(left(curr))
    states.append(right(curr))
    states.append(up(curr))
    states.append(down(curr))
    
    
    
    arr = []
    
    for i in states:
        
        if (i not in visited):
            
            arr.append(i)
    
    
    if(len(arr)==0):
        
        return -1
    
    
    

    heuristic_array = []
    
    for i in arr:
        heuristic_array.append(heuristic(i))
  
    ind = heuristic_array.index(min(heuristic_array))
    return arr[ind]    
    states = []
    states.append(up(curr))
    states.append(down(curr))
    states.append(right(curr))
    states.append(left(curr))
    
    arr = []
    for i in states:
        if (i not in visited):
            arr.append(i)
            
    if(len(arr)==0):
        return -1
    return min(arr)

def display(state):
    for i in state:
        for j in i:
            print(j, end='')
        print()
    print()

def EightPuzzle():
    if compare(s):
        return s
    curr = s
    global steps
    
    while(compare(curr)==0):
            steps+=1
            print("step ",steps)
            display(curr)
            visited.append(curr)
            curr = getStates(curr)
            if (curr == -1):
                return "no solution"
    return curr

EightPuzzle()
print("The total number of steps are: ",steps)
print ("*********END*********")
