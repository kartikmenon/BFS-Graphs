# Program to draw vertices on a map
# Kartikeya Menon
# May 2013

from cs1lib import *
from load_graph import load_graph
from bfs import bfs

NAPTIME = 1./50

dictionary = load_graph("dartmouth_graph.txt")


def map_DM():
    
    # Loading the map
    map1 = load_image("dartmouth_map.png")
    draw_image(map1, 0, 0)
    
    # Initializing some variables. When nothing is clicked, the vertices will register as not found.
    start_found = False # start_found and goal_found are Booleans that will check if a start or goal has been chosen.
    goal_found = False
    start = None # These will store the actual vertex objects.
    goal = None
    
    
    #Main graphics loop.
    while not window_closed():
        
        # Looping through all of the vertices in the dictionary.
        for vertex in dictionary:
            
            # Drawing all of the vertices and edges between them.
            # Didn't want to make another function to do this, as it's only two lines.
            dictionary[vertex].draw(0, 0, 1)
            dictionary[vertex].draw_ad_list(0, 0, 1)
            
            # Finding the start vertex, conditions being that the mouse is on top of it and clicking.
            if dictionary[vertex].on_vertex(mouse_x(), mouse_y()) and mouse_down():
                    
                # Assigning two variables: one stores the name of the vertex (so it can be used to index dictionaries) and 
                # the other stores the actual vertex object.
                start_vertex_name = dictionary[vertex].name
                start = dictionary[vertex]
                
                # Drawing the relevant start vertex and assigning a Boolean saying that a start vertex has been picked.
                dictionary[start_vertex_name].draw(1, 0, 0)
                start_found = True
            
            # This keeps all of the vertices other than the start vertex red and the start vertex blue.
            if start_found == True and vertex != start_vertex_name:
                
                dictionary[start_vertex_name].draw(1, 0, 0) # Red
                dictionary[vertex].draw(0, 0, 1) # Blue

            
            # Same thing, but for the goal vertex. The goal vertex will only be chosen if a start vertex has been chosen.
            if start_found == True and dictionary[vertex].on_vertex(mouse_x(), mouse_y()):
                
                end_vertex_name = dictionary[vertex].name
                goal = dictionary[vertex]
                dictionary[end_vertex_name].draw(1, 0, 0)

                goal_found = True
            
            # So that the goal vertex will stay blue and the rest of the vertices will stay red.
            if goal_found == True and vertex != end_vertex_name:
                dictionary[end_vertex_name].draw(1, 0, 0)
                dictionary[vertex].draw(0, 0, 1)

            
            # Initializing a counter that I will use to loop through 
            counter = 1
            
            # If both the start vertex and the end vertex have been found, then call BFS on the assigned
            # start and end (goal) vertices. 
            if start_found == goal_found == True:
                
                # Making a list out of the start and end points, calling BFS.
                path = bfs(start, goal)
        
                # Going through all of the vertices of the path list, created by BFS.
                for vertex in path[:-1]:
                    
                    # Draw the vertex and the edges. Have to increment the edges so they draw properly.
                    vertex.draw(1, 0, 0)
                    vertex.draw_edge(path[counter], 1, 0, 0)
                    counter = counter + 1

        # Standard graphics stuff
        request_redraw()
        sleep(NAPTIME)
    
start_graphics(map_DM, "Campus Map", 1012, 811)


