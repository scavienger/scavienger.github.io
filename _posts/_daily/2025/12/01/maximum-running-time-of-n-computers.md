---
layout: post
title: "Maximum Running Time of N Computers"
date: 2025-12-01 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Binary Search", "Greedy", "Sorting"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/maximum-running-time-of-n-computers/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    bool check(long long target_time, int n,\
        \ const std::vector<int>& batteries) {\n        long long extra_power = 0;\n\
        \        long long computers_to_power = n;\n\n        for (int b : batteries)\
        \ {\n            if (b >= target_time) {\n                computers_to_power--;\n\
        \                extra_power += (b - target_time);\n            } else {\n \
        \               extra_power += b;\n            }\n        }\n\n        // If\
        \ computers_to_power is negative, it means we have more than enough strong batteries\n\
        \        // to cover all 'n' computers individually for 'target_time' minutes.\n\
        \        // In this case, no additional power is needed from the 'extra_power'\
        \ pool for these computers.\n        return extra_power >= std::max(0LL, computers_to_power)\
        \ * target_time;\n    }\n\n    long long maxRunTime(int n, std::vector<int>&\
        \ batteries) {\n        long long low = 0;\n        long long high = 0;\n  \
        \      for (int b : batteries) {\n            high += b;\n        }\n      \
        \  high /= n;\n\n        long long ans = 0;\n\n        while (low <= high) {\n\
        \            long long mid = low + (high - low) / 2;\n            if (check(mid,\
        \ n, batteries)) {\n                ans = mid;\n                low = mid +\
        \ 1;\n            } else {\n                high = mid - 1;\n            }\n\
        \        }\n        return ans;\n    }\n};"
      java: "class Solution {\n    public boolean check(long target_time, int n, int[]\
        \ batteries) {\n        long extra_power = 0;\n        long computers_to_power\
        \ = n;\n\n        for (int b : batteries) {\n            if (b >= target_time)\
        \ {\n                computers_to_power--;\n                extra_power += (b\
        \ - target_time);\n            } else {\n                extra_power += b;\n\
        \            }\n        }\n\n        return extra_power >= Math.max(0L, computers_to_power)\
        \ * target_time;\n    }\n\n    public long maxRunTime(int n, int[] batteries)\
        \ {\n        long low = 0;\n        long high = 0;\n        for (int b : batteries)\
        \ {\n            high += b;\n        }\n        high /= n;\n\n        long ans\
        \ = 0;\n\n        while (low <= high) {\n            long mid = low + (high\
        \ - low) / 2;\n            if (check(mid, n, batteries)) {\n               \
        \ ans = mid;\n                low = mid + 1;\n            } else {\n       \
        \         high = mid - 1;\n            }\n        }\n        return ans;\n \
        \   }\n}"
      python: "class Solution:\n    def maxRunTime(self, n: int, batteries: List[int])\
        \ -> int:\n\n        def check(target_time: int) -> bool:\n            extra_power\
        \ = 0\n            computers_to_power = n\n\n            for b in batteries:\n\
        \                if b >= target_time:\n                    computers_to_power\
        \ -= 1\n                    extra_power += (b - target_time)\n             \
        \   else:\n                    extra_power += b\n\n            return extra_power\
        \ >= max(0, computers_to_power) * target_time\n\n        low = 0\n        high\
        \ = sum(batteries) // n\n        ans = 0\n\n        while low <= high:\n   \
        \         mid = low + (high - low) // 2\n            if check(mid):\n      \
        \          ans = mid\n                low = mid + 1\n            else:\n   \
        \             high = mid - 1\n\n        return ans"
      python3: "class Solution:\n    def maxRunTime(self, n: int, batteries: List[int])\
        \ -> int:\n\n        def check(target_time: int) -> bool:\n            extra_power\
        \ = 0\n            computers_to_power = n\n\n            for b in batteries:\n\
        \                if b >= target_time:\n                    computers_to_power\
        \ -= 1\n                    extra_power += (b - target_time)\n             \
        \   else:\n                    extra_power += b\n\n            return extra_power\
        \ >= max(0, computers_to_power) * target_time\n\n        low = 0\n        high\
        \ = sum(batteries) // n\n        ans = 0\n\n        while low <= high:\n   \
        \         mid = low + (high - low) // 2\n            if check(mid):\n      \
        \          ans = mid\n                low = mid + 1\n            else:\n   \
        \             high = mid - 1\n\n        return ans"
      c: "#include <stdio.h>\n#include <stdbool.h>\n#include <stdlib.h>\n#include <string.h>\n\
        \n// Using long long for sums and time values to prevent overflow\nbool check(long\
        \ long target_time, int n, int* batteries, int batteriesSize) {\n    long long\
        \ extra_power = 0;\n    long long computers_to_power = n;\n\n    for (int i\
        \ = 0; i < batteriesSize; i++) {\n        long long b = batteries[i];\n    \
        \    if (b >= target_time) {\n            computers_to_power--;\n          \
        \  extra_power += (b - target_time);\n        } else {\n            extra_power\
        \ += b;\n        }\n    }\n\n    long long needed_power = (computers_to_power\
        \ > 0 ? computers_to_power : 0) * target_time;\n    return extra_power >= needed_power;\n\
        }\n\nlong long maxRunTime(int n, int* batteries, int batteriesSize) {\n    long\
        \ long low = 0;\n    long long high = 0;\n    for (int i = 0; i < batteriesSize;\
        \ i++) {\n        high += batteries[i];\n    }\n    high /= n;\n\n    long long\
        \ ans = 0;\n\n    while (low <= high) {\n        long long mid = low + (high\
        \ - low) / 2;\n        if (check(mid, n, batteries, batteriesSize)) {\n    \
        \        ans = mid;\n            low = mid + 1;\n        } else {\n        \
        \    high = mid - 1;\n        }\n    }\n    return ans;\n}"
      csharp: "public class Solution {\n    private bool Check(long targetTime, int\
        \ n, int[] batteries) {\n        long extraPower = 0;\n        long computersToPower\
        \ = n;\n\n        foreach (int b in batteries) {\n            if (b >= targetTime)\
        \ {\n                computersToPower--;\n                extraPower += (b -\
        \ targetTime);\n            } else {\n                extraPower += b;\n   \
        \         }\n        }\n\n        return extraPower >= Math.Max(0L, computersToPower)\
        \ * targetTime;\n    }\n\n    public long MaxRunTime(int n, int[] batteries)\
        \ {\n        long low = 0;\n        long high = 0;\n        foreach (int b in\
        \ batteries) {\n            high += b;\n        }\n        high /= n;\n\n  \
        \      long ans = 0;\n\n        while (low <= high) {\n            long mid\
        \ = low + (high - low) / 2;\n            if (Check(mid, n, batteries)) {\n \
        \               ans = mid;\n                low = mid + 1;\n            } else\
        \ {\n                high = mid - 1;\n            }\n        }\n        return\
        \ ans;\n    }\n}"
      javascript: "/**\n * @param {number} n\n * @param {number[]} batteries\n * @return\
        \ {number}\n */\nvar maxRunTime = function(n, batteries) {\n    const check\
        \ = (targetTime) => {\n        let extraPower = 0n; // Use BigInt for large\
        \ numbers\n        let computersToPower = BigInt(n);\n        const targetTimeBig\
        \ = BigInt(targetTime);\n\n        for (const b of batteries) {\n          \
        \  const batteryCapacityBig = BigInt(b);\n            if (batteryCapacityBig\
        \ >= targetTimeBig) {\n                computersToPower--;\n               \
        \ extraPower += (batteryCapacityBig - targetTimeBig);\n            } else {\n\
        \                extraPower += batteryCapacityBig;\n            }\n        }\n\
        \n        return extraPower >= (computersToPower > 0n ? computersToPower : 0n)\
        \ * targetTimeBig;\n    };\n\n    let low = 0n;\n    let high = 0n;\n    for\
        \ (const b of batteries) {\n        high += BigInt(b);\n    }\n    high /= BigInt(n);\n\
        \n    let ans = 0n;\n\n    while (low <= high) {\n        let mid = low + (high\
        \ - low) / 2n;\n        if (check(Number(mid))) { // Pass Number to check function,\
        \ convert back to BigInt inside if needed\n            ans = mid;\n        \
        \    low = mid + 1n;\n        } else {\n            high = mid - 1n;\n     \
        \   }\n    }\n    return Number(ans);\n};"
      typescript: "function maxRunTime(n: number, batteries: number[]): number {\n \
        \   const check = (targetTime: bigint): boolean => {\n        let extraPower:\
        \ bigint = 0n;\n        let computersToPower: bigint = BigInt(n);\n\n      \
        \  for (const b of batteries) {\n            const batteryCapacityBig = BigInt(b);\n\
        \            if (batteryCapacityBig >= targetTime) {\n                computersToPower--;\n\
        \                extraPower += (batteryCapacityBig - targetTime);\n        \
        \    } else {\n                extraPower += batteryCapacityBig;\n         \
        \   }\n        }\n\n        return extraPower >= (computersToPower > 0n ? computersToPower\
        \ : 0n) * targetTime;\n    };\n\n    let low: bigint = 0n;\n    let high: bigint\
        \ = 0n;\n    for (const b of batteries) {\n        high += BigInt(b);\n    }\n\
        \    high /= BigInt(n);\n\n    let ans: bigint = 0n;\n\n    while (low <= high)\
        \ {\n        const mid: bigint = low + (high - low) / 2n;\n        if (check(mid))\
        \ {\n            ans = mid;\n            low = mid + 1n;\n        } else {\n\
        \            high = mid - 1n;\n        }\n    }\n    return Number(ans);\n};"
      php: "class Solution {\n    /**\n     * @param Integer $n\n     * @param Integer[]\
        \ $batteries\n     * @return Integer\n     */\n    function maxRunTime($n, $batteries)\
        \ {\n        $check = function($target_time) use ($n, $batteries) {\n      \
        \      $extra_power = 0;\n            $computers_to_power = $n;\n\n        \
        \    foreach ($batteries as $b) {\n                if ($b >= $target_time) {\n\
        \                    $computers_to_power--;\n                    $extra_power\
        \ += ($b - $target_time);\n                else {\n                    $extra_power\
        \ += $b;\n                }\n            }\n\n            return $extra_power\
        \ >= max(0, $computers_to_power) * $target_time;\n        };\n\n        $low\
        \ = 0;\n        $high = 0;\n        foreach ($batteries as $b) {\n         \
        \   $high += $b;\n        }\n        $high = intdiv($high, $n);\n\n        $ans\
        \ = 0;\n\n        while ($low <= $high) {\n            $mid = $low + intdiv($high\
        \ - $low, 2);\n            if ($check($mid)) {\n                $ans = $mid;\n\
        \                $low = $mid + 1;\n            } else {\n                $high\
        \ = $mid - 1;\n            }\n        }\n        return $ans;\n    }\n}"
      swift: "class Solution {\n    func maxRunTime(_ n: Int, _ batteries: [Int]) ->\
        \ Int {\n        func check(_ targetTime: Int) -> Bool {\n            var extraPower:\
        \ Int = 0\n            var computersToPower: Int = n\n\n            for b in\
        \ batteries {\n                if b >= targetTime {\n                    computersToPower\
        \ -= 1\n                    extraPower += (b - targetTime)\n               \
        \ } else {\n                    extraPower += b\n                }\n       \
        \     }\n\n            return extraPower >= max(0, computersToPower) * targetTime\n\
        \        }\n\n        var low: Int = 0\n        var high: Int = batteries.reduce(0,\
        \ +) / n\n        var ans: Int = 0\n\n        while low <= high {\n        \
        \    let mid = low + (high - low) / 2\n            if check(mid) {\n       \
        \         ans = mid\n                low = mid + 1\n            } else {\n \
        \               high = mid - 1\n            }\n        }\n        return ans\n\
        \    }\n}"
      kotlin: "class Solution {\n    fun maxRunTime(n: Int, batteries: IntArray): Long\
        \ {\n        fun check(targetTime: Long, n: Int, batteries: IntArray): Boolean\
        \ {\n            var extraPower: Long = 0L\n            var computersToPower:\
        \ Long = n.toLong()\n\n            for (b in batteries) {\n                val\
        \ batteryCapacity = b.toLong()\n                if (batteryCapacity >= targetTime)\
        \ {\n                    computersToPower--\n                    extraPower\
        \ += (batteryCapacity - targetTime)\n                } else {\n            \
        \        extraPower += batteryCapacity\n                }\n            }\n\n\
        \            return extraPower >= Math.max(0L, computersToPower) * targetTime\n\
        \        }\n\n        var low: Long = 0L\n        var high: Long = 0L\n    \
        \    for (b in batteries) {\n            high += b.toLong()\n        }\n   \
        \     high /= n.toLong()\n\n        var ans: Long = 0L\n\n        while (low\
        \ <= high) {\n            val mid = low + (high - low) / 2\n            if (check(mid,\
        \ n, batteries)) {\n                ans = mid\n                low = mid + 1\n\
        \            } else {\n                high = mid - 1\n            }\n     \
        \   }\n        return ans\n    }\n}"
      dart: "class Solution {\n  bool _check(int targetTime, int n, List<int> batteries)\
        \ {\n    int extraPower = 0;\n    int computersToPower = n;\n\n    for (int\
        \ b in batteries) {\n      if (b >= targetTime) {\n        computersToPower--;\n\
        \        extraPower += (b - targetTime);\n      } else {\n        extraPower\
        \ += b;\n      }\n    }\n\n    return extraPower >= (computersToPower > 0 ?\
        \ computersToPower : 0) * targetTime;\n  }\n\n  int maxRunTime(int n, List<int>\
        \ batteries) {\n    int low = 0;\n    int high = 0;\n    for (int b in batteries)\
        \ {\n      high += b;\n    }\n    high ~/= n; // Integer division\n\n    int\
        \ ans = 0;\n\n    while (low <= high) {\n      int mid = low + (high - low)\
        \ ~/ 2;\n      if (_check(mid, n, batteries)) {\n        ans = mid;\n      \
        \  low = mid + 1;\n      } else {\n        high = mid - 1;\n      }\n    }\n\
        \    return ans;\n  }\n}"
      go: "func maxRunTime(n int, batteries []int) int64 {\n    check := func(targetTime\
        \ int64) bool {\n        var extraPower int64 = 0\n        var computersToPower\
        \ int64 = int64(n)\n\n        for _, b := range batteries {\n            batteryCapacity\
        \ := int64(b);\n            if batteryCapacity >= targetTime {\n           \
        \     computersToPower--;\n                extraPower += (batteryCapacity -\
        \ targetTime);\n            } else {\n                extraPower += batteryCapacity;\n\
        \            }\n        }\n\n        neededPower := int64(0);\n        if computersToPower\
        \ > 0 {\n            neededPower = computersToPower * targetTime;\n        }\n\
        \        return extraPower >= neededPower;\n    }\n\n    var low int64 = 0;\n\
        \    var high int64 = 0;\n    for _, b := range batteries {\n        high +=\
        \ int64(b);\n    }\n    high /= int64(n);\n\n    var ans int64 = 0;\n\n    for\
        \ low <= high {\n        mid := low + (high - low) / 2;\n        if check(mid)\
        \ {\n            ans = mid;\n            low = mid + 1;\n        } else {\n\
        \            high = mid - 1;\n        }\n    }\n    return ans;\n}"
      ruby: "class Solution\n    # @param {Integer} n\n    # @param {Integer[]} batteries\n\
        \    # @return {Integer}\n    def max_run_time(n, batteries)\n        check\
        \ = lambda target_time do\n            extra_power = 0\n            computers_to_power\
        \ = n\n\n            batteries.each do |b|\n                if b >= target_time\n\
        \                    computers_to_power -= 1\n                    extra_power\
        \ += (b - target_time)\n                else\n                    extra_power\
        \ += b\n                end\n            end\n\n            return extra_power\
        \ >= [0, computers_to_power].max * target_time\n        end\n\n        low =\
        \ 0\n        high = batteries.sum / n\n        ans = 0\n\n        while low\
        \ <= high\n            mid = low + (high - low) / 2\n            if check.call(mid)\n\
        \                ans = mid\n                low = mid + 1\n            else\n\
        \                high = mid - 1\n            end\n        end\n        return\
        \ ans\n    end\nend"
      scala: "object Solution {\n    def maxRunTime(n: Int, batteries: Array[Int]):\
        \ Long = {\n        def check(targetTime: Long): Boolean = {\n            var\
        \ extraPower: Long = 0L\n            var computersToPower: Long = n.toLong\n\
        \n            for (b <- batteries) {\n                val batteryCapacity =\
        \ b.toLong\n                if (batteryCapacity >= targetTime) {\n         \
        \           computersToPower -= 1\n                    extraPower += (batteryCapacity\
        \ - targetTime)\n                } else {\n                    extraPower +=\
        \ batteryCapacity\n                }\n            }\n\n            extraPower\
        \ >= Math.max(0L, computersToPower) * targetTime\n        }\n\n        var low:\
        \ Long = 0L\n        var high: Long = batteries.map(_.toLong).sum / n.toLong\n\
        \        var ans: Long = 0L\n\n        while (low <= high) {\n            val\
        \ mid = low + (high - low) / 2\n            if (check(mid)) {\n            \
        \    ans = mid\n                low = mid + 1\n            } else {\n      \
        \          high = mid - 1\n            }\n        }\n        ans\n    }\n}"
      rust: "impl Solution {\n    pub fn max_run_time(n: i32, batteries: Vec<i32>) ->\
        \ i64 {\n        let check = |target_time: i64| -> bool {\n            let mut\
        \ extra_power: i64 = 0;\n            let mut computers_to_power: i64 = n as\
        \ i64;\n\n            for &b_val in batteries.iter() {\n                let\
        \ b = b_val as i64;\n                if b >= target_time {\n               \
        \     computers_to_power -= 1;\n                    extra_power += (b - target_time);\n\
        \                } else {\n                    extra_power += b;\n         \
        \       }\n            }\n\n            extra_power >= computers_to_power.max(0)\
        \ * target_time\n        };\n\n        let mut low: i64 = 0;\n        let mut\
        \ high: i64 = batteries.iter().map(|&b| b as i64).sum::<i64>() / n as i64;\n\
        \        let mut ans: i64 = 0;\n\n        while low <= high {\n            let\
        \ mid = low + (high - low) / 2;\n            if check(mid) {\n             \
        \   ans = mid;\n                low = mid + 1;\n            } else {\n     \
        \           high = mid - 1;\n            }\n        }\n        ans\n    }\n}"
      racket: "#lang racket\n\n(define (max-run-time n batteries)\n  (define (check\
        \ target-time)\n    (let loop ((bs batteries)\n               (extra-power 0)\n\
        \               (computers-to-power n))\n      (if (null? bs)\n          (>=\
        \ extra-power (* (max 0 computers-to-power) target-time))\n          (let ((b\
        \ (car bs)))\n            (if (>= b target-time)\n                (loop (cdr\
        \ bs)\n                      (+ extra-power (- b target-time))\n           \
        \           (- computers-to-power 1))\n                (loop (cdr bs)\n    \
        \                  (+ extra-power b)\n                      computers-to-power))))))\n\
        \n  (let* ((low 0)\n         (high (quotient (apply + batteries) n)))\n    (let\
        \ loop ((l low) (h high) (ans 0))\n      (if (> l h)\n          ans\n      \
        \    (let ((mid (+ l (quotient (- h l) 2))))\n            (if (check mid)\n\
        \                (loop (+ mid 1) h mid)\n                (loop l (- mid 1) ans)))))))"
      erlang: "-module(solution).\n-export([max_run_time/2]).\n\nmax_run_time(N, Batteries)\
        \ ->\n    Check = fun(TargetTime) ->\n        {ExtraPower, ComputersToPower}\
        \ = lists:foldl(\n            fun(B, {AccExtraPower, AccComputersToPower}) ->\n\
        \                if B >= TargetTime ->\n                    {AccExtraPower +\
        \ (B - TargetTime), AccComputersToPower - 1};\n                true ->\n   \
        \                 {AccExtraPower + B, AccComputersToPower}\n               \
        \ end\n            end,\n            {0, N},\n            Batteries\n      \
        \  ),\n        ExtraPower >= max(0, ComputersToPower) * TargetTime\n    end,\n\
        \n    Low = 0,\n    High = lists:sum(Batteries) div N,\n\n    binary_search(Low,\
        \ High, 0, Check).\n\n\nbinary_search(Low, High, Ans, Check) when Low =< High\
        \ ->\n    Mid = Low + (High - Low) div 2,\n    if Check(Mid) ->\n        binary_search(Mid\
        \ + 1, High, Mid, Check);\n    true ->\n        binary_search(Low, Mid - 1,\
        \ Ans, Check)\n    end;\nbinary_search(_, _, Ans, _) ->\n    Ans."
      elixir: "defmodule Solution do\n  @spec max_run_time(n :: integer, batteries ::\
        \ [integer]) :: integer\n  def max_run_time(n, batteries) do\n    check = fn\
        \ target_time ->\n      {extra_power, computers_to_power} = Enum.reduce(batteries,\
        \ {0, n}, fn b, {acc_extra_power, acc_computers_to_power} ->\n        if b >=\
        \ target_time do\n          {acc_extra_power + (b - target_time), acc_computers_to_power\
        \ - 1}\n        else\n          {acc_extra_power + b, acc_computers_to_power}\n\
        \        end\n      end)\n      extra_power >= max(0, computers_to_power) *\
        \ target_time\n    end\n\n    low = 0\n    high = Enum.sum(batteries) |> div(n)\n\
        \    ans = 0\n\n    binary_search(low, high, ans, check)\n  end\n\n  defp binary_search(low,\
        \ high, ans, check) when low <= high do\n    mid = low + div(high - low, 2)\n\
        \    if check.(mid) do\n      binary_search(mid + 1, high, mid, check)\n   \
        \ else\n      binary_search(low, mid - 1, ans, check)\n    end\n  end\n  defp\
        \ binary_search(_low, _high, ans, _check), do: ans\nend"
    approach: 'The problem asks for the maximum time ''T'' that ''n'' computers can
      run simultaneously. This exhibits a monotonic property: if ''T'' minutes are achievable,
      any time ''T'' < ''T'' is also achievable. This makes binary search an efficient
      approach. We binary search on the possible running time ''T''. The lower bound
      for ''T'' is 0, and a safe upper bound is the total sum of all battery capacities
      divided by ''n'', as this represents the average power available per computer
      if all energy could be perfectly distributed without time constraints on individual
      batteries.


      The core of the binary search is a `check(target_time)` function, which determines
      if it''s possible to run all ''n'' computers simultaneously for `target_time`
      minutes. For each battery `b` in the `batteries` array: if `b` is greater than
      or equal to `target_time`, this battery can fully power one computer for `target_time`
      minutes. We ''assign'' it to a computer, decrementing the count of computers still
      needing full power, and add the excess capacity (`b - target_time`) to a general
      pool of `extra_power`. If `b` is less than `target_time`, this battery cannot
      fully power a computer alone, so its entire capacity `b` is added to the `extra_power`
      pool. After processing all batteries, if the accumulated `extra_power` is sufficient
      to cover the remaining `computers_to_power` (i.e., `extra_power >= max(0, computers_to_power)
      * target_time`), then `target_time` is achievable.'
    time_complexity: The time complexity is dominated by the binary search and the `check`
      function. The binary search performs `log(high - low)` iterations. The `high`
      value can be up to `sum(batteries) / n`, which is approximately `10^14` (since
      `batteries.length` is `10^5` and `batteries[i]` is `10^9`, `sum(batteries)` can
      be `10^14`). Thus, `log(10^14)` is roughly 47 iterations. Inside each iteration,
      the `check` function iterates through all `m` batteries, taking `O(m)` time. Therefore,
      the total time complexity is `O(m * log(sum(batteries) / n))`, where `m` is the
      number of batteries.
    space_complexity: The space complexity is `O(1)` auxiliary space. The `check` function
      uses a few constant variables. The input `batteries` array is considered part
      of the input and not counted towards auxiliary space. If the input array needs
      to be copied or sorted, it would be `O(m)`, but in this solution, it's processed
      in-place.
    elapsed_time: 90.32353615760803
    model: gemini-2.5-flash
    generated_at: '2025-12-01 01:17:44 '
  - solutions:
      cpp: "class Solution {\npublic:\n    long long maxRunTime(int n, vector<int>&\
        \ batteries) {\n        long long sum = 0;\n        for (int battery : batteries)\
        \ sum += battery;\n        long long left = 0, right = sum / n;\n        while\
        \ (left < right) {\n            long long mid = left + (right - left + 1) /\
        \ 2;\n            if (canRun(batteries, n, mid)) left = mid;\n            else\
        \ right = mid - 1;\n        }\n        return left;\n    }\n\n    bool canRun(vector<int>&\
        \ batteries, int n, long long time) {\n        sort(batteries.begin(), batteries.end(),\
        \ greater<int>());\n        priority_queue<int> pq;\n        for (int i = 0;\
        \ i < n; i++) pq.push(batteries[i]);\n        for (int i = n; i < batteries.size();\
        \ i++) {\n            int top = pq.top(); pq.pop();\n            if (top + batteries[i]\
        \ < time) return false;\n            pq.push(batteries[i]);\n        }\n   \
        \     return true;\n    }\n};"
      java: "class Solution {\n    public long maxRunTime(int n, int[] batteries) {\n\
        \        long sum = 0;\n        for (int battery : batteries) sum += battery;\n\
        \        long left = 0, right = sum / n;\n        while (left < right) {\n \
        \           long mid = left + (right - left + 1) / 2;\n            if (canRun(batteries,\
        \ n, mid)) left = mid;\n            else right = mid - 1;\n        }\n     \
        \   return left;\n    }\n\n    public boolean canRun(int[] batteries, int n,\
        \ long time) {\n        Arrays.sort(batteries);\n        PriorityQueue<Integer>\
        \ pq = new PriorityQueue<>((a, b) -> b - a);\n        for (int i = 0; i < n;\
        \ i++) pq.offer(batteries[i]);\n        for (int i = n; i < batteries.length;\
        \ i++) {\n            int top = pq.poll();\n            if (top + batteries[i]\
        \ < time) return false;\n            pq.offer(batteries[i]);\n        }\n  \
        \      return true;\n    }\n};"
      python: "class Solution:\n    def maxRunTime(self, n: int, batteries: List[int])\
        \ -> int:\n        sum_batteries = sum(batteries)\n        left, right = 0,\
        \ sum_batteries // n\n        while left < right:\n            mid = left +\
        \ (right - left + 1) // 2\n            if self.canRun(batteries, n, mid):\n\
        \                left = mid\n            else:\n                right = mid\
        \ - 1\n        return left\n\n    def canRun(self, batteries: List[int], n:\
        \ int, time: int) -> bool:\n        batteries.sort(reverse=True)\n        pq\
        \ = []\n        for i in range(n):\n            pq.append(batteries[i])\n  \
        \      for i in range(n, len(batteries)):\n            pq.sort(reverse=True)\n\
        \            top = pq.pop(0)\n            if top + batteries[i] < time:\n  \
        \              return False\n            pq.append(batteries[i])\n        return\
        \ True"
      python3: "class Solution:\n    def maxRunTime(self, n: int, batteries: List[int])\
        \ -> int:\n        sum_batteries = sum(batteries)\n        left, right = 0,\
        \ sum_batteries // n\n        while left < right:\n            mid = left +\
        \ (right - left + 1) // 2\n            if self.canRun(batteries, n, mid):\n\
        \                left = mid\n            else:\n                right = mid\
        \ - 1\n        return left\n\n    def canRun(self, batteries: List[int], n:\
        \ int, time: int) -> bool:\n        batteries.sort(reverse=True)\n        pq\
        \ = []\n        for i in range(n):\n            pq.append(batteries[i])\n  \
        \      for i in range(n, len(batteries)):\n            pq.sort(reverse=True)\n\
        \            top = pq.pop(0)\n            if top + batteries[i] < time:\n  \
        \              return False\n            pq.append(batteries[i])\n        return\
        \ True"
      c: "typedef struct {\n    int val;\n    struct Node* next;\n} Node;\n\nNode* newNode(int\
        \ val) {\n    Node* node = (Node*)malloc(sizeof(Node));\n    node->val = val;\n\
        \    node->next = NULL;\n    return node;\n}\n\nvoid push(Node** head, int val)\
        \ {\n    Node* node = newNode(val);\n    node->next = *head;\n    *head = node;\n\
        }\n\nint pop(Node** head) {\n    int val = (*head)->val;\n    Node* temp = *head;\n\
        \    *head = (*head)->next;\n    free(temp);\n    return val;\n}\n\nint maxRunTime(int\
        \ n, int* batteries, int batteriesSize) {\n    long long sum = 0;\n    for (int\
        \ i = 0; i < batteriesSize; i++) sum += batteries[i];\n    long long left =\
        \ 0, right = sum / n;\n    while (left < right) {\n        long long mid = left\
        \ + (right - left + 1) / 2;\n        if (canRun(batteries, batteriesSize, n,\
        \ mid)) left = mid;\n        else right = mid - 1;\n    }\n    return left;\n\
        }\n\nint canRun(int* batteries, int batteriesSize, int n, long long time) {\n\
        \    int* sortedBatteries = (int*)malloc(batteriesSize * sizeof(int));\n   \
        \ for (int i = 0; i < batteriesSize; i++) sortedBatteries[i] = batteries[i];\n\
        \    qsort(sortedBatteries, batteriesSize, sizeof(int), compare);\n    Node*\
        \ head = NULL;\n    for (int i = 0; i < n; i++) push(&head, sortedBatteries[i]);\n\
        \    for (int i = n; i < batteriesSize; i++) {\n        int top = pop(&head);\n\
        \        if (top + sortedBatteries[i] < time) return 0;\n        push(&head,\
        \ sortedBatteries[i]);\n    }\n    return 1;\n}\n\nint compare(const void* a,\
        \ const void* b) {\n    return (*(int*)b - *(int*)a);\n}"
      csharp: "public class Solution {\n    public long MaxRunTime(int n, int[] batteries)\
        \ {\n        long sum = 0;\n        foreach (int battery in batteries) sum +=\
        \ battery;\n        long left = 0, right = sum / n;\n        while (left < right)\
        \ {\n            long mid = left + (right - left + 1) / 2;\n            if (CanRun(batteries,\
        \ n, mid)) left = mid;\n            else right = mid - 1;\n        }\n     \
        \   return left;\n    }\n\n    public bool CanRun(int[] batteries, int n, long\
        \ time) {\n        Array.Sort(batteries);\n        Array.Reverse(batteries);\n\
        \        var pq = new List<int>();\n        for (int i = 0; i < n; i++) pq.Add(batteries[i]);\n\
        \        for (int i = n; i < batteries.Length; i++) {\n            pq.Sort((a,\
        \ b) => b.CompareTo(a));\n            int top = pq[0];\n            pq.RemoveAt(0);\n\
        \            if (top + batteries[i] < time) return false;\n            pq.Add(batteries[i]);\n\
        \        }\n        return true;\n    }\n}"
      javascript: "var maxRunTime = function(n, batteries) {\n    let sum = 0;\n   \
        \ for (let battery of batteries) sum += battery;\n    let left = 0, right =\
        \ Math.floor(sum / n);\n    while (left < right) {\n        let mid = left +\
        \ Math.floor((right - left + 1) / 2);\n        if (canRun(batteries, n, mid))\
        \ left = mid;\n        else right = mid - 1;\n    }\n    return left;\n};\n\n\
        var canRun = function(batteries, n, time) {\n    batteries.sort((a, b) => b\
        \ - a);\n    let pq = [];\n    for (let i = 0; i < n; i++) pq.push(batteries[i]);\n\
        \    for (let i = n; i < batteries.length; i++) {\n        pq.sort((a, b) =>\
        \ b - a);\n        let top = pq.shift();\n        if (top + batteries[i] < time)\
        \ return false;\n        pq.push(batteries[i]);\n    }\n    return true;\n};"
      typescript: "function maxRunTime(n: number, batteries: number[]): number {\n \
        \   let sum = 0;\n    for (let battery of batteries) sum += battery;\n    let\
        \ left = 0, right = Math.floor(sum / n);\n    while (left < right) {\n     \
        \   let mid = left + Math.floor((right - left + 1) / 2);\n        if (canRun(batteries,\
        \ n, mid)) left = mid;\n        else right = mid - 1;\n    }\n    return left;\n\
        }\n\nfunction canRun(batteries: number[], n: number, time: number): boolean\
        \ {\n    batteries.sort((a, b) => b - a);\n    let pq: number[] = [];\n    for\
        \ (let i = 0; i < n; i++) pq.push(batteries[i]);\n    for (let i = n; i < batteries.length;\
        \ i++) {\n        pq.sort((a, b) => b - a);\n        let top = pq.shift() as\
        \ number;\n        if (top + batteries[i] < time) return false;\n        pq.push(batteries[i]);\n\
        \    }\n    return true;\n};"
      php: "class Solution {\n    function maxRunTime($n, $batteries) {\n        $sum\
        \ = 0;\n        foreach ($batteries as $battery) $sum += $battery;\n       \
        \ $left = 0; $right = floor($sum / $n);\n        while ($left < $right) {\n\
        \            $mid = $left + floor(($right - $left + 1) / 2);\n            if\
        \ ($this->canRun($batteries, $n, $mid)) $left = $mid;\n            else $right\
        \ = $mid - 1;\n        }\n        return $left;\n    }\n\n    function canRun($batteries,\
        \ $n, $time) {\n        rsort($batteries);\n        $pq = array_slice($batteries,\
        \ 0, $n);\n        for ($i = $n; $i < count($batteries); $i++) {\n         \
        \   rsort($pq);\n            $top = array_shift($pq);\n            if ($top\
        \ + $batteries[$i] < $time) return false;\n            $pq[] = $batteries[$i];\n\
        \        }\n        return true;\n    }\n};"
      swift: "class Solution {\n    func maxRunTime(_ n: Int, _ batteries: [Int]) ->\
        \ Int {\n        var sum = 0\n        for battery in batteries {\n         \
        \   sum += battery\n        }\n        var left = 0\n        var right = sum\
        \ / n\n        while left < right {\n            let mid = left + (right - left\
        \ + 1) / 2\n            if canRun(batteries, n, mid) {\n                left\
        \ = mid\n            } else {\n                right = mid - 1\n           \
        \ }\n        }\n        return left\n    }\n\n    func canRun(_ batteries: [Int],\
        \ _ n: Int, _ time: Int) -> Bool {\n        var batteries = batteries\n    \
        \    batteries.sort { $0 > $1 }\n        var pq: [Int] = []\n        for i in\
        \ 0..<n {\n            pq.append(batteries[i])\n        }\n        for i in\
        \ n..<batteries.count {\n            pq.sort { $0 > $1 }\n            let top\
        \ = pq.removeFirst()\n            if top + batteries[i] < time {\n         \
        \       return false\n            }\n            pq.append(batteries[i])\n \
        \       }\n        return true\n    }\n};"
      kotlin: "class Solution {\n    fun maxRunTime(n: Int, batteries: IntArray): Int\
        \ {\n        var sum = 0\n        for (battery in batteries) sum += battery\n\
        \        var left = 0\n        var right = sum / n\n        while (left < right)\
        \ {\n            val mid = left + (right - left + 1) / 2\n            if (canRun(batteries,\
        \ n, mid)) left = mid\n            else right = mid - 1\n        }\n       \
        \ return left\n    }\n\n    fun canRun(batteries: IntArray, n: Int, time: Int):\
        \ Boolean {\n        batteries.sortDescending()\n        val pq = mutableListOf<Int>()\n\
        \        for (i in 0 until n) pq.add(batteries[i])\n        for (i in n until\
        \ batteries.size) {\n            pq.sortDescending()\n            val top =\
        \ pq.removeAt(0)\n            if (top + batteries[i] < time) return false\n\
        \            pq.add(batteries[i])\n        }\n        return true\n    }\n};"
      dart: "class Solution {\n    int maxRunTime(int n, List<int> batteries) {\n  \
        \      int sum = 0;\n        for (int battery in batteries) sum += battery;\n\
        \        int left = 0, right = sum ~/ n;\n        while (left < right) {\n \
        \           int mid = left + (right - left + 1) ~/ 2;\n            if (canRun(batteries,\
        \ n, mid)) left = mid;\n            else right = mid - 1;\n        }\n     \
        \   return left;\n    }\n\n    bool canRun(List<int> batteries, int n, int time)\
        \ {\n        batteries.sort((a, b) => b - a);\n        List<int> pq = [];\n\
        \        for (int i = 0; i < n; i++) pq.add(batteries[i]);\n        for (int\
        \ i = n; i < batteries.length; i++) {\n            pq.sort((a, b) => b - a);\n\
        \            int top = pq.removeAt(0);\n            if (top + batteries[i] <\
        \ time) return false;\n            pq.add(batteries[i]);\n        }\n      \
        \  return true;\n    }\n};"
      go: "package main\n\nimport (\n    \"fmt\"\n    \"sort\"\n)\n\nfunc maxRunTime(n\
        \ int, batteries []int) int {\n    sum := 0\n    for _, battery := range batteries\
        \ {\n        sum += battery\n    }\n    left, right := 0, sum/n\n    for left\
        \ < right {\n        mid := left + (right-left+1)/2\n        if canRun(batteries,\
        \ n, mid) {\n            left = mid\n        } else {\n            right = mid\
        \ - 1\n        }\n    }\n    return left\n}\n\nfunc canRun(batteries []int,\
        \ n, time int) bool {\n    sort.Sort(sort.Reverse(sort.IntSlice(batteries)))\n\
        \    pq := make([]int, 0)\n    for i := 0; i < n; i++ {\n        pq = append(pq,\
        \ batteries[i])\n    }\n    for i := n; i < len(batteries); i++ {\n        sort.Sort(sort.Reverse(sort.IntSlice(pq)))\n\
        \        top := pq[0]\n        pq = pq[1:]\n        if top+batteries[i] < time\
        \ {\n            return false\n        }\n        pq = append(pq, batteries[i])\n\
        \    }\n    return true\n}"
      ruby: "class Solution\n    def max_run_time(n, batteries)\n        sum = 0\n \
        \       batteries.each { |battery| sum += battery }\n        left, right = 0,\
        \ sum / n\n        while left < right\n            mid = left + (right - left\
        \ + 1) / 2\n            if can_run(batteries, n, mid)\n                left\
        \ = mid\n            else\n                right = mid - 1\n            end\n\
        \        end\n        left\n    end\n\n    def can_run(batteries, n, time)\n\
        \        batteries.sort!.reverse!\n        pq = []\n        n.times { |i| pq\
        \ << batteries[i] }\n        (n...batteries.size).each do |i|\n            pq.sort!.reverse!\n\
        \            top = pq.shift\n            if top + batteries[i] < time\n    \
        \            return false\n            end\n            pq << batteries[i]\n\
        \        end\n        true\n    end\nend"
      scala: "object Solution {\n    def maxRunTime(n: Int, batteries: Array[Int]):\
        \ Int = {\n        val sum = batteries.sum\n        var left = 0\n        var\
        \ right = sum / n\n        while (left < right) {\n            val mid = left\
        \ + (right - left + 1) / 2\n            if (canRun(batteries, n, mid)) left\
        \ = mid\n            else right = mid - 1\n        }\n        left\n    }\n\n\
        \    def canRun(batteries: Array[Int], n: Int, time: Int): Boolean = {\n   \
        \     val sortedBatteries = batteries.sorted.reverse\n        val pq = scala.collection.mutable.PriorityQueue[Int]()\n\
        \        for (i <- 0 until n) pq.enqueue(sortedBatteries(i))\n        for (i\
        \ <- n until sortedBatteries.length) {\n            val top = pq.dequeue()\n\
        \            if (top + sortedBatteries(i) < time) return false\n           \
        \ pq.enqueue(sortedBatteries(i))\n        }\n        true\n    }\n};"
      rust: "struct Solution;\n\nimpl Solution {\n    pub fn max_run_time(n: i32, batteries:\
        \ Vec<i32>) -> i32 {\n        let sum: i64 = batteries.iter().sum::<i32>() as\
        \ i64;\n        let mut left = 0;\n        let mut right = sum / n as i64;\n\
        \        while left < right {\n            let mid = left + (right - left +\
        \ 1) / 2;\n            if Solution::can_run(&batteries, n, mid) {\n        \
        \        left = mid;\n            } else {\n                right = mid - 1;\n\
        \            }\n        }\n        left as i32\n    }\n\n    pub fn can_run(batteries:\
        \ &Vec<i32>, n: i32, time: i64) -> bool {\n        let mut batteries = batteries.clone();\n\
        \        batteries.sort_unstable_by(|a, b| b.cmp(a));\n        let mut pq: Vec<i32>\
        \ = batteries.iter().take(n as usize).cloned().collect();\n        for i in\
        \ n as usize..batteries.len() {\n            pq.sort_unstable_by(|a, b| b.cmp(a));\n\
        \            let top = pq.remove(0);\n            if top as i64 + batteries[i]\
        \ as i64 < time {\n                return false;\n            }\n          \
        \  pq.push(batteries[i]);\n        }\n        true\n    }\n};"
      racket: "define (max-run-time n batteries)\n    (let loop ((left 0) (right (quotient\
        \ (apply + batteries) n)))\n        (if (< left right)\n            (let ((mid\
        \ (quotient (+ left right 1) 2)))\n                (if (can-run batteries n\
        \ mid)\n                    (loop mid right)\n                    (loop left\
        \ (- mid 1))))\n            left))\n\n(define (can-run batteries n time)\n \
        \   (let ((batteries (sort batteries >)))\n        (let loop ((pq (take batteries\
        \ n)) (i n))\n            (if (< i (length batteries))\n                (let\
        \ ((top (car pq)))\n                    (if (< (+ top (list-ref batteries i))\
        \ time)\n                        #f\n                        (loop (append (cdr\
        \ pq) (list (list-ref batteries i))) (+ i 1))))\n                #t))))"
      erlang: "max_run_time(N, Batteries) ->\n    Left = 0,\n    Right = lists:sum(Batteries)\
        \ div N,\n    loop(Left, Right, Batteries, N).\n\nloop(Left, Right, Batteries,\
        \ N) when Left < Right ->\n    Mid = Left + (Right - Left + 1) div 2,\n    case\
        \ can_run(Batteries, N, Mid) of\n        true -> loop(Mid, Right, Batteries,\
        \ N);\n        false -> loop(Left, Mid - 1, Batteries, N)\n    end;\nloop(Left,\
        \ _, _, _) -> Left.\n\ncan_run(Batteries, N, Time) ->\n    SortedBatteries =\
        \ lists:sort(fun(A, B) -> B =< A end, Batteries),\n    PQ = lists:sublist(SortedBatteries,\
        \ N),\n    can_run_loop(PQ, lists:nthtail(N, SortedBatteries), Time).\n\ncan_run_loop(PQ,\
        \ [], _) -> true;\n\ncan_run_loop(PQ, [H | T], Time) ->\n    [Top | Rest] =\
        \ lists:sort(fun(A, B) -> B =< A end, PQ),\n    case Top + H < Time of\n   \
        \     true -> false;\n        false -> can_run_loop(Rest ++ [H], T, Time)\n\
        \    end."
      elixir: "defmodule Solution do\n    def max_run_time(n, batteries) do\n      \
        \  sum = Enum.sum(batteries)\n        left = 0\n        right = div(sum, n)\n\
        \        loop(left, right, batteries, n)\n    end\n\n    defp loop(left, right,\
        \ batteries, n) when left < right do\n        mid = left + div(right - left\
        \ + 1, 2)\n        case can_run(batteries, n, mid) do\n            true -> loop(mid,\
        \ right, batteries, n)\n            false -> loop(left, mid - 1, batteries,\
        \ n)\n        end\n    end\n\n    defp loop(left, _, _, _) do\n        left\n\
        \    end\n\n    defp can_run(batteries, n, time) do\n        sorted_batteries\
        \ = Enum.sort(batteries, &(&1 >= &2))\n        pq = Enum.take(sorted_batteries,\
        \ n)\n        can_run_loop(pq, Enum.drop(sorted_batteries, n), time)\n    end\n\
        \n    defp can_run_loop(pq, [], _) do\n        true\n    end\n\n    defp can_run_loop(pq,\
        \ [h | t], time) do\n        [top | rest] = Enum.sort(pq, &(&1 >= &2))\n   \
        \     case top + h < time do\n            true -> can_run_loop(rest ++ [h],\
        \ t, time)\n            false -> false\n        end\n    end\nend"
    approach: The problem can be solved using a binary search approach. We need to find
      the maximum running time for all n computers. We can start by finding the minimum
      and maximum possible running times. The minimum running time is 0, and the maximum
      running time is the sum of all battery times divided by n. We can then perform
      a binary search between these two values to find the maximum running time. For
      each mid value, we can check if it is possible to run all n computers for that
      amount of time by using a greedy approach to assign batteries to computers.
    time_complexity: The time complexity of this solution is O(m log m log (sum of batteries
      / n)), where m is the number of batteries and n is the number of computers. This
      is because we are performing a binary search over the possible running times,
      and for each mid value, we are sorting the batteries and assigning them to computers.
    space_complexity: The space complexity of this solution is O(m), where m is the
      number of batteries. This is because we need to store the batteries and the computers,
      and we are using a greedy approach to assign batteries to computers, which requires
      a small amount of extra space.
    elapsed_time: 12.738838911056519
    model: llama-3.3-70b-versatile
    generated_at: '2025-12-01 01:17:57 '
