# Stubs for scipy.spatial.kdtree (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

def minkowski_distance_p(x: Any, y: Any, p: int = ...): ...
def minkowski_distance(x: Any, y: Any, p: int = ...): ...

class Rectangle:
    maxes: Any = ...
    mins: Any = ...
    def __init__(self, maxes: Any, mins: Any) -> None: ...
    def __repr__(self): ...
    def volume(self): ...
    def split(self, d: Any, split: Any): ...
    def min_distance_point(self, x: Any, p: float = ...): ...
    def max_distance_point(self, x: Any, p: float = ...): ...
    def min_distance_rectangle(self, other: Any, p: float = ...): ...
    def max_distance_rectangle(self, other: Any, p: float = ...): ...

class KDTree:
    data: Any = ...
    leafsize: Any = ...
    maxes: Any = ...
    mins: Any = ...
    tree: Any = ...
    def __init__(self, data: Any, leafsize: int = ...) -> None: ...
    class node:
        def __lt__(self, other: Any): ...
        def __gt__(self, other: Any): ...
        def __le__(self, other: Any): ...
        def __ge__(self, other: Any): ...
        def __eq__(self, other: Any): ...
    class leafnode(node):
        idx: Any = ...
        children: Any = ...
        def __init__(self, idx: Any) -> None: ...
    class innernode(node):
        split_dim: Any = ...
        split: Any = ...
        less: Any = ...
        greater: Any = ...
        children: Any = ...
        def __init__(self, split_dim: Any, split: Any, less: Any, greater: Any) -> None: ...
    def __build(self, idx: Any, maxes: Any, mins: Any): ...
    def __query(self, x: Any, k: int = ..., eps: int = ..., p: int = ..., distance_upper_bound: Any = ...): ...
    def query(self, x: Any, k: int = ..., eps: int = ..., p: int = ..., distance_upper_bound: Any = ...): ...
    def __query_ball_point(self, x: Any, r: Any, p: float = ..., eps: int = ...): ...
    def query_ball_point(self, x: Any, r: Any, p: float = ..., eps: int = ...): ...
    def query_ball_tree(self, other: Any, r: Any, p: float = ..., eps: int = ...): ...
    def query_pairs(self, r: Any, p: float = ..., eps: int = ...): ...
    def count_neighbors(self, other: Any, r: Any, p: float = ...): ...
    def sparse_distance_matrix(self, other: Any, max_distance: Any, p: float = ...): ...

def distance_matrix(x: Any, y: Any, p: int = ..., threshold: int = ...): ...
