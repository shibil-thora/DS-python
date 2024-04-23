graph = {
 '5' : ['3','7'],
 '3' : ['2', '4'],
 '7' : ['8'],
 '2' : [],
 '4' : ['8'],
 '8' : []
}

visited = []  
queue = []      

def bfs(visited, graph, node):  
    visited.append(node)
    queue.append(node)

    while queue:          
        m = queue.pop(0) 
        print (m, end = " ") 

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

 
print("Following is the Breadth-First Search")
bfs(visited, graph, '5')     




