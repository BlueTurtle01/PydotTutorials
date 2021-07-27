# Import the pydot package, which includes the relevant method to create a graph
import pydot

# Create the graph
# first we define a name for our graph,
# and then a type - either "digraph" for a Directed Graph, or "graph" for an Undirected Graph
graph = pydot.Dot("my_graph", graph_type="graph")

# I have added a node so we can better see that our graph creation has worked. This is naturally a trivial
# graph as it has no edges, but as a minimum working example it suffices.
# Add the node - replace "Node Name" with your desired Node Title in string form
graph.add_node(pydot.Node("Node Name"))

# Save the output
graph.write_png("CreateGraph.png")
