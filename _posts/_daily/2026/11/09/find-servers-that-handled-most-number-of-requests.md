---
layout: post
title: "Find Servers That Handled Most Number of Requests"
date: 2026-11-09 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Heap (Priority Queue)", "Simulation", "Ordered Set"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    vector<int> busiestServers(int k, vector<int>&\
        \ arrival, vector<int>& load) {\n        set<int> available;\n        for (int\
        \ server = 0; server < k; ++server) {\n            available.insert(server);\n\
        \        }\n\n        priority_queue<pair<long long, int>, vector<pair<long\
        \ long, int>>, greater<pair<long long, int>>> running;\n        vector<int>\
        \ handled(k, 0);\n\n        for (int i = 0; i < static_cast<int>(arrival.size());\
        \ ++i) {\n            while (!running.empty() && running.top().first <= arrival[i])\
        \ {\n                available.insert(running.top().second);\n             \
        \   running.pop();\n            }\n\n            if (available.empty()) {\n\
        \                continue;\n            }\n\n            int preferred = i %\
        \ k;\n            auto it = available.lower_bound(preferred);\n            if\
        \ (it == available.end()) {\n                it = available.begin();\n     \
        \       }\n\n            int server = *it;\n            available.erase(it);\n\
        \            ++handled[server];\n            running.emplace(static_cast<long\
        \ long>(arrival[i]) + load[i], server);\n        }\n\n        int maximum =\
        \ *max_element(handled.begin(), handled.end());\n        vector<int> result;\n\
        \        for (int server = 0; server < k; ++server) {\n            if (handled[server]\
        \ == maximum) {\n                result.push_back(server);\n            }\n\
        \        }\n        return result;\n    }\n};"
      java: "class Solution {\n    public List<Integer> busiestServers(int k, int[]\
        \ arrival, int[] load) {\n        TreeSet<Integer> available = new TreeSet<>();\n\
        \        for (int server = 0; server < k; ++server) {\n            available.add(server);\n\
        \        }\n\n        PriorityQueue<long[]> running = new PriorityQueue<>(Comparator.comparingLong(request\
        \ -> request[0]));\n        int[] handled = new int[k];\n\n        for (int\
        \ i = 0; i < arrival.length; ++i) {\n            while (!running.isEmpty() &&\
        \ running.peek()[0] <= arrival[i]) {\n                available.add((int) running.poll()[1]);\n\
        \            }\n\n            if (available.isEmpty()) {\n                continue;\n\
        \            }\n\n            int preferred = i % k;\n            Integer server\
        \ = available.ceiling(preferred);\n            if (server == null) {\n     \
        \           server = available.first();\n            }\n\n            available.remove(server);\n\
        \            ++handled[server];\n            running.offer(new long[] {(long)\
        \ arrival[i] + load[i], server});\n        }\n\n        int maximum = 0;\n \
        \       for (int count : handled) {\n            maximum = Math.max(maximum,\
        \ count);\n        }\n\n        List<Integer> result = new ArrayList<>();\n\
        \        for (int server = 0; server < k; ++server) {\n            if (handled[server]\
        \ == maximum) {\n                result.add(server);\n            }\n      \
        \  }\n        return result;\n    }\n}"
      python: "class Solution(object):\n    def busiestServers(self, k, arrival, load):\n\
        \        \"\"\"\n        :type k: int\n        :type arrival: List[int]\n  \
        \      :type load: List[int]\n        :rtype: List[int]\n        \"\"\"\n  \
        \      import heapq\n        from sortedcontainers import SortedList\n\n   \
        \     available = SortedList(range(k))\n        running = []\n        handled\
        \ = [0] * k\n\n        for i, time in enumerate(arrival):\n            while\
        \ running and running[0][0] <= time:\n                _, server = heapq.heappop(running)\n\
        \                available.add(server)\n\n            if not available:\n  \
        \              continue\n\n            preferred = i % k\n            position\
        \ = available.bisect_left(preferred)\n            if position == len(available):\n\
        \                position = 0\n\n            server = available.pop(position)\n\
        \            handled[server] += 1\n            heapq.heappush(running, (time\
        \ + load[i], server))\n\n        maximum = max(handled)\n        return [server\
        \ for server, count in enumerate(handled) if count == maximum]"
      python3: "class Solution:\n    def busiestServers(self, k: int, arrival: list[int],\
        \ load: list[int]) -> list[int]:\n        import heapq\n        from sortedcontainers\
        \ import SortedList\n\n        available = SortedList(range(k))\n        running\
        \ = []\n        handled = [0] * k\n\n        for i, time in enumerate(arrival):\n\
        \            while running and running[0][0] <= time:\n                _, server\
        \ = heapq.heappop(running)\n                available.add(server)\n\n      \
        \      if not available:\n                continue\n\n            preferred\
        \ = i % k\n            position = available.bisect_left(preferred)\n       \
        \     if position == len(available):\n                position = 0\n\n     \
        \       server = available.pop(position)\n            handled[server] += 1\n\
        \            heapq.heappush(running, (time + load[i], server))\n\n        maximum\
        \ = max(handled)\n        return [server for server, count in enumerate(handled)\
        \ if count == maximum]"
      c: "#include <stdlib.h>\n\ntypedef struct {\n    int server;\n    int start;\n\
        \    int size;\n} ServerSet;\n\ntypedef struct {\n    long long time;\n    int\
        \ server;\n} HeapItem;\n\nstatic int setFind(ServerSet* set, int value) {\n\
        \    int left = 0;\n    int right = set->size;\n    while (left < right) {\n\
        \        int mid = left + (right - left) / 2;\n        if (set->server[mid]\
        \ < value) left = mid + 1;\n        else right = mid;\n    }\n    return left;\n\
        }\n\nstatic void setRemove(ServerSet* set, int index) {\n    for (int i = index;\
        \ i + 1 < set->size; ++i) set->server[i] = set->server[i + 1];\n    --set->size;\n\
        }\n\nstatic void setAdd(ServerSet* set, int value) {\n    int index = setFind(set,\
        \ value);\n    for (int i = set->size; i > index; --i) set->server[i] = set->server[i\
        \ - 1];\n    set->server[index] = value;\n    ++set->size;\n}\n\nstatic void\
        \ heapPush(HeapItem* heap, int* size, HeapItem item) {\n    int index = (*size)++;\n\
        \    while (index > 0) {\n        int parent = (index - 1) / 2;\n        if\
        \ (heap[parent].time <= item.time) break;\n        heap[index] = heap[parent];\n\
        \        index = parent;\n    }\n    heap[index] = item;\n}\n\nstatic HeapItem\
        \ heapPop(HeapItem* heap, int* size) {\n    HeapItem result = heap[0];\n   \
        \ HeapItem last = heap[--(*size)];\n    if (*size > 0) {\n        int index\
        \ = 0;\n        while (index * 2 + 1 < *size) {\n            int child = index\
        \ * 2 + 1;\n            if (child + 1 < *size && heap[child + 1].time < heap[child].time)\
        \ ++child;\n            if (heap[child].time >= last.time) break;\n        \
        \    heap[index] = heap[child];\n            index = child;\n        }\n   \
        \     heap[index] = last;\n    }\n    return result;\n}\n\nint* busiestServers(int\
        \ k, int* arrival, int arrivalSize, int* load, int loadSize, int* returnSize)\
        \ {\n    ServerSet available;\n    available.server = (int*)malloc(sizeof(int)\
        \ * k);\n    available.size = k;\n    for (int i = 0; i < k; ++i) available.server[i]\
        \ = i;\n\n    HeapItem* running = (HeapItem*)malloc(sizeof(HeapItem) * arrivalSize);\n\
        \    int runningSize = 0;\n    int* handled = (int*)calloc(k, sizeof(int));\n\
        \n    for (int i = 0; i < arrivalSize; ++i) {\n        while (runningSize >\
        \ 0 && running[0].time <= arrival[i]) {\n            HeapItem item = heapPop(running,\
        \ &runningSize);\n            setAdd(&available, item.server);\n        }\n\
        \        if (available.size == 0) continue;\n\n        int preferred = i % k;\n\
        \        int index = setFind(&available, preferred);\n        if (index == available.size)\
        \ index = 0;\n        int server = available.server[index];\n        setRemove(&available,\
        \ index);\n        ++handled[server];\n        HeapItem item = {(long long)arrival[i]\
        \ + load[i], server};\n        heapPush(running, &runningSize, item);\n    }\n\
        \n    int maximum = 0;\n    for (int i = 0; i < k; ++i) if (handled[i] > maximum)\
        \ maximum = handled[i];\n    int* result = (int*)malloc(sizeof(int) * k);\n\
        \    *returnSize = 0;\n    for (int i = 0; i < k; ++i) {\n        if (handled[i]\
        \ == maximum) result[(*returnSize)++] = i;\n    }\n\n    free(available.server);\n\
        \    free(running);\n    free(handled);\n    return result;\n}"
      csharp: "public class Solution {\n    public IList<int> BusiestServers(int k,\
        \ int[] arrival, int[] load) {\n        var available = new SortedSet<int>();\n\
        \        for (int i = 0; i < k; i++) available.Add(i);\n        var running\
        \ = new PriorityQueue<int, long>();\n        int[] handled = new int[k];\n\n\
        \        for (int i = 0; i < arrival.Length; i++) {\n            while (running.Count\
        \ > 0 && running.PeekPriority() <= arrival[i]) {\n                int server\
        \ = running.Dequeue();\n                available.Add(server);\n           \
        \ }\n\n            if (available.Count == 0) continue;\n\n            int preferred\
        \ = i % k;\n            int serverToUse = -1;\n            foreach (int server\
        \ in available) {\n                if (server >= preferred) {\n            \
        \        serverToUse = server;\n                    break;\n               \
        \ }\n            }\n            if (serverToUse == -1) serverToUse = available.Min;\n\
        \n            available.Remove(serverToUse);\n            handled[serverToUse]++;\n\
        \            running.Enqueue(serverToUse, (long)arrival[i] + load[i]);\n   \
        \     }\n\n        int maximum = 0;\n        foreach (int count in handled)\
        \ maximum = Math.Max(maximum, count);\n        var result = new List<int>();\n\
        \        for (int i = 0; i < k; i++) {\n            if (handled[i] == maximum)\
        \ result.Add(i);\n        }\n        return result;\n    }\n}"
      javascript: "/**\n * @param {number} k\n * @param {number[]} arrival\n * @param\
        \ {number[]} load\n * @return {number[]}\n */\nvar busiestServers = function(k,\
        \ arrival, load) {\n    const available = Array.from({ length: k }, (_, i) =>\
        \ i);\n    const handled = new Array(k).fill(0);\n    const running = [];\n\n\
        \    const push = (time, server) => {\n        let index = running.length;\n\
        \        running.push([time, server]);\n        while (index > 0) {\n      \
        \      const parent = (index - 1) >> 1;\n            if (running[parent][0]\
        \ <= time) break;\n            running[index] = running[parent];\n         \
        \   index = parent;\n        }\n        running[index] = [time, server];\n \
        \   };\n\n    const pop = () => {\n        const result = running[0];\n    \
        \    const last = running.pop();\n        if (running.length > 0) {\n      \
        \      let index = 0;\n            while (index * 2 + 1 < running.length) {\n\
        \                let child = index * 2 + 1;\n                if (child + 1 <\
        \ running.length && running[child + 1][0] < running[child][0]) child++;\n  \
        \              if (running[child][0] >= last[0]) break;\n                running[index]\
        \ = running[child];\n                index = child;\n            }\n       \
        \     running[index] = last;\n        }\n        return result;\n    };\n\n\
        \    for (let i = 0; i < arrival.length; i++) {\n        while (running.length\
        \ > 0 && running[0][0] <= arrival[i]) {\n            const [, server] = pop();\n\
        \            let left = 0;\n            let right = available.length;\n    \
        \        while (left < right) {\n                const mid = (left + right)\
        \ >> 1;\n                if (available[mid] < server) left = mid + 1;\n    \
        \            else right = mid;\n            }\n            available.splice(left,\
        \ 0, server);\n        }\n\n        if (available.length === 0) continue;\n\n\
        \        const preferred = i % k;\n        let left = 0;\n        let right\
        \ = available.length;\n        while (left < right) {\n            const mid\
        \ = (left + right) >> 1;\n            if (available[mid] < preferred) left =\
        \ mid + 1;\n            else right = mid;\n        }\n        const index =\
        \ left === available.length ? 0 : left;\n        const server = available.splice(index,\
        \ 1)[0];\n        handled[server]++;\n        push(arrival[i] + load[i], server);\n\
        \    }\n\n    const maximum = Math.max(...handled);\n    const result = [];\n\
        \    for (let server = 0; server < k; server++) {\n        if (handled[server]\
        \ === maximum) result.push(server);\n    }\n    return result;\n};"
      typescript: "function busiestServers(k: number, arrival: number[], load: number[]):\
        \ number[] {\n    const available: number[] = Array.from({ length: k }, (_,\
        \ i) => i);\n    const running: Array<[number, number]> = [];\n    const handled:\
        \ number[] = new Array(k).fill(0);\n\n    const pushRunning = (completion: number,\
        \ server: number): void => {\n        running.push([completion, server]);\n\
        \        let index = running.length - 1;\n        while (index > 0) {\n    \
        \        const parent = Math.floor((index - 1) / 2);\n            const a =\
        \ running[index];\n            const b = running[parent];\n            if (a[0]\
        \ > b[0] || (a[0] === b[0] && a[1] >= b[1])) break;\n            running[index]\
        \ = b;\n            running[parent] = a;\n            index = parent;\n    \
        \    }\n    };\n\n    const popRunning = (): [number, number] => {\n       \
        \ const root = running[0];\n        const last = running.pop()!;\n        if\
        \ (running.length > 0) {\n            running[0] = last;\n            let index\
        \ = 0;\n            while (true) {\n                const left = index * 2 +\
        \ 1;\n                const right = left + 1;\n                let smallest\
        \ = index;\n                if (left < running.length && (running[left][0] <\
        \ running[smallest][0] || (running[left][0] === running[smallest][0] && running[left][1]\
        \ < running[smallest][1]))) smallest = left;\n                if (right < running.length\
        \ && (running[right][0] < running[smallest][0] || (running[right][0] === running[smallest][0]\
        \ && running[right][1] < running[smallest][1]))) smallest = right;\n       \
        \         if (smallest === index) break;\n                [running[index], running[smallest]]\
        \ = [running[smallest], running[index]];\n                index = smallest;\n\
        \            }\n        }\n        return root;\n    };\n\n    for (let i =\
        \ 0; i < arrival.length; i++) {\n        const time = arrival[i];\n        while\
        \ (running.length > 0 && running[0][0] <= time) {\n            const [, server]\
        \ = popRunning();\n            let low = 0;\n            let high = available.length;\n\
        \            while (low < high) {\n                const mid = (low + high)\
        \ >>> 1;\n                if (available[mid] < server) low = mid + 1;\n    \
        \            else high = mid;\n            }\n            available.splice(low,\
        \ 0, server);\n        }\n\n        if (available.length === 0) continue;\n\n\
        \        const preferred = i % k;\n        let low = 0;\n        let high =\
        \ available.length;\n        while (low < high) {\n            const mid = (low\
        \ + high) >>> 1;\n            if (available[mid] < preferred) low = mid + 1;\n\
        \            else high = mid;\n        }\n        const index = low === available.length\
        \ ? 0 : low;\n        const server = available.splice(index, 1)[0];\n      \
        \  handled[server]++;\n        pushRunning(time + load[i], server);\n    }\n\
        \n    const maximum = Math.max(...handled);\n    return handled.map((count,\
        \ server) => count === maximum ? server : -1).filter(server => server !== -1);\n\
        };"
      php: "class Solution {\n\n    /**\n     * @param Integer $k\n     * @param Integer[]\
        \ $arrival\n     * @param Integer[] $load\n     * @return Integer[]\n     */\n\
        \    function busiestServers($k, $arrival, $load) {\n        $available = range(0,\
        \ $k - 1);\n        $running = [];\n        $handled = array_fill(0, $k, 0);\n\
        \n        $push = function ($completion, $server) use (&$running) {\n      \
        \      $running[] = [$completion, $server];\n            $index = count($running)\
        \ - 1;\n            while ($index > 0) {\n                $parent = intdiv($index\
        \ - 1, 2);\n                if ($running[$index][0] > $running[$parent][0] ||\
        \ ($running[$index][0] === $running[$parent][0] && $running[$index][1] >= $running[$parent][1]))\
        \ {\n                    break;\n                }\n                [$running[$index],\
        \ $running[$parent]] = [$running[$parent], $running[$index]];\n            \
        \    $index = $parent;\n            }\n        };\n\n        $pop = function\
        \ () use (&$running) {\n            $root = $running[0];\n            $last\
        \ = array_pop($running);\n            if (count($running) > 0) {\n         \
        \       $running[0] = $last;\n                $index = 0;\n                $size\
        \ = count($running);\n                while (true) {\n                    $left\
        \ = $index * 2 + 1;\n                    $right = $left + 1;\n             \
        \       $smallest = $index;\n                    if ($left < $size && ($running[$left][0]\
        \ < $running[$smallest][0] || ($running[$left][0] === $running[$smallest][0]\
        \ && $running[$left][1] < $running[$smallest][1]))) {\n                    \
        \    $smallest = $left;\n                    }\n                    if ($right\
        \ < $size && ($running[$right][0] < $running[$smallest][0] || ($running[$right][0]\
        \ === $running[$smallest][0] && $running[$right][1] < $running[$smallest][1])))\
        \ {\n                        $smallest = $right;\n                    }\n  \
        \                  if ($smallest === $index) {\n                        break;\n\
        \                    }\n                    [$running[$index], $running[$smallest]]\
        \ = [$running[$smallest], $running[$index]];\n                    $index = $smallest;\n\
        \                }\n            }\n            return $root;\n        };\n\n\
        \        for ($i = 0; $i < count($arrival); $i++) {\n            $time = $arrival[$i];\n\
        \            while (count($running) > 0 && $running[0][0] <= $time) {\n    \
        \            [, $server] = $pop();\n                $low = 0;\n            \
        \    $high = count($available);\n                while ($low < $high) {\n  \
        \                  $mid = intdiv($low + $high, 2);\n                    if ($available[$mid]\
        \ < $server) {\n                        $low = $mid + 1;\n                 \
        \   } else {\n                        $high = $mid;\n                    }\n\
        \                }\n                array_splice($available, $low, 0, [$server]);\n\
        \            }\n\n            if (count($available) === 0) {\n             \
        \   continue;\n            }\n\n            $preferred = $i % $k;\n        \
        \    $low = 0;\n            $high = count($available);\n            while ($low\
        \ < $high) {\n                $mid = intdiv($low + $high, 2);\n            \
        \    if ($available[$mid] < $preferred) {\n                    $low = $mid +\
        \ 1;\n                } else {\n                    $high = $mid;\n        \
        \        }\n            }\n            $index = $low === count($available) ?\
        \ 0 : $low;\n            $server = $available[$index];\n            array_splice($available,\
        \ $index, 1);\n            $handled[$server]++;\n            $push($time + $load[$i],\
        \ $server);\n        }\n\n        $maximum = max($handled);\n        $result\
        \ = [];\n        foreach ($handled as $server => $count) {\n            if ($count\
        \ === $maximum) {\n                $result[] = $server;\n            }\n   \
        \     }\n        return $result;\n    }\n}"
      swift: "class Solution {\n    func busiestServers(_ k: Int, _ arrival: [Int],\
        \ _ load: [Int]) -> [Int] {\n        var available = Array(0..<k)\n        var\
        \ running: [(completion: Int, server: Int)] = []\n        var handled = Array(repeating:\
        \ 0, count: k)\n\n        func less(_ a: (completion: Int, server: Int), _ b:\
        \ (completion: Int, server: Int)) -> Bool {\n            if a.completion !=\
        \ b.completion { return a.completion < b.completion }\n            return a.server\
        \ < b.server\n        }\n\n        func push(_ completion: Int, _ server: Int)\
        \ {\n            running.append((completion, server))\n            var index\
        \ = running.count - 1\n            while index > 0 {\n                let parent\
        \ = (index - 1) / 2\n                if !less(running[index], running[parent])\
        \ { break }\n                running.swapAt(index, parent)\n               \
        \ index = parent\n            }\n        }\n\n        func pop() -> (completion:\
        \ Int, server: Int) {\n            let root = running[0]\n            let last\
        \ = running.removeLast()\n            if !running.isEmpty {\n              \
        \  running[0] = last\n                var index = 0\n                while true\
        \ {\n                    let left = index * 2 + 1\n                    let right\
        \ = left + 1\n                    var smallest = index\n                   \
        \ if left < running.count && less(running[left], running[smallest]) { smallest\
        \ = left }\n                    if right < running.count && less(running[right],\
        \ running[smallest]) { smallest = right }\n                    if smallest ==\
        \ index { break }\n                    running.swapAt(index, smallest)\n   \
        \                 index = smallest\n                }\n            }\n     \
        \       return root\n        }\n\n        for i in 0..<arrival.count {\n   \
        \         let time = arrival[i]\n            while !running.isEmpty && running[0].completion\
        \ <= time {\n                let server = pop().server\n                var\
        \ low = 0\n                var high = available.count\n                while\
        \ low < high {\n                    let mid = (low + high) / 2\n           \
        \         if available[mid] < server { low = mid + 1 }\n                   \
        \ else { high = mid }\n                }\n                available.insert(server,\
        \ at: low)\n            }\n\n            if available.isEmpty { continue }\n\
        \n            let preferred = i % k\n            var low = 0\n            var\
        \ high = available.count\n            while low < high {\n                let\
        \ mid = (low + high) / 2\n                if available[mid] < preferred { low\
        \ = mid + 1 }\n                else { high = mid }\n            }\n        \
        \    let index = low == available.count ? 0 : low\n            let server =\
        \ available.remove(at: index)\n            handled[server] += 1\n          \
        \  push(time + load[i], server)\n        }\n\n        let maximum = handled.max()!\n\
        \        return handled.indices.filter { handled[$0] == maximum }\n    }\n}"
      kotlin: "class Solution {\n    fun busiestServers(k: Int, arrival: IntArray, load:\
        \ IntArray): List<Int> {\n        val available = java.util.TreeSet<Int>()\n\
        \        for (server in 0 until k) available.add(server)\n        val running\
        \ = java.util.PriorityQueue<Pair<Int, Int>>(compareBy<Pair<Int, Int>> { it.first\
        \ }.thenBy { it.second })\n        val handled = IntArray(k)\n\n        for\
        \ (i in arrival.indices) {\n            val time = arrival[i]\n            while\
        \ (running.isNotEmpty() && running.peek().first <= time) {\n               \
        \ available.add(running.poll().second)\n            }\n\n            if (available.isEmpty())\
        \ continue\n\n            val preferred = i % k\n            val server = available.ceiling(preferred)\
        \ ?: available.first()\n            available.remove(server)\n            handled[server]++\n\
        \            running.add(Pair(time + load[i], server))\n        }\n\n      \
        \  val maximum = handled.maxOrNull() ?: 0\n        return handled.indices.filter\
        \ { handled[it] == maximum }\n    }\n}"
      dart: "class Solution {\n  List<int> busiestServers(int k, List<int> arrival,\
        \ List<int> load) {\n    final available = List<int>.generate(k, (i) => i);\n\
        \    final running = <List<int>>[];\n    final handled = List<int>.filled(k,\
        \ 0);\n\n    void push(List<int> item) {\n      running.add(item);\n      var\
        \ index = running.length - 1;\n      while (index > 0) {\n        final parent\
        \ = (index - 1) ~/ 2;\n        if (running[parent][0] <= running[index][0])\
        \ break;\n        final temp = running[parent];\n        running[parent] = running[index];\n\
        \        running[index] = temp;\n        index = parent;\n      }\n    }\n\n\
        \    List<int> pop() {\n      final result = running[0];\n      final last =\
        \ running.removeLast();\n      if (running.isNotEmpty) {\n        running[0]\
        \ = last;\n        var index = 0;\n        while (true) {\n          final left\
        \ = index * 2 + 1;\n          final right = left + 1;\n          var smallest\
        \ = index;\n          if (left < running.length && running[left][0] < running[smallest][0])\
        \ {\n            smallest = left;\n          }\n          if (right < running.length\
        \ && running[right][0] < running[smallest][0]) {\n            smallest = right;\n\
        \          }\n          if (smallest == index) break;\n          final temp\
        \ = running[index];\n          running[index] = running[smallest];\n       \
        \   running[smallest] = temp;\n          index = smallest;\n        }\n    \
        \  }\n      return result;\n    }\n\n    for (var i = 0; i < arrival.length;\
        \ i++) {\n      while (running.isNotEmpty && running[0][0] <= arrival[i]) {\n\
        \        final server = pop()[1];\n        var low = 0;\n        var high =\
        \ available.length;\n        while (low < high) {\n          final mid = (low\
        \ + high) ~/ 2;\n          if (available[mid] < server) {\n            low =\
        \ mid + 1;\n          } else {\n            high = mid;\n          }\n     \
        \   }\n        available.insert(low, server);\n      }\n\n      if (available.isEmpty)\
        \ continue;\n\n      final preferred = i % k;\n      var low = 0;\n      var\
        \ high = available.length;\n      while (low < high) {\n        final mid =\
        \ (low + high) ~/ 2;\n        if (available[mid] < preferred) {\n          low\
        \ = mid + 1;\n        } else {\n          high = mid;\n        }\n      }\n\
        \      if (low == available.length) low = 0;\n      final server = available.removeAt(low);\n\
        \      handled[server]++;\n      push([arrival[i] + load[i], server]);\n   \
        \ }\n\n    final maximum = handled.reduce((a, b) => a > b ? a : b);\n    return\
        \ List<int>.generate(k, (i) => i).where((i) => handled[i] == maximum).toList();\n\
        \  }\n}"
      go: "func busiestServers(k int, arrival []int, load []int) []int {\n\tavailable\
        \ := make([]int, k)\n\tfor i := range available {\n\t\tavailable[i] = i\n\t\
        }\n\thandled := make([]int, k)\n\trunning := make([][2]int, 0, len(arrival))\n\
        \n\tpush := func(item [2]int) {}\n\t_ = push\n\n\tvar heapPush func([2]int)\n\
        \theapPush = func(item [2]int) {\n\t\trunning = append(running, item)\n\t\t\
        index := len(running) - 1\n\t\tfor index > 0 {\n\t\t\tparent := (index - 1)\
        \ / 2\n\t\t\tif running[parent][0] <= running[index][0] {\n\t\t\t\tbreak\n\t\
        \t\t}\n\t\t\trunning[parent], running[index] = running[index], running[parent]\n\
        \t\t\tindex = parent\n\t\t}\n\t}\n\n\theapPop := func() [2]int {\n\t\tresult\
        \ := running[0]\n\t\tlast := running[len(running)-1]\n\t\trunning = running[:len(running)-1]\n\
        \t\tif len(running) > 0 {\n\t\t\trunning[0] = last\n\t\t\tindex := 0\n\t\t\t\
        for {\n\t\t\t\tleft := index*2 + 1\n\t\t\t\tright := left + 1\n\t\t\t\tsmallest\
        \ := index\n\t\t\t\tif left < len(running) && running[left][0] < running[smallest][0]\
        \ {\n\t\t\t\t\tsmallest = left\n\t\t\t\t}\n\t\t\t\tif right < len(running) &&\
        \ running[right][0] < running[smallest][0] {\n\t\t\t\t\tsmallest = right\n\t\
        \t\t\t}\n\t\t\t\tif smallest == index {\n\t\t\t\t\tbreak\n\t\t\t\t}\n\t\t\t\t\
        running[index], running[smallest] = running[smallest], running[index]\n\t\t\t\
        \tindex = smallest\n\t\t\t}\n\t\t}\n\t\treturn result\n\t}\n\n\tinsertAvailable\
        \ := func(server int) {\n\t\tlow, high := 0, len(available)\n\t\tfor low < high\
        \ {\n\t\t\tmid := (low + high) / 2\n\t\t\tif available[mid] < server {\n\t\t\
        \t\tlow = mid + 1\n\t\t\t} else {\n\t\t\t\thigh = mid\n\t\t\t}\n\t\t}\n\t\t\
        available = append(available, 0)\n\t\tcopy(available[low+1:], available[low:])\n\
        \t\tavailable[low] = server\n\t}\n\n\tfor i, time := range arrival {\n\t\tfor\
        \ len(running) > 0 && running[0][0] <= time {\n\t\t\tserver := heapPop()[1]\n\
        \t\t\tinsertAvailable(server)\n\t\t}\n\t\tif len(available) == 0 {\n\t\t\tcontinue\n\
        \t\t}\n\t\tpreferred := i % k\n\t\tlow, high := 0, len(available)\n\t\tfor low\
        \ < high {\n\t\t\tmid := (low + high) / 2\n\t\t\tif available[mid] < preferred\
        \ {\n\t\t\t\tlow = mid + 1\n\t\t\t} else {\n\t\t\t\thigh = mid\n\t\t\t}\n\t\t\
        }\n\t\tif low == len(available) {\n\t\t\tlow = 0\n\t\t}\n\t\tserver := available[low]\n\
        \t\tavailable = append(available[:low], available[low+1:]...)\n\t\thandled[server]++\n\
        \t\theapPush([2]int{time + load[i], server})\n\t}\n\n\tmaximum := 0\n\tfor _,\
        \ count := range handled {\n\t\tif count > maximum {\n\t\t\tmaximum = count\n\
        \t\t}\n\t}\n\tresult := make([]int, 0)\n\tfor server, count := range handled\
        \ {\n\t\tif count == maximum {\n\t\t\tresult = append(result, server)\n\t\t\
        }\n\t}\n\treturn result\n}"
      ruby: "# @param {Integer} k\n# @param {Integer[]} arrival\n# @param {Integer[]}\
        \ load\n# @return {Integer[]}\ndef busiest_servers(k, arrival, load)\n  available\
        \ = (0...k).to_a\n  running = []\n  handled = Array.new(k, 0)\n\n  push = lambda\
        \ do |item|\n    running << item\n    index = running.length - 1\n    while\
        \ index > 0\n      parent = (index - 1) / 2\n      break if running[parent][0]\
        \ <= running[index][0]\n      running[parent], running[index] = running[index],\
        \ running[parent]\n      index = parent\n    end\n  end\n\n  pop = lambda do\n\
        \    result = running[0]\n    last = running.pop\n    unless running.empty?\n\
        \      running[0] = last\n      index = 0\n      loop do\n        left = index\
        \ * 2 + 1\n        right = left + 1\n        smallest = index\n        smallest\
        \ = left if left < running.length && running[left][0] < running[smallest][0]\n\
        \        smallest = right if right < running.length && running[right][0] < running[smallest][0]\n\
        \        break if smallest == index\n        running[index], running[smallest]\
        \ = running[smallest], running[index]\n        index = smallest\n      end\n\
        \    end\n    result\n  end\n\n  arrival.each_index do |i|\n    while !running.empty?\
        \ && running[0][0] <= arrival[i]\n      server = pop.call[1]\n      low = 0\n\
        \      high = available.length\n      while low < high\n        mid = (low +\
        \ high) / 2\n        if available[mid] < server\n          low = mid + 1\n \
        \       else\n          high = mid\n        end\n      end\n      available.insert(low,\
        \ server)\n    end\n\n    next if available.empty?\n\n    preferred = i % k\n\
        \    low = 0\n    high = available.length\n    while low < high\n      mid =\
        \ (low + high) / 2\n      if available[mid] < preferred\n        low = mid +\
        \ 1\n      else\n        high = mid\n      end\n    end\n    low = 0 if low\
        \ == available.length\n    server = available.delete_at(low)\n    handled[server]\
        \ += 1\n    push.call([arrival[i] + load[i], server])\n  end\n\n  maximum =\
        \ handled.max\n  handled.each_index.select { |server| handled[server] == maximum\
        \ }\nend"
      scala: "object Solution {\n    def busiestServers(k: Int, arrival: Array[Int],\
        \ load: Array[Int]): List[Int] = {\n        val available = scala.collection.mutable.ArrayBuffer.from(0\
        \ until k)\n        val handled = Array.fill(k)(0)\n        val running = scala.collection.mutable.ArrayBuffer.empty[(Int,\
        \ Int)]\n\n        def push(item: (Int, Int)): Unit = {\n            running\
        \ += item\n            var index = running.length - 1\n            while (index\
        \ > 0) {\n                val parent = (index - 1) / 2\n                if (running(parent)._1\
        \ <= running(index)._1) index = 0\n                else {\n                \
        \    val temp = running(parent)\n                    running(parent) = running(index)\n\
        \                    running(index) = temp\n                    index = parent\n\
        \                }\n            }\n        }\n\n        def pop(): (Int, Int)\
        \ = {\n            val result = running(0)\n            val last = running.remove(running.length\
        \ - 1)\n            if (running.nonEmpty) {\n                running(0) = last\n\
        \                var index = 0\n                var continue = true\n      \
        \          while (continue) {\n                    val left = index * 2 + 1\n\
        \                    val right = left + 1\n                    var smallest\
        \ = index\n                    if (left < running.length && running(left)._1\
        \ < running(smallest)._1) smallest = left\n                    if (right < running.length\
        \ && running(right)._1 < running(smallest)._1) smallest = right\n          \
        \          if (smallest == index) continue = false\n                    else\
        \ {\n                        val temp = running(index)\n                   \
        \     running(index) = running(smallest)\n                        running(smallest)\
        \ = temp\n                        index = smallest\n                    }\n\
        \                }\n            }\n            result\n        }\n\n       \
        \ def insertAvailable(server: Int): Unit = {\n            var low = 0\n    \
        \        var high = available.length\n            while (low < high) {\n   \
        \             val mid = (low + high) / 2\n                if (available(mid)\
        \ < server) low = mid + 1 else high = mid\n            }\n            available.insert(low,\
        \ server)\n        }\n\n        for (i <- arrival.indices) {\n            while\
        \ (running.nonEmpty && running(0)._1 <= arrival(i)) {\n                insertAvailable(pop()._2)\n\
        \            }\n            if (available.nonEmpty) {\n                val preferred\
        \ = i % k\n                var low = 0\n                var high = available.length\n\
        \                while (low < high) {\n                    val mid = (low +\
        \ high) / 2\n                    if (available(mid) < preferred) low = mid +\
        \ 1 else high = mid\n                }\n                if (low == available.length)\
        \ low = 0\n                val server = available.remove(low)\n            \
        \    handled(server) += 1\n                push((arrival(i) + load(i), server))\n\
        \            }\n        }\n\n        val maximum = handled.max\n        handled.indices.filter(server\
        \ => handled(server) == maximum).toList\n    }\n}"
      rust: "impl Solution {\n    pub fn busiest_servers(k: i32, arrival: Vec<i32>,\
        \ load: Vec<i32>) -> Vec<i32> {\n        use std::cmp::Reverse;\n        use\
        \ std::collections::BTreeSet;\n        use std::collections::BinaryHeap;\n\n\
        \        let k = k as usize;\n        let mut available: BTreeSet<usize> = (0..k).collect();\n\
        \        let mut running: BinaryHeap<Reverse<(i64, usize)>> = BinaryHeap::new();\n\
        \        let mut handled = vec![0; k];\n\n        for (i, &time) in arrival.iter().enumerate()\
        \ {\n            let time = time as i64;\n            while let Some(&Reverse((end,\
        \ server))) = running.peek() {\n                if end > time {\n          \
        \          break;\n                }\n                running.pop();\n     \
        \           available.insert(server);\n            }\n\n            if available.is_empty()\
        \ {\n                continue;\n            }\n\n            let preferred =\
        \ i % k;\n            let server = available\n                .range(preferred..)\n\
        \                .next()\n                .copied()\n                .or_else(||\
        \ available.iter().next().copied())\n                .unwrap();\n          \
        \  available.remove(&server);\n            handled[server] += 1;\n         \
        \   running.push(Reverse((time + load[i] as i64, server)));\n        }\n\n \
        \       let maximum = *handled.iter().max().unwrap();\n        handled\n   \
        \         .iter()\n            .enumerate()\n            .filter_map(|(server,\
        \ &count)| {\n                if count == maximum {\n                    Some(server\
        \ as i32)\n                } else {\n                    None\n            \
        \    }\n            })\n            .collect()\n    }\n}"
      racket: "(define/contract (busiest-servers k arrival load)\n  (-> exact-integer?\
        \ (listof exact-integer?) (listof exact-integer?) (listof exact-integer?))\n\
        \  (define available (build-vector k values))\n  (define running '())\n  (define\
        \ handled (make-vector k 0))\n  (define (insert-available server)\n    (let\
        \ loop ([before '()] [after available])\n      (cond\n        [(null? after)\
        \ (set! available (append (reverse before) (list server)))]\n        [(< server\
        \ (car after))\n         (set! available (append (reverse before) (cons server\
        \ after)))]\n        [else (loop (cons (car after) before) (cdr after))])))\n\
        \  (define (pop-running)\n    (let ([server (cadar running)])\n      (set! running\
        \ (cdr running))\n      server))\n  (define (push-running end server)\n    (let\
        \ loop ([before '()] [after running])\n      (cond\n        [(null? after) (set!\
        \ running (append (reverse before) (list (list end server))))]\n        [(<\
        \ end (caar after))\n         (set! running (append (reverse before) (cons (list\
        \ end server) after)))]\n        [else (loop (cons (car after) before) (cdr\
        \ after))])))\n  (define (process requests times i)\n    (unless (null? requests)\n\
        \      (let ([time (car requests)])\n        (let release ()\n          (when\
        \ (and (pair? running) (<= (caar running) time))\n            (insert-available\
        \ (pop-running))\n            (release)))\n        (unless (null? available)\n\
        \          (let* ([preferred (modulo i k)]\n                 [server (or (findf\
        \ (lambda (s) (>= s preferred)) available)\n                             (car\
        \ available))])\n            (set! available (remove server available))\n  \
        \          (vector-set! handled server (add1 (vector-ref handled server)))\n\
        \            (push-running (+ time (car times)) server)))\n        (process\
        \ (cdr requests) (cdr times) (add1 i)))))\n  (process arrival load 0)\n  (define\
        \ maximum (apply max (vector->list handled)))\n  (for/list ([server (in-range\
        \ k)]\n             #:when (= (vector-ref handled server) maximum))\n    server))"
      erlang: "-spec busiest_servers(K :: integer(), Arrival :: [integer()], Load ::\
        \ [integer()]) -> [integer()].\nbusiest_servers(K, Arrival, Load) ->\n  Available\
        \ = gb_sets:from_list(lists:seq(0, K - 1)),\n  {Running, _Available, Counts}\
        \ = process_requests(Arrival, Load, 0, K, [], Available, array:new(K, {default,\
        \ 0})),\n  _ = Running,\n  MaxCount = lists:max(array:to_list(Counts)),\n  [Server\
        \ || Server <- lists:seq(0, K - 1), array:get(Server, Counts) =:= MaxCount].\n\
        \nprocess_requests([], [], _I, _K, Running, Available, Counts) ->\n  {Running,\
        \ Available, Counts};\nprocess_requests([Time | Times], [Duration | Durations],\
        \ I, K, Running, Available, Counts) ->\n  {Ready, Busy} = release_servers(Running,\
        \ Time, Available),\n  case gb_sets:is_empty(Ready) of\n    true -> process_requests(Times,\
        \ Durations, I + 1, K, Busy, Ready, Counts);\n    false ->\n      Preferred\
        \ = I rem K,\n      Server = case gb_sets:iterator_from(Preferred, Ready) of\n\
        \        Iter ->\n          case gb_sets:next(Iter) of\n            none ->\
        \ gb_sets:smallest(Ready);\n            {Value, _} -> Value\n          end\n\
        \      end,\n      NewAvailable = gb_sets:delete(Server, Ready),\n      NewCounts\
        \ = array:set(Server, array:get(Server, Counts) + 1, Counts),\n      Completion\
        \ = Time + Duration,\n      NewRunning = lists:sort([{Completion, Server} |\
        \ Busy]),\n      process_requests(Times, Durations, I + 1, K, NewRunning, NewAvailable,\
        \ NewCounts)\n  end.\n\nrelease_servers([{End, Server} | Rest], Time, Available)\
        \ when End =< Time ->\n  release_servers(Rest, Time, gb_sets:add(Server, Available));\n\
        release_servers(Running, _Time, Available) ->\n  {Available, Running}."
      elixir: "defmodule Solution do\n  @spec busiest_servers(k :: integer, arrival\
        \ :: [integer], load :: [integer]) :: [integer]\n  def busiest_servers(k, arrival,\
        \ load) do\n    available = 0..(k - 1) |> MapSet.new()\n    {_, _, handled}\
        \ = process_requests(arrival, load, 0, k, [], available, List.duplicate(0, k))\n\
        \    maximum = Enum.max(handled)\n    handled\n    |> Enum.with_index()\n  \
        \  |> Enum.filter(fn {count, _server} -> count == maximum end)\n    |> Enum.map(fn\
        \ {_count, server} -> server end)\n  end\n\n  defp process_requests([], [],\
        \ _i, _k, running, available, handled) do\n    {running, available, handled}\n\
        \  end\n\n  defp process_requests([time | times], [duration | durations], i,\
        \ k, running, available, handled) do\n    {ready, busy} = release_servers(running,\
        \ time, available)\n\n    if MapSet.size(ready) == 0 do\n      process_requests(times,\
        \ durations, i + 1, k, busy, ready, handled)\n    else\n      preferred = rem(i,\
        \ k)\n      server =\n        ready\n        |> Enum.filter(&(&1 >= preferred))\n\
        \        |> Enum.min(fn -> Enum.min(ready) end)\n\n      new_available = MapSet.delete(ready,\
        \ server)\n      new_handled = List.update_at(handled, server, &(&1 + 1))\n\
        \      new_running = Enum.sort([{time + duration, server} | busy])\n      process_requests(times,\
        \ durations, i + 1, k, new_running, new_available, new_handled)\n    end\n \
        \ end\n\n  defp release_servers([{finish, server} | rest], time, available)\
        \ when finish <= time do\n    release_servers(rest, time, MapSet.put(available,\
        \ server))\n  end\n\n  defp release_servers(running, _time, available) do\n\
        \    {available, running}\n  end\nend"
    approach: 'Keep the available server IDs in an ordered set and the currently running
      requests in a min-heap of (completion time, server ID). Before each request arrives,
      return every server whose completion time is less than or equal to the arrival
      time to the available set.


      For request i, find the smallest available server ID at least i % k; if none exists,
      wrap around to the smallest available ID. Assign the request there, update its
      request count, and push its completion time into the heap. Return every server
      whose count equals the maximum count.'
    time_complexity: O(n log k), where n is the number of requests. Each request and
      server availability update performs heap or ordered-set operations.
    space_complexity: O(k), for the available server set, running-request heap, and
      request counts.
    elapsed_time: 214.20579504966736
    model: gpt-6-luna
    generated_at: '2026-11-12 23:48:01 '
