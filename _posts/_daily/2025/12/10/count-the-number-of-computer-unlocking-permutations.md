---
layout: post
title: "Count the Number of Computer Unlocking Permutations"
date: 2025-12-10 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Math", "Brainteaser", "Combinatorics"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/
ai_solutions:
  - solutions:
      cpp: "// Generation failed for C++\n// Reason: Error: 429 You exceeded your current\
        \ quota, please check your plan and billing details. For more information on\
        \ this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To\
        \ monitor your current usage, head to: https://ai.dev/usage?tab=rate-limit.\
        \ \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests,\
        \ limit: 5, model: gemini-2.5-flash\nPlease retry in 25.922789297s. [links {\n\
        \  description: \"Learn more about Gemini API quotas\"\n  url: \"https://ai.google.dev/gemini-api/docs/rate-limits\"\
        \n}\n, violations {\n  quota_metric: \"generativelanguage.googleapis.com/generate_content_free_tier_requests\"\
        \n  quota_id: \"GenerateRequestsPerMinutePerProjectPerModel-FreeTier\"\n  quota_dimensions\
        \ {\n    key: \"model\"\n    value: \"gemini-2.5-flash\"\n  }\n  quota_dimensions\
        \ {\n    key: \"location\"\n    value: \"global\"\n  }\n  quota_value: 5\n}\n\
        , retry_delay {\n  seconds: 25\n}\n]"
      java: "// Generation failed for Java\n// Reason: Error: 429 You exceeded your\
        \ current quota, please check your plan and billing details. For more information\
        \ on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits.\
        \ To monitor your current usage, head to: https://ai.dev/usage?tab=rate-limit.\
        \ \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests,\
        \ limit: 5, model: gemini-2.5-flash\nPlease retry in 25.922789297s. [links {\n\
        \  description: \"Learn more about Gemini API quotas\"\n  url: \"https://ai.google.dev/gemini-api/docs/rate-limits\"\
        \n}\n, violations {\n  quota_metric: \"generativelanguage.googleapis.com/generate_content_free_tier_requests\"\
        \n  quota_id: \"GenerateRequestsPerMinutePerProjectPerModel-FreeTier\"\n  quota_dimensions\
        \ {\n    key: \"model\"\n    value: \"gemini-2.5-flash\"\n  }\n  quota_dimensions\
        \ {\n    key: \"location\"\n    value: \"global\"\n  }\n  quota_value: 5\n}\n\
        , retry_delay {\n  seconds: 25\n}\n]"
      python: "// Generation failed for Python\n// Reason: Error: 429 You exceeded your\
        \ current quota, please check your plan and billing details. For more information\
        \ on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits.\
        \ To monitor your current usage, head to: https://ai.dev/usage?tab=rate-limit.\
        \ \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests,\
        \ limit: 5, model: gemini-2.5-flash\nPlease retry in 25.922789297s. [links {\n\
        \  description: \"Learn more about Gemini API quotas\"\n  url: \"https://ai.google.dev/gemini-api/docs/rate-limits\"\
        \n}\n, violations {\n  quota_metric: \"generativelanguage.googleapis.com/generate_content_free_tier_requests\"\
        \n  quota_id: \"GenerateRequestsPerMinutePerProjectPerModel-FreeTier\"\n  quota_dimensions\
        \ {\n    key: \"model\"\n    value: \"gemini-2.5-flash\"\n  }\n  quota_dimensions\
        \ {\n    key: \"location\"\n    value: \"global\"\n  }\n  quota_value: 5\n}\n\
        , retry_delay {\n  seconds: 25\n}\n]"
      python3: "// Generation failed for Python3\n// Reason: Error: 429 You exceeded\
        \ your current quota, please check your plan and billing details. For more information\
        \ on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits.\
        \ To monitor your current usage, head to: https://ai.dev/usage?tab=rate-limit.\
        \ \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests,\
        \ limit: 5, model: gemini-2.5-flash\nPlease retry in 25.922789297s. [links {\n\
        \  description: \"Learn more about Gemini API quotas\"\n  url: \"https://ai.google.dev/gemini-api/docs/rate-limits\"\
        \n}\n, violations {\n  quota_metric: \"generativelanguage.googleapis.com/generate_content_free_tier_requests\"\
        \n  quota_id: \"GenerateRequestsPerMinutePerProjectPerModel-FreeTier\"\n  quota_dimensions\
        \ {\n    key: \"model\"\n    value: \"gemini-2.5-flash\"\n  }\n  quota_dimensions\
        \ {\n    key: \"location\"\n    value: \"global\"\n  }\n  quota_value: 5\n}\n\
        , retry_delay {\n  seconds: 25\n}\n]"
      c: "// Generation failed for C\n// Reason: Error: 429 You exceeded your current\
        \ quota, please check your plan and billing details. For more information on\
        \ this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To\
        \ monitor your current usage, head to: https://ai.dev/usage?tab=rate-limit.\
        \ \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests,\
        \ limit: 5, model: gemini-2.5-flash\nPlease retry in 25.922789297s. [links {\n\
        \  description: \"Learn more about Gemini API quotas\"\n  url: \"https://ai.google.dev/gemini-api/docs/rate-limits\"\
        \n}\n, violations {\n  quota_metric: \"generativelanguage.googleapis.com/generate_content_free_tier_requests\"\
        \n  quota_id: \"GenerateRequestsPerMinutePerProjectPerModel-FreeTier\"\n  quota_dimensions\
        \ {\n    key: \"model\"\n    value: \"gemini-2.5-flash\"\n  }\n  quota_dimensions\
        \ {\n    key: \"location\"\n    value: \"global\"\n  }\n  quota_value: 5\n}\n\
        , retry_delay {\n  seconds: 25\n}\n]"
      csharp: "// Generation failed for C#\n// Reason: Error: 429 You exceeded your\
        \ current quota, please check your plan and billing details. For more information\
        \ on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits.\
        \ To monitor your current usage, head to: https://ai.dev/usage?tab=rate-limit.\
        \ \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests,\
        \ limit: 5, model: gemini-2.5-flash\nPlease retry in 25.922789297s. [links {\n\
        \  description: \"Learn more about Gemini API quotas\"\n  url: \"https://ai.google.dev/gemini-api/docs/rate-limits\"\
        \n}\n, violations {\n  quota_metric: \"generativelanguage.googleapis.com/generate_content_free_tier_requests\"\
        \n  quota_id: \"GenerateRequestsPerMinutePerProjectPerModel-FreeTier\"\n  quota_dimensions\
        \ {\n    key: \"model\"\n    value: \"gemini-2.5-flash\"\n  }\n  quota_dimensions\
        \ {\n    key: \"location\"\n    value: \"global\"\n  }\n  quota_value: 5\n}\n\
        , retry_delay {\n  seconds: 25\n}\n]"
      javascript: "// Generation failed for JavaScript\n// Reason: Error: 429 You exceeded\
        \ your current quota, please check your plan and billing details. For more information\
        \ on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits.\
        \ To monitor your current usage, head to: https://ai.dev/usage?tab=rate-limit.\
        \ \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests,\
        \ limit: 5, model: gemini-2.5-flash\nPlease retry in 25.922789297s. [links {\n\
        \  description: \"Learn more about Gemini API quotas\"\n  url: \"https://ai.google.dev/gemini-api/docs/rate-limits\"\
        \n}\n, violations {\n  quota_metric: \"generativelanguage.googleapis.com/generate_content_free_tier_requests\"\
        \n  quota_id: \"GenerateRequestsPerMinutePerProjectPerModel-FreeTier\"\n  quota_dimensions\
        \ {\n    key: \"model\"\n    value: \"gemini-2.5-flash\"\n  }\n  quota_dimensions\
        \ {\n    key: \"location\"\n    value: \"global\"\n  }\n  quota_value: 5\n}\n\
        , retry_delay {\n  seconds: 25\n}\n]"
      typescript: "// Generation failed for TypeScript\n// Reason: Error: 429 You exceeded\
        \ your current quota, please check your plan and billing details. For more information\
        \ on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits.\
        \ To monitor your current usage, head to: https://ai.dev/usage?tab=rate-limit.\
        \ \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests,\
        \ limit: 5, model: gemini-2.5-flash\nPlease retry in 25.922789297s. [links {\n\
        \  description: \"Learn more about Gemini API quotas\"\n  url: \"https://ai.google.dev/gemini-api/docs/rate-limits\"\
        \n}\n, violations {\n  quota_metric: \"generativelanguage.googleapis.com/generate_content_free_tier_requests\"\
        \n  quota_id: \"GenerateRequestsPerMinutePerProjectPerModel-FreeTier\"\n  quota_dimensions\
        \ {\n    key: \"model\"\n    value: \"gemini-2.5-flash\"\n  }\n  quota_dimensions\
        \ {\n    key: \"location\"\n    value: \"global\"\n  }\n  quota_value: 5\n}\n\
        , retry_delay {\n  seconds: 25\n}\n]"
      php: "// Generation failed for PHP\n// Reason: Error: 429 You exceeded your current\
        \ quota, please check your plan and billing details. For more information on\
        \ this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To\
        \ monitor your current usage, head to: https://ai.dev/usage?tab=rate-limit.\
        \ \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests,\
        \ limit: 5, model: gemini-2.5-flash\nPlease retry in 25.922789297s. [links {\n\
        \  description: \"Learn more about Gemini API quotas\"\n  url: \"https://ai.google.dev/gemini-api/docs/rate-limits\"\
        \n}\n, violations {\n  quota_metric: \"generativelanguage.googleapis.com/generate_content_free_tier_requests\"\
        \n  quota_id: \"GenerateRequestsPerMinutePerProjectPerModel-FreeTier\"\n  quota_dimensions\
        \ {\n    key: \"model\"\n    value: \"gemini-2.5-flash\"\n  }\n  quota_dimensions\
        \ {\n    key: \"location\"\n    value: \"global\"\n  }\n  quota_value: 5\n}\n\
        , retry_delay {\n  seconds: 25\n}\n]"
      swift: "// Generation failed for Swift\n// Reason: Error: 429 You exceeded your\
        \ current quota, please check your plan and billing details. For more information\
        \ on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits.\
        \ To monitor your current usage, head to: https://ai.dev/usage?tab=rate-limit.\
        \ \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests,\
        \ limit: 5, model: gemini-2.5-flash\nPlease retry in 25.922789297s. [links {\n\
        \  description: \"Learn more about Gemini API quotas\"\n  url: \"https://ai.google.dev/gemini-api/docs/rate-limits\"\
        \n}\n, violations {\n  quota_metric: \"generativelanguage.googleapis.com/generate_content_free_tier_requests\"\
        \n  quota_id: \"GenerateRequestsPerMinutePerProjectPerModel-FreeTier\"\n  quota_dimensions\
        \ {\n    key: \"model\"\n    value: \"gemini-2.5-flash\"\n  }\n  quota_dimensions\
        \ {\n    key: \"location\"\n    value: \"global\"\n  }\n  quota_value: 5\n}\n\
        , retry_delay {\n  seconds: 25\n}\n]"
      kotlin: "// Generation failed for Kotlin\n// Reason: Error: 429 You exceeded your\
        \ current quota, please check your plan and billing details. For more information\
        \ on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits.\
        \ To monitor your current usage, head to: https://ai.dev/usage?tab=rate-limit.\
        \ \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests,\
        \ limit: 5, model: gemini-2.5-flash\nPlease retry in 25.922789297s. [links {\n\
        \  description: \"Learn more about Gemini API quotas\"\n  url: \"https://ai.google.dev/gemini-api/docs/rate-limits\"\
        \n}\n, violations {\n  quota_metric: \"generativelanguage.googleapis.com/generate_content_free_tier_requests\"\
        \n  quota_id: \"GenerateRequestsPerMinutePerProjectPerModel-FreeTier\"\n  quota_dimensions\
        \ {\n    key: \"model\"\n    value: \"gemini-2.5-flash\"\n  }\n  quota_dimensions\
        \ {\n    key: \"location\"\n    value: \"global\"\n  }\n  quota_value: 5\n}\n\
        , retry_delay {\n  seconds: 25\n}\n]"
      dart: "// Generation failed for Dart\n// Reason: Error: 429 You exceeded your\
        \ current quota, please check your plan and billing details. For more information\
        \ on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits.\
        \ To monitor your current usage, head to: https://ai.dev/usage?tab=rate-limit.\
        \ \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests,\
        \ limit: 5, model: gemini-2.5-flash\nPlease retry in 25.922789297s. [links {\n\
        \  description: \"Learn more about Gemini API quotas\"\n  url: \"https://ai.google.dev/gemini-api/docs/rate-limits\"\
        \n}\n, violations {\n  quota_metric: \"generativelanguage.googleapis.com/generate_content_free_tier_requests\"\
        \n  quota_id: \"GenerateRequestsPerMinutePerProjectPerModel-FreeTier\"\n  quota_dimensions\
        \ {\n    key: \"model\"\n    value: \"gemini-2.5-flash\"\n  }\n  quota_dimensions\
        \ {\n    key: \"location\"\n    value: \"global\"\n  }\n  quota_value: 5\n}\n\
        , retry_delay {\n  seconds: 25\n}\n]"
      go: "// Generation failed for Go\n// Reason: Error: 429 You exceeded your current\
        \ quota, please check your plan and billing details. For more information on\
        \ this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To\
        \ monitor your current usage, head to: https://ai.dev/usage?tab=rate-limit.\
        \ \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests,\
        \ limit: 5, model: gemini-2.5-flash\nPlease retry in 25.922789297s. [links {\n\
        \  description: \"Learn more about Gemini API quotas\"\n  url: \"https://ai.google.dev/gemini-api/docs/rate-limits\"\
        \n}\n, violations {\n  quota_metric: \"generativelanguage.googleapis.com/generate_content_free_tier_requests\"\
        \n  quota_id: \"GenerateRequestsPerMinutePerProjectPerModel-FreeTier\"\n  quota_dimensions\
        \ {\n    key: \"model\"\n    value: \"gemini-2.5-flash\"\n  }\n  quota_dimensions\
        \ {\n    key: \"location\"\n    value: \"global\"\n  }\n  quota_value: 5\n}\n\
        , retry_delay {\n  seconds: 25\n}\n]"
      ruby: "// Generation failed for Ruby\n// Reason: Error: 429 You exceeded your\
        \ current quota, please check your plan and billing details. For more information\
        \ on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits.\
        \ To monitor your current usage, head to: https://ai.dev/usage?tab=rate-limit.\
        \ \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests,\
        \ limit: 5, model: gemini-2.5-flash\nPlease retry in 25.922789297s. [links {\n\
        \  description: \"Learn more about Gemini API quotas\"\n  url: \"https://ai.google.dev/gemini-api/docs/rate-limits\"\
        \n}\n, violations {\n  quota_metric: \"generativelanguage.googleapis.com/generate_content_free_tier_requests\"\
        \n  quota_id: \"GenerateRequestsPerMinutePerProjectPerModel-FreeTier\"\n  quota_dimensions\
        \ {\n    key: \"model\"\n    value: \"gemini-2.5-flash\"\n  }\n  quota_dimensions\
        \ {\n    key: \"location\"\n    value: \"global\"\n  }\n  quota_value: 5\n}\n\
        , retry_delay {\n  seconds: 25\n}\n]"
      scala: "// Generation failed for Scala\n// Reason: Error: 429 You exceeded your\
        \ current quota, please check your plan and billing details. For more information\
        \ on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits.\
        \ To monitor your current usage, head to: https://ai.dev/usage?tab=rate-limit.\
        \ \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests,\
        \ limit: 5, model: gemini-2.5-flash\nPlease retry in 25.922789297s. [links {\n\
        \  description: \"Learn more about Gemini API quotas\"\n  url: \"https://ai.google.dev/gemini-api/docs/rate-limits\"\
        \n}\n, violations {\n  quota_metric: \"generativelanguage.googleapis.com/generate_content_free_tier_requests\"\
        \n  quota_id: \"GenerateRequestsPerMinutePerProjectPerModel-FreeTier\"\n  quota_dimensions\
        \ {\n    key: \"model\"\n    value: \"gemini-2.5-flash\"\n  }\n  quota_dimensions\
        \ {\n    key: \"location\"\n    value: \"global\"\n  }\n  quota_value: 5\n}\n\
        , retry_delay {\n  seconds: 25\n}\n]"
      rust: "// Generation failed for Rust\n// Reason: Error: 429 You exceeded your\
        \ current quota, please check your plan and billing details. For more information\
        \ on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits.\
        \ To monitor your current usage, head to: https://ai.dev/usage?tab=rate-limit.\
        \ \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests,\
        \ limit: 5, model: gemini-2.5-flash\nPlease retry in 25.922789297s. [links {\n\
        \  description: \"Learn more about Gemini API quotas\"\n  url: \"https://ai.google.dev/gemini-api/docs/rate-limits\"\
        \n}\n, violations {\n  quota_metric: \"generativelanguage.googleapis.com/generate_content_free_tier_requests\"\
        \n  quota_id: \"GenerateRequestsPerMinutePerProjectPerModel-FreeTier\"\n  quota_dimensions\
        \ {\n    key: \"model\"\n    value: \"gemini-2.5-flash\"\n  }\n  quota_dimensions\
        \ {\n    key: \"location\"\n    value: \"global\"\n  }\n  quota_value: 5\n}\n\
        , retry_delay {\n  seconds: 25\n}\n]"
      racket: "// Generation failed for Racket\n// Reason: Error: 429 You exceeded your\
        \ current quota, please check your plan and billing details. For more information\
        \ on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits.\
        \ To monitor your current usage, head to: https://ai.dev/usage?tab=rate-limit.\
        \ \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests,\
        \ limit: 5, model: gemini-2.5-flash\nPlease retry in 25.922789297s. [links {\n\
        \  description: \"Learn more about Gemini API quotas\"\n  url: \"https://ai.google.dev/gemini-api/docs/rate-limits\"\
        \n}\n, violations {\n  quota_metric: \"generativelanguage.googleapis.com/generate_content_free_tier_requests\"\
        \n  quota_id: \"GenerateRequestsPerMinutePerProjectPerModel-FreeTier\"\n  quota_dimensions\
        \ {\n    key: \"model\"\n    value: \"gemini-2.5-flash\"\n  }\n  quota_dimensions\
        \ {\n    key: \"location\"\n    value: \"global\"\n  }\n  quota_value: 5\n}\n\
        , retry_delay {\n  seconds: 25\n}\n]"
      erlang: "// Generation failed for Erlang\n// Reason: Error: 429 You exceeded your\
        \ current quota, please check your plan and billing details. For more information\
        \ on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits.\
        \ To monitor your current usage, head to: https://ai.dev/usage?tab=rate-limit.\
        \ \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests,\
        \ limit: 5, model: gemini-2.5-flash\nPlease retry in 25.922789297s. [links {\n\
        \  description: \"Learn more about Gemini API quotas\"\n  url: \"https://ai.google.dev/gemini-api/docs/rate-limits\"\
        \n}\n, violations {\n  quota_metric: \"generativelanguage.googleapis.com/generate_content_free_tier_requests\"\
        \n  quota_id: \"GenerateRequestsPerMinutePerProjectPerModel-FreeTier\"\n  quota_dimensions\
        \ {\n    key: \"model\"\n    value: \"gemini-2.5-flash\"\n  }\n  quota_dimensions\
        \ {\n    key: \"location\"\n    value: \"global\"\n  }\n  quota_value: 5\n}\n\
        , retry_delay {\n  seconds: 25\n}\n]"
      elixir: "// Generation failed for Elixir\n// Reason: Error: 429 You exceeded your\
        \ current quota, please check your plan and billing details. For more information\
        \ on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits.\
        \ To monitor your current usage, head to: https://ai.dev/usage?tab=rate-limit.\
        \ \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests,\
        \ limit: 5, model: gemini-2.5-flash\nPlease retry in 25.922789297s. [links {\n\
        \  description: \"Learn more about Gemini API quotas\"\n  url: \"https://ai.google.dev/gemini-api/docs/rate-limits\"\
        \n}\n, violations {\n  quota_metric: \"generativelanguage.googleapis.com/generate_content_free_tier_requests\"\
        \n  quota_id: \"GenerateRequestsPerMinutePerProjectPerModel-FreeTier\"\n  quota_dimensions\
        \ {\n    key: \"model\"\n    value: \"gemini-2.5-flash\"\n  }\n  quota_dimensions\
        \ {\n    key: \"location\"\n    value: \"global\"\n  }\n  quota_value: 5\n}\n\
        , retry_delay {\n  seconds: 25\n}\n]"
    elapsed_time: 0.0
    model: gemini-2.5-flash
    generated_at: '2025-12-10 01:08:34 '
  - solutions:
      cpp: "class Solution {\npublic:\n    int countPermutations(vector<int>& complexity)\
        \ {\n        int n = complexity.size();\n        int MOD = 1e9 + 7;\n      \
        \  if (complexity[0] != *min_element(complexity.begin(), complexity.end()))\
        \ return 0;\n        long long res = 1;\n        for (int i = 1; i < n; i++)\
        \ {\n            res = (res * i) % MOD;\n        }\n        return res;\n  \
        \  }\n};"
      java: "class Solution {\n    public int countPermutations(int[] complexity) {\n\
        \        int n = complexity.length;\n        int MOD = (int)1e9 + 7;\n     \
        \   if (complexity[0] != Arrays.stream(complexity).min().getAsInt()) return\
        \ 0;\n        long res = 1;\n        for (int i = 1; i < n; i++) {\n       \
        \     res = (res * i) % MOD;\n        }\n        return (int)res;\n    }\n}"
      python: "class Solution:\n    def countPermutations(self, complexity: list[int])\
        \ -> int:\n        n = len(complexity)\n        MOD = 10**9 + 7\n        if\
        \ complexity[0] != min(complexity): return 0\n        res = 1\n        for i\
        \ in range(1, n):\n            res = (res * i) % MOD\n        return res"
      python3: "class Solution:\n    def countPermutations(self, complexity: list[int])\
        \ -> int:\n        n = len(complexity)\n        MOD = 10**9 + 7\n        if\
        \ complexity[0] != min(complexity): return 0\n        res = 1\n        for i\
        \ in range(1, n):\n            res = (res * i) % MOD\n        return res"
      c: "int countPermutations(int* complexity, int complexitySize) {\n    int MOD\
        \ = 1000000007;\n    int res = 1;\n    if (complexity[0] != *min_element(complexity,\
        \ complexity + complexitySize)) return 0;\n    for (int i = 1; i < complexitySize;\
        \ i++) {\n        res = (res * i) % MOD;\n    }\n    return res;\n}"
      csharp: "public class Solution {\n    public int CountPermutations(int[] complexity)\
        \ {\n        int n = complexity.Length;\n        int MOD = 1000000007;\n   \
        \     if (complexity[0] != complexity.Min()) return 0;\n        long res = 1;\n\
        \        for (int i = 1; i < n; i++) {\n            res = (res * i) % MOD;\n\
        \        }\n        return (int)res;\n    }\n}"
      javascript: "var countPermutations = function(complexity) {\n    let n = complexity.length;\n\
        \    let MOD = 1000000007;\n    if (complexity[0] != Math.min(...complexity))\
        \ return 0;\n    let res = 1;\n    for (let i = 1; i < n; i++) {\n        res\
        \ = (res * i) % MOD;\n    }\n    return res;\n};"
      typescript: "function countPermutations(complexity: number[]): number {\n    let\
        \ n = complexity.length;\n    let MOD = 1000000007;\n    if (complexity[0] !=\
        \ Math.min(...complexity)) return 0;\n    let res = 1;\n    for (let i = 1;\
        \ i < n; i++) {\n        res = (res * i) % MOD;\n    }\n    return res;\n}"
      php: "$MOD = 1000000007;\nfunction countPermutations($complexity) {\n    $n =\
        \ count($complexity);\n    if ($complexity[0] != min($complexity)) return 0;\n\
        \    $res = 1;\n    for ($i = 1; $i < $n; $i++) {\n        $res = ($res * $i)\
        \ % $GLOBALS['MOD'];\n    }\n    return $res;\n}"
      swift: "class Solution {\n    func countPermutations(_ complexity: [Int]) -> Int\
        \ {\n        let n = complexity.count\n        let MOD = 1000000007\n      \
        \  if complexity[0] != complexity.min()! return 0\n        var res = 1\n   \
        \     for i in 1..<n {\n            res = (res * i) % MOD\n        }\n     \
        \   return res\n    }\n}"
      kotlin: "class Solution {\n    fun countPermutations(complexity: IntArray): Int\
        \ {\n        val n = complexity.size\n        val MOD = 1000000007\n       \
        \ if (complexity[0] != complexity.minOrNull()!!) return 0\n        var res =\
        \ 1\n        for (i in 1 until n) {\n            res = (res * i) % MOD\n   \
        \     }\n        return res\n    }\n}"
      dart: "class Solution {\n    int countPermutations(List<int> complexity) {\n \
        \       int n = complexity.length;\n        int MOD = 1000000007;\n        if\
        \ (complexity[0] != complexity.reduce((a, b) => a < b ? a : b)) return 0;\n\
        \        int res = 1;\n        for (int i = 1; i < n; i++) {\n            res\
        \ = (res * i) % MOD;\n        }\n        return res;\n    }\n}"
      go: "func countPermutations(complexity []int) int {\n    n := len(complexity)\n\
        \    MOD := 1000000007\n    if complexity[0] != min(complexity) { return 0 }\n\
        \    res := 1\n    for i := 1; i < n; i++ {\n        res = (res * i) % MOD\n\
        \    }\n    return res\n}\nfunc min(arr []int) int {\n    min := arr[0]\n  \
        \  for _, v := range arr {\n        if v < min { min = v }\n    }\n    return\
        \ min\n}"
      ruby: "def count_permutations(complexity)\n    n = complexity.size\n    MOD =\
        \ 1000000007\n    if complexity[0] != complexity.min return 0 end\n    res =\
        \ 1\n    (1...n).each do |i|\n        res = (res * i) % MOD\n    end\n    res\n\
        end"
      scala: "object Solution {\n    def countPermutations(complexity: Array[Int]):\
        \ Int = {\n        val n = complexity.length\n        val MOD = 1000000007\n\
        \        if (complexity(0) != complexity.min) return 0\n        var res = 1\n\
        \        for (i <- 1 until n) {\n            res = (res * i) % MOD\n       \
        \ }\n        res\n    }\n}"
      rust: "impl Solution {\n    pub fn count_permutations(complexity: Vec<i32>) ->\
        \ i32 {\n        let n = complexity.len();\n        let MOD = 1000000007;\n\
        \        if complexity[0] != *complexity.iter().min().unwrap() { return 0; }\n\
        \        let mut res = 1;\n        for i in 1..n {\n            res = (res *\
        \ i as i32) % MOD;\n        }\n        res\n    }\n}"
      racket: "(define (count-permutations complexity)\n    (let ((n (length complexity))\n\
        \          (MOD 1000000007))\n        (if (not (= (car complexity) (apply min\
        \ complexity)))\n            0\n            (let loop ((i 1) (res 1))\n    \
        \            (if (= i n)\n                    res\n                    (loop\
        \ (+ i 1) (modulo (* res i) MOD)))))))"
      erlang: '-module(solution).

        -export([count_permutations/1]).


        count_permutations(Complexity) ->

        N = length(Complexity),

        MOD = 1000000007,

        case lists:min(Complexity) of

        [H | _] when H =:= lists:nth(1, Complexity) ->

        count_permutations(Complexity, 1, 1, MOD, N);

        _ -> 0

        end.


        count_permutations(_Complexity, I, Res, MOD, N) when I =:= N -> Res;

        count_permutations(Complexity, I, Res, MOD, N) ->

        count_permutations(Complexity, I + 1, (Res * I) rem MOD, MOD, N).'
      elixir: "defmodule Solution do\n    def count_permutations(complexity) do\n  \
        \      n = length(complexity)\n        mod = 1_000_000_007\n        if Enum.min(complexity)\
        \ != Enum.at(complexity, 0) do\n            0\n        else\n            count_permutations(complexity,\
        \ 1, 1, mod, n)\n        end\n    end\n    defp count_permutations(_complexity,\
        \ i, res, mod, n) when i == n do\n        res\n    end\n    defp count_permutations(complexity,\
        \ i, res, mod, n) do\n        count_permutations(complexity, i + 1, rem(res\
        \ * i, mod), mod, n)\n    end\nend"
    approach: The problem can be solved by first checking if the complexity of the first
      computer is unique and less than all other complexities. If this condition is
      met, we can fix the first computer as the starting point and arrange the remaining
      computers in any order, resulting in (n-1)! permutations. However, if there are
      other computers with the same complexity as the first one, or if the first computer's
      complexity is not the minimum, we need to return 0 because there are no valid
      permutations. The key intuition here is that the first computer must have a unique
      minimum complexity to ensure that it can unlock all other computers.
    time_complexity: The time complexity of this solution is O(n) because we need to
      iterate through the complexity array to check if the first computer's complexity
      is unique and less than all other complexities. Additionally, we need to calculate
      the factorial of (n-1), which can be done in O(n) time using a loop or a recursive
      function.
    space_complexity: The space complexity of this solution is O(1) because we only
      need a constant amount of space to store the complexity array and the result.
      We do not need any additional data structures that scale with the input size.
    elapsed_time: 5.447366952896118
    model: llama-3.3-70b-versatile
    generated_at: '2025-12-10 01:08:39 '
