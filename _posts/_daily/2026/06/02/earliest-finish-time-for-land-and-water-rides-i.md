---
layout: post
title: "Earliest Finish Time for Land and Water Rides I"
date: 2026-06-02 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Two Pointers", "Binary Search", "Greedy", "Sorting"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i/
ai_solutions:
  - solutions:
      typescript: "function earliestFinishTime(landStartTime: number[], landDuration:\
        \ number[], waterStartTime: number[], waterDuration: number[]): number {\n \
        \   let minFinishTime = Infinity;\n    const n = landStartTime.length;\n   \
        \ const m = waterStartTime.length;\n\n    for (let i = 0; i < n; i++) {\n  \
        \      for (let j = 0; j < m; j++) {\n            const landEnd = landStartTime[i]\
        \ + landDuration[i];\n            const finish1 = Math.max(landEnd, waterStartTime[j])\
        \ + waterDuration[j];\n\n            const waterEnd = waterStartTime[j] + waterDuration[j];\n\
        \            const finish2 = Math.max(waterEnd, landStartTime[i]) + landDuration[i];\n\
        \n            minFinishTime = Math.min(minFinishTime, finish1, finish2);\n \
        \       }\n    }\n\n    return minFinishTime;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $landStartTime\n  \
        \   * @param Integer[] $landDuration\n     * @param Integer[] $waterStartTime\n\
        \     * @param Integer[] $waterDuration\n     * @return Integer\n     */\n \
        \   function earliestFinishTime($landStartTime, $landDuration, $waterStartTime,\
        \ $waterDuration) {\n        $minFinishTime = PHP_INT_MAX;\n        $n = count($landStartTime);\n\
        \        $m = count($waterStartTime);\n\n        for ($i = 0; $i < $n; $i++)\
        \ {\n            for ($j = 0; $j < $m; $j++) {\n                $landEnd = $landStartTime[$i]\
        \ + $landDuration[$i];\n                $finish1 = max($landEnd, $waterStartTime[$j])\
        \ + $waterDuration[$j];\n\n                $waterEnd = $waterStartTime[$j] +\
        \ $waterDuration[$j];\n                $finish2 = max($waterEnd, $landStartTime[$i])\
        \ + $landDuration[$i];\n\n                $minFinishTime = min($minFinishTime,\
        \ min($finish1, $finish2));\n            }\n        }\n\n        return $minFinishTime;\n\
        \    }\n}"
      swift: "class Solution {\n    func earliestFinishTime(_ landStartTime: [Int],\
        \ _ landDuration: [Int], _ waterStartTime: [Int], _ waterDuration: [Int]) ->\
        \ Int {\n        var minFinishTime = Int.max\n        let n = landStartTime.count\n\
        \        let m = waterStartTime.count\n\n        for i in 0..<n {\n        \
        \    for j in 0..<m {\n                let landEnd = landStartTime[i] + landDuration[i]\n\
        \                let finish1 = max(landEnd, waterStartTime[j]) + waterDuration[j]\n\
        \n                let waterEnd = waterStartTime[j] + waterDuration[j]\n    \
        \            let finish2 = max(waterEnd, landStartTime[i]) + landDuration[i]\n\
        \n                minFinishTime = min(minFinishTime, finish1, finish2)\n   \
        \         }\n        }\n\n        return minFinishTime\n    }\n}"
      kotlin: "class Solution {\n    fun earliestFinishTime(landStartTime: IntArray,\
        \ landDuration: IntArray, waterStartTime: IntArray, waterDuration: IntArray):\
        \ Int {\n        var minFinishTime = Int.MAX_VALUE\n        val n = landStartTime.size\n\
        \        val m = waterStartTime.size\n\n        for (i in 0 until n) {\n   \
        \         for (j in 0 until m) {\n                val landEnd = landStartTime[i]\
        \ + landDuration[i]\n                val finish1 = maxOf(landEnd, waterStartTime[j])\
        \ + waterDuration[j]\n\n                val waterEnd = waterStartTime[j] + waterDuration[j]\n\
        \                val finish2 = maxOf(waterEnd, landStartTime[i]) + landDuration[i]\n\
        \n                minFinishTime = minOf(minFinishTime, finish1, finish2)\n \
        \           }\n        }\n\n        return minFinishTime\n    }\n}"
      dart: "import 'dart:math';\n\nclass Solution {\n  int earliestFinishTime(List<int>\
        \ landStartTime, List<int> landDuration, List<int> waterStartTime, List<int>\
        \ waterDuration) {\n    int minFinishTime = 1 << 62;\n    int n = landStartTime.length;\n\
        \    int m = waterStartTime.length;\n\n    for (int i = 0; i < n; i++) {\n \
        \     for (int j = 0; j < m; j++) {\n        int landEnd = landStartTime[i]\
        \ + landDuration[i];\n        int finish1 = max(landEnd, waterStartTime[j])\
        \ + waterDuration[j];\n\n        int waterEnd = waterStartTime[j] + waterDuration[j];\n\
        \        int finish2 = max(waterEnd, landStartTime[i]) + landDuration[i];\n\n\
        \        minFinishTime = min(minFinishTime, min(finish1, finish2));\n      }\n\
        \    }\n\n    return minFinishTime;\n  }\n}"
      go: "func earliestFinishTime(landStartTime []int, landDuration []int, waterStartTime\
        \ []int, waterDuration []int) int {\n    minFinishTime := int(^uint(0) >> 1)\n\
        \    n := len(landStartTime)\n    m := len(waterStartTime)\n\n    for i := 0;\
        \ i < n; i++ {\n        for j := 0; j < m; j++ {\n            landEnd := landStartTime[i]\
        \ + landDuration[i]\n            startWater := landEnd\n            if waterStartTime[j]\
        \ > startWater {\n                startWater = waterStartTime[j]\n         \
        \   }\n            finish1 := startWater + waterDuration[j]\n\n            waterEnd\
        \ := waterStartTime[j] + waterDuration[j]\n            startLand := waterEnd\n\
        \            if landStartTime[i] > startLand {\n                startLand =\
        \ landStartTime[i]\n            }\n            finish2 := startLand + landDuration[i]\n\
        \n            if finish1 < minFinishTime {\n                minFinishTime =\
        \ finish1\n            }\n            if finish2 < minFinishTime {\n       \
        \         minFinishTime = finish2\n            }\n        }\n    }\n\n    return\
        \ minFinishTime\n}"
      ruby: "# @param {Integer[]} land_start_time\n# @param {Integer[]} land_duration\n\
        # @param {Integer[]} water_start_time\n# @param {Integer[]} water_duration\n\
        # @return {Integer}\ndef earliest_finish_time(land_start_time, land_duration,\
        \ water_start_time, water_duration)\n  min_finish = Float::INFINITY\n  land_start_time.each_with_index\
        \ do |ls, i|\n    ld = land_duration[i]\n    t_land = ls + ld\n    water_start_time.each_with_index\
        \ do |ws, j|\n      wd = water_duration[j]\n      t_water = ws + wd\n\n    \
        \  finish1 = [t_land, ws].max + wd\n      finish2 = [t_water, ls].max + ld\n\
        \n      min_finish = [min_finish, finish1, finish2].min\n    end\n  end\n  min_finish\n\
        end"
      scala: "object Solution {\n    def earliestFinishTime(landStartTime: Array[Int],\
        \ landDuration: Array[Int], waterStartTime: Array[Int], waterDuration: Array[Int]):\
        \ Int = {\n        var minFinish = Int.MaxValue\n        for (i <- landStartTime.indices)\
        \ {\n            val ls = landStartTime(i)\n            val ld = landDuration(i)\n\
        \            val tLand = ls + ld\n            for (j <- waterStartTime.indices)\
        \ {\n                val ws = waterStartTime(j)\n                val wd = waterDuration(j)\n\
        \                val tWater = ws + wd\n\n                val finish1 = math.max(tLand,\
        \ ws) + wd\n                val finish2 = math.max(tWater, ls) + ld\n\n    \
        \            minFinish = math.min(minFinish, math.min(finish1, finish2))\n \
        \           }\n        }\n        minFinish\n    }\n}"
      rust: "impl Solution {\n    pub fn earliest_finish_time(land_start_time: Vec<i32>,\
        \ land_duration: Vec<i32>, water_start_time: Vec<i32>, water_duration: Vec<i32>)\
        \ -> i32 {\n        let mut min_finish = i32::MAX;\n        for i in 0..land_start_time.len()\
        \ {\n            let ls = land_start_time[i];\n            let ld = land_duration[i];\n\
        \            let t_land = ls + ld;\n            for j in 0..water_start_time.len()\
        \ {\n                let ws = water_start_time[j];\n                let wd =\
        \ water_duration[j];\n                let t_water = ws + wd;\n\n           \
        \     let finish1 = t_land.max(ws) + wd;\n                let finish2 = t_water.max(ls)\
        \ + ld;\n\n                min_finish = min_finish.min(finish1.min(finish2));\n\
        \            }\n        }\n        min_finish\n    }\n}"
      racket: "(define/contract (earliest-finish-time landStartTime landDuration waterStartTime\
        \ waterDuration)\n  (-> (listof exact-integer?) (listof exact-integer?) (listof\
        \ exact-integer?) (listof exact-integer?) exact-integer?)\n  (let ([lands (map\
        \ cons landStartTime landDuration)]\n        [waters (map cons waterStartTime\
        \ waterDuration)])\n    (for*/fold ([min-finish +inf.0])\n               ([land\
        \ lands]\n                [water waters])\n      (let* ([ls (car land)]\n  \
        \           [ld (cdr land)]\n             [ws (car water)]\n             [wd\
        \ (cdr water)]\n             [t-land (+ ls ld)]\n             [t-water (+ ws\
        \ wd)]\n             [finish1 (+ (max t-land ws) wd)]\n             [finish2\
        \ (+ (max t-water ls) ld)])\n        (min min-finish finish1 finish2))))\n \
        \ )"
      erlang: "-spec earliest_finish_time(LandStartTime :: [integer()], LandDuration\
        \ :: [integer()], WaterStartTime :: [integer()], WaterDuration :: [integer()])\
        \ -> integer().\nearliest_finish_time(LandStartTime, LandDuration, WaterStartTime,\
        \ WaterDuration) ->\n  Lands = lists:zip(LandStartTime, LandDuration),\n  Waters\
        \ = lists:zip(WaterStartTime, WaterDuration),\n  Finishes = [\n    min(max(LS\
        \ + LD, WS) + WD, max(WS + WD, LS) + LD)\n    || {LS, LD} <- Lands, {WS, WD}\
        \ <- Waters\n  ],\n  lists:min(Finishes)."
      elixir: "defmodule Solution do\n  @spec earliest_finish_time(land_start_time ::\
        \ [integer], land_duration :: [integer], water_start_time :: [integer], water_duration\
        \ :: [integer]) :: integer\n  def earliest_finish_time(land_start_time, land_duration,\
        \ water_start_time, water_duration) do\n    lands = Enum.zip(land_start_time,\
        \ land_duration)\n    waters = Enum.zip(water_start_time, water_duration)\n\n\
        \    for {ls, ld} <- lands, {ws, wd} <- waters do\n      finish1 = max(ls +\
        \ ld, ws) + wd\n      finish2 = max(ws + wd, ls) + ld\n      min(finish1, finish2)\n\
        \    end\n    |> Enum.min()\n  end\nend"
      cpp: "class Solution {\npublic:\n    int earliestFinishTime(vector<int>& landStartTime,\
        \ vector<int>& landDuration, vector<int>& waterStartTime, vector<int>& waterDuration)\
        \ {\n        int answer = INT_MAX;\n        for (int i = 0; i < landStartTime.size();\
        \ ++i) {\n            for (int j = 0; j < waterStartTime.size(); ++j) {\n  \
        \              int landFirst = max(landStartTime[i] + landDuration[i], waterStartTime[j])\
        \ + waterDuration[j];\n                int waterFirst = max(waterStartTime[j]\
        \ + waterDuration[j], landStartTime[i]) + landDuration[i];\n               \
        \ answer = min(answer, min(landFirst, waterFirst));\n            }\n       \
        \ }\n        return answer;\n    }\n};"
      java: "class Solution {\n    public int earliestFinishTime(int[] landStartTime,\
        \ int[] landDuration, int[] waterStartTime, int[] waterDuration) {\n       \
        \ int answer = Integer.MAX_VALUE;\n        for (int i = 0; i < landStartTime.length;\
        \ i++) {\n            for (int j = 0; j < waterStartTime.length; j++) {\n  \
        \              int landFirst = Math.max(landStartTime[i] + landDuration[i],\
        \ waterStartTime[j]) + waterDuration[j];\n                int waterFirst = Math.max(waterStartTime[j]\
        \ + waterDuration[j], landStartTime[i]) + landDuration[i];\n               \
        \ answer = Math.min(answer, Math.min(landFirst, waterFirst));\n            }\n\
        \        }\n        return answer;\n    }\n}"
      python: "class Solution(object):\n    def earliestFinishTime(self, landStartTime,\
        \ landDuration, waterStartTime, waterDuration):\n        \"\"\"\n        :type\
        \ landStartTime: List[int]\n        :type landDuration: List[int]\n        :type\
        \ waterStartTime: List[int]\n        :type waterDuration: List[int]\n      \
        \  :rtype: int\n        \"\"\"\n        answer = float('inf')\n        for i\
        \ in range(len(landStartTime)):\n            for j in range(len(waterStartTime)):\n\
        \                land_first = max(landStartTime[i] + landDuration[i], waterStartTime[j])\
        \ + waterDuration[j]\n                water_first = max(waterStartTime[j] +\
        \ waterDuration[j], landStartTime[i]) + landDuration[i]\n                answer\
        \ = min(answer, land_first, water_first)\n        return answer"
      python3: "class Solution:\n    def earliestFinishTime(self, landStartTime: List[int],\
        \ landDuration: List[int], waterStartTime: List[int], waterDuration: List[int])\
        \ -> int:\n        answer = float('inf')\n        for i in range(len(landStartTime)):\n\
        \            for j in range(len(waterStartTime)):\n                land_first\
        \ = max(landStartTime[i] + landDuration[i], waterStartTime[j]) + waterDuration[j]\n\
        \                water_first = max(waterStartTime[j] + waterDuration[j], landStartTime[i])\
        \ + landDuration[i]\n                answer = min(answer, land_first, water_first)\n\
        \        return answer"
      c: "#include <limits.h>\n\nint earliestFinishTime(int* landStartTime, int landStartTimeSize,\
        \ int* landDuration, int landDurationSize, int* waterStartTime, int waterStartTimeSize,\
        \ int* waterDuration, int waterDurationSize) {\n    int answer = INT_MAX;\n\
        \    for (int i = 0; i < landStartTimeSize; ++i) {\n        for (int j = 0;\
        \ j < waterStartTimeSize; ++j) {\n            int landEnd = landStartTime[i]\
        \ + landDuration[i];\n            int waterEnd = waterStartTime[j] + waterDuration[j];\n\
        \            int landFirst = (landEnd > waterStartTime[j] ? landEnd : waterStartTime[j])\
        \ + waterDuration[j];\n            int waterFirst = (waterEnd > landStartTime[i]\
        \ ? waterEnd : landStartTime[i]) + landDuration[i];\n            if (landFirst\
        \ < answer) answer = landFirst;\n            if (waterFirst < answer) answer\
        \ = waterFirst;\n        }\n    }\n    return answer;\n}"
      csharp: "public class Solution {\n    public int EarliestFinishTime(int[] landStartTime,\
        \ int[] landDuration, int[] waterStartTime, int[] waterDuration) {\n       \
        \ int answer = int.MaxValue;\n        for (int i = 0; i < landStartTime.Length;\
        \ i++) {\n            for (int j = 0; j < waterStartTime.Length; j++) {\n  \
        \              int landFirst = Math.Max(landStartTime[i] + landDuration[i],\
        \ waterStartTime[j]) + waterDuration[j];\n                int waterFirst = Math.Max(waterStartTime[j]\
        \ + waterDuration[j], landStartTime[i]) + landDuration[i];\n               \
        \ answer = Math.Min(answer, Math.Min(landFirst, waterFirst));\n            }\n\
        \        }\n        return answer;\n    }\n}"
      javascript: "/**\n * @param {number[]} landStartTime\n * @param {number[]} landDuration\n\
        \ * @param {number[]} waterStartTime\n * @param {number[]} waterDuration\n *\
        \ @return {number}\n */\nvar earliestFinishTime = function(landStartTime, landDuration,\
        \ waterStartTime, waterDuration) {\n    let answer = Infinity;\n    for (let\
        \ i = 0; i < landStartTime.length; i++) {\n        for (let j = 0; j < waterStartTime.length;\
        \ j++) {\n            const landFirst = Math.max(landStartTime[i] + landDuration[i],\
        \ waterStartTime[j]) + waterDuration[j];\n            const waterFirst = Math.max(waterStartTime[j]\
        \ + waterDuration[j], landStartTime[i]) + landDuration[i];\n            answer\
        \ = Math.min(answer, landFirst, waterFirst);\n        }\n    }\n    return answer;\n\
        };"
    approach: 'We can determine the earliest finish time by evaluating all possible
      combinations of a land ride and a water ride in both possible orders. Given ride
      $i$ from land rides and ride $j$ from water rides, there are two sequences to
      consider: land ride first or water ride first. In the first sequence, the land
      ride starts at its earliest opening time landStartTime[i] and finishes at $t_1
      = \text{landStartTime}[i] + \text{landDuration}[i]$. The water ride can then begin
      at $\max(t_1, \text{waterStartTime}[j])$ and finishes at $\max(t_1, \text{waterStartTime}[j])
      + \text{waterDuration}[j]$.


      Similarly, in the second sequence where the water ride is taken first, the water
      ride starts at waterStartTime[j] and ends at $t_2 = \text{waterStartTime}[j] +
      \text{waterDuration}[j]$. The subsequent land ride then finishes at $\max(t_2,
      \text{landStartTime}[i]) + \text{landDuration}[i]$. Since the constraints on $n$
      and $m$ are up to 100, we can use a nested loop over all pairs $(i, j)$ to compute
      the finish time for both orders and return the minimum finish time observed across
      all candidates.'
    time_complexity: O(n * m), where n is the number of land rides and m is the number
      of water rides. We iterate through every pair of land and water rides and compute
      the finish times for both sequences in constant time.
    space_complexity: O(1) auxiliary space, as the algorithm only uses a few scalar
      variables to track the minimum finish time without allocating extra data structures.
    elapsed_time: 27.11763572692871
    model: gpt-6-luna
    generated_at: '2026-11-11 20:38:23 '
