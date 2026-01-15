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
      cpp: "class Solution {\npublic:\n    int getMaxConsecutiveLength(std::vector<int>&\
        \ bars) {\n        if (bars.empty()) {\n            return 0;\n        }\n \
        \       std::sort(bars.begin(), bars.end());\n        int max_len = 1;\n   \
        \     int current_len = 1;\n        for (int i = 1; i < bars.size(); ++i) {\n\
        \            if (bars[i] == bars[i-1] + 1) {\n                current_len++;\n\
        \            } else {\n                max_len = std::max(max_len, current_len);\n\
        \                current_len = 1;\n            }\n        }\n        max_len\
        \ = std::max(max_len, current_len);\n        return max_len;\n    }\n\n    int\
        \ maximizeSquareHoleArea(int n, int m, std::vector<int>& hBars, std::vector<int>&\
        \ vBars) {\n        int h_max_len = getMaxConsecutiveLength(hBars);\n      \
        \  int v_max_len = getMaxConsecutiveLength(vBars);\n\n        int side = std::min(h_max_len\
        \ + 1, v_max_len + 1);\n        return side * side;\n    }\n};"
      java: "import java.util.Arrays;\n\nclass Solution {\n    private int getMaxConsecutiveLength(int[]\
        \ bars) {\n        if (bars == null || bars.length == 0) {\n            return\
        \ 0;\n        }\n        Arrays.sort(bars);\n        int max_len = 1;\n    \
        \    int current_len = 1;\n        for (int i = 1; i < bars.length; i++) {\n\
        \            if (bars[i] == bars[i-1] + 1) {\n                current_len++;\n\
        \            } else {\n                max_len = Math.max(max_len, current_len);\n\
        \                current_len = 1;\n            }\n        }\n        max_len\
        \ = Math.max(max_len, current_len);\n        return max_len;\n    }\n\n    public\
        \ int maximizeSquareHoleArea(int n, int m, int[] hBars, int[] vBars) {\n   \
        \     int h_max_len = getMaxConsecutiveLength(hBars);\n        int v_max_len\
        \ = getMaxConsecutiveLength(vBars);\n\n        int side = Math.min(h_max_len\
        \ + 1, v_max_len + 1);\n        return side * side;\n    }\n}"
      python: "# Failed to parse response\n# Check logs for full output.\n# Full Response:\n\
        '''\n{\n  \"approach\": \"The problem asks for the maximum area of a square-shaped\
        \ hole that can be created by removing some horizontal bars from `hBars` and\
        \ some vertical bars from `vBars`. The key insight, guided by the problem's\
        \ hints and examples, is to understand how removing a sequence of consecutive\
        \ bars creates a larger gap. If we remove `L` consecutive horizontal bars (e.g.,\
        \ `i, i+1, ..., i+L-1`), this creates a hole of height `L+1` units. This hole\
        \ is bounded by the fixed horizontal bars `i-1` and `i+L`, which are guaranteed\
        \ to be present because `hBars` only contains indices between `2` and `n+1`,\
        \ meaning `1` and `n+2` are never in `hBars` and thus always fixed. Similarly,\
        \ removing `L'` consecutive vertical bars creates a hole of width `L'+1` units.\"\
        ,\n  \"time_complexity\": \"The time complexity is dominated by sorting the\
        \ `hBars` and `vBars` arrays. Let `L_h` be the length of `hBars` and `L_v` be\
        \ the length of `vBars`. Sorting takes `O(L_h log L_h)` and `O(L_v log L_v)`\
        \ respectively. After sorting, iterating through each array to find the longest\
        \ consecutive sequence takes `O(L_h)` and `O(L_v)` time. Since `L_h` and `L_v`\
        \ are at most 100, this is very efficient. The overall time complexity is `O(L_h\
        \ log L_h + L_v log L_v)`.\",\n  \"space_complexity\": \"The space complexity\
        \ is `O(L_h + L_v)` if the sorting algorithm used requires auxiliary space proportional\
        \ to the input size. If an in-place sorting algorithm is used, the space complexity\
        \ would be `O(1)` (or `O(log L)` for the recursion stack in some quicksort implementations),\
        \ ignoring the space for the input arrays themselves. Given the constraints\
        \ (maximum length of 100 for `hBars` and `vBars`), the space usage is minimal.\"\
        \n}\n'''"
      python3: "from typing import List\n\nclass Solution:\n    def _get_max_consecutive_length(self,\
        \ bars: List[int]) -> int:\n        if not bars:\n            return 0\n\n \
        \       bars.sort()\n\n        max_len = 1\n        current_len = 1\n\n    \
        \    for i in range(1, len(bars)):\n            if bars[i] == bars[i-1] + 1:\n\
        \                current_len += 1\n            else:\n                max_len\
        \ = max(max_len, current_len)\n                current_len = 1\n\n        max_len\
        \ = max(max_len, current_len) # Check the last sequence\n        return max_len\n\
        \n    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars:\
        \ List[int]) -> int:\n        h_max_len = self._get_max_consecutive_length(hBars)\n\
        \        v_max_len = self._get_max_consecutive_length(vBars)\n\n        side\
        \ = min(h_max_len + 1, v_max_len + 1)\n        return side * side"
      c: "#include <stdlib.h> // For qsort\n\n// Comparison function for qsort\nint\
        \ compareInts(const void *a, const void *b) {\n    return (*(int*)a - *(int*)b);\n\
        }\n\nint getMaxConsecutiveLength(int* bars, int barsSize) {\n    if (barsSize\
        \ == 0) {\n        return 0;\n    }\n\n    qsort(bars, barsSize, sizeof(int),\
        \ compareInts);\n\n    int max_len = 1;\n    int current_len = 1;\n\n    for\
        \ (int i = 1; i < barsSize; ++i) {\n        if (bars[i] == bars[i-1] + 1) {\n\
        \            current_len++;\n        } else {\n            if (current_len >\
        \ max_len) {\n                max_len = current_len;\n            }\n      \
        \      current_len = 1;\n        }\n    }\n    // After loop, check the last\
        \ sequence\n    if (current_len > max_len) {\n        max_len = current_len;\n\
        \    }\n    return max_len;\n}\n\nint maximizeSquareHoleArea(int n, int m, int*\
        \ hBars, int hBarsSize, int* vBars, int vBarsSize) {\n    int h_max_len = getMaxConsecutiveLength(hBars,\
        \ hBarsSize);\n    int v_max_len = getMaxConsecutiveLength(vBars, vBarsSize);\n\
        \n    int side_h = h_max_len + 1;\n    int side_v = v_max_len + 1;\n\n    int\
        \ side = (side_h < side_v) ? side_h : side_v; // Equivalent to min(side_h, side_v)\n\
        \    return side * side;\n}"
      csharp: "using System;\nusing System.Linq;\n\npublic class Solution {\n    private\
        \ int GetMaxConsecutiveLength(int[] bars) {\n        if (bars == null || bars.Length\
        \ == 0) {\n            return 0;\n        }\n        Array.Sort(bars);\n   \
        \     int max_len = 1;\n        int current_len = 1;\n        for (int i = 1;\
        \ i < bars.Length; i++) {\n            if (bars[i] == bars[i-1] + 1) {\n   \
        \             current_len++;\n            } else {\n                max_len\
        \ = Math.Max(max_len, current_len);\n                current_len = 1;\n    \
        \        }\n        }\n        max_len = Math.Max(max_len, current_len);\n \
        \       return max_len;\n    }\n\n    public int MaximizeSquareHoleArea(int\
        \ n, int m, int[] hBars, int[] vBars) {\n        int h_max_len = GetMaxConsecutiveLength(hBars);\n\
        \        int v_max_len = GetMaxConsecutiveLength(vBars);\n\n        int side\
        \ = Math.Min(h_max_len + 1, v_max_len + 1);\n        return side * side;\n \
        \   }\n}"
      javascript: "/**\n * @param {number[]} bars\n * @return {number}\n */\nfunction\
        \ getMaxConsecutiveLength(bars) {\n    if (!bars || bars.length === 0) {\n \
        \       return 0;\n    }\n    bars.sort((a, b) => a - b);\n    let max_len =\
        \ 1;\n    let current_len = 1;\n    for (let i = 1; i < bars.length; i++) {\n\
        \        if (bars[i] === bars[i-1] + 1) {\n            current_len++;\n    \
        \    } else {\n            max_len = Math.max(max_len, current_len);\n     \
        \       current_len = 1;\n        }\n    }\n    max_len = Math.max(max_len,\
        \ current_len);\n    return max_len;\n}\n\n/**\n * @param {number} n\n * @param\
        \ {number} m\n * @param {number[]} hBars\n * @param {number[]} vBars\n * @return\
        \ {number}\n */\nvar maximizeSquareHoleArea = function(n, m, hBars, vBars) {\n\
        \    let h_max_len = getMaxConsecutiveLength(hBars);\n    let v_max_len = getMaxConsecutiveLength(vBars);\n\
        \n    let side = Math.min(h_max_len + 1, v_max_len + 1);\n    return side *\
        \ side;\n};"
      typescript: "function getMaxConsecutiveLength(bars: number[]): number {\n    if\
        \ (!bars || bars.length === 0) {\n        return 0;\n    }\n    bars.sort((a,\
        \ b) => a - b);\n    let max_len = 1;\n    let current_len = 1;\n    for (let\
        \ i = 1; i < bars.length; i++) {\n        if (bars[i] === bars[i-1] + 1) {\n\
        \            current_len++;\n        } else {\n            max_len = Math.max(max_len,\
        \ current_len);\n            current_len = 1;\n        }\n    }\n    max_len\
        \ = Math.max(max_len, current_len);\n    return max_len;\n}\n\nfunction maximizeSquareHoleArea(n:\
        \ number, m: number, hBars: number[], vBars: number[]): number {\n    let h_max_len\
        \ = getMaxConsecutiveLength(hBars);\n    let v_max_len = getMaxConsecutiveLength(vBars);\n\
        \n    let side = Math.min(h_max_len + 1, v_max_len + 1);\n    return side *\
        \ side;\n};"
      php: "<?php\nclass Solution {\n\n    /**\n     * @param Integer[] $bars\n    \
        \ * @return Integer\n     */\n    private function getMaxConsecutiveLength(array\
        \ $bars): int {\n        if (empty($bars)) {\n            return 0;\n      \
        \  }\n        sort($bars);\n        $max_len = 1;\n        $current_len = 1;\n\
        \        for ($i = 1; $i < count($bars); $i++) {\n            if ($bars[$i]\
        \ === $bars[$i-1] + 1) {\n                $current_len++;\n            } else\
        \ {\n                $max_len = max($max_len, $current_len);\n             \
        \   $current_len = 1;\n            }\n        }\n        $max_len = max($max_len,\
        \ $current_len);\n        return $max_len;\n    }\n\n    /**\n     * @param\
        \ Integer $n\n     * @param Integer $m\n     * @param Integer[] $hBars\n   \
        \  * @param Integer[] $vBars\n     * @return Integer\n     */\n    function\
        \ maximizeSquareHoleArea($n, $m, $hBars, $vBars) {\n        $h_max_len = $this->getMaxConsecutiveLength($hBars);\n\
        \        $v_max_len = $this->getMaxConsecutiveLength($vBars);\n\n        $side\
        \ = min($h_max_len + 1, $v_max_len + 1);\n        return $side * $side;\n  \
        \  }\n}\n?>"
      swift: "import Foundation\n\nclass Solution {\n    private func getMaxConsecutiveLength(_\
        \ bars: [Int]) -> Int {\n        if bars.isEmpty {\n            return 0\n \
        \       }\n        var sortedBars = bars.sorted()\n        var max_len = 1\n\
        \        var current_len = 1\n        for i in 1..<sortedBars.count {\n    \
        \        if sortedBars[i] == sortedBars[i-1] + 1 {\n                current_len\
        \ += 1\n            } else {\n                max_len = max(max_len, current_len)\n\
        \                current_len = 1\n            }\n        }\n        max_len\
        \ = max(max_len, current_len)\n        return max_len\n    }\n\n    func maximizeSquareHoleArea(_\
        \ n: Int, _ m: Int, _ hBars: [Int], _ vBars: [Int]) -> Int {\n        let h_max_len\
        \ = getMaxConsecutiveLength(hBars)\n        let v_max_len = getMaxConsecutiveLength(vBars)\n\
        \n        let side = min(h_max_len + 1, v_max_len + 1)\n        return side\
        \ * side\n    }\n}"
    approach: 'The problem asks for the maximum area of a square hole, which implies
      finding the maximum possible side length S such that a square of side S can be
      formed. A square hole of side S requires S+1 horizontal bars and S+1 vertical
      bars to define its boundaries. To achieve this, S-1 intermediate horizontal bars
      must be removable and removed, and similarly, S-1 intermediate vertical bars must
      be removable and removed. The bars 1 and n+2 (for horizontal) and 1 and m+2 (for
      vertical) are always fixed. Any other bar k not present in hBars or vBars is also
      fixed.


      The core idea is to determine the maximum number of consecutive removable bars
      in both the horizontal and vertical dimensions. For hBars, we first sort the array.
      Then, we iterate through the sorted array to find the longest sequence of consecutive
      integers. For example, if hBars = [2,3,4], the longest consecutive sequence has
      length 3. If hBars = [2,4,5], the longest consecutive sequence is [4,5] with length
      2. Let this maximum length be max_len_h. This max_len_h represents the number
      of intermediate horizontal bars that can be removed. These max_len_h removed bars
      create a gap of max_len_h + 1 units. We apply the same logic to vBars to find
      max_len_v, which allows for a vertical gap of max_len_v + 1 units. The maximum
      side length S of a square hole is then the minimum of these two possible side
      lengths: min(max_len_h + 1, max_len_v + 1). The final answer is S * S.'
    time_complexity: The time complexity is dominated by sorting the input arrays hBars
      and vBars. Let L_h be the length of hBars and L_v be the length of vBars. Sorting
      takes O(L_h log L_h) for hBars and O(L_v log L_v) for vBars. After sorting, iterating
      through each array to find the longest consecutive sequence takes O(L_h) and O(L_v)
      respectively. Therefore, the total time complexity is O(L_h log L_h + L_v log
      L_v). Given L_h, L_v <= 100, this is very efficient.
    space_complexity: The space complexity depends primarily on the sorting algorithm
      used. If an in-place sort (like C++ std::sort or Java's Arrays.sort for primitives)
      is used, the auxiliary space complexity is O(log L) due to recursion stack depth.
      If a sort requiring auxiliary space (like Python's Timsort or Java's Arrays.sort
      for objects) is used, it can be O(L). In either case, L is L_h or L_v. Additionally,
      a few constant variables are used. Thus, the overall space complexity is O(L_h
      + L_v) in the worst case for auxiliary space, or O(log L_h + log L_v) for in-place
      sorts. Considering L_h, L_v <= 100, this is very small.
    elapsed_time: 103.42253494262695
    model: gemini-2.5-flash
    generated_at: '2026-01-15 01:09:40 '
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
  <small class="solution-timestamp">(2026-01-15 01:09:40 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks for the maximum area of a square hole, which implies finding the maximum possible side length S such that a square of side S can be formed. A square hole of side S requires S+1 horizontal bars and S+1 vertical bars to define its boundaries. To achieve this, S-1 intermediate horizontal bars must be removable and removed, and similarly, S-1 intermediate vertical bars must be removable and removed. The bars 1 and n+2 (for horizontal) and 1 and m+2 (for vertical) are always fixed. Any other bar k not present in hBars or vBars is also fixed.

The core idea is to determine the maximum number of consecutive removable bars in both the horizontal and vertical dimensions. For hBars, we first sort the array. Then, we iterate through the sorted array to find the longest sequence of consecutive integers. For example, if hBars = [2,3,4], the longest consecutive sequence has length 3. If hBars = [2,4,5], the longest consecutive sequence is [4,5] with length 2. Let this maximum length be max_len_h. This max_len_h represents the number of intermediate horizontal bars that can be removed. These max_len_h removed bars create a gap of max_len_h + 1 units. We apply the same logic to vBars to find max_len_v, which allows for a vertical gap of max_len_v + 1 units. The maximum side length S of a square hole is then the minimum of these two possible side lengths: min(max_len_h + 1, max_len_v + 1). The final answer is S * S.

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
  </div>

  <div class="tab-panel" data-lang="cpp">

{% highlight cpp %}
{% raw %}
class Solution {
public:
    int getMaxConsecutiveLength(std::vector<int>& bars) {
        if (bars.empty()) {
            return 0;
        }
        std::sort(bars.begin(), bars.end());
        int max_len = 1;
        int current_len = 1;
        for (int i = 1; i < bars.size(); ++i) {
            if (bars[i] == bars[i-1] + 1) {
                current_len++;
            } else {
                max_len = std::max(max_len, current_len);
                current_len = 1;
            }
        }
        max_len = std::max(max_len, current_len);
        return max_len;
    }

    int maximizeSquareHoleArea(int n, int m, std::vector<int>& hBars, std::vector<int>& vBars) {
        int h_max_len = getMaxConsecutiveLength(hBars);
        int v_max_len = getMaxConsecutiveLength(vBars);

        int side = std::min(h_max_len + 1, v_max_len + 1);
        return side * side;
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
    private int getMaxConsecutiveLength(int[] bars) {
        if (bars == null || bars.length == 0) {
            return 0;
        }
        Arrays.sort(bars);
        int max_len = 1;
        int current_len = 1;
        for (int i = 1; i < bars.length; i++) {
            if (bars[i] == bars[i-1] + 1) {
                current_len++;
            } else {
                max_len = Math.max(max_len, current_len);
                current_len = 1;
            }
        }
        max_len = Math.max(max_len, current_len);
        return max_len;
    }

    public int maximizeSquareHoleArea(int n, int m, int[] hBars, int[] vBars) {
        int h_max_len = getMaxConsecutiveLength(hBars);
        int v_max_len = getMaxConsecutiveLength(vBars);

        int side = Math.min(h_max_len + 1, v_max_len + 1);
        return side * side;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
# Failed to parse response
# Check logs for full output.
# Full Response:
'''
{
  "approach": "The problem asks for the maximum area of a square-shaped hole that can be created by removing some horizontal bars from `hBars` and some vertical bars from `vBars`. The key insight, guided by the problem's hints and examples, is to understand how removing a sequence of consecutive bars creates a larger gap. If we remove `L` consecutive horizontal bars (e.g., `i, i+1, ..., i+L-1`), this creates a hole of height `L+1` units. This hole is bounded by the fixed horizontal bars `i-1` and `i+L`, which are guaranteed to be present because `hBars` only contains indices between `2` and `n+1`, meaning `1` and `n+2` are never in `hBars` and thus always fixed. Similarly, removing `L'` consecutive vertical bars creates a hole of width `L'+1` units.",
  "time_complexity": "The time complexity is dominated by sorting the `hBars` and `vBars` arrays. Let `L_h` be the length of `hBars` and `L_v` be the length of `vBars`. Sorting takes `O(L_h log L_h)` and `O(L_v log L_v)` respectively. After sorting, iterating through each array to find the longest consecutive sequence takes `O(L_h)` and `O(L_v)` time. Since `L_h` and `L_v` are at most 100, this is very efficient. The overall time complexity is `O(L_h log L_h + L_v log L_v)`.",
  "space_complexity": "The space complexity is `O(L_h + L_v)` if the sorting algorithm used requires auxiliary space proportional to the input size. If an in-place sorting algorithm is used, the space complexity would be `O(1)` (or `O(log L)` for the recursion stack in some quicksort implementations), ignoring the space for the input arrays themselves. Given the constraints (maximum length of 100 for `hBars` and `vBars`), the space usage is minimal."
}
'''
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
from typing import List

class Solution:
    def _get_max_consecutive_length(self, bars: List[int]) -> int:
        if not bars:
            return 0

        bars.sort()

        max_len = 1
        current_len = 1

        for i in range(1, len(bars)):
            if bars[i] == bars[i-1] + 1:
                current_len += 1
            else:
                max_len = max(max_len, current_len)
                current_len = 1

        max_len = max(max_len, current_len) # Check the last sequence
        return max_len

    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        h_max_len = self._get_max_consecutive_length(hBars)
        v_max_len = self._get_max_consecutive_length(vBars)

        side = min(h_max_len + 1, v_max_len + 1)
        return side * side
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h> // For qsort

// Comparison function for qsort
int compareInts(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

int getMaxConsecutiveLength(int* bars, int barsSize) {
    if (barsSize == 0) {
        return 0;
    }

    qsort(bars, barsSize, sizeof(int), compareInts);

    int max_len = 1;
    int current_len = 1;

    for (int i = 1; i < barsSize; ++i) {
        if (bars[i] == bars[i-1] + 1) {
            current_len++;
        } else {
            if (current_len > max_len) {
                max_len = current_len;
            }
            current_len = 1;
        }
    }
    // After loop, check the last sequence
    if (current_len > max_len) {
        max_len = current_len;
    }
    return max_len;
}

int maximizeSquareHoleArea(int n, int m, int* hBars, int hBarsSize, int* vBars, int vBarsSize) {
    int h_max_len = getMaxConsecutiveLength(hBars, hBarsSize);
    int v_max_len = getMaxConsecutiveLength(vBars, vBarsSize);

    int side_h = h_max_len + 1;
    int side_v = v_max_len + 1;

    int side = (side_h < side_v) ? side_h : side_v; // Equivalent to min(side_h, side_v)
    return side * side;
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
    private int GetMaxConsecutiveLength(int[] bars) {
        if (bars == null || bars.Length == 0) {
            return 0;
        }
        Array.Sort(bars);
        int max_len = 1;
        int current_len = 1;
        for (int i = 1; i < bars.Length; i++) {
            if (bars[i] == bars[i-1] + 1) {
                current_len++;
            } else {
                max_len = Math.Max(max_len, current_len);
                current_len = 1;
            }
        }
        max_len = Math.Max(max_len, current_len);
        return max_len;
    }

    public int MaximizeSquareHoleArea(int n, int m, int[] hBars, int[] vBars) {
        int h_max_len = GetMaxConsecutiveLength(hBars);
        int v_max_len = GetMaxConsecutiveLength(vBars);

        int side = Math.Min(h_max_len + 1, v_max_len + 1);
        return side * side;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[]} bars
 * @return {number}
 */
function getMaxConsecutiveLength(bars) {
    if (!bars || bars.length === 0) {
        return 0;
    }
    bars.sort((a, b) => a - b);
    let max_len = 1;
    let current_len = 1;
    for (let i = 1; i < bars.length; i++) {
        if (bars[i] === bars[i-1] + 1) {
            current_len++;
        } else {
            max_len = Math.max(max_len, current_len);
            current_len = 1;
        }
    }
    max_len = Math.max(max_len, current_len);
    return max_len;
}

/**
 * @param {number} n
 * @param {number} m
 * @param {number[]} hBars
 * @param {number[]} vBars
 * @return {number}
 */
var maximizeSquareHoleArea = function(n, m, hBars, vBars) {
    let h_max_len = getMaxConsecutiveLength(hBars);
    let v_max_len = getMaxConsecutiveLength(vBars);

    let side = Math.min(h_max_len + 1, v_max_len + 1);
    return side * side;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function getMaxConsecutiveLength(bars: number[]): number {
    if (!bars || bars.length === 0) {
        return 0;
    }
    bars.sort((a, b) => a - b);
    let max_len = 1;
    let current_len = 1;
    for (let i = 1; i < bars.length; i++) {
        if (bars[i] === bars[i-1] + 1) {
            current_len++;
        } else {
            max_len = Math.max(max_len, current_len);
            current_len = 1;
        }
    }
    max_len = Math.max(max_len, current_len);
    return max_len;
}

function maximizeSquareHoleArea(n: number, m: number, hBars: number[], vBars: number[]): number {
    let h_max_len = getMaxConsecutiveLength(hBars);
    let v_max_len = getMaxConsecutiveLength(vBars);

    let side = Math.min(h_max_len + 1, v_max_len + 1);
    return side * side;
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
     * @param Integer[] $bars
     * @return Integer
     */
    private function getMaxConsecutiveLength(array $bars): int {
        if (empty($bars)) {
            return 0;
        }
        sort($bars);
        $max_len = 1;
        $current_len = 1;
        for ($i = 1; $i < count($bars); $i++) {
            if ($bars[$i] === $bars[$i-1] + 1) {
                $current_len++;
            } else {
                $max_len = max($max_len, $current_len);
                $current_len = 1;
            }
        }
        $max_len = max($max_len, $current_len);
        return $max_len;
    }

    /**
     * @param Integer $n
     * @param Integer $m
     * @param Integer[] $hBars
     * @param Integer[] $vBars
     * @return Integer
     */
    function maximizeSquareHoleArea($n, $m, $hBars, $vBars) {
        $h_max_len = $this->getMaxConsecutiveLength($hBars);
        $v_max_len = $this->getMaxConsecutiveLength($vBars);

        $side = min($h_max_len + 1, $v_max_len + 1);
        return $side * $side;
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
    private func getMaxConsecutiveLength(_ bars: [Int]) -> Int {
        if bars.isEmpty {
            return 0
        }
        var sortedBars = bars.sorted()
        var max_len = 1
        var current_len = 1
        for i in 1..<sortedBars.count {
            if sortedBars[i] == sortedBars[i-1] + 1 {
                current_len += 1
            } else {
                max_len = max(max_len, current_len)
                current_len = 1
            }
        }
        max_len = max(max_len, current_len)
        return max_len
    }

    func maximizeSquareHoleArea(_ n: Int, _ m: Int, _ hBars: [Int], _ vBars: [Int]) -> Int {
        let h_max_len = getMaxConsecutiveLength(hBars)
        let v_max_len = getMaxConsecutiveLength(vBars)

        let side = min(h_max_len + 1, v_max_len + 1)
        return side * side
    }
}
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is dominated by sorting the input arrays hBars and vBars. Let L_h be the length of hBars and L_v be the length of vBars. Sorting takes O(L_h log L_h) for hBars and O(L_v log L_v) for vBars. After sorting, iterating through each array to find the longest consecutive sequence takes O(L_h) and O(L_v) respectively. Therefore, the total time complexity is O(L_h log L_h + L_v log L_v). Given L_h, L_v <= 100, this is very efficient.

- **Space Complexity:** The space complexity depends primarily on the sorting algorithm used. If an in-place sort (like C++ std::sort or Java's Arrays.sort for primitives) is used, the auxiliary space complexity is O(log L) due to recursion stack depth. If a sort requiring auxiliary space (like Python's Timsort or Java's Arrays.sort for objects) is used, it can be O(L). In either case, L is L_h or L_v. Additionally, a few constant variables are used. Thus, the overall space complexity is O(L_h + L_v) in the worst case for auxiliary space, or O(log L_h + log L_v) for in-place sorts. Considering L_h, L_v <= 100, this is very small.

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