---

## Problem #3577: Count the Number of Computer Unlocking Permutations

**Difficulty:** Medium

**Topics:** Array, Math, Brainteaser, Combinatorics

## Problem Description

<p>You are given an array <code>complexity</code> of length <code>n</code>.</p>

<p>There are <code>n</code> <strong>locked</strong> computers in a room with labels from 0 to <code>n - 1</code>, each with its own <strong>unique</strong> password. The password of the computer <code>i</code> has a complexity <code>complexity[i]</code>.</p>

<p>The password for the computer labeled 0 is <strong>already</strong> decrypted and serves as the root. All other computers must be unlocked using it or another previously unlocked computer, following this information:</p>

<ul>
	<li>You can decrypt the password for the computer <code>i</code> using the password for computer <code>j</code>, where <code>j</code> is <strong>any</strong> integer less than <code>i</code> with a lower complexity. (i.e. <code>j &lt; i</code> and <code>complexity[j] &lt; complexity[i]</code>)</li>
	<li>To decrypt the password for computer <code>i</code>, you must have already unlocked a computer <code>j</code> such that <code>j &lt; i</code> and <code>complexity[j] &lt; complexity[i]</code>.</li>
</ul>

<p>Find the number of <span data-keyword="permutation-array">permutations</span> of <code>[0, 1, 2, ..., (n - 1)]</code> that represent a valid order in which the computers can be unlocked, starting from computer 0 as the only initially unlocked one.</p>

