import pydot

# I like to use the full path for the image as it seems less error prone.
# Therefore, first we find the current path of this file and use that to locate the image - assuming the image,
# is in the same folder as this file.
import pathlib
current_path = pathlib.Path(__file__).parent.resolve()


# Create the graph
graph = pydot.Dot("my_graph", graph_type="graph", overlap=False, splines='true')


"""
Use fixedsize argument to stop the image resizing to the node size. We also need to tell the image what size we
want it to be. width/height are in inches (not pixels), and accept floats.

Images must be .png format.
"""

graph.add_node(pydot.Node("Node 1", image=(str(current_path) + "/" + "Flower.png"), fixedsize="true",
                          width=2.0, height=2.0))

graph.add_node(pydot.Node("Node 2"))

# Add edge
graph.add_edge(pydot.Edge("Node 1", "Node 2"))

# Save the output
graph.write_png("AddNodeImage.png")