---

## Problem #3633: Earliest Finish Time for Land and Water Rides I

**Difficulty:** Easy

**Topics:** Array, Two Pointers, Binary Search, Greedy, Sorting

## Problem Description

<p data-end="143" data-start="53">You are given two categories of theme park attractions: <strong data-end="122" data-start="108">land rides</strong> and <strong data-end="142" data-start="127">water rides</strong>.</p>

<ul>
	<li data-end="163" data-start="147"><strong data-end="161" data-start="147">Land rides</strong>

	<ul>
		<li data-end="245" data-start="168"><code data-end="186" data-start="168">landStartTime[i]</code> &ndash; the earliest time the <code>i<sup>th</sup></code> land ride can be boarded.</li>
		<li data-end="306" data-start="250"><code data-end="267" data-start="250">landDuration[i]</code> &ndash; how long the <code>i<sup>th</sup></code> land ride lasts.</li>
	</ul>
	</li>
	<li><strong data-end="325" data-start="310">Water rides</strong>
	<ul>
		<li><code data-end="351" data-start="332">waterStartTime[j]</code> &ndash; the earliest time the <code>j<sup>th</sup></code> water ride can be boarded.</li>
		<li><code data-end="434" data-start="416">waterDuration[j]</code> &ndash; how long the <code>j<sup>th</sup></code> water ride lasts.</li>
	</ul>
	</li>
