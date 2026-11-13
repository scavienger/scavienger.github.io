---
layout: post
title: "Count Zero Request Servers"
date: 2026-11-06 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Hash Table", "Sliding Window", "Sorting"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/count-zero-request-servers/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    vector<int> countServers(int n, vector<vector<int>>&\
        \ logs, int x, vector<int>& queries) {\n        sort(logs.begin(), logs.end(),\
        \ [](const auto& a, const auto& b) {\n            return a[1] < b[1];\n    \
        \    });\n        vector<pair<int, int>> orderedQueries;\n        for (int i\
        \ = 0; i < queries.size(); ++i) {\n            orderedQueries.emplace_back(queries[i],\
        \ i);\n        }\n        sort(orderedQueries.begin(), orderedQueries.end());\n\
        \n        vector<int> counts(n + 1, 0);\n        vector<int> answer(queries.size());\n\
        \        int left = 0;\n        int right = 0;\n        int activeServers =\
        \ 0;\n\n        for (const auto& [time, index] : orderedQueries) {\n       \
        \     while (right < logs.size() && logs[right][1] <= time) {\n            \
        \    int server = logs[right][0];\n                if (counts[server] == 0)\
        \ {\n                    ++activeServers;\n                }\n             \
        \   ++counts[server];\n                ++right;\n            }\n           \
        \ while (left < right && logs[left][1] < time - x) {\n                int server\
        \ = logs[left][0];\n                --counts[server];\n                if (counts[server]\
        \ == 0) {\n                    --activeServers;\n                }\n       \
        \         ++left;\n            }\n            answer[index] = n - activeServers;\n\
        \        }\n        return answer;\n    }\n};"
      java: "class Solution {\n    public int[] countServers(int n, int[][] logs, int\
        \ x, int[] queries) {\n        Arrays.sort(logs, (a, b) -> Integer.compare(a[1],\
        \ b[1]));\n        int[][] orderedQueries = new int[queries.length][2];\n  \
        \      for (int i = 0; i < queries.length; i++) {\n            orderedQueries[i][0]\
        \ = queries[i];\n            orderedQueries[i][1] = i;\n        }\n        Arrays.sort(orderedQueries,\
        \ (a, b) -> Integer.compare(a[0], b[0]));\n\n        int[] counts = new int[n\
        \ + 1];\n        int[] answer = new int[queries.length];\n        int left =\
        \ 0;\n        int right = 0;\n        int activeServers = 0;\n\n        for\
        \ (int[] query : orderedQueries) {\n            int time = query[0];\n     \
        \       while (right < logs.length && logs[right][1] <= time) {\n          \
        \      int server = logs[right][0];\n                if (counts[server] == 0)\
        \ {\n                    activeServers++;\n                }\n             \
        \   counts[server]++;\n                right++;\n            }\n           \
        \ while (left < right && logs[left][1] < time - x) {\n                int server\
        \ = logs[left][0];\n                counts[server]--;\n                if (counts[server]\
        \ == 0) {\n                    activeServers--;\n                }\n       \
        \         left++;\n            }\n            answer[query[1]] = n - activeServers;\n\
        \        }\n        return answer;\n    }\n}"
      python: "class Solution(object):\n    def countServers(self, n, logs, x, queries):\n\
        \        \"\"\"\n        :type n: int\n        :type logs: List[List[int]]\n\
        \        :type x: int\n        :type queries: List[int]\n        :rtype: List[int]\n\
        \        \"\"\"\n        logs.sort(key=lambda log: log[1])\n        ordered_queries\
        \ = sorted((time, index) for index, time in enumerate(queries))\n        counts\
        \ = [0] * (n + 1)\n        answer = [0] * len(queries)\n        left = 0\n \
        \       right = 0\n        active_servers = 0\n\n        for time, index in\
        \ ordered_queries:\n            while right < len(logs) and logs[right][1] <=\
        \ time:\n                server = logs[right][0]\n                if counts[server]\
        \ == 0:\n                    active_servers += 1\n                counts[server]\
        \ += 1\n                right += 1\n            while left < right and logs[left][1]\
        \ < time - x:\n                server = logs[left][0]\n                counts[server]\
        \ -= 1\n                if counts[server] == 0:\n                    active_servers\
        \ -= 1\n                left += 1\n            answer[index] = n - active_servers\n\
        \n        return answer"
      python3: "class Solution:\n    def countServers(self, n: int, logs: List[List[int]],\
        \ x: int, queries: List[int]) -> List[int]:\n        logs.sort(key=lambda log:\
        \ log[1])\n        ordered_queries = sorted((time, index) for index, time in\
        \ enumerate(queries))\n        counts = [0] * (n + 1)\n        answer = [0]\
        \ * len(queries)\n        left = 0\n        right = 0\n        active_servers\
        \ = 0\n\n        for time, index in ordered_queries:\n            while right\
        \ < len(logs) and logs[right][1] <= time:\n                server = logs[right][0]\n\
        \                if counts[server] == 0:\n                    active_servers\
        \ += 1\n                counts[server] += 1\n                right += 1\n  \
        \          while left < right and logs[left][1] < time - x:\n              \
        \  server = logs[left][0]\n                counts[server] -= 1\n           \
        \     if counts[server] == 0:\n                    active_servers -= 1\n   \
        \             left += 1\n            answer[index] = n - active_servers\n\n\
        \        return answer"
      c: "typedef struct {\n    int time;\n    int index;\n} Query;\n\nstatic int compareLogs(const\
        \ void* a, const void* b) {\n    const int* logA = *(const int**)a;\n    const\
        \ int* logB = *(const int**)b;\n    return (logA[1] > logB[1]) - (logA[1] <\
        \ logB[1]);\n}\n\nstatic int compareQueries(const void* a, const void* b) {\n\
        \    const Query* queryA = (const Query*)a;\n    const Query* queryB = (const\
        \ Query*)b;\n    if (queryA->time != queryB->time) {\n        return (queryA->time\
        \ > queryB->time) - (queryA->time < queryB->time);\n    }\n    return (queryA->index\
        \ > queryB->index) - (queryA->index < queryB->index);\n}\n\nint* countServers(int\
        \ n, int** logs, int logsSize, int* logsColSize, int x, int* queries, int queriesSize,\
        \ int* returnSize) {\n    qsort(logs, logsSize, sizeof(int*), compareLogs);\n\
        \    Query* orderedQueries = (Query*)malloc(sizeof(Query) * queriesSize);\n\
        \    int* counts = (int*)calloc(n + 1, sizeof(int));\n    int* answer = (int*)malloc(sizeof(int)\
        \ * queriesSize);\n\n    for (int i = 0; i < queriesSize; ++i) {\n        orderedQueries[i].time\
        \ = queries[i];\n        orderedQueries[i].index = i;\n    }\n    qsort(orderedQueries,\
        \ queriesSize, sizeof(Query), compareQueries);\n\n    int left = 0;\n    int\
        \ right = 0;\n    int activeServers = 0;\n\n    for (int i = 0; i < queriesSize;\
        \ ++i) {\n        int time = orderedQueries[i].time;\n        while (right <\
        \ logsSize && logs[right][1] <= time) {\n            int server = logs[right][0];\n\
        \            if (counts[server] == 0) {\n                ++activeServers;\n\
        \            }\n            ++counts[server];\n            ++right;\n      \
        \  }\n        while (left < right && logs[left][1] < time - x) {\n         \
        \   int server = logs[left][0];\n            --counts[server];\n           \
        \ if (counts[server] == 0) {\n                --activeServers;\n           \
        \ }\n            ++left;\n        }\n        answer[orderedQueries[i].index]\
        \ = n - activeServers;\n    }\n\n    free(orderedQueries);\n    free(counts);\n\
        \    *returnSize = queriesSize;\n    return answer;\n}"
      csharp: "public class Solution {\n    public int[] CountServers(int n, int[][]\
        \ logs, int x, int[] queries) {\n        Array.Sort(logs, (a, b) => a[1].CompareTo(b[1]));\n\
        \        var orderedQueries = new (int Time, int Index)[queries.Length];\n \
        \       for (int i = 0; i < queries.Length; i++) {\n            orderedQueries[i]\
        \ = (queries[i], i);\n        }\n        Array.Sort(orderedQueries, (a, b) =>\
        \ a.Time.CompareTo(b.Time));\n\n        int[] counts = new int[n + 1];\n   \
        \     int[] answer = new int[queries.Length];\n        int left = 0;\n     \
        \   int right = 0;\n        int activeServers = 0;\n\n        foreach (var query\
        \ in orderedQueries) {\n            while (right < logs.Length && logs[right][1]\
        \ <= query.Time) {\n                int server = logs[right][0];\n         \
        \       if (counts[server] == 0) {\n                    activeServers++;\n \
        \               }\n                counts[server]++;\n                right++;\n\
        \            }\n            while (left < right && logs[left][1] < query.Time\
        \ - x) {\n                int server = logs[left][0];\n                counts[server]--;\n\
        \                if (counts[server] == 0) {\n                    activeServers--;\n\
        \                }\n                left++;\n            }\n            answer[query.Index]\
        \ = n - activeServers;\n        }\n\n        return answer;\n    }\n}"
      javascript: "/**\n * @param {number} n\n * @param {number[][]} logs\n * @param\
        \ {number} x\n * @param {number[]} queries\n * @return {number[]}\n */\nvar\
        \ countServers = function(n, logs, x, queries) {\n    logs.sort((a, b) => a[1]\
        \ - b[1]);\n    const orderedQueries = queries.map((time, index) => [time, index]);\n\
        \    orderedQueries.sort((a, b) => a[0] - b[0]);\n\n    const counts = new Array(n\
        \ + 1).fill(0);\n    const answer = new Array(queries.length).fill(0);\n   \
        \ let left = 0;\n    let right = 0;\n    let activeServers = 0;\n\n    for (const\
        \ [time, index] of orderedQueries) {\n        while (right < logs.length &&\
        \ logs[right][1] <= time) {\n            const server = logs[right][0];\n  \
        \          if (counts[server] === 0) {\n                activeServers++;\n \
        \           }\n            counts[server]++;\n            right++;\n       \
        \ }\n        while (left < right && logs[left][1] < time - x) {\n          \
        \  const server = logs[left][0];\n            counts[server]--;\n          \
        \  if (counts[server] === 0) {\n                activeServers--;\n         \
        \   }\n            left++;\n        }\n        answer[index] = n - activeServers;\n\
        \    }\n\n    return answer;\n};"
      typescript: "function countServers(n: number, logs: number[][], x: number, queries:\
        \ number[]): number[] {\n    logs.sort((a, b) => a[1] - b[1]);\n    const orderedQueries\
        \ = queries.map((time, index) => [time, index]);\n    orderedQueries.sort((a,\
        \ b) => a[0] - b[0]);\n\n    const counts = new Array(n + 1).fill(0);\n    const\
        \ answer = new Array(queries.length).fill(0);\n    let left = 0;\n    let right\
        \ = 0;\n    let activeServers = 0;\n\n    for (const [time, index] of orderedQueries)\
        \ {\n        while (right < logs.length && logs[right][1] <= time) {\n     \
        \       const server = logs[right][0];\n            if (counts[server] === 0)\
        \ {\n                activeServers++;\n            }\n            counts[server]++;\n\
        \            right++;\n        }\n        while (left < right && logs[left][1]\
        \ < time - x) {\n            const server = logs[left][0];\n            counts[server]--;\n\
        \            if (counts[server] === 0) {\n                activeServers--;\n\
        \            }\n            left++;\n        }\n        answer[index] = n -\
        \ activeServers;\n    }\n\n    return answer;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer $n\n     * @param Integer[][]\
        \ $logs\n     * @param Integer $x\n     * @param Integer[] $queries\n     *\
        \ @return Integer[]\n     */\n    function countServers($n, $logs, $x, $queries)\
        \ {\n        usort($logs, function ($a, $b) {\n            return $a[1] <=>\
        \ $b[1];\n        });\n\n        $orderedQueries = [];\n        foreach ($queries\
        \ as $index => $time) {\n            $orderedQueries[] = [$time, $index];\n\
        \        }\n        usort($orderedQueries, function ($a, $b) {\n           \
        \ return $a[0] <=> $b[0];\n        });\n\n        $counts = array_fill(0, $n\
        \ + 1, 0);\n        $answer = array_fill(0, count($queries), 0);\n        $left\
        \ = 0;\n        $right = 0;\n        $activeServers = 0;\n        $logCount\
        \ = count($logs);\n\n        foreach ($orderedQueries as $query) {\n       \
        \     $time = $query[0];\n            $index = $query[1];\n\n            while\
        \ ($right < $logCount && $logs[$right][1] <= $time) {\n                $server\
        \ = $logs[$right][0];\n                if ($counts[$server] === 0) {\n     \
        \               $activeServers++;\n                }\n                $counts[$server]++;\n\
        \                $right++;\n            }\n            while ($left < $right\
        \ && $logs[$left][1] < $time - $x) {\n                $server = $logs[$left][0];\n\
        \                $counts[$server]--;\n                if ($counts[$server] ===\
        \ 0) {\n                    $activeServers--;\n                }\n         \
        \       $left++;\n            }\n            $answer[$index] = $n - $activeServers;\n\
        \        }\n\n        return $answer;\n    }\n}"
      swift: "class Solution {\n    func countServers(_ n: Int, _ logs: [[Int]], _ x:\
        \ Int, _ queries: [Int]) -> [Int] {\n        let sortedLogs = logs.sorted {\
        \ $0[1] < $1[1] }\n        let orderedQueries = queries.enumerated().map { ($0.element,\
        \ $0.offset) }.sorted { $0.0 < $1.0 }\n\n        var counts = Array(repeating:\
        \ 0, count: n + 1)\n        var answer = Array(repeating: 0, count: queries.count)\n\
        \        var left = 0\n        var right = 0\n        var activeServers = 0\n\
        \n        for (time, index) in orderedQueries {\n            while right < sortedLogs.count\
        \ && sortedLogs[right][1] <= time {\n                let server = sortedLogs[right][0]\n\
        \                if counts[server] == 0 {\n                    activeServers\
        \ += 1\n                }\n                counts[server] += 1\n           \
        \     right += 1\n            }\n            while left < right && sortedLogs[left][1]\
        \ < time - x {\n                let server = sortedLogs[left][0]\n         \
        \       counts[server] -= 1\n                if counts[server] == 0 {\n    \
        \                activeServers -= 1\n                }\n                left\
        \ += 1\n            }\n            answer[index] = n - activeServers\n     \
        \   }\n\n        return answer\n    }\n}"
      kotlin: "class Solution {\n    fun countServers(n: Int, logs: Array<IntArray>,\
        \ x: Int, queries: IntArray): IntArray {\n        logs.sortBy { it[1] }\n  \
        \      val orderedQueries = queries.indices\n            .map { intArrayOf(queries[it],\
        \ it) }\n            .sortedBy { it[0] }\n        val counts = IntArray(n +\
        \ 1)\n        val answer = IntArray(queries.size)\n        var left = 0\n  \
        \      var right = 0\n        var activeServers = 0\n\n        for (query in\
        \ orderedQueries) {\n            val time = query[0]\n            val index\
        \ = query[1]\n\n            while (right < logs.size && logs[right][1] <= time)\
        \ {\n                val server = logs[right][0]\n                if (counts[server]\
        \ == 0) activeServers++\n                counts[server]++\n                right++\n\
        \            }\n\n            while (left < right && logs[left][1] < time -\
        \ x) {\n                val server = logs[left][0]\n                counts[server]--\n\
        \                if (counts[server] == 0) activeServers--\n                left++\n\
        \            }\n\n            answer[index] = n - activeServers\n        }\n\
        \n        return answer\n    }\n}"
      dart: "class Solution {\n  List<int> countServers(int n, List<List<int>> logs,\
        \ int x, List<int> queries) {\n    logs.sort((a, b) => a[1].compareTo(b[1]));\n\
        \    final orderedQueries = List<List<int>>.generate(\n      queries.length,\n\
        \      (index) => [queries[index], index],\n    )..sort((a, b) => a[0].compareTo(b[0]));\n\
        \    final counts = List<int>.filled(n + 1, 0);\n    final answer = List<int>.filled(queries.length,\
        \ 0);\n    var left = 0;\n    var right = 0;\n    var activeServers = 0;\n\n\
        \    for (final query in orderedQueries) {\n      final time = query[0];\n \
        \     final index = query[1];\n\n      while (right < logs.length && logs[right][1]\
        \ <= time) {\n        final server = logs[right][0];\n        if (counts[server]\
        \ == 0) activeServers++;\n        counts[server]++;\n        right++;\n    \
        \  }\n\n      while (left < right && logs[left][1] < time - x) {\n        final\
        \ server = logs[left][0];\n        counts[server]--;\n        if (counts[server]\
        \ == 0) activeServers--;\n        left++;\n      }\n\n      answer[index] =\
        \ n - activeServers;\n    }\n\n    return answer;\n  }\n}"
      go: "import \"sort\"\n\nfunc countServers(n int, logs [][]int, x int, queries\
        \ []int) []int {\n\tsort.Slice(logs, func(i, j int) bool {\n\t\treturn logs[i][1]\
        \ < logs[j][1]\n\t})\n\n\ttype queryEntry struct {\n\t\ttime  int\n\t\tindex\
        \ int\n\t}\n\torderedQueries := make([]queryEntry, len(queries))\n\tfor i, time\
        \ := range queries {\n\t\torderedQueries[i] = queryEntry{time: time, index:\
        \ i}\n\t}\n\tsort.Slice(orderedQueries, func(i, j int) bool {\n\t\treturn orderedQueries[i].time\
        \ < orderedQueries[j].time\n\t})\n\n\tcounts := make([]int, n+1)\n\tanswer :=\
        \ make([]int, len(queries))\n\tleft, right := 0, 0\n\tactiveServers := 0\n\n\
        \tfor _, query := range orderedQueries {\n\t\tfor right < len(logs) && logs[right][1]\
        \ <= query.time {\n\t\t\tserver := logs[right][0]\n\t\t\tif counts[server] ==\
        \ 0 {\n\t\t\t\tactiveServers++\n\t\t\t}\n\t\t\tcounts[server]++\n\t\t\tright++\n\
        \t\t}\n\n\t\tfor left < right && logs[left][1] < query.time-x {\n\t\t\tserver\
        \ := logs[left][0]\n\t\t\tcounts[server]--\n\t\t\tif counts[server] == 0 {\n\
        \t\t\t\tactiveServers--\n\t\t\t}\n\t\t\tleft++\n\t\t}\n\n\t\tanswer[query.index]\
        \ = n - activeServers\n\t}\n\n\treturn answer\n}"
      ruby: "# @param {Integer} n\n# @param {Integer[][]} logs\n# @param {Integer} x\n\
        # @param {Integer[]} queries\n# @return {Integer[]}\ndef count_servers(n, logs,\
        \ x, queries)\n  logs.sort_by! { |log| log[1] }\n  ordered_queries = queries.each_with_index.map\
        \ { |time, index| [time, index] }\n  ordered_queries.sort_by! { |query| query[0]\
        \ }\n\n  counts = Array.new(n + 1, 0)\n  answer = Array.new(queries.length,\
        \ 0)\n  left = 0\n  right = 0\n  active_servers = 0\n\n  ordered_queries.each\
        \ do |time, index|\n    while right < logs.length && logs[right][1] <= time\n\
        \      server = logs[right][0]\n      active_servers += 1 if counts[server]\
        \ == 0\n      counts[server] += 1\n      right += 1\n    end\n\n    while left\
        \ < right && logs[left][1] < time - x\n      server = logs[left][0]\n      counts[server]\
        \ -= 1\n      active_servers -= 1 if counts[server] == 0\n      left += 1\n\
        \    end\n\n    answer[index] = n - active_servers\n  end\n\n  answer\nend"
      scala: "object Solution {\n    def countServers(n: Int, logs: Array[Array[Int]],\
        \ x: Int, queries: Array[Int]): Array[Int] = {\n        val sortedLogs = logs.sortBy(_(1))\n\
        \        val orderedQueries = queries.indices\n            .map(index => (queries(index),\
        \ index))\n            .sortBy(_._1)\n        val counts = Array.fill(n + 1)(0)\n\
        \        val answer = Array.fill(queries.length)(0)\n        var left = 0\n\
        \        var right = 0\n        var activeServers = 0\n\n        orderedQueries.foreach\
        \ { case (time, index) =>\n            while (right < sortedLogs.length && sortedLogs(right)(1)\
        \ <= time) {\n                val server = sortedLogs(right)(0)\n          \
        \      if (counts(server) == 0) activeServers += 1\n                counts(server)\
        \ += 1\n                right += 1\n            }\n\n            while (left\
        \ < right && sortedLogs(left)(1) < time - x) {\n                val server =\
        \ sortedLogs(left)(0)\n                counts(server) -= 1\n               \
        \ if (counts(server) == 0) activeServers -= 1\n                left += 1\n \
        \           }\n\n            answer(index) = n - activeServers\n        }\n\n\
        \        answer\n    }\n}"
      rust: "impl Solution {\n    pub fn count_servers(n: i32, logs: Vec<Vec<i32>>,\
        \ x: i32, queries: Vec<i32>) -> Vec<i32> {\n        let mut logs = logs;\n \
        \       logs.sort_by_key(|log| log[1]);\n\n        let mut ordered_queries:\
        \ Vec<(i32, usize)> = queries\n            .iter()\n            .enumerate()\n\
        \            .map(|(index, &time)| (time, index))\n            .collect();\n\
        \        ordered_queries.sort_unstable_by_key(|&(time, _)| time);\n\n      \
        \  let mut counts = vec![0; n as usize + 1];\n        let mut answer = vec![0;\
        \ queries.len()];\n        let mut left = 0;\n        let mut right = 0;\n \
        \       let mut active_servers = 0;\n\n        for (time, index) in ordered_queries\
        \ {\n            while right < logs.len() && logs[right][1] <= time {\n    \
        \            let server = logs[right][0] as usize;\n                if counts[server]\
        \ == 0 {\n                    active_servers += 1;\n                }\n    \
        \            counts[server] += 1;\n                right += 1;\n           \
        \ }\n\n            while left < right && logs[left][1] < time - x {\n      \
        \          let server = logs[left][0] as usize;\n                counts[server]\
        \ -= 1;\n                if counts[server] == 0 {\n                    active_servers\
        \ -= 1;\n                }\n                left += 1;\n            }\n\n  \
        \          answer[index] = n - active_servers;\n        }\n\n        answer\n\
        \    }\n}"
      racket: "(define/contract (count-servers n logs x queries)\n  (-> exact-integer?\
        \ (listof (listof exact-integer?)) exact-integer? (listof exact-integer?) (listof\
        \ exact-integer?))\n  (let* ([sorted-logs (sort logs < #:key cadr)]\n      \
        \   [ordered-queries (sort (for/list ([time queries] [index (in-naturals)])\n\
        \                                  (cons time index))\n                    \
        \            <\n                                #:key car)]\n         [counts\
        \ (make-vector (add1 n) 0)]\n         [answer (make-vector (length queries)\
        \ 0)])\n    (let loop ([remaining-queries ordered-queries]\n               [remaining-logs\
        \ sorted-logs]\n               [active-servers 0])\n      (if (null? remaining-queries)\n\
        \          (vector->list answer)\n          (let* ([query (car remaining-queries)]\n\
        \                 [time (car query)]\n                 [index (cdr query)])\n\
        \            (define-values (logs-after-add active-after-add)\n            \
        \  (let add-loop ([logs-to-add remaining-logs]\n                           \
        \  [active active-servers])\n                (if (and (pair? logs-to-add) (<=\
        \ (cadar logs-to-add) time))\n                    (let* ([log (car logs-to-add)]\n\
        \                           [server (car log)])\n                      (when\
        \ (= (vector-ref counts server) 0)\n                        (set! active (add1\
        \ active)))\n                      (vector-set! counts server (add1 (vector-ref\
        \ counts server)))\n                      (add-loop (cdr logs-to-add) active))\n\
        \                    (values logs-to-add active))))\n            (define-values\
        \ (logs-after-remove active-after-remove)\n              (let remove-loop ([logs-to-remove\
        \ sorted-logs]\n                                [logs-remaining logs-after-add]\n\
        \                                [active active-after-add])\n              \
        \  (if (and (pair? logs-to-remove)\n                         (not (eq? logs-to-remove\
        \ logs-remaining))\n                         (< (cadar logs-to-remove) (- time\
        \ x)))\n                    (let* ([log (car logs-to-remove)]\n            \
        \               [server (car log)])\n                      (vector-set! counts\
        \ server (sub1 (vector-ref counts server)))\n                      (when (=\
        \ (vector-ref counts server) 0)\n                        (set! active (sub1\
        \ active)))\n                      (remove-loop (cdr logs-to-remove) logs-remaining\
        \ active))\n                    (values logs-to-remove active))))\n        \
        \    (vector-set! answer index (- n active-after-remove))\n            (loop\
        \ (cdr remaining-queries) logs-after-add active-after-add))))))"
      erlang: "-spec count_servers(N :: integer(), Logs :: [[integer()]], X :: integer(),\
        \ Queries :: [integer()]) -> [integer()].\ncount_servers(N, Logs, X, Queries)\
        \ ->\n    SortedLogs = lists:sort(fun([_, T1], [_, T2]) -> T1 =< T2 end, Logs),\n\
        \    OrderedQueries = lists:sort(fun({T1, _}, {T2, _}) -> T1 =< T2 end,\n  \
        \                              lists:zip(Queries, lists:seq(0, length(Queries)\
        \ - 1))),\n    Counts = array:new(N + 1, {default, 0}),\n    Answer = array:new(length(Queries),\
        \ {default, 0}),\n    {_, _, _, Result} = lists:foldl(\n        fun({Time, Index},\
        \ {RemainingLogs, LeftLogs, Active, Answers}) ->\n            {LogsAfterAdd,\
        \ ActiveAfterAdd, AddedLogs} = add_logs(RemainingLogs, Time, Counts, Active,\
        \ []),\n            {LeftAfterRemove, ActiveAfterRemove} = remove_logs(LeftLogs\
        \ ++ AddedLogs, Time - X, Counts, ActiveAfterAdd),\n            {LogsAfterAdd,\
        \ LeftAfterRemove, ActiveAfterRemove,\n             array:set(Index, N - ActiveAfterRemove,\
        \ Answers)}\n        end,\n        {SortedLogs, [], 0, Answer},\n        OrderedQueries),\n\
        \    [array:get(I, Result) || I <- lists:seq(0, length(Queries) - 1)].\n\nadd_logs([[Server,\
        \ Time] = Log | Rest], Limit, Counts, Active, Added) when Time =< Limit ->\n\
        \    Count = array:get(Server, Counts),\n    NewCounts = array:set(Server, Count\
        \ + 1, Counts),\n    NewActive = if Count =:= 0 -> Active + 1; true -> Active\
        \ end,\n    add_logs(Rest, Limit, NewCounts, NewActive, [Log | Added]);\nadd_logs(Rest,\
        \ _Limit, _Counts, Active, Added) ->\n    {Rest, Active, lists:reverse(Added)}.\n\
        \nremove_logs([[Server, Time] | Rest], LowerBound, Counts, Active) when Time\
        \ < LowerBound ->\n    Count = array:get(Server, Counts) - 1,\n    NewCounts\
        \ = array:set(Server, Count, Counts),\n    NewActive = if Count =:= 0 -> Active\
        \ - 1; true -> Active end,\n    remove_logs(Rest, LowerBound, NewCounts, NewActive);\n\
        remove_logs(Logs, _LowerBound, _Counts, Active) ->\n    {Logs, Active}."
      elixir: "defmodule Solution do\n  @spec count_servers(n :: integer, logs :: [[integer]],\
        \ x :: integer, queries :: [integer]) :: [integer]\n  def count_servers(n, logs,\
        \ x, queries) do\n    sorted_logs = Enum.sort_by(logs, fn [_, time] -> time\
        \ end)\n\n    ordered_queries =\n      queries\n      |> Enum.with_index()\n\
        \      |> Enum.sort_by(fn {time, _index} -> time end)\n\n    counts = :array.new(n\
        \ + 1, default: 0)\n    answer = :array.new(length(queries), default: 0)\n\n\
        \    {_, _, _, result} =\n      Enum.reduce(ordered_queries, {sorted_logs, [],\
        \ 0, answer}, fn {time, index},\n                                          \
        \                         {remaining_logs, active_logs, active_servers, answers}\
        \ ->\n        {logs_after_add, active_after_add, added_logs, counts_after_add}\
        \ =\n          add_logs(remaining_logs, time, counts, active_servers, [])\n\n\
        \        {active_logs_after_remove, active_after_remove, counts_after_remove}\
        \ =\n          remove_logs(active_logs ++ added_logs, time - x, counts_after_add,\
        \ active_after_add)\n\n        updated_answers = :array.set(index, n - active_after_remove,\
        \ answers)\n\n        {logs_after_add, active_logs_after_remove, active_after_remove,\
        \ updated_answers,\n         counts_after_remove}\n      end)\n      |> then(fn\
        \ {remaining, active, servers, answers, _counts} ->\n        {remaining, active,\
        \ servers, answers}\n      end)\n\n    Enum.map(0..(length(queries) - 1), fn\
        \ index -> :array.get(index, result) end)\n  end\n\n  defp add_logs([[server,\
        \ time] = log | rest], limit, counts, active_servers, added_logs)\n       when\
        \ time <= limit do\n    count = :array.get(server, counts)\n    updated_counts\
        \ = :array.set(server, count + 1, counts)\n    updated_active = if count ==\
        \ 0, do: active_servers + 1, else: active_servers\n    add_logs(rest, limit,\
        \ updated_counts, updated_active, [log | added_logs])\n  end\n\n  defp add_logs(remaining_logs,\
        \ _limit, counts, active_servers, added_logs) do\n    {remaining_logs, active_servers,\
        \ Enum.reverse(added_logs), counts}\n  end\n\n  defp remove_logs([[server, time]\
        \ | rest], lower_bound, counts, active_servers)\n       when time < lower_bound\
        \ do\n    count = :array.get(server, counts) - 1\n    updated_counts = :array.set(server,\
        \ count, counts)\n    updated_active = if count == 0, do: active_servers - 1,\
        \ else: active_servers\n    remove_logs(rest, lower_bound, updated_counts, updated_active)\n\
        \  end\n\n  defp remove_logs(active_logs, _lower_bound, counts, active_servers)\
        \ do\n    {active_logs, active_servers, counts}\n  end\nend"
    approach: 'Sort the logs by time and sort the queries while keeping their original
      indices. Sweep through the queries in increasing order, adding logs whose times
      are at most the query time and removing logs that are earlier than query time
      minus x. Track each server''s number of logs in the active interval and how many
      servers currently have at least one log.


      For each query, the answer is n minus the number of active servers. The interval
      bounds are inclusive: add logs at the query time and remove logs strictly earlier
      than query time minus x. Store each result at its original query index.'
    time_complexity: O((L + Q) log(L + Q)), where L is the number of logs and Q is the
      number of queries, due to sorting.
    space_complexity: O(L + Q + n) for sorted data, query indices, and per-server request
      counts.
    elapsed_time: 152.33096575737
    model: gpt-6-luna
    generated_at: '2026-11-12 23:39:25 '
