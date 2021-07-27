import pydot

# Create the graph
# include the "bgcolor" argument with a string value.
graph = pydot.Dot("my_graph", graph_type="graph", bgcolor="yellow")

# I have added a node so we can better see that our graph creation has worked. This is naturally a trivial
# graph as it has no edges, but as a minimum working example it suffices.

# Add the node - replace "Node Name" with your desired Node Title in string form
graph.add_node(pydot.Node("Node Name"))

# Save the output
graph.write_png("CreateGraph.png")
