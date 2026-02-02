---
layout: post
title: "Divide an Array Into Subarrays With Minimum Cost II"
date: 2026-02-02 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Hash Table", "Sliding Window", "Heap (Priority Queue)"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/
ai_solutions:
  - solutions:
      cpp: '// Generation failed for C++

        // Reason: Parsing failed'
      java: '// Generation failed for Java

        // Reason: Parsing failed'
      python: '// Generation failed for Python

        // Reason: Parsing failed'
      python3: '// Generation failed for Python3

        // Reason: Parsing failed'
      c: '// Generation failed for C

        // Reason: Parsing failed'
      csharp: '// Generation failed for C#

        // Reason: Parsing failed'
      javascript: '// Generation failed for JavaScript

        // Reason: Parsing failed'
      typescript: "function minimumCost(nums: number[], k: number, dist: number): number\
        \ {\n    const n = nums.length;\n    const sub = nums.slice(1);\n    const sortedSub\
        \ = [...sub].sort((a, b) => a - b);\n    const unique: number[] = [];\n    if\
        \ (sortedSub.length > 0) {\n        unique.push(sortedSub[0]);\n        for\
        \ (let i = 1; i < sortedSub.length; i++) {\n            if (sortedSub[i] !==\
        \ sortedSub[i - 1]) unique.push(sortedSub[i]);\n        }\n    }\n\n    const\
        \ uSize = unique.length;\n    const map = new Map<number, number>();\n    unique.forEach((v,\
        \ i) => map.set(v, i + 1));\n\n    const countTree = new Float64Array(uSize\
        \ + 1);\n    const sumTree = new Float64Array(uSize + 1);\n\n    function update(i:\
        \ number, delta: number, val: number) {\n        for (; i <= uSize; i += i &\
        \ -i) {\n            countTree[i] += delta;\n            sumTree[i] += val;\n\
        \        }\n    }\n\n    function query(m: number): number {\n        let idx\
        \ = 0, currC = 0, currS = 0;\n        let logN = uSize > 0 ? Math.floor(Math.log2(uSize))\
        \ : 0;\n        for (let i = logN; i >= 0; i--) {\n            let nextIdx =\
        \ idx + (1 << i);\n            if (nextIdx <= uSize && currC + countTree[nextIdx]\
        \ < m) {\n                idx = nextIdx;\n                currC += countTree[idx];\n\
        \                currS += sumTree[idx];\n            }\n        }\n        return\
        \ currS + (m - currC) * unique[idx];\n    }\n\n    for (let i = 1; i <= dist\
        \ + 1; i++) {\n        update(map.get(nums[i])!, 1, nums[i]);\n    }\n\n   \
        \ let minSum = query(k - 1);\n    for (let i = dist + 2; i < n; i++) {\n   \
        \     update(map.get(nums[i - dist - 1])!, -1, -nums[i - dist - 1]);\n     \
        \   update(map.get(nums[i])!, 1, nums[i]);\n        minSum = Math.min(minSum,\
        \ query(k - 1));\n    }\n\n    return nums[0] + minSum;\n}"
      php: "class Solution {\n    function minimumCost($nums, $k, $dist) {\n       \
        \ $n = count($nums);\n        $sub = array_slice($nums, 1);\n        $unique\
        \ = array_unique($sub);\n        sort($unique);\n        $unique = array_values($unique);\n\
        \        $uSize = count($unique);\n        $map = array_flip($unique);\n\n \
        \       $countTree = array_fill(0, $uSize + 1, 0);\n        $sumTree = array_fill(0,\
        \ $uSize + 1, 0);\n\n        $update = function($i, $delta, $val) use (&$countTree,\
        \ &$sumTree, $uSize) {\n            $i++;\n            for (; $i <= $uSize;\
        \ $i += $i & -$i) {\n                $countTree[$i] += $delta;\n           \
        \     $sumTree[$i] += $val;\n            }\n        };\n\n        $query = function($m)\
        \ use (&$countTree, &$sumTree, $unique, $uSize) {\n            $idx = 0; $currC\
        \ = 0; $currS = 0;\n            $logN = $uSize > 0 ? (int)log($uSize, 2) : 0;\n\
        \            for ($i = $logN; $i >= 0; $i--) {\n                $nextIdx = $idx\
        \ + (1 << $i);\n                if ($nextIdx <= $uSize && $currC + $countTree[$nextIdx]\
        \ < $m) {\n                    $idx = $nextIdx;\n                    $currC\
        \ += $countTree[$idx];\n                    $currS += $sumTree[$idx];\n    \
        \            }\n            }\n            return $currS + ($m - $currC) * $unique[$idx];\n\
        \        };\n\n        for ($i = 1; $i <= $dist + 1; $i++) {\n            $update($map[$nums[$i]],\
        \ 1, $nums[$i]);\n        }\n\n        $minSum = $query($k - 1);\n        for\
        \ ($i = $dist + 2; $i < $n; $i++) {\n            $update($map[$nums[$i - $dist\
        \ - 1]], -1, -$nums[$i - $dist - 1]);\n            $update($map[$nums[$i]],\
        \ 1, $nums[$i]);\n            $minSum = min($minSum, $query($k - 1));\n    \
        \    }\n\n        return $nums[0] + $minSum;\n    }\n}"
      swift: "class Solution {\n    func minimumCost(_ nums: [Int], _ k: Int, _ dist:\
        \ Int) -> Int {\n        let n = nums.count\n        let sub = Array(nums[1...])\n\
        \        let unique = Array(Set(sub)).sorted()\n        let uSize = unique.count\n\
        \        var map = [Int: Int]()\n        for (i, v) in unique.enumerated() {\n\
        \            map[v] = i + 1\n        }\n\n        var countTree = [Int](repeating:\
        \ 0, count: uSize + 1)\n        var sumTree = [Int](repeating: 0, count: uSize\
        \ + 1)\n\n        func update(_ i: Int, _ delta: Int, _ val: Int) {\n      \
        \      var idx = i\n            while idx <= uSize {\n                countTree[idx]\
        \ += delta\n                sumTree[idx] += val\n                idx += idx\
        \ & -idx\n            }\n        }\n\n        func query(_ m: Int) -> Int {\n\
        \            var idx = 0, currC = 0, currS = 0\n            let logN = uSize\
        \ > 0 ? Int(log2(Double(uSize))) : 0\n            for i in (0...logN).reversed()\
        \ {\n                let nextIdx = idx + (1 << i)\n                if nextIdx\
        \ <= uSize && currC + countTree[nextIdx] < m {\n                    idx = nextIdx\n\
        \                    currC += countTree[idx]\n                    currS += sumTree[idx]\n\
        \                }\n            }\n            return currS + (m - currC) *\
        \ unique[idx]\n        }\n\n        for i in 1...(dist + 1) {\n            update(map[nums[i]]!,\
        \ 1, nums[i])\n        }\n\n        var minSum = query(k - 1)\n        if dist\
        \ + 2 < n {\n            for i in (dist + 2)..<n {\n                update(map[nums[i\
        \ - dist - 1]]!, -1, -nums[i - dist - 1])\n                update(map[nums[i]]!,\
        \ 1, nums[i])\n                minSum = min(minSum, query(k - 1))\n        \
        \    }\n        }\n\n        return nums[0] + minSum\n    }\n}"
      kotlin: "class Solution {\n    fun minimumCost(nums: IntArray, k: Int, dist: Int):\
        \ Long {\n        val n = nums.size\n        val sub = nums.copyOfRange(1, n)\n\
        \        val unique = sub.distinct().sorted()\n        val uSize = unique.size\n\
        \        val map = unique.withIndex().associate { it.value to it.index + 1 }\n\
        \n        val countTree = LongArray(uSize + 1)\n        val sumTree = LongArray(uSize\
        \ + 1)\n\n        fun update(i: Int, delta: Long, value: Long) {\n         \
        \   var idx = i\n            while (idx <= uSize) {\n                countTree[idx]\
        \ += delta\n                sumTree[idx] += value\n                idx += idx\
        \ and -idx\n            }\n        }\n\n        fun query(m: Int): Long {\n\
        \            var idx = 0\n            var currC = 0L\n            var currS\
        \ = 0L\n            val logN = if (uSize > 0) 31 - Integer.numberOfLeadingZeros(uSize)\
        \ else 0\n            for (i in logN downTo 0) {\n                val nextIdx\
        \ = idx + (1 shl i)\n                if (nextIdx <= uSize && currC + countTree[nextIdx]\
        \ < m) {\n                    idx = nextIdx\n                    currC += countTree[idx]\n\
        \                    currS += sumTree[idx]\n                }\n            }\n\
        \            return currS + (m - currC) * unique[idx].toLong()\n        }\n\n\
        \        for (i in 1..dist + 1) {\n            update(map[nums[i]]!!, 1L, nums[i].toLong())\n\
        \        }\n\n        var minSum = query(k - 1)\n        for (i in dist + 2\
        \ until n) {\n            update(map[nums[i - dist - 1]]!!, -1L, -nums[i - dist\
        \ - 1].toLong())\n            update(map[nums[i]]!!, 1L, nums[i].toLong())\n\
        \            val current = query(k - 1)\n            if (current < minSum) minSum\
        \ = current\n        }\n\n        return nums[0].toLong() + minSum\n    }\n}"
      dart: "import 'dart:math';\n\nclass Solution {\n  int minimumCost(List<int> nums,\
        \ int k, int dist) {\n    int n = nums.length;\n    List<int> sub = nums.sublist(1);\n\
        \    List<int> unique = sub.toSet().toList()..sort();\n    int uSize = unique.length;\n\
        \    Map<int, int> map = {};\n    for (int i = 0; i < uSize; i++) {\n      map[unique[i]]\
        \ = i + 1;\n    }\n\n    List<int> countTree = List.filled(uSize + 1, 0);\n\
        \    List<int> sumTree = List.filled(uSize + 1, 0);\n\n    void update(int i,\
        \ int delta, int val) {\n      while (i <= uSize) {\n        countTree[i] +=\
        \ delta;\n        sumTree[i] += val;\n        i += i & -i;\n      }\n    }\n\
        \n    int query(int m) {\n      int idx = 0, currC = 0, currS = 0;\n      int\
        \ logN = uSize > 0 ? (uSize.bitLength - 1) : 0;\n      for (int i = logN; i\
        \ >= 0; i--) {\n        int nextIdx = idx + (1 << i);\n        if (nextIdx <=\
        \ uSize && currC + countTree[nextIdx] < m) {\n          idx = nextIdx;\n   \
        \       currC += countTree[idx];\n          currS += sumTree[idx];\n       \
        \ }\n      }\n      return currS + (m - currC) * unique[idx];\n    }\n\n   \
        \ for (int i = 1; i <= dist + 1; i++) {\n      update(map[nums[i]]!, 1, nums[i]);\n\
        \    }\n\n    int minSum = query(k - 1);\n    for (int i = dist + 2; i < n;\
        \ i++) {\n      update(map[nums[i - dist - 1]]!, -1, -nums[i - dist - 1]);\n\
        \      update(map[nums[i]]!, 1, nums[i]);\n      int current = query(k - 1);\n\
        \      if (current < minSum) minSum = current\n    }\n\n    return nums[0] +\
        \ minSum;\n  }\n}"
      go: "import (\n\t\"math\"\n\t\"math/bits\"\n\t\"sort\"\n)\n\nfunc minimumCost(nums\
        \ []int, k int, dist int) int64 {\n\tn := len(nums)\n\tsortedNums := make([]int,\
        \ n-1)\n\tcopy(sortedNums, nums[1:])\n\tsort.Ints(sortedNums)\n\n\tunique :=\
        \ sortedNums[:0]\n\tif n > 1 {\n\t\tunique = append(unique, sortedNums[0])\n\
        \t\tfor i := 1; i < n-1; i++ {\n\t\tif sortedNums[i] != sortedNums[i-1] {\n\t\
        \t\t\tunique = append(unique, sortedNums[i])\n\t\t\t}\n\t\t}\n\t}\n\tuSize :=\
        \ len(unique)\n\tvalMap := make(map[int]int)\n\tfor i, v := range unique {\n\
        \t\tvalMap[v] = i + 1\n\t}\n\n\tcountTree := make([]int64, uSize+1)\n\tsumTree\
        \ := make([]int64, uSize+1)\n\n\tupdate := func(i int, delta int64, val int64)\
        \ {\n\t\tfor ; i <= uSize; i += i & -i {\n\t\t\tcountTree[i] += delta\n\t\t\t\
        sumTree[i] += val\n\t\t}\n\t}\n\n\tquery := func(m int) int64 {\n\t\tidx :=\
        \ 0\n\t\tvar currC, currS int64\n\t\tlogN := 0\n\t\tif uSize > 0 {\n\t\t\tlogN\
        \ = bits.Len(uint(uSize)) - 1\n\t\t}\n\t\tfor i := logN; i >= 0; i-- {\n\t\t\
        \tnextIdx := idx + (1 << i)\n\t\t\tif nextIdx <= uSize && currC+countTree[nextIdx]\
        \ < int64(m) {\n\t\t\t\tidx = nextIdx\n\t\t\t\tcurrC += countTree[idx]\n\t\t\
        \t\tcurrS += sumTree[idx]\n\t\t\t}\n\t\t}\n\t\treturn currS + (int64(m)-currC)*int64(unique[idx])\n\
        \t}\n\n\tfor i := 1; i <= dist+1; i++ {\n\t\tupdate(valMap[nums[i]], 1, int64(nums[i]))\n\
        \t}\n\n\tminSum := query(k - 1)\n\tfor i := dist + 2; i < n; i++ {\n\t\tupdate(valMap[nums[i-dist-1]],\
        \ -1, -int64(nums[i-dist-1]))\n\t\tupdate(valMap[nums[i]], 1, int64(nums[i]))\n\
        \t\tcurrent := query(k - 1)\n\t\tif current < minSum {\n\t\t\tminSum = current\n\
        \t\t}\n\t}\n\n\treturn int64(nums[0]) + minSum\n}"
      ruby: "def minimum_cost(nums, k, dist)\n  n = nums.length\n  m_count = k - 2\n\
        \  sorted_unique = nums.uniq.sort\n  m = sorted_unique.length\n  rank_map =\
        \ {}\n  sorted_unique.each_with_index { |v, i| rank_map[v] = i + 1 }\n\n  count_bit\
        \ = Array.new(m + 1, 0)\n  sum_bit = Array.new(m + 1, 0)\n\n  update = lambda\
        \ do |bit, idx, delta|\n    while idx <= m\n      bit[idx] += delta\n      idx\
        \ += idx & -idx\n    end\n  end\n\n  query = lambda do |bit, idx|\n    s = 0\n\
        \    while idx > 0\n      s += bit[idx]\n      idx -= idx & -idx\n    end\n\
        \    s\n  end\n\n  find_kth = lambda do |k_val|\n    idx = 0\n    p = 1\n  \
        \  p *= 2 while p * 2 <= m\n    while p > 0\n      next_idx = idx + p\n    \
        \  if next_idx <= m && count_bit[next_idx] < k_val\n        idx = next_idx\n\
        \        k_val -= count_bit[idx]\n      end\n      p /= 2\n    end\n    idx\
        \ + 1\n  end\n\n  get_low_sum = lambda do\n    rank = find_kth.call(m_count)\n\
        \    c_prev = query.call(count_bit, rank - 1)\n    s_prev = query.call(sum_bit,\
        \ rank - 1)\n    s_prev + (m_count - c_prev) * sorted_unique[rank - 1]\n  end\n\
        \n  add = lambda { |val| r = rank_map[val]; update.call(count_bit, r, 1); update.call(sum_bit,\
        \ r, val) }\n  remove = lambda { |val| r = rank_map[val]; update.call(count_bit,\
        \ r, -1); update.call(sum_bit, r, -val) }\n\n  (2..[1 + dist, n - 1].min).each\
        \ { |i| add.call(nums[i]) }\n\n  min_cost = 10**18\n  (1..n - k + 1).each do\
        \ |i1|\n    low_sum_val = get_low_sum.call\n    current_cost = nums[0] + nums[i1]\
        \ + low_sum_val\n    min_cost = [min_cost, current_cost].min\n\n    if i1 <\
        \ n - k + 1\n      remove.call(nums[i1 + 1])\n      add.call(nums[i1 + 1 + dist])\
        \ if i1 + 1 + dist < n\n    end\n  end\n\n  min_cost\nend"
      scala: "import java.util.Arrays\n\nobject Solution {\n  def minimumCost(nums:\
        \ Array[Int], k: Int, dist: Int): Long = {\n    val n = nums.length\n    val\
        \ mCount = k - 2\n    val sortedUnique = nums.distinct.sorted\n    val m = sortedUnique.length\n\
        \n    val countBit = new Array[Int](m + 1)\n    val sumBit = new Array[Long](m\
        \ + 1)\n\n    def update(bit: Array[Int], idx: Int, delta: Int): Unit = {\n\
        \      var i = idx\n      while (i <= m) {\n        bit(i) += delta\n      \
        \  i += i & -i\n      }\n    }\n\n    def updateLong(bit: Array[Long], idx:\
        \ Int, delta: Long): Unit = {\n      var i = idx\n      while (i <= m) {\n \
        \       bit(i) += delta\n        i += i & -i\n      }\n    }\n\n    def query(bit:\
        \ Array[Int], idx: Int): Int = {\n      var i = idx\n      var s = 0\n     \
        \ while (i > 0) {\n        s += bit(i)\n        i -= i & -i\n      }\n     \
        \ s\n    }\n\n    def queryLong(bit: Array[Long], idx: Int): Long = {\n    \
        \  var i = idx\n      var s = 0L\n      while (i > 0) {\n        s += bit(i)\n\
        \        i -= i & -i\n      }\n      s\n    }\n\n    def findKth(kVal: Int):\
        \ Int = {\n      var idx = 0\n      var kv = kVal\n      var p = 1\n      while\
        \ (p * 2 <= m) p *= 2\n      while (p > 0) {\n        val nextIdx = idx + p\n\
        \        if (nextIdx <= m && countBit(nextIdx) < kv) {\n          idx = nextIdx\n\
        \          kv -= countBit(idx)\n        }\n        p /= 2\n      }\n      idx\
        \ + 1\n    }\n\n    def getLowSum(): Long = {\n      val rank = findKth(mCount)\n\
        \      val cPrev = query(countBit, rank - 1)\n      val sPrev = queryLong(sumBit,\
        \ rank - 1)\n      sPrev + (mCount - cPrev).toLong * sortedUnique(rank - 1)\n\
        \    }\n\n    def add(valIn: Int): Unit = {\n      val r = Arrays.binarySearch(sortedUnique,\
        \ valIn) + 1\n      update(countBit, r, 1)\n      updateLong(sumBit, r, valIn.toLong)\n\
        \    }\n\n    def remove(valIn: Int): Unit = {\n      val r = Arrays.binarySearch(sortedUnique,\
        \ valIn) + 1\n      update(countBit, r, -1)\n      updateLong(sumBit, r, -valIn.toLong)\n\
        \    }\n\n    for (i <- 2 to Math.min(1 + dist, n - 1)) add(nums(i))\n\n   \
        \ var minCost = Long.MaxValue\n    for (i1 <- 1 to n - k + 1) {\n      val lowSumVal\
        \ = getLowSum()\n      minCost = Math.min(minCost, nums(0).toLong + nums(i1).toLong\
        \ + lowSumVal)\n      if (i1 < n - k + 1) {\n        remove(nums(i1 + 1))\n\
        \        if (i1 + 1 + dist < n) add(nums(i1 + 1 + dist))\n      }\n    }\n \
        \   minCost\n  }\n}"
      rust: "impl Solution {\n    pub fn minimum_cost(nums: Vec<i32>, k: i32, dist:\
        \ i32) -> i64 {\n        let n = nums.len();\n        let m_count = k - 2;\n\
        \        let mut sorted_unique = nums.clone();\n        sorted_unique.sort();\n\
        \        sorted_unique.dedup();\n        let m = sorted_unique.len();\n\n  \
        \      let mut count_bit = vec![0; m + 1];\n        let mut sum_bit = vec![0i64;\
        \ m + 1];\n\n        fn update_count(bit: &mut Vec<i32>, mut idx: usize, delta:\
        \ i32) {\n            let m = bit.len() - 1;\n            while idx <= m {\n\
        \                bit[idx] += delta;\n                idx += (idx as i32 & -(idx\
        \ as i32)) as usize;\n            }\n        }\n\n        fn update_sum(bit:\
        \ &mut Vec<i64>, mut idx: usize, delta: i64) {\n            let m = bit.len()\
        \ - 1;\n            while idx <= m {\n                bit[idx] += delta;\n \
        \               idx += (idx as i32 & -(idx as i32)) as usize;\n            }\n\
        \        }\n\n        fn query_count(bit: &Vec<i32>, mut idx: usize) -> i32\
        \ {\n            let mut s = 0;\n            while idx > 0 {\n             \
        \   s += bit[idx];\n                idx -= (idx as i32 & -(idx as i32)) as usize;\n\
        \            }\n            s\n        }\n\n        fn query_sum(bit: &Vec<i64>,\
        \ mut idx: usize) -> i64 {\n            let mut s = 0;\n            while idx\
        \ > 0 {\n                s += bit[idx];\n                idx -= (idx as i32\
        \ & -(idx as i32)) as usize;\n            }\n            s\n        }\n\n  \
        \      fn find_kth(bit: &Vec<i32>, mut k_val: i32, m: usize) -> usize {\n  \
        \          let mut idx = 0;\n            let mut p = 1;\n            while p\
        \ * 2 <= m { p *= 2; }\n            while p > 0 {\n                let next_idx\
        \ = idx + p;\n                if next_idx <= m && bit[next_idx] < k_val {\n\
        \                    idx = next_idx;\n                    k_val -= bit[idx];\n\
        \                }\n                p /= 2;\n            }\n            idx\
        \ + 1\n        }\n\n        let get_rank = |val: i32| sorted_unique.binary_search(&val).unwrap()\
        \ + 1;\n\n        for i in 2..=((1 + dist as usize).min(n - 1)) {\n        \
        \    let r = get_rank(nums[i]);\n            update_count(&mut count_bit, r,\
        \ 1);\n            update_sum(&mut sum_bit, r, nums[i] as i64);\n        }\n\
        \n        let mut min_cost = i64::MAX;\n        for i1 in 1..=n - k as usize\
        \ + 1 {\n            let rank = find_kth(&count_bit, m_count, m);\n        \
        \    let c_prev = query_count(&count_bit, rank - 1);\n            let s_prev\
        \ = query_sum(&sum_bit, rank - 1);\n            let low_sum_val = s_prev + (m_count\
        \ - c_prev) as i64 * sorted_unique[rank - 1] as i64;\n            min_cost =\
        \ min_cost.min(nums[0] as i64 + nums[i1] as i64 + low_sum_val);\n\n        \
        \    if i1 < n - k as usize + 1 {\n                let r_remove = get_rank(nums[i1\
        \ + 1]);\n                update_count(&mut count_bit, r_remove, -1);\n    \
        \            update_sum(&mut sum_bit, r_remove, -(nums[i1 + 1] as i64));\n \
        \               if i1 + 1 + dist as usize < n {\n                    let r_add\
        \ = get_rank(nums[i1 + 1 + dist as usize]);\n                    update_count(&mut\
        \ count_bit, r_add, 1);\n                    update_sum(&mut sum_bit, r_add,\
        \ nums[i1 + 1 + dist as usize] as i64);\n                }\n            }\n\
        \        }\n        min_cost\n    }\n}"
      racket: "(define/contract (minimum-cost nums k dist)\n  (-> (listof exact-integer?)\
        \ exact-integer? exact-integer? exact-integer?)\n  (let* ([n (length nums)]\n\
        \         [nums-vec (list->vector nums)]\n         [m-count (- k 2)]\n     \
        \    [sorted-unique (sort (remove-duplicates nums) <)]\n         [m (length\
        \ sorted-unique)]\n         [sorted-unique-vec (list->vector sorted-unique)]\n\
        \         [rank-map (make-hash (for/list ([v sorted-unique] [i (in-naturals\
        \ 1)]) (cons v i)))]\n         [count-bit (make-vector (+ m 1) 0)]\n       \
        \  [sum-bit (make-vector (+ m 1) 0)])\n\n    (define (update-bit! bit idx delta)\n\
        \      (let loop ([i idx])\n        (when (<= i m)\n          (vector-set! bit\
        \ i (+ (vector-ref bit i) delta))\n          (loop (+ i (bitwise-and i (- i)))))))\n\
        \n    (define (query-bit bit idx)\n      (let loop ([i idx] [s 0])\n       \
        \ (if (<= i 0) s (loop (- i (bitwise-and i (- i))) (+ s (vector-ref bit i))))))\n\
        \n    (define (find-kth kv)\n      (let* ([p (let loop ([val 1]) (if (> (* val\
        \ 2) m) val (loop (* val 2))))])\n        (let loop ([idx 0] [p p] [k-val kv])\n\
        \          (if (= p 0)\n              (+ idx 1)\n              (let ([next-idx\
        \ (+ idx p)])\n                (if (and (<= next-idx m) (< (vector-ref count-bit\
        \ next-idx) k-val))\n                    (loop next-idx (quotient p 2) (- k-val\
        \ (vector-ref count-bit next-idx)))\n                    (loop idx (quotient\
        \ p 2) k-val)))))))\n\n    (define (get-low-sum)\n      (let* ([rank (find-kth\
        \ m-count)]\n             [c-prev (query-bit count-bit (- rank 1))]\n      \
        \       [s-prev (query-bit sum-bit (- rank 1))])\n        (+ s-prev (* (- m-count\
        \ c-prev) (vector-ref sorted-unique-vec (- rank 1))))))\n\n    (define (add\
        \ val)\n      (let ([r (hash-ref rank-map val)])\n        (update-bit! count-bit\
        \ r 1)\n        (update-bit! sum-bit r val)))\n\n    (define (remove val)\n\
        \      (let ([r (hash-ref rank-map val)])\n        (update-bit! count-bit r\
        \ -1)\n        (update-bit! sum-bit r (- val))))\n\n    (for ([i (in-range 2\
        \ (+ 1 (min (+ 1 dist) (- n 1))))])\n      (add (vector-ref nums-vec i)))\n\n\
        \    (let loop ([i1 1] [min-cost 1000000000000000])\n      (if (> i1 (- n k\
        \ -1))\n          min-cost\n          (let* ([low-sum-val (get-low-sum)]\n \
        \                [current-cost (+ (vector-ref nums-vec 0) (vector-ref nums-vec\
        \ i1) low-sum-val)]\n                 [next-min-cost (min min-cost current-cost)])\n\
        \            (if (< i1 (- n k -1))\n                (begin\n               \
        \   (remove (vector-ref nums-vec (+ i1 1)))\n                  (when (< (+ i1\
        \ 1 dist) n)\n                    (add (vector-ref nums-vec (+ i1 1 dist))))\n\
        \                  (loop (+ i1 1) next-min-cost))\n                next-min-cost))))))"
      erlang: "minimum_cost(Nums, K, Dist) ->\n    N = length(Nums),\n    NumsArr =\
        \ array:from_list(Nums),\n    MCount = K - 2,\n    SortedUnique = lists:usort(Nums),\n\
        \    M = length(SortedUnique),\n    RankMap = maps:from_list(lists:zip(SortedUnique,\
        \ lists:seq(1, M))),\n    ValueTuple = list_to_tuple(SortedUnique),\n\n    CountBIT\
        \ = array:new([{size, M + 1}, {default, 0}]),\n    SumBIT = array:new([{size,\
        \ M + 1}, {default, 0}]),\n\n    Update = fun Up(BIT, Idx, Delta) when Idx =<\
        \ M ->\n                    Up(array:set(Idx, array:get(Idx, BIT) + Delta, BIT),\
        \ Idx + (Idx band -Idx), Delta);\n                 Up(BIT, _, _) -> BIT\n  \
        \           end,\n\n    Query = fun Q(BIT, Idx, S) when Idx > 0 ->\n       \
        \             Q(BIT, Idx - (Idx band -Idx), S + array:get(Idx, BIT));\n    \
        \            Q(_, _, S) -> S\n            end,\n\n    P = get_p(M),\n    FindKth\
        \ = fun F(BIT, KV, Idx, Pow) when Pow > 0 ->\n                      NextIdx\
        \ = Idx + Pow,\n                      if NextIdx =< M andalso array:get(NextIdx,\
        \ BIT) < KV ->\n                             F(BIT, KV - array:get(NextIdx,\
        \ BIT), NextIdx, Pow div 2);\n                         true ->\n           \
        \                  F(BIT, KV, Idx, Pow div 2)\n                      end;\n\
        \                  F(_, _, Idx, _) -> Idx + 1\n              end,\n\n    InitWindow\
        \ = fun Init(CB, SB, I) when I =< 1 + Dist, I < N ->\n                     \
        \    Val = array:get(I, NumsArr),\n                         Rank = maps:get(Val,\
        \ RankMap),\n                         Init(Update(CB, Rank, 1), Update(SB, Rank,\
        \ Val), I + 1);\n                     Init(CB, SB, _) -> {CB, SB}\n        \
        \         end,\n\n    {CBIT0, SBIT0} = InitWindow(CountBIT, SumBIT, 2),\n\n\
        \    Solve = fun S(I1, CBIT, SBIT, MinCost) when I1 =< N - K + 1 ->\n      \
        \              Rank = FindKth(CBIT, MCount, 0, P),\n                    CPrev\
        \ = Query(CBIT, Rank - 1, 0),\n                    SPrev = Query(SBIT, Rank\
        \ - 1, 0),\n                    LowSum = SPrev + (MCount - CPrev) * element(Rank,\
        \ ValueTuple),\n                    Cost = array:get(0, NumsArr) + array:get(I1,\
        \ NumsArr) + LowSum,\n                    NewMinCost = if Cost < MinCost ->\
        \ Cost; true -> MinCost end,\n                    if I1 < N - K + 1 ->\n   \
        \                        VRem = array:get(I1 + 1, NumsArr),\n              \
        \             RRem = maps:get(VRem, RankMap),\n                           CBIT1\
        \ = Update(CBIT, RRem, -1),\n                           SBIT1 = Update(SBIT,\
        \ RRem, -VRem),\n                           {CBIT2, SBIT2} = if I1 + 1 + Dist\
        \ < N ->\n                                                   VAdd = array:get(I1\
        \ + 1 + Dist, NumsArr),\n                                                  \
        \ RAdd = maps:get(VAdd, RankMap),\n                                        \
        \           {Update(CBIT1, RAdd, 1), Update(SBIT1, RAdd, VAdd)};\n         \
        \                                      true -> {CBIT1, SBIT1}\n            \
        \                                end,\n                           S(I1 + 1,\
        \ CBIT2, SBIT2, NewMinCost);\n                       true -> NewMinCost\n  \
        \                  end;\n                S(_, _, _, MinCost) -> MinCost\n  \
        \          end,\n    Solve(1, CBIT0, SBIT0, 1000000000000000).\n\nget_p(M) ->\
        \ get_p(M, 1).\nget_p(M, P) when P * 2 =< M -> get_p(M, P * 2);\nget_p(_, P)\
        \ -> P."
      elixir: "defmodule Solution do\n  import Bitwise\n\n  @spec minimum_cost(nums\
        \ :: [integer], k :: integer, dist :: integer) :: integer\n  def minimum_cost(nums,\
        \ k, dist) do\n    n = length(nums)\n    nums_tuple = List.to_tuple(nums)\n\
        \    m_count = k - 2\n    sorted_unique = Enum.uniq(nums) |> Enum.sort()\n \
        \   m = length(sorted_unique)\n    rank_map = sorted_unique |> Enum.with_index(1)\
        \ |> Enum.into(%{})\n    value_tuple = List.to_tuple(sorted_unique)\n\n    count_bit\
        \ = %{}\n    sum_bit = %{}\n\n    update = fn bit, idx, delta ->\n      let_update\
        \ = fn f, b, i, d ->\n        if i <= m do\n          f.(f, Map.put(b, i, Map.get(b,\
        \ i, 0) + d), i + (i &&& -i), d)\n        else\n          b\n        end\n \
        \     end\n      let_update.(let_update, bit, idx, delta)\n    end\n\n    query\
        \ = fn bit, idx ->\n      let_query = fn f, b, i, s ->\n        if i > 0 do\n\
        \          f.(f, b, i - (i &&& -i), s + Map.get(b, i, 0))\n        else\n  \
        \        s\n        end\n      end\n      let_query.(let_query, bit, idx, 0)\n\
        \    end\n\n    p = get_p(m)\n    find_kth = fn kv, bit ->\n      let_find =\
        \ fn f, kv_val, idx, pow ->\n        if pow > 0 do\n          next_idx = idx\
        \ + pow\n          if next_idx <= m && Map.get(bit, next_idx, 0) < kv_val do\n\
        \            f.(f, kv_val - Map.get(bit, next_idx, 0), next_idx, div(pow, 2))\n\
        \          else\n            f.(f, kv_val, idx, div(pow, 2))\n          end\n\
        \        else\n          idx + 1\n        end\n      end\n      let_find.(let_find,\
        \ kv, 0, p)\n    end\n\n    {cbit, sbit} = Enum.reduce(2..min(1 + dist, n -\
        \ 1), {count_bit, sum_bit}, fn i, {cb, sb} ->\n      val = elem(nums_tuple,\
        \ i)\n      r = Map.get(rank_map, val)\n      {update.(cb, r, 1), update.(sb,\
        \ r, val)}\n    end)\n\n    solve(1, n, k, dist, nums_tuple, cbit, sbit, rank_map,\
        \ value_tuple, m, m_count, find_kth, query, update, 1_000_000_000_000_000)\n\
        \  end\n\n  defp get_p(m) do\n    let_p = fn f, cur -> if cur * 2 <= m, do:\
        \ f.(f, cur * 2), else: cur end\n    let_p.(let_p, 1)\n  end\n\n  defp solve(i1,\
        \ n, k, dist, nums_tuple, cbit, sbit, rank_map, value_tuple, m, m_count, find_kth,\
        \ query, update, min_cost) do\n    rank = find_kth.(m_count, cbit)\n    c_prev\
        \ = query.(cbit, rank - 1)\n    s_prev = query.(sbit, rank - 1)\n    low_sum\
        \ = s_prev + (m_count - c_prev) * elem(value_tuple, rank - 1)\n    cost = elem(nums_tuple,\
        \ 0) + elem(nums_tuple, i1) + low_sum\n    new_min_cost = min(min_cost, cost)\n\
        \n    if i1 < n - k + 1 do\n      v_rem = elem(nums_tuple, i1 + 1)\n      r_rem\
        \ = Map.get(rank_map, v_rem)\n      cbit1 = update.(cbit, r_rem, -1)\n     \
        \ sbit1 = update.(sbit, r_rem, -v_rem)\n      {cbit2, sbit2} = if i1 + 1 + dist\
        \ < n do\n        v_add = elem(nums_tuple, i1 + 1 + dist)\n        r_add = Map.get(rank_map,\
        \ v_add)\n        {update.(cbit1, r_add, 1), update.(sbit1, r_add, v_add)}\n\
        \      else\n        {cbit1, sbit1}\n      end\n      solve(i1 + 1, n, k, dist,\
        \ nums_tuple, cbit2, sbit2, rank_map, value_tuple, m, m_count, find_kth, query,\
        \ update, new_min_cost)\n    else\n      new_min_cost\n    end\n  end\nend"
    approach: 'The problem asks for the minimum sum of $k$ subarrays'' costs, which
      is equivalent to $nums[0]$ plus the sum of the $k-1$ smallest elements chosen
      from $nums[1 \dots n-1]$, such that the index difference between the first and
      last chosen elements is at most $dist$. This constraint implies that we are looking
      for a window of indices $[i_1, i_{k-1}]$ such that $i_{k-1} - i_1 \le dist$. Such
      a set of indices is always contained within some window of fixed size $dist+1$.
      Therefore, the problem reduces to finding the minimum sum of $k-1$ smallest elements
      within any sliding window of size $dist+1$ in $nums[1 \dots n-1]$.


      To efficiently solve the sliding window smallest sum problem, we use coordinate
      compression on the values in $nums[1 \dots n-1]$ and maintain a Fenwick tree (Binary
      Indexed Tree) that stores frequencies and sums of values currently in the window.
      For each window, we perform a binary lifting search on the Fenwick tree to find
      the sum of the $k-1$ smallest elements in $O(\log n)$ time. The window is updated
      by adding the entering element and removing the exiting element as it slides from
      index $1$ to $n-1$, resulting in an overall time complexity of $O(n \log n)$.'
    time_complexity: O(n log n) because we perform coordinate compression in O(n log
      n), and then process n elements through a sliding window where each insertion,
      deletion, and M-smallest sum query takes O(log n) time using a Fenwick tree and
      binary lifting.
    space_complexity: O(n) to store the Fenwick trees (frequency and sum), the coordinate
      compression map, and the array of unique values.
    elapsed_time: 489.08460903167725
    model: gemini-3-flash-preview
    generated_at: '2026-02-02 01:32:47 '