<p>Since the answer may be large, return it <strong>modulo</strong> 10<sup>9</sup> + 7.</p>

<p><strong>Note</strong> that the password for the computer <strong>with label</strong> 0 is decrypted, and <em>not</em> the computer with the first position in the permutation.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">complexity = [1,2,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>The valid permutations are:</p>

<ul>
	<li>[0, 1, 2]
	<ul>
		<li>Unlock computer 0 first with root password.</li>
		<li>Unlock computer 1 with password of computer 0 since <code>complexity[0] &lt; complexity[1]</code>.</li>
		<li>Unlock computer 2 with password of computer 1 since <code>complexity[1] &lt; complexity[2]</code>.</li>
	</ul>
	</li>
	<li>[0, 2, 1]
	<ul>
		<li>Unlock computer 0 first with root password.</li>
		<li>Unlock computer 2 with password of computer 0 since <code>complexity[0] &lt; complexity[2]</code>.</li>
		<li>Unlock computer 1 with password of computer 0 since <code>complexity[0] &lt; complexity[1]</code>.</li>
	</ul>
	</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">complexity = [3,3,3,4,4,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>There are no possible permutations which can unlock all computers.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= complexity.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= complexity[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## Hints

1. Ensure that the element at index 0 has the unique minimum complexity (no other element can match its value).

