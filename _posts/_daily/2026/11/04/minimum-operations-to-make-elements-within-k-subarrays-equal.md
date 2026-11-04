---
layout: post
title: "Minimum Operations to Make Elements Within K Subarrays Equal"
date: 2026-11-04 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Hash Table", "Math", "Dynamic Programming", "Sliding Window", "Heap (Priority Queue)"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    long long minOperations(vector<int>& nums,\
        \ int x, int k) {\n        int n = nums.size();\n        vector<int> sortedUnique\
        \ = nums;\n        sort(sortedUnique.begin(), sortedUnique.end());\n       \
        \ sortedUnique.erase(unique(sortedUnique.begin(), sortedUnique.end()), sortedUnique.end());\n\
        \        int u = sortedUnique.size();\n\n        auto getRank = [&](int val)\
        \ {\n            return lower_bound(sortedUnique.begin(), sortedUnique.end(),\
        \ val) - sortedUnique.begin() + 1;\n        };\n\n        vector<long long>\
        \ bitCount(u + 1, 0), bitSum(u + 1, 0);\n        auto update = [&](int idx,\
        \ int val, int cnt) {\n            for (; idx <= u; idx += idx & -idx) {\n \
        \               bitCount[idx] += cnt;\n                bitSum[idx] += (long\
        \ long)cnt * val;\n            }\n        };\n\n        auto query = [&](vector<long\
        \ long>& bit, int idx) {\n            long long res = 0;\n            for (;\
        \ idx > 0; idx -= idx & -idx) res += bit[idx];\n            return res;\n  \
        \      };\n\n        int h = 0;\n        if (u > 0) while ((1 << (h + 1)) <=\
        \ u) h++;\n\n        vector<long long> costs(n - x + 1);\n        long long\
        \ totalSum = 0;\n        for (int i = 0; i < n; ++i) {\n            totalSum\
        \ += nums[i];\n            update(getRank(nums[i]), nums[i], 1);\n         \
        \   if (i >= x) {\n                totalSum -= nums[i - x];\n              \
        \  update(getRank(nums[i - x]), nums[i - x], -1);\n            }\n         \
        \   if (i >= x - 1) {\n                int target = (x + 1) / 2, idx = 0;\n\
        \                for (int j = h; j >= 0; j--) {\n                    int next\
        \ = idx + (1 << j);\n                    if (next <= u && bitCount[next] < target)\
        \ {\n                        idx = next;\n                        target -=\
        \ bitCount[idx];\n                    }\n                }\n               \
        \ int medianRank = idx + 1;\n                long long M = sortedUnique[medianRank\
        \ - 1];\n                long long numLess = query(bitCount, medianRank - 1);\n\
        \                long long sumLess = query(bitSum, medianRank - 1);\n      \
        \          long long numUpToMedian = query(bitCount, medianRank);\n        \
        \        long long sumUpToMedian = query(bitSum, medianRank);\n            \
        \    long long numGreater = x - numUpToMedian;\n                long long sumGreater\
        \ = totalSum - sumUpToMedian;\n                costs[i - x + 1] = (sumGreater\
        \ - numGreater * M) + (numLess * M - sumLess);\n            }\n        }\n\n\
        \        vector<long long> dp(n + 1, 0);\n        long long INF = 1e16;\n  \
        \      for (int j = 1; j <= k; ++j) {\n            vector<long long> next_dp(n\
        \ + 1, INF);\n            long long min_val = INF;\n            for (int i =\
        \ j * x; i <= n; ++i) {\n                if (dp[i - x] + costs[i - x] < min_val)\
        \ min_val = dp[i - x] + costs[i - x];\n                next_dp[i] = min_val;\n\
        \            }\n            dp = next_dp;\n        }\n        return dp[n];\n\
        \    }\n};"
      java: "import java.util.*;\n\nclass Solution {\n    public long minOperations(int[]\
        \ nums, int x, int k) {\n        int n = nums.length;\n        int[] sortedUnique\
        \ = nums.clone();\n        Arrays.sort(sortedUnique);\n        int u = 0;\n\
        \        for (int i = 0; i < n; i++) {\n            if (i == 0 || sortedUnique[i]\
        \ != sortedUnique[i - 1]) sortedUnique[u++] = sortedUnique[i];\n        }\n\
        \        int[] uniqueArr = Arrays.copyOf(sortedUnique, u);\n\n        long[]\
        \ bitCount = new long[u + 1];\n        long[] bitSum = new long[u + 1];\n  \
        \      long[] costs = new long[n - x + 1];\n        long totalSum = 0;\n   \
        \     int h = 0;\n        while ((1 << (h + 1)) <= u) h++;\n\n        for (int\
        \ i = 0; i < n; i++) {\n            totalSum += nums[i];\n            int rank\
        \ = Arrays.binarySearch(uniqueArr, nums[i]) + 1;\n            for (int idx =\
        \ rank; idx <= u; idx += idx & -idx) {\n                bitCount[idx] += 1;\n\
        \                bitSum[idx] += nums[i];\n            }\n            if (i >=\
        \ x) {\n                totalSum -= nums[i - x];\n                int oldRank\
        \ = Arrays.binarySearch(uniqueArr, nums[i - x]) + 1;\n                for (int\
        \ idx = oldRank; idx <= u; idx += idx & -idx) {\n                    bitCount[idx]\
        \ -= 1;\n                    bitSum[idx] -= nums[i - x];\n                }\n\
        \            }\n            if (i >= x - 1) {\n                int target =\
        \ (x + 1) / 2, idx = 0, currTarget = target;\n                for (int j = h;\
        \ j >= 0; j--) {\n                    int next = idx + (1 << j);\n         \
        \           if (next <= u && bitCount[next] < currTarget) {\n              \
        \          idx = next;\n                        currTarget -= bitCount[idx];\n\
        \                    }\n                }\n                int mRank = idx +\
        \ 1;\n                long M = uniqueArr[mRank - 1];\n                long numL\
        \ = 0, sumL = 0, numU = 0, sumU = 0;\n                for (int r = mRank - 1;\
        \ r > 0; r -= r & -r) { numL += bitCount[r]; sumL += bitSum[r]; }\n        \
        \        for (int r = mRank; r > 0; r -= r & -r) { numU += bitCount[r]; sumU\
        \ += bitSum[r]; }\n                long numG = x - numU, sumG = totalSum - sumU;\n\
        \                costs[i - x + 1] = (sumG - numG * M) + (numL * M - sumL);\n\
        \            }\n        }\n\n        long[] dp = new long[n + 1];\n        long\
        \ INF = (long) 1e16;\n        for (int j = 1; j <= k; j++) {\n            long[]\
        \ next_dp = new long[n + 1];\n            Arrays.fill(next_dp, INF);\n     \
        \       long min_val = INF;\n            for (int i = j * x; i <= n; i++) {\n\
        \                if (dp[i - x] + costs[i - x] < min_val) min_val = dp[i - x]\
        \ + costs[i - x];\n                next_dp[i] = min_val;\n            }\n  \
        \          dp = next_dp;\n        }\n        return dp[n];\n    }\n}"
      python: "class Solution(object):\n    def minOperations(self, nums, x, k):\n \
        \       n = len(nums)\n        unique_vals = sorted(list(set(nums)))\n     \
        \   rank_map = {val: i + 1 for i, val in enumerate(unique_vals)}\n        ranks\
        \ = [rank_map[v] for v in nums]\n        U = len(unique_vals)\n        h = U.bit_length()\
        \ - 1\n        bit_count, bit_sum = [0] * (U + 1), [0] * (U + 1)\n        costs\
        \ = [0] * (n - x + 1)\n        total_sum_window = 0\n\n        for i in range(n):\n\
        \            val, r = nums[i], ranks[i]\n            total_sum_window += val\n\
        \            curr_r = r\n            while curr_r <= U:\n                bit_count[curr_r]\
        \ += 1\n                bit_sum[curr_r] += val\n                curr_r += curr_r\
        \ & -curr_r\n            if i >= x:\n                old_val, old_r = nums[i\
        \ - x], ranks[i - x]\n                total_sum_window -= old_val\n        \
        \        curr_r = old_r\n                while curr_r <= U:\n              \
        \      bit_count[curr_r] -= 1\n                    bit_sum[curr_r] -= old_val\n\
        \                    curr_r += curr_r & -curr_r\n            if i >= x - 1:\n\
        \                idx, target = 0, (x + 1) // 2\n                for j in range(h,\
        \ -1, -1):\n                    next_idx = idx + (1 << j)\n                \
        \    if next_idx <= U and bit_count[next_idx] < target:\n                  \
        \      idx = next_idx\n                        target -= bit_count[idx]\n  \
        \              m_rank = idx + 1\n                m_val = unique_vals[m_rank\
        \ - 1]\n                num_up, sum_up, num_l, sum_l = 0, 0, 0, 0\n        \
        \        curr_r = m_rank\n                while curr_r > 0:\n              \
        \      num_up += bit_count[curr_r]\n                    sum_up += bit_sum[curr_r]\n\
        \                    curr_r -= curr_r & -curr_r\n                curr_r = m_rank\
        \ - 1\n                while curr_r > 0:\n                    num_l += bit_count[curr_r]\n\
        \                    sum_l += bit_sum[curr_r]\n                    curr_r -=\
        \ curr_r & -curr_r\n                num_g = x - num_up\n                sum_g\
        \ = total_sum_window - sum_up\n                costs[i - x + 1] = (sum_g - num_g\
        \ * m_val) + (num_l * m_val - sum_l)\n\n        dp = [0] * (n + 1)\n       \
        \ INF = 10**16\n        for j in range(1, k + 1):\n            next_dp = [INF]\
        \ * (n + 1)\n            min_val = INF\n            for i in range(j * x, n\
        \ + 1):\n                val_to_check = dp[i - x] + costs[i - x]\n         \
        \       if val_to_check < min_val: min_val = val_to_check\n                next_dp[i]\
        \ = min_val\n            dp = next_dp\n        return dp[n]"
      python3: "class Solution:\n    def minOperations(self, nums: List[int], x: int,\
        \ k: int) -> int:\n        n = len(nums)\n        unique_vals = sorted(list(set(nums)))\n\
        \        num_unique = len(unique_vals)\n        val_to_idx = {v: i + 1 for i,\
        \ v in enumerate(unique_vals)}\n\n        bit_count = [0] * (num_unique + 1)\n\
        \        bit_sum = [0] * (num_unique + 1)\n\n        def update(bit, idx, val):\n\
        \            while idx <= num_unique:\n                bit[idx] += val\n   \
        \             idx += idx & -idx\n\n        def query(bit, idx):\n          \
        \  s = 0\n            while idx > 0:\n                s += bit[idx]\n      \
        \          idx -= idx & -idx\n            return s\n\n        def find_kth(target):\n\
        \            idx = 0\n            max_pow = 1 << 17\n            for i in range(17,\
        \ -1, -1):\n                p = 1 << i\n                next_idx = idx + p\n\
        \                if next_idx <= num_unique and bit_count[next_idx] < target:\n\
        \                    idx = next_idx\n                    target -= bit_count[idx]\n\
        \            return idx + 1\n\n        costs = [0] * (n - x + 1)\n        current_window_sum\
        \ = 0\n        for i in range(x):\n            idx = val_to_idx[nums[i]]\n \
        \           update(bit_count, idx, 1)\n            update(bit_sum, idx, nums[i])\n\
        \            current_window_sum += nums[i]\n\n        m = (x + 1) // 2\n   \
        \     def get_cost():\n            m_idx = find_kth(m)\n            val_m =\
        \ unique_vals[m_idx - 1]\n            cnt_l = query(bit_count, m_idx)\n    \
        \        sum_l = query(bit_sum, m_idx)\n            cnt_r = x - cnt_l\n    \
        \        sum_r = current_window_sum - sum_l\n            return (cnt_l * val_m\
        \ - sum_l) + (sum_r - cnt_r * val_m)\n\n        costs[0] = get_cost()\n    \
        \    for i in range(1, n - x + 1):\n            idx_rem = val_to_idx[nums[i\
        \ - 1]]\n            update(bit_count, idx_rem, -1)\n            update(bit_sum,\
        \ idx_rem, -nums[i - 1])\n            idx_add = val_to_idx[nums[i + x - 1]]\n\
        \            update(bit_count, idx_add, 1)\n            update(bit_sum, idx_add,\
        \ nums[i + x - 1])\n            current_window_sum += nums[i + x - 1] - nums[i\
        \ - 1]\n            costs[i] = get_cost()\n\n        dp = [0] * (n + 1)\n  \
        \      for j in range(1, k + 1):\n            new_dp = [float('inf')] * (n +\
        \ 1)\n            for i in range(j * x, n + 1):\n                new_dp[i] =\
        \ new_dp[i - 1]\n                option = dp[i - x] + costs[i - x]\n       \
        \         if option < new_dp[i]:\n                    new_dp[i] = option\n \
        \           dp = new_dp\n\n        return int(dp[n])"
      c: "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <limits.h>\n\
        \nint compare(const void* a, const void* b) {\n    int arg1 = *(const int*)a;\n\
        \    int arg2 = *(const int*)b;\n    if (arg1 < arg2) return -1;\n    if (arg1\
        \ > arg2) return 1;\n    return 0;\n}\n\nvoid update(long long* bit, int idx,\
        \ long long val, int n) {\n    for (; idx <= n; idx += idx & -idx) {\n     \
        \   bit[idx] += val;\n    }\n}\n\nlong long query(long long* bit, int idx) {\n\
        \    long long res = 0;\n    for (; idx > 0; idx -= idx & -idx) {\n        res\
        \ += bit[idx];\n    }\n    return res;\n}\n\nint find_kth(long long* bit_count,\
        \ int target, int n) {\n    int idx = 0;\n    for (int p = 1 << 17; p > 0; p\
        \ >>= 1) {\n        int next_idx = idx + p;\n        if (next_idx <= n && bit_count[next_idx]\
        \ < target) {\n            idx = next_idx;\n            target -= bit_count[idx];\n\
        \        }\n    }\n    return idx + 1;\n}\n\nint find_val_idx(int* arr, int\
        \ size, int val) {\n    int low = 0, high = size - 1;\n    while (low <= high)\
        \ {\n        int mid = low + (high - low) / 2;\n        if (arr[mid] == val)\
        \ return mid + 1;\n        if (arr[mid] < val) low = mid + 1;\n        else\
        \ high = mid - 1;\n    }\n    return -1;\n}\n\nlong long minOperations(int*\
        \ nums, int numsSize, int x, int k) {\n    int* sorted_nums = malloc(numsSize\
        \ * sizeof(int));\n    memcpy(sorted_nums, nums, numsSize * sizeof(int));\n\
        \    qsort(sorted_nums, numsSize, sizeof(int), compare);\n\n    int num_unique\
        \ = 0;\n    if (numsSize > 0) {\n        num_unique = 1;\n        for (int i\
        \ = 1; i < numsSize; i++) {\n            if (sorted_nums[i] != sorted_nums[i-1])\
        \ {\n                sorted_nums[num_unique++] = sorted_nums[i];\n         \
        \   }\n        }\n    }\n\n    long long* bit_count = calloc(num_unique + 1,\
        \ sizeof(long long));\n    long long* bit_sum = calloc(num_unique + 1, sizeof(long\
        \ long));\n    long long current_window_sum = 0;\n\n    long long* costs = malloc((numsSize\
        \ - x + 1) * sizeof(long long));\n    int m = (x + 1) / 2;\n\n    for (int i\
        \ = 0; i < x; i++) {\n        int idx = find_val_idx(sorted_nums, num_unique,\
        \ nums[i]);\n        update(bit_count, idx, 1, num_unique);\n        update(bit_sum,\
        \ idx, nums[i], num_unique);\n        current_window_sum += nums[i];\n    }\n\
        \n    for (int i = 0; i <= numsSize - x; i++) {\n        if (i > 0) {\n    \
        \        int idx_rem = find_val_idx(sorted_nums, num_unique, nums[i - 1]);\n\
        \            update(bit_count, idx_rem, -1, num_unique);\n            update(bit_sum,\
        \ idx_rem, -nums[i - 1], num_unique);\n            int idx_add = find_val_idx(sorted_nums,\
        \ num_unique, nums[i + x - 1]);\n            update(bit_count, idx_add, 1, num_unique);\n\
        \            update(bit_sum, idx_add, nums[i + x - 1], num_unique);\n      \
        \      current_window_sum += (long long)nums[i + x - 1] - nums[i - 1];\n   \
        \     }\n        int m_idx = find_kth(bit_count, m, num_unique);\n        long\
        \ long val_m = sorted_nums[m_idx - 1];\n        long long cnt_l = query(bit_count,\
        \ m_idx);\n        long long sum_l = query(bit_sum, m_idx);\n        long long\
        \ cnt_r = x - cnt_l;\n        long long sum_r = current_window_sum - sum_l;\n\
        \        costs[i] = (cnt_l * val_m - sum_l) + (sum_r - cnt_r * val_m);\n   \
        \ }\n\n    long long* dp = malloc((numsSize + 1) * sizeof(long long));\n   \
        \ long long* next_dp = malloc((numsSize + 1) * sizeof(long long));\n    for\
        \ (int i = 0; i <= numsSize; i++) dp[i] = 0;\n\n    for (int j = 1; j <= k;\
        \ j++) {\n        for (int i = 0; i <= numsSize; i++) next_dp[i] = LLONG_MAX;\n\
        \        for (int i = j * x; i <= numsSize; i++) {\n            next_dp[i] =\
        \ next_dp[i - 1];\n            if (dp[i - x] != LLONG_MAX) {\n             \
        \   long long option = dp[i - x] + costs[i - x];\n                if (option\
        \ < next_dp[i]) next_dp[i] = option;\n            }\n        }\n        memcpy(dp,\
        \ next_dp, (numsSize + 1) * sizeof(long long));\n    }\n\n    long long result\
        \ = dp[numsSize];\n    free(sorted_nums); free(bit_count); free(bit_sum); free(costs);\
        \ free(dp); free(next_dp);\n    return result;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\nusing System.Linq;\n\
        \npublic class Solution {\n    public long MinOperations(int[] nums, int x,\
        \ int k) {\n        int n = nums.Length;\n        int[] uniqueVals = nums.Distinct().OrderBy(v\
        \ => v).ToArray();\n        int numUnique = uniqueVals.Length;\n\n        long[]\
        \ bitCount = new long[numUnique + 1];\n        long[] bitSum = new long[numUnique\
        \ + 1];\n\n        void Update(long[] bit, int idx, long val) {\n          \
        \  for (; idx <= numUnique; idx += idx & -idx) {\n                bit[idx] +=\
        \ val;\n            }\n        }\n\n        long Query(long[] bit, int idx)\
        \ {\n            long res = 0;\n            for (; idx > 0; idx -= idx & -idx)\
        \ {\n                res += bit[idx];\n            }\n            return res;\n\
        \        }\n\n        int FindKth(int target) {\n            int idx = 0;\n\
        \            for (int p = 1 << 17; p > 0; p >>= 1) {\n                int nextIdx\
        \ = idx + p;\n                if (nextIdx <= numUnique && bitCount[nextIdx]\
        \ < target) {\n                    idx = nextIdx;\n                    target\
        \ -= (int)bitCount[idx];\n                }\n            }\n            return\
        \ idx + 1;\n        }\n\n        long[] costs = new long[n - x + 1];\n     \
        \   long currentWindowSum = 0;\n        int m = (x + 1) / 2;\n\n        for\
        \ (int i = 0; i < x; i++) {\n            int idx = Array.BinarySearch(uniqueVals,\
        \ nums[i]) + 1;\n            Update(bitCount, idx, 1);\n            Update(bitSum,\
        \ idx, nums[i]);\n            currentWindowSum += nums[i];\n        }\n\n  \
        \      for (int i = 0; i <= n - x; i++) {\n            if (i > 0) {\n      \
        \          int idxRem = Array.BinarySearch(uniqueVals, nums[i - 1]) + 1;\n \
        \               Update(bitCount, idxRem, -1);\n                Update(bitSum,\
        \ idxRem, -nums[i - 1]);\n                int idxAdd = Array.BinarySearch(uniqueVals,\
        \ nums[i + x - 1]) + 1;\n                Update(bitCount, idxAdd, 1);\n    \
        \            Update(bitSum, idxAdd, nums[i + x - 1]);\n                currentWindowSum\
        \ += (long)nums[i + x - 1] - nums[i - 1];\n            }\n            int mIdx\
        \ = FindKth(m);\n            long valM = uniqueVals[mIdx - 1];\n           \
        \ long cntL = Query(bitCount, mIdx);\n            long sumL = Query(bitSum,\
        \ mIdx);\n            long cntR = x - cntL;\n            long sumR = currentWindowSum\
        \ - sumL;\n            costs[i] = (cntL * valM - sumL) + (sumR - cntR * valM);\n\
        \        }\n\n        long[] dp = new long[n + 1];\n        for (int j = 1;\
        \ j <= k; j++) {\n            long[] nextDp = new long[n + 1];\n           \
        \ for (int i = 0; i <= n; i++) nextDp[i] = long.MaxValue;\n            for (int\
        \ i = j * x; i <= n; i++) {\n                nextDp[i] = nextDp[i - 1];\n  \
        \              if (dp[i - x] != long.MaxValue) {\n                    long option\
        \ = dp[i - x] + costs[i - x];\n                    if (option < nextDp[i]) nextDp[i]\
        \ = option;\n                }\n            }\n            dp = nextDp;\n  \
        \      }\n\n        return dp[n];\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @param {number} x\n * @param {number}\
        \ k\n * @return {number}\n */\nvar minOperations = function(nums, x, k) {\n\
        \    const n = nums.length;\n    const uniqueVals = Array.from(new Set(nums)).sort((a,\
        \ b) => a - b);\n    const numUnique = uniqueVals.length;\n    const valToIdx\
        \ = new Map();\n    for (let i = 0; i < numUnique; i++) {\n        valToIdx.set(uniqueVals[i],\
        \ i + 1);\n    }\n\n    const bitCount = new Float64Array(numUnique + 1);\n\
        \    const bitSum = new Float64Array(numUnique + 1);\n\n    function update(bit,\
        \ idx, val) {\n        while (idx <= numUnique) {\n            bit[idx] += val;\n\
        \            idx += idx & -idx;\n        }\n    }\n\n    function query(bit,\
        \ idx) {\n        let s = 0;\n        while (idx > 0) {\n            s += bit[idx];\n\
        \            idx -= idx & -idx;\n        }\n        return s;\n    }\n\n   \
        \ function findKth(target) {\n        let idx = 0;\n        for (let p = 1 <<\
        \ 17; p > 0; p >>= 1) {\n            let nextIdx = idx + p;\n            if\
        \ (nextIdx <= numUnique && bitCount[nextIdx] < target) {\n                idx\
        \ = nextIdx;\n                target -= bitCount[idx];\n            }\n    \
        \    }\n        return idx + 1;\n    }\n\n    const costs = new Float64Array(n\
        \ - x + 1);\n    let currentWindowSum = 0;\n    const m = Math.floor((x + 1)\
        \ / 2);\n\n    for (let i = 0; i < x; i++) {\n        const idx = valToIdx.get(nums[i]);\n\
        \        update(bitCount, idx, 1);\n        update(bitSum, idx, nums[i]);\n\
        \        currentWindowSum += nums[i];\n    }\n\n    for (let i = 0; i <= n -\
        \ x; i++) {\n        if (i > 0) {\n            const idxRem = valToIdx.get(nums[i\
        \ - 1]);\n            update(bitCount, idxRem, -1);\n            update(bitSum,\
        \ idxRem, -nums[i - 1]);\n            const idxAdd = valToIdx.get(nums[i + x\
        \ - 1]);\n            update(bitCount, idxAdd, 1);\n            update(bitSum,\
        \ idxAdd, nums[i + x - 1]);\n            currentWindowSum += nums[i + x - 1]\
        \ - nums[i - 1];\n        }\n        const mIdx = findKth(m);\n        const\
        \ valM = uniqueVals[mIdx - 1];\n        const cntL = query(bitCount, mIdx);\n\
        \        const sumL = query(bitSum, mIdx);\n        const cntR = x - cntL;\n\
        \        const sumR = currentWindowSum - sumL;\n        costs[i] = (cntL * valM\
        \ - sumL) + (sumR - cntR * valM);\n    }\n\n    let dp = new Float64Array(n\
        \ + 1).fill(0);\n    for (let j = 1; j <= k; j++) {\n        const nextDp =\
        \ new Float64Array(n + 1).fill(Infinity);\n        for (let i = j * x; i <=\
        \ n; i++) {\n            nextDp[i] = nextDp[i - 1];\n            const option\
        \ = dp[i - x] + costs[i - x];\n            if (option < nextDp[i]) nextDp[i]\
        \ = option;\n        }\n        dp = nextDp;\n    }\n\n    return dp[n];\n};"
      typescript: "function minOperations(nums: number[], x: number, k: number): number\
        \ {\n    const n = nums.length;\n    const unique = Array.from(new Set(nums)).sort((a,\
        \ b) => a - b);\n    const rankMap = new Map<number, number>();\n    for (let\
        \ i = 0; i < unique.length; i++) rankMap.set(unique[i], i + 1);\n    const uniqueSize\
        \ = unique.length;\n\n    const bitCount = new Float64Array(uniqueSize + 1);\n\
        \    const bitSum = new Float64Array(uniqueSize + 1);\n\n    function update(bit:\
        \ Float64Array, idx: number, delta: number) {\n        for (; idx <= uniqueSize;\
        \ idx += idx & -idx) {\n            bit[idx] += delta;\n        }\n    }\n\n\
        \    function query(bit: Float64Array, idx: number): number {\n        let sum\
        \ = 0;\n        for (; idx > 0; idx -= idx & -idx) {\n            sum += bit[idx];\n\
        \        }\n        return sum;\n    }\n\n    let stepStart = 1;\n    while\
        \ ((stepStart << 1) <= uniqueSize) stepStart <<= 1;\n\n    function findKth(kVal:\
        \ number): number {\n        let pos = 0;\n        let currentK = kVal;\n  \
        \      let step = stepStart;\n        while (step > 0) {\n            if (pos\
        \ + step <= uniqueSize && bitCount[pos + step] < currentK) {\n             \
        \   pos += step;\n                currentK -= bitCount[pos];\n            }\n\
        \            step >>= 1;\n        }\n        return pos + 1;\n    }\n\n    const\
        \ costs = new Float64Array(n - x + 1);\n    const m = Math.floor((x + 1) / 2);\n\
        \    let currentTotalSum = 0;\n\n    for (let i = 0; i < n; i++) {\n       \
        \ const val = nums[i];\n        const r = rankMap.get(val)!;\n        update(bitCount,\
        \ r, 1);\n        update(bitSum, r, val);\n        currentTotalSum += val;\n\
        \n        if (i >= x) {\n            const prevVal = nums[i - x];\n        \
        \    const pr = rankMap.get(prevVal)!;\n            update(bitCount, pr, -1);\n\
        \            update(bitSum, pr, -prevVal);\n            currentTotalSum -= prevVal;\n\
        \        }\n\n        if (i >= x - 1) {\n            const medianIdx = findKth(m);\n\
        \            const medianVal = unique[medianIdx - 1];\n            const countLow\
        \ = query(bitCount, medianIdx);\n            const sumLow = query(bitSum, medianIdx);\n\
        \            const countHigh = x - countLow;\n            const sumHigh = currentTotalSum\
        \ - sumLow;\n            costs[i - x + 1] = (countLow * medianVal - sumLow)\
        \ + (sumHigh - countHigh * medianVal);\n        }\n    }\n\n    const INF =\
        \ Number.MAX_SAFE_INTEGER;\n    let dp = new Float64Array(n + 1).fill(0);\n\n\
        \    for (let i = 1; i <= k; i++) {\n        const nextDp = new Float64Array(n\
        \ + 1).fill(INF);\n        for (let j = i * x; j <= n; j++) {\n            nextDp[j]\
        \ = Math.min(nextDp[j - 1], dp[j - x] + costs[j - x]);\n        }\n        dp\
        \ = nextDp;\n    }\n\n    return dp[n];\n}"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @param\
        \ Integer $x\n     * @param Integer $k\n     * @return Integer\n     */\n  \
        \  function minOperations($nums, $x, $k) {\n        $n = count($nums);\n   \
        \     $unique = array_unique($nums);\n        sort($unique);\n        $rankMap\
        \ = [];\n        foreach ($unique as $i => $val) {\n            $rankMap[$val]\
        \ = $i + 1;\n        }\n        $uniqueSize = count($unique);\n        $bitCount\
        \ = new SplFixedArray($uniqueSize + 1);\n        $bitSum = new SplFixedArray($uniqueSize\
        \ + 1);\n        for ($i = 0; $i <= $uniqueSize; $i++) {\n            $bitCount[$i]\
        \ = 0;\n            $bitSum[$i] = 0;\n        }\n\n        $update = function(&$bit,\
        \ $idx, $delta) use ($uniqueSize) {\n            for (; $idx <= $uniqueSize;\
        \ $idx += $idx & -$idx) {\n                $bit[$idx] += $delta;\n         \
        \   }\n        };\n\n        $query = function($bit, $idx) {\n            $sum\
        \ = 0;\n            for (; $idx > 0; $idx -= $idx & -$idx) {\n             \
        \   $sum += $bit[$idx];\n            }\n            return $sum;\n        };\n\
        \n        $stepStart = 1;\n        while (($stepStart << 1) <= $uniqueSize)\
        \ $stepStart <<= 1;\n\n        $findKth = function($kVal) use ($bitCount, $uniqueSize,\
        \ $stepStart) {\n            $pos = 0;\n            $step = $stepStart;\n  \
        \          while ($step > 0) {\n                if ($pos + $step <= $uniqueSize\
        \ && $bitCount[$pos + $step] < $kVal) {\n                    $pos += $step;\n\
        \                    $kVal -= $bitCount[$pos];\n                }\n        \
        \        $step >>= 1;\n            }\n            return $pos + 1;\n       \
        \ };\n\n        $costs = new SplFixedArray($n - $x + 1);\n        $m = (int)(($x\
        \ + 1) / 2);\n        $currentTotalSum = 0;\n\n        for ($i = 0; $i < $n;\
        \ $i++) {\n            $val = $nums[$i];\n            $r = $rankMap[$val];\n\
        \            $update($bitCount, $r, 1);\n            $update($bitSum, $r, $val);\n\
        \            $currentTotalSum += $val;\n\n            if ($i >= $x) {\n    \
        \            $prevVal = $nums[$i - $x];\n                $pr = $rankMap[$prevVal];\n\
        \                $update($bitCount, $pr, -1);\n                $update($bitSum,\
        \ $pr, -$prevVal);\n                $currentTotalSum -= $prevVal;\n        \
        \    }\n\n            if ($i >= $x - 1) {\n                $medianIdx = $findKth($m);\n\
        \                $medianVal = $unique[$medianIdx - 1];\n                $countLow\
        \ = $query($bitCount, $medianIdx);\n                $sumLow = $query($bitSum,\
        \ $medianIdx);\n                $countHigh = $x - $countLow;\n             \
        \   $sumHigh = $currentTotalSum - $sumLow;\n                $costs[$i - $x +\
        \ 1] = ($countLow * $medianVal - $sumLow) + ($sumHigh - $countHigh * $medianVal);\n\
        \            }\n        }\n\n        $inf = 1e16;\n        $dp = new SplFixedArray($n\
        \ + 1);\n        for ($i = 0; $i <= $n; $i++) $dp[$i] = 0;\n\n        for ($i\
        \ = 1; $i <= $k; $i++) {\n            $nextDp = new SplFixedArray($n + 1);\n\
        \            for ($j = 0; $j < $i * $x; $j++) $nextDp[$j] = $inf;\n        \
        \    for ($j = $i * $x; $j <= $n; $j++) {\n                $opt1 = $nextDp[$j\
        \ - 1];\n                $opt2 = $dp[$j - $x] + $costs[$j - $x];\n         \
        \       $nextDp[$j] = $opt1 < $opt2 ? $opt1 : $opt2;\n            }\n      \
        \      $dp = $nextDp;\n        }\n\n        return (int)$dp[$n];\n    }\n}"
      swift: "class Solution {\n    func minOperations(_ nums: [Int], _ x: Int, _ k:\
        \ Int) -> Int {\n        let n = nums.count\n        let sortedUnique = Array(Set(nums)).sorted()\n\
        \        let uniqueSize = sortedUnique.count\n        var rankMap: [Int: Int]\
        \ = [:]\n        for (i, val) in sortedUnique.enumerated() {\n            rankMap[val]\
        \ = i + 1\n        }\n\n        var bitCount = [Int](repeating: 0, count: uniqueSize\
        \ + 1)\n        var bitSum = [Int](repeating: 0, count: uniqueSize + 1)\n\n\
        \        func update(_ bit: inout [Int], _ idx: Int, _ delta: Int) {\n     \
        \       var i = idx\n            while i <= uniqueSize {\n                bit[i]\
        \ += delta\n                i += i & -i\n            }\n        }\n\n      \
        \  func query(_ bit: [Int], _ idx: Int) -> Int {\n            var sum = 0\n\
        \            var i = idx\n            while i > 0 {\n                sum +=\
        \ bit[i]\n                i -= i & -i\n            }\n            return sum\n\
        \        }\n\n        var stepStart = 1\n        while (stepStart << 1) <= uniqueSize\
        \ { stepStart <<= 1 }\n\n        func findKth(_ kVal: Int) -> Int {\n      \
        \      var pos = 0\n            var curK = kVal\n            var step = stepStart\n\
        \            while step > 0 {\n                if pos + step <= uniqueSize &&\
        \ bitCount[pos + step] < curK {\n                    pos += step\n         \
        \           curK -= bitCount[pos]\n                }\n                step >>=\
        \ 1\n            }\n            return pos + 1\n        }\n\n        var costs\
        \ = [Int](repeating: 0, count: n - x + 1)\n        let m = (x + 1) / 2\n   \
        \     var currentTotalSum = 0\n\n        for i in 0..<n {\n            let val\
        \ = nums[i]\n            let r = rankMap[val]!\n            update(&bitCount,\
        \ r, 1)\n            update(&bitSum, r, val)\n            currentTotalSum +=\
        \ val\n\n            if i >= x {\n                let prevVal = nums[i - x]\n\
        \                let pr = rankMap[prevVal]!\n                update(&bitCount,\
        \ pr, -1)\n                update(&bitSum, pr, -prevVal)\n                currentTotalSum\
        \ -= prevVal\n            }\n\n            if i >= x - 1 {\n               \
        \ let medianIdx = findKth(m)\n                let medianVal = sortedUnique[medianIdx\
        \ - 1]\n                let countLow = query(bitCount, medianIdx)\n        \
        \        let sumLow = query(bitSum, medianIdx)\n                let countHigh\
        \ = x - countLow\n                let sumHigh = currentTotalSum - sumLow\n \
        \               costs[i - x + 1] = (countLow * medianVal - sumLow) + (sumHigh\
        \ - countHigh * medianVal)\n            }\n        }\n\n        let inf = Int.max\
        \ / 2\n        var dp = [Int](repeating: 0, count: n + 1)\n\n        for i in\
        \ 1...k {\n            var nextDp = [Int](repeating: inf, count: n + 1)\n  \
        \          for j in (i * x)...n {\n                nextDp[j] = min(nextDp[j\
        \ - 1], dp[j - x] + costs[j - x])\n            }\n            dp = nextDp\n\
        \        }\n\n        return dp[n]\n    }\n}"
      kotlin: "class Solution {\n    fun minOperations(nums: IntArray, x: Int, k: Int):\
        \ Long {\n        val n = nums.size\n        val sortedUnique = nums.distinct().sorted()\n\
        \        val uniqueSize = sortedUnique.size\n        val rankMap = mutableMapOf<Int,\
        \ Int>()\n        for (i in sortedUnique.indices) {\n            rankMap[sortedUnique[i]]\
        \ = i + 1\n        }\n\n        val bitCount = LongArray(uniqueSize + 1)\n \
        \       val bitSum = LongArray(uniqueSize + 1)\n\n        fun update(bit: LongArray,\
        \ idx: Int, delta: Long) {\n            var i = idx\n            while (i <=\
        \ uniqueSize) {\n                bit[i] += delta\n                i += i and\
        \ -i\n            }\n        }\n\n        fun query(bit: LongArray, idx: Int):\
        \ Long {\n            var sum = 0L\n            var i = idx\n            while\
        \ (i > 0) {\n                sum += bit[i]\n                i -= i and -i\n\
        \            }\n            return sum\n        }\n\n        var stepStart =\
        \ 1\n        while ((stepStart shl 1) <= uniqueSize) stepStart = stepStart shl\
        \ 1\n\n        fun findKth(kVal: Long): Int {\n            var pos = 0\n   \
        \         var curK = kVal\n            var step = stepStart\n            while\
        \ (step > 0) {\n                if (pos + step <= uniqueSize && bitCount[pos\
        \ + step] < curK) {\n                    pos += step\n                    curK\
        \ -= bitCount[pos]\n                }\n                step = step shr 1\n \
        \           }\n            return pos + 1\n        }\n\n        val costs =\
        \ LongArray(n - x + 1)\n        val m = (x + 1) / 2\n        var currentTotalSum\
        \ = 0L\n\n        for (i in 0 until n) {\n            val valAtI = nums[i]\n\
        \            val r = rankMap[valAtI]!!\n            update(bitCount, r, 1L)\n\
        \            update(bitSum, r, valAtI.toLong())\n            currentTotalSum\
        \ += valAtI\n\n            if (i >= x) {\n                val prevVal = nums[i\
        \ - x]\n                val pr = rankMap[prevVal]!!\n                update(bitCount,\
        \ pr, -1L)\n                update(bitSum, pr, -prevVal.toLong())\n        \
        \        currentTotalSum -= prevVal\n            }\n\n            if (i >= x\
        \ - 1) {\n                val medianIdx = findKth(m.toLong())\n            \
        \    val medianVal = sortedUnique[medianIdx - 1].toLong()\n                val\
        \ countLow = query(bitCount, medianIdx)\n                val sumLow = query(bitSum,\
        \ medianIdx)\n                val countHigh = x.toLong() - countLow\n      \
        \          val sumHigh = currentTotalSum - sumLow\n                costs[i -\
        \ x + 1] = (countLow * medianVal - sumLow) + (sumHigh - countHigh * medianVal)\n\
        \            }\n        }\n\n        val inf = Long.MAX_VALUE / 2\n        var\
        \ dp = LongArray(n + 1) { 0L }\n\n        for (i in 1..k) {\n            val\
        \ nextDp = LongArray(n + 1) { inf }\n            for (j in (i * x)..n) {\n \
        \               nextDp[j] = Math.min(nextDp[j - 1], dp[j - x] + costs[j - x])\n\
        \            }\n            dp = nextDp\n        }\n\n        return dp[n]\n\
        \    }\n}"
      dart: "import 'dart:math';\n\nclass Solution {\n  int minOperations(List<int>\
        \ nums, int x, int k) {\n    int n = nums.length;\n    List<int> sortedUnique\
        \ = nums.toSet().toList()..sort();\n    int m_val = (x + 1) ~/ 2;\n    int l\
        \ = sortedUnique.length;\n\n    List<int> numIndices = nums.map((v) {\n    \
        \  int low = 0, high = l - 1;\n      while (low <= high) {\n        int mid\
        \ = (low + high) ~/ 2;\n        if (sortedUnique[mid] == v) return mid + 1;\n\
        \        if (sortedUnique[mid] < v) low = mid + 1;\n        else high = mid\
        \ - 1;\n      }\n      return -1;\n    }).toList();\n\n    List<int> bitCnt\
        \ = List.filled(l + 1, 0);\n    List<int> bitSum = List.filled(l + 1, 0);\n\n\
        \    void update(List<int> bit, int idx, int val) {\n      for (; idx <= l;\
        \ idx += idx & -idx) {\n        bit[idx] += val;\n      }\n    }\n\n    int\
        \ query(List<int> bit, int idx) {\n      int sum = 0;\n      for (; idx > 0;\
        \ idx -= idx & -idx) {\n        sum += bit[idx];\n      }\n      return sum;\n\
        \    }\n\n    int findKth(int target) {\n      int idx = 0;\n      for (int\
        \ i = 1 << 16; i > 0; i >>= 1) {\n        if (idx + i <= l && bitCnt[idx + i]\
        \ < target) {\n          idx += i;\n          target -= bitCnt[idx];\n     \
        \   }\n      }\n      return idx + 1;\n    }\n\n    List<int> costs = List.filled(n\
        \ - x + 1, 0);\n    for (int i = 0; i < n; i++) {\n      update(bitCnt, numIndices[i],\
        \ 1);\n      update(bitSum, numIndices[i], nums[i]);\n      if (i >= x) {\n\
        \        update(bitCnt, numIndices[i - x], -1);\n        update(bitSum, numIndices[i\
        \ - x], -nums[i - x]);\n      }\n      if (i >= x - 1) {\n        int medianIdx\
        \ = findKth(m_val);\n        int medianVal = sortedUnique[medianIdx - 1];\n\
        \        int countLessEqual = query(bitCnt, medianIdx);\n        int sumLessEqual\
        \ = query(bitSum, medianIdx);\n        int sumTotal = query(bitSum, l);\n  \
        \      int cost = (medianVal * countLessEqual - sumLessEqual) +\n          \
        \  ((sumTotal - sumLessEqual) - medianVal * (x - countLessEqual));\n       \
        \ costs[i - x + 1] = cost;\n      }\n    }\n\n    const int INF = 10000000000000000;\n\
        \    List<int> dp = List.filled(n + 1, INF);\n    dp[0] = 0;\n\n    for (int\
        \ j = 0; j < k; j++) {\n      List<int> nextDp = List.filled(n + 1, INF);\n\
        \      for (int i = 1; i <= n; i++) {\n        int res = nextDp[i - 1];\n  \
        \      if (i >= x && dp[i - x] != INF) {\n          int c = dp[i - x] + costs[i\
        \ - x];\n          if (c < res) res = c;\n        }\n        nextDp[i] = res;\n\
        \      }\n      dp = nextDp;\n    }\n\n    return dp[n];\n  }\n}"
      go: "func minOperations(nums []int, x int, k int) int64 {\n\tn := len(nums)\n\t\
        sortedUnique := make([]int, n)\n\tcopy(sortedUnique, nums)\n\timportSort(sortedUnique)\n\
        \n\tl := 0\n\tfor i := 1; i < len(sortedUnique); i++ {\n\t\tif sortedUnique[i]\
        \ != sortedUnique[l] {\n\t\t\tl++\n\t\t\tsortedUnique[l] = sortedUnique[i]\n\
        \t\t}\n\t}\n\tsortedUnique = sortedUnique[:l+1]\n\tmSize := len(sortedUnique)\n\
        \n\tnumIndices := make([]int, n)\n\tfor i, v := range nums {\n\t\tidx := 0\n\
        \t\tlow, high := 0, mSize-1\n\t\tfor low <= high {\n\t\t\tmid := (low + high)\
        \ / 2\n\t\t\tif sortedUnique[mid] == v {\n\t\t\t\tidx = mid + 1\n\t\t\t\tbreak\n\
        \t\t\t}\n\t\t\tif sortedUnique[mid] < v {\n\t\t\t\tlow = mid + 1\n\t\t\t} else\
        \ {\n\t\t\t\thigh = mid - 1\n\t\t\t}\n\t\t}\n\t\tnumIndices[i] = idx\n\t}\n\n\
        \tbitCnt := make([]int64, mSize+1)\n\tbitSum := make([]int64, mSize+1)\n\tupdate\
        \ := func(bit []int64, idx int, val int64) {\n\t\tfor ; idx <= mSize; idx +=\
        \ idx & -idx {\n\t\t\tbit[idx] += val\n\t\t}\n\t}\n\tquery := func(bit []int64,\
        \ idx int) int64 {\n\t\tvar res int64 = 0\n\t\tfor ; idx > 0; idx -= idx & -idx\
        \ {\n\t\t\tres += bit[idx]\n\t\t}\n\t\treturn res\n\t}\n\tfindKth := func(target\
        \ int64) int {\n\t\tidx := 0\n\t\tfor i := 1 << 16; i > 0; i >>= 1 {\n\t\t\t\
        if idx+i <= mSize && bitCnt[idx+i] < target {\n\t\t\t\tidx += i\n\t\t\t\ttarget\
        \ -= bitCnt[idx]\n\t\t\t}\n\t\t}\n\t\treturn idx + 1\n\t}\n\n\tcosts := make([]int64,\
        \ n-x+1)\n\tmPos := int64((x + 1) / 2)\n\tfor i := 0; i < n; i++ {\n\t\tupdate(bitCnt,\
        \ numIndices[i], 1)\n\t\tupdate(bitSum, numIndices[i], int64(nums[i]))\n\t\t\
        if i >= x {\n\t\t\tupdate(bitCnt, numIndices[i-x], -1)\n\t\t\tupdate(bitSum,\
        \ numIndices[i-x], int64(-nums[i-x]))\n\t\t}\n\t\tif i >= x-1 {\n\t\t\tmidIdx\
        \ := findKth(mPos)\n\t\t\tmedianVal := int64(sortedUnique[midIdx-1])\n\t\t\t\
        countLessEqual := query(bitCnt, midIdx)\n\t\t\tsumLessEqual := query(bitSum,\
        \ midIdx)\n\t\t\tsumTotal := query(bitSum, mSize)\n\t\t\tcost := (medianVal*countLessEqual\
        \ - sumLessEqual) + ((sumTotal - sumLessEqual) - medianVal*(int64(x)-countLessEqual))\n\
        \t\t\tcosts[i-x+1] = cost\n\t\t}\n\t}\n\n\tconst INF int64 = 1e16\n\tdp := make([]int64,\
        \ n+1)\n\tfor i := range dp {\n\t\tdp[i] = INF\n\t}\n\tdp[0] = 0\n\n\tfor j\
        \ := 0; j < k; j++ {\n\t\tnextDp := make([]int64, n+1)\n\t\tfor i := range nextDp\
        \ {\n\t\t\tnextDp[i] = INF\n\t\t}\n\t\tfor i := 1; i <= n; i++ {\n\t\t\tres\
        \ := nextDp[i-1]\n\t\t\tif i >= x && dp[i-x] != INF {\n\t\t\t\tc := dp[i-x]\
        \ + costs[i-x]\n\t\t\t\tif c < res {\n\t\t\t\t\tres = c\n\t\t\t\t}\n\t\t\t}\n\
        \t\t\tnextDp[i] = res\n\t\t}\n\t\tdp = nextDp\n\t}\n\treturn dp[n]\n}\n\nfunc\
        \ importSort(a []int) {\n\tfor i := 1; i < len(a); i++ {\n\t\tj := i\n\t\tfor\
        \ j > 0 && a[j] < a[j-1] {\n\t\t\ta[j], a[j-1] = a[j-1], a[j]\n\t\t\tj--\n\t\
        \t}\n\t}\n\timportFastSort(a)\n}\n\nfunc importFastSort(a []int) {\n\tif len(a)\
        \ < 20 {\n\t\tfor i := 1; i < len(a); i++ {\n\t\t\tfor j := i; j > 0 && a[j]\
        \ < a[j-1]; j-- {\n\t\t\t\ta[j], a[j-1] = a[j-1], a[j]\n\t\t\t}\n\t\t}\n\t\t\
        return\n\t}\n\tpivot := a[len(a)/2]\n\tleft, right := 0, len(a)-1\n\tfor left\
        \ <= right {\n\t\tfor a[left] < pivot { left++ }\n\t\tfor a[right] > pivot {\
        \ right-- }\n\t\tif left <= right {\n\t\t\ta[left], a[right] = a[right], a[left]\n\
        \t\t\tleft++\n\t\t\tright--\n\t\t}\n\t}\n\timportFastSort(a[:right+1])\n\timportFastSort(a[left:])\n\
        }"
      ruby: "def min_operations(nums, x, k)\n  n = nums.length\n  sorted_unique = nums.uniq.sort\n\
        \  l = sorted_unique.length\n\n  num_indices = nums.map { |v| sorted_unique.bsearch_index\
        \ { |val| val >= v } + 1 }\n\n  bit_cnt = Array.new(l + 1, 0)\n  bit_sum = Array.new(l\
        \ + 1, 0)\n\n  update = lambda do |bit, idx, val|\n    while idx <= l\n    \
        \  bit[idx] += val\n      idx += (idx & -idx)\n    end\n  end\n\n  query = lambda\
        \ do |bit, idx|\n    res = 0\n    while idx > 0\n      res += bit[idx]\n   \
        \   idx -= (idx & -idx)\n    end\n    res\n  end\n\n  find_kth = lambda do |target|\n\
        \    idx = 0\n    i = 1 << 16\n    while i > 0\n      if idx + i <= l && bit_cnt[idx\
        \ + i] < target\n        idx += i\n        target -= bit_cnt[idx]\n      end\n\
        \      i >>= 1\n    end\n    idx + 1\n  end\n\n  costs = Array.new(n - x + 1)\n\
        \  m_pos = (x + 1) / 2\n\n  (0...n).each do |i|\n    update.call(bit_cnt, num_indices[i],\
        \ 1)\n    update.call(bit_sum, num_indices[i], nums[i])\n\n    if i >= x\n \
        \     update.call(bit_cnt, num_indices[i - x], -1)\n      update.call(bit_sum,\
        \ num_indices[i - x], -nums[i - x])\n    end\n\n    if i >= x - 1\n      mid_idx\
        \ = find_kth.call(m_pos)\n      m_val = sorted_unique[mid_idx - 1]\n      count_le\
        \ = query.call(bit_cnt, mid_idx)\n      sum_le = query.call(bit_sum, mid_idx)\n\
        \      sum_total = query.call(bit_sum, l)\n\n      cost = (m_val * count_le\
        \ - sum_le) + (sum_total - sum_le - m_val * (x - count_le))\n      costs[i -\
        \ x + 1] = cost\n    end\n  end\n\n  inf = 10**16\n  dp = Array.new(n + 1, inf)\n\
        \  dp[0] = 0\n\n  k.times do\n    next_dp = Array.new(n + 1, inf)\n    i = 1\n\
        \    while i <= n\n      res = next_dp[i - 1]\n      if i >= x && dp[i - x]\
        \ != inf\n        c = dp[i - x] + costs[i - x]\n        res = c if c < res\n\
        \      end\n      next_dp[i] = res\n      i += 1\n    end\n    dp = next_dp\n\
        \  end\n\n  dp[n]\nend"
      scala: "object Solution {\n  def minOperations(nums: Array[Int], x: Int, k: Int):\
        \ Long = {\n    val n = nums.length\n    val sortedUnique = nums.distinct.sorted\n\
        \    val l = sortedUnique.length\n\n    def binarySearch(target: Int): Int =\
        \ {\n      var low = 0\n      var high = l - 1\n      while (low <= high) {\n\
        \        val mid = (low + high) / 2\n        if (sortedUnique(mid) == target)\
        \ return mid + 1\n        if (sortedUnique(mid) < target) low = mid + 1\n  \
        \      else high = mid - 1\n      }\n      -1\n    }\n\n    val numIndices =\
        \ nums.map(binarySearch)\n    val bitCnt = new Array[Long](l + 1)\n    val bitSum\
        \ = new Array[Long](l + 1)\n\n    def update(bit: Array[Long], i: Int, v: Long):\
        \ Unit = {\n      var idx = i\n      while (idx <= l) {\n        bit(idx) +=\
        \ v\n        idx += (idx & -idx)\n      }\n    }\n\n    def query(bit: Array[Long],\
        \ i: Int): Long = {\n      var idx = i\n      var sum = 0L\n      while (idx\
        \ > 0) {\n        sum += bit(idx)\n        idx -= (idx & -idx)\n      }\n  \
        \    sum\n    }\n\n    def findKth(targetValue: Long): Int = {\n      var idx\
        \ = 0\n      var target = targetValue\n      var i = 1 << 16\n      while (i\
        \ > 0) {\n        if (idx + i <= l && bitCnt(idx + i) < target) {\n        \
        \  idx += i\n          target -= bitCnt(idx)\n        }\n        i >>= 1\n \
        \     }\n      idx + 1\n    }\n\n    val costs = new Array[Long](n - x + 1)\n\
        \    val mPos = (x + 1) / 2\n\n    for (i <- 0 until n) {\n      update(bitCnt,\
        \ numIndices(i), 1L)\n      update(bitSum, numIndices(i), nums(i).toLong)\n\
        \      if (i >= x) {\n        update(bitCnt, numIndices(i - x), -1L)\n     \
        \   update(bitSum, numIndices(i - x), -nums(i - x).toLong)\n      }\n      if\
        \ (i >= x - 1) {\n        val midIdx = findKth(mPos.toLong)\n        val mVal\
        \ = sortedUnique(midIdx - 1).toLong\n        val countLE = query(bitCnt, midIdx)\n\
        \        val sumLE = query(bitSum, midIdx)\n        val sumTotal = query(bitSum,\
        \ l)\n        val cost = (mVal * countLE - sumLE) + (sumTotal - sumLE - mVal\
        \ * (x - countLE))\n        costs(i - x + 1) = cost\n      }\n    }\n\n    val\
        \ INF = 10000000000000000L\n    var dp = Array.fill(n + 1)(INF)\n    dp(0) =\
        \ 0L\n\n    for (_ <- 0 until k) {\n      val nextDp = Array.fill(n + 1)(INF)\n\
        \      var i = 1\n      while (i <= n) {\n        var res = nextDp(i - 1)\n\
        \        if (i >= x && dp(i - x) != INF) {\n          val c = dp(i - x) + costs(i\
        \ - x)\n          if (c < res) res = c\n        }\n        nextDp(i) = res\n\
        \        i += 1\n      }\n      dp = nextDp\n    }\n    dp(n)\n  }\n}"
      rust: "impl Solution {\n    pub fn min_operations(nums: Vec<i32>, x: i32, k: i32)\
        \ -> i64 {\n        let n = nums.len();\n        let x = x as usize;\n     \
        \   let k = k as usize;\n\n        let mut sorted_unique = nums.clone();\n \
        \       sorted_unique.sort_unstable();\n        sorted_unique.dedup();\n   \
        \     let n_unique = sorted_unique.len();\n\n        let mut val_to_idx = std::collections::HashMap::with_capacity(n_unique);\n\
        \        for (i, &v) in sorted_unique.iter().enumerate() {\n            val_to_idx.insert(v,\
        \ i + 1);\n        }\n\n        let mut bit_count = vec![0; n_unique + 1];\n\
        \        let mut bit_sum = vec![0i64; n_unique + 1];\n\n        fn update_count(bit:\
        \ &mut [i32], mut idx: usize, delta: i32, n: usize) {\n            while idx\
        \ <= n {\n                bit[idx] += delta;\n                idx += idx & idx.wrapping_neg();\n\
        \            }\n        }\n\n        fn update_sum(bit: &mut [i64], mut idx:\
        \ usize, delta: i64, n: usize) {\n            while idx <= n {\n           \
        \     bit[idx] += delta;\n                idx += idx & idx.wrapping_neg();\n\
        \            }\n        }\n\n        fn query_count(bit: &[i32], mut idx: usize)\
        \ -> i32 {\n            let mut sum = 0;\n            while idx > 0 {\n    \
        \            sum += bit[idx];\n                idx -= idx & idx.wrapping_neg();\n\
        \            }\n            sum\n        }\n\n        fn query_sum(bit: &[i64],\
        \ mut idx: usize) -> i64 {\n            let mut sum = 0;\n            while\
        \ idx > 0 {\n                sum += bit[idx];\n                idx -= idx &\
        \ idx.wrapping_neg();\n            }\n            sum\n        }\n\n       \
        \ fn get_kth(bit: &[i32], mut k: i32, n_unique: usize) -> usize {\n        \
        \    let mut idx = 0;\n            let mut i = 1;\n            while i * 2 <=\
        \ n_unique { i *= 2; }\n            while i > 0 {\n                if idx +\
        \ i <= n_unique {\n                    let val = bit[idx + i];\n           \
        \         if val < k {\n                        idx += i;\n                \
        \        k -= val;\n                    }\n                }\n             \
        \   i >>= 1;\n            }\n            idx + 1\n        }\n\n        let mut\
        \ costs = vec![0i64; n - x + 1];\n        let mut window_sum = 0i64;\n     \
        \   for i in 0..n {\n            let v = nums[i];\n            let idx = *val_to_idx.get(&v).unwrap();\n\
        \            update_count(&mut bit_count, idx, 1, n_unique);\n            update_sum(&mut\
        \ bit_sum, idx, v as i64, n_unique);\n            window_sum += v as i64;\n\n\
        \            if i >= x {\n                let old_v = nums[i - x];\n       \
        \         let old_idx = *val_to_idx.get(&old_v).unwrap();\n                update_count(&mut\
        \ bit_count, old_idx, -1, n_unique);\n                update_sum(&mut bit_sum,\
        \ old_idx, -(old_v as i64), n_unique);\n                window_sum -= old_v\
        \ as i64;\n            }\n\n            if i >= x - 1 {\n                let\
        \ mid_count = ((x + 1) / 2) as i32;\n                let mid_idx = get_kth(&bit_count,\
        \ mid_count, n_unique);\n                let median_val = sorted_unique[mid_idx\
        \ - 1] as i64;\n                let count_low = query_count(&bit_count, mid_idx)\
        \ as i64;\n                let sum_low = query_sum(&bit_sum, mid_idx);\n   \
        \             let count_high = x as i64 - count_low;\n                let sum_high\
        \ = window_sum - sum_low;\n                costs[i - x + 1] = (count_low * median_val\
        \ - sum_low) + (sum_high - count_high * median_val);\n            }\n      \
        \  }\n\n        let inf = 1e16 as i64;\n        let mut prev_dp = vec![0i64;\
        \ n + 1];\n        for j in 1..=k {\n            let mut curr_dp = vec![inf;\
        \ n + 1];\n            for i in (j * x)..=n {\n                curr_dp[i] =\
        \ curr_dp[i - 1].min(prev_dp[i - x] + costs[i - x]);\n            }\n      \
        \      prev_dp = curr_dp;\n        }\n\n        prev_dp[n]\n    }\n}"
      racket: "(define/contract (min-operations nums x k)\n  (-> (listof exact-integer?)\
        \ exact-integer? exact-integer? exact-integer?)\n  (let* ([n (length nums)]\n\
        \         [nums-vec (list->vector nums)]\n         [sorted-unique (list->vector\
        \ (sort (remove-duplicates nums) <))]\n         [n-unique (vector-length sorted-unique)]\n\
        \         [val-to-idx (make-hash)])\n    (for ([i (in-range n-unique)])\n  \
        \    (hash-set! val-to-idx (vector-ref sorted-unique i) (+ i 1)))\n    (define\
        \ bit-count (make-vector (+ n-unique 1) 0))\n    (define bit-sum (make-vector\
        \ (+ n-unique 1) 0))\n    (define (update! bit idx delta max-idx)\n      (let\
        \ loop ((i idx))\n        (when (<= i max-idx)\n          (vector-set! bit i\
        \ (+ (vector-ref bit i) delta))\n          (loop (+ i (bitwise-and i (- i)))))))\n\
        \    (define (query bit idx)\n      (let loop ((i idx) (s 0))\n        (if (<=\
        \ i 0) s (loop (- i (bitwise-and i (- i))) (+ s (vector-ref bit i))))))\n  \
        \  (define (get-kth bit target-k)\n      (let* ([max-pow (let p-loop ([p 1])\
        \ (if (<= (* p 2) n-unique) (p-loop (* p 2)) p))])\n        (let loop ((idx\
        \ 0) (cur-k target-k) (i max-pow))\n          (if (zero? i)\n              (+\
        \ idx 1)\n              (let ((next-idx (+ idx i)))\n                (if (and\
        \ (<= next-idx n-unique) (< (vector-ref bit next-idx) cur-k))\n            \
        \        (loop next-idx (- cur-k (vector-ref bit next-idx)) (arithmetic-shift\
        \ i -1))\n                    (loop idx cur-k (arithmetic-shift i -1))))))))\n\
        \    (define costs (make-vector (+ (- n x) 1) 0))\n    (let ([window-sum 0])\n\
        \      (for ([i (in-range n)])\n        (let* ([v (vector-ref nums-vec i)]\n\
        \               [idx (hash-ref val-to-idx v)])\n          (update! bit-count\
        \ idx 1 n-unique)\n          (update! bit-sum idx v n-unique)\n          (set!\
        \ window-sum (+ window-sum v))\n          (when (>= i x)\n            (let*\
        \ ([old-v (vector-ref nums-vec (- i x))]\n                   [old-idx (hash-ref\
        \ val-to-idx old-v)])\n              (update! bit-count old-idx -1 n-unique)\n\
        \              (update! bit-sum old-idx (- old-v) n-unique)\n              (set!\
        \ window-sum (- window-sum old-v))))\n          (when (>= i (- x 1))\n     \
        \       (let* ([mid-count (quotient (+ x 1) 2)]\n                   [mid-idx\
        \ (get-kth bit-count mid-count)]\n                   [median (vector-ref sorted-unique\
        \ (- mid-idx 1))]\n                   [count-low (query bit-count mid-idx)]\n\
        \                   [sum-low (query bit-sum mid-idx)]\n                   [count-high\
        \ (- x count-low)]\n                   [sum-high (- window-sum sum-low)])\n\
        \              (vector-set! costs (+ (- i x) 1) (+ (- (* count-low median) sum-low)\
        \ (- sum-high (* count-high median)))))))))\n    (define inf 10000000000000000)\n\
        \    (define prev-dp (make-vector (+ n 1) 0))\n    (for ([j (in-range 1 (+ k\
        \ 1))])\n      (define curr-dp (make-vector (+ n 1) inf))\n      (for ([i (in-range\
        \ (* j x) (+ n 1))])\n        (vector-set! curr-dp i (min (vector-ref curr-dp\
        \ (- i 1))\n                                    (+ (vector-ref prev-dp (- i\
        \ x)) (vector-ref costs (- i x))))))\n      (set! prev-dp curr-dp))\n    (vector-ref\
        \ prev-dp n)))"
      erlang: "-spec min_operations(Nums :: [integer()], X :: integer(), K :: integer())\
        \ -> integer().\nmin_operations(Nums, X, K) ->\n    N = length(Nums),\n    NumsVec\
        \ = list_to_tuple(Nums),\n    UniqueSorted = lists:usort(Nums),\n    NUnique\
        \ = length(UniqueSorted),\n    ValToIdx = maps:from_list(lists:zip(UniqueSorted,\
        \ lists:seq(1, NUnique))),\n    BitCount = ets:new(bit_count, [set, public]),\n\
        \    BitSum = ets:new(bit_sum, [set, public]),\n    ets:insert(BitCount, [{I,\
        \ 0} || I <- lists:seq(1, NUnique)]),\n    ets:insert(BitSum, [{I, 0} || I <-\
        \ lists:seq(1, NUnique)]),\n    CostsTab = ets:new(costs, [set, public]),\n\
        \    MaxPow = get_max_pow2(NUnique),\n    fold_costs(0, 0, N, X, NUnique, NumsVec,\
        \ ValToIdx, BitCount, BitSum, UniqueSorted, MaxPow, CostsTab),\n    Inf = 1000000000000000,\n\
        \    PrevDP = array:new([{size, N + 1}, {default, 0}]),\n    FinalDP = lists:foldl(fun(J,\
        \ AccDP) ->\n        CurrDP = array:new([{size, N + 1}, {default, Inf}]),\n\
        \        update_dp(J * X, J * X, N, X, AccDP, CurrDP, CostsTab)\n    end, PrevDP,\
        \ lists:seq(1, K)),\n    array:get(N, FinalDP).\n\nget_max_pow2(N) ->\n    get_max_pow2_inner(1,\
        \ N).\nget_max_pow2_inner(P, N) when P * 2 =< N -> get_max_pow2_inner(P * 2,\
        \ N);\nget_max_pow2_inner(P, _) -> P.\n\nupdate_bit(Tab, Idx, Delta, Max) ->\n\
        \    case Idx =< Max of\n        true ->\n            ets:update_counter(Tab,\
        \ Idx, Delta),\n            update_bit(Tab, Idx + (Idx band -Idx), Delta, Max);\n\
        \        false -> ok\n    end.\n\nquery_bit(Tab, Idx) ->\n    query_bit_inner(Tab,\
        \ Idx, 0).\nquery_bit_inner(_, 0, Sum) -> Sum;\nquery_bit_inner(Tab, Idx, Sum)\
        \ ->\n    query_bit_inner(Tab, Idx - (Idx band -Idx), Sum + ets:lookup_element(Tab,\
        \ Idx, 2)).\n\nget_kth(Tab, K, MaxIdx, MaxPow) ->\n    get_kth_inner(Tab, K,\
        \ 0, MaxPow, MaxIdx).\nget_kth_inner(_Tab, _K, Idx, 0, _MaxIdx) -> Idx + 1;\n\
        get_kth_inner(Tab, K, Idx, Step, MaxIdx) ->\n    NextIdx = Idx + Step,\n   \
        \ case NextIdx =< MaxIdx of\n        true ->\n            Val = ets:lookup_element(Tab,\
        \ NextIdx, 2),\n            case Val < K of\n                true -> get_kth_inner(Tab,\
        \ K - Val, NextIdx, Step div 2, MaxIdx);\n                false -> get_kth_inner(Tab,\
        \ K, Idx, Step div 2, MaxIdx)\n            end;\n        false ->\n        \
        \    get_kth_inner(Tab, K, Idx, Step div 2, MaxIdx)\n    end.\n\nfold_costs(I,\
        \ WindowSum, N, X, NUnique, NumsVec, ValToIdx, BitCount, BitSum, UniqueSorted,\
        \ MaxPow, CostsTab) when I < N ->\n    V = element(I + 1, NumsVec),\n    Idx\
        \ = maps:get(V, ValToIdx),\n    update_bit(BitCount, Idx, 1, NUnique),\n   \
        \ update_bit(BitSum, Idx, V, NUnique),\n    NewSum = WindowSum + V,\n    FinalSum\
        \ = if I >= X ->\n        OldV = element(I - X + 1, NumsVec),\n        OldIdx\
        \ = maps:get(OldV, ValToIdx),\n        update_bit(BitCount, OldIdx, -1, NUnique),\n\
        \        update_bit(BitSum, OldIdx, -OldV, NUnique),\n        NewSum - OldV;\n\
        \        true -> NewSum\n    end,\n    if I >= X - 1 ->\n        MidCount =\
        \ (X + 1) div 2,\n        MidIdx = get_kth(BitCount, MidCount, NUnique, MaxPow),\n\
        \        Median = lists:nth(MidIdx, UniqueSorted),\n        CountLow = query_bit(BitCount,\
        \ MidIdx),\n        SumLow = query_bit(BitSum, MidIdx),\n        CountHigh =\
        \ X - CountLow,\n        SumHigh = FinalSum - SumLow,\n        Cost = (CountLow\
        \ * Median - SumLow) + (SumHigh - CountHigh * Median),\n        ets:insert(CostsTab,\
        \ {I - X + 1, Cost});\n        true -> ok\n    end,\n    fold_costs(I + 1, FinalSum,\
        \ N, X, NUnique, NumsVec, ValToIdx, BitCount, BitSum, UniqueSorted, MaxPow,\
        \ CostsTab);\nfold_costs(_, _, _, _, _, _, _, _, _, _, _, _) -> ok.\n\nupdate_dp(I,\
        \ JX, N, X, PrevDP, CurrDP, CostsTab) when I =< N ->\n    PrevVal = if I > JX\
        \ -> array:get(I - 1, CurrDP); true -> 1000000000000000 end,\n    Option = array:get(I\
        \ - X, PrevDP) + ets:lookup_element(CostsTab, I - X, 2),\n    NewCurrDP = array:set(I,\
        \ min(PrevVal, Option), CurrDP),\n    update_dp(I + 1, JX, N, X, PrevDP, NewCurrDP,\
        \ CostsTab);\nupdate_dp(_, _, _, _, _, CurrDP, _) -> CurrDP."
      elixir: "defmodule Solution do\n  import Bitwise\n\n  @spec min_operations(nums\
        \ :: [integer], x :: integer, k :: integer) :: integer\n  def min_operations(nums,\
        \ x, k) do\n    n = length(nums)\n    nums_vec = List.to_tuple(nums)\n    unique_sorted\
        \ = Enum.uniq(nums) |> Enum.sort()\n    n_unique = length(unique_sorted)\n \
        \   val_to_idx = unique_sorted |> Enum.with_index(1) |> Enum.into(%{})\n   \
        \ bit_count = :ets.new(:bit_count, [:set, :public])\n    bit_sum = :ets.new(:bit_sum,\
        \ [:set, :public])\n    :ets.insert(bit_count, for(i <- 1..n_unique, do: {i,\
        \ 0}))\n    :ets.insert(bit_sum, for(i <- 1..n_unique, do: {i, 0}))\n    costs_tab\
        \ = :ets.new(:costs, [:set, :public])\n    max_pow = get_max_pow2(n_unique)\n\
        \n    fold_costs(0, 0, n, x, n_unique, nums_vec, val_to_idx, bit_count, bit_sum,\
        \ List.to_tuple(unique_sorted), max_pow, costs_tab)\n\n    inf = 10_000_000_000_000_000\n\
        \    prev_dp = :array.new(size: n + 1, default: 0)\n\n    final_dp = Enum.reduce(1..k,\
        \ prev_dp, fn j, acc_dp ->\n      curr_dp = :array.new(size: n + 1, default:\
        \ inf)\n      update_dp(j * x, j * x, n, x, acc_dp, curr_dp, costs_tab, inf)\n\
        \    end)\n\n    :array.get(n, final_dp)\n  end\n\n  defp get_max_pow2(n), do:\
        \ get_max_pow2_inner(1, n)\n  defp get_max_pow2_inner(p, n) when p * 2 <= n,\
        \ do: get_max_pow2_inner(p * 2, n)\n  defp get_max_pow2_inner(p, _), do: p\n\
        \n  defp update_bit(tab, idx, delta, max) when idx <= max do\n    :ets.update_counter(tab,\
        \ idx, delta)\n    update_bit(tab, idx + (idx &&& -idx), delta, max)\n  end\n\
        \  defp update_bit(_, _, _, _), do: :ok\n\n  defp query_bit(tab, idx), do: query_bit_inner(tab,\
        \ idx, 0)\n  defp query_bit_inner(_, 0, sum), do: sum\n  defp query_bit_inner(tab,\
        \ idx, sum), do: query_bit_inner(tab, idx - (idx &&& -idx), sum + :ets.lookup_element(tab,\
        \ idx, 2))\n\n  defp get_kth(tab, k, max_idx, max_pow), do: get_kth_inner(tab,\
        \ k, 0, max_pow, max_idx)\n  defp get_kth_inner(_, _, idx, 0, _), do: idx +\
        \ 1\n  defp get_kth_inner(tab, k, idx, step, max_idx) do\n    next_idx = idx\
        \ + step\n    if next_idx <= max_idx do\n      val = :ets.lookup_element(tab,\
        \ next_idx, 2)\n      if val < k, do: get_kth_inner(tab, k - val, next_idx,\
        \ div(step, 2), max_idx), else: get_kth_inner(tab, k, idx, div(step, 2), max_idx)\n\
        \    else\n      get_kth_inner(tab, k, idx, div(step, 2), max_idx)\n    end\n\
        \  end\n\n  defp fold_costs(i, window_sum, n, x, n_unique, nums_vec, val_to_idx,\
        \ bit_count, bit_sum, unique_tuple, max_pow, costs_tab) when i < n do\n    v\
        \ = elem(nums_vec, i)\n    idx = Map.get(val_to_idx, v)\n    update_bit(bit_count,\
        \ idx, 1, n_unique)\n    update_bit(bit_sum, idx, v, n_unique)\n    new_sum\
        \ = window_sum + v\n    final_sum = if i >= x do\n      old_v = elem(nums_vec,\
        \ i - x)\n      old_idx = Map.get(val_to_idx, old_v)\n      update_bit(bit_count,\
        \ old_idx, -1, n_unique)\n      update_bit(bit_sum, old_idx, -old_v, n_unique)\n\
        \      new_sum - old_v\n    else\n      new_sum\n    end\n    if i >= x - 1\
        \ do\n      mid_count = div(x + 1, 2)\n      mid_idx = get_kth(bit_count, mid_count,\
        \ n_unique, max_pow)\n      median = elem(unique_tuple, mid_idx - 1)\n     \
        \ count_low = query_bit(bit_count, mid_idx)\n      sum_low = query_bit(bit_sum,\
        \ mid_idx)\n      count_high = x - count_low\n      sum_high = final_sum - sum_low\n\
        \      cost = (count_low * median - sum_low) + (sum_high - count_high * median)\n\
        \      :ets.insert(costs_tab, {i - x + 1, cost})\n    end\n    fold_costs(i\
        \ + 1, final_sum, n, x, n_unique, nums_vec, val_to_idx, bit_count, bit_sum,\
        \ unique_tuple, max_pow, costs_tab)\n  end\n  defp fold_costs(_, _, _, _, _,\
        \ _, _, _, _, _, _, _), do: :ok\n\n  defp update_dp(i, jx, n, x, prev_dp, curr_dp,\
        \ costs_tab, inf) when i <= n do\n    prev_val = if i > jx, do: :array.get(i\
        \ - 1, curr_dp), else: inf\n    option = :array.get(i - x, prev_dp) + :ets.lookup_element(costs_tab,\
        \ i - x, 2)\n    new_curr_dp = :array.set(i, Enum.min([prev_val, option]), curr_dp)\n\
        \    update_dp(i + 1, jx, n, x, prev_dp, new_curr_dp, costs_tab, inf)\n  end\n\
        \  defp update_dp(_, _, _, _, _, curr_dp, _, _), do: curr_dp\nend"
    approach: 'The optimal target value to make all elements within a subarray equal
      is its median, as it minimizes the sum of absolute differences. We first precalculate
      the minimum operations (cost) for every possible subarray of size exactly $x$
      in $O(n \log n)$ time. This is achieved by using a sliding window and maintaining
      two Fenwick trees (one for frequency counts and one for prefix sums) to find the
      median and calculate the cost via the formula $\sum |nums[i] - M| = (\sum_{x_i
      > M} x_i - \text{count}_{x_i > M} \cdot M) + (\text{count}_{x_i < M} \cdot M -
      \sum_{x_i < M} x_i)$. Coordinate compression is used to map the large values of
      $nums$ to a range suitable for the Fenwick tree.


      After precalculating the costs for all $n-x+1$ subarrays, we utilize dynamic programming
      to find the minimum cost to select at least $k$ non-overlapping subarrays. We
      define $dp[j][i]$ as the minimum cost to select $j$ non-overlapping subarrays
      from the first $i$ elements. The state transition is $dp[j][i] = \min(dp[j][i-1],
      dp[j-1][i-x] + \text{cost}[i-x])$, which ensures that the selected subarrays are
      of size exactly $x$ and do not overlap. The space complexity is optimized to $O(n)$
      by observing that each state $j$ only depends on the previous row $j-1$. Given
      the constraints $n \le 10^5$ and $k \le 15$, this $O(nk + n \log n)$ algorithm
      efficiently finds the global minimum cost.'
    time_complexity: O(n log n + nk) where $n$ is the length of the array and $k$ is
      the number of subarrays. Precalculating the median costs for all windows using
      coordinate compression and Fenwick trees takes $O(n \log n)$, and the dynamic
      programming step takes $O(nk)$.
    space_complexity: O(n) for storing the input array, the precalculated costs, coordinate
      mapping, the Fenwick trees, and the optimized DP table rows.
    elapsed_time: 405.3378977775574
    model: gemini-3-flash-preview
    generated_at: '2026-11-04 04:19:04 '