---

## Problem #3013: Divide an Array Into Subarrays With Minimum Cost II

**Difficulty:** Hard

**Topics:** Array, Hash Table, Sliding Window, Heap (Priority Queue)

## Problem Description

<p>You are given a <strong>0-indexed</strong> array of integers <code>nums</code> of length <code>n</code>, and two <strong>positive</strong> integers <code>k</code> and <code>dist</code>.</p>

<p>The <strong>cost</strong> of an array is the value of its <strong>first</strong> element. For example, the cost of <code>[1,2,3]</code> is <code>1</code> while the cost of <code>[3,4,1]</code> is <code>3</code>.</p>

<p>You need to divide <code>nums</code> into <code>k</code> <strong>disjoint contiguous </strong><span data-keyword="subarray-nonempty">subarrays</span>, such that the difference between the starting index of the <strong>second</strong> subarray and the starting index of the <code>kth</code> subarray should be <strong>less than or equal to</strong> <code>dist</code>. In other words, if you divide <code>nums</code> into the subarrays <code>nums[0..(i<sub>1</sub> - 1)], nums[i<sub>1</sub>..(i<sub>2</sub> - 1)], ..., nums[i<sub>k-1</sub>..(n - 1)]</code>, then <code>i<sub>k-1</sub> - i<sub>1</sub> &lt;= dist</code>.</p>

