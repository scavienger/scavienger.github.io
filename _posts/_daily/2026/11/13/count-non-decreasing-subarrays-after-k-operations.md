---
layout: post
title: "Count Non-Decreasing Subarrays After K Operations"
date: 2026-11-13 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Stack", "Segment Tree", "Queue", "Sliding Window", "Monotonic Stack", "Monotonic Queue"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/count-non-decreasing-subarrays-after-k-operations/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    long long countNonDecreasingSubarrays(vector<int>&\
        \ nums, int k) {\n        int n = nums.size();\n        if (n == 0) return 0;\n\
        \        long long total = 0;\n        long long cost = 0;\n        struct Element\
        \ {\n            long long val;\n            long long count;\n        };\n\
        \        std::deque<Element> dq;\n\n        int R = n - 1;\n        dq.push_back({(long\
        \ long)nums[n - 1], 1});\n        total += 1;\n\n        for (int L = n - 2;\
        \ L >= 0; --L) {\n            long long new_count = 0;\n            while (!dq.empty()\
        \ && dq.front().val < (long long)nums[L]) {\n                cost += (long long)(nums[L]\
        \ - dq.front().val) * dq.front().count;\n                new_count += dq.front().count;\n\
        \                dq.pop_front();\n            }\n            dq.push_front({(long\
        \ long)nums[L], new_count + 1});\n\n            while (cost > (long long)k)\
        \ {\n                long long v = dq.back().val;\n                cost -= (v\
        \ - (long long)nums[R]);\n                dq.back().count--;\n             \
        \   if (dq.back().count == 0) {\n                    dq.pop_back();\n      \
        \          }\n                R--;\n            }\n            total += (long\
        \ long)(R - L + 1);\n        }\n\n        return total;\n    }\n};"
      java: "class Solution {\n    public long countNonDecreasingSubarrays(int[] nums,\
        \ int k) {\n        int n = nums.length;\n        if (n == 0) return 0;\n  \
        \      long total = 0;\n        long cost = 0;\n        java.util.Deque<long[]>\
        \ dq = new java.util.ArrayDeque<>();\n\n        int R = n - 1;\n        dq.addLast(new\
        \ long[]{(long) nums[n - 1], 1L});\n        total += 1;\n\n        for (int\
        \ L = n - 2; L >= 0; --L) {\n            long newCount = 0;\n            while\
        \ (!dq.isEmpty() && dq.peekFirst()[0] < (long) nums[L]) {\n                long[]\
        \ first = dq.pollFirst();\n                cost += (long) (nums[L] - first[0])\
        \ * first[1];\n                newCount += first[1];\n            }\n      \
        \      dq.addFirst(new long[]{(long) nums[L], newCount + 1L});\n\n         \
        \   while (cost > (long) k) {\n                long[] last = dq.peekLast();\n\
        \                cost -= (last[0] - (long) nums[R]);\n                last[1]--;\n\
        \                if (last[1] == 0) {\n                    dq.pollLast();\n \
        \               }\n                R--;\n            }\n            total +=\
        \ (long) (R - L + 1);\n        }\n\n        return total;\n    }\n}"
      python: "from collections import deque\n\nclass Solution(object):\n    def countNonDecreasingSubarrays(self,\
        \ nums, k):\n        \"\"\"\n        :type nums: List[int]\n        :type k:\
        \ int\n        :rtype: int\n        \"\"\"\n        n = len(nums)\n        if\
        \ n == 0: return 0\n\n        total = 0\n        cost = 0\n        dq = deque()\
        \  # stores [value, count]\n\n        R = n - 1\n        dq.append([nums[n -\
        \ 1], 1])\n        total += 1\n\n        for L in range(n - 2, -1, -1):\n  \
        \          new_count = 0\n            while dq and dq[0][0] < nums[L]:\n   \
        \             val, count = dq.popleft()\n                cost += (nums[L] -\
        \ val) * count\n                new_count += count\n            dq.appendleft([nums[L],\
        \ new_count + 1])\n\n            while cost > k:\n                val = dq[-1][0]\n\
        \                cost -= (val - nums[R])\n                dq[-1][1] -= 1\n \
        \               if dq[-1][1] == 0:\n                    dq.pop()\n         \
        \       R -= 1\n            total += (R - L + 1)\n\n        return total"
      python3: "from collections import deque\nfrom typing import List\n\nclass Solution:\n\
        \    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:\n\
        \        n = len(nums)\n        if n == 0:\n            return 0\n\n       \
        \ total = 0\n        cost = 0\n        dq = deque()  # stores [value, count]\n\
        \        R = n - 1\n\n        for L in range(n - 1, -1, -1):\n            new_count\
        \ = 0\n            while dq and dq[0][0] < nums[L]:\n                val, count\
        \ = dq.popleft()\n                cost += (nums[L] - val) * count\n        \
        \        new_count += count\n\n            dq.appendleft([nums[L], new_count\
        \ + 1])\n\n            while cost > k:\n                val = dq[-1][0]\n  \
        \              cost -= (val - nums[R])\n                dq[-1][1] -= 1\n   \
        \             if dq[-1][1] == 0:\n                    dq.pop()\n           \
        \     R -= 1\n\n            total += (R - L + 1)\n\n        return total"
      c: "#include <stdlib.h>\n\ntypedef struct {\n    long long val;\n    int count;\n\
        } Node;\n\nlong long countNonDecreasingSubarrays(int* nums, int numsSize, int\
        \ k) {\n    int n = numsSize;\n    if (n == 0) return 0;\n\n    Node* dq = (Node*)malloc(sizeof(Node)\
        \ * (n + 1));\n    int head = n, tail = n;\n    long long cost = 0;\n    long\
        \ long total = 0;\n    int R = n - 1;\n\n    for (int L = n - 1; L >= 0; L--)\
        \ {\n        int new_count = 0;\n        while (head < tail && dq[head].val\
        \ < (long long)nums[L]) {\n            cost += ((long long)nums[L] - dq[head].val)\
        \ * (long long)dq[head].count;\n            new_count += dq[head].count;\n \
        \           head++;\n        }\n\n        dq[--head] = (Node){(long long)nums[L],\
        \ new_count + 1};\n\n        while (cost > (long long)k) {\n            long\
        \ long val = dq[tail - 1].val;\n            cost -= (val - (long long)nums[R]);\n\
        \            dq[tail - 1].count--;\n            if (dq[tail - 1].count == 0)\
        \ {\n                tail--;\n            }\n            R--;\n        }\n\n\
        \        total += (long long)(R - L + 1);\n    }\n\n    free(dq);\n    return\
        \ total;\n}"
      csharp: "public class Solution {\n    public struct Node {\n        public long\
        \ val;\n        public int count;\n    }\n\n    public long CountNonDecreasingSubarrays(int[]\
        \ nums, int k) {\n        int n = nums.Length;\n        if (n == 0) return 0;\n\
        \n        Node[] dq = new Node[n + 1];\n        int head = n, tail = n;\n  \
        \      long cost = 0;\n        long total = 0;\n        int R = n - 1;\n\n \
        \       for (int L = n - 1; L >= 0; L--) {\n            int newCount = 0;\n\
        \            while (head < tail && dq[head].val < (long)nums[L]) {\n       \
        \         cost += ((long)nums[L] - dq[head].val) * (long)dq[head].count;\n \
        \               newCount += dq[head].count;\n                head++;\n     \
        \       }\n\n            dq[--head] = new Node { val = (long)nums[L], count\
        \ = newCount + 1 };\n\n            while (cost > (long)k) {\n              \
        \  long val = dq[tail - 1].val;\n                cost -= (val - (long)nums[R]);\n\
        \                dq[tail - 1].count--;\n                if (dq[tail - 1].count\
        \ == 0) {\n                    tail--;\n                }\n                R--;\n\
        \            }\n\n            total += (long)(R - L + 1);\n        }\n\n   \
        \     return total;\n    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @param {number} k\n * @return\
        \ {number}\n */\nvar countNonDecreasingSubarrays = function(nums, k) {\n   \
        \ const n = nums.length;\n    if (n === 0) return 0;\n\n    let dq_val = new\
        \ Float64Array(n + 1);\n    let dq_count = new Int32Array(n + 1);\n    let head\
        \ = n, tail = n;\n    let cost = 0;\n    let total = 0;\n    let R = n - 1;\n\
        \n    for (let L = n - 1; L >= 0; L--) {\n        let newCount = 0;\n      \
        \  while (head < tail && dq_val[head] < nums[L]) {\n            cost += (nums[L]\
        \ - dq_val[head]) * dq_count[head];\n            newCount += dq_count[head];\n\
        \            head++;\n        }\n\n        dq_val[--head] = nums[L];\n     \
        \   dq_count[head] = newCount + 1;\n\n        while (cost > k) {\n         \
        \   let val = dq_val[tail - 1];\n            cost -= (val - nums[R]);\n    \
        \        dq_count[tail - 1]--;\n            if (dq_count[tail - 1] === 0) {\n\
        \                tail--;\n            }\n            R--;\n        }\n\n   \
        \     total += (R - L + 1);\n    }\n\n    return total;\n};"
      typescript: "function countNonDecreasingSubarrays(nums: number[], k: number):\
        \ number {\n    const n = nums.length;\n    let total = 0;\n    let cost = 0;\n\
        \    let R = n - 1;\n\n    const valArr = new Float64Array(2 * n + 1);\n   \
        \ const cntArr = new Float64Array(2 * n + 1);\n    let f = n;\n    let b = n\
        \ - 1;\n\n    for (let L = n - 1; L >= 0; L--) {\n        let newCount = 0;\n\
        \        while (f <= b && valArr[f] < nums[L]) {\n            const v = valArr[f];\n\
        \            const c = cntArr[f];\n            f++;\n            cost += (nums[L]\
        \ - v) * c;\n            newCount += c;\n        }\n\n        f--;\n       \
        \ valArr[f] = nums[L];\n        cntArr[f] = newCount + 1;\n\n        while (cost\
        \ > k) {\n            const v = valArr[b];\n            cost -= (v - nums[R]);\n\
        \            cntArr[b]--;\n            if (cntArr[b] === 0) {\n            \
        \    b--;\n            }\n            R--;\n        }\n\n        total += (R\
        \ - L + 1);\n    }\n\n    return total;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @param\
        \ Integer $k\n     * @return Integer\n     */\n    function countNonDecreasingSubarrays($nums,\
        \ $k) {\n        $n = count($nums);\n        $total = 0;\n        $cost = 0;\n\
        \        $R = $n - 1;\n        $dq = new SplDoublyLinkedList();\n\n        for\
        \ ($L = $n - 1; $L >= 0; $L--) {\n            $newCount = 0;\n            while\
        \ (!$dq->isEmpty() && $dq->bottom()[0] < $nums[$L]) {\n                $pair\
        \ = $dq->shift();\n                $v = $pair[0];\n                $c = $pair[1];\n\
        \                $cost += ($nums[$L] - $v) * $c;\n                $newCount\
        \ += $c;\n            }\n\n            $dq->unshift([$nums[$L], $newCount +\
        \ 1]);\n\n            while ($cost > $k) {\n                $pair = $dq->top();\n\
        \                $v = $pair[0];\n                $cost -= ($v - $nums[$R]);\n\
        \                $pair[1]--;\n                if ($pair[1] == 0) {\n       \
        \             $dq->pop();\n                } else {\n                    $dq->offsetSet($dq->count()\
        \ - 1, $pair);\n                }\n                $R--;\n            }\n\n\
        \            $total += ($R - $L + 1);\n        }\n\n        return $total;\n\
        \    }\n}"
      swift: "class Solution {\n    func countNonDecreasingSubarrays(_ nums: [Int],\
        \ _ k: Int) -> Int {\n        let n = nums.count\n        var total = 0\n  \
        \      var cost = 0\n        var R = n - 1\n\n        var valArr = [Int](repeating:\
        \ 0, count: 2 * n + 1)\n        var cntArr = [Int](repeating: 0, count: 2 *\
        \ n + 1)\n        var f = n\n        var b = n - 1\n\n        for L in stride(from:\
        \ n - 1, through: 0, by: -1) {\n            var newCount = 0\n            while\
        \ f <= b && valArr[f] < nums[L] {\n                let v = valArr[f]\n     \
        \           let c = cntArr[f]\n                f += 1\n                cost\
        \ += (nums[L] - v) * c\n                newCount += c\n            }\n\n   \
        \         f -= 1\n            valArr[f] = nums[L]\n            cntArr[f] = newCount\
        \ + 1\n\n            while cost > k {\n                let v = valArr[b]\n \
        \               cost -= (v - nums[R])\n                cntArr[b] -= 1\n    \
        \            if cntArr[b] == 0 {\n                    b -= 1\n             \
        \   }\n                R -= 1\n            }\n\n            total += (R - L\
        \ + 1)\n        }\n\n        return total\n    }\n}"
      kotlin: "class Solution {\n    fun countNonDecreasingSubarrays(nums: IntArray,\
        \ k: Int): Long {\n        val n = nums.size\n        var total: Long = 0\n\
        \        var cost: Long = 0\n        var R = n - 1\n\n        val dq = java.util.ArrayDeque<Node>()\n\
        \n        for (L in n - 1 downTo 0) {\n            var newCount: Long = 0\n\
        \            while (dq.isNotEmpty() && dq.peekFirst().value < nums[L]) {\n \
        \               val node = dq.removeFirst()\n                cost += (nums[L].toLong()\
        \ - node.value) * node.count\n                newCount += node.count\n     \
        \       }\n\n            dq.addFirst(Node(nums[L].toLong(), newCount + 1))\n\
        \n            while (cost > k) {\n                val node = dq.peekLast()\n\
        \                cost -= (node.value - nums[R].toLong())\n                node.count\
        \ -= 1\n                if (node.count == 0L) {\n                    dq.removeLast()\n\
        \                }\n                R--\n            }\n\n            total\
        \ += (R - L + 1).toLong()\n        }\n\n        return total\n    }\n\n    class\
        \ Node(val value: Long, var count: Long)\n}"
      dart: "import 'dart:collection';\n\nclass Solution {\n  int countNonDecreasingSubarrays(List<int>\
        \ nums, int k) {\n    int n = nums.length;\n    if (n == 0) return 0;\n\n  \
        \  int total = 0;\n    int cost = 0;\n    ListQueue<List<int>> dq = ListQueue<List<int>>();\n\
        \    int r = n - 1;\n\n    for (int l = n - 1; l >= 0; l--) {\n      int newCount\
        \ = 1;\n      while (dq.isNotEmpty && dq.first[0] < nums[l]) {\n        List<int>\
        \ first = dq.removeFirst();\n        cost += (nums[l] - first[0]) * first[1];\n\
        \        newCount += first[1];\n      }\n      dq.addFirst([nums[l], newCount]);\n\
        \n      while (cost > k) {\n        List<int> last = dq.last;\n        cost\
        \ -= (last[0] - nums[r]);\n        last[1]--;\n        if (last[1] == 0) {\n\
        \          dq.removeLast();\n        }\n        r -= 1;\n      }\n      total\
        \ += (r - l + 1);\n    }\n    return total;\n  }\n}"
      go: "func countNonDecreasingSubarrays(nums []int, k int) int64 {\n\tn := len(nums)\n\
        \tif n == 0 {\n\t\treturn 0\n\t}\n\n\tvar total int64 = 0\n\tvar cost int64\
        \ = 0\n\n\ttype pair struct {\n\t\tval   int\n\t\tcount int\n\t}\n\n\tdq :=\
        \ make([]pair, n+1)\n\thead := n\n\ttail := n\n\tr := n - 1\n\tk64 := int64(k)\n\
        \n\tfor l := n - 1; l >= 0; l-- {\n\t\tnewCount := 1\n\t\tfor head < tail &&\
        \ dq[head].val < nums[l] {\n\t\t\tv := dq[head].val\n\t\t\tc := dq[head].count\n\
        \t\t\tcost += int64(nums[l]-v) * int64(c)\n\t\t\tnewCount += c\n\t\t\thead++\n\
        \t\t}\n\t\thead--\n\t\tdq[head] = pair{nums[l], newCount}\n\n\t\tfor cost >\
        \ k64 {\n\t\t\tv := dq[tail-1].val\n\t\t\tcost -= int64(v - nums[r])\n\t\t\t\
        dq[tail-1].count--\n\t\t\tif dq[tail-1].count == 0 {\n\t\t\t\ttail--\n\t\t\t\
        }\n\t\t\tr--\n\t\t}\n\t\ttotal += int64(r - l + 1)\n\t}\n\n\treturn total\n}"
      ruby: "# @param {Integer[]} nums\n# @param {Integer} k\n# @return {Integer}\n\
        def count_non_decreasing_subarrays(nums, k)\n  n = nums.length\n  return 0 if\
        \ n == 0\n\n  total = 0\n  cost = 0\n  dq = []\n  r = n - 1\n\n  (n - 1).step(0,\
        \ -1) do |l|\n    new_count = 1\n    while !dq.empty? && dq.first[0] < nums[l]\n\
        \      pair = dq.shift\n      val = pair[0]\n      count = pair[1]\n      cost\
        \ += (nums[l] - val) * count\n      new_count += count\n    end\n    dq.unshift([nums[l],\
        \ new_count])\n\n    while cost > k\n      last_pair = dq.last\n      val =\
        \ last_pair[0]\n      cost -= (val - nums[r])\n      last_pair[1] -= 1\n   \
        \   dq.pop if last_pair[1] == 0\n      r -= 1\n    end\n    total += (r - l\
        \ + 1)\n  end\n  total\nend"
      scala: "import scala.collection.mutable\n\nobject Solution {\n  class Pair(val\
        \ v: Long, var c: Long)\n\n  def countNonDecreasingSubarrays(nums: Array[Int],\
        \ k: Int): Long = {\n    val n = nums.length\n    if (n == 0) return 0L\n\n\
        \    var total: Long = 0L\n    var cost: Long = 0L\n    val dq = new mutable.ArrayDeque[Pair]()\n\
        \    var r = n - 1\n\n    var l = n - 1\n    while (l >= 0) {\n      var newCount:\
        \ Long = 1L\n      while (dq.nonEmpty && dq.head.v < nums(l).toLong) {\n   \
        \     val first = dq.removeHead()\n        cost += (nums(l).toLong - first.v)\
        \ * first.c\n        newCount += first.c\n      }\n      dq.prepend(new Pair(nums(l).toLong,\
        \ newCount))\n\n      while (cost > k.toLong) {\n        val lastPair = dq.last\n\
        \        cost -= (lastPair.v - nums(r).toLong)\n        lastPair.c -= 1L\n \
        \       if (lastPair.c == 0L) {\n          dq.removeLast()\n        }\n    \
        \    r -= 1\n      }\n      total += (r - l + 1).toLong\n      l -= 1\n    }\n\
        \    total\n  }\n}"
      rust: "use std::collections::VecDeque;\n\nimpl Solution {\n    pub fn count_non_decreasing_subarrays(nums:\
        \ Vec<i32>, k: i32) -> i64 {\n        let n = nums.len();\n        if n == 0\
        \ {\n            return 0;\n        }\n        let k_long = k as i64;\n    \
        \    let mut total: i64 = 0;\n        let mut cost: i64 = 0;\n        let mut\
        \ dq: VecDeque<(i64, i64)> = VecDeque::new();\n        let mut r = n - 1;\n\n\
        \        for l in (0..n).rev() {\n            let cur = nums[l] as i64;\n  \
        \          let mut new_count: i64 = 1;\n            while let Some(&(v, c))\
        \ = dq.front() {\n                if v < cur {\n                    cost +=\
        \ (cur - v) * c;\n                    new_count += c;\n                    dq.pop_front();\n\
        \                } else {\n                    break;\n                }\n \
        \           }\n            dq.push_front((cur, new_count));\n\n            while\
        \ cost > k_long {\n                if let Some(&(v, c)) = dq.back() {\n    \
        \                cost -= v - nums[r] as i64;\n                    if c > 1 {\n\
        \                        if let Some(pair) = dq.back_mut() {\n             \
        \               pair.1 -= 1;\n                        }\n                  \
        \  } else {\n                        dq.pop_back();\n                    }\n\
        \                }\n                if r == 0 {\n                    break;\n\
        \                }\n                r -= 1;\n            }\n            total\
        \ += (r - l + 1) as i64;\n        }\n        total\n    }\n}"
      racket: "(define/contract (count-non-decreasing-subarrays nums k)\n  (-> (listof\
        \ exact-integer?) exact-integer? exact-integer?)\n  (let* ([nums-vec (list->vector\
        \ nums)]\n         [n (vector-length nums-vec)]\n         [dq-v (make-vector\
        \ (+ n 1))]\n         [dq-c (make-vector (+ n 1))]\n         [head n]\n    \
        \     [tail n]\n         [cost 0]\n         [total 0]\n         [r (- n 1)])\n\
        \    (for ([l (in-range (- n 1) -1 -1)])\n      (let ([cur (vector-ref nums-vec\
        \ l)]\n            [new-count 1])\n        (let loop-left ()\n          (when\
        \ (and (< head tail) (< (vector-ref dq-v head) cur))\n            (let ([v (vector-ref\
        \ dq-v head)]\n                  [c (vector-ref dq-c head)])\n             \
        \ (set! cost (+ cost (* (- cur v) c)))\n              (set! new-count (+ new-count\
        \ c))\n              (set! head (+ head 1))\n              (loop-left))))\n\
        \        (set! head (- head 1))\n        (vector-set! dq-v head cur)\n     \
        \   (vector-set! dq-c head new-count)\n        (let loop-right ()\n        \
        \  (when (> cost k)\n            (let* ([v (vector-ref dq-v (- tail 1))]\n \
        \                  [c (vector-ref dq-c (- tail 1))])\n              (set! cost\
        \ (- cost (- v (vector-ref nums-vec r))))\n              (if (> c 1)\n     \
        \             (vector-set! dq-c (- tail 1) (- c 1))\n                  (set!\
        \ tail (- tail 1)))\n              (set! r (- r 1))\n              (loop-right))))\n\
        \        (set! total (+ total (- r l -1)))))\n    total))"
      erlang: "-spec count_non_decreasing_subarrays(Nums :: [integer()], K :: integer())\
        \ -> integer().\ncount_non_decreasing_subarrays(Nums, K) ->\n  NumsArr = list_to_tuple(Nums),\n\
        \  N = tuple_size(NumsArr),\n  solve(N - 1, N - 1, 0, 0, queue:new(), NumsArr,\
        \ K).\n\nsolve(L, R, Cost, Total, Dq, NumsArr, K) when L >= 0 ->\n  Cur = element(L\
        \ + 1, NumsArr),\n  {NewDq, NewCost, NewCount} = process_left(Cur, Dq, Cost,\
        \ 1),\n  AddedDq = queue:in_r({Cur, NewCount}, NewDq),\n  {FinalDq, FinalCost,\
        \ FinalR} = process_right(AddedDq, NewCost, R, NumsArr, K),\n  solve(L - 1,\
        \ FinalR, FinalCost, Total + (FinalR - L + 1), FinalDq, NumsArr, K);\nsolve(_,\
        \ _, _, Total, _, _, _) ->\n  Total.\n\nprocess_left(Cur, Dq, Cost, Count) ->\n\
        \  case queue:out(Dq) of\n    {{value, {V, C}}, Rest} when V < Cur ->\n    \
        \  process_left(Cur, Rest, Cost + (Cur - V) * C, Count + C);\n    _ ->\n   \
        \   {Dq, Cost, Count}\n  end.\n\nprocess_right(Dq, Cost, R, NumsArr, K) when\
        \ Cost > K ->\n  {{value, {V, C}}, Rest} = queue:out_r(Dq),\n  NewCost = Cost\
        \ - (V - element(R + 1, NumsArr)),\n  if C > 1 ->\n    process_right(queue:in({V,\
        \ C - 1}, Rest), NewCost, R - 1, NumsArr, K);\n  true ->\n    process_right(Rest,\
        \ NewCost, R - 1, NumsArr, K)\n  end;\nprocess_right(Dq, Cost, R, _, _) ->\n\
        \  {Dq, Cost, R}."
      elixir: "defmodule Solution do\n  @spec count_non_decreasing_subarrays(nums ::\
        \ [integer], k :: integer) :: integer\n  def count_non_decreasing_subarrays(nums,\
        \ k) do\n    nums_tuple = List.to_tuple(nums)\n    n = tuple_size(nums_tuple)\n\
        \    solve(n - 1, n - 1, 0, 0, :queue.new(), nums_tuple, k)\n  end\n\n  defp\
        \ solve(l, r, cost, total, dq, nums_tuple, k) when l >= 0 do\n    cur = elem(nums_tuple,\
        \ l)\n    {new_dq, new_cost, new_count} = process_left(cur, dq, cost, 1)\n \
        \   added_dq = :queue.in_r({cur, new_count}, new_dq)\n    {final_dq, final_cost,\
        \ final_r} = process_right(added_dq, new_cost, r, nums_tuple, k)\n    solve(l\
        \ - 1, final_r, final_cost, total + (final_r - l + 1), final_dq, nums_tuple,\
        \ k)\n  end\n\n  defp solve(_l, _r, _cost, total, _dq, _nums_tuple, _k), do:\
        \ total\n\n  defp process_left(cur, dq, cost, count) do\n    case :queue.out(dq)\
        \ do\n      {{:value, {v, c}}, rest} when v < cur ->\n        process_left(cur,\
        \ rest, cost + (cur - v) * c, count + c)\n      _ ->\n        {dq, cost, count}\n\
        \    end\n  end\n\n  defp process_right(dq, cost, r, nums_tuple, k) when cost\
        \ > k do\n    {{:value, {v, c}}, rest} = :queue.out_r(dq)\n    new_cost = cost\
        \ - (v - elem(nums_tuple, r))\n    if c > 1 do\n      process_right(:queue.in({v,\
        \ c - 1}, rest), new_cost, r - 1, nums_tuple, k)\n    else\n      process_right(rest,\
        \ new_cost, r - 1, nums_tuple, k)\n    end\n  end\n\n  defp process_right(dq,\
        \ cost, r, _nums_tuple, _k), do: {dq, cost, r}\nend"
    approach: 'The problem can be modeled as finding the number of subarrays $[L, R]$
      such that the minimum number of operations to make them non-decreasing is at most
      $k$. The cost to make a subarray $nums[L \dots R]$ non-decreasing is given by
      $\sum_{i=L}^R (M_i - nums[i])$, where $M_i = \max(nums[L \dots i])$ are the prefix
      maximums of the subarray starting from $L$. This cost function is monotonic: it
      increases as $R$ increases and decreases as $L$ increases. Thus, we can utilize
      a two-pointer sliding window where we iterate with the left pointer $L$ from right
      to left (from $n-1$ down to 0) and maintain the largest possible right pointer
      $R$ such that the cost remains within $k$.


      To efficiently update the cost as $L$ moves to the left, we use a monotonic deque
      to store the values and frequencies of the current prefix maximums $M_i$ in the
      window $[L, R]$. When $L$ decreases, the value $nums[L-1]$ becomes the new prefix
      maximum for a certain range starting at $L-1$, potentially overriding previous
      $M_i$ values that were smaller than $nums[L-1]$. The monotonic deque allows us
      to pop these smaller values from the front and update the total cost accordingly.
      Conversely, when the cost exceeds $k$, we decrement $R$, using the value from
      the back of the deque to subtract $(M_R - nums[R])$ from the current cost. The
      total count of valid subarrays is calculated as the sum of the lengths of these
      valid windows $(R - L + 1)$ for each starting position $L$.'
    time_complexity: O(n) where n is the length of the input array. Each pointer (L
      and R) traverses the array at most once, and every element is added to and removed
      from the monotonic deque at most once.
    space_complexity: O(n) to store the monotonic deque and the original array in the
      case of some languages, which is the space required to maintain the window state.
    elapsed_time: 338.64296221733093
    model: gemini-3-flash-preview
    generated_at: '2026-11-13 04:31:42 '
