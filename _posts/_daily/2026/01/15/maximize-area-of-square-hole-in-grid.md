---
layout: post
title: "Maximize Area of Square Hole in Grid"
date: 2026-01-15 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Sorting"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int getMaxConsecutive(std::vector<int>& bars)\
        \ {\n        if (bars.empty()) {\n            return 0; // Based on constraints,\
        \ bars will not be empty.\n        }\n        std::sort(bars.begin(), bars.end());\n\
        \        int max_consecutive = 1;\n        int current_consecutive = 1;\n  \
        \      for (int i = 1; i < bars.size(); ++i) {\n            if (bars[i] == bars[i-1]\
        \ + 1) {\n                current_consecutive++;\n            } else {\n   \
        \             current_consecutive = 1;\n            }\n            max_consecutive\
        \ = std::max(max_consecutive, current_consecutive);\n        }\n        return\
        \ max_consecutive;\n    }\n\n    int maximizeSquareHoleArea(int n, int m, std::vector<int>&\
        \ hBars, std::vector<int>& vBars) {\n        int max_h = getMaxConsecutive(hBars);\n\
        \        int max_v = getMaxConsecutive(vBars);\n        int side_length = std::min(max_h\
        \ + 1, max_v + 1);\n        return side_length * side_length;\n    }\n};"
      java: "import java.util.Arrays;\n\nclass Solution {\n    private int getMaxConsecutive(int[]\
        \ bars) {\n        if (bars.length == 0) {\n            return 0; // Based on\
        \ constraints, bars will not be empty.\n        }\n        Arrays.sort(bars);\n\
        \        int maxConsecutive = 1;\n        int currentConsecutive = 1;\n    \
        \    for (int i = 1; i < bars.length; i++) {\n            if (bars[i] == bars[i-1]\
        \ + 1) {\n                currentConsecutive++;\n            } else {\n    \
        \            currentConsecutive = 1;\n            }\n            maxConsecutive\
        \ = Math.max(maxConsecutive, currentConsecutive);\n        }\n        return\
        \ maxConsecutive;\n    }\n\n    public int maximizeSquareHoleArea(int n, int\
        \ m, int[] hBars, int[] vBars) {\n        int maxH = getMaxConsecutive(hBars);\n\
        \        int maxV = getMaxConsecutive(vBars);\n        int sideLength = Math.min(maxH\
        \ + 1, maxV + 1);\n        return sideLength * sideLength;\n    }\n}"
      python: "class Solution(object):\n    def _get_max_consecutive(self, bars):\n\
        \        if not bars:\n            return 0 # Based on constraints, bars will\
        \ not be empty.\n        bars.sort()\n        max_consecutive = 1\n        current_consecutive\
        \ = 1\n        for i in range(1, len(bars)):\n            if bars[i] == bars[i-1]\
        \ + 1:\n                current_consecutive += 1\n            else:\n      \
        \          current_consecutive = 1\n            max_consecutive = max(max_consecutive,\
        \ current_consecutive)\n        return max_consecutive\n\n    def maximizeSquareHoleArea(self,\
        \ n, m, hBars, vBars):\n        \"\"\"\n        :type n: int\n        :type\
        \ m: int\n        :type hBars: List[int]\n        :type vBars: List[int]\n \
        \       :rtype: int\n        \"\"\"\n        max_h = self._get_max_consecutive(hBars)\n\
        \        max_v = self._get_max_consecutive(vBars)\n        side_length = min(max_h\
        \ + 1, max_v + 1)\n        return side_length * side_length"
      python3: "class Solution:\n    def _get_max_consecutive(self, bars: List[int])\
        \ -> int:\n        if not bars:\n            return 0 # Based on constraints,\
        \ bars will not be empty.\n        bars.sort()\n        max_consecutive = 1\n\
        \        current_consecutive = 1\n        for i in range(1, len(bars)):\n  \
        \          if bars[i] == bars[i-1] + 1:\n                current_consecutive\
        \ += 1\n            else:\n                current_consecutive = 1\n       \
        \     max_consecutive = max(max_consecutive, current_consecutive)\n        return\
        \ max_consecutive\n\n    def maximizeSquareHoleArea(self, n: int, m: int, hBars:\
        \ List[int], vBars: List[int]) -> int:\n        max_h = self._get_max_consecutive(hBars)\n\
        \        max_v = self._get_max_consecutive(vBars)\n        side_length = min(max_h\
        \ + 1, max_v + 1)\n        return side_length * side_length"
      c: "#include <stdlib.h>\n#include <string.h>\n#include <stdio.h>\n\n// Comparison\
        \ function for qsort\nint compareInts(const void *a, const void *b) {\n    return\
        \ (*(int*)a - *(int*)b);\n}\n\nint getMaxConsecutive(int* bars, int barsSize)\
        \ {\n    if (barsSize == 0) {\n        return 0; // Based on constraints, bars\
        \ will not be empty.\n    }\n    qsort(bars, barsSize, sizeof(int), compareInts);\n\
        \    int max_consecutive = 1;\n    int current_consecutive = 1;\n    for (int\
        \ i = 1; i < barsSize; i++) {\n        if (bars[i] == bars[i-1] + 1) {\n   \
        \         current_consecutive++;\n        } else {\n            current_consecutive\
        \ = 1;\n        }\n        if (current_consecutive > max_consecutive) {\n  \
        \          max_consecutive = current_consecutive;\n        }\n    }\n    return\
        \ max_consecutive;\n}\n\nint maximizeSquareHoleArea(int n, int m, int* hBars,\
        \ int hBarsSize, int* vBars, int vBarsSize) {\n    int max_h = getMaxConsecutive(hBars,\
        \ hBarsSize);\n    int max_v = getMaxConsecutive(vBars, vBarsSize);\n    int\
        \ side_length = (max_h + 1 < max_v + 1) ? (max_h + 1) : (max_v + 1);\n    return\
        \ side_length * side_length;\n}"
      csharp: "using System;\nusing System.Linq;\n\npublic class Solution {\n    private\
        \ int GetMaxConsecutive(int[] bars) {\n        if (bars.Length == 0) {\n   \
        \         return 0; // Based on constraints, bars will not be empty.\n     \
        \   }\n        Array.Sort(bars);\n        int maxConsecutive = 1;\n        int\
        \ currentConsecutive = 1;\n        for (int i = 1; i < bars.Length; i++) {\n\
        \            if (bars[i] == bars[i-1] + 1) {\n                currentConsecutive++;\n\
        \            } else {\n                currentConsecutive = 1;\n           \
        \ }\n            maxConsecutive = Math.Max(maxConsecutive, currentConsecutive);\n\
        \        }\n        return maxConsecutive;\n    }\n\n    public int MaximizeSquareHoleArea(int\
        \ n, int m, int[] hBars, int[] vBars) {\n        int maxH = GetMaxConsecutive(hBars);\n\
        \        int maxV = GetMaxConsecutive(vBars);\n        int sideLength = Math.Min(maxH\
        \ + 1, maxV + 1);\n        return sideLength * sideLength;\n    }\n}"
      javascript: "/**\n * @param {number} n\n * @param {number} m\n * @param {number[]}\
        \ hBars\n * @param {number[]} vBars\n * @return {number}\n */\nvar maximizeSquareHoleArea\
        \ = function(n, m, hBars, vBars) {\n    const getMaxConsecutive = (bars) =>\
        \ {\n        if (bars.length === 0) {\n            return 0; // Based on constraints,\
        \ bars will not be empty.\n        }\n        bars.sort((a, b) => a - b);\n\
        \        let maxConsecutive = 1;\n        let currentConsecutive = 1;\n    \
        \    for (let i = 1; i < bars.length; i++) {\n            if (bars[i] === bars[i-1]\
        \ + 1) {\n                currentConsecutive++;\n            } else {\n    \
        \            currentConsecutive = 1;\n            }\n            maxConsecutive\
        \ = Math.max(maxConsecutive, currentConsecutive);\n        }\n        return\
        \ maxConsecutive;\n    };\n\n    const maxH = getMaxConsecutive(hBars);\n  \
        \  const maxV = getMaxConsecutive(vBars);\n    const sideLength = Math.min(maxH\
        \ + 1, maxV + 1);\n    return sideLength * sideLength;\n};"
      typescript: "function maximizeSquareHoleArea(n: number, m: number, hBars: number[],\
        \ vBars: number[]): number {\n    const getMaxConsecutive = (bars: number[]):\
        \ number => {\n        if (bars.length === 0) {\n            return 0; // Based\
        \ on constraints, bars will not be empty.\n        }\n        bars.sort((a,\
        \ b) => a - b);\n        let maxConsecutive = 1;\n        let currentConsecutive\
        \ = 1;\n        for (let i = 1; i < bars.length; i++) {\n            if (bars[i]\
        \ === bars[i-1] + 1) {\n                currentConsecutive++;\n            }\
        \ else {\n                currentConsecutive = 1;\n            }\n         \
        \   maxConsecutive = Math.max(maxConsecutive, currentConsecutive);\n       \
        \ }\n        return maxConsecutive;\n    };\n\n    const maxH = getMaxConsecutive(hBars);\n\
        \    const maxV = getMaxConsecutive(vBars);\n    const sideLength = Math.min(maxH\
        \ + 1, maxV + 1);\n    return sideLength * sideLength;\n};"
      php: "<?php\nclass Solution {\n\n    /**\n     * @param Integer $n\n     * @param\
        \ Integer $m\n     * @param Integer[] $hBars\n     * @param Integer[] $vBars\n\
        \     * @return Integer\n     */\n    function maximizeSquareHoleArea($n, $m,\
        \ $hBars, $vBars) {\n        $getMaxConsecutive = function($bars) {\n      \
        \      if (empty($bars)) {\n                return 0; // Based on constraints,\
        \ bars will not be empty.\n            }\n            sort($bars);\n       \
        \     $maxConsecutive = 1;\n            $currentConsecutive = 1;\n         \
        \   for ($i = 1; $i < count($bars); $i++) {\n                if ($bars[$i] ==\
        \ $bars[$i-1] + 1) {\n                    $currentConsecutive++;\n         \
        \       } else {\n                    $currentConsecutive = 1;\n           \
        \     }\n                $maxConsecutive = max($maxConsecutive, $currentConsecutive);\n\
        \            }\n            return $maxConsecutive;\n        };\n\n        $maxH\
        \ = $getMaxConsecutive($hBars);\n        $maxV = $getMaxConsecutive($vBars);\n\
        \        $sideLength = min($maxH + 1, $maxV + 1);\n        return $sideLength\
        \ * $sideLength;\n    }\n}\n?>"
      swift: "import Foundation\n\nclass Solution {\n    private func getMaxConsecutive(_\
        \ bars: [Int]) -> Int {\n        if bars.isEmpty {\n            return 0 //\
        \ Based on constraints, bars will not be empty.\n        }\n        var sortedBars\
        \ = bars.sorted()\n        var maxConsecutive = 1\n        var currentConsecutive\
        \ = 1\n        for i in 1..<sortedBars.count {\n            if sortedBars[i]\
        \ == sortedBars[i-1] + 1 {\n                currentConsecutive += 1\n      \
        \      } else {\n                currentConsecutive = 1\n            }\n   \
        \         maxConsecutive = max(maxConsecutive, currentConsecutive)\n       \
        \ }\n        return maxConsecutive\n    }\n\n    func maximizeSquareHoleArea(_\
        \ n: Int, _ m: Int, _ hBars: [Int], _ vBars: [Int]) -> Int {\n        let maxH\
        \ = getMaxConsecutive(hBars)\n        let maxV = getMaxConsecutive(vBars)\n\
        \        let sideLength = min(maxH + 1, maxV + 1)\n        return sideLength\
        \ * sideLength\n    }\n}"
      kotlin: "class Solution {\n    fun maximizeSquareHoleArea(n: Int, m: Int, hBars:\
        \ IntArray, vBars: IntArray): Int {\n        val maxLenH = getMaxConsecutiveLength(hBars)\n\
        \        val maxLenV = getMaxConsecutiveLength(vBars)\n\n        val side =\
        \ minOf(maxLenH + 1, maxLenV + 1)\n        return side * side\n    }\n\n   \
        \ private fun getMaxConsecutiveLength(bars: IntArray): Int {\n        if (bars.isEmpty())\
        \ {\n            return 0\n        }\n\n        bars.sort()\n        var maxLen\
        \ = 1\n        var currentLen = 1\n\n        for (i in 1 until bars.size) {\n\
        \            if (bars[i] == bars[i-1] + 1) {\n                currentLen++\n\
        \            } else {\n                currentLen = 1\n            }\n     \
        \       maxLen = maxOf(maxLen, currentLen)\n        }\n\n        return maxLen\n\
        \    }\n}"
      dart: "class Solution {\n  int maximizeSquareHoleArea(int n, int m, List<int>\
        \ hBars, List<int> vBars) {\n    int maxLenH = _getMaxConsecutiveLength(hBars);\n\
        \    int maxLenV = _getMaxConsecutiveLength(vBars);\n\n    int side = (maxLenH\
        \ + 1 < maxLenV + 1) ? (maxLenH + 1) : (maxLenV + 1);\n    return side * side;\n\
        \  }\n\n  int _getMaxConsecutiveLength(List<int> bars) {\n    if (bars.isEmpty)\
        \ {\n      return 0;\n    }\n\n    bars.sort();\n    int maxLen = 1;\n    int\
        \ currentLen = 1;\n\n    for (int i = 1; i < bars.length; i++) {\n      if (bars[i]\
        \ == bars[i-1] + 1) {\n        currentLen++;\n      } else {\n        currentLen\
        \ = 1;\n      }\n      if (currentLen > maxLen) {\n        maxLen = currentLen;\n\
        \      }\n    }\n\n    return maxLen;\n  }\n}"
      go: "import \"sort\"\n\nfunc maximizeSquareHoleArea(n int, m int, hBars []int,\
        \ vBars []int) int {\n    maxLenH := getMaxConsecutiveLength(hBars)\n    maxLenV\
        \ := getMaxConsecutiveLength(vBars)\n\n    side := min(maxLenH + 1, maxLenV\
        \ + 1)\n    return side * side\n}\n\nfunc getMaxConsecutiveLength(bars []int)\
        \ int {\n    if len(bars) == 0 {\n        return 0\n    }\n\n    sort.Ints(bars)\n\
        \    maxLen := 1\n    currentLen := 1\n\n    for i := 1; i < len(bars); i++\
        \ {\n        if bars[i] == bars[i-1] + 1 {\n            currentLen++\n     \
        \   } else {\n            currentLen = 1\n        }\n        if currentLen >\
        \ maxLen {\n            maxLen = currentLen\n        }\n    }\n\n    return\
        \ maxLen\n}\n\nfunc min(a, b int) int {\n    if a < b {\n        return a\n\
        \    }\n    return b\n}"
      ruby: "# @param {Integer} n\n# @param {Integer} m\n# @param {Integer[]} h_bars\n\
        # @param {Integer[]} v_bars\n# @return {Integer}\ndef maximize_square_hole_area(n,\
        \ m, h_bars, v_bars)\n    max_len_h = get_max_consecutive_length(h_bars)\n \
        \   max_len_v = get_max_consecutive_length(v_bars)\n\n    side = [max_len_h\
        \ + 1, max_len_v + 1].min\n    side * side\nend\n\ndef get_max_consecutive_length(bars)\n\
        \    return 0 if bars.empty?\n\n    bars.sort!\n    max_len = 1\n    current_len\
        \ = 1\n\n    (1...bars.length).each do |i|\n        if bars[i] == bars[i-1]\
        \ + 1\n            current_len += 1\n        else\n            current_len =\
        \ 1\n        end\n        max_len = [max_len, current_len].max\n    end\n\n\
        \    max_len\nend"
      scala: "object Solution {\n    def maximizeSquareHoleArea(n: Int, m: Int, hBars:\
        \ Array[Int], vBars: Array[Int]): Int = {\n        val maxLenH = getMaxConsecutiveLength(hBars)\n\
        \        val maxLenV = getMaxConsecutiveLength(vBars)\n\n        val side =\
        \ Math.min(maxLenH + 1, maxLenV + 1)\n        side * side\n    }\n\n    private\
        \ def getMaxConsecutiveLength(bars: Array[Int]): Int = {\n        if (bars.isEmpty)\
        \ {\n            return 0\n        }\n\n        val sortedBars = bars.sorted\n\
        \        var maxLen = 1\n        var currentLen = 1\n\n        for (i <- 1 until\
        \ sortedBars.length) {\n            if (sortedBars(i) == sortedBars(i-1) + 1)\
        \ {\n                currentLen += 1\n            } else {\n               \
        \ currentLen = 1\n            }\n            maxLen = Math.max(maxLen, currentLen)\n\
        \        }\n\n        maxLen\n    }\n}"
      rust: "impl Solution {\n    pub fn maximize_square_hole_area(n: i32, m: i32, h_bars:\
        \ Vec<i32>, v_bars: Vec<i32>) -> i32 {\n        let max_len_h = Self::get_max_consecutive_length(h_bars);\n\
        \        let max_len_v = Self::get_max_consecutive_length(v_bars);\n\n     \
        \   let side = std::cmp::min(max_len_h + 1, max_len_v + 1);\n        side *\
        \ side\n    }\n\n    fn get_max_consecutive_length(mut bars: Vec<i32>) -> i32\
        \ {\n        if bars.is_empty() {\n            return 0;\n        }\n\n    \
        \    bars.sort_unstable();\n        let mut max_len = 1;\n        let mut current_len\
        \ = 1;\n\n        for i in 1..bars.len() {\n            if bars[i] == bars[i-1]\
        \ + 1 {\n                current_len += 1;\n            } else {\n         \
        \       current_len = 1;\n            }\n            max_len = std::cmp::max(max_len,\
        \ current_len);\n        }\n\n        max_len\n    }\n}"
      racket: "(define/contract (maximize-square-hole-area n m hBars vBars)\n  (-> exact-integer?\
        \ exact-integer? (listof exact-integer?) (listof exact-integer?) exact-integer?)\n\
        \  (define (get-max-consecutive-length bars)\n    (if (empty? bars)\n      \
        \  0\n        (let* ([sorted-bars (list->vector (sort bars <))]\n          \
        \     [len (vector-length sorted-bars)])\n          (if (= len 1)\n        \
        \      1\n              (let-values ([(max-len current-len)\n              \
        \              (for/fold ([max-len 1] [current-len 1])\n                   \
        \                   ([i (in-range 1 len)])\n                              (let\
        \ ([prev-bar (vector-ref sorted-bars (- i 1))]\n                           \
        \         [curr-bar (vector-ref sorted-bars i)])\n                         \
        \       (if (= curr-bar (+ prev-bar 1))\n                                  \
        \  (values (max max-len (+ current-len 1)) (+ current-len 1))\n            \
        \                        (values (max max-len 1) 1))))])\n                max-len)))))\
        \ ; max-len is the result of the fold\n\n  (let* ([max-len-h (get-max-consecutive-length\
        \ hBars)]\n         [max-len-v (get-max-consecutive-length vBars)]\n       \
        \  [side (+ 1 (min max-len-h max-len-v))])\n    (* side side)))"
      erlang: "-spec maximize_square_hole_area(N :: integer(), M :: integer(), HBars\
        \ :: [integer()], VBars :: [integer()]) -> integer().\nmaximize_square_hole_area(N,\
        \ M, HBars, VBars) ->\n  MaxLenH = get_max_consecutive_length(HBars),\n  MaxLenV\
        \ = get_max_consecutive_length(VBars),\n  Side = min(MaxLenH + 1, MaxLenV +\
        \ 1),\n  Side * Side.\n\nget_max_consecutive_length(Bars) ->\n  case Bars of\n\
        \    [] -> 0;\n    _ ->\n      SortedBars = lists:sort(Bars),\n      get_max_consecutive_length_impl(SortedBars,\
        \ 1, 1)\n  end.\n\nget_max_consecutive_length_impl([_], MaxLen, _CurrentLen)\
        \ ->\n  MaxLen;\nget_max_consecutive_length_impl([H1, H2 | T], MaxLen, CurrentLen)\
        \ ->\n  if H2 == H1 + 1 ->\n    NewCurrentLen = CurrentLen + 1,\n    NewMaxLen\
        \ = max(MaxLen, NewCurrentLen),\n    get_max_consecutive_length_impl([H2 | T],\
        \ NewMaxLen, NewCurrentLen);\n  true ->\n    NewCurrentLen = 1,\n    NewMaxLen\
        \ = max(MaxLen, NewCurrentLen),\n    get_max_consecutive_length_impl([H2 | T],\
        \ NewMaxLen, NewCurrentLen)\n  end."
      elixir: "defmodule Solution do\n  @spec maximize_square_hole_area(n :: integer,\
        \ m :: integer, h_bars :: [integer], v_bars :: [integer]) :: integer\n  def\
        \ maximize_square_hole_area(n, m, h_bars, v_bars) do\n    max_len_h = get_max_consecutive_length(h_bars)\n\
        \    max_len_v = get_max_consecutive_length(v_bars)\n\n    side = min(max_len_h\
        \ + 1, max_len_v + 1)\n    side * side\n  end\n\n  defp get_max_consecutive_length(bars)\
        \ do\n    case bars do\n      [] -> 0\n      _ ->\n        sorted_bars = Enum.sort(bars)\n\
        \        do_get_max_consecutive_length(sorted_bars, 1, 1)\n    end\n  end\n\n\
        \  defp do_get_max_consecutive_length([_], max_len, _current_len), do: max_len\n\
        \  defp do_get_max_consecutive_length([h1, h2 | t], max_len, current_len) do\n\
        \    if h2 == h1 + 1 do\n      new_current_len = current_len + 1\n      new_max_len\
        \ = max(max_len, new_current_len)\n      do_get_max_consecutive_length([h2 |\
        \ t], new_max_len, new_current_len)\n    else\n      new_current_len = 1\n \
        \     new_max_len = max(max_len, new_current_len)\n      do_get_max_consecutive_length([h2\
        \ | t], new_max_len, new_current_len)\n    end\n  end\nend"
    approach: 'The problem asks for the maximum area of a square-shaped hole that can
      be formed by removing certain horizontal and vertical bars. A square hole of side
      length ''S'' implies that we need to remove ''S-1'' consecutive horizontal bars
      and ''S-1'' consecutive vertical bars, such that the remaining boundary bars define
      an ''S'' unit span. For example, to create a 1x1 hole, we need 0 bars removed,
      meaning the space between two fixed adjacent bars. To create a 2x2 hole, we need
      to remove one horizontal bar (e.g., bar 2 to open space between 1 and 3) and one
      vertical bar (e.g., bar 2 to open space between 1 and 3). The key insight, as
      suggested by the hints, is that if we have ''k'' consecutive removable bars (e.g.,
      `i, i+1, ..., i+k-1`), we can remove all of them to create an open span of `k+1`
      units between the fixed bars `i-1` and `i+k`. The bars `1` and `n+2` (or `m+2`)
      are always fixed boundaries because `hBars[i]` and `vBars[i]` are constrained
      to be between `2` and `n+1` (or `m+1`).


      The algorithm proceeds by first determining the maximum possible side length achievable
      horizontally and vertically. For each set of bars (`hBars` and `vBars`), we sort
      the array. Then, we iterate through the sorted array to find the longest sequence
      of consecutive integers. If `k` is the length of the longest consecutive sequence
      of removable bars (e.g., `[2,3]` has length 2), then the maximum span we can create
      in that dimension is `k+1`. We calculate this `k+1` value for both horizontal
      and vertical bars. The side length of the largest square hole will be the minimum
      of these two maximum achievable spans. Finally, the area is the square of this
      side length.'
    time_complexity: The time complexity is dominated by sorting the input arrays. Let
      `L_h` be the length of `hBars` and `L_v` be the length of `vBars`. Sorting `hBars`
      takes O(L_h log L_h) time, and sorting `vBars` takes O(L_v log L_v) time. After
      sorting, iterating through each array to find the longest consecutive sequence
      takes O(L_h) and O(L_v) time, respectively. Therefore, the total time complexity
      is O(L_h log L_h + L_v log L_v). Given that `L_h` and `L_v` are at most 100, this
      is very efficient.
    space_complexity: The space complexity depends on the sorting algorithm used. If
      an in-place sort is used, the auxiliary space complexity would be O(1) (excluding
      the input arrays). If the sorting algorithm requires auxiliary space (e.g., Timsort
      used by Python's list.sort() or Scala's sorted method which creates a new array),
      it would be O(L_h) for `hBars` and O(L_v) for `vBars`. Thus, the total auxiliary
      space complexity is O(L_h + L_v) in the worst case, which is minimal given the
      constraints on `L_h` and `L_v`.
    elapsed_time: 113.55222988128662
    model: gemini-2.5-flash
    generated_at: '2026-01-15 22:44:43 '
  - solutions:
      cpp: "class Solution {\npublic:\n    int maximizeSquareHoleArea(int n, int m,\
        \ vector<int>& hBars, vector<int>& vBars) {\n        sort(hBars.begin(), hBars.end());\n\
        \        sort(vBars.begin(), vBars.end());\n        int hx = hBars[0], hy =\
        \ hBars[0], vx = vBars[0], vy = vBars[0];\n        for (int i = 1; i < hBars.size();\
        \ i++) {\n            if (hBars[i] == hBars[i-1] + 1) {\n                hy\
        \ = hBars[i];\n            } else {\n                break;\n            }\n\
        \        }\n        for (int i = 1; i < vBars.size(); i++) {\n            if\
        \ (vBars[i] == vBars[i-1] + 1) {\n                vy = vBars[i];\n         \
        \   } else {\n                break;\n            }\n        }\n        int\
        \ maxLen = min(hy - hx + 2, vy - vx + 2);\n        return maxLen * maxLen;\n\
        \    }\n};"
      java: "class Solution {\n    public int maximizeSquareHoleArea(int n, int m, int[]\
        \ hBars, int[] vBars) {\n        Arrays.sort(hBars);\n        Arrays.sort(vBars);\n\
        \        int hx = hBars[0], hy = hBars[0], vx = vBars[0], vy = vBars[0];\n \
        \       for (int i = 1; i < hBars.length; i++) {\n            if (hBars[i] ==\
        \ hBars[i-1] + 1) {\n                hy = hBars[i];\n            } else {\n\
        \                break;\n            }\n        }\n        for (int i = 1; i\
        \ < vBars.length; i++) {\n            if (vBars[i] == vBars[i-1] + 1) {\n  \
        \              vy = vBars[i];\n            } else {\n                break;\n\
        \            }\n        }\n        int maxLen = Math.min(hy - hx + 2, vy - vx\
        \ + 2);\n        return maxLen * maxLen;\n    }\n}"
      python: "class Solution(object):\n    def maximizeSquareHoleArea(self, n, m, hBars,\
        \ vBars):\n        hBars.sort()\n        vBars.sort()\n        hx, hy = hBars[0],\
        \ hBars[0]\n        vx, vy = vBars[0], vBars[0]\n        for i in range(1, len(hBars)):\n\
        \            if hBars[i] == hBars[i-1] + 1:\n                hy = hBars[i]\n\
        \            else:\n                break\n        for i in range(1, len(vBars)):\n\
        \            if vBars[i] == vBars[i-1] + 1:\n                vy = vBars[i]\n\
        \            else:\n                break\n        maxLen = min(hy - hx + 2,\
        \ vy - vx + 2)\n        return maxLen * maxLen"
      python3: "class Solution:\n    def maximizeSquareHoleArea(self, n: int, m: int,\
        \ hBars: list[int], vBars: list[int]) -> int:\n        hBars.sort()\n      \
        \  vBars.sort()\n        hx, hy = hBars[0], hBars[0]\n        vx, vy = vBars[0],\
        \ vBars[0]\n        for i in range(1, len(hBars)):\n            if hBars[i]\
        \ == hBars[i-1] + 1:\n                hy = hBars[i]\n            else:\n   \
        \             break\n        for i in range(1, len(vBars)):\n            if\
        \ vBars[i] == vBars[i-1] + 1:\n                vy = vBars[i]\n            else:\n\
        \                break\n        maxLen = min(hy - hx + 2, vy - vx + 2)\n   \
        \     return maxLen * maxLen"
      c: "int maximizeSquareHoleArea(int n, int m, int* hBars, int hBarsSize, int* vBars,\
        \ int vBarsSize) {\n    int hx = hBars[0], hy = hBars[0], vx = vBars[0], vy\
        \ = vBars[0];\n    for (int i = 1; i < hBarsSize; i++) {\n        if (hBars[i]\
        \ == hBars[i-1] + 1) {\n            hy = hBars[i];\n        } else {\n     \
        \       break;\n        }\n    }\n    for (int i = 1; i < vBarsSize; i++) {\n\
        \        if (vBars[i] == vBars[i-1] + 1) {\n            vy = vBars[i];\n   \
        \     } else {\n            break;\n        }\n    }\n    int maxLen = (hy -\
        \ hx + 2 < vy - vx + 2) ? hy - hx + 2 : vy - vx + 2;\n    return maxLen * maxLen;\n\
        }"
      csharp: "public class Solution {\n    public int MaximizeSquareHoleArea(int n,\
        \ int m, int[] hBars, int[] vBars) {\n        Array.Sort(hBars);\n        Array.Sort(vBars);\n\
        \        int hx = hBars[0], hy = hBars[0], vx = vBars[0], vy = vBars[0];\n \
        \       for (int i = 1; i < hBars.Length; i++) {\n            if (hBars[i] ==\
        \ hBars[i-1] + 1) {\n                hy = hBars[i];\n            } else {\n\
        \                break;\n            }\n        }\n        for (int i = 1; i\
        \ < vBars.Length; i++) {\n            if (vBars[i] == vBars[i-1] + 1) {\n  \
        \              vy = vBars[i];\n            } else {\n                break;\n\
        \            }\n        }\n        int maxLen = Math.Min(hy - hx + 2, vy - vx\
        \ + 2);\n        return maxLen * maxLen;\n    }\n}"
      javascript: "var maximizeSquareHoleArea = function(n, m, hBars, vBars) {\n   \
        \ hBars.sort((a, b) => a - b);\n    vBars.sort((a, b) => a - b);\n    let hx\
        \ = hBars[0], hy = hBars[0], vx = vBars[0], vy = vBars[0];\n    for (let i =\
        \ 1; i < hBars.length; i++) {\n        if (hBars[i] == hBars[i-1] + 1) {\n \
        \           hy = hBars[i];\n        } else {\n            break;\n        }\n\
        \    }\n    for (let i = 1; i < vBars.length; i++) {\n        if (vBars[i] ==\
        \ vBars[i-1] + 1) {\n            vy = vBars[i];\n        } else {\n        \
        \    break;\n        }\n    }\n    let maxLen = Math.min(hy - hx + 2, vy - vx\
        \ + 2);\n    return maxLen * maxLen;\n};"
      typescript: "function maximizeSquareHoleArea(n: number, m: number, hBars: number[],\
        \ vBars: number[]): number {\n    hBars.sort((a, b) => a - b);\n    vBars.sort((a,\
        \ b) => a - b);\n    let hx: number = hBars[0], hy: number = hBars[0], vx: number\
        \ = vBars[0], vy: number = vBars[0];\n    for (let i: number = 1; i < hBars.length;\
        \ i++) {\n        if (hBars[i] == hBars[i-1] + 1) {\n            hy = hBars[i];\n\
        \        } else {\n            break;\n        }\n    }\n    for (let i: number\
        \ = 1; i < vBars.length; i++) {\n        if (vBars[i] == vBars[i-1] + 1) {\n\
        \            vy = vBars[i];\n        } else {\n            break;\n        }\n\
        \    }\n    let maxLen: number = Math.min(hy - hx + 2, vy - vx + 2);\n    return\
        \ maxLen * maxLen;\n}"
      php: "class Solution {\n    function maximizeSquareHoleArea($n, $m, $hBars, $vBars)\
        \ {\n        sort($hBars);\n        sort($vBars);\n        $hx = $hBars[0];\
        \ $hy = $hBars[0]; $vx = $vBars[0]; $vy = $vBars[0];\n        for ($i = 1; $i\
        \ < count($hBars); $i++) {\n            if ($hBars[$i] == $hBars[$i-1] + 1)\
        \ {\n                $hy = $hBars[$i];\n            } else {\n             \
        \   break;\n            }\n        }\n        for ($i = 1; $i < count($vBars);\
        \ $i++) {\n            if ($vBars[$i] == $vBars[$i-1] + 1) {\n             \
        \   $vy = $vBars[$i];\n            } else {\n                break;\n      \
        \      }\n        }\n        $maxLen = min($hy - $hx + 2, $vy - $vx + 2);\n\
        \        return $maxLen * $maxLen;\n    }\n}"
      swift: "class Solution {\n    func maximizeSquareHoleArea(_ n: Int, _ m: Int,\
        \ _ hBars: [Int], _ vBars: [Int]) -> Int {\n        let sortedHBars = hBars.sorted();\n\
        \        let sortedVBars = vBars.sorted();\n        var hx: Int = sortedHBars[0],\
        \ hy: Int = sortedHBars[0], vx: Int = sortedVBars[0], vy: Int = sortedVBars[0];\n\
        \        for i in 1..<sortedHBars.count {\n            if sortedHBars[i] ==\
        \ sortedHBars[i-1] + 1 {\n                hy = sortedHBars[i];\n           \
        \ } else {\n                break;\n            }\n        }\n        for i\
        \ in 1..<sortedVBars.count {\n            if sortedVBars[i] == sortedVBars[i-1]\
        \ + 1 {\n                vy = sortedVBars[i];\n            } else {\n      \
        \          break;\n            }\n        }\n        let maxLen = min(hy - hx\
        \ + 2, vy - vx + 2);\n        return maxLen * maxLen;\n    }\n}"
      kotlin: "class Solution {\n    fun maximizeSquareHoleArea(n: Int, m: Int, hBars:\
        \ IntArray, vBars: IntArray): Int {\n        val sortedHBars = hBars.sorted()\n\
        \        val sortedVBars = vBars.sorted()\n        var maxHSequence = 0\n  \
        \      var maxVSequence = 0\n        var currentHSequence = 1\n        var currentVSequence\
        \ = 1\n        for (i in 1 until sortedHBars.size) {\n            if (sortedHBars[i]\
        \ - sortedHBars[i - 1] == 1) {\n                currentHSequence++\n       \
        \     } else {\n                maxHSequence = maxOf(maxHSequence, currentHSequence)\n\
        \                currentHSequence = 1\n            }\n        }\n        maxHSequence\
        \ = maxOf(maxHSequence, currentHSequence)\n        for (i in 1 until sortedVBars.size)\
        \ {\n            if (sortedVBars[i] - sortedVBars[i - 1] == 1) {\n         \
        \       currentVSequence++\n            } else {\n                maxVSequence\
        \ = maxOf(maxVSequence, currentVSequence)\n                currentVSequence\
        \ = 1\n            }\n        }\n        maxVSequence = maxOf(maxVSequence,\
        \ currentVSequence)\n        val maxSquareLength = minOf(maxHSequence + 1, maxVSequence\
        \ + 1)\n        return maxSquareLength * maxSquareLength\n    }\n}"
      dart: "class Solution {\n  int maximizeSquareHoleArea(int n, int m, List<int>\
        \ hBars, List<int> vBars) {\n    hBars.sort();\n    vBars.sort();\n    int maxHSequence\
        \ = 0;\n    int maxVSequence = 0;\n    int currentHSequence = 1;\n    int currentVSequence\
        \ = 1;\n    for (int i = 1; i < hBars.length; i++) {\n      if (hBars[i] - hBars[i\
        \ - 1] == 1) {\n        currentHSequence++;\n      } else {\n        maxHSequence\
        \ = maxHSequence > currentHSequence ? maxHSequence : currentHSequence;\n   \
        \     currentHSequence = 1;\n      }\n    }\n    maxHSequence = maxHSequence\
        \ > currentHSequence ? maxHSequence : currentHSequence;\n    for (int i = 1;\
        \ i < vBars.length; i++) {\n      if (vBars[i] - vBars[i - 1] == 1) {\n    \
        \    currentVSequence++;\n      } else {\n        maxVSequence = maxVSequence\
        \ > currentVSequence ? maxVSequence : currentVSequence;\n        currentVSequence\
        \ = 1;\n      }\n    }\n    maxVSequence = maxVSequence > currentVSequence ?\
        \ maxVSequence : currentVSequence;\n    int maxSquareLength = maxHSequence <\
        \ maxVSequence + 1 ? maxHSequence + 1 : maxVSequence + 1;\n    return maxSquareLength\
        \ * maxSquareLength;\n  }\n}"
      go: "func maximizeSquareHoleArea(n int, m int, hBars []int, vBars []int) int {\n\
        \    sort.Ints(hBars)\n    sort.Ints(vBars)\n    maxHSequence := 0\n    maxVSequence\
        \ := 0\n    currentHSequence := 1\n    currentVSequence := 1\n    for i := 1;\
        \ i < len(hBars); i++ {\n        if hBars[i]-hBars[i-1] == 1 {\n           \
        \ currentHSequence++\n        } else {\n            if currentHSequence > maxHSequence\
        \ {\n                maxHSequence = currentHSequence\n            }\n      \
        \      currentHSequence = 1\n        }\n    }\n    if currentHSequence > maxHSequence\
        \ {\n        maxHSequence = currentHSequence\n    }\n    for i := 1; i < len(vBars);\
        \ i++ {\n        if vBars[i]-vBars[i-1] == 1 {\n            currentVSequence++\n\
        \        } else {\n            if currentVSequence > maxVSequence {\n      \
        \          maxVSequence = currentVSequence\n            }\n            currentVSequence\
        \ = 1\n        }\n    }\n    if currentVSequence > maxVSequence {\n        maxVSequence\
        \ = currentVSequence\n    }\n    maxSquareLength := min(maxHSequence+1, maxVSequence+1)\n\
        \    return maxSquareLength * maxSquareLength\n}"
      ruby: "# @param {Integer} n\n# @param {Integer} m\n# @param {Integer[]} h_bars\n\
        # @param {Integer[]} v_bars\n# @return {Integer}\ndef maximize_square_hole_area(n,\
        \ m, h_bars, v_bars)\n    h_bars.sort!\n    v_bars.sort!\n    max_h_sequence\
        \ = 0\n    max_v_sequence = 0\n    current_h_sequence = 1\n    current_v_sequence\
        \ = 1\n    (1...h_bars.size).each do |i|\n        if h_bars[i] - h_bars[i -\
        \ 1] == 1\n            current_h_sequence += 1\n        else\n            max_h_sequence\
        \ = [max_h_sequence, current_h_sequence].max\n            current_h_sequence\
        \ = 1\n        end\n    end\n    max_h_sequence = [max_h_sequence, current_h_sequence].max\n\
        \    (1...v_bars.size).each do |i|\n        if v_bars[i] - v_bars[i - 1] ==\
        \ 1\n            current_v_sequence += 1\n        else\n            max_v_sequence\
        \ = [max_v_sequence, current_v_sequence].max\n            current_v_sequence\
        \ = 1\n        end\n    end\n    max_v_sequence = [max_v_sequence, current_v_sequence].max\n\
        \    max_square_length = [max_h_sequence + 1, max_v_sequence + 1].min\n    max_square_length\
        \ * max_square_length\nend"
      scala: "object Solution {\n    def maximizeSquareHoleArea(n: Int, m: Int, hBars:\
        \ Array[Int], vBars: Array[Int]): Int = {\n        val sortedHBars = hBars.sorted\n\
        \        val sortedVBars = vBars.sorted\n        var maxHSequence = 0\n    \
        \    var maxVSequence = 0\n        var currentHSequence = 1\n        var currentVSequence\
        \ = 1\n        for (i <- 1 until sortedHBars.length) {\n            if (sortedHBars(i)\
        \ - sortedHBars(i - 1) == 1) {\n                currentHSequence += 1\n    \
        \        } else {\n                maxHSequence = math.max(maxHSequence, currentHSequence)\n\
        \                currentHSequence = 1\n            }\n        }\n        maxHSequence\
        \ = math.max(maxHSequence, currentHSequence)\n        for (i <- 1 until sortedVBars.length)\
        \ {\n            if (sortedVBars(i) - sortedVBars(i - 1) == 1) {\n         \
        \       currentVSequence += 1\n            } else {\n                maxVSequence\
        \ = math.max(maxVSequence, currentVSequence)\n                currentVSequence\
        \ = 1\n            }\n        }\n        maxVSequence = math.max(maxVSequence,\
        \ currentVSequence)\n        val maxSquareLength = math.min(maxHSequence + 1,\
        \ maxVSequence + 1)\n        maxSquareLength * maxSquareLength\n    }\n}"
      rust: "impl Solution {\n    pub fn maximize_square_hole_area(n: i32, m: i32, h_bars:\
        \ Vec<i32>, v_bars: Vec<i32>) -> i32 {\n        let mut h_bars = h_bars;\n \
        \       let mut v_bars = v_bars;\n        h_bars.sort();\n        v_bars.sort();\n\
        \        let mut max_h_sequence = 0;\n        let mut max_v_sequence = 0;\n\
        \        let mut current_h_sequence = 1;\n        let mut current_v_sequence\
        \ = 1;\n        for i in 1..h_bars.len() {\n            if h_bars[i] - h_bars[i\
        \ - 1] == 1 {\n                current_h_sequence += 1;\n            } else\
        \ {\n                max_h_sequence = max_h_sequence.max(current_h_sequence);\n\
        \                current_h_sequence = 1;\n            }\n        }\n       \
        \ max_h_sequence = max_h_sequence.max(current_h_sequence);\n        for i in\
        \ 1..v_bars.len() {\n            if v_bars[i] - v_bars[i - 1] == 1 {\n     \
        \           current_v_sequence += 1;\n            } else {\n               \
        \ max_v_sequence = max_v_sequence.max(current_v_sequence);\n               \
        \ current_v_sequence = 1;\n            }\n        }\n        max_v_sequence\
        \ = max_v_sequence.max(current_v_sequence);\n        let max_square_length =\
        \ max_h_sequence.min(max_v_sequence) + 1;\n        max_square_length * max_square_length\n\
        \    }\n}"
      racket: "(define/contract (maximize-square-hole-area n m hBars vBars)\n  (-> exact-integer?\
        \ exact-integer? (listof exact-integer?) (listof exact-integer?) exact-integer?)\n\
        \  (let* (\n         (hBars (sort hBars <))\n         (vBars (sort vBars <))\n\
        \         (max-h-sequence 0)\n         (max-v-sequence 0)\n         (current-h-sequence\
        \ 1)\n         (current-v-sequence 1))\n    (for ((i (range 1 (length hBars))))\n\
        \      (if (= (- (list-ref hBars i) (list-ref hBars (- i 1))) 1)\n         \
        \ (set! current-h-sequence (+ current-h-sequence 1))\n          (begin\n   \
        \         (set! max-h-sequence (max max-h-sequence current-h-sequence))\n  \
        \          (set! current-h-sequence 1)))))\n    (set! max-h-sequence (max max-h-sequence\
        \ current-h-sequence))\n    (for ((i (range 1 (length vBars))))\n      (if (=\
        \ (- (list-ref vBars i) (list-ref vBars (- i 1))) 1)\n          (set! current-v-sequence\
        \ (+ current-v-sequence 1))\n          (begin\n            (set! max-v-sequence\
        \ (max max-v-sequence current-v-sequence))\n            (set! current-v-sequence\
        \ 1)))))\n    (set! max-v-sequence (max max-v-sequence current-v-sequence))\n\
        \    (let ((max-square-length (min (+ max-h-sequence 1) (+ max-v-sequence 1))))\n\
        \      (* max-square-length max-square-length))))"
      erlang: "-spec maximize_square_hole_area(N :: integer(), M :: integer(), HBars\
        \ :: [integer()], VBars :: [integer()]) -> integer().\nmaximize_square_hole_area(N,\
        \ M, HBars, VBars) ->\n    lists:foldl(\n      fun(X, {MaxH, MaxV, CurrentH,\
        \ CurrentV}) ->\n              case X - hd(HBars) of\n                  1 ->\
        \ {MaxH, MaxV, CurrentH + 1, CurrentV};\n                  _ -> {max(MaxH, CurrentH),\
        \ MaxV, 1, CurrentV}\n              end\n      end,\n      {0, 0, 1, 1},\n \
        \     lists:sort(HBars))"
      elixir: "defmodule Solution do\n  @spec maximize_square_hole_area(n :: integer,\
        \ m :: integer, h_bars :: [integer], v_bars :: [integer]) :: integer\n  def\
        \ maximize_square_hole_area(n, m, h_bars, v_bars) do\n    h_bars = Enum.sort(h_bars)\n\
        \    v_bars = Enum.sort(v_bars)\n    max_h_sequence = 0\n    max_v_sequence\
        \ = 0\n    current_h_sequence = 1\n    current_v_sequence = 1\n    for i <-\
        \ 1..length(h_bars) - 1 do\n      if Enum.at(h_bars, i) - Enum.at(h_bars, i\
        \ - 1) == 1 do\n        current_h_sequence = current_h_sequence + 1\n      else\n\
        \        max_h_sequence = max(max_h_sequence, current_h_sequence)\n        current_h_sequence\
        \ = 1\n      end\n    end\n    max_h_sequence = max(max_h_sequence, current_h_sequence)\n\
        \    for i <- 1..length(v_bars) - 1 do\n      if Enum.at(v_bars, i) - Enum.at(v_bars,\
        \ i - 1) == 1 do\n        current_v_sequence = current_v_sequence + 1\n    \
        \  else\n        max_v_sequence = max(max_v_sequence, current_v_sequence)\n\
        \        current_v_sequence = 1\n      end\n    end\n    max_v_sequence = max(max_v_sequence,\
        \ current_v_sequence)\n    max_square_length = min(max_h_sequence + 1, max_v_sequence\
        \ + 1)\n    max_square_length * max_square_length\n  end\nend"
    approach: 'The problem can be solved by first sorting the hBars and vBars arrays.
      Then, we can find the longest sequence of consecutive integer values in each array,
      denoted as [hx, hy] and [vx, vy], respectively. The maximum square length we can
      get is min(hy - hx + 2, vy - vx + 2). Finally, we square the maximum square length
      to get the area. The key intuition is to consider the possible square holes that
      can be formed by removing some of the bars in hBars and vBars, and then find the
      maximum area among these possible holes.


      The algorithm works by iterating over the sorted hBars and vBars arrays to find
      the longest sequence of consecutive integer values. We can use two pointers to
      track the start and end of the current sequence. If the current element is consecutive
      to the previous one, we move the end pointer forward. Otherwise, we update the
      maximum sequence length if necessary and move the start pointer forward. After
      finding the maximum sequence lengths for hBars and vBars, we can calculate the
      maximum square length and area.'
    time_complexity: The time complexity of the algorithm is O(n log n + m log m), where
      n and m are the lengths of the hBars and vBars arrays, respectively. This is because
      we need to sort the arrays first, which takes O(n log n) and O(m log m) time.
      Then, we iterate over the sorted arrays to find the longest sequence of consecutive
      integer values, which takes O(n) and O(m) time. Therefore, the overall time complexity
      is dominated by the sorting step.
    space_complexity: The space complexity of the algorithm is O(n + m), where n and
      m are the lengths of the hBars and vBars arrays, respectively. This is because
      we need to store the sorted arrays, which takes O(n) and O(m) space. We also need
      to store the maximum sequence lengths and the maximum square length, which takes
      constant space. Therefore, the overall space complexity is linear in the input
      size.
    elapsed_time: 11.906725883483887
    model: llama-3.3-70b-versatile
    generated_at: '2026-01-15 01:09:57 '