---

## Problem #2141: Maximum Running Time of N Computers

**Difficulty:** Hard

**Topics:** Array, Binary Search, Greedy, Sorting

## Problem Description

<p>You have <code>n</code> computers. You are given the integer <code>n</code> and a <strong>0-indexed</strong> integer array <code>batteries</code> where the <code>i<sup>th</sup></code> battery can <strong>run</strong> a computer for <code>batteries[i]</code> minutes. You are interested in running <strong>all</strong> <code>n</code> computers <strong>simultaneously</strong> using the given batteries.</p>

<p>Initially, you can insert <strong>at most one battery</strong> into each computer. After that and at any integer time moment, you can remove a battery from a computer and insert another battery <strong>any number of times</strong>. The inserted battery can be a totally new battery or a battery from another computer. You may assume that the removing and inserting processes take no time.</p>

<p>Note that the batteries cannot be recharged.</p>

<p>Return <em>the <strong>maximum</strong> number of minutes you can run all the </em><code>n</code><em> computers simultaneously.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/01/06/example1-fit.png" style="width: 762px; height: 150px;" />
<pre>
<strong>Input:</strong> n = 2, batteries = [3,3,3]
<strong>Output:</strong> 4
<strong>Explanation:</strong> 
Initially, insert battery 0 into the first computer and battery 1 into the second computer.
After two minutes, remove battery 1 from the second computer and insert battery 2 instead. Note that battery 1 can still run for one minute.
At the end of the third minute, battery 0 is drained, and you need to remove it from the first computer and insert battery 1 instead.
By the end of the fourth minute, battery 1 is also drained, and the first computer is no longer running.
We can run the two computers simultaneously for at most 4 minutes, so we return 4.

