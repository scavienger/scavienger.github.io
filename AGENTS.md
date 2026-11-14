# AGENTS.md

이 문서는 프로젝트(`scavienger.github.io`)의 전체 구조, 핵심 아키텍처, 실행 명령, 주의사항 및 운영 원칙을 통합한 AI 에이전트 기준 문서입니다.
> **에이전트 운영 원칙**: 사용자가 대화 중 프로젝트의 핵심 방향, 모델 전략, 프롬프트/배치 정책 등 중요한 의사결정을 이야기하면 이를 요약해 안내하고 본 `AGENTS.md` 파일에도 즉시 반영하여 최신 상태를 유지하세요.

---

## 1. 프로젝트 개요

- **목적**: 매일 00:00 UTC에 LeetCode Daily Challenge 문제를 자동으로 수집하고, Google Gemini를 이용해 19개 프로그래밍 언어의 풀이와 복잡도 분석을 생성하여 GitHub Pages(Jekyll) 블로그로 배포합니다.
- **성격**: 실시간 상용(Live) 서비스가 아닌 개인 자동화 기술 블로그이므로, 무리한 다중 폴백이나 과도한 재시도로 API 쿼터를 소진하기보다 실패 시 깔끔하게 실패 상태로 두고 추후 배치(Follow-up)로 보완하는 방향을 지향합니다.
- **호스팅**: GitHub Pages (`https://scavienger.github.io`)
- **기본 브랜치**: `master` (일일 자동화 커밋 및 GitHub Pages 배포가 모두 `master` 기준으로 동작)

---

## 2. 핵심 규칙 (Critical Rules)

1. **AI 프로바이더 이원화 및 Rate Limit(할당량) 전략**:
   - **일일 자동화 (GitHub Actions, `--provider gemini` 기본값)**:
     - **기본(메인) 모델**: `gemini-3.8-flash` (Google AI Studio의 **Gemini 3.8 Flash**, `GEMINI_MODEL` 환경변수로 오버라이드 가능)
     - **할당량 초과(`429`) 및 서버 과부하(`503`) 폴백 모델**: `gemini-3-flash-preview` (Google AI Studio 표시명 **Gemini 3 Flash**의 실제 API 엔드포인트 코드)
     - 무료 티어 기준 두 모델 모두 **분당 5회(5 RPM) / 일일 20회(20 RPD) / 분당 25만 토큰(250K TPM)**으로 제한이 타이트합니다.
     - `gemini-3.8-flash` 호출 중 `429` 또는 `503` 발생 시 같은 모델에 재시도하며 시간을 낭비하지 않고 **즉시 `gemini-3-flash-preview`로 전환**합니다.
     - 의미 없는 `404` 임의 폴백(예: 구버전 `gemini-2.5-flash` 등)은 두지 않습니다.
     - **배치 간 대기 시간**: Hard 문제(5회 호출) 등이 5 RPM 제한에 걸리지 않도록 기본 `BATCH_DELAY_SECONDS=15`(15초)를 유지합니다.
   - **누락분 Follow-up (로컬 실행, `--provider codex`)**:
     - 개인 학습·이력 관리 목적의 블로그이므로, 로컬에서 밀린 날짜들을 Follow-up할 때는 Gemini 무료 API 일일 쿼터(20 RPD)를 소모하지 않도록 **ChatGPT 구독 기반의 OpenAI Codex CLI(`codex exec`, `--provider codex`)**를 사용합니다.
     - **기본 Codex 모델**: `gpt-6-luna` (가볍고 빠른 경량 모델, `reasoning_effort="low"` 기본 적용으로 배치당 약 3,500~5,000 토큰만 소모하여 5시간 리셋 윈도우 내에서 여유롭게 다수 날짜 처리 가능; 필요 시 `--model gpt-6.1-sol` 등으로 오버라이드 가능).
     - 일부 언어만 실패한 포스트(Partial failure)는 우선 패스하고, **포스트 파일 자체가 누락된 날짜 및 AI 솔루션이 아예 없는 날짜(`TODO: Add solution approach here.`, 24개)**를 먼저 작업합니다. (단, 특정 배치만 실패한 포스트를 이어서 채울 때는 `--only-missing` 플래그를 사용하면 이미 성공한 배치는 건너뛰고 실패한 배치만 생성합니다.)
     - Follow-up은 GitHub Actions가 아니라 **로컬에서 에이전트를 통해 직접 실행하고, 오류 발생 시 즉시 확인·수정하는 방식**으로 진행합니다.
     - 배치 분할 수는 일일 생성과 Follow-up 모두 동일하게 **Easy 3분할(7/6/6), Medium 4분할(5/5/5/4), Hard 5분할(3/4/4/4/4)**을 유지합니다.
   - **Python SDK 및 `api_version`**: Gemini 호출 시 반드시 `google-genai`를 사용하며(`google-generativeai` 사용 금지), `google-genai >= 3.0.0`부터 기본 API 버전이 `v1`으로 바뀌어 `gemini-3-flash-preview`가 404를 반환하므로 `genai.Client(..., http_options={"api_version": "v1beta"})`를 필수 지정합니다.