---

## Problem #2943: Maximize Area of Square Hole in Grid

**Difficulty:** Medium

**Topics:** Array, Sorting

## Problem Description

<p>You are given the two integers, <code>n</code> and <code>m</code> and two integer arrays, <code>hBars</code> and <code>vBars</code>. The grid has <code>n + 2</code> horizontal and <code>m + 2</code> vertical bars, creating 1 x 1 unit cells. The bars are indexed starting from <code>1</code>.</p>

<p>You can <strong>remove</strong> some of the bars in <code>hBars</code> from horizontal bars and some of the bars in <code>vBars</code> from vertical bars. Note that other bars are fixed and cannot be removed.</p>

<p>Return an integer denoting the <strong>maximum area</strong> of a <em>square-shaped</em> hole in the grid, after removing some bars (possibly none).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2023/11/05/screenshot-from-2023-11-05-22-40-25.png" style="width: 411px; height: 220px;" /></p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
<p><strong>Input: </strong><span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">n = 2, m = 1, hBars = [2,3], vBars = [2]</span></p>

<p><strong>Output: </strong><span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">4</span></p>

<p><strong>Explanation:</strong></p>

<p>The left image shows the initial grid formed by the bars. The horizontal bars are <code>[1,2,3,4]</code>, and the vertical bars are&nbsp;<code>[1,2,3]</code>.</p>

