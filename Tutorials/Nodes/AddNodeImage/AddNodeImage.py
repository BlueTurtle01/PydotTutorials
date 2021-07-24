import pydot

# I like to use the full path for the image as it seems less error prone.
# Therefore, first we find the current path of this file and use that to locate the image - assuming the image,
# is in the same folder as this file.
import pathlib
current_path = pathlib.Path(__file__).parent.resolve()


# Create the graph
graph = pydot.Dot("my_graph", graph_type="graph", overlap=False, splines='true')


"""
Use image argument.

The default values are to size the node to the image size. From looking at the output we can see that it
is much too large and makes the other nodes difficult to read. In addition to this we still have the node text name
on top of the node image. Both of these will be changed in separate tutorials.

Images must be .png format.
"""

graph.add_node(pydot.Node("Node 1", image=(str(current_path) + "/" + "Flower.png")))
graph.add_node(pydot.Node("Node 2"))

# Add edge
graph.add_edge(pydot.Edge("Node 1", "Node 2"))

# Save the output
graph.write_png("AddNodeImage.png")
