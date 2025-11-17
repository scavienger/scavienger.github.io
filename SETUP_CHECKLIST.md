# Branch Protection Setup Checklist

브랜치 전략 설정을 완료하기 위해 GitHub에서 다음 작업을 수행하세요.

## ✅ 완료된 작업
- [x] `develop` 브랜치 생성 및 push
- [x] GitHub Actions 워크플로우를 develop 브랜치 타겟으로 업데이트
- [x] CLAUDE.md 및 BRANCHING_STRATEGY.md 문서화
- [x] 변경사항 커밋 및 push

## 🔧 GitHub에서 수동으로 수행할 작업

### 1. Master 브랜치 보호 설정 ⭐ 중요!

1. **GitHub 저장소** → **Settings** → **Branches** 이동
2. **Branch protection rules** → **Add rule** 클릭
3. **Branch name pattern**: `master` 입력
4. 다음 옵션 활성화:
   ```
   ✅ Require a pull request before merging
      ✅ Require approvals (1개 권장)
      ✅ Dismiss stale pull request approvals when new commits are pushed
   ✅ Require status checks to pass before merging (선택사항)
   ✅ Require conversation resolution before merging
   ✅ Require linear history (선택사항)
   ✅ Include administrators (관리자도 규칙 적용)
   ⚠️ Allow force pushes: 비활성화 (체크 해제)
   ⚠️ Allow deletions: 비활성화 (체크 해제)
   ```
5. **Create** 버튼 클릭

### 2. Develop을 기본 브랜치로 설정 ⭐ 권장!

1. **GitHub 저장소** → **Settings** → **Branches** 이동
2. **Default branch** 섹션
3. 오른쪽 **Switch to another branch** 버튼 클릭
4. `develop` 선택
5. **Update** 클릭
6. 경고 팝업에서 **I understand, update the default branch** 클릭

**장점**:
- 새로운 clone 시 자동으로 develop 체크아웃
- PR 생성 시 기본 타겟이 develop
- 협업자들이 자연스럽게 develop에서 작업

### 3. 기존 Master 브랜치와 Develop 동기화 (선택사항)

현재 master와 develop이 동일한 상태입니다. 필요시 다음을 실행:

```bash
# 로컬에서 확인
git checkout master
git pull origin master
git log --oneline -5

git checkout develop
git pull origin develop
git log --oneline -5

# 차이 확인
git log master..develop
```

### 4. README.md 업데이트 (선택사항)

README.md에 브랜치 전략 안내 추가:

```markdown
## Branching Strategy

This project uses a simplified Git Flow:
- `master`: Production branch (protected, deployed to GitHub Pages)
- `develop`: Development branch (default, receives daily posts)
- `develop-feature-*`: Feature branches

See [BRANCHING_STRATEGY.md](BRANCHING_STRATEGY.md) for details.
```

## 🧪 테스트

### 보호 설정 테스트

Master 브랜치 보호가 작동하는지 확인:

```bash
# 이 명령은 실패해야 함 (보호된 브랜치)
git checkout master
echo "test" >> test.txt
git add test.txt
git commit -m "Test commit"
git push origin master
# 예상 결과: remote rejected (protected branch)

# 정리
git reset HEAD~1
git checkout develop
```

### Workflow 테스트

Develop 브랜치에서 워크플로우 실행 확인:

1. **GitHub Actions** 탭 이동
2. **LeetCode Daily Challenge** 워크플로우 선택
3. **Run workflow** 클릭
4. Branch: `develop` 선택
5. **Run workflow** 실행
6. 완료 후 develop 브랜치에 커밋 확인

## 📋 일상 워크플로우 예시

### 새 기능 개발

```bash
# 1. 최신 develop pull
git checkout develop
git pull origin develop

# 2. Feature 브랜치 생성
git checkout -b develop-feature-add-tags-xyz123

# 3. 작업 및 커밋
# ... 코드 수정 ...
git add .
git commit -m "Add tag filtering feature"

# 4. Push 및 PR 생성
git push -u origin develop-feature-add-tags-xyz123
# GitHub에서 develop으로 PR 생성
```

### 릴리스 (Develop → Master)

```bash
# GitHub에서:
# 1. New Pull Request 클릭
# 2. base: master ← compare: develop
# 3. 제목: "Release: Week of 2025-11-18"
# 4. 설명에 변경사항 작성
# 5. Create pull request
# 6. 리뷰 및 Merge
```

## 🎉 완료 후

모든 설정이 완료되면:

1. ✅ Master는 프로덕션 전용 (직접 push 불가)
2. ✅ Develop은 개발 허브 (일일 포스트 자동 커밋)
3. ✅ Feature 브랜치로 격리된 개발
4. ✅ PR 리뷰 프로세스 강제
5. ✅ 안정적인 릴리스 관리

**이 파일은 설정 완료 후 삭제해도 됩니다.**
