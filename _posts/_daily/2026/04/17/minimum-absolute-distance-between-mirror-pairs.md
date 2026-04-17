---
layout: post
title: "Minimum Absolute Distance Between Mirror Pairs"
date: 2026-04-17 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Hash Table", "Math"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int minMirrorPairDistance(vector<int>& nums)\
        \ {\n        long long min_dist = -1;\n        std::unordered_map<long long,\
        \ int> last_seen_rev;\n\n        for (int j = 0; j < nums.size(); ++j) {\n \
        \           long long current = nums[j];\n            if (last_seen_rev.count(current))\
        \ {\n                int dist = j - last_seen_rev[current];\n              \
        \  if (min_dist == -1 || dist < min_dist) {\n                    min_dist =\
        \ dist;\n                }\n            }\n\n            long long rev = 0;\n\
        \            long long temp = nums[j];\n            while (temp > 0) {\n   \
        \             rev = rev * 10 + (temp % 10);\n                temp /= 10;\n \
        \           }\n            last_seen_rev[rev] = j;\n        }\n\n        return\
        \ (int)min_dist;\n    }\n};"
      java: "class Solution {\n    public int minMirrorPairDistance(int[] nums) {\n\
        \        int minDist = Integer.MAX_VALUE;\n        java.util.HashMap<Long, Integer>\
        \ lastSeenRev = new java.util.HashMap<>();\n\n        for (int j = 0; j < nums.length;\
        \ j++) {\n            long current = (long) nums[j];\n            if (lastSeenRev.containsKey(current))\
        \ {\n                minDist = Math.min(minDist, j - lastSeenRev.get(current));\n\
        \            }\n\n            long rev = 0;\n            long temp = current;\n\
        \            while (temp > 0) {\n                rev = rev * 10 + (temp % 10);\n\
        \                temp /= 10;\n            }\n            lastSeenRev.put(rev,\
        \ j);\n        }\n\n        return (minDist == Integer.MAX_VALUE) ? -1 : minDist;\n\
        \    }\n}"
      python: "class Solution(object):\n    def minMirrorPairDistance(self, nums):\n\
        \        \"\"\"\n        :type nums: List[int]\n        :rtype: int\n      \
        \  \"\"\"\n        last_seen_rev = {}\n        min_dist = float('inf')\n\n \
        \       for j, num in enumerate(nums):\n            if num in last_seen_rev:\n\
        \                min_dist = min(min_dist, j - last_seen_rev[num])\n\n      \
        \      rev = 0\n            temp = num\n            while temp > 0:\n      \
        \          rev = rev * 10 + (temp % 10)\n                temp //= 10\n     \
        \       last_seen_rev[rev] = j\n\n        return int(min_dist) if min_dist !=\
        \ float('inf') else -1"
      python3: "class Solution:\n    def minMirrorPairDistance(self, nums: List[int])\
        \ -> int:\n        last_seen_rev = {}\n        min_dist = float('inf')\n\n \
        \       for j, num in enumerate(nums):\n            if num in last_seen_rev:\n\
        \                min_dist = min(min_dist, j - last_seen_rev[num])\n\n      \
        \      rev = 0\n            temp = num\n            while temp > 0:\n      \
        \          rev = rev * 10 + (temp % 10)\n                temp //= 10\n     \
        \       last_seen_rev[rev] = j\n\n        return int(min_dist) if min_dist !=\
        \ float('inf') else -1"
      c: "#include <stdlib.h>\n#include <limits.h>\n\n#define TABLE_SIZE 300007\n\n\
        long long get_reverse(int n) {\n    long long rev = 0;\n    while (n > 0) {\n\
        \        rev = rev * 10 + (n % 10);\n        n /= 10;\n    }\n    return rev;\n\
        }\n\nint minMirrorPairDistance(int* nums, int numsSize) {\n    long long* keys\
        \ = (long long*)malloc(sizeof(long long) * TABLE_SIZE);\n    int* values = (int*)malloc(sizeof(int)\
        \ * TABLE_SIZE);\n    for (int i = 0; i < TABLE_SIZE; i++) values[i] = -1;\n\
        \n    int min_dist = INT_MAX;\n\n    for (int j = 0; j < numsSize; j++) {\n\
        \        long long current = (long long)nums[j];\n        unsigned int h1 =\
        \ (unsigned int)(current % TABLE_SIZE);\n        while (values[h1] != -1) {\n\
        \            if (keys[h1] == current) {\n                int d = j - values[h1];\n\
        \                if (d < min_dist) min_dist = d;\n                break;\n \
        \           }\n            h1 = (h1 + 1) % TABLE_SIZE;\n        }\n\n      \
        \  long long rev = get_reverse(nums[j]);\n        unsigned int h2 = (unsigned\
        \ int)(rev % TABLE_SIZE);\n        while (values[h2] != -1 && keys[h2] != rev)\
        \ {\n            h2 = (h2 + 1) % TABLE_SIZE;\n        }\n        keys[h2] =\
        \ rev;\n        values[h2] = j;\n    }\n\n    free(keys);\n    free(values);\n\
        \    return (min_dist == INT_MAX) ? -1 : min_dist;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\n\npublic class Solution\
        \ {\n    public int MinMirrorPairDistance(int[] nums) {\n        int minDist\
        \ = int.MaxValue;\n        Dictionary<int, int> lastSeenIndices = new Dictionary<int,\
        \ int>();\n\n        for (int j = 0; j < nums.Length; j++) {\n            int\
        \ val = nums[j];\n            if (lastSeenIndices.ContainsKey(val)) {\n    \
        \            int currentDist = j - lastSeenIndices[val];\n                if\
        \ (currentDist < minDist) {\n                    minDist = currentDist;\n  \
        \              }\n            }\n\n            int revVal = 0;\n           \
        \ int temp = val;\n            while (temp > 0) {\n                revVal =\
        \ revVal * 10 + (temp % 10);\n                temp /= 10;\n            }\n \
        \           lastSeenIndices[revVal] = j;\n        }\n\n        return minDist\
        \ == int.MaxValue ? -1 : minDist;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar minMirrorPairDistance\
        \ = function(nums) {\n    let minDist = Infinity;\n    const lastSeenIndices\
        \ = new Map();\n\n    for (let j = 0; j < nums.length; j++) {\n        const\
        \ val = nums[j];\n        if (lastSeenIndices.has(val)) {\n            minDist\
        \ = Math.min(minDist, j - lastSeenIndices.get(val));\n        }\n\n        let\
        \ revVal = 0;\n        let temp = val;\n        while (temp > 0) {\n       \
        \     revVal = revVal * 10 + (temp % 10);\n            temp = Math.floor(temp\
        \ / 10);\n        }\n        lastSeenIndices.set(revVal, j);\n    }\n\n    return\
        \ minDist === Infinity ? -1 : minDist;\n};"
      typescript: "function minMirrorPairDistance(nums: number[]): number {\n    let\
        \ minDist = Infinity;\n    const lastSeenIndices = new Map<number, number>();\n\
        \n    for (let j = 0; j < nums.length; j++) {\n        const val = nums[j];\n\
        \        if (lastSeenIndices.has(val)) {\n            minDist = Math.min(minDist,\
        \ j - lastSeenIndices.get(val)!);\n        }\n\n        let revVal = 0;\n  \
        \      let temp = val;\n        while (temp > 0) {\n            revVal = revVal\
        \ * 10 + (temp % 10);\n            temp = Math.floor(temp / 10);\n        }\n\
        \        lastSeenIndices.set(revVal, j);\n    }\n\n    return minDist === Infinity\
        \ ? -1 : minDist;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer\n     */\n    function minMirrorPairDistance($nums) {\n        $minDist\
        \ = -1;\n        $lastSeenIndices = [];\n\n        foreach ($nums as $j => $val)\
        \ {\n            if (isset($lastSeenIndices[$val])) {\n                $dist\
        \ = $j - $lastSeenIndices[$val];\n                if ($minDist === -1 || $dist\
        \ < $minDist) {\n                    $minDist = $dist;\n                }\n\
        \            }\n\n            $revVal = 0;\n            $temp = $val;\n    \
        \        while ($temp > 0) {\n                $revVal = $revVal * 10 + ($temp\
        \ % 10);\n                $temp = (int)($temp / 10);\n            }\n      \
        \      $lastSeenIndices[$revVal] = $j;\n        }\n\n        return $minDist;\n\
        \    }\n}"
      swift: "class Solution {\n    func minMirrorPairDistance(_ nums: [Int]) -> Int\
        \ {\n        var minDist = -1\n        var lastSeenIndices = [Int: Int]()\n\n\
        \        for j in 0..<nums.count {\n            let val = nums[j]\n        \
        \    if let i = lastSeenIndices[val] {\n                let dist = j - i\n \
        \               if minDist == -1 || dist < minDist {\n                    minDist\
        \ = dist\n                }\n            }\n\n            var revVal = 0\n \
        \           var temp = val\n            while temp > 0 {\n                revVal\
        \ = revVal * 10 + (temp % 10)\n                temp /= 10\n            }\n \
        \           lastSeenIndices[revVal] = j\n        }\n\n        return minDist\n\
        \    }\n}"
      kotlin: "class Solution {\n    fun minMirrorPairDistance(nums: IntArray): Int\
        \ {\n        val lastSeenTarget = mutableMapOf<Int, Int>()\n        var minDist\
        \ = -1\n        for (j in nums.indices) {\n            val currentVal = nums[j]\n\
        \            if (lastSeenTarget.containsKey(currentVal)) {\n               \
        \ val dist = j - lastSeenTarget[currentVal]!!\n                if (minDist ==\
        \ -1 || dist < minDist) {\n                    minDist = dist\n            \
        \    }\n            }\n            var num = currentVal\n            var rev\
        \ = 0\n            while (num > 0) {\n                rev = rev * 10 + (num\
        \ % 10)\n                num /= 10\n            }\n            lastSeenTarget[rev]\
        \ = j\n        }\n        return minDist\n    }\n}"
      dart: "class Solution {\n  int minMirrorPairDistance(List<int> nums) {\n    Map<int,\
        \ int> lastSeenTarget = {};\n    int minDist = -1;\n    for (int j = 0; j <\
        \ nums.length; j++) {\n      int currentVal = nums[j];\n      if (lastSeenTarget.containsKey(currentVal))\
        \ {\n        int dist = j - lastSeenTarget[currentVal]!;\n        if (minDist\
        \ == -1 || dist < minDist) {\n          minDist = dist;\n        }\n      }\n\
        \      int num = currentVal;\n      int rev = 0;\n      while (num > 0) {\n\
        \        rev = rev * 10 + (num % 10);\n        num ~/= 10;\n      }\n      lastSeenTarget[rev]\
        \ = j;\n    }\n    return minDist;\n  }\n}"
      go: "func minMirrorPairDistance(nums []int) int {\n    lastSeenTarget := make(map[int]int)\n\
        \    minDist := -1\n    for j, currentVal := range nums {\n        if pos, ok\
        \ := lastSeenTarget[currentVal]; ok {\n            dist := j - pos\n       \
        \     if minDist == -1 || dist < minDist {\n                minDist = dist\n\
        \            }\n        }\n        num := currentVal\n        rev := 0\n   \
        \     for num > 0 {\n            rev = rev*10 + num%10\n            num /= 10\n\
        \        }\n        lastSeenTarget[rev] = j\n    }\n    return minDist\n}"
      ruby: "# @param {Integer[]} nums\n# @return {Integer}\ndef min_mirror_pair_distance(nums)\n\
        \  last_seen_target = {}\n  min_dist = -1\n  nums.each_with_index do |current_val,\
        \ j|\n    if last_seen_target.has_key?(current_val)\n      dist = j - last_seen_target[current_val]\n\
        \      if min_dist == -1 || dist < min_dist\n        min_dist = dist\n     \
        \ end\n    end\n    num = current_val\n    rev = 0\n    while num > 0\n    \
        \  rev = rev * 10 + (num % 10)\n      num /= 10\n    end\n    last_seen_target[rev]\
        \ = j\n  end\n  min_dist\nend"
      scala: "object Solution {\n    def minMirrorPairDistance(nums: Array[Int]): Int\
        \ = {\n        val lastSeenTarget = scala.collection.mutable.Map[Int, Int]()\n\
        \        var minDist = -1\n        for (j <- nums.indices) {\n            val\
        \ currentVal = nums(j)\n            if (lastSeenTarget.contains(currentVal))\
        \ {\n                val dist = j - lastSeenTarget(currentVal)\n           \
        \     if (minDist == -1 || dist < minDist) {\n                    minDist =\
        \ dist\n                }\n            }\n            var num = currentVal\n\
        \            var rev = 0\n            while (num > 0) {\n                rev\
        \ = rev * 10 + (num % 10)\n                num /= 10\n            }\n      \
        \      lastSeenTarget(rev) = j\n        }\n        minDist\n    }\n}"
      rust: "use std::collections::HashMap;\n\nimpl Solution {\n    pub fn min_mirror_pair_distance(nums:\
        \ Vec<i32>) -> i32 {\n        let mut last_pos: HashMap<i32, usize> = HashMap::new();\n\
        \        let mut min_dist = i32::MAX;\n        let mut found = false;\n\n  \
        \      for (j, &num) in nums.iter().enumerate() {\n            if let Some(&i)\
        \ = last_pos.get(&num) {\n                let dist = (j - i) as i32;\n     \
        \           if dist < min_dist {\n                    min_dist = dist;\n   \
        \             }\n                found = true;\n            }\n\n          \
        \  let mut n = num;\n            let mut rev = 0;\n            while n > 0 {\n\
        \                rev = rev * 10 + n % 10;\n                n /= 10;\n      \
        \      }\n            last_pos.insert(rev, j);\n        }\n\n        if found\
        \ { min_dist } else { -1 }\n    }\n}"
      racket: "(define/contract (min-mirror-pair-distance nums)\n  (-> (listof exact-integer?)\
        \ exact-integer?)\n  (let-values ([(final-min-dist final-last-pos)\n       \
        \          (for/fold ([min-dist #f]\n                            [last-pos (hash)])\n\
        \                           ([num (in-list nums)]\n                        \
        \    [j (in-naturals)])\n                   (let* ([i (hash-ref last-pos num\
        \ #f)]\n                          [new-min-dist (if i\n                    \
        \                       (let ([dist (- j i)])\n                            \
        \                 (if (or (not min-dist) (< dist min-dist))\n              \
        \                                   dist\n                                 \
        \                min-dist))\n                                           min-dist)]\n\
        \                          [rev (let loop ([n num] [res 0])\n              \
        \                   (if (= n 0)\n                                     res\n\
        \                                     (loop (quotient n 10) (+ (* res 10) (remainder\
        \ n 10)))))])\n                     (values new-min-dist (hash-set last-pos\
        \ rev j))))])\n    (if final-min-dist final-min-dist -1)))"
      erlang: "-spec min_mirror_pair_distance(Nums :: [integer()]) -> integer().\nmin_mirror_pair_distance(Nums)\
        \ ->\n    solve(Nums, 0, #{}, -1).\n\nsolve([], _J, _LastPos, MinDist) ->\n\
        \    MinDist;\nsolve([Num | Rest], J, LastPos, MinDist) ->\n    NewMinDist =\
        \ case maps:find(Num, LastPos) of\n        {ok, I} ->\n            Dist = J\
        \ - I,\n            if\n                MinDist =:= -1 -> Dist;\n          \
        \      Dist < MinDist -> Dist;\n                true -> MinDist\n          \
        \  end;\n        error ->\n            MinDist\n    end,\n    Rev = reverse_num(Num,\
        \ 0),\n    solve(Rest, J + 1, maps:put(Rev, J, LastPos), NewMinDist).\n\nreverse_num(0,\
        \ Rev) -> Rev;\nreverse_num(N, Rev) -> reverse_num(N div 10, Rev * 10 + (N rem\
        \ 10))."
      elixir: "defmodule Solution do\n  @spec min_mirror_pair_distance(nums :: [integer])\
        \ :: integer\n  def min_mirror_pair_distance(nums) do\n    {min_dist, _} = Enum.reduce(Enum.with_index(nums),\
        \ {nil, %{}}, fn {num, j}, {min_dist, last_pos} ->\n      new_min_dist = case\
        \ Map.get(last_pos, num) do\n        nil -> min_dist\n        i ->\n       \
        \   dist = j - i\n          if is_nil(min_dist) or dist < min_dist, do: dist,\
        \ else: min_dist\n      end\n\n      rev = reverse_num(num)\n      {new_min_dist,\
        \ Map.put(last_pos, rev, j)}\n    end)\n\n    min_dist || -1\n  end\n\n  defp\
        \ reverse_num(n, rev \\\\ 0)\n  defp reverse_num(0, rev), do: rev\n  defp reverse_num(n,\
        \ rev), do: reverse_num(div(n, 10), rev * 10 + rem(n, 10))\nend"
    approach: 'The core problem is to find pairs $(i, j)$ with $i < j$ such that $nums[j]$
      is the reversed version of $nums[i]$, while minimizing $j - i$. We can solve this
      efficiently by iterating through the array once and using a hash map to keep track
      of the most recent index where each ''mirror value'' was seen. Specifically, at
      each index $j$, we check if the current value $nums[j]$ has been registered as
      a reversed value of any previous element $nums[i]$. To always get the minimum
      distance for $j$, we only need to care about the largest index $i < j$ that satisfies
      the condition.


      During the linear scan, for each element $nums[j]$, we look up $nums[j]$ in our
      hash map. If it exists, the stored value is the most recent index $i$ where $reverse(nums[i])$
      equals the current $nums[j]$, thus providing a candidate for the minimum distance.
      After checking the map, we calculate $r = reverse(nums[j])$ and update the map
      with the entry `r: j`. This ensures that for any future element $nums[k]$ ($k
      > j$), if $nums[k] == reverse(nums[j])$, it will find the closest possible index
      $j$.'
    time_complexity: O(N) where N is the length of the nums array. For each element,
      we reverse its digits (at most 10 digits for a number up to $10^9$) and perform
      hash map insertions and lookups, which take $O(1)$ on average.
    space_complexity: O(N) to store the indices of the reversed numbers in a hash map,
      with at most N entries in the worst case.
    elapsed_time: 476.0354731082916
    model: gemini-3-flash-preview
    generated_at: '2026-04-17 02:02:37 '
