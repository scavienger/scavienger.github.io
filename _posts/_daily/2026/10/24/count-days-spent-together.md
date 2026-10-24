---
layout: post
title: "Count Days Spent Together"
date: 2026-10-24 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Math", "String"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/count-days-spent-together/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int countDaysTogether(string arriveAlice,\
        \ string leaveAlice, string arriveBob, string leaveBob) {\n        int months[]\
        \ = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};\n        auto toDayOfYear\
        \ = [&](string date) {\n            int m = stoi(date.substr(0, 2));\n     \
        \       int d = stoi(date.substr(3, 2));\n            int day = 0;\n       \
        \     for (int i = 0; i < m - 1; ++i) {\n                day += months[i];\n\
        \            }\n            return day + d;\n        };\n\n        int startAlice\
        \ = toDayOfYear(arriveAlice);\n        int endAlice = toDayOfYear(leaveAlice);\n\
        \        int startBob = toDayOfYear(arriveBob);\n        int endBob = toDayOfYear(leaveBob);\n\
        \n        int start = max(startAlice, startBob);\n        int end = min(endAlice,\
        \ endBob);\n\n        return max(0, end - start + 1);\n    }\n};"
      java: "class Solution {\n    public int countDaysTogether(String arriveAlice,\
        \ String leaveAlice, String arriveBob, String leaveBob) {\n        int[] months\
        \ = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};\n\n        int startAlice\
        \ = toDayOfYear(arriveAlice, months);\n        int endAlice = toDayOfYear(leaveAlice,\
        \ months);\n        int startBob = toDayOfYear(arriveBob, months);\n       \
        \ int endBob = toDayOfYear(leaveBob, months);\n\n        int start = Math.max(startAlice,\
        \ startBob);\n        int end = Math.min(endAlice, endBob);\n\n        return\
        \ Math.max(0, end - start + 1);\n    }\n\n    private int toDayOfYear(String\
        \ date, int[] months) {\n        int m = Integer.parseInt(date.substring(0,\
        \ 2));\n        int d = Integer.parseInt(date.substring(3, 5));\n        int\
        \ day = 0;\n        for (int i = 0; i < m - 1; i++) {\n            day += months[i];\n\
        \        }\n        return day + d;\n    }\n}"
      python: "class Solution(object):\n    def countDaysTogether(self, arriveAlice,\
        \ leaveAlice, arriveBob, leaveBob):\n        \"\"\"\n        :type arriveAlice:\
        \ str\n        :type leaveAlice: str\n        :type arriveBob: str\n       \
        \ :type leaveBob: str\n        :rtype: int\n        \"\"\"\n        months =\
        \ [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]\n\n        def to_day_of_year(date):\n\
        \            m, d = map(int, date.split('-'))\n            return sum(months[:m-1])\
        \ + d\n\n        start_alice = to_day_of_year(arriveAlice)\n        end_alice\
        \ = to_day_of_year(leaveAlice)\n        start_bob = to_day_of_year(arriveBob)\n\
        \        end_bob = to_day_of_year(leaveBob)\n\n        start = max(start_alice,\
        \ start_bob)\n        end = min(end_alice, end_bob)\n\n        return max(0,\
        \ end - start + 1)"
      python3: "class Solution:\n    def countDaysTogether(self, arriveAlice: str, leaveAlice:\
        \ str, arriveBob: str, leaveBob: str) -> int:\n        months = [31, 28, 31,\
        \ 30, 31, 30, 31, 31, 30, 31, 30, 31]\n\n        def to_day_of_year(date: str)\
        \ -> int:\n            m, d = map(int, date.split('-'))\n            return\
        \ sum(months[:m-1]) + d\n\n        start_alice = to_day_of_year(arriveAlice)\n\
        \        end_alice = to_day_of_year(leaveAlice)\n        start_bob = to_day_of_year(arriveBob)\n\
        \        end_bob = to_day_of_year(leaveBob)\n\n        overlap_start = max(start_alice,\
        \ start_bob)\n        overlap_end = min(end_alice, end_bob)\n\n        return\
        \ max(0, overlap_end - overlap_start + 1)"
      c: "int toDayOfYear(char* date, int* months) {\n    int m = (date[0] - '0') *\
        \ 10 + (date[1] - '0');\n    int d = (date[3] - '0') * 10 + (date[4] - '0');\n\
        \    int day = 0;\n    for (int i = 0; i < m - 1; i++) {\n        day += months[i];\n\
        \    }\n    return day + d;\n}\n\nint countDaysTogether(char* arriveAlice, char*\
        \ leaveAlice, char* arriveBob, char* leaveBob) {\n    int months[] = {31, 28,\
        \ 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};\n\n    int startAlice = toDayOfYear(arriveAlice,\
        \ months);\n    int endAlice = toDayOfYear(leaveAlice, months);\n    int startBob\
        \ = toDayOfYear(arriveBob, months);\n    int endBob = toDayOfYear(leaveBob,\
        \ months);\n\n    int start = startAlice > startBob ? startAlice : startBob;\n\
        \    int end = endAlice < endBob ? endAlice : endBob;\n\n    int result = end\
        \ - start + 1;\n    return result > 0 ? result : 0;\n}"
      csharp: "public class Solution {\n    public int CountDaysTogether(string arriveAlice,\
        \ string leaveAlice, string arriveBob, string leaveBob) {\n        int[] months\
        \ = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };\n\n        int ToDayOfYear(string\
        \ date) {\n            int m = int.Parse(date.Substring(0, 2));\n          \
        \  int d = int.Parse(date.Substring(3, 2));\n            int day = 0;\n    \
        \        for (int i = 0; i < m - 1; i++) {\n                day += months[i];\n\
        \            }\n            return day + d;\n        }\n\n        int startAlice\
        \ = ToDayOfYear(arriveAlice);\n        int endAlice = ToDayOfYear(leaveAlice);\n\
        \        int startBob = ToDayOfYear(arriveBob);\n        int endBob = ToDayOfYear(leaveBob);\n\
        \n        int start = Math.Max(startAlice, startBob);\n        int end = Math.Min(endAlice,\
        \ endBob);\n\n        return Math.Max(0, end - start + 1);\n    }\n}"
      javascript: "/**\n * @param {string} arriveAlice\n * @param {string} leaveAlice\n\
        \ * @param {string} arriveBob\n * @param {string} leaveBob\n * @return {number}\n\
        \ */\nvar countDaysTogether = function(arriveAlice, leaveAlice, arriveBob, leaveBob)\
        \ {\n    const months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];\n\n\
        \    const toDayOfYear = (date) => {\n        const [m, d] = date.split('-').map(Number);\n\
        \        let day = 0;\n        for (let i = 0; i < m - 1; i++) {\n         \
        \   day += months[i];\n        }\n        return day + d;\n    };\n\n    const\
        \ startAlice = toDayOfYear(arriveAlice);\n    const endAlice = toDayOfYear(leaveAlice);\n\
        \    const startBob = toDayOfYear(arriveBob);\n    const endBob = toDayOfYear(leaveBob);\n\
        \n    const start = Math.max(startAlice, startBob);\n    const end = Math.min(endAlice,\
        \ endBob);\n\n    return Math.max(0, end - start + 1);\n};"
      typescript: "function countDaysTogether(arriveAlice: string, leaveAlice: string,\
        \ arriveBob: string, leaveBob: string): number {\n    const daysInMonth = [31,\
        \ 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];\n\n    function getDayOfYear(dateStr:\
        \ string): number {\n        const parts = dateStr.split(\"-\");\n        const\
        \ month = parseInt(parts[0], 10);\n        const day = parseInt(parts[1], 10);\n\
        \        let dayOfYear = 0;\n        for (let i = 0; i < month - 1; i++) {\n\
        \            dayOfYear += daysInMonth[i];\n        }\n        dayOfYear += day;\n\
        \        return dayOfYear;\n    }\n\n    const startA = getDayOfYear(arriveAlice);\n\
        \    const endA = getDayOfYear(leaveAlice);\n    const startB = getDayOfYear(arriveBob);\n\
        \    const endB = getDayOfYear(leaveBob);\n\n    const overlapStart = Math.max(startA,\
        \ startB);\n    const overlapEnd = Math.min(endA, endB);\n\n    const totalDays\
        \ = overlapEnd - overlapStart + 1;\n    return totalDays > 0 ? totalDays : 0;\n\
        };"
      php: "class Solution {\n\n    /**\n     * @param String $arriveAlice\n     * @param\
        \ String $leaveAlice\n     * @param String $arriveBob\n     * @param String\
        \ $leaveBob\n     * @return Integer\n     */\n    function countDaysTogether($arriveAlice,\
        \ $leaveAlice, $arriveBob, $leaveBob) {\n        $daysInMonth = [31, 28, 31,\
        \ 30, 31, 30, 31, 31, 30, 31, 30, 31];\n\n        $getDayOfYear = function($dateStr)\
        \ use ($daysInMonth) {\n            $parts = explode(\"-\", $dateStr);\n   \
        \         $month = intval($parts[0]);\n            $day = intval($parts[1]);\n\
        \            $dayOfYear = 0;\n            for ($i = 0; $i < $month - 1; $i++)\
        \ {\n                $dayOfYear += $daysInMonth[$i];\n            }\n      \
        \      $dayOfYear += $day;\n            return $dayOfYear;\n        };\n\n \
        \       $startA = $getDayOfYear($arriveAlice);\n        $endA = $getDayOfYear($leaveAlice);\n\
        \        $startB = $getDayOfYear($arriveBob);\n        $endB = $getDayOfYear($leaveBob);\n\
        \n        $overlapStart = max($startA, $startB);\n        $overlapEnd = min($endA,\
        \ $endB);\n\n        $totalDays = $overlapEnd - $overlapStart + 1;\n       \
        \ return $totalDays > 0 ? $totalDays : 0;\n    }\n}"
      swift: "class Solution {\n    func countDaysTogether(_ arriveAlice: String, _\
        \ leaveAlice: String, _ arriveBob: String, _ leaveBob: String) -> Int {\n  \
        \      let daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]\n\n\
        \        func getDayOfYear(_ dateStr: String) -> Int {\n            let parts\
        \ = dateStr.split(separator: \"-\")\n            guard parts.count == 2, let\
        \ month = Int(parts[0]), let day = Int(parts[1]) else { return 0 }\n       \
        \     var dayOfYear = 0\n            for i in 0..<(month - 1) {\n          \
        \      dayOfYear += daysInMonth[i]\n            }\n            dayOfYear +=\
        \ day\n            return dayOfYear\n        }\n\n        let startA = getDayOfYear(arriveAlice)\n\
        \        let endA = getDayOfYear(leaveAlice)\n        let startB = getDayOfYear(arriveBob)\n\
        \        let endB = getDayOfYear(leaveBob)\n\n        let overlapStart = max(startA,\
        \ startB)\n        let overlapEnd = min(endA, endB)\n\n        let totalDays\
        \ = overlapEnd - overlapStart + 1\n        return totalDays > 0 ? totalDays\
        \ : 0\n    }\n}"
      kotlin: "class Solution {\n    fun countDaysTogether(arriveAlice: String, leaveAlice:\
        \ String, arriveBob: String, leaveBob: String): Int {\n        val daysInMonth\
        \ = intArrayOf(31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)\n\n        fun\
        \ getDayOfYear(dateStr: String): Int {\n            val parts = dateStr.split(\"\
        -\")\n            val month = parts[0].toInt()\n            val day = parts[1].toInt()\n\
        \            var total = 0\n            for (i in 0 until month - 1) {\n   \
        \             total += daysInMonth[i]\n            }\n            return total\
        \ + day\n        }\n\n        val startA = getDayOfYear(arriveAlice)\n     \
        \   val endA = getDayOfYear(leaveAlice)\n        val startB = getDayOfYear(arriveBob)\n\
        \        val endB = getDayOfYear(leaveBob)\n\n        val overlapStart = if\
        \ (startA > startB) startA else startB\n        val overlapEnd = if (endA <\
        \ endB) endA else endB\n\n        val totalDays = overlapEnd - overlapStart\
        \ + 1\n        return if (totalDays > 0) totalDays else 0\n    }\n}"
      dart: "class Solution {\n  int countDaysTogether(String arriveAlice, String leaveAlice,\
        \ String arriveBob, String leaveBob) {\n    final List<int> daysInMonth = [31,\
        \ 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];\n\n    int getDayOfYear(String\
        \ dateStr) {\n      final List<String> parts = dateStr.split('-');\n      final\
        \ int month = int.parse(parts[0]);\n      final int day = int.parse(parts[1]);\n\
        \      int total = 0;\n      for (int i = 0; i < month - 1; i++) {\n       \
        \ total += daysInMonth[i];\n      }\n      return total + day;\n    }\n\n  \
        \  final int startA = getDayOfYear(arriveAlice);\n    final int endA = getDayOfYear(leaveAlice);\n\
        \    final int startB = getDayOfYear(arriveBob);\n    final int endB = getDayOfYear(leaveBob);\n\
        \n    final int overlapStart = startA > startB ? startA : startB;\n    final\
        \ int overlapEnd = endA < endB ? endA : endB;\n\n    final int totalDays = overlapEnd\
        \ - overlapStart + 1;\n    return totalDays > 0 ? totalDays : 0;\n  }\n}"
      go: "import (\n    \"strconv\"\n    \"strings\"\n)\n\nfunc countDaysTogether(arriveAlice\
        \ string, leaveAlice string, arriveBob string, leaveBob string) int {\n    daysInMonth\
        \ := []int{31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}\n\n    getDayOfYear\
        \ := func(dateStr string) int {\n        parts := strings.Split(dateStr, \"\
        -\")\n        month, _ := strconv.Atoi(parts[0])\n        day, _ := strconv.Atoi(parts[1])\n\
        \        total := 0\n        for i := 0; i < month-1; i++ {\n            total\
        \ += daysInMonth[i]\n        }\n        return total + day\n    }\n\n    startA\
        \ := getDayOfYear(arriveAlice)\n    endA := getDayOfYear(leaveAlice)\n    startB\
        \ := getDayOfYear(arriveBob)\n    endB := getDayOfYear(leaveBob)\n\n    overlapStart\
        \ := startA\n    if startB > overlapStart {\n        overlapStart = startB\n\
        \    }\n\n    overlapEnd := endA\n    if endB < overlapEnd {\n        overlapEnd\
        \ = endB\n    }\n\n    totalDays := overlapEnd - overlapStart + 1\n    if totalDays\
        \ < 0 {\n        return 0\n    }\n    return totalDays\n}"
      ruby: "def count_days_together(arrive_alice, leave_alice, arrive_bob, leave_bob)\n\
        \  start_a = to_day_of_year(arrive_alice)\n  end_a = to_day_of_year(leave_alice)\n\
        \  start_b = to_day_of_year(arrive_bob)\n  end_b = to_day_of_year(leave_bob)\n\
        \n  overlap_start = [start_a, start_b].max\n  overlap_end = [end_a, end_b].min\n\
        \n  [0, overlap_end - overlap_start + 1].max\nend\n\ndef to_day_of_year(date)\n\
        \  m, d = date.split('-').map(&:to_i)\n  days_in_month = [31, 28, 31, 30, 31,\
        \ 30, 31, 31, 30, 31, 30, 31]\n  days_in_month.first(m - 1).sum + d\nend"
      scala: "object Solution {\n    def countDaysTogether(arriveAlice: String, leaveAlice:\
        \ String, arriveBob: String, leaveBob: String): Int = {\n        def toDayOfYear(date:\
        \ String): Int = {\n            val parts = date.split(\"-\")\n            val\
        \ m = parts(0).toInt\n            val d = parts(1).toInt\n            val daysInMonth\
        \ = Array(31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)\n            daysInMonth.take(m\
        \ - 1).sum + d\n        }\n\n        val startA = toDayOfYear(arriveAlice)\n\
        \        val endA = toDayOfYear(leaveAlice)\n        val startB = toDayOfYear(arriveBob)\n\
        \        val endB = toDayOfYear(leaveBob)\n\n        val overlapStart = math.max(startA,\
        \ startB)\n        val overlapEnd = math.min(endA, endB)\n\n        math.max(0,\
        \ overlapEnd - overlapStart + 1)\n    }\n}"
      rust: "impl Solution {\n    pub fn count_days_together(arrive_alice: String, leave_alice:\
        \ String, arrive_bob: String, leave_bob: String) -> i32 {\n        fn to_day_of_year(date:\
        \ &str) -> i32 {\n            let m: usize = date[0..2].parse().unwrap();\n\
        \            let d: i32 = date[3..5].parse().unwrap();\n            let days_in_month\
        \ = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];\n            let sum_prev:\
        \ i32 = days_in_month[0..m-1].iter().sum();\n            sum_prev + d\n    \
        \    }\n\n        let start_a = to_day_of_year(&arrive_alice);\n        let\
        \ end_a = to_day_of_year(&leave_alice);\n        let start_b = to_day_of_year(&arrive_bob);\n\
        \        let end_b = to_day_of_year(&leave_bob);\n\n        let overlap_start\
        \ = start_a.max(start_b);\n        let overlap_end = end_a.min(end_b);\n\n \
        \       (overlap_end - overlap_start + 1).max(0)\n    }\n}"
      racket: "(define/contract (count-days-together arriveAlice leaveAlice arriveBob\
        \ leaveBob)\n  (-> string? string? string? string? exact-integer?)\n  (define\
        \ (to-day-of-year date)\n    (let ([m (string->number (substring date 0 2))]\n\
        \          [d (string->number (substring date 3 5))]\n          [days-in-month\
        \ '(31 28 31 30 31 30 31 31 30 31 30 31)])\n      (+ (for/sum ([dm days-in-month]\
        \ [i (in-range (- m 1))]) dm) d)))\n  (let ([startA (to-day-of-year arriveAlice)]\n\
        \        [endA (to-day-of-year leaveAlice)]\n        [startB (to-day-of-year\
        \ arriveBob)]\n        [endB (to-day-of-year leaveBob)])\n    (max 0 (+ 1 (-\
        \ (min endA endB) (max startA startB)))))\n  )"
      erlang: "-spec count_days_together(ArriveAlice :: unicode:unicode_binary(), LeaveAlice\
        \ :: unicode:unicode_binary(), ArriveBob :: unicode:unicode_binary(), LeaveBob\
        \ :: unicode:unicode_binary()) -> integer().\ncount_days_together(ArriveAlice,\
        \ LeaveAlice, ArriveBob, LeaveBob) ->\n  StartA = to_day_of_year(ArriveAlice),\n\
        \  EndA = to_day_of_year(LeaveAlice),\n  StartB = to_day_of_year(ArriveBob),\n\
        \  EndB = to_day_of_year(LeaveBob),\n  OverlapStart = max(StartA, StartB),\n\
        \  OverlapEnd = min(EndA, EndB),\n  max(0, OverlapEnd - OverlapStart + 1).\n\
        \nto_day_of_year(Date) ->\n  [MStr, DStr] = binary:split(Date, <<\"-\">>),\n\
        \  M = binary_to_integer(MStr),\n  D = binary_to_integer(DStr),\n  DaysInMonth\
        \ = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],\n  lists:sum(lists:sublist(DaysInMonth,\
        \ M - 1)) + D."
      elixir: "defmodule Solution do\n  @spec count_days_together(arrive_alice :: String.t,\
        \ leave_alice :: String.t, arrive_bob :: String.t, leave_bob :: String.t) ::\
        \ integer\n  def count_days_together(arrive_alice, leave_alice, arrive_bob,\
        \ leave_bob) do\n    start_a = to_day_of_year(arrive_alice)\n    end_a = to_day_of_year(leave_alice)\n\
        \    start_b = to_day_of_year(arrive_bob)\n    end_b = to_day_of_year(leave_bob)\n\
        \n    overlap_start = max(start_a, start_b)\n    overlap_end = min(end_a, end_b)\n\
        \n    max(0, overlap_end - overlap_start + 1)\n  end\n\n  defp to_day_of_year(date)\
        \ do\n    [m, d] = String.split(date, \"-\") |> Enum.map(&String.to_integer/1)\n\
        \    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]\n    Enum.take(days_in_month,\
        \ m - 1) |> Enum.sum() |> Kernel.+(d)\n  end\nend"
    approach: 'To solve this problem, we first convert the given dates from the "MM-DD"
      string format into a single integer representing the day of the year (from 1 to
      365). This is done by summing the total number of days in the months preceding
      the current month and adding the current day. Since the year is not a leap year,
      we use the fixed monthly distribution: [31, 28, 31, 30, 31, 30, 31, 31, 30, 31,
      30, 31].


      Once Alice''s stay is represented as an interval [startAlice, endAlice] and Bob''s
      stay as [startBob, endBob], the number of days they spend together is the size
      of the intersection of these two intervals. The intersection of [a, b] and [c,
      d] is [max(a, c), min(b, d)]. The number of overlapping days is calculated as
      max(0, min(endAlice, endBob) - max(startAlice, startBob) + 1). If the start of
      the intersection is greater than the end, the result is 0.'
    time_complexity: O(1) with one-paragraph explanation
    space_complexity: O(1) with one-paragraph explanation
    elapsed_time: 135.75934624671936
    model: gemini-3-flash-preview
    generated_at: '2026-10-24 02:46:29 '
