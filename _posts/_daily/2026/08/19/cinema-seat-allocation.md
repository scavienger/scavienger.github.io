---
layout: post
title: "Cinema Seat Allocation"
date: 2026-08-19 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Hash Table", "Greedy", "Bit Manipulation"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/cinema-seat-allocation/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int maxNumberOfFamilies(int n, vector<vector<int>>&\
        \ reservedSeats) {\n        unordered_map<int, int> rowMasks;\n        for (const\
        \ auto& seat : reservedSeats) {\n            int row = seat[0];\n          \
        \  int col = seat[1];\n            if (col >= 2 && col <= 9) {\n           \
        \     rowMasks[row] |= (1 << (col - 2));\n            }\n        }\n\n     \
        \   long long totalGroups = (long long)(n - (int)rowMasks.size()) * 2;\n   \
        \     for (auto it = rowMasks.begin(); it != rowMasks.end(); ++it) {\n     \
        \       int mask = it->second;\n            bool leftFree = (mask & 15) == 0;\n\
        \            bool rightFree = (mask & 240) == 0;\n            bool middleFree\
        \ = (mask & 60) == 0;\n\n            if (leftFree && rightFree) {\n        \
        \        totalGroups += 2;\n            } else if (leftFree || rightFree ||\
        \ middleFree) {\n                totalGroups += 1;\n            }\n        }\n\
        \n        return (int)totalGroups;\n    }\n};"
      java: "import java.util.*;\n\nclass Solution {\n    public int maxNumberOfFamilies(int\
        \ n, int[][] reservedSeats) {\n        Map<Integer, Integer> rowMasks = new\
        \ HashMap<>();\n        for (int[] seat : reservedSeats) {\n            int\
        \ row = seat[0];\n            int col = seat[1];\n            if (col >= 2 &&\
        \ col <= 9) {\n                rowMasks.put(row, rowMasks.getOrDefault(row,\
        \ 0) | (1 << (col - 2)));\n            }\n        }\n\n        long totalGroups\
        \ = (long) (n - rowMasks.size()) * 2;\n        for (int mask : rowMasks.values())\
        \ {\n            boolean leftFree = (mask & 15) == 0;\n            boolean rightFree\
        \ = (mask & 240) == 0;\n            boolean middleFree = (mask & 60) == 0;\n\
        \n            if (leftFree && rightFree) {\n                totalGroups += 2;\n\
        \            } else if (leftFree || rightFree || middleFree) {\n           \
        \     totalGroups += 1;\n            }\n        }\n\n        return (int) totalGroups;\n\
        \    }\n}"
      python: "class Solution(object):\n    def maxNumberOfFamilies(self, n, reservedSeats):\n\
        \        \"\"\"\n        :type n: int\n        :type reservedSeats: List[List[int]]\n\
        \        :rtype: int\n        \"\"\"\n        row_masks = {}\n        for row,\
        \ col in reservedSeats:\n            if 2 <= col <= 9:\n                row_masks[row]\
        \ = row_masks.get(row, 0) | (1 << (col - 2))\n\n        total_groups = (n -\
        \ len(row_masks)) * 2\n        for mask in row_masks.values():\n           \
        \ left_free = (mask & 15) == 0\n            right_free = (mask & 240) == 0\n\
        \            mid_free = (mask & 60) == 0\n\n            if left_free and right_free:\n\
        \                total_groups += 2\n            elif left_free or right_free\
        \ or mid_free:\n                total_groups += 1\n\n        return total_groups"
      python3: "class Solution:\n    def maxNumberOfFamilies(self, n: int, reservedSeats:\
        \ List[List[int]]) -> int:\n        row_masks = {}\n        for row, col in\
        \ reservedSeats:\n            if 2 <= col <= 9:\n                row_masks[row]\
        \ = row_masks.get(row, 0) | (1 << (col - 2))\n\n        total_groups = (n -\
        \ len(row_masks)) * 2\n        for mask in row_masks.values():\n           \
        \ left_free = (mask & 15) == 0\n            right_free = (mask & 240) == 0\n\
        \            mid_free = (mask & 60) == 0\n\n            if left_free and right_free:\n\
        \                total_groups += 2\n            elif left_free or right_free\
        \ or mid_free:\n                total_groups += 1\n\n        return total_groups"
      c: "#include <stdlib.h>\n\nint compareRows(const void* a, const void* b) {\n \
        \   int* rowA = *(int**)a;\n    int* rowB = *(int**)b;\n    if (rowA[0] < rowB[0])\
        \ return -1;\n    if (rowA[0] > rowB[0]) return 1;\n    return 0;\n}\n\nint\
        \ maxNumberOfFamilies(int n, int** reservedSeats, int reservedSeatsSize, int*\
        \ reservedSeatsColSize) {\n    if (reservedSeatsSize == 0) return (int)(2L *\
        \ n);\n\n    qsort(reservedSeats, reservedSeatsSize, sizeof(int*), compareRows);\n\
        \n    long long totalGroups = 0;\n    int uniqueRowsCount = 0;\n    int i =\
        \ 0;\n\n    while (i < reservedSeatsSize) {\n        int currentRow = reservedSeats[i][0];\n\
        \        int mask = 0;\n        while (i < reservedSeatsSize && reservedSeats[i][0]\
        \ == currentRow) {\n            int seat = reservedSeats[i][1];\n          \
        \  if (seat >= 2 && seat <= 9) {\n                mask |= (1 << (seat - 2));\n\
        \            }\n            i++;\n        }\n\n        uniqueRowsCount++;\n\
        \        if ((mask & 15) == 0 && (mask & 240) == 0) {\n            totalGroups\
        \ += 2;\n        } else if ((mask & 15) == 0 || (mask & 240) == 0 || (mask &\
        \ 60) == 0) {\n            totalGroups += 1;\n        }\n    }\n\n    totalGroups\
        \ += (long long)(n - uniqueRowsCount) * 2;\n    return (int)totalGroups;\n}"
      csharp: "using System.Collections.Generic;\n\npublic class Solution {\n    public\
        \ int MaxNumberOfFamilies(int n, int[][] reservedSeats) {\n        var rowMap\
        \ = new Dictionary<int, int>();\n        foreach (var seat in reservedSeats)\
        \ {\n            int r = seat[0];\n            int c = seat[1];\n          \
        \  if (c >= 2 && c <= 9) {\n                if (!rowMap.ContainsKey(r)) {\n\
        \                    rowMap[r] = 0;\n                }\n                rowMap[r]\
        \ |= (1 << c);\n            }\n        }\n\n        long res = (long)(n - rowMap.Count)\
        \ * 2;\n        foreach (var mask in rowMap.Values) {\n            bool left\
        \ = (mask & 60) == 0;     // 1<<2 | 1<<3 | 1<<4 | 1<<5\n            bool right\
        \ = (mask & 960) == 0;   // 1<<6 | 1<<7 | 1<<8 | 1<<9\n            bool middle\
        \ = (mask & 240) == 0;  // 1<<4 | 1<<5 | 1<<6 | 1<<7\n\n            if (left\
        \ && right) {\n                res += 2;\n            } else if (left || right\
        \ || middle) {\n                res += 1;\n            }\n        }\n\n    \
        \    return (int)res;\n    }\n}"
      javascript: "/**\n * @param {number} n\n * @param {number[][]} reservedSeats\n\
        \ * @return {number}\n */\nvar maxNumberOfFamilies = function(n, reservedSeats)\
        \ {\n    const rowMap = new Map();\n    for (let i = 0; i < reservedSeats.length;\
        \ i++) {\n        const r = reservedSeats[i][0];\n        const c = reservedSeats[i][1];\n\
        \        if (c >= 2 && c <= 9) {\n            rowMap.set(r, (rowMap.get(r) ||\
        \ 0) | (1 << c));\n        }\n    }\n\n    let res = (n - rowMap.size) * 2;\n\
        \    for (const mask of rowMap.values()) {\n        const left = (mask & 60)\
        \ === 0;\n        const right = (mask & 960) === 0;\n        const middle =\
        \ (mask & 240) === 0;\n\n        if (left && right) {\n            res += 2;\n\
        \        } else if (left || right || middle) {\n            res += 1;\n    \
        \    }\n    }\n\n    return res;\n};"
      typescript: "function maxNumberOfFamilies(n: number, reservedSeats: number[][]):\
        \ number {\n    const rowMap = new Map<number, number>();\n    for (const seat\
        \ of reservedSeats) {\n        const r = seat[0];\n        const c = seat[1];\n\
        \        if (c >= 2 && c <= 9) {\n            rowMap.set(r, (rowMap.get(r) ||\
        \ 0) | (1 << c));\n        }\n    }\n\n    let res = (n - rowMap.size) * 2;\n\
        \    for (const mask of rowMap.values()) {\n        const left = (mask & 60)\
        \ === 0;\n        const right = (mask & 960) === 0;\n        const middle =\
        \ (mask & 240) === 0;\n\n        if (left && right) {\n            res += 2;\n\
        \        } else if (left || right || middle) {\n            res += 1;\n    \
        \    }\n    }\n\n    return res;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer $n\n     * @param Integer[][]\
        \ $reservedSeats\n     * @return Integer\n     */\n    function maxNumberOfFamilies($n,\
        \ $reservedSeats) {\n        $rowMap = [];\n        foreach ($reservedSeats\
        \ as $seat) {\n            $r = $seat[0];\n            $c = $seat[1];\n    \
        \        if ($c >= 2 && $c <= 9) {\n                if (!isset($rowMap[$r]))\
        \ {\n                    $rowMap[$r] = 0;\n                }\n             \
        \   $rowMap[$r] |= (1 << $c);\n            }\n        }\n\n        $res = ($n\
        \ - count($rowMap)) * 2;\n        foreach ($rowMap as $mask) {\n           \
        \ $left = ($mask & 60) === 0;\n            $right = ($mask & 960) === 0;\n \
        \           $middle = ($mask & 240) === 0;\n\n            if ($left && $right)\
        \ {\n                $res += 2;\n            } else if ($left || $right || $middle)\
        \ {\n                $res += 1;\n            }\n        }\n\n        return\
        \ $res;\n    }\n}"
      swift: "class Solution {\n    func maxNumberOfFamilies(_ n: Int, _ reservedSeats:\
        \ [[Int]]) -> Int {\n        var rowMap: [Int: Int] = [:]\n        for seat\
        \ in reservedSeats {\n            let r = seat[0]\n            let c = seat[1]\n\
        \            if c >= 2 && c <= 9 {\n                rowMap[r, default: 0] |=\
        \ (1 << c)\n            }\n        }\n\n        var res = (n - rowMap.count)\
        \ * 2\n        for mask in rowMap.values {\n            let left = (mask & 60)\
        \ == 0\n            let right = (mask & 960) == 0\n            let middle =\
        \ (mask & 240) == 0\n\n            if left && right {\n                res +=\
        \ 2\n            } else if left || right || middle {\n                res +=\
        \ 1\n            }\n        }\n\n        return res\n    }\n}"
      kotlin: "class Solution {\n    fun maxNumberOfFamilies(n: Int, reservedSeats:\
        \ Array<IntArray>): Int {\n        val rowMap = mutableMapOf<Int, Int>()\n \
        \       for (res in reservedSeats) {\n            val row = res[0]\n       \
        \     val seat = res[1]\n            if (seat in 2..9) {\n                rowMap[row]\
        \ = (rowMap[row] ?: 0) or (1 shl (seat - 1))\n            }\n        }\n\n \
        \       var total = (n - rowMap.size).toLong() * 2\n\n        for (mask in rowMap.values)\
        \ {\n            val left = (mask and 30) == 0\n            val right = (mask\
        \ and 480) == 0\n            val mid = (mask and 120) == 0\n\n            if\
        \ (left && right) {\n                total += 2\n            } else if (left\
        \ || right || mid) {\n                total += 1\n            }\n        }\n\
        \n        return total.toInt()\n    }\n}"
      dart: "class Solution {\n  int maxNumberOfFamilies(int n, List<List<int>> reservedSeats)\
        \ {\n    Map<int, int> rowMap = {};\n    for (var res in reservedSeats) {\n\
        \      int row = res[0];\n      int seat = res[1];\n      if (seat >= 2 && seat\
        \ <= 9) {\n        rowMap[row] = (rowMap[row] ?? 0) | (1 << (seat - 1));\n \
        \     }\n    }\n\n    int total = (n - rowMap.length) * 2;\n\n    for (var mask\
        \ in rowMap.values) {\n      bool left = (mask & 30) == 0;\n      bool right\
        \ = (mask & 480) == 0;\n      bool mid = (mask & 120) == 0;\n\n      if (left\
        \ && right) {\n        total += 2;\n      } else if (left || right || mid) {\n\
        \        total += 1;\n      }\n    }\n\n    return total;\n  }\n}"
      go: "func maxNumberOfFamilies(n int, reservedSeats [][]int) int {\n\trowMap :=\
        \ make(map[int]int)\n\tfor _, res := range reservedSeats {\n\t\trow, seat :=\
        \ res[0], res[1]\n\t\tif seat >= 2 && seat <= 9 {\n\t\t\trowMap[row] |= (1 <<\
        \ (seat - 1))\n\t\t}\n\t}\n\n\ttotal := (n - len(rowMap)) * 2\n\tfor _, mask\
        \ := range rowMap {\n\t\tleft := (mask & 30) == 0\n\t\tright := (mask & 480)\
        \ == 0\n\t\tmid := (mask & 120) == 0\n\n\t\tif left && right {\n\t\t\ttotal\
        \ += 2\n\t\t} else if left || right || mid {\n\t\t\ttotal += 1\n\t\t}\n\t}\n\
        \n\treturn total\n}"
      ruby: "# @param {Integer} n\n# @param {Integer[][]} reserved_seats\n# @return\
        \ {Integer}\ndef max_number_of_families(n, reserved_seats)\n  row_map = Hash.new(0)\n\
        \  reserved_seats.each do |res|\n    row, seat = res[0], res[1]\n    if seat\
        \ >= 2 && seat <= 9\n      row_map[row] |= (1 << (seat - 1))\n    end\n  end\n\
        \n  total = (n - row_map.length) * 2\n\n  row_map.each_value do |mask|\n   \
        \ left = (mask & 30) == 0\n    right = (mask & 480) == 0\n    mid = (mask &\
        \ 120) == 0\n\n    if left && right\n      total += 2\n    elsif left || right\
        \ || mid\n      total += 1\n    end\n  end\n\n  total\nend"
      scala: "import scala.collection.mutable\n\nobject Solution {\n    def maxNumberOfFamilies(n:\
        \ Int, reservedSeats: Array[Array[Int]]): Int = {\n        val rowMap = mutable.HashMap[Int,\
        \ Int]()\n        for (res <- reservedSeats) {\n            val row = res(0)\n\
        \            val seat = res(1)\n            if (seat >= 2 && seat <= 9) {\n\
        \                rowMap(row) = rowMap.getOrElse(row, 0) | (1 << (seat - 1))\n\
        \            }\n        }\n\n        var total: Long = (n.toLong - rowMap.size)\
        \ * 2\n\n        for (mask <- rowMap.values) {\n            val left = (mask\
        \ & 30) == 0\n            val right = (mask & 480) == 0\n            val mid\
        \ = (mask & 120) == 0\n\n            if (left && right) {\n                total\
        \ += 2\n            } else if (left || right || mid) {\n                total\
        \ += 1\n            }\n        }\n\n        total.toInt\n    }\n}"
      rust: "use std::collections::HashMap;\n\nimpl Solution {\n    pub fn max_number_of_families(n:\
        \ i32, reserved_seats: Vec<Vec<i32>>) -> i32 {\n        let mut row_masks: HashMap<i32,\
        \ i32> = HashMap::new();\n        for seat in reserved_seats {\n           \
        \ let row = seat[0];\n            let col = seat[1];\n            if col >=\
        \ 2 && col <= 9 {\n                let mask = row_masks.entry(row).or_insert(0);\n\
        \                *mask |= 1 << (col - 2);\n            }\n        }\n\n    \
        \    let mut count: i32 = (n - row_masks.len() as i32) * 2;\n        for mask\
        \ in row_masks.values() {\n            let left_free = (mask & 0x0F) == 0;\n\
        \            let right_free = (mask & 0xF0) == 0;\n            let mid_free\
        \ = (mask & 0x3C) == 0;\n\n            if left_free && right_free {\n      \
        \          count += 2;\n            } else if left_free || right_free || mid_free\
        \ {\n                count += 1;\n            }\n        }\n        count\n\
        \    }\n}"
      racket: "(define/contract (max-number-of-families n reservedSeats)\n  (-> exact-integer?\
        \ (listof (listof exact-integer?)) exact-integer?)\n  (let ([row-masks (make-hash)])\n\
        \    (for ([seat reservedSeats])\n      (let ([row (list-ref seat 0)]\n    \
        \        [col (list-ref seat 1)])\n        (when (and (>= col 2) (<= col 9))\n\
        \          (let ([current-mask (hash-ref row-masks row 0)])\n            (hash-set!\
        \ row-masks row (bitwise-ior current-mask (arithmetic-shift 1 (- col 2))))))))\n\
        \    (let* ([num-reserved-rows (hash-count row-masks)]\n           [initial-count\
        \ (* 2 (- n num-reserved-rows))]\n           [additional-count (hash-fold row-masks\n\
        \                                        (lambda (row mask acc)\n          \
        \                                (let ([left-free (= (bitwise-and mask #x0F)\
        \ 0)]\n                                                [right-free (= (bitwise-and\
        \ mask #xF0) 0)]\n                                                [mid-free\
        \ (= (bitwise-and mask #x3C) 0)])\n                                        \
        \    (cond\n                                              [(and left-free right-free)\
        \ (+ acc 2)]\n                                              [(or left-free right-free\
        \ mid-free) (+ acc 1)]\n                                              [else\
        \ acc])))\n                                        0)])\n      (+ initial-count\
        \ additional-count))))"
      erlang: "-spec max_number_of_families(N :: integer(), ReservedSeats :: [[integer()]])\
        \ -> integer().\nmax_number_of_families(N, ReservedSeats) ->\n    RowMasks =\
        \ lists:foldl(fun([Row, Col], Acc) ->\n        if Col >= 2, Col =< 9 ->\n  \
        \          CurrentMask = maps:get(Row, Acc, 0),\n            maps:put(Row, CurrentMask\
        \ bor (1 bsl (Col - 2)), Acc);\n        true -> Acc\n        end\n    end, #{},\
        \ ReservedSeats),\n    NumReservedRows = maps:size(RowMasks),\n    InitialCount\
        \ = (N - NumReservedRows) * 2,\n    maps:fold(fun(_Row, Mask, Acc) ->\n    \
        \    LeftFree = (Mask band 16#0F) == 0,\n        RightFree = (Mask band 16#F0)\
        \ == 0,\n        MidFree = (Mask band 16#3C) == 0,\n        if\n           \
        \ LeftFree andalso RightFree -> Acc + 2;\n            LeftFree orelse RightFree\
        \ orelse MidFree -> Acc + 1;\n            true -> Acc\n        end\n    end,\
        \ InitialCount, RowMasks)."
      elixir: "defmodule Solution do\n  require Bitwise\n\n  @spec max_number_of_families(n\
        \ :: integer, reserved_seats :: [[integer]]) :: integer\n  def max_number_of_families(n,\
        \ reserved_seats) do\n    row_masks = Enum.reduce(reserved_seats, %{}, fn [row,\
        \ col], acc ->\n      if col >= 2 and col <= 9 do\n        current_mask = Map.get(acc,\
        \ row, 0)\n        Map.put(acc, row, Bitwise.bor(current_mask, Bitwise.bsl(1,\
        \ col - 2)))\n      else\n        acc\n      end\n    end)\n\n    num_reserved_rows\
        \ = Map.size(row_masks)\n    initial_count = (n - num_reserved_rows) * 2\n\n\
        \    Enum.reduce(row_masks, initial_count, fn {_row, mask}, acc ->\n      left_free\
        \ = Bitwise.band(mask, 0x0F) == 0\n      right_free = Bitwise.band(mask, 0xF0)\
        \ == 0\n      mid_free = Bitwise.band(mask, 0x3C) == 0\n\n      cond do\n  \
        \      left_free and right_free -> acc + 2\n        left_free or right_free\
        \ or mid_free -> acc + 1\n        true -> acc\n      end\n    end)\n  end\n\
        end"
    approach: 'The problem asks for the maximum number of four-person groups that can
      be seated in a cinema. Each row has three possible four-person blocks: seats (2,
      3, 4, 5), (6, 7, 8, 9), and a middle block (4, 5, 6, 7). A row can fit two groups
      if both the left (2-5) and right (6-9) blocks are free. If that is not possible,
      we can fit at most one group if any of the three blocks are entirely unreserved.
      Since the total number of rows $n$ can reach $10^9$, we only process rows explicitly
      mentioned in the reservations and assume all other rows can accommodate two groups.


      To efficiently check for available blocks, we use a bitmask for each row to represent
      the occupancy of seats 2 through 9 (eight seats in total). We iterate through
      the reserved seats to construct these masks. For each row with at least one reservation,
      we check the occupancy of the three target blocks using bitwise AND operations
      with pre-defined masks: 15 (bits 0-3 for seats 2-5), 240 (bits 4-7 for seats 6-9),
      and 60 (bits 2-5 for seats 4-7). We greedily count 2 groups if both side blocks
      are free, otherwise 1 group if any of the three blocks are free.'
    time_complexity: O(M \log M) or O(M) where M is the number of reserved seats. In
      Python, Java, and C++, a hash map approach takes O(M) time to store reservations
      and O(M) time to iterate over unique rows. In C, sorting the reservations by row
      takes O(M \log M) time followed by a single O(M) pass.
    space_complexity: O(M) space. In the worst case, every reservation belongs to a
      unique row, requiring space in the hash map (or sorting array) proportional to
      the number of reserved seats.
    elapsed_time: 253.71212148666382
    model: gemini-3-flash-preview
    generated_at: '2026-08-19 00:51:02 '