---

## Problem #3505: Minimum Operations to Make Elements Within K Subarrays Equal

**Difficulty:** Hard

**Topics:** Array, Hash Table, Math, Dynamic Programming, Sliding Window, Heap (Priority Queue)

## Problem Description

<p>You are given an integer array <code>nums</code> and two integers, <code>x</code> and <code>k</code>. You can perform the following operation any number of times (<strong>including zero</strong>):</p>

<ul>
	<li>Increase or decrease any element of <code>nums</code> by 1.</li>
</ul>

<p>Return the <strong>minimum</strong> number of operations needed to have <strong>at least</strong> <code>k</code> <em>non-overlapping <span data-keyword="subarray-nonempty">subarrays</span></em> of size <strong>exactly</strong> <code>x</code> in <code>nums</code>, where all elements within each subarray are equal.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [5,-2,1,3,7,3,6,4,-1], x = 3, k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">8</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Use 3 operations to add 3 to <code>nums[1]</code> and use 2 operations to subtract 2 from <code>nums[3]</code>. The resulting array is <code>[5, 1, 1, 1, 7, 3, 6, 4, -1]</code>.</li>
	<li>Use 1 operation to add 1 to <code>nums[5]</code> and use 2 operations to subtract 2 from <code>nums[6]</code>. The resulting array is <code>[5, 1, 1, 1, 7, 4, 4, 4, -1]</code>.</li>
	<li>Now, all elements within each subarray <code>[1, 1, 1]</code> (from indices 1 to 3) and <code>[4, 4, 4]</code> (from indices 5 to 7) are equal. Since 8 total operations were used, 8 is the output.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [9,-2,-2,-2,1,5], x = 2, k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Use 3 operations to subtract 3 from <code>nums[4]</code>. The resulting array is <code>[9, -2, -2, -2, -2, 5]</code>.</li>
	<li>Now, all elements within each subarray <code>[-2, -2]</code> (from indices 1 to 2) and <code>[-2, -2]</code> (from indices 3 to 4) are equal. Since 3 operations were used, 3 is the output.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>6</sup> &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
	<li><code>2 &lt;= x &lt;= nums.length</code></li>
	<li><code>1 &lt;= k &lt;= 15</code></li>
	<li><code>2 &lt;= k * x &lt;= nums.length</code></li>
