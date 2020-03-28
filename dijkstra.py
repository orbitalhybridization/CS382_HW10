# File: dijkstra.py

"""
This module implements Dijkstra's algorithm for solving the single-source
shortest-path problem.
"""

from pqueue import PriorityQueue
import math

# Implementation notes
# --------------------
# This implementation of Dijkstra's algorithm follows the logic of the
# pseudocode from CLRS and computes the minimum distance from the start
# node to every other node in the graph.  Unlike Dijkstra's original
# algorithm, it does not support stopping when a destination node is
# reached or visiting only a subset of the nodes.  It also uses an
# implementation of the PriorityQueue class that does not guarantee
# the logarithmic time performance of the raisePriority method.  Your
# job on the assignment is to repair these deficiencies.

def applyDijkstra(g, start, finish=None):
    """
    Applies Dijkstra's algorithm to the graph g, updating the
    distance from start to each node in g.
    """
    initializeSingleSource(g, start)
    finalized = set()
    pq = PriorityQueue()
    pq.enqueue(start)
    while not pq.isEmpty():
        node = pq.dequeue()
        finalized.add(start)
        if node == finish: #if we are at the finish node then we are all done!
            break
        for arc in node.getArcsFrom():
            n1 = arc.getStart()
            n2 = arc.getFinish()
            if n2 not in finalized:
                if n2.distance is math.inf: #check if the node is one that we have not visited before, in which case we will add it to the queue
                    pq.enqueue(n2)
                oldDistance = n2.distance
                relax(n1, n2, arc.getCost())
                if n2.distance < oldDistance:
                    pq.raisePriority(n2, n2.distance)

def initializeSingleSource(g, start):
    """Initialize the distance and predecessor attributes."""
    for node in g.getNodes():
        node.distance = math.inf
        node.predecessor = None
    start.distance = 0

def relax(n1, n2, cost):
    """Update the fields of n2 using the path n1 -> n2."""
    if n2.distance > n1.distance + cost:
        n2.distance = n1.distance + cost
        n2.predecessor = n1