---

## Problem #1386: Cinema Seat Allocation

**Difficulty:** Medium

**Topics:** Array, Hash Table, Greedy, Bit Manipulation

## Problem Description

<p><img alt="" src="https://assets.leetcode.com/uploads/2020/02/14/cinema_seats_1.png" style="width: 400px; height: 149px;" /></p>

<p>A cinema has <code>n</code> rows of seats, numbered from 1 to <code>n</code>. Each row has 10 seats, numbered from 1 to 10.</p>

<p>You are given a 2D integer array <code data-end="170" data-start="155">reservedSeats</code>, where <code data-end="212" data-start="178">reservedSeats[i] = [row<sub>i</sub>, seat<sub>i</sub>]</code> means that seat <code data-end="236" data-start="229">seat<sub>i</sub></code> in row <code data-end="250" data-start="244">row<sub>i</sub></code> is already reserved.</p>

<p>A four-person group must be assigned to four seats in the <strong>same</strong> row. The group can be seated in one of the following seat blocks:</p>

<ul>
	<li>seats <code data-end="423" data-start="411">2, 3, 4, 5</code></li>
	<li>seats <code data-end="444" data-start="432">4, 5, 6, 7</code></li>
	<li>seats <code data-end="465" data-start="453">6, 7, 8, 9</code></li>