</ul>


## Hints

1. Making every element of an x-sized window equal to its median is optimal.

2. Precalculate this for each window.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The optimal target value to make all elements within a subarray equal is its median, as it minimizes the sum of absolute differences. We first precalculate the minimum operations (cost) for every possible subarray of size exactly $x$ in $O(n \log n)$ time. This is achieved by using a sliding window and maintaining two Fenwick trees (one for frequency counts and one for prefix sums) to find the median and calculate the cost via the formula $\sum |nums[i] - M| = (\sum_{x_i > M} x_i - \text{count}_{x_i > M} \cdot M) + (\text{count}_{x_i < M} \cdot M - \sum_{x_i < M} x_i)$. Coordinate compression is used to map the large values of $nums$ to a range suitable for the Fenwick tree.

After precalculating the costs for all $n-x+1$ subarrays, we utilize dynamic programming to find the minimum cost to select at least $k$ non-overlapping subarrays. We define $dp[j][i]$ as the minimum cost to select $j$ non-overlapping subarrays from the first $i$ elements. The state transition is $dp[j][i] = \min(dp[j][i-1], dp[j-1][i-x] + \text{cost}[i-x])$, which ensures that the selected subarrays are of size exactly $x$ and do not overlap. The space complexity is optimized to $O(n)$ by observing that each state $j$ only depends on the previous row $j-1$. Given the constraints $n \le 10^5$ and $k \le 15$, this $O(nk + n \log n)$ algorithm efficiently finds the global minimum cost.

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
public:
    long long minOperations(vector<int>& nums, int x, int k) {
        int n = nums.size();
        vector<int> sortedUnique = nums;
        sort(sortedUnique.begin(), sortedUnique.end());
        sortedUnique.erase(unique(sortedUnique.begin(), sortedUnique.end()), sortedUnique.end());
        int u = sortedUnique.size();

        auto getRank = [&](int val) {
            return lower_bound(sortedUnique.begin(), sortedUnique.end(), val) - sortedUnique.begin() + 1;
        };

        vector<long long> bitCount(u + 1, 0), bitSum(u + 1, 0);
        auto update = [&](int idx, int val, int cnt) {
            for (; idx <= u; idx += idx & -idx) {
                bitCount[idx] += cnt;
                bitSum[idx] += (long long)cnt * val;
            }
        };

        auto query = [&](vector<long long>& bit, int idx) {
            long long res = 0;
            for (; idx > 0; idx -= idx & -idx) res += bit[idx];
            return res;
        };

        int h = 0;
        if (u > 0) while ((1 << (h + 1)) <= u) h++;

        vector<long long> costs(n - x + 1);
        long long totalSum = 0;
        for (int i = 0; i < n; ++i) {
            totalSum += nums[i];
            update(getRank(nums[i]), nums[i], 1);
            if (i >= x) {
                totalSum -= nums[i - x];
                update(getRank(nums[i - x]), nums[i - x], -1);
            }
            if (i >= x - 1) {
                int target = (x + 1) / 2, idx = 0;
                for (int j = h; j >= 0; j--) {
                    int next = idx + (1 << j);
                    if (next <= u && bitCount[next] < target) {
                        idx = next;
                        target -= bitCount[idx];
                    }
                }
                int medianRank = idx + 1;
                long long M = sortedUnique[medianRank - 1];
                long long numLess = query(bitCount, medianRank - 1);
                long long sumLess = query(bitSum, medianRank - 1);
                long long numUpToMedian = query(bitCount, medianRank);
                long long sumUpToMedian = query(bitSum, medianRank);
                long long numGreater = x - numUpToMedian;
                long long sumGreater = totalSum - sumUpToMedian;
                costs[i - x + 1] = (sumGreater - numGreater * M) + (numLess * M - sumLess);
            }
        }

        vector<long long> dp(n + 1, 0);
        long long INF = 1e16;
        for (int j = 1; j <= k; ++j) {
            vector<long long> next_dp(n + 1, INF);
            long long min_val = INF;
            for (int i = j * x; i <= n; ++i) {
                if (dp[i - x] + costs[i - x] < min_val) min_val = dp[i - x] + costs[i - x];
                next_dp[i] = min_val;
            }
            dp = next_dp;
        }
        return dp[n];
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
    public long minOperations(int[] nums, int x, int k) {
        int n = nums.length;
        int[] sortedUnique = nums.clone();
        Arrays.sort(sortedUnique);
        int u = 0;
        for (int i = 0; i < n; i++) {
            if (i == 0 || sortedUnique[i] != sortedUnique[i - 1]) sortedUnique[u++] = sortedUnique[i];
        }
        int[] uniqueArr = Arrays.copyOf(sortedUnique, u);

        long[] bitCount = new long[u + 1];
        long[] bitSum = new long[u + 1];
        long[] costs = new long[n - x + 1];
        long totalSum = 0;
        int h = 0;
        while ((1 << (h + 1)) <= u) h++;

        for (int i = 0; i < n; i++) {
            totalSum += nums[i];
            int rank = Arrays.binarySearch(uniqueArr, nums[i]) + 1;
            for (int idx = rank; idx <= u; idx += idx & -idx) {
                bitCount[idx] += 1;
                bitSum[idx] += nums[i];
            }
            if (i >= x) {
                totalSum -= nums[i - x];
                int oldRank = Arrays.binarySearch(uniqueArr, nums[i - x]) + 1;
                for (int idx = oldRank; idx <= u; idx += idx & -idx) {
                    bitCount[idx] -= 1;
                    bitSum[idx] -= nums[i - x];
                }
            }
            if (i >= x - 1) {
                int target = (x + 1) / 2, idx = 0, currTarget = target;
                for (int j = h; j >= 0; j--) {
                    int next = idx + (1 << j);
                    if (next <= u && bitCount[next] < currTarget) {
                        idx = next;
                        currTarget -= bitCount[idx];
                    }
                }
                int mRank = idx + 1;
                long M = uniqueArr[mRank - 1];
                long numL = 0, sumL = 0, numU = 0, sumU = 0;
                for (int r = mRank - 1; r > 0; r -= r & -r) { numL += bitCount[r]; sumL += bitSum[r]; }
                for (int r = mRank; r > 0; r -= r & -r) { numU += bitCount[r]; sumU += bitSum[r]; }
                long numG = x - numU, sumG = totalSum - sumU;
                costs[i - x + 1] = (sumG - numG * M) + (numL * M - sumL);
            }
        }

        long[] dp = new long[n + 1];
        long INF = (long) 1e16;
        for (int j = 1; j <= k; j++) {
            long[] next_dp = new long[n + 1];
            Arrays.fill(next_dp, INF);
            long min_val = INF;
            for (int i = j * x; i <= n; i++) {
                if (dp[i - x] + costs[i - x] < min_val) min_val = dp[i - x] + costs[i - x];
                next_dp[i] = min_val;
            }
            dp = next_dp;
        }
        return dp[n];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def minOperations(self, nums, x, k):
        n = len(nums)
        unique_vals = sorted(list(set(nums)))
        rank_map = {val: i + 1 for i, val in enumerate(unique_vals)}
        ranks = [rank_map[v] for v in nums]
        U = len(unique_vals)
        h = U.bit_length() - 1
        bit_count, bit_sum = [0] * (U + 1), [0] * (U + 1)
        costs = [0] * (n - x + 1)
        total_sum_window = 0

        for i in range(n):
            val, r = nums[i], ranks[i]
            total_sum_window += val
            curr_r = r
            while curr_r <= U:
                bit_count[curr_r] += 1
                bit_sum[curr_r] += val
                curr_r += curr_r & -curr_r
            if i >= x:
                old_val, old_r = nums[i - x], ranks[i - x]
                total_sum_window -= old_val
                curr_r = old_r
                while curr_r <= U:
                    bit_count[curr_r] -= 1
                    bit_sum[curr_r] -= old_val
                    curr_r += curr_r & -curr_r
            if i >= x - 1:
                idx, target = 0, (x + 1) // 2
                for j in range(h, -1, -1):
                    next_idx = idx + (1 << j)
                    if next_idx <= U and bit_count[next_idx] < target:
                        idx = next_idx
                        target -= bit_count[idx]
                m_rank = idx + 1
                m_val = unique_vals[m_rank - 1]
                num_up, sum_up, num_l, sum_l = 0, 0, 0, 0
                curr_r = m_rank
                while curr_r > 0:
                    num_up += bit_count[curr_r]
                    sum_up += bit_sum[curr_r]
                    curr_r -= curr_r & -curr_r
                curr_r = m_rank - 1
                while curr_r > 0:
                    num_l += bit_count[curr_r]
                    sum_l += bit_sum[curr_r]
                    curr_r -= curr_r & -curr_r
                num_g = x - num_up
                sum_g = total_sum_window - sum_up
                costs[i - x + 1] = (sum_g - num_g * m_val) + (num_l * m_val - sum_l)

        dp = [0] * (n + 1)
        INF = 10**16
        for j in range(1, k + 1):
            next_dp = [INF] * (n + 1)
            min_val = INF
            for i in range(j * x, n + 1):
                val_to_check = dp[i - x] + costs[i - x]
                if val_to_check < min_val: min_val = val_to_check
                next_dp[i] = min_val
            dp = next_dp
        return dp[n]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        unique_vals = sorted(list(set(nums)))
        num_unique = len(unique_vals)
        val_to_idx = {v: i + 1 for i, v in enumerate(unique_vals)}

        bit_count = [0] * (num_unique + 1)
        bit_sum = [0] * (num_unique + 1)

        def update(bit, idx, val):
            while idx <= num_unique:
                bit[idx] += val
                idx += idx & -idx

        def query(bit, idx):
            s = 0
            while idx > 0:
                s += bit[idx]
                idx -= idx & -idx
            return s

        def find_kth(target):
            idx = 0
            max_pow = 1 << 17
            for i in range(17, -1, -1):
                p = 1 << i
                next_idx = idx + p
                if next_idx <= num_unique and bit_count[next_idx] < target:
                    idx = next_idx
                    target -= bit_count[idx]
            return idx + 1

        costs = [0] * (n - x + 1)
        current_window_sum = 0
        for i in range(x):
            idx = val_to_idx[nums[i]]
            update(bit_count, idx, 1)
            update(bit_sum, idx, nums[i])
            current_window_sum += nums[i]

        m = (x + 1) // 2
        def get_cost():
            m_idx = find_kth(m)
            val_m = unique_vals[m_idx - 1]
            cnt_l = query(bit_count, m_idx)
            sum_l = query(bit_sum, m_idx)
            cnt_r = x - cnt_l
            sum_r = current_window_sum - sum_l
            return (cnt_l * val_m - sum_l) + (sum_r - cnt_r * val_m)

        costs[0] = get_cost()
        for i in range(1, n - x + 1):
            idx_rem = val_to_idx[nums[i - 1]]
            update(bit_count, idx_rem, -1)
            update(bit_sum, idx_rem, -nums[i - 1])
            idx_add = val_to_idx[nums[i + x - 1]]
            update(bit_count, idx_add, 1)
            update(bit_sum, idx_add, nums[i + x - 1])
            current_window_sum += nums[i + x - 1] - nums[i - 1]
            costs[i] = get_cost()

        dp = [0] * (n + 1)
        for j in range(1, k + 1):
            new_dp = [float('inf')] * (n + 1)
            for i in range(j * x, n + 1):
                new_dp[i] = new_dp[i - 1]
                option = dp[i - x] + costs[i - x]
                if option < new_dp[i]:
                    new_dp[i] = option
            dp = new_dp

        return int(dp[n])
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

int compare(const void* a, const void* b) {
    int arg1 = *(const int*)a;
    int arg2 = *(const int*)b;
    if (arg1 < arg2) return -1;
    if (arg1 > arg2) return 1;
    return 0;
}

void update(long long* bit, int idx, long long val, int n) {
    for (; idx <= n; idx += idx & -idx) {
        bit[idx] += val;
    }
}

long long query(long long* bit, int idx) {
    long long res = 0;
    for (; idx > 0; idx -= idx & -idx) {
        res += bit[idx];
    }
    return res;
}

int find_kth(long long* bit_count, int target, int n) {
    int idx = 0;
    for (int p = 1 << 17; p > 0; p >>= 1) {
        int next_idx = idx + p;
        if (next_idx <= n && bit_count[next_idx] < target) {
            idx = next_idx;
            target -= bit_count[idx];
        }
    }
    return idx + 1;
}

int find_val_idx(int* arr, int size, int val) {
    int low = 0, high = size - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] == val) return mid + 1;
        if (arr[mid] < val) low = mid + 1;
        else high = mid - 1;
    }
    return -1;
}