<p>One way to get the maximum square-shaped hole is by removing horizontal bar 2 and vertical bar 2.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2023/11/04/screenshot-from-2023-11-04-17-01-02.png" style="width: 368px; height: 145px;" /></p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
<p><strong>Input: </strong><span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">n = 1, m = 1, hBars = [2], vBars = [2]</span></p>

<p><strong>Output: </strong><span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">4</span></p>

<p><strong>Explanation:</strong></p>

<p>To get the maximum square-shaped hole, we remove horizontal bar 2 and vertical bar 2.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/03/12/unsaved-image-2.png" style="width: 648px; height: 218px;" /></p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
<p><strong>Input: </strong><span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">n = 2, m = 3, hBars = [2,3], vBars = [2,4]</span></p>

<p><strong>Output: </strong><span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">4</span></p>

<p><strong>Explanation:</strong></p>

<p><span style="color: var(--text-secondary); font-size: 0.875rem;">One way to get the maximum square-shaped hole is by removing horizontal bar 3, and vertical bar 4.</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= m &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= hBars.length &lt;= 100</code></li>
	<li><code>2 &lt;= hBars[i] &lt;= n + 1</code></li>
	<li><code>1 &lt;= vBars.length &lt;= 100</code></li>
	<li><code>2 &lt;= vBars[i] &lt;= m + 1</code></li>
	<li>All values in <code>hBars</code> are distinct.</li>
	<li>All values in <code>vBars</code> are distinct.</li>
