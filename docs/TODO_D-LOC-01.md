# TODO List — D-LOC-01 (FR-LOC-01)

> Phase: RED · Layer: entity · Track: Logic(D-*)
> 이번 RED 묶음: **D-LOC-01** — 빈칸 좌표를 row-major 순서로 수집 (`find_blanks(grid)`)
> 상위 문서: [PRD.md](PRD.md) · 작성일: 2026-06-04

---

## 1. C2C 추적 (Rule 1~3)

PRD 인용 (`docs/PRD.md`)
- [ ] §5.1 Rule 근거 확인 — *"빈칸(0) 하나라도 있으면 → `무효(미완성)`"* (L35)
- [ ] §2 Output 근거 확인 — *"무효 시 **틀린 줄의 위치 목록**"* (L18)
- [ ] §3.2 성공기준 근거 확인 — *"손 검산 없이 즉시 유효/무효"* (L22)

To-Do (판단 포함 1개)
- [ ] 격자 각 칸이 0인지 **판단**해, 빈칸 좌표를 row-major(행 우선·동일 행은 열 오름차순)로 수집한다.

Test ID → Given / When / Then
- [ ] **D-LOC-01**
  - **Given**: 빈칸(0) 2개를 (1,2)·(3,4)에 둔 4×4 격자 G1
  - **When**: `find_blanks(grid)` 호출
  - **Then**: `[(1,2),(3,4)]` — 1-index 좌표를 row-major 순서로 정확히 반환 (개수·순서·값 일치)

---

## 2. Track B (D-*) RED 설계표

| Test ID | 대상 함수 | Given→Then | Invariant | Expected RED Failure |
| --- | --- | --- | --- | --- |
| D-LOC-01 | `find_blanks(grid)` (entity) | 빈칸 2개 G1 → `[(1,2),(3,4)]` row-major 반환 | 좌표 1-index(row,col∈1..4) · blank ⇔ cell==0 · 출력은 row-major 정렬 · 순수함수(부수효과 0) | `ModuleNotFoundError`/`ImportError` — entity 모듈·함수 미존재(src 미생성) |

---

## 3. 테스트 플랜

- [ ] **파일**: `tests/entity/test_d_loc_01.py` *(RED 스켈레톤 단계에서 생성)*
- [ ] **test 함수명 후보**
  - [ ] `test_d_loc_01_blank_coords_row_major` (주)
  - [ ] `test_d_loc_01_returns_empty_when_no_blank`
  - [ ] `test_d_loc_01_multiple_blanks_same_row`
- [ ] **conftest 픽스처 (로직 無)**
  - [ ] `g1_grid` → 빈칸 2개 박힌 4×4 리터럴만 반환
  - [ ] `full_grid` → 빈칸 0개 리터럴
  - [ ] (탐색/정렬 코드 절대 포함 금지 — 픽스처는 순수 데이터만)
- [ ] **pytest 명령**
  ```bash
  python -m pytest tests/entity/test_d_loc_01.py::test_d_loc_01_blank_coords_row_major -v
  ```
- [ ] **RED 묶음 범위**: 이번 묶음 = **D-LOC-01 단일 ID** (FR-LOC-01). 추가 ID 없음

---

## 4. ECB·Mock 점검

- [ ] Logic Track → Domain Mock **금지** — 실제 격자 리터럴로 검증, Domain Mock 없음
- [ ] entity **E001~E005 emit 금지** — 빈칸 좌표 수집은 순수 도메인 계산. `E001~E007`은 boundary 전용(U-* 표 책임)
- [ ] 의존 방향 — `entity → *` import 없음 (단방향 준수)
- [ ] 기타 금지 — `src/` 미수정 · GREEN/REFACTOR 미진입 · `skip`/`xfail` 미사용

---

## 다음 단계
- [ ] `/red-skeleton` 으로 진행 — D-LOC-01 실패 테스트 스켈레톤을 `tests/entity/test_d_loc_01.py`에 작성
