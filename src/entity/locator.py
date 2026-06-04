"""빈칸 좌표 수집 — 순수 도메인 계산 (entity 계층).

ECB: entity는 boundary/control을 import 하지 않는다.
오류 코드(E001~E007)는 boundary 책임이므로 여기서 raise 하지 않는다.
"""

from entity.constants import BLANK_CELL, GRID_SIZE, INDEX_BASE


def find_blank_coords(grid):
    """격자에서 빈칸(BLANK_CELL) 좌표를 row-major 순서로 수집한다.

    좌표는 1-index `(row, col)` 튜플이며, 행 우선·동일 행은 열 오름차순이다.
    부수효과 없는 순수 함수.
    """
    coords = []
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if grid[row][col] == BLANK_CELL:
                coords.append((row + INDEX_BASE, col + INDEX_BASE))
    return coords
