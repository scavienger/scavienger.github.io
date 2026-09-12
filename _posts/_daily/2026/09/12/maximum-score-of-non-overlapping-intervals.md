---
layout: post
title: "Maximum Score of Non-overlapping Intervals"
date: 2026-09-12 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Binary Search", "Dynamic Programming", "Sorting"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/
ai_solutions:
  - solutions:
      cpp: "class Solution {\n    struct State {\n        long long score;\n       \
        \ int cnt;\n        int idx[4];\n\n        State() : score(-1), cnt(0) {}\n\n\
        \        bool isBetterThan(const State& other) const {\n            if (score\
        \ != other.score) return score > other.score;\n            if (cnt == 0) return\
        \ false;\n            if (other.cnt == 0) return true;\n            int len\
        \ = std::min(cnt, other.cnt);\n            for (int i = 0; i < len; ++i) {\n\
        \                if (idx[i] != other.idx[i]) return idx[i] < other.idx[i];\n\
        \            }\n            return cnt < other.cnt;\n        }\n\n        void\
        \ set(long long s, int c, const int* existing, int extra) {\n            score\
        \ = s;\n            cnt = c;\n            if (existing) {\n                for\
        \ (int i = 0; i < c - 1; ++i) idx[i] = existing[i];\n            }\n       \
        \     idx[c - 1] = extra;\n            std::sort(idx, idx + cnt);\n        }\n\
        \    };\n\n    struct Interval {\n        int l, r, weight, id;\n    };\n\n\
        public:\n    vector<int> maximumWeight(vector<vector<int>>& intervals) {\n \
        \       int n = intervals.size();\n        vector<Interval> ivs(n);\n      \
        \  for (int i = 0; i < n; ++i) {\n            ivs[i] = {intervals[i][0], intervals[i][1],\
        \ intervals[i][2], i};\n        }\n        std::sort(ivs.begin(), ivs.end(),\
        \ [](const Interval& a, const Interval& b) {\n            return a.r < b.r;\n\
        \        });\n\n        vector<State> prev_dp(n);\n        vector<State> curr_dp(n);\n\
        \        State ans;\n\n        for (int k = 1; k <= 4; ++k) {\n            for\
        \ (int i = 0; i < n; ++i) {\n                if (i > 0) curr_dp[i] = curr_dp[i\
        \ - 1];\n                else curr_dp[i] = State();\n\n                int j\
        \ = -1, low = 0, high = i - 1;\n                while (low <= high) {\n    \
        \                int mid = low + (high - low) / 2;\n                    if (ivs[mid].r\
        \ < ivs[i].l) { j = mid; low = mid + 1; } \n                    else high =\
        \ mid - 1;\n                }\n\n                State cand;\n             \
        \   if (k == 1) {\n                    cand.set(ivs[i].weight, 1, nullptr, ivs[i].id);\n\
        \                } else if (j != -1 && prev_dp[j].score != -1) {\n         \
        \           cand.set(prev_dp[j].score + ivs[i].weight, k, prev_dp[j].idx, ivs[i].id);\n\
        \                }\n\n                if (cand.isBetterThan(curr_dp[i])) curr_dp[i]\
        \ = cand;\n            }\n            if (curr_dp[n - 1].isBetterThan(ans))\
        \ ans = curr_dp[n - 1];\n            prev_dp = curr_dp;\n        }\n\n     \
        \   vector<int> res;\n        for (int i = 0; i < ans.cnt; ++i) res.push_back(ans.idx[i]);\n\
        \        return res;\n    }\n};"
      java: "import java.util.*;\n\nclass Solution {\n    static class Interval {\n\
        \        int l, r, w, id;\n        Interval(int l, int r, int w, int id) {\n\
        \            this.l = l; this.r = r; this.w = w; this.id = id;\n        }\n\
        \    }\n\n    static class State {\n        long score;\n        int[] idx;\n\
        \        State(long score, int[] idx) { this.score = score; this.idx = idx;\
        \ }\n    }\n\n    private boolean isBetter(long s1, int[] i1, long s2, int[]\
        \ i2) {\n        if (s1 != s2) return s1 > s2;\n        if (i1 == null) return\
        \ false;\n        if (i2 == null) return true;\n        int len = Math.min(i1.length,\
        \ i2.length);\n        for (int i = 0; i < len; i++) {\n            if (i1[i]\
        \ != i2[i]) return i1[i] < i2[i];\n        }\n        return i1.length < i2.length;\n\
        \    }\n\n    public int[] maximumWeight(List<List<Integer>> intervals) {\n\
        \        int n = intervals.size();\n        Interval[] ivs = new Interval[n];\n\
        \        for (int i = 0; i < n; i++) {\n            ivs[i] = new Interval(intervals.get(i).get(0),\
        \ intervals.get(i).get(1), intervals.get(i).get(2), i);\n        }\n       \
        \ Arrays.sort(ivs, (a, b) -> Integer.compare(a.r, b.r));\n\n        State[]\
        \ prevDp = new State[n];\n        State ans = new State(-1, null);\n\n     \
        \   for (int k = 1; k <= 4; k++) {\n            State[] currDp = new State[n];\n\
        \            for (int i = 0; i < n; i++) {\n                long resScore =\
        \ -1;\n                int[] resIdx = null;\n                if (i > 0) {\n\
        \                    resScore = currDp[i - 1].score;\n                    resIdx\
        \ = currDp[i - 1].idx;\n                }\n\n                int j = -1, low\
        \ = 0, high = i - 1;\n                while (low <= high) {\n              \
        \      int mid = low + (high - low) / 2;\n                    if (ivs[mid].r\
        \ < ivs[i].l) { j = mid; low = mid + 1; }\n                    else high = mid\
        \ - 1;\n                }\n\n                long candScore = -1;\n        \
        \        int[] candIdx = null;\n                if (k == 1) {\n            \
        \        candScore = ivs[i].w;\n                    candIdx = new int[]{ivs[i].id};\n\
        \                } else if (j != -1 && prevDp[j].score != -1) {\n          \
        \          candScore = prevDp[j].score + ivs[i].w;\n                    candIdx\
        \ = new int[k];\n                    System.arraycopy(prevDp[j].idx, 0, candIdx,\
        \ 0, k - 1);\n                    candIdx[k - 1] = ivs[i].id;\n            \
        \        Arrays.sort(candIdx);\n                }\n\n                if (isBetter(candScore,\
        \ candIdx, resScore, resIdx)) {\n                    currDp[i] = new State(candScore,\
        \ candIdx);\n                } else {\n                    currDp[i] = new State(resScore,\
        \ resIdx);\n                }\n            }\n            if (isBetter(currDp[n\
        \ - 1].score, currDp[n - 1].idx, ans.score, ans.idx)) ans = currDp[n - 1];\n\
        \            prevDp = currDp;\n        }\n        return ans.idx;\n    }\n}"
      python: "import bisect\n\nclass Solution(object):\n    def maximumWeight(self,\
        \ intervals):\n        n = len(intervals)\n        ivs = []\n        for i in\
        \ range(n):\n            ivs.append(intervals[i] + [i])\n        ivs.sort(key=lambda\
        \ x: x[1])\n\n        ends = [x[1] for x in ivs]\n        prev_dp = [(-1, [])\
        \ for _ in range(n)]\n\n        ans_score = -1\n        ans_indices = []\n\n\
        \        for k in range(1, 5):\n            curr_dp = [None] * n\n         \
        \   for i in range(n):\n                res_score, res_indices = (-1, [])\n\
        \                if i > 0:\n                    res_score, res_indices = curr_dp[i-1]\n\
        \n                j = bisect.bisect_left(ends, ivs[i][0]) - 1\n\n          \
        \      cand_score = -1\n                cand_indices = []\n                if\
        \ k == 1:\n                    cand_score = ivs[i][2]\n                    cand_indices\
        \ = [ivs[i][3]]\n                else:\n                    if j >= 0 and prev_dp[j][0]\
        \ != -1:\n                        cand_score = prev_dp[j][0] + ivs[i][2]\n \
        \                       cand_indices = sorted(prev_dp[j][1] + [ivs[i][3]])\n\
        \n                if cand_score > res_score:\n                    res_score,\
        \ res_indices = cand_score, cand_indices\n                elif cand_score ==\
        \ res_score and cand_score != -1:\n                    if not res_indices or\
        \ cand_indices < res_indices:\n                        res_indices = cand_indices\n\
        \n                curr_dp[i] = (res_score, res_indices)\n\n            best_k_score,\
        \ best_k_indices = curr_dp[n-1]\n            if best_k_score > ans_score:\n\
        \                ans_score, ans_indices = best_k_score, best_k_indices\n   \
        \         elif best_k_score == ans_score and best_k_score != -1:\n         \
        \       if not ans_indices or best_k_indices < ans_indices:\n              \
        \      ans_indices = best_k_indices\n            prev_dp = curr_dp\n\n     \
        \   return ans_indices"
      python3: "import bisect\n\nclass Solution:\n    def maximumWeight(self, intervals:\
        \ list[list[int]]) -> list[int]:\n        n = len(intervals)\n        ivs =\
        \ []\n        for i in range(n):\n            ivs.append((intervals[i][0], intervals[i][1],\
        \ intervals[i][2], i))\n\n        ivs.sort(key=lambda x: x[1])\n        r_values\
        \ = [x[1] for x in ivs]\n\n        dp = [[(0, []) for _ in range(n + 1)]]\n\
        \        for k in range(1, 5):\n            dp.append([(-1, []) for _ in range(n\
        \ + 1)])\n\n        def is_better(s1, idx1, s2, idx2):\n            if s1 >\
        \ s2: return True\n            if s1 < s2: return False\n            if not\
        \ idx1: return False\n            if not idx2: return True\n            n1,\
        \ n2 = len(idx1), len(idx2)\n            for i in range(min(n1, n2)):\n    \
        \            if idx1[i] < idx2[i]: return True\n                if idx1[i] >\
        \ idx2[i]: return False\n            return n1 < n2\n\n        for k in range(1,\
        \ 5):\n            for i in range(1, n + 1):\n                dp[k][i] = dp[k][i-1]\n\
        \n                l, r, w, idx = ivs[i-1]\n                prev_idx = bisect.bisect_left(r_values,\
        \ l)\n\n                if dp[k-1][prev_idx][0] != -1:\n                   \
        \ new_score = dp[k-1][prev_idx][0] + w\n                    new_indices = sorted(dp[k-1][prev_idx][1]\
        \ + [idx])\n                    if is_better(new_score, new_indices, dp[k][i][0],\
        \ dp[k][i][1]):\n                        dp[k][i] = (new_score, new_indices)\n\
        \n        best_score, best_indices = -1, []\n        for k in range(1, 5):\n\
        \            if is_better(dp[k][n][0], dp[k][n][1], best_score, best_indices):\n\
        \                best_score, best_indices = dp[k][n]\n\n        return best_indices"
      c: "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <stdbool.h>\n\
        \ntypedef struct {\n    int l, r, w, id;\n} Interval;\n\ntypedef struct {\n\
        \    long long score;\n    int indices[4];\n    int count;\n} Result;\n\nint\
        \ compareIntervals(const void* a, const void* b) {\n    Interval* i1 = (Interval*)a;\n\
        \    Interval* i2 = (Interval*)b;\n    if (i1->r != i2->r) return i1->r - i2->r;\n\
        \    return i1->l - i2->l;\n}\n\nbool is_better(Result* a, Result* b) {\n  \
        \  if (a->score > b->score) return true;\n    if (a->score < b->score) return\
        \ false;\n    if (a->count == 0) return false;\n    if (b->count == 0) return\
        \ true;\n    int min_c = a->count < b->count ? a->count : b->count;\n    for\
        \ (int i = 0; i < min_c; i++) {\n        if (a->indices[i] < b->indices[i])\
        \ return true;\n        if (a->indices[i] > b->indices[i]) return false;\n \
        \   }\n    return a->count < b->count;\n}\n\nvoid combine(Result* dest, Result*\
        \ src, long long new_score, int new_idx) {\n    dest->score = new_score;\n \
        \   int i = 0, j = 0;\n    bool added = false;\n    while (j < src->count) {\n\
        \        if (!added && new_idx < src->indices[j]) {\n            dest->indices[i++]\
        \ = new_idx;\n            added = true;\n        }\n        dest->indices[i++]\
        \ = src->indices[j++];\n    }\n    if (!added) dest->indices[i++] = new_idx;\n\
        \    dest->count = src->count + 1;\n}\n\nint* maximumWeight(int** intervals,\
        \ int intervalsSize, int* intervalsColSize, int* returnSize) {\n    Interval*\
        \ ivs = (Interval*)malloc(intervalsSize * sizeof(Interval));\n    for (int i\
        \ = 0; i < intervalsSize; i++) {\n        ivs[i].l = intervals[i][0];\n    \
        \    ivs[i].r = intervals[i][1];\n        ivs[i].w = intervals[i][2];\n    \
        \    ivs[i].id = i;\n    }\n    qsort(ivs, intervalsSize, sizeof(Interval),\
        \ compareIntervals);\n\n    Result* dp = (Result*)malloc(5 * (intervalsSize\
        \ + 1) * sizeof(Result));\n    for (int k = 0; k < 5; k++) {\n        for (int\
        \ i = 0; i <= intervalsSize; i++) {\n            dp[k * (intervalsSize + 1)\
        \ + i].score = -1;\n            dp[k * (intervalsSize + 1) + i].count = 0;\n\
        \        }\n    }\n    for (int i = 0; i <= intervalsSize; i++) dp[i].score\
        \ = 0;\n\n    for (int k = 1; k <= 4; k++) {\n        for (int i = 1; i <= intervalsSize;\
        \ i++) {\n            dp[k * (intervalsSize + 1) + i] = dp[k * (intervalsSize\
        \ + 1) + i - 1];\n\n            int target_l = ivs[i-1].l;\n            int\
        \ low = 0, high = i - 2, prev_idx = -1;\n            while (low <= high) {\n\
        \                int mid = low + (high - low) / 2;\n                if (ivs[mid].r\
        \ < target_l) {\n                    prev_idx = mid;\n                    low\
        \ = mid + 1;\n                } else {\n                    high = mid - 1;\n\
        \                }\n            }\n            int idx = prev_idx + 1;\n   \
        \         if (dp[(k-1) * (intervalsSize + 1) + idx].score != -1) {\n       \
        \         Result temp;\n                combine(&temp, &dp[(k-1) * (intervalsSize\
        \ + 1) + idx], dp[(k-1) * (intervalsSize + 1) + idx].score + ivs[i-1].w, ivs[i-1].id);\n\
        \                if (is_better(&temp, &dp[k * (intervalsSize + 1) + i])) {\n\
        \                    dp[k * (intervalsSize + 1) + i] = temp;\n             \
        \   }\n            }\n        }\n    }\n\n    Result best = { -1, {0, 0, 0,\
        \ 0}, 0 };\n    for (int k = 1; k <= 4; k++) {\n        if (is_better(&dp[k\
        \ * (intervalsSize + 1) + intervalsSize], &best)) {\n            best = dp[k\
        \ * (intervalsSize + 1) + intervalsSize];\n        }\n    }\n\n    *returnSize\
        \ = best.count;\n    int* res = (int*)malloc(best.count * sizeof(int));\n  \
        \  for (int i = 0; i < best.count; i++) res[i] = best.indices[i];\n\n    free(ivs);\n\
        \    free(dp);\n    return res;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\nusing System.Linq;\n\
        \npublic class Solution {\n    struct Interval {\n        public int l, r, w,\
        \ id;\n    }\n\n    struct Result {\n        public long score;\n        public\
        \ int[] indices;\n        public int count;\n\n        public Result(long s,\
        \ int[] i, int c) {\n            score = s;\n            indices = i;\n    \
        \        count = c;\n        }\n    }\n\n    private bool IsBetter(long s1,\
        \ int c1, int[] i1, long s2, int c2, int[] i2) {\n        if (s1 > s2) return\
        \ true;\n        if (s1 < s2) return false;\n        if (c1 == 0) return false;\n\
        \        if (c2 == 0) return true;\n        int minC = Math.Min(c1, c2);\n \
        \       for (int i = 0; i < minC; i++) {\n            if (i1[i] < i2[i]) return\
        \ true;\n            if (i1[i] > i2[i]) return false;\n        }\n        return\
        \ c1 < c2;\n    }\n\n    public int[] MaximumWeight(IList<IList<int>> intervals)\
        \ {\n        int n = intervals.Count;\n        Interval[] ivs = new Interval[n];\n\
        \        for (int i = 0; i < n; i++) {\n            ivs[i] = new Interval {\
        \ l = intervals[i][0], r = intervals[i][1], w = intervals[i][2], id = i };\n\
        \        }\n        Array.Sort(ivs, (a, b) => a.r.CompareTo(b.r));\n\n     \
        \   int[] rValues = ivs.Select(x => x.r).ToArray();\n        Result[,] dp =\
        \ new Result[5, n + 1];\n\n        for (int k = 0; k < 5; k++) {\n         \
        \   for (int i = 0; i <= n; i++) {\n                dp[k, i] = new Result(-1,\
        \ new int[0], 0);\n            }\n        }\n        for (int i = 0; i <= n;\
        \ i++) dp[0, i] = new Result(0, new int[0], 0);\n\n        for (int k = 1; k\
        \ <= 4; k++) {\n            for (int i = 1; i <= n; i++) {\n               \
        \ dp[k, i] = dp[k, i - 1];\n\n                int targetL = ivs[i - 1].l;\n\
        \                int idx = Array.BinarySearch(rValues, 0, i - 1, targetL);\n\
        \                if (idx < 0) idx = ~idx;\n                else {\n        \
        \            while (idx > 0 && rValues[idx - 1] == targetL) idx--;\n       \
        \         }\n                // Array.BinarySearch idx is where targetL would\
        \ be. We need r < targetL.\n                // The number of elements with r\
        \ < targetL is the count 'idx'.\n\n                if (dp[k - 1, idx].score\
        \ != -1) {\n                    long newScore = dp[k - 1, idx].score + ivs[i\
        \ - 1].w;\n                    int[] newIndices = new int[k];\n            \
        \        int p = 0;\n                    bool added = false;\n             \
        \       for (int j = 0; j < dp[k - 1, idx].count; j++) {\n                 \
        \       if (!added && ivs[i - 1].id < dp[k - 1, idx].indices[j]) {\n       \
        \                     newIndices[p++] = ivs[i - 1].id;\n                   \
        \         added = true;\n                        }\n                       \
        \ newIndices[p++] = dp[k - 1, idx].indices[j];\n                    }\n    \
        \                if (!added) newIndices[p++] = ivs[i - 1].id;\n\n          \
        \          if (IsBetter(newScore, k, newIndices, dp[k, i].score, dp[k, i].count,\
        \ dp[k, i].indices)) {\n                        dp[k, i] = new Result(newScore,\
        \ newIndices, k);\n                    }\n                }\n            }\n\
        \        }\n\n        Result best = new Result(-1, new int[0], 0);\n       \
        \ for (int k = 1; k <= 4; k++) {\n            if (IsBetter(dp[k, n].score, dp[k,\
        \ n].count, dp[k, n].indices, best.score, best.count, best.indices)) {\n   \
        \             best = dp[k, n];\n            }\n        }\n\n        return best.indices;\n\
        \    }\n}"
      javascript: "/**\n * @param {number[][]} intervals\n * @return {number[]}\n */\n\
        var maximumWeight = function(intervals) {\n    const n = intervals.length;\n\
        \    const ivs = intervals.map((v, i) => [v[0], v[1], v[2], i]);\n    ivs.sort((a,\
        \ b) => a[1] - b[1]);\n\n    const rValues = ivs.map(x => x[1]);\n    const\
        \ scores = new Float64Array(5 * (n + 1)).fill(-1);\n    const counts = new Int8Array(5\
        \ * (n + 1)).fill(0);\n    const indices = new Int32Array(5 * (n + 1) * 4).fill(0);\n\
        \n    for (let i = 0; i <= n; i++) {\n        scores[i] = 0;\n    }\n\n    function\
        \ isBetter(s1, c1, idx1, s2, c2, idx2) {\n        if (s1 > s2) return true;\n\
        \        if (s1 < s2) return false;\n        if (c1 === 0) return false;\n \
        \       if (c2 === 0) return true;\n        const minC = Math.min(c1, c2);\n\
        \        for (let i = 0; i < minC; i++) {\n            if (idx1[i] < idx2[i])\
        \ return true;\n            if (idx1[i] > idx2[i]) return false;\n        }\n\
        \        return c1 < c2;\n    }\n\n    for (let k = 1; k <= 4; k++) {\n    \
        \    for (let i = 1; i <= n; i++) {\n            const curr = k * (n + 1) +\
        \ i;\n            const prevInRow = k * (n + 1) + i - 1;\n\n            // Copy\
        \ prev in row\n            scores[curr] = scores[prevInRow];\n            counts[curr]\
        \ = counts[prevInRow];\n            let target = curr * 4;\n            let\
        \ source = prevInRow * 4;\n            for (let j = 0; j < counts[prevInRow];\
        \ j++) indices[target + j] = indices[source + j];\n\n            let low = 0,\
        \ high = i - 2, prevIdx = -1;\n            const targetL = ivs[i - 1][0];\n\
        \            while (low <= high) {\n                let mid = (low + high) >>\
        \ 1;\n                if (rValues[mid] < targetL) {\n                    prevIdx\
        \ = mid;\n                    low = mid + 1;\n                } else {\n   \
        \                 high = mid - 1;\n                }\n            }\n\n    \
        \        const prevCol = (k - 1) * (n + 1) + (prevIdx + 1);\n            if\
        \ (scores[prevCol] !== -1) {\n                const newScore = scores[prevCol]\
        \ + ivs[i - 1][2];\n                const newCount = counts[prevCol] + 1;\n\
        \                const tempIdx = new Int32Array(4);\n                let p =\
        \ 0, added = false;\n                const prevIdxs = indices.subarray(prevCol\
        \ * 4, prevCol * 4 + counts[prevCol]);\n                for (let j = 0; j <\
        \ counts[prevCol]; j++) {\n                    if (!added && ivs[i - 1][3] <\
        \ prevIdxs[j]) {\n                        tempIdx[p++] = ivs[i - 1][3];\n  \
        \                      added = true;\n                    }\n              \
        \      tempIdx[p++] = prevIdxs[j];\n                }\n                if (!added)\
        \ tempIdx[p++] = ivs[i - 1][3];\n\n                if (isBetter(newScore, newCount,\
        \ tempIdx, scores[curr], counts[curr], indices.subarray(curr * 4, curr * 4 +\
        \ counts[curr]))) {\n                    scores[curr] = newScore;\n        \
        \            counts[curr] = newCount;\n                    for (let j = 0; j\
        \ < newCount; j++) indices[curr * 4 + j] = tempIdx[j];\n                }\n\
        \            }\n        }\n    }\n\n    let bestScore = -1, bestK = -1;\n  \
        \  for (let k = 1; k <= 4; k++) {\n        const idx = k * (n + 1) + n;\n  \
        \      if (isBetter(scores[idx], counts[idx], indices.subarray(idx * 4, idx\
        \ * 4 + counts[idx]), bestScore, bestK === -1 ? 0 : counts[bestK * (n + 1) +\
        \ n], bestK === -1 ? [] : indices.subarray((bestK * (n + 1) + n) * 4))) {\n\
        \            bestScore = scores[idx];\n            bestK = k;\n        }\n \
        \   }\n\n    const finalIdx = bestK * (n + 1) + n;\n    return Array.from(indices.subarray(finalIdx\
        \ * 4, finalIdx * 4 + counts[finalIdx]));\n};"
      typescript: "class State {\n  weight: number;\n  indices: number[];\n  constructor(weight:\
        \ number, indices: number[]) {\n    this.weight = weight;\n    this.indices\
        \ = indices;\n  }\n}\n\nfunction maximumWeight(intervals: number[][]): number[]\
        \ {\n  const n = intervals.length;\n  const sortedIntervals = intervals.map((val,\
        \ idx) => ({\n    l: val[0],\n    r: val[1],\n    w: val[2],\n    id: idx\n\
        \  })).sort((a, b) => a.r - b.r);\n\n  function findLastEndingBefore(targetL:\
        \ number): number {\n    let low = 0;\n    let high = n - 1;\n    let ans =\
        \ -1;\n    while (low <= high) {\n      const mid = (low + high) >>> 1;\n  \
        \    if (sortedIntervals[mid].r < targetL) {\n        ans = mid;\n        low\
        \ = mid + 1;\n      } else {\n        high = mid - 1;\n      }\n    }\n    return\
        \ ans;\n  }\n\n  function isBetter(w1: number, idx1: number[], w2: number, idx2:\
        \ number[]): boolean {\n    if (w1 !== w2) return w1 > w2;\n    const len1 =\
        \ idx1.length;\n    const len2 = idx2.length;\n    const minLen = Math.min(len1,\
        \ len2);\n    for (let i = 0; i < minLen; i++) {\n      if (idx1[i] !== idx2[i])\
        \ return idx1[i] < idx2[i];\n    }\n    return len1 < len2;\n  }\n\n  const\
        \ dp: (State | null)[][] = Array.from({ length: 5 }, () => Array(n + 1).fill(null));\n\
        \  for (let i = 0; i <= n; i++) {\n    dp[0][i] = new State(0, []);\n  }\n\n\
        \  for (let k = 1; k <= 4; k++) {\n    for (let i = 1; i <= n; i++) {\n    \
        \  dp[k][i] = dp[k][i - 1];\n      const j = findLastEndingBefore(sortedIntervals[i\
        \ - 1].l);\n      const prev = dp[k - 1][j + 1];\n      if (prev !== null) {\n\
        \        const currentWeight = prev.weight + sortedIntervals[i - 1].w;\n   \
        \     const currentIndices = [...prev.indices, sortedIntervals[i - 1].id].sort((a,\
        \ b) => a - b);\n        if (dp[k][i] === null || isBetter(currentWeight, currentIndices,\
        \ dp[k][i]!.weight, dp[k][i]!.indices)) {\n          dp[k][i] = new State(currentWeight,\
        \ currentIndices);\n        }\n      }\n    }\n  }\n\n  let bestState: State\
        \ = new State(0, []);\n  for (let k = 1; k <= 4; k++) {\n    if (dp[k][n] !==\
        \ null && isBetter(dp[k][n]!.weight, dp[k][n]!.indices, bestState.weight, bestState.indices))\
        \ {\n      bestState = dp[k][n]!;\n    }\n  }\n\n  return bestState.indices;\n\
        }"
      php: "class State {\n    public $weight;\n    public $indices;\n    public function\
        \ __construct($w, $idx) {\n        $this->weight = $w;\n        $this->indices\
        \ = $idx;\n    }\n}\n\nclass Solution {\n    /**\n     * @param Integer[][]\
        \ $intervals\n     * @return Integer[]\n     */\n    function maximumWeight($intervals)\
        \ {\n        $n = count($intervals);\n        $mappedIntervals = [];\n     \
        \   for ($i = 0; $i < $n; $i++) {\n            $mappedIntervals[] = [\n    \
        \            'l' => $intervals[$i][0],\n                'r' => $intervals[$i][1],\n\
        \                'w' => $intervals[$i][2],\n                'id' => $i\n   \
        \         ];\n        }\n        usort($mappedIntervals, function($a, $b) {\n\
        \            return $a['r'] <=> $b['r'];\n        });\n\n        $dp = array_fill(0,\
        \ 5, array_fill(0, $n + 1, null));\n        for ($i = 0; $i <= $n; $i++) {\n\
        \            $dp[0][$i] = new State(0, []);\n        }\n\n        for ($k =\
        \ 1; $k <= 4; $k++) {\n            for ($i = 1; $i <= $n; $i++) {\n        \
        \        $dp[$k][$i] = $dp[$k][$i - 1];\n\n                $targetL = $mappedIntervals[$i\
        \ - 1]['l'];\n                $low = 0;\n                $high = $n - 1;\n \
        \               $idx = -1;\n                while ($low <= $high) {\n      \
        \              $mid = ($low + $high) >> 1;\n                    if ($mappedIntervals[$mid]['r']\
        \ < $targetL) {\n                        $idx = $mid;\n                    \
        \    $low = $mid + 1;\n                    } else {\n                      \
        \  $high = $mid - 1;\n                    }\n                }\n\n         \
        \       $prev = $dp[$k - 1][$idx + 1];\n                if ($prev !== null)\
        \ {\n                    $currentWeight = $prev->weight + $mappedIntervals[$i\
        \ - 1]['w'];\n                    $currentIndices = $prev->indices;\n      \
        \              $currentIndices[] = $mappedIntervals[$i - 1]['id'];\n       \
        \             sort($currentIndices, SORT_NUMERIC);\n\n                    if\
        \ ($dp[$k][$i] === null || \n                        $currentWeight > $dp[$k][$i]->weight\
        \ || \n                        ($currentWeight === $dp[$k][$i]->weight && $currentIndices\
        \ < $dp[$k][$i]->indices)) {\n                        $dp[$k][$i] = new State($currentWeight,\
        \ $currentIndices);\n                    }\n                }\n            }\n\
        \        }\n\n        $bestState = new State(0, []);\n        for ($k = 1; $k\
        \ <= 4; $k++) {\n            if ($dp[$k][$n] !== null) {\n                if\
        \ ($dp[$k][$n]->weight > $bestState->weight || \n                   ($dp[$k][$n]->weight\
        \ === $bestState->weight && (empty($bestState->indices) || $dp[$k][$n]->indices\
        \ < $bestState->indices))) {\n                    $bestState = $dp[$k][$n];\n\
        \                }\n            }\n        }\n\n        return $bestState->indices;\n\
        \    }\n}"
      swift: "class Solution {\n    struct State {\n        let weight: Int\n      \
        \  let indices: [Int]\n    }\n\n    struct Interval {\n        let l: Int\n\
        \        let r: Int\n        let w: Int\n        let id: Int\n    }\n\n    func\
        \ maximumWeight(_ intervals: [[Int]]) -> [Int] {\n        let n = intervals.count\n\
        \        var sortedIntervals: [Interval] = []\n        for i in 0..<n {\n  \
        \          sortedIntervals.append(Interval(l: intervals[i][0], r: intervals[i][1],\
        \ w: intervals[i][2], id: i))\n        }\n        sortedIntervals.sort { $0.r\
        \ < $1.r }\n\n        var dp: [[State?]] = Array(repeating: Array(repeating:\
        \ nil, count: n + 1), count: 5)\n        for i in 0...n {\n            dp[0][i]\
        \ = State(weight: 0, indices: [])\n        }\n\n        for k in 1...4 {\n \
        \           for i in 1...n {\n                dp[k][i] = dp[k][i - 1]\n\n  \
        \              let targetL = sortedIntervals[i - 1].l\n                var low\
        \ = 0\n                var high = i - 2\n                var idx = -1\n    \
        \            while low <= high {\n                    let mid = (low + high)\
        \ / 2\n                    if sortedIntervals[mid].r < targetL {\n         \
        \               idx = mid\n                        low = mid + 1\n         \
        \           } else {\n                        high = mid - 1\n             \
        \       }\n                }\n\n                if let prev = dp[k - 1][idx\
        \ + 1] {\n                    let currentWeight = prev.weight + sortedIntervals[i\
        \ - 1].w\n                    var currentIndices = prev.indices\n          \
        \          currentIndices.append(sortedIntervals[i - 1].id)\n              \
        \      currentIndices.sort()\n\n                    if dp[k][i] == nil || \n\
        \                       currentWeight > dp[k][i]!.weight || \n             \
        \          (currentWeight == dp[k][i]!.weight && currentIndices.lexicographicallyPrecedes(dp[k][i]!.indices))\
        \ {\n                        dp[k][i] = State(weight: currentWeight, indices:\
        \ currentIndices)\n                    }\n                }\n            }\n\
        \        }\n\n        var bestState: State = State(weight: 0, indices: [])\n\
        \        for k in 1...4 {\n            if let current = dp[k][n] {\n       \
        \         if current.weight > bestState.weight || \n                   (current.weight\
        \ == bestState.weight && (bestState.indices.isEmpty || current.indices.lexicographicallyPrecedes(bestState.indices)))\
        \ {\n                    bestState = current\n                }\n          \
        \  }\n        }\n\n        return bestState.indices\n    }\n}"
      kotlin: "class Solution {\n    class Interval(val l: Int, val r: Int, val weight:\
        \ Long, val id: Int)\n    class State(val weight: Long, val indices: IntArray)\n\
        \n    fun maximumWeight(intervals: List<List<Int>>): IntArray {\n        val\
        \ n = intervals.size\n        val sortedIntervals = Array(n) { i ->\n      \
        \      Interval(intervals[i][0], intervals[i][1], intervals[i][2].toLong(),\
        \ i)\n        }\n        sortedIntervals.sortBy { it.r }\n\n        val dp =\
        \ Array(5) { arrayOfNulls<State>(n + 1) }\n        for (i in 0..n) {\n     \
        \       dp[0][i] = State(0L, intArrayOf())\n        }\n\n        fun isBetter(w1:\
        \ Long, idx1: IntArray, w2: Long, idx2: IntArray): Boolean {\n            if\
        \ (w1 != w2) return w1 > w2\n            val n1 = idx1.size\n            val\
        \ n2 = idx2.size\n            val minLen = if (n1 < n2) n1 else n2\n       \
        \     for (i in 0 until minLen) {\n                if (idx1[i] < idx2[i]) return\
        \ true\n                if (idx1[i] > idx2[i]) return false\n            }\n\
        \            return n1 < n2\n        }\n\n        for (k in 1..4) {\n      \
        \      for (i in 1..n) {\n                dp[k][i] = dp[k][i - 1]\n\n      \
        \          val targetL = sortedIntervals[i - 1].l\n                var low =\
        \ 0\n                var high = n - 1\n                var lastIdx = -1\n  \
        \              while (low <= high) {\n                    val mid = (low + high)\
        \ ushr 1\n                    if (sortedIntervals[mid].r < targetL) {\n    \
        \                    lastIdx = mid\n                        low = mid + 1\n\
        \                    } else {\n                        high = mid - 1\n    \
        \                }\n                }\n\n                val prev = dp[k - 1][lastIdx\
        \ + 1]\n                if (prev != null) {\n                    val currentWeight\
        \ = prev.weight + sortedIntervals[i - 1].weight\n                    val currentIndices\
        \ = IntArray(prev.indices.size + 1)\n                    System.arraycopy(prev.indices,\
        \ 0, currentIndices, 0, prev.indices.size)\n                    currentIndices[prev.indices.size]\
        \ = sortedIntervals[i - 1].id\n                    currentIndices.sort()\n\n\
        \                    if (dp[k][i] == null || isBetter(currentWeight, currentIndices,\
        \ dp[k][i]!!.weight, dp[k][i]!!.indices)) {\n                        dp[k][i]\
        \ = State(currentWeight, currentIndices)\n                    }\n          \
        \      }\n            }\n        }\n\n        var bestState: State? = null\n\
        \        for (k in 1..4) {\n            val current = dp[k][n]\n           \
        \ if (current != null) {\n                if (bestState == null || isBetter(current.weight,\
        \ current.indices, bestState.weight, bestState.indices)) {\n               \
        \     bestState = current\n                }\n            }\n        }\n\n \
        \       return bestState?.indices ?: intArrayOf()\n    }\n}"
      dart: "class Interval {\n  final int l, r, weight, id;\n  Interval(this.l, this.r,\
        \ this.weight, this.id);\n}\n\nclass State {\n  final int weight;\n  final List<int>\
        \ indices;\n  State(this.weight, this.indices);\n}\n\nclass Solution {\n  List<int>\
        \ maximumWeight(List<List<int>> intervals) {\n    int n = intervals.length;\n\
        \    List<Interval> sorted = [];\n    for (int i = 0; i < n; i++) {\n      sorted.add(Interval(intervals[i][0],\
        \ intervals[i][1], intervals[i][2], i));\n    }\n    sorted.sort((a, b) => a.r.compareTo(b.r));\n\
        \n    List<List<State>> dp = List.generate(5, (_) => List.generate(n + 1, (_)\
        \ => State(-1, [])));\n\n    for (int j = 0; j <= n; j++) {\n      dp[0][j]\
        \ = State(0, []);\n    }\n\n    for (int k = 1; k <= 4; k++) {\n      for (int\
        \ i = 1; i <= n; i++) {\n        Interval curr = sorted[i - 1];\n        //\
        \ Option 1: Don't include sorted[i-1]\n        State best = dp[k][i - 1];\n\n\
        \        // Option 2: Include sorted[i-1]\n        int prevIdx = findPrev(sorted,\
        \ curr.l);\n        if (dp[k - 1][prevIdx + 1].weight != -1) {\n          int\
        \ newWeight = dp[k - 1][prevIdx + 1].weight + curr.weight;\n          List<int>\
        \ newIndices = List<int>.from(dp[k - 1][prevIdx + 1].indices)..add(curr.id);\n\
        \          newIndices.sort();\n          if (isBetter(newWeight, newIndices,\
        \ best.weight, best.indices)) {\n            best = State(newWeight, newIndices);\n\
        \          }\n        }\n        dp[k][i] = best;\n      }\n    }\n\n    State\
        \ finalBest = State(-1, []);\n    for (int k = 1; k <= 4; k++) {\n      if (isBetter(dp[k][n].weight,\
        \ dp[k][n].indices, finalBest.weight, finalBest.indices)) {\n        finalBest\
        \ = dp[k][n];\n      }\n    }\n    return finalBest.indices;\n  }\n\n  int findPrev(List<Interval>\
        \ sorted, int targetL) {\n    int low = 0, high = sorted.length - 1, ans = -1;\n\
        \    while (low <= high) {\n      int mid = low + (high - low) ~/ 2;\n     \
        \ if (sorted[mid].r < targetL) {\n        ans = mid;\n        low = mid + 1;\n\
        \      } else {\n        high = mid - 1;\n      }\n    }\n    return ans;\n\
        \  }\n\n  bool isBetter(int w1, List<int> idx1, int w2, List<int> idx2) {\n\
        \    if (w1 != w2) return w1 > w2;\n    if (w1 == -1) return false;\n    int\
        \ n1 = idx1.length, n2 = idx2.length;\n    int minLen = n1 < n2 ? n1 : n2;\n\
        \    for (int i = 0; i < minLen; i++) {\n      if (idx1[i] < idx2[i]) return\
        \ true;\n      if (idx1[i] > idx2[i]) return false;\n    }\n    return n1 <\
        \ n2;\n  }\n}"
      go: "func maximumWeight(intervals [][]int) []int {\n\tn := len(intervals)\n\t\
        type Interval struct {\n\t\tl, r, id int\n\t\tw        int64\n\t}\n\tsorted\
        \ := make([]Interval, n)\n\tfor i := 0; i < n; i++ {\n\t\tsorted[i] = Interval{intervals[i][0],\
        \ intervals[i][1], i, int64(intervals[i][2])}\n\t}\n\timport \"sort\"\n\tsort.Slice(sorted,\
        \ func(i, j int) bool {\n\t\treturn sorted[i].r < sorted[j].r\n\t})\n\n\ttype\
        \ State struct {\n\t\tweight  int64\n\t\tindices []int\n\t}\n\n\tisBetter :=\
        \ func(w1 int64, idx1 []int, w2 int64, idx2 []int) bool {\n\t\tif w1 != w2 {\n\
        \t\t\treturn w1 > w2\n\t\t}\n\t\tif w1 == -1 {\n\t\t\treturn false\n\t\t}\n\t\
        \tn1, n2 := len(idx1), len(idx2)\n\t\tlimit := n1\n\t\tif n2 < limit {\n\t\t\
        \tlimit = n2\n\t\t}\n\t\tfor i := 0; i < limit; i++ {\n\t\t\tif idx1[i] < idx2[i]\
        \ {\n\t\t\t\treturn true\n\t\t\t}\n\t\t\tif idx1[i] > idx2[i] {\n\t\t\t\treturn\
        \ false\n\t\t\t}\n\t\t}\n\t\treturn n1 < n2\n\t}\n\n\tdp := make([][]State,\
        \ 5)\n\tfor k := 0; k < 5; k++ {\n\t\tdp[k] = make([]State, n+1)\n\t\tfor i\
        \ := 0; i <= n; i++ {\n\t\t\tdp[k][i] = State{weight: -1}\n\t\t}\n\t}\n\tfor\
        \ i := 0; i <= n; i++ {\n\t\tdp[0][i] = State{weight: 0, indices: []int{}}\n\
        \t}\n\n\tfor k := 1; k <= 4; k++ {\n\t\tfor i := 1; i <= n; i++ {\n\t\t\tcurr\
        \ := sorted[i-1]\n\t\t\tbestWeight := dp[k][i-1].weight\n\t\t\tbestIndices :=\
        \ dp[k][i-1].indices\n\n\t\t\ttargetL := curr.l\n\t\t\tprevIdx := sort.Search(i,\
        \ func(j int) bool {\n\t\t\t\treturn sorted[j].r >= targetL\n\t\t\t}) - 1\n\n\
        \t\t\tif dp[k-1][prevIdx+1].weight != -1 {\n\t\t\t\tnewWeight := dp[k-1][prevIdx+1].weight\
        \ + curr.w\n\t\t\t\tnewIndices := make([]int, len(dp[k-1][prevIdx+1].indices),\
        \ len(dp[k-1][prevIdx+1].indices)+1)\n\t\t\t\tcopy(newIndices, dp[k-1][prevIdx+1].indices)\n\
        \t\t\t\tnewIndices = append(newIndices, curr.id)\n\t\t\t\tsort.Ints(newIndices)\n\
        \n\t\t\t\tif isBetter(newWeight, newIndices, bestWeight, bestIndices) {\n\t\t\
        \t\t\tbestWeight = newWeight\n\t\t\t\t\tbestIndices = newIndices\n\t\t\t\t}\n\
        \t\t\t}\n\t\t\tdp[k][i] = State{bestWeight, bestIndices}\n\t\t}\n\t}\n\n\tvar\
        \ finalW int64 = -1\n\tvar finalIdx []int\n\tfor k := 1; k <= 4; k++ {\n\t\t\
        if isBetter(dp[k][n].weight, dp[k][n].indices, finalW, finalIdx) {\n\t\t\tfinalW\
        \ = dp[k][n].weight\n\t\t\tfinalIdx = dp[k][n].indices\n\t\t}\n\t}\n\treturn\
        \ finalIdx\n}"
      ruby: "def maximum_weight(intervals)\n  n = intervals.length\n  interval_struct\
        \ = Struct.new(:l, :r, :w, :id)\n  sorted = intervals.each_with_index.map {\
        \ |(l, r, w), i| interval_struct.new(l, r, w, i) }.sort_by(&:r)\n\n  state_struct\
        \ = Struct.new(:weight, :indices)\n  dp = Array.new(5) { Array.new(n + 1) {\
        \ state_struct.new(-1, []) } }\n  (0..n).each { |i| dp[0][i] = state_struct.new(0,\
        \ []) }\n\n  def compare(w1, ids1, w2, ids2)\n    return false if w1 == -1\n\
        \    return true if w2 == -1\n    return true if w1 > w2\n    return false if\
        \ w1 < w2\n    (ids1 <=> ids2) == -1\n  end\n\n  (1..4).each do |k|\n    (1..n).each\
        \ do |i|\n      curr = sorted[i - 1]\n      best_weight = dp[k][i - 1].weight\n\
        \      best_indices = dp[k][i - 1].indices\n\n      idx = sorted.bsearch_index\
        \ { |x| x.r >= curr.l }\n      prev_idx = idx ? idx - 1 : n - 1\n\n      if\
        \ dp[k - 1][prev_idx + 1].weight != -1\n        new_weight = dp[k - 1][prev_idx\
        \ + 1].weight + curr.w\n        new_indices = (dp[k - 1][prev_idx + 1].indices\
        \ + [curr.id]).sort\n        if compare(new_weight, new_indices, best_weight,\
        \ best_indices)\n          best_weight = new_weight\n          best_indices\
        \ = new_indices\n        end\n      end\n      dp[k][i] = state_struct.new(best_weight,\
        \ best_indices)\n    end\n  end\n\n  final_best = state_struct.new(-1, [])\n\
        \  (1..4).each do |k|\n    if compare(dp[k][n].weight, dp[k][n].indices, final_best.weight,\
        \ final_best.indices)\n      final_best = dp[k][n]\n    end\n  end\n  final_best.indices\n\
        end"
      scala: "object Solution {\n    case class Interval(l: Int, r: Int, w: Long, id:\
        \ Int)\n    case class State(weight: Long, indices: Array[Int])\n\n    def maximumWeight(intervals:\
        \ List[List[Int]]): Array[Int] = {\n        val n = intervals.length\n     \
        \   val sorted = intervals.zipWithIndex.map { case (list, idx) =>\n        \
        \    Interval(list(0), list(1), list(2).toLong, idx)\n        }.toArray.sortBy(_.r)\n\
        \n        val dp = Array.fill(5, n + 1)(State(-1L, Array.empty[Int]))\n    \
        \    for (i <- 0 to n) dp(0)(i) = State(0L, Array.empty[Int])\n\n        def\
        \ isBetter(w1: Long, idx1: Array[Int], w2: Long, idx2: Array[Int]): Boolean\
        \ = {\n            if (w1 != w2) return w1 > w2\n            if (w1 == -1L)\
        \ return false\n            val n1 = idx1.length\n            val n2 = idx2.length\n\
        \            var i = 0\n            val minLen = if (n1 < n2) n1 else n2\n \
        \           while (i < minLen) {\n                if (idx1(i) < idx2(i)) return\
        \ true\n                if (idx1(i) > idx2(i)) return false\n              \
        \  i += 1\n            }\n            n1 < n2\n        }\n\n        def findPrev(arr:\
        \ Array[Interval], targetL: Int): Int = {\n            var low = 0\n       \
        \     var high = arr.length - 1\n            var ans = -1\n            while\
        \ (low <= high) {\n                val mid = low + (high - low) / 2\n      \
        \          if (arr(mid).r < targetL) {\n                    ans = mid\n    \
        \                low = mid + 1\n                } else {\n                 \
        \   high = mid - 1\n                }\n            }\n            ans\n    \
        \    }\n\n        for (k <- 1 to 4) {\n            for (i <- 1 to n) {\n   \
        \             val curr = sorted(i - 1)\n                var bestWeight = dp(k)(i\
        \ - 1).weight\n                var bestIndices = dp(k)(i - 1).indices\n\n  \
        \              val prevIdx = findPrev(sorted.take(i), curr.l)\n            \
        \    if (dp(k - 1)(prevIdx + 1).weight != -1L) {\n                    val newWeight\
        \ = dp(k - 1)(prevIdx + 1).weight + curr.w\n                    val newIndices\
        \ = (dp(k - 1)(prevIdx + 1).indices :+ curr.id).sorted\n                   \
        \ if (isBetter(newWeight, newIndices, bestWeight, bestIndices)) {\n        \
        \                bestWeight = newWeight\n                        bestIndices\
        \ = newIndices\n                    }\n                }\n                dp(k)(i)\
        \ = State(bestWeight, bestIndices)\n            }\n        }\n\n        var\
        \ finalW = -1L\n        var finalIdx = Array.empty[Int]\n        for (k <- 1\
        \ to 4) {\n            if (isBetter(dp(k)(n).weight, dp(k)(n).indices, finalW,\
        \ finalIdx)) {\n                finalW = dp(k)(n).weight\n                finalIdx\
        \ = dp(k)(n).indices\n            }\n        }\n        finalIdx\n    }\n}"
      rust: "impl Solution {\n    pub fn maximum_weight(intervals: Vec<Vec<i32>>) ->\
        \ Vec<i32> {\n        let n = intervals.len();\n        struct Interval {\n\
        \            l: i32,\n            r: i32,\n            w: i32,\n           \
        \ id: i32,\n        }\n        let mut sorted: Vec<_> = intervals.into_iter().enumerate().map(|(i,\
        \ v)| {\n            Interval { l: v[0], r: v[1], w: v[2], id: i as i32 }\n\
        \        }).collect();\n        sorted.sort_unstable_by(|a, b| a.r.cmp(&b.r).then(a.l.cmp(&b.l)).then(a.w.cmp(&b.w)).then(a.id.cmp(&b.id)));\n\
        \n        let mut dp = vec![(0i64, vec![]); n + 1];\n        let mut overall_best\
        \ = (0i64, vec![]);\n\n        for _k in 1..=4 {\n            let mut next_dp\
        \ = vec![(0i64, vec![]); n + 1];\n            for i in 1..=n {\n           \
        \     let interval = &sorted[i - 1];\n                let mut low = 0;\n   \
        \             let mut high = i - 1;\n                while low < high {\n  \
        \                  let mid = low + (high - low) / 2;\n                    if\
        \ sorted[mid].r < interval.l {\n                        low = mid + 1;\n   \
        \                 } else {\n                        high = mid;\n          \
        \          }\n                }\n                let prev_idx = low;\n\n   \
        \             let mut pick_i_indices = dp[prev_idx].1.clone();\n           \
        \     pick_i_indices.push(interval.id);\n                pick_i_indices.sort_unstable();\n\
        \                let pick_i_weight = dp[prev_idx].0 + interval.w as i64;\n \
        \               let pick_i = (pick_i_weight, pick_i_indices);\n\n          \
        \      let option1 = &next_dp[i - 1];\n                if is_better(pick_i.0,\
        \ &pick_i.1, option1.0, &option1.1) {\n                    next_dp[i] = pick_i;\n\
        \                } else {\n                    next_dp[i] = option1.clone();\n\
        \                }\n            }\n            dp = next_dp;\n            if\
        \ is_better(dp[n].0, &dp[n].1, overall_best.0, &overall_best.1) {\n        \
        \        overall_best = dp[n].clone();\n            }\n        }\n        overall_best.1\n\
        \    }\n}\n\nfn is_better(w1: i64, idx1: &[i32], w2: i64, idx2: &[i32]) -> bool\
        \ {\n    if w1 != w2 {\n        return w1 > w2;\n    }\n    if idx1.is_empty()\
        \ && !idx2.is_empty() { return false; }\n    if !idx1.is_empty() && idx2.is_empty()\
        \ { return true; }\n    idx1 < idx2\n}"
      racket: "(define/contract (maximum-weight intervals)\n  (-> (listof (listof exact-integer?))\
        \ (listof exact-integer?))\n  (let* ([n (length intervals)]\n         [intervals-list\n\
        \          (sort\n           (for/list ([inter (in-list intervals)] [i (in-naturals)])\n\
        \             (list (first inter) (second inter) (third inter) i))\n       \
        \    (lambda (a b)\n             (if (not (= (second a) (second b)))\n     \
        \            (< (second a) (second b))\n                 (if (not (= (first\
        \ a) (first b)))\n                     (< (first a) (first b))\n           \
        \          (if (not (= (third a) (third b)))\n                         (< (third\
        \ a) (third b))\n                         (< (fourth a) (fourth b)))))))]\n\
        \         [sorted-intervals (list->vector intervals-list)])\n\n    (define (find-prev\
        \ target-l)\n      (let loop ([low 0] [high (vector-length sorted-intervals)])\n\
        \        (if (< low high)\n            (let* ([mid (quotient (+ low high) 2)]\n\
        \                   [r (second (vector-ref sorted-intervals mid))])\n      \
        \        (if (< r target-l)\n                  (loop (+ mid 1) high)\n     \
        \             (loop low mid)))\n            low)))\n\n    (define (lex-less?\
        \ l1 l2)\n      (cond\n        [(null? l1) (not (null? l2))]\n        [(null?\
        \ l2) #f]\n        [(< (car l1) (car l2)) #t]\n        [(> (car l1) (car l2))\
        \ #f]\n        [else (lex-less? (cdr l1) (cdr l2))]))\n\n    (define (is-better?\
        \ s1 s2)\n      (if (> (car s1) (car s2)) #t\n          (if (< (car s1) (car\
        \ s2)) #f\n              (lex-less? (cdr s1) (cdr s2)))))\n\n    (define dp\
        \ (make-vector (+ n 1) '(0 . ())))\n    (define overall-best '(0 . ()))\n\n\
        \    (for ([k (in-range 1 5)])\n      (define next-dp (make-vector (+ n 1)))\n\
        \      (vector-set! next-dp 0 '(0 . ()))\n      (for ([i (in-range 1 (+ n 1))])\n\
        \        (let* ([interval (vector-ref sorted-intervals (- i 1))]\n         \
        \      [l (first interval)]\n               [w (third interval)]\n         \
        \      [id (fourth interval)]\n               [prev-idx (find-prev l)]\n   \
        \            [option1 (vector-ref next-dp (- i 1))]\n               [prev-state\
        \ (vector-ref dp prev-idx)]\n               [option2 (cons (+ (car prev-state)\
        \ w)\n                              (sort (cons id (cdr prev-state)) <))])\n\
        \          (vector-set! next-dp i (if (is-better? option2 option1) option2 option1))))\n\
        \      (set! dp next-dp)\n      (if (is-better? (vector-ref dp n) overall-best)\n\
        \          (set! overall-best (vector-ref dp n))\n          #t))\n    (cdr overall-best)))"
      erlang: "-spec maximum_weight(Intervals :: [[integer()]]) -> [integer()].\nmaximum_weight(Intervals)\
        \ ->\n  N = length(Intervals),\n  IntervalsWithId = lists:zipwith(fun([L, R,\
        \ W], Id) -> {L, R, W, Id} end, Intervals, lists:seq(0, N - 1)),\n  SortedIntervals\
        \ = lists:sort(fun({L1, R1, W1, Id1}, {L2, R2, W2, Id2}) ->\n              \
        \                    if R1 /= R2 -> R1 < R2;\n                             \
        \        L1 /= L2 -> L1 < L2;\n                                     W1 /= W2\
        \ -> W1 < W2;\n                                     true -> Id1 < Id2\n    \
        \                              end\n                               end, IntervalsWithId),\n\
        \  IntervalsTuple = list_to_tuple(SortedIntervals),\n  InitialDP = lists:duplicate(N\
        \ + 1, {0, []}),\n  FinalBest = solve_dp(1, IntervalsTuple, InitialDP, {0, []}),\n\
        \  element(2, FinalBest).\n\nsolve_dp(K, _Intervals, DP, BestOverall) when K\
        \ > 4 -> BestOverall;\nsolve_dp(K, Intervals, DP, BestOverall) ->\n  PrevDP\
        \ = list_to_tuple(DP),\n  N = tuple_size(Intervals),\n  NewDPList = compute_k(1,\
        \ N, Intervals, PrevDP, {0, []}, [{0, []}]),\n  CurrentDP = lists:reverse(NewDPList),\n\
        \  CurrentBest = lists:last(CurrentDP),\n  NewBest = if element(1, CurrentBest)\
        \ > element(1, BestOverall) -> CurrentBest;\n               element(1, CurrentBest)\
        \ < element(1, BestOverall) -> BestOverall;\n               element(2, CurrentBest)\
        \ < element(2, BestOverall) -> CurrentBest;\n               true -> BestOverall\n\
        \            end,\n  solve_dp(K + 1, Intervals, CurrentDP, NewBest).\n\ncompute_k(I,\
        \ N, Intervals, PrevDP, PrevKDP, Acc) when I =< N ->\n  {L, _, W, Id} = element(I,\
        \ Intervals),\n  PrevIdx = find_prev(Intervals, L, 1, I - 1, 0),\n  {PrevW,\
        \ PrevIdxs} = element(PrevIdx + 1, PrevDP),\n  NewW = PrevW + W,\n  NewIdxs\
        \ = lists:sort([Id | PrevIdxs]),\n  PickI = {NewW, NewIdxs},\n  {BestW, BestIdxs}\
        \ = PrevKDP,\n  CurrentBest = if NewW > BestW -> PickI;\n                  \
        \ NewW < BestW -> PrevKDP;\n                   NewIdxs < BestIdxs -> PickI;\n\
        \                   true -> PrevKDP\n                end,\n  compute_k(I + 1,\
        \ N, Intervals, PrevDP, CurrentBest, [CurrentBest | Acc]);\ncompute_k(_I, _N,\
        \ _Intervals, _PrevDP, _PrevKDP, Acc) -> Acc.\n\nfind_prev(Intervals, L, Low,\
        \ High, Best) when Low =< High ->\n  Mid = (Low + High) div 2,\n  {_, Ri, _,\
        \ _} = element(Mid, Intervals),\n  if Ri < L -> find_prev(Intervals, L, Mid\
        \ + 1, High, Mid);\n     true -> find_prev(Intervals, L, Low, Mid - 1, Best)\n\
        \  end;\nfind_prev(_Intervals, _L, _Low, _High, Best) -> Best."
      elixir: "defmodule Solution do\n  @spec maximum_weight(intervals :: [[integer]])\
        \ :: [integer]\n  def maximum_weight(intervals) do\n    n = length(intervals)\n\
        \    intervals_with_id = Enum.with_index(intervals) |> Enum.map(fn {[l, r, w],\
        \ id} -> {l, r, w, id} end)\n    sorted_intervals = Enum.sort(intervals_with_id,\
        \ fn {l1, r1, w1, id1}, {l2, r2, w2, id2} ->\n      if r1 != r2, do: r1 < r2,\
        \ else: (if l1 != l2, do: l1 < l2, else: (if w1 != w2, do: w1 < w2, else: id1\
        \ < id2))\n    end)\n    intervals_tuple = List.to_tuple(sorted_intervals)\n\
        \    initial_dp = List.duplicate({0, []}, n + 1)\n\n    final_state = Enum.reduce(1..4,\
        \ {{0, []}, initial_dp}, fn _k, {overall_best, dp} ->\n      prev_dp_tuple =\
        \ List.to_tuple(dp)\n      new_dp_list = compute_k(1, n, intervals_tuple, prev_dp_tuple,\
        \ {0, []}, [{0, []}])\n      current_dp = Enum.reverse(new_dp_list)\n      current_best\
        \ = List.last(current_dp)\n\n      new_overall = if is_better?(current_best,\
        \ overall_best), do: current_best, else: overall_best\n      {new_overall, current_dp}\n\
        \    end)\n\n    elem(elem(final_state, 0), 1)\n  end\n\n  defp compute_k(i,\
        \ n, intervals, prev_dp, prev_k_dp, acc) when i <= n do\n    {l, _r, w, id}\
        \ = elem(intervals, i - 1)\n    prev_idx = find_prev(intervals, l, 1, i - 1,\
        \ 0)\n    {prev_w, prev_idxs} = elem(prev_dp, prev_idx)\n\n    pick_i = {prev_w\
        \ + w, Enum.sort([id | prev_idxs])}\n    current_best = if is_better?(pick_i,\
        \ prev_k_dp), do: pick_i, else: prev_k_dp\n    compute_k(i + 1, n, intervals,\
        \ prev_dp, current_best, [current_best | acc])\n  end\n  defp compute_k(_i,\
        \ _n, _intervals, _prev_dp, _prev_k_dp, acc), do: acc\n\n  defp find_prev(intervals,\
        \ l, low, high, best) when low <= high do\n    mid = div(low + high, 2)\n  \
        \  {_li, ri, _wi, _idi} = elem(intervals, mid - 1)\n    if ri < l do\n     \
        \ find_prev(intervals, l, mid + 1, high, mid)\n    else\n      find_prev(intervals,\
        \ l, low, mid - 1, best)\n    end\n  end\n  defp find_prev(_intervals, _l, _low,\
        \ _high, best), do: best\n\n  defp is_better?({w1, idx1}, {w2, idx2}) do\n \
        \   cond do\n      w1 > w2 -> true\n      w1 < w2 -> false\n      true -> idx1\
        \ < idx2\n    end\n  end\nend"
    approach: 'To solve this problem, we use dynamic programming with a state $dp[k][i]$
      representing the maximum score achievable using exactly $k$ non-overlapping intervals
      from the first $i$ intervals (when sorted by their right boundaries). The DP transition
      is $dp[k][i] = \text{best}(dp[k][i-1], \text{candidate})$, where the ''candidate''
      is formed by picking the $i$-th interval and combining it with the best $k-1$
      intervals that end before the $i$-th interval starts. We use binary search on
      the sorted end times to find the largest index $j$ such that $intervals[j].r <
      intervals[i].l$ in $O(\log N)$ time.


      To satisfy the lexicographically smallest requirement, each DP state also stores
      the sorted array of indices that yield the maximum score. When comparing two sets
      of intervals with the same score, we choose the one whose sorted indices are lexicographically
      smaller. Since $K$ is small (up to 4), we can efficiently maintain and compare
      these sets. To optimize space, we observe that the $k$-th DP layer only depends
      on the $(k-1)$-th layer, allowing us to use only $O(N)$ space per layer.'
    time_complexity: O(K \cdot N \log N), where $K = 4$ and $N$ is the number of intervals.
      Sorting the intervals takes $O(N \log N)$. For each $k \in \{1, 2, 3, 4\}$, we
      iterate through $N$ intervals and perform a binary search in $O(\log N)$. Comparing
      and sorting the small index lists takes $O(K)$ time, which is constant.
    space_complexity: O(K \cdot N), to store the DP table. By optimizing the DP to only
      keep the current and previous layers, this can be reduced to $O(N)$, though $O(K
      \cdot N)$ is well within limits for $N = 5 \times 10^4$.
    elapsed_time: 655.244756937027
    model: gemini-3-flash-preview
    generated_at: '2026-09-12 02:37:37 '