</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/01/06/example2.png" style="width: 629px; height: 150px;" />
<pre>
<strong>Input:</strong> n = 2, batteries = [1,1,1,1]
<strong>Output:</strong> 2
<strong>Explanation:</strong> 
Initially, insert battery 0 into the first computer and battery 2 into the second computer. 
After one minute, battery 0 and battery 2 are drained so you need to remove them and insert battery 1 into the first computer and battery 3 into the second computer. 
After another minute, battery 1 and battery 3 are also drained so the first and second computers are no longer running.
We can run the two computers simultaneously for at most 2 minutes, so we return 2.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= batteries.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= batteries[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## Hints

1. For a given running time, can you determine if it is possible to run all n computers simultaneously?

2. Try to use Binary Search to find the maximal running time

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-12-01 01:17:44 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks for the maximum time 'T' that 'n' computers can run simultaneously. This exhibits a monotonic property: if 'T' minutes are achievable, any time 'T' < 'T' is also achievable. This makes binary search an efficient approach. We binary search on the possible running time 'T'. The lower bound for 'T' is 0, and a safe upper bound is the total sum of all battery capacities divided by 'n', as this represents the average power available per computer if all energy could be perfectly distributed without time constraints on individual batteries.

The core of the binary search is a `check(target_time)` function, which determines if it's possible to run all 'n' computers simultaneously for `target_time` minutes. For each battery `b` in the `batteries` array: if `b` is greater than or equal to `target_time`, this battery can fully power one computer for `target_time` minutes. We 'assign' it to a computer, decrementing the count of computers still needing full power, and add the excess capacity (`b - target_time`) to a general pool of `extra_power`. If `b` is less than `target_time`, this battery cannot fully power a computer alone, so its entire capacity `b` is added to the `extra_power` pool. After processing all batteries, if the accumulated `extra_power` is sufficient to cover the remaining `computers_to_power` (i.e., `extra_power >= max(0, computers_to_power) * target_time`), then `target_time` is achievable.

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
    bool check(long long target_time, int n, const std::vector<int>& batteries) {
        long long extra_power = 0;
        long long computers_to_power = n;

        for (int b : batteries) {
            if (b >= target_time) {
                computers_to_power--;
                extra_power += (b - target_time);
            } else {
                extra_power += b;
            }
        }

        // If computers_to_power is negative, it means we have more than enough strong batteries
        // to cover all 'n' computers individually for 'target_time' minutes.
        // In this case, no additional power is needed from the 'extra_power' pool for these computers.
        return extra_power >= std::max(0LL, computers_to_power) * target_time;
    }

    long long maxRunTime(int n, std::vector<int>& batteries) {
        long long low = 0;
        long long high = 0;
        for (int b : batteries) {
            high += b;
        }
        high /= n;

        long long ans = 0;

        while (low <= high) {
            long long mid = low + (high - low) / 2;
            if (check(mid, n, batteries)) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
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
    public boolean check(long target_time, int n, int[] batteries) {
        long extra_power = 0;
        long computers_to_power = n;

        for (int b : batteries) {
            if (b >= target_time) {
                computers_to_power--;
                extra_power += (b - target_time);
            } else {
                extra_power += b;
            }
        }

        return extra_power >= Math.max(0L, computers_to_power) * target_time;
    }

    public long maxRunTime(int n, int[] batteries) {
        long low = 0;
        long high = 0;
        for (int b : batteries) {
            high += b;
        }
        high /= n;

        long ans = 0;

        while (low <= high) {
            long mid = low + (high - low) / 2;
            if (check(mid, n, batteries)) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
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
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:

        def check(target_time: int) -> bool:
            extra_power = 0
            computers_to_power = n

            for b in batteries:
                if b >= target_time:
                    computers_to_power -= 1
                    extra_power += (b - target_time)
                else:
                    extra_power += b

            return extra_power >= max(0, computers_to_power) * target_time

        low = 0
        high = sum(batteries) // n
        ans = 0

        while low <= high:
            mid = low + (high - low) // 2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:

        def check(target_time: int) -> bool:
            extra_power = 0
            computers_to_power = n

            for b in batteries:
                if b >= target_time:
                    computers_to_power -= 1
                    extra_power += (b - target_time)
                else:
                    extra_power += b

            return extra_power >= max(0, computers_to_power) * target_time

        low = 0
        high = sum(batteries) // n
        ans = 0

        while low <= high:
            mid = low + (high - low) // 2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// Using long long for sums and time values to prevent overflow
bool check(long long target_time, int n, int* batteries, int batteriesSize) {
    long long extra_power = 0;
    long long computers_to_power = n;

    for (int i = 0; i < batteriesSize; i++) {
        long long b = batteries[i];
        if (b >= target_time) {
            computers_to_power--;
            extra_power += (b - target_time);
        } else {
            extra_power += b;
        }
    }

    long long needed_power = (computers_to_power > 0 ? computers_to_power : 0) * target_time;
    return extra_power >= needed_power;
}

long long maxRunTime(int n, int* batteries, int batteriesSize) {
    long long low = 0;
    long long high = 0;
    for (int i = 0; i < batteriesSize; i++) {
        high += batteries[i];
    }
    high /= n;

    long long ans = 0;

    while (low <= high) {
        long long mid = low + (high - low) / 2;
        if (check(mid, n, batteries, batteriesSize)) {
            ans = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
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
public class Solution {
    private bool Check(long targetTime, int n, int[] batteries) {
        long extraPower = 0;
        long computersToPower = n;

        foreach (int b in batteries) {
            if (b >= targetTime) {
                computersToPower--;
                extraPower += (b - targetTime);
            } else {
                extraPower += b;
            }
        }

        return extraPower >= Math.Max(0L, computersToPower) * targetTime;
    }

    public long MaxRunTime(int n, int[] batteries) {
        long low = 0;
        long high = 0;
        foreach (int b in batteries) {
            high += b;
        }
        high /= n;

        long ans = 0;

        while (low <= high) {
            long mid = low + (high - low) / 2;
            if (Check(mid, n, batteries)) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
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
 * @param {number} n
 * @param {number[]} batteries
 * @return {number}
 */
var maxRunTime = function(n, batteries) {
    const check = (targetTime) => {
        let extraPower = 0n; // Use BigInt for large numbers
        let computersToPower = BigInt(n);
        const targetTimeBig = BigInt(targetTime);

        for (const b of batteries) {
            const batteryCapacityBig = BigInt(b);
            if (batteryCapacityBig >= targetTimeBig) {
                computersToPower--;
                extraPower += (batteryCapacityBig - targetTimeBig);
            } else {
                extraPower += batteryCapacityBig;
            }
        }

        return extraPower >= (computersToPower > 0n ? computersToPower : 0n) * targetTimeBig;
    };

    let low = 0n;
    let high = 0n;
    for (const b of batteries) {
        high += BigInt(b);
    }
    high /= BigInt(n);

    let ans = 0n;

    while (low <= high) {
        let mid = low + (high - low) / 2n;
        if (check(Number(mid))) { // Pass Number to check function, convert back to BigInt inside if needed
            ans = mid;
            low = mid + 1n;
        } else {
            high = mid - 1n;
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
function maxRunTime(n: number, batteries: number[]): number {
    const check = (targetTime: bigint): boolean => {
        let extraPower: bigint = 0n;
        let computersToPower: bigint = BigInt(n);

        for (const b of batteries) {
            const batteryCapacityBig = BigInt(b);
            if (batteryCapacityBig >= targetTime) {
                computersToPower--;
                extraPower += (batteryCapacityBig - targetTime);
            } else {
                extraPower += batteryCapacityBig;
            }
        }

        return extraPower >= (computersToPower > 0n ? computersToPower : 0n) * targetTime;
    };

    let low: bigint = 0n;
    let high: bigint = 0n;
    for (const b of batteries) {
        high += BigInt(b);
    }
    high /= BigInt(n);

    let ans: bigint = 0n;

    while (low <= high) {
        const mid: bigint = low + (high - low) / 2n;
        if (check(mid)) {
            ans = mid;
            low = mid + 1n;
        } else {
            high = mid - 1n;
        }
    }
    return Number(ans);
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
     * @param Integer[] $batteries
     * @return Integer
     */
    function maxRunTime($n, $batteries) {
        $check = function($target_time) use ($n, $batteries) {
            $extra_power = 0;
            $computers_to_power = $n;

            foreach ($batteries as $b) {
                if ($b >= $target_time) {
                    $computers_to_power--;
                    $extra_power += ($b - $target_time);
                else {
                    $extra_power += $b;
                }
            }

            return $extra_power >= max(0, $computers_to_power) * $target_time;
        };

        $low = 0;
        $high = 0;
        foreach ($batteries as $b) {
            $high += $b;
        }
        $high = intdiv($high, $n);

        $ans = 0;

        while ($low <= $high) {
            $mid = $low + intdiv($high - $low, 2);
            if ($check($mid)) {
                $ans = $mid;
                $low = $mid + 1;
            } else {
                $high = $mid - 1;
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
    func maxRunTime(_ n: Int, _ batteries: [Int]) -> Int {
        func check(_ targetTime: Int) -> Bool {
            var extraPower: Int = 0
            var computersToPower: Int = n

            for b in batteries {
                if b >= targetTime {
                    computersToPower -= 1
                    extraPower += (b - targetTime)
                } else {
                    extraPower += b
                }
            }

            return extraPower >= max(0, computersToPower) * targetTime
        }

        var low: Int = 0
        var high: Int = batteries.reduce(0, +) / n
        var ans: Int = 0

        while low <= high {
            let mid = low + (high - low) / 2
            if check(mid) {
                ans = mid
                low = mid + 1
            } else {
                high = mid - 1
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
    fun maxRunTime(n: Int, batteries: IntArray): Long {
        fun check(targetTime: Long, n: Int, batteries: IntArray): Boolean {
            var extraPower: Long = 0L
            var computersToPower: Long = n.toLong()

            for (b in batteries) {
                val batteryCapacity = b.toLong()
                if (batteryCapacity >= targetTime) {
                    computersToPower--
                    extraPower += (batteryCapacity - targetTime)
                } else {
                    extraPower += batteryCapacity
                }
            }

            return extraPower >= Math.max(0L, computersToPower) * targetTime
        }

        var low: Long = 0L
        var high: Long = 0L
        for (b in batteries) {
            high += b.toLong()
        }
        high /= n.toLong()

        var ans: Long = 0L

        while (low <= high) {
            val mid = low + (high - low) / 2
            if (check(mid, n, batteries)) {
                ans = mid
                low = mid + 1
            } else {
                high = mid - 1
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
class Solution {
  bool _check(int targetTime, int n, List<int> batteries) {
    int extraPower = 0;
    int computersToPower = n;

    for (int b in batteries) {
      if (b >= targetTime) {
        computersToPower--;
        extraPower += (b - targetTime);
      } else {
        extraPower += b;
      }
    }

    return extraPower >= (computersToPower > 0 ? computersToPower : 0) * targetTime;
  }

  int maxRunTime(int n, List<int> batteries) {
    int low = 0;
    int high = 0;
    for (int b in batteries) {
      high += b;
    }
    high ~/= n; // Integer division

    int ans = 0;

    while (low <= high) {
      int mid = low + (high - low) ~/ 2;
      if (_check(mid, n, batteries)) {
        ans = mid;
        low = mid + 1;
      } else {
        high = mid - 1;
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
func maxRunTime(n int, batteries []int) int64 {
    check := func(targetTime int64) bool {
        var extraPower int64 = 0
        var computersToPower int64 = int64(n)

        for _, b := range batteries {
            batteryCapacity := int64(b);
            if batteryCapacity >= targetTime {
                computersToPower--;
                extraPower += (batteryCapacity - targetTime);
            } else {
                extraPower += batteryCapacity;
            }
        }

        neededPower := int64(0);
        if computersToPower > 0 {
            neededPower = computersToPower * targetTime;
        }
        return extraPower >= neededPower;
    }

    var low int64 = 0;
    var high int64 = 0;
    for _, b := range batteries {
        high += int64(b);
    }
    high /= int64(n);

    var ans int64 = 0;

    for low <= high {
        mid := low + (high - low) / 2;
        if check(mid) {
            ans = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return ans;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
class Solution
    # @param {Integer} n
    # @param {Integer[]} batteries
    # @return {Integer}
    def max_run_time(n, batteries)
        check = lambda target_time do
            extra_power = 0
            computers_to_power = n

            batteries.each do |b|
                if b >= target_time
                    computers_to_power -= 1
                    extra_power += (b - target_time)
                else
                    extra_power += b
                end
            end

            return extra_power >= [0, computers_to_power].max * target_time
        end

        low = 0
        high = batteries.sum / n
        ans = 0

        while low <= high
            mid = low + (high - low) / 2
            if check.call(mid)
                ans = mid
                low = mid + 1
            else
                high = mid - 1
            end
        end
        return ans
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def maxRunTime(n: Int, batteries: Array[Int]): Long = {
        def check(targetTime: Long): Boolean = {
            var extraPower: Long = 0L
            var computersToPower: Long = n.toLong

            for (b <- batteries) {
                val batteryCapacity = b.toLong
                if (batteryCapacity >= targetTime) {
                    computersToPower -= 1
                    extraPower += (batteryCapacity - targetTime)
                } else {
                    extraPower += batteryCapacity
                }
            }

            extraPower >= Math.max(0L, computersToPower) * targetTime
        }

        var low: Long = 0L
        var high: Long = batteries.map(_.toLong).sum / n.toLong
        var ans: Long = 0L

        while (low <= high) {
            val mid = low + (high - low) / 2
            if (check(mid)) {
                ans = mid
                low = mid + 1
            } else {
                high = mid - 1
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
    pub fn max_run_time(n: i32, batteries: Vec<i32>) -> i64 {
        let check = |target_time: i64| -> bool {
            let mut extra_power: i64 = 0;
            let mut computers_to_power: i64 = n as i64;

            for &b_val in batteries.iter() {
                let b = b_val as i64;
                if b >= target_time {
                    computers_to_power -= 1;
                    extra_power += (b - target_time);
                } else {
                    extra_power += b;
                }
            }

            extra_power >= computers_to_power.max(0) * target_time
        };

        let mut low: i64 = 0;
        let mut high: i64 = batteries.iter().map(|&b| b as i64).sum::<i64>() / n as i64;
        let mut ans: i64 = 0;

        while low <= high {
            let mid = low + (high - low) / 2;
            if check(mid) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
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
#lang racket

(define (max-run-time n batteries)
  (define (check target-time)
    (let loop ((bs batteries)
               (extra-power 0)
               (computers-to-power n))
      (if (null? bs)
          (>= extra-power (* (max 0 computers-to-power) target-time))
          (let ((b (car bs)))
            (if (>= b target-time)
                (loop (cdr bs)
                      (+ extra-power (- b target-time))
                      (- computers-to-power 1))
                (loop (cdr bs)
                      (+ extra-power b)
                      computers-to-power))))))

  (let* ((low 0)
         (high (quotient (apply + batteries) n)))
    (let loop ((l low) (h high) (ans 0))
      (if (> l h)
          ans
          (let ((mid (+ l (quotient (- h l) 2))))
            (if (check mid)
                (loop (+ mid 1) h mid)
                (loop l (- mid 1) ans)))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([max_run_time/2]).

max_run_time(N, Batteries) ->
    Check = fun(TargetTime) ->
        {ExtraPower, ComputersToPower} = lists:foldl(
            fun(B, {AccExtraPower, AccComputersToPower}) ->
                if B >= TargetTime ->
                    {AccExtraPower + (B - TargetTime), AccComputersToPower - 1};
                true ->
                    {AccExtraPower + B, AccComputersToPower}
                end
            end,
            {0, N},
            Batteries
        ),
        ExtraPower >= max(0, ComputersToPower) * TargetTime
    end,

    Low = 0,
    High = lists:sum(Batteries) div N,

    binary_search(Low, High, 0, Check).


binary_search(Low, High, Ans, Check) when Low =< High ->
    Mid = Low + (High - Low) div 2,
    if Check(Mid) ->
        binary_search(Mid + 1, High, Mid, Check);
    true ->
        binary_search(Low, Mid - 1, Ans, Check)
    end;
binary_search(_, _, Ans, _) ->
    Ans.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec max_run_time(n :: integer, batteries :: [integer]) :: integer
  def max_run_time(n, batteries) do
    check = fn target_time ->
      {extra_power, computers_to_power} = Enum.reduce(batteries, {0, n}, fn b, {acc_extra_power, acc_computers_to_power} ->
        if b >= target_time do
          {acc_extra_power + (b - target_time), acc_computers_to_power - 1}
        else
          {acc_extra_power + b, acc_computers_to_power}
        end
      end)
      extra_power >= max(0, computers_to_power) * target_time
    end

    low = 0
    high = Enum.sum(batteries) |> div(n)
    ans = 0

    binary_search(low, high, ans, check)
  end

  defp binary_search(low, high, ans, check) when low <= high do
    mid = low + div(high - low, 2)
    if check.(mid) do
      binary_search(mid + 1, high, mid, check)
    else
      binary_search(low, mid - 1, ans, check)
    end
  end
  defp binary_search(_low, _high, ans, _check), do: ans
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is dominated by the binary search and the `check` function. The binary search performs `log(high - low)` iterations. The `high` value can be up to `sum(batteries) / n`, which is approximately `10^14` (since `batteries.length` is `10^5` and `batteries[i]` is `10^9`, `sum(batteries)` can be `10^14`). Thus, `log(10^14)` is roughly 47 iterations. Inside each iteration, the `check` function iterates through all `m` batteries, taking `O(m)` time. Therefore, the total time complexity is `O(m * log(sum(batteries) / n))`, where `m` is the number of batteries.

- **Space Complexity:** The space complexity is `O(1)` auxiliary space. The `check` function uses a few constant variables. The input `batteries` array is considered part of the input and not counted towards auxiliary space. If the input array needs to be copied or sorted, it would be `O(m)`, but in this solution, it's processed in-place.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-12-01 01:17:57 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved using a binary search approach. We need to find the maximum running time for all n computers. We can start by finding the minimum and maximum possible running times. The minimum running time is 0, and the maximum running time is the sum of all battery times divided by n. We can then perform a binary search between these two values to find the maximum running time. For each mid value, we can check if it is possible to run all n computers for that amount of time by using a greedy approach to assign batteries to computers.

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
    long long maxRunTime(int n, vector<int>& batteries) {
        long long sum = 0;
        for (int battery : batteries) sum += battery;
        long long left = 0, right = sum / n;
        while (left < right) {
            long long mid = left + (right - left + 1) / 2;
            if (canRun(batteries, n, mid)) left = mid;
            else right = mid - 1;
        }
        return left;
    }

    bool canRun(vector<int>& batteries, int n, long long time) {
        sort(batteries.begin(), batteries.end(), greater<int>());
        priority_queue<int> pq;
        for (int i = 0; i < n; i++) pq.push(batteries[i]);
        for (int i = n; i < batteries.size(); i++) {
            int top = pq.top(); pq.pop();
            if (top + batteries[i] < time) return false;
            pq.push(batteries[i]);
        }
        return true;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public long maxRunTime(int n, int[] batteries) {
        long sum = 0;
        for (int battery : batteries) sum += battery;
        long left = 0, right = sum / n;
        while (left < right) {
            long mid = left + (right - left + 1) / 2;
            if (canRun(batteries, n, mid)) left = mid;
            else right = mid - 1;
        }
        return left;
    }

    public boolean canRun(int[] batteries, int n, long time) {
        Arrays.sort(batteries);
        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> b - a);
        for (int i = 0; i < n; i++) pq.offer(batteries[i]);
        for (int i = n; i < batteries.length; i++) {
            int top = pq.poll();
            if (top + batteries[i] < time) return false;
            pq.offer(batteries[i]);
        }
        return true;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        sum_batteries = sum(batteries)
        left, right = 0, sum_batteries // n
        while left < right:
            mid = left + (right - left + 1) // 2
            if self.canRun(batteries, n, mid):
                left = mid
            else:
                right = mid - 1
        return left

    def canRun(self, batteries: List[int], n: int, time: int) -> bool:
        batteries.sort(reverse=True)
        pq = []
        for i in range(n):
            pq.append(batteries[i])
        for i in range(n, len(batteries)):
            pq.sort(reverse=True)
            top = pq.pop(0)
            if top + batteries[i] < time:
                return False
            pq.append(batteries[i])
        return True
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        sum_batteries = sum(batteries)
        left, right = 0, sum_batteries // n
        while left < right:
            mid = left + (right - left + 1) // 2
            if self.canRun(batteries, n, mid):
                left = mid
            else:
                right = mid - 1
        return left

    def canRun(self, batteries: List[int], n: int, time: int) -> bool:
        batteries.sort(reverse=True)
        pq = []
        for i in range(n):
            pq.append(batteries[i])
        for i in range(n, len(batteries)):
            pq.sort(reverse=True)
            top = pq.pop(0)
            if top + batteries[i] < time:
                return False
            pq.append(batteries[i])
        return True
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
typedef struct {
    int val;
    struct Node* next;
} Node;

Node* newNode(int val) {
    Node* node = (Node*)malloc(sizeof(Node));
    node->val = val;
    node->next = NULL;
    return node;
}

void push(Node** head, int val) {
    Node* node = newNode(val);
    node->next = *head;
    *head = node;
}

int pop(Node** head) {
    int val = (*head)->val;
    Node* temp = *head;
    *head = (*head)->next;
    free(temp);
    return val;
}

int maxRunTime(int n, int* batteries, int batteriesSize) {
    long long sum = 0;
    for (int i = 0; i < batteriesSize; i++) sum += batteries[i];
    long long left = 0, right = sum / n;
    while (left < right) {
        long long mid = left + (right - left + 1) / 2;
        if (canRun(batteries, batteriesSize, n, mid)) left = mid;
        else right = mid - 1;
    }
    return left;
}

int canRun(int* batteries, int batteriesSize, int n, long long time) {
    int* sortedBatteries = (int*)malloc(batteriesSize * sizeof(int));
    for (int i = 0; i < batteriesSize; i++) sortedBatteries[i] = batteries[i];
    qsort(sortedBatteries, batteriesSize, sizeof(int), compare);
    Node* head = NULL;
    for (int i = 0; i < n; i++) push(&head, sortedBatteries[i]);
    for (int i = n; i < batteriesSize; i++) {
        int top = pop(&head);
        if (top + sortedBatteries[i] < time) return 0;
        push(&head, sortedBatteries[i]);
    }
    return 1;
}

int compare(const void* a, const void* b) {
    return (*(int*)b - *(int*)a);
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public long MaxRunTime(int n, int[] batteries) {
        long sum = 0;
        foreach (int battery in batteries) sum += battery;
        long left = 0, right = sum / n;
        while (left < right) {
            long mid = left + (right - left + 1) / 2;
            if (CanRun(batteries, n, mid)) left = mid;
            else right = mid - 1;
        }
        return left;
    }

    public bool CanRun(int[] batteries, int n, long time) {
        Array.Sort(batteries);
        Array.Reverse(batteries);
        var pq = new List<int>();
        for (int i = 0; i < n; i++) pq.Add(batteries[i]);
        for (int i = n; i < batteries.Length; i++) {
            pq.Sort((a, b) => b.CompareTo(a));
            int top = pq[0];
            pq.RemoveAt(0);
            if (top + batteries[i] < time) return false;
            pq.Add(batteries[i]);
        }
        return true;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var maxRunTime = function(n, batteries) {
    let sum = 0;
    for (let battery of batteries) sum += battery;
    let left = 0, right = Math.floor(sum / n);
    while (left < right) {
        let mid = left + Math.floor((right - left + 1) / 2);
        if (canRun(batteries, n, mid)) left = mid;
        else right = mid - 1;
    }
    return left;
};

var canRun = function(batteries, n, time) {
    batteries.sort((a, b) => b - a);
    let pq = [];
    for (let i = 0; i < n; i++) pq.push(batteries[i]);
    for (let i = n; i < batteries.length; i++) {
        pq.sort((a, b) => b - a);
        let top = pq.shift();
        if (top + batteries[i] < time) return false;
        pq.push(batteries[i]);
    }
    return true;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maxRunTime(n: number, batteries: number[]): number {
    let sum = 0;
    for (let battery of batteries) sum += battery;
    let left = 0, right = Math.floor(sum / n);
    while (left < right) {
        let mid = left + Math.floor((right - left + 1) / 2);
        if (canRun(batteries, n, mid)) left = mid;
        else right = mid - 1;
    }
    return left;
}

function canRun(batteries: number[], n: number, time: number): boolean {
    batteries.sort((a, b) => b - a);
    let pq: number[] = [];
    for (let i = 0; i < n; i++) pq.push(batteries[i]);
    for (let i = n; i < batteries.length; i++) {
        pq.sort((a, b) => b - a);
        let top = pq.shift() as number;
        if (top + batteries[i] < time) return false;
        pq.push(batteries[i]);
    }
    return true;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function maxRunTime($n, $batteries) {
        $sum = 0;
        foreach ($batteries as $battery) $sum += $battery;
        $left = 0; $right = floor($sum / $n);
        while ($left < $right) {
            $mid = $left + floor(($right - $left + 1) / 2);
            if ($this->canRun($batteries, $n, $mid)) $left = $mid;
            else $right = $mid - 1;
        }
        return $left;
    }

    function canRun($batteries, $n, $time) {
        rsort($batteries);
        $pq = array_slice($batteries, 0, $n);
        for ($i = $n; $i < count($batteries); $i++) {
            rsort($pq);
            $top = array_shift($pq);
            if ($top + $batteries[$i] < $time) return false;
            $pq[] = $batteries[$i];
        }
        return true;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func maxRunTime(_ n: Int, _ batteries: [Int]) -> Int {
        var sum = 0
        for battery in batteries {
            sum += battery
        }
        var left = 0
        var right = sum / n
        while left < right {
            let mid = left + (right - left + 1) / 2
            if canRun(batteries, n, mid) {
                left = mid
            } else {
                right = mid - 1
            }
        }
        return left
    }

    func canRun(_ batteries: [Int], _ n: Int, _ time: Int) -> Bool {
        var batteries = batteries
        batteries.sort { $0 > $1 }
        var pq: [Int] = []
        for i in 0..<n {
            pq.append(batteries[i])
        }
        for i in n..<batteries.count {
            pq.sort { $0 > $1 }
            let top = pq.removeFirst()
            if top + batteries[i] < time {
                return false
            }
            pq.append(batteries[i])
        }
        return true
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun maxRunTime(n: Int, batteries: IntArray): Int {
        var sum = 0
        for (battery in batteries) sum += battery
        var left = 0
        var right = sum / n
        while (left < right) {
            val mid = left + (right - left + 1) / 2
            if (canRun(batteries, n, mid)) left = mid
            else right = mid - 1
        }
        return left
    }

    fun canRun(batteries: IntArray, n: Int, time: Int): Boolean {
        batteries.sortDescending()
        val pq = mutableListOf<Int>()
        for (i in 0 until n) pq.add(batteries[i])
        for (i in n until batteries.size) {
            pq.sortDescending()
            val top = pq.removeAt(0)
            if (top + batteries[i] < time) return false
            pq.add(batteries[i])
        }
        return true
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
    int maxRunTime(int n, List<int> batteries) {
        int sum = 0;
        for (int battery in batteries) sum += battery;
        int left = 0, right = sum ~/ n;
        while (left < right) {
            int mid = left + (right - left + 1) ~/ 2;
            if (canRun(batteries, n, mid)) left = mid;
            else right = mid - 1;
        }
        return left;
    }

    bool canRun(List<int> batteries, int n, int time) {
        batteries.sort((a, b) => b - a);
        List<int> pq = [];
        for (int i = 0; i < n; i++) pq.add(batteries[i]);
        for (int i = n; i < batteries.length; i++) {
            pq.sort((a, b) => b - a);
            int top = pq.removeAt(0);
            if (top + batteries[i] < time) return false;
            pq.add(batteries[i]);
        }
        return true;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
package main

import (
    "fmt"
    "sort"
)

func maxRunTime(n int, batteries []int) int {
    sum := 0
    for _, battery := range batteries {
        sum += battery
    }
    left, right := 0, sum/n
    for left < right {
        mid := left + (right-left+1)/2
        if canRun(batteries, n, mid) {
            left = mid
        } else {
            right = mid - 1
        }
    }
    return left
}

func canRun(batteries []int, n, time int) bool {
    sort.Sort(sort.Reverse(sort.IntSlice(batteries)))
    pq := make([]int, 0)
    for i := 0; i < n; i++ {
        pq = append(pq, batteries[i])
    }
    for i := n; i < len(batteries); i++ {
        sort.Sort(sort.Reverse(sort.IntSlice(pq)))
        top := pq[0]
        pq = pq[1:]
        if top+batteries[i] < time {
            return false
        }
        pq = append(pq, batteries[i])
    }
    return true
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
class Solution
    def max_run_time(n, batteries)
        sum = 0
        batteries.each { |battery| sum += battery }
        left, right = 0, sum / n
        while left < right
            mid = left + (right - left + 1) / 2
            if can_run(batteries, n, mid)
                left = mid
            else
                right = mid - 1
            end
        end
        left
    end

    def can_run(batteries, n, time)
        batteries.sort!.reverse!
        pq = []
        n.times { |i| pq << batteries[i] }
        (n...batteries.size).each do |i|
            pq.sort!.reverse!
            top = pq.shift
            if top + batteries[i] < time
                return false
            end
            pq << batteries[i]
        end
        true
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def maxRunTime(n: Int, batteries: Array[Int]): Int = {
        val sum = batteries.sum
        var left = 0
        var right = sum / n
        while (left < right) {
            val mid = left + (right - left + 1) / 2
            if (canRun(batteries, n, mid)) left = mid
            else right = mid - 1
        }
        left
    }

    def canRun(batteries: Array[Int], n: Int, time: Int): Boolean = {
        val sortedBatteries = batteries.sorted.reverse
        val pq = scala.collection.mutable.PriorityQueue[Int]()
        for (i <- 0 until n) pq.enqueue(sortedBatteries(i))
        for (i <- n until sortedBatteries.length) {
            val top = pq.dequeue()
            if (top + sortedBatteries(i) < time) return false
            pq.enqueue(sortedBatteries(i))
        }
        true
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
struct Solution;

impl Solution {
    pub fn max_run_time(n: i32, batteries: Vec<i32>) -> i32 {
        let sum: i64 = batteries.iter().sum::<i32>() as i64;
        let mut left = 0;
        let mut right = sum / n as i64;
        while left < right {
            let mid = left + (right - left + 1) / 2;
            if Solution::can_run(&batteries, n, mid) {
                left = mid;
            } else {
                right = mid - 1;
            }
        }
        left as i32
    }

    pub fn can_run(batteries: &Vec<i32>, n: i32, time: i64) -> bool {
        let mut batteries = batteries.clone();
        batteries.sort_unstable_by(|a, b| b.cmp(a));
        let mut pq: Vec<i32> = batteries.iter().take(n as usize).cloned().collect();
        for i in n as usize..batteries.len() {
            pq.sort_unstable_by(|a, b| b.cmp(a));
            let top = pq.remove(0);
            if top as i64 + batteries[i] as i64 < time {
                return false;
            }
            pq.push(batteries[i]);
        }
        true
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
define (max-run-time n batteries)
    (let loop ((left 0) (right (quotient (apply + batteries) n)))
        (if (< left right)
            (let ((mid (quotient (+ left right 1) 2)))
                (if (can-run batteries n mid)
                    (loop mid right)
                    (loop left (- mid 1))))
            left))

(define (can-run batteries n time)
    (let ((batteries (sort batteries >)))
        (let loop ((pq (take batteries n)) (i n))
            (if (< i (length batteries))
                (let ((top (car pq)))
                    (if (< (+ top (list-ref batteries i)) time)
                        #f
                        (loop (append (cdr pq) (list (list-ref batteries i))) (+ i 1))))
                #t))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
max_run_time(N, Batteries) ->
    Left = 0,
    Right = lists:sum(Batteries) div N,
    loop(Left, Right, Batteries, N).

loop(Left, Right, Batteries, N) when Left < Right ->
    Mid = Left + (Right - Left + 1) div 2,
    case can_run(Batteries, N, Mid) of
        true -> loop(Mid, Right, Batteries, N);
        false -> loop(Left, Mid - 1, Batteries, N)
    end;
loop(Left, _, _, _) -> Left.

can_run(Batteries, N, Time) ->
    SortedBatteries = lists:sort(fun(A, B) -> B =< A end, Batteries),
    PQ = lists:sublist(SortedBatteries, N),
    can_run_loop(PQ, lists:nthtail(N, SortedBatteries), Time).

can_run_loop(PQ, [], _) -> true;

can_run_loop(PQ, [H | T], Time) ->
    [Top | Rest] = lists:sort(fun(A, B) -> B =< A end, PQ),
    case Top + H < Time of
        true -> false;
        false -> can_run_loop(Rest ++ [H], T, Time)
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
    def max_run_time(n, batteries) do
        sum = Enum.sum(batteries)
        left = 0
        right = div(sum, n)
        loop(left, right, batteries, n)
    end

    defp loop(left, right, batteries, n) when left < right do
        mid = left + div(right - left + 1, 2)
        case can_run(batteries, n, mid) do
            true -> loop(mid, right, batteries, n)
            false -> loop(left, mid - 1, batteries, n)
        end
    end

    defp loop(left, _, _, _) do
        left
    end

    defp can_run(batteries, n, time) do
        sorted_batteries = Enum.sort(batteries, &(&1 >= &2))
        pq = Enum.take(sorted_batteries, n)
        can_run_loop(pq, Enum.drop(sorted_batteries, n), time)
    end

    defp can_run_loop(pq, [], _) do
        true
    end

    defp can_run_loop(pq, [h | t], time) do
        [top | rest] = Enum.sort(pq, &(&1 >= &2))
        case top + h < time do
            true -> can_run_loop(rest ++ [h], t, time)
            false -> false
        end
    end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of this solution is O(m log m log (sum of batteries / n)), where m is the number of batteries and n is the number of computers. This is because we are performing a binary search over the possible running times, and for each mid value, we are sorting the batteries and assigning them to computers.

- **Space Complexity:** The space complexity of this solution is O(m), where m is the number of batteries. This is because we need to store the batteries and the computers, and we are using a greedy approach to assign batteries to computers, which requires a small amount of extra space.

</div>
</details>
