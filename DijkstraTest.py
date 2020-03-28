# File: DijkstraTest.py

"""
This module extends the GraphConsoleTest program to test the
implementation of Dijkstra's algorithm.
"""

from graphtest import GraphConsoleTest
from dijkstra import applyDijkstra

class DijkstraTest(GraphConsoleTest):

    def __init__(self):
        GraphConsoleTest.__init__(self)

    def distancesCommand(self, scanner):
        """distances start -- Compute distance to each node from start"""
        start = self.scanNode(scanner)
        applyDijkstra(self.graph, start)
        for node in sorted(self.graph.getNodes(), key=getDistance):
            dstr = str(node.distance)
            if dstr.endswith(".0"):
                dstr = dstr[:-2]
            print(str(node) + ": " + dstr)

    def pathsCommand(self, scanner):
        """paths start -- Compute shortest path to each node from start"""
        start = self.scanNode(scanner)
        applyDijkstra(self.graph, start)
        for node in sorted(self.graph.getNodes(), key=getDistance):
            dstr = str(node.distance)
            if dstr.endswith(".0"):
                dstr = dstr[:-2]
            print(getPath(node) + " (" + dstr + ")")

    def pathCommand(self,scanner):
        """path start finish -- Compute shortest path to each node from start to finish"""
        start = self.scanNode(scanner)
        finish = self.scanNode(scanner)
        applyDijkstra(self.graph,start,finish)
        for node in sorted(self.graph.getNodes(), key=getDistance)
            dstr = str(node.distance)
            if dstr.endswith(".0"):
                dstr = dstr[:-2]
            print(getPath(node) + " (" + dstr + ")")

def getDistance(node):
    return node.distance

def getPath(node):
    if node.predecessor is None:
        return node.getName()
    else:
        return getPath(node.predecessor) + "->" + node.getName()
    
# Startup code

if __name__ == "__main__":
    DijkstraTest()