2. **프롬프트 분리 및 토큰 한도(`MAX_OUTPUT_TOKENS`) 관리**:
   - **프롬프트 외부 파일 분리**: 프롬프트는 Python 코드(`scripts/solve_with_ai.py`)에 하드코딩하지 않고 `scripts/prompts/` 하위 파일에서 관리합니다:
     - `scripts/prompts/solve_with_metadata.txt`: 첫 번째 배치용 (`approach`, `time_complexity`, `space_complexity` + `solutions` 요청)
     - `scripts/prompts/solve_solutions_only.txt`: 이후 배치용 (`solutions` 코드만 요청)
   - **Thinking 토큰과 `MAX_OUTPUT_TOKENS = 65536`**:
     - Gemini Thinking 모델에서 `max_output_tokens`는 **내부 추론 토큰(`thoughts_token_count`) + 실제 JSON 출력 토큰(`candidates_token_count`)의 합산 한도(Hard Cutoff)**입니다.
     - 추론 토큰으로 인해 JSON 응답이 중간에 잘리는 현상을 방지하기 위해 모델 최대 한도인 `MAX_OUTPUT_TOKENS = 65536` (64K)을 사용하며, 로그에 `thoughts_token_count`를 함께 기록합니다.
   - **Batch 2+ 에 Batch 1의 검증된 알고리즘/코드 전달**:
     - Batch 2 이후(`include_metadata=False`) 호출 시에는 Batch 1에서 생성된 `approach`와 기준 구현 코드(`python3`/`python`/`cpp`)를 프롬프트(`VERIFIED ALGORITHM`, `REFERENCE IMPLEMENTATION`)에 주입하여, 모델이 매 배치마다 문제를 처음부터 다시 추론하느라 Thinking 토큰을 낭비하지 않고 언어 변환에만 집중하도록 합니다.
   - **템플릿 중복 주입 금지**: 요청된 `target_languages`에 해당하는 코드 템플릿만 프롬프트에 포함하며, 요청 목록에 없는 언어의 템플릿을 중복 삽입하지 않습니다.

3. **Jekyll Liquid 구문 이스케이프 필수 (`{% raw %}`)**:
   - Jekyll의 Liquid 템플릿 엔진은 Markdown/HTML 렌더링 전에 `{{` 와 `{%`를 먼저 파싱합니다.
   - 코드 블록(`_generate_code_tabs` 및 fallback 코드 블록)은 반드시 `{% raw %}...{% endraw %}`로 감싸야 합니다.
   - 문제 설명(`content`), 힌트(`hints`), AI 풀이 설명(`approach`, `time_complexity`, `space_complexity`) 내의 `{{` 및 `{%` 역시 `PostGenerator._escape_liquid()`를 통해 `{% raw %}{{{% endraw %}` 형태로 이스케이프되어야 합니다 (예: 2026-09-25 `Brace Expansion II` 문제의 `{{a,b},{b,c}}` 구문 오류 방지).