2. Fix index 0 as the first in the unlocking order.

3. The remaining indices from `1` to `n - 1` can then be arranged arbitrarily, yielding `factorial(n - 1)` possible orders.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-12-10 01:08:34 )</small>
</summary>

<div class="ai-solution-content">

### Approach

No approach provided

### Code

<div class="code-tabs" markdown="0">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-cpp-gemini-2-5-flash" checked>
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-java-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-python-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-python3-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-c-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-csharp-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-javascript-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-typescript-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-php-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-swift-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-kotlin-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-dart-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-go-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-ruby-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-scala-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-rust-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-racket-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-erlang-gemini-2-5-flash">
  <input type="radio" name="code-lang-gemini-2-5-flash" id="lang-elixir-gemini-2-5-flash">
  <div class="tab-labels">
    <label for="lang-cpp-gemini-2-5-flash">C++</label>
    <label for="lang-java-gemini-2-5-flash">Java</label>
    <label for="lang-python-gemini-2-5-flash">Python</label>
    <label for="lang-python3-gemini-2-5-flash">Python3</label>
    <label for="lang-c-gemini-2-5-flash">C</label>
    <label for="lang-csharp-gemini-2-5-flash">C#</label>
    <label for="lang-javascript-gemini-2-5-flash">JavaScript</label>
    <label for="lang-typescript-gemini-2-5-flash">TypeScript</label>
    <label for="lang-php-gemini-2-5-flash">PHP</label>
    <label for="lang-swift-gemini-2-5-flash">Swift</label>
    <label for="lang-kotlin-gemini-2-5-flash">Kotlin</label>
    <label for="lang-dart-gemini-2-5-flash">Dart</label>
    <label for="lang-go-gemini-2-5-flash">Go</label>
    <label for="lang-ruby-gemini-2-5-flash">Ruby</label>
    <label for="lang-scala-gemini-2-5-flash">Scala</label>
    <label for="lang-rust-gemini-2-5-flash">Rust</label>
    <label for="lang-racket-gemini-2-5-flash">Racket</label>
    <label for="lang-erlang-gemini-2-5-flash">Erlang</label>
    <label for="lang-elixir-gemini-2-5-flash">Elixir</label>
  </div>

  <div class="tab-panel" data-lang="cpp">

