---
layout: post
title: "Jump Game IX"
date: 2026-05-07 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Dynamic Programming"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/jump-game-ix/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    vector<int> maxValue(vector<int>& nums) {\n\
        \        int n = nums.size();\n        if (n == 0) return {};\n\n        vector<int>\
        \ suffMin(n);\n        suffMin[n - 1] = nums[n - 1];\n        for (int i = n\
        \ - 2; i >= 0; --i) {\n            suffMin[i] = min(nums[i], suffMin[i + 1]);\n\
        \        }\n\n        vector<int> ans(n);\n        int start = 0;\n        int\
        \ currentPrefMax = nums[0];\n        for (int i = 0; i < n; ++i) {\n       \
        \     if (nums[i] > currentPrefMax) currentPrefMax = nums[i];\n            if\
        \ (i == n - 1 || currentPrefMax <= suffMin[i + 1]) {\n                int blockMax\
        \ = currentPrefMax;\n                for (int k = start; k <= i; ++k) {\n  \
        \                  ans[k] = blockMax;\n                }\n                start\
        \ = i + 1;\n                if (i + 1 < n) currentPrefMax = nums[i + 1];\n \
        \           }\n        }\n\n        return ans;\n    }\n};"
      java: "class Solution {\n    public int[] maxValue(int[] nums) {\n        int\
        \ n = nums.length;\n        if (n == 0) return new int[0];\n\n        int[]\
        \ suffMin = new int[n];\n        suffMin[n - 1] = nums[n - 1];\n        for\
        \ (int i = n - 2; i >= 0; i--) {\n            suffMin[i] = Math.min(nums[i],\
        \ suffMin[i + 1]);\n        }\n\n        int[] ans = new int[n];\n        int\
        \ start = 0;\n        int currentPrefMax = nums[0];\n        for (int i = 0;\
        \ i < n; i++) {\n            if (nums[i] > currentPrefMax) currentPrefMax =\
        \ nums[i];\n            if (i == n - 1 || currentPrefMax <= suffMin[i + 1])\
        \ {\n                int blockMax = currentPrefMax;\n                for (int\
        \ k = start; k <= i; k++) {\n                    ans[k] = blockMax;\n      \
        \          }\n                start = i + 1;\n                if (i + 1 < n)\
        \ currentPrefMax = nums[i + 1];\n            }\n        }\n\n        return\
        \ ans;\n    }\n}"
      python: "class Solution(object):\n    def maxValue(self, nums):\n        \"\"\"\
        \n        :type nums: List[int]\n        :rtype: List[int]\n        \"\"\"\n\
        \        n = len(nums)\n        if n == 0:\n            return []\n\n      \
        \  suffMin = [0] * n\n        suffMin[n - 1] = nums[n - 1]\n        for i in\
        \ range(n - 2, -1, -1):\n            suffMin[i] = min(nums[i], suffMin[i + 1])\n\
        \n        ans = [0] * n\n        start = 0\n        currentPrefMax = nums[0]\n\
        \        for i in range(n):\n            if nums[i] > currentPrefMax:\n    \
        \            currentPrefMax = nums[i]\n            if i == n - 1 or currentPrefMax\
        \ <= suffMin[i + 1]:\n                blockMax = currentPrefMax\n          \
        \      for k in range(start, i + 1):\n                    ans[k] = blockMax\n\
        \                start = i + 1\n                if i + 1 < n:\n            \
        \        currentPrefMax = nums[i + 1]\n\n        return ans"
      python3: "class Solution:\n    def maxValue(self, nums: List[int]) -> List[int]:\n\
        \        n = len(nums)\n        if n == 0:\n            return []\n\n      \
        \  suffMin = [0] * n\n        suffMin[n - 1] = nums[n - 1]\n        for i in\
        \ range(n - 2, -1, -1):\n            suffMin[i] = min(nums[i], suffMin[i + 1])\n\
        \n        ans = [0] * n\n        start = 0\n        current_pref_max = nums[0]\n\
        \        for i in range(n):\n            if nums[i] > current_pref_max:\n  \
        \              current_pref_max = nums[i]\n            if i == n - 1 or current_pref_max\
        \ <= suffMin[i + 1]:\n                block_max = current_pref_max\n       \
        \         for k in range(start, i + 1):\n                    ans[k] = block_max\n\
        \                start = i + 1\n                if i + 1 < n:\n            \
        \        current_pref_max = nums[i + 1]\n\n        return ans"
      c: "#include <stdlib.h>\n#include <string.h>\n\n/**\n * Note: The returned array\
        \ must be malloced, assume caller calls free().\n */\nint* maxValue(int* nums,\
        \ int numsSize, int* returnSize) {\n    *returnSize = numsSize;\n    if (numsSize\
        \ == 0) return NULL;\n\n    int* suffMin = (int*)malloc(sizeof(int) * numsSize);\n\
        \    int* ans = (int*)malloc(sizeof(int) * numsSize);\n\n    suffMin[numsSize\
        \ - 1] = nums[numsSize - 1];\n    for (int i = numsSize - 2; i >= 0; i--) {\n\
        \        suffMin[i] = (nums[i] < suffMin[i + 1]) ? nums[i] : suffMin[i + 1];\n\
        \    }\n\n    int start = 0;\n    int currentPrefMax = nums[0];\n    for (int\
        \ i = 0; i < numsSize; i++) {\n        if (nums[i] > currentPrefMax) {\n   \
        \         currentPrefMax = nums[i];\n        }\n        if (i == numsSize -\
        \ 1 || currentPrefMax <= suffMin[i + 1]) {\n            int blockMax = currentPrefMax;\n\
        \            for (int k = start; k <= i; k++) {\n                ans[k] = blockMax;\n\
        \            }\n            start = i + 1;\n            if (i + 1 < numsSize)\
        \ {\n                currentPrefMax = nums[i + 1];\n            }\n        }\n\
        \    }\n\n    free(suffMin);\n    return ans;\n}"
      csharp: "public class Solution {\n    public int[] MaxValue(int[] nums) {\n  \
        \      int n = nums.Length;\n        if (n == 0) return new int[0];\n\n    \
        \    int[] prefMax = new int[n];\n        int[] suffMin = new int[n];\n\n  \
        \      prefMax[0] = nums[0];\n        for (int i = 1; i < n; i++) {\n      \
        \      prefMax[i] = Math.Max(prefMax[i - 1], nums[i]);\n        }\n\n      \
        \  suffMin[n - 1] = nums[n - 1];\n        for (int i = n - 2; i >= 0; i--) {\n\
        \            suffMin[i] = Math.Min(suffMin[i + 1], nums[i]);\n        }\n\n\
        \        int[] ans = new int[n];\n        int start = 0;\n        for (int i\
        \ = 0; i < n; i++) {\n            if (i == n - 1 || prefMax[i] <= suffMin[i\
        \ + 1]) {\n                int currMax = nums[start];\n                for (int\
        \ k = start + 1; k <= i; k++) {\n                    if (nums[k] > currMax)\
        \ {\n                        currMax = nums[k];\n                    }\n   \
        \             }\n                for (int k = start; k <= i; k++) {\n      \
        \              ans[k] = currMax;\n                }\n                start =\
        \ i + 1;\n            }\n        }\n\n        return ans;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number[]}\n */\nvar maxValue\
        \ = function(nums) {\n    let n = nums.length;\n    if (n === 0) return [];\n\
        \n    let prefMax = new Array(n);\n    let suffMin = new Array(n);\n\n    prefMax[0]\
        \ = nums[0];\n    for (let i = 1; i < n; i++) {\n        prefMax[i] = Math.max(prefMax[i\
        \ - 1], nums[i]);\n    }\n\n    suffMin[n - 1] = nums[n - 1];\n    for (let\
        \ i = n - 2; i >= 0; i--) {\n        suffMin[i] = Math.min(suffMin[i + 1], nums[i]);\n\
        \    }\n\n    let ans = new Array(n);\n    let start = 0;\n    for (let i =\
        \ 0; i < n; i++) {\n        if (i === n - 1 || prefMax[i] <= suffMin[i + 1])\
        \ {\n            let currMax = nums[start];\n            for (let k = start\
        \ + 1; k <= i; k++) {\n                if (nums[k] > currMax) {\n          \
        \          currMax = nums[k];\n                }\n            }\n          \
        \  for (let k = start; k <= i; k++) {\n                ans[k] = currMax;\n \
        \           }\n            start = i + 1;\n        }\n    }\n\n    return ans;\n\
        };"
      typescript: "function maxValue(nums: number[]): number[] {\n    let n = nums.length;\n\
        \    if (n === 0) return [];\n\n    let prefMax: number[] = new Array(n);\n\
        \    let suffMin: number[] = new Array(n);\n\n    prefMax[0] = nums[0];\n  \
        \  for (let i = 1; i < n; i++) {\n        prefMax[i] = Math.max(prefMax[i -\
        \ 1], nums[i]);\n    }\n\n    suffMin[n - 1] = nums[n - 1];\n    for (let i\
        \ = n - 2; i >= 0; i--) {\n        suffMin[i] = Math.min(suffMin[i + 1], nums[i]);\n\
        \    }\n\n    let ans: number[] = new Array(n);\n    let start = 0;\n    for\
        \ (let i = 0; i < n; i++) {\n        if (i === n - 1 || prefMax[i] <= suffMin[i\
        \ + 1]) {\n            let currMax = nums[start];\n            for (let k =\
        \ start + 1; k <= i; k++) {\n                if (nums[k] > currMax) {\n    \
        \                currMax = nums[k];\n                }\n            }\n    \
        \        for (let k = start; k <= i; k++) {\n                ans[k] = currMax;\n\
        \            }\n            start = i + 1;\n        }\n    }\n\n    return ans;\n\
        };"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer[]\n     */\n    function maxValue($nums) {\n        $n = count($nums);\n\
        \        if ($n === 0) return [];\n\n        $prefMax = array_fill(0, $n, 0);\n\
        \        $suffMin = array_fill(0, $n, 0);\n\n        $prefMax[0] = $nums[0];\n\
        \        for ($i = 1; $i < $n; $i++) {\n            $prefMax[$i] = max($prefMax[$i\
        \ - 1], $nums[$i]);\n        }\n\n        $suffMin[$n - 1] = $nums[$n - 1];\n\
        \        for ($i = $n - 2; $i >= 0; $i--) {\n            $suffMin[$i] = min($suffMin[$i\
        \ + 1], $nums[$i]);\n        }\n\n        $ans = array_fill(0, $n, 0);\n   \
        \     $start = 0;\n        for ($i = 0; $i < $n; $i++) {\n            if ($i\
        \ == $n - 1 || $prefMax[$i] <= $suffMin[$i + 1]) {\n                $currMax\
        \ = $nums[$start];\n                for ($k = $start + 1; $k <= $i; $k++) {\n\
        \                    if ($nums[$k] > $currMax) {\n                        $currMax\
        \ = $nums[$k];\n                    }\n                }\n                for\
        \ ($k = $start; $k <= $i; $k++) {\n                    $ans[$k] = $currMax;\n\
        \                }\n                $start = $i + 1;\n            }\n      \
        \  }\n\n        return $ans;\n    }\n}"
      swift: "class Solution {\n    func maxValue(_ nums: [Int]) -> [Int] {\n      \
        \  let n = nums.count\n        if n == 0 { return [] }\n\n        var prefMax\
        \ = [Int](repeating: 0, count: n)\n        var suffMin = [Int](repeating: 0,\
        \ count: n)\n\n        prefMax[0] = nums[0]\n        for i in 1..<n {\n    \
        \        prefMax[i] = max(prefMax[i - 1], nums[i])\n        }\n\n        suffMin[n\
        \ - 1] = nums[n - 1]\n        if n > 1 {\n            for i in stride(from:\
        \ n - 2, through: 0, by: -1) {\n                suffMin[i] = min(suffMin[i +\
        \ 1], nums[i])\n            }\n        }\n\n        var ans = [Int](repeating:\
        \ 0, count: n)\n        var start = 0\n        for i in 0..<n {\n          \
        \  if i == n - 1 || prefMax[i] <= suffMin[i + 1] {\n                var currMax\
        \ = nums[start]\n                for k in start...i {\n                    if\
        \ nums[k] > currMax {\n                        currMax = nums[k]\n         \
        \           }\n                }\n                for k in start...i {\n   \
        \                 ans[k] = currMax\n                }\n                start\
        \ = i + 1\n            }\n        }\n\n        return ans\n    }\n}"
      kotlin: "class Solution {\n    fun maxValue(nums: IntArray): IntArray {\n    \
        \    val n = nums.size\n        if (n == 0) return IntArray(0)\n\n        val\
        \ prefixMax = IntArray(n)\n        val suffixMin = IntArray(n)\n\n        prefixMax[0]\
        \ = nums[0]\n        for (i in 1 until n) {\n            prefixMax[i] = if (nums[i]\
        \ > prefixMax[i - 1]) nums[i] else prefixMax[i - 1]\n        }\n\n        suffixMin[n\
        \ - 1] = nums[n - 1]\n        for (i in n - 2 downTo 0) {\n            suffixMin[i]\
        \ = if (nums[i] < suffixMin[i + 1]) nums[i] else suffixMin[i + 1]\n        }\n\
        \n        val ans = IntArray(n)\n        var start = 0\n        while (start\
        \ < n) {\n            var finish = start\n            while (finish < n - 1\
        \ && prefixMax[finish] > suffixMin[finish + 1]) {\n                finish++\n\
        \            }\n            val currentMax = prefixMax[finish]\n           \
        \ for (i in start..finish) {\n                ans[i] = currentMax\n        \
        \    }\n            start = finish + 1\n        }\n        return ans\n    }\n\
        }"
      dart: "class Solution {\n  List<int> maxValue(List<int> nums) {\n    int n = nums.length;\n\
        \    if (n == 0) return [];\n\n    List<int> prefixMax = List<int>.filled(n,\
        \ 0);\n    List<int> suffixMin = List<int>.filled(n, 0);\n\n    prefixMax[0]\
        \ = nums[0];\n    for (int i = 1; i < n; i++) {\n      prefixMax[i] = nums[i]\
        \ > prefixMax[i - 1] ? nums[i] : prefixMax[i - 1];\n    }\n\n    suffixMin[n\
        \ - 1] = nums[n - 1];\n    for (int i = n - 2; i >= 0; i--) {\n      suffixMin[i]\
        \ = nums[i] < suffixMin[i + 1] ? nums[i] : suffixMin[i + 1];\n    }\n\n    List<int>\
        \ ans = List<int>.filled(n, 0);\n    int start = 0;\n    while (start < n) {\n\
        \      int finish = start;\n      while (finish < n - 1 && prefixMax[finish]\
        \ > suffixMin[finish + 1]) {\n        finish++;\n      }\n      int currentMax\
        \ = prefixMax[finish];\n      for (int i = start; i <= finish; i++) {\n    \
        \    ans[i] = currentMax;\n      }\n      start = finish + 1;\n    }\n    return\
        \ ans;\n  }\n}"
      go: "func maxValue(nums []int) []int {\n    n := len(nums)\n    if n == 0 {\n\
        \        return []int{}\n    }\n\n    prefixMax := make([]int, n)\n    suffixMin\
        \ := make([]int, n)\n\n    prefixMax[0] = nums[0]\n    for i := 1; i < n; i++\
        \ {\n        prefixMax[i] = prefixMax[i-1]\n        if nums[i] > prefixMax[i]\
        \ {\n            prefixMax[i] = nums[i]\n        }\n    }\n\n    suffixMin[n-1]\
        \ = nums[n-1]\n    for i := n - 2; i >= 0; i-- {\n        suffixMin[i] = suffixMin[i+1]\n\
        \        if nums[i] < suffixMin[i] {\n            suffixMin[i] = nums[i]\n \
        \       }\n    }\n\n    ans := make([]int, n)\n    start := 0\n    for start\
        \ < n {\n        finish := start\n        for finish < n-1 && prefixMax[finish]\
        \ > suffixMin[finish+1] {\n            finish++\n        }\n        currentMax\
        \ := prefixMax[finish]\n        for i := start; i <= finish; i++ {\n       \
        \     ans[i] = currentMax\n        }\n        start = finish + 1\n    }\n  \
        \  return ans\n}"
      ruby: "# @param {Integer[]} nums\n# @return {Integer[]}\ndef max_value(nums)\n\
        \  n = nums.length\n  return [] if n == 0\n\n  prefix_max = Array.new(n)\n \
        \ suffix_min = Array.new(n)\n\n  prefix_max[0] = nums[0]\n  (1...n).each do\
        \ |i|\n    prefix_max[i] = prefix_max[i - 1] > nums[i] ? prefix_max[i - 1] :\
        \ nums[i]\n  end\n\n  suffix_min[n - 1] = nums[n - 1]\n  (n - 2).downto(0) do\
        \ |i|\n    suffix_min[i] = suffix_min[i + 1] < nums[i] ? suffix_min[i + 1] :\
        \ nums[i]\n  end\n\n  ans = Array.new(n)\n  start = 0\n  while start < n\n \
        \   finish = start\n    while finish < n - 1 && prefix_max[finish] > suffix_min[finish\
        \ + 1]\n      finish += 1\n    end\n\n    current_max = prefix_max[finish]\n\
        \    (start..finish).each do |i|\n      ans[i] = current_max\n    end\n    start\
        \ = finish + 1\n  end\n  ans\nend"
      scala: "object Solution {\n    def maxValue(nums: Array[Int]): Array[Int] = {\n\
        \        val n = nums.length\n        if (n == 0) return new Array[Int](0)\n\
        \n        val prefixMax = new Array[Int](n)\n        val suffixMin = new Array[Int](n)\n\
        \n        prefixMax(0) = nums(0)\n        for (i <- 1 until n) {\n         \
        \   prefixMax(i) = if (prefixMax(i - 1) > nums(i)) prefixMax(i - 1) else nums(i)\n\
        \        }\n\n        suffixMin(n - 1) = nums(n - 1)\n        for (i <- (n -\
        \ 2) to 0 by -1) {\n            suffixMin(i) = if (suffixMin(i + 1) < nums(i))\
        \ suffixMin(i + 1) else nums(i)\n        }\n\n        val ans = new Array[Int](n)\n\
        \        var start = 0\n        while (start < n) {\n            var finish\
        \ = start\n            while (finish < n - 1 && prefixMax(finish) > suffixMin(finish\
        \ + 1)) {\n                finish += 1\n            }\n            val currentMax\
        \ = prefixMax(finish)\n            for (i <- start to finish) {\n          \
        \      ans(i) = currentMax\n            }\n            start = finish + 1\n\
        \        }\n        ans\n    }\n}"
      rust: "impl Solution {\n    pub fn max_value(nums: Vec<i32>) -> Vec<i32> {\n \
        \       let n = nums.len();\n        if n == 0 {\n            return vec![];\n\
        \        }\n        let mut pre_max = vec![0; n];\n        let mut suf_min =\
        \ vec![0; n];\n\n        pre_max[0] = nums[0];\n        for i in 1..n {\n  \
        \          pre_max[i] = pre_max[i - 1].max(nums[i]);\n        }\n\n        suf_min[n\
        \ - 1] = nums[n - 1];\n        for i in (0..n - 1).rev() {\n            suf_min[i]\
        \ = suf_min[i + 1].min(nums[i]);\n        }\n\n        let mut ans = vec![0;\
        \ n];\n        let mut start = 0;\n        while start < n {\n            let\
        \ mut end = start;\n            while end < n - 1 && pre_max[end] > suf_min[end\
        \ + 1] {\n                end += 1;\n            }\n            let mut current_max\
        \ = nums[start];\n            for i in start..=end {\n                if nums[i]\
        \ > current_max {\n                    current_max = nums[i];\n            \
        \    }\n            }\n            for i in start..=end {\n                ans[i]\
        \ = current_max;\n            }\n            start = end + 1;\n        }\n \
        \       ans\n    }\n}"
      racket: "(define/contract (max-value nums)\n  (-> (listof exact-integer?) (listof\
        \ exact-integer?))\n  (let* ([n (length nums)]\n         [nums-vec (list->vector\
        \ nums)]\n         [pre-max (make-vector n)]\n         [suf-min (make-vector\
        \ n)])\n    (if (= n 0)\n        '()\n        (begin\n          (vector-set!\
        \ pre-max 0 (vector-ref nums-vec 0))\n          (for ([i (in-range 1 n)])\n\
        \            (vector-set! pre-max i (max (vector-ref pre-max (- i 1)) (vector-ref\
        \ nums-vec i))))\n          (vector-set! suf-min (- n 1) (vector-ref nums-vec\
        \ (- n 1)))\n          (for ([i (in-range (- n 2) -1 -1)])\n            (vector-set!\
        \ suf-min i (min (vector-ref suf-min (+ i 1)) (vector-ref nums-vec i))))\n\n\
        \          (let ([ans (make-vector n)])\n            (let loop ([start 0])\n\
        \              (when (< start n)\n                (let inner-loop ([end start])\n\
        \                  (if (and (< end (- n 1))\n                           (> (vector-ref\
        \ pre-max end) (vector-ref suf-min (+ end 1))))\n                      (inner-loop\
        \ (+ end 1))\n                      (let ([current-max (let find-max ([i start]\
        \ [m (vector-ref nums-vec start)])\n                                       \
        \    (if (> i end)\n                                               m\n     \
        \                                          (find-max (+ i 1) (max m (vector-ref\
        \ nums-vec i)))))])\n                        (for ([i (in-range start (+ end\
        \ 1))])\n                          (vector-set! ans i current-max))\n      \
        \                  (loop (+ end 1)))))))\n            (vector->list ans))))))"
      erlang: "-spec max_value(Nums :: [integer()]) -> [integer()].\nmax_value(Nums)\
        \ ->\n    N = length(Nums),\n    if N =:= 0 -> [];\n       true ->\n       \
        \    NumsVec = list_to_tuple(Nums),\n           PreMax = list_to_tuple(calc_pre_max(Nums)),\n\
        \           SufMin = list_to_tuple(calc_suf_min(lists:reverse(Nums))),\n   \
        \        process_segments(1, N, NumsVec, PreMax, SufMin, [])\n    end.\n\ncalc_pre_max([H\
        \ | T]) -> calc_pre_max(T, H, [H]).\ncalc_pre_max([], _, Acc) -> lists:reverse(Acc);\n\
        calc_pre_max([H | T], Max, Acc) ->\n    NewMax = erlang:max(H, Max),\n    calc_pre_max(T,\
        \ NewMax, [NewMax | Acc]).\n\ncalc_suf_min([H | T]) -> calc_suf_min(T, H, [H]).\n\
        calc_suf_min([], _, Acc) -> Acc;\ncalc_suf_min([H | T], Min, Acc) ->\n    NewMin\
        \ = erlang:min(H, Min),\n    calc_suf_min(T, NewMin, [NewMin | Acc]).\n\nprocess_segments(Start,\
        \ N, NumsVec, PreMax, SufMin, AnsAcc) when Start > N ->\n    lists:flatten(lists:reverse(AnsAcc));\n\
        process_segments(Start, N, NumsVec, PreMax, SufMin, AnsAcc) ->\n    End = find_end(Start,\
        \ N, PreMax, SufMin),\n    CurrentMax = find_max(Start, End, NumsVec, 0),\n\
        \    Segment = lists:duplicate(End - Start + 1, CurrentMax),\n    process_segments(End\
        \ + 1, N, NumsVec, PreMax, SufMin, [Segment | AnsAcc]).\n\nfind_end(End, N,\
        \ PreMax, SufMin) when End < N ->\n    case element(End, PreMax) > element(End\
        \ + 1, SufMin) of\n        true -> find_end(End + 1, N, PreMax, SufMin);\n \
        \       false -> End\n    end;\nfind_end(End, _, _, _) -> End.\n\nfind_max(I,\
        \ End, NumsVec, Max) when I =< End ->\n    find_max(I + 1, End, NumsVec, erlang:max(Max,\
        \ element(I, NumsVec)));\nfind_max(_, _, _, Max) -> Max."
      elixir: "defmodule Solution do\n  @spec max_value(nums :: [integer]) :: [integer]\n\
        \  def max_value(nums) do\n    n = length(nums)\n    if n == 0 do\n      []\n\
        \    else\n      pre_max = Enum.scan(nums, &max/2) |> List.to_tuple()\n    \
        \  suf_min = Enum.reverse(nums) |> Enum.scan(&min/2) |> Enum.reverse() |> List.to_tuple()\n\
        \      nums_tuple = List.to_tuple(nums)\n\n      process_segments(0, n, nums_tuple,\
        \ pre_max, suf_min, [])\n    end\n  end\n\n  defp process_segments(start, n,\
        \ nums_tuple, pre_max, suf_min, acc) when start < n do\n    end_idx = find_end(start,\
        \ n, pre_max, suf_min)\n\n    current_max = Enum.reduce(start..end_idx, 0, fn\
        \ i, m ->\n      max(m, elem(nums_tuple, i))\n    end)\n\n    segment = List.duplicate(current_max,\
        \ end_idx - start + 1)\n    process_segments(end_idx + 1, n, nums_tuple, pre_max,\
        \ suf_min, [segment | acc])\n  end\n\n  defp process_segments(_start, _n, _nums_tuple,\
        \ _pre_max, _suf_min, acc) do\n    acc |> Enum.reverse() |> List.flatten()\n\
        \  end\n\n  defp find_end(idx, n, pre_max, suf_min) when idx < n - 1 do\n  \
        \  if elem(pre_max, idx) > elem(suf_min, idx + 1) do\n      find_end(idx + 1,\
        \ n, pre_max, suf_min)\n    else\n      idx\n    end\n  end\n\n  defp find_end(idx,\
        \ _n, _pre_max, _suf_min), do: idx\nend"
    approach: 'The problem asks for the maximum reachable value from each index $i$
      given two jump rules: jumping forward to a smaller value or jumping backward to
      a larger value. These rules describe a directed graph where an edge exists from
      $i$ to $j$ if $(i < j \text{ and } nums[j] < nums[i])$ or $(j < i \text{ and }
      nums[j] > nums[i])$. Crucially, these two rules are symmetric: if there is a jump
      from $i$ to $j$, there is also a jump from $j$ to $i$. Thus, the graph is effectively
      undirected, and an edge exists between $i$ and $j$ ($i < j$) if and only if $nums[i]
      > nums[j]$, which is the definition of an inversion. The maximum reachable value
      for any index $i$ is therefore the maximum value in its connected component within
      this ''inversion graph''.


      Connected components in an inversion graph are identified by ''cut'' points. A
      cut occurs after index $k$ if all elements in the prefix $nums[0 \dots k]$ are
      less than or equal to all elements in the suffix $nums[k+1 \dots n-1]$. This condition
      is equivalent to $\max(nums[0 \dots k]) \le \min(nums[k+1 \dots n-1])$. We can
      identify these blocks by precalculating prefix maximums and suffix minimums. Within
      each block, every node can reach every other node, so the answer for every index
      in a block is simply the maximum value within that block. This maximum value is
      efficiently tracked using the prefix maximum array.'
    time_complexity: O(n) where n is the length of the input array. We perform one linear
      pass to calculate suffix minimums, one pass for prefix maximums (which can be
      done on the fly), and one final pass to identify component boundaries and fill
      the result array. Each index is visited a constant number of times.
    space_complexity: O(n) to store the suffix minimum array and the result array. In
      C, we allocate $O(n)$ space for suffix minimums and the result, while other variables
      use $O(1)$ additional space.
    elapsed_time: 314.0618965625763
    model: gemini-3-flash-preview
    generated_at: '2026-05-07 02:13:42 '
