import pydot

# Create the graph
graph = pydot.Dot("my_graph", graph_type="graph", overlap=False, splines='true')


# Use color argument.
# Possible colours are basic names such as 'red', 'green', 'yellow', 'purple', 'orange'.
graph.add_node(pydot.Node("Node 1", color='red'))
graph.add_node(pydot.Node("Node 2"))

# Add edge
graph.add_edge(pydot.Edge("Node 1", "Node 2"))

# Save the output
graph.write_png("ChangeNodeLineColour.png")