---

## Problem #2409: Count Days Spent Together

**Difficulty:** Easy

**Topics:** Math, String

## Problem Description

<p>Alice and Bob are traveling to Rome for separate business meetings.</p>

<p>You are given 4 strings <code>arriveAlice</code>, <code>leaveAlice</code>, <code>arriveBob</code>, and <code>leaveBob</code>. Alice will be in the city from the dates <code>arriveAlice</code> to <code>leaveAlice</code> (<strong>inclusive</strong>), while Bob will be in the city from the dates <code>arriveBob</code> to <code>leaveBob</code> (<strong>inclusive</strong>). Each will be a 5-character string in the format <code>&quot;MM-DD&quot;</code>, corresponding to the month and day of the date.</p>

<p>Return<em> the total number of days that Alice and Bob are in Rome together.</em></p>

<p>You can assume that all dates occur in the <strong>same</strong> calendar year, which is <strong>not</strong> a leap year. Note that the number of days per month can be represented as: <code>[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arriveAlice = &quot;08-15&quot;, leaveAlice = &quot;08-18&quot;, arriveBob = &quot;08-16&quot;, leaveBob = &quot;08-19&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> Alice will be in Rome from August 15 to August 18. Bob will be in Rome from August 16 to August 19. They are both in Rome together on August 16th, 17th, and 18th, so the answer is 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arriveAlice = &quot;10-01&quot;, leaveAlice = &quot;10-31&quot;, arriveBob = &quot;11-01&quot;, leaveBob = &quot;12-31&quot;
<strong>Output:</strong> 0
<strong>Explanation:</strong> There is no day when Alice and Bob are in Rome together, so we return 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>All dates are provided in the format <code>&quot;MM-DD&quot;</code>.</li>
	<li>Alice and Bob&#39;s arrival dates are <strong>earlier than or equal to</strong> their leaving dates.</li>
	<li>The given dates are valid dates of a <strong>non-leap</strong> year.</li>
</ul>


## Hints

1. For a given day, determine if Alice or Bob or both are in Rome.

2. Brute force all 365 days for both Alice and Bob.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To solve this problem, we first convert the given dates from the "MM-DD" string format into a single integer representing the day of the year (from 1 to 365). This is done by summing the total number of days in the months preceding the current month and adding the current day. Since the year is not a leap year, we use the fixed monthly distribution: [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31].

Once Alice's stay is represented as an interval [startAlice, endAlice] and Bob's stay as [startBob, endBob], the number of days they spend together is the size of the intersection of these two intervals. The intersection of [a, b] and [c, d] is [max(a, c), min(b, d)]. The number of overlapping days is calculated as max(0, min(endAlice, endBob) - max(startAlice, startBob) + 1). If the start of the intersection is greater than the end, the result is 0.

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
    int countDaysTogether(string arriveAlice, string leaveAlice, string arriveBob, string leaveBob) {
        int months[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        auto toDayOfYear = [&](string date) {
            int m = stoi(date.substr(0, 2));
            int d = stoi(date.substr(3, 2));
            int day = 0;
            for (int i = 0; i < m - 1; ++i) {
                day += months[i];
            }
            return day + d;
        };

        int startAlice = toDayOfYear(arriveAlice);
        int endAlice = toDayOfYear(leaveAlice);
        int startBob = toDayOfYear(arriveBob);
        int endBob = toDayOfYear(leaveBob);

        int start = max(startAlice, startBob);
        int end = min(endAlice, endBob);

        return max(0, end - start + 1);
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int countDaysTogether(String arriveAlice, String leaveAlice, String arriveBob, String leaveBob) {
        int[] months = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

        int startAlice = toDayOfYear(arriveAlice, months);
        int endAlice = toDayOfYear(leaveAlice, months);
        int startBob = toDayOfYear(arriveBob, months);
        int endBob = toDayOfYear(leaveBob, months);

        int start = Math.max(startAlice, startBob);
        int end = Math.min(endAlice, endBob);

        return Math.max(0, end - start + 1);
    }

    private int toDayOfYear(String date, int[] months) {
        int m = Integer.parseInt(date.substring(0, 2));
        int d = Integer.parseInt(date.substring(3, 5));
        int day = 0;
        for (int i = 0; i < m - 1; i++) {
            day += months[i];
        }
        return day + d;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def to_day_of_year(date):
            m, d = map(int, date.split('-'))
            return sum(months[:m-1]) + d

        start_alice = to_day_of_year(arriveAlice)
        end_alice = to_day_of_year(leaveAlice)
        start_bob = to_day_of_year(arriveBob)
        end_bob = to_day_of_year(leaveBob)

        start = max(start_alice, start_bob)
        end = min(end_alice, end_bob)

        return max(0, end - start + 1)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def to_day_of_year(date: str) -> int:
            m, d = map(int, date.split('-'))
            return sum(months[:m-1]) + d

        start_alice = to_day_of_year(arriveAlice)
        end_alice = to_day_of_year(leaveAlice)
        start_bob = to_day_of_year(arriveBob)
        end_bob = to_day_of_year(leaveBob)

        overlap_start = max(start_alice, start_bob)
        overlap_end = min(end_alice, end_bob)

        return max(0, overlap_end - overlap_start + 1)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int toDayOfYear(char* date, int* months) {
    int m = (date[0] - '0') * 10 + (date[1] - '0');
    int d = (date[3] - '0') * 10 + (date[4] - '0');
    int day = 0;
    for (int i = 0; i < m - 1; i++) {
        day += months[i];
    }
    return day + d;
}

int countDaysTogether(char* arriveAlice, char* leaveAlice, char* arriveBob, char* leaveBob) {
    int months[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

    int startAlice = toDayOfYear(arriveAlice, months);
    int endAlice = toDayOfYear(leaveAlice, months);
    int startBob = toDayOfYear(arriveBob, months);
    int endBob = toDayOfYear(leaveBob, months);

    int start = startAlice > startBob ? startAlice : startBob;
    int end = endAlice < endBob ? endAlice : endBob;

    int result = end - start + 1;
    return result > 0 ? result : 0;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int CountDaysTogether(string arriveAlice, string leaveAlice, string arriveBob, string leaveBob) {
        int[] months = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };

        int ToDayOfYear(string date) {
            int m = int.Parse(date.Substring(0, 2));
            int d = int.Parse(date.Substring(3, 2));
            int day = 0;
            for (int i = 0; i < m - 1; i++) {
                day += months[i];
            }
            return day + d;
        }

        int startAlice = ToDayOfYear(arriveAlice);
        int endAlice = ToDayOfYear(leaveAlice);
        int startBob = ToDayOfYear(arriveBob);
        int endBob = ToDayOfYear(leaveBob);

        int start = Math.Max(startAlice, startBob);
        int end = Math.Min(endAlice, endBob);

        return Math.Max(0, end - start + 1);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {string} arriveAlice
 * @param {string} leaveAlice
 * @param {string} arriveBob
 * @param {string} leaveBob
 * @return {number}
 */
var countDaysTogether = function(arriveAlice, leaveAlice, arriveBob, leaveBob) {
    const months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

    const toDayOfYear = (date) => {
        const [m, d] = date.split('-').map(Number);
        let day = 0;
        for (let i = 0; i < m - 1; i++) {
            day += months[i];
        }
        return day + d;
    };

    const startAlice = toDayOfYear(arriveAlice);
    const endAlice = toDayOfYear(leaveAlice);
    const startBob = toDayOfYear(arriveBob);
    const endBob = toDayOfYear(leaveBob);

    const start = Math.max(startAlice, startBob);
    const end = Math.min(endAlice, endBob);

    return Math.max(0, end - start + 1);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function countDaysTogether(arriveAlice: string, leaveAlice: string, arriveBob: string, leaveBob: string): number {
    const daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

    function getDayOfYear(dateStr: string): number {
        const parts = dateStr.split("-");
        const month = parseInt(parts[0], 10);
        const day = parseInt(parts[1], 10);
        let dayOfYear = 0;
        for (let i = 0; i < month - 1; i++) {
            dayOfYear += daysInMonth[i];
        }
        dayOfYear += day;
        return dayOfYear;
    }

    const startA = getDayOfYear(arriveAlice);
    const endA = getDayOfYear(leaveAlice);
    const startB = getDayOfYear(arriveBob);
    const endB = getDayOfYear(leaveBob);

    const overlapStart = Math.max(startA, startB);
    const overlapEnd = Math.min(endA, endB);

    const totalDays = overlapEnd - overlapStart + 1;
    return totalDays > 0 ? totalDays : 0;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param String $arriveAlice
     * @param String $leaveAlice
     * @param String $arriveBob
     * @param String $leaveBob
     * @return Integer
     */
    function countDaysTogether($arriveAlice, $leaveAlice, $arriveBob, $leaveBob) {
        $daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

        $getDayOfYear = function($dateStr) use ($daysInMonth) {
            $parts = explode("-", $dateStr);
            $month = intval($parts[0]);
            $day = intval($parts[1]);
            $dayOfYear = 0;
            for ($i = 0; $i < $month - 1; $i++) {
                $dayOfYear += $daysInMonth[$i];
            }
            $dayOfYear += $day;
            return $dayOfYear;
        };

        $startA = $getDayOfYear($arriveAlice);
        $endA = $getDayOfYear($leaveAlice);
        $startB = $getDayOfYear($arriveBob);
        $endB = $getDayOfYear($leaveBob);

        $overlapStart = max($startA, $startB);
        $overlapEnd = min($endA, $endB);

        $totalDays = $overlapEnd - $overlapStart + 1;
        return $totalDays > 0 ? $totalDays : 0;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func countDaysTogether(_ arriveAlice: String, _ leaveAlice: String, _ arriveBob: String, _ leaveBob: String) -> Int {
        let daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        func getDayOfYear(_ dateStr: String) -> Int {
            let parts = dateStr.split(separator: "-")
            guard parts.count == 2, let month = Int(parts[0]), let day = Int(parts[1]) else { return 0 }
            var dayOfYear = 0
            for i in 0..<(month - 1) {
                dayOfYear += daysInMonth[i]
            }
            dayOfYear += day
            return dayOfYear
        }

        let startA = getDayOfYear(arriveAlice)
        let endA = getDayOfYear(leaveAlice)
        let startB = getDayOfYear(arriveBob)
        let endB = getDayOfYear(leaveBob)

        let overlapStart = max(startA, startB)
        let overlapEnd = min(endA, endB)

        let totalDays = overlapEnd - overlapStart + 1
        return totalDays > 0 ? totalDays : 0
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun countDaysTogether(arriveAlice: String, leaveAlice: String, arriveBob: String, leaveBob: String): Int {
        val daysInMonth = intArrayOf(31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

        fun getDayOfYear(dateStr: String): Int {
            val parts = dateStr.split("-")
            val month = parts[0].toInt()
            val day = parts[1].toInt()
            var total = 0
            for (i in 0 until month - 1) {
                total += daysInMonth[i]
            }
            return total + day
        }

        val startA = getDayOfYear(arriveAlice)
        val endA = getDayOfYear(leaveAlice)
        val startB = getDayOfYear(arriveBob)
        val endB = getDayOfYear(leaveBob)

        val overlapStart = if (startA > startB) startA else startB
        val overlapEnd = if (endA < endB) endA else endB

        val totalDays = overlapEnd - overlapStart + 1
        return if (totalDays > 0) totalDays else 0
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int countDaysTogether(String arriveAlice, String leaveAlice, String arriveBob, String leaveBob) {
    final List<int> daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

    int getDayOfYear(String dateStr) {
      final List<String> parts = dateStr.split('-');
      final int month = int.parse(parts[0]);
      final int day = int.parse(parts[1]);
      int total = 0;
      for (int i = 0; i < month - 1; i++) {
        total += daysInMonth[i];
      }
      return total + day;
    }

    final int startA = getDayOfYear(arriveAlice);
    final int endA = getDayOfYear(leaveAlice);
    final int startB = getDayOfYear(arriveBob);
    final int endB = getDayOfYear(leaveBob);

    final int overlapStart = startA > startB ? startA : startB;
    final int overlapEnd = endA < endB ? endA : endB;

    final int totalDays = overlapEnd - overlapStart + 1;
    return totalDays > 0 ? totalDays : 0;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import (
    "strconv"
    "strings"
)

func countDaysTogether(arriveAlice string, leaveAlice string, arriveBob string, leaveBob string) int {
    daysInMonth := []int{31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}

    getDayOfYear := func(dateStr string) int {
        parts := strings.Split(dateStr, "-")
        month, _ := strconv.Atoi(parts[0])
        day, _ := strconv.Atoi(parts[1])
        total := 0
        for i := 0; i < month-1; i++ {
            total += daysInMonth[i]
        }
        return total + day
    }

    startA := getDayOfYear(arriveAlice)
    endA := getDayOfYear(leaveAlice)
    startB := getDayOfYear(arriveBob)
    endB := getDayOfYear(leaveBob)

    overlapStart := startA
    if startB > overlapStart {
        overlapStart = startB
    }

    overlapEnd := endA
    if endB < overlapEnd {
        overlapEnd = endB
    }

    totalDays := overlapEnd - overlapStart + 1
    if totalDays < 0 {
        return 0
    }
    return totalDays
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def count_days_together(arrive_alice, leave_alice, arrive_bob, leave_bob)
  start_a = to_day_of_year(arrive_alice)
  end_a = to_day_of_year(leave_alice)
  start_b = to_day_of_year(arrive_bob)
  end_b = to_day_of_year(leave_bob)

  overlap_start = [start_a, start_b].max
  overlap_end = [end_a, end_b].min

  [0, overlap_end - overlap_start + 1].max
end

def to_day_of_year(date)
  m, d = date.split('-').map(&:to_i)
  days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  days_in_month.first(m - 1).sum + d
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def countDaysTogether(arriveAlice: String, leaveAlice: String, arriveBob: String, leaveBob: String): Int = {
        def toDayOfYear(date: String): Int = {
            val parts = date.split("-")
            val m = parts(0).toInt
            val d = parts(1).toInt
            val daysInMonth = Array(31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
            daysInMonth.take(m - 1).sum + d
        }

        val startA = toDayOfYear(arriveAlice)
        val endA = toDayOfYear(leaveAlice)
        val startB = toDayOfYear(arriveBob)
        val endB = toDayOfYear(leaveBob)

        val overlapStart = math.max(startA, startB)
        val overlapEnd = math.min(endA, endB)

        math.max(0, overlapEnd - overlapStart + 1)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn count_days_together(arrive_alice: String, leave_alice: String, arrive_bob: String, leave_bob: String) -> i32 {
        fn to_day_of_year(date: &str) -> i32 {
            let m: usize = date[0..2].parse().unwrap();
            let d: i32 = date[3..5].parse().unwrap();
            let days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
            let sum_prev: i32 = days_in_month[0..m-1].iter().sum();
            sum_prev + d
        }

        let start_a = to_day_of_year(&arrive_alice);
        let end_a = to_day_of_year(&leave_alice);
        let start_b = to_day_of_year(&arrive_bob);
        let end_b = to_day_of_year(&leave_bob);

        let overlap_start = start_a.max(start_b);
        let overlap_end = end_a.min(end_b);

        (overlap_end - overlap_start + 1).max(0)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (count-days-together arriveAlice leaveAlice arriveBob leaveBob)
  (-> string? string? string? string? exact-integer?)
  (define (to-day-of-year date)
    (let ([m (string->number (substring date 0 2))]
          [d (string->number (substring date 3 5))]
          [days-in-month '(31 28 31 30 31 30 31 31 30 31 30 31)])
      (+ (for/sum ([dm days-in-month] [i (in-range (- m 1))]) dm) d)))
  (let ([startA (to-day-of-year arriveAlice)]
        [endA (to-day-of-year leaveAlice)]
        [startB (to-day-of-year arriveBob)]
        [endB (to-day-of-year leaveBob)])
    (max 0 (+ 1 (- (min endA endB) (max startA startB)))))
  )
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec count_days_together(ArriveAlice :: unicode:unicode_binary(), LeaveAlice :: unicode:unicode_binary(), ArriveBob :: unicode:unicode_binary(), LeaveBob :: unicode:unicode_binary()) -> integer().
count_days_together(ArriveAlice, LeaveAlice, ArriveBob, LeaveBob) ->
  StartA = to_day_of_year(ArriveAlice),
  EndA = to_day_of_year(LeaveAlice),
  StartB = to_day_of_year(ArriveBob),
  EndB = to_day_of_year(LeaveBob),
  OverlapStart = max(StartA, StartB),
  OverlapEnd = min(EndA, EndB),
  max(0, OverlapEnd - OverlapStart + 1).

to_day_of_year(Date) ->
  [MStr, DStr] = binary:split(Date, <<"-">>),
  M = binary_to_integer(MStr),
  D = binary_to_integer(DStr),
  DaysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
  lists:sum(lists:sublist(DaysInMonth, M - 1)) + D.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec count_days_together(arrive_alice :: String.t, leave_alice :: String.t, arrive_bob :: String.t, leave_bob :: String.t) :: integer
  def count_days_together(arrive_alice, leave_alice, arrive_bob, leave_bob) do
    start_a = to_day_of_year(arrive_alice)
    end_a = to_day_of_year(leave_alice)
    start_b = to_day_of_year(arrive_bob)
    end_b = to_day_of_year(leave_bob)

    overlap_start = max(start_a, start_b)
    overlap_end = min(end_a, end_b)

    max(0, overlap_end - overlap_start + 1)
  end

  defp to_day_of_year(date) do
    [m, d] = String.split(date, "-") |> Enum.map(&String.to_integer/1)
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    Enum.take(days_in_month, m - 1) |> Enum.sum() |> Kernel.+(d)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(1) with one-paragraph explanation
- **Space Complexity:** O(1) with one-paragraph explanation