---

## Problem #3761: Minimum Absolute Distance Between Mirror Pairs

**Difficulty:** Medium

**Topics:** Array, Hash Table, Math

## Problem Description

<p>You are given an integer array <code>nums</code>.</p>

<p>A <strong>mirror pair</strong> is a pair of indices <code>(i, j)</code> such that:</p>

<ul>
	<li><code>0 &lt;= i &lt; j &lt; nums.length</code>, and</li>
	<li><code>reverse(nums[i]) == nums[j]</code>, where <code>reverse(x)</code> denotes the integer formed by reversing the digits of <code>x</code>. Leading zeros are omitted after reversing, for example <code>reverse(120) = 21</code>.</li>
</ul>

<p>Return the <strong>minimum</strong> absolute distance between the indices of any mirror pair. The absolute distance between indices <code>i</code> and <code>j</code> is <code>abs(i - j)</code>.</p>

<p>If no mirror pair exists, return <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [12,21,45,33,54]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p>The mirror pairs are:</p>

<ul>
	<li>(0, 1) since <code>reverse(nums[0]) = reverse(12) = 21 = nums[1]</code>, giving an absolute distance <code>abs(0 - 1) = 1</code>.</li>
	<li>(2, 4) since <code>reverse(nums[2]) = reverse(45) = 54 = nums[4]</code>, giving an absolute distance <code>abs(2 - 4) = 2</code>.</li>