---

## Problem #2747: Count Zero Request Servers

**Difficulty:** Medium

**Topics:** Array, Hash Table, Sliding Window, Sorting

## Problem Description

<p>You are given an integer <code>n</code> denoting the total number of servers and a <strong>2D</strong> <strong>0-indexed </strong>integer array <code>logs</code>, where <code>logs[i] = [server_id, time]</code> denotes that the server with id <code>server_id</code> received a request at time <code>time</code>.</p>

<p>You are also given an integer <code>x</code> and a <strong>0-indexed</strong> integer array <code>queries</code>.</p>

<p>Return <em>a <strong>0-indexed</strong> integer array</em> <code>arr</code> <em>of length</em> <code>queries.length</code> <em>where</em> <code>arr[i]</code> <em>represents the number of servers that <strong>did not receive</strong> any requests during the time interval</em> <code>[queries[i] - x, queries[i]]</code>.</p>

<p>Note that the time intervals are inclusive.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 3, logs = [[1,3],[2,6],[1,5]], x = 5, queries = [10,11]
<strong>Output:</strong> [1,2]
<strong>Explanation:</strong> 
For queries[0]: The servers with ids 1 and 2 get requests in the duration of [5, 10]. Hence, only server 3 gets zero requests.
For queries[1]: Only the server with id 2 gets a request in duration of [6,11]. Hence, the servers with ids 1 and 3 are the only servers that do not receive any requests during that time period.

