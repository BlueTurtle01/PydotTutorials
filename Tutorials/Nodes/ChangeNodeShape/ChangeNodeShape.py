import pydot

# Create the graph
graph = pydot.Dot("my_graph", graph_type="graph", overlap=False, splines='true')

# Use the shape argument.
# Some possible shapes are; 'rectangle', 'circle', 'triangle', 'star'.
# More Shapes can be found at: https://graphviz.org/doc/info/shapes.html
# Default value: 'rectangle'.
graph.add_node(pydot.Node("Node 1", shape='star'))
graph.add_node(pydot.Node("Node 2"))

# Add edge
graph.add_edge(pydot.Edge("Node 1", "Node 2"))

# Save the output
graph.write_png("ChangeNodeShape.png")