---

## Problem #3660: Jump Game IX

**Difficulty:** Medium

**Topics:** Array, Dynamic Programming

## Problem Description

<p>You are given an integer array <code>nums</code>.</p>

<p>From any index <code>i</code>, you can jump to another index <code>j</code> under the following rules:</p>

<ul>
	<li>Jump to index <code>j</code> where <code>j &gt; i</code> is allowed only if <code>nums[j] &lt; nums[i]</code>.</li>
	<li>Jump to index <code>j</code> where <code>j &lt; i</code> is allowed only if <code>nums[j] &gt; nums[i]</code>.</li>
</ul>

<p>For each index <code>i</code>, find the <strong>maximum</strong> <strong>value</strong> in <code>nums</code> that can be reached by following <strong>any</strong> sequence of valid jumps starting at <code>i</code>.</p>

<p>Return an array <code>ans</code> where <code>ans[i]</code> is the <strong>maximum</strong> <strong>value</strong> reachable starting from index <code>i</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,1,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">[2,2,3]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>For <code>i = 0</code>: No jump increases the value.</li>
	<li>For <code>i = 1</code>: Jump to <code>j = 0</code> as <code>nums[j] = 2</code> is greater than <code>nums[i]</code>.</li>
	<li>For <code>i = 2</code>: Since <code>nums[2] = 3</code> is the maximum value in <code>nums</code>, no jump increases the value.</li>
