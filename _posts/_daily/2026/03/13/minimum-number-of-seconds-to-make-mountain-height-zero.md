---
layout: post
title: "Minimum Number of Seconds to Make Mountain Height Zero"
date: 2026-03-13 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Math", "Binary Search", "Greedy", "Heap (Priority Queue)"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    long long minNumberOfSeconds(int mountainHeight,\
        \ vector<int>& workerTimes) {\n        long long low = 0;\n        int minW\
        \ = workerTimes[0];\n        for (int w : workerTimes) if (w < minW) minW =\
        \ w;\n\n        long long high = (long long)minW * mountainHeight * (mountainHeight\
        \ + 1LL) / 2LL;\n        long long ans = high;\n\n        while (low <= high)\
        \ {\n            long long mid = low + (high - low) / 2LL;\n            if (check(mid,\
        \ mountainHeight, workerTimes)) {\n                ans = mid;\n            \
        \    high = mid - 1LL;\n            } else {\n                low = mid + 1LL;\n\
        \            }\n        }\n        return ans;\n    }\n\nprivate:\n    bool\
        \ check(long long t, int mountainHeight, const vector<int>& workerTimes) {\n\
        \        long long total_h = 0;\n        for (int w : workerTimes) {\n     \
        \       long long x = (long long)((sqrt(8.0 * t / w + 1.0) - 1.0) / 2.0);\n\
        \            total_h += x;\n            if (total_h >= mountainHeight) return\
        \ true;\n        }\n        return false;\n    }\n};"
      java: "class Solution {\n    public long minNumberOfSeconds(int mountainHeight,\
        \ int[] workerTimes) {\n        long low = 0;\n        int minW = workerTimes[0];\n\
        \        for (int w : workerTimes) {\n            if (w < minW) minW = w;\n\
        \        }\n        long high = (long) minW * mountainHeight * (mountainHeight\
        \ + 1L) / 2L;\n        long ans = high;\n        while (low <= high) {\n   \
        \         long mid = low + (high - low) / 2;\n            if (check(mid, mountainHeight,\
        \ workerTimes)) {\n                ans = mid;\n                high = mid -\
        \ 1;\n            } else {\n                low = mid + 1;\n            }\n\
        \        }\n        return ans;\n    }\n\n    private boolean check(long t,\
        \ int mountainHeight, int[] workerTimes) {\n        long totalH = 0;\n     \
        \   for (int w : workerTimes) {\n            long x = (long) ((Math.sqrt(8.0\
        \ * t / w + 1.0) - 1.0) / 2.0);\n            totalH += x;\n            if (totalH\
        \ >= mountainHeight) return true;\n        }\n        return false;\n    }\n\
        }"
      python: "import math\n\nclass Solution(object):\n    def minNumberOfSeconds(self,\
        \ mountainHeight, workerTimes):\n        \"\"\"\n        :type mountainHeight:\
        \ int\n        :type workerTimes: List[int]\n        :rtype: int\n        \"\
        \"\"\n        def check(t):\n            total_h = 0\n            for w in workerTimes:\n\
        \                k = (8 * t) // w + 1\n                x = (int(math.sqrt(k))\
        \ - 1) // 2\n                total_h += x\n                if total_h >= mountainHeight:\n\
        \                    return True\n            return False\n\n        low =\
        \ 0\n        high = min(workerTimes) * mountainHeight * (mountainHeight + 1)\
        \ // 2\n        ans = high\n        while low <= high:\n            mid = (low\
        \ + high) // 2\n            if check(mid):\n                ans = mid\n    \
        \            high = mid - 1\n            else:\n                low = mid +\
        \ 1\n        return ans"
      python3: "import math\n\nclass Solution:\n    def minNumberOfSeconds(self, mountainHeight:\
        \ int, workerTimes: List[int]) -> int:\n        def check(t):\n            total_h\
        \ = 0\n            for w in workerTimes:\n                k = (8 * t) // w +\
        \ 1\n                x = (math.isqrt(k) - 1) // 2\n                total_h +=\
        \ x\n                if total_h >= mountainHeight:\n                    return\
        \ True\n            return False\n\n        low = 0\n        high = min(workerTimes)\
        \ * mountainHeight * (mountainHeight + 1) // 2\n        ans = high\n       \
        \ while low <= high:\n            mid = (low + high) // 2\n            if check(mid):\n\
        \                ans = mid\n                high = mid - 1\n            else:\n\
        \                low = mid + 1\n        return ans"
      c: "#include <math.h>\n#include <stdio.h>\n\nlong long minNumberOfSeconds(int\
        \ mountainHeight, int* workerTimes, int workerTimesSize) {\n    long long minW\
        \ = workerTimes[0];\n    for (int i = 1; i < workerTimesSize; i++) {\n     \
        \   if (workerTimes[i] < minW) minW = workerTimes[i];\n    }\n\n    long long\
        \ low = 0;\n    long long high = minW * (long long)mountainHeight * (mountainHeight\
        \ + 1LL) / 2LL;\n    long long ans = high;\n\n    while (low <= high) {\n  \
        \      long long mid = low + (high - low) / 2LL;\n        long long total_h\
        \ = 0;\n        for (int i = 0; i < workerTimesSize; i++) {\n            long\
        \ long x = (long long)((sqrt(8.0 * mid / workerTimes[i] + 1.0) - 1.0) / 2.0);\n\
        \            total_h += x;\n            if (total_h >= mountainHeight) break;\n\
        \        }\n\n        if (total_h >= mountainHeight) {\n            ans = mid;\n\
        \            high = mid - 1LL;\n        } else {\n            low = mid + 1LL;\n\
        \        }\n    }\n    return ans;\n}"
      csharp: "using System;\n\npublic class Solution {\n    public long MinNumberOfSeconds(int\
        \ mountainHeight, int[] workerTimes) {\n        long low = 0;\n        int minW\
        \ = workerTimes[0];\n        foreach (int w in workerTimes) {\n            if\
        \ (w < minW) minW = w;\n        }\n\n        long high = (long)minW * mountainHeight\
        \ * (mountainHeight + 1L) / 2L;\n        long ans = high;\n\n        while (low\
        \ <= high) {\n            long mid = low + (high - low) / 2;\n            if\
        \ (Check(mid, mountainHeight, workerTimes)) {\n                ans = mid;\n\
        \                high = mid - 1;\n            } else {\n                low\
        \ = mid + 1;\n            }\n        }\n        return ans;\n    }\n\n    private\
        \ bool Check(long t, int mountainHeight, int[] workerTimes) {\n        long\
        \ totalH = 0;\n        foreach (int w in workerTimes) {\n            long x\
        \ = (long)((Math.Sqrt(8.0 * t / w + 1.0) - 1.0) / 2.0);\n            totalH\
        \ += x;\n            if (totalH >= mountainHeight) return true;\n        }\n\
        \        return false;\n    }\n}"
      javascript: "/**\n * @param {number} mountainHeight\n * @param {number[]} workerTimes\n\
        \ * @return {number}\n */\nvar minNumberOfSeconds = function(mountainHeight,\
        \ workerTimes) {\n    let low = 0n;\n    let minW = BigInt(Math.min(...workerTimes));\n\
        \    let h = BigInt(mountainHeight);\n    let high = minW * h * (h + 1n) / 2n;\n\
        \    let ans = high;\n\n    while (low <= high) {\n        let mid = (low +\
        \ high) / 2n;\n        let total_h = 0n;\n        for (let w of workerTimes)\
        \ {\n            let bw = BigInt(w);\n            let k = (8n * mid) / bw +\
        \ 1n;\n            let x = BigInt(Math.floor((Math.sqrt(Number(k)) - 1) / 2));\n\
        \            total_h += x;\n            if (total_h >= h) break;\n        }\n\
        \n        if (total_h >= h) {\n            ans = mid;\n            high = mid\
        \ - 1n;\n        } else {\n            low = mid + 1n;\n        }\n    }\n \
        \   return Number(ans);\n};"
      typescript: "function minNumberOfSeconds(mountainHeight: number, workerTimes:\
        \ number[]): number {\n    let minWValue = workerTimes[0];\n    for (let w of\
        \ workerTimes) {\n        if (w < minWValue) minWValue = w;\n    }\n    let\
        \ minW = BigInt(minWValue);\n    let h = BigInt(mountainHeight);\n    let low\
        \ = 0n;\n    let high = minW * h * (h + 1n) / 2n;\n    let ans = high;\n\n \
        \   while (low <= high) {\n        let mid = low + (high - low) / 2n;\n    \
        \    let totalHeight = 0n;\n        let midNum = Number(mid);\n        for (let\
        \ w of workerTimes) {\n            let x = Math.floor((Math.sqrt(1 + 8 * (midNum\
        \ / w)) - 1) / 2);\n            totalHeight += BigInt(x);\n            if (totalHeight\
        \ >= h) break;\n        }\n\n        if (totalHeight >= h) {\n            ans\
        \ = mid;\n            high = mid - 1n;\n        } else {\n            low =\
        \ mid + 1n;\n        }\n    }\n    return Number(ans);\n}"
      php: "class Solution {\n\n    /**\n     * @param Integer $mountainHeight\n   \
        \  * @param Integer[] $workerTimes\n     * @return Integer\n     */\n    function\
        \ minNumberOfSeconds($mountainHeight, $workerTimes) {\n        $minW = $workerTimes[0];\n\
        \        foreach ($workerTimes as $w) {\n            if ($w < $minW) $minW =\
        \ $w;\n        }\n        $low = 0;\n        $high = (int)($minW * $mountainHeight\
        \ * ($mountainHeight + 1) / 2);\n        $ans = $high;\n\n        while ($low\
        \ <= $high) {\n            $mid = $low + (int)(($high - $low) / 2);\n      \
        \      $totalHeight = 0;\n            foreach ($workerTimes as $w) {\n     \
        \           $totalHeight += (int)((sqrt(1 + 8 * ($mid / $w)) - 1) / 2);\n  \
        \              if ($totalHeight >= $mountainHeight) break;\n            }\n\
        \            if ($totalHeight >= $mountainHeight) {\n                $ans =\
        \ $mid;\n                $high = $mid - 1;\n            } else {\n         \
        \       $low = $mid + 1;\n            }\n        }\n        return $ans;\n \
        \   }\n}"
      swift: "import Foundation\n\nclass Solution {\n    func minNumberOfSeconds(_ mountainHeight:\
        \ Int, _ workerTimes: [Int]) -> Int {\n        let minW = workerTimes.min()\
        \ ?? 0\n        var low = 0\n        var high = minW * mountainHeight * (mountainHeight\
        \ + 1) / 2\n        var ans = high\n\n        while low <= high {\n        \
        \    let mid = low + (high - low) / 2\n            var totalHeight = 0\n   \
        \         for w in workerTimes {\n                let x = Int((sqrt(1.0 + 8.0\
        \ * (Double(mid) / Double(w))) - 1.0) / 2.0)\n                totalHeight +=\
        \ x\n                if totalHeight >= mountainHeight { break }\n          \
        \  }\n            if totalHeight >= mountainHeight {\n                ans =\
        \ mid\n                high = mid - 1\n            } else {\n              \
        \  low = mid + 1\n            }\n        }\n        return ans\n    }\n}"
      kotlin: "class Solution {\n    fun minNumberOfSeconds(mountainHeight: Int, workerTimes:\
        \ IntArray): Long {\n        var minW = workerTimes[0].toLong()\n        for\
        \ (w in workerTimes) {\n            if (w.toLong() < minW) minW = w.toLong()\n\
        \        }\n        val h = mountainHeight.toLong()\n        var low = 0L\n\
        \        var high = minW * h * (h + 1) / 2\n        var ans = high\n\n     \
        \   while (low <= high) {\n            val mid = low + (high - low) / 2\n  \
        \          var totalHeight = 0L\n            for (w in workerTimes) {\n    \
        \            val x = ((Math.sqrt(1.0 + 8.0 * (mid.toDouble() / w.toDouble()))\
        \ - 1.0) / 2.0).toLong()\n                totalHeight += x\n               \
        \ if (totalHeight >= h) break\n            }\n            if (totalHeight >=\
        \ h) {\n                ans = mid\n                high = mid - 1\n        \
        \    } else {\n                low = mid + 1\n            }\n        }\n   \
        \     return ans\n    }\n}"
      dart: "import 'dart:math';\n\nclass Solution {\n  int minNumberOfSeconds(int mountainHeight,\
        \ List<int> workerTimes) {\n    int minW = workerTimes.reduce((a, b) => a <\
        \ b ? a : b);\n    int low = 0;\n    int high = (minW * mountainHeight * (mountainHeight\
        \ + 1) ~/ 2);\n    int ans = high;\n\n    while (low <= high) {\n      int mid\
        \ = low + (high - low) ~/ 2;\n      int totalHeight = 0;\n      for (int w in\
        \ workerTimes) {\n        int x = ((sqrt(1 + 8 * (mid / w)) - 1) / 2).floor();\n\
        \        totalHeight += x;\n        if (totalHeight >= mountainHeight) break;\n\
        \      }\n      if (totalHeight >= mountainHeight) {\n        ans = mid;\n \
        \       high = mid - 1;\n      } else {\n        low = mid + 1;\n      }\n \
        \   }\n    return ans;\n  }\n}"
      go: "import (\n    \"math\"\n)\n\nfunc minNumberOfSeconds(mountainHeight int,\
        \ workerTimes []int) int64 {\n    minW := workerTimes[0]\n    for _, w := range\
        \ workerTimes {\n        if w < minW {\n            minW = w\n        }\n  \
        \  }\n    h := int64(mountainHeight)\n    var low int64 = 0\n    var high int64\
        \ = int64(minW) * h * (h + 1) / 2\n    ans := high\n\n    for low <= high {\n\
        \        mid := low + (high-low)/2\n        var totalHeight int64 = 0\n    \
        \    for _, w := range workerTimes {\n            x := int64((math.Sqrt(1 +\
        \ 8*(float64(mid)/float64(w))) - 1) / 2)\n            totalHeight += x\n   \
        \         if totalHeight >= h {\n                break\n            }\n    \
        \    }\n        if totalHeight >= h {\n            ans = mid\n            high\
        \ = mid - 1\n        } else {\n            low = mid + 1\n        }\n    }\n\
        \    return ans\n}"
      ruby: "def min_number_of_seconds(mountain_height, worker_times)\n  l = 0\n  min_w\
        \ = worker_times.min\n  r = min_w * mountain_height * (mountain_height + 1)\
        \ / 2\n  ans = r\n  while l <= r\n    mid = (l + r) / 2\n    total_height =\
        \ 0\n    worker_times.each do |w|\n      x = (Integer.sqrt(1 + 8 * mid / w)\
        \ - 1) / 2\n      total_height += x\n      break if total_height >= mountain_height\n\
        \    end\n    if total_height >= mountain_height\n      ans = mid\n      r =\
        \ mid - 1\n    else\n      l = mid + 1\n    end\n  end\n  ans\nend"
      scala: "object Solution {\n    def minNumberOfSeconds(mountainHeight: Int, workerTimes:\
        \ Array[Int]): Long = {\n        val minW = workerTimes.min.toLong\n       \
        \ val h = mountainHeight.toLong\n        var l: Long = 0\n        var r: Long\
        \ = minW * h * (h + 1) / 2\n        var ans: Long = r\n        while (l <= r)\
        \ {\n            val mid = l + (r - l) / 2\n            var total: Long = 0\n\
        \            var i = 0\n            while (i < workerTimes.length && total <\
        \ mountainHeight) {\n                val w = workerTimes(i)\n              \
        \  val x = ((Math.sqrt(1.0 + 8.0 * mid / w) - 1.0) / 2.0).toLong\n         \
        \       total += x\n                i += 1\n            }\n            if (total\
        \ >= mountainHeight) {\n                ans = mid\n                r = mid -\
        \ 1\n            } else {\n                l = mid + 1\n            }\n    \
        \    }\n        ans\n    }\n}"
      rust: "impl Solution {\n    pub fn min_number_of_seconds(mountain_height: i32,\
        \ worker_times: Vec<i32>) -> i64 {\n        let h = mountain_height as i64;\n\
        \        let min_w = *worker_times.iter().min().unwrap() as i64;\n        let\
        \ mut l: i64 = 0;\n        let mut r: i64 = min_w * h * (h + 1) / 2;\n     \
        \   let mut ans = r;\n        while l <= r {\n            let mid = l + (r -\
        \ l) / 2;\n            let mut total: i64 = 0;\n            for &w in &worker_times\
        \ {\n                let w64 = w as i64;\n                let k = 8 * mid /\
        \ w64;\n                let x = (((1 + k) as f64).sqrt() as i64 - 1) / 2;\n\
        \                total += x;\n                if total >= h {\n            \
        \        break;\n                }\n            }\n            if total >= h\
        \ {\n                ans = mid;\n                r = mid - 1;\n            }\
        \ else {\n                l = mid + 1;\n            }\n        }\n        ans\n\
        \    }\n}"
      racket: "(define/contract (min-number-of-seconds mountainHeight workerTimes)\n\
        \  (-> exact-integer? (listof exact-integer?) exact-integer?)\n  (let* ([min-w\
        \ (apply min workerTimes)]\n         [initial-r (quotient (* min-w mountainHeight\
        \ (+ mountainHeight 1)) 2)])\n    (let loop ([l 0]\n               [r initial-r]\n\
        \               [ans initial-r])\n      (if (<= l r)\n          (let* ([mid\
        \ (quotient (+ l r) 2)]\n                 [total (for/fold ([sum 0])\n     \
        \                             ([w workerTimes] #:break (>= sum mountainHeight))\n\
        \                          (+ sum (quotient (- (integer-sqrt (+ 1 (quotient\
        \ (* 8 mid) w))) 1) 2)))])\n            (if (>= total mountainHeight)\n    \
        \            (loop l (- mid 1) mid)\n                (loop (+ mid 1) r ans)))\n\
        \          ans))))"
      erlang: "-spec min_number_of_seconds(MountainHeight :: integer(), WorkerTimes\
        \ :: [integer()]) -> integer().\nmin_number_of_seconds(MountainHeight, WorkerTimes)\
        \ ->\n    MinW = lists:min(WorkerTimes),\n    R = MinW * MountainHeight * (MountainHeight\
        \ + 1) div 2,\n    binary_search(0, R, R, MountainHeight, WorkerTimes).\n\n\
        binary_search(L, R, Ans, MountainHeight, WorkerTimes) when L =< R ->\n    Mid\
        \ = (L + R) div 2,\n    case check_height(Mid, MountainHeight, WorkerTimes)\
        \ of\n        true -> binary_search(L, Mid - 1, Mid, MountainHeight, WorkerTimes);\n\
        \        false -> binary_search(Mid + 1, R, Ans, MountainHeight, WorkerTimes)\n\
        \    end;\nbinary_search(_L, _R, Ans, _MountainHeight, _WorkerTimes) ->\n  \
        \  Ans.\n\ncheck_height(Mid, MountainHeight, WorkerTimes) ->\n    check_height_acc(Mid,\
        \ MountainHeight, WorkerTimes, 0).\n\ncheck_height_acc(_Mid, MountainHeight,\
        \ _, Acc) when Acc >= MountainHeight -> true;\ncheck_height_acc(_Mid, _MountainHeight,\
        \ [], _Acc) -> false;\ncheck_height_acc(Mid, MountainHeight, [W|Rest], Acc)\
        \ ->\n    K = (8 * Mid) div W,\n    X = (trunc(math:sqrt(1 + K)) - 1) div 2,\n\
        \    check_height_acc(Mid, MountainHeight, Rest, Acc + X)."
      elixir: "defmodule Solution do\n  @spec min_number_of_seconds(mountain_height\
        \ :: integer, worker_times :: [integer]) :: integer\n  def min_number_of_seconds(mountain_height,\
        \ worker_times) do\n    min_w = Enum.min(worker_times)\n    r = div(min_w *\
        \ mountain_height * (mountain_height + 1), 2)\n    binary_search(0, r, r, mountain_height,\
        \ worker_times)\n  end\n\n  defp binary_search(l, r, ans, mountain_height, worker_times)\
        \ when l <= r do\n    mid = div(l + r, 2)\n    if check(mid, mountain_height,\
        \ worker_times) do\n      binary_search(l, mid - 1, mid, mountain_height, worker_times)\n\
        \    else\n      binary_search(mid + 1, r, ans, mountain_height, worker_times)\n\
        \    end\n  end\n  defp binary_search(_l, _r, ans, _mountain_height, _worker_times),\
        \ do: ans\n\n  defp check(mid, mountain_height, worker_times) do\n    Enum.reduce_while(worker_times,\
        \ 0, fn w, acc ->\n      k = div(8 * mid, w)\n      x = div(trunc(:math.sqrt(1\
        \ + k)) - 1, 2)\n      new_acc = acc + x\n      if new_acc >= mountain_height,\
        \ do: {:halt, new_acc}, else: {:cont, new_acc}\n    end) >= mountain_height\n\
        \  end\nend"
    approach: 'To find the minimum time required to reduce the mountain''s height to
      zero, we observe that the total reduction achieved by all workers is a monotonically
      increasing function of time. This property allows us to use binary search over
      the possible range of time. The lower bound of the search is 0, and the upper
      bound is the time it would take the most efficient worker (with the minimum $workerTimes[i]$)
      to reduce the entire mountain height alone, calculated as $min(workerTimes) \cdot
      \frac{mountainHeight(mountainHeight + 1)}{2}$.


      For a given time $T$ in the binary search, we determine the maximum height $x_i$
      each worker $i$ can reduce by solving the inequality $workerTimes[i] \cdot \frac{x_i(x_i+1)}{2}
      \le T$. Rearranging this quadratic inequality, we find $x_i = \lfloor \frac{-1
      + \sqrt{1 + 8T/workerTimes[i]}}{2} \rfloor$. If the sum of all $x_i$ for all workers
      is at least $mountainHeight$, the given time $T$ is sufficient, and we attempt
      to find a smaller time. Otherwise, we increase the time. Using 64-bit integers
      ensures we handle the large time values (up to $5 \cdot 10^{15}$) safely.'
    time_complexity: O(N \log(min(workerTimes) \cdot H^2)), where $N$ is the number
      of workers and $H$ is the mountain height. The binary search range spans $O(min(W)
      \cdot H^2)$, and each check takes $O(N)$ time to iterate through the workers and
      calculate their height reductions using the quadratic formula.
    space_complexity: O(1) as we only use a constant amount of extra space for variables
      during the binary search, independent of the input size.
    elapsed_time: 255.91339349746704
    model: gemini-3-flash-preview
    generated_at: '2026-03-13 01:27:00 '
