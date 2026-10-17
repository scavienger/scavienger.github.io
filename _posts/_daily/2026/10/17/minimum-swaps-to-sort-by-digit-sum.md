---
layout: post
title: "Minimum Swaps to Sort by Digit Sum"
date: 2026-10-17 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Hash Table", "Sorting"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/
ai_solutions:
  - solutions:
      cpp: "#include <vector>\n#include <algorithm>\n#include <numeric>\n\nusing namespace\
        \ std;\n\nclass Solution {\npublic:\n    int minSwaps(vector<int>& nums) {\n\
        \        int n = nums.size();\n        struct Node {\n            int val;\n\
        \            int sum;\n            int originalIdx;\n        };\n\n        auto\
        \ getDigitSum = [](int num) {\n            int s = 0;\n            while (num\
        \ > 0) {\n                s += num % 10;\n                num /= 10;\n     \
        \       }\n            return s;\n        };\n\n        vector<Node> nodes(n);\n\
        \        for (int i = 0; i < n; ++i) {\n            nodes[i] = {nums[i], getDigitSum(nums[i]),\
        \ i};\n        }\n\n        sort(nodes.begin(), nodes.end(), [](const Node&\
        \ a, const Node& b) {\n            if (a.sum != b.sum) return a.sum < b.sum;\n\
        \            return a.val < b.val;\n        });\n\n        vector<int> p(n);\n\
        \        for (int i = 0; i < n; ++i) {\n            p[i] = nodes[i].originalIdx;\n\
        \        }\n\n        vector<bool> visited(n, false);\n        int totalSwaps\
        \ = 0;\n        for (int i = 0; i < n; ++i) {\n            if (visited[i]) continue;\n\
        \n            int curr = i;\n            int cycleSize = 0;\n            while\
        \ (!visited[curr]) {\n                visited[curr] = true;\n              \
        \  curr = p[curr];\n                cycleSize++;\n            }\n          \
        \  if (cycleSize > 1) {\n                totalSwaps += (cycleSize - 1);\n  \
        \          }\n        }\n\n        return totalSwaps;\n    }\n};"
      java: "import java.util.Arrays;\nimport java.util.Comparator;\n\nclass Solution\
        \ {\n    static class Node {\n        int val;\n        int sum;\n        int\
        \ originalIdx;\n\n        Node(int val, int sum, int originalIdx) {\n      \
        \      this.val = val;\n            this.sum = sum;\n            this.originalIdx\
        \ = originalIdx;\n        }\n    }\n\n    public int minSwaps(int[] nums) {\n\
        \        int n = nums.length;\n        Node[] nodes = new Node[n];\n       \
        \ for (int i = 0; i < n; i++) {\n            int s = 0;\n            int temp\
        \ = nums[i];\n            while (temp > 0) {\n                s += temp % 10;\n\
        \                temp /= 10;\n            }\n            nodes[i] = new Node(nums[i],\
        \ s, i);\n        }\n\n        Arrays.sort(nodes, (a, b) -> {\n            if\
        \ (a.sum != b.sum) return Integer.compare(a.sum, b.sum);\n            return\
        \ Integer.compare(a.val, b.val);\n        });\n\n        int[] p = new int[n];\n\
        \        for (int i = 0; i < n; i++) {\n            p[i] = nodes[i].originalIdx;\n\
        \        }\n\n        boolean[] visited = new boolean[n];\n        int totalSwaps\
        \ = 0;\n        for (int i = 0; i < n; i++) {\n            if (visited[i]) continue;\n\
        \n            int curr = i;\n            int cycleSize = 0;\n            while\
        \ (!visited[curr]) {\n                visited[curr] = true;\n              \
        \  curr = p[curr];\n                cycleSize++;\n            }\n          \
        \  if (cycleSize > 1) {\n                totalSwaps += (cycleSize - 1);\n  \
        \          }\n        }\n\n        return totalSwaps;\n    }\n}"
      python: "class Solution(object):\n    def minSwaps(self, nums):\n        \"\"\"\
        \n        :type nums: List[int]\n        :rtype: int\n        \"\"\"\n     \
        \   def get_digit_sum(n):\n            s = 0\n            while n > 0:\n   \
        \             s += n % 10\n                n //= 10\n            return s\n\n\
        \        n = len(nums)\n        arr = []\n        for i in xrange(n):\n    \
        \        arr.append((get_digit_sum(nums[i]), nums[i], i))\n\n        arr.sort()\n\
        \n        p = [x[2] for x in arr]\n        visited = [False] * n\n        total_swaps\
        \ = 0\n\n        for i in xrange(n):\n            if visited[i]:\n         \
        \       continue\n\n            curr = i\n            cycle_size = 0\n     \
        \       while not visited[curr]:\n                visited[curr] = True\n   \
        \             curr = p[curr]\n                cycle_size += 1\n\n          \
        \  if cycle_size > 1:\n                total_swaps += (cycle_size - 1)\n\n \
        \       return total_swaps"
      python3: "from typing import List\n\nclass Solution:\n    def minSwaps(self, nums:\
        \ List[int]) -> int:\n        def get_digit_sum(n):\n            s = 0\n   \
        \         while n > 0:\n                s += n % 10\n                n //= 10\n\
        \            return s\n\n        n = len(nums)\n        # Create tuples of (digit_sum,\
        \ value, original_index)\n        # Sorting will automatically use sum as primary\
        \ and value as secondary.\n        arr = sorted([(get_digit_sum(nums[i]), nums[i],\
        \ i) for i in range(n)])\n\n        p = [x[2] for x in arr]\n        visited\
        \ = [False] * n\n        total_swaps = 0\n\n        for i in range(n):\n   \
        \         if visited[i]:\n                continue\n\n            curr = i\n\
        \            cycle_size = 0\n            while not visited[curr]:\n        \
        \        visited[curr] = True\n                curr = p[curr]\n            \
        \    cycle_size += 1\n\n            if cycle_size > 1:\n                total_swaps\
        \ += (cycle_size - 1)\n\n        return total_swaps"
      c: "#include <stdlib.h>\n\ntypedef struct {\n    int val;\n    int sum;\n    int\
        \ originalIdx;\n} Node;\n\nint getSum(int n) {\n    int s = 0;\n    while (n\
        \ > 0) {\n        s += n % 10;\n        n /= 10;\n    }\n    return s;\n}\n\n\
        int compareNodes(const void* a, const void* b) {\n    Node* n1 = (Node*)a;\n\
        \    Node* n2 = (Node*)b;\n    if (n1->sum != n2->sum) return n1->sum - n2->sum;\n\
        \    if (n1->val < n2->val) return -1;\n    if (n1->val > n2->val) return 1;\n\
        \    return 0;\n}\n\nint minSwaps(int* nums, int numsSize) {\n    Node* arr\
        \ = (Node*)malloc(sizeof(Node) * numsSize);\n    for (int i = 0; i < numsSize;\
        \ i++) {\n        arr[i].val = nums[i];\n        arr[i].sum = getSum(nums[i]);\n\
        \        arr[i].originalIdx = i;\n    }\n\n    qsort(arr, numsSize, sizeof(Node),\
        \ compareNodes);\n\n    int* p = (int*)malloc(sizeof(int) * numsSize);\n   \
        \ for (int i = 0; i < numsSize; i++) {\n        p[i] = arr[i].originalIdx;\n\
        \    }\n\n    char* visited = (char*)calloc(numsSize, sizeof(char));\n    int\
        \ totalSwaps = 0;\n    for (int i = 0; i < numsSize; i++) {\n        if (visited[i])\
        \ continue;\n\n        int curr = i;\n        int cycleSize = 0;\n        while\
        \ (!visited[curr]) {\n            visited[curr] = 1;\n            curr = p[curr];\n\
        \            cycleSize++;\n        }\n        if (cycleSize > 1) {\n       \
        \     totalSwaps += (cycleSize - 1);\n        }\n    }\n\n    free(arr);\n \
        \   free(p);\n    free(visited);\n    return totalSwaps;\n}"
      csharp: "public class Solution {\n    public int MinSwaps(int[] nums) {\n    \
        \    int n = nums.Length;\n        (int s, int v, int i)[] items = new (int\
        \ s, int v, int i)[n];\n        for (int k = 0; k < n; k++) {\n            int\
        \ sum = 0, temp = nums[k];\n            while (temp > 0) {\n               \
        \ sum += temp % 10;\n                temp /= 10;\n            }\n          \
        \  items[k] = (sum, nums[k], k);\n        }\n\n        System.Array.Sort(items,\
        \ (a, b) => {\n            if (a.s != b.s) return a.s.CompareTo(b.s);\n    \
        \        return a.v.CompareTo(b.v);\n        });\n\n        int[] p = new int[n];\n\
        \        for (int k = 0; k < n; k++) {\n            p[items[k].i] = k;\n   \
        \     }\n\n        bool[] visited = new bool[n];\n        int cycles = 0;\n\
        \        for (int k = 0; k < n; k++) {\n            if (!visited[k]) {\n   \
        \             cycles++;\n                int curr = k;\n                while\
        \ (!visited[curr]) {\n                    visited[curr] = true;\n          \
        \          curr = p[curr];\n                }\n            }\n        }\n  \
        \      return n - cycles;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @return {number}\n */\nvar minSwaps\
        \ = function(nums) {\n    const n = nums.length;\n    const items = new Array(n);\n\
        \    for (let i = 0; i < n; i++) {\n        let s = 0, temp = nums[i];\n   \
        \     while (temp > 0) {\n            s += temp % 10;\n            temp = Math.floor(temp\
        \ / 10);\n        }\n        items[i] = { s, v: nums[i], i };\n    }\n\n   \
        \ items.sort((a, b) => a.s - b.s || a.v - b.v);\n\n    const p = new Int32Array(n);\n\
        \    for (let i = 0; i < n; i++) {\n        p[items[i].i] = i;\n    }\n\n  \
        \  let cycles = 0;\n    const visited = new Uint8Array(n);\n    for (let i =\
        \ 0; i < n; i++) {\n        if (!visited[i]) {\n            cycles++;\n    \
        \        let curr = i;\n            while (!visited[curr]) {\n             \
        \   visited[curr] = 1;\n                curr = p[curr];\n            }\n   \
        \     }\n    }\n    return n - cycles;\n};"
      typescript: "function minSwaps(nums: number[]): number {\n    const n = nums.length;\n\
        \    const items: { s: number, v: number, i: number }[] = new Array(n);\n  \
        \  for (let i = 0; i < n; i++) {\n        let s = 0, temp = nums[i];\n     \
        \   while (temp > 0) {\n            s += temp % 10;\n            temp = Math.floor(temp\
        \ / 10);\n        }\n        items[i] = { s, v: nums[i], i };\n    }\n\n   \
        \ items.sort((a, b) => a.s - b.s || a.v - b.v);\n\n    const p = new Int32Array(n);\n\
        \    for (let i = 0; i < n; i++) {\n        p[items[i].i] = i;\n    }\n\n  \
        \  let cycles = 0;\n    const visited = new Uint8Array(n);\n    for (let i =\
        \ 0; i < n; i++) {\n        if (visited[i] === 0) {\n            cycles++;\n\
        \            let curr = i;\n            while (visited[curr] === 0) {\n    \
        \            visited[curr] = 1;\n                curr = p[curr];\n         \
        \   }\n        }\n    }\n    return n - cycles;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @return\
        \ Integer\n     */\n    function minSwaps($nums) {\n        $n = count($nums);\n\
        \        $items = [];\n        for ($i = 0; $i < $n; $i++) {\n            $s\
        \ = 0;\n            $temp = $nums[$i];\n            while ($temp > 0) {\n  \
        \              $s += $temp % 10;\n                $temp = intdiv($temp, 10);\n\
        \            }\n            $items[] = ['s' => $s, 'v' => $nums[$i], 'i' =>\
        \ $i];\n        }\n\n        usort($items, function($a, $b) {\n            if\
        \ ($a['s'] !== $b['s']) return $a['s'] <=> $b['s'];\n            return $a['v']\
        \ <=> $b['v'];\n        });\n\n        $p = array_fill(0, $n, 0);\n        for\
        \ ($i = 0; $i < $n; $i++) {\n            $p[$items[$i]['i']] = $i;\n       \
        \ }\n\n        $visited = array_fill(0, $n, false);\n        $cycles = 0;\n\
        \        for ($i = 0; $i < $n; $i++) {\n            if (!$visited[$i]) {\n \
        \               $cycles++;\n                $curr = $i;\n                while\
        \ (!$visited[$curr]) {\n                    $visited[$curr] = true;\n      \
        \              $curr = $p[$curr];\n                }\n            }\n      \
        \  }\n        return $n - $cycles;\n    }\n}"
      swift: "class Solution {\n    func minSwaps(_ nums: [Int]) -> Int {\n        let\
        \ n = nums.count\n        struct Item {\n            let s: Int\n          \
        \  let v: Int\n            let i: Int\n        }\n        var items: [Item]\
        \ = []\n        items.reserveCapacity(n)\n        for k in 0..<n {\n       \
        \     var sum = 0\n            var temp = nums[k]\n            while temp >\
        \ 0 {\n                sum += temp % 10\n                temp /= 10\n      \
        \      }\n            items.append(Item(s: sum, v: nums[k], i: k))\n       \
        \ }\n\n        items.sort { a, b in\n            if a.s != b.s { return a.s\
        \ < b.s }\n            return a.v < b.v\n        }\n\n        var p = [Int](repeating:\
        \ 0, count: n)\n        for k in 0..<n {\n            p[items[k].i] = k\n  \
        \      }\n\n        var visited = [Bool](repeating: false, count: n)\n     \
        \   var cycles = 0\n        for k in 0..<n {\n            if !visited[k] {\n\
        \                cycles += 1\n                var curr = k\n               \
        \ while !visited[curr] {\n                    visited[curr] = true\n       \
        \             curr = p[curr]\n                }\n            }\n        }\n\
        \        return n - cycles\n    }\n}"
      kotlin: "class Solution {\n    fun minSwaps(nums: IntArray): Int {\n        val\
        \ n = nums.size\n        val items = Array(n) { i ->\n            var sum =\
        \ 0\n            var temp = nums[i]\n            while (temp > 0) {\n      \
        \          sum += temp % 10\n                temp /= 10\n            }\n   \
        \         Triple(sum, nums[i], i)\n        }\n\n        items.sortWith(Comparator\
        \ { a, b ->\n            if (a.first != b.first) a.first.compareTo(b.first)\n\
        \            else a.second.compareTo(b.second)\n        })\n\n        val targetPos\
        \ = IntArray(n)\n        for (i in 0 until n) {\n            targetPos[items[i].third]\
        \ = i\n        }\n\n        var swaps = 0\n        val visited = BooleanArray(n)\n\
        \        for (i in 0 until n) {\n            if (visited[i] || targetPos[i]\
        \ == i) continue\n\n            var cycleSize = 0\n            var curr = i\n\
        \            while (!visited[curr]) {\n                visited[curr] = true\n\
        \                curr = targetPos[curr]\n                cycleSize++\n     \
        \       }\n            if (cycleSize > 1) {\n                swaps += (cycleSize\
        \ - 1)\n            }\n        }\n        return swaps\n    }\n}"
      dart: "class Solution {\n  int minSwaps(List<int> nums) {\n    int n = nums.length;\n\
        \    List<_Item> items = List.generate(n, (i) {\n      int sum = 0;\n      int\
        \ temp = nums[i];\n      while (temp > 0) {\n        sum += temp % 10;\n   \
        \     temp ~/= 10;\n      }\n      return _Item(sum, nums[i], i);\n    });\n\
        \n    items.sort((a, b) {\n      if (a.sum != b.sum) return a.sum.compareTo(b.sum);\n\
        \      return a.val.compareTo(b.val);\n    });\n\n    List<int> targetPos =\
        \ List<int>.filled(n, 0);\n    for (int i = 0; i < n; i++) {\n      targetPos[items[i].oldIdx]\
        \ = i;\n    }\n\n    int swaps = 0;\n    List<bool> visited = List<bool>.filled(n,\
        \ false);\n    for (int i = 0; i < n; i++) {\n      if (visited[i] || targetPos[i]\
        \ == i) continue;\n\n      int cycleSize = 0;\n      int curr = i;\n      while\
        \ (!visited[curr]) {\n        visited[curr] = true;\n        curr = targetPos[curr];\n\
        \        cycleSize++;\n      }\n      if (cycleSize > 1) {\n        swaps +=\
        \ (cycleSize - 1);\n      }\n    }\n    return swaps;\n  }\n}\n\nclass _Item\
        \ {\n  final int sum;\n  final int val;\n  final int oldIdx;\n  _Item(this.sum,\
        \ this.val, this.oldIdx);\n}"
      go: "import \"sort\"\n\nfunc minSwaps(nums []int) int {\n\tn := len(nums)\n\t\
        type node struct {\n\t\tsum, val, idx int\n\t}\n\tnodes := make([]node, n)\n\
        \tfor i, v := range nums {\n\t\ts, temp := 0, v\n\t\tfor temp > 0 {\n\t\t\t\
        s += temp % 10\n\t\t\ttemp /= 10\n\t\t}\n\t\tnodes[i] = node{s, v, i}\n\t}\n\
        \n\tsort.Slice(nodes, func(i, j int) bool {\n\t\tif nodes[i].sum != nodes[j].sum\
        \ {\n\t\t\treturn nodes[i].sum < nodes[j].sum\n\t\t}\n\t\treturn nodes[i].val\
        \ < nodes[j].val\n\t})\n\n\ttargetPos := make([]int, n)\n\tfor i := 0; i < n;\
        \ i++ {\n\t\ttargetPos[nodes[i].idx] = i\n\t}\n\n\tswaps := 0\n\tvisited :=\
        \ make([]bool, n)\n\tfor i := 0; i < n; i++ {\n\t\tif visited[i] || targetPos[i]\
        \ == i {\n\t\t\tcontinue\n\t\t}\n\t\tcycleSize := 0\n\t\tcurr := i\n\t\tfor\
        \ !visited[curr] {\n\t\t\tvisited[curr] = true\n\t\t\tcurr = targetPos[curr]\n\
        \t\t\tcycleSize++\n\t\t}\n\t\tif cycleSize > 1 {\n\t\t\tswaps += (cycleSize\
        \ - 1)\n\t\t}\n\t}\n\treturn swaps\n}"
      ruby: "# @param {Integer[]} nums\n# @return {Integer}\ndef min_swaps(nums)\n \
        \ n = nums.length\n  items = []\n  nums.each_with_index do |v, i|\n    sum =\
        \ 0\n    temp = v\n    while temp > 0\n      sum += temp % 10\n      temp /=\
        \ 10\n    end\n    items << [sum, v, i]\n  end\n\n  items.sort!\n\n  target_pos\
        \ = Array.new(n)\n  items.each_with_index do |item, i|\n    target_pos[item[2]]\
        \ = i\n  end\n\n  swaps = 0\n  visited = Array.new(n, false)\n  (0...n).each\
        \ do |i|\n    next if visited[i] || target_pos[i] == i\n\n    cycle_size = 0\n\
        \    curr = i\n    while !visited[curr]\n      visited[curr] = true\n      curr\
        \ = target_pos[curr]\n      cycle_size += 1\n    end\n    swaps += (cycle_size\
        \ - 1) if cycle_size > 1\n  end\n  swaps\nend"
      scala: "object Solution {\n    def minSwaps(nums: Array[Int]): Int = {\n     \
        \   val n = nums.length\n        val items = new Array[(Int, Int, Int)](n)\n\
        \        var i = 0\n        while (i < n) {\n            val v = nums(i)\n \
        \           var sum = 0\n            var temp = v\n            while (temp >\
        \ 0) {\n                sum += temp % 10\n                temp /= 10\n     \
        \       }\n            items(i) = (sum, v, i)\n            i += 1\n        }\n\
        \n        val sortedItems = items.sortBy(t => (t._1, t._2))\n        val targetPos\
        \ = new Array[Int](n)\n        i = 0\n        while (i < n) {\n            targetPos(sortedItems(i)._3)\
        \ = i\n            i += 1\n        }\n\n        var swaps = 0\n        val visited\
        \ = new Array[Boolean](n)\n        i = 0\n        while (i < n) {\n        \
        \    if (!visited(i) && targetPos(i) != i) {\n                var cycleSize\
        \ = 0\n                var curr = i\n                while (!visited(curr))\
        \ {\n                    visited(curr) = true\n                    curr = targetPos(curr)\n\
        \                    cycleSize += 1\n                }\n                if (cycleSize\
        \ > 1) {\n                    swaps += (cycleSize - 1)\n                }\n\
        \            }\n            i += 1\n        }\n        swaps\n    }\n}"
      rust: "use std::collections::HashMap;\n\nimpl Solution {\n    pub fn min_swaps(nums:\
        \ Vec<i32>) -> i32 {\n        let n = nums.len();\n        let digit_sum = |mut\
        \ val: i32| -> i32 {\n            let mut sum = 0;\n            while val >\
        \ 0 {\n                sum += val % 10;\n                val /= 10;\n      \
        \      }\n            sum\n        };\n\n        let mut nums_with_sums: Vec<(i32,\
        \ i32)> = nums.iter().map(|&x| (x, digit_sum(x))).collect();\n        nums_with_sums.sort_by(|a,\
        \ b| {\n            if a.1 != b.1 {\n                a.1.cmp(&b.1)\n       \
        \     } else {\n                a.0.cmp(&b.0)\n            }\n        });\n\n\
        \        let mut pos_map = HashMap::with_capacity(n);\n        for (i, (val,\
        \ _)) in nums_with_sums.iter().enumerate() {\n            pos_map.insert(*val,\
        \ i);\n        }\n\n        let mut visited = vec![false; n];\n        let mut\
        \ swaps: usize = 0;\n        for i in 0..n {\n            if visited[i] {\n\
        \                continue;\n            }\n            let mut curr = i;\n \
        \           let mut cycle_size = 0;\n            while !visited[curr] {\n  \
        \              visited[curr] = true;\n                let val = nums[curr];\n\
        \                curr = *pos_map.get(&val).unwrap();\n                cycle_size\
        \ += 1;\n            }\n            if cycle_size > 1 {\n                swaps\
        \ += cycle_size - 1;\n            }\n        }\n        swaps as i32\n    }\n\
        }"
      racket: "(define/contract (min-swaps nums)\n  (-> (listof exact-integer?) exact-integer?)\n\
        \  (let* ([digit-sum (lambda (n)\n                      (let loop ([n n] [acc\
        \ 0])\n                        (if (= n 0) acc (loop (quotient n 10) (+ acc\
        \ (remainder n 10))))))]\n         [nums-with-sums (map (lambda (n) (cons n\
        \ (digit-sum n))) nums)]\n         [sorted-with-sums (sort nums-with-sums (lambda\
        \ (a b)\n                                                  (let ([s1 (cdr a)]\
        \ [s2 (cdr b)]\n                                                        [v1\
        \ (car a)] [v2 (car b)])\n                                                 \
        \   (if (= s1 s2) (< v1 v2) (< s1 s2)))))]\n         [n (length nums)]\n   \
        \      [nums-vec (list->vector nums)]\n         [pos-map (make-hash)]\n    \
        \     [_ (for ([v (in-list sorted-with-sums)] [i (in-range n)]) \n         \
        \     (hash-set! pos-map (car v) i))]\n         [visited (make-vector n #f)]\n\
        \         [swaps 0])\n    (for ([i (in-range n)])\n      (when (not (vector-ref\
        \ visited i))\n        (let ([cycle-size (let loop ([curr i] [size 0])\n   \
        \                          (if (vector-ref visited curr)\n                 \
        \                size\n                                 (begin\n           \
        \                        (vector-set! visited curr #t)\n                   \
        \                (loop (hash-ref pos-map (vector-ref nums-vec curr)) (+ size\
        \ 1)))))])\n          (set! swaps (+ swaps (- cycle-size 1))))))\n    swaps))"
      erlang: "-spec min_swaps(Nums :: [integer()]) -> integer().\nmin_swaps(Nums) ->\n\
        \    DigitSum = fun DS(0) -> 0; DS(X) -> (X rem 10) + DS(X div 10) end,\n  \
        \  NumsWithSums = [{N, DigitSum(N)} || N <- Nums],\n    SortedWithSums = lists:sort(fun({V1,\
        \ S1}, {V2, S2}) ->\n        if S1 < S2 -> true;\n           S1 > S2 -> false;\n\
        \           true -> V1 =< V2\n        end\n    end, NumsWithSums),\n    N =\
        \ length(Nums),\n    SortedVals = [V || {V, _} <- SortedWithSums],\n    TargetMap\
        \ = maps:from_list(lists:zip(SortedVals, lists:seq(0, N - 1))),\n    OriginalToTarget\
        \ = list_to_tuple([maps:get(V, TargetMap) || V <- Nums]),\n    find_cycles(0,\
        \ N, OriginalToTarget, sets:new(), 0).\n\nfind_cycles(I, N, OriginalToTarget,\
        \ Visited, Swaps) ->\n    if I >= N -> Swaps;\n       true ->\n           case\
        \ sets:is_element(I, Visited) of\n               true -> find_cycles(I + 1,\
        \ N, OriginalToTarget, Visited, Swaps);\n               false ->\n         \
        \          {NewVisited, CycleSize} = traverse_cycle(I, OriginalToTarget, Visited,\
        \ 0),\n                   find_cycles(I + 1, N, OriginalToTarget, NewVisited,\
        \ Swaps + CycleSize - 1)\n           end\n    end.\n\ntraverse_cycle(Curr, OriginalToTarget,\
        \ Visited, Size) ->\n    case sets:is_element(Curr, Visited) of\n        true\
        \ -> {Visited, Size};\n        false ->\n            NextIdx = element(Curr\
        \ + 1, OriginalToTarget),\n            traverse_cycle(NextIdx, OriginalToTarget,\
        \ sets:add_element(Curr, Visited), Size + 1)\n    end."
      elixir: "defmodule Solution do\n  @spec min_swaps(nums :: [integer]) :: integer\n\
        \  def min_swaps(nums) do\n    n = length(nums)\n    digit_sum = fn n ->\n \
        \     Integer.digits(n) |> Enum.sum()\n    end\n\n    sorted_nums = nums\n \
        \     |> Enum.map(fn v -> {v, digit_sum.(v)} end)\n      |> Enum.sort(fn {v1,\
        \ s1}, {v2, s2} ->\n        if s1 == s2, do: v1 <= v2, else: s1 < s2\n     \
        \ end)\n      |> Enum.map(fn {v, _s} -> v end)\n\n    target_map = sorted_nums\
        \ |> Enum.with_index() |> Map.new()\n\n    target_indices = nums\n      |> Enum.with_index()\n\
        \      |> Map.new(fn {v, i} -> {i, Map.get(target_map, v)} end)\n\n    {_visited,\
        \ swaps} = Enum.reduce(0..(n - 1), {MapSet.new(), 0}, fn i, {visited, count}\
        \ ->\n      if MapSet.member?(visited, i) do\n        {visited, count}\n   \
        \   else\n        {new_visited, cycle_size} = get_cycle(i, target_indices, visited,\
        \ 0)\n        {new_visited, count + cycle_size - 1}\n      end\n    end)\n\n\
        \    swaps\n  end\n\n  defp get_cycle(curr, target_indices, visited, size) do\n\
        \    if MapSet.member?(visited, curr) do\n      {visited, size}\n    else\n\
        \      next_idx = Map.get(target_indices, curr)\n      get_cycle(next_idx, target_indices,\
        \ MapSet.put(visited, curr), size + 1)\n    end\n  end\nend"
    approach: 'The problem is solved by first identifying the target sorted order of
      the elements based on the digit sum of each number and using the numerical value
      as a tie-breaker. By associating each number with its original index before sorting,
      we can determine the permutation required to transform the original array into
      the sorted one. This involves calculating the digit sum for every element and
      storing it in a way that allows sorting by the custom criteria: primarily by the
      sum and secondarily by the original value.'
    time_complexity: O(N log N) where N is the number of elements in the array. This
      complexity arises from calculating the digit sum for each element in O(N log_{10}
      M) time, where M is the maximum integer value ($10^9$), followed by sorting the
      elements in O(N log N) time. The final step of cycle decomposition to find the
      minimum number of swaps takes linear time O(N).
    space_complexity: O(N) because we store the original values, their digit sums, and
      their initial indices in an auxiliary data structure for sorting. Additionally,
      a boolean visited array of size N is used during the cycle decomposition process
      to track processed elements in the permutation.
    elapsed_time: 311.4100091457367
    model: gemini-3-flash-preview
    generated_at: '2026-10-17 02:29:03 '
