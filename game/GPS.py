import pygame as pg
from .parkingSpot import parkingSpot
from .interestPoints import interestPoints
        
#############################################################################################
#inverted
"""
|---------B-----------------|-------------------C-------|
|                           |                           |
|                           |                           |
|                           |                           |
|                           F                           |
|                           |                           |
A                           |                           A
|                           |                           |
|------------G--------------------------------D---------|
"""
#############################################################################################
CITY = [[1, 1, 1, 1,   1, 1, 1, 1, 1, 1,    1, 1, 1, 1, 1, 1, 1, 1,     1, 1, 1, 1, 1, 1, 1,    1,     1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1,   1, 1, 1, 1, 1, 1,    1, 1, 1, 1, 1, 1, 1, 1,     1, 1, 1, 1, 1, 1, 1,    1,     1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1,   1, 1, 1, 1, 1, 1,    1, 1, 1, 1, 1, 1, 1, 1,     1, 1, 1, 1, 1, 1, 1,    1,     1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 0,   0, 0, 0, 0, 0, 'B',  0, 0, 0, 0, 0, 0, 0, 0,     0, 0, 0, 0, 0, 0, 0,    'C',   0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
        [1, 1, 1, 0,   1, 1, 1, 1, 1, 1,    1, 1, 1, 1, 1, 1, 1, 0,     1, 1, 1, 1, 1, 1, 1,    1,     1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0,   1, 1, 1, 1, 1, 1,    1, 1, 1, 1, 1, 1, 1, 0,     1, 1, 1, 1, 1, 1, 1,    1,     1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0,   1, 1, 1, 1, 1, 1,    1, 1, 1, 1, 1, 1, 1, 0,     1, 1, 1, 1, 1, 1, 1,    1,     1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0,   1, 1, 1, 1, 1, 1,    1, 1, 1, 1, 1, 1, 1, 0,     1, 1, 1, 1, 1, 1, 1,    1,     1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0,   1, 1, 1, 1, 1, 1,    1, 1, 1, 1, 1, 1, 1, 0,     1, 1, 1, 1, 1, 1, 1,    1,     1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0,   1, 1, 1, 1, 1, 1,    1, 1, 1, 1, 1, 1, 1, 0,     1, 1, 1, 1, 1, 1, 1,    1,     1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0,   1, 1, 1, 1, 1, 1,    1, 1, 1, 1, 1, 1, 1, 'G',   1, 1, 1, 1, 1, 1, 1,    1,     1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0,   1, 1, 1, 1, 1, 1,    1, 1, 1, 1, 1, 1, 1, 0,     1, 1, 1, 1, 1, 1, 1,    1,     1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 'A', 1, 1, 1, 1, 1, 1,    1, 1, 1, 1, 1, 1, 1, 0,     1, 1, 1, 1, 1, 1, 1,    1,     1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0,   1, 1, 1, 1, 1, 1,    1, 1, 1, 1, 1, 1, 1, 0,     1, 1, 1, 1, 1, 1, 1,    1,     1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0,   0, 0, 0, 0, 0, 'F',  0, 0, 0, 0, 0, 0, 0, 0,     0, 0, 0, 0, 0, 0, 'E',  0,     0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
        [1, 1, 1, 1,   1, 1, 1, 1, 1, 1,    1, 1, 1, 1, 1, 1, 1, 1,     1, 1, 1, 1, 1, 1, 1,    1,     1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1,   1, 1, 1, 1, 1, 1,    1, 1, 1, 1, 1, 1, 1, 1,     1, 1, 1, 1, 1, 1, 1,    1,     1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1,   1, 1, 1, 1, 1, 1,    1, 1, 1, 1, 1, 1, 1, 1,     1, 1, 1, 1, 1, 1, 1,    1,     1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]




class Node():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):
    
    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] == 1:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)