---

## Problem #3296: Minimum Number of Seconds to Make Mountain Height Zero

**Difficulty:** Medium

**Topics:** Array, Math, Binary Search, Greedy, Heap (Priority Queue)

## Problem Description

<p>You are given an integer <code>mountainHeight</code> denoting the height of a mountain.</p>

<p>You are also given an integer array <code>workerTimes</code> representing the work time of workers in <strong>seconds</strong>.</p>

<p>The workers work <strong>simultaneously</strong> to <strong>reduce</strong> the height of the mountain. For worker <code>i</code>:</p>

<ul>
	<li>To decrease the mountain&#39;s height by <code>x</code>, it takes <code>workerTimes[i] + workerTimes[i] * 2 + ... + workerTimes[i] * x</code> seconds. For example:

	<ul>
		<li>To reduce the height of the mountain by 1, it takes <code>workerTimes[i]</code> seconds.</li>
		<li>To reduce the height of the mountain by 2, it takes <code>workerTimes[i] + workerTimes[i] * 2</code> seconds, and so on.</li>
	</ul>
	</li>
</ul>

<p>Return an integer representing the <strong>minimum</strong> number of seconds required for the workers to make the height of the mountain 0.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">mountainHeight = 4, workerTimes = [2,1,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>One way the height of the mountain can be reduced to 0 is:</p>

