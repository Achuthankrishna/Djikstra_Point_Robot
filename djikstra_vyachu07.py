import pygame
import numpy as np
from sys import exit
import math
from queue import PriorityQueue
from Map import obs_coord
#Defining action sets. We will initially use same as BFS with cost as 1 and write 4 new functions to update cost as 1.4
#Our given action set is A= {(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,1), (1,-1), (-1,-1)}
#Lets first define set of possible routes
def ActionMoveUp(pnode,init_cost,visited,node,costcome,parent):

    newn = pnode[:] 
    xc=newn[0] 
    yc=newn[1]+1 #Y action for up is +1 from current position
    cost=init_cost+1
    #We are sendinf the information of coordinate ,neighbor,previous node visited,costtakensofar,cost and the parent node to our queue in dijkstra function, which will calculate 
    # least cost to determine the route
    newn,cost=path(newn,xc,yc,cost,pnode,visited,node,costcome,parent)

#Defining fr downwards
def ActionMoveDown(pnode,init_cost,visited,node,costcome,parent):

    newn = pnode[:] 
    xc=newn[0] 
    yc=newn[1]-1 #Y action for down is -1 from current position
    cost=init_cost+1
    newn,cost=path(newn,xc,yc,cost,pnode,visited,node,costcome,parent)
#Defining fr left
def ActionMoveLeft(pnode,init_cost,visited,node,costcome,parent):

    newn = pnode[:] 
    xc=newn[0]-1 #X action for Left is -1 from current position 
    yc=newn[1] 
    cost=init_cost+1
    newn,cost=path(newn,xc,yc,cost,pnode,visited,node,costcome,parent)
    return newn
#Defining fr Right
def ActionMoveRight(pnode,init_cost,visited,node,costcome,parent):

    newn = pnode[:] 
    xc=newn[0]+1 #X action for Right is +1 from current position 
    yc=newn[1] 
    cost=init_cost+1
    newn,cost=path(newn,xc,yc,cost,pnode,visited,node,costcome,parent)
    return newn
#Now lets write function for our diagonal elements with cost 1.4
def ActionMoveRightUp(pnode,init_cost,visited,node,costcome,parent):
    #Right and Up, so x+1 and y+1
    newn = pnode[:] 
    xc=newn[0]+1 #X action for right is +1 from current position 
    yc=newn[1]+1 #Y action for up is +1 from current position 
    cost=init_cost+1.4
    newn,cost=path(newn,xc,yc,cost,pnode,visited,node,costcome,parent)
def ActionMoveRightDown(pnode,init_cost,visited,node,costcome,parent):
    #Right and Down, so x+1 and y-1
    newn = pnode[:] 
    xc=newn[0]+1 #X action for right is +1 from current position 
    yc=newn[1]-1 #Y action for down is -1 from current position 
    cost=init_cost+1.4
    newn,cost=path(newn,xc,yc,cost,pnode,visited,node,costcome,parent)
#Now for UpLeft and DownLeft
def ActionMoveLeftDown(pnode,init_cost,visited,node,costcome,parent):
    #Left and Down, so x-1 and y-1
    newn = pnode[:] 
    xc=newn[0]-1 #X action for Left is +1 from current position 
    yc=newn[1]-1 #Y action for down is -1 from current position 
    cost=init_cost+1.4
    newn,cost=path(newn,xc,yc,cost,pnode,visited,node,costcome,parent)
def ActionMoveLeftUp(pnode,init_cost,visited,node,costcome,parent):
    #Left and Down, so x-1 and y+1
    newn = pnode[:] 
    xc=newn[0]-1 #X action for Left is +1 from current position 
    yc=newn[1]+1 #Y action for Up is -1 from current position 
    cost=init_cost+1.4
    newn,cost=path(newn,xc,yc,cost,pnode,visited,node,costcome,parent)
#Now we define the obstacles. We have written a sepearate code for obstacles using pygame and just we need to access it 
def list_of_obs(x,y):
    ind=obs_coord(x,y)
    return ind

def search(pnode):
    d=list_of_obs(pnode[0],pnode[1])
    if(d==1 or pnode[1] not in range(0,256) or pnode[0] not in range (0,601)):
        print("Starting Pos not in space")
        exit()
    else:
        pass

def end(enode):
    e=list_of_obs(enode[0],enode[1])
    if(e==1 or enode[1] not in range(0,256) or enode[1] not in range(0,601)):
        print("Goal Pos not in space")
        exit()
    else:
        pass
def path(newn,xc,yc,cost,pnode,visited,node,costcome,parent):
    m=list_of_obs(xc,yc)
    if xc in range(0,601) and yc in range(0,251) and m==0:
        newn[0]=xc
        newn[1]=yc
        cost=cost
        if newn not in visited:
             # update only if the node is not visited
            if newn in node:
                check=node.index(newn)
                costcheck=costcome[check]
                if costcheck<cost:
                    pass
                else:
                    node.pop(check)
                    costcome.pop(check)
                    parent.pop(check)
                    node.append(newn)
                    costcome.append(cost)
                    parent.append(pnode)
            else:
                node.append(newn)
                costcome.append(cost)
                parent.append(pnode)
        else:
            pass
    return newn,cost