---

## Problem #3414: Maximum Score of Non-overlapping Intervals

**Difficulty:** Hard

**Topics:** Array, Binary Search, Dynamic Programming, Sorting

## Problem Description

<p>You are given a 2D integer array <code>intervals</code>, where <code>intervals[i] = [l<sub>i</sub>, r<sub>i</sub>, weight<sub>i</sub>]</code>. Interval <code>i</code> starts at position <code>l<sub>i</sub></code> and ends at <code>r<sub>i</sub></code>, and has a weight of <code>weight<sub>i</sub></code>. You can choose <em>up to</em> 4 <strong>non-overlapping</strong> intervals. The <strong>score</strong> of the chosen intervals is defined as the total sum of their weights.</p>

<p>Return the <span data-keyword="lexicographically-smaller-array">lexicographically smallest</span> array of at most 4 indices from <code>intervals</code> with <strong>maximum</strong> score, representing your choice of non-overlapping intervals.</p>

<p>Two intervals are said to be <strong>non-overlapping</strong> if they do not share any points. In particular, intervals sharing a left or right boundary are considered overlapping.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">intervals = [[1,3,2],[4,5,2],[1,5,5],[6,9,3],[6,7,1],[8,9,1]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[2,3]</span></p>

<p><strong>Explanation:</strong></p>

