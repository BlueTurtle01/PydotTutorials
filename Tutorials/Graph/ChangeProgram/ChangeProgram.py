import pydot

# Create the graph
graph = pydot.Dot("my_graph", graph_type="graph", overlap=False, splines='true')

# Add the node - replace "Node Name" with your desired Node Title
graph.add_node(pydot.Node("Node Name"))

# Save the output and included the "prog" argument - that takes a string.
# Default: dot.
# Possible values: "dot", "circo", "twopi", "fdp", "neato"
# With this trivial graph there will be no difference in the output but with a larger graph it is worth trying each
# program to decide on which you prefer.
graph.write_png("ChangeProg.png", prog="circo")