def possiblemoves(i,init_cost,visited,node,costcome,parent):
    ActionMoveUp(i,init_cost,visited,node,costcome,parent)
    ActionMoveDown(i,init_cost,visited,node,costcome,parent)
    ActionMoveLeft(i,init_cost,visited,node,costcome,parent)
    ActionMoveRight(i,init_cost,visited,node,costcome,parent)
    ActionMoveRightDown(i,init_cost,visited,node,costcome,parent)
    ActionMoveRightUp(i,init_cost,visited,node,costcome,parent)
    ActionMoveLeftDown(i,init_cost,visited,node,costcome,parent)
    ActionMoveLeftUp(i,init_cost,visited,node,costcome,parent)


def backtrack(enode, visited, newparent, startx, starty, newegoal):
    while True:
        if enode in visited:
            # If done, we are gonna get status as True
            egoal_i = visited.index(enode)
            # After goal is reached, goal is the new parent
            enode = newparent[egoal_i]
            newegoal.append(enode)
            if enode == [float(startx), float(starty)]:
                print("Goal Reached")
                break
def visualise(newegoal,visited):
    # explored,ind=obs_coord()
    index=1
    explored=[]
    for x in range(0,601):
        for y in range(0, 251):
            i=list_of_obs(x,y)
            if i==1:
                explored.append([x,y])
    state=np.array(explored)
    explored=state*index
    visited_buffer = np.array(visited)
    visited=visited_buffer*index
    visited_buffer1 = np.array(newegoal)
    newegoal=visited_buffer1*index
    pygame.init()
    display=pygame.display.set_mode((600,250))
    pygame.display.set_caption("Dijkstra ") 
    done = False
    HexV = []
    HexV1=[]
    center1 = [300,125]
    center = [300,125]
    side_length =65
    side_length1=75
    Trianlge=[(460,25),(460,225),(510,125)]
    obs=[]
    clock = pygame.time.Clock()
    index=1
    print ("reached  a goal !!!!!!!!!!!!!!!!!!!")
    while not done:
        # fill the obstacles
        for i in explored:
            pygame.draw.rect(display, (255,255,255), [i[0],250*index-i[1],1,1])
        pygame.display.flip()
        for i in range(6):
            angle_deg = 60 * i - 30
            angle_rad = math.pi / 180 * angle_deg
            x = center[0] + side_length1 * math.cos(angle_rad)
            y = center[1] + side_length1 * math.sin(angle_rad)
            x1 = center1[0] + side_length * math.cos(angle_rad)
            y1 = center1[1] + side_length * math.sin(angle_rad)
            HexV.append((x1,y1))
            HexV1.append((x,y))
        color1 = (255,255,0)  # change color to yellow
        obs.append(pygame.draw.rect(display, color1, pygame.Rect(100, 145, 50, 100)))
        obs.append(pygame.draw.rect(display, color1, pygame.Rect(100, 5, 50, 100)))
        obs.append(pygame.draw.polygon(display,color1,HexV))
        obs.append(pygame.draw.polygon(display,color1,Trianlge))
        pygame.display.update()
        # fill the traversed nodes will green
        for i in visited:
            pygame.time.wait(1)
            pygame.draw.rect(display, (0,255,0), [i[0],250*index-i[1],1,1])
            display.blit(display,(0,0))
            pygame.display.flip()
            pygame.display.update()
        # draw the shortest path in blue
        for j in newegoal[::-1]:
            pygame.time.wait(1)
            pygame.draw.rect(display, (0,0,255), [j[0], 250*index-j[1], 1,1])
            pygame.display.flip()
            
                
        pygame.display.flip()
        done = True
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False 
                pygame.display.flip()
        done = True
        display.blit(display,(0, 0))
        pygame.display.update()
    pygame.quit()

def djikstra(pnode,enode,startx,starty):
    #We define calculation for node
    node=[]
    node.append(pnode)
    parents=[]
    #initialsing new parent when old curr is popped
    parents.append(pnode)
    costcome=[]
    visited=[]
    #Let the cost be zero initally
    cost=float(0)
    costcome.append(cost)
    newparent=[]
    newegoal=[]
    newegoal.append(enode)
    n=0
    init_cost=0
    count=0
    print("Starting Djikstra Algorithm and Exploring nodes")
    while enode not in visited:
        possiblemoves(node[n],init_cost,visited,node,costcome,parents)
        #Check visited
        visited.append(node[n])
        # print(visited)
        #Once visited, we append it as new parent
        newparent.append(parents[n])
        #We pop the parent ie our pnode from path to move
        node.pop(n)
        costcome.pop(n)
        parents.pop(n)
        count+=1
        if len(costcome)!=0:
            init_cost=min(costcome)
            ind=costcome.index(init_cost)
            n=ind
    print("Node Visited:",len(visited))
    backtrack(enode, visited, newparent, startx, starty, newegoal)
    visualise(newegoal,visited)

print("#######################################DIJKSTRA'S ALGORITHM########################################################")
startvalx=float(input("input x coordinate for initial node"))
startvaly=float(input("input y coordinate for initial node"))
goalvalx=float(input("input x coordinate for goal node"))
goalvaly=float(input("input y coordinate for goal node"))
pnode = [startvalx,startvaly]
egoal=[goalvalx,goalvaly]
search(pnode)
end(egoal)
djikstra(pnode,egoal,startvalx,startvaly)
    