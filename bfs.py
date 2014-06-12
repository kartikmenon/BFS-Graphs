# Breadth-first Search
# Kartikeya Menon
# May 2013

from collections import deque


def bfs(start, goal):
    
    # Initialize dictionary as empty.
    backpointer = {}
    
    # Appending the starting vertex to the queue.
    q = deque()
    q.append(start)
    
    # The start has no previous vertex.
    backpointer[start] = None

    while not goal in backpointer:
        # Popping off the leftmost vertex in the queue.
        vertex1 = q.popleft()
        
        # Looping over the vertices in the adjacency list of the most recently popped-off vertex. 
        for vertex in vertex1.ad_list:
            
            # If the vertex hasn't been visited.
            if vertex not in backpointer:
                
                # Increment distance, set the backpointer of the adjacent vertex to the original vertex.
                backpointer[vertex] = vertex1
                
                # Add that vertex to the queue so the process can be repeated.
                q.append(vertex)
                
    # Initializing a list that will contain the list of vertices between start and goal, and starting it with the goal.
    path_list = []
    path_list.append(goal)
    
    # This loop stops when the next element in the backpointer is None, i.e., the starting vertex.
    while backpointer[path_list[-1]] != None:
        
        # Keep appending to the path list the backpointer of the last element in the path list. Eventually the last element
        # in this list will be the start vertex, i.e., None.
        path_list.append(backpointer[path_list[-1]])
        
    return path_list