</ul>

<p>The minimum absolute distance among all pairs is 1.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [120,21]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p>There is only one mirror pair (0, 1) since <code>reverse(nums[0]) = reverse(120) = 21 = nums[1]</code>.</p>

<p>The minimum absolute distance is 1.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [21,120]</span></p>

<p><strong>Output:</strong> <span class="example-io">-1</span></p>

<p><strong>Explanation:</strong></p>

<p>There are no mirror pairs in the array.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code>​​​​​​​</li>
</ul>


## Hints

1. Scan left to right with a hash map: for each `nums[i]`, if the map contains key `nums[i]` then set `ans = min(ans, i - map[nums[i]])`.

2. Store/update the current index under key `reverse(nums[i])`, so future matches use the most recent index.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The core problem is to find pairs $(i, j)$ with $i < j$ such that $nums[j]$ is the reversed version of $nums[i]$, while minimizing $j - i$. We can solve this efficiently by iterating through the array once and using a hash map to keep track of the most recent index where each 'mirror value' was seen. Specifically, at each index $j$, we check if the current value $nums[j]$ has been registered as a reversed value of any previous element $nums[i]$. To always get the minimum distance for $j$, we only need to care about the largest index $i < j$ that satisfies the condition.

During the linear scan, for each element $nums[j]$, we look up $nums[j]$ in our hash map. If it exists, the stored value is the most recent index $i$ where $reverse(nums[i])$ equals the current $nums[j]$, thus providing a candidate for the minimum distance. After checking the map, we calculate $r = reverse(nums[j])$ and update the map with the entry `r: j`. This ensures that for any future element $nums[k]$ ($k > j$), if $nums[k] == reverse(nums[j])$, it will find the closest possible index $j$.

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
    int minMirrorPairDistance(vector<int>& nums) {
        long long min_dist = -1;
        std::unordered_map<long long, int> last_seen_rev;

        for (int j = 0; j < nums.size(); ++j) {
            long long current = nums[j];
            if (last_seen_rev.count(current)) {
                int dist = j - last_seen_rev[current];
                if (min_dist == -1 || dist < min_dist) {
                    min_dist = dist;
                }
            }

            long long rev = 0;
            long long temp = nums[j];
            while (temp > 0) {
                rev = rev * 10 + (temp % 10);
                temp /= 10;
            }
            last_seen_rev[rev] = j;
        }

        return (int)min_dist;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int minMirrorPairDistance(int[] nums) {
        int minDist = Integer.MAX_VALUE;
        java.util.HashMap<Long, Integer> lastSeenRev = new java.util.HashMap<>();

        for (int j = 0; j < nums.length; j++) {
            long current = (long) nums[j];
            if (lastSeenRev.containsKey(current)) {
                minDist = Math.min(minDist, j - lastSeenRev.get(current));
            }

            long rev = 0;
            long temp = current;
            while (temp > 0) {
                rev = rev * 10 + (temp % 10);
                temp /= 10;
            }
            lastSeenRev.put(rev, j);
        }

        return (minDist == Integer.MAX_VALUE) ? -1 : minDist;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def minMirrorPairDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last_seen_rev = {}
        min_dist = float('inf')

        for j, num in enumerate(nums):
            if num in last_seen_rev:
                min_dist = min(min_dist, j - last_seen_rev[num])

            rev = 0
            temp = num
            while temp > 0:
                rev = rev * 10 + (temp % 10)
                temp //= 10
            last_seen_rev[rev] = j

        return int(min_dist) if min_dist != float('inf') else -1
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        last_seen_rev = {}
        min_dist = float('inf')

        for j, num in enumerate(nums):
            if num in last_seen_rev:
                min_dist = min(min_dist, j - last_seen_rev[num])

            rev = 0
            temp = num
            while temp > 0:
                rev = rev * 10 + (temp % 10)
                temp //= 10
            last_seen_rev[rev] = j

        return int(min_dist) if min_dist != float('inf') else -1
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <limits.h>

#define TABLE_SIZE 300007

long long get_reverse(int n) {
    long long rev = 0;
    while (n > 0) {
        rev = rev * 10 + (n % 10);
        n /= 10;
    }
    return rev;
}

int minMirrorPairDistance(int* nums, int numsSize) {
    long long* keys = (long long*)malloc(sizeof(long long) * TABLE_SIZE);
    int* values = (int*)malloc(sizeof(int) * TABLE_SIZE);
    for (int i = 0; i < TABLE_SIZE; i++) values[i] = -1;

    int min_dist = INT_MAX;

    for (int j = 0; j < numsSize; j++) {
        long long current = (long long)nums[j];
        unsigned int h1 = (unsigned int)(current % TABLE_SIZE);
        while (values[h1] != -1) {
            if (keys[h1] == current) {
                int d = j - values[h1];
                if (d < min_dist) min_dist = d;
                break;
            }
            h1 = (h1 + 1) % TABLE_SIZE;
        }

        long long rev = get_reverse(nums[j]);
        unsigned int h2 = (unsigned int)(rev % TABLE_SIZE);
        while (values[h2] != -1 && keys[h2] != rev) {
            h2 = (h2 + 1) % TABLE_SIZE;
        }
        keys[h2] = rev;
        values[h2] = j;
    }

    free(keys);
    free(values);
    return (min_dist == INT_MAX) ? -1 : min_dist;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;
using System.Collections.Generic;

public class Solution {
    public int MinMirrorPairDistance(int[] nums) {
        int minDist = int.MaxValue;
        Dictionary<int, int> lastSeenIndices = new Dictionary<int, int>();

        for (int j = 0; j < nums.Length; j++) {
            int val = nums[j];
            if (lastSeenIndices.ContainsKey(val)) {
                int currentDist = j - lastSeenIndices[val];
                if (currentDist < minDist) {
                    minDist = currentDist;
                }
            }

            int revVal = 0;
            int temp = val;
            while (temp > 0) {
                revVal = revVal * 10 + (temp % 10);
                temp /= 10;
            }
            lastSeenIndices[revVal] = j;
        }

        return minDist == int.MaxValue ? -1 : minDist;
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
 * @return {number}
 */
var minMirrorPairDistance = function(nums) {
    let minDist = Infinity;
    const lastSeenIndices = new Map();

    for (let j = 0; j < nums.length; j++) {
        const val = nums[j];
        if (lastSeenIndices.has(val)) {
            minDist = Math.min(minDist, j - lastSeenIndices.get(val));
        }

        let revVal = 0;
        let temp = val;
        while (temp > 0) {
            revVal = revVal * 10 + (temp % 10);
            temp = Math.floor(temp / 10);
        }
        lastSeenIndices.set(revVal, j);
    }

    return minDist === Infinity ? -1 : minDist;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minMirrorPairDistance(nums: number[]): number {
    let minDist = Infinity;
    const lastSeenIndices = new Map<number, number>();

    for (let j = 0; j < nums.length; j++) {
        const val = nums[j];
        if (lastSeenIndices.has(val)) {
            minDist = Math.min(minDist, j - lastSeenIndices.get(val)!);
        }

        let revVal = 0;
        let temp = val;
        while (temp > 0) {
            revVal = revVal * 10 + (temp % 10);
            temp = Math.floor(temp / 10);
        }
        lastSeenIndices.set(revVal, j);
    }

    return minDist === Infinity ? -1 : minDist;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minMirrorPairDistance($nums) {
        $minDist = -1;
        $lastSeenIndices = [];

        foreach ($nums as $j => $val) {
            if (isset($lastSeenIndices[$val])) {
                $dist = $j - $lastSeenIndices[$val];
                if ($minDist === -1 || $dist < $minDist) {
                    $minDist = $dist;
                }
            }

            $revVal = 0;
            $temp = $val;
            while ($temp > 0) {
                $revVal = $revVal * 10 + ($temp % 10);
                $temp = (int)($temp / 10);
            }
            $lastSeenIndices[$revVal] = $j;
        }

        return $minDist;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minMirrorPairDistance(_ nums: [Int]) -> Int {
        var minDist = -1
        var lastSeenIndices = [Int: Int]()

        for j in 0..<nums.count {
            let val = nums[j]
            if let i = lastSeenIndices[val] {
                let dist = j - i
                if minDist == -1 || dist < minDist {
                    minDist = dist
                }
            }

            var revVal = 0
            var temp = val
            while temp > 0 {
                revVal = revVal * 10 + (temp % 10)
                temp /= 10
            }
            lastSeenIndices[revVal] = j
        }

        return minDist
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minMirrorPairDistance(nums: IntArray): Int {
        val lastSeenTarget = mutableMapOf<Int, Int>()
        var minDist = -1
        for (j in nums.indices) {
            val currentVal = nums[j]
            if (lastSeenTarget.containsKey(currentVal)) {
                val dist = j - lastSeenTarget[currentVal]!!
                if (minDist == -1 || dist < minDist) {
                    minDist = dist
                }
            }
            var num = currentVal
            var rev = 0
            while (num > 0) {
                rev = rev * 10 + (num % 10)
                num /= 10
            }
            lastSeenTarget[rev] = j
        }
        return minDist
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int minMirrorPairDistance(List<int> nums) {
    Map<int, int> lastSeenTarget = {};
    int minDist = -1;
    for (int j = 0; j < nums.length; j++) {
      int currentVal = nums[j];
      if (lastSeenTarget.containsKey(currentVal)) {
        int dist = j - lastSeenTarget[currentVal]!;
        if (minDist == -1 || dist < minDist) {
          minDist = dist;
        }
      }
      int num = currentVal;
      int rev = 0;
      while (num > 0) {
        rev = rev * 10 + (num % 10);
        num ~/= 10;
      }
      lastSeenTarget[rev] = j;
    }
    return minDist;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func minMirrorPairDistance(nums []int) int {
    lastSeenTarget := make(map[int]int)
    minDist := -1
    for j, currentVal := range nums {
        if pos, ok := lastSeenTarget[currentVal]; ok {
            dist := j - pos
            if minDist == -1 || dist < minDist {
                minDist = dist
            }
        }
        num := currentVal
        rev := 0
        for num > 0 {
            rev = rev*10 + num%10
            num /= 10
        }
        lastSeenTarget[rev] = j
    }
    return minDist
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @return {Integer}
def min_mirror_pair_distance(nums)
  last_seen_target = {}
  min_dist = -1
  nums.each_with_index do |current_val, j|
    if last_seen_target.has_key?(current_val)
      dist = j - last_seen_target[current_val]
      if min_dist == -1 || dist < min_dist
        min_dist = dist
      end
    end
    num = current_val
    rev = 0
    while num > 0
      rev = rev * 10 + (num % 10)
      num /= 10
    end
    last_seen_target[rev] = j
  end
  min_dist
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def minMirrorPairDistance(nums: Array[Int]): Int = {
        val lastSeenTarget = scala.collection.mutable.Map[Int, Int]()
        var minDist = -1
        for (j <- nums.indices) {
            val currentVal = nums(j)
            if (lastSeenTarget.contains(currentVal)) {
                val dist = j - lastSeenTarget(currentVal)
                if (minDist == -1 || dist < minDist) {
                    minDist = dist
                }
            }
            var num = currentVal
            var rev = 0
            while (num > 0) {
                rev = rev * 10 + (num % 10)
                num /= 10
            }
            lastSeenTarget(rev) = j
        }
        minDist
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
use std::collections::HashMap;

impl Solution {
    pub fn min_mirror_pair_distance(nums: Vec<i32>) -> i32 {
        let mut last_pos: HashMap<i32, usize> = HashMap::new();
        let mut min_dist = i32::MAX;
        let mut found = false;

        for (j, &num) in nums.iter().enumerate() {
            if let Some(&i) = last_pos.get(&num) {
                let dist = (j - i) as i32;
                if dist < min_dist {
                    min_dist = dist;
                }
                found = true;
            }

            let mut n = num;
            let mut rev = 0;
            while n > 0 {
                rev = rev * 10 + n % 10;
                n /= 10;
            }
            last_pos.insert(rev, j);
        }

        if found { min_dist } else { -1 }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (min-mirror-pair-distance nums)
  (-> (listof exact-integer?) exact-integer?)
  (let-values ([(final-min-dist final-last-pos)
                 (for/fold ([min-dist #f]
                            [last-pos (hash)])
                           ([num (in-list nums)]
                            [j (in-naturals)])
                   (let* ([i (hash-ref last-pos num #f)]
                          [new-min-dist (if i
                                           (let ([dist (- j i)])
                                             (if (or (not min-dist) (< dist min-dist))
                                                 dist
                                                 min-dist))
                                           min-dist)]
                          [rev (let loop ([n num] [res 0])
                                 (if (= n 0)
                                     res
                                     (loop (quotient n 10) (+ (* res 10) (remainder n 10)))))])
                     (values new-min-dist (hash-set last-pos rev j))))])
    (if final-min-dist final-min-dist -1)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec min_mirror_pair_distance(Nums :: [integer()]) -> integer().
min_mirror_pair_distance(Nums) ->
    solve(Nums, 0, #{}, -1).

solve([], _J, _LastPos, MinDist) ->
    MinDist;
solve([Num | Rest], J, LastPos, MinDist) ->
    NewMinDist = case maps:find(Num, LastPos) of
        {ok, I} ->
            Dist = J - I,
            if
                MinDist =:= -1 -> Dist;
                Dist < MinDist -> Dist;
                true -> MinDist
            end;
        error ->
            MinDist
    end,
    Rev = reverse_num(Num, 0),
    solve(Rest, J + 1, maps:put(Rev, J, LastPos), NewMinDist).

reverse_num(0, Rev) -> Rev;
reverse_num(N, Rev) -> reverse_num(N div 10, Rev * 10 + (N rem 10)).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec min_mirror_pair_distance(nums :: [integer]) :: integer
  def min_mirror_pair_distance(nums) do
    {min_dist, _} = Enum.reduce(Enum.with_index(nums), {nil, %{}}, fn {num, j}, {min_dist, last_pos} ->
      new_min_dist = case Map.get(last_pos, num) do
        nil -> min_dist
        i ->
          dist = j - i
          if is_nil(min_dist) or dist < min_dist, do: dist, else: min_dist
      end

      rev = reverse_num(num)
      {new_min_dist, Map.put(last_pos, rev, j)}
    end)

    min_dist || -1
  end

  defp reverse_num(n, rev \\ 0)
  defp reverse_num(0, rev), do: rev
  defp reverse_num(n, rev), do: reverse_num(div(n, 10), rev * 10 + rem(n, 10))
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N) where N is the length of the nums array. For each element, we reverse its digits (at most 10 digits for a number up to $10^9$) and perform hash map insertions and lookups, which take $O(1)$ on average.
- **Space Complexity:** O(N) to store the indices of the reversed numbers in a hash map, with at most N entries in the worst case.
