# Git Branching Strategy

이 프로젝트는 Git Flow를 간소화한 브랜치 전략을 사용합니다.

## 브랜치 구조

### 🔒 `master` (Protected)
- **용도**: 프로덕션/릴리스 브랜치
- **보호**: GitHub에서 브랜치 보호 활성화
  - Direct push 금지
  - Pull Request를 통한 머지만 허용
  - Code review 필수 (선택사항)
- **배포**: GitHub Pages가 이 브랜치에서 자동 배포
- **업데이트**: `develop` 브랜치에서 PR을 통해서만 머지

### 🚀 `develop` (Default Branch)
- **용도**: 메인 개발 브랜치
- **자동화**: GitHub Actions의 일일 LeetCode 포스트가 여기에 커밋됨
- **테스트**: 새로운 기능들이 여기서 통합되고 테스트됨
- **배포 전 단계**: 안정화되면 `master`로 PR 생성

### 🌿 `develop-feature-{feature-name}-{id}`
- **용도**: 개별 기능 개발
- **생성**: `develop`에서 분기
- **머지**: 완료 후 `develop`으로 PR
- **삭제**: 머지 후 삭제 권장

## 워크플로우

### 1️⃣ 일상 개발 (Feature Development)

```bash
# 1. develop 브랜치로 전환
git checkout develop
git pull origin develop

# 2. 새 feature 브랜치 생성
git checkout -b develop-feature-search-function-abc123

# 3. 작업 수행 및 커밋
git add .
git commit -m "Add search functionality"

# 4. 원격에 푸시
git push -u origin develop-feature-search-function-abc123

# 5. GitHub에서 develop으로 PR 생성
# 6. 리뷰 후 머지
# 7. 로컬에서 브랜치 정리
git checkout develop
git pull origin develop
git branch -d develop-feature-search-function-abc123
```

### 2️⃣ 릴리스 배포 (Release to Production)

```bash
# 1. develop이 안정적일 때 GitHub에서 PR 생성
#    develop → master

# 2. PR 설명에 포함할 내용:
#    - 새로운 포스트 개수
#    - 추가된 기능
#    - 수정된 버그
#    - Breaking changes (있다면)

# 3. 리뷰 및 승인 후 머지

# 4. master 브랜치 확인 (선택)
git checkout master
git pull origin master
git log --oneline -5
```

### 3️⃣ 핫픽스 (Urgent Bug Fix)

긴급 버그 수정이 필요한 경우:

```bash
# 옵션 A: develop에서 수정 후 빠른 릴리스
git checkout develop
git checkout -b develop-hotfix-critical-bug-xyz
# 수정 작업
git push -u origin develop-hotfix-critical-bug-xyz
# develop으로 PR → 머지
# develop → master PR → 즉시 머지

# 옵션 B: master에서 직접 수정 (권장하지 않음)
# 브랜치 보호 설정에 따라 불가능할 수 있음
```

## GitHub Actions와의 통합

### 자동화된 워크플로우

1. **Daily LeetCode Post** (`.github/workflows/leetcode-daily.yml`)
   - **실행**: 매일 09:00 KST
   - **타겟 브랜치**: `develop`
   - **동작**: 자동으로 새 포스트를 `develop`에 커밋

2. **Regenerate Solution** (`.github/workflows/regenerate-solution.yml`)
   - **실행**: 수동 트리거
   - **타겟 브랜치**: `develop`
   - **동작**: 특정 날짜의 포스트를 재생성

### 워크플로우 파일 변경사항

두 워크플로우 모두 `develop` 브랜치를 체크아웃하고 커밋합니다:

```yaml
# Checkout
- uses: actions/checkout@v4
  with:
    ref: develop

# Push
git push origin develop
```

## 브랜치 네이밍 규칙

### Feature 브랜치
```
develop-feature-{기능명}-{session-id}

예시:
- develop-feature-search-01J63oC4
- develop-feature-dark-mode-xyz123
- develop-feature-ui-improvements-abc456
```

### Hotfix 브랜치 (필요시)
```
develop-hotfix-{버그명}-{session-id}

예시:
- develop-hotfix-broken-tabs-abc123
- develop-hotfix-css-overflow-xyz789
```

## 베스트 프랙티스

### ✅ DO
- Feature 작업 전 항상 `develop`에서 최신 코드 pull
- 의미 있는 커밋 메시지 작성
- PR에 충분한 설명과 스크린샷 포함
- 작은 단위로 자주 커밋
- 머지 후 feature 브랜치 삭제
- `develop`에서 충분히 테스트 후 `master`로 머지

### ❌ DON'T
- `master`에 직접 push (보호 설정으로 차단됨)
- 큰 기능을 한 번에 커밋
- Force push to shared branches (`develop`, `master`)
- Feature 브랜치를 오래 유지 (merge conflict 위험)
- 테스트 없이 `master`로 머지

## 릴리스 주기 권장사항

### 주간 릴리스
```
매주 일요일:
1. develop의 변경사항 검토
2. 문제 없으면 develop → master PR 생성
3. 리뷰 및 머지
4. 새로운 주 시작
```

### 기능별 릴리스
```
주요 기능 완료 시:
1. Feature 브랜치 → develop 머지
2. develop에서 통합 테스트
3. 안정화되면 develop → master PR
4. 머지 후 릴리스 노트 작성
```

## GitHub Pages 배포

- **배포 소스**: `master` 브랜치
- **자동 배포**: `master`에 push될 때마다 자동 빌드 및 배포
- **테스트 환경**: `develop`의 변경사항을 로컬에서 테스트
  ```bash
  git checkout develop
  bundle exec jekyll serve
  # http://localhost:4000 에서 확인
  ```

## 트러블슈팅

### Q: develop에서 작업했는데 실수로 master에 push하려고 했어요
A: 브랜치 보호 설정으로 차단됩니다. develop으로 전환하세요.

### Q: Feature 브랜치가 develop과 너무 달라졌어요 (conflict)
A: develop의 최신 변경사항을 feature 브랜치로 머지하세요:
```bash
git checkout develop-feature-xyz
git pull origin develop
# conflict 해결
git push
```

### Q: 급하게 master를 수정해야 해요
A: GitHub Settings에서 일시적으로 보호 해제하거나, Admin 권한으로 강제 머지할 수 있습니다. 하지만 권장하지 않습니다.

### Q: GitHub Actions가 develop에 커밋하는데 master에는 반영 안 돼요
A: 정상입니다. develop → master PR을 생성하여 릴리스하세요.

## 요약

```
일일 자동 포스트
    ↓
develop (개발/테스트)
    ↓
develop-feature-* (새 기능)
    ↓
develop (머지)
    ↓
master (릴리스) → GitHub Pages 배포
```

이 전략을 통해:
- ✅ 안정적인 프로덕션 환경 (master)
- ✅ 자유로운 개발 환경 (develop)
- ✅ 격리된 기능 개발 (feature branches)
- ✅ 자동화된 일일 업데이트
- ✅ 리뷰 프로세스 강제

