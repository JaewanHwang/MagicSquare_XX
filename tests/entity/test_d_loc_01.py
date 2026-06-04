from _approval import assert_matches_golden
from entity.locator import find_blank_coords


def _format_coords(coords):
    """좌표 목록을 golden 포맷(1-index, 줄당 'row,col')으로 고정한다."""
    return "\n".join(f"{row},{col}" for row, col in coords)


class TestDLoc01:
    def test_d_loc_01_blank_coords_row_major(self, grid_g1):
        # Given: G1 격자 (0이 2개 — (2,2), (3,3))
        # When: find_blank_coords(grid_g1) 호출
        # Then: [(2,2),(3,3)] 반환 (1-index, row-major)
        assert find_blank_coords(grid_g1) == [(2, 2), (3, 3)]

    def test_d_loc_01_blank_coords_golden(self, grid_g1):
        # Given: G1 격자 / When: find_blank_coords / Then: golden 기준 일치
        actual = _format_coords(find_blank_coords(grid_g1))
        assert_matches_golden(actual, "d_loc_01_g1.approved.txt")
