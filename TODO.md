# LeetCode Daily Challenge Blog - TODO List

## 작업 완료 현황 (2025-11-15 기준)

### ✅ 완료된 주요 기능
- [x] **Jekyll 블로그 기본 셋업** - Phase 1 완료
- [x] **Archive & Tag Pages** - 문제 탐색 기능 완료
- [x] **Visual Improvements** - 다크모드, 반응형 디자인 완료
- [x] **AI Solution Generation** - Gemini/Groq 자동 솔루션 생성 완료
- [x] **GitHub Actions 자동화** - 매일 00:00 UTC 자동 실행

---

## 현재 진행 중 🔄

### 🎨 UI/UX Enhancement (다음 작업)
- [ ] 레이아웃 개선 (더 유려한 디자인)
- [ ] 포스트 상세 페이지 레이아웃 최적화
- [ ] 홈페이지 히어로 섹션 추가
- [ ] 카드 기반 포스트 목록 디자인
- [ ] 타이포그래피 개선

---

## High Priority 🔥

### 1. 🔧 Manual Post Generation (기존 문제 수동 작업)
**목적:** 특정 날짜의 문제를 수동으로 추가하거나 재생성

- [ ] 날짜 지정 스크립트 작성
  ```bash
  python scripts/fetch_leetcode_by_date.py --date 2025-11-14
  ```
- [ ] LeetCode 아카이브 API 조사 (과거 문제 접근 가능 여부)
- [ ] 수동 실행용 GitHub Actions workflow 추가
- [ ] README에 수동 실행 가이드 추가

**참고:** LeetCode API는 "오늘의 문제"만 반환 가능. 과거 문제는 별도 방법 필요.

### 2. 🤖 Multi-AI Solution Comparison (AI 솔루션 비교)
**목적:** 여러 AI 솔루션을 비교 분석하여 더 나은 접근법 제시

- [ ] 다중 AI provider 동시 실행 구조 변경
  - [ ] solve_with_ai.py 리팩토링: 단일 → 다중 솔루션 지원
  - [ ] `ai_solutions` 배열 구조로 변경
- [ ] 포스트 템플릿에 비교 섹션 추가
  - [ ] 각 AI별 솔루션 섹션
  - [ ] 비교 테이블 (복잡도, 코드 길이, 접근법)
  - [ ] 권장 솔루션 하이라이트
- [ ] Provider 관리
  - [ ] Gemini (무료)
  - [ ] Groq (무료)
  - [ ] OpenAI (선택적, 유료)
  - [ ] Claude (선택적, 유료)
- [ ] 워크플로우 설정
  ```yaml
  AI_COMPARISON_MODE: true  # 비교 모드 활성화
  AI_PROVIDERS: "gemini,groq"  # 사용할 provider 목록
  ```

### 3. 📊 Enhanced Statistics Dashboard
- [ ] 주제별 분포 차트 추가
- [ ] 최근 해결 문제 타임라인
- [ ] 난이도별 진행률 바
- [ ] 월별 활동 히트맵

---

## Medium Priority 📝

### 4. 🔍 Search Functionality (검색 기능)
- [ ] 클라이언트 사이드 검색 구현 (Jekyll Search 또는 Lunr.js)
- [ ] 문제 제목/태그/난이도로 검색
- [ ] 검색 결과 하이라이팅

### 5. 💬 Comment System (댓글 시스템)
- [ ] utterances 통합 (GitHub Issues 기반)
- [ ] 문제별 토론 가능
- [ ] 다크모드 지원

### 6. 🌐 Multi-language Code Support (다국어 코드)
- [ ] Python 외 Java, C++, JavaScript 코드도 포함
- [ ] 언어별 탭으로 전환 가능
- [ ] LeetCode API에서 모든 언어 코드 템플릿 가져오기

---

## Low Priority 💡