</ul>

<p data-end="569" data-start="476">A tourist must experience <strong data-end="517" data-start="502">exactly one</strong> ride from <strong data-end="536" data-start="528">each</strong> category, in <strong data-end="566" data-start="550">either order</strong>.</p>

<ul>
	<li data-end="641" data-start="573">A ride may be started at its opening time or <strong data-end="638" data-start="618">any later moment</strong>.</li>
	<li data-end="715" data-start="644">If a ride is started at time <code data-end="676" data-start="673">t</code>, it finishes at time <code data-end="712" data-start="698">t + duration</code>.</li>
	<li data-end="834" data-start="718">Immediately after finishing one ride the tourist may board the other (if it is already open) or wait until it opens.</li>
</ul>

<p data-end="917" data-start="836">Return the <strong data-end="873" data-start="847">earliest possible time</strong> at which the tourist can finish both rides.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">landStartTime = [2,8], landDuration = [4,1], waterStartTime = [6], waterDuration = [3]</span></p>

<p><strong>Output:</strong> <span class="example-io">9</span></p>

<p><strong>Explanation:</strong>​​​​​​​</p>

<ul>
	<li data-end="181" data-start="145">Plan A (land ride 0 &rarr; water ride 0):
	<ul>
		<li data-end="272" data-start="186">Start land ride 0 at time <code data-end="234" data-start="212">landStartTime[0] = 2</code>. Finish at <code data-end="271" data-start="246">2 + landDuration[0] = 6</code>.</li>
		<li data-end="392" data-start="277">Water ride 0 opens at time <code data-end="327" data-start="304">waterStartTime[0] = 6</code>. Start immediately at <code data-end="353" data-start="350">6</code>, finish at <code data-end="391" data-start="365">6 + waterDuration[0] = 9</code>.</li>
	</ul>
	</li>
	<li data-end="432" data-start="396">Plan B (water ride 0 &rarr; land ride 1):
	<ul>
		<li data-end="526" data-start="437">Start water ride 0 at time <code data-end="487" data-start="464">waterStartTime[0] = 6</code>. Finish at <code data-end="525" data-start="499">6 + waterDuration[0] = 9</code>.</li>
		<li data-end="632" data-start="531">Land ride 1 opens at <code data-end="574" data-start="552">landStartTime[1] = 8</code>. Start at time <code data-end="593" data-start="590">9</code>, finish at <code data-end="631" data-start="605">9 + landDuration[1] = 10</code>.</li>
	</ul>
	</li>
	<li data-end="672" data-start="636">Plan C (land ride 1 &rarr; water ride 0):
	<ul>
		<li data-end="763" data-start="677">Start land ride 1 at time <code data-end="725" data-start="703">landStartTime[1] = 8</code>. Finish at <code data-end="762" data-start="737">8 + landDuration[1] = 9</code>.</li>
		<li data-end="873" data-start="768">Water ride 0 opened at <code data-end="814" data-start="791">waterStartTime[0] = 6</code>. Start at time <code data-end="833" data-start="830">9</code>, finish at <code data-end="872" data-start="845">9 + waterDuration[0] = 12</code>.</li>
	</ul>
	</li>
	<li data-end="913" data-start="877">Plan D (water ride 0 &rarr; land ride 0):
	<ul>
		<li data-end="1007" data-start="918">Start water ride 0 at time <code data-end="968" data-start="945">waterStartTime[0] = 6</code>. Finish at <code data-end="1006" data-start="980">6 + waterDuration[0] = 9</code>.</li>
		<li data-end="1114" data-start="1012">Land ride 0 opened at <code data-end="1056" data-start="1034">landStartTime[0] = 2</code>. Start at time <code data-end="1075" data-start="1072">9</code>, finish at <code data-end="1113" data-start="1087">9 + landDuration[0] = 13</code>.</li>
	</ul>
	</li>