{% highlight cpp %}
{% raw %}
// Generation failed for C++
// Reason: Error: 429 You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/usage?tab=rate-limit. 
* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-2.5-flash
Please retry in 25.922789297s. [links {
  description: "Learn more about Gemini API quotas"
  url: "https://ai.google.dev/gemini-api/docs/rate-limits"
}
, violations {
  quota_metric: "generativelanguage.googleapis.com/generate_content_free_tier_requests"
  quota_id: "GenerateRequestsPerMinutePerProjectPerModel-FreeTier"
  quota_dimensions {
    key: "model"
    value: "gemini-2.5-flash"
  }
  quota_dimensions {
    key: "location"
    value: "global"
  }
  quota_value: 5
}
, retry_delay {
  seconds: 25
}
]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
// Generation failed for Java
// Reason: Error: 429 You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/usage?tab=rate-limit. 
* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-2.5-flash
Please retry in 25.922789297s. [links {
  description: "Learn more about Gemini API quotas"
  url: "https://ai.google.dev/gemini-api/docs/rate-limits"
}
, violations {
  quota_metric: "generativelanguage.googleapis.com/generate_content_free_tier_requests"
  quota_id: "GenerateRequestsPerMinutePerProjectPerModel-FreeTier"
  quota_dimensions {
    key: "model"
    value: "gemini-2.5-flash"
  }
  quota_dimensions {
    key: "location"
    value: "global"
  }
  quota_value: 5
}
, retry_delay {
  seconds: 25
}
]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
// Generation failed for Python
// Reason: Error: 429 You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/usage?tab=rate-limit. 
* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-2.5-flash
Please retry in 25.922789297s. [links {
  description: "Learn more about Gemini API quotas"
  url: "https://ai.google.dev/gemini-api/docs/rate-limits"
}
, violations {
  quota_metric: "generativelanguage.googleapis.com/generate_content_free_tier_requests"
  quota_id: "GenerateRequestsPerMinutePerProjectPerModel-FreeTier"
  quota_dimensions {
    key: "model"
    value: "gemini-2.5-flash"
  }
  quota_dimensions {
    key: "location"
    value: "global"
  }
  quota_value: 5
}
, retry_delay {
  seconds: 25
}
]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
// Generation failed for Python3
// Reason: Error: 429 You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/usage?tab=rate-limit. 
* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-2.5-flash
Please retry in 25.922789297s. [links {
  description: "Learn more about Gemini API quotas"
  url: "https://ai.google.dev/gemini-api/docs/rate-limits"
}
, violations {
  quota_metric: "generativelanguage.googleapis.com/generate_content_free_tier_requests"
  quota_id: "GenerateRequestsPerMinutePerProjectPerModel-FreeTier"
  quota_dimensions {
    key: "model"
    value: "gemini-2.5-flash"
  }
  quota_dimensions {
    key: "location"
    value: "global"
  }
  quota_value: 5
}
, retry_delay {
  seconds: 25
}
]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
// Generation failed for C
// Reason: Error: 429 You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/usage?tab=rate-limit. 
* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-2.5-flash
Please retry in 25.922789297s. [links {
  description: "Learn more about Gemini API quotas"
  url: "https://ai.google.dev/gemini-api/docs/rate-limits"
}
, violations {
  quota_metric: "generativelanguage.googleapis.com/generate_content_free_tier_requests"
  quota_id: "GenerateRequestsPerMinutePerProjectPerModel-FreeTier"
  quota_dimensions {
    key: "model"
    value: "gemini-2.5-flash"
  }
  quota_dimensions {
    key: "location"
    value: "global"
  }
  quota_value: 5
}
, retry_delay {
  seconds: 25
}
]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
// Generation failed for C#
// Reason: Error: 429 You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/usage?tab=rate-limit. 
* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-2.5-flash
Please retry in 25.922789297s. [links {
  description: "Learn more about Gemini API quotas"
  url: "https://ai.google.dev/gemini-api/docs/rate-limits"
}
, violations {
  quota_metric: "generativelanguage.googleapis.com/generate_content_free_tier_requests"
  quota_id: "GenerateRequestsPerMinutePerProjectPerModel-FreeTier"
  quota_dimensions {
    key: "model"
    value: "gemini-2.5-flash"
  }
  quota_dimensions {
    key: "location"
    value: "global"
  }
  quota_value: 5
}
, retry_delay {
  seconds: 25
}
]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
// Generation failed for JavaScript
// Reason: Error: 429 You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/usage?tab=rate-limit. 
* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-2.5-flash
Please retry in 25.922789297s. [links {
  description: "Learn more about Gemini API quotas"
  url: "https://ai.google.dev/gemini-api/docs/rate-limits"
}
, violations {
  quota_metric: "generativelanguage.googleapis.com/generate_content_free_tier_requests"
  quota_id: "GenerateRequestsPerMinutePerProjectPerModel-FreeTier"
  quota_dimensions {
    key: "model"
    value: "gemini-2.5-flash"
  }
  quota_dimensions {
    key: "location"
    value: "global"
  }
  quota_value: 5
}
, retry_delay {
  seconds: 25
}
]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
// Generation failed for TypeScript
// Reason: Error: 429 You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/usage?tab=rate-limit. 
* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-2.5-flash
Please retry in 25.922789297s. [links {
  description: "Learn more about Gemini API quotas"
  url: "https://ai.google.dev/gemini-api/docs/rate-limits"
}
, violations {
  quota_metric: "generativelanguage.googleapis.com/generate_content_free_tier_requests"
  quota_id: "GenerateRequestsPerMinutePerProjectPerModel-FreeTier"
  quota_dimensions {
    key: "model"
    value: "gemini-2.5-flash"
  }
  quota_dimensions {
    key: "location"
    value: "global"
  }
  quota_value: 5
}
, retry_delay {
  seconds: 25
}
]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
// Generation failed for PHP
// Reason: Error: 429 You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/usage?tab=rate-limit. 
* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-2.5-flash
Please retry in 25.922789297s. [links {
  description: "Learn more about Gemini API quotas"
  url: "https://ai.google.dev/gemini-api/docs/rate-limits"
}
, violations {
  quota_metric: "generativelanguage.googleapis.com/generate_content_free_tier_requests"
  quota_id: "GenerateRequestsPerMinutePerProjectPerModel-FreeTier"
  quota_dimensions {
    key: "model"
    value: "gemini-2.5-flash"
  }
  quota_dimensions {
    key: "location"
    value: "global"
  }
  quota_value: 5
}
, retry_delay {
  seconds: 25
}
]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
// Generation failed for Swift
// Reason: Error: 429 You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/usage?tab=rate-limit. 
* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-2.5-flash
Please retry in 25.922789297s. [links {
  description: "Learn more about Gemini API quotas"
  url: "https://ai.google.dev/gemini-api/docs/rate-limits"
}
, violations {
  quota_metric: "generativelanguage.googleapis.com/generate_content_free_tier_requests"
  quota_id: "GenerateRequestsPerMinutePerProjectPerModel-FreeTier"
  quota_dimensions {
    key: "model"
    value: "gemini-2.5-flash"
  }
  quota_dimensions {
    key: "location"
    value: "global"
  }
  quota_value: 5
}
, retry_delay {
  seconds: 25
}
]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
// Generation failed for Kotlin
// Reason: Error: 429 You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/usage?tab=rate-limit. 
* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-2.5-flash
Please retry in 25.922789297s. [links {
  description: "Learn more about Gemini API quotas"
  url: "https://ai.google.dev/gemini-api/docs/rate-limits"
}
, violations {
  quota_metric: "generativelanguage.googleapis.com/generate_content_free_tier_requests"
  quota_id: "GenerateRequestsPerMinutePerProjectPerModel-FreeTier"
  quota_dimensions {
    key: "model"
    value: "gemini-2.5-flash"
  }
  quota_dimensions {
    key: "location"
    value: "global"
  }
  quota_value: 5
}
, retry_delay {
  seconds: 25
}
]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
// Generation failed for Dart
// Reason: Error: 429 You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/usage?tab=rate-limit. 
* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-2.5-flash
Please retry in 25.922789297s. [links {
  description: "Learn more about Gemini API quotas"
  url: "https://ai.google.dev/gemini-api/docs/rate-limits"
}
, violations {
  quota_metric: "generativelanguage.googleapis.com/generate_content_free_tier_requests"
  quota_id: "GenerateRequestsPerMinutePerProjectPerModel-FreeTier"
  quota_dimensions {
    key: "model"
    value: "gemini-2.5-flash"
  }
  quota_dimensions {
    key: "location"
    value: "global"
  }
  quota_value: 5
}
, retry_delay {
  seconds: 25
}
]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
// Generation failed for Go
// Reason: Error: 429 You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/usage?tab=rate-limit. 
* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-2.5-flash
Please retry in 25.922789297s. [links {
  description: "Learn more about Gemini API quotas"
  url: "https://ai.google.dev/gemini-api/docs/rate-limits"
}
, violations {
  quota_metric: "generativelanguage.googleapis.com/generate_content_free_tier_requests"
  quota_id: "GenerateRequestsPerMinutePerProjectPerModel-FreeTier"
  quota_dimensions {
    key: "model"
    value: "gemini-2.5-flash"
  }
  quota_dimensions {
    key: "location"
    value: "global"
  }
  quota_value: 5
}
, retry_delay {
  seconds: 25
}
]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
// Generation failed for Ruby
// Reason: Error: 429 You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/usage?tab=rate-limit. 
* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-2.5-flash
Please retry in 25.922789297s. [links {
  description: "Learn more about Gemini API quotas"
  url: "https://ai.google.dev/gemini-api/docs/rate-limits"
}
, violations {
  quota_metric: "generativelanguage.googleapis.com/generate_content_free_tier_requests"
  quota_id: "GenerateRequestsPerMinutePerProjectPerModel-FreeTier"
  quota_dimensions {
    key: "model"
    value: "gemini-2.5-flash"
  }
  quota_dimensions {
    key: "location"
    value: "global"
  }
  quota_value: 5
}
, retry_delay {
  seconds: 25
}
]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
// Generation failed for Scala
// Reason: Error: 429 You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/usage?tab=rate-limit. 
* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-2.5-flash
Please retry in 25.922789297s. [links {
  description: "Learn more about Gemini API quotas"
  url: "https://ai.google.dev/gemini-api/docs/rate-limits"
}
, violations {
  quota_metric: "generativelanguage.googleapis.com/generate_content_free_tier_requests"
  quota_id: "GenerateRequestsPerMinutePerProjectPerModel-FreeTier"
  quota_dimensions {
    key: "model"
    value: "gemini-2.5-flash"
  }
  quota_dimensions {
    key: "location"
    value: "global"
  }
  quota_value: 5
}
, retry_delay {
  seconds: 25
}
]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
// Generation failed for Rust
// Reason: Error: 429 You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/usage?tab=rate-limit. 
* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-2.5-flash
Please retry in 25.922789297s. [links {
  description: "Learn more about Gemini API quotas"
  url: "https://ai.google.dev/gemini-api/docs/rate-limits"
}
, violations {
  quota_metric: "generativelanguage.googleapis.com/generate_content_free_tier_requests"
  quota_id: "GenerateRequestsPerMinutePerProjectPerModel-FreeTier"
  quota_dimensions {
    key: "model"
    value: "gemini-2.5-flash"
  }
  quota_dimensions {
    key: "location"
    value: "global"
  }
  quota_value: 5
}
, retry_delay {
  seconds: 25
}
]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
// Generation failed for Racket
// Reason: Error: 429 You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/usage?tab=rate-limit. 
* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-2.5-flash
Please retry in 25.922789297s. [links {
  description: "Learn more about Gemini API quotas"
  url: "https://ai.google.dev/gemini-api/docs/rate-limits"
}
, violations {
  quota_metric: "generativelanguage.googleapis.com/generate_content_free_tier_requests"
  quota_id: "GenerateRequestsPerMinutePerProjectPerModel-FreeTier"
  quota_dimensions {
    key: "model"
    value: "gemini-2.5-flash"
  }
  quota_dimensions {
    key: "location"
    value: "global"
  }
  quota_value: 5
}
, retry_delay {
  seconds: 25
}
]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
// Generation failed for Erlang
// Reason: Error: 429 You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/usage?tab=rate-limit. 
* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-2.5-flash
Please retry in 25.922789297s. [links {
  description: "Learn more about Gemini API quotas"
  url: "https://ai.google.dev/gemini-api/docs/rate-limits"
}
, violations {
  quota_metric: "generativelanguage.googleapis.com/generate_content_free_tier_requests"
  quota_id: "GenerateRequestsPerMinutePerProjectPerModel-FreeTier"
  quota_dimensions {
    key: "model"
    value: "gemini-2.5-flash"
  }
  quota_dimensions {
    key: "location"
    value: "global"
  }
  quota_value: 5
}
, retry_delay {
  seconds: 25
}
]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
// Generation failed for Elixir
// Reason: Error: 429 You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/usage?tab=rate-limit. 
* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 5, model: gemini-2.5-flash
Please retry in 25.922789297s. [links {
  description: "Learn more about Gemini API quotas"
  url: "https://ai.google.dev/gemini-api/docs/rate-limits"
}
, violations {
  quota_metric: "generativelanguage.googleapis.com/generate_content_free_tier_requests"
  quota_id: "GenerateRequestsPerMinutePerProjectPerModel-FreeTier"
  quota_dimensions {
    key: "model"
    value: "gemini-2.5-flash"
  }
  quota_dimensions {
    key: "location"
    value: "global"
  }
  quota_value: 5
}
, retry_delay {
  seconds: 25
}
]
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** N/A

