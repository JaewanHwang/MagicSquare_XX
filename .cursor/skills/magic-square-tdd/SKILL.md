---
name: magic-square-tdd
description: >-
  MagicSquare_XX Dual-Track TDD·ECB 개발 시 Agent가 따를 절차. 4×4 부분 마방진
  검증기(SquareValidator)를 entity/control/boundary 계층으로 구현할 때, RED→GREEN
  →REFACTOR 사이클·Logic/UI Track 분리·Mock 정책·E001~E007 오류 책임을 강제한다.
  Use when implementing or modifying MagicSquare_XX src/ or tests/ under TDD,
  또는 사용자가 D-*/U-* 테스트, ECB 계층, 마방진 검증 구현을 요청할 때.
---

# MagicSquare_XX — Dual-Track TDD · ECB

## 언제 이 Skill을 켜는가
- `src/{entity,control,boundary}` 또는 `tests/`에 코드를 추가/수정할 때.
- 마방진 검증 로직(10줄 합=34, 빈칸 2개, 1~16)을 TDD로 구현할 때.
- 사용자가 `D-*`(Logic)·`U-*`(UI) 테스트, RED/GREEN/REFACTOR를 언급할 때.
- 켜지 않는 경우: 문서(`Report/`, `docs/`)·설정만 수정하는 단순 작업.

## 시작 시 선언 (필수)
매 응답 첫 줄에 현재 상태를 명시한다.
`Phase: RED|GREEN|REFACTOR · Layer: entity|control|boundary · Track: Logic(D-*)|UI(U-*)`

## RED — 실패하는 테스트 먼저
1. `reference.md`에서 대상 `D-*`(또는 `U-*`) ID를 고른다.
2. 대상 계층 결정: 도메인 규칙=entity, 흐름/조합=control, 입출력=boundary.
3. Track 확정: entity/control→Logic, boundary→UI.
4. `tests/<layer>/test_d_*.py`(또는 `test_u_*.py`)에 테스트 1개 작성.
5. 기대값은 도메인 불변식(`MAGIC_SUM=34`, `int[6]` 1-index)으로 단언.
6. `pytest`로 실행해 **그 테스트가 실패함**을 확인(import/AssertionError).
7. 실패 메시지를 응답에 인용한다. assert 완화·skip·xfail 금지.

## GREEN — 최소 구현으로 통과
1. 실패 원인을 한 줄로 진단.
2. 대상 계층에 **통과에 필요한 최소 코드만** 작성.
3. ECB 의존 방향 준수: `boundary → control → entity`, `entity → *` import 금지.
4. `MAGIC_SUM`/`16` 등 상수는 SSOT 모듈에서 import (리터럴 산재 금지).
5. 해당 테스트만 실행해 GREEN 확인.
6. 전체 `pytest` 실행해 회귀 없음 확인.
7. 통과한 테스트 ID와 결과를 보고.

## REFACTOR — 통과 유지하며 정리
1. 중복 제거·명명 정리(동작 변경 금지).
2. 계층 경계 위반(특히 `entity`의 외부 import) 점검·제거.
3. 매직 리터럴을 SSOT 상수로 치환.
4. 오류 처리 책임이 올바른 계층에 있는지 확인(아래 표).
5. `pytest` 전체 재실행해 여전히 GREEN인지 확인.
6. assert를 약화시킨 곳이 없는지 점검.
7. 리팩터링 범위와 테스트 결과를 보고.

## Logic Track vs UI Track
| 구분 | Logic Track | UI Track |
| --- | --- | --- |
| 대상 계층 | entity, control | boundary |
| 테스트 ID | `D-*` | `U-*` |
| 파일명 | `tests/{entity,control}/test_d_*.py` | `tests/boundary/test_u_*.py` |
| Domain Mock | **금지**(실제 객체로 검증) | **허용** |
| 초점 | 규칙·계산 정확성, 완전성(10줄 누락 0) | 입력 검증·출력 포맷·오류 코드 |

## ECB · Mock · 오류 코드 규칙
- 의존 방향: `boundary → control → entity` (단방향). `entity → *` import **금지**.
- 계층 책임: entity=순수 도메인, control=흐름/조합, boundary=입출력/검증.
- Mock: Logic Track에서 Domain 객체 Mock 금지. UI Track(boundary)만 Mock 허용.
- 오류 코드: `E001~E007`은 **boundary 전용**. `entity`는 `E001~E005` 처리 **금지**.
- 상수: `MAGIC_SUM=34`, 범위 `1~16`은 SSOT로 단일 관리.

## 완료 보고 항목
1. Phase / Layer / Track (최종 상태).
2. 추가·수정한 테스트 ID 목록(`D-*`/`U-*`)과 RED→GREEN 전이.
3. 변경한 `src/` 파일과 핵심 구현 요지.
4. `pytest` 실행 결과(통과/실패 수, 회귀 없음 여부).
5. ECB·Mock·오류 코드 규칙 준수 확인.
6. 다음 RED 후보 테스트 ID.

## Test / Review Loop — 어떤 pytest를 언제
| 시점 | 명령 | 목적 |
| --- | --- | --- |
| RED 직후 | `pytest tests/<layer>/test_d_*.py::<id> -q` | 대상 테스트 실패 확인 |
| GREEN 중 | `pytest tests/<layer> -q` | 해당 계층 통과 확인 |
| GREEN 끝 | `pytest -q` | 전체 회귀 없음 확인 |
| REFACTOR 후 | `pytest -q` | 동작 유지(GREEN) 재확인 |
| Logic만 | `pytest tests/entity tests/control -q` | D-* 전체 |
| UI만 | `pytest tests/boundary -q` | U-* 전체 |

## 참고 자료
- 대상 `D-*` 테스트 ID 목록: [reference.md](reference.md)