long long minOperations(int* nums, int numsSize, int x, int k) {
    int* sorted_nums = malloc(numsSize * sizeof(int));
    memcpy(sorted_nums, nums, numsSize * sizeof(int));
    qsort(sorted_nums, numsSize, sizeof(int), compare);

    int num_unique = 0;
    if (numsSize > 0) {
        num_unique = 1;
        for (int i = 1; i < numsSize; i++) {
            if (sorted_nums[i] != sorted_nums[i-1]) {
                sorted_nums[num_unique++] = sorted_nums[i];
            }
        }
    }

    long long* bit_count = calloc(num_unique + 1, sizeof(long long));
    long long* bit_sum = calloc(num_unique + 1, sizeof(long long));
    long long current_window_sum = 0;

    long long* costs = malloc((numsSize - x + 1) * sizeof(long long));
    int m = (x + 1) / 2;

    for (int i = 0; i < x; i++) {
        int idx = find_val_idx(sorted_nums, num_unique, nums[i]);
        update(bit_count, idx, 1, num_unique);
        update(bit_sum, idx, nums[i], num_unique);
        current_window_sum += nums[i];
    }

    for (int i = 0; i <= numsSize - x; i++) {
        if (i > 0) {
            int idx_rem = find_val_idx(sorted_nums, num_unique, nums[i - 1]);
            update(bit_count, idx_rem, -1, num_unique);
            update(bit_sum, idx_rem, -nums[i - 1], num_unique);
            int idx_add = find_val_idx(sorted_nums, num_unique, nums[i + x - 1]);
            update(bit_count, idx_add, 1, num_unique);
            update(bit_sum, idx_add, nums[i + x - 1], num_unique);
            current_window_sum += (long long)nums[i + x - 1] - nums[i - 1];
        }
        int m_idx = find_kth(bit_count, m, num_unique);
        long long val_m = sorted_nums[m_idx - 1];
        long long cnt_l = query(bit_count, m_idx);
        long long sum_l = query(bit_sum, m_idx);
        long long cnt_r = x - cnt_l;
        long long sum_r = current_window_sum - sum_l;
        costs[i] = (cnt_l * val_m - sum_l) + (sum_r - cnt_r * val_m);
    }

    long long* dp = malloc((numsSize + 1) * sizeof(long long));
    long long* next_dp = malloc((numsSize + 1) * sizeof(long long));
    for (int i = 0; i <= numsSize; i++) dp[i] = 0;

    for (int j = 1; j <= k; j++) {
        for (int i = 0; i <= numsSize; i++) next_dp[i] = LLONG_MAX;
        for (int i = j * x; i <= numsSize; i++) {
            next_dp[i] = next_dp[i - 1];
            if (dp[i - x] != LLONG_MAX) {
                long long option = dp[i - x] + costs[i - x];
                if (option < next_dp[i]) next_dp[i] = option;
            }
        }
        memcpy(dp, next_dp, (numsSize + 1) * sizeof(long long));
    }

    long long result = dp[numsSize];
    free(sorted_nums); free(bit_count); free(bit_sum); free(costs); free(dp); free(next_dp);
    return result;
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
    public long MinOperations(int[] nums, int x, int k) {
        int n = nums.Length;
        int[] uniqueVals = nums.Distinct().OrderBy(v => v).ToArray();
        int numUnique = uniqueVals.Length;

        long[] bitCount = new long[numUnique + 1];
        long[] bitSum = new long[numUnique + 1];

        void Update(long[] bit, int idx, long val) {
            for (; idx <= numUnique; idx += idx & -idx) {
                bit[idx] += val;
            }
        }

        long Query(long[] bit, int idx) {
            long res = 0;
            for (; idx > 0; idx -= idx & -idx) {
                res += bit[idx];
            }
            return res;
        }

        int FindKth(int target) {
            int idx = 0;
            for (int p = 1 << 17; p > 0; p >>= 1) {
                int nextIdx = idx + p;
                if (nextIdx <= numUnique && bitCount[nextIdx] < target) {
                    idx = nextIdx;
                    target -= (int)bitCount[idx];
                }
            }
            return idx + 1;
        }

        long[] costs = new long[n - x + 1];
        long currentWindowSum = 0;
        int m = (x + 1) / 2;

        for (int i = 0; i < x; i++) {
            int idx = Array.BinarySearch(uniqueVals, nums[i]) + 1;
            Update(bitCount, idx, 1);
            Update(bitSum, idx, nums[i]);
            currentWindowSum += nums[i];
        }

        for (int i = 0; i <= n - x; i++) {
            if (i > 0) {
                int idxRem = Array.BinarySearch(uniqueVals, nums[i - 1]) + 1;
                Update(bitCount, idxRem, -1);
                Update(bitSum, idxRem, -nums[i - 1]);
                int idxAdd = Array.BinarySearch(uniqueVals, nums[i + x - 1]) + 1;
                Update(bitCount, idxAdd, 1);
                Update(bitSum, idxAdd, nums[i + x - 1]);
                currentWindowSum += (long)nums[i + x - 1] - nums[i - 1];
            }
            int mIdx = FindKth(m);
            long valM = uniqueVals[mIdx - 1];
            long cntL = Query(bitCount, mIdx);
            long sumL = Query(bitSum, mIdx);
            long cntR = x - cntL;
            long sumR = currentWindowSum - sumL;
            costs[i] = (cntL * valM - sumL) + (sumR - cntR * valM);
        }

        long[] dp = new long[n + 1];
        for (int j = 1; j <= k; j++) {
            long[] nextDp = new long[n + 1];
            for (int i = 0; i <= n; i++) nextDp[i] = long.MaxValue;
            for (int i = j * x; i <= n; i++) {
                nextDp[i] = nextDp[i - 1];
                if (dp[i - x] != long.MaxValue) {
                    long option = dp[i - x] + costs[i - x];
                    if (option < nextDp[i]) nextDp[i] = option;
                }
            }
            dp = nextDp;
        }

        return dp[n];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[]} nums
 * @param {number} x
 * @param {number} k
 * @return {number}
 */
var minOperations = function(nums, x, k) {
    const n = nums.length;
    const uniqueVals = Array.from(new Set(nums)).sort((a, b) => a - b);
    const numUnique = uniqueVals.length;
    const valToIdx = new Map();
    for (let i = 0; i < numUnique; i++) {
        valToIdx.set(uniqueVals[i], i + 1);
    }

    const bitCount = new Float64Array(numUnique + 1);
    const bitSum = new Float64Array(numUnique + 1);

    function update(bit, idx, val) {
        while (idx <= numUnique) {
            bit[idx] += val;
            idx += idx & -idx;
        }
    }

    function query(bit, idx) {
        let s = 0;
        while (idx > 0) {
            s += bit[idx];
            idx -= idx & -idx;
        }
        return s;
    }

    function findKth(target) {
        let idx = 0;
        for (let p = 1 << 17; p > 0; p >>= 1) {
            let nextIdx = idx + p;
            if (nextIdx <= numUnique && bitCount[nextIdx] < target) {
                idx = nextIdx;
                target -= bitCount[idx];
            }
        }
        return idx + 1;
    }

    const costs = new Float64Array(n - x + 1);
    let currentWindowSum = 0;
    const m = Math.floor((x + 1) / 2);

    for (let i = 0; i < x; i++) {
        const idx = valToIdx.get(nums[i]);
        update(bitCount, idx, 1);
        update(bitSum, idx, nums[i]);
        currentWindowSum += nums[i];
    }

    for (let i = 0; i <= n - x; i++) {
        if (i > 0) {
            const idxRem = valToIdx.get(nums[i - 1]);
            update(bitCount, idxRem, -1);
            update(bitSum, idxRem, -nums[i - 1]);
            const idxAdd = valToIdx.get(nums[i + x - 1]);
            update(bitCount, idxAdd, 1);
            update(bitSum, idxAdd, nums[i + x - 1]);
            currentWindowSum += nums[i + x - 1] - nums[i - 1];
        }
        const mIdx = findKth(m);
        const valM = uniqueVals[mIdx - 1];
        const cntL = query(bitCount, mIdx);
        const sumL = query(bitSum, mIdx);
        const cntR = x - cntL;
        const sumR = currentWindowSum - sumL;
        costs[i] = (cntL * valM - sumL) + (sumR - cntR * valM);
    }

    let dp = new Float64Array(n + 1).fill(0);
    for (let j = 1; j <= k; j++) {
        const nextDp = new Float64Array(n + 1).fill(Infinity);
        for (let i = j * x; i <= n; i++) {
            nextDp[i] = nextDp[i - 1];
            const option = dp[i - x] + costs[i - x];
            if (option < nextDp[i]) nextDp[i] = option;
        }
        dp = nextDp;
    }

    return dp[n];
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minOperations(nums: number[], x: number, k: number): number {
    const n = nums.length;
    const unique = Array.from(new Set(nums)).sort((a, b) => a - b);
    const rankMap = new Map<number, number>();
    for (let i = 0; i < unique.length; i++) rankMap.set(unique[i], i + 1);
    const uniqueSize = unique.length;

    const bitCount = new Float64Array(uniqueSize + 1);
    const bitSum = new Float64Array(uniqueSize + 1);

    function update(bit: Float64Array, idx: number, delta: number) {
        for (; idx <= uniqueSize; idx += idx & -idx) {
            bit[idx] += delta;
        }
    }

    function query(bit: Float64Array, idx: number): number {
        let sum = 0;
        for (; idx > 0; idx -= idx & -idx) {
            sum += bit[idx];
        }
        return sum;
    }

    let stepStart = 1;
    while ((stepStart << 1) <= uniqueSize) stepStart <<= 1;

    function findKth(kVal: number): number {
        let pos = 0;
        let currentK = kVal;
        let step = stepStart;
        while (step > 0) {
            if (pos + step <= uniqueSize && bitCount[pos + step] < currentK) {
                pos += step;
                currentK -= bitCount[pos];
            }
            step >>= 1;
        }
        return pos + 1;
    }

    const costs = new Float64Array(n - x + 1);
    const m = Math.floor((x + 1) / 2);
    let currentTotalSum = 0;

    for (let i = 0; i < n; i++) {
        const val = nums[i];
        const r = rankMap.get(val)!;
        update(bitCount, r, 1);
        update(bitSum, r, val);
        currentTotalSum += val;

        if (i >= x) {
            const prevVal = nums[i - x];
            const pr = rankMap.get(prevVal)!;
            update(bitCount, pr, -1);
            update(bitSum, pr, -prevVal);
            currentTotalSum -= prevVal;
        }

        if (i >= x - 1) {
            const medianIdx = findKth(m);
            const medianVal = unique[medianIdx - 1];
            const countLow = query(bitCount, medianIdx);
            const sumLow = query(bitSum, medianIdx);
            const countHigh = x - countLow;
            const sumHigh = currentTotalSum - sumLow;
            costs[i - x + 1] = (countLow * medianVal - sumLow) + (sumHigh - countHigh * medianVal);
        }
    }

    const INF = Number.MAX_SAFE_INTEGER;
    let dp = new Float64Array(n + 1).fill(0);

    for (let i = 1; i <= k; i++) {
        const nextDp = new Float64Array(n + 1).fill(INF);
        for (let j = i * x; j <= n; j++) {
            nextDp[j] = Math.min(nextDp[j - 1], dp[j - x] + costs[j - x]);
        }
        dp = nextDp;
    }

    return dp[n];
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $x
     * @param Integer $k
     * @return Integer
     */
    function minOperations($nums, $x, $k) {
        $n = count($nums);
        $unique = array_unique($nums);
        sort($unique);
        $rankMap = [];
        foreach ($unique as $i => $val) {
            $rankMap[$val] = $i + 1;
        }
        $uniqueSize = count($unique);
        $bitCount = new SplFixedArray($uniqueSize + 1);
        $bitSum = new SplFixedArray($uniqueSize + 1);
        for ($i = 0; $i <= $uniqueSize; $i++) {
            $bitCount[$i] = 0;
            $bitSum[$i] = 0;
        }

        $update = function(&$bit, $idx, $delta) use ($uniqueSize) {
            for (; $idx <= $uniqueSize; $idx += $idx & -$idx) {
                $bit[$idx] += $delta;
            }
        };

        $query = function($bit, $idx) {
            $sum = 0;
            for (; $idx > 0; $idx -= $idx & -$idx) {
                $sum += $bit[$idx];
            }
            return $sum;
        };

        $stepStart = 1;
        while (($stepStart << 1) <= $uniqueSize) $stepStart <<= 1;

        $findKth = function($kVal) use ($bitCount, $uniqueSize, $stepStart) {
            $pos = 0;
            $step = $stepStart;
            while ($step > 0) {
                if ($pos + $step <= $uniqueSize && $bitCount[$pos + $step] < $kVal) {
                    $pos += $step;
                    $kVal -= $bitCount[$pos];
                }
                $step >>= 1;
            }
            return $pos + 1;
        };

        $costs = new SplFixedArray($n - $x + 1);
        $m = (int)(($x + 1) / 2);
        $currentTotalSum = 0;

        for ($i = 0; $i < $n; $i++) {
            $val = $nums[$i];
            $r = $rankMap[$val];
            $update($bitCount, $r, 1);
            $update($bitSum, $r, $val);
            $currentTotalSum += $val;

            if ($i >= $x) {
                $prevVal = $nums[$i - $x];
                $pr = $rankMap[$prevVal];
                $update($bitCount, $pr, -1);
                $update($bitSum, $pr, -$prevVal);
                $currentTotalSum -= $prevVal;
            }

            if ($i >= $x - 1) {
                $medianIdx = $findKth($m);
                $medianVal = $unique[$medianIdx - 1];
                $countLow = $query($bitCount, $medianIdx);
                $sumLow = $query($bitSum, $medianIdx);
                $countHigh = $x - $countLow;
                $sumHigh = $currentTotalSum - $sumLow;
                $costs[$i - $x + 1] = ($countLow * $medianVal - $sumLow) + ($sumHigh - $countHigh * $medianVal);
            }
        }

        $inf = 1e16;
        $dp = new SplFixedArray($n + 1);
        for ($i = 0; $i <= $n; $i++) $dp[$i] = 0;

        for ($i = 1; $i <= $k; $i++) {
            $nextDp = new SplFixedArray($n + 1);
            for ($j = 0; $j < $i * $x; $j++) $nextDp[$j] = $inf;
            for ($j = $i * $x; $j <= $n; $j++) {
                $opt1 = $nextDp[$j - 1];
                $opt2 = $dp[$j - $x] + $costs[$j - $x];
                $nextDp[$j] = $opt1 < $opt2 ? $opt1 : $opt2;
            }
            $dp = $nextDp;
        }

        return (int)$dp[$n];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minOperations(_ nums: [Int], _ x: Int, _ k: Int) -> Int {
        let n = nums.count
        let sortedUnique = Array(Set(nums)).sorted()
        let uniqueSize = sortedUnique.count
        var rankMap: [Int: Int] = [:]
        for (i, val) in sortedUnique.enumerated() {
            rankMap[val] = i + 1
        }

        var bitCount = [Int](repeating: 0, count: uniqueSize + 1)
        var bitSum = [Int](repeating: 0, count: uniqueSize + 1)

        func update(_ bit: inout [Int], _ idx: Int, _ delta: Int) {
            var i = idx
            while i <= uniqueSize {
                bit[i] += delta
                i += i & -i
            }
        }

        func query(_ bit: [Int], _ idx: Int) -> Int {
            var sum = 0
            var i = idx
            while i > 0 {
                sum += bit[i]
                i -= i & -i
            }
            return sum
        }

        var stepStart = 1
        while (stepStart << 1) <= uniqueSize { stepStart <<= 1 }

        func findKth(_ kVal: Int) -> Int {
            var pos = 0
            var curK = kVal
            var step = stepStart
            while step > 0 {
                if pos + step <= uniqueSize && bitCount[pos + step] < curK {
                    pos += step
                    curK -= bitCount[pos]
                }
                step >>= 1
            }
            return pos + 1
        }

        var costs = [Int](repeating: 0, count: n - x + 1)
        let m = (x + 1) / 2
        var currentTotalSum = 0

        for i in 0..<n {
            let val = nums[i]
            let r = rankMap[val]!
            update(&bitCount, r, 1)
            update(&bitSum, r, val)
            currentTotalSum += val

            if i >= x {
                let prevVal = nums[i - x]
                let pr = rankMap[prevVal]!
                update(&bitCount, pr, -1)
                update(&bitSum, pr, -prevVal)
                currentTotalSum -= prevVal
            }

            if i >= x - 1 {
                let medianIdx = findKth(m)
                let medianVal = sortedUnique[medianIdx - 1]
                let countLow = query(bitCount, medianIdx)
                let sumLow = query(bitSum, medianIdx)
                let countHigh = x - countLow
                let sumHigh = currentTotalSum - sumLow
                costs[i - x + 1] = (countLow * medianVal - sumLow) + (sumHigh - countHigh * medianVal)
            }
        }

        let inf = Int.max / 2
        var dp = [Int](repeating: 0, count: n + 1)

        for i in 1...k {
            var nextDp = [Int](repeating: inf, count: n + 1)
            for j in (i * x)...n {
                nextDp[j] = min(nextDp[j - 1], dp[j - x] + costs[j - x])
            }
            dp = nextDp
        }

        return dp[n]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minOperations(nums: IntArray, x: Int, k: Int): Long {
        val n = nums.size
        val sortedUnique = nums.distinct().sorted()
        val uniqueSize = sortedUnique.size
        val rankMap = mutableMapOf<Int, Int>()
        for (i in sortedUnique.indices) {
            rankMap[sortedUnique[i]] = i + 1
        }

        val bitCount = LongArray(uniqueSize + 1)
        val bitSum = LongArray(uniqueSize + 1)

        fun update(bit: LongArray, idx: Int, delta: Long) {
            var i = idx
            while (i <= uniqueSize) {
                bit[i] += delta
                i += i and -i
            }
        }

        fun query(bit: LongArray, idx: Int): Long {
            var sum = 0L
            var i = idx
            while (i > 0) {
                sum += bit[i]
                i -= i and -i
            }
            return sum
        }

        var stepStart = 1
        while ((stepStart shl 1) <= uniqueSize) stepStart = stepStart shl 1

        fun findKth(kVal: Long): Int {
            var pos = 0
            var curK = kVal
            var step = stepStart
            while (step > 0) {
                if (pos + step <= uniqueSize && bitCount[pos + step] < curK) {
                    pos += step
                    curK -= bitCount[pos]
                }
                step = step shr 1
            }
            return pos + 1
        }

        val costs = LongArray(n - x + 1)
        val m = (x + 1) / 2
        var currentTotalSum = 0L

        for (i in 0 until n) {
            val valAtI = nums[i]
            val r = rankMap[valAtI]!!
            update(bitCount, r, 1L)
            update(bitSum, r, valAtI.toLong())
            currentTotalSum += valAtI

            if (i >= x) {
                val prevVal = nums[i - x]
                val pr = rankMap[prevVal]!!
                update(bitCount, pr, -1L)
                update(bitSum, pr, -prevVal.toLong())
                currentTotalSum -= prevVal
            }

            if (i >= x - 1) {
                val medianIdx = findKth(m.toLong())
                val medianVal = sortedUnique[medianIdx - 1].toLong()
                val countLow = query(bitCount, medianIdx)
                val sumLow = query(bitSum, medianIdx)
                val countHigh = x.toLong() - countLow
                val sumHigh = currentTotalSum - sumLow
                costs[i - x + 1] = (countLow * medianVal - sumLow) + (sumHigh - countHigh * medianVal)
            }
        }

        val inf = Long.MAX_VALUE / 2
        var dp = LongArray(n + 1) { 0L }

        for (i in 1..k) {
            val nextDp = LongArray(n + 1) { inf }
            for (j in (i * x)..n) {
                nextDp[j] = Math.min(nextDp[j - 1], dp[j - x] + costs[j - x])
            }
            dp = nextDp
        }

        return dp[n]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
import 'dart:math';

class Solution {
  int minOperations(List<int> nums, int x, int k) {
    int n = nums.length;
    List<int> sortedUnique = nums.toSet().toList()..sort();
    int m_val = (x + 1) ~/ 2;
    int l = sortedUnique.length;

    List<int> numIndices = nums.map((v) {
      int low = 0, high = l - 1;
      while (low <= high) {
        int mid = (low + high) ~/ 2;
        if (sortedUnique[mid] == v) return mid + 1;
        if (sortedUnique[mid] < v) low = mid + 1;
        else high = mid - 1;
      }
      return -1;
    }).toList();

    List<int> bitCnt = List.filled(l + 1, 0);
    List<int> bitSum = List.filled(l + 1, 0);

    void update(List<int> bit, int idx, int val) {
      for (; idx <= l; idx += idx & -idx) {
        bit[idx] += val;
      }
    }

    int query(List<int> bit, int idx) {
      int sum = 0;
      for (; idx > 0; idx -= idx & -idx) {
        sum += bit[idx];
      }
      return sum;
    }

    int findKth(int target) {
      int idx = 0;
      for (int i = 1 << 16; i > 0; i >>= 1) {
        if (idx + i <= l && bitCnt[idx + i] < target) {
          idx += i;
          target -= bitCnt[idx];
        }
      }
      return idx + 1;
    }

    List<int> costs = List.filled(n - x + 1, 0);
    for (int i = 0; i < n; i++) {
      update(bitCnt, numIndices[i], 1);
      update(bitSum, numIndices[i], nums[i]);
      if (i >= x) {
        update(bitCnt, numIndices[i - x], -1);
        update(bitSum, numIndices[i - x], -nums[i - x]);
      }
      if (i >= x - 1) {
        int medianIdx = findKth(m_val);
        int medianVal = sortedUnique[medianIdx - 1];
        int countLessEqual = query(bitCnt, medianIdx);
        int sumLessEqual = query(bitSum, medianIdx);
        int sumTotal = query(bitSum, l);
        int cost = (medianVal * countLessEqual - sumLessEqual) +
            ((sumTotal - sumLessEqual) - medianVal * (x - countLessEqual));
        costs[i - x + 1] = cost;
      }
    }

    const int INF = 10000000000000000;
    List<int> dp = List.filled(n + 1, INF);
    dp[0] = 0;

    for (int j = 0; j < k; j++) {
      List<int> nextDp = List.filled(n + 1, INF);
      for (int i = 1; i <= n; i++) {
        int res = nextDp[i - 1];
        if (i >= x && dp[i - x] != INF) {
          int c = dp[i - x] + costs[i - x];
          if (c < res) res = c;
        }
        nextDp[i] = res;
      }
      dp = nextDp;
    }

    return dp[n];
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func minOperations(nums []int, x int, k int) int64 {
	n := len(nums)
	sortedUnique := make([]int, n)
	copy(sortedUnique, nums)
	importSort(sortedUnique)

	l := 0
	for i := 1; i < len(sortedUnique); i++ {
		if sortedUnique[i] != sortedUnique[l] {
			l++
			sortedUnique[l] = sortedUnique[i]
		}
	}
	sortedUnique = sortedUnique[:l+1]
	mSize := len(sortedUnique)

	numIndices := make([]int, n)
	for i, v := range nums {
		idx := 0
		low, high := 0, mSize-1
		for low <= high {
			mid := (low + high) / 2
			if sortedUnique[mid] == v {
				idx = mid + 1
				break
			}
			if sortedUnique[mid] < v {
				low = mid + 1
			} else {
				high = mid - 1
			}
		}
		numIndices[i] = idx
	}

	bitCnt := make([]int64, mSize+1)
	bitSum := make([]int64, mSize+1)
	update := func(bit []int64, idx int, val int64) {
		for ; idx <= mSize; idx += idx & -idx {
			bit[idx] += val
		}
	}
	query := func(bit []int64, idx int) int64 {
		var res int64 = 0
		for ; idx > 0; idx -= idx & -idx {
			res += bit[idx]
		}
		return res
	}
	findKth := func(target int64) int {
		idx := 0
		for i := 1 << 16; i > 0; i >>= 1 {
			if idx+i <= mSize && bitCnt[idx+i] < target {
				idx += i
				target -= bitCnt[idx]
			}
		}
		return idx + 1
	}

	costs := make([]int64, n-x+1)
	mPos := int64((x + 1) / 2)
	for i := 0; i < n; i++ {
		update(bitCnt, numIndices[i], 1)
		update(bitSum, numIndices[i], int64(nums[i]))
		if i >= x {
			update(bitCnt, numIndices[i-x], -1)
			update(bitSum, numIndices[i-x], int64(-nums[i-x]))
		}
		if i >= x-1 {
			midIdx := findKth(mPos)
			medianVal := int64(sortedUnique[midIdx-1])
			countLessEqual := query(bitCnt, midIdx)
			sumLessEqual := query(bitSum, midIdx)
			sumTotal := query(bitSum, mSize)
			cost := (medianVal*countLessEqual - sumLessEqual) + ((sumTotal - sumLessEqual) - medianVal*(int64(x)-countLessEqual))
			costs[i-x+1] = cost
		}
	}

	const INF int64 = 1e16
	dp := make([]int64, n+1)
	for i := range dp {
		dp[i] = INF
	}
	dp[0] = 0

	for j := 0; j < k; j++ {
		nextDp := make([]int64, n+1)
		for i := range nextDp {
			nextDp[i] = INF
		}
		for i := 1; i <= n; i++ {
			res := nextDp[i-1]
			if i >= x && dp[i-x] != INF {
				c := dp[i-x] + costs[i-x]
				if c < res {
					res = c
				}
			}
			nextDp[i] = res
		}
		dp = nextDp
	}
	return dp[n]
}

func importSort(a []int) {
	for i := 1; i < len(a); i++ {
		j := i
		for j > 0 && a[j] < a[j-1] {
			a[j], a[j-1] = a[j-1], a[j]
			j--
		}
	}
	importFastSort(a)
}

func importFastSort(a []int) {
	if len(a) < 20 {
		for i := 1; i < len(a); i++ {
			for j := i; j > 0 && a[j] < a[j-1]; j-- {
				a[j], a[j-1] = a[j-1], a[j]
			}
		}
		return
	}
	pivot := a[len(a)/2]
	left, right := 0, len(a)-1
	for left <= right {
		for a[left] < pivot { left++ }
		for a[right] > pivot { right-- }
		if left <= right {
			a[left], a[right] = a[right], a[left]
			left++
			right--
		}
	}
	importFastSort(a[:right+1])
	importFastSort(a[left:])
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def min_operations(nums, x, k)
  n = nums.length
  sorted_unique = nums.uniq.sort
  l = sorted_unique.length

  num_indices = nums.map { |v| sorted_unique.bsearch_index { |val| val >= v } + 1 }

  bit_cnt = Array.new(l + 1, 0)
  bit_sum = Array.new(l + 1, 0)

  update = lambda do |bit, idx, val|
    while idx <= l
      bit[idx] += val
      idx += (idx & -idx)
    end
  end

  query = lambda do |bit, idx|
    res = 0
    while idx > 0
      res += bit[idx]
      idx -= (idx & -idx)
    end
    res
  end

  find_kth = lambda do |target|
    idx = 0
    i = 1 << 16
    while i > 0
      if idx + i <= l && bit_cnt[idx + i] < target
        idx += i
        target -= bit_cnt[idx]
      end
      i >>= 1
    end
    idx + 1
  end

  costs = Array.new(n - x + 1)
  m_pos = (x + 1) / 2

  (0...n).each do |i|
    update.call(bit_cnt, num_indices[i], 1)
    update.call(bit_sum, num_indices[i], nums[i])

    if i >= x
      update.call(bit_cnt, num_indices[i - x], -1)
      update.call(bit_sum, num_indices[i - x], -nums[i - x])
    end

    if i >= x - 1
      mid_idx = find_kth.call(m_pos)
      m_val = sorted_unique[mid_idx - 1]
      count_le = query.call(bit_cnt, mid_idx)
      sum_le = query.call(bit_sum, mid_idx)
      sum_total = query.call(bit_sum, l)

      cost = (m_val * count_le - sum_le) + (sum_total - sum_le - m_val * (x - count_le))
      costs[i - x + 1] = cost
    end
  end

  inf = 10**16
  dp = Array.new(n + 1, inf)
  dp[0] = 0

  k.times do
    next_dp = Array.new(n + 1, inf)
    i = 1
    while i <= n
      res = next_dp[i - 1]
      if i >= x && dp[i - x] != inf
        c = dp[i - x] + costs[i - x]
        res = c if c < res
      end
      next_dp[i] = res
      i += 1
    end
    dp = next_dp
  end

  dp[n]
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
  def minOperations(nums: Array[Int], x: Int, k: Int): Long = {
    val n = nums.length
    val sortedUnique = nums.distinct.sorted
    val l = sortedUnique.length

    def binarySearch(target: Int): Int = {
      var low = 0
      var high = l - 1
      while (low <= high) {
        val mid = (low + high) / 2
        if (sortedUnique(mid) == target) return mid + 1
        if (sortedUnique(mid) < target) low = mid + 1
        else high = mid - 1
      }
      -1
    }

    val numIndices = nums.map(binarySearch)
    val bitCnt = new Array[Long](l + 1)
    val bitSum = new Array[Long](l + 1)

    def update(bit: Array[Long], i: Int, v: Long): Unit = {
      var idx = i
      while (idx <= l) {
        bit(idx) += v
        idx += (idx & -idx)
      }
    }

    def query(bit: Array[Long], i: Int): Long = {
      var idx = i
      var sum = 0L
      while (idx > 0) {
        sum += bit(idx)
        idx -= (idx & -idx)
      }
      sum
    }

    def findKth(targetValue: Long): Int = {
      var idx = 0
      var target = targetValue
      var i = 1 << 16
      while (i > 0) {
        if (idx + i <= l && bitCnt(idx + i) < target) {
          idx += i
          target -= bitCnt(idx)
        }
        i >>= 1
      }
      idx + 1
    }

    val costs = new Array[Long](n - x + 1)
    val mPos = (x + 1) / 2

    for (i <- 0 until n) {
      update(bitCnt, numIndices(i), 1L)
      update(bitSum, numIndices(i), nums(i).toLong)
      if (i >= x) {
        update(bitCnt, numIndices(i - x), -1L)
        update(bitSum, numIndices(i - x), -nums(i - x).toLong)
      }
      if (i >= x - 1) {
        val midIdx = findKth(mPos.toLong)
        val mVal = sortedUnique(midIdx - 1).toLong
        val countLE = query(bitCnt, midIdx)
        val sumLE = query(bitSum, midIdx)
        val sumTotal = query(bitSum, l)
        val cost = (mVal * countLE - sumLE) + (sumTotal - sumLE - mVal * (x - countLE))
        costs(i - x + 1) = cost
      }
    }

    val INF = 10000000000000000L
    var dp = Array.fill(n + 1)(INF)
    dp(0) = 0L

    for (_ <- 0 until k) {
      val nextDp = Array.fill(n + 1)(INF)
      var i = 1
      while (i <= n) {
        var res = nextDp(i - 1)
        if (i >= x && dp(i - x) != INF) {
          val c = dp(i - x) + costs(i - x)
          if (c < res) res = c
        }
        nextDp(i) = res
        i += 1
      }
      dp = nextDp
    }
    dp(n)
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn min_operations(nums: Vec<i32>, x: i32, k: i32) -> i64 {
        let n = nums.len();
        let x = x as usize;
        let k = k as usize;

        let mut sorted_unique = nums.clone();
        sorted_unique.sort_unstable();
        sorted_unique.dedup();
        let n_unique = sorted_unique.len();

        let mut val_to_idx = std::collections::HashMap::with_capacity(n_unique);
        for (i, &v) in sorted_unique.iter().enumerate() {
            val_to_idx.insert(v, i + 1);
        }

        let mut bit_count = vec![0; n_unique + 1];
        let mut bit_sum = vec![0i64; n_unique + 1];

        fn update_count(bit: &mut [i32], mut idx: usize, delta: i32, n: usize) {
            while idx <= n {
                bit[idx] += delta;
                idx += idx & idx.wrapping_neg();
            }
        }

        fn update_sum(bit: &mut [i64], mut idx: usize, delta: i64, n: usize) {
            while idx <= n {
                bit[idx] += delta;
                idx += idx & idx.wrapping_neg();
            }
        }

        fn query_count(bit: &[i32], mut idx: usize) -> i32 {
            let mut sum = 0;
            while idx > 0 {
                sum += bit[idx];
                idx -= idx & idx.wrapping_neg();
            }
            sum
        }

        fn query_sum(bit: &[i64], mut idx: usize) -> i64 {
            let mut sum = 0;
            while idx > 0 {
                sum += bit[idx];
                idx -= idx & idx.wrapping_neg();
            }
            sum
        }

        fn get_kth(bit: &[i32], mut k: i32, n_unique: usize) -> usize {
            let mut idx = 0;
            let mut i = 1;
            while i * 2 <= n_unique { i *= 2; }
            while i > 0 {
                if idx + i <= n_unique {
                    let val = bit[idx + i];
                    if val < k {
                        idx += i;
                        k -= val;
                    }
                }
                i >>= 1;
            }
            idx + 1
        }

        let mut costs = vec![0i64; n - x + 1];
        let mut window_sum = 0i64;
        for i in 0..n {
            let v = nums[i];
            let idx = *val_to_idx.get(&v).unwrap();
            update_count(&mut bit_count, idx, 1, n_unique);
            update_sum(&mut bit_sum, idx, v as i64, n_unique);
            window_sum += v as i64;

            if i >= x {
                let old_v = nums[i - x];
                let old_idx = *val_to_idx.get(&old_v).unwrap();
                update_count(&mut bit_count, old_idx, -1, n_unique);
                update_sum(&mut bit_sum, old_idx, -(old_v as i64), n_unique);
                window_sum -= old_v as i64;
            }

            if i >= x - 1 {
                let mid_count = ((x + 1) / 2) as i32;
                let mid_idx = get_kth(&bit_count, mid_count, n_unique);
                let median_val = sorted_unique[mid_idx - 1] as i64;
                let count_low = query_count(&bit_count, mid_idx) as i64;
                let sum_low = query_sum(&bit_sum, mid_idx);
                let count_high = x as i64 - count_low;
                let sum_high = window_sum - sum_low;
                costs[i - x + 1] = (count_low * median_val - sum_low) + (sum_high - count_high * median_val);
            }
        }

        let inf = 1e16 as i64;
        let mut prev_dp = vec![0i64; n + 1];
        for j in 1..=k {
            let mut curr_dp = vec![inf; n + 1];
            for i in (j * x)..=n {
                curr_dp[i] = curr_dp[i - 1].min(prev_dp[i - x] + costs[i - x]);
            }
            prev_dp = curr_dp;
        }

        prev_dp[n]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (min-operations nums x k)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  (let* ([n (length nums)]
         [nums-vec (list->vector nums)]
         [sorted-unique (list->vector (sort (remove-duplicates nums) <))]
         [n-unique (vector-length sorted-unique)]
         [val-to-idx (make-hash)])
    (for ([i (in-range n-unique)])
      (hash-set! val-to-idx (vector-ref sorted-unique i) (+ i 1)))
    (define bit-count (make-vector (+ n-unique 1) 0))
    (define bit-sum (make-vector (+ n-unique 1) 0))
    (define (update! bit idx delta max-idx)
      (let loop ((i idx))
        (when (<= i max-idx)
          (vector-set! bit i (+ (vector-ref bit i) delta))
          (loop (+ i (bitwise-and i (- i)))))))
    (define (query bit idx)
      (let loop ((i idx) (s 0))
        (if (<= i 0) s (loop (- i (bitwise-and i (- i))) (+ s (vector-ref bit i))))))
    (define (get-kth bit target-k)
      (let* ([max-pow (let p-loop ([p 1]) (if (<= (* p 2) n-unique) (p-loop (* p 2)) p))])
        (let loop ((idx 0) (cur-k target-k) (i max-pow))
          (if (zero? i)
              (+ idx 1)
              (let ((next-idx (+ idx i)))
                (if (and (<= next-idx n-unique) (< (vector-ref bit next-idx) cur-k))
                    (loop next-idx (- cur-k (vector-ref bit next-idx)) (arithmetic-shift i -1))
                    (loop idx cur-k (arithmetic-shift i -1))))))))
    (define costs (make-vector (+ (- n x) 1) 0))
    (let ([window-sum 0])
      (for ([i (in-range n)])
        (let* ([v (vector-ref nums-vec i)]
               [idx (hash-ref val-to-idx v)])
          (update! bit-count idx 1 n-unique)
          (update! bit-sum idx v n-unique)
          (set! window-sum (+ window-sum v))
          (when (>= i x)
            (let* ([old-v (vector-ref nums-vec (- i x))]
                   [old-idx (hash-ref val-to-idx old-v)])
              (update! bit-count old-idx -1 n-unique)
              (update! bit-sum old-idx (- old-v) n-unique)
              (set! window-sum (- window-sum old-v))))
          (when (>= i (- x 1))
            (let* ([mid-count (quotient (+ x 1) 2)]
                   [mid-idx (get-kth bit-count mid-count)]
                   [median (vector-ref sorted-unique (- mid-idx 1))]
                   [count-low (query bit-count mid-idx)]
                   [sum-low (query bit-sum mid-idx)]
                   [count-high (- x count-low)]
                   [sum-high (- window-sum sum-low)])
              (vector-set! costs (+ (- i x) 1) (+ (- (* count-low median) sum-low) (- sum-high (* count-high median)))))))))
    (define inf 10000000000000000)
    (define prev-dp (make-vector (+ n 1) 0))
    (for ([j (in-range 1 (+ k 1))])
      (define curr-dp (make-vector (+ n 1) inf))
      (for ([i (in-range (* j x) (+ n 1))])
        (vector-set! curr-dp i (min (vector-ref curr-dp (- i 1))
                                    (+ (vector-ref prev-dp (- i x)) (vector-ref costs (- i x))))))
      (set! prev-dp curr-dp))
    (vector-ref prev-dp n)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec min_operations(Nums :: [integer()], X :: integer(), K :: integer()) -> integer().
min_operations(Nums, X, K) ->
    N = length(Nums),
    NumsVec = list_to_tuple(Nums),
    UniqueSorted = lists:usort(Nums),
    NUnique = length(UniqueSorted),
    ValToIdx = maps:from_list(lists:zip(UniqueSorted, lists:seq(1, NUnique))),
    BitCount = ets:new(bit_count, [set, public]),
    BitSum = ets:new(bit_sum, [set, public]),
    ets:insert(BitCount, [{I, 0} || I <- lists:seq(1, NUnique)]),
    ets:insert(BitSum, [{I, 0} || I <- lists:seq(1, NUnique)]),
    CostsTab = ets:new(costs, [set, public]),
    MaxPow = get_max_pow2(NUnique),
    fold_costs(0, 0, N, X, NUnique, NumsVec, ValToIdx, BitCount, BitSum, UniqueSorted, MaxPow, CostsTab),
    Inf = 1000000000000000,
    PrevDP = array:new([{size, N + 1}, {default, 0}]),
    FinalDP = lists:foldl(fun(J, AccDP) ->
        CurrDP = array:new([{size, N + 1}, {default, Inf}]),
        update_dp(J * X, J * X, N, X, AccDP, CurrDP, CostsTab)
    end, PrevDP, lists:seq(1, K)),
    array:get(N, FinalDP).

get_max_pow2(N) ->
    get_max_pow2_inner(1, N).
get_max_pow2_inner(P, N) when P * 2 =< N -> get_max_pow2_inner(P * 2, N);
get_max_pow2_inner(P, _) -> P.

update_bit(Tab, Idx, Delta, Max) ->
    case Idx =< Max of
        true ->
            ets:update_counter(Tab, Idx, Delta),
            update_bit(Tab, Idx + (Idx band -Idx), Delta, Max);
        false -> ok
    end.

query_bit(Tab, Idx) ->
    query_bit_inner(Tab, Idx, 0).
query_bit_inner(_, 0, Sum) -> Sum;
query_bit_inner(Tab, Idx, Sum) ->
    query_bit_inner(Tab, Idx - (Idx band -Idx), Sum + ets:lookup_element(Tab, Idx, 2)).

get_kth(Tab, K, MaxIdx, MaxPow) ->
    get_kth_inner(Tab, K, 0, MaxPow, MaxIdx).
get_kth_inner(_Tab, _K, Idx, 0, _MaxIdx) -> Idx + 1;
get_kth_inner(Tab, K, Idx, Step, MaxIdx) ->
    NextIdx = Idx + Step,
    case NextIdx =< MaxIdx of
        true ->
            Val = ets:lookup_element(Tab, NextIdx, 2),
            case Val < K of
                true -> get_kth_inner(Tab, K - Val, NextIdx, Step div 2, MaxIdx);
                false -> get_kth_inner(Tab, K, Idx, Step div 2, MaxIdx)
            end;
        false ->
            get_kth_inner(Tab, K, Idx, Step div 2, MaxIdx)
    end.

fold_costs(I, WindowSum, N, X, NUnique, NumsVec, ValToIdx, BitCount, BitSum, UniqueSorted, MaxPow, CostsTab) when I < N ->
    V = element(I + 1, NumsVec),
    Idx = maps:get(V, ValToIdx),
    update_bit(BitCount, Idx, 1, NUnique),
    update_bit(BitSum, Idx, V, NUnique),
    NewSum = WindowSum + V,
    FinalSum = if I >= X ->
        OldV = element(I - X + 1, NumsVec),
        OldIdx = maps:get(OldV, ValToIdx),
        update_bit(BitCount, OldIdx, -1, NUnique),
        update_bit(BitSum, OldIdx, -OldV, NUnique),
        NewSum - OldV;
        true -> NewSum
    end,
    if I >= X - 1 ->
        MidCount = (X + 1) div 2,
        MidIdx = get_kth(BitCount, MidCount, NUnique, MaxPow),
        Median = lists:nth(MidIdx, UniqueSorted),
        CountLow = query_bit(BitCount, MidIdx),
        SumLow = query_bit(BitSum, MidIdx),
        CountHigh = X - CountLow,
        SumHigh = FinalSum - SumLow,
        Cost = (CountLow * Median - SumLow) + (SumHigh - CountHigh * Median),
        ets:insert(CostsTab, {I - X + 1, Cost});
        true -> ok
    end,
    fold_costs(I + 1, FinalSum, N, X, NUnique, NumsVec, ValToIdx, BitCount, BitSum, UniqueSorted, MaxPow, CostsTab);
fold_costs(_, _, _, _, _, _, _, _, _, _, _, _) -> ok.

update_dp(I, JX, N, X, PrevDP, CurrDP, CostsTab) when I =< N ->
    PrevVal = if I > JX -> array:get(I - 1, CurrDP); true -> 1000000000000000 end,
    Option = array:get(I - X, PrevDP) + ets:lookup_element(CostsTab, I - X, 2),
    NewCurrDP = array:set(I, min(PrevVal, Option), CurrDP),
    update_dp(I + 1, JX, N, X, PrevDP, NewCurrDP, CostsTab);
update_dp(_, _, _, _, _, CurrDP, _) -> CurrDP.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  import Bitwise

  @spec min_operations(nums :: [integer], x :: integer, k :: integer) :: integer
  def min_operations(nums, x, k) do
    n = length(nums)
    nums_vec = List.to_tuple(nums)
    unique_sorted = Enum.uniq(nums) |> Enum.sort()
    n_unique = length(unique_sorted)
    val_to_idx = unique_sorted |> Enum.with_index(1) |> Enum.into(%{})
    bit_count = :ets.new(:bit_count, [:set, :public])
    bit_sum = :ets.new(:bit_sum, [:set, :public])
    :ets.insert(bit_count, for(i <- 1..n_unique, do: {i, 0}))
    :ets.insert(bit_sum, for(i <- 1..n_unique, do: {i, 0}))
    costs_tab = :ets.new(:costs, [:set, :public])
    max_pow = get_max_pow2(n_unique)

    fold_costs(0, 0, n, x, n_unique, nums_vec, val_to_idx, bit_count, bit_sum, List.to_tuple(unique_sorted), max_pow, costs_tab)

    inf = 10_000_000_000_000_000
    prev_dp = :array.new(size: n + 1, default: 0)

    final_dp = Enum.reduce(1..k, prev_dp, fn j, acc_dp ->
      curr_dp = :array.new(size: n + 1, default: inf)
      update_dp(j * x, j * x, n, x, acc_dp, curr_dp, costs_tab, inf)
    end)

    :array.get(n, final_dp)
  end

  defp get_max_pow2(n), do: get_max_pow2_inner(1, n)
  defp get_max_pow2_inner(p, n) when p * 2 <= n, do: get_max_pow2_inner(p * 2, n)
  defp get_max_pow2_inner(p, _), do: p

  defp update_bit(tab, idx, delta, max) when idx <= max do
    :ets.update_counter(tab, idx, delta)
    update_bit(tab, idx + (idx &&& -idx), delta, max)
  end
  defp update_bit(_, _, _, _), do: :ok

  defp query_bit(tab, idx), do: query_bit_inner(tab, idx, 0)
  defp query_bit_inner(_, 0, sum), do: sum
  defp query_bit_inner(tab, idx, sum), do: query_bit_inner(tab, idx - (idx &&& -idx), sum + :ets.lookup_element(tab, idx, 2))

  defp get_kth(tab, k, max_idx, max_pow), do: get_kth_inner(tab, k, 0, max_pow, max_idx)
  defp get_kth_inner(_, _, idx, 0, _), do: idx + 1
  defp get_kth_inner(tab, k, idx, step, max_idx) do
    next_idx = idx + step
    if next_idx <= max_idx do
      val = :ets.lookup_element(tab, next_idx, 2)
      if val < k, do: get_kth_inner(tab, k - val, next_idx, div(step, 2), max_idx), else: get_kth_inner(tab, k, idx, div(step, 2), max_idx)
    else
      get_kth_inner(tab, k, idx, div(step, 2), max_idx)
    end
  end

  defp fold_costs(i, window_sum, n, x, n_unique, nums_vec, val_to_idx, bit_count, bit_sum, unique_tuple, max_pow, costs_tab) when i < n do
    v = elem(nums_vec, i)
    idx = Map.get(val_to_idx, v)
    update_bit(bit_count, idx, 1, n_unique)
    update_bit(bit_sum, idx, v, n_unique)
    new_sum = window_sum + v
    final_sum = if i >= x do
      old_v = elem(nums_vec, i - x)
      old_idx = Map.get(val_to_idx, old_v)
      update_bit(bit_count, old_idx, -1, n_unique)
      update_bit(bit_sum, old_idx, -old_v, n_unique)
      new_sum - old_v
    else
      new_sum
    end
    if i >= x - 1 do
      mid_count = div(x + 1, 2)
      mid_idx = get_kth(bit_count, mid_count, n_unique, max_pow)
      median = elem(unique_tuple, mid_idx - 1)
      count_low = query_bit(bit_count, mid_idx)
      sum_low = query_bit(bit_sum, mid_idx)
      count_high = x - count_low
      sum_high = final_sum - sum_low
      cost = (count_low * median - sum_low) + (sum_high - count_high * median)
      :ets.insert(costs_tab, {i - x + 1, cost})
    end
    fold_costs(i + 1, final_sum, n, x, n_unique, nums_vec, val_to_idx, bit_count, bit_sum, unique_tuple, max_pow, costs_tab)
  end
  defp fold_costs(_, _, _, _, _, _, _, _, _, _, _, _), do: :ok

  defp update_dp(i, jx, n, x, prev_dp, curr_dp, costs_tab, inf) when i <= n do
    prev_val = if i > jx, do: :array.get(i - 1, curr_dp), else: inf
    option = :array.get(i - x, prev_dp) + :ets.lookup_element(costs_tab, i - x, 2)
    new_curr_dp = :array.set(i, Enum.min([prev_val, option]), curr_dp)
    update_dp(i + 1, jx, n, x, prev_dp, new_curr_dp, costs_tab, inf)
  end
  defp update_dp(_, _, _, _, _, curr_dp, _, _), do: curr_dp
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n log n + nk) where $n$ is the length of the array and $k$ is the number of subarrays. Precalculating the median costs for all windows using coordinate compression and Fenwick trees takes $O(n \log n)$, and the dynamic programming step takes $O(nk)$.
- **Space Complexity:** O(n) for storing the input array, the precalculated costs, coordinate mapping, the Fenwick trees, and the optimized DP table rows.