</ul>

<p>Thus, <code>ans = [2, 2, 3]</code>.</p>

<ul>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,3,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">[3,3,3]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>For <code>i = 0</code>: Jump forward to <code>j = 2</code> as <code>nums[j] = 1</code> is less than <code>nums[i] = 2</code>, then from <code>i = 2</code> jump to <code>j = 1</code> as <code>nums[j] = 3</code> is greater than <code>nums[2]</code>.</li>
	<li>For <code>i = 1</code>: Since <code>nums[1] = 3</code> is the maximum value in <code>nums</code>, no jump increases the value.</li>
	<li>For <code>i = 2</code>: Jump to <code>j = 1</code> as <code>nums[j] = 3</code> is greater than <code>nums[2] = 1</code>.</li>
</ul>

<p>Thus, <code>ans = [3, 3, 3]</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup>​​​​​​​</code></li>
</ul>


## Hints

1. Think of the array as a directed graph where edges represent valid jumps.

2. From index `i`, forward jumps go only to smaller values; backward jumps go only to larger values.

3. The maximum reachable value from `i` is the maximum value in the connected component reachable under these jump rules.

4. You can find connected ranges by looking at prefix maximums and suffix minimums, a cut happens where all values to the left are <= all values to the right.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks for the maximum reachable value from each index $i$ given two jump rules: jumping forward to a smaller value or jumping backward to a larger value. These rules describe a directed graph where an edge exists from $i$ to $j$ if $(i < j \text{ and } nums[j] < nums[i])$ or $(j < i \text{ and } nums[j] > nums[i])$. Crucially, these two rules are symmetric: if there is a jump from $i$ to $j$, there is also a jump from $j$ to $i$. Thus, the graph is effectively undirected, and an edge exists between $i$ and $j$ ($i < j$) if and only if $nums[i] > nums[j]$, which is the definition of an inversion. The maximum reachable value for any index $i$ is therefore the maximum value in its connected component within this 'inversion graph'.