<p>You can choose the intervals with indices 2, and 3 with respective weights of 5, and 3.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">intervals = [[5,8,1],[6,7,7],[4,7,3],[9,10,6],[7,8,2],[11,14,3],[3,5,5]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[1,3,5,6]</span></p>

<p><strong>Explanation:</strong></p>

<p>You can choose the intervals with indices 1, 3, 5, and 6 with respective weights of 7, 6, 3, and 5.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= intevals.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>intervals[i].length == 3</code></li>
	<li><code>intervals[i] = [l<sub>i</sub>, r<sub>i</sub>, weight<sub>i</sub>]</code></li>
	<li><code>1 &lt;= l<sub>i</sub> &lt;= r<sub>i</sub> &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= weight<sub>i</sub> &lt;= 10<sup>9</sup></code></li>
</ul>


## Hints

1. Use Dynamic Programming.

2. Sort `intervals` by right boundary.

3. Let `dp[r][i]` denote the maximum score having picked `r` intervals from the prefix of `intervals` ending at index `i`.

4. `dp[r][i] = max(dp[r][i - 1], intervals[i][2] + dp[r][j])` where `j` is the largest index such that `intervals[j][1] < intervals[i][0]`.

5. Since `intervals` is sorted by right boundary, we can find index `j` using binary search.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To solve this problem, we use dynamic programming with a state $dp[k][i]$ representing the maximum score achievable using exactly $k$ non-overlapping intervals from the first $i$ intervals (when sorted by their right boundaries). The DP transition is $dp[k][i] = \text{best}(dp[k][i-1], \text{candidate})$, where the 'candidate' is formed by picking the $i$-th interval and combining it with the best $k-1$ intervals that end before the $i$-th interval starts. We use binary search on the sorted end times to find the largest index $j$ such that $intervals[j].r < intervals[i].l$ in $O(\log N)$ time.