---

## Problem #1606: Find Servers That Handled Most Number of Requests

**Difficulty:** Hard

**Topics:** Array, Heap (Priority Queue), Simulation, Ordered Set

## Problem Description

<p>You have <code>k</code> servers numbered from <code>0</code> to <code>k-1</code> that are being used to handle multiple requests simultaneously. Each server has infinite computational capacity but <strong>cannot handle more than one request at a time</strong>. The requests are assigned to servers according to a specific algorithm:</p>

<ul>
	<li>The <code>i<sup>th</sup></code> (0-indexed) request arrives.</li>
	<li>If all servers are busy, the request is dropped (not handled at all).</li>
	<li>If the <code>(i % k)<sup>th</sup></code> server is available, assign the request to that server.</li>
	<li>Otherwise, assign the request to the next available server (wrapping around the list of servers and starting from 0 if necessary). For example, if the <code>i<sup>th</sup></code> server is busy, try to assign the request to the <code>(i+1)<sup>th</sup></code> server, then the <code>(i+2)<sup>th</sup></code> server, and so on.</li>
</ul>

<p>You are given a <strong>strictly increasing</strong> array <code>arrival</code> of positive integers, where <code>arrival[i]</code> represents the arrival time of the <code>i<sup>th</sup></code> request, and another array <code>load</code>, where <code>load[i]</code> represents the load of the <code>i<sup>th</sup></code> request (the time it takes to complete). Your goal is to find the <strong>busiest server(s)</strong>. A server is considered <strong>busiest</strong> if it handled the most number of requests successfully among all the servers.</p>