</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 3, logs = [[2,4],[2,1],[1,2],[3,1]], x = 2, queries = [3,4]
<strong>Output:</strong> [0,1]
<strong>Explanation:</strong> 
For queries[0]: All servers get at least one request in the duration of [1, 3].
For queries[1]: Only server with id 3 gets no request in the duration [2,4].

</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= logs.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= queries.length &lt;= 10<sup>5</sup></code></li>
	<li><code><font face="monospace">logs[i].length == 2</font></code></li>
	<li><code>1 &lt;= logs[i][0] &lt;= n</code></li>
	<li><code>1 &lt;= logs[i][1] &lt;= 10<sup>6</sup></code></li>
	<li><code>1 &lt;= x &lt;= 10<sup>5</sup></code></li>
	<li><code>x &lt;&nbsp;queries[i]&nbsp;&lt;= 10<sup>6</sup></code></li>
</ul>


## Hints

1. Can we use sorting and two-pointer approach here?

2. Sort the queries array and logs array based on time in increasing order.

3. For every window of size x, use sliding window and two-pointer approach to find the answer to the queries.

## 🤖 AI-Generated Solution (gpt-6-luna)

### Approach

Sort the logs by time and sort the queries while keeping their original indices. Sweep through the queries in increasing order, adding logs whose times are at most the query time and removing logs that are earlier than query time minus x. Track each server's number of logs in the active interval and how many servers currently have at least one log.

