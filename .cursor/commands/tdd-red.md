# TDD RED — 실패 테스트 먼저

MagicSquare_1004 Dual-Track TDD의 **RED 단계만** 수행한다. 구현은 하지 않는다.

## 필수 선언
응답 첫 줄에 현재 상태를 선언한다.

```
Phase: red | Layer: entity|control|boundary | Track: Logic(D-*)|UI(U-*)
```

## 절차
1. **ID 확인** — 대상 테스트 ID를 고른다(`D-*`=Logic, `U-*`=UI). 계층 결정: 도메인 규칙=entity, 흐름/조합=control, 입출력=boundary.
2. **AAA 테스트 작성** — `tests/<layer>/test_d_*.py`(Logic) 또는 `tests/boundary/test_u_*.py`(UI)에 테스트 1개를 Arrange–Act–Assert로 작성.
   - 기대값은 도메인 불변식(`MAGIC_SUM=34`, `int[6]` 1-index)으로 단언.
3. **pytest FAIL 확인** — 실행해 그 테스트가 **실패**하는지 확인하고, 실패 메시지를 인용한다(import 실패/AssertionError).

## pytest 예시

```bash
# 대상 테스트 1개만 실행해 RED 확인
pytest tests/entity/test_d_collect_lines.py::test_D02_collect_10_lines -q

# 계층 단위로 확인
pytest tests/entity -q
```

## 보고
- 작성한 **테스트 ID**(`D-*`/`U-*`)와 대상 Layer/Track.
- **FAIL 요약** — 실패 종류(import/Assertion)와 메시지 한 줄.
- **변경 파일** — `tests/` 하위만 나열.

## 금지
- `src/` 수정(구현은 GREEN 단계에서).
- Logic Track에서 Domain 객체 **Mock 사용**.
- assert 완화·`skip`·`xfail`로 실패 회피.
