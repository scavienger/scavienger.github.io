# AGENTS.md

이 레포는 Gemini만 사용합니다.

핵심 규칙:
- AI 모델: `gemini-3-pro-preview` (기본) → 429 시 `gemini-3-flash-preview` 폴백.
- Python SDK: `google-genai` 사용. `google-generativeai`는 사용하지 않음.
- `_site/`는 빌드 산출물이므로 수정하지 않음.
- 문서 업데이트 시 Groq/Llama/Qwen 관련 내용은 제거.

빠른 실행:
```
export GEMINI_API_KEY="your-key"
python scripts/generate_posts.py 2026-01-23
```