To satisfy the lexicographically smallest requirement, each DP state also stores the sorted array of indices that yield the maximum score. When comparing two sets of intervals with the same score, we choose the one whose sorted indices are lexicographically smaller. Since $K$ is small (up to 4), we can efficiently maintain and compare these sets. To optimize space, we observe that the $k$-th DP layer only depends on the $(k-1)$-th layer, allowing us to use only $O(N)$ space per layer.

### Code

<div class="code-tabs" markdown="0">
  <input type="radio" name="code-lang" id="lang-cpp" checked>
  <input type="radio" name="code-lang" id="lang-java">
  <input type="radio" name="code-lang" id="lang-python">
  <input type="radio" name="code-lang" id="lang-python3">
  <input type="radio" name="code-lang" id="lang-c">
  <input type="radio" name="code-lang" id="lang-csharp">
  <input type="radio" name="code-lang" id="lang-javascript">
  <input type="radio" name="code-lang" id="lang-typescript">
  <input type="radio" name="code-lang" id="lang-php">
  <input type="radio" name="code-lang" id="lang-swift">
  <input type="radio" name="code-lang" id="lang-kotlin">
  <input type="radio" name="code-lang" id="lang-dart">
  <input type="radio" name="code-lang" id="lang-go">
  <input type="radio" name="code-lang" id="lang-ruby">
  <input type="radio" name="code-lang" id="lang-scala">
  <input type="radio" name="code-lang" id="lang-rust">
  <input type="radio" name="code-lang" id="lang-racket">
  <input type="radio" name="code-lang" id="lang-erlang">
  <input type="radio" name="code-lang" id="lang-elixir">
  <div class="tab-labels">
    <label for="lang-cpp">C++</label>
    <label for="lang-java">Java</label>
    <label for="lang-python">Python</label>
    <label for="lang-python3">Python3</label>
    <label for="lang-c">C</label>
    <label for="lang-csharp">C#</label>
    <label for="lang-javascript">JavaScript</label>
    <label for="lang-typescript">TypeScript</label>
    <label for="lang-php">PHP</label>
    <label for="lang-swift">Swift</label>
    <label for="lang-kotlin">Kotlin</label>
    <label for="lang-dart">Dart</label>
    <label for="lang-go">Go</label>
    <label for="lang-ruby">Ruby</label>
    <label for="lang-scala">Scala</label>
    <label for="lang-rust">Rust</label>
    <label for="lang-racket">Racket</label>
    <label for="lang-erlang">Erlang</label>
    <label for="lang-elixir">Elixir</label>
  </div>

  <div class="tab-panel" data-lang="cpp">

