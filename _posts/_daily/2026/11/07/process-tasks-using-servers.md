---
layout: post
title: "Process Tasks Using Servers"
date: 2026-11-07 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Heap (Priority Queue)"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/process-tasks-using-servers/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    vector<int> assignTasks(vector<int>& servers,\
        \ vector<int>& tasks) {\n        using Available = pair<int, int>;\n       \
        \ using Busy = pair<long long, int>;\n        priority_queue<Available, vector<Available>,\
        \ greater<Available>> available;\n        priority_queue<Busy, vector<Busy>,\
        \ greater<Busy>> busy;\n        for (int i = 0; i < static_cast<int>(servers.size());\
        \ ++i) {\n            available.push({servers[i], i});\n        }\n        vector<int>\
        \ ans(tasks.size());\n        long long time = 0;\n        for (int j = 0; j\
        \ < static_cast<int>(tasks.size()); ++j) {\n            time = max(time, static_cast<long\
        \ long>(j));\n            while (!busy.empty() && busy.top().first <= time)\
        \ {\n                int index = busy.top().second;\n                busy.pop();\n\
        \                available.push({servers[index], index});\n            }\n \
        \           if (available.empty()) {\n                time = busy.top().first;\n\
        \                while (!busy.empty() && busy.top().first <= time) {\n     \
        \               int index = busy.top().second;\n                    busy.pop();\n\
        \                    available.push({servers[index], index});\n            \
        \    }\n            }\n            auto [weight, index] = available.top();\n\
        \            available.pop();\n            ans[j] = index;\n            busy.push({time\
        \ + tasks[j], index});\n        }\n        return ans;\n    }\n};"
      java: "class Solution {\n    public int[] assignTasks(int[] servers, int[] tasks)\
        \ {\n        PriorityQueue<Integer> available = new PriorityQueue<>((a, b) ->\
        \ {\n            int byWeight = Integer.compare(servers[a], servers[b]);\n \
        \           return byWeight != 0 ? byWeight : Integer.compare(a, b);\n     \
        \   });\n        PriorityQueue<long[]> busy = new PriorityQueue<>((a, b) ->\
        \ {\n            int byTime = Long.compare(a[0], b[0]);\n            return\
        \ byTime != 0 ? byTime : Integer.compare((int) a[1], (int) b[1]);\n        });\n\
        \        for (int i = 0; i < servers.length; i++) {\n            available.offer(i);\n\
        \        }\n        int[] ans = new int[tasks.length];\n        long time =\
        \ 0;\n        for (int j = 0; j < tasks.length; j++) {\n            time = Math.max(time,\
        \ j);\n            while (!busy.isEmpty() && busy.peek()[0] <= time) {\n   \
        \             available.offer((int) busy.poll()[1]);\n            }\n      \
        \      if (available.isEmpty()) {\n                time = busy.peek()[0];\n\
        \                while (!busy.isEmpty() && busy.peek()[0] <= time) {\n     \
        \               available.offer((int) busy.poll()[1]);\n                }\n\
        \            }\n            int server = available.poll();\n            ans[j]\
        \ = server;\n            busy.offer(new long[]{time + tasks[j], server});\n\
        \        }\n        return ans;\n    }\n}"
      python: "import heapq\n\nclass Solution(object):\n    def assignTasks(self, servers,\
        \ tasks):\n        \"\"\"\n        :type servers: List[int]\n        :type tasks:\
        \ List[int]\n        :rtype: List[int]\n        \"\"\"\n        available =\
        \ [(weight, index) for index, weight in enumerate(servers)]\n        heapq.heapify(available)\n\
        \        busy = []\n        ans = [0] * len(tasks)\n        time = 0\n     \
        \   for j, duration in enumerate(tasks):\n            time = max(time, j)\n\
        \            while busy and busy[0][0] <= time:\n                finish, weight,\
        \ index = heapq.heappop(busy)\n                heapq.heappush(available, (weight,\
        \ index))\n            if not available:\n                time = busy[0][0]\n\
        \                while busy and busy[0][0] <= time:\n                    finish,\
        \ weight, index = heapq.heappop(busy)\n                    heapq.heappush(available,\
        \ (weight, index))\n            weight, index = heapq.heappop(available)\n \
        \           ans[j] = index\n            heapq.heappush(busy, (time + duration,\
        \ weight, index))\n        return ans"
      python3: "import heapq\n\nclass Solution:\n    def assignTasks(self, servers:\
        \ list[int], tasks: list[int]) -> list[int]:\n        available = [(weight,\
        \ index) for index, weight in enumerate(servers)]\n        heapq.heapify(available)\n\
        \        busy = []\n        ans = [0] * len(tasks)\n        time = 0\n     \
        \   for j, duration in enumerate(tasks):\n            time = max(time, j)\n\
        \            while busy and busy[0][0] <= time:\n                finish, weight,\
        \ index = heapq.heappop(busy)\n                heapq.heappush(available, (weight,\
        \ index))\n            if not available:\n                time = busy[0][0]\n\
        \                while busy and busy[0][0] <= time:\n                    finish,\
        \ weight, index = heapq.heappop(busy)\n                    heapq.heappush(available,\
        \ (weight, index))\n            weight, index = heapq.heappop(available)\n \
        \           ans[j] = index\n            heapq.heappush(busy, (time + duration,\
        \ weight, index))\n        return ans"
      c: "#include <stdlib.h>\n\ntypedef struct {\n    long long time;\n    int weight;\n\
        \    int index;\n} Node;\n\nstatic int availableLess(Node a, Node b) {\n   \
        \ if (a.weight != b.weight) return a.weight < b.weight;\n    return a.index\
        \ < b.index;\n}\n\nstatic int busyLess(Node a, Node b) {\n    if (a.time !=\
        \ b.time) return a.time < b.time;\n    return a.index < b.index;\n}\n\nstatic\
        \ void push(Node* heap, int* size, Node value, int (*less)(Node, Node)) {\n\
        \    int i = (*size)++;\n    while (i > 0) {\n        int parent = (i - 1) /\
        \ 2;\n        if (!less(value, heap[parent])) break;\n        heap[i] = heap[parent];\n\
        \        i = parent;\n    }\n    heap[i] = value;\n}\n\nstatic Node pop(Node*\
        \ heap, int* size, int (*less)(Node, Node)) {\n    Node result = heap[0];\n\
        \    Node last = heap[--(*size)];\n    if (*size == 0) return result;\n    int\
        \ i = 0;\n    while (2 * i + 1 < *size) {\n        int child = 2 * i + 1;\n\
        \        if (child + 1 < *size && less(heap[child + 1], heap[child])) child++;\n\
        \        if (!less(heap[child], last)) break;\n        heap[i] = heap[child];\n\
        \        i = child;\n    }\n    heap[i] = last;\n    return result;\n}\n\nint*\
        \ assignTasks(int* servers, int serversSize, int* tasks, int tasksSize, int*\
        \ returnSize) {\n    Node* available = malloc(sizeof(Node) * serversSize);\n\
        \    Node* busy = malloc(sizeof(Node) * serversSize);\n    int availableSize\
        \ = 0;\n    int busySize = 0;\n    int* ans = malloc(sizeof(int) * tasksSize);\n\
        \    *returnSize = tasksSize;\n    for (int i = 0; i < serversSize; i++) {\n\
        \        Node server = {0, servers[i], i};\n        push(available, &availableSize,\
        \ server, availableLess);\n    }\n    long long time = 0;\n    for (int j =\
        \ 0; j < tasksSize; j++) {\n        if (time < j) time = j;\n        while (busySize\
        \ > 0 && busy[0].time <= time) {\n            Node server = pop(busy, &busySize,\
        \ busyLess);\n            push(available, &availableSize, server, availableLess);\n\
        \        }\n        if (availableSize == 0) {\n            time = busy[0].time;\n\
        \            while (busySize > 0 && busy[0].time <= time) {\n              \
        \  Node server = pop(busy, &busySize, busyLess);\n                push(available,\
        \ &availableSize, server, availableLess);\n            }\n        }\n      \
        \  Node server = pop(available, &availableSize, availableLess);\n        ans[j]\
        \ = server.index;\n        server.time = time + tasks[j];\n        push(busy,\
        \ &busySize, server, busyLess);\n    }\n    free(available);\n    free(busy);\n\
        \    return ans;\n}"
      csharp: "public class Solution {\n    public int[] AssignTasks(int[] servers,\
        \ int[] tasks) {\n        int n = servers.Length;\n        var available = new\
        \ PriorityQueue<int, (int weight, int index)>();\n        for (int i = 0; i\
        \ < n; i++) {\n            available.Enqueue(i, (servers[i], i));\n        }\n\
        \n        var busy = new PriorityQueue<(int index, int weight), (long finish,\
        \ int weight, int index)>();\n        int[] answer = new int[tasks.Length];\n\
        \        long time = 0;\n\n        for (int j = 0; j < tasks.Length; j++) {\n\
        \            time = Math.Max(time, j);\n            while (busy.Count > 0 &&\
        \ busy.Peek().finish <= time) {\n                var entry = busy.Dequeue();\n\
        \                available.Enqueue(entry.index, (entry.weight, entry.index));\n\
        \            }\n\n            if (available.Count == 0) {\n                time\
        \ = busy.Peek().finish;\n                while (busy.Count > 0 && busy.Peek().finish\
        \ <= time) {\n                    var entry = busy.Dequeue();\n            \
        \        available.Enqueue(entry.index, (entry.weight, entry.index));\n    \
        \            }\n            }\n\n            int serverIndex = available.Dequeue();\n\
        \            answer[j] = serverIndex;\n            busy.Enqueue((serverIndex,\
        \ servers[serverIndex]), (time + tasks[j], servers[serverIndex], serverIndex));\n\
        \        }\n\n        return answer;\n    }\n}"
      javascript: "/**\n * @param {number[]} servers\n * @param {number[]} tasks\n *\
        \ @return {number[]}\n */\nvar assignTasks = function(servers, tasks) {\n  \
        \  class MinHeap {\n        constructor(compare) {\n            this.data =\
        \ [];\n            this.compare = compare;\n        }\n\n        get size()\
        \ {\n            return this.data.length;\n        }\n\n        peek() {\n \
        \           return this.data[0];\n        }\n\n        push(value) {\n     \
        \       const data = this.data;\n            data.push(value);\n           \
        \ let index = data.length - 1;\n            while (index > 0) {\n          \
        \      const parent = (index - 1) >> 1;\n                if (this.compare(data[parent],\
        \ value) <= 0) break;\n                data[index] = data[parent];\n       \
        \         index = parent;\n            }\n            data[index] = value;\n\
        \        }\n\n        pop() {\n            const data = this.data;\n       \
        \     const root = data[0];\n            const last = data.pop();\n        \
        \    if (data.length > 0) {\n                let index = 0;\n              \
        \  while (true) {\n                    let child = index * 2 + 1;\n        \
        \            if (child >= data.length) break;\n                    if (child\
        \ + 1 < data.length && this.compare(data[child + 1], data[child]) < 0) child++;\n\
        \                    if (this.compare(last, data[child]) <= 0) break;\n    \
        \                data[index] = data[child];\n                    index = child;\n\
        \                }\n                data[index] = last;\n            }\n   \
        \         return root;\n        }\n    }\n\n    const available = new MinHeap((a,\
        \ b) => a.weight - b.weight || a.index - b.index);\n    const busy = new MinHeap((a,\
        \ b) => a.finish - b.finish || a.weight - b.weight || a.index - b.index);\n\
        \    for (let i = 0; i < servers.length; i++) available.push({ weight: servers[i],\
        \ index: i });\n\n    const answer = new Array(tasks.length);\n    let time\
        \ = 0;\n    for (let j = 0; j < tasks.length; j++) {\n        time = Math.max(time,\
        \ j);\n        while (busy.size > 0 && busy.peek().finish <= time) {\n     \
        \       const server = busy.pop();\n            available.push({ weight: server.weight,\
        \ index: server.index });\n        }\n        if (available.size === 0) {\n\
        \            time = busy.peek().finish;\n            while (busy.size > 0 &&\
        \ busy.peek().finish <= time) {\n                const server = busy.pop();\n\
        \                available.push({ weight: server.weight, index: server.index\
        \ });\n            }\n        }\n        const server = available.pop();\n \
        \       answer[j] = server.index;\n        busy.push({ finish: time + tasks[j],\
        \ weight: server.weight, index: server.index });\n    }\n    return answer;\n\
        };"
      typescript: "function assignTasks(servers: number[], tasks: number[]): number[]\
        \ {\n    type Server = { weight: number; index: number };\n    type BusyServer\
        \ = { finish: number; weight: number; index: number };\n\n    class MinHeap<T>\
        \ {\n        private data: T[] = [];\n        constructor(private compare: (a:\
        \ T, b: T) => number) {}\n\n        get size(): number {\n            return\
        \ this.data.length;\n        }\n\n        peek(): T {\n            return this.data[0];\n\
        \        }\n\n        push(value: T): void {\n            const data = this.data;\n\
        \            data.push(value);\n            let index = data.length - 1;\n \
        \           while (index > 0) {\n                const parent = (index - 1)\
        \ >> 1;\n                if (this.compare(data[parent], value) <= 0) break;\n\
        \                data[index] = data[parent];\n                index = parent;\n\
        \            }\n            data[index] = value;\n        }\n\n        pop():\
        \ T {\n            const data = this.data;\n            const root = data[0];\n\
        \            const last = data.pop() as T;\n            if (data.length > 0)\
        \ {\n                let index = 0;\n                while (true) {\n      \
        \              let child = index * 2 + 1;\n                    if (child >=\
        \ data.length) break;\n                    if (child + 1 < data.length && this.compare(data[child\
        \ + 1], data[child]) < 0) child++;\n                    if (this.compare(last,\
        \ data[child]) <= 0) break;\n                    data[index] = data[child];\n\
        \                    index = child;\n                }\n                data[index]\
        \ = last;\n            }\n            return root;\n        }\n    }\n\n   \
        \ const available = new MinHeap<Server>((a, b) => a.weight - b.weight || a.index\
        \ - b.index);\n    const busy = new MinHeap<BusyServer>((a, b) => a.finish -\
        \ b.finish || a.weight - b.weight || a.index - b.index);\n    for (let i = 0;\
        \ i < servers.length; i++) available.push({ weight: servers[i], index: i });\n\
        \n    const answer = new Array<number>(tasks.length);\n    let time = 0;\n \
        \   for (let j = 0; j < tasks.length; j++) {\n        time = Math.max(time,\
        \ j);\n        while (busy.size > 0 && busy.peek().finish <= time) {\n     \
        \       const server = busy.pop();\n            available.push({ weight: server.weight,\
        \ index: server.index });\n        }\n        if (available.size === 0) {\n\
        \            time = busy.peek().finish;\n            while (busy.size > 0 &&\
        \ busy.peek().finish <= time) {\n                const server = busy.pop();\n\
        \                available.push({ weight: server.weight, index: server.index\
        \ });\n            }\n        }\n        const server = available.pop();\n \
        \       answer[j] = server.index;\n        busy.push({ finish: time + tasks[j],\
        \ weight: server.weight, index: server.index });\n    }\n    return answer;\n\
        };"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $servers\n     * @param\
        \ Integer[] $tasks\n     * @return Integer[]\n     */\n    function assignTasks($servers,\
        \ $tasks) {\n        $available = new SplPriorityQueue();\n        $available->setExtractFlags(SplPriorityQueue::EXTR_DATA);\n\
        \        foreach ($servers as $index => $weight) {\n            $available->insert([$weight,\
        \ $index], [-$weight, -$index]);\n        }\n\n        $busy = new SplPriorityQueue();\n\
        \        $busy->setExtractFlags(SplPriorityQueue::EXTR_DATA);\n        $answer\
        \ = array_fill(0, count($tasks), 0);\n        $time = 0;\n\n        foreach\
        \ ($tasks as $j => $duration) {\n            $time = max($time, $j);\n     \
        \       while (!$busy->isEmpty()) {\n                $busy->top();\n       \
        \         $entry = $busy->current();\n                if ($entry[0] > $time)\
        \ break;\n                $entry = $busy->extract();\n                $available->insert([$entry[1],\
        \ $entry[2]], [-$entry[1], -$entry[2]]);\n            }\n\n            if ($available->isEmpty())\
        \ {\n                $busy->top();\n                $time = $busy->current()[0];\n\
        \                while (!$busy->isEmpty()) {\n                    $busy->top();\n\
        \                    if ($busy->current()[0] > $time) break;\n             \
        \       $entry = $busy->extract();\n                    $available->insert([$entry[1],\
        \ $entry[2]], [-$entry[1], -$entry[2]]);\n                }\n            }\n\
        \n            [$weight, $index] = $available->extract();\n            $answer[$j]\
        \ = $index;\n            $busy->insert([$time + $duration, $weight, $index],\
        \ [-($time + $duration), -$weight, -$index]);\n        }\n\n        return $answer;\n\
        \    }\n}"
      swift: "class Solution {\n    func assignTasks(_ servers: [Int], _ tasks: [Int])\
        \ -> [Int] {\n        struct Server {\n            let weight: Int\n       \
        \     let index: Int\n        }\n\n        struct BusyServer {\n           \
        \ let finish: Int\n            let weight: Int\n            let index: Int\n\
        \        }\n\n        struct MinHeap<Element> {\n            var elements: [Element]\
        \ = []\n            let orderedBefore: (Element, Element) -> Bool\n\n      \
        \      var isEmpty: Bool { elements.isEmpty }\n            var first: Element?\
        \ { elements.first }\n\n            mutating func insert(_ value: Element) {\n\
        \                elements.append(value)\n                var index = elements.count\
        \ - 1\n                while index > 0 {\n                    let parent = (index\
        \ - 1) / 2\n                    if !orderedBefore(elements[index], elements[parent])\
        \ { break }\n                    elements.swapAt(index, parent)\n          \
        \          index = parent\n                }\n            }\n\n            mutating\
        \ func removeFirst() -> Element {\n                if elements.count == 1 {\
        \ return elements.removeLast() }\n                let result = elements[0]\n\
        \                elements[0] = elements.removeLast()\n                var index\
        \ = 0\n                while true {\n                    let left = index *\
        \ 2 + 1\n                    let right = left + 1\n                    var smallest\
        \ = index\n                    if left < elements.count && orderedBefore(elements[left],\
        \ elements[smallest]) {\n                        smallest = left\n         \
        \           }\n                    if right < elements.count && orderedBefore(elements[right],\
        \ elements[smallest]) {\n                        smallest = right\n        \
        \            }\n                    if smallest == index { break }\n       \
        \             elements.swapAt(index, smallest)\n                    index =\
        \ smallest\n                }\n                return result\n            }\n\
        \        }\n\n        var available = MinHeap<Server> {\n            $0.weight\
        \ == $1.weight ? $0.index < $1.index : $0.weight < $1.weight\n        }\n  \
        \      for (index, weight) in servers.enumerated() {\n            available.insert(Server(weight:\
        \ weight, index: index))\n        }\n\n        var busy = MinHeap<BusyServer>\
        \ {\n            if $0.finish != $1.finish { return $0.finish < $1.finish }\n\
        \            if $0.weight != $1.weight { return $0.weight < $1.weight }\n  \
        \          return $0.index < $1.index\n        }\n\n        var answer = Array(repeating:\
        \ 0, count: tasks.count)\n        var time = 0\n\n        for j in tasks.indices\
        \ {\n            time = max(time, j)\n            while let first = busy.first,\
        \ first.finish <= time {\n                let server = busy.removeFirst()\n\
        \                available.insert(Server(weight: server.weight, index: server.index))\n\
        \            }\n\n            if available.isEmpty {\n                time =\
        \ busy.first!.finish\n                while let first = busy.first, first.finish\
        \ <= time {\n                    let server = busy.removeFirst()\n         \
        \           available.insert(Server(weight: server.weight, index: server.index))\n\
        \                }\n            }\n\n            let server = available.removeFirst()\n\
        \            answer[j] = server.index\n            busy.insert(BusyServer(finish:\
        \ time + tasks[j], weight: server.weight, index: server.index))\n        }\n\
        \n        return answer\n    }\n}"
      kotlin: "class Solution {\n    fun assignTasks(servers: IntArray, tasks: IntArray):\
        \ IntArray {\n        val available = java.util.PriorityQueue<IntArray>(compareBy<IntArray>\
        \ { it[0] }.thenBy { it[1] })\n        val busy = java.util.PriorityQueue<LongArray>(compareBy<LongArray>\
        \ { it[0] })\n        for (i in servers.indices) {\n            available.add(intArrayOf(servers[i],\
        \ i))\n        }\n        val ans = IntArray(tasks.size)\n        var time =\
        \ 0L\n        for (j in tasks.indices) {\n            time = maxOf(time, j.toLong())\n\
        \            while (busy.isNotEmpty() && busy.peek()[0] <= time) {\n       \
        \         val server = busy.poll()\n                available.add(intArrayOf(server[1].toInt(),\
        \ server[2].toInt()))\n            }\n            if (available.isEmpty()) {\n\
        \                time = busy.peek()[0]\n                while (busy.isNotEmpty()\
        \ && busy.peek()[0] <= time) {\n                    val server = busy.poll()\n\
        \                    available.add(intArrayOf(server[1].toInt(), server[2].toInt()))\n\
        \                }\n            }\n            val server = available.poll()\n\
        \            ans[j] = server[1]\n            busy.add(longArrayOf(time + tasks[j],\
        \ server[0].toLong(), server[1].toLong()))\n        }\n        return ans\n\
        \    }\n}"
      dart: "import 'dart:collection';\n\nclass Solution {\n  List<int> assignTasks(List<int>\
        \ servers, List<int> tasks) {\n    final available = Heap<int>((a, b) {\n  \
        \    final weightComparison = servers[a].compareTo(servers[b]);\n      return\
        \ weightComparison != 0 ? weightComparison : a.compareTo(b);\n    });\n    final\
        \ busy = Heap<int>((a, b) {\n      final timeComparison = finishTime[a].compareTo(finishTime[b]);\n\
        \      return timeComparison != 0 ? timeComparison : a.compareTo(b);\n    });\n\
        \    final finishTime = List<int>.filled(servers.length, 0);\n    for (var i\
        \ = 0; i < servers.length; i++) {\n      available.add(i);\n    }\n    final\
        \ ans = List<int>.filled(tasks.length, 0);\n    var time = 0;\n    for (var\
        \ j = 0; j < tasks.length; j++) {\n      if (time < j) time = j;\n      while\
        \ (busy.isNotEmpty && finishTime[busy.first] <= time) {\n        available.add(busy.removeFirst());\n\
        \      }\n      if (available.isEmpty) {\n        time = finishTime[busy.first];\n\
        \        while (busy.isNotEmpty && finishTime[busy.first] <= time) {\n     \
        \     available.add(busy.removeFirst());\n        }\n      }\n      final server\
        \ = available.removeFirst();\n      ans[j] = server;\n      finishTime[server]\
        \ = time + tasks[j];\n      busy.add(server);\n    }\n    return ans;\n  }\n\
        }\n\nclass Heap<T> {\n  Heap(this.compare);\n\n  final int Function(T, T) compare;\n\
        \  final List<T> _data = [];\n\n  bool get isNotEmpty => _data.isNotEmpty;\n\
        \  bool get isEmpty => _data.isEmpty;\n  T get first => _data.first;\n\n  void\
        \ add(T value) {\n    _data.add(value);\n    var index = _data.length - 1;\n\
        \    while (index > 0) {\n      final parent = (index - 1) ~/ 2;\n      if (compare(_data[index],\
        \ _data[parent]) >= 0) break;\n      final temp = _data[index];\n      _data[index]\
        \ = _data[parent];\n      _data[parent] = temp;\n      index = parent;\n   \
        \ }\n  }\n\n  T removeFirst() {\n    final result = _data[0];\n    final last\
        \ = _data.removeLast();\n    if (_data.isNotEmpty) {\n      _data[0] = last;\n\
        \      var index = 0;\n      while (true) {\n        final left = index * 2\
        \ + 1;\n        final right = left + 1;\n        var smallest = index;\n   \
        \     if (left < _data.length && compare(_data[left], _data[smallest]) < 0)\
        \ {\n          smallest = left;\n        }\n        if (right < _data.length\
        \ && compare(_data[right], _data[smallest]) < 0) {\n          smallest = right;\n\
        \        }\n        if (smallest == index) break;\n        final temp = _data[index];\n\
        \        _data[index] = _data[smallest];\n        _data[smallest] = temp;\n\
        \        index = smallest;\n      }\n    }\n    return result;\n  }\n}"
      go: "package main\n\nimport \"container/heap\"\n\ntype availableServer struct\
        \ {\n\tweight int\n\tindex  int\n}\n\ntype availableHeap []availableServer\n\
        \nfunc (h availableHeap) Len() int { return len(h) }\nfunc (h availableHeap)\
        \ Less(i, j int) bool {\n\tif h[i].weight != h[j].weight {\n\t\treturn h[i].weight\
        \ < h[j].weight\n\t}\n\treturn h[i].index < h[j].index\n}\nfunc (h availableHeap)\
        \ Swap(i, j int) { h[i], h[j] = h[j], h[i] }\nfunc (h *availableHeap) Push(x\
        \ interface{}) { *h = append(*h, x.(availableServer)) }\nfunc (h *availableHeap)\
        \ Pop() interface{} {\n\told := *h\n\tn := len(old)\n\tx := old[n-1]\n\t*h =\
        \ old[:n-1]\n\treturn x\n}\n\ntype busyServer struct {\n\tfinish int64\n\tserver\
        \ availableServer\n}\n\ntype busyHeap []busyServer\n\nfunc (h busyHeap) Len()\
        \ int { return len(h) }\nfunc (h busyHeap) Less(i, j int) bool {\n\tif h[i].finish\
        \ != h[j].finish {\n\t\treturn h[i].finish < h[j].finish\n\t}\n\tif h[i].server.weight\
        \ != h[j].server.weight {\n\t\treturn h[i].server.weight < h[j].server.weight\n\
        \t}\n\treturn h[i].server.index < h[j].server.index\n}\nfunc (h busyHeap) Swap(i,\
        \ j int) { h[i], h[j] = h[j], h[i] }\nfunc (h *busyHeap) Push(x interface{})\
        \ { *h = append(*h, x.(busyServer)) }\nfunc (h *busyHeap) Pop() interface{}\
        \ {\n\told := *h\n\tn := len(old)\n\tx := old[n-1]\n\t*h = old[:n-1]\n\treturn\
        \ x\n}\n\nfunc assignTasks(servers []int, tasks []int) []int {\n\tavailable\
        \ := &availableHeap{}\n\tbusy := &busyHeap{}\n\theap.Init(available)\n\theap.Init(busy)\n\
        \tfor i, weight := range servers {\n\t\theap.Push(available, availableServer{weight:\
        \ weight, index: i})\n\t}\n\tans := make([]int, len(tasks))\n\tvar time int64\n\
        \tfor j, duration := range tasks {\n\t\tif time < int64(j) {\n\t\t\ttime = int64(j)\n\
        \t\t}\n\t\tfor busy.Len() > 0 && (*busy)[0].finish <= time {\n\t\t\tserver :=\
        \ heap.Pop(busy).(busyServer).server\n\t\t\theap.Push(available, server)\n\t\
        \t}\n\t\tif available.Len() == 0 {\n\t\t\ttime = (*busy)[0].finish\n\t\t\tfor\
        \ busy.Len() > 0 && (*busy)[0].finish <= time {\n\t\t\t\tserver := heap.Pop(busy).(busyServer).server\n\
        \t\t\t\theap.Push(available, server)\n\t\t\t}\n\t\t}\n\t\tserver := heap.Pop(available).(availableServer)\n\
        \t\tans[j] = server.index\n\t\theap.Push(busy, busyServer{finish: time + int64(duration),\
        \ server: server})\n\t}\n\treturn ans\n}"
      ruby: "# @param {Integer[]} servers\n# @param {Integer[]} tasks\n# @return {Integer[]}\n\
        def assign_tasks(servers, tasks)\n  available = []\n  servers.each_with_index\
        \ { |weight, index| available << [weight, index] }\n  available.sort!\n  busy\
        \ = []\n  ans = Array.new(tasks.length, 0)\n  time = 0\n\n  tasks.each_with_index\
        \ do |duration, j|\n    time = [time, j].max\n    while !busy.empty? && busy[0][0]\
        \ <= time\n      server = busy.shift\n      available << [server[1], server[2]]\n\
        \      available.sort!\n    end\n    if available.empty?\n      time = busy[0][0]\n\
        \      while !busy.empty? && busy[0][0] <= time\n        server = busy.shift\n\
        \        available << [server[1], server[2]]\n      end\n      available.sort!\n\
        \    end\n    weight, index = available.shift\n    ans[j] = index\n    busy\
        \ << [time + duration, weight, index]\n    busy.sort_by! { |finish, server_weight,\
        \ server_index| [finish, server_weight, server_index] }\n  end\n\n  ans\nend"
      scala: "object Solution {\n    def assignTasks(servers: Array[Int], tasks: Array[Int]):\
        \ Array[Int] = {\n        implicit val availableOrdering: Ordering[(Int, Int)]\
        \ = Ordering.Tuple2[Int, Int].reverse\n        implicit val busyOrdering: Ordering[(Long,\
        \ Int, Int)] = Ordering.Tuple3[Long, Int, Int].reverse\n        val available\
        \ = scala.collection.mutable.PriorityQueue.empty[(Int, Int)]\n        val busy\
        \ = scala.collection.mutable.PriorityQueue.empty[(Long, Int, Int)]\n       \
        \ for (i <- servers.indices) {\n            available.enqueue((servers(i), i))\n\
        \        }\n        val ans = new Array[Int](tasks.length)\n        var time\
        \ = 0L\n        for (j <- tasks.indices) {\n            time = math.max(time,\
        \ j.toLong)\n            while (busy.nonEmpty && busy.head._1 <= time) {\n \
        \               val (_, weight, index) = busy.dequeue()\n                available.enqueue((weight,\
        \ index))\n            }\n            if (available.isEmpty) {\n           \
        \     time = busy.head._1\n                while (busy.nonEmpty && busy.head._1\
        \ <= time) {\n                    val (_, weight, index) = busy.dequeue()\n\
        \                    available.enqueue((weight, index))\n                }\n\
        \            }\n            val (weight, index) = available.dequeue()\n    \
        \        ans(j) = index\n            busy.enqueue((time + tasks(j), weight,\
        \ index))\n        }\n        ans\n    }\n}"
      rust: "impl Solution {\n    pub fn assign_tasks(servers: Vec<i32>, tasks: Vec<i32>)\
        \ -> Vec<i32> {\n        use std::cmp::Reverse;\n        use std::collections::BinaryHeap;\n\
        \n        let mut available = BinaryHeap::new();\n        for (index, weight)\
        \ in servers.iter().enumerate() {\n            available.push(Reverse((*weight,\
        \ index as i32)));\n        }\n\n        let mut busy = BinaryHeap::new();\n\
        \        let mut ans = vec![0; tasks.len()];\n        let mut time: i64 = 0;\n\
        \n        for (j, duration) in tasks.iter().enumerate() {\n            time\
        \ = time.max(j as i64);\n            while let Some(Reverse((finish, weight,\
        \ index))) = busy.peek().copied() {\n                if finish > time {\n  \
        \                  break;\n                }\n                busy.pop();\n\
        \                available.push(Reverse((weight, index)));\n            }\n\n\
        \            if available.is_empty() {\n                time = busy.peek().unwrap().0.0;\n\
        \                while let Some(Reverse((finish, weight, index))) = busy.peek().copied()\
        \ {\n                    if finish > time {\n                        break;\n\
        \                    }\n                    busy.pop();\n                  \
        \  available.push(Reverse((weight, index)));\n                }\n          \
        \  }\n\n            let Reverse((weight, index)) = available.pop().unwrap().0;\n\
        \            ans[j] = index;\n            busy.push(Reverse((time + *duration\
        \ as i64, weight, index)));\n        }\n\n        ans\n    }\n}"
      racket: "(define/contract (assign-tasks servers tasks)\n  (-> (listof exact-integer?)\
        \ (listof exact-integer?) (listof exact-integer?))\n  (let* ([server-vector\
        \ (list->vector servers)]\n         [task-vector (list->vector tasks)]\n   \
        \      [n (vector-length server-vector)]\n         [m (vector-length task-vector)]\n\
        \         [available (make-vector n #f)]\n         [busy (make-vector m #f)]\n\
        \         [ans (make-vector m 0)])\n    (define (available-less? a b)\n    \
        \  (or (< (car a) (car b))\n          (and (= (car a) (car b)) (< (cdr a) (cdr\
        \ b))))\n    (define (busy-less? a b)\n      (or (< (car a) (car b))\n     \
        \     (and (= (car a) (car b))\n               (or (< (cadr a) (cadr b))\n \
        \                  (and (= (cadr a) (cadr b)) (< (caddr a) (caddr b))))))\n\
        \    (define (heap-push! heap size less? value)\n      (let loop ([i size])\n\
        \        (if (and (> i 0) (less? value (vector-ref heap (quotient (sub1 i) 2))))\n\
        \            (begin\n              (vector-set! heap i (vector-ref heap (quotient\
        \ (sub1 i) 2)))\n              (loop (quotient (sub1 i) 2))\n            (vector-set!\
        \ heap i value)))\n      (void))\n    (define (heap-pop! heap size less?)\n\
        \      (let ([root (vector-ref heap 0)]\n            [last (vector-ref heap\
        \ (sub1 size))])\n        (let loop ([i 0])\n          (let* ([left (+ (* 2\
        \ i) 1)]\n                 [right (+ left 1)])\n            (if (>= left (sub1\
        \ size))\n                (vector-set! heap i last)\n                (let* ([child\
        \ (if (and (< right (sub1 size))\n                                       (less?\
        \ (vector-ref heap right) (vector-ref heap left)))\n                       \
        \           right\n                                  left)])\n             \
        \     (if (less? (vector-ref heap child) last)\n                      (begin\n\
        \                        (vector-set! heap i (vector-ref heap child))\n    \
        \                    (loop child))\n                      (vector-set! heap\
        \ i last))))))\n        root))\n    (let init ([i 0])\n      (when (< i n)\n\
        \        (heap-push! available i available-less? (cons (vector-ref server-vector\
        \ i) i))\n        (init (add1 i))))\n    (let loop ([j 0] [available-size n]\
        \ [busy-size 0] [time 0])\n      (if (= j m)\n          (vector->list ans)\n\
        \          (let* ([now (max time j)]\n                 [sizes (let release ([as\
        \ available-size] [bs busy-size])\n                          (if (and (> bs\
        \ 0) (<= (car (vector-ref busy 0)) now))\n                              (let\
        \ ([entry (heap-pop! busy bs busy-less?)])\n                               \
        \ (heap-push! available as available-less?\n                               \
        \             (cons (cadr entry) (caddr entry)))\n                         \
        \       (release (add1 as) (sub1 bs)))\n                              (cons\
        \ as bs)))])\n            (let* ([as (car sizes)] [bs (cdr sizes)]\n       \
        \            [assign-time (if (> as 0) now (car (vector-ref busy 0)))])\n  \
        \            (let release-at-time ([as as] [bs bs])\n                (if (and\
        \ (= as 0) (> bs 0)\n                         (<= (car (vector-ref busy 0))\
        \ assign-time))\n                    (let ([entry (heap-pop! busy bs busy-less?)])\n\
        \                      (heap-push! available as available-less?\n          \
        \                        (cons (cadr entry) (caddr entry)))\n              \
        \        (release-at-time (add1 as) (sub1 bs)))\n                    (let* ([server\
        \ (heap-pop! available as available-less?)]\n                           [index\
        \ (cdr server)]\n                           [weight (car server)])\n       \
        \               (vector-set! ans j index)\n                      (heap-push!\
        \ busy bs busy-less?\n                                  (list (+ assign-time\
        \ (vector-ref task-vector j)) weight index))\n                      (loop (add1\
        \ j) (sub1 as) (add1 bs) assign-time))))))))))"
      erlang: "-spec assign_tasks(Servers :: [integer()], Tasks :: [integer()]) -> [integer()].\n\
        assign_tasks(Servers, Tasks) ->\n  Available = lists:sort([{Weight, Index} ||\
        \ {Weight, Index} <- lists:zip(Servers, lists:seq(0, length(Servers) - 1))]),\n\
        \  TasksWithIndex = lists:zip(Tasks, lists:seq(0, length(Tasks) - 1)),\n  assign_tasks_loop(TasksWithIndex,\
        \ Available, [], 0, []).\n\nassign_tasks_loop([], _Available, _Busy, _Time,\
        \ Acc) ->\n  lists:reverse(Acc);\nassign_tasks_loop([{Duration, J} | Rest],\
        \ Available0, Busy0, Time0, Acc) ->\n  Time1 = max(Time0, J),\n  {Available1,\
        \ Busy1} = release_servers(Busy0, Available0, Time1),\n  {Time2, Available2,\
        \ Busy2} =\n    case Available1 of\n      [] ->\n        [{Finish, _, _} | _]\
        \ = Busy1,\n        {AvailableReleased, BusyReleased} = release_servers(Busy1,\
        \ Available1, Finish),\n        {Finish, AvailableReleased, BusyReleased};\n\
        \      _ ->\n        {Time1, Available1, Busy1}\n    end,\n  [{Weight, Index}\
        \ | Available3] = lists:sort(Available2),\n  Busy3 = lists:sort([{Time2 + Duration,\
        \ Weight, Index} | Busy2]),\n  assign_tasks_loop(Rest, Available3, Busy3, Time2,\
        \ [Index | Acc]).\n\nrelease_servers([{Finish, Weight, Index} | Rest], Available,\
        \ Time) when Finish =< Time ->\n  release_servers(Rest, lists:sort([{Weight,\
        \ Index} | Available]), Time);\nrelease_servers(Busy, Available, _Time) ->\n\
        \  {Available, Busy}."
      elixir: "defmodule Solution do\n  @spec assign_tasks(servers :: [integer], tasks\
        \ :: [integer]) :: [integer]\n  def assign_tasks(servers, tasks) do\n    available\
        \ =\n      servers\n      |> Enum.with_index()\n      |> Enum.map(fn {weight,\
        \ index} -> {weight, index} end)\n      |> Enum.sort()\n\n    tasks\n    |>\
        \ Enum.with_index()\n    |> Enum.reduce({available, [], 0, []}, fn {duration,\
        \ j}, {available, busy, time, acc} ->\n      now = max(time, j)\n      {available,\
        \ busy} = release_servers(busy, available, now)\n\n      {now, available, busy}\
        \ =\n        case available do\n          [] ->\n            [{finish, _, _}\
        \ | _] = busy\n            {available, busy} = release_servers(busy, available,\
        \ finish)\n            {finish, available, busy}\n          _ ->\n         \
        \   {now, available, busy}\n        end\n\n      [{weight, index} | available]\
        \ = Enum.sort(available)\n      busy = Enum.sort([{now + duration, weight, index}\
        \ | busy])\n      {available, busy, now, [index | acc]}\n    end)\n    |> elem(3)\n\
        \    |> Enum.reverse()\n  end\n\n  defp release_servers([{finish, weight, index}\
        \ | rest], available, time) when finish <= time do\n    release_servers(rest,\
        \ Enum.sort([{weight, index} | available]), time)\n  end\n\n  defp release_servers(busy,\
        \ available, _time) do\n    {available, busy}\n  end\nend"
    approach: 'Maintain two min-heaps: one for available servers ordered by weight and
      then index, and one for busy servers ordered by their finish time. Before assigning
      each task, release every server whose finish time is at or before the current
      time. If no server is available, advance the current time to the earliest finish
      time and release all servers finishing then. Assign the task to the best available
      server and record its finish time.


      Process tasks in input order, advancing the current time to at least each task''s
      insertion time. This preserves the queue order while the heaps enforce the server
      selection rules, including when several servers become free simultaneously.'
    time_complexity: O((n + m) log n), since each server and task causes a constant
      number of heap operations.
    space_complexity: O(n) for the available and busy server heaps.
    elapsed_time: 192.04191875457764
    model: gpt-6-luna
    generated_at: '2026-11-12 23:42:42 '