<ul>
	<li>Worker 0 reduces the height by 1, taking <code>workerTimes[0] = 2</code> seconds.</li>
	<li>Worker 1 reduces the height by 2, taking <code>workerTimes[1] + workerTimes[1] * 2 = 3</code> seconds.</li>
	<li>Worker 2 reduces the height by 1, taking <code>workerTimes[2] = 1</code> second.</li>
</ul>

<p>Since they work simultaneously, the minimum time needed is <code>max(2, 3, 1) = 3</code> seconds.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">mountainHeight = 10, workerTimes = [3,2,2,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">12</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Worker 0 reduces the height by 2, taking <code>workerTimes[0] + workerTimes[0] * 2 = 9</code> seconds.</li>
	<li>Worker 1 reduces the height by 3, taking <code>workerTimes[1] + workerTimes[1] * 2 + workerTimes[1] * 3 = 12</code> seconds.</li>
	<li>Worker 2 reduces the height by 3, taking <code>workerTimes[2] + workerTimes[2] * 2 + workerTimes[2] * 3 = 12</code> seconds.</li>
	<li>Worker 3 reduces the height by 2, taking <code>workerTimes[3] + workerTimes[3] * 2 = 12</code> seconds.</li>
</ul>

<p>The number of seconds needed is <code>max(9, 12, 12, 12) = 12</code> seconds.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">mountainHeight = 5, workerTimes = [1]</span></p>

