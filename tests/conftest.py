import pytest


@pytest.fixture
def grid_g1():
    """G1 격자 — 빈칸(0) 2개, 1-index 기준 (2,2)·(3,3) 위치.

    순수 데이터만 제공한다(탐색/정렬 로직 없음).
    값은 4×4 마방진에서 두 칸을 0으로 비운 형태.
    상수(34/16/4) import는 GREEN 단계에서 entity/constants.py 도입 시 적용.
    """
    return [
        [16, 3, 2, 13],
        [5, 0, 11, 8],
        [9, 6, 0, 12],
        [4, 15, 14, 1],
    ]