</ul>

<p data-end="1161" data-is-last-node="" data-is-only-node="" data-start="1116">Plan A gives the earliest finish time of 9.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">landStartTime = [5], landDuration = [3], waterStartTime = [1], waterDuration = [10]</span></p>

<p><strong>Output:</strong> <span class="example-io">14</span></p>

<p><strong>Explanation:</strong>​​​​​​​</p>

<ul data-end="1589" data-start="1086">
	<li data-end="1124" data-start="1088">Plan A (water ride 0 &rarr; land ride 0):
	<ul>
		<li data-end="1219" data-start="1129">Start water ride 0 at time <code data-end="1179" data-start="1156">waterStartTime[0] = 1</code>. Finish at <code data-end="1218" data-start="1191">1 + waterDuration[0] = 11</code>.</li>
		<li data-end="1338" data-start="1224">Land ride 0 opened at <code data-end="1268" data-start="1246">landStartTime[0] = 5</code>. Start immediately at <code data-end="1295" data-start="1291">11</code> and finish at <code data-end="1337" data-start="1310">11 + landDuration[0] = 14</code>.</li>
	</ul>
	</li>
	<li data-end="1378" data-start="1342">Plan B (land ride 0 &rarr; water ride 0):
	<ul>
		<li data-end="1469" data-start="1383">Start land ride 0 at time <code data-end="1431" data-start="1409">landStartTime[0] = 5</code>. Finish at <code data-end="1468" data-start="1443">5 + landDuration[0] = 8</code>.</li>
		<li data-end="1589" data-start="1474">Water ride 0 opened at <code data-end="1520" data-start="1497">waterStartTime[0] = 1</code>. Start immediately at <code data-end="1546" data-start="1543">8</code> and finish at <code data-end="1588" data-start="1561">8 + waterDuration[0] = 18</code>.</li>
	</ul>
	</li>