</ul>


## Hints

1. Sort `hBars` and `vBars` and consider them separately.

2. Compute the longest sequence of consecutive integer values in each array, denoted as `[hx, hy]` and `[vx, vy]`, respectively.

3. The maximum square length we can get is `min(hy - hx + 2, vy - vx + 2)`.

4. Square the maximum square length to get the area.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2026-01-15 22:44:43 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks for the maximum area of a square-shaped hole that can be formed by removing certain horizontal and vertical bars. A square hole of side length 'S' implies that we need to remove 'S-1' consecutive horizontal bars and 'S-1' consecutive vertical bars, such that the remaining boundary bars define an 'S' unit span. For example, to create a 1x1 hole, we need 0 bars removed, meaning the space between two fixed adjacent bars. To create a 2x2 hole, we need to remove one horizontal bar (e.g., bar 2 to open space between 1 and 3) and one vertical bar (e.g., bar 2 to open space between 1 and 3). The key insight, as suggested by the hints, is that if we have 'k' consecutive removable bars (e.g., `i, i+1, ..., i+k-1`), we can remove all of them to create an open span of `k+1` units between the fixed bars `i-1` and `i+k`. The bars `1` and `n+2` (or `m+2`) are always fixed boundaries because `hBars[i]` and `vBars[i]` are constrained to be between `2` and `n+1` (or `m+1`).

