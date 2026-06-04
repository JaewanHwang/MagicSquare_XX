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

## TDD 진행 현황 (D-LOC-01 / FR-LOC-01)
> Layer: entity · Track: Logic(D-*) · 상세: [docs/TODO_D-LOC-01.md](docs/TODO_D-LOC-01.md)

| STEP | Phase | 산출물 | 상태 |
| --- | --- | --- | --- |
| 3 | RED | `tests/entity/test_d_loc_01.py` (`pytest.fail` 스켈레톤) | ✅ |
| 4 | GREEN | `src/entity/locator.py` `find_blank_coords` + `constants.py`(SSOT) | ✅ |
| 5 | Golden Master | `tests/_approval.py` + `tests/golden/d_loc_01_g1.approved.txt` | ✅ |
| 6 | REFACTOR | `assert_matches_golden` 파라미터 명명 정리(C1) | ✅ |

- [x] **C2C 추적** — PRD §5.1/§2/§3.2 인용 + 판단 포함 To-Do 1개 + D-LOC-01 Given/When/Then
- [x] **RED → GREEN** — `find_blank_coords(grid)` → `[(2,2),(3,3)]` row-major (1-index)
- [x] **Golden Master** — `UPDATE_GOLDEN=1` 기준 생성 후 matched 검증
- [x] **ECB·Mock** — Domain Mock 금지 · entity E001~E005 미emit · `entity → *` import 없음
- 현재 `python -m pytest -v` → **2 passed**

## 테스트 실행 (가상환경)
> Windows 기준. 프로젝트 루트(`MagicSquare_XX/`)에서 실행한다. 셸에 따라 활성화 명령만 다르다.

**Git Bash**
```bash
# 1) 가상환경 생성
python -m venv .venv

# 2) 활성화 (프롬프트에 (.venv) 표시 확인)
source .venv/Scripts/activate

# 3) 의존성 설치 (editable + dev) — src/ 패키지가 import 경로에 잡힘
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"

# 4) 테스트 실행
python -m pytest -v                                  # 전체
python -m pytest tests/entity tests/control -q       # Logic Track(D-*)만
python -m pytest tests/entity/test_d_loc_01.py -v    # 단일 파일

# 5) 비활성화
deactivate
```

**PowerShell** — 생성·설치·실행 명령은 동일하고, 활성화만 다음과 같다.
```powershell
.\.venv\Scripts\Activate.ps1
#  실행 정책 오류 시 현재 세션에만 허용:
#  Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

> 참고: `pyproject.toml`의 `pythonpath = ["src", "tests"]` 덕분에 editable 설치 없이도 pytest가 `entity` 패키지와 `_approval` 헬퍼를 찾는다. 설치(`-e .`)를 하면 venv 어디서든 `import entity`가 가능하다.

## 프로젝트 구조
```
MagicSquare_XX/
├─ README.md                  # 본 문서
├─ pyproject.toml             # pytest 설정 (pythonpath=src,tests)
├─ src/
│  ├─ entity/                 # 순수 도메인 (ECB: 외부 import 금지)
│  │  ├─ constants.py         # SSOT 상수 (MAGIC_SUM=34, GRID_SIZE=4 …)
│  │  └─ locator.py           # find_blank_coords(grid)
│  ├─ control/                # 흐름/조합 (예정)
│  └─ boundary/               # 입출력/검증 (예정)
├─ tests/
│  ├─ conftest.py             # grid_g1 픽스처 (순수 데이터)
│  ├─ _approval.py            # Golden Master 헬퍼 assert_matches_golden
│  ├─ golden/                 # 승인된 기준 출력 (.approved.txt)
│  └─ entity/test_d_loc_01.py # D-LOC-01 (assert + golden)
├─ Report/                    # STEP별 보고서 (01~06)
├─ Prompting/                 # 세션 트랜스크립트 (01~06)
└─ docs/
   ├─ PRD.md                  # 제품 요구사항 정의서
   └─ TODO_D-LOC-01.md        # D-LOC-01 TODO List
```

## 문서 읽는 순서
1. `Report/01.MagicSquare_ProblemDefinition_Report.md` — 왜 만드는가(문제 정의)
2. `docs/PRD.md` — 무엇을 만드는가(사양 · 성공 기준 · 테스트)
3. `prompting/01_mom_test_interview_transcript.md` — 문제 도출 과정(인터뷰 원본)

## ECB 설계 개요
- **Entity**: `MagicSquare`, `Cell`, `SolveResult`
- **Control**: `SquareValidator`, `MissingFinder`, `Solver`
- **Boundary**: `GridUI`, `InputHandler`, `ResultDisplay`