---

## Problem #1882: Process Tasks Using Servers

**Difficulty:** Medium

**Topics:** Array, Heap (Priority Queue)

## Problem Description

<p>You are given two <strong>0-indexed</strong> integer arrays <code>servers</code> and <code>tasks</code> of lengths <code>n</code>​​​​​​ and <code>m</code>​​​​​​ respectively. <code>servers[i]</code> is the <strong>weight</strong> of the <code>i<sup>​​​​​​th</sup></code>​​​​ server, and <code>tasks[j]</code> is the <strong>time needed</strong> to process the <code>j<sup>​​​​​​th</sup></code>​​​​ task <strong>in seconds</strong>.</p>

<p>Tasks are assigned to the servers using a <strong>task queue</strong>. Initially, all servers are free, and the queue is <strong>empty</strong>.</p>

<p>At second <code>j</code>, the <code>j<sup>th</sup></code> task is <strong>inserted</strong> into the queue (starting with the <code>0<sup>th</sup></code> task being inserted at second <code>0</code>). As long as there are free servers and the queue is not empty, the task in the front of the queue will be assigned to a free server with the <strong>smallest weight</strong>, and in case of a tie, it is assigned to a free server with the <strong>smallest index</strong>.</p>

<p>If there are no free servers and the queue is not empty, we wait until a server becomes free and immediately assign the next task. If multiple servers become free at the same time, then multiple tasks from the queue will be assigned <strong>in order of insertion</strong> following the weight and index priorities above.</p>