</ul>

<p data-end="1640" data-is-last-node="" data-is-only-node="" data-start="1591">Plan A provides the earliest finish time of 14.<strong>​​​​​​​</strong></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li data-end="38" data-start="16"><code data-end="36" data-start="16">1 &lt;= n, m &lt;= 100</code></li>
	<li data-end="93" data-start="41"><code data-end="91" data-start="41">landStartTime.length == landDuration.length == n</code></li>
	<li data-end="150" data-start="96"><code data-end="148" data-start="96">waterStartTime.length == waterDuration.length == m</code></li>
	<li data-end="237" data-start="153"><code data-end="235" data-start="153">1 &lt;= landStartTime[i], landDuration[i], waterStartTime[j], waterDuration[j] &lt;= 1000</code></li>
</ul>


## Hints

1. Use brute force

## 🤖 AI-Generated Solution (gpt-6-luna)

### Approach

We can determine the earliest finish time by evaluating all possible combinations of a land ride and a water ride in both possible orders. Given ride $i$ from land rides and ride $j$ from water rides, there are two sequences to consider: land ride first or water ride first. In the first sequence, the land ride starts at its earliest opening time landStartTime[i] and finishes at $t_1 = \text{landStartTime}[i] + \text{landDuration}[i]$. The water ride can then begin at $\max(t_1, \text{waterStartTime}[j])$ and finishes at $\max(t_1, \text{waterStartTime}[j]) + \text{waterDuration}[j]$.

