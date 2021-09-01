#Give the pseudocode for Bellman Ford's algorithm. (Hint this was given in the slides for Topological sorting and shortest path)  
def bellmanFord(G, 5):
    for each vertex v in G:
        distance[V] <- infinite
        previous [V] <- NULL
    distancers1 <-0
    for each vertex v in G:
        for each edge (U,V) in G:
            tempDistance <- distance[U] + edge_weight(U, V)
            if tempDistance < distance[V]:
                distance[V] <- tempDistance
                previous [V] <-U
    for each edge (U,V) in G:
        if distance[U] + edge_weight(U, V) < distance[V]: 
            Error: Negative Cycle Exists
    return distance[], previous[]
  
