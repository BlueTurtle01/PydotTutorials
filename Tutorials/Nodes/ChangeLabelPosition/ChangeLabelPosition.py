import pydot

# I like to use the full path for the image as it seems less error prone.
# Therefore, first we find the current path of this file and use that to locate the image - assuming the image,
# is in the same folder as this file.
import pathlib
current_path = pathlib.Path(__file__).parent.resolve()


# Create the graph
graph = pydot.Dot("my_graph", graph_type="graph", overlap=False, splines='true')


"""
Use labelloc argument.
'b' = bottom
't' = top
Images must be .png format.
"""

graph.add_node(pydot.Node("Node 1", image=(str(current_path) + "/" + "Flower.png"), labelloc="b"))
graph.add_node(pydot.Node("Node 2"))

# Add edge
graph.add_edge(pydot.Edge("Node 1", "Node 2"))

# Save the output
graph.write_png("AddNodeImage.png")