<p>Return <em>a list containing the IDs (0-indexed) of the <strong>busiest server(s)</strong></em>. You may return the IDs in any order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/08/load-1.png" style="width: 389px; height: 221px;" />
<pre>
<strong>Input:</strong> k = 3, arrival = [1,2,3,4,5], load = [5,2,3,3,3] 
<strong>Output:</strong> [1] 
<strong>Explanation:</strong> 
All of the servers start out available.
The first 3 requests are handled by the first 3 servers in order.
Request 3 comes in. Server 0 is busy, so it&#39;s assigned to the next available server, which is 1.
Request 4 comes in. It cannot be handled since all servers are busy, so it is dropped.
Servers 0 and 2 handled one request each, while server 1 handled two requests. Hence server 1 is the busiest server.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> k = 3, arrival = [1,2,3,4], load = [1,2,1,2]
<strong>Output:</strong> [0]
<strong>Explanation:</strong> 
The first 3 requests are handled by first 3 servers.
Request 3 comes in. It is handled by server 0 since the server is available.
Server 0 handled two requests, while servers 1 and 2 handled one request each. Hence server 0 is the busiest server.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> k = 3, arrival = [1,2,3], load = [10,12,11]
<strong>Output:</strong> [0,1,2]
<strong>Explanation:</strong> Each server handles a single request, so they are all considered the busiest.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= arrival.length, load.length &lt;= 10<sup>5</sup></code></li>
	<li><code>arrival.length == load.length</code></li>
	<li><code>1 &lt;= arrival[i], load[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>arrival</code> is <strong>strictly increasing</strong>.</li>
</ul>


## Hints

1. To speed up the next available server search, keep track of the available servers in a sorted structure such as an ordered set.

2. To determine if a server is available, keep track of the end times for each task in a heap and add the server to the available set once the soonest task ending time is less than or equal to the next task to add.

## 🤖 AI-Generated Solution (gpt-6-luna)

### Approach

Keep the available server IDs in an ordered set and the currently running requests in a min-heap of (completion time, server ID). Before each request arrives, return every server whose completion time is less than or equal to the arrival time to the available set.

For request i, find the smallest available server ID at least i % k; if none exists, wrap around to the smallest available ID. Assign the request there, update its request count, and push its completion time into the heap. Return every server whose count equals the maximum count.

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
    vector<int> busiestServers(int k, vector<int>& arrival, vector<int>& load) {
        set<int> available;
        for (int server = 0; server < k; ++server) {
            available.insert(server);
        }

        priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> running;
        vector<int> handled(k, 0);

        for (int i = 0; i < static_cast<int>(arrival.size()); ++i) {
            while (!running.empty() && running.top().first <= arrival[i]) {
                available.insert(running.top().second);
                running.pop();
            }

            if (available.empty()) {
                continue;
            }

            int preferred = i % k;
            auto it = available.lower_bound(preferred);
            if (it == available.end()) {
                it = available.begin();
            }

            int server = *it;
            available.erase(it);
            ++handled[server];
            running.emplace(static_cast<long long>(arrival[i]) + load[i], server);
        }

        int maximum = *max_element(handled.begin(), handled.end());
        vector<int> result;
        for (int server = 0; server < k; ++server) {
            if (handled[server] == maximum) {
                result.push_back(server);
            }
        }
        return result;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public List<Integer> busiestServers(int k, int[] arrival, int[] load) {
        TreeSet<Integer> available = new TreeSet<>();
        for (int server = 0; server < k; ++server) {
            available.add(server);
        }

        PriorityQueue<long[]> running = new PriorityQueue<>(Comparator.comparingLong(request -> request[0]));
        int[] handled = new int[k];

        for (int i = 0; i < arrival.length; ++i) {
            while (!running.isEmpty() && running.peek()[0] <= arrival[i]) {
                available.add((int) running.poll()[1]);
            }

            if (available.isEmpty()) {
                continue;
            }

            int preferred = i % k;
            Integer server = available.ceiling(preferred);
            if (server == null) {
                server = available.first();
            }

            available.remove(server);
            ++handled[server];
            running.offer(new long[] {(long) arrival[i] + load[i], server});
        }

        int maximum = 0;
        for (int count : handled) {
            maximum = Math.max(maximum, count);
        }

        List<Integer> result = new ArrayList<>();
        for (int server = 0; server < k; ++server) {
            if (handled[server] == maximum) {
                result.add(server);
            }
        }
        return result;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def busiestServers(self, k, arrival, load):
        """
        :type k: int
        :type arrival: List[int]
        :type load: List[int]
        :rtype: List[int]
        """
        import heapq
        from sortedcontainers import SortedList

        available = SortedList(range(k))
        running = []
        handled = [0] * k

        for i, time in enumerate(arrival):
            while running and running[0][0] <= time:
                _, server = heapq.heappop(running)
                available.add(server)

            if not available:
                continue

            preferred = i % k
            position = available.bisect_left(preferred)
            if position == len(available):
                position = 0

            server = available.pop(position)
            handled[server] += 1
            heapq.heappush(running, (time + load[i], server))

        maximum = max(handled)
        return [server for server, count in enumerate(handled) if count == maximum]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        import heapq
        from sortedcontainers import SortedList

        available = SortedList(range(k))
        running = []
        handled = [0] * k

        for i, time in enumerate(arrival):
            while running and running[0][0] <= time:
                _, server = heapq.heappop(running)
                available.add(server)

            if not available:
                continue

            preferred = i % k
            position = available.bisect_left(preferred)
            if position == len(available):
                position = 0

            server = available.pop(position)
            handled[server] += 1
            heapq.heappush(running, (time + load[i], server))

        maximum = max(handled)
        return [server for server, count in enumerate(handled) if count == maximum]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>

typedef struct {
    int server;
    int start;
    int size;
} ServerSet;

typedef struct {
    long long time;
    int server;
} HeapItem;

static int setFind(ServerSet* set, int value) {
    int left = 0;
    int right = set->size;
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (set->server[mid] < value) left = mid + 1;
        else right = mid;
    }
    return left;
}

static void setRemove(ServerSet* set, int index) {
    for (int i = index; i + 1 < set->size; ++i) set->server[i] = set->server[i + 1];
    --set->size;
}

static void setAdd(ServerSet* set, int value) {
    int index = setFind(set, value);
    for (int i = set->size; i > index; --i) set->server[i] = set->server[i - 1];
    set->server[index] = value;
    ++set->size;
}

static void heapPush(HeapItem* heap, int* size, HeapItem item) {
    int index = (*size)++;
    while (index > 0) {
        int parent = (index - 1) / 2;
        if (heap[parent].time <= item.time) break;
        heap[index] = heap[parent];
        index = parent;
    }
    heap[index] = item;
}

static HeapItem heapPop(HeapItem* heap, int* size) {
    HeapItem result = heap[0];
    HeapItem last = heap[--(*size)];
    if (*size > 0) {
        int index = 0;
        while (index * 2 + 1 < *size) {
            int child = index * 2 + 1;
            if (child + 1 < *size && heap[child + 1].time < heap[child].time) ++child;
            if (heap[child].time >= last.time) break;
            heap[index] = heap[child];
            index = child;
        }
        heap[index] = last;
    }
    return result;
}

int* busiestServers(int k, int* arrival, int arrivalSize, int* load, int loadSize, int* returnSize) {
    ServerSet available;
    available.server = (int*)malloc(sizeof(int) * k);
    available.size = k;
    for (int i = 0; i < k; ++i) available.server[i] = i;

    HeapItem* running = (HeapItem*)malloc(sizeof(HeapItem) * arrivalSize);
    int runningSize = 0;
    int* handled = (int*)calloc(k, sizeof(int));

    for (int i = 0; i < arrivalSize; ++i) {
        while (runningSize > 0 && running[0].time <= arrival[i]) {
            HeapItem item = heapPop(running, &runningSize);
            setAdd(&available, item.server);
        }
        if (available.size == 0) continue;

        int preferred = i % k;
        int index = setFind(&available, preferred);
        if (index == available.size) index = 0;
        int server = available.server[index];
        setRemove(&available, index);
        ++handled[server];
        HeapItem item = {(long long)arrival[i] + load[i], server};
        heapPush(running, &runningSize, item);
    }

    int maximum = 0;
    for (int i = 0; i < k; ++i) if (handled[i] > maximum) maximum = handled[i];
    int* result = (int*)malloc(sizeof(int) * k);
    *returnSize = 0;
    for (int i = 0; i < k; ++i) {
        if (handled[i] == maximum) result[(*returnSize)++] = i;
    }

    free(available.server);
    free(running);
    free(handled);
    return result;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public IList<int> BusiestServers(int k, int[] arrival, int[] load) {
        var available = new SortedSet<int>();
        for (int i = 0; i < k; i++) available.Add(i);
        var running = new PriorityQueue<int, long>();
        int[] handled = new int[k];

        for (int i = 0; i < arrival.Length; i++) {
            while (running.Count > 0 && running.PeekPriority() <= arrival[i]) {
                int server = running.Dequeue();
                available.Add(server);
            }

            if (available.Count == 0) continue;

            int preferred = i % k;
            int serverToUse = -1;
            foreach (int server in available) {
                if (server >= preferred) {
                    serverToUse = server;
                    break;
                }
            }
            if (serverToUse == -1) serverToUse = available.Min;

            available.Remove(serverToUse);
            handled[serverToUse]++;
            running.Enqueue(serverToUse, (long)arrival[i] + load[i]);
        }

        int maximum = 0;
        foreach (int count in handled) maximum = Math.Max(maximum, count);
        var result = new List<int>();
        for (int i = 0; i < k; i++) {
            if (handled[i] == maximum) result.Add(i);
        }
        return result;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number} k
 * @param {number[]} arrival
 * @param {number[]} load
 * @return {number[]}
 */
var busiestServers = function(k, arrival, load) {
    const available = Array.from({ length: k }, (_, i) => i);
    const handled = new Array(k).fill(0);
    const running = [];

    const push = (time, server) => {
        let index = running.length;
        running.push([time, server]);
        while (index > 0) {
            const parent = (index - 1) >> 1;
            if (running[parent][0] <= time) break;
            running[index] = running[parent];
            index = parent;
        }
        running[index] = [time, server];
    };

    const pop = () => {
        const result = running[0];
        const last = running.pop();
        if (running.length > 0) {
            let index = 0;
            while (index * 2 + 1 < running.length) {
                let child = index * 2 + 1;
                if (child + 1 < running.length && running[child + 1][0] < running[child][0]) child++;
                if (running[child][0] >= last[0]) break;
                running[index] = running[child];
                index = child;
            }
            running[index] = last;
        }
        return result;
    };

    for (let i = 0; i < arrival.length; i++) {
        while (running.length > 0 && running[0][0] <= arrival[i]) {
            const [, server] = pop();
            let left = 0;
            let right = available.length;
            while (left < right) {
                const mid = (left + right) >> 1;
                if (available[mid] < server) left = mid + 1;
                else right = mid;
            }
            available.splice(left, 0, server);
        }

        if (available.length === 0) continue;

        const preferred = i % k;
        let left = 0;
        let right = available.length;
        while (left < right) {
            const mid = (left + right) >> 1;
            if (available[mid] < preferred) left = mid + 1;
            else right = mid;
        }
        const index = left === available.length ? 0 : left;
        const server = available.splice(index, 1)[0];
        handled[server]++;
        push(arrival[i] + load[i], server);
    }

    const maximum = Math.max(...handled);
    const result = [];
    for (let server = 0; server < k; server++) {
        if (handled[server] === maximum) result.push(server);
    }
    return result;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function busiestServers(k: number, arrival: number[], load: number[]): number[] {
    const available: number[] = Array.from({ length: k }, (_, i) => i);
    const running: Array<[number, number]> = [];
    const handled: number[] = new Array(k).fill(0);

    const pushRunning = (completion: number, server: number): void => {
        running.push([completion, server]);
        let index = running.length - 1;
        while (index > 0) {
            const parent = Math.floor((index - 1) / 2);
            const a = running[index];
            const b = running[parent];
            if (a[0] > b[0] || (a[0] === b[0] && a[1] >= b[1])) break;
            running[index] = b;
            running[parent] = a;
            index = parent;
        }
    };

    const popRunning = (): [number, number] => {
        const root = running[0];
        const last = running.pop()!;
        if (running.length > 0) {
            running[0] = last;
            let index = 0;
            while (true) {
                const left = index * 2 + 1;
                const right = left + 1;
                let smallest = index;
                if (left < running.length && (running[left][0] < running[smallest][0] || (running[left][0] === running[smallest][0] && running[left][1] < running[smallest][1]))) smallest = left;
                if (right < running.length && (running[right][0] < running[smallest][0] || (running[right][0] === running[smallest][0] && running[right][1] < running[smallest][1]))) smallest = right;
                if (smallest === index) break;
                [running[index], running[smallest]] = [running[smallest], running[index]];
                index = smallest;
            }
        }
        return root;
    };

    for (let i = 0; i < arrival.length; i++) {
        const time = arrival[i];
        while (running.length > 0 && running[0][0] <= time) {
            const [, server] = popRunning();
            let low = 0;
            let high = available.length;
            while (low < high) {
                const mid = (low + high) >>> 1;
                if (available[mid] < server) low = mid + 1;
                else high = mid;
            }
            available.splice(low, 0, server);
        }

        if (available.length === 0) continue;

        const preferred = i % k;
        let low = 0;
        let high = available.length;
        while (low < high) {
            const mid = (low + high) >>> 1;
            if (available[mid] < preferred) low = mid + 1;
            else high = mid;
        }
        const index = low === available.length ? 0 : low;
        const server = available.splice(index, 1)[0];
        handled[server]++;
        pushRunning(time + load[i], server);
    }

    const maximum = Math.max(...handled);
    return handled.map((count, server) => count === maximum ? server : -1).filter(server => server !== -1);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer $k
     * @param Integer[] $arrival
     * @param Integer[] $load
     * @return Integer[]
     */
    function busiestServers($k, $arrival, $load) {
        $available = range(0, $k - 1);
        $running = [];
        $handled = array_fill(0, $k, 0);

        $push = function ($completion, $server) use (&$running) {
            $running[] = [$completion, $server];
            $index = count($running) - 1;
            while ($index > 0) {
                $parent = intdiv($index - 1, 2);
                if ($running[$index][0] > $running[$parent][0] || ($running[$index][0] === $running[$parent][0] && $running[$index][1] >= $running[$parent][1])) {
                    break;
                }
                [$running[$index], $running[$parent]] = [$running[$parent], $running[$index]];
                $index = $parent;
            }
        };

        $pop = function () use (&$running) {
            $root = $running[0];
            $last = array_pop($running);
            if (count($running) > 0) {
                $running[0] = $last;
                $index = 0;
                $size = count($running);
                while (true) {
                    $left = $index * 2 + 1;
                    $right = $left + 1;
                    $smallest = $index;
                    if ($left < $size && ($running[$left][0] < $running[$smallest][0] || ($running[$left][0] === $running[$smallest][0] && $running[$left][1] < $running[$smallest][1]))) {
                        $smallest = $left;
                    }
                    if ($right < $size && ($running[$right][0] < $running[$smallest][0] || ($running[$right][0] === $running[$smallest][0] && $running[$right][1] < $running[$smallest][1]))) {
                        $smallest = $right;
                    }
                    if ($smallest === $index) {
                        break;
                    }
                    [$running[$index], $running[$smallest]] = [$running[$smallest], $running[$index]];
                    $index = $smallest;
                }
            }
            return $root;
        };

        for ($i = 0; $i < count($arrival); $i++) {
            $time = $arrival[$i];
            while (count($running) > 0 && $running[0][0] <= $time) {
                [, $server] = $pop();
                $low = 0;
                $high = count($available);
                while ($low < $high) {
                    $mid = intdiv($low + $high, 2);
                    if ($available[$mid] < $server) {
                        $low = $mid + 1;
                    } else {
                        $high = $mid;
                    }
                }
                array_splice($available, $low, 0, [$server]);
            }

            if (count($available) === 0) {
                continue;
            }

            $preferred = $i % $k;
            $low = 0;
            $high = count($available);
            while ($low < $high) {
                $mid = intdiv($low + $high, 2);
                if ($available[$mid] < $preferred) {
                    $low = $mid + 1;
                } else {
                    $high = $mid;
                }
            }
            $index = $low === count($available) ? 0 : $low;
            $server = $available[$index];
            array_splice($available, $index, 1);
            $handled[$server]++;
            $push($time + $load[$i], $server);
        }

        $maximum = max($handled);
        $result = [];
        foreach ($handled as $server => $count) {
            if ($count === $maximum) {
                $result[] = $server;
            }
        }
        return $result;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func busiestServers(_ k: Int, _ arrival: [Int], _ load: [Int]) -> [Int] {
        var available = Array(0..<k)
        var running: [(completion: Int, server: Int)] = []
        var handled = Array(repeating: 0, count: k)

        func less(_ a: (completion: Int, server: Int), _ b: (completion: Int, server: Int)) -> Bool {
            if a.completion != b.completion { return a.completion < b.completion }
            return a.server < b.server
        }

        func push(_ completion: Int, _ server: Int) {
            running.append((completion, server))
            var index = running.count - 1
            while index > 0 {
                let parent = (index - 1) / 2
                if !less(running[index], running[parent]) { break }
                running.swapAt(index, parent)
                index = parent
            }
        }

        func pop() -> (completion: Int, server: Int) {
            let root = running[0]
            let last = running.removeLast()
            if !running.isEmpty {
                running[0] = last
                var index = 0
                while true {
                    let left = index * 2 + 1
                    let right = left + 1
                    var smallest = index
                    if left < running.count && less(running[left], running[smallest]) { smallest = left }
                    if right < running.count && less(running[right], running[smallest]) { smallest = right }
                    if smallest == index { break }
                    running.swapAt(index, smallest)
                    index = smallest
                }
            }
            return root
        }

        for i in 0..<arrival.count {
            let time = arrival[i]
            while !running.isEmpty && running[0].completion <= time {
                let server = pop().server
                var low = 0
                var high = available.count
                while low < high {
                    let mid = (low + high) / 2
                    if available[mid] < server { low = mid + 1 }
                    else { high = mid }
                }
                available.insert(server, at: low)
            }

            if available.isEmpty { continue }

            let preferred = i % k
            var low = 0
            var high = available.count
            while low < high {
                let mid = (low + high) / 2
                if available[mid] < preferred { low = mid + 1 }
                else { high = mid }
            }
            let index = low == available.count ? 0 : low
            let server = available.remove(at: index)
            handled[server] += 1
            push(time + load[i], server)
        }

        let maximum = handled.max()!
        return handled.indices.filter { handled[$0] == maximum }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun busiestServers(k: Int, arrival: IntArray, load: IntArray): List<Int> {
        val available = java.util.TreeSet<Int>()
        for (server in 0 until k) available.add(server)
        val running = java.util.PriorityQueue<Pair<Int, Int>>(compareBy<Pair<Int, Int>> { it.first }.thenBy { it.second })
        val handled = IntArray(k)

        for (i in arrival.indices) {
            val time = arrival[i]
            while (running.isNotEmpty() && running.peek().first <= time) {
                available.add(running.poll().second)
            }

            if (available.isEmpty()) continue

            val preferred = i % k
            val server = available.ceiling(preferred) ?: available.first()
            available.remove(server)
            handled[server]++
            running.add(Pair(time + load[i], server))
        }

        val maximum = handled.maxOrNull() ?: 0
        return handled.indices.filter { handled[it] == maximum }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  List<int> busiestServers(int k, List<int> arrival, List<int> load) {
    final available = List<int>.generate(k, (i) => i);
    final running = <List<int>>[];
    final handled = List<int>.filled(k, 0);

    void push(List<int> item) {
      running.add(item);
      var index = running.length - 1;
      while (index > 0) {
        final parent = (index - 1) ~/ 2;
        if (running[parent][0] <= running[index][0]) break;
        final temp = running[parent];
        running[parent] = running[index];
        running[index] = temp;
        index = parent;
      }
    }

    List<int> pop() {
      final result = running[0];
      final last = running.removeLast();
      if (running.isNotEmpty) {
        running[0] = last;
        var index = 0;
        while (true) {
          final left = index * 2 + 1;
          final right = left + 1;
          var smallest = index;
          if (left < running.length && running[left][0] < running[smallest][0]) {
            smallest = left;
          }
          if (right < running.length && running[right][0] < running[smallest][0]) {
            smallest = right;
          }
          if (smallest == index) break;
          final temp = running[index];
          running[index] = running[smallest];
          running[smallest] = temp;
          index = smallest;
        }
      }
      return result;
    }

    for (var i = 0; i < arrival.length; i++) {
      while (running.isNotEmpty && running[0][0] <= arrival[i]) {
        final server = pop()[1];
        var low = 0;
        var high = available.length;
        while (low < high) {
          final mid = (low + high) ~/ 2;
          if (available[mid] < server) {
            low = mid + 1;
          } else {
            high = mid;
          }
        }
        available.insert(low, server);
      }

      if (available.isEmpty) continue;

      final preferred = i % k;
      var low = 0;
      var high = available.length;
      while (low < high) {
        final mid = (low + high) ~/ 2;
        if (available[mid] < preferred) {
          low = mid + 1;
        } else {
          high = mid;
        }
      }
      if (low == available.length) low = 0;
      final server = available.removeAt(low);
      handled[server]++;
      push([arrival[i] + load[i], server]);
    }

    final maximum = handled.reduce((a, b) => a > b ? a : b);
    return List<int>.generate(k, (i) => i).where((i) => handled[i] == maximum).toList();
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func busiestServers(k int, arrival []int, load []int) []int {
	available := make([]int, k)
	for i := range available {
		available[i] = i
	}
	handled := make([]int, k)
	running := make([][2]int, 0, len(arrival))

	push := func(item [2]int) {}
	_ = push

	var heapPush func([2]int)
	heapPush = func(item [2]int) {
		running = append(running, item)
		index := len(running) - 1
		for index > 0 {
			parent := (index - 1) / 2
			if running[parent][0] <= running[index][0] {
				break
			}
			running[parent], running[index] = running[index], running[parent]
			index = parent
		}
	}

	heapPop := func() [2]int {
		result := running[0]
		last := running[len(running)-1]
		running = running[:len(running)-1]
		if len(running) > 0 {
			running[0] = last
			index := 0
			for {
				left := index*2 + 1
				right := left + 1
				smallest := index
				if left < len(running) && running[left][0] < running[smallest][0] {
					smallest = left
				}
				if right < len(running) && running[right][0] < running[smallest][0] {
					smallest = right
				}
				if smallest == index {
					break
				}
				running[index], running[smallest] = running[smallest], running[index]
				index = smallest
			}
		}
		return result
	}

	insertAvailable := func(server int) {
		low, high := 0, len(available)
		for low < high {
			mid := (low + high) / 2
			if available[mid] < server {
				low = mid + 1
			} else {
				high = mid
			}
		}
		available = append(available, 0)
		copy(available[low+1:], available[low:])
		available[low] = server
	}

	for i, time := range arrival {
		for len(running) > 0 && running[0][0] <= time {
			server := heapPop()[1]
			insertAvailable(server)
		}
		if len(available) == 0 {
			continue
		}
		preferred := i % k
		low, high := 0, len(available)
		for low < high {
			mid := (low + high) / 2
			if available[mid] < preferred {
				low = mid + 1
			} else {
				high = mid
			}
		}
		if low == len(available) {
			low = 0
		}
		server := available[low]
		available = append(available[:low], available[low+1:]...)
		handled[server]++
		heapPush([2]int{time + load[i], server})
	}

	maximum := 0
	for _, count := range handled {
		if count > maximum {
			maximum = count
		}
	}
	result := make([]int, 0)
	for server, count := range handled {
		if count == maximum {
			result = append(result, server)
		}
	}
	return result
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer} k
# @param {Integer[]} arrival
# @param {Integer[]} load
# @return {Integer[]}
def busiest_servers(k, arrival, load)
  available = (0...k).to_a
  running = []
  handled = Array.new(k, 0)

  push = lambda do |item|
    running << item
    index = running.length - 1
    while index > 0
      parent = (index - 1) / 2
      break if running[parent][0] <= running[index][0]
      running[parent], running[index] = running[index], running[parent]
      index = parent
    end
  end

  pop = lambda do
    result = running[0]
    last = running.pop
    unless running.empty?
      running[0] = last
      index = 0
      loop do
        left = index * 2 + 1
        right = left + 1
        smallest = index
        smallest = left if left < running.length && running[left][0] < running[smallest][0]
        smallest = right if right < running.length && running[right][0] < running[smallest][0]
        break if smallest == index
        running[index], running[smallest] = running[smallest], running[index]
        index = smallest
      end
    end
    result
  end

  arrival.each_index do |i|
    while !running.empty? && running[0][0] <= arrival[i]
      server = pop.call[1]
      low = 0
      high = available.length
      while low < high
        mid = (low + high) / 2
        if available[mid] < server
          low = mid + 1
        else
          high = mid
        end
      end
      available.insert(low, server)
    end

    next if available.empty?

    preferred = i % k
    low = 0
    high = available.length
    while low < high
      mid = (low + high) / 2
      if available[mid] < preferred
        low = mid + 1
      else
        high = mid
      end
    end
    low = 0 if low == available.length
    server = available.delete_at(low)
    handled[server] += 1
    push.call([arrival[i] + load[i], server])
  end

  maximum = handled.max
  handled.each_index.select { |server| handled[server] == maximum }
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def busiestServers(k: Int, arrival: Array[Int], load: Array[Int]): List[Int] = {
        val available = scala.collection.mutable.ArrayBuffer.from(0 until k)
        val handled = Array.fill(k)(0)
        val running = scala.collection.mutable.ArrayBuffer.empty[(Int, Int)]

        def push(item: (Int, Int)): Unit = {
            running += item
            var index = running.length - 1
            while (index > 0) {
                val parent = (index - 1) / 2
                if (running(parent)._1 <= running(index)._1) index = 0
                else {
                    val temp = running(parent)
                    running(parent) = running(index)
                    running(index) = temp
                    index = parent
                }
            }
        }

        def pop(): (Int, Int) = {
            val result = running(0)
            val last = running.remove(running.length - 1)
            if (running.nonEmpty) {
                running(0) = last
                var index = 0
                var continue = true
                while (continue) {
                    val left = index * 2 + 1
                    val right = left + 1
                    var smallest = index
                    if (left < running.length && running(left)._1 < running(smallest)._1) smallest = left
                    if (right < running.length && running(right)._1 < running(smallest)._1) smallest = right
                    if (smallest == index) continue = false
                    else {
                        val temp = running(index)
                        running(index) = running(smallest)
                        running(smallest) = temp
                        index = smallest
                    }
                }
            }
            result
        }

        def insertAvailable(server: Int): Unit = {
            var low = 0
            var high = available.length
            while (low < high) {
                val mid = (low + high) / 2
                if (available(mid) < server) low = mid + 1 else high = mid
            }
            available.insert(low, server)
        }

        for (i <- arrival.indices) {
            while (running.nonEmpty && running(0)._1 <= arrival(i)) {
                insertAvailable(pop()._2)
            }
            if (available.nonEmpty) {
                val preferred = i % k
                var low = 0
                var high = available.length
                while (low < high) {
                    val mid = (low + high) / 2
                    if (available(mid) < preferred) low = mid + 1 else high = mid
                }
                if (low == available.length) low = 0
                val server = available.remove(low)
                handled(server) += 1
                push((arrival(i) + load(i), server))
            }
        }

        val maximum = handled.max
        handled.indices.filter(server => handled(server) == maximum).toList
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn busiest_servers(k: i32, arrival: Vec<i32>, load: Vec<i32>) -> Vec<i32> {
        use std::cmp::Reverse;
        use std::collections::BTreeSet;
        use std::collections::BinaryHeap;

        let k = k as usize;
        let mut available: BTreeSet<usize> = (0..k).collect();
        let mut running: BinaryHeap<Reverse<(i64, usize)>> = BinaryHeap::new();
        let mut handled = vec![0; k];

        for (i, &time) in arrival.iter().enumerate() {
            let time = time as i64;
            while let Some(&Reverse((end, server))) = running.peek() {
                if end > time {
                    break;
                }
                running.pop();
                available.insert(server);
            }

            if available.is_empty() {
                continue;
            }

            let preferred = i % k;
            let server = available
                .range(preferred..)
                .next()
                .copied()
                .or_else(|| available.iter().next().copied())
                .unwrap();
            available.remove(&server);
            handled[server] += 1;
            running.push(Reverse((time + load[i] as i64, server)));
        }

        let maximum = *handled.iter().max().unwrap();
        handled
            .iter()
            .enumerate()
            .filter_map(|(server, &count)| {
                if count == maximum {
                    Some(server as i32)
                } else {
                    None
                }
            })
            .collect()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (busiest-servers k arrival load)
  (-> exact-integer? (listof exact-integer?) (listof exact-integer?) (listof exact-integer?))
  (define available (build-vector k values))
  (define running '())
  (define handled (make-vector k 0))
  (define (insert-available server)
    (let loop ([before '()] [after available])
      (cond
        [(null? after) (set! available (append (reverse before) (list server)))]
        [(< server (car after))
         (set! available (append (reverse before) (cons server after)))]
        [else (loop (cons (car after) before) (cdr after))])))
  (define (pop-running)
    (let ([server (cadar running)])
      (set! running (cdr running))
      server))
  (define (push-running end server)
    (let loop ([before '()] [after running])
      (cond
        [(null? after) (set! running (append (reverse before) (list (list end server))))]
        [(< end (caar after))
         (set! running (append (reverse before) (cons (list end server) after)))]
        [else (loop (cons (car after) before) (cdr after))])))
  (define (process requests times i)
    (unless (null? requests)
      (let ([time (car requests)])
        (let release ()
          (when (and (pair? running) (<= (caar running) time))
            (insert-available (pop-running))
            (release)))
        (unless (null? available)
          (let* ([preferred (modulo i k)]
                 [server (or (findf (lambda (s) (>= s preferred)) available)
                             (car available))])
            (set! available (remove server available))
            (vector-set! handled server (add1 (vector-ref handled server)))
            (push-running (+ time (car times)) server)))
        (process (cdr requests) (cdr times) (add1 i)))))
  (process arrival load 0)
  (define maximum (apply max (vector->list handled)))
  (for/list ([server (in-range k)]
             #:when (= (vector-ref handled server) maximum))
    server))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec busiest_servers(K :: integer(), Arrival :: [integer()], Load :: [integer()]) -> [integer()].
busiest_servers(K, Arrival, Load) ->
  Available = gb_sets:from_list(lists:seq(0, K - 1)),
  {Running, _Available, Counts} = process_requests(Arrival, Load, 0, K, [], Available, array:new(K, {default, 0})),
  _ = Running,
  MaxCount = lists:max(array:to_list(Counts)),
  [Server || Server <- lists:seq(0, K - 1), array:get(Server, Counts) =:= MaxCount].

process_requests([], [], _I, _K, Running, Available, Counts) ->
  {Running, Available, Counts};
process_requests([Time | Times], [Duration | Durations], I, K, Running, Available, Counts) ->
  {Ready, Busy} = release_servers(Running, Time, Available),
  case gb_sets:is_empty(Ready) of
    true -> process_requests(Times, Durations, I + 1, K, Busy, Ready, Counts);
    false ->
      Preferred = I rem K,
      Server = case gb_sets:iterator_from(Preferred, Ready) of
        Iter ->
          case gb_sets:next(Iter) of
            none -> gb_sets:smallest(Ready);
            {Value, _} -> Value
          end
      end,
      NewAvailable = gb_sets:delete(Server, Ready),
      NewCounts = array:set(Server, array:get(Server, Counts) + 1, Counts),
      Completion = Time + Duration,
      NewRunning = lists:sort([{Completion, Server} | Busy]),
      process_requests(Times, Durations, I + 1, K, NewRunning, NewAvailable, NewCounts)
  end.

release_servers([{End, Server} | Rest], Time, Available) when End =< Time ->
  release_servers(Rest, Time, gb_sets:add(Server, Available));
release_servers(Running, _Time, Available) ->
  {Available, Running}.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec busiest_servers(k :: integer, arrival :: [integer], load :: [integer]) :: [integer]
  def busiest_servers(k, arrival, load) do
    available = 0..(k - 1) |> MapSet.new()
    {_, _, handled} = process_requests(arrival, load, 0, k, [], available, List.duplicate(0, k))
    maximum = Enum.max(handled)
    handled
    |> Enum.with_index()
    |> Enum.filter(fn {count, _server} -> count == maximum end)
    |> Enum.map(fn {_count, server} -> server end)
  end

  defp process_requests([], [], _i, _k, running, available, handled) do
    {running, available, handled}
  end

  defp process_requests([time | times], [duration | durations], i, k, running, available, handled) do
    {ready, busy} = release_servers(running, time, available)

    if MapSet.size(ready) == 0 do
      process_requests(times, durations, i + 1, k, busy, ready, handled)
    else
      preferred = rem(i, k)
      server =
        ready
        |> Enum.filter(&(&1 >= preferred))
        |> Enum.min(fn -> Enum.min(ready) end)

      new_available = MapSet.delete(ready, server)
      new_handled = List.update_at(handled, server, &(&1 + 1))
      new_running = Enum.sort([{time + duration, server} | busy])
      process_requests(times, durations, i + 1, k, new_running, new_available, new_handled)
    end
  end

  defp release_servers([{finish, server} | rest], time, available) when finish <= time do
    release_servers(rest, time, MapSet.put(available, server))
  end

  defp release_servers(running, _time, available) do
    {available, running}
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n log k), where n is the number of requests. Each request and server availability update performs heap or ordered-set operations.
- **Space Complexity:** O(k), for the available server set, running-request heap, and request counts.