Connected components in an inversion graph are identified by 'cut' points. A cut occurs after index $k$ if all elements in the prefix $nums[0 \dots k]$ are less than or equal to all elements in the suffix $nums[k+1 \dots n-1]$. This condition is equivalent to $\max(nums[0 \dots k]) \le \min(nums[k+1 \dots n-1])$. We can identify these blocks by precalculating prefix maximums and suffix minimums. Within each block, every node can reach every other node, so the answer for every index in a block is simply the maximum value within that block. This maximum value is efficiently tracked using the prefix maximum array.

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
    vector<int> maxValue(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) return {};

        vector<int> suffMin(n);
        suffMin[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= 0; --i) {
            suffMin[i] = min(nums[i], suffMin[i + 1]);
        }

        vector<int> ans(n);
        int start = 0;
        int currentPrefMax = nums[0];
        for (int i = 0; i < n; ++i) {
            if (nums[i] > currentPrefMax) currentPrefMax = nums[i];
            if (i == n - 1 || currentPrefMax <= suffMin[i + 1]) {
                int blockMax = currentPrefMax;
                for (int k = start; k <= i; ++k) {
                    ans[k] = blockMax;
                }
                start = i + 1;
                if (i + 1 < n) currentPrefMax = nums[i + 1];
            }
        }

        return ans;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int[] maxValue(int[] nums) {
        int n = nums.length;
        if (n == 0) return new int[0];

        int[] suffMin = new int[n];
        suffMin[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            suffMin[i] = Math.min(nums[i], suffMin[i + 1]);
        }

        int[] ans = new int[n];
        int start = 0;
        int currentPrefMax = nums[0];
        for (int i = 0; i < n; i++) {
            if (nums[i] > currentPrefMax) currentPrefMax = nums[i];
            if (i == n - 1 || currentPrefMax <= suffMin[i + 1]) {
                int blockMax = currentPrefMax;
                for (int k = start; k <= i; k++) {
                    ans[k] = blockMax;
                }
                start = i + 1;
                if (i + 1 < n) currentPrefMax = nums[i + 1];
            }
        }

        return ans;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def maxValue(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0:
            return []

        suffMin = [0] * n
        suffMin[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffMin[i] = min(nums[i], suffMin[i + 1])

        ans = [0] * n
        start = 0
        currentPrefMax = nums[0]
        for i in range(n):
            if nums[i] > currentPrefMax:
                currentPrefMax = nums[i]
            if i == n - 1 or currentPrefMax <= suffMin[i + 1]:
                blockMax = currentPrefMax
                for k in range(start, i + 1):
                    ans[k] = blockMax
                start = i + 1
                if i + 1 < n:
                    currentPrefMax = nums[i + 1]

        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0:
            return []

        suffMin = [0] * n
        suffMin[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffMin[i] = min(nums[i], suffMin[i + 1])

        ans = [0] * n
        start = 0
        current_pref_max = nums[0]
        for i in range(n):
            if nums[i] > current_pref_max:
                current_pref_max = nums[i]
            if i == n - 1 or current_pref_max <= suffMin[i + 1]:
                block_max = current_pref_max
                for k in range(start, i + 1):
                    ans[k] = block_max
                start = i + 1
                if i + 1 < n:
                    current_pref_max = nums[i + 1]

        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <string.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* maxValue(int* nums, int numsSize, int* returnSize) {
    *returnSize = numsSize;
    if (numsSize == 0) return NULL;

    int* suffMin = (int*)malloc(sizeof(int) * numsSize);
    int* ans = (int*)malloc(sizeof(int) * numsSize);

    suffMin[numsSize - 1] = nums[numsSize - 1];
    for (int i = numsSize - 2; i >= 0; i--) {
        suffMin[i] = (nums[i] < suffMin[i + 1]) ? nums[i] : suffMin[i + 1];
    }

    int start = 0;
    int currentPrefMax = nums[0];
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] > currentPrefMax) {
            currentPrefMax = nums[i];
        }
        if (i == numsSize - 1 || currentPrefMax <= suffMin[i + 1]) {
            int blockMax = currentPrefMax;
            for (int k = start; k <= i; k++) {
                ans[k] = blockMax;
            }
            start = i + 1;
            if (i + 1 < numsSize) {
                currentPrefMax = nums[i + 1];
            }
        }
    }

    free(suffMin);
    return ans;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int[] MaxValue(int[] nums) {
        int n = nums.Length;
        if (n == 0) return new int[0];

        int[] prefMax = new int[n];
        int[] suffMin = new int[n];

        prefMax[0] = nums[0];
        for (int i = 1; i < n; i++) {
            prefMax[i] = Math.Max(prefMax[i - 1], nums[i]);
        }

        suffMin[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            suffMin[i] = Math.Min(suffMin[i + 1], nums[i]);
        }

        int[] ans = new int[n];
        int start = 0;
        for (int i = 0; i < n; i++) {
            if (i == n - 1 || prefMax[i] <= suffMin[i + 1]) {
                int currMax = nums[start];
                for (int k = start + 1; k <= i; k++) {
                    if (nums[k] > currMax) {
                        currMax = nums[k];
                    }
                }
                for (int k = start; k <= i; k++) {
                    ans[k] = currMax;
                }
                start = i + 1;
            }
        }

        return ans;
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
 * @return {number[]}
 */
var maxValue = function(nums) {
    let n = nums.length;
    if (n === 0) return [];

    let prefMax = new Array(n);
    let suffMin = new Array(n);

    prefMax[0] = nums[0];
    for (let i = 1; i < n; i++) {
        prefMax[i] = Math.max(prefMax[i - 1], nums[i]);
    }

    suffMin[n - 1] = nums[n - 1];
    for (let i = n - 2; i >= 0; i--) {
        suffMin[i] = Math.min(suffMin[i + 1], nums[i]);
    }

    let ans = new Array(n);
    let start = 0;
    for (let i = 0; i < n; i++) {
        if (i === n - 1 || prefMax[i] <= suffMin[i + 1]) {
            let currMax = nums[start];
            for (let k = start + 1; k <= i; k++) {
                if (nums[k] > currMax) {
                    currMax = nums[k];
                }
            }
            for (let k = start; k <= i; k++) {
                ans[k] = currMax;
            }
            start = i + 1;
        }
    }

    return ans;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maxValue(nums: number[]): number[] {
    let n = nums.length;
    if (n === 0) return [];

    let prefMax: number[] = new Array(n);
    let suffMin: number[] = new Array(n);

    prefMax[0] = nums[0];
    for (let i = 1; i < n; i++) {
        prefMax[i] = Math.max(prefMax[i - 1], nums[i]);
    }

    suffMin[n - 1] = nums[n - 1];
    for (let i = n - 2; i >= 0; i--) {
        suffMin[i] = Math.min(suffMin[i + 1], nums[i]);
    }

    let ans: number[] = new Array(n);
    let start = 0;
    for (let i = 0; i < n; i++) {
        if (i === n - 1 || prefMax[i] <= suffMin[i + 1]) {
            let currMax = nums[start];
            for (let k = start + 1; k <= i; k++) {
                if (nums[k] > currMax) {
                    currMax = nums[k];
                }
            }
            for (let k = start; k <= i; k++) {
                ans[k] = currMax;
            }
            start = i + 1;
        }
    }

    return ans;
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
     * @return Integer[]
     */
    function maxValue($nums) {
        $n = count($nums);
        if ($n === 0) return [];

        $prefMax = array_fill(0, $n, 0);
        $suffMin = array_fill(0, $n, 0);

        $prefMax[0] = $nums[0];
        for ($i = 1; $i < $n; $i++) {
            $prefMax[$i] = max($prefMax[$i - 1], $nums[$i]);
        }

        $suffMin[$n - 1] = $nums[$n - 1];
        for ($i = $n - 2; $i >= 0; $i--) {
            $suffMin[$i] = min($suffMin[$i + 1], $nums[$i]);
        }

        $ans = array_fill(0, $n, 0);
        $start = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($i == $n - 1 || $prefMax[$i] <= $suffMin[$i + 1]) {
                $currMax = $nums[$start];
                for ($k = $start + 1; $k <= $i; $k++) {
                    if ($nums[$k] > $currMax) {
                        $currMax = $nums[$k];
                    }
                }
                for ($k = $start; $k <= $i; $k++) {
                    $ans[$k] = $currMax;
                }
                $start = $i + 1;
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
class Solution {
    func maxValue(_ nums: [Int]) -> [Int] {
        let n = nums.count
        if n == 0 { return [] }

        var prefMax = [Int](repeating: 0, count: n)
        var suffMin = [Int](repeating: 0, count: n)

        prefMax[0] = nums[0]
        for i in 1..<n {
            prefMax[i] = max(prefMax[i - 1], nums[i])
        }

        suffMin[n - 1] = nums[n - 1]
        if n > 1 {
            for i in stride(from: n - 2, through: 0, by: -1) {
                suffMin[i] = min(suffMin[i + 1], nums[i])
            }
        }

        var ans = [Int](repeating: 0, count: n)
        var start = 0
        for i in 0..<n {
            if i == n - 1 || prefMax[i] <= suffMin[i + 1] {
                var currMax = nums[start]
                for k in start...i {
                    if nums[k] > currMax {
                        currMax = nums[k]
                    }
                }
                for k in start...i {
                    ans[k] = currMax
                }
                start = i + 1
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
    fun maxValue(nums: IntArray): IntArray {
        val n = nums.size
        if (n == 0) return IntArray(0)

        val prefixMax = IntArray(n)
        val suffixMin = IntArray(n)

        prefixMax[0] = nums[0]
        for (i in 1 until n) {
            prefixMax[i] = if (nums[i] > prefixMax[i - 1]) nums[i] else prefixMax[i - 1]
        }

        suffixMin[n - 1] = nums[n - 1]
        for (i in n - 2 downTo 0) {
            suffixMin[i] = if (nums[i] < suffixMin[i + 1]) nums[i] else suffixMin[i + 1]
        }

        val ans = IntArray(n)
        var start = 0
        while (start < n) {
            var finish = start
            while (finish < n - 1 && prefixMax[finish] > suffixMin[finish + 1]) {
                finish++
            }
            val currentMax = prefixMax[finish]
            for (i in start..finish) {
                ans[i] = currentMax
            }
            start = finish + 1
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
class Solution {
  List<int> maxValue(List<int> nums) {
    int n = nums.length;
    if (n == 0) return [];

    List<int> prefixMax = List<int>.filled(n, 0);
    List<int> suffixMin = List<int>.filled(n, 0);

    prefixMax[0] = nums[0];
    for (int i = 1; i < n; i++) {
      prefixMax[i] = nums[i] > prefixMax[i - 1] ? nums[i] : prefixMax[i - 1];
    }

    suffixMin[n - 1] = nums[n - 1];
    for (int i = n - 2; i >= 0; i--) {
      suffixMin[i] = nums[i] < suffixMin[i + 1] ? nums[i] : suffixMin[i + 1];
    }

    List<int> ans = List<int>.filled(n, 0);
    int start = 0;
    while (start < n) {
      int finish = start;
      while (finish < n - 1 && prefixMax[finish] > suffixMin[finish + 1]) {
        finish++;
      }
      int currentMax = prefixMax[finish];
      for (int i = start; i <= finish; i++) {
        ans[i] = currentMax;
      }
      start = finish + 1;
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
func maxValue(nums []int) []int {
    n := len(nums)
    if n == 0 {
        return []int{}
    }

    prefixMax := make([]int, n)
    suffixMin := make([]int, n)

    prefixMax[0] = nums[0]
    for i := 1; i < n; i++ {
        prefixMax[i] = prefixMax[i-1]
        if nums[i] > prefixMax[i] {
            prefixMax[i] = nums[i]
        }
    }

    suffixMin[n-1] = nums[n-1]
    for i := n - 2; i >= 0; i-- {
        suffixMin[i] = suffixMin[i+1]
        if nums[i] < suffixMin[i] {
            suffixMin[i] = nums[i]
        }
    }

    ans := make([]int, n)
    start := 0
    for start < n {
        finish := start
        for finish < n-1 && prefixMax[finish] > suffixMin[finish+1] {
            finish++
        }
        currentMax := prefixMax[finish]
        for i := start; i <= finish; i++ {
            ans[i] = currentMax
        }
        start = finish + 1
    }
    return ans
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @return {Integer[]}
def max_value(nums)
  n = nums.length
  return [] if n == 0

  prefix_max = Array.new(n)
  suffix_min = Array.new(n)

  prefix_max[0] = nums[0]
  (1...n).each do |i|
    prefix_max[i] = prefix_max[i - 1] > nums[i] ? prefix_max[i - 1] : nums[i]
  end

  suffix_min[n - 1] = nums[n - 1]
  (n - 2).downto(0) do |i|
    suffix_min[i] = suffix_min[i + 1] < nums[i] ? suffix_min[i + 1] : nums[i]
  end

  ans = Array.new(n)
  start = 0
  while start < n
    finish = start
    while finish < n - 1 && prefix_max[finish] > suffix_min[finish + 1]
      finish += 1
    end

    current_max = prefix_max[finish]
    (start..finish).each do |i|
      ans[i] = current_max
    end
    start = finish + 1
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
    def maxValue(nums: Array[Int]): Array[Int] = {
        val n = nums.length
        if (n == 0) return new Array[Int](0)

        val prefixMax = new Array[Int](n)
        val suffixMin = new Array[Int](n)

        prefixMax(0) = nums(0)
        for (i <- 1 until n) {
            prefixMax(i) = if (prefixMax(i - 1) > nums(i)) prefixMax(i - 1) else nums(i)
        }

        suffixMin(n - 1) = nums(n - 1)
        for (i <- (n - 2) to 0 by -1) {
            suffixMin(i) = if (suffixMin(i + 1) < nums(i)) suffixMin(i + 1) else nums(i)
        }

        val ans = new Array[Int](n)
        var start = 0
        while (start < n) {
            var finish = start
            while (finish < n - 1 && prefixMax(finish) > suffixMin(finish + 1)) {
                finish += 1
            }
            val currentMax = prefixMax(finish)
            for (i <- start to finish) {
                ans(i) = currentMax
            }
            start = finish + 1
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
    pub fn max_value(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        if n == 0 {
            return vec![];
        }
        let mut pre_max = vec![0; n];
        let mut suf_min = vec![0; n];

        pre_max[0] = nums[0];
        for i in 1..n {
            pre_max[i] = pre_max[i - 1].max(nums[i]);
        }

        suf_min[n - 1] = nums[n - 1];
        for i in (0..n - 1).rev() {
            suf_min[i] = suf_min[i + 1].min(nums[i]);
        }

        let mut ans = vec![0; n];
        let mut start = 0;
        while start < n {
            let mut end = start;
            while end < n - 1 && pre_max[end] > suf_min[end + 1] {
                end += 1;
            }
            let mut current_max = nums[start];
            for i in start..=end {
                if nums[i] > current_max {
                    current_max = nums[i];
                }
            }
            for i in start..=end {
                ans[i] = current_max;
            }
            start = end + 1;
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
(define/contract (max-value nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  (let* ([n (length nums)]
         [nums-vec (list->vector nums)]
         [pre-max (make-vector n)]
         [suf-min (make-vector n)])
    (if (= n 0)
        '()
        (begin
          (vector-set! pre-max 0 (vector-ref nums-vec 0))
          (for ([i (in-range 1 n)])
            (vector-set! pre-max i (max (vector-ref pre-max (- i 1)) (vector-ref nums-vec i))))
          (vector-set! suf-min (- n 1) (vector-ref nums-vec (- n 1)))
          (for ([i (in-range (- n 2) -1 -1)])
            (vector-set! suf-min i (min (vector-ref suf-min (+ i 1)) (vector-ref nums-vec i))))

          (let ([ans (make-vector n)])
            (let loop ([start 0])
              (when (< start n)
                (let inner-loop ([end start])
                  (if (and (< end (- n 1))
                           (> (vector-ref pre-max end) (vector-ref suf-min (+ end 1))))
                      (inner-loop (+ end 1))
                      (let ([current-max (let find-max ([i start] [m (vector-ref nums-vec start)])
                                           (if (> i end)
                                               m
                                               (find-max (+ i 1) (max m (vector-ref nums-vec i)))))])
                        (for ([i (in-range start (+ end 1))])
                          (vector-set! ans i current-max))
                        (loop (+ end 1)))))))
            (vector->list ans))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec max_value(Nums :: [integer()]) -> [integer()].
max_value(Nums) ->
    N = length(Nums),
    if N =:= 0 -> [];
       true ->
           NumsVec = list_to_tuple(Nums),
           PreMax = list_to_tuple(calc_pre_max(Nums)),
           SufMin = list_to_tuple(calc_suf_min(lists:reverse(Nums))),
           process_segments(1, N, NumsVec, PreMax, SufMin, [])
    end.

calc_pre_max([H | T]) -> calc_pre_max(T, H, [H]).
calc_pre_max([], _, Acc) -> lists:reverse(Acc);
calc_pre_max([H | T], Max, Acc) ->
    NewMax = erlang:max(H, Max),
    calc_pre_max(T, NewMax, [NewMax | Acc]).

calc_suf_min([H | T]) -> calc_suf_min(T, H, [H]).
calc_suf_min([], _, Acc) -> Acc;
calc_suf_min([H | T], Min, Acc) ->
    NewMin = erlang:min(H, Min),
    calc_suf_min(T, NewMin, [NewMin | Acc]).

process_segments(Start, N, NumsVec, PreMax, SufMin, AnsAcc) when Start > N ->
    lists:flatten(lists:reverse(AnsAcc));
process_segments(Start, N, NumsVec, PreMax, SufMin, AnsAcc) ->
    End = find_end(Start, N, PreMax, SufMin),
    CurrentMax = find_max(Start, End, NumsVec, 0),
    Segment = lists:duplicate(End - Start + 1, CurrentMax),
    process_segments(End + 1, N, NumsVec, PreMax, SufMin, [Segment | AnsAcc]).

find_end(End, N, PreMax, SufMin) when End < N ->
    case element(End, PreMax) > element(End + 1, SufMin) of
        true -> find_end(End + 1, N, PreMax, SufMin);
        false -> End
    end;
find_end(End, _, _, _) -> End.

find_max(I, End, NumsVec, Max) when I =< End ->
    find_max(I + 1, End, NumsVec, erlang:max(Max, element(I, NumsVec)));
find_max(_, _, _, Max) -> Max.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec max_value(nums :: [integer]) :: [integer]
  def max_value(nums) do
    n = length(nums)
    if n == 0 do
      []
    else
      pre_max = Enum.scan(nums, &max/2) |> List.to_tuple()
      suf_min = Enum.reverse(nums) |> Enum.scan(&min/2) |> Enum.reverse() |> List.to_tuple()
      nums_tuple = List.to_tuple(nums)

      process_segments(0, n, nums_tuple, pre_max, suf_min, [])
    end
  end

  defp process_segments(start, n, nums_tuple, pre_max, suf_min, acc) when start < n do
    end_idx = find_end(start, n, pre_max, suf_min)

    current_max = Enum.reduce(start..end_idx, 0, fn i, m ->
      max(m, elem(nums_tuple, i))
    end)

    segment = List.duplicate(current_max, end_idx - start + 1)
    process_segments(end_idx + 1, n, nums_tuple, pre_max, suf_min, [segment | acc])
  end

  defp process_segments(_start, _n, _nums_tuple, _pre_max, _suf_min, acc) do
    acc |> Enum.reverse() |> List.flatten()
  end

  defp find_end(idx, n, pre_max, suf_min) when idx < n - 1 do
    if elem(pre_max, idx) > elem(suf_min, idx + 1) do
      find_end(idx + 1, n, pre_max, suf_min)
    else
      idx
    end
  end

  defp find_end(idx, _n, _pre_max, _suf_min), do: idx
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where n is the length of the input array. We perform one linear pass to calculate suffix minimums, one pass for prefix maximums (which can be done on the fly), and one final pass to identify component boundaries and fill the result array. Each index is visited a constant number of times.
- **Space Complexity:** O(n) to store the suffix minimum array and the result array. In C, we allocate $O(n)$ space for suffix minimums and the result, while other variables use $O(1)$ additional space.