---

## Problem #3420: Count Non-Decreasing Subarrays After K Operations

**Difficulty:** Hard

**Topics:** Array, Stack, Segment Tree, Queue, Sliding Window, Monotonic Stack, Monotonic Queue

## Problem Description

<p>You are given an array <code>nums</code> of <code>n</code> integers and an integer <code>k</code>.</p>

<p>For each subarray of <code>nums</code>, you can apply <strong>up to</strong> <code>k</code> operations on it. In each operation, you increment any element of the subarray by 1.</p>

<p><strong>Note</strong> that each subarray is considered independently, meaning changes made to one subarray do not persist to another.</p>

<p>Return the number of subarrays that you can make <strong>non-decreasing</strong> ​​​​​after performing at most <code>k</code> operations.</p>

<p>An array is said to be <strong>non-decreasing</strong> if each element is greater than or equal to its previous element, if it exists.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [6,3,1,2,4,4], k = 7</span></p>

<p><strong>Output:</strong> <span class="example-io">17</span></p>

<p><strong>Explanation:</strong></p>

<p>Out of all 21 possible subarrays of <code>nums</code>, only the subarrays <code>[6, 3, 1]</code>, <code>[6, 3, 1, 2]</code>, <code>[6, 3, 1, 2, 4]</code> and <code>[6, 3, 1, 2, 4, 4]</code> cannot be made non-decreasing after applying up to k = 7 operations. Thus, the number of non-decreasing subarrays is <code>21 - 4 = 17</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [6,3,1,3,6], k = 4</span></p>

