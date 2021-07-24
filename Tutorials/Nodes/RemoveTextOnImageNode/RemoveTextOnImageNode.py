import pydot

# I like to use the full path for the image as it seems less error prone.
# Therefore, first we find the current path of this file and use that to locate the image - assuming the image,
# is in the same folder as this file.
import pathlib
current_path = pathlib.Path(__file__).parent.resolve()


# Create the graph
graph = pydot.Dot("my_graph", graph_type="graph", overlap=False, splines='true')

# The default values are to size the node to the image size. From looking at the output we can see that it
# still has the node name over the image. The easiest solution is to just remove the text.
# We do this by setting the "label" argument to empty. Naturally this does not remove the node name itself,
# but gives the appearance that it has, which is sufficient.
graph.add_node(pydot.Node("Node 1", image=(str(current_path) + "/" + "Elon.png"), label=""))
graph.add_node(pydot.Node("Node 2"))

# Add edge
graph.add_edge(pydot.Edge("Node 1", "Node 2"))

# Save the output
graph.write_png("RemoveTextOnImageNode.png")
