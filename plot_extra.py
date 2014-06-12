# Program to draw vertices on a map
# Kartikeya Menon
# May 2013

from cs1lib import *
from vertex_extra import Vertex
from load_extra import load_graph
from bfs import bfs
from math import *

NAPTIME = 1./50
WINDOW_HEIGHT = 1012
WINDOW_WIDTH = 811
Y_SHIFT = 20
PIXEL_FOOT_CONVERSION = 3
FEET_PER_MINUTE = 4.265 * 60 # Seconds/minute

dictionary = load_graph("graph_extra.txt")

def draw_facts():
    disable_stroke()
    set_stroke_color(0, 0, 0)
    set_fill_color(0.03, 0.46, 0.4)
    draw_rectangle(0, 0, 400, 80)
    set_font_size(20)
    enable_stroke()
    draw_text("Distance:", 10, 20)
    draw_text("Walking time:", 10, 40)

def distance(x1, x2, y1, y2):
    return sqrt((x2-x1)**2 + (y2 - y1)**2)

    
def map_dartmouth():
    

    # Loading the map
    graph = load_image("dartmouth_map.png")
    draw_image(graph, 0, 0)
    foco = load_image("53atdusk.jpg")
    
    # Initializing some variables. When nothing is clicked, the vertices will register as not found.
    start_found = False
    goal_found = False
    start_vertex_name = None
    end_vertex_name = None
    
    draw_facts()
    
    #Main graphics loop.
    while not window_closed():
        
        draw_facts()
        # Looping through all of the vertices in the dictionary.
        for vertex in dictionary:
            draw_facts()
            # Making the name of the vertex show up when you pass your mouse over it.
            set_font_size(15)
            enable_smoothing()

            if dictionary[vertex].on_vertex(mouse_x(), mouse_y()):
                dictionary[vertex].print_name(int(dictionary[vertex].x), int(dictionary[vertex].y) - Y_SHIFT)
                
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
                draw_facts()
            
            # This keeps all of the vertices other than the start vertex red and the start vertex blue.
            if start_found == True and vertex != start_vertex_name:
                
                dictionary[start_vertex_name].draw(1, 0, 0) # Red
                dictionary[vertex].draw(0, 0, 1) # Blue
                draw_facts()
            
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
                
            if start_found == True and goal_found == True:
                
                # Making a list out of the start and end points, calling BFS.
                path = bfs(start, goal)
        
                # Going through all of the vertices of the path list, created by BFS.
                for vertex in path[:-1]:
                    
                    # Draw the vertex and the edges. Have to increment the edges so they draw properly.
                    vertex.draw(1, 0, 0)
                    vertex.draw_edge(path[counter], 1, 0, 0)
                    counter = counter + 1
                    
                draw_facts()
                enable_smoothing()
                d = PIXEL_FOOT_CONVERSION * int(distance(int(start.x), int(goal.x), int(start.y), int(goal.y)))
                draw_text(str(d) + " ft", 100, 20)
                draw_text(str(int(d / FEET_PER_MINUTE)) + " min", 135, 40)
                draw_text("Path: " + str(start.name) + " to " + str(goal.name), 10, 60)
                
                if dictionary[goal.name] == dictionary["Foco"] and not dictionary[start.name] == dictionary["Foco"]:
                    clear()
                    draw_image(foco, 75, 95)
                    set_font_size(40)
                    draw_text("You've arrived at Foco!", 100, 80)
                
                
                
        # Standard graphics stuff
        request_redraw()
        sleep(NAPTIME)

    
start_graphics(map_dartmouth, "Campus Map", WINDOW_HEIGHT, WINDOW_WIDTH)


