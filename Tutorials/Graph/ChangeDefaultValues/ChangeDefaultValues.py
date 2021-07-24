import pydot

# Create the graph
graph = pydot.Dot("my_graph", graph_type="graph", overlap=False, splines='true')

# Use any of the normal attributes that we have looked at for single edges and set them as defaults for the whole graph
# Naturally you can then change any individual node to a different value on a case-by-case basis.
graph.set_edge_defaults(style='dashed', color='blue')

# The same can be said for nodes.
graph.set_node_defaults(shape='rectangle', color='red', fontname='arial')

graph.add_node(pydot.Node("Node 1"))
graph.add_node(pydot.Node("Node 2"))

# add_edge takes the form graph.add_edge(pydot.Edge(<Edge 1>, <Edge 2>))
graph.add_edge(pydot.Edge("Node 1", "Node 2"))

# Save the output
graph.write_png("ChangeDefalutValues.png")