{% highlight cpp %}
{% raw %}
class Solution {
    struct State {
        long long score;
        int cnt;
        int idx[4];

        State() : score(-1), cnt(0) {}

        bool isBetterThan(const State& other) const {
            if (score != other.score) return score > other.score;
            if (cnt == 0) return false;
            if (other.cnt == 0) return true;
            int len = std::min(cnt, other.cnt);
            for (int i = 0; i < len; ++i) {
                if (idx[i] != other.idx[i]) return idx[i] < other.idx[i];
            }
            return cnt < other.cnt;
        }

        void set(long long s, int c, const int* existing, int extra) {
            score = s;
            cnt = c;
            if (existing) {
                for (int i = 0; i < c - 1; ++i) idx[i] = existing[i];
            }
            idx[c - 1] = extra;
            std::sort(idx, idx + cnt);
        }
    };

    struct Interval {
        int l, r, weight, id;
    };

public:
    vector<int> maximumWeight(vector<vector<int>>& intervals) {
        int n = intervals.size();
        vector<Interval> ivs(n);
        for (int i = 0; i < n; ++i) {
            ivs[i] = {intervals[i][0], intervals[i][1], intervals[i][2], i};
        }
        std::sort(ivs.begin(), ivs.end(), [](const Interval& a, const Interval& b) {
            return a.r < b.r;
        });

        vector<State> prev_dp(n);
        vector<State> curr_dp(n);
        State ans;

        for (int k = 1; k <= 4; ++k) {
            for (int i = 0; i < n; ++i) {
                if (i > 0) curr_dp[i] = curr_dp[i - 1];
                else curr_dp[i] = State();

                int j = -1, low = 0, high = i - 1;
                while (low <= high) {
                    int mid = low + (high - low) / 2;
                    if (ivs[mid].r < ivs[i].l) { j = mid; low = mid + 1; } 
                    else high = mid - 1;
                }

                State cand;
                if (k == 1) {
                    cand.set(ivs[i].weight, 1, nullptr, ivs[i].id);
                } else if (j != -1 && prev_dp[j].score != -1) {
                    cand.set(prev_dp[j].score + ivs[i].weight, k, prev_dp[j].idx, ivs[i].id);
                }

                if (cand.isBetterThan(curr_dp[i])) curr_dp[i] = cand;
            }
            if (curr_dp[n - 1].isBetterThan(ans)) ans = curr_dp[n - 1];
            prev_dp = curr_dp;
        }

        vector<int> res;
        for (int i = 0; i < ans.cnt; ++i) res.push_back(ans.idx[i]);
        return res;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.*;

class Solution {
    static class Interval {
        int l, r, w, id;
        Interval(int l, int r, int w, int id) {
            this.l = l; this.r = r; this.w = w; this.id = id;
        }
    }

    static class State {
        long score;
        int[] idx;
        State(long score, int[] idx) { this.score = score; this.idx = idx; }
    }

    private boolean isBetter(long s1, int[] i1, long s2, int[] i2) {
        if (s1 != s2) return s1 > s2;
        if (i1 == null) return false;
        if (i2 == null) return true;
        int len = Math.min(i1.length, i2.length);
        for (int i = 0; i < len; i++) {
            if (i1[i] != i2[i]) return i1[i] < i2[i];
        }
        return i1.length < i2.length;
    }

    public int[] maximumWeight(List<List<Integer>> intervals) {
        int n = intervals.size();
        Interval[] ivs = new Interval[n];
        for (int i = 0; i < n; i++) {
            ivs[i] = new Interval(intervals.get(i).get(0), intervals.get(i).get(1), intervals.get(i).get(2), i);
        }
        Arrays.sort(ivs, (a, b) -> Integer.compare(a.r, b.r));

        State[] prevDp = new State[n];
        State ans = new State(-1, null);

        for (int k = 1; k <= 4; k++) {
            State[] currDp = new State[n];
            for (int i = 0; i < n; i++) {
                long resScore = -1;
                int[] resIdx = null;
                if (i > 0) {
                    resScore = currDp[i - 1].score;
                    resIdx = currDp[i - 1].idx;
                }

                int j = -1, low = 0, high = i - 1;
                while (low <= high) {
                    int mid = low + (high - low) / 2;
                    if (ivs[mid].r < ivs[i].l) { j = mid; low = mid + 1; }
                    else high = mid - 1;
                }

                long candScore = -1;
                int[] candIdx = null;
                if (k == 1) {
                    candScore = ivs[i].w;
                    candIdx = new int[]{ivs[i].id};
                } else if (j != -1 && prevDp[j].score != -1) {
                    candScore = prevDp[j].score + ivs[i].w;
                    candIdx = new int[k];
                    System.arraycopy(prevDp[j].idx, 0, candIdx, 0, k - 1);
                    candIdx[k - 1] = ivs[i].id;
                    Arrays.sort(candIdx);
                }

                if (isBetter(candScore, candIdx, resScore, resIdx)) {
                    currDp[i] = new State(candScore, candIdx);
                } else {
                    currDp[i] = new State(resScore, resIdx);
                }
            }
            if (isBetter(currDp[n - 1].score, currDp[n - 1].idx, ans.score, ans.idx)) ans = currDp[n - 1];
            prevDp = currDp;
        }
        return ans.idx;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
import bisect

class Solution(object):
    def maximumWeight(self, intervals):
        n = len(intervals)
        ivs = []
        for i in range(n):
            ivs.append(intervals[i] + [i])
        ivs.sort(key=lambda x: x[1])

        ends = [x[1] for x in ivs]
        prev_dp = [(-1, []) for _ in range(n)]

        ans_score = -1
        ans_indices = []

        for k in range(1, 5):
            curr_dp = [None] * n
            for i in range(n):
                res_score, res_indices = (-1, [])
                if i > 0:
                    res_score, res_indices = curr_dp[i-1]

                j = bisect.bisect_left(ends, ivs[i][0]) - 1

                cand_score = -1
                cand_indices = []
                if k == 1:
                    cand_score = ivs[i][2]
                    cand_indices = [ivs[i][3]]
                else:
                    if j >= 0 and prev_dp[j][0] != -1:
                        cand_score = prev_dp[j][0] + ivs[i][2]
                        cand_indices = sorted(prev_dp[j][1] + [ivs[i][3]])

                if cand_score > res_score:
                    res_score, res_indices = cand_score, cand_indices
                elif cand_score == res_score and cand_score != -1:
                    if not res_indices or cand_indices < res_indices:
                        res_indices = cand_indices

                curr_dp[i] = (res_score, res_indices)

            best_k_score, best_k_indices = curr_dp[n-1]
            if best_k_score > ans_score:
                ans_score, ans_indices = best_k_score, best_k_indices
            elif best_k_score == ans_score and best_k_score != -1:
                if not ans_indices or best_k_indices < ans_indices:
                    ans_indices = best_k_indices
            prev_dp = curr_dp

        return ans_indices
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
import bisect

class Solution:
    def maximumWeight(self, intervals: list[list[int]]) -> list[int]:
        n = len(intervals)
        ivs = []
        for i in range(n):
            ivs.append((intervals[i][0], intervals[i][1], intervals[i][2], i))

        ivs.sort(key=lambda x: x[1])
        r_values = [x[1] for x in ivs]

        dp = [[(0, []) for _ in range(n + 1)]]
        for k in range(1, 5):
            dp.append([(-1, []) for _ in range(n + 1)])

        def is_better(s1, idx1, s2, idx2):
            if s1 > s2: return True
            if s1 < s2: return False
            if not idx1: return False
            if not idx2: return True
            n1, n2 = len(idx1), len(idx2)
            for i in range(min(n1, n2)):
                if idx1[i] < idx2[i]: return True
                if idx1[i] > idx2[i]: return False
            return n1 < n2

        for k in range(1, 5):
            for i in range(1, n + 1):
                dp[k][i] = dp[k][i-1]

                l, r, w, idx = ivs[i-1]
                prev_idx = bisect.bisect_left(r_values, l)

                if dp[k-1][prev_idx][0] != -1:
                    new_score = dp[k-1][prev_idx][0] + w
                    new_indices = sorted(dp[k-1][prev_idx][1] + [idx])
                    if is_better(new_score, new_indices, dp[k][i][0], dp[k][i][1]):
                        dp[k][i] = (new_score, new_indices)

        best_score, best_indices = -1, []
        for k in range(1, 5):
            if is_better(dp[k][n][0], dp[k][n][1], best_score, best_indices):
                best_score, best_indices = dp[k][n]

        return best_indices
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct {
    int l, r, w, id;
} Interval;

typedef struct {
    long long score;
    int indices[4];
    int count;
} Result;

int compareIntervals(const void* a, const void* b) {
    Interval* i1 = (Interval*)a;
    Interval* i2 = (Interval*)b;
    if (i1->r != i2->r) return i1->r - i2->r;
    return i1->l - i2->l;
}

bool is_better(Result* a, Result* b) {
    if (a->score > b->score) return true;
    if (a->score < b->score) return false;
    if (a->count == 0) return false;
    if (b->count == 0) return true;
    int min_c = a->count < b->count ? a->count : b->count;
    for (int i = 0; i < min_c; i++) {
        if (a->indices[i] < b->indices[i]) return true;
        if (a->indices[i] > b->indices[i]) return false;
    }
    return a->count < b->count;
}

void combine(Result* dest, Result* src, long long new_score, int new_idx) {
    dest->score = new_score;
    int i = 0, j = 0;
    bool added = false;
    while (j < src->count) {
        if (!added && new_idx < src->indices[j]) {
            dest->indices[i++] = new_idx;
            added = true;
        }
        dest->indices[i++] = src->indices[j++];
    }
    if (!added) dest->indices[i++] = new_idx;
    dest->count = src->count + 1;
}

int* maximumWeight(int** intervals, int intervalsSize, int* intervalsColSize, int* returnSize) {
    Interval* ivs = (Interval*)malloc(intervalsSize * sizeof(Interval));
    for (int i = 0; i < intervalsSize; i++) {
        ivs[i].l = intervals[i][0];
        ivs[i].r = intervals[i][1];
        ivs[i].w = intervals[i][2];
        ivs[i].id = i;
    }
    qsort(ivs, intervalsSize, sizeof(Interval), compareIntervals);

    Result* dp = (Result*)malloc(5 * (intervalsSize + 1) * sizeof(Result));
    for (int k = 0; k < 5; k++) {
        for (int i = 0; i <= intervalsSize; i++) {
            dp[k * (intervalsSize + 1) + i].score = -1;
            dp[k * (intervalsSize + 1) + i].count = 0;
        }
    }
    for (int i = 0; i <= intervalsSize; i++) dp[i].score = 0;

    for (int k = 1; k <= 4; k++) {
        for (int i = 1; i <= intervalsSize; i++) {
            dp[k * (intervalsSize + 1) + i] = dp[k * (intervalsSize + 1) + i - 1];

            int target_l = ivs[i-1].l;
            int low = 0, high = i - 2, prev_idx = -1;
            while (low <= high) {
                int mid = low + (high - low) / 2;
                if (ivs[mid].r < target_l) {
                    prev_idx = mid;
                    low = mid + 1;
                } else {
                    high = mid - 1;
                }
            }
            int idx = prev_idx + 1;
            if (dp[(k-1) * (intervalsSize + 1) + idx].score != -1) {
                Result temp;
                combine(&temp, &dp[(k-1) * (intervalsSize + 1) + idx], dp[(k-1) * (intervalsSize + 1) + idx].score + ivs[i-1].w, ivs[i-1].id);
                if (is_better(&temp, &dp[k * (intervalsSize + 1) + i])) {
                    dp[k * (intervalsSize + 1) + i] = temp;
                }
            }
        }
    }

    Result best = { -1, {0, 0, 0, 0}, 0 };
    for (int k = 1; k <= 4; k++) {
        if (is_better(&dp[k * (intervalsSize + 1) + intervalsSize], &best)) {
            best = dp[k * (intervalsSize + 1) + intervalsSize];
        }
    }

    *returnSize = best.count;
    int* res = (int*)malloc(best.count * sizeof(int));
    for (int i = 0; i < best.count; i++) res[i] = best.indices[i];

    free(ivs);
    free(dp);
    return res;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    struct Interval {
        public int l, r, w, id;
    }

    struct Result {
        public long score;
        public int[] indices;
        public int count;

        public Result(long s, int[] i, int c) {
            score = s;
            indices = i;
            count = c;
        }
    }

    private bool IsBetter(long s1, int c1, int[] i1, long s2, int c2, int[] i2) {
        if (s1 > s2) return true;
        if (s1 < s2) return false;
        if (c1 == 0) return false;
        if (c2 == 0) return true;
        int minC = Math.Min(c1, c2);
        for (int i = 0; i < minC; i++) {
            if (i1[i] < i2[i]) return true;
            if (i1[i] > i2[i]) return false;
        }
        return c1 < c2;
    }

    public int[] MaximumWeight(IList<IList<int>> intervals) {
        int n = intervals.Count;
        Interval[] ivs = new Interval[n];
        for (int i = 0; i < n; i++) {
            ivs[i] = new Interval { l = intervals[i][0], r = intervals[i][1], w = intervals[i][2], id = i };
        }
        Array.Sort(ivs, (a, b) => a.r.CompareTo(b.r));

        int[] rValues = ivs.Select(x => x.r).ToArray();
        Result[,] dp = new Result[5, n + 1];

        for (int k = 0; k < 5; k++) {
            for (int i = 0; i <= n; i++) {
                dp[k, i] = new Result(-1, new int[0], 0);
            }
        }
        for (int i = 0; i <= n; i++) dp[0, i] = new Result(0, new int[0], 0);

        for (int k = 1; k <= 4; k++) {
            for (int i = 1; i <= n; i++) {
                dp[k, i] = dp[k, i - 1];

                int targetL = ivs[i - 1].l;
                int idx = Array.BinarySearch(rValues, 0, i - 1, targetL);
                if (idx < 0) idx = ~idx;
                else {
                    while (idx > 0 && rValues[idx - 1] == targetL) idx--;
                }
                // Array.BinarySearch idx is where targetL would be. We need r < targetL.
                // The number of elements with r < targetL is the count 'idx'.

                if (dp[k - 1, idx].score != -1) {
                    long newScore = dp[k - 1, idx].score + ivs[i - 1].w;
                    int[] newIndices = new int[k];
                    int p = 0;
                    bool added = false;
                    for (int j = 0; j < dp[k - 1, idx].count; j++) {
                        if (!added && ivs[i - 1].id < dp[k - 1, idx].indices[j]) {
                            newIndices[p++] = ivs[i - 1].id;
                            added = true;
                        }
                        newIndices[p++] = dp[k - 1, idx].indices[j];
                    }
                    if (!added) newIndices[p++] = ivs[i - 1].id;

                    if (IsBetter(newScore, k, newIndices, dp[k, i].score, dp[k, i].count, dp[k, i].indices)) {
                        dp[k, i] = new Result(newScore, newIndices, k);
                    }
                }
            }
        }

        Result best = new Result(-1, new int[0], 0);
        for (int k = 1; k <= 4; k++) {
            if (IsBetter(dp[k, n].score, dp[k, n].count, dp[k, n].indices, best.score, best.count, best.indices)) {
                best = dp[k, n];
            }
        }

        return best.indices;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[][]} intervals
 * @return {number[]}
 */
var maximumWeight = function(intervals) {
    const n = intervals.length;
    const ivs = intervals.map((v, i) => [v[0], v[1], v[2], i]);
    ivs.sort((a, b) => a[1] - b[1]);

    const rValues = ivs.map(x => x[1]);
    const scores = new Float64Array(5 * (n + 1)).fill(-1);
    const counts = new Int8Array(5 * (n + 1)).fill(0);
    const indices = new Int32Array(5 * (n + 1) * 4).fill(0);

    for (let i = 0; i <= n; i++) {
        scores[i] = 0;
    }

    function isBetter(s1, c1, idx1, s2, c2, idx2) {
        if (s1 > s2) return true;
        if (s1 < s2) return false;
        if (c1 === 0) return false;
        if (c2 === 0) return true;
        const minC = Math.min(c1, c2);
        for (let i = 0; i < minC; i++) {
            if (idx1[i] < idx2[i]) return true;
            if (idx1[i] > idx2[i]) return false;
        }
        return c1 < c2;
    }

    for (let k = 1; k <= 4; k++) {
        for (let i = 1; i <= n; i++) {
            const curr = k * (n + 1) + i;
            const prevInRow = k * (n + 1) + i - 1;

            // Copy prev in row
            scores[curr] = scores[prevInRow];
            counts[curr] = counts[prevInRow];
            let target = curr * 4;
            let source = prevInRow * 4;
            for (let j = 0; j < counts[prevInRow]; j++) indices[target + j] = indices[source + j];

            let low = 0, high = i - 2, prevIdx = -1;
            const targetL = ivs[i - 1][0];
            while (low <= high) {
                let mid = (low + high) >> 1;
                if (rValues[mid] < targetL) {
                    prevIdx = mid;
                    low = mid + 1;
                } else {
                    high = mid - 1;
                }
            }

            const prevCol = (k - 1) * (n + 1) + (prevIdx + 1);
            if (scores[prevCol] !== -1) {
                const newScore = scores[prevCol] + ivs[i - 1][2];
                const newCount = counts[prevCol] + 1;
                const tempIdx = new Int32Array(4);
                let p = 0, added = false;
                const prevIdxs = indices.subarray(prevCol * 4, prevCol * 4 + counts[prevCol]);
                for (let j = 0; j < counts[prevCol]; j++) {
                    if (!added && ivs[i - 1][3] < prevIdxs[j]) {
                        tempIdx[p++] = ivs[i - 1][3];
                        added = true;
                    }
                    tempIdx[p++] = prevIdxs[j];
                }
                if (!added) tempIdx[p++] = ivs[i - 1][3];

                if (isBetter(newScore, newCount, tempIdx, scores[curr], counts[curr], indices.subarray(curr * 4, curr * 4 + counts[curr]))) {
                    scores[curr] = newScore;
                    counts[curr] = newCount;
                    for (let j = 0; j < newCount; j++) indices[curr * 4 + j] = tempIdx[j];
                }
            }
        }
    }

    let bestScore = -1, bestK = -1;
    for (let k = 1; k <= 4; k++) {
        const idx = k * (n + 1) + n;
        if (isBetter(scores[idx], counts[idx], indices.subarray(idx * 4, idx * 4 + counts[idx]), bestScore, bestK === -1 ? 0 : counts[bestK * (n + 1) + n], bestK === -1 ? [] : indices.subarray((bestK * (n + 1) + n) * 4))) {
            bestScore = scores[idx];
            bestK = k;
        }
    }

    const finalIdx = bestK * (n + 1) + n;
    return Array.from(indices.subarray(finalIdx * 4, finalIdx * 4 + counts[finalIdx]));
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
class State {
  weight: number;
  indices: number[];
  constructor(weight: number, indices: number[]) {
    this.weight = weight;
    this.indices = indices;
  }
}

function maximumWeight(intervals: number[][]): number[] {
  const n = intervals.length;
  const sortedIntervals = intervals.map((val, idx) => ({
    l: val[0],
    r: val[1],
    w: val[2],
    id: idx
  })).sort((a, b) => a.r - b.r);

  function findLastEndingBefore(targetL: number): number {
    let low = 0;
    let high = n - 1;
    let ans = -1;
    while (low <= high) {
      const mid = (low + high) >>> 1;
      if (sortedIntervals[mid].r < targetL) {
        ans = mid;
        low = mid + 1;
      } else {
        high = mid - 1;
      }
    }
    return ans;
  }

  function isBetter(w1: number, idx1: number[], w2: number, idx2: number[]): boolean {
    if (w1 !== w2) return w1 > w2;
    const len1 = idx1.length;
    const len2 = idx2.length;
    const minLen = Math.min(len1, len2);
    for (let i = 0; i < minLen; i++) {
      if (idx1[i] !== idx2[i]) return idx1[i] < idx2[i];
    }
    return len1 < len2;
  }

  const dp: (State | null)[][] = Array.from({ length: 5 }, () => Array(n + 1).fill(null));
  for (let i = 0; i <= n; i++) {
    dp[0][i] = new State(0, []);
  }

  for (let k = 1; k <= 4; k++) {
    for (let i = 1; i <= n; i++) {
      dp[k][i] = dp[k][i - 1];
      const j = findLastEndingBefore(sortedIntervals[i - 1].l);
      const prev = dp[k - 1][j + 1];
      if (prev !== null) {
        const currentWeight = prev.weight + sortedIntervals[i - 1].w;
        const currentIndices = [...prev.indices, sortedIntervals[i - 1].id].sort((a, b) => a - b);
        if (dp[k][i] === null || isBetter(currentWeight, currentIndices, dp[k][i]!.weight, dp[k][i]!.indices)) {
          dp[k][i] = new State(currentWeight, currentIndices);
        }
      }
    }
  }

  let bestState: State = new State(0, []);
  for (let k = 1; k <= 4; k++) {
    if (dp[k][n] !== null && isBetter(dp[k][n]!.weight, dp[k][n]!.indices, bestState.weight, bestState.indices)) {
      bestState = dp[k][n]!;
    }
  }

  return bestState.indices;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class State {
    public $weight;
    public $indices;
    public function __construct($w, $idx) {
        $this->weight = $w;
        $this->indices = $idx;
    }
}

class Solution {
    /**
     * @param Integer[][] $intervals
     * @return Integer[]
     */
    function maximumWeight($intervals) {
        $n = count($intervals);
        $mappedIntervals = [];
        for ($i = 0; $i < $n; $i++) {
            $mappedIntervals[] = [
                'l' => $intervals[$i][0],
                'r' => $intervals[$i][1],
                'w' => $intervals[$i][2],
                'id' => $i
            ];
        }
        usort($mappedIntervals, function($a, $b) {
            return $a['r'] <=> $b['r'];
        });

        $dp = array_fill(0, 5, array_fill(0, $n + 1, null));
        for ($i = 0; $i <= $n; $i++) {
            $dp[0][$i] = new State(0, []);
        }

        for ($k = 1; $k <= 4; $k++) {
            for ($i = 1; $i <= $n; $i++) {
                $dp[$k][$i] = $dp[$k][$i - 1];

                $targetL = $mappedIntervals[$i - 1]['l'];
                $low = 0;
                $high = $n - 1;
                $idx = -1;
                while ($low <= $high) {
                    $mid = ($low + $high) >> 1;
                    if ($mappedIntervals[$mid]['r'] < $targetL) {
                        $idx = $mid;
                        $low = $mid + 1;
                    } else {
                        $high = $mid - 1;
                    }
                }

                $prev = $dp[$k - 1][$idx + 1];
                if ($prev !== null) {
                    $currentWeight = $prev->weight + $mappedIntervals[$i - 1]['w'];
                    $currentIndices = $prev->indices;
                    $currentIndices[] = $mappedIntervals[$i - 1]['id'];
                    sort($currentIndices, SORT_NUMERIC);

                    if ($dp[$k][$i] === null || 
                        $currentWeight > $dp[$k][$i]->weight || 
                        ($currentWeight === $dp[$k][$i]->weight && $currentIndices < $dp[$k][$i]->indices)) {
                        $dp[$k][$i] = new State($currentWeight, $currentIndices);
                    }
                }
            }
        }

        $bestState = new State(0, []);
        for ($k = 1; $k <= 4; $k++) {
            if ($dp[$k][$n] !== null) {
                if ($dp[$k][$n]->weight > $bestState->weight || 
                   ($dp[$k][$n]->weight === $bestState->weight && (empty($bestState->indices) || $dp[$k][$n]->indices < $bestState->indices))) {
                    $bestState = $dp[$k][$n];
                }
            }
        }

        return $bestState->indices;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    struct State {
        let weight: Int
        let indices: [Int]
    }

    struct Interval {
        let l: Int
        let r: Int
        let w: Int
        let id: Int
    }

    func maximumWeight(_ intervals: [[Int]]) -> [Int] {
        let n = intervals.count
        var sortedIntervals: [Interval] = []
        for i in 0..<n {
            sortedIntervals.append(Interval(l: intervals[i][0], r: intervals[i][1], w: intervals[i][2], id: i))
        }
        sortedIntervals.sort { $0.r < $1.r }

        var dp: [[State?]] = Array(repeating: Array(repeating: nil, count: n + 1), count: 5)
        for i in 0...n {
            dp[0][i] = State(weight: 0, indices: [])
        }

        for k in 1...4 {
            for i in 1...n {
                dp[k][i] = dp[k][i - 1]

                let targetL = sortedIntervals[i - 1].l
                var low = 0
                var high = i - 2
                var idx = -1
                while low <= high {
                    let mid = (low + high) / 2
                    if sortedIntervals[mid].r < targetL {
                        idx = mid
                        low = mid + 1
                    } else {
                        high = mid - 1
                    }
                }

                if let prev = dp[k - 1][idx + 1] {
                    let currentWeight = prev.weight + sortedIntervals[i - 1].w
                    var currentIndices = prev.indices
                    currentIndices.append(sortedIntervals[i - 1].id)
                    currentIndices.sort()

                    if dp[k][i] == nil || 
                       currentWeight > dp[k][i]!.weight || 
                       (currentWeight == dp[k][i]!.weight && currentIndices.lexicographicallyPrecedes(dp[k][i]!.indices)) {
                        dp[k][i] = State(weight: currentWeight, indices: currentIndices)
                    }
                }
            }
        }

        var bestState: State = State(weight: 0, indices: [])
        for k in 1...4 {
            if let current = dp[k][n] {
                if current.weight > bestState.weight || 
                   (current.weight == bestState.weight && (bestState.indices.isEmpty || current.indices.lexicographicallyPrecedes(bestState.indices))) {
                    bestState = current
                }
            }
        }

        return bestState.indices
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    class Interval(val l: Int, val r: Int, val weight: Long, val id: Int)
    class State(val weight: Long, val indices: IntArray)

    fun maximumWeight(intervals: List<List<Int>>): IntArray {
        val n = intervals.size
        val sortedIntervals = Array(n) { i ->
            Interval(intervals[i][0], intervals[i][1], intervals[i][2].toLong(), i)
        }
        sortedIntervals.sortBy { it.r }

        val dp = Array(5) { arrayOfNulls<State>(n + 1) }
        for (i in 0..n) {
            dp[0][i] = State(0L, intArrayOf())
        }

        fun isBetter(w1: Long, idx1: IntArray, w2: Long, idx2: IntArray): Boolean {
            if (w1 != w2) return w1 > w2
            val n1 = idx1.size
            val n2 = idx2.size
            val minLen = if (n1 < n2) n1 else n2
            for (i in 0 until minLen) {
                if (idx1[i] < idx2[i]) return true
                if (idx1[i] > idx2[i]) return false
            }
            return n1 < n2
        }

        for (k in 1..4) {
            for (i in 1..n) {
                dp[k][i] = dp[k][i - 1]

                val targetL = sortedIntervals[i - 1].l
                var low = 0
                var high = n - 1
                var lastIdx = -1
                while (low <= high) {
                    val mid = (low + high) ushr 1
                    if (sortedIntervals[mid].r < targetL) {
                        lastIdx = mid
                        low = mid + 1
                    } else {
                        high = mid - 1
                    }
                }

                val prev = dp[k - 1][lastIdx + 1]
                if (prev != null) {
                    val currentWeight = prev.weight + sortedIntervals[i - 1].weight
                    val currentIndices = IntArray(prev.indices.size + 1)
                    System.arraycopy(prev.indices, 0, currentIndices, 0, prev.indices.size)
                    currentIndices[prev.indices.size] = sortedIntervals[i - 1].id
                    currentIndices.sort()

                    if (dp[k][i] == null || isBetter(currentWeight, currentIndices, dp[k][i]!!.weight, dp[k][i]!!.indices)) {
                        dp[k][i] = State(currentWeight, currentIndices)
                    }
                }
            }
        }

        var bestState: State? = null
        for (k in 1..4) {
            val current = dp[k][n]
            if (current != null) {
                if (bestState == null || isBetter(current.weight, current.indices, bestState.weight, bestState.indices)) {
                    bestState = current
                }
            }
        }

        return bestState?.indices ?: intArrayOf()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Interval {
  final int l, r, weight, id;
  Interval(this.l, this.r, this.weight, this.id);
}

class State {
  final int weight;
  final List<int> indices;
  State(this.weight, this.indices);
}

class Solution {
  List<int> maximumWeight(List<List<int>> intervals) {
    int n = intervals.length;
    List<Interval> sorted = [];
    for (int i = 0; i < n; i++) {
      sorted.add(Interval(intervals[i][0], intervals[i][1], intervals[i][2], i));
    }
    sorted.sort((a, b) => a.r.compareTo(b.r));

    List<List<State>> dp = List.generate(5, (_) => List.generate(n + 1, (_) => State(-1, [])));

    for (int j = 0; j <= n; j++) {
      dp[0][j] = State(0, []);
    }

    for (int k = 1; k <= 4; k++) {
      for (int i = 1; i <= n; i++) {
        Interval curr = sorted[i - 1];
        // Option 1: Don't include sorted[i-1]
        State best = dp[k][i - 1];

        // Option 2: Include sorted[i-1]
        int prevIdx = findPrev(sorted, curr.l);
        if (dp[k - 1][prevIdx + 1].weight != -1) {
          int newWeight = dp[k - 1][prevIdx + 1].weight + curr.weight;
          List<int> newIndices = List<int>.from(dp[k - 1][prevIdx + 1].indices)..add(curr.id);
          newIndices.sort();
          if (isBetter(newWeight, newIndices, best.weight, best.indices)) {
            best = State(newWeight, newIndices);
          }
        }
        dp[k][i] = best;
      }
    }

    State finalBest = State(-1, []);
    for (int k = 1; k <= 4; k++) {
      if (isBetter(dp[k][n].weight, dp[k][n].indices, finalBest.weight, finalBest.indices)) {
        finalBest = dp[k][n];
      }
    }
    return finalBest.indices;
  }

  int findPrev(List<Interval> sorted, int targetL) {
    int low = 0, high = sorted.length - 1, ans = -1;
    while (low <= high) {
      int mid = low + (high - low) ~/ 2;
      if (sorted[mid].r < targetL) {
        ans = mid;
        low = mid + 1;
      } else {
        high = mid - 1;
      }
    }
    return ans;
  }

  bool isBetter(int w1, List<int> idx1, int w2, List<int> idx2) {
    if (w1 != w2) return w1 > w2;
    if (w1 == -1) return false;
    int n1 = idx1.length, n2 = idx2.length;
    int minLen = n1 < n2 ? n1 : n2;
    for (int i = 0; i < minLen; i++) {
      if (idx1[i] < idx2[i]) return true;
      if (idx1[i] > idx2[i]) return false;
    }
    return n1 < n2;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func maximumWeight(intervals [][]int) []int {
	n := len(intervals)
	type Interval struct {
		l, r, id int
		w        int64
	}
	sorted := make([]Interval, n)
	for i := 0; i < n; i++ {
		sorted[i] = Interval{intervals[i][0], intervals[i][1], i, int64(intervals[i][2])}
	}
	import "sort"
	sort.Slice(sorted, func(i, j int) bool {
		return sorted[i].r < sorted[j].r
	})

	type State struct {
		weight  int64
		indices []int
	}

	isBetter := func(w1 int64, idx1 []int, w2 int64, idx2 []int) bool {
		if w1 != w2 {
			return w1 > w2
		}
		if w1 == -1 {
			return false
		}
		n1, n2 := len(idx1), len(idx2)
		limit := n1
		if n2 < limit {
			limit = n2
		}
		for i := 0; i < limit; i++ {
			if idx1[i] < idx2[i] {
				return true
			}
			if idx1[i] > idx2[i] {
				return false
			}
		}
		return n1 < n2
	}

	dp := make([][]State, 5)
	for k := 0; k < 5; k++ {
		dp[k] = make([]State, n+1)
		for i := 0; i <= n; i++ {
			dp[k][i] = State{weight: -1}
		}
	}
	for i := 0; i <= n; i++ {
		dp[0][i] = State{weight: 0, indices: []int{}}
	}

	for k := 1; k <= 4; k++ {
		for i := 1; i <= n; i++ {
			curr := sorted[i-1]
			bestWeight := dp[k][i-1].weight
			bestIndices := dp[k][i-1].indices

			targetL := curr.l
			prevIdx := sort.Search(i, func(j int) bool {
				return sorted[j].r >= targetL
			}) - 1

			if dp[k-1][prevIdx+1].weight != -1 {
				newWeight := dp[k-1][prevIdx+1].weight + curr.w
				newIndices := make([]int, len(dp[k-1][prevIdx+1].indices), len(dp[k-1][prevIdx+1].indices)+1)
				copy(newIndices, dp[k-1][prevIdx+1].indices)
				newIndices = append(newIndices, curr.id)
				sort.Ints(newIndices)

				if isBetter(newWeight, newIndices, bestWeight, bestIndices) {
					bestWeight = newWeight
					bestIndices = newIndices
				}
			}
			dp[k][i] = State{bestWeight, bestIndices}
		}
	}

	var finalW int64 = -1
	var finalIdx []int
	for k := 1; k <= 4; k++ {
		if isBetter(dp[k][n].weight, dp[k][n].indices, finalW, finalIdx) {
			finalW = dp[k][n].weight
			finalIdx = dp[k][n].indices
		}
	}
	return finalIdx
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def maximum_weight(intervals)
  n = intervals.length
  interval_struct = Struct.new(:l, :r, :w, :id)
  sorted = intervals.each_with_index.map { |(l, r, w), i| interval_struct.new(l, r, w, i) }.sort_by(&:r)

  state_struct = Struct.new(:weight, :indices)
  dp = Array.new(5) { Array.new(n + 1) { state_struct.new(-1, []) } }
  (0..n).each { |i| dp[0][i] = state_struct.new(0, []) }

  def compare(w1, ids1, w2, ids2)
    return false if w1 == -1
    return true if w2 == -1
    return true if w1 > w2
    return false if w1 < w2
    (ids1 <=> ids2) == -1
  end

  (1..4).each do |k|
    (1..n).each do |i|
      curr = sorted[i - 1]
      best_weight = dp[k][i - 1].weight
      best_indices = dp[k][i - 1].indices

      idx = sorted.bsearch_index { |x| x.r >= curr.l }
      prev_idx = idx ? idx - 1 : n - 1

      if dp[k - 1][prev_idx + 1].weight != -1
        new_weight = dp[k - 1][prev_idx + 1].weight + curr.w
        new_indices = (dp[k - 1][prev_idx + 1].indices + [curr.id]).sort
        if compare(new_weight, new_indices, best_weight, best_indices)
          best_weight = new_weight
          best_indices = new_indices
        end
      end
      dp[k][i] = state_struct.new(best_weight, best_indices)
    end
  end

  final_best = state_struct.new(-1, [])
  (1..4).each do |k|
    if compare(dp[k][n].weight, dp[k][n].indices, final_best.weight, final_best.indices)
      final_best = dp[k][n]
    end
  end
  final_best.indices
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    case class Interval(l: Int, r: Int, w: Long, id: Int)
    case class State(weight: Long, indices: Array[Int])

    def maximumWeight(intervals: List[List[Int]]): Array[Int] = {
        val n = intervals.length
        val sorted = intervals.zipWithIndex.map { case (list, idx) =>
            Interval(list(0), list(1), list(2).toLong, idx)
        }.toArray.sortBy(_.r)

        val dp = Array.fill(5, n + 1)(State(-1L, Array.empty[Int]))
        for (i <- 0 to n) dp(0)(i) = State(0L, Array.empty[Int])

        def isBetter(w1: Long, idx1: Array[Int], w2: Long, idx2: Array[Int]): Boolean = {
            if (w1 != w2) return w1 > w2
            if (w1 == -1L) return false
            val n1 = idx1.length
            val n2 = idx2.length
            var i = 0
            val minLen = if (n1 < n2) n1 else n2
            while (i < minLen) {
                if (idx1(i) < idx2(i)) return true
                if (idx1(i) > idx2(i)) return false
                i += 1
            }
            n1 < n2
        }

        def findPrev(arr: Array[Interval], targetL: Int): Int = {
            var low = 0
            var high = arr.length - 1
            var ans = -1
            while (low <= high) {
                val mid = low + (high - low) / 2
                if (arr(mid).r < targetL) {
                    ans = mid
                    low = mid + 1
                } else {
                    high = mid - 1
                }
            }
            ans
        }

        for (k <- 1 to 4) {
            for (i <- 1 to n) {
                val curr = sorted(i - 1)
                var bestWeight = dp(k)(i - 1).weight
                var bestIndices = dp(k)(i - 1).indices

                val prevIdx = findPrev(sorted.take(i), curr.l)
                if (dp(k - 1)(prevIdx + 1).weight != -1L) {
                    val newWeight = dp(k - 1)(prevIdx + 1).weight + curr.w
                    val newIndices = (dp(k - 1)(prevIdx + 1).indices :+ curr.id).sorted
                    if (isBetter(newWeight, newIndices, bestWeight, bestIndices)) {
                        bestWeight = newWeight
                        bestIndices = newIndices
                    }
                }
                dp(k)(i) = State(bestWeight, bestIndices)
            }
        }

        var finalW = -1L
        var finalIdx = Array.empty[Int]
        for (k <- 1 to 4) {
            if (isBetter(dp(k)(n).weight, dp(k)(n).indices, finalW, finalIdx)) {
                finalW = dp(k)(n).weight
                finalIdx = dp(k)(n).indices
            }
        }
        finalIdx
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn maximum_weight(intervals: Vec<Vec<i32>>) -> Vec<i32> {
        let n = intervals.len();
        struct Interval {
            l: i32,
            r: i32,
            w: i32,
            id: i32,
        }
        let mut sorted: Vec<_> = intervals.into_iter().enumerate().map(|(i, v)| {
            Interval { l: v[0], r: v[1], w: v[2], id: i as i32 }
        }).collect();
        sorted.sort_unstable_by(|a, b| a.r.cmp(&b.r).then(a.l.cmp(&b.l)).then(a.w.cmp(&b.w)).then(a.id.cmp(&b.id)));

        let mut dp = vec![(0i64, vec![]); n + 1];
        let mut overall_best = (0i64, vec![]);

        for _k in 1..=4 {
            let mut next_dp = vec![(0i64, vec![]); n + 1];
            for i in 1..=n {
                let interval = &sorted[i - 1];
                let mut low = 0;
                let mut high = i - 1;
                while low < high {
                    let mid = low + (high - low) / 2;
                    if sorted[mid].r < interval.l {
                        low = mid + 1;
                    } else {
                        high = mid;
                    }
                }
                let prev_idx = low;

                let mut pick_i_indices = dp[prev_idx].1.clone();
                pick_i_indices.push(interval.id);
                pick_i_indices.sort_unstable();
                let pick_i_weight = dp[prev_idx].0 + interval.w as i64;
                let pick_i = (pick_i_weight, pick_i_indices);

                let option1 = &next_dp[i - 1];
                if is_better(pick_i.0, &pick_i.1, option1.0, &option1.1) {
                    next_dp[i] = pick_i;
                } else {
                    next_dp[i] = option1.clone();
                }
            }
            dp = next_dp;
            if is_better(dp[n].0, &dp[n].1, overall_best.0, &overall_best.1) {
                overall_best = dp[n].clone();
            }
        }
        overall_best.1
    }
}

fn is_better(w1: i64, idx1: &[i32], w2: i64, idx2: &[i32]) -> bool {
    if w1 != w2 {
        return w1 > w2;
    }
    if idx1.is_empty() && !idx2.is_empty() { return false; }
    if !idx1.is_empty() && idx2.is_empty() { return true; }
    idx1 < idx2
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (maximum-weight intervals)
  (-> (listof (listof exact-integer?)) (listof exact-integer?))
  (let* ([n (length intervals)]
         [intervals-list
          (sort
           (for/list ([inter (in-list intervals)] [i (in-naturals)])
             (list (first inter) (second inter) (third inter) i))
           (lambda (a b)
             (if (not (= (second a) (second b)))
                 (< (second a) (second b))
                 (if (not (= (first a) (first b)))
                     (< (first a) (first b))
                     (if (not (= (third a) (third b)))
                         (< (third a) (third b))
                         (< (fourth a) (fourth b)))))))]
         [sorted-intervals (list->vector intervals-list)])

    (define (find-prev target-l)
      (let loop ([low 0] [high (vector-length sorted-intervals)])
        (if (< low high)
            (let* ([mid (quotient (+ low high) 2)]
                   [r (second (vector-ref sorted-intervals mid))])
              (if (< r target-l)
                  (loop (+ mid 1) high)
                  (loop low mid)))
            low)))

    (define (lex-less? l1 l2)
      (cond
        [(null? l1) (not (null? l2))]
        [(null? l2) #f]
        [(< (car l1) (car l2)) #t]
        [(> (car l1) (car l2)) #f]
        [else (lex-less? (cdr l1) (cdr l2))]))

    (define (is-better? s1 s2)
      (if (> (car s1) (car s2)) #t
          (if (< (car s1) (car s2)) #f
              (lex-less? (cdr s1) (cdr s2)))))

    (define dp (make-vector (+ n 1) '(0 . ())))
    (define overall-best '(0 . ()))

    (for ([k (in-range 1 5)])
      (define next-dp (make-vector (+ n 1)))
      (vector-set! next-dp 0 '(0 . ()))
      (for ([i (in-range 1 (+ n 1))])
        (let* ([interval (vector-ref sorted-intervals (- i 1))]
               [l (first interval)]
               [w (third interval)]
               [id (fourth interval)]
               [prev-idx (find-prev l)]
               [option1 (vector-ref next-dp (- i 1))]
               [prev-state (vector-ref dp prev-idx)]
               [option2 (cons (+ (car prev-state) w)
                              (sort (cons id (cdr prev-state)) <))])
          (vector-set! next-dp i (if (is-better? option2 option1) option2 option1))))
      (set! dp next-dp)
      (if (is-better? (vector-ref dp n) overall-best)
          (set! overall-best (vector-ref dp n))
          #t))
    (cdr overall-best)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec maximum_weight(Intervals :: [[integer()]]) -> [integer()].
maximum_weight(Intervals) ->
  N = length(Intervals),
  IntervalsWithId = lists:zipwith(fun([L, R, W], Id) -> {L, R, W, Id} end, Intervals, lists:seq(0, N - 1)),
  SortedIntervals = lists:sort(fun({L1, R1, W1, Id1}, {L2, R2, W2, Id2}) ->
                                  if R1 /= R2 -> R1 < R2;
                                     L1 /= L2 -> L1 < L2;
                                     W1 /= W2 -> W1 < W2;
                                     true -> Id1 < Id2
                                  end
                               end, IntervalsWithId),
  IntervalsTuple = list_to_tuple(SortedIntervals),
  InitialDP = lists:duplicate(N + 1, {0, []}),
  FinalBest = solve_dp(1, IntervalsTuple, InitialDP, {0, []}),
  element(2, FinalBest).

solve_dp(K, _Intervals, DP, BestOverall) when K > 4 -> BestOverall;
solve_dp(K, Intervals, DP, BestOverall) ->
  PrevDP = list_to_tuple(DP),
  N = tuple_size(Intervals),
  NewDPList = compute_k(1, N, Intervals, PrevDP, {0, []}, [{0, []}]),
  CurrentDP = lists:reverse(NewDPList),
  CurrentBest = lists:last(CurrentDP),
  NewBest = if element(1, CurrentBest) > element(1, BestOverall) -> CurrentBest;
               element(1, CurrentBest) < element(1, BestOverall) -> BestOverall;
               element(2, CurrentBest) < element(2, BestOverall) -> CurrentBest;
               true -> BestOverall
            end,
  solve_dp(K + 1, Intervals, CurrentDP, NewBest).

compute_k(I, N, Intervals, PrevDP, PrevKDP, Acc) when I =< N ->
  {L, _, W, Id} = element(I, Intervals),
  PrevIdx = find_prev(Intervals, L, 1, I - 1, 0),
  {PrevW, PrevIdxs} = element(PrevIdx + 1, PrevDP),
  NewW = PrevW + W,
  NewIdxs = lists:sort([Id | PrevIdxs]),
  PickI = {NewW, NewIdxs},
  {BestW, BestIdxs} = PrevKDP,
  CurrentBest = if NewW > BestW -> PickI;
                   NewW < BestW -> PrevKDP;
                   NewIdxs < BestIdxs -> PickI;
                   true -> PrevKDP
                end,
  compute_k(I + 1, N, Intervals, PrevDP, CurrentBest, [CurrentBest | Acc]);
compute_k(_I, _N, _Intervals, _PrevDP, _PrevKDP, Acc) -> Acc.

find_prev(Intervals, L, Low, High, Best) when Low =< High ->
  Mid = (Low + High) div 2,
  {_, Ri, _, _} = element(Mid, Intervals),
  if Ri < L -> find_prev(Intervals, L, Mid + 1, High, Mid);
     true -> find_prev(Intervals, L, Low, Mid - 1, Best)
  end;
find_prev(_Intervals, _L, _Low, _High, Best) -> Best.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec maximum_weight(intervals :: [[integer]]) :: [integer]
  def maximum_weight(intervals) do
    n = length(intervals)
    intervals_with_id = Enum.with_index(intervals) |> Enum.map(fn {[l, r, w], id} -> {l, r, w, id} end)
    sorted_intervals = Enum.sort(intervals_with_id, fn {l1, r1, w1, id1}, {l2, r2, w2, id2} ->
      if r1 != r2, do: r1 < r2, else: (if l1 != l2, do: l1 < l2, else: (if w1 != w2, do: w1 < w2, else: id1 < id2))
    end)
    intervals_tuple = List.to_tuple(sorted_intervals)
    initial_dp = List.duplicate({0, []}, n + 1)

    final_state = Enum.reduce(1..4, {{0, []}, initial_dp}, fn _k, {overall_best, dp} ->
      prev_dp_tuple = List.to_tuple(dp)
      new_dp_list = compute_k(1, n, intervals_tuple, prev_dp_tuple, {0, []}, [{0, []}])
      current_dp = Enum.reverse(new_dp_list)
      current_best = List.last(current_dp)

      new_overall = if is_better?(current_best, overall_best), do: current_best, else: overall_best
      {new_overall, current_dp}
    end)

    elem(elem(final_state, 0), 1)
  end

  defp compute_k(i, n, intervals, prev_dp, prev_k_dp, acc) when i <= n do
    {l, _r, w, id} = elem(intervals, i - 1)
    prev_idx = find_prev(intervals, l, 1, i - 1, 0)
    {prev_w, prev_idxs} = elem(prev_dp, prev_idx)

    pick_i = {prev_w + w, Enum.sort([id | prev_idxs])}
    current_best = if is_better?(pick_i, prev_k_dp), do: pick_i, else: prev_k_dp
    compute_k(i + 1, n, intervals, prev_dp, current_best, [current_best | acc])
  end
  defp compute_k(_i, _n, _intervals, _prev_dp, _prev_k_dp, acc), do: acc

  defp find_prev(intervals, l, low, high, best) when low <= high do
    mid = div(low + high, 2)
    {_li, ri, _wi, _idi} = elem(intervals, mid - 1)
    if ri < l do
      find_prev(intervals, l, mid + 1, high, mid)
    else
      find_prev(intervals, l, low, mid - 1, best)
    end
  end
  defp find_prev(_intervals, _l, _low, _high, best), do: best

  defp is_better?({w1, idx1}, {w2, idx2}) do
    cond do
      w1 > w2 -> true
      w1 < w2 -> false
      true -> idx1 < idx2
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(K \cdot N \log N), where $K = 4$ and $N$ is the number of intervals. Sorting the intervals takes $O(N \log N)$. For each $k \in \{1, 2, 3, 4\}$, we iterate through $N$ intervals and perform a binary search in $O(\log N)$. Comparing and sorting the small index lists takes $O(K)$ time, which is constant.
- **Space Complexity:** O(K \cdot N), to store the DP table. By optimizing the DP to only keep the current and previous layers, this can be reduced to $O(N)$, though $O(K \cdot N)$ is well within limits for $N = 5 \times 10^4$.
