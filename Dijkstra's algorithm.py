#Give the pseudocode for Dijkstra's algorithm. (Hint this was given in the slides for Topological sorting and shortest path)  
def dijkstra(G, S):
    for each vertex v in G:
        distance[V] <- infinite
        previous [V] <-NULL
        if V!= S, add V to Priority Queue Q
    distance[S] <- 0
    while Q IS NOT EMPTY:
        U <- Extract MIN from Q
        for each unvisited neighbour V of U:
            tempDistance <- distance[U] + edge_weight(U, V)
            if tempDistance < distance[V]:
                distance[V] <- tempDistance
                previous [V] <-U
    return distance[], previous[]
  
