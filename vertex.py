b# Lab 4 vertex class
# Kartikeya Menon
# May 2013
from cs1lib import *

VERTEX_RADIUS = 10
EDGE_WIDTH = 2

class Vertex:
    
    # Instance variables
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.ad_list = [] # Initially, no vertices in the adjacency list.
        
    

    def __str__(self):
        
        # Starting a variable as an empty string.
        names = ""
        # Looping over the list and adding the names of the vertices to the variable.
        for vertex in range(len(self.ad_list) - 1):
            names = names + self.ad_list[vertex].name + ", "

        # Manually adding the last vertex name to the list to the variable to avoid having a comma at the end.
        names = names + self.ad_list[-1].name
        
        return self.name + "; " + "Location: " + str(self.x) + ", " + str(self.y) + "; " + \
            "Adjacent vertices: " + str(names)

    # Drawing an individual vertex.
    def draw(self, r, g, b):
        set_fill_color(r, g, b)
        disable_stroke()
        enable_smoothing()
        draw_circle(int(self.x), int(self.y), VERTEX_RADIUS)
    
    # Drawing an edge between some other vertex and the current one.
    def draw_edge(self, other_vertex, r, g, b):
        enable_stroke()
        set_stroke_color(r, g, b)
        set_stroke_width(EDGE_WIDTH)

        draw_line(int(self.x), int(self.y), int(other_vertex.x), int(other_vertex.y))
    
    # Drawing the whole list.
    def draw_ad_list(self, r, g, b):
        # Looping over the object references in the adjacency list
        # and drawing an edge between the current vertex and all of the other vertices.
        for vertex in range(len(self.ad_list)):
            self.draw_edge(self.ad_list[vertex], r, g, b)
    
    # Just a test to see if some coordinates (i.e., the mouse's coordinates) are in the square surrounding a vertex.
    def on_vertex(self, x, y):
        return (int(self.x) - VERTEX_RADIUS < x < int(self.x) + VERTEX_RADIUS) and\
        (int(self.y) - VERTEX_RADIUS < y < int(self.y) + VERTEX_RADIUS)
    