---

## Problem #3551: Minimum Swaps to Sort by Digit Sum

**Difficulty:** Medium

**Topics:** Array, Hash Table, Sorting

## Problem Description

<p>You are given an array <code>nums</code> of <strong>distinct</strong> positive integers. You need to sort the array in <strong>increasing</strong> order based on the sum of the digits of each number. If two numbers have the same digit sum, the <strong>smaller</strong> number appears first in the sorted order.</p>

<p>Return the <strong>minimum</strong> number of swaps required to rearrange <code>nums</code> into this sorted order.</p>

<p>A <strong>swap</strong> is defined as exchanging the values at two distinct positions in the array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [37,100]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Compute the digit sum for each integer: <code>[3 + 7 = 10, 1 + 0 + 0 = 1] &rarr; [10, 1]</code></li>
	<li>Sort the integers based on digit sum: <code>[100, 37]</code>. Swap <code>37</code> with <code>100</code> to obtain the sorted order.</li>
	<li>Thus, the minimum number of swaps required to rearrange <code>nums</code> is 1.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [22,14,33,7]</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Compute the digit sum for each integer: <code>[2 + 2 = 4, 1 + 4 = 5, 3 + 3 = 6, 7 = 7] &rarr; [4, 5, 6, 7]</code></li>
	<li>Sort the integers based on digit sum: <code>[22, 14, 33, 7]</code>. The array is already sorted.</li>
	<li>Thus, the minimum number of swaps required to rearrange <code>nums</code> is 0.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [18,43,34,16]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>Compute the digit sum for each integer: <code>[1 + 8 = 9, 4 + 3 = 7, 3 + 4 = 7, 1 + 6 = 7] &rarr; [9, 7, 7, 7]</code></li>
	<li>Sort the integers based on digit sum: <code>[16, 34, 43, 18]</code>. Swap <code>18</code> with <code>16</code>, and swap <code>43</code> with <code>34</code> to obtain the sorted order.</li>
	<li>Thus, the minimum number of swaps required to rearrange <code>nums</code> is 2.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>nums</code> consists of <strong>distinct</strong> positive integers.</li>