<p>Return <em>the <strong>minimum</strong> possible sum of the cost of these</em> <em>subarrays</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,2,6,4,2], k = 3, dist = 3
<strong>Output:</strong> 5
<strong>Explanation:</strong> The best possible way to divide nums into 3 subarrays is: [1,3], [2,6,4], and [2]. This choice is valid because i<sub>k-1</sub> - i<sub>1</sub> is 5 - 2 = 3 which is equal to dist. The total cost is nums[0] + nums[2] + nums[5] which is 1 + 2 + 2 = 5.
It can be shown that there is no possible way to divide nums into 3 subarrays at a cost lower than 5.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [10,1,2,2,2,1], k = 4, dist = 3
<strong>Output:</strong> 15
<strong>Explanation:</strong> The best possible way to divide nums into 4 subarrays is: [10], [1], [2], and [2,2,1]. This choice is valid because i<sub>k-1</sub> - i<sub>1</sub> is 3 - 1 = 2 which is less than dist. The total cost is nums[0] + nums[1] + nums[2] + nums[3] which is 10 + 1 + 2 + 2 = 15.
The division [10], [1], [2,2,2], and [1] is not valid, because the difference between i<sub>k-1</sub> and i<sub>1</sub> is 5 - 1 = 4, which is greater than dist.
It can be shown that there is no possible way to divide nums into 4 subarrays at a cost lower than 15.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [10,8,18,9], k = 3, dist = 1
<strong>Output:</strong> 36
<strong>Explanation:</strong> The best possible way to divide nums into 4 subarrays is: [10], [8], and [18,9]. This choice is valid because i<sub>k-1</sub> - i<sub>1</sub> is 2 - 1 = 1 which is equal to dist.The total cost is nums[0] + nums[1] + nums[2] which is 10 + 8 + 18 = 36.
The division [10], [8,18], and [9] is not valid, because the difference between i<sub>k-1</sub> and i<sub>1</sub> is 3 - 1 = 2, which is greater than dist.
It can be shown that there is no possible way to divide nums into 3 subarrays at a cost lower than 36.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>3 &lt;= k &lt;= n</code></li>
	<li><code>k - 2 &lt;= dist &lt;= n - 2</code></li>
