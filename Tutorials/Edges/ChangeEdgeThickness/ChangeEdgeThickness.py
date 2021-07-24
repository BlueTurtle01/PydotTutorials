import pydot

# Create the graph
graph = pydot.Dot("my_graph", graph_type="graph", overlap=False, splines='true')

# An edge joins two nodes, hence we must first create two node - replace "Node Name" with your desired Node Title
graph.add_node(pydot.Node("Node 1"))
graph.add_node(pydot.Node("Node 2"))

"""
Add the argument "penwidth" and a float for the width you desire.
This only changes this edge's thickness, there is also a tutorial for changing the default values that affects
the thickness of all edges.
"""
graph.add_edge(pydot.Edge("Node 1", "Node 2", penwidth=2.0))

# Save the output
graph.write_png("ChangeEdgeThickness.png")