### 7. 📧 Notification System (알림 시스템)
- [ ] 빌드 실패시 이메일 알림
- [ ] 새 포스트 생성 알림
- [ ] 에러 로그 자동 수집

### 8. 🔒 Enhanced Error Handling (에러 처리 강화)
- [ ] 재시도 메커니즘 추가 (API 실패시)
- [ ] 중복 포스트 방지 로직 강화
- [ ] Fallback chain: Gemini → Groq → 기본 템플릿

### 9. 🚀 SEO Optimization (SEO 최적화)
- [ ] 메타 태그 최적화
- [ ] Open Graph 이미지 자동 생성
- [ ] Schema.org 구조화된 데이터 추가
- [ ] robots.txt 최적화
- [ ] sitemap.xml 자동 생성

### 10. 📱 Progressive Web App (PWA)
- [ ] manifest.json 추가
- [ ] 오프라인 지원
- [ ] 모바일 앱처럼 설치 가능

---

## Completed ✅

### Phase 1: 기본 인프라
- [x] Jekyll 블로그 기본 셋업
- [x] GitHub Actions 자동화 워크플로우 (매일 00:00 UTC)
- [x] LeetCode API 연동 스크립트
- [x] 포스트 자동 생성 스크립트
- [x] AdSense 인증 코드 추가
- [x] README.md 문서화

### Phase 2: 탐색 & 네비게이션
- [x] Archive page (연도/월별)
- [x] Difficulty page (Easy/Medium/Hard)
- [x] Topics/Tags page
- [x] Header navigation 추가

### Phase 3: 시각적 개선
- [x] 커스텀 CSS 스타일 (_sass/custom.scss)
- [x] 다크 모드 자동 지원 (_sass/dark-mode.scss)
- [x] 코드 하이라이팅 테마 (GitHub 스타일)
- [x] 반응형 디자인 (모바일 최적화)
- [x] 통계 대시보드 (홈페이지)
- [x] Gradient 효과 & 애니메이션

### Phase 4: AI 솔루션 생성
- [x] Gemini API 연동 (gemini-2.5-flash)
- [x] Groq API 연동 (llama-3.3-70b-versatile)
- [x] 자동 솔루션 생성 (approach, code, complexity)
- [x] Provider 선택 기능 (gemini/groq)
- [x] API 키 없이도 작동 (graceful fallback)
- [x] 포스트에 AI 솔루션 포함

---

## 기술 스택 📚

### 프론트엔드
- Jekyll 4.3.0
- Minima theme (customized)
- Sass (CSS preprocessing)
- Kramdown (Markdown processor)
- Rouge (Syntax highlighting)

### 백엔드/자동화
- Python 3.11
- GitHub Actions
- LeetCode GraphQL API
- Google Gemini API (gemini-2.5-flash)
- Groq API (llama-3.3-70b-versatile)

### 배포
- GitHub Pages
- 자동 빌드 & 배포

---

## 작업 로그 📝

### 2025-11-15
- ✅ AI Solution Generation 완료 (Gemini, Groq)
- ✅ Visual Improvements 완료 (다크모드, 반응형)
- ✅ Archive & Tag Pages 완료
- ✅ 첫 AI 솔루션 포스트 생성 성공

### 향후 계획
1. **즉시:** UI/UX 레이아웃 개선
2. **단기:** Manual Post Generation 구현
3. **중기:** Multi-AI Solution Comparison
4. **장기:** Search, Comments, PWA

---

## Notes

- 각 작업은 별도 브랜치에서 진행 (`claude/{feature-name}-{session-id}`)
- PR을 통한 머지 필수
- 테스트 후 master에 반영
- API 키는 GitHub Secrets로 관리
- 설정 값은 워크플로우 파일에서 관리
- Sass import migration (planned)
  - Replace @import with @use/@forward in assets/main.scss and partials (custom.scss, dark-mode.scss, minima integration).
  - Verify minima entry points; add wrapper if needed.
  - After changes, run `bundle exec jekyll build` to ensure no warnings.