4. **코드 들여쓰기 정규화 (Indentation Normalization)**:
   - `scripts/solve_with_ai.py`의 `_clean_code()`에서 `textwrap.dedent()` 및 LeetCode 공식 스니펫(`_posts/_daily/YYYY/MM/DD/{lang}.txt`) 기반 들여쓰기 보정 로직을 절대 제거하지 마세요.

5. **빌드 산출물 및 프론트매터(Frontmatter) 파싱 주의**:
   - `_site/` 디렉토리는 Jekyll 빌드 산출물이므로 직접 수정하거나 커밋하지 않습니다.
   - `_config.yml`의 `exclude` 목록에 모든 문서 파일(`AGENTS.md`, `CLAUDE.md`, `README.md`, `TODO.md`, `BRANCHING_STRATEGY.md`, `SETUP_CHECKLIST.md`), 스크립트(`scripts/`), 테스트(`tests/`), 스니펫(`**/*.txt`)이 포함되어 있어야 합니다.
   - 포스트의 YAML 프론트매터(`ai_solutions`) 내부 코드에 `---` 문자열이 포함될 수 있으므로, 프론트매터 분리 시 단순 `content.split("---")` 대신 줄 단위 정규식 `re.split(r"^---\s*$", content, maxsplit=2, flags=re.MULTILINE)`을 사용해야 합니다.

---

## 3. 디렉토리 구조

```text
scavienger.github.io/
├── .github/workflows/
│   ├── leetcode-daily.yml         # 매일 00:00 UTC 자동 포스트 생성 워크플로우
│   ├── regenerate-solution.yml    # 특정 날짜(또는 기간) AI 솔루션 재생성 워크플로우
│   └── generate-post-by-date.yml  # 특정 날짜(또는 기간) 포스트 수동 생성 워크플로우
├── _includes/
│   ├── head.html                  # 기본 <head> 템플릿
│   ├── custom-head.html           # 다크모드, 코드 탭, 코드 복사, 북마크, 검색 팔레트 JS 및 AdSense 로드
│   ├── dark-mode-toggle.html      # 우측 상단 다크모드 토글 버튼
│   ├── search-palette.html        # Cmd+K / Ctrl+K 글로벌 검색 모달 컴포넌트
│   └── toc.html                   # 스크롤 스파이 지원 목차(TOC) 컴포넌트
├── _layouts/
│   ├── home.html                  # 홈 화면 (히어로, 문제 통계 대시보드, 최근 문제 그리드)
│   └── post.html                  # 포스트 상세 레이아웃 (브레드크럼, TOC, 관련 문제, 이전/다음 네비게이션)
├── _posts/
│   └── _daily/                    # 일일 챌린지 포스트 컬렉션 (`site.daily`)
│       └── YYYY/MM/DD/
│           ├── {slug}.md          # 생성된 Jekyll 포스트 (파일명에 날짜 접두사 없음)
│           └── {lang}.txt         # 19개 언어별 LeetCode 공식 코드 템플릿 스니펫
├── _sass/
│   ├── custom.scss                # 커스텀 스타일 (코드 탭, 카드, 레이아웃 등)
│   └── dark-mode.scss             # 다크모드 스타일 오버라이드
├── assets/
│   ├── main.scss                  # 메인 SCSS 엔트리포인트
│   └── js/
│       ├── dark-mode.js           # 다크모드 상태 관리 및 localStorage 연동
│       ├── code-tabs.js           # 선호 언어 탭 localStorage 저장/복원
│       ├── code-copy.js           # 코드 블록 원클릭 복사 버튼
│       ├── bookmarks.js           # 개인 Solved/Bookmark 체크리스트 (localStorage)
│       └── search-palette.js      # Cmd+K / Ctrl+K 빠른 검색 팔레트 로직
├── data/
│   └── daily_challenges.json      # 날짜별 LeetCode 문제 매핑 캐시 (date -> link, titleSlug)
├── scripts/
│   ├── prompts/
│   │   ├── solve_with_metadata.txt  # Batch 1 프롬프트 템플릿 (풀이 설명 + 복잡도 + 코드)
│   │   └── solve_solutions_only.txt # Batch 2+ 프롬프트 템플릿 (코드 전용)
│   ├── generate_posts.py          # 통합 실행 스크립트 (캐시 조회 + 문제 수집 + AI 풀이 + 포스트 생성)
│   ├── solve_with_ai.py           # Gemini API 기반 19개 언어 솔루션 배치 생성기
│   ├── generate_post.py           # Jekyll 마크다운 포스트 생성기
│   └── requirements.txt           # Python 의존성 목록
├── tests/
│   ├── test_generate_post.py      # 포스트 생성 및 Liquid 이스케이프 단위 테스트
│   ├── test_solve_with_ai.py      # 프롬프트, 들여쓰기 보정, JSON 파싱, 429 폴백 단위 테스트
│   └── test_generate_posts_cli.py # CLI 인자 및 날짜 범위 처리 테스트
├── index.md                       # 메인 홈 페이지
├── calendar.md                    # 연도별 52주 잔디 히트맵 캘린더 페이지 (`/calendar/`)
├── search.json                    # 글로벌 빠른 검색용 JSON 인덱스 (`/search.json`)
├── tags.md                        # 토픽/태그별 분류 페이지 (`/topics/`)
├── _config.yml                    # Jekyll 설정 파일 (`collections_dir: _posts`)
├── Gemfile                        # Ruby/Jekyll 의존성
├── pytest.ini                     # Pytest 설정
└── AGENTS.md                      # AI 에이전트 및 개발자 통합 가이드 (자동 로드됨)
```

