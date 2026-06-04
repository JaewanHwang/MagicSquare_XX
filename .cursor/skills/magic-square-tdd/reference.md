# D-* 테스트 ID (Logic Track)

> entity/control 대상 · 파일명 `test_d_*.py` · Domain Mock 금지

| ID | 대상 | 기대 | 검증 초점 |
| --- | --- | --- | --- |
| D-01 | `sumLine(cells)` | 한 줄 합 정확 | 계산 기본 |
| D-02 | `collectLines(grid)` | 4행+4열+2대각 = 10줄 | 완전성(누락 0) |
| D-03 | 정답 마방진 | `valid=true` | 즉시 판정 |
| D-04 | 대각선 1줄만 틀림 | `valid=false`, `failedLines=[대각선]` | 완전성(대각선 누락 방지) |
| D-05 | 빈칸(0) 포함 | `valid=false`(미완성) | 즉시 판정 |
| D-06 | 같은 격자 2회 | 동일 결과 | 재현 방지 |
| D-07 | 행 정상·열 1개 틀림 | `failedLines=[col*]` | 완전성(열 누락 방지) |
| D-08 | `MAGIC_SUM` 상수 | `== 34`, 단일 출처 | SSOT |