<p>A server that is assigned task <code>j</code> at second <code>t</code> will be free again at second <code>t + tasks[j]</code>.</p>

<p>Build an array <code>ans</code>​​​​ of length <code>m</code>, where <code>ans[j]</code> is the <strong>index</strong> of the server the <code>j<sup>​​​​​​th</sup></code> task will be assigned to.</p>

<p>Return <em>the array </em><code>ans</code>​​​​.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> servers = [3,3,2], tasks = [1,2,3,2,1,2]
<strong>Output:</strong> [2,2,0,2,1,2]
<strong>Explanation: </strong>Events in chronological order go as follows:
- At second 0, task 0 is added and processed using server 2 until second 1.
- At second 1, server 2 becomes free. Task 1 is added and processed using server 2 until second 3.
- At second 2, task 2 is added and processed using server 0 until second 5.
- At second 3, server 2 becomes free. Task 3 is added and processed using server 2 until second 5.
- At second 4, task 4 is added and processed using server 1 until second 5.
- At second 5, all servers become free. Task 5 is added and processed using server 2 until second 7.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> servers = [5,1,4,3,2], tasks = [2,1,2,4,5,2,1]
<strong>Output:</strong> [1,4,1,4,1,3,2]
<strong>Explanation: </strong>Events in chronological order go as follows: 
- At second 0, task 0 is added and processed using server 1 until second 2.
- At second 1, task 1 is added and processed using server 4 until second 2.
- At second 2, servers 1 and 4 become free. Task 2 is added and processed using server 1 until second 4. 
- At second 3, task 3 is added and processed using server 4 until second 7.
- At second 4, server 1 becomes free. Task 4 is added and processed using server 1 until second 9. 
- At second 5, task 5 is added and processed using server 3 until second 7.
- At second 6, task 6 is added and processed using server 2 until second 7.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>servers.length == n</code></li>
	<li><code>tasks.length == m</code></li>
	<li><code>1 &lt;= n, m &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>1 &lt;= servers[i], tasks[j] &lt;= 2 * 10<sup>5</sup></code></li>
