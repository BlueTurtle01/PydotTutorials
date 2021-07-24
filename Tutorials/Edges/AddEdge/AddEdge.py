import pydot

# Create the graph
graph = pydot.Dot("my_graph", graph_type="graph", overlap=False, splines='true')

# An edge joins two nodes, hence we must first create two node - replace "Node Name" with your desired Node Title
graph.add_node(pydot.Node("Node 1"))
graph.add_node(pydot.Node("Node 2"))

# add_edge takes the form graph.add_edge(pydot.Edge(<Edge 1>, <Edge 2>))
graph.add_edge(pydot.Edge("Node 1", "Node 2"))

# Save the output
graph.write_png("AddEdge.png")
