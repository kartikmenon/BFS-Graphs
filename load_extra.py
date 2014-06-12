# Load graph function
# Kartikeya Menon
# May 2013

from vertex_extra import Vertex



dictionary = {}

def load_graph(file1):
    
    graph = open(file1, "r")

    
    # Making the first pass. Looping over the lines in dartmouth_graph.txt
    for line in graph:
        
        # Stripping the lines and turning each line into a list, with elements separated by semicolons.
        line = line.strip()
        graph_list = line.split(";")
        
        # Since the x, y coordinates are stored as one element in graph_list, 
        # I can split them up into a separate list by their separating comma.
        coordinate_list = graph_list[2].split(",")
        
        # Clearing up spaces
        coordinate_list[0] = coordinate_list[0].strip()
        coordinate_list[1] = coordinate_list[1].strip()
        
        # Creating the vertex object with the name, x, y coordinates and no adjacency list yet.
        vertex = Vertex(graph_list[0], coordinate_list[0], coordinate_list[1])
        
        # Putting each new vertex object into the dictionary initialized above.
        dictionary[vertex.name] = vertex

        
    # Closing and reopening files in between looping over dartmouth_graph.txt
    graph.close()
    graph = open(file1, "r")
    
    # Making the second pass.
    for line in graph:
        
        # Repeating the process so I can access the names in order of lines in the file.
        line = line.strip()
        graph_list = line.split(";")
        
        # Grabbing the name of each vertex and creating a list of the vertexes adjacent to it.
        # (The adjacent vertices will be separated by commas in the second list item of graph_list)
        vertex_name = graph_list[0]
        adjacent_list = graph_list[1].split(",")
        
        # Getting the current vertex out of the dictionary.
        current_vertex = dictionary[vertex_name]
        
        # Looping over all of the adjacent vertices.
        for vertex in adjacent_list:
            
            # Removing spaces from the names, finding the adjacent vertices in the dictionary, and 
            # adding them to the relevant adjacency list of the current vertex.
            vertex = vertex.strip()
            adjacent_vertex = dictionary[vertex]
            
            current_vertex.ad_list.append(adjacent_vertex)
    
    return dictionary
