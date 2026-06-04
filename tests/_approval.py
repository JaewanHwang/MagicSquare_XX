"""Golden Master(Approval) 테스트 헬퍼.

`assert_matches_golden(actual, relative_path)`:
- 실제 출력(actual)을 `tests/golden/<relative_path>` 기준 파일과 비교한다.
- 환경변수 `UPDATE_GOLDEN=1`이면 기준 파일을 생성/갱신만 하고 통과한다.
- 그 외에는 기준 파일과 정확히 일치해야 하며, 불일치 시 diff를 함께 보고한다.

규칙: 기준 파일은 코드로만 생성한다(수동 편집으로 통과 우회 금지).
"""

import difflib
import os
from pathlib import Path

GOLDEN_ROOT = Path(__file__).parent / "golden"
UPDATE_ENV = "UPDATE_GOLDEN"


def _normalize(actual):
    """비교 가능한 문자열로 정규화한다(개행 끝 보정 포함)."""
    text = actual if isinstance(actual, str) else str(actual)
    if not text.endswith("\n"):
        text += "\n"
    return text


def _format_diff(expected, actual, golden_path):
    diff = difflib.unified_diff(
        expected.splitlines(keepends=True),
        actual.splitlines(keepends=True),
        fromfile=f"{golden_path} (approved)",
        tofile="actual",
    )
    return f"Golden mismatch: {golden_path}\n" + "".join(diff)


def assert_matches_golden(actual, relative_path):
    golden_path = GOLDEN_ROOT / relative_path
    normalized = _normalize(actual)

    if os.environ.get(UPDATE_ENV):
        golden_path.parent.mkdir(parents=True, exist_ok=True)
        golden_path.write_text(normalized, encoding="utf-8")
        return

    assert golden_path.exists(), (
        f"golden 파일 없음: {golden_path}\n"
        f"{UPDATE_ENV}=1 로 먼저 기준 파일을 생성하세요."
    )
    expected = golden_path.read_text(encoding="utf-8")
    assert normalized == expected, _format_diff(expected, normalized, golden_path)