- **Space Complexity:** N/A

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-12-10 01:08:39 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved by first checking if the complexity of the first computer is unique and less than all other complexities. If this condition is met, we can fix the first computer as the starting point and arrange the remaining computers in any order, resulting in (n-1)! permutations. However, if there are other computers with the same complexity as the first one, or if the first computer's complexity is not the minimum, we need to return 0 because there are no valid permutations. The key intuition here is that the first computer must have a unique minimum complexity to ensure that it can unlock all other computers.

### Code

<div class="code-tabs" markdown="0">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-cpp-llama-3-3-70b-versatile" checked>
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-java-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-python-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-python3-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-c-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-csharp-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-javascript-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-typescript-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-php-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-swift-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-kotlin-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-dart-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-go-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-ruby-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-scala-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-rust-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-racket-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-erlang-llama-3-3-70b-versatile">
  <input type="radio" name="code-lang-llama-3-3-70b-versatile" id="lang-elixir-llama-3-3-70b-versatile">
  <div class="tab-labels">
    <label for="lang-cpp-llama-3-3-70b-versatile">C++</label>
    <label for="lang-java-llama-3-3-70b-versatile">Java</label>
    <label for="lang-python-llama-3-3-70b-versatile">Python</label>
    <label for="lang-python3-llama-3-3-70b-versatile">Python3</label>
    <label for="lang-c-llama-3-3-70b-versatile">C</label>
    <label for="lang-csharp-llama-3-3-70b-versatile">C#</label>
    <label for="lang-javascript-llama-3-3-70b-versatile">JavaScript</label>
    <label for="lang-typescript-llama-3-3-70b-versatile">TypeScript</label>
    <label for="lang-php-llama-3-3-70b-versatile">PHP</label>
    <label for="lang-swift-llama-3-3-70b-versatile">Swift</label>
    <label for="lang-kotlin-llama-3-3-70b-versatile">Kotlin</label>
    <label for="lang-dart-llama-3-3-70b-versatile">Dart</label>
    <label for="lang-go-llama-3-3-70b-versatile">Go</label>
    <label for="lang-ruby-llama-3-3-70b-versatile">Ruby</label>
    <label for="lang-scala-llama-3-3-70b-versatile">Scala</label>
    <label for="lang-rust-llama-3-3-70b-versatile">Rust</label>
    <label for="lang-racket-llama-3-3-70b-versatile">Racket</label>
    <label for="lang-erlang-llama-3-3-70b-versatile">Erlang</label>
    <label for="lang-elixir-llama-3-3-70b-versatile">Elixir</label>
  </div>

  <div class="tab-panel" data-lang="cpp">