<p><strong>Output:</strong> <span class="example-io">15</span></p>

<p><strong>Explanation:</strong></p>

<p>There is only one worker in this example, so the answer is <code>workerTimes[0] + workerTimes[0] * 2 + workerTimes[0] * 3 + workerTimes[0] * 4 + workerTimes[0] * 5 = 15</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= mountainHeight &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= workerTimes.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= workerTimes[i] &lt;= 10<sup>6</sup></code></li>
</ul>


## Hints

1. Can we use binary search to solve this problem?

2. Do a binary search on the number of seconds to check if it's enough to reduce the mountain height to 0 or less with all workers working simultaneously.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To find the minimum time required to reduce the mountain's height to zero, we observe that the total reduction achieved by all workers is a monotonically increasing function of time. This property allows us to use binary search over the possible range of time. The lower bound of the search is 0, and the upper bound is the time it would take the most efficient worker (with the minimum $workerTimes[i]$) to reduce the entire mountain height alone, calculated as $min(workerTimes) \cdot \frac{mountainHeight(mountainHeight + 1)}{2}$.

For a given time $T$ in the binary search, we determine the maximum height $x_i$ each worker $i$ can reduce by solving the inequality $workerTimes[i] \cdot \frac{x_i(x_i+1)}{2} \le T$. Rearranging this quadratic inequality, we find $x_i = \lfloor \frac{-1 + \sqrt{1 + 8T/workerTimes[i]}}{2} \rfloor$. If the sum of all $x_i$ for all workers is at least $mountainHeight$, the given time $T$ is sufficient, and we attempt to find a smaller time. Otherwise, we increase the time. Using 64-bit integers ensures we handle the large time values (up to $5 \cdot 10^{15}$) safely.

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
    long long minNumberOfSeconds(int mountainHeight, vector<int>& workerTimes) {
        long long low = 0;
        int minW = workerTimes[0];
        for (int w : workerTimes) if (w < minW) minW = w;

        long long high = (long long)minW * mountainHeight * (mountainHeight + 1LL) / 2LL;
        long long ans = high;

        while (low <= high) {
            long long mid = low + (high - low) / 2LL;
            if (check(mid, mountainHeight, workerTimes)) {
                ans = mid;
                high = mid - 1LL;
            } else {
                low = mid + 1LL;
            }
        }
        return ans;
    }

