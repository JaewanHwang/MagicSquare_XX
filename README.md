# MagicSquare_XX

4×4 마방진(Magic Square) 학습 프로젝트.
**Mom Test → 문제 정의 → PRD → 구현**으로 이어지는 문제 중심(Problem-First) 워크플로우를 따른다.

## 한 줄 소개
Magic Square = 모든 행·열·대각선의 합이 같은 4×4 숫자 배열.
빈칸 2개(0)를 채워 1~16을 배치하고, 합이 34인지 **빠짐없이 즉시 판정**하는 것이 목표.

## 진짜 문제 (Mom Test 도출)
> 손으로 줄 단위 검산을 할 때 검사해야 할 **10개 줄(4행·4열·2대각선)** 중 하나를 빠뜨려도 즉시 판정되지 않아, 다 맞았다고 착각하고 넘어갔다가 뒤늦게 오답을 발견해 시간을 날린다.

근거(Mom Test 증거):
- "대각선 하나를 빼먹어서 **20분 날렸다**" — 비용
- "한 줄씩 손으로 더했지" → "**나중에** 틀린 걸 발견" — 판정 지연
- "**전에도 있었어**" — 반복 패턴

## 범위 (이번 프로젝트)
- ✅ 완성 격자가 마방진인지 **검증**(SquareValidator) — 10줄 합=34 판정
- ❌ 빈칸 자동 풀이(Solver), GUI, 1~16 중복/범위 검증은 범위 밖

## 핵심 사양
| 항목 | 내용 |
| --- | --- |
| Role | 마방진 검증기 |
| Goal | 10줄(4행+4열+2대각선) 누락 없이 합=34 판정 |
| Input | 4×4 정수 격자 (1~16, 빈칸은 0) |
| Output | `유효/무효` + 무효 시 틀린 줄 위치 목록 |

```
validate(grid: int[4][4]) -> { valid: bool, failedLines: Line[] }
```

## 성공 기준
1. **완전성** — 10개 줄 100% 검사(누락 0)
2. **즉시 판정** — 손 검산 없이 입력 즉시 유효/무효
3. **재현 방지** — 같은 격자는 항상 같은 판정

## RED 단계 체크리스트 (D-LOC-01 / FR-LOC-01)
> Phase: RED · Layer: entity · Track: Logic(D-*) · 상세: [docs/TODO_D-LOC-01.md](docs/TODO_D-LOC-01.md)

- [ ] **C2C 추적** — PRD §5.1/§2/§3.2 인용 + 판단 포함 To-Do 1개 + D-LOC-01 Given/When/Then 정리
- [ ] **RED 설계표** — `find_blanks(grid)` 대상 / Invariant(좌표 1-index·blank⇔0·row-major) / Expected RED Failure 확정
- [ ] **테스트 플랜** — `tests/entity/test_d_loc_01.py` 함수명·conftest 픽스처(`g1_grid`,`full_grid`)·pytest 명령 정의
- [ ] **ECB·Mock 점검** — Domain Mock 금지 · entity E001~E005 emit 금지 · `entity → *` import 없음
- [ ] **RED 스켈레톤 작성** — `/red-skeleton`으로 `test_d_loc_01_blank_coords_row_major` 실패 테스트 생성
- [ ] **FAIL 확인** — `python -m pytest tests/entity/test_d_loc_01.py::test_d_loc_01_blank_coords_row_major -v` 로 `ModuleNotFoundError`/`ImportError` 인용

## 프로젝트 구조
```
MagicSquare_XX/
├─ README.md                  # 본 문서
├─ Report/                    # 문제 정의 보고서
│  ├─ 01.MagicSquare_ProblemDefinition_Report.md
│  └─ 01_REPORT.md
├─ docs/
│  ├─ PRD.md                  # 제품 요구사항 정의서 (R-G-I-O · 사양 · Test Loop)
│  └─ TODO_D-LOC-01.md        # D-LOC-01 RED 단계 TODO List
└─ prompting/                 # 프롬프트 / 인터뷰 기록
   └─ 01_mom_test_interview_transcript.md
```

## 문서 읽는 순서
1. `Report/01.MagicSquare_ProblemDefinition_Report.md` — 왜 만드는가(문제 정의)
2. `docs/PRD.md` — 무엇을 만드는가(사양 · 성공 기준 · 테스트)
3. `prompting/01_mom_test_interview_transcript.md` — 문제 도출 과정(인터뷰 원본)

## ECB 설계 개요
- **Entity**: `MagicSquare`, `Cell`, `SolveResult`
- **Control**: `SquareValidator`, `MissingFinder`, `Solver`
- **Boundary**: `GridUI`, `InputHandler`, `ResultDisplay`
