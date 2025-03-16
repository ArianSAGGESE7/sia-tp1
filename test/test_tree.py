from src.sokoban import Sokoban
from src.tree import bfs

basic_grid_with_objective = """
#######
#@$  .#
#   $ #
#   . #
#     #
#######
"""
def test_bfs():
    s_init = Sokoban()
    s_init.parse_grid(basic_grid_with_objective)
    s_finished = bfs(s_init)    
    assert s_finished.is_finished()
    assert s_finished.movements == "rrrd"