---

## 4. 자동화 파이프라인 동작 방식

1. **`scripts/generate_posts.py` (통합 오케스트레이터)**
   - 입력받은 날짜(`YYYY-MM-DD`) 또는 날짜 범위(`start_date` ~ `end_date`)에 대해 `data/daily_challenges.json` 캐시를 확인합니다.
   - 캐시에 없는 날짜가 있으면 LeetCode GraphQL API(`dailyCodingChallengeV2`)를 월 단위로 호출해 캐시를 갱신합니다.
   - 문제 상세 정보(`question` GraphQL 쿼리)를 가져와 19개 언어 코드 템플릿을 `_posts/_daily/YYYY/MM/DD/{lang_slug}.txt`에 저장합니다.
   - `AISolutionGenerator`를 호출해 풀이를 생성하고, 실패 시 기존 포스트의 `ai_solutions`를 보존합니다.
   - `PostGenerator`를 호출해 `_posts/_daily/YYYY/MM/DD/{slug}.md` 파일을 생성합니다.

2. **`scripts/solve_with_ai.py` (AI 솔루션 생성기)**
   - 문제 난이도별로 19개 언어를 동적 배치 분할하여 요청합니다:
     - **Easy** (3회 요청): 7 / 6 / 6개 언어
     - **Medium** (4회 요청): 5 / 5 / 5 / 4개 언어
     - **Hard** (5회 요청): 3 / 4 / 4 / 4 / 4개 언어
   - 첫 번째 배치에서만 메타데이터(`approach`, `time_complexity`, `space_complexity`)를 함께 요청하고, 이후 배치에서는 Batch 1의 `approach` 및 기준 코드를 컨텍스트로 넘겨주며 `solutions` 코드만 요청합니다.
   - 무료 티어 분당 제한(5 RPM)에 걸리지 않도록 배치 간 기본 `15초`(`BATCH_DELAY_SECONDS=15`) 간격을 둡니다.
   - `gemini-3.8-flash`에서 `429`(Rate Limit / 20 RPD 초과) 발생 시 대기 없이 즉시 `gemini-3-flash-preview`(Gemini 3 Flash)로 전환하며, 폴백 모델에서도 `429`(60초 대기) 또는 `503`(Overloaded, 120초 대기) 발생 시 최대 6회(`MAX_RETRIES = 6`) 재시도합니다.
   - LLM 응답의 깨진 백슬래시 이스케이프나 불필요한 후행 괄호를 자동 복구하는 JSON 전처리 로직(`parse_json_response`)을 포함합니다.