</ul>


## Hints

1. You can maintain a Heap of available Servers and a Heap of unavailable servers

2. Note that the tasks will be processed in the input order so you just need to find the x-th server that will be available according to the rules

## 🤖 AI-Generated Solution (gpt-6-luna)

### Approach

Maintain two min-heaps: one for available servers ordered by weight and then index, and one for busy servers ordered by their finish time. Before assigning each task, release every server whose finish time is at or before the current time. If no server is available, advance the current time to the earliest finish time and release all servers finishing then. Assign the task to the best available server and record its finish time.

Process tasks in input order, advancing the current time to at least each task's insertion time. This preserves the queue order while the heaps enforce the server selection rules, including when several servers become free simultaneously.

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
    vector<int> assignTasks(vector<int>& servers, vector<int>& tasks) {
        using Available = pair<int, int>;
        using Busy = pair<long long, int>;
        priority_queue<Available, vector<Available>, greater<Available>> available;
        priority_queue<Busy, vector<Busy>, greater<Busy>> busy;
        for (int i = 0; i < static_cast<int>(servers.size()); ++i) {
            available.push({servers[i], i});
        }
        vector<int> ans(tasks.size());
        long long time = 0;
        for (int j = 0; j < static_cast<int>(tasks.size()); ++j) {
            time = max(time, static_cast<long long>(j));
            while (!busy.empty() && busy.top().first <= time) {
                int index = busy.top().second;
                busy.pop();
                available.push({servers[index], index});
            }
            if (available.empty()) {
                time = busy.top().first;
                while (!busy.empty() && busy.top().first <= time) {
                    int index = busy.top().second;
                    busy.pop();
                    available.push({servers[index], index});
                }
            }
            auto [weight, index] = available.top();
            available.pop();
            ans[j] = index;
            busy.push({time + tasks[j], index});
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
    public int[] assignTasks(int[] servers, int[] tasks) {
        PriorityQueue<Integer> available = new PriorityQueue<>((a, b) -> {
            int byWeight = Integer.compare(servers[a], servers[b]);
            return byWeight != 0 ? byWeight : Integer.compare(a, b);
        });
        PriorityQueue<long[]> busy = new PriorityQueue<>((a, b) -> {
            int byTime = Long.compare(a[0], b[0]);
            return byTime != 0 ? byTime : Integer.compare((int) a[1], (int) b[1]);
        });
        for (int i = 0; i < servers.length; i++) {
            available.offer(i);
        }
        int[] ans = new int[tasks.length];
        long time = 0;
        for (int j = 0; j < tasks.length; j++) {
            time = Math.max(time, j);
            while (!busy.isEmpty() && busy.peek()[0] <= time) {
                available.offer((int) busy.poll()[1]);
            }
            if (available.isEmpty()) {
                time = busy.peek()[0];
                while (!busy.isEmpty() && busy.peek()[0] <= time) {
                    available.offer((int) busy.poll()[1]);
                }
            }
            int server = available.poll();
            ans[j] = server;
            busy.offer(new long[]{time + tasks[j], server});
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
import heapq

class Solution(object):
    def assignTasks(self, servers, tasks):
        """
        :type servers: List[int]
        :type tasks: List[int]
        :rtype: List[int]
        """
        available = [(weight, index) for index, weight in enumerate(servers)]
        heapq.heapify(available)
        busy = []
        ans = [0] * len(tasks)
        time = 0
        for j, duration in enumerate(tasks):
            time = max(time, j)
            while busy and busy[0][0] <= time:
                finish, weight, index = heapq.heappop(busy)
                heapq.heappush(available, (weight, index))
            if not available:
                time = busy[0][0]
                while busy and busy[0][0] <= time:
                    finish, weight, index = heapq.heappop(busy)
                    heapq.heappush(available, (weight, index))
            weight, index = heapq.heappop(available)
            ans[j] = index
            heapq.heappush(busy, (time + duration, weight, index))
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        available = [(weight, index) for index, weight in enumerate(servers)]
        heapq.heapify(available)
        busy = []
        ans = [0] * len(tasks)
        time = 0
        for j, duration in enumerate(tasks):
            time = max(time, j)
            while busy and busy[0][0] <= time:
                finish, weight, index = heapq.heappop(busy)
                heapq.heappush(available, (weight, index))
            if not available:
                time = busy[0][0]
                while busy and busy[0][0] <= time:
                    finish, weight, index = heapq.heappop(busy)
                    heapq.heappush(available, (weight, index))
            weight, index = heapq.heappop(available)
            ans[j] = index
            heapq.heappush(busy, (time + duration, weight, index))
        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>

typedef struct {
    long long time;
    int weight;
    int index;
} Node;

static int availableLess(Node a, Node b) {
    if (a.weight != b.weight) return a.weight < b.weight;
    return a.index < b.index;
}

static int busyLess(Node a, Node b) {
    if (a.time != b.time) return a.time < b.time;
    return a.index < b.index;
}

static void push(Node* heap, int* size, Node value, int (*less)(Node, Node)) {
    int i = (*size)++;
    while (i > 0) {
        int parent = (i - 1) / 2;
        if (!less(value, heap[parent])) break;
        heap[i] = heap[parent];
        i = parent;
    }
    heap[i] = value;
}

static Node pop(Node* heap, int* size, int (*less)(Node, Node)) {
    Node result = heap[0];
    Node last = heap[--(*size)];
    if (*size == 0) return result;
    int i = 0;
    while (2 * i + 1 < *size) {
        int child = 2 * i + 1;
        if (child + 1 < *size && less(heap[child + 1], heap[child])) child++;
        if (!less(heap[child], last)) break;
        heap[i] = heap[child];
        i = child;
    }
    heap[i] = last;
    return result;
}

int* assignTasks(int* servers, int serversSize, int* tasks, int tasksSize, int* returnSize) {
    Node* available = malloc(sizeof(Node) * serversSize);
    Node* busy = malloc(sizeof(Node) * serversSize);
    int availableSize = 0;
    int busySize = 0;
    int* ans = malloc(sizeof(int) * tasksSize);
    *returnSize = tasksSize;
    for (int i = 0; i < serversSize; i++) {
        Node server = {0, servers[i], i};
        push(available, &availableSize, server, availableLess);
    }
    long long time = 0;
    for (int j = 0; j < tasksSize; j++) {
        if (time < j) time = j;
        while (busySize > 0 && busy[0].time <= time) {
            Node server = pop(busy, &busySize, busyLess);
            push(available, &availableSize, server, availableLess);
        }
        if (availableSize == 0) {
            time = busy[0].time;
            while (busySize > 0 && busy[0].time <= time) {
                Node server = pop(busy, &busySize, busyLess);
                push(available, &availableSize, server, availableLess);
            }
        }
        Node server = pop(available, &availableSize, availableLess);
        ans[j] = server.index;
        server.time = time + tasks[j];
        push(busy, &busySize, server, busyLess);
    }
    free(available);
    free(busy);
    return ans;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int[] AssignTasks(int[] servers, int[] tasks) {
        int n = servers.Length;
        var available = new PriorityQueue<int, (int weight, int index)>();
        for (int i = 0; i < n; i++) {
            available.Enqueue(i, (servers[i], i));
        }

        var busy = new PriorityQueue<(int index, int weight), (long finish, int weight, int index)>();
        int[] answer = new int[tasks.Length];
        long time = 0;

        for (int j = 0; j < tasks.Length; j++) {
            time = Math.Max(time, j);
            while (busy.Count > 0 && busy.Peek().finish <= time) {
                var entry = busy.Dequeue();
                available.Enqueue(entry.index, (entry.weight, entry.index));
            }

            if (available.Count == 0) {
                time = busy.Peek().finish;
                while (busy.Count > 0 && busy.Peek().finish <= time) {
                    var entry = busy.Dequeue();
                    available.Enqueue(entry.index, (entry.weight, entry.index));
                }
            }

            int serverIndex = available.Dequeue();
            answer[j] = serverIndex;
            busy.Enqueue((serverIndex, servers[serverIndex]), (time + tasks[j], servers[serverIndex], serverIndex));
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
 * @param {number[]} servers
 * @param {number[]} tasks
 * @return {number[]}
 */
var assignTasks = function(servers, tasks) {
    class MinHeap {
        constructor(compare) {
            this.data = [];
            this.compare = compare;
        }

        get size() {
            return this.data.length;
        }

        peek() {
            return this.data[0];
        }

        push(value) {
            const data = this.data;
            data.push(value);
            let index = data.length - 1;
            while (index > 0) {
                const parent = (index - 1) >> 1;
                if (this.compare(data[parent], value) <= 0) break;
                data[index] = data[parent];
                index = parent;
            }
            data[index] = value;
        }

        pop() {
            const data = this.data;
            const root = data[0];
            const last = data.pop();
            if (data.length > 0) {
                let index = 0;
                while (true) {
                    let child = index * 2 + 1;
                    if (child >= data.length) break;
                    if (child + 1 < data.length && this.compare(data[child + 1], data[child]) < 0) child++;
                    if (this.compare(last, data[child]) <= 0) break;
                    data[index] = data[child];
                    index = child;
                }
                data[index] = last;
            }
            return root;
        }
    }

    const available = new MinHeap((a, b) => a.weight - b.weight || a.index - b.index);
    const busy = new MinHeap((a, b) => a.finish - b.finish || a.weight - b.weight || a.index - b.index);
    for (let i = 0; i < servers.length; i++) available.push({ weight: servers[i], index: i });

    const answer = new Array(tasks.length);
    let time = 0;
    for (let j = 0; j < tasks.length; j++) {
        time = Math.max(time, j);
        while (busy.size > 0 && busy.peek().finish <= time) {
            const server = busy.pop();
            available.push({ weight: server.weight, index: server.index });
        }
        if (available.size === 0) {
            time = busy.peek().finish;
            while (busy.size > 0 && busy.peek().finish <= time) {
                const server = busy.pop();
                available.push({ weight: server.weight, index: server.index });
            }
        }
        const server = available.pop();
        answer[j] = server.index;
        busy.push({ finish: time + tasks[j], weight: server.weight, index: server.index });
    }
    return answer;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function assignTasks(servers: number[], tasks: number[]): number[] {
    type Server = { weight: number; index: number };
    type BusyServer = { finish: number; weight: number; index: number };

    class MinHeap<T> {
        private data: T[] = [];
        constructor(private compare: (a: T, b: T) => number) {}

        get size(): number {
            return this.data.length;
        }

        peek(): T {
            return this.data[0];
        }

        push(value: T): void {
            const data = this.data;
            data.push(value);
            let index = data.length - 1;
            while (index > 0) {
                const parent = (index - 1) >> 1;
                if (this.compare(data[parent], value) <= 0) break;
                data[index] = data[parent];
                index = parent;
            }
            data[index] = value;
        }

        pop(): T {
            const data = this.data;
            const root = data[0];
            const last = data.pop() as T;
            if (data.length > 0) {
                let index = 0;
                while (true) {
                    let child = index * 2 + 1;
                    if (child >= data.length) break;
                    if (child + 1 < data.length && this.compare(data[child + 1], data[child]) < 0) child++;
                    if (this.compare(last, data[child]) <= 0) break;
                    data[index] = data[child];
                    index = child;
                }
                data[index] = last;
            }
            return root;
        }
    }

    const available = new MinHeap<Server>((a, b) => a.weight - b.weight || a.index - b.index);
    const busy = new MinHeap<BusyServer>((a, b) => a.finish - b.finish || a.weight - b.weight || a.index - b.index);
    for (let i = 0; i < servers.length; i++) available.push({ weight: servers[i], index: i });

    const answer = new Array<number>(tasks.length);
    let time = 0;
    for (let j = 0; j < tasks.length; j++) {
        time = Math.max(time, j);
        while (busy.size > 0 && busy.peek().finish <= time) {
            const server = busy.pop();
            available.push({ weight: server.weight, index: server.index });
        }
        if (available.size === 0) {
            time = busy.peek().finish;
            while (busy.size > 0 && busy.peek().finish <= time) {
                const server = busy.pop();
                available.push({ weight: server.weight, index: server.index });
            }
        }
        const server = available.pop();
        answer[j] = server.index;
        busy.push({ finish: time + tasks[j], weight: server.weight, index: server.index });
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
     * @param Integer[] $servers
     * @param Integer[] $tasks
     * @return Integer[]
     */
    function assignTasks($servers, $tasks) {
        $available = new SplPriorityQueue();
        $available->setExtractFlags(SplPriorityQueue::EXTR_DATA);
        foreach ($servers as $index => $weight) {
            $available->insert([$weight, $index], [-$weight, -$index]);
        }

        $busy = new SplPriorityQueue();
        $busy->setExtractFlags(SplPriorityQueue::EXTR_DATA);
        $answer = array_fill(0, count($tasks), 0);
        $time = 0;

        foreach ($tasks as $j => $duration) {
            $time = max($time, $j);
            while (!$busy->isEmpty()) {
                $busy->top();
                $entry = $busy->current();
                if ($entry[0] > $time) break;
                $entry = $busy->extract();
                $available->insert([$entry[1], $entry[2]], [-$entry[1], -$entry[2]]);
            }

            if ($available->isEmpty()) {
                $busy->top();
                $time = $busy->current()[0];
                while (!$busy->isEmpty()) {
                    $busy->top();
                    if ($busy->current()[0] > $time) break;
                    $entry = $busy->extract();
                    $available->insert([$entry[1], $entry[2]], [-$entry[1], -$entry[2]]);
                }
            }

            [$weight, $index] = $available->extract();
            $answer[$j] = $index;
            $busy->insert([$time + $duration, $weight, $index], [-($time + $duration), -$weight, -$index]);
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
    func assignTasks(_ servers: [Int], _ tasks: [Int]) -> [Int] {
        struct Server {
            let weight: Int
            let index: Int
        }

        struct BusyServer {
            let finish: Int
            let weight: Int
            let index: Int
        }

        struct MinHeap<Element> {
            var elements: [Element] = []
            let orderedBefore: (Element, Element) -> Bool

            var isEmpty: Bool { elements.isEmpty }
            var first: Element? { elements.first }

            mutating func insert(_ value: Element) {
                elements.append(value)
                var index = elements.count - 1
                while index > 0 {
                    let parent = (index - 1) / 2
                    if !orderedBefore(elements[index], elements[parent]) { break }
                    elements.swapAt(index, parent)
                    index = parent
                }
            }

            mutating func removeFirst() -> Element {
                if elements.count == 1 { return elements.removeLast() }
                let result = elements[0]
                elements[0] = elements.removeLast()
                var index = 0
                while true {
                    let left = index * 2 + 1
                    let right = left + 1
                    var smallest = index
                    if left < elements.count && orderedBefore(elements[left], elements[smallest]) {
                        smallest = left
                    }
                    if right < elements.count && orderedBefore(elements[right], elements[smallest]) {
                        smallest = right
                    }
                    if smallest == index { break }
                    elements.swapAt(index, smallest)
                    index = smallest
                }
                return result
            }
        }

        var available = MinHeap<Server> {
            $0.weight == $1.weight ? $0.index < $1.index : $0.weight < $1.weight
        }
        for (index, weight) in servers.enumerated() {
            available.insert(Server(weight: weight, index: index))
        }

        var busy = MinHeap<BusyServer> {
            if $0.finish != $1.finish { return $0.finish < $1.finish }
            if $0.weight != $1.weight { return $0.weight < $1.weight }
            return $0.index < $1.index
        }

        var answer = Array(repeating: 0, count: tasks.count)
        var time = 0

        for j in tasks.indices {
            time = max(time, j)
            while let first = busy.first, first.finish <= time {
                let server = busy.removeFirst()
                available.insert(Server(weight: server.weight, index: server.index))
            }

            if available.isEmpty {
                time = busy.first!.finish
                while let first = busy.first, first.finish <= time {
                    let server = busy.removeFirst()
                    available.insert(Server(weight: server.weight, index: server.index))
                }
            }

            let server = available.removeFirst()
            answer[j] = server.index
            busy.insert(BusyServer(finish: time + tasks[j], weight: server.weight, index: server.index))
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
    fun assignTasks(servers: IntArray, tasks: IntArray): IntArray {
        val available = java.util.PriorityQueue<IntArray>(compareBy<IntArray> { it[0] }.thenBy { it[1] })
        val busy = java.util.PriorityQueue<LongArray>(compareBy<LongArray> { it[0] })
        for (i in servers.indices) {
            available.add(intArrayOf(servers[i], i))
        }
        val ans = IntArray(tasks.size)
        var time = 0L
        for (j in tasks.indices) {
            time = maxOf(time, j.toLong())
            while (busy.isNotEmpty() && busy.peek()[0] <= time) {
                val server = busy.poll()
                available.add(intArrayOf(server[1].toInt(), server[2].toInt()))
            }
            if (available.isEmpty()) {
                time = busy.peek()[0]
                while (busy.isNotEmpty() && busy.peek()[0] <= time) {
                    val server = busy.poll()
                    available.add(intArrayOf(server[1].toInt(), server[2].toInt()))
                }
            }
            val server = available.poll()
            ans[j] = server[1]
            busy.add(longArrayOf(time + tasks[j], server[0].toLong(), server[1].toLong()))
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
import 'dart:collection';

class Solution {
  List<int> assignTasks(List<int> servers, List<int> tasks) {
    final available = Heap<int>((a, b) {
      final weightComparison = servers[a].compareTo(servers[b]);
      return weightComparison != 0 ? weightComparison : a.compareTo(b);
    });
    final busy = Heap<int>((a, b) {
      final timeComparison = finishTime[a].compareTo(finishTime[b]);
      return timeComparison != 0 ? timeComparison : a.compareTo(b);
    });
    final finishTime = List<int>.filled(servers.length, 0);
    for (var i = 0; i < servers.length; i++) {
      available.add(i);
    }
    final ans = List<int>.filled(tasks.length, 0);
    var time = 0;
    for (var j = 0; j < tasks.length; j++) {
      if (time < j) time = j;
      while (busy.isNotEmpty && finishTime[busy.first] <= time) {
        available.add(busy.removeFirst());
      }
      if (available.isEmpty) {
        time = finishTime[busy.first];
        while (busy.isNotEmpty && finishTime[busy.first] <= time) {
          available.add(busy.removeFirst());
        }
      }
      final server = available.removeFirst();
      ans[j] = server;
      finishTime[server] = time + tasks[j];
      busy.add(server);
    }
    return ans;
  }
}

class Heap<T> {
  Heap(this.compare);

  final int Function(T, T) compare;
  final List<T> _data = [];

  bool get isNotEmpty => _data.isNotEmpty;
  bool get isEmpty => _data.isEmpty;
  T get first => _data.first;

  void add(T value) {
    _data.add(value);
    var index = _data.length - 1;
    while (index > 0) {
      final parent = (index - 1) ~/ 2;
      if (compare(_data[index], _data[parent]) >= 0) break;
      final temp = _data[index];
      _data[index] = _data[parent];
      _data[parent] = temp;
      index = parent;
    }
  }

  T removeFirst() {
    final result = _data[0];
    final last = _data.removeLast();
    if (_data.isNotEmpty) {
      _data[0] = last;
      var index = 0;
      while (true) {
        final left = index * 2 + 1;
        final right = left + 1;
        var smallest = index;
        if (left < _data.length && compare(_data[left], _data[smallest]) < 0) {
          smallest = left;
        }
        if (right < _data.length && compare(_data[right], _data[smallest]) < 0) {
          smallest = right;
        }
        if (smallest == index) break;
        final temp = _data[index];
        _data[index] = _data[smallest];
        _data[smallest] = temp;
        index = smallest;
      }
    }
    return result;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
package main

import "container/heap"

type availableServer struct {
	weight int
	index  int
}

type availableHeap []availableServer

func (h availableHeap) Len() int { return len(h) }
func (h availableHeap) Less(i, j int) bool {
	if h[i].weight != h[j].weight {
		return h[i].weight < h[j].weight
	}
	return h[i].index < h[j].index
}
func (h availableHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }
func (h *availableHeap) Push(x interface{}) { *h = append(*h, x.(availableServer)) }
func (h *availableHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

type busyServer struct {
	finish int64
	server availableServer
}

type busyHeap []busyServer

func (h busyHeap) Len() int { return len(h) }
func (h busyHeap) Less(i, j int) bool {
	if h[i].finish != h[j].finish {
		return h[i].finish < h[j].finish
	}
	if h[i].server.weight != h[j].server.weight {
		return h[i].server.weight < h[j].server.weight
	}
	return h[i].server.index < h[j].server.index
}
func (h busyHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }
func (h *busyHeap) Push(x interface{}) { *h = append(*h, x.(busyServer)) }
func (h *busyHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func assignTasks(servers []int, tasks []int) []int {
	available := &availableHeap{}
	busy := &busyHeap{}
	heap.Init(available)
	heap.Init(busy)
	for i, weight := range servers {
		heap.Push(available, availableServer{weight: weight, index: i})
	}
	ans := make([]int, len(tasks))
	var time int64
	for j, duration := range tasks {
		if time < int64(j) {
			time = int64(j)
		}
		for busy.Len() > 0 && (*busy)[0].finish <= time {
			server := heap.Pop(busy).(busyServer).server
			heap.Push(available, server)
		}
		if available.Len() == 0 {
			time = (*busy)[0].finish
			for busy.Len() > 0 && (*busy)[0].finish <= time {
				server := heap.Pop(busy).(busyServer).server
				heap.Push(available, server)
			}
		}
		server := heap.Pop(available).(availableServer)
		ans[j] = server.index
		heap.Push(busy, busyServer{finish: time + int64(duration), server: server})
	}
	return ans
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} servers
# @param {Integer[]} tasks
# @return {Integer[]}
def assign_tasks(servers, tasks)
  available = []
  servers.each_with_index { |weight, index| available << [weight, index] }
  available.sort!
  busy = []
  ans = Array.new(tasks.length, 0)
  time = 0

  tasks.each_with_index do |duration, j|
    time = [time, j].max
    while !busy.empty? && busy[0][0] <= time
      server = busy.shift
      available << [server[1], server[2]]
      available.sort!
    end
    if available.empty?
      time = busy[0][0]
      while !busy.empty? && busy[0][0] <= time
        server = busy.shift
        available << [server[1], server[2]]
      end
      available.sort!
    end
    weight, index = available.shift
    ans[j] = index
    busy << [time + duration, weight, index]
    busy.sort_by! { |finish, server_weight, server_index| [finish, server_weight, server_index] }
  end

  ans
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def assignTasks(servers: Array[Int], tasks: Array[Int]): Array[Int] = {
        implicit val availableOrdering: Ordering[(Int, Int)] = Ordering.Tuple2[Int, Int].reverse
        implicit val busyOrdering: Ordering[(Long, Int, Int)] = Ordering.Tuple3[Long, Int, Int].reverse
        val available = scala.collection.mutable.PriorityQueue.empty[(Int, Int)]
        val busy = scala.collection.mutable.PriorityQueue.empty[(Long, Int, Int)]
        for (i <- servers.indices) {
            available.enqueue((servers(i), i))
        }
        val ans = new Array[Int](tasks.length)
        var time = 0L
        for (j <- tasks.indices) {
            time = math.max(time, j.toLong)
            while (busy.nonEmpty && busy.head._1 <= time) {
                val (_, weight, index) = busy.dequeue()
                available.enqueue((weight, index))
            }
            if (available.isEmpty) {
                time = busy.head._1
                while (busy.nonEmpty && busy.head._1 <= time) {
                    val (_, weight, index) = busy.dequeue()
                    available.enqueue((weight, index))
                }
            }
            val (weight, index) = available.dequeue()
            ans(j) = index
            busy.enqueue((time + tasks(j), weight, index))
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
    pub fn assign_tasks(servers: Vec<i32>, tasks: Vec<i32>) -> Vec<i32> {
        use std::cmp::Reverse;
        use std::collections::BinaryHeap;

        let mut available = BinaryHeap::new();
        for (index, weight) in servers.iter().enumerate() {
            available.push(Reverse((*weight, index as i32)));
        }

        let mut busy = BinaryHeap::new();
        let mut ans = vec![0; tasks.len()];
        let mut time: i64 = 0;

        for (j, duration) in tasks.iter().enumerate() {
            time = time.max(j as i64);
            while let Some(Reverse((finish, weight, index))) = busy.peek().copied() {
                if finish > time {
                    break;
                }
                busy.pop();
                available.push(Reverse((weight, index)));
            }

            if available.is_empty() {
                time = busy.peek().unwrap().0.0;
                while let Some(Reverse((finish, weight, index))) = busy.peek().copied() {
                    if finish > time {
                        break;
                    }
                    busy.pop();
                    available.push(Reverse((weight, index)));
                }
            }

            let Reverse((weight, index)) = available.pop().unwrap().0;
            ans[j] = index;
            busy.push(Reverse((time + *duration as i64, weight, index)));
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
(define/contract (assign-tasks servers tasks)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?))
  (let* ([server-vector (list->vector servers)]
         [task-vector (list->vector tasks)]
         [n (vector-length server-vector)]
         [m (vector-length task-vector)]
         [available (make-vector n #f)]
         [busy (make-vector m #f)]
         [ans (make-vector m 0)])
    (define (available-less? a b)
      (or (< (car a) (car b))
          (and (= (car a) (car b)) (< (cdr a) (cdr b))))
    (define (busy-less? a b)
      (or (< (car a) (car b))
          (and (= (car a) (car b))
               (or (< (cadr a) (cadr b))
                   (and (= (cadr a) (cadr b)) (< (caddr a) (caddr b))))))
    (define (heap-push! heap size less? value)
      (let loop ([i size])
        (if (and (> i 0) (less? value (vector-ref heap (quotient (sub1 i) 2))))
            (begin
              (vector-set! heap i (vector-ref heap (quotient (sub1 i) 2)))
              (loop (quotient (sub1 i) 2))
            (vector-set! heap i value)))
      (void))
    (define (heap-pop! heap size less?)
      (let ([root (vector-ref heap 0)]
            [last (vector-ref heap (sub1 size))])
        (let loop ([i 0])
          (let* ([left (+ (* 2 i) 1)]
                 [right (+ left 1)])
            (if (>= left (sub1 size))
                (vector-set! heap i last)
                (let* ([child (if (and (< right (sub1 size))
                                       (less? (vector-ref heap right) (vector-ref heap left)))
                                  right
                                  left)])
                  (if (less? (vector-ref heap child) last)
                      (begin
                        (vector-set! heap i (vector-ref heap child))
                        (loop child))
                      (vector-set! heap i last))))))
        root))
    (let init ([i 0])
      (when (< i n)
        (heap-push! available i available-less? (cons (vector-ref server-vector i) i))
        (init (add1 i))))
    (let loop ([j 0] [available-size n] [busy-size 0] [time 0])
      (if (= j m)
          (vector->list ans)
          (let* ([now (max time j)]
                 [sizes (let release ([as available-size] [bs busy-size])
                          (if (and (> bs 0) (<= (car (vector-ref busy 0)) now))
                              (let ([entry (heap-pop! busy bs busy-less?)])
                                (heap-push! available as available-less?
                                            (cons (cadr entry) (caddr entry)))
                                (release (add1 as) (sub1 bs)))
                              (cons as bs)))])
            (let* ([as (car sizes)] [bs (cdr sizes)]
                   [assign-time (if (> as 0) now (car (vector-ref busy 0)))])
              (let release-at-time ([as as] [bs bs])
                (if (and (= as 0) (> bs 0)
                         (<= (car (vector-ref busy 0)) assign-time))
                    (let ([entry (heap-pop! busy bs busy-less?)])
                      (heap-push! available as available-less?
                                  (cons (cadr entry) (caddr entry)))
                      (release-at-time (add1 as) (sub1 bs)))
                    (let* ([server (heap-pop! available as available-less?)]
                           [index (cdr server)]
                           [weight (car server)])
                      (vector-set! ans j index)
                      (heap-push! busy bs busy-less?
                                  (list (+ assign-time (vector-ref task-vector j)) weight index))
                      (loop (add1 j) (sub1 as) (add1 bs) assign-time))))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec assign_tasks(Servers :: [integer()], Tasks :: [integer()]) -> [integer()].
assign_tasks(Servers, Tasks) ->
  Available = lists:sort([{Weight, Index} || {Weight, Index} <- lists:zip(Servers, lists:seq(0, length(Servers) - 1))]),
  TasksWithIndex = lists:zip(Tasks, lists:seq(0, length(Tasks) - 1)),
  assign_tasks_loop(TasksWithIndex, Available, [], 0, []).

assign_tasks_loop([], _Available, _Busy, _Time, Acc) ->
  lists:reverse(Acc);
assign_tasks_loop([{Duration, J} | Rest], Available0, Busy0, Time0, Acc) ->
  Time1 = max(Time0, J),
  {Available1, Busy1} = release_servers(Busy0, Available0, Time1),
  {Time2, Available2, Busy2} =
    case Available1 of
      [] ->
        [{Finish, _, _} | _] = Busy1,
        {AvailableReleased, BusyReleased} = release_servers(Busy1, Available1, Finish),
        {Finish, AvailableReleased, BusyReleased};
      _ ->
        {Time1, Available1, Busy1}
    end,
  [{Weight, Index} | Available3] = lists:sort(Available2),
  Busy3 = lists:sort([{Time2 + Duration, Weight, Index} | Busy2]),
  assign_tasks_loop(Rest, Available3, Busy3, Time2, [Index | Acc]).

release_servers([{Finish, Weight, Index} | Rest], Available, Time) when Finish =< Time ->
  release_servers(Rest, lists:sort([{Weight, Index} | Available]), Time);
release_servers(Busy, Available, _Time) ->
  {Available, Busy}.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec assign_tasks(servers :: [integer], tasks :: [integer]) :: [integer]
  def assign_tasks(servers, tasks) do
    available =
      servers
      |> Enum.with_index()
      |> Enum.map(fn {weight, index} -> {weight, index} end)
      |> Enum.sort()

    tasks
    |> Enum.with_index()
    |> Enum.reduce({available, [], 0, []}, fn {duration, j}, {available, busy, time, acc} ->
      now = max(time, j)
      {available, busy} = release_servers(busy, available, now)

      {now, available, busy} =
        case available do
          [] ->
            [{finish, _, _} | _] = busy
            {available, busy} = release_servers(busy, available, finish)
            {finish, available, busy}
          _ ->
            {now, available, busy}
        end

      [{weight, index} | available] = Enum.sort(available)
      busy = Enum.sort([{now + duration, weight, index} | busy])
      {available, busy, now, [index | acc]}
    end)
    |> elem(3)
    |> Enum.reverse()
  end

  defp release_servers([{finish, weight, index} | rest], available, time) when finish <= time do
    release_servers(rest, Enum.sort([{weight, index} | available]), time)
  end

  defp release_servers(busy, available, _time) do
    {available, busy}
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O((n + m) log n), since each server and task causes a constant number of heap operations.
- **Space Complexity:** O(n) for the available and busy server heaps.
