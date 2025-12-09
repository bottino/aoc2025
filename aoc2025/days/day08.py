import math
import networkx as nx

Box = tuple[int, int, int]
Connection = tuple[int, tuple[Box, Box]]


def part_1(input: str) -> int:
    boxes = _read_boxes(input)
    connections: set[Connection] = set()
    for a in boxes:
        for b in boxes:
            if a != b:
                pair = tuple(sorted((a, b)))
                connections.add((_dist(a, b), pair))
    connections = sorted(connections)

    MAX_CONNECTIONS = 10 if len(boxes) == 20 else 1000  # example vs input
    pairs = [c[1] for c in connections[:MAX_CONNECTIONS]]

    G = nx.Graph()
    G.add_nodes_from(boxes)
    G.add_edges_from(pairs)

    NUM_LARGEST_CIRCUITS = 3
    largest_cc = [
        len(cc) for cc in sorted(nx.connected_components(G), key=len, reverse=True)
    ]

    solution = 1
    for cc in largest_cc[:NUM_LARGEST_CIRCUITS]:
        solution *= cc
    return solution


def _read_boxes(input: str) -> list[Box]:
    boxes = []
    for line in input.splitlines():
        row = tuple([int(char) for char in line.split(",")])
        boxes.append(row)
    return boxes


def _dist(a: Box, b: Box) -> float:
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2)