3. **`scripts/generate_post.py` (포스트 렌더러)**
   - YAML 프론트매터에 메타데이터와 `ai_solutions` 원본 데이터를 함께 저장하여 추후 재생성 시 활용합니다.
   - 19개 언어(C++, Java, Python, Python3, C, C#, JavaScript, TypeScript, PHP, Swift, Kotlin, Dart, Go, Ruby, Scala, Rust, Racket, Erlang, Elixir)를 Pure CSS 라디오 탭(`.code-tabs`)으로 렌더링합니다.

---

## 5. 주요 실행 명령어

### 로컬 개발 환경 설정 및 테스트

```bash
# Python 가상환경 생성 및 의존성 설치
python3 -m venv venv
./venv/bin/pip install -r scripts/requirements.txt pytest

# 전체 단위 테스트 실행
./venv/bin/pytest -v

# Jekyll 로컬 서버 실행 (Ruby & Bundler 필요)
bundle install
bundle exec jekyll serve
```

### 포스트 수동 생성 및 누락분 Follow-up (CLI)

```bash
# 아예 빠진 날짜(파일 누락 또는 AI 솔루션 전체 누락) 목록 조회 (최신순)
./venv/bin/python scripts/generate_posts.py --list-missing

# [권장] 로컬 Follow-up: ChatGPT 구독(Codex CLI, gpt-6-luna)으로 생성 (Gemini API 쿼터 미소모)
./venv/bin/python scripts/generate_posts.py --provider codex 2026-11-11

# 일부 배치만 실패한 포스트에서 실패한 배치만 이어서 생성
./venv/bin/python scripts/generate_posts.py --provider codex --only-missing 2026-06-02

# Gemini API로 특정 날짜 포스트 생성 또는 재생성 (.env 또는 환경변수 GEMINI_API_KEY 사용)
./venv/bin/python scripts/generate_posts.py --provider gemini 2026-11-11
```

---

## 6. GitHub Actions 설정 및 연동 가이드

### 필수 GitHub Repository 설정
1. **GitHub Secrets (`Settings` → `Secrets and variables` → `Actions`)**:
   - `GEMINI_API_KEY`: Google AI Studio에서 발급받은 Gemini API 키 (필수)
2. **Workflow 권한 (`Settings` → `Actions` → `General`)**:
   - `Workflow permissions`: **Read and write permissions** 활성화 (자동 커밋 및 푸시에 필요)
3. **GitHub Pages (`Settings` → `Pages`)**:
   - `Source`: **Deploy from a branch**
   - `Branch`: **`master` / `/ (root)`**

### 워크플로우 목록
- **`LeetCode Daily Challenge` (`leetcode-daily.yml`)**: 매일 00:00 UTC 자동 실행 및 수동 실행(`workflow_dispatch`) 지원
- **`Regenerate AI Solution for Post` (`regenerate-solution.yml`)**: `date`(필수) 및 `end_date`(선택, 범위 지정) 입력을 받아 기존 포스트의 AI 솔루션을 재생성
- **`Generate Post by Date` (`generate-post-by-date.yml`)**: `date`(필수) 및 `end_date`(선택, 범위 지정) 입력을 받아 특정 날짜/기간의 포스트를 생성