The algorithm proceeds by first determining the maximum possible side length achievable horizontally and vertically. For each set of bars (`hBars` and `vBars`), we sort the array. Then, we iterate through the sorted array to find the longest sequence of consecutive integers. If `k` is the length of the longest consecutive sequence of removable bars (e.g., `[2,3]` has length 2), then the maximum span we can create in that dimension is `k+1`. We calculate this `k+1` value for both horizontal and vertical bars. The side length of the largest square hole will be the minimum of these two maximum achievable spans. Finally, the area is the square of this side length.

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
class Solution {
public:
    int getMaxConsecutive(std::vector<int>& bars) {
        if (bars.empty()) {
            return 0; // Based on constraints, bars will not be empty.
        }
        std::sort(bars.begin(), bars.end());
        int max_consecutive = 1;
        int current_consecutive = 1;
        for (int i = 1; i < bars.size(); ++i) {
            if (bars[i] == bars[i-1] + 1) {
                current_consecutive++;
            } else {
                current_consecutive = 1;
            }
            max_consecutive = std::max(max_consecutive, current_consecutive);
        }
        return max_consecutive;
    }

    int maximizeSquareHoleArea(int n, int m, std::vector<int>& hBars, std::vector<int>& vBars) {
        int max_h = getMaxConsecutive(hBars);
        int max_v = getMaxConsecutive(vBars);
        int side_length = std::min(max_h + 1, max_v + 1);
        return side_length * side_length;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.Arrays;

class Solution {
    private int getMaxConsecutive(int[] bars) {
        if (bars.length == 0) {
            return 0; // Based on constraints, bars will not be empty.
        }
        Arrays.sort(bars);
        int maxConsecutive = 1;
        int currentConsecutive = 1;
        for (int i = 1; i < bars.length; i++) {
            if (bars[i] == bars[i-1] + 1) {
                currentConsecutive++;
            } else {
                currentConsecutive = 1;
            }
            maxConsecutive = Math.max(maxConsecutive, currentConsecutive);
        }
        return maxConsecutive;
    }

    public int maximizeSquareHoleArea(int n, int m, int[] hBars, int[] vBars) {
        int maxH = getMaxConsecutive(hBars);
        int maxV = getMaxConsecutive(vBars);
        int sideLength = Math.min(maxH + 1, maxV + 1);
        return sideLength * sideLength;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def _get_max_consecutive(self, bars):
        if not bars:
            return 0 # Based on constraints, bars will not be empty.
        bars.sort()
        max_consecutive = 1
        current_consecutive = 1
        for i in range(1, len(bars)):
            if bars[i] == bars[i-1] + 1:
                current_consecutive += 1
            else:
                current_consecutive = 1
            max_consecutive = max(max_consecutive, current_consecutive)
        return max_consecutive

    def maximizeSquareHoleArea(self, n, m, hBars, vBars):
        """
        :type n: int
        :type m: int
        :type hBars: List[int]
        :type vBars: List[int]
        :rtype: int
        """
        max_h = self._get_max_consecutive(hBars)
        max_v = self._get_max_consecutive(vBars)
        side_length = min(max_h + 1, max_v + 1)
        return side_length * side_length
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def _get_max_consecutive(self, bars: List[int]) -> int:
        if not bars:
            return 0 # Based on constraints, bars will not be empty.
        bars.sort()
        max_consecutive = 1
        current_consecutive = 1
        for i in range(1, len(bars)):
            if bars[i] == bars[i-1] + 1:
                current_consecutive += 1
            else:
                current_consecutive = 1
            max_consecutive = max(max_consecutive, current_consecutive)
        return max_consecutive

    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        max_h = self._get_max_consecutive(hBars)
        max_v = self._get_max_consecutive(vBars)
        side_length = min(max_h + 1, max_v + 1)
        return side_length * side_length
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

// Comparison function for qsort
int compareInts(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

int getMaxConsecutive(int* bars, int barsSize) {
    if (barsSize == 0) {
        return 0; // Based on constraints, bars will not be empty.
    }
    qsort(bars, barsSize, sizeof(int), compareInts);
    int max_consecutive = 1;
    int current_consecutive = 1;
    for (int i = 1; i < barsSize; i++) {
        if (bars[i] == bars[i-1] + 1) {
            current_consecutive++;
        } else {
            current_consecutive = 1;
        }
        if (current_consecutive > max_consecutive) {
            max_consecutive = current_consecutive;
        }
    }
    return max_consecutive;
}

int maximizeSquareHoleArea(int n, int m, int* hBars, int hBarsSize, int* vBars, int vBarsSize) {
    int max_h = getMaxConsecutive(hBars, hBarsSize);
    int max_v = getMaxConsecutive(vBars, vBarsSize);
    int side_length = (max_h + 1 < max_v + 1) ? (max_h + 1) : (max_v + 1);
    return side_length * side_length;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;
using System.Linq;

public class Solution {
    private int GetMaxConsecutive(int[] bars) {
        if (bars.Length == 0) {
            return 0; // Based on constraints, bars will not be empty.
        }
        Array.Sort(bars);
        int maxConsecutive = 1;
        int currentConsecutive = 1;
        for (int i = 1; i < bars.Length; i++) {
            if (bars[i] == bars[i-1] + 1) {
                currentConsecutive++;
            } else {
                currentConsecutive = 1;
            }
            maxConsecutive = Math.Max(maxConsecutive, currentConsecutive);
        }
        return maxConsecutive;
    }

    public int MaximizeSquareHoleArea(int n, int m, int[] hBars, int[] vBars) {
        int maxH = GetMaxConsecutive(hBars);
        int maxV = GetMaxConsecutive(vBars);
        int sideLength = Math.Min(maxH + 1, maxV + 1);
        return sideLength * sideLength;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number} n
 * @param {number} m
 * @param {number[]} hBars
 * @param {number[]} vBars
 * @return {number}
 */
var maximizeSquareHoleArea = function(n, m, hBars, vBars) {
    const getMaxConsecutive = (bars) => {
        if (bars.length === 0) {
            return 0; // Based on constraints, bars will not be empty.
        }
        bars.sort((a, b) => a - b);
        let maxConsecutive = 1;
        let currentConsecutive = 1;
        for (let i = 1; i < bars.length; i++) {
            if (bars[i] === bars[i-1] + 1) {
                currentConsecutive++;
            } else {
                currentConsecutive = 1;
            }
            maxConsecutive = Math.max(maxConsecutive, currentConsecutive);
        }
        return maxConsecutive;
    };

    const maxH = getMaxConsecutive(hBars);
    const maxV = getMaxConsecutive(vBars);
    const sideLength = Math.min(maxH + 1, maxV + 1);
    return sideLength * sideLength;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maximizeSquareHoleArea(n: number, m: number, hBars: number[], vBars: number[]): number {
    const getMaxConsecutive = (bars: number[]): number => {
        if (bars.length === 0) {
            return 0; // Based on constraints, bars will not be empty.
        }
        bars.sort((a, b) => a - b);
        let maxConsecutive = 1;
        let currentConsecutive = 1;
        for (let i = 1; i < bars.length; i++) {
            if (bars[i] === bars[i-1] + 1) {
                currentConsecutive++;
            } else {
                currentConsecutive = 1;
            }
            maxConsecutive = Math.max(maxConsecutive, currentConsecutive);
        }
        return maxConsecutive;
    };

    const maxH = getMaxConsecutive(hBars);
    const maxV = getMaxConsecutive(vBars);
    const sideLength = Math.min(maxH + 1, maxV + 1);
    return sideLength * sideLength;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
<?php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $m
     * @param Integer[] $hBars
     * @param Integer[] $vBars
     * @return Integer
     */
    function maximizeSquareHoleArea($n, $m, $hBars, $vBars) {
        $getMaxConsecutive = function($bars) {
            if (empty($bars)) {
                return 0; // Based on constraints, bars will not be empty.
            }
            sort($bars);
            $maxConsecutive = 1;
            $currentConsecutive = 1;
            for ($i = 1; $i < count($bars); $i++) {
                if ($bars[$i] == $bars[$i-1] + 1) {
                    $currentConsecutive++;
                } else {
                    $currentConsecutive = 1;
                }
                $maxConsecutive = max($maxConsecutive, $currentConsecutive);
            }
            return $maxConsecutive;
        };

        $maxH = $getMaxConsecutive($hBars);
        $maxV = $getMaxConsecutive($vBars);
        $sideLength = min($maxH + 1, $maxV + 1);
        return $sideLength * $sideLength;
    }
}
?>
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
import Foundation

class Solution {
    private func getMaxConsecutive(_ bars: [Int]) -> Int {
        if bars.isEmpty {
            return 0 // Based on constraints, bars will not be empty.
        }
        var sortedBars = bars.sorted()
        var maxConsecutive = 1
        var currentConsecutive = 1
        for i in 1..<sortedBars.count {
            if sortedBars[i] == sortedBars[i-1] + 1 {
                currentConsecutive += 1
            } else {
                currentConsecutive = 1
            }
            maxConsecutive = max(maxConsecutive, currentConsecutive)
        }
        return maxConsecutive
    }

    func maximizeSquareHoleArea(_ n: Int, _ m: Int, _ hBars: [Int], _ vBars: [Int]) -> Int {
        let maxH = getMaxConsecutive(hBars)
        let maxV = getMaxConsecutive(vBars)
        let sideLength = min(maxH + 1, maxV + 1)
        return sideLength * sideLength
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun maximizeSquareHoleArea(n: Int, m: Int, hBars: IntArray, vBars: IntArray): Int {
        val maxLenH = getMaxConsecutiveLength(hBars)
        val maxLenV = getMaxConsecutiveLength(vBars)

        val side = minOf(maxLenH + 1, maxLenV + 1)
        return side * side
    }

    private fun getMaxConsecutiveLength(bars: IntArray): Int {
        if (bars.isEmpty()) {
            return 0
        }

        bars.sort()
        var maxLen = 1
        var currentLen = 1

        for (i in 1 until bars.size) {
            if (bars[i] == bars[i-1] + 1) {
                currentLen++
            } else {
                currentLen = 1
            }
            maxLen = maxOf(maxLen, currentLen)
        }

        return maxLen
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int maximizeSquareHoleArea(int n, int m, List<int> hBars, List<int> vBars) {
    int maxLenH = _getMaxConsecutiveLength(hBars);
    int maxLenV = _getMaxConsecutiveLength(vBars);

    int side = (maxLenH + 1 < maxLenV + 1) ? (maxLenH + 1) : (maxLenV + 1);
    return side * side;
  }

  int _getMaxConsecutiveLength(List<int> bars) {
    if (bars.isEmpty) {
      return 0;
    }

    bars.sort();
    int maxLen = 1;
    int currentLen = 1;

    for (int i = 1; i < bars.length; i++) {
      if (bars[i] == bars[i-1] + 1) {
        currentLen++;
      } else {
        currentLen = 1;
      }
      if (currentLen > maxLen) {
        maxLen = currentLen;
      }
    }

    return maxLen;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import "sort"

func maximizeSquareHoleArea(n int, m int, hBars []int, vBars []int) int {
    maxLenH := getMaxConsecutiveLength(hBars)
    maxLenV := getMaxConsecutiveLength(vBars)

    side := min(maxLenH + 1, maxLenV + 1)
    return side * side
}

func getMaxConsecutiveLength(bars []int) int {
    if len(bars) == 0 {
        return 0
    }

    sort.Ints(bars)
    maxLen := 1
    currentLen := 1

    for i := 1; i < len(bars); i++ {
        if bars[i] == bars[i-1] + 1 {
            currentLen++
        } else {
            currentLen = 1
        }
        if currentLen > maxLen {
            maxLen = currentLen
        }
    }

    return maxLen
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer} n
# @param {Integer} m
# @param {Integer[]} h_bars
# @param {Integer[]} v_bars
# @return {Integer}
def maximize_square_hole_area(n, m, h_bars, v_bars)
    max_len_h = get_max_consecutive_length(h_bars)
    max_len_v = get_max_consecutive_length(v_bars)

    side = [max_len_h + 1, max_len_v + 1].min
    side * side
end

def get_max_consecutive_length(bars)
    return 0 if bars.empty?

    bars.sort!
    max_len = 1
    current_len = 1

    (1...bars.length).each do |i|
        if bars[i] == bars[i-1] + 1
            current_len += 1
        else
            current_len = 1
        end
        max_len = [max_len, current_len].max
    end

    max_len
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def maximizeSquareHoleArea(n: Int, m: Int, hBars: Array[Int], vBars: Array[Int]): Int = {
        val maxLenH = getMaxConsecutiveLength(hBars)
        val maxLenV = getMaxConsecutiveLength(vBars)

        val side = Math.min(maxLenH + 1, maxLenV + 1)
        side * side
    }

    private def getMaxConsecutiveLength(bars: Array[Int]): Int = {
        if (bars.isEmpty) {
            return 0
        }

        val sortedBars = bars.sorted
        var maxLen = 1
        var currentLen = 1

        for (i <- 1 until sortedBars.length) {
            if (sortedBars(i) == sortedBars(i-1) + 1) {
                currentLen += 1
            } else {
                currentLen = 1
            }
            maxLen = Math.max(maxLen, currentLen)
        }

        maxLen
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn maximize_square_hole_area(n: i32, m: i32, h_bars: Vec<i32>, v_bars: Vec<i32>) -> i32 {
        let max_len_h = Self::get_max_consecutive_length(h_bars);
        let max_len_v = Self::get_max_consecutive_length(v_bars);

        let side = std::cmp::min(max_len_h + 1, max_len_v + 1);
        side * side
    }

    fn get_max_consecutive_length(mut bars: Vec<i32>) -> i32 {
        if bars.is_empty() {
            return 0;
        }

        bars.sort_unstable();
        let mut max_len = 1;
        let mut current_len = 1;

        for i in 1..bars.len() {
            if bars[i] == bars[i-1] + 1 {
                current_len += 1;
            } else {
                current_len = 1;
            }
            max_len = std::cmp::max(max_len, current_len);
        }

        max_len
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (maximize-square-hole-area n m hBars vBars)
  (-> exact-integer? exact-integer? (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (define (get-max-consecutive-length bars)
    (if (empty? bars)
        0
        (let* ([sorted-bars (list->vector (sort bars <))]
               [len (vector-length sorted-bars)])
          (if (= len 1)
              1
              (let-values ([(max-len current-len)
                            (for/fold ([max-len 1] [current-len 1])
                                      ([i (in-range 1 len)])
                              (let ([prev-bar (vector-ref sorted-bars (- i 1))]
                                    [curr-bar (vector-ref sorted-bars i)])
                                (if (= curr-bar (+ prev-bar 1))
                                    (values (max max-len (+ current-len 1)) (+ current-len 1))
                                    (values (max max-len 1) 1))))])
                max-len))))) ; max-len is the result of the fold

  (let* ([max-len-h (get-max-consecutive-length hBars)]
         [max-len-v (get-max-consecutive-length vBars)]
         [side (+ 1 (min max-len-h max-len-v))])
    (* side side)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec maximize_square_hole_area(N :: integer(), M :: integer(), HBars :: [integer()], VBars :: [integer()]) -> integer().
maximize_square_hole_area(N, M, HBars, VBars) ->
  MaxLenH = get_max_consecutive_length(HBars),
  MaxLenV = get_max_consecutive_length(VBars),
  Side = min(MaxLenH + 1, MaxLenV + 1),
  Side * Side.

get_max_consecutive_length(Bars) ->
  case Bars of
    [] -> 0;
    _ ->
      SortedBars = lists:sort(Bars),
      get_max_consecutive_length_impl(SortedBars, 1, 1)
  end.

get_max_consecutive_length_impl([_], MaxLen, _CurrentLen) ->
  MaxLen;
get_max_consecutive_length_impl([H1, H2 | T], MaxLen, CurrentLen) ->
  if H2 == H1 + 1 ->
    NewCurrentLen = CurrentLen + 1,
    NewMaxLen = max(MaxLen, NewCurrentLen),
    get_max_consecutive_length_impl([H2 | T], NewMaxLen, NewCurrentLen);
  true ->
    NewCurrentLen = 1,
    NewMaxLen = max(MaxLen, NewCurrentLen),
    get_max_consecutive_length_impl([H2 | T], NewMaxLen, NewCurrentLen)
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec maximize_square_hole_area(n :: integer, m :: integer, h_bars :: [integer], v_bars :: [integer]) :: integer
  def maximize_square_hole_area(n, m, h_bars, v_bars) do
    max_len_h = get_max_consecutive_length(h_bars)
    max_len_v = get_max_consecutive_length(v_bars)

    side = min(max_len_h + 1, max_len_v + 1)
    side * side
  end

  defp get_max_consecutive_length(bars) do
    case bars do
      [] -> 0
      _ ->
        sorted_bars = Enum.sort(bars)
        do_get_max_consecutive_length(sorted_bars, 1, 1)
    end
  end

  defp do_get_max_consecutive_length([_], max_len, _current_len), do: max_len
  defp do_get_max_consecutive_length([h1, h2 | t], max_len, current_len) do
    if h2 == h1 + 1 do
      new_current_len = current_len + 1
      new_max_len = max(max_len, new_current_len)
      do_get_max_consecutive_length([h2 | t], new_max_len, new_current_len)
    else
      new_current_len = 1
      new_max_len = max(max_len, new_current_len)
      do_get_max_consecutive_length([h2 | t], new_max_len, new_current_len)
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is dominated by sorting the input arrays. Let `L_h` be the length of `hBars` and `L_v` be the length of `vBars`. Sorting `hBars` takes O(L_h log L_h) time, and sorting `vBars` takes O(L_v log L_v) time. After sorting, iterating through each array to find the longest consecutive sequence takes O(L_h) and O(L_v) time, respectively. Therefore, the total time complexity is O(L_h log L_h + L_v log L_v). Given that `L_h` and `L_v` are at most 100, this is very efficient.

- **Space Complexity:** The space complexity depends on the sorting algorithm used. If an in-place sort is used, the auxiliary space complexity would be O(1) (excluding the input arrays). If the sorting algorithm requires auxiliary space (e.g., Timsort used by Python's list.sort() or Scala's sorted method which creates a new array), it would be O(L_h) for `hBars` and O(L_v) for `vBars`. Thus, the total auxiliary space complexity is O(L_h + L_v) in the worst case, which is minimal given the constraints on `L_h` and `L_v`.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2026-01-15 01:09:57 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved by first sorting the hBars and vBars arrays. Then, we can find the longest sequence of consecutive integer values in each array, denoted as [hx, hy] and [vx, vy], respectively. The maximum square length we can get is min(hy - hx + 2, vy - vx + 2). Finally, we square the maximum square length to get the area. The key intuition is to consider the possible square holes that can be formed by removing some of the bars in hBars and vBars, and then find the maximum area among these possible holes.

The algorithm works by iterating over the sorted hBars and vBars arrays to find the longest sequence of consecutive integer values. We can use two pointers to track the start and end of the current sequence. If the current element is consecutive to the previous one, we move the end pointer forward. Otherwise, we update the maximum sequence length if necessary and move the start pointer forward. After finding the maximum sequence lengths for hBars and vBars, we can calculate the maximum square length and area.

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
    int maximizeSquareHoleArea(int n, int m, vector<int>& hBars, vector<int>& vBars) {
        sort(hBars.begin(), hBars.end());
        sort(vBars.begin(), vBars.end());
        int hx = hBars[0], hy = hBars[0], vx = vBars[0], vy = vBars[0];
        for (int i = 1; i < hBars.size(); i++) {
            if (hBars[i] == hBars[i-1] + 1) {
                hy = hBars[i];
            } else {
                break;
            }
        }
        for (int i = 1; i < vBars.size(); i++) {
            if (vBars[i] == vBars[i-1] + 1) {
                vy = vBars[i];
            } else {
                break;
            }
        }
        int maxLen = min(hy - hx + 2, vy - vx + 2);
        return maxLen * maxLen;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int maximizeSquareHoleArea(int n, int m, int[] hBars, int[] vBars) {
        Arrays.sort(hBars);
        Arrays.sort(vBars);
        int hx = hBars[0], hy = hBars[0], vx = vBars[0], vy = vBars[0];
        for (int i = 1; i < hBars.length; i++) {
            if (hBars[i] == hBars[i-1] + 1) {
                hy = hBars[i];
            } else {
                break;
            }
        }
        for (int i = 1; i < vBars.length; i++) {
            if (vBars[i] == vBars[i-1] + 1) {
                vy = vBars[i];
            } else {
                break;
            }
        }
        int maxLen = Math.min(hy - hx + 2, vy - vx + 2);
        return maxLen * maxLen;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def maximizeSquareHoleArea(self, n, m, hBars, vBars):
        hBars.sort()
        vBars.sort()
        hx, hy = hBars[0], hBars[0]
        vx, vy = vBars[0], vBars[0]
        for i in range(1, len(hBars)):
            if hBars[i] == hBars[i-1] + 1:
                hy = hBars[i]
            else:
                break
        for i in range(1, len(vBars)):
            if vBars[i] == vBars[i-1] + 1:
                vy = vBars[i]
            else:
                break
        maxLen = min(hy - hx + 2, vy - vx + 2)
        return maxLen * maxLen
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: list[int], vBars: list[int]) -> int:
        hBars.sort()
        vBars.sort()
        hx, hy = hBars[0], hBars[0]
        vx, vy = vBars[0], vBars[0]
        for i in range(1, len(hBars)):
            if hBars[i] == hBars[i-1] + 1:
                hy = hBars[i]
            else:
                break
        for i in range(1, len(vBars)):
            if vBars[i] == vBars[i-1] + 1:
                vy = vBars[i]
            else:
                break
        maxLen = min(hy - hx + 2, vy - vx + 2)
        return maxLen * maxLen
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int maximizeSquareHoleArea(int n, int m, int* hBars, int hBarsSize, int* vBars, int vBarsSize) {
    int hx = hBars[0], hy = hBars[0], vx = vBars[0], vy = vBars[0];
    for (int i = 1; i < hBarsSize; i++) {
        if (hBars[i] == hBars[i-1] + 1) {
            hy = hBars[i];
        } else {
            break;
        }
    }
    for (int i = 1; i < vBarsSize; i++) {
        if (vBars[i] == vBars[i-1] + 1) {
            vy = vBars[i];
        } else {
            break;
        }
    }
    int maxLen = (hy - hx + 2 < vy - vx + 2) ? hy - hx + 2 : vy - vx + 2;
    return maxLen * maxLen;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MaximizeSquareHoleArea(int n, int m, int[] hBars, int[] vBars) {
        Array.Sort(hBars);
        Array.Sort(vBars);
        int hx = hBars[0], hy = hBars[0], vx = vBars[0], vy = vBars[0];
        for (int i = 1; i < hBars.Length; i++) {
            if (hBars[i] == hBars[i-1] + 1) {
                hy = hBars[i];
            } else {
                break;
            }
        }
        for (int i = 1; i < vBars.Length; i++) {
            if (vBars[i] == vBars[i-1] + 1) {
                vy = vBars[i];
            } else {
                break;
            }
        }
        int maxLen = Math.Min(hy - hx + 2, vy - vx + 2);
        return maxLen * maxLen;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var maximizeSquareHoleArea = function(n, m, hBars, vBars) {
    hBars.sort((a, b) => a - b);
    vBars.sort((a, b) => a - b);
    let hx = hBars[0], hy = hBars[0], vx = vBars[0], vy = vBars[0];
    for (let i = 1; i < hBars.length; i++) {
        if (hBars[i] == hBars[i-1] + 1) {
            hy = hBars[i];
        } else {
            break;
        }
    }
    for (let i = 1; i < vBars.length; i++) {
        if (vBars[i] == vBars[i-1] + 1) {
            vy = vBars[i];
        } else {
            break;
        }
    }
    let maxLen = Math.min(hy - hx + 2, vy - vx + 2);
    return maxLen * maxLen;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maximizeSquareHoleArea(n: number, m: number, hBars: number[], vBars: number[]): number {
    hBars.sort((a, b) => a - b);
    vBars.sort((a, b) => a - b);
    let hx: number = hBars[0], hy: number = hBars[0], vx: number = vBars[0], vy: number = vBars[0];
    for (let i: number = 1; i < hBars.length; i++) {
        if (hBars[i] == hBars[i-1] + 1) {
            hy = hBars[i];
        } else {
            break;
        }
    }
    for (let i: number = 1; i < vBars.length; i++) {
        if (vBars[i] == vBars[i-1] + 1) {
            vy = vBars[i];
        } else {
            break;
        }
    }
    let maxLen: number = Math.min(hy - hx + 2, vy - vx + 2);
    return maxLen * maxLen;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function maximizeSquareHoleArea($n, $m, $hBars, $vBars) {
        sort($hBars);
        sort($vBars);
        $hx = $hBars[0]; $hy = $hBars[0]; $vx = $vBars[0]; $vy = $vBars[0];
        for ($i = 1; $i < count($hBars); $i++) {
            if ($hBars[$i] == $hBars[$i-1] + 1) {
                $hy = $hBars[$i];
            } else {
                break;
            }
        }
        for ($i = 1; $i < count($vBars); $i++) {
            if ($vBars[$i] == $vBars[$i-1] + 1) {
                $vy = $vBars[$i];
            } else {
                break;
            }
        }
        $maxLen = min($hy - $hx + 2, $vy - $vx + 2);
        return $maxLen * $maxLen;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func maximizeSquareHoleArea(_ n: Int, _ m: Int, _ hBars: [Int], _ vBars: [Int]) -> Int {
        let sortedHBars = hBars.sorted();
        let sortedVBars = vBars.sorted();
        var hx: Int = sortedHBars[0], hy: Int = sortedHBars[0], vx: Int = sortedVBars[0], vy: Int = sortedVBars[0];
        for i in 1..<sortedHBars.count {
            if sortedHBars[i] == sortedHBars[i-1] + 1 {
                hy = sortedHBars[i];
            } else {
                break;
            }
        }
        for i in 1..<sortedVBars.count {
            if sortedVBars[i] == sortedVBars[i-1] + 1 {
                vy = sortedVBars[i];
            } else {
                break;
            }
        }
        let maxLen = min(hy - hx + 2, vy - vx + 2);
        return maxLen * maxLen;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun maximizeSquareHoleArea(n: Int, m: Int, hBars: IntArray, vBars: IntArray): Int {
        val sortedHBars = hBars.sorted()
        val sortedVBars = vBars.sorted()
        var maxHSequence = 0
        var maxVSequence = 0
        var currentHSequence = 1
        var currentVSequence = 1
        for (i in 1 until sortedHBars.size) {
            if (sortedHBars[i] - sortedHBars[i - 1] == 1) {
                currentHSequence++
            } else {
                maxHSequence = maxOf(maxHSequence, currentHSequence)
                currentHSequence = 1
            }
        }
        maxHSequence = maxOf(maxHSequence, currentHSequence)
        for (i in 1 until sortedVBars.size) {
            if (sortedVBars[i] - sortedVBars[i - 1] == 1) {
                currentVSequence++
            } else {
                maxVSequence = maxOf(maxVSequence, currentVSequence)
                currentVSequence = 1
            }
        }
        maxVSequence = maxOf(maxVSequence, currentVSequence)
        val maxSquareLength = minOf(maxHSequence + 1, maxVSequence + 1)
        return maxSquareLength * maxSquareLength
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int maximizeSquareHoleArea(int n, int m, List<int> hBars, List<int> vBars) {
    hBars.sort();
    vBars.sort();
    int maxHSequence = 0;
    int maxVSequence = 0;
    int currentHSequence = 1;
    int currentVSequence = 1;
    for (int i = 1; i < hBars.length; i++) {
      if (hBars[i] - hBars[i - 1] == 1) {
        currentHSequence++;
      } else {
        maxHSequence = maxHSequence > currentHSequence ? maxHSequence : currentHSequence;
        currentHSequence = 1;
      }
    }
    maxHSequence = maxHSequence > currentHSequence ? maxHSequence : currentHSequence;
    for (int i = 1; i < vBars.length; i++) {
      if (vBars[i] - vBars[i - 1] == 1) {
        currentVSequence++;
      } else {
        maxVSequence = maxVSequence > currentVSequence ? maxVSequence : currentVSequence;
        currentVSequence = 1;
      }
    }
    maxVSequence = maxVSequence > currentVSequence ? maxVSequence : currentVSequence;
    int maxSquareLength = maxHSequence < maxVSequence + 1 ? maxHSequence + 1 : maxVSequence + 1;
    return maxSquareLength * maxSquareLength;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func maximizeSquareHoleArea(n int, m int, hBars []int, vBars []int) int {
    sort.Ints(hBars)
    sort.Ints(vBars)
    maxHSequence := 0
    maxVSequence := 0
    currentHSequence := 1
    currentVSequence := 1
    for i := 1; i < len(hBars); i++ {
        if hBars[i]-hBars[i-1] == 1 {
            currentHSequence++
        } else {
            if currentHSequence > maxHSequence {
                maxHSequence = currentHSequence
            }
            currentHSequence = 1
        }
    }
    if currentHSequence > maxHSequence {
        maxHSequence = currentHSequence
    }
    for i := 1; i < len(vBars); i++ {
        if vBars[i]-vBars[i-1] == 1 {
            currentVSequence++
        } else {
            if currentVSequence > maxVSequence {
                maxVSequence = currentVSequence
            }
            currentVSequence = 1
        }
    }
    if currentVSequence > maxVSequence {
        maxVSequence = currentVSequence
    }
    maxSquareLength := min(maxHSequence+1, maxVSequence+1)
    return maxSquareLength * maxSquareLength
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer} n
# @param {Integer} m
# @param {Integer[]} h_bars
# @param {Integer[]} v_bars
# @return {Integer}
def maximize_square_hole_area(n, m, h_bars, v_bars)
    h_bars.sort!
    v_bars.sort!
    max_h_sequence = 0
    max_v_sequence = 0
    current_h_sequence = 1
    current_v_sequence = 1
    (1...h_bars.size).each do |i|
        if h_bars[i] - h_bars[i - 1] == 1
            current_h_sequence += 1
        else
            max_h_sequence = [max_h_sequence, current_h_sequence].max
            current_h_sequence = 1
        end
    end
    max_h_sequence = [max_h_sequence, current_h_sequence].max
    (1...v_bars.size).each do |i|
        if v_bars[i] - v_bars[i - 1] == 1
            current_v_sequence += 1
        else
            max_v_sequence = [max_v_sequence, current_v_sequence].max
            current_v_sequence = 1
        end
    end
    max_v_sequence = [max_v_sequence, current_v_sequence].max
    max_square_length = [max_h_sequence + 1, max_v_sequence + 1].min
    max_square_length * max_square_length
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def maximizeSquareHoleArea(n: Int, m: Int, hBars: Array[Int], vBars: Array[Int]): Int = {
        val sortedHBars = hBars.sorted
        val sortedVBars = vBars.sorted
        var maxHSequence = 0
        var maxVSequence = 0
        var currentHSequence = 1
        var currentVSequence = 1
        for (i <- 1 until sortedHBars.length) {
            if (sortedHBars(i) - sortedHBars(i - 1) == 1) {
                currentHSequence += 1
            } else {
                maxHSequence = math.max(maxHSequence, currentHSequence)
                currentHSequence = 1
            }
        }
        maxHSequence = math.max(maxHSequence, currentHSequence)
        for (i <- 1 until sortedVBars.length) {
            if (sortedVBars(i) - sortedVBars(i - 1) == 1) {
                currentVSequence += 1
            } else {
                maxVSequence = math.max(maxVSequence, currentVSequence)
                currentVSequence = 1
            }
        }
        maxVSequence = math.max(maxVSequence, currentVSequence)
        val maxSquareLength = math.min(maxHSequence + 1, maxVSequence + 1)
        maxSquareLength * maxSquareLength
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn maximize_square_hole_area(n: i32, m: i32, h_bars: Vec<i32>, v_bars: Vec<i32>) -> i32 {
        let mut h_bars = h_bars;
        let mut v_bars = v_bars;
        h_bars.sort();
        v_bars.sort();
        let mut max_h_sequence = 0;
        let mut max_v_sequence = 0;
        let mut current_h_sequence = 1;
        let mut current_v_sequence = 1;
        for i in 1..h_bars.len() {
            if h_bars[i] - h_bars[i - 1] == 1 {
                current_h_sequence += 1;
            } else {
                max_h_sequence = max_h_sequence.max(current_h_sequence);
                current_h_sequence = 1;
            }
        }
        max_h_sequence = max_h_sequence.max(current_h_sequence);
        for i in 1..v_bars.len() {
            if v_bars[i] - v_bars[i - 1] == 1 {
                current_v_sequence += 1;
            } else {
                max_v_sequence = max_v_sequence.max(current_v_sequence);
                current_v_sequence = 1;
            }
        }
        max_v_sequence = max_v_sequence.max(current_v_sequence);
        let max_square_length = max_h_sequence.min(max_v_sequence) + 1;
        max_square_length * max_square_length
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (maximize-square-hole-area n m hBars vBars)
  (-> exact-integer? exact-integer? (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let* (
         (hBars (sort hBars <))
         (vBars (sort vBars <))
         (max-h-sequence 0)
         (max-v-sequence 0)
         (current-h-sequence 1)
         (current-v-sequence 1))
    (for ((i (range 1 (length hBars))))
      (if (= (- (list-ref hBars i) (list-ref hBars (- i 1))) 1)
          (set! current-h-sequence (+ current-h-sequence 1))
          (begin
            (set! max-h-sequence (max max-h-sequence current-h-sequence))
            (set! current-h-sequence 1)))))
    (set! max-h-sequence (max max-h-sequence current-h-sequence))
    (for ((i (range 1 (length vBars))))
      (if (= (- (list-ref vBars i) (list-ref vBars (- i 1))) 1)
          (set! current-v-sequence (+ current-v-sequence 1))
          (begin
            (set! max-v-sequence (max max-v-sequence current-v-sequence))
            (set! current-v-sequence 1)))))
    (set! max-v-sequence (max max-v-sequence current-v-sequence))
    (let ((max-square-length (min (+ max-h-sequence 1) (+ max-v-sequence 1))))
      (* max-square-length max-square-length))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec maximize_square_hole_area(N :: integer(), M :: integer(), HBars :: [integer()], VBars :: [integer()]) -> integer().
maximize_square_hole_area(N, M, HBars, VBars) ->
    lists:foldl(
      fun(X, {MaxH, MaxV, CurrentH, CurrentV}) ->
              case X - hd(HBars) of
                  1 -> {MaxH, MaxV, CurrentH + 1, CurrentV};
                  _ -> {max(MaxH, CurrentH), MaxV, 1, CurrentV}
              end
      end,
      {0, 0, 1, 1},
      lists:sort(HBars))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec maximize_square_hole_area(n :: integer, m :: integer, h_bars :: [integer], v_bars :: [integer]) :: integer
  def maximize_square_hole_area(n, m, h_bars, v_bars) do
    h_bars = Enum.sort(h_bars)
    v_bars = Enum.sort(v_bars)
    max_h_sequence = 0
    max_v_sequence = 0
    current_h_sequence = 1
    current_v_sequence = 1
    for i <- 1..length(h_bars) - 1 do
      if Enum.at(h_bars, i) - Enum.at(h_bars, i - 1) == 1 do
        current_h_sequence = current_h_sequence + 1
      else
        max_h_sequence = max(max_h_sequence, current_h_sequence)
        current_h_sequence = 1
      end
    end
    max_h_sequence = max(max_h_sequence, current_h_sequence)
    for i <- 1..length(v_bars) - 1 do
      if Enum.at(v_bars, i) - Enum.at(v_bars, i - 1) == 1 do
        current_v_sequence = current_v_sequence + 1
      else
        max_v_sequence = max(max_v_sequence, current_v_sequence)
        current_v_sequence = 1
      end
    end
    max_v_sequence = max(max_v_sequence, current_v_sequence)
    max_square_length = min(max_h_sequence + 1, max_v_sequence + 1)
    max_square_length * max_square_length
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of the algorithm is O(n log n + m log m), where n and m are the lengths of the hBars and vBars arrays, respectively. This is because we need to sort the arrays first, which takes O(n log n) and O(m log m) time. Then, we iterate over the sorted arrays to find the longest sequence of consecutive integer values, which takes O(n) and O(m) time. Therefore, the overall time complexity is dominated by the sorting step.

- **Space Complexity:** The space complexity of the algorithm is O(n + m), where n and m are the lengths of the hBars and vBars arrays, respectively. This is because we need to store the sorted arrays, which takes O(n) and O(m) space. We also need to store the maximum sequence lengths and the maximum square length, which takes constant space. Therefore, the overall space complexity is linear in the input size.

</div>
</details>