</ul>

<p>A block can be used only if <strong>none</strong> of its seats are reserved. Each seat can be assigned to <strong>at most </strong>one group.</p>

<p>Return an integer denoting the <strong>maximum</strong> number of four-person groups that can be assigned.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2020/02/14/cinema_seats_3.png" style="width: 400px; height: 96px;" /></p>

<pre>
<strong>Input:</strong> n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The figure above shows an optimal allocation of four groups. Seats marked in blue are already reserved, and each set of four contiguous seats marked in orange is assigned to one group.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 2, reservedSeats = [[2,1],[1,8],[2,6]]
<strong>Output:</strong> 2
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 4, reservedSeats = [[4,3],[1,4],[4,6],[1,7]]
<strong>Output:</strong> 4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= reservedSeats.length &lt;= min(10 * n, 10<sup>4</sup>)</code></li>
	<li><code>reservedSeats[i] == [row<sub>i</sub>, seat<sub>i</sub>]</code></li>
	<li><code>1 &lt;= row<sub>i</sub> &lt;= n</code></li>
	<li><code>1 &lt;= seat<sub>i</sub> &lt;= 10</code></li>
	<li>All <code>reservedSeats[i]</code> are distinct.</li>
</ul>


## Hints

1. Note you can allocate at most two four-person groups in one row.