</ul>


## Hints

1. First, sort the array based on digit sum (and value as a tiebreaker). Then, map each original value to its index in the sorted array.

2. Now, the problem reduces to finding the minimum number of swaps to sort this mapped array. The answer is `n - number_of_cycles` in the permutation.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem is solved by first identifying the target sorted order of the elements based on the digit sum of each number and using the numerical value as a tie-breaker. By associating each number with its original index before sorting, we can determine the permutation required to transform the original array into the sorted one. This involves calculating the digit sum for every element and storing it in a way that allows sorting by the custom criteria: primarily by the sum and secondarily by the original value.

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
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

class Solution {
public:
    int minSwaps(vector<int>& nums) {
        int n = nums.size();
        struct Node {
            int val;
            int sum;
            int originalIdx;
        };

        auto getDigitSum = [](int num) {
            int s = 0;
            while (num > 0) {
                s += num % 10;
                num /= 10;
            }
            return s;
        };

        vector<Node> nodes(n);
        for (int i = 0; i < n; ++i) {
            nodes[i] = {nums[i], getDigitSum(nums[i]), i};
        }

        sort(nodes.begin(), nodes.end(), [](const Node& a, const Node& b) {
            if (a.sum != b.sum) return a.sum < b.sum;
            return a.val < b.val;
        });

        vector<int> p(n);
        for (int i = 0; i < n; ++i) {
            p[i] = nodes[i].originalIdx;
        }

        vector<bool> visited(n, false);
        int totalSwaps = 0;
        for (int i = 0; i < n; ++i) {
            if (visited[i]) continue;

            int curr = i;
            int cycleSize = 0;
            while (!visited[curr]) {
                visited[curr] = true;
                curr = p[curr];
                cycleSize++;
            }
            if (cycleSize > 1) {
                totalSwaps += (cycleSize - 1);
            }
        }

        return totalSwaps;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.Arrays;
import java.util.Comparator;

class Solution {
    static class Node {
        int val;
        int sum;
        int originalIdx;

        Node(int val, int sum, int originalIdx) {
            this.val = val;
            this.sum = sum;
            this.originalIdx = originalIdx;
        }
    }

    public int minSwaps(int[] nums) {
        int n = nums.length;
        Node[] nodes = new Node[n];
        for (int i = 0; i < n; i++) {
            int s = 0;
            int temp = nums[i];
            while (temp > 0) {
                s += temp % 10;
                temp /= 10;
            }
            nodes[i] = new Node(nums[i], s, i);
        }

        Arrays.sort(nodes, (a, b) -> {
            if (a.sum != b.sum) return Integer.compare(a.sum, b.sum);
            return Integer.compare(a.val, b.val);
        });

        int[] p = new int[n];
        for (int i = 0; i < n; i++) {
            p[i] = nodes[i].originalIdx;
        }

        boolean[] visited = new boolean[n];
        int totalSwaps = 0;
        for (int i = 0; i < n; i++) {
            if (visited[i]) continue;

            int curr = i;
            int cycleSize = 0;
            while (!visited[curr]) {
                visited[curr] = true;
                curr = p[curr];
                cycleSize++;
            }
            if (cycleSize > 1) {
                totalSwaps += (cycleSize - 1);
            }
        }

        return totalSwaps;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def get_digit_sum(n):
            s = 0
            while n > 0:
                s += n % 10
                n //= 10
            return s

        n = len(nums)
        arr = []
        for i in xrange(n):
            arr.append((get_digit_sum(nums[i]), nums[i], i))

        arr.sort()

        p = [x[2] for x in arr]
        visited = [False] * n
        total_swaps = 0

        for i in xrange(n):
            if visited[i]:
                continue

            curr = i
            cycle_size = 0
            while not visited[curr]:
                visited[curr] = True
                curr = p[curr]
                cycle_size += 1

            if cycle_size > 1:
                total_swaps += (cycle_size - 1)

        return total_swaps
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def get_digit_sum(n):
            s = 0
            while n > 0:
                s += n % 10
                n //= 10
            return s

        n = len(nums)
        # Create tuples of (digit_sum, value, original_index)
        # Sorting will automatically use sum as primary and value as secondary.
        arr = sorted([(get_digit_sum(nums[i]), nums[i], i) for i in range(n)])

        p = [x[2] for x in arr]
        visited = [False] * n
        total_swaps = 0

        for i in range(n):
            if visited[i]:
                continue

            curr = i
            cycle_size = 0
            while not visited[curr]:
                visited[curr] = True
                curr = p[curr]
                cycle_size += 1

            if cycle_size > 1:
                total_swaps += (cycle_size - 1)

        return total_swaps
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>

typedef struct {
    int val;
    int sum;
    int originalIdx;
} Node;

int getSum(int n) {
    int s = 0;
    while (n > 0) {
        s += n % 10;
        n /= 10;
    }
    return s;
}

int compareNodes(const void* a, const void* b) {
    Node* n1 = (Node*)a;
    Node* n2 = (Node*)b;
    if (n1->sum != n2->sum) return n1->sum - n2->sum;
    if (n1->val < n2->val) return -1;
    if (n1->val > n2->val) return 1;
    return 0;
}

int minSwaps(int* nums, int numsSize) {
    Node* arr = (Node*)malloc(sizeof(Node) * numsSize);
    for (int i = 0; i < numsSize; i++) {
        arr[i].val = nums[i];
        arr[i].sum = getSum(nums[i]);
        arr[i].originalIdx = i;
    }

    qsort(arr, numsSize, sizeof(Node), compareNodes);

    int* p = (int*)malloc(sizeof(int) * numsSize);
    for (int i = 0; i < numsSize; i++) {
        p[i] = arr[i].originalIdx;
    }

    char* visited = (char*)calloc(numsSize, sizeof(char));
    int totalSwaps = 0;
    for (int i = 0; i < numsSize; i++) {
        if (visited[i]) continue;

        int curr = i;
        int cycleSize = 0;
        while (!visited[curr]) {
            visited[curr] = 1;
            curr = p[curr];
            cycleSize++;
        }
        if (cycleSize > 1) {
            totalSwaps += (cycleSize - 1);
        }
    }

    free(arr);
    free(p);
    free(visited);
    return totalSwaps;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MinSwaps(int[] nums) {
        int n = nums.Length;
        (int s, int v, int i)[] items = new (int s, int v, int i)[n];
        for (int k = 0; k < n; k++) {
            int sum = 0, temp = nums[k];
            while (temp > 0) {
                sum += temp % 10;
                temp /= 10;
            }
            items[k] = (sum, nums[k], k);
        }

        System.Array.Sort(items, (a, b) => {
            if (a.s != b.s) return a.s.CompareTo(b.s);
            return a.v.CompareTo(b.v);
        });

        int[] p = new int[n];
        for (int k = 0; k < n; k++) {
            p[items[k].i] = k;
        }

        bool[] visited = new bool[n];
        int cycles = 0;
        for (int k = 0; k < n; k++) {
            if (!visited[k]) {
                cycles++;
                int curr = k;
                while (!visited[curr]) {
                    visited[curr] = true;
                    curr = p[curr];
                }
            }
        }
        return n - cycles;
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
var minSwaps = function(nums) {
    const n = nums.length;
    const items = new Array(n);
    for (let i = 0; i < n; i++) {
        let s = 0, temp = nums[i];
        while (temp > 0) {
            s += temp % 10;
            temp = Math.floor(temp / 10);
        }
        items[i] = { s, v: nums[i], i };
    }

    items.sort((a, b) => a.s - b.s || a.v - b.v);

    const p = new Int32Array(n);
    for (let i = 0; i < n; i++) {
        p[items[i].i] = i;
    }

    let cycles = 0;
    const visited = new Uint8Array(n);
    for (let i = 0; i < n; i++) {
        if (!visited[i]) {
            cycles++;
            let curr = i;
            while (!visited[curr]) {
                visited[curr] = 1;
                curr = p[curr];
            }
        }
    }
    return n - cycles;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minSwaps(nums: number[]): number {
    const n = nums.length;
    const items: { s: number, v: number, i: number }[] = new Array(n);
    for (let i = 0; i < n; i++) {
        let s = 0, temp = nums[i];
        while (temp > 0) {
            s += temp % 10;
            temp = Math.floor(temp / 10);
        }
        items[i] = { s, v: nums[i], i };
    }

    items.sort((a, b) => a.s - b.s || a.v - b.v);

    const p = new Int32Array(n);
    for (let i = 0; i < n; i++) {
        p[items[i].i] = i;
    }

    let cycles = 0;
    const visited = new Uint8Array(n);
    for (let i = 0; i < n; i++) {
        if (visited[i] === 0) {
            cycles++;
            let curr = i;
            while (visited[curr] === 0) {
                visited[curr] = 1;
                curr = p[curr];
            }
        }
    }
    return n - cycles;
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
    function minSwaps($nums) {
        $n = count($nums);
        $items = [];
        for ($i = 0; $i < $n; $i++) {
            $s = 0;
            $temp = $nums[$i];
            while ($temp > 0) {
                $s += $temp % 10;
                $temp = intdiv($temp, 10);
            }
            $items[] = ['s' => $s, 'v' => $nums[$i], 'i' => $i];
        }

        usort($items, function($a, $b) {
            if ($a['s'] !== $b['s']) return $a['s'] <=> $b['s'];
            return $a['v'] <=> $b['v'];
        });

        $p = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) {
            $p[$items[$i]['i']] = $i;
        }

        $visited = array_fill(0, $n, false);
        $cycles = 0;
        for ($i = 0; $i < $n; $i++) {
            if (!$visited[$i]) {
                $cycles++;
                $curr = $i;
                while (!$visited[$curr]) {
                    $visited[$curr] = true;
                    $curr = $p[$curr];
                }
            }
        }
        return $n - $cycles;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minSwaps(_ nums: [Int]) -> Int {
        let n = nums.count
        struct Item {
            let s: Int
            let v: Int
            let i: Int
        }
        var items: [Item] = []
        items.reserveCapacity(n)
        for k in 0..<n {
            var sum = 0
            var temp = nums[k]
            while temp > 0 {
                sum += temp % 10
                temp /= 10
            }
            items.append(Item(s: sum, v: nums[k], i: k))
        }

        items.sort { a, b in
            if a.s != b.s { return a.s < b.s }
            return a.v < b.v
        }

        var p = [Int](repeating: 0, count: n)
        for k in 0..<n {
            p[items[k].i] = k
        }

        var visited = [Bool](repeating: false, count: n)
        var cycles = 0
        for k in 0..<n {
            if !visited[k] {
                cycles += 1
                var curr = k
                while !visited[curr] {
                    visited[curr] = true
                    curr = p[curr]
                }
            }
        }
        return n - cycles
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minSwaps(nums: IntArray): Int {
        val n = nums.size
        val items = Array(n) { i ->
            var sum = 0
            var temp = nums[i]
            while (temp > 0) {
                sum += temp % 10
                temp /= 10
            }
            Triple(sum, nums[i], i)
        }

        items.sortWith(Comparator { a, b ->
            if (a.first != b.first) a.first.compareTo(b.first)
            else a.second.compareTo(b.second)
        })

        val targetPos = IntArray(n)
        for (i in 0 until n) {
            targetPos[items[i].third] = i
        }

        var swaps = 0
        val visited = BooleanArray(n)
        for (i in 0 until n) {
            if (visited[i] || targetPos[i] == i) continue

            var cycleSize = 0
            var curr = i
            while (!visited[curr]) {
                visited[curr] = true
                curr = targetPos[curr]
                cycleSize++
            }
            if (cycleSize > 1) {
                swaps += (cycleSize - 1)
            }
        }
        return swaps
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int minSwaps(List<int> nums) {
    int n = nums.length;
    List<_Item> items = List.generate(n, (i) {
      int sum = 0;
      int temp = nums[i];
      while (temp > 0) {
        sum += temp % 10;
        temp ~/= 10;
      }
      return _Item(sum, nums[i], i);
    });

    items.sort((a, b) {
      if (a.sum != b.sum) return a.sum.compareTo(b.sum);
      return a.val.compareTo(b.val);
    });

    List<int> targetPos = List<int>.filled(n, 0);
    for (int i = 0; i < n; i++) {
      targetPos[items[i].oldIdx] = i;
    }

    int swaps = 0;
    List<bool> visited = List<bool>.filled(n, false);
    for (int i = 0; i < n; i++) {
      if (visited[i] || targetPos[i] == i) continue;

      int cycleSize = 0;
      int curr = i;
      while (!visited[curr]) {
        visited[curr] = true;
        curr = targetPos[curr];
        cycleSize++;
      }
      if (cycleSize > 1) {
        swaps += (cycleSize - 1);
      }
    }
    return swaps;
  }
}

class _Item {
  final int sum;
  final int val;
  final int oldIdx;
  _Item(this.sum, this.val, this.oldIdx);
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import "sort"

func minSwaps(nums []int) int {
	n := len(nums)
	type node struct {
		sum, val, idx int
	}
	nodes := make([]node, n)
	for i, v := range nums {
		s, temp := 0, v
		for temp > 0 {
			s += temp % 10
			temp /= 10
		}
		nodes[i] = node{s, v, i}
	}

	sort.Slice(nodes, func(i, j int) bool {
		if nodes[i].sum != nodes[j].sum {
			return nodes[i].sum < nodes[j].sum
		}
		return nodes[i].val < nodes[j].val
	})

	targetPos := make([]int, n)
	for i := 0; i < n; i++ {
		targetPos[nodes[i].idx] = i
	}

	swaps := 0
	visited := make([]bool, n)
	for i := 0; i < n; i++ {
		if visited[i] || targetPos[i] == i {
			continue
		}
		cycleSize := 0
		curr := i
		for !visited[curr] {
			visited[curr] = true
			curr = targetPos[curr]
			cycleSize++
		}
		if cycleSize > 1 {
			swaps += (cycleSize - 1)
		}
	}
	return swaps
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @return {Integer}
def min_swaps(nums)
  n = nums.length
  items = []
  nums.each_with_index do |v, i|
    sum = 0
    temp = v
    while temp > 0
      sum += temp % 10
      temp /= 10
    end
    items << [sum, v, i]
  end

  items.sort!

  target_pos = Array.new(n)
  items.each_with_index do |item, i|
    target_pos[item[2]] = i
  end

  swaps = 0
  visited = Array.new(n, false)
  (0...n).each do |i|
    next if visited[i] || target_pos[i] == i

    cycle_size = 0
    curr = i
    while !visited[curr]
      visited[curr] = true
      curr = target_pos[curr]
      cycle_size += 1
    end
    swaps += (cycle_size - 1) if cycle_size > 1
  end
  swaps
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def minSwaps(nums: Array[Int]): Int = {
        val n = nums.length
        val items = new Array[(Int, Int, Int)](n)
        var i = 0
        while (i < n) {
            val v = nums(i)
            var sum = 0
            var temp = v
            while (temp > 0) {
                sum += temp % 10
                temp /= 10
            }
            items(i) = (sum, v, i)
            i += 1
        }

        val sortedItems = items.sortBy(t => (t._1, t._2))
        val targetPos = new Array[Int](n)
        i = 0
        while (i < n) {
            targetPos(sortedItems(i)._3) = i
            i += 1
        }

        var swaps = 0
        val visited = new Array[Boolean](n)
        i = 0
        while (i < n) {
            if (!visited(i) && targetPos(i) != i) {
                var cycleSize = 0
                var curr = i
                while (!visited(curr)) {
                    visited(curr) = true
                    curr = targetPos(curr)
                    cycleSize += 1
                }
                if (cycleSize > 1) {
                    swaps += (cycleSize - 1)
                }
            }
            i += 1
        }
        swaps
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
    pub fn min_swaps(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let digit_sum = |mut val: i32| -> i32 {
            let mut sum = 0;
            while val > 0 {
                sum += val % 10;
                val /= 10;
            }
            sum
        };

        let mut nums_with_sums: Vec<(i32, i32)> = nums.iter().map(|&x| (x, digit_sum(x))).collect();
        nums_with_sums.sort_by(|a, b| {
            if a.1 != b.1 {
                a.1.cmp(&b.1)
            } else {
                a.0.cmp(&b.0)
            }
        });

        let mut pos_map = HashMap::with_capacity(n);
        for (i, (val, _)) in nums_with_sums.iter().enumerate() {
            pos_map.insert(*val, i);
        }

        let mut visited = vec![false; n];
        let mut swaps: usize = 0;
        for i in 0..n {
            if visited[i] {
                continue;
            }
            let mut curr = i;
            let mut cycle_size = 0;
            while !visited[curr] {
                visited[curr] = true;
                let val = nums[curr];
                curr = *pos_map.get(&val).unwrap();
                cycle_size += 1;
            }
            if cycle_size > 1 {
                swaps += cycle_size - 1;
            }
        }
        swaps as i32
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (min-swaps nums)
  (-> (listof exact-integer?) exact-integer?)
  (let* ([digit-sum (lambda (n)
                      (let loop ([n n] [acc 0])
                        (if (= n 0) acc (loop (quotient n 10) (+ acc (remainder n 10))))))]
         [nums-with-sums (map (lambda (n) (cons n (digit-sum n))) nums)]
         [sorted-with-sums (sort nums-with-sums (lambda (a b)
                                                  (let ([s1 (cdr a)] [s2 (cdr b)]
                                                        [v1 (car a)] [v2 (car b)])
                                                    (if (= s1 s2) (< v1 v2) (< s1 s2)))))]
         [n (length nums)]
         [nums-vec (list->vector nums)]
         [pos-map (make-hash)]
         [_ (for ([v (in-list sorted-with-sums)] [i (in-range n)]) 
              (hash-set! pos-map (car v) i))]
         [visited (make-vector n #f)]
         [swaps 0])
    (for ([i (in-range n)])
      (when (not (vector-ref visited i))
        (let ([cycle-size (let loop ([curr i] [size 0])
                             (if (vector-ref visited curr)
                                 size
                                 (begin
                                   (vector-set! visited curr #t)
                                   (loop (hash-ref pos-map (vector-ref nums-vec curr)) (+ size 1)))))])
          (set! swaps (+ swaps (- cycle-size 1))))))
    swaps))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec min_swaps(Nums :: [integer()]) -> integer().
min_swaps(Nums) ->
    DigitSum = fun DS(0) -> 0; DS(X) -> (X rem 10) + DS(X div 10) end,
    NumsWithSums = [{N, DigitSum(N)} || N <- Nums],
    SortedWithSums = lists:sort(fun({V1, S1}, {V2, S2}) ->
        if S1 < S2 -> true;
           S1 > S2 -> false;
           true -> V1 =< V2
        end
    end, NumsWithSums),
    N = length(Nums),
    SortedVals = [V || {V, _} <- SortedWithSums],
    TargetMap = maps:from_list(lists:zip(SortedVals, lists:seq(0, N - 1))),
    OriginalToTarget = list_to_tuple([maps:get(V, TargetMap) || V <- Nums]),
    find_cycles(0, N, OriginalToTarget, sets:new(), 0).

find_cycles(I, N, OriginalToTarget, Visited, Swaps) ->
    if I >= N -> Swaps;
       true ->
           case sets:is_element(I, Visited) of
               true -> find_cycles(I + 1, N, OriginalToTarget, Visited, Swaps);
               false ->
                   {NewVisited, CycleSize} = traverse_cycle(I, OriginalToTarget, Visited, 0),
                   find_cycles(I + 1, N, OriginalToTarget, NewVisited, Swaps + CycleSize - 1)
           end
    end.

traverse_cycle(Curr, OriginalToTarget, Visited, Size) ->
    case sets:is_element(Curr, Visited) of
        true -> {Visited, Size};
        false ->
            NextIdx = element(Curr + 1, OriginalToTarget),
            traverse_cycle(NextIdx, OriginalToTarget, sets:add_element(Curr, Visited), Size + 1)
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec min_swaps(nums :: [integer]) :: integer
  def min_swaps(nums) do
    n = length(nums)
    digit_sum = fn n ->
      Integer.digits(n) |> Enum.sum()
    end

    sorted_nums = nums
      |> Enum.map(fn v -> {v, digit_sum.(v)} end)
      |> Enum.sort(fn {v1, s1}, {v2, s2} ->
        if s1 == s2, do: v1 <= v2, else: s1 < s2
      end)
      |> Enum.map(fn {v, _s} -> v end)

    target_map = sorted_nums |> Enum.with_index() |> Map.new()

    target_indices = nums
      |> Enum.with_index()
      |> Map.new(fn {v, i} -> {i, Map.get(target_map, v)} end)

    {_visited, swaps} = Enum.reduce(0..(n - 1), {MapSet.new(), 0}, fn i, {visited, count} ->
      if MapSet.member?(visited, i) do
        {visited, count}
      else
        {new_visited, cycle_size} = get_cycle(i, target_indices, visited, 0)
        {new_visited, count + cycle_size - 1}
      end
    end)

    swaps
  end

  defp get_cycle(curr, target_indices, visited, size) do
    if MapSet.member?(visited, curr) do
      {visited, size}
    else
      next_idx = Map.get(target_indices, curr)
      get_cycle(next_idx, target_indices, MapSet.put(visited, curr), size + 1)
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N log N) where N is the number of elements in the array. This complexity arises from calculating the digit sum for each element in O(N log_{10} M) time, where M is the maximum integer value ($10^9$), followed by sorting the elements in O(N log N) time. The final step of cycle decomposition to find the minimum number of swaps takes linear time O(N).
- **Space Complexity:** O(N) because we store the original values, their digit sums, and their initial indices in an auxiliary data structure for sorting. Additionally, a boolean visited array of size N is used during the cycle decomposition process to track processed elements in the permutation.