<p><strong>Output:</strong> <span class="example-io">12</span></p>

<p><strong>Explanation:</strong></p>

<p>The subarray <code>[3, 1, 3, 6]</code> along with all subarrays of <code>nums</code> with three or fewer elements, except <code>[6, 3, 1]</code>, can be made non-decreasing after <code>k</code> operations. There are 5 subarrays of a single element, 4 subarrays of two elements, and 2 subarrays of three elements except <code>[6, 3, 1]</code>, so there are <code>1 + 5 + 4 + 2 = 12</code> subarrays that can be made non-decreasing.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>9</sup></code></li>
</ul>


## Hints

1. Use a sparse table.

2. Compute `sp[e][i] = [lastElement, operations]` where `operations` is the number of `operations` required to make the subarray `nums[i...i + 2^e - 1]` non-decreasing, and `lastElement` be the value of the last element after the operations were applied on it.

3. How can we combine `sp[a][i]` with `sp[b][i + 2^a]` to find the answer for the subarray `nums[i...i + 2^a + 2^b - 1]`?

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem can be modeled as finding the number of subarrays $[L, R]$ such that the minimum number of operations to make them non-decreasing is at most $k$. The cost to make a subarray $nums[L \dots R]$ non-decreasing is given by $\sum_{i=L}^R (M_i - nums[i])$, where $M_i = \max(nums[L \dots i])$ are the prefix maximums of the subarray starting from $L$. This cost function is monotonic: it increases as $R$ increases and decreases as $L$ increases. Thus, we can utilize a two-pointer sliding window where we iterate with the left pointer $L$ from right to left (from $n-1$ down to 0) and maintain the largest possible right pointer $R$ such that the cost remains within $k$.