2. Greedily check if you can allocate seats for two groups, one group or none.

3. Process only rows that appear in the input, for other rows you can always allocate seats for two groups.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks for the maximum number of four-person groups that can be seated in a cinema. Each row has three possible four-person blocks: seats (2, 3, 4, 5), (6, 7, 8, 9), and a middle block (4, 5, 6, 7). A row can fit two groups if both the left (2-5) and right (6-9) blocks are free. If that is not possible, we can fit at most one group if any of the three blocks are entirely unreserved. Since the total number of rows $n$ can reach $10^9$, we only process rows explicitly mentioned in the reservations and assume all other rows can accommodate two groups.

To efficiently check for available blocks, we use a bitmask for each row to represent the occupancy of seats 2 through 9 (eight seats in total). We iterate through the reserved seats to construct these masks. For each row with at least one reservation, we check the occupancy of the three target blocks using bitwise AND operations with pre-defined masks: 15 (bits 0-3 for seats 2-5), 240 (bits 4-7 for seats 6-9), and 60 (bits 2-5 for seats 4-7). We greedily count 2 groups if both side blocks are free, otherwise 1 group if any of the three blocks are free.

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
    int maxNumberOfFamilies(int n, vector<vector<int>>& reservedSeats) {
        unordered_map<int, int> rowMasks;
        for (const auto& seat : reservedSeats) {
            int row = seat[0];
            int col = seat[1];
            if (col >= 2 && col <= 9) {
                rowMasks[row] |= (1 << (col - 2));
            }
        }

        long long totalGroups = (long long)(n - (int)rowMasks.size()) * 2;
        for (auto it = rowMasks.begin(); it != rowMasks.end(); ++it) {
            int mask = it->second;
            bool leftFree = (mask & 15) == 0;
            bool rightFree = (mask & 240) == 0;
            bool middleFree = (mask & 60) == 0;

            if (leftFree && rightFree) {
                totalGroups += 2;
            } else if (leftFree || rightFree || middleFree) {
                totalGroups += 1;
            }
        }

        return (int)totalGroups;
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
    public int maxNumberOfFamilies(int n, int[][] reservedSeats) {
        Map<Integer, Integer> rowMasks = new HashMap<>();
        for (int[] seat : reservedSeats) {
            int row = seat[0];
            int col = seat[1];
            if (col >= 2 && col <= 9) {
                rowMasks.put(row, rowMasks.getOrDefault(row, 0) | (1 << (col - 2)));
            }
        }

        long totalGroups = (long) (n - rowMasks.size()) * 2;
        for (int mask : rowMasks.values()) {
            boolean leftFree = (mask & 15) == 0;
            boolean rightFree = (mask & 240) == 0;
            boolean middleFree = (mask & 60) == 0;

            if (leftFree && rightFree) {
                totalGroups += 2;
            } else if (leftFree || rightFree || middleFree) {
                totalGroups += 1;
            }
        }

        return (int) totalGroups;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        row_masks = {}
        for row, col in reservedSeats:
            if 2 <= col <= 9:
                row_masks[row] = row_masks.get(row, 0) | (1 << (col - 2))

        total_groups = (n - len(row_masks)) * 2
        for mask in row_masks.values():
            left_free = (mask & 15) == 0
            right_free = (mask & 240) == 0
            mid_free = (mask & 60) == 0

            if left_free and right_free:
                total_groups += 2
            elif left_free or right_free or mid_free:
                total_groups += 1

        return total_groups
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        row_masks = {}
        for row, col in reservedSeats:
            if 2 <= col <= 9:
                row_masks[row] = row_masks.get(row, 0) | (1 << (col - 2))

        total_groups = (n - len(row_masks)) * 2
        for mask in row_masks.values():
            left_free = (mask & 15) == 0
            right_free = (mask & 240) == 0
            mid_free = (mask & 60) == 0

            if left_free and right_free:
                total_groups += 2
            elif left_free or right_free or mid_free:
                total_groups += 1

        return total_groups
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>

int compareRows(const void* a, const void* b) {
    int* rowA = *(int**)a;
    int* rowB = *(int**)b;
    if (rowA[0] < rowB[0]) return -1;
    if (rowA[0] > rowB[0]) return 1;
    return 0;
}

int maxNumberOfFamilies(int n, int** reservedSeats, int reservedSeatsSize, int* reservedSeatsColSize) {
    if (reservedSeatsSize == 0) return (int)(2L * n);

    qsort(reservedSeats, reservedSeatsSize, sizeof(int*), compareRows);

    long long totalGroups = 0;
    int uniqueRowsCount = 0;
    int i = 0;

    while (i < reservedSeatsSize) {
        int currentRow = reservedSeats[i][0];
        int mask = 0;
        while (i < reservedSeatsSize && reservedSeats[i][0] == currentRow) {
            int seat = reservedSeats[i][1];
            if (seat >= 2 && seat <= 9) {
                mask |= (1 << (seat - 2));
            }
            i++;
        }

        uniqueRowsCount++;
        if ((mask & 15) == 0 && (mask & 240) == 0) {
            totalGroups += 2;
        } else if ((mask & 15) == 0 || (mask & 240) == 0 || (mask & 60) == 0) {
            totalGroups += 1;
        }
    }

    totalGroups += (long long)(n - uniqueRowsCount) * 2;
    return (int)totalGroups;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System.Collections.Generic;

public class Solution {
    public int MaxNumberOfFamilies(int n, int[][] reservedSeats) {
        var rowMap = new Dictionary<int, int>();
        foreach (var seat in reservedSeats) {
            int r = seat[0];
            int c = seat[1];
            if (c >= 2 && c <= 9) {
                if (!rowMap.ContainsKey(r)) {
                    rowMap[r] = 0;
                }
                rowMap[r] |= (1 << c);
            }
        }

        long res = (long)(n - rowMap.Count) * 2;
        foreach (var mask in rowMap.Values) {
            bool left = (mask & 60) == 0;     // 1<<2 | 1<<3 | 1<<4 | 1<<5
            bool right = (mask & 960) == 0;   // 1<<6 | 1<<7 | 1<<8 | 1<<9
            bool middle = (mask & 240) == 0;  // 1<<4 | 1<<5 | 1<<6 | 1<<7

            if (left && right) {
                res += 2;
            } else if (left || right || middle) {
                res += 1;
            }
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
/**
 * @param {number} n
 * @param {number[][]} reservedSeats
 * @return {number}
 */
var maxNumberOfFamilies = function(n, reservedSeats) {
    const rowMap = new Map();
    for (let i = 0; i < reservedSeats.length; i++) {
        const r = reservedSeats[i][0];
        const c = reservedSeats[i][1];
        if (c >= 2 && c <= 9) {
            rowMap.set(r, (rowMap.get(r) || 0) | (1 << c));
        }
    }

    let res = (n - rowMap.size) * 2;
    for (const mask of rowMap.values()) {
        const left = (mask & 60) === 0;
        const right = (mask & 960) === 0;
        const middle = (mask & 240) === 0;

        if (left && right) {
            res += 2;
        } else if (left || right || middle) {
            res += 1;
        }
    }

    return res;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maxNumberOfFamilies(n: number, reservedSeats: number[][]): number {
    const rowMap = new Map<number, number>();
    for (const seat of reservedSeats) {
        const r = seat[0];
        const c = seat[1];
        if (c >= 2 && c <= 9) {
            rowMap.set(r, (rowMap.get(r) || 0) | (1 << c));
        }
    }

    let res = (n - rowMap.size) * 2;
    for (const mask of rowMap.values()) {
        const left = (mask & 60) === 0;
        const right = (mask & 960) === 0;
        const middle = (mask & 240) === 0;

        if (left && right) {
            res += 2;
        } else if (left || right || middle) {
            res += 1;
        }
    }

    return res;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $reservedSeats
     * @return Integer
     */
    function maxNumberOfFamilies($n, $reservedSeats) {
        $rowMap = [];
        foreach ($reservedSeats as $seat) {
            $r = $seat[0];
            $c = $seat[1];
            if ($c >= 2 && $c <= 9) {
                if (!isset($rowMap[$r])) {
                    $rowMap[$r] = 0;
                }
                $rowMap[$r] |= (1 << $c);
            }
        }

        $res = ($n - count($rowMap)) * 2;
        foreach ($rowMap as $mask) {
            $left = ($mask & 60) === 0;
            $right = ($mask & 960) === 0;
            $middle = ($mask & 240) === 0;

            if ($left && $right) {
                $res += 2;
            } else if ($left || $right || $middle) {
                $res += 1;
            }
        }

        return $res;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func maxNumberOfFamilies(_ n: Int, _ reservedSeats: [[Int]]) -> Int {
        var rowMap: [Int: Int] = [:]
        for seat in reservedSeats {
            let r = seat[0]
            let c = seat[1]
            if c >= 2 && c <= 9 {
                rowMap[r, default: 0] |= (1 << c)
            }
        }

        var res = (n - rowMap.count) * 2
        for mask in rowMap.values {
            let left = (mask & 60) == 0
            let right = (mask & 960) == 0
            let middle = (mask & 240) == 0

            if left && right {
                res += 2
            } else if left || right || middle {
                res += 1
            }
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
    fun maxNumberOfFamilies(n: Int, reservedSeats: Array<IntArray>): Int {
        val rowMap = mutableMapOf<Int, Int>()
        for (res in reservedSeats) {
            val row = res[0]
            val seat = res[1]
            if (seat in 2..9) {
                rowMap[row] = (rowMap[row] ?: 0) or (1 shl (seat - 1))
            }
        }

        var total = (n - rowMap.size).toLong() * 2

        for (mask in rowMap.values) {
            val left = (mask and 30) == 0
            val right = (mask and 480) == 0
            val mid = (mask and 120) == 0

            if (left && right) {
                total += 2
            } else if (left || right || mid) {
                total += 1
            }
        }

        return total.toInt()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int maxNumberOfFamilies(int n, List<List<int>> reservedSeats) {
    Map<int, int> rowMap = {};
    for (var res in reservedSeats) {
      int row = res[0];
      int seat = res[1];
      if (seat >= 2 && seat <= 9) {
        rowMap[row] = (rowMap[row] ?? 0) | (1 << (seat - 1));
      }
    }

    int total = (n - rowMap.length) * 2;

    for (var mask in rowMap.values) {
      bool left = (mask & 30) == 0;
      bool right = (mask & 480) == 0;
      bool mid = (mask & 120) == 0;

      if (left && right) {
        total += 2;
      } else if (left || right || mid) {
        total += 1;
      }
    }

    return total;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func maxNumberOfFamilies(n int, reservedSeats [][]int) int {
	rowMap := make(map[int]int)
	for _, res := range reservedSeats {
		row, seat := res[0], res[1]
		if seat >= 2 && seat <= 9 {
			rowMap[row] |= (1 << (seat - 1))
		}
	}

	total := (n - len(rowMap)) * 2
	for _, mask := range rowMap {
		left := (mask & 30) == 0
		right := (mask & 480) == 0
		mid := (mask & 120) == 0

		if left && right {
			total += 2
		} else if left || right || mid {
			total += 1
		}
	}

	return total
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer} n
# @param {Integer[][]} reserved_seats
# @return {Integer}
def max_number_of_families(n, reserved_seats)
  row_map = Hash.new(0)
  reserved_seats.each do |res|
    row, seat = res[0], res[1]
    if seat >= 2 && seat <= 9
      row_map[row] |= (1 << (seat - 1))
    end
  end

  total = (n - row_map.length) * 2

  row_map.each_value do |mask|
    left = (mask & 30) == 0
    right = (mask & 480) == 0
    mid = (mask & 120) == 0

    if left && right
      total += 2
    elsif left || right || mid
      total += 1
    end
  end

  total
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.collection.mutable

object Solution {
    def maxNumberOfFamilies(n: Int, reservedSeats: Array[Array[Int]]): Int = {
        val rowMap = mutable.HashMap[Int, Int]()
        for (res <- reservedSeats) {
            val row = res(0)
            val seat = res(1)
            if (seat >= 2 && seat <= 9) {
                rowMap(row) = rowMap.getOrElse(row, 0) | (1 << (seat - 1))
            }
        }

        var total: Long = (n.toLong - rowMap.size) * 2

        for (mask <- rowMap.values) {
            val left = (mask & 30) == 0
            val right = (mask & 480) == 0
            val mid = (mask & 120) == 0

            if (left && right) {
                total += 2
            } else if (left || right || mid) {
                total += 1
            }
        }

        total.toInt
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
    pub fn max_number_of_families(n: i32, reserved_seats: Vec<Vec<i32>>) -> i32 {
        let mut row_masks: HashMap<i32, i32> = HashMap::new();
        for seat in reserved_seats {
            let row = seat[0];
            let col = seat[1];
            if col >= 2 && col <= 9 {
                let mask = row_masks.entry(row).or_insert(0);
                *mask |= 1 << (col - 2);
            }
        }

        let mut count: i32 = (n - row_masks.len() as i32) * 2;
        for mask in row_masks.values() {
            let left_free = (mask & 0x0F) == 0;
            let right_free = (mask & 0xF0) == 0;
            let mid_free = (mask & 0x3C) == 0;

            if left_free && right_free {
                count += 2;
            } else if left_free || right_free || mid_free {
                count += 1;
            }
        }
        count
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (max-number-of-families n reservedSeats)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  (let ([row-masks (make-hash)])
    (for ([seat reservedSeats])
      (let ([row (list-ref seat 0)]
            [col (list-ref seat 1)])
        (when (and (>= col 2) (<= col 9))
          (let ([current-mask (hash-ref row-masks row 0)])
            (hash-set! row-masks row (bitwise-ior current-mask (arithmetic-shift 1 (- col 2))))))))
    (let* ([num-reserved-rows (hash-count row-masks)]
           [initial-count (* 2 (- n num-reserved-rows))]
           [additional-count (hash-fold row-masks
                                        (lambda (row mask acc)
                                          (let ([left-free (= (bitwise-and mask #x0F) 0)]
                                                [right-free (= (bitwise-and mask #xF0) 0)]
                                                [mid-free (= (bitwise-and mask #x3C) 0)])
                                            (cond
                                              [(and left-free right-free) (+ acc 2)]
                                              [(or left-free right-free mid-free) (+ acc 1)]
                                              [else acc])))
                                        0)])
      (+ initial-count additional-count))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec max_number_of_families(N :: integer(), ReservedSeats :: [[integer()]]) -> integer().
max_number_of_families(N, ReservedSeats) ->
    RowMasks = lists:foldl(fun([Row, Col], Acc) ->
        if Col >= 2, Col =< 9 ->
            CurrentMask = maps:get(Row, Acc, 0),
            maps:put(Row, CurrentMask bor (1 bsl (Col - 2)), Acc);
        true -> Acc
        end
    end, #{}, ReservedSeats),
    NumReservedRows = maps:size(RowMasks),
    InitialCount = (N - NumReservedRows) * 2,
    maps:fold(fun(_Row, Mask, Acc) ->
        LeftFree = (Mask band 16#0F) == 0,
        RightFree = (Mask band 16#F0) == 0,
        MidFree = (Mask band 16#3C) == 0,
        if
            LeftFree andalso RightFree -> Acc + 2;
            LeftFree orelse RightFree orelse MidFree -> Acc + 1;
            true -> Acc
        end
    end, InitialCount, RowMasks).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  require Bitwise

  @spec max_number_of_families(n :: integer, reserved_seats :: [[integer]]) :: integer
  def max_number_of_families(n, reserved_seats) do
    row_masks = Enum.reduce(reserved_seats, %{}, fn [row, col], acc ->
      if col >= 2 and col <= 9 do
        current_mask = Map.get(acc, row, 0)
        Map.put(acc, row, Bitwise.bor(current_mask, Bitwise.bsl(1, col - 2)))
      else
        acc
      end
    end)

    num_reserved_rows = Map.size(row_masks)
    initial_count = (n - num_reserved_rows) * 2

    Enum.reduce(row_masks, initial_count, fn {_row, mask}, acc ->
      left_free = Bitwise.band(mask, 0x0F) == 0
      right_free = Bitwise.band(mask, 0xF0) == 0
      mid_free = Bitwise.band(mask, 0x3C) == 0

      cond do
        left_free and right_free -> acc + 2
        left_free or right_free or mid_free -> acc + 1
        true -> acc
      end
    end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(M \log M) or O(M) where M is the number of reserved seats. In Python, Java, and C++, a hash map approach takes O(M) time to store reservations and O(M) time to iterate over unique rows. In C, sorting the reservations by row takes O(M \log M) time followed by a single O(M) pass.
- **Space Complexity:** O(M) space. In the worst case, every reservation belongs to a unique row, requiring space in the hash map (or sorting array) proportional to the number of reserved seats.
