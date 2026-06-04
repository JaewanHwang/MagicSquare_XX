# Review ECB — 계약 위반 점검

MagicSquare_1004 코드를 ECB·계약 관점에서만 리뷰한다. **코드 수정 금지** — 위반 사항만 표로 보고한다.

## 점검 항목
1. **import 방향** — `boundary → control → entity` 단방향 준수. `entity → *`(control/boundary) import 금지.
2. **entity E001~E005** — `entity` 계층이 오류 코드 `E001~E005`를 처리하지 않는지(boundary 책임).
3. **int[6] 1-index** — 정답 출력이 `[r1,c1,n1,r2,c2,n2]` 형태이며 좌표가 1-index(1~4)인지.
4. **MagicConstant SSOT** — `34`/`16` 리터럴이 산재하지 않고 단일 상수(`MAGIC_SUM` 등)에서 import되는지.
5. **Logic Track Domain Mock** — `tests/{entity,control}`(D-*)에서 Domain 객체 Mock을 쓰지 않는지(UI Track만 허용).

## 출력 — 위반 표

| # | 항목 | 위치(파일:라인) | 위반 내용 | 권고 |
| --- | --- | --- | --- | --- |
| 1 | import 방향 | `src/entity/...:NN` | 예: entity가 control import | 의존 제거/역전 |

- 위반이 없는 항목은 별도 행에 `✅ 통과`로 표기한다.
- 각 위반은 항목 번호(1~5)와 정확한 위치를 명시한다.

## 금지
- 코드/테스트 파일 **수정**(리뷰 전용).
- 위반 외 스타일·취향 코멘트(범위 밖).