For each query, the answer is n minus the number of active servers. The interval bounds are inclusive: add logs at the query time and remove logs strictly earlier than query time minus x. Store each result at its original query index.

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
    vector<int> countServers(int n, vector<vector<int>>& logs, int x, vector<int>& queries) {
        sort(logs.begin(), logs.end(), [](const auto& a, const auto& b) {
            return a[1] < b[1];
        });
        vector<pair<int, int>> orderedQueries;
        for (int i = 0; i < queries.size(); ++i) {
            orderedQueries.emplace_back(queries[i], i);
        }
        sort(orderedQueries.begin(), orderedQueries.end());

        vector<int> counts(n + 1, 0);
        vector<int> answer(queries.size());
        int left = 0;
        int right = 0;
        int activeServers = 0;

        for (const auto& [time, index] : orderedQueries) {
            while (right < logs.size() && logs[right][1] <= time) {
                int server = logs[right][0];
                if (counts[server] == 0) {
                    ++activeServers;
                }
                ++counts[server];
                ++right;
            }
            while (left < right && logs[left][1] < time - x) {
                int server = logs[left][0];
                --counts[server];
                if (counts[server] == 0) {
                    --activeServers;
                }
                ++left;
            }
            answer[index] = n - activeServers;
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
    public int[] countServers(int n, int[][] logs, int x, int[] queries) {
        Arrays.sort(logs, (a, b) -> Integer.compare(a[1], b[1]));
        int[][] orderedQueries = new int[queries.length][2];
        for (int i = 0; i < queries.length; i++) {
            orderedQueries[i][0] = queries[i];
            orderedQueries[i][1] = i;
        }
        Arrays.sort(orderedQueries, (a, b) -> Integer.compare(a[0], b[0]));

        int[] counts = new int[n + 1];
        int[] answer = new int[queries.length];
        int left = 0;
        int right = 0;
        int activeServers = 0;

        for (int[] query : orderedQueries) {
            int time = query[0];
            while (right < logs.length && logs[right][1] <= time) {
                int server = logs[right][0];
                if (counts[server] == 0) {
                    activeServers++;
                }
                counts[server]++;
                right++;
            }
            while (left < right && logs[left][1] < time - x) {
                int server = logs[left][0];
                counts[server]--;
                if (counts[server] == 0) {
                    activeServers--;
                }
                left++;
            }
            answer[query[1]] = n - activeServers;
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
    def countServers(self, n, logs, x, queries):
        """
        :type n: int
        :type logs: List[List[int]]
        :type x: int
        :type queries: List[int]
        :rtype: List[int]
        """
        logs.sort(key=lambda log: log[1])
        ordered_queries = sorted((time, index) for index, time in enumerate(queries))
        counts = [0] * (n + 1)
        answer = [0] * len(queries)
        left = 0
        right = 0
        active_servers = 0

        for time, index in ordered_queries:
            while right < len(logs) and logs[right][1] <= time:
                server = logs[right][0]
                if counts[server] == 0:
                    active_servers += 1
                counts[server] += 1
                right += 1
            while left < right and logs[left][1] < time - x:
                server = logs[left][0]
                counts[server] -= 1
                if counts[server] == 0:
                    active_servers -= 1
                left += 1
            answer[index] = n - active_servers

        return answer
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda log: log[1])
        ordered_queries = sorted((time, index) for index, time in enumerate(queries))
        counts = [0] * (n + 1)
        answer = [0] * len(queries)
        left = 0
        right = 0
        active_servers = 0

        for time, index in ordered_queries:
            while right < len(logs) and logs[right][1] <= time:
                server = logs[right][0]
                if counts[server] == 0:
                    active_servers += 1
                counts[server] += 1
                right += 1
            while left < right and logs[left][1] < time - x:
                server = logs[left][0]
                counts[server] -= 1
                if counts[server] == 0:
                    active_servers -= 1
                left += 1
            answer[index] = n - active_servers

        return answer
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
typedef struct {
    int time;
    int index;
} Query;

static int compareLogs(const void* a, const void* b) {
    const int* logA = *(const int**)a;
    const int* logB = *(const int**)b;
    return (logA[1] > logB[1]) - (logA[1] < logB[1]);
}

static int compareQueries(const void* a, const void* b) {
    const Query* queryA = (const Query*)a;
    const Query* queryB = (const Query*)b;
    if (queryA->time != queryB->time) {
        return (queryA->time > queryB->time) - (queryA->time < queryB->time);
    }
    return (queryA->index > queryB->index) - (queryA->index < queryB->index);
}

int* countServers(int n, int** logs, int logsSize, int* logsColSize, int x, int* queries, int queriesSize, int* returnSize) {
    qsort(logs, logsSize, sizeof(int*), compareLogs);
    Query* orderedQueries = (Query*)malloc(sizeof(Query) * queriesSize);
    int* counts = (int*)calloc(n + 1, sizeof(int));
    int* answer = (int*)malloc(sizeof(int) * queriesSize);

    for (int i = 0; i < queriesSize; ++i) {
        orderedQueries[i].time = queries[i];
        orderedQueries[i].index = i;
    }
    qsort(orderedQueries, queriesSize, sizeof(Query), compareQueries);

    int left = 0;
    int right = 0;
    int activeServers = 0;

    for (int i = 0; i < queriesSize; ++i) {
        int time = orderedQueries[i].time;
        while (right < logsSize && logs[right][1] <= time) {
            int server = logs[right][0];
            if (counts[server] == 0) {
                ++activeServers;
            }
            ++counts[server];
            ++right;
        }
        while (left < right && logs[left][1] < time - x) {
            int server = logs[left][0];
            --counts[server];
            if (counts[server] == 0) {
                --activeServers;
            }
            ++left;
        }
        answer[orderedQueries[i].index] = n - activeServers;
    }

    free(orderedQueries);
    free(counts);
    *returnSize = queriesSize;
    return answer;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int[] CountServers(int n, int[][] logs, int x, int[] queries) {
        Array.Sort(logs, (a, b) => a[1].CompareTo(b[1]));
        var orderedQueries = new (int Time, int Index)[queries.Length];
        for (int i = 0; i < queries.Length; i++) {
            orderedQueries[i] = (queries[i], i);
        }
        Array.Sort(orderedQueries, (a, b) => a.Time.CompareTo(b.Time));

        int[] counts = new int[n + 1];
        int[] answer = new int[queries.Length];
        int left = 0;
        int right = 0;
        int activeServers = 0;

        foreach (var query in orderedQueries) {
            while (right < logs.Length && logs[right][1] <= query.Time) {
                int server = logs[right][0];
                if (counts[server] == 0) {
                    activeServers++;
                }
                counts[server]++;
                right++;
            }
            while (left < right && logs[left][1] < query.Time - x) {
                int server = logs[left][0];
                counts[server]--;
                if (counts[server] == 0) {
                    activeServers--;
                }
                left++;
            }
            answer[query.Index] = n - activeServers;
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
 * @param {number} n
 * @param {number[][]} logs
 * @param {number} x
 * @param {number[]} queries
 * @return {number[]}
 */
var countServers = function(n, logs, x, queries) {
    logs.sort((a, b) => a[1] - b[1]);
    const orderedQueries = queries.map((time, index) => [time, index]);
    orderedQueries.sort((a, b) => a[0] - b[0]);

    const counts = new Array(n + 1).fill(0);
    const answer = new Array(queries.length).fill(0);
    let left = 0;
    let right = 0;
    let activeServers = 0;

    for (const [time, index] of orderedQueries) {
        while (right < logs.length && logs[right][1] <= time) {
            const server = logs[right][0];
            if (counts[server] === 0) {
                activeServers++;
            }
            counts[server]++;
            right++;
        }
        while (left < right && logs[left][1] < time - x) {
            const server = logs[left][0];
            counts[server]--;
            if (counts[server] === 0) {
                activeServers--;
            }
            left++;
        }
        answer[index] = n - activeServers;
    }

    return answer;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function countServers(n: number, logs: number[][], x: number, queries: number[]): number[] {
    logs.sort((a, b) => a[1] - b[1]);
    const orderedQueries = queries.map((time, index) => [time, index]);
    orderedQueries.sort((a, b) => a[0] - b[0]);

    const counts = new Array(n + 1).fill(0);
    const answer = new Array(queries.length).fill(0);
    let left = 0;
    let right = 0;
    let activeServers = 0;

    for (const [time, index] of orderedQueries) {
        while (right < logs.length && logs[right][1] <= time) {
            const server = logs[right][0];
            if (counts[server] === 0) {
                activeServers++;
            }
            counts[server]++;
            right++;
        }
        while (left < right && logs[left][1] < time - x) {
            const server = logs[left][0];
            counts[server]--;
            if (counts[server] === 0) {
                activeServers--;
            }
            left++;
        }
        answer[index] = n - activeServers;
    }

    return answer;
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
     * @param Integer[][] $logs
     * @param Integer $x
     * @param Integer[] $queries
     * @return Integer[]
     */
    function countServers($n, $logs, $x, $queries) {
        usort($logs, function ($a, $b) {
            return $a[1] <=> $b[1];
        });

        $orderedQueries = [];
        foreach ($queries as $index => $time) {
            $orderedQueries[] = [$time, $index];
        }
        usort($orderedQueries, function ($a, $b) {
            return $a[0] <=> $b[0];
        });

        $counts = array_fill(0, $n + 1, 0);
        $answer = array_fill(0, count($queries), 0);
        $left = 0;
        $right = 0;
        $activeServers = 0;
        $logCount = count($logs);

        foreach ($orderedQueries as $query) {
            $time = $query[0];
            $index = $query[1];

            while ($right < $logCount && $logs[$right][1] <= $time) {
                $server = $logs[$right][0];
                if ($counts[$server] === 0) {
                    $activeServers++;
                }
                $counts[$server]++;
                $right++;
            }
            while ($left < $right && $logs[$left][1] < $time - $x) {
                $server = $logs[$left][0];
                $counts[$server]--;
                if ($counts[$server] === 0) {
                    $activeServers--;
                }
                $left++;
            }
            $answer[$index] = $n - $activeServers;
        }

        return $answer;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func countServers(_ n: Int, _ logs: [[Int]], _ x: Int, _ queries: [Int]) -> [Int] {
        let sortedLogs = logs.sorted { $0[1] < $1[1] }
        let orderedQueries = queries.enumerated().map { ($0.element, $0.offset) }.sorted { $0.0 < $1.0 }

        var counts = Array(repeating: 0, count: n + 1)
        var answer = Array(repeating: 0, count: queries.count)
        var left = 0
        var right = 0
        var activeServers = 0

        for (time, index) in orderedQueries {
            while right < sortedLogs.count && sortedLogs[right][1] <= time {
                let server = sortedLogs[right][0]
                if counts[server] == 0 {
                    activeServers += 1
                }
                counts[server] += 1
                right += 1
            }
            while left < right && sortedLogs[left][1] < time - x {
                let server = sortedLogs[left][0]
                counts[server] -= 1
                if counts[server] == 0 {
                    activeServers -= 1
                }
                left += 1
            }
            answer[index] = n - activeServers
        }

        return answer
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun countServers(n: Int, logs: Array<IntArray>, x: Int, queries: IntArray): IntArray {
        logs.sortBy { it[1] }
        val orderedQueries = queries.indices
            .map { intArrayOf(queries[it], it) }
            .sortedBy { it[0] }
        val counts = IntArray(n + 1)
        val answer = IntArray(queries.size)
        var left = 0
        var right = 0
        var activeServers = 0

        for (query in orderedQueries) {
            val time = query[0]
            val index = query[1]

            while (right < logs.size && logs[right][1] <= time) {
                val server = logs[right][0]
                if (counts[server] == 0) activeServers++
                counts[server]++
                right++
            }

            while (left < right && logs[left][1] < time - x) {
                val server = logs[left][0]
                counts[server]--
                if (counts[server] == 0) activeServers--
                left++
            }

            answer[index] = n - activeServers
        }

        return answer
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  List<int> countServers(int n, List<List<int>> logs, int x, List<int> queries) {
    logs.sort((a, b) => a[1].compareTo(b[1]));
    final orderedQueries = List<List<int>>.generate(
      queries.length,
      (index) => [queries[index], index],
    )..sort((a, b) => a[0].compareTo(b[0]));
    final counts = List<int>.filled(n + 1, 0);
    final answer = List<int>.filled(queries.length, 0);
    var left = 0;
    var right = 0;
    var activeServers = 0;

    for (final query in orderedQueries) {
      final time = query[0];
      final index = query[1];

      while (right < logs.length && logs[right][1] <= time) {
        final server = logs[right][0];
        if (counts[server] == 0) activeServers++;
        counts[server]++;
        right++;
      }

      while (left < right && logs[left][1] < time - x) {
        final server = logs[left][0];
        counts[server]--;
        if (counts[server] == 0) activeServers--;
        left++;
      }

      answer[index] = n - activeServers;
    }

    return answer;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import "sort"

func countServers(n int, logs [][]int, x int, queries []int) []int {
	sort.Slice(logs, func(i, j int) bool {
		return logs[i][1] < logs[j][1]
	})

	type queryEntry struct {
		time  int
		index int
	}
	orderedQueries := make([]queryEntry, len(queries))
	for i, time := range queries {
		orderedQueries[i] = queryEntry{time: time, index: i}
	}
	sort.Slice(orderedQueries, func(i, j int) bool {
		return orderedQueries[i].time < orderedQueries[j].time
	})

	counts := make([]int, n+1)
	answer := make([]int, len(queries))
	left, right := 0, 0
	activeServers := 0

	for _, query := range orderedQueries {
		for right < len(logs) && logs[right][1] <= query.time {
			server := logs[right][0]
			if counts[server] == 0 {
				activeServers++
			}
			counts[server]++
			right++
		}

		for left < right && logs[left][1] < query.time-x {
			server := logs[left][0]
			counts[server]--
			if counts[server] == 0 {
				activeServers--
			}
			left++
		}

		answer[query.index] = n - activeServers
	}

	return answer
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer} n
# @param {Integer[][]} logs
# @param {Integer} x
# @param {Integer[]} queries
# @return {Integer[]}
def count_servers(n, logs, x, queries)
  logs.sort_by! { |log| log[1] }
  ordered_queries = queries.each_with_index.map { |time, index| [time, index] }
  ordered_queries.sort_by! { |query| query[0] }

  counts = Array.new(n + 1, 0)
  answer = Array.new(queries.length, 0)
  left = 0
  right = 0
  active_servers = 0

  ordered_queries.each do |time, index|
    while right < logs.length && logs[right][1] <= time
      server = logs[right][0]
      active_servers += 1 if counts[server] == 0
      counts[server] += 1
      right += 1
    end

    while left < right && logs[left][1] < time - x
      server = logs[left][0]
      counts[server] -= 1
      active_servers -= 1 if counts[server] == 0
      left += 1
    end

    answer[index] = n - active_servers
  end

  answer
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def countServers(n: Int, logs: Array[Array[Int]], x: Int, queries: Array[Int]): Array[Int] = {
        val sortedLogs = logs.sortBy(_(1))
        val orderedQueries = queries.indices
            .map(index => (queries(index), index))
            .sortBy(_._1)
        val counts = Array.fill(n + 1)(0)
        val answer = Array.fill(queries.length)(0)
        var left = 0
        var right = 0
        var activeServers = 0

        orderedQueries.foreach { case (time, index) =>
            while (right < sortedLogs.length && sortedLogs(right)(1) <= time) {
                val server = sortedLogs(right)(0)
                if (counts(server) == 0) activeServers += 1
                counts(server) += 1
                right += 1
            }

            while (left < right && sortedLogs(left)(1) < time - x) {
                val server = sortedLogs(left)(0)
                counts(server) -= 1
                if (counts(server) == 0) activeServers -= 1
                left += 1
            }

            answer(index) = n - activeServers
        }

        answer
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn count_servers(n: i32, logs: Vec<Vec<i32>>, x: i32, queries: Vec<i32>) -> Vec<i32> {
        let mut logs = logs;
        logs.sort_by_key(|log| log[1]);

        let mut ordered_queries: Vec<(i32, usize)> = queries
            .iter()
            .enumerate()
            .map(|(index, &time)| (time, index))
            .collect();
        ordered_queries.sort_unstable_by_key(|&(time, _)| time);

        let mut counts = vec![0; n as usize + 1];
        let mut answer = vec![0; queries.len()];
        let mut left = 0;
        let mut right = 0;
        let mut active_servers = 0;

        for (time, index) in ordered_queries {
            while right < logs.len() && logs[right][1] <= time {
                let server = logs[right][0] as usize;
                if counts[server] == 0 {
                    active_servers += 1;
                }
                counts[server] += 1;
                right += 1;
            }

            while left < right && logs[left][1] < time - x {
                let server = logs[left][0] as usize;
                counts[server] -= 1;
                if counts[server] == 0 {
                    active_servers -= 1;
                }
                left += 1;
            }

            answer[index] = n - active_servers;
        }

        answer
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (count-servers n logs x queries)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer? (listof exact-integer?) (listof exact-integer?))
  (let* ([sorted-logs (sort logs < #:key cadr)]
         [ordered-queries (sort (for/list ([time queries] [index (in-naturals)])
                                  (cons time index))
                                <
                                #:key car)]
         [counts (make-vector (add1 n) 0)]
         [answer (make-vector (length queries) 0)])
    (let loop ([remaining-queries ordered-queries]
               [remaining-logs sorted-logs]
               [active-servers 0])
      (if (null? remaining-queries)
          (vector->list answer)
          (let* ([query (car remaining-queries)]
                 [time (car query)]
                 [index (cdr query)])
            (define-values (logs-after-add active-after-add)
              (let add-loop ([logs-to-add remaining-logs]
                             [active active-servers])
                (if (and (pair? logs-to-add) (<= (cadar logs-to-add) time))
                    (let* ([log (car logs-to-add)]
                           [server (car log)])
                      (when (= (vector-ref counts server) 0)
                        (set! active (add1 active)))
                      (vector-set! counts server (add1 (vector-ref counts server)))
                      (add-loop (cdr logs-to-add) active))
                    (values logs-to-add active))))
            (define-values (logs-after-remove active-after-remove)
              (let remove-loop ([logs-to-remove sorted-logs]
                                [logs-remaining logs-after-add]
                                [active active-after-add])
                (if (and (pair? logs-to-remove)
                         (not (eq? logs-to-remove logs-remaining))
                         (< (cadar logs-to-remove) (- time x)))
                    (let* ([log (car logs-to-remove)]
                           [server (car log)])
                      (vector-set! counts server (sub1 (vector-ref counts server)))
                      (when (= (vector-ref counts server) 0)
                        (set! active (sub1 active)))
                      (remove-loop (cdr logs-to-remove) logs-remaining active))
                    (values logs-to-remove active))))
            (vector-set! answer index (- n active-after-remove))
            (loop (cdr remaining-queries) logs-after-add active-after-add))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec count_servers(N :: integer(), Logs :: [[integer()]], X :: integer(), Queries :: [integer()]) -> [integer()].
count_servers(N, Logs, X, Queries) ->
    SortedLogs = lists:sort(fun([_, T1], [_, T2]) -> T1 =< T2 end, Logs),
    OrderedQueries = lists:sort(fun({T1, _}, {T2, _}) -> T1 =< T2 end,
                                lists:zip(Queries, lists:seq(0, length(Queries) - 1))),
    Counts = array:new(N + 1, {default, 0}),
    Answer = array:new(length(Queries), {default, 0}),
    {_, _, _, Result} = lists:foldl(
        fun({Time, Index}, {RemainingLogs, LeftLogs, Active, Answers}) ->
            {LogsAfterAdd, ActiveAfterAdd, AddedLogs} = add_logs(RemainingLogs, Time, Counts, Active, []),
            {LeftAfterRemove, ActiveAfterRemove} = remove_logs(LeftLogs ++ AddedLogs, Time - X, Counts, ActiveAfterAdd),
            {LogsAfterAdd, LeftAfterRemove, ActiveAfterRemove,
             array:set(Index, N - ActiveAfterRemove, Answers)}
        end,
        {SortedLogs, [], 0, Answer},
        OrderedQueries),
    [array:get(I, Result) || I <- lists:seq(0, length(Queries) - 1)].

add_logs([[Server, Time] = Log | Rest], Limit, Counts, Active, Added) when Time =< Limit ->
    Count = array:get(Server, Counts),
    NewCounts = array:set(Server, Count + 1, Counts),
    NewActive = if Count =:= 0 -> Active + 1; true -> Active end,
    add_logs(Rest, Limit, NewCounts, NewActive, [Log | Added]);
add_logs(Rest, _Limit, _Counts, Active, Added) ->
    {Rest, Active, lists:reverse(Added)}.

remove_logs([[Server, Time] | Rest], LowerBound, Counts, Active) when Time < LowerBound ->
    Count = array:get(Server, Counts) - 1,
    NewCounts = array:set(Server, Count, Counts),
    NewActive = if Count =:= 0 -> Active - 1; true -> Active end,
    remove_logs(Rest, LowerBound, NewCounts, NewActive);
remove_logs(Logs, _LowerBound, _Counts, Active) ->
    {Logs, Active}.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec count_servers(n :: integer, logs :: [[integer]], x :: integer, queries :: [integer]) :: [integer]
  def count_servers(n, logs, x, queries) do
    sorted_logs = Enum.sort_by(logs, fn [_, time] -> time end)

    ordered_queries =
      queries
      |> Enum.with_index()
      |> Enum.sort_by(fn {time, _index} -> time end)

    counts = :array.new(n + 1, default: 0)
    answer = :array.new(length(queries), default: 0)

    {_, _, _, result} =
      Enum.reduce(ordered_queries, {sorted_logs, [], 0, answer}, fn {time, index},
                                                                   {remaining_logs, active_logs, active_servers, answers} ->
        {logs_after_add, active_after_add, added_logs, counts_after_add} =
          add_logs(remaining_logs, time, counts, active_servers, [])

        {active_logs_after_remove, active_after_remove, counts_after_remove} =
          remove_logs(active_logs ++ added_logs, time - x, counts_after_add, active_after_add)

        updated_answers = :array.set(index, n - active_after_remove, answers)

        {logs_after_add, active_logs_after_remove, active_after_remove, updated_answers,
         counts_after_remove}
      end)
      |> then(fn {remaining, active, servers, answers, _counts} ->
        {remaining, active, servers, answers}
      end)

    Enum.map(0..(length(queries) - 1), fn index -> :array.get(index, result) end)
  end

  defp add_logs([[server, time] = log | rest], limit, counts, active_servers, added_logs)
       when time <= limit do
    count = :array.get(server, counts)
    updated_counts = :array.set(server, count + 1, counts)
    updated_active = if count == 0, do: active_servers + 1, else: active_servers
    add_logs(rest, limit, updated_counts, updated_active, [log | added_logs])
  end

  defp add_logs(remaining_logs, _limit, counts, active_servers, added_logs) do
    {remaining_logs, active_servers, Enum.reverse(added_logs), counts}
  end

  defp remove_logs([[server, time] | rest], lower_bound, counts, active_servers)
       when time < lower_bound do
    count = :array.get(server, counts) - 1
    updated_counts = :array.set(server, count, counts)
    updated_active = if count == 0, do: active_servers - 1, else: active_servers
    remove_logs(rest, lower_bound, updated_counts, updated_active)
  end

  defp remove_logs(active_logs, _lower_bound, counts, active_servers) do
    {active_logs, active_servers, counts}
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O((L + Q) log(L + Q)), where L is the number of logs and Q is the number of queries, due to sorting.
- **Space Complexity:** O(L + Q + n) for sorted data, query indices, and per-server request counts.
