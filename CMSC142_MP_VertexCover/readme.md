# Vertex Cover
[Tristan John P. Almonia](https://github.com/tpalmonia)\
CMSC 142 MP

## Introduction
### Important Terms
   1.   **GRAPH** - is a mathematical representation of a set of points, called *nodes or vertices*, which are interconnected by a set of lines called edges.
   2.   **VERTICES/NODES** - one of the *points* on which the graph is defined and which may be connected by graph edges.
   3.   **EDGE** - is one of the *connections* between the nodes (or vertices) of the network.
        -   **Undirected graphs** have edges that do not have a direction. The edges indicate a *two-way relationship*, in that each edge can be traversed in both directions.
        -   **Directed graphs** have edges with direction. The edges indicate a *one-way relationship*, in that each edge can only be traversed in a single direction. 
        -   Graph edges sometimes have **Weights**, which indicate the strength (or some other attribute) of each connection between the nodes.

### Background of the Problem
#### WHAT IS A VERTEX COVER?
-   A vertex cover of a graph is a set of vertices that includes at least one endpoint of every edge of the graph.
-   **FORMAL DEFINITION:** A vertex cover is a subset **_V’_** of the vertices of graph **_G = (V,E)_** such that for every edge **_(u,v) ∈ E_**, either **_u ∈ V’_** or **_v ∈ V’_**.
-   A minimum vertex cover is a vertex cover of smallest possible size.

#### PROPERTIES OF A VERTEX COVER
-   The set of all vertices is a vertex cover.
-   A set of vertices is a vertex cover if and only if its complement is an independent set.
-   Consequently, the number of vertices of a graph is equal to its minimum vertex cover number plus the size of a maximum independent set (Gallai 1959).

## Illustration
### Given a graph with eight (8) vertices labeled _V<sub>1</sub>, V<sub>2</sub>, ..., V<sub>8</sub>_
![Illustration1](https://github.com/210913-CMSC142-G/Tristan-code/blob/master/CMSC142_MP_VertexCover/images/illustration1.jpg?raw=true)

- ### *{V<sub>1</sub> , V<sub>3</sub> , V<sub>5</sub> , V<sub>6</sub> , V<sub>7</sub> , V<sub>8</sub> }* is a vertex cover.

![Illustration2](https://github.com/210913-CMSC142-G/Tristan-code/blob/master/CMSC142_MP_VertexCover/images/illustration2.jpg?raw=true)

- ### *{V<sub>2</sub> , V<sub>4</sub> , V<sub>5</sub> }* is a vertex cover.

![Illustration3](https://github.com/210913-CMSC142-G/Tristan-code/blob/master/CMSC142_MP_VertexCover/images/illustration3.jpg?raw=true)

- ### *{V<sub>2</sub> , V<sub>3</sub> , V<sub>8</sub> }* is NOT a vertex cover.

![Illustration4](https://github.com/210913-CMSC142-G/Tristan-code/blob/master/CMSC142_MP_VertexCover/images/illustration4.jpg?raw=true)

## Applications of Vertex Cover
1. ### Biology
   - Has seen potential in some fields of computational biology, synthetic biology, and metabolic engineering (elimination of repetitive DNA sequences model)
2. ### Security
   - A commercial establishment interested in installing the fewest possible closed circuit cameras covering all hallways (edges) connecting all rooms (nodes) on a floor

## **References**

- General Idea and Proof: https://www.geeksforgeeks.org/proof-that-vertex-cover-is-np-complete/
- Code 1 (Minimum Vertex Cover): https://www.geeksforgeeks.org/set-cover-problem-set-1-greedy-approximate-algorithm/
- Code 2 (Size): https://www.geeksforgeeks.org/vertex-cover-problem-set-2-dynamic-programming-solution-tree/