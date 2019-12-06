import networkx as nx

nodes = ["Product Rule",
         "Sum Rule",
         "Permutations",
         "r-Permutations",
         "Subsets",
         "r-Combinations",
         "Probability",
         "Occupancy Problems",
         "Pigeonhole Principle",
         "Induction Proofs",
         "Connectedness",
         "Graph Coloring",
         "Chromatic Polynomials",
         "Walks",
         "Trees",
         "Adjacency Matrix",
         "Representing Graphs in Computers",
         "Generating Functions",
         "Characteristic Roots",
         "Solving Recurrences",
         "MacLaurin Expansion",
         "Partial Fraction Decomposition"]

def main():
    g = nx.Graph()
    g.add_nodes_from(nodes)
    
    # Add edges node-by-node
    productRule = [("Product Rule", "Probability")]
    g.add_edges_from(productRule)
    
    rPermutations = [("r-Permutations", "Probability")]
    g.add_edges_from(rPermutations)
    
    probability = [("Probability", "Sum Rule"), ("Probability", "Permutations"), ("Probability", "r-Combinations")]
    g.add_edges_from(probability)
    
    pigeonholePrinciple = [("Pigeonhole Principle", "Subsets"), ("Pigeonhole Principle", "Occupancy Problems"), ("Pigeonhole Principle", "Induction Proofs")]
    g.add_edges_from(pigeonholePrinciple)
    
    subsets = [("Subsets", "Occupancy Problems")]
    g.add_edges_from(subsets)
    
    inductionProofs = [("Induction Proofs", "r-Combinations"), ("Induction Proofs", "Graph Coloring"), ("Induction Proofs", "Chromatic Polynomials"), 
                       ("Induction Proofs", "Connectedness"), ("Induction Proofs", "Generating Functions"), ("Induction Proofs", "Partial Fraction Decomposition")]
    g.add_edges_from(inductionProofs)
    
    graphColoring = [("Graph Coloring", "Walks"), ("Graph Coloring", "Trees"), ("Graph Coloring", "Connectedness"), ("Graph Coloring", "Chromatic Polynomials"), 
                     ("Graph Coloring", "Adjacency Matrix")]
    g.add_edges_from(graphColoring)
    
    adjacencyMatrix = [("Adjacency Matrix", "Connectedness"), ("Adjacency Matrix", "Representing Graphs in Computers")]
    g.add_edges_from(adjacencyMatrix)
    
    trees = [("Trees", "Connectedness"), ("Trees", "Walks")]
    g.add_edges_from(trees)
    
    partialFractions = [("Partial Fraction Decomposition", "Generating Functions"), ("Partial Fraction Decomposition", "MacLaurin Expansion")]
    g.add_edges_from(partialFractions)
    
    recurrences = [("Solving Recurrences", "Generating Functions"), ("Solving Recurrences", "Characteristic Roots")]
    g.add_edges_from(recurrences)
        
    return g

if __name__ == '__main__':
    main()