{% highlight cpp %}
{% raw %}
class Solution {
public:
    int countPermutations(vector<int>& complexity) {
        int n = complexity.size();
        int MOD = 1e9 + 7;
        if (complexity[0] != *min_element(complexity.begin(), complexity.end())) return 0;
        long long res = 1;
        for (int i = 1; i < n; i++) {
            res = (res * i) % MOD;
        }
        return res;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int countPermutations(int[] complexity) {
        int n = complexity.length;
        int MOD = (int)1e9 + 7;
        if (complexity[0] != Arrays.stream(complexity).min().getAsInt()) return 0;
        long res = 1;
        for (int i = 1; i < n; i++) {
            res = (res * i) % MOD;
        }
        return (int)res;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def countPermutations(self, complexity: list[int]) -> int:
        n = len(complexity)
        MOD = 10**9 + 7
        if complexity[0] != min(complexity): return 0
        res = 1
        for i in range(1, n):
            res = (res * i) % MOD
        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def countPermutations(self, complexity: list[int]) -> int:
        n = len(complexity)
        MOD = 10**9 + 7
        if complexity[0] != min(complexity): return 0
        res = 1
        for i in range(1, n):
            res = (res * i) % MOD
        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int countPermutations(int* complexity, int complexitySize) {
    int MOD = 1000000007;
    int res = 1;
    if (complexity[0] != *min_element(complexity, complexity + complexitySize)) return 0;
    for (int i = 1; i < complexitySize; i++) {
        res = (res * i) % MOD;
    }
    return res;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int CountPermutations(int[] complexity) {
        int n = complexity.Length;
        int MOD = 1000000007;
        if (complexity[0] != complexity.Min()) return 0;
        long res = 1;
        for (int i = 1; i < n; i++) {
            res = (res * i) % MOD;
        }
        return (int)res;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var countPermutations = function(complexity) {
    let n = complexity.length;
    let MOD = 1000000007;
    if (complexity[0] != Math.min(...complexity)) return 0;
    let res = 1;
    for (let i = 1; i < n; i++) {
        res = (res * i) % MOD;
    }
    return res;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function countPermutations(complexity: number[]): number {
    let n = complexity.length;
    let MOD = 1000000007;
    if (complexity[0] != Math.min(...complexity)) return 0;
    let res = 1;
    for (let i = 1; i < n; i++) {
        res = (res * i) % MOD;
    }
    return res;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
$MOD = 1000000007;
function countPermutations($complexity) {
    $n = count($complexity);
    if ($complexity[0] != min($complexity)) return 0;
    $res = 1;
    for ($i = 1; $i < $n; $i++) {
        $res = ($res * $i) % $GLOBALS['MOD'];
    }
    return $res;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func countPermutations(_ complexity: [Int]) -> Int {
        let n = complexity.count
        let MOD = 1000000007
        if complexity[0] != complexity.min()! return 0
        var res = 1
        for i in 1..<n {
            res = (res * i) % MOD
        }
        return res
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun countPermutations(complexity: IntArray): Int {
        val n = complexity.size
        val MOD = 1000000007
        if (complexity[0] != complexity.minOrNull()!!) return 0
        var res = 1
        for (i in 1 until n) {
            res = (res * i) % MOD
        }
        return res
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
    int countPermutations(List<int> complexity) {
        int n = complexity.length;
        int MOD = 1000000007;
        if (complexity[0] != complexity.reduce((a, b) => a < b ? a : b)) return 0;
        int res = 1;
        for (int i = 1; i < n; i++) {
            res = (res * i) % MOD;
        }
        return res;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func countPermutations(complexity []int) int {
    n := len(complexity)
    MOD := 1000000007
    if complexity[0] != min(complexity) { return 0 }
    res := 1
    for i := 1; i < n; i++ {
        res = (res * i) % MOD
    }
    return res
}
func min(arr []int) int {
    min := arr[0]
    for _, v := range arr {
        if v < min { min = v }
    }
    return min
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def count_permutations(complexity)
    n = complexity.size
    MOD = 1000000007
    if complexity[0] != complexity.min return 0 end
    res = 1
    (1...n).each do |i|
        res = (res * i) % MOD
    end
    res
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def countPermutations(complexity: Array[Int]): Int = {
        val n = complexity.length
        val MOD = 1000000007
        if (complexity(0) != complexity.min) return 0
        var res = 1
        for (i <- 1 until n) {
            res = (res * i) % MOD
        }
        res
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn count_permutations(complexity: Vec<i32>) -> i32 {
        let n = complexity.len();
        let MOD = 1000000007;
        if complexity[0] != *complexity.iter().min().unwrap() { return 0; }
        let mut res = 1;
        for i in 1..n {
            res = (res * i as i32) % MOD;
        }
        res
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define (count-permutations complexity)
    (let ((n (length complexity))
          (MOD 1000000007))
        (if (not (= (car complexity) (apply min complexity)))
            0
            (let loop ((i 1) (res 1))
                (if (= i n)
                    res
                    (loop (+ i 1) (modulo (* res i) MOD)))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([count_permutations/1]).

count_permutations(Complexity) ->
N = length(Complexity),
MOD = 1000000007,
case lists:min(Complexity) of
[H | _] when H =:= lists:nth(1, Complexity) ->
count_permutations(Complexity, 1, 1, MOD, N);
_ -> 0
end.

count_permutations(_Complexity, I, Res, MOD, N) when I =:= N -> Res;
count_permutations(Complexity, I, Res, MOD, N) ->
count_permutations(Complexity, I + 1, (Res * I) rem MOD, MOD, N).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
    def count_permutations(complexity) do
        n = length(complexity)
        mod = 1_000_000_007
        if Enum.min(complexity) != Enum.at(complexity, 0) do
            0
        else
            count_permutations(complexity, 1, 1, mod, n)
        end
    end
    defp count_permutations(_complexity, i, res, mod, n) when i == n do
        res
    end
    defp count_permutations(complexity, i, res, mod, n) do
        count_permutations(complexity, i + 1, rem(res * i, mod), mod, n)
    end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of this solution is O(n) because we need to iterate through the complexity array to check if the first computer's complexity is unique and less than all other complexities. Additionally, we need to calculate the factorial of (n-1), which can be done in O(n) time using a loop or a recursive function.

- **Space Complexity:** The space complexity of this solution is O(1) because we only need a constant amount of space to store the complexity array and the result. We do not need any additional data structures that scale with the input size.

</div>
</details>