Similarly, in the second sequence where the water ride is taken first, the water ride starts at waterStartTime[j] and ends at $t_2 = \text{waterStartTime}[j] + \text{waterDuration}[j]$. The subsequent land ride then finishes at $\max(t_2, \text{landStartTime}[i]) + \text{landDuration}[i]$. Since the constraints on $n$ and $m$ are up to 100, we can use a nested loop over all pairs $(i, j)$ to compute the finish time for both orders and return the minimum finish time observed across all candidates.

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
    int earliestFinishTime(vector<int>& landStartTime, vector<int>& landDuration, vector<int>& waterStartTime, vector<int>& waterDuration) {
        int answer = INT_MAX;
        for (int i = 0; i < landStartTime.size(); ++i) {
            for (int j = 0; j < waterStartTime.size(); ++j) {
                int landFirst = max(landStartTime[i] + landDuration[i], waterStartTime[j]) + waterDuration[j];
                int waterFirst = max(waterStartTime[j] + waterDuration[j], landStartTime[i]) + landDuration[i];
                answer = min(answer, min(landFirst, waterFirst));
            }
        }
        return answer;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int earliestFinishTime(int[] landStartTime, int[] landDuration, int[] waterStartTime, int[] waterDuration) {
        int answer = Integer.MAX_VALUE;
        for (int i = 0; i < landStartTime.length; i++) {
            for (int j = 0; j < waterStartTime.length; j++) {
                int landFirst = Math.max(landStartTime[i] + landDuration[i], waterStartTime[j]) + waterDuration[j];
                int waterFirst = Math.max(waterStartTime[j] + waterDuration[j], landStartTime[i]) + landDuration[i];
                answer = Math.min(answer, Math.min(landFirst, waterFirst));
            }
        }
        return answer;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        answer = float('inf')
        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                land_first = max(landStartTime[i] + landDuration[i], waterStartTime[j]) + waterDuration[j]
                water_first = max(waterStartTime[j] + waterDuration[j], landStartTime[i]) + landDuration[i]
                answer = min(answer, land_first, water_first)
        return answer
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        answer = float('inf')
        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                land_first = max(landStartTime[i] + landDuration[i], waterStartTime[j]) + waterDuration[j]
                water_first = max(waterStartTime[j] + waterDuration[j], landStartTime[i]) + landDuration[i]
                answer = min(answer, land_first, water_first)
        return answer
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <limits.h>

int earliestFinishTime(int* landStartTime, int landStartTimeSize, int* landDuration, int landDurationSize, int* waterStartTime, int waterStartTimeSize, int* waterDuration, int waterDurationSize) {
    int answer = INT_MAX;
    for (int i = 0; i < landStartTimeSize; ++i) {
        for (int j = 0; j < waterStartTimeSize; ++j) {
            int landEnd = landStartTime[i] + landDuration[i];
            int waterEnd = waterStartTime[j] + waterDuration[j];
            int landFirst = (landEnd > waterStartTime[j] ? landEnd : waterStartTime[j]) + waterDuration[j];
            int waterFirst = (waterEnd > landStartTime[i] ? waterEnd : landStartTime[i]) + landDuration[i];
            if (landFirst < answer) answer = landFirst;
            if (waterFirst < answer) answer = waterFirst;
        }
    }
    return answer;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int EarliestFinishTime(int[] landStartTime, int[] landDuration, int[] waterStartTime, int[] waterDuration) {
        int answer = int.MaxValue;
        for (int i = 0; i < landStartTime.Length; i++) {
            for (int j = 0; j < waterStartTime.Length; j++) {
                int landFirst = Math.Max(landStartTime[i] + landDuration[i], waterStartTime[j]) + waterDuration[j];
                int waterFirst = Math.Max(waterStartTime[j] + waterDuration[j], landStartTime[i]) + landDuration[i];
                answer = Math.Min(answer, Math.Min(landFirst, waterFirst));
            }
        }
        return answer;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[]} landStartTime
 * @param {number[]} landDuration
 * @param {number[]} waterStartTime
 * @param {number[]} waterDuration
 * @return {number}
 */
var earliestFinishTime = function(landStartTime, landDuration, waterStartTime, waterDuration) {
    let answer = Infinity;
    for (let i = 0; i < landStartTime.length; i++) {
        for (let j = 0; j < waterStartTime.length; j++) {
            const landFirst = Math.max(landStartTime[i] + landDuration[i], waterStartTime[j]) + waterDuration[j];
            const waterFirst = Math.max(waterStartTime[j] + waterDuration[j], landStartTime[i]) + landDuration[i];
            answer = Math.min(answer, landFirst, waterFirst);
        }
    }
    return answer;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function earliestFinishTime(landStartTime: number[], landDuration: number[], waterStartTime: number[], waterDuration: number[]): number {
    let minFinishTime = Infinity;
    const n = landStartTime.length;
    const m = waterStartTime.length;

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            const landEnd = landStartTime[i] + landDuration[i];
            const finish1 = Math.max(landEnd, waterStartTime[j]) + waterDuration[j];

            const waterEnd = waterStartTime[j] + waterDuration[j];
            const finish2 = Math.max(waterEnd, landStartTime[i]) + landDuration[i];

            minFinishTime = Math.min(minFinishTime, finish1, finish2);
        }
    }

    return minFinishTime;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[] $landStartTime
     * @param Integer[] $landDuration
     * @param Integer[] $waterStartTime
     * @param Integer[] $waterDuration
     * @return Integer
     */
    function earliestFinishTime($landStartTime, $landDuration, $waterStartTime, $waterDuration) {
        $minFinishTime = PHP_INT_MAX;
        $n = count($landStartTime);
        $m = count($waterStartTime);

        for ($i = 0; $i < $n; $i++) {
            for ($j = 0; $j < $m; $j++) {
                $landEnd = $landStartTime[$i] + $landDuration[$i];
                $finish1 = max($landEnd, $waterStartTime[$j]) + $waterDuration[$j];

                $waterEnd = $waterStartTime[$j] + $waterDuration[$j];
                $finish2 = max($waterEnd, $landStartTime[$i]) + $landDuration[$i];

                $minFinishTime = min($minFinishTime, min($finish1, $finish2));
            }
        }

        return $minFinishTime;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func earliestFinishTime(_ landStartTime: [Int], _ landDuration: [Int], _ waterStartTime: [Int], _ waterDuration: [Int]) -> Int {
        var minFinishTime = Int.max
        let n = landStartTime.count
        let m = waterStartTime.count

        for i in 0..<n {
            for j in 0..<m {
                let landEnd = landStartTime[i] + landDuration[i]
                let finish1 = max(landEnd, waterStartTime[j]) + waterDuration[j]

                let waterEnd = waterStartTime[j] + waterDuration[j]
                let finish2 = max(waterEnd, landStartTime[i]) + landDuration[i]

                minFinishTime = min(minFinishTime, finish1, finish2)
            }
        }

        return minFinishTime
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun earliestFinishTime(landStartTime: IntArray, landDuration: IntArray, waterStartTime: IntArray, waterDuration: IntArray): Int {
        var minFinishTime = Int.MAX_VALUE
        val n = landStartTime.size
        val m = waterStartTime.size

        for (i in 0 until n) {
            for (j in 0 until m) {
                val landEnd = landStartTime[i] + landDuration[i]
                val finish1 = maxOf(landEnd, waterStartTime[j]) + waterDuration[j]

                val waterEnd = waterStartTime[j] + waterDuration[j]
                val finish2 = maxOf(waterEnd, landStartTime[i]) + landDuration[i]

                minFinishTime = minOf(minFinishTime, finish1, finish2)
            }
        }

        return minFinishTime
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
  int earliestFinishTime(List<int> landStartTime, List<int> landDuration, List<int> waterStartTime, List<int> waterDuration) {
    int minFinishTime = 1 << 62;
    int n = landStartTime.length;
    int m = waterStartTime.length;

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        int landEnd = landStartTime[i] + landDuration[i];
        int finish1 = max(landEnd, waterStartTime[j]) + waterDuration[j];

        int waterEnd = waterStartTime[j] + waterDuration[j];
        int finish2 = max(waterEnd, landStartTime[i]) + landDuration[i];

        minFinishTime = min(minFinishTime, min(finish1, finish2));
      }
    }

    return minFinishTime;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func earliestFinishTime(landStartTime []int, landDuration []int, waterStartTime []int, waterDuration []int) int {
    minFinishTime := int(^uint(0) >> 1)
    n := len(landStartTime)
    m := len(waterStartTime)

    for i := 0; i < n; i++ {
        for j := 0; j < m; j++ {
            landEnd := landStartTime[i] + landDuration[i]
            startWater := landEnd
            if waterStartTime[j] > startWater {
                startWater = waterStartTime[j]
            }
            finish1 := startWater + waterDuration[j]

            waterEnd := waterStartTime[j] + waterDuration[j]
            startLand := waterEnd
            if landStartTime[i] > startLand {
                startLand = landStartTime[i]
            }
            finish2 := startLand + landDuration[i]

            if finish1 < minFinishTime {
                minFinishTime = finish1
            }
            if finish2 < minFinishTime {
                minFinishTime = finish2
            }
        }
    }

    return minFinishTime
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} land_start_time
# @param {Integer[]} land_duration
# @param {Integer[]} water_start_time
# @param {Integer[]} water_duration
# @return {Integer}
def earliest_finish_time(land_start_time, land_duration, water_start_time, water_duration)
  min_finish = Float::INFINITY
  land_start_time.each_with_index do |ls, i|
    ld = land_duration[i]
    t_land = ls + ld
    water_start_time.each_with_index do |ws, j|
      wd = water_duration[j]
      t_water = ws + wd

      finish1 = [t_land, ws].max + wd
      finish2 = [t_water, ls].max + ld

      min_finish = [min_finish, finish1, finish2].min
    end
  end
  min_finish
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def earliestFinishTime(landStartTime: Array[Int], landDuration: Array[Int], waterStartTime: Array[Int], waterDuration: Array[Int]): Int = {
        var minFinish = Int.MaxValue
        for (i <- landStartTime.indices) {
            val ls = landStartTime(i)
            val ld = landDuration(i)
            val tLand = ls + ld
            for (j <- waterStartTime.indices) {
                val ws = waterStartTime(j)
                val wd = waterDuration(j)
                val tWater = ws + wd

                val finish1 = math.max(tLand, ws) + wd
                val finish2 = math.max(tWater, ls) + ld

                minFinish = math.min(minFinish, math.min(finish1, finish2))
            }
        }
        minFinish
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn earliest_finish_time(land_start_time: Vec<i32>, land_duration: Vec<i32>, water_start_time: Vec<i32>, water_duration: Vec<i32>) -> i32 {
        let mut min_finish = i32::MAX;
        for i in 0..land_start_time.len() {
            let ls = land_start_time[i];
            let ld = land_duration[i];
            let t_land = ls + ld;
            for j in 0..water_start_time.len() {
                let ws = water_start_time[j];
                let wd = water_duration[j];
                let t_water = ws + wd;

                let finish1 = t_land.max(ws) + wd;
                let finish2 = t_water.max(ls) + ld;

                min_finish = min_finish.min(finish1.min(finish2));
            }
        }
        min_finish
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (earliest-finish-time landStartTime landDuration waterStartTime waterDuration)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?) (listof exact-integer?) exact-integer?)
  (let ([lands (map cons landStartTime landDuration)]
        [waters (map cons waterStartTime waterDuration)])
    (for*/fold ([min-finish +inf.0])
               ([land lands]
                [water waters])
      (let* ([ls (car land)]
             [ld (cdr land)]
             [ws (car water)]
             [wd (cdr water)]
             [t-land (+ ls ld)]
             [t-water (+ ws wd)]
             [finish1 (+ (max t-land ws) wd)]
             [finish2 (+ (max t-water ls) ld)])
        (min min-finish finish1 finish2))))
  )
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec earliest_finish_time(LandStartTime :: [integer()], LandDuration :: [integer()], WaterStartTime :: [integer()], WaterDuration :: [integer()]) -> integer().
earliest_finish_time(LandStartTime, LandDuration, WaterStartTime, WaterDuration) ->
  Lands = lists:zip(LandStartTime, LandDuration),
  Waters = lists:zip(WaterStartTime, WaterDuration),
  Finishes = [
    min(max(LS + LD, WS) + WD, max(WS + WD, LS) + LD)
    || {LS, LD} <- Lands, {WS, WD} <- Waters
  ],
  lists:min(Finishes).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec earliest_finish_time(land_start_time :: [integer], land_duration :: [integer], water_start_time :: [integer], water_duration :: [integer]) :: integer
  def earliest_finish_time(land_start_time, land_duration, water_start_time, water_duration) do
    lands = Enum.zip(land_start_time, land_duration)
    waters = Enum.zip(water_start_time, water_duration)

    for {ls, ld} <- lands, {ws, wd} <- waters do
      finish1 = max(ls + ld, ws) + wd
      finish2 = max(ws + wd, ls) + ld
      min(finish1, finish2)
    end
    |> Enum.min()
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n * m), where n is the number of land rides and m is the number of water rides. We iterate through every pair of land and water rides and compute the finish times for both sequences in constant time.
- **Space Complexity:** O(1) auxiliary space, as the algorithm only uses a few scalar variables to track the minimum finish time without allocating extra data structures.