</ul>


## Hints

1. For each `i > 0`, try each `nums[i]` as the first element of the second subarray. We need to find the sum of `k - 2` smallest values in the index range `[i + 1, min(i + dist, n - 1)]`.

2. Typically, we use a max heap to maintain the top `k - 2` smallest values dynamically. Here we also have a sliding window, which is the index range `[i + 1, min(i + dist, n - 1)]`. We can use another min heap to put unselected values for future use.

3. Update the two heaps when iteration over `i`. Ordered/Tree sets are also a good choice since we have to delete elements.

4. If the max heap’s size is less than `k - 2`, use the min heap’s value to fill it. If the maximum value in the max heap is larger than the smallest value in the min heap, swap them in the two heaps.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The problem asks for the minimum sum of $k$ subarrays' costs, which is equivalent to $nums[0]$ plus the sum of the $k-1$ smallest elements chosen from $nums[1 \dots n-1]$, such that the index difference between the first and last chosen elements is at most $dist$. This constraint implies that we are looking for a window of indices $[i_1, i_{k-1}]$ such that $i_{k-1} - i_1 \le dist$. Such a set of indices is always contained within some window of fixed size $dist+1$. Therefore, the problem reduces to finding the minimum sum of $k-1$ smallest elements within any sliding window of size $dist+1$ in $nums[1 \dots n-1]$.