To efficiently update the cost as $L$ moves to the left, we use a monotonic deque to store the values and frequencies of the current prefix maximums $M_i$ in the window $[L, R]$. When $L$ decreases, the value $nums[L-1]$ becomes the new prefix maximum for a certain range starting at $L-1$, potentially overriding previous $M_i$ values that were smaller than $nums[L-1]$. The monotonic deque allows us to pop these smaller values from the front and update the total cost accordingly. Conversely, when the cost exceeds $k$, we decrement $R$, using the value from the back of the deque to subtract $(M_R - nums[R])$ from the current cost. The total count of valid subarrays is calculated as the sum of the lengths of these valid windows $(R - L + 1)$ for each starting position $L$.

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
    long long countNonDecreasingSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        if (n == 0) return 0;
        long long total = 0;
        long long cost = 0;
        struct Element {
            long long val;
            long long count;
        };
        std::deque<Element> dq;

        int R = n - 1;
        dq.push_back({(long long)nums[n - 1], 1});
        total += 1;

        for (int L = n - 2; L >= 0; --L) {
            long long new_count = 0;
            while (!dq.empty() && dq.front().val < (long long)nums[L]) {
                cost += (long long)(nums[L] - dq.front().val) * dq.front().count;
                new_count += dq.front().count;
                dq.pop_front();
            }
            dq.push_front({(long long)nums[L], new_count + 1});

            while (cost > (long long)k) {
                long long v = dq.back().val;
                cost -= (v - (long long)nums[R]);
                dq.back().count--;
                if (dq.back().count == 0) {
                    dq.pop_back();
                }
                R--;
            }
            total += (long long)(R - L + 1);
        }

        return total;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public long countNonDecreasingSubarrays(int[] nums, int k) {
        int n = nums.length;
        if (n == 0) return 0;
        long total = 0;
        long cost = 0;
        java.util.Deque<long[]> dq = new java.util.ArrayDeque<>();

        int R = n - 1;
        dq.addLast(new long[]{(long) nums[n - 1], 1L});
        total += 1;

        for (int L = n - 2; L >= 0; --L) {
            long newCount = 0;
            while (!dq.isEmpty() && dq.peekFirst()[0] < (long) nums[L]) {
                long[] first = dq.pollFirst();
                cost += (long) (nums[L] - first[0]) * first[1];
                newCount += first[1];
            }
            dq.addFirst(new long[]{(long) nums[L], newCount + 1L});

            while (cost > (long) k) {
                long[] last = dq.peekLast();
                cost -= (last[0] - (long) nums[R]);
                last[1]--;
                if (last[1] == 0) {
                    dq.pollLast();
                }
                R--;
            }
            total += (long) (R - L + 1);
        }

        return total;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
from collections import deque

class Solution(object):
    def countNonDecreasingSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if n == 0: return 0

        total = 0
        cost = 0
        dq = deque()  # stores [value, count]

        R = n - 1
        dq.append([nums[n - 1], 1])
        total += 1

        for L in range(n - 2, -1, -1):
            new_count = 0
            while dq and dq[0][0] < nums[L]:
                val, count = dq.popleft()
                cost += (nums[L] - val) * count
                new_count += count
            dq.appendleft([nums[L], new_count + 1])

            while cost > k:
                val = dq[-1][0]
                cost -= (val - nums[R])
                dq[-1][1] -= 1
                if dq[-1][1] == 0:
                    dq.pop()
                R -= 1
            total += (R - L + 1)

        return total
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
from collections import deque
from typing import List

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 0:
            return 0

        total = 0
        cost = 0
        dq = deque()  # stores [value, count]
        R = n - 1

        for L in range(n - 1, -1, -1):
            new_count = 0
            while dq and dq[0][0] < nums[L]:
                val, count = dq.popleft()
                cost += (nums[L] - val) * count
                new_count += count

            dq.appendleft([nums[L], new_count + 1])

            while cost > k:
                val = dq[-1][0]
                cost -= (val - nums[R])
                dq[-1][1] -= 1
                if dq[-1][1] == 0:
                    dq.pop()
                R -= 1

            total += (R - L + 1)

        return total
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>

typedef struct {
    long long val;
    int count;
} Node;

long long countNonDecreasingSubarrays(int* nums, int numsSize, int k) {
    int n = numsSize;
    if (n == 0) return 0;

    Node* dq = (Node*)malloc(sizeof(Node) * (n + 1));
    int head = n, tail = n;
    long long cost = 0;
    long long total = 0;
    int R = n - 1;

    for (int L = n - 1; L >= 0; L--) {
        int new_count = 0;
        while (head < tail && dq[head].val < (long long)nums[L]) {
            cost += ((long long)nums[L] - dq[head].val) * (long long)dq[head].count;
            new_count += dq[head].count;
            head++;
        }

        dq[--head] = (Node){(long long)nums[L], new_count + 1};

        while (cost > (long long)k) {
            long long val = dq[tail - 1].val;
            cost -= (val - (long long)nums[R]);
            dq[tail - 1].count--;
            if (dq[tail - 1].count == 0) {
                tail--;
            }
            R--;
        }

        total += (long long)(R - L + 1);
    }

    free(dq);
    return total;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public struct Node {
        public long val;
        public int count;
    }

    public long CountNonDecreasingSubarrays(int[] nums, int k) {
        int n = nums.Length;
        if (n == 0) return 0;

        Node[] dq = new Node[n + 1];
        int head = n, tail = n;
        long cost = 0;
        long total = 0;
        int R = n - 1;

        for (int L = n - 1; L >= 0; L--) {
            int newCount = 0;
            while (head < tail && dq[head].val < (long)nums[L]) {
                cost += ((long)nums[L] - dq[head].val) * (long)dq[head].count;
                newCount += dq[head].count;
                head++;
            }

            dq[--head] = new Node { val = (long)nums[L], count = newCount + 1 };

            while (cost > (long)k) {
                long val = dq[tail - 1].val;
                cost -= (val - (long)nums[R]);
                dq[tail - 1].count--;
                if (dq[tail - 1].count == 0) {
                    tail--;
                }
                R--;
            }

            total += (long)(R - L + 1);
        }

        return total;
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
 * @param {number} k
 * @return {number}
 */
var countNonDecreasingSubarrays = function(nums, k) {
    const n = nums.length;
    if (n === 0) return 0;

    let dq_val = new Float64Array(n + 1);
    let dq_count = new Int32Array(n + 1);
    let head = n, tail = n;
    let cost = 0;
    let total = 0;
    let R = n - 1;

    for (let L = n - 1; L >= 0; L--) {
        let newCount = 0;
        while (head < tail && dq_val[head] < nums[L]) {
            cost += (nums[L] - dq_val[head]) * dq_count[head];
            newCount += dq_count[head];
            head++;
        }

        dq_val[--head] = nums[L];
        dq_count[head] = newCount + 1;

        while (cost > k) {
            let val = dq_val[tail - 1];
            cost -= (val - nums[R]);
            dq_count[tail - 1]--;
            if (dq_count[tail - 1] === 0) {
                tail--;
            }
            R--;
        }

        total += (R - L + 1);
    }

    return total;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function countNonDecreasingSubarrays(nums: number[], k: number): number {
    const n = nums.length;
    let total = 0;
    let cost = 0;
    let R = n - 1;

    const valArr = new Float64Array(2 * n + 1);
    const cntArr = new Float64Array(2 * n + 1);
    let f = n;
    let b = n - 1;

    for (let L = n - 1; L >= 0; L--) {
        let newCount = 0;
        while (f <= b && valArr[f] < nums[L]) {
            const v = valArr[f];
            const c = cntArr[f];
            f++;
            cost += (nums[L] - v) * c;
            newCount += c;
        }

        f--;
        valArr[f] = nums[L];
        cntArr[f] = newCount + 1;

        while (cost > k) {
            const v = valArr[b];
            cost -= (v - nums[R]);
            cntArr[b]--;
            if (cntArr[b] === 0) {
                b--;
            }
            R--;
        }

        total += (R - L + 1);
    }

    return total;
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
     * @param Integer $k
     * @return Integer
     */
    function countNonDecreasingSubarrays($nums, $k) {
        $n = count($nums);
        $total = 0;
        $cost = 0;
        $R = $n - 1;
        $dq = new SplDoublyLinkedList();

        for ($L = $n - 1; $L >= 0; $L--) {
            $newCount = 0;
            while (!$dq->isEmpty() && $dq->bottom()[0] < $nums[$L]) {
                $pair = $dq->shift();
                $v = $pair[0];
                $c = $pair[1];
                $cost += ($nums[$L] - $v) * $c;
                $newCount += $c;
            }

            $dq->unshift([$nums[$L], $newCount + 1]);

            while ($cost > $k) {
                $pair = $dq->top();
                $v = $pair[0];
                $cost -= ($v - $nums[$R]);
                $pair[1]--;
                if ($pair[1] == 0) {
                    $dq->pop();
                } else {
                    $dq->offsetSet($dq->count() - 1, $pair);
                }
                $R--;
            }

            $total += ($R - $L + 1);
        }

        return $total;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func countNonDecreasingSubarrays(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        var total = 0
        var cost = 0
        var R = n - 1

        var valArr = [Int](repeating: 0, count: 2 * n + 1)
        var cntArr = [Int](repeating: 0, count: 2 * n + 1)
        var f = n
        var b = n - 1

        for L in stride(from: n - 1, through: 0, by: -1) {
            var newCount = 0
            while f <= b && valArr[f] < nums[L] {
                let v = valArr[f]
                let c = cntArr[f]
                f += 1
                cost += (nums[L] - v) * c
                newCount += c
            }

            f -= 1
            valArr[f] = nums[L]
            cntArr[f] = newCount + 1

            while cost > k {
                let v = valArr[b]
                cost -= (v - nums[R])
                cntArr[b] -= 1
                if cntArr[b] == 0 {
                    b -= 1
                }
                R -= 1
            }

            total += (R - L + 1)
        }

        return total
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun countNonDecreasingSubarrays(nums: IntArray, k: Int): Long {
        val n = nums.size
        var total: Long = 0
        var cost: Long = 0
        var R = n - 1

        val dq = java.util.ArrayDeque<Node>()

        for (L in n - 1 downTo 0) {
            var newCount: Long = 0
            while (dq.isNotEmpty() && dq.peekFirst().value < nums[L]) {
                val node = dq.removeFirst()
                cost += (nums[L].toLong() - node.value) * node.count
                newCount += node.count
            }

            dq.addFirst(Node(nums[L].toLong(), newCount + 1))

            while (cost > k) {
                val node = dq.peekLast()
                cost -= (node.value - nums[R].toLong())
                node.count -= 1
                if (node.count == 0L) {
                    dq.removeLast()
                }
                R--
            }

            total += (R - L + 1).toLong()
        }

        return total
    }

    class Node(val value: Long, var count: Long)
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
import 'dart:collection';

class Solution {
  int countNonDecreasingSubarrays(List<int> nums, int k) {
    int n = nums.length;
    if (n == 0) return 0;

    int total = 0;
    int cost = 0;
    ListQueue<List<int>> dq = ListQueue<List<int>>();
    int r = n - 1;

    for (int l = n - 1; l >= 0; l--) {
      int newCount = 1;
      while (dq.isNotEmpty && dq.first[0] < nums[l]) {
        List<int> first = dq.removeFirst();
        cost += (nums[l] - first[0]) * first[1];
        newCount += first[1];
      }
      dq.addFirst([nums[l], newCount]);

      while (cost > k) {
        List<int> last = dq.last;
        cost -= (last[0] - nums[r]);
        last[1]--;
        if (last[1] == 0) {
          dq.removeLast();
        }
        r -= 1;
      }
      total += (r - l + 1);
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
func countNonDecreasingSubarrays(nums []int, k int) int64 {
	n := len(nums)
	if n == 0 {
		return 0
	}

	var total int64 = 0
	var cost int64 = 0

	type pair struct {
		val   int
		count int
	}

	dq := make([]pair, n+1)
	head := n
	tail := n
	r := n - 1
	k64 := int64(k)

	for l := n - 1; l >= 0; l-- {
		newCount := 1
		for head < tail && dq[head].val < nums[l] {
			v := dq[head].val
			c := dq[head].count
			cost += int64(nums[l]-v) * int64(c)
			newCount += c
			head++
		}
		head--
		dq[head] = pair{nums[l], newCount}

		for cost > k64 {
			v := dq[tail-1].val
			cost -= int64(v - nums[r])
			dq[tail-1].count--
			if dq[tail-1].count == 0 {
				tail--
			}
			r--
		}
		total += int64(r - l + 1)
	}

	return total
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def count_non_decreasing_subarrays(nums, k)
  n = nums.length
  return 0 if n == 0

  total = 0
  cost = 0
  dq = []
  r = n - 1

  (n - 1).step(0, -1) do |l|
    new_count = 1
    while !dq.empty? && dq.first[0] < nums[l]
      pair = dq.shift
      val = pair[0]
      count = pair[1]
      cost += (nums[l] - val) * count
      new_count += count
    end
    dq.unshift([nums[l], new_count])

    while cost > k
      last_pair = dq.last
      val = last_pair[0]
      cost -= (val - nums[r])
      last_pair[1] -= 1
      dq.pop if last_pair[1] == 0
      r -= 1
    end
    total += (r - l + 1)
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
  class Pair(val v: Long, var c: Long)

  def countNonDecreasingSubarrays(nums: Array[Int], k: Int): Long = {
    val n = nums.length
    if (n == 0) return 0L

    var total: Long = 0L
    var cost: Long = 0L
    val dq = new mutable.ArrayDeque[Pair]()
    var r = n - 1

    var l = n - 1
    while (l >= 0) {
      var newCount: Long = 1L
      while (dq.nonEmpty && dq.head.v < nums(l).toLong) {
        val first = dq.removeHead()
        cost += (nums(l).toLong - first.v) * first.c
        newCount += first.c
      }
      dq.prepend(new Pair(nums(l).toLong, newCount))

      while (cost > k.toLong) {
        val lastPair = dq.last
        cost -= (lastPair.v - nums(r).toLong)
        lastPair.c -= 1L
        if (lastPair.c == 0L) {
          dq.removeLast()
        }
        r -= 1
      }
      total += (r - l + 1).toLong
      l -= 1
    }
    total
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
use std::collections::VecDeque;

impl Solution {
    pub fn count_non_decreasing_subarrays(nums: Vec<i32>, k: i32) -> i64 {
        let n = nums.len();
        if n == 0 {
            return 0;
        }
        let k_long = k as i64;
        let mut total: i64 = 0;
        let mut cost: i64 = 0;
        let mut dq: VecDeque<(i64, i64)> = VecDeque::new();
        let mut r = n - 1;

        for l in (0..n).rev() {
            let cur = nums[l] as i64;
            let mut new_count: i64 = 1;
            while let Some(&(v, c)) = dq.front() {
                if v < cur {
                    cost += (cur - v) * c;
                    new_count += c;
                    dq.pop_front();
                } else {
                    break;
                }
            }
            dq.push_front((cur, new_count));

            while cost > k_long {
                if let Some(&(v, c)) = dq.back() {
                    cost -= v - nums[r] as i64;
                    if c > 1 {
                        if let Some(pair) = dq.back_mut() {
                            pair.1 -= 1;
                        }
                    } else {
                        dq.pop_back();
                    }
                }
                if r == 0 {
                    break;
                }
                r -= 1;
            }
            total += (r - l + 1) as i64;
        }
        total
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (count-non-decreasing-subarrays nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  (let* ([nums-vec (list->vector nums)]
         [n (vector-length nums-vec)]
         [dq-v (make-vector (+ n 1))]
         [dq-c (make-vector (+ n 1))]
         [head n]
         [tail n]
         [cost 0]
         [total 0]
         [r (- n 1)])
    (for ([l (in-range (- n 1) -1 -1)])
      (let ([cur (vector-ref nums-vec l)]
            [new-count 1])
        (let loop-left ()
          (when (and (< head tail) (< (vector-ref dq-v head) cur))
            (let ([v (vector-ref dq-v head)]
                  [c (vector-ref dq-c head)])
              (set! cost (+ cost (* (- cur v) c)))
              (set! new-count (+ new-count c))
              (set! head (+ head 1))
              (loop-left))))
        (set! head (- head 1))
        (vector-set! dq-v head cur)
        (vector-set! dq-c head new-count)
        (let loop-right ()
          (when (> cost k)
            (let* ([v (vector-ref dq-v (- tail 1))]
                   [c (vector-ref dq-c (- tail 1))])
              (set! cost (- cost (- v (vector-ref nums-vec r))))
              (if (> c 1)
                  (vector-set! dq-c (- tail 1) (- c 1))
                  (set! tail (- tail 1)))
              (set! r (- r 1))
              (loop-right))))
        (set! total (+ total (- r l -1)))))
    total))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec count_non_decreasing_subarrays(Nums :: [integer()], K :: integer()) -> integer().
count_non_decreasing_subarrays(Nums, K) ->
  NumsArr = list_to_tuple(Nums),
  N = tuple_size(NumsArr),
  solve(N - 1, N - 1, 0, 0, queue:new(), NumsArr, K).

solve(L, R, Cost, Total, Dq, NumsArr, K) when L >= 0 ->
  Cur = element(L + 1, NumsArr),
  {NewDq, NewCost, NewCount} = process_left(Cur, Dq, Cost, 1),
  AddedDq = queue:in_r({Cur, NewCount}, NewDq),
  {FinalDq, FinalCost, FinalR} = process_right(AddedDq, NewCost, R, NumsArr, K),
  solve(L - 1, FinalR, FinalCost, Total + (FinalR - L + 1), FinalDq, NumsArr, K);
solve(_, _, _, Total, _, _, _) ->
  Total.

process_left(Cur, Dq, Cost, Count) ->
  case queue:out(Dq) of
    {{value, {V, C}}, Rest} when V < Cur ->
      process_left(Cur, Rest, Cost + (Cur - V) * C, Count + C);
    _ ->
      {Dq, Cost, Count}
  end.

process_right(Dq, Cost, R, NumsArr, K) when Cost > K ->
  {{value, {V, C}}, Rest} = queue:out_r(Dq),
  NewCost = Cost - (V - element(R + 1, NumsArr)),
  if C > 1 ->
    process_right(queue:in({V, C - 1}, Rest), NewCost, R - 1, NumsArr, K);
  true ->
    process_right(Rest, NewCost, R - 1, NumsArr, K)
  end;
process_right(Dq, Cost, R, _, _) ->
  {Dq, Cost, R}.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec count_non_decreasing_subarrays(nums :: [integer], k :: integer) :: integer
  def count_non_decreasing_subarrays(nums, k) do
    nums_tuple = List.to_tuple(nums)
    n = tuple_size(nums_tuple)
    solve(n - 1, n - 1, 0, 0, :queue.new(), nums_tuple, k)
  end

  defp solve(l, r, cost, total, dq, nums_tuple, k) when l >= 0 do
    cur = elem(nums_tuple, l)
    {new_dq, new_cost, new_count} = process_left(cur, dq, cost, 1)
    added_dq = :queue.in_r({cur, new_count}, new_dq)
    {final_dq, final_cost, final_r} = process_right(added_dq, new_cost, r, nums_tuple, k)
    solve(l - 1, final_r, final_cost, total + (final_r - l + 1), final_dq, nums_tuple, k)
  end

  defp solve(_l, _r, _cost, total, _dq, _nums_tuple, _k), do: total

  defp process_left(cur, dq, cost, count) do
    case :queue.out(dq) do
      {{:value, {v, c}}, rest} when v < cur ->
        process_left(cur, rest, cost + (cur - v) * c, count + c)
      _ ->
        {dq, cost, count}
    end
  end

  defp process_right(dq, cost, r, nums_tuple, k) when cost > k do
    {{:value, {v, c}}, rest} = :queue.out_r(dq)
    new_cost = cost - (v - elem(nums_tuple, r))
    if c > 1 do
      process_right(:queue.in({v, c - 1}, rest), new_cost, r - 1, nums_tuple, k)
    else
      process_right(rest, new_cost, r - 1, nums_tuple, k)
    end
  end

  defp process_right(dq, cost, r, _nums_tuple, _k), do: {dq, cost, r}
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where n is the length of the input array. Each pointer (L and R) traverses the array at most once, and every element is added to and removed from the monotonic deque at most once.
- **Space Complexity:** O(n) to store the monotonic deque and the original array in the case of some languages, which is the space required to maintain the window state.
