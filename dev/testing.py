import sys
sys.path.append('../')

from lib.graphLib.graph import Graph,Vertex,Edge,Table

import lib.graphLib.graphUtils as graphUtils

#create Graph
heystack = Graph()

v0 = Vertex("blue")
v1 = Vertex("red")
v2 = Vertex("blue")
v3 = Vertex("yellow")
v4 = Vertex("red")
v5 = Vertex("red")
v6 = Vertex("blue")
v7 = Vertex("blue")
v8 = Vertex("red")
v9 = Vertex("yellow")
v10 = Vertex("yellow")
v11 = Vertex("red")
v12 = Vertex("yellow")
v13 = Vertex("yellow")
v14 = Vertex("yellow")
v15 = Vertex("red")
v16 = Vertex("blue")
v17 = Vertex("blue")
v18 = Vertex("red")
v19 = Vertex("blue")
v20 = Vertex("red")
v21 = Vertex("blue")
heystack.addVertices([v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21])
heystack.addEdge(Edge(),v0.id,v1.id)
heystack.addEdge(Edge(),v1.id,v2.id)
heystack.addEdge(Edge(),v1.id,v3.id)
heystack.addEdge(Edge(),v3.id,v4.id)
heystack.addEdge(Edge(),v4.id,v5.id)
heystack.addEdge(Edge(),v5.id,v6.id)
heystack.addEdge(Edge(),v5.id,v7.id)
heystack.addEdge(Edge(),v4.id,v8.id)
heystack.addEdge(Edge(),v8.id,v9.id)
heystack.addEdge(Edge(),v9.id,v10.id)
heystack.addEdge(Edge(),v10.id,v11.id)
heystack.addEdge(Edge(),v11.id,v12.id)
heystack.addEdge(Edge(),v12.id,v13.id)
heystack.addEdge(Edge(),v13.id,v8.id)
heystack.addEdge(Edge(),v11.id,v18.id)
heystack.addEdge(Edge(),v14.id,v15.id)
heystack.addEdge(Edge(),v15.id,v16.id)
heystack.addEdge(Edge(),v15.id,v17.id)
heystack.addEdge(Edge(),v14.id,v18.id)
heystack.addEdge(Edge(),v18.id,v20.id)
heystack.addEdge(Edge(),v20.id,v19.id)
heystack.addEdge(Edge(),v20.id,v21.id)

v22 = Vertex(color="green")

heystack.group([v8,v9,v10,v11,v12,v13],v22)

graphUtils.drawGraph(heystack)


needle = Graph()
v1 = Vertex(color="red")
v2 = Vertex(color="yellow")
v3 = Vertex(color="yellow")
v4 = Vertex(color="red")
v5 = Vertex(color="yellow")
v6 = Vertex(color="yellow")
needle.addVertices([v1,v2,v3,v4,v5,v6])
needle.addEdge(Edge(), v1.id, v2.id)
needle.addEdge(Edge(), v2.id, v3.id)
needle.addEdge(Edge(), v3.id, v4.id)
needle.addEdge(Edge(), v4.id, v5.id)
needle.addEdge(Edge(), v5.id, v6.id)
needle.addEdge(Edge(), v6.id, v1.id)



#heystack = Graph()
#v1 = Vertex("blue")
#v2 = Vertex("red")
#v3 = Vertex("blue")
#heystack.addVertices([v1,v2,v3])
#heystack.addEdge(Edge(), v1.id, v2.id)
#heystack.addEdge(Edge(color="red"), v2.id, v3.id)
#heystack.addEdge(Edge(), v3.id, v1.id)
#
#needle = Graph()
#v1 = Vertex(color="blue")
#v2 = Vertex(color="red")
#v3 = Vertex(color="blue")
#needle.addVertices([v1,v2,v3])
#needle.addEdge(Edge(), v1.id, v2.id)
#needle.addEdge(Edge(color="red"), v2.id, v3.id)
#needle.addEdge(Edge(), v3.id, v1.id)