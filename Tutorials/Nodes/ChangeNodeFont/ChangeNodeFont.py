import pydot

# Create the graph
graph = pydot.Dot("my_graph", graph_type="graph", overlap=False, splines='true')

# Add the node - replace "Node Name" with your desired Node Title
graph.add_node(pydot.Node("Node Name", fontname='arial'))

# Save the output
graph.write_png("ChangeNodeFont.png")