class GPS:
    def __init__(self):
        self.interestPointsDic=self.createInterestPointsAndPaths()

    def createInterestPointsAndPaths(self):
        interestPointsDic = {}
        #Hospital
        parkingSpotA_0 = parkingSpot(0,11,2)
        parkingSpotA_1 = parkingSpot(1,10,2)
        parkingSpotA_2 = parkingSpot(2,9,2)
        parkingSpotA = []
        parkingSpotA.append(parkingSpotA_0)
        parkingSpotA.append(parkingSpotA_1)
        parkingSpotA.append(parkingSpotA_2)

        interestPointA = interestPoints('A',11,3, parkingSpotA)
        #Restaurant
        parkingSpotB_0 = parkingSpot(0,2,7)
        parkingSpotB_1 = parkingSpot(1,2,8)
        parkingSpotB_2 = parkingSpot(2,2,9)
        parkingSpotB = []
        parkingSpotB.append(parkingSpotB_0)
        parkingSpotB.append(parkingSpotB_1)
        parkingSpotB.append(parkingSpotB_2)
        interestPointB = interestPoints('B',3,9, parkingSpotB)
        #School
        parkingSpotC_0 = parkingSpot(0,2,24)
        parkingSpotC_1 = parkingSpot(1,2,25)
        parkingSpotC_2 = parkingSpot(2,2,26)
        parkingSpotC = []
        parkingSpotC.append(parkingSpotC_0)
        parkingSpotC.append(parkingSpotC_1)
        parkingSpotC.append(parkingSpotC_2)
        interestPointC = interestPoints('C',3,25, parkingSpotC)
        
        #Skyscrapper
        parkingSpotD_0 = parkingSpot(0,8,31)
        parkingSpotD_1 = parkingSpot(1,9,31)
        parkingSpotD_2 = parkingSpot(2,10,31)
        parkingSpotD = []
        parkingSpotD.append(parkingSpotD_0)
        parkingSpotD.append(parkingSpotD_1)
        parkingSpotD.append(parkingSpotD_2)
        interestPointD = interestPoints('D',9,32, parkingSpotD)
        #Building
        parkingSpotE_0 = parkingSpot(0,13,23)
        parkingSpotE_1 = parkingSpot(1,14,23)
        parkingSpotE_2 = parkingSpot(2,15,23)
        parkingSpotE = []
        parkingSpotE.append(parkingSpotE_0)
        parkingSpotE.append(parkingSpotE_1)
        parkingSpotE.append(parkingSpotE_2)
        interestPointE = interestPoints('E',14,24, parkingSpotE)

        #Court
        parkingSpotF_0 = parkingSpot(0,13,9)
        parkingSpotF_1 = parkingSpot(1,13,10)
        parkingSpotF_2 = parkingSpot(2,13,11)
        parkingSpotF = []
        parkingSpotF.append(parkingSpotF_0)
        parkingSpotF.append(parkingSpotF_1)
        parkingSpotF.append(parkingSpotF_2)
        interestPointF = interestPoints('F',14,10, parkingSpotF)

        #Market
        parkingSpotG_0 = parkingSpot(0,7,16)
        parkingSpotG_1 = parkingSpot(1,8,16)
        parkingSpotG_2 = parkingSpot(2,9,16)
        parkingSpotG = []
        parkingSpotG.append(parkingSpotG_0)
        parkingSpotG.append(parkingSpotG_1)
        parkingSpotG.append(parkingSpotG_2)
        interestPointG = interestPoints('G',8,17, parkingSpotG)




        interestPointsDic['A'] = interestPointA
        interestPointsDic['B'] = interestPointB
        interestPointsDic['C'] = interestPointC
        interestPointsDic['D'] = interestPointD
        interestPointsDic['E'] = interestPointE
        interestPointsDic['F'] = interestPointF
        interestPointsDic['G'] = interestPointG



        #A is 11,3(cause it is inverted)
        #B is 3,9 (cause it is inverted)
        #C is 3,25 (cause it is inverted)
        #D is 9,32 (cause it is inverted)
        #E is 14,24 (cause it is inverted)
        #F is 14,10 (cause it is inverted)
        #G is 8,17 (cause it is inverted)

        #(y,x)
        

        return interestPointsDic