private:
    bool check(long long t, int mountainHeight, const vector<int>& workerTimes) {
        long long total_h = 0;
        for (int w : workerTimes) {
            long long x = (long long)((sqrt(8.0 * t / w + 1.0) - 1.0) / 2.0);
            total_h += x;
            if (total_h >= mountainHeight) return true;
        }
        return false;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public long minNumberOfSeconds(int mountainHeight, int[] workerTimes) {
        long low = 0;
        int minW = workerTimes[0];
        for (int w : workerTimes) {
            if (w < minW) minW = w;
        }
        long high = (long) minW * mountainHeight * (mountainHeight + 1L) / 2L;
        long ans = high;
        while (low <= high) {
            long mid = low + (high - low) / 2;
            if (check(mid, mountainHeight, workerTimes)) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return ans;
    }

    private boolean check(long t, int mountainHeight, int[] workerTimes) {
        long totalH = 0;
        for (int w : workerTimes) {
            long x = (long) ((Math.sqrt(8.0 * t / w + 1.0) - 1.0) / 2.0);
            totalH += x;
            if (totalH >= mountainHeight) return true;
        }
        return false;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
import math

class Solution(object):
    def minNumberOfSeconds(self, mountainHeight, workerTimes):
        """
        :type mountainHeight: int
        :type workerTimes: List[int]
        :rtype: int
        """
        def check(t):
            total_h = 0
            for w in workerTimes:
                k = (8 * t) // w + 1
                x = (int(math.sqrt(k)) - 1) // 2
                total_h += x
                if total_h >= mountainHeight:
                    return True
            return False

        low = 0
        high = min(workerTimes) * mountainHeight * (mountainHeight + 1) // 2
        ans = high
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
import math

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        def check(t):
            total_h = 0
            for w in workerTimes:
                k = (8 * t) // w + 1
                x = (math.isqrt(k) - 1) // 2
                total_h += x
                if total_h >= mountainHeight:
                    return True
            return False

        low = 0
        high = min(workerTimes) * mountainHeight * (mountainHeight + 1) // 2
        ans = high
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <math.h>
#include <stdio.h>

long long minNumberOfSeconds(int mountainHeight, int* workerTimes, int workerTimesSize) {
    long long minW = workerTimes[0];
    for (int i = 1; i < workerTimesSize; i++) {
        if (workerTimes[i] < minW) minW = workerTimes[i];
    }

    long long low = 0;
    long long high = minW * (long long)mountainHeight * (mountainHeight + 1LL) / 2LL;
    long long ans = high;

    while (low <= high) {
        long long mid = low + (high - low) / 2LL;
        long long total_h = 0;
        for (int i = 0; i < workerTimesSize; i++) {
            long long x = (long long)((sqrt(8.0 * mid / workerTimes[i] + 1.0) - 1.0) / 2.0);
            total_h += x;
            if (total_h >= mountainHeight) break;
        }

        if (total_h >= mountainHeight) {
            ans = mid;
            high = mid - 1LL;
        } else {
            low = mid + 1LL;
        }
    }
    return ans;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;

public class Solution {
    public long MinNumberOfSeconds(int mountainHeight, int[] workerTimes) {
        long low = 0;
        int minW = workerTimes[0];
        foreach (int w in workerTimes) {
            if (w < minW) minW = w;
        }

        long high = (long)minW * mountainHeight * (mountainHeight + 1L) / 2L;
        long ans = high;

        while (low <= high) {
            long mid = low + (high - low) / 2;
            if (Check(mid, mountainHeight, workerTimes)) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return ans;
    }

    private bool Check(long t, int mountainHeight, int[] workerTimes) {
        long totalH = 0;
        foreach (int w in workerTimes) {
            long x = (long)((Math.Sqrt(8.0 * t / w + 1.0) - 1.0) / 2.0);
            totalH += x;
            if (totalH >= mountainHeight) return true;
        }
        return false;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number} mountainHeight
 * @param {number[]} workerTimes
 * @return {number}
 */
var minNumberOfSeconds = function(mountainHeight, workerTimes) {
    let low = 0n;
    let minW = BigInt(Math.min(...workerTimes));
    let h = BigInt(mountainHeight);
    let high = minW * h * (h + 1n) / 2n;
    let ans = high;

    while (low <= high) {
        let mid = (low + high) / 2n;
        let total_h = 0n;
        for (let w of workerTimes) {
            let bw = BigInt(w);
            let k = (8n * mid) / bw + 1n;
            let x = BigInt(Math.floor((Math.sqrt(Number(k)) - 1) / 2));
            total_h += x;
            if (total_h >= h) break;
        }

        if (total_h >= h) {
            ans = mid;
            high = mid - 1n;
        } else {
            low = mid + 1n;
        }
    }
    return Number(ans);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minNumberOfSeconds(mountainHeight: number, workerTimes: number[]): number {
    let minWValue = workerTimes[0];
    for (let w of workerTimes) {
        if (w < minWValue) minWValue = w;
    }
    let minW = BigInt(minWValue);
    let h = BigInt(mountainHeight);
    let low = 0n;
    let high = minW * h * (h + 1n) / 2n;
    let ans = high;

    while (low <= high) {
        let mid = low + (high - low) / 2n;
        let totalHeight = 0n;
        let midNum = Number(mid);
        for (let w of workerTimes) {
            let x = Math.floor((Math.sqrt(1 + 8 * (midNum / w)) - 1) / 2);
            totalHeight += BigInt(x);
            if (totalHeight >= h) break;
        }

        if (totalHeight >= h) {
            ans = mid;
            high = mid - 1n;
        } else {
            low = mid + 1n;
        }
    }
    return Number(ans);
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer $mountainHeight
     * @param Integer[] $workerTimes
     * @return Integer
     */
    function minNumberOfSeconds($mountainHeight, $workerTimes) {
        $minW = $workerTimes[0];
        foreach ($workerTimes as $w) {
            if ($w < $minW) $minW = $w;
        }
        $low = 0;
        $high = (int)($minW * $mountainHeight * ($mountainHeight + 1) / 2);
        $ans = $high;

        while ($low <= $high) {
            $mid = $low + (int)(($high - $low) / 2);
            $totalHeight = 0;
            foreach ($workerTimes as $w) {
                $totalHeight += (int)((sqrt(1 + 8 * ($mid / $w)) - 1) / 2);
                if ($totalHeight >= $mountainHeight) break;
            }
            if ($totalHeight >= $mountainHeight) {
                $ans = $mid;
                $high = $mid - 1;
            } else {
                $low = $mid + 1;
            }
        }
        return $ans;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
import Foundation

class Solution {
    func minNumberOfSeconds(_ mountainHeight: Int, _ workerTimes: [Int]) -> Int {
        let minW = workerTimes.min() ?? 0
        var low = 0
        var high = minW * mountainHeight * (mountainHeight + 1) / 2
        var ans = high

        while low <= high {
            let mid = low + (high - low) / 2
            var totalHeight = 0
            for w in workerTimes {
                let x = Int((sqrt(1.0 + 8.0 * (Double(mid) / Double(w))) - 1.0) / 2.0)
                totalHeight += x
                if totalHeight >= mountainHeight { break }
            }
            if totalHeight >= mountainHeight {
                ans = mid
                high = mid - 1
            } else {
                low = mid + 1
            }
        }
        return ans
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minNumberOfSeconds(mountainHeight: Int, workerTimes: IntArray): Long {
        var minW = workerTimes[0].toLong()
        for (w in workerTimes) {
            if (w.toLong() < minW) minW = w.toLong()
        }
        val h = mountainHeight.toLong()
        var low = 0L
        var high = minW * h * (h + 1) / 2
        var ans = high

        while (low <= high) {
            val mid = low + (high - low) / 2
            var totalHeight = 0L
            for (w in workerTimes) {
                val x = ((Math.sqrt(1.0 + 8.0 * (mid.toDouble() / w.toDouble())) - 1.0) / 2.0).toLong()
                totalHeight += x
                if (totalHeight >= h) break
            }
            if (totalHeight >= h) {
                ans = mid
                high = mid - 1
            } else {
                low = mid + 1
            }
        }
        return ans
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
  int minNumberOfSeconds(int mountainHeight, List<int> workerTimes) {
    int minW = workerTimes.reduce((a, b) => a < b ? a : b);
    int low = 0;
    int high = (minW * mountainHeight * (mountainHeight + 1) ~/ 2);
    int ans = high;

    while (low <= high) {
      int mid = low + (high - low) ~/ 2;
      int totalHeight = 0;
      for (int w in workerTimes) {
        int x = ((sqrt(1 + 8 * (mid / w)) - 1) / 2).floor();
        totalHeight += x;
        if (totalHeight >= mountainHeight) break;
      }
      if (totalHeight >= mountainHeight) {
        ans = mid;
        high = mid - 1;
      } else {
        low = mid + 1;
      }
    }
    return ans;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import (
    "math"
)

func minNumberOfSeconds(mountainHeight int, workerTimes []int) int64 {
    minW := workerTimes[0]
    for _, w := range workerTimes {
        if w < minW {
            minW = w
        }
    }
    h := int64(mountainHeight)
    var low int64 = 0
    var high int64 = int64(minW) * h * (h + 1) / 2
    ans := high

    for low <= high {
        mid := low + (high-low)/2
        var totalHeight int64 = 0
        for _, w := range workerTimes {
            x := int64((math.Sqrt(1 + 8*(float64(mid)/float64(w))) - 1) / 2)
            totalHeight += x
            if totalHeight >= h {
                break
            }
        }
        if totalHeight >= h {
            ans = mid
            high = mid - 1
        } else {
            low = mid + 1
        }
    }
    return ans
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def min_number_of_seconds(mountain_height, worker_times)
  l = 0
  min_w = worker_times.min
  r = min_w * mountain_height * (mountain_height + 1) / 2
  ans = r
  while l <= r
    mid = (l + r) / 2
    total_height = 0
    worker_times.each do |w|
      x = (Integer.sqrt(1 + 8 * mid / w) - 1) / 2
      total_height += x
      break if total_height >= mountain_height
    end
    if total_height >= mountain_height
      ans = mid
      r = mid - 1
    else
      l = mid + 1
    end
  end
  ans
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def minNumberOfSeconds(mountainHeight: Int, workerTimes: Array[Int]): Long = {
        val minW = workerTimes.min.toLong
        val h = mountainHeight.toLong
        var l: Long = 0
        var r: Long = minW * h * (h + 1) / 2
        var ans: Long = r
        while (l <= r) {
            val mid = l + (r - l) / 2
            var total: Long = 0
            var i = 0
            while (i < workerTimes.length && total < mountainHeight) {
                val w = workerTimes(i)
                val x = ((Math.sqrt(1.0 + 8.0 * mid / w) - 1.0) / 2.0).toLong
                total += x
                i += 1
            }
            if (total >= mountainHeight) {
                ans = mid
                r = mid - 1
            } else {
                l = mid + 1
            }
        }
        ans
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn min_number_of_seconds(mountain_height: i32, worker_times: Vec<i32>) -> i64 {
        let h = mountain_height as i64;
        let min_w = *worker_times.iter().min().unwrap() as i64;
        let mut l: i64 = 0;
        let mut r: i64 = min_w * h * (h + 1) / 2;
        let mut ans = r;
        while l <= r {
            let mid = l + (r - l) / 2;
            let mut total: i64 = 0;
            for &w in &worker_times {
                let w64 = w as i64;
                let k = 8 * mid / w64;
                let x = (((1 + k) as f64).sqrt() as i64 - 1) / 2;
                total += x;
                if total >= h {
                    break;
                }
            }
            if total >= h {
                ans = mid;
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        ans
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (min-number-of-seconds mountainHeight workerTimes)
  (-> exact-integer? (listof exact-integer?) exact-integer?)
  (let* ([min-w (apply min workerTimes)]
         [initial-r (quotient (* min-w mountainHeight (+ mountainHeight 1)) 2)])
    (let loop ([l 0]
               [r initial-r]
               [ans initial-r])
      (if (<= l r)
          (let* ([mid (quotient (+ l r) 2)]
                 [total (for/fold ([sum 0])
                                  ([w workerTimes] #:break (>= sum mountainHeight))
                          (+ sum (quotient (- (integer-sqrt (+ 1 (quotient (* 8 mid) w))) 1) 2)))])
            (if (>= total mountainHeight)
                (loop l (- mid 1) mid)
                (loop (+ mid 1) r ans)))
          ans))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec min_number_of_seconds(MountainHeight :: integer(), WorkerTimes :: [integer()]) -> integer().
min_number_of_seconds(MountainHeight, WorkerTimes) ->
    MinW = lists:min(WorkerTimes),
    R = MinW * MountainHeight * (MountainHeight + 1) div 2,
    binary_search(0, R, R, MountainHeight, WorkerTimes).

binary_search(L, R, Ans, MountainHeight, WorkerTimes) when L =< R ->
    Mid = (L + R) div 2,
    case check_height(Mid, MountainHeight, WorkerTimes) of
        true -> binary_search(L, Mid - 1, Mid, MountainHeight, WorkerTimes);
        false -> binary_search(Mid + 1, R, Ans, MountainHeight, WorkerTimes)
    end;
binary_search(_L, _R, Ans, _MountainHeight, _WorkerTimes) ->
    Ans.

check_height(Mid, MountainHeight, WorkerTimes) ->
    check_height_acc(Mid, MountainHeight, WorkerTimes, 0).

check_height_acc(_Mid, MountainHeight, _, Acc) when Acc >= MountainHeight -> true;
check_height_acc(_Mid, _MountainHeight, [], _Acc) -> false;
check_height_acc(Mid, MountainHeight, [W|Rest], Acc) ->
    K = (8 * Mid) div W,
    X = (trunc(math:sqrt(1 + K)) - 1) div 2,
    check_height_acc(Mid, MountainHeight, Rest, Acc + X).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec min_number_of_seconds(mountain_height :: integer, worker_times :: [integer]) :: integer
  def min_number_of_seconds(mountain_height, worker_times) do
    min_w = Enum.min(worker_times)
    r = div(min_w * mountain_height * (mountain_height + 1), 2)
    binary_search(0, r, r, mountain_height, worker_times)
  end

  defp binary_search(l, r, ans, mountain_height, worker_times) when l <= r do
    mid = div(l + r, 2)
    if check(mid, mountain_height, worker_times) do
      binary_search(l, mid - 1, mid, mountain_height, worker_times)
    else
      binary_search(mid + 1, r, ans, mountain_height, worker_times)
    end
  end
  defp binary_search(_l, _r, ans, _mountain_height, _worker_times), do: ans

  defp check(mid, mountain_height, worker_times) do
    Enum.reduce_while(worker_times, 0, fn w, acc ->
      k = div(8 * mid, w)
      x = div(trunc(:math.sqrt(1 + k)) - 1, 2)
      new_acc = acc + x
      if new_acc >= mountain_height, do: {:halt, new_acc}, else: {:cont, new_acc}
    end) >= mountain_height
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N \log(min(workerTimes) \cdot H^2)), where $N$ is the number of workers and $H$ is the mountain height. The binary search range spans $O(min(W) \cdot H^2)$, and each check takes $O(N)$ time to iterate through the workers and calculate their height reductions using the quadratic formula.
- **Space Complexity:** O(1) as we only use a constant amount of extra space for variables during the binary search, independent of the input size.