To efficiently solve the sliding window smallest sum problem, we use coordinate compression on the values in $nums[1 \dots n-1]$ and maintain a Fenwick tree (Binary Indexed Tree) that stores frequencies and sums of values currently in the window. For each window, we perform a binary lifting search on the Fenwick tree to find the sum of the $k-1$ smallest elements in $O(\log n)$ time. The window is updated by adding the entering element and removing the exiting element as it slides from index $1$ to $n-1$, resulting in an overall time complexity of $O(n \log n)$.

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
// Generation failed for C++
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
// Generation failed for Java
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
// Generation failed for Python
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
// Generation failed for Python3
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
// Generation failed for C
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
// Generation failed for C#
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
// Generation failed for JavaScript
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minimumCost(nums: number[], k: number, dist: number): number {
    const n = nums.length;
    const sub = nums.slice(1);
    const sortedSub = [...sub].sort((a, b) => a - b);
    const unique: number[] = [];
    if (sortedSub.length > 0) {
        unique.push(sortedSub[0]);
        for (let i = 1; i < sortedSub.length; i++) {
            if (sortedSub[i] !== sortedSub[i - 1]) unique.push(sortedSub[i]);
        }
    }

    const uSize = unique.length;
    const map = new Map<number, number>();
    unique.forEach((v, i) => map.set(v, i + 1));

    const countTree = new Float64Array(uSize + 1);
    const sumTree = new Float64Array(uSize + 1);

    function update(i: number, delta: number, val: number) {
        for (; i <= uSize; i += i & -i) {
            countTree[i] += delta;
            sumTree[i] += val;
        }
    }

    function query(m: number): number {
        let idx = 0, currC = 0, currS = 0;
        let logN = uSize > 0 ? Math.floor(Math.log2(uSize)) : 0;
        for (let i = logN; i >= 0; i--) {
            let nextIdx = idx + (1 << i);
            if (nextIdx <= uSize && currC + countTree[nextIdx] < m) {
                idx = nextIdx;
                currC += countTree[idx];
                currS += sumTree[idx];
            }
        }
        return currS + (m - currC) * unique[idx];
    }

    for (let i = 1; i <= dist + 1; i++) {
        update(map.get(nums[i])!, 1, nums[i]);
    }

    let minSum = query(k - 1);
    for (let i = dist + 2; i < n; i++) {
        update(map.get(nums[i - dist - 1])!, -1, -nums[i - dist - 1]);
        update(map.get(nums[i])!, 1, nums[i]);
        minSum = Math.min(minSum, query(k - 1));
    }

    return nums[0] + minSum;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function minimumCost($nums, $k, $dist) {
        $n = count($nums);
        $sub = array_slice($nums, 1);
        $unique = array_unique($sub);
        sort($unique);
        $unique = array_values($unique);
        $uSize = count($unique);
        $map = array_flip($unique);

        $countTree = array_fill(0, $uSize + 1, 0);
        $sumTree = array_fill(0, $uSize + 1, 0);

        $update = function($i, $delta, $val) use (&$countTree, &$sumTree, $uSize) {
            $i++;
            for (; $i <= $uSize; $i += $i & -$i) {
                $countTree[$i] += $delta;
                $sumTree[$i] += $val;
            }
        };

        $query = function($m) use (&$countTree, &$sumTree, $unique, $uSize) {
            $idx = 0; $currC = 0; $currS = 0;
            $logN = $uSize > 0 ? (int)log($uSize, 2) : 0;
            for ($i = $logN; $i >= 0; $i--) {
                $nextIdx = $idx + (1 << $i);
                if ($nextIdx <= $uSize && $currC + $countTree[$nextIdx] < $m) {
                    $idx = $nextIdx;
                    $currC += $countTree[$idx];
                    $currS += $sumTree[$idx];
                }
            }
            return $currS + ($m - $currC) * $unique[$idx];
        };

        for ($i = 1; $i <= $dist + 1; $i++) {
            $update($map[$nums[$i]], 1, $nums[$i]);
        }

        $minSum = $query($k - 1);
        for ($i = $dist + 2; $i < $n; $i++) {
            $update($map[$nums[$i - $dist - 1]], -1, -$nums[$i - $dist - 1]);
            $update($map[$nums[$i]], 1, $nums[$i]);
            $minSum = min($minSum, $query($k - 1));
        }

        return $nums[0] + $minSum;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minimumCost(_ nums: [Int], _ k: Int, _ dist: Int) -> Int {
        let n = nums.count
        let sub = Array(nums[1...])
        let unique = Array(Set(sub)).sorted()
        let uSize = unique.count
        var map = [Int: Int]()
        for (i, v) in unique.enumerated() {
            map[v] = i + 1
        }

        var countTree = [Int](repeating: 0, count: uSize + 1)
        var sumTree = [Int](repeating: 0, count: uSize + 1)

        func update(_ i: Int, _ delta: Int, _ val: Int) {
            var idx = i
            while idx <= uSize {
                countTree[idx] += delta
                sumTree[idx] += val
                idx += idx & -idx
            }
        }

        func query(_ m: Int) -> Int {
            var idx = 0, currC = 0, currS = 0
            let logN = uSize > 0 ? Int(log2(Double(uSize))) : 0
            for i in (0...logN).reversed() {
                let nextIdx = idx + (1 << i)
                if nextIdx <= uSize && currC + countTree[nextIdx] < m {
                    idx = nextIdx
                    currC += countTree[idx]
                    currS += sumTree[idx]
                }
            }
            return currS + (m - currC) * unique[idx]
        }

        for i in 1...(dist + 1) {
            update(map[nums[i]]!, 1, nums[i])
        }

        var minSum = query(k - 1)
        if dist + 2 < n {
            for i in (dist + 2)..<n {
                update(map[nums[i - dist - 1]]!, -1, -nums[i - dist - 1])
                update(map[nums[i]]!, 1, nums[i])
                minSum = min(minSum, query(k - 1))
            }
        }

        return nums[0] + minSum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun minimumCost(nums: IntArray, k: Int, dist: Int): Long {
        val n = nums.size
        val sub = nums.copyOfRange(1, n)
        val unique = sub.distinct().sorted()
        val uSize = unique.size
        val map = unique.withIndex().associate { it.value to it.index + 1 }

        val countTree = LongArray(uSize + 1)
        val sumTree = LongArray(uSize + 1)

        fun update(i: Int, delta: Long, value: Long) {
            var idx = i
            while (idx <= uSize) {
                countTree[idx] += delta
                sumTree[idx] += value
                idx += idx and -idx
            }
        }

        fun query(m: Int): Long {
            var idx = 0
            var currC = 0L
            var currS = 0L
            val logN = if (uSize > 0) 31 - Integer.numberOfLeadingZeros(uSize) else 0
            for (i in logN downTo 0) {
                val nextIdx = idx + (1 shl i)
                if (nextIdx <= uSize && currC + countTree[nextIdx] < m) {
                    idx = nextIdx
                    currC += countTree[idx]
                    currS += sumTree[idx]
                }
            }
            return currS + (m - currC) * unique[idx].toLong()
        }

        for (i in 1..dist + 1) {
            update(map[nums[i]]!!, 1L, nums[i].toLong())
        }

        var minSum = query(k - 1)
        for (i in dist + 2 until n) {
            update(map[nums[i - dist - 1]]!!, -1L, -nums[i - dist - 1].toLong())
            update(map[nums[i]]!!, 1L, nums[i].toLong())
            val current = query(k - 1)
            if (current < minSum) minSum = current
        }

        return nums[0].toLong() + minSum
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
  int minimumCost(List<int> nums, int k, int dist) {
    int n = nums.length;
    List<int> sub = nums.sublist(1);
    List<int> unique = sub.toSet().toList()..sort();
    int uSize = unique.length;
    Map<int, int> map = {};
    for (int i = 0; i < uSize; i++) {
      map[unique[i]] = i + 1;
    }

    List<int> countTree = List.filled(uSize + 1, 0);
    List<int> sumTree = List.filled(uSize + 1, 0);

    void update(int i, int delta, int val) {
      while (i <= uSize) {
        countTree[i] += delta;
        sumTree[i] += val;
        i += i & -i;
      }
    }

    int query(int m) {
      int idx = 0, currC = 0, currS = 0;
      int logN = uSize > 0 ? (uSize.bitLength - 1) : 0;
      for (int i = logN; i >= 0; i--) {
        int nextIdx = idx + (1 << i);
        if (nextIdx <= uSize && currC + countTree[nextIdx] < m) {
          idx = nextIdx;
          currC += countTree[idx];
          currS += sumTree[idx];
        }
      }
      return currS + (m - currC) * unique[idx];
    }

    for (int i = 1; i <= dist + 1; i++) {
      update(map[nums[i]]!, 1, nums[i]);
    }

    int minSum = query(k - 1);
    for (int i = dist + 2; i < n; i++) {
      update(map[nums[i - dist - 1]]!, -1, -nums[i - dist - 1]);
      update(map[nums[i]]!, 1, nums[i]);
      int current = query(k - 1);
      if (current < minSum) minSum = current
    }

    return nums[0] + minSum;
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
	"math/bits"
	"sort"
)

func minimumCost(nums []int, k int, dist int) int64 {
	n := len(nums)
	sortedNums := make([]int, n-1)
	copy(sortedNums, nums[1:])
	sort.Ints(sortedNums)

	unique := sortedNums[:0]
	if n > 1 {
		unique = append(unique, sortedNums[0])
		for i := 1; i < n-1; i++ {
		if sortedNums[i] != sortedNums[i-1] {
				unique = append(unique, sortedNums[i])
			}
		}
	}
	uSize := len(unique)
	valMap := make(map[int]int)
	for i, v := range unique {
		valMap[v] = i + 1
	}

	countTree := make([]int64, uSize+1)
	sumTree := make([]int64, uSize+1)

	update := func(i int, delta int64, val int64) {
		for ; i <= uSize; i += i & -i {
			countTree[i] += delta
			sumTree[i] += val
		}
	}

	query := func(m int) int64 {
		idx := 0
		var currC, currS int64
		logN := 0
		if uSize > 0 {
			logN = bits.Len(uint(uSize)) - 1
		}
		for i := logN; i >= 0; i-- {
			nextIdx := idx + (1 << i)
			if nextIdx <= uSize && currC+countTree[nextIdx] < int64(m) {
				idx = nextIdx
				currC += countTree[idx]
				currS += sumTree[idx]
			}
		}
		return currS + (int64(m)-currC)*int64(unique[idx])
	}

	for i := 1; i <= dist+1; i++ {
		update(valMap[nums[i]], 1, int64(nums[i]))
	}

	minSum := query(k - 1)
	for i := dist + 2; i < n; i++ {
		update(valMap[nums[i-dist-1]], -1, -int64(nums[i-dist-1]))
		update(valMap[nums[i]], 1, int64(nums[i]))
		current := query(k - 1)
		if current < minSum {
			minSum = current
		}
	}

	return int64(nums[0]) + minSum
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def minimum_cost(nums, k, dist)
  n = nums.length
  m_count = k - 2
  sorted_unique = nums.uniq.sort
  m = sorted_unique.length
  rank_map = {}
  sorted_unique.each_with_index { |v, i| rank_map[v] = i + 1 }

  count_bit = Array.new(m + 1, 0)
  sum_bit = Array.new(m + 1, 0)

  update = lambda do |bit, idx, delta|
    while idx <= m
      bit[idx] += delta
      idx += idx & -idx
    end
  end

  query = lambda do |bit, idx|
    s = 0
    while idx > 0
      s += bit[idx]
      idx -= idx & -idx
    end
    s
  end

  find_kth = lambda do |k_val|
    idx = 0
    p = 1
    p *= 2 while p * 2 <= m
    while p > 0
      next_idx = idx + p
      if next_idx <= m && count_bit[next_idx] < k_val
        idx = next_idx
        k_val -= count_bit[idx]
      end
      p /= 2
    end
    idx + 1
  end

  get_low_sum = lambda do
    rank = find_kth.call(m_count)
    c_prev = query.call(count_bit, rank - 1)
    s_prev = query.call(sum_bit, rank - 1)
    s_prev + (m_count - c_prev) * sorted_unique[rank - 1]
  end

  add = lambda { |val| r = rank_map[val]; update.call(count_bit, r, 1); update.call(sum_bit, r, val) }
  remove = lambda { |val| r = rank_map[val]; update.call(count_bit, r, -1); update.call(sum_bit, r, -val) }

  (2..[1 + dist, n - 1].min).each { |i| add.call(nums[i]) }

  min_cost = 10**18
  (1..n - k + 1).each do |i1|
    low_sum_val = get_low_sum.call
    current_cost = nums[0] + nums[i1] + low_sum_val
    min_cost = [min_cost, current_cost].min

    if i1 < n - k + 1
      remove.call(nums[i1 + 1])
      add.call(nums[i1 + 1 + dist]) if i1 + 1 + dist < n
    end
  end

  min_cost
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import java.util.Arrays

object Solution {
  def minimumCost(nums: Array[Int], k: Int, dist: Int): Long = {
    val n = nums.length
    val mCount = k - 2
    val sortedUnique = nums.distinct.sorted
    val m = sortedUnique.length

    val countBit = new Array[Int](m + 1)
    val sumBit = new Array[Long](m + 1)

    def update(bit: Array[Int], idx: Int, delta: Int): Unit = {
      var i = idx
      while (i <= m) {
        bit(i) += delta
        i += i & -i
      }
    }

    def updateLong(bit: Array[Long], idx: Int, delta: Long): Unit = {
      var i = idx
      while (i <= m) {
        bit(i) += delta
        i += i & -i
      }
    }

    def query(bit: Array[Int], idx: Int): Int = {
      var i = idx
      var s = 0
      while (i > 0) {
        s += bit(i)
        i -= i & -i
      }
      s
    }

    def queryLong(bit: Array[Long], idx: Int): Long = {
      var i = idx
      var s = 0L
      while (i > 0) {
        s += bit(i)
        i -= i & -i
      }
      s
    }

    def findKth(kVal: Int): Int = {
      var idx = 0
      var kv = kVal
      var p = 1
      while (p * 2 <= m) p *= 2
      while (p > 0) {
        val nextIdx = idx + p
        if (nextIdx <= m && countBit(nextIdx) < kv) {
          idx = nextIdx
          kv -= countBit(idx)
        }
        p /= 2
      }
      idx + 1
    }

    def getLowSum(): Long = {
      val rank = findKth(mCount)
      val cPrev = query(countBit, rank - 1)
      val sPrev = queryLong(sumBit, rank - 1)
      sPrev + (mCount - cPrev).toLong * sortedUnique(rank - 1)
    }

    def add(valIn: Int): Unit = {
      val r = Arrays.binarySearch(sortedUnique, valIn) + 1
      update(countBit, r, 1)
      updateLong(sumBit, r, valIn.toLong)
    }

    def remove(valIn: Int): Unit = {
      val r = Arrays.binarySearch(sortedUnique, valIn) + 1
      update(countBit, r, -1)
      updateLong(sumBit, r, -valIn.toLong)
    }

    for (i <- 2 to Math.min(1 + dist, n - 1)) add(nums(i))

    var minCost = Long.MaxValue
    for (i1 <- 1 to n - k + 1) {
      val lowSumVal = getLowSum()
      minCost = Math.min(minCost, nums(0).toLong + nums(i1).toLong + lowSumVal)
      if (i1 < n - k + 1) {
        remove(nums(i1 + 1))
        if (i1 + 1 + dist < n) add(nums(i1 + 1 + dist))
      }
    }
    minCost
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn minimum_cost(nums: Vec<i32>, k: i32, dist: i32) -> i64 {
        let n = nums.len();
        let m_count = k - 2;
        let mut sorted_unique = nums.clone();
        sorted_unique.sort();
        sorted_unique.dedup();
        let m = sorted_unique.len();

        let mut count_bit = vec![0; m + 1];
        let mut sum_bit = vec![0i64; m + 1];

        fn update_count(bit: &mut Vec<i32>, mut idx: usize, delta: i32) {
            let m = bit.len() - 1;
            while idx <= m {
                bit[idx] += delta;
                idx += (idx as i32 & -(idx as i32)) as usize;
            }
        }

        fn update_sum(bit: &mut Vec<i64>, mut idx: usize, delta: i64) {
            let m = bit.len() - 1;
            while idx <= m {
                bit[idx] += delta;
                idx += (idx as i32 & -(idx as i32)) as usize;
            }
        }

        fn query_count(bit: &Vec<i32>, mut idx: usize) -> i32 {
            let mut s = 0;
            while idx > 0 {
                s += bit[idx];
                idx -= (idx as i32 & -(idx as i32)) as usize;
            }
            s
        }

        fn query_sum(bit: &Vec<i64>, mut idx: usize) -> i64 {
            let mut s = 0;
            while idx > 0 {
                s += bit[idx];
                idx -= (idx as i32 & -(idx as i32)) as usize;
            }
            s
        }

        fn find_kth(bit: &Vec<i32>, mut k_val: i32, m: usize) -> usize {
            let mut idx = 0;
            let mut p = 1;
            while p * 2 <= m { p *= 2; }
            while p > 0 {
                let next_idx = idx + p;
                if next_idx <= m && bit[next_idx] < k_val {
                    idx = next_idx;
                    k_val -= bit[idx];
                }
                p /= 2;
            }
            idx + 1
        }

        let get_rank = |val: i32| sorted_unique.binary_search(&val).unwrap() + 1;

        for i in 2..=((1 + dist as usize).min(n - 1)) {
            let r = get_rank(nums[i]);
            update_count(&mut count_bit, r, 1);
            update_sum(&mut sum_bit, r, nums[i] as i64);
        }

        let mut min_cost = i64::MAX;
        for i1 in 1..=n - k as usize + 1 {
            let rank = find_kth(&count_bit, m_count, m);
            let c_prev = query_count(&count_bit, rank - 1);
            let s_prev = query_sum(&sum_bit, rank - 1);
            let low_sum_val = s_prev + (m_count - c_prev) as i64 * sorted_unique[rank - 1] as i64;
            min_cost = min_cost.min(nums[0] as i64 + nums[i1] as i64 + low_sum_val);

            if i1 < n - k as usize + 1 {
                let r_remove = get_rank(nums[i1 + 1]);
                update_count(&mut count_bit, r_remove, -1);
                update_sum(&mut sum_bit, r_remove, -(nums[i1 + 1] as i64));
                if i1 + 1 + dist as usize < n {
                    let r_add = get_rank(nums[i1 + 1 + dist as usize]);
                    update_count(&mut count_bit, r_add, 1);
                    update_sum(&mut sum_bit, r_add, nums[i1 + 1 + dist as usize] as i64);
                }
            }
        }
        min_cost
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (minimum-cost nums k dist)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  (let* ([n (length nums)]
         [nums-vec (list->vector nums)]
         [m-count (- k 2)]
         [sorted-unique (sort (remove-duplicates nums) <)]
         [m (length sorted-unique)]
         [sorted-unique-vec (list->vector sorted-unique)]
         [rank-map (make-hash (for/list ([v sorted-unique] [i (in-naturals 1)]) (cons v i)))]
         [count-bit (make-vector (+ m 1) 0)]
         [sum-bit (make-vector (+ m 1) 0)])

    (define (update-bit! bit idx delta)
      (let loop ([i idx])
        (when (<= i m)
          (vector-set! bit i (+ (vector-ref bit i) delta))
          (loop (+ i (bitwise-and i (- i)))))))

    (define (query-bit bit idx)
      (let loop ([i idx] [s 0])
        (if (<= i 0) s (loop (- i (bitwise-and i (- i))) (+ s (vector-ref bit i))))))

    (define (find-kth kv)
      (let* ([p (let loop ([val 1]) (if (> (* val 2) m) val (loop (* val 2))))])
        (let loop ([idx 0] [p p] [k-val kv])
          (if (= p 0)
              (+ idx 1)
              (let ([next-idx (+ idx p)])
                (if (and (<= next-idx m) (< (vector-ref count-bit next-idx) k-val))
                    (loop next-idx (quotient p 2) (- k-val (vector-ref count-bit next-idx)))
                    (loop idx (quotient p 2) k-val)))))))

    (define (get-low-sum)
      (let* ([rank (find-kth m-count)]
             [c-prev (query-bit count-bit (- rank 1))]
             [s-prev (query-bit sum-bit (- rank 1))])
        (+ s-prev (* (- m-count c-prev) (vector-ref sorted-unique-vec (- rank 1))))))

    (define (add val)
      (let ([r (hash-ref rank-map val)])
        (update-bit! count-bit r 1)
        (update-bit! sum-bit r val)))

    (define (remove val)
      (let ([r (hash-ref rank-map val)])
        (update-bit! count-bit r -1)
        (update-bit! sum-bit r (- val))))

    (for ([i (in-range 2 (+ 1 (min (+ 1 dist) (- n 1))))])
      (add (vector-ref nums-vec i)))

    (let loop ([i1 1] [min-cost 1000000000000000])
      (if (> i1 (- n k -1))
          min-cost
          (let* ([low-sum-val (get-low-sum)]
                 [current-cost (+ (vector-ref nums-vec 0) (vector-ref nums-vec i1) low-sum-val)]
                 [next-min-cost (min min-cost current-cost)])
            (if (< i1 (- n k -1))
                (begin
                  (remove (vector-ref nums-vec (+ i1 1)))
                  (when (< (+ i1 1 dist) n)
                    (add (vector-ref nums-vec (+ i1 1 dist))))
                  (loop (+ i1 1) next-min-cost))
                next-min-cost))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
minimum_cost(Nums, K, Dist) ->
    N = length(Nums),
    NumsArr = array:from_list(Nums),
    MCount = K - 2,
    SortedUnique = lists:usort(Nums),
    M = length(SortedUnique),
    RankMap = maps:from_list(lists:zip(SortedUnique, lists:seq(1, M))),
    ValueTuple = list_to_tuple(SortedUnique),

    CountBIT = array:new([{size, M + 1}, {default, 0}]),
    SumBIT = array:new([{size, M + 1}, {default, 0}]),

    Update = fun Up(BIT, Idx, Delta) when Idx =< M ->
                    Up(array:set(Idx, array:get(Idx, BIT) + Delta, BIT), Idx + (Idx band -Idx), Delta);
                 Up(BIT, _, _) -> BIT
             end,

    Query = fun Q(BIT, Idx, S) when Idx > 0 ->
                    Q(BIT, Idx - (Idx band -Idx), S + array:get(Idx, BIT));
                Q(_, _, S) -> S
            end,

    P = get_p(M),
    FindKth = fun F(BIT, KV, Idx, Pow) when Pow > 0 ->
                      NextIdx = Idx + Pow,
                      if NextIdx =< M andalso array:get(NextIdx, BIT) < KV ->
                             F(BIT, KV - array:get(NextIdx, BIT), NextIdx, Pow div 2);
                         true ->
                             F(BIT, KV, Idx, Pow div 2)
                      end;
                  F(_, _, Idx, _) -> Idx + 1
              end,

    InitWindow = fun Init(CB, SB, I) when I =< 1 + Dist, I < N ->
                         Val = array:get(I, NumsArr),
                         Rank = maps:get(Val, RankMap),
                         Init(Update(CB, Rank, 1), Update(SB, Rank, Val), I + 1);
                     Init(CB, SB, _) -> {CB, SB}
                 end,

    {CBIT0, SBIT0} = InitWindow(CountBIT, SumBIT, 2),

    Solve = fun S(I1, CBIT, SBIT, MinCost) when I1 =< N - K + 1 ->
                    Rank = FindKth(CBIT, MCount, 0, P),
                    CPrev = Query(CBIT, Rank - 1, 0),
                    SPrev = Query(SBIT, Rank - 1, 0),
                    LowSum = SPrev + (MCount - CPrev) * element(Rank, ValueTuple),
                    Cost = array:get(0, NumsArr) + array:get(I1, NumsArr) + LowSum,
                    NewMinCost = if Cost < MinCost -> Cost; true -> MinCost end,
                    if I1 < N - K + 1 ->
                           VRem = array:get(I1 + 1, NumsArr),
                           RRem = maps:get(VRem, RankMap),
                           CBIT1 = Update(CBIT, RRem, -1),
                           SBIT1 = Update(SBIT, RRem, -VRem),
                           {CBIT2, SBIT2} = if I1 + 1 + Dist < N ->
                                                   VAdd = array:get(I1 + 1 + Dist, NumsArr),
                                                   RAdd = maps:get(VAdd, RankMap),
                                                   {Update(CBIT1, RAdd, 1), Update(SBIT1, RAdd, VAdd)};
                                               true -> {CBIT1, SBIT1}
                                            end,
                           S(I1 + 1, CBIT2, SBIT2, NewMinCost);
                       true -> NewMinCost
                    end;
                S(_, _, _, MinCost) -> MinCost
            end,
    Solve(1, CBIT0, SBIT0, 1000000000000000).

get_p(M) -> get_p(M, 1).
get_p(M, P) when P * 2 =< M -> get_p(M, P * 2);
get_p(_, P) -> P.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  import Bitwise

  @spec minimum_cost(nums :: [integer], k :: integer, dist :: integer) :: integer
  def minimum_cost(nums, k, dist) do
    n = length(nums)
    nums_tuple = List.to_tuple(nums)
    m_count = k - 2
    sorted_unique = Enum.uniq(nums) |> Enum.sort()
    m = length(sorted_unique)
    rank_map = sorted_unique |> Enum.with_index(1) |> Enum.into(%{})
    value_tuple = List.to_tuple(sorted_unique)

    count_bit = %{}
    sum_bit = %{}

    update = fn bit, idx, delta ->
      let_update = fn f, b, i, d ->
        if i <= m do
          f.(f, Map.put(b, i, Map.get(b, i, 0) + d), i + (i &&& -i), d)
        else
          b
        end
      end
      let_update.(let_update, bit, idx, delta)
    end

    query = fn bit, idx ->
      let_query = fn f, b, i, s ->
        if i > 0 do
          f.(f, b, i - (i &&& -i), s + Map.get(b, i, 0))
        else
          s
        end
      end
      let_query.(let_query, bit, idx, 0)
    end

    p = get_p(m)
    find_kth = fn kv, bit ->
      let_find = fn f, kv_val, idx, pow ->
        if pow > 0 do
          next_idx = idx + pow
          if next_idx <= m && Map.get(bit, next_idx, 0) < kv_val do
            f.(f, kv_val - Map.get(bit, next_idx, 0), next_idx, div(pow, 2))
          else
            f.(f, kv_val, idx, div(pow, 2))
          end
        else
          idx + 1
        end
      end
      let_find.(let_find, kv, 0, p)
    end

    {cbit, sbit} = Enum.reduce(2..min(1 + dist, n - 1), {count_bit, sum_bit}, fn i, {cb, sb} ->
      val = elem(nums_tuple, i)
      r = Map.get(rank_map, val)
      {update.(cb, r, 1), update.(sb, r, val)}
    end)

    solve(1, n, k, dist, nums_tuple, cbit, sbit, rank_map, value_tuple, m, m_count, find_kth, query, update, 1_000_000_000_000_000)
  end

  defp get_p(m) do
    let_p = fn f, cur -> if cur * 2 <= m, do: f.(f, cur * 2), else: cur end
    let_p.(let_p, 1)
  end

  defp solve(i1, n, k, dist, nums_tuple, cbit, sbit, rank_map, value_tuple, m, m_count, find_kth, query, update, min_cost) do
    rank = find_kth.(m_count, cbit)
    c_prev = query.(cbit, rank - 1)
    s_prev = query.(sbit, rank - 1)
    low_sum = s_prev + (m_count - c_prev) * elem(value_tuple, rank - 1)
    cost = elem(nums_tuple, 0) + elem(nums_tuple, i1) + low_sum
    new_min_cost = min(min_cost, cost)

    if i1 < n - k + 1 do
      v_rem = elem(nums_tuple, i1 + 1)
      r_rem = Map.get(rank_map, v_rem)
      cbit1 = update.(cbit, r_rem, -1)
      sbit1 = update.(sbit, r_rem, -v_rem)
      {cbit2, sbit2} = if i1 + 1 + dist < n do
        v_add = elem(nums_tuple, i1 + 1 + dist)
        r_add = Map.get(rank_map, v_add)
        {update.(cbit1, r_add, 1), update.(sbit1, r_add, v_add)}
      else
        {cbit1, sbit1}
      end
      solve(i1 + 1, n, k, dist, nums_tuple, cbit2, sbit2, rank_map, value_tuple, m, m_count, find_kth, query, update, new_min_cost)
    else
      new_min_cost
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n log n) because we perform coordinate compression in O(n log n), and then process n elements through a sliding window where each insertion, deletion, and M-smallest sum query takes O(log n) time using a Fenwick tree and binary lifting.
- **Space Complexity:** O(n) to store the Fenwick trees (frequency and sum), the coordinate compression map, and the array of unique values.
