# Import the pydot package, which includes the relevant method to create a graph
import pydot
import networkx

# Create the graph
graph = pydot.Dot("my_graph", graph_type="graph")

# Create a node
graph.add_node(pydot.Node("Node Name"))

# Save the output using the write_png method to a file
graph.write_png("SaveGraph.png")



# The below methods are taken from the official documentation: https://pypi.org/project/pydot.
# I have included them here to hopefully create a central place for all information RE Pydot
# and it is only just to give them appropriate credit.

# Save the output as a string that can be further passed to NetworkX
# As a string:
output_raw_dot = graph.to_string()
# Or, save it as a DOT-file:
graph.write_raw('SaveGraphDot.dot')

# As a bytes literal:
output_graphviz_dot = graph.create_dot()
# Or, save it as a DOT-file:
graph.write_dot('SaveGraphViz.dot')

my_networkx_graph = networkx.drawing.nx_pydot.from_pydot(graph)