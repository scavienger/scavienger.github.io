---
layout: post
title: "Find All People With Secret"
date: 2025-12-19 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Depth-First Search", "Breadth-First Search", "Union Find", "Graph", "Sorting"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/find-all-people-with-secret/
ai_solutions:
  - solutions:
      cpp: "class UnionFind {\npublic:\n    std::vector<int> parent;\n    std::vector<int>\
        \ rank;\n\n    UnionFind(int n) {\n        parent.resize(n);\n        std::iota(parent.begin(),\
        \ parent.end(), 0);\n        rank.assign(n, 0);\n    }\n\n    int find(int i)\
        \ {\n        if (parent[i] == i) {\n            return i;\n        }\n     \
        \   return parent[i] = find(parent[i]);\n    }\n\n    void unite(int i, int\
        \ j) {\n        int root_i = find(i);\n        int root_j = find(j);\n\n   \
        \     if (root_i != root_j) {\n            if (rank[root_i] < rank[root_j])\
        \ {\n                parent[root_i] = root_j;\n            } else if (rank[root_j]\
        \ < rank[root_i]) {\n                parent[root_j] = root_i;\n            }\
        \ else {\n                parent[root_j] = root_i;\n                rank[root_i]++;\n\
        \            }\n        }\n    }\n};\n\nclass Solution {\npublic:\n    std::vector<int>\
        \ findAllPeople(int n, std::vector<std::vector<int>>& meetings, int firstPerson)\
        \ {\n        std::vector<bool> known_secret(n, false);\n        known_secret[0]\
        \ = true;\n        known_secret[firstPerson] = true;\n\n        std::map<int,\
        \ std::vector<std::pair<int, int>>> time_to_meetings;\n        for (const auto&\
        \ meeting : meetings) {\n            time_to_meetings[meeting[2]].push_back({meeting[0],\
        \ meeting[1]});\n        }\n\n        for (auto const& [time, current_meetings]\
        \ : time_to_meetings) {\n            UnionFind uf(n);\n            std::unordered_set<int>\
        \ current_participants;\n\n            for (const auto& meeting_pair : current_meetings)\
        \ {\n                uf.unite(meeting_pair.first, meeting_pair.second);\n  \
        \              current_participants.insert(meeting_pair.first);\n          \
        \      current_participants.insert(meeting_pair.second);\n            }\n\n\
        \            std::unordered_set<int> secret_roots;\n            for (int p :\
        \ current_participants) {\n                if (known_secret[p]) {\n        \
        \            secret_roots.insert(uf.find(p));\n                }\n         \
        \   }\n\n            for (int p : current_participants) {\n                if\
        \ (secret_roots.count(uf.find(p))) {\n                    known_secret[p] =\
        \ true;\n                }\n            }\n        }\n\n        std::vector<int>\
        \ result;\n        for (int i = 0; i < n; ++i) {\n            if (known_secret[i])\
        \ {\n                result.push_back(i);\n            }\n        }\n      \
        \  return result;\n    }\n};"
      java: "import java.util.*;\n\nclass UnionFind {\n    int[] parent;\n    int[]\
        \ rank;\n\n    public UnionFind(int n) {\n        parent = new int[n];\n   \
        \     rank = new int[n];\n        for (int i = 0; i < n; i++) {\n          \
        \  parent[i] = i;\n        }\n    }\n\n    public int find(int i) {\n      \
        \  if (parent[i] == i) {\n            return i;\n        }\n        return parent[i]\
        \ = find(parent[i]);\n    }\n\n    public void unite(int i, int j) {\n     \
        \   int root_i = find(i);\n        int root_j = find(j);\n\n        if (root_i\
        \ != root_j) {\n            if (rank[root_i] < rank[root_j]) {\n           \
        \     parent[root_i] = root_j;\n            } else if (rank[root_j] < rank[root_i])\
        \ {\n                parent[root_j] = root_i;\n            } else {\n      \
        \          parent[root_j] = root_i;\n                rank[root_i]++;\n     \
        \       }\n        }\n    }\n}\n\nclass Solution {\n    public List<Integer>\
        \ findAllPeople(int n, int[][] meetings, int firstPerson) {\n        boolean[]\
        \ knownSecret = new boolean[n];\n        knownSecret[0] = true;\n        knownSecret[firstPerson]\
        \ = true;\n\n        Map<Integer, List<int[]>> timeToMeetings = new TreeMap<>();\
        \ // TreeMap to sort by time\n        for (int[] meeting : meetings) {\n   \
        \         timeToMeetings.computeIfAbsent(meeting[2], k -> new ArrayList<>()).add(new\
        \ int[]{meeting[0], meeting[1]});\n        }\n\n        for (Map.Entry<Integer,\
        \ List<int[]>> entry : timeToMeetings.entrySet()) {\n            // int currentTime\
        \ = entry.getKey(); // Not strictly needed, but good for clarity\n         \
        \   List<int[]> currentMeetings = entry.getValue();\n\n            UnionFind\
        \ uf = new UnionFind(n);\n            Set<Integer> currentParticipants = new\
        \ HashSet<>();\n\n            for (int[] meetingPair : currentMeetings) {\n\
        \                uf.unite(meetingPair[0], meetingPair[1]);\n               \
        \ currentParticipants.add(meetingPair[0]);\n                currentParticipants.add(meetingPair[1]);\n\
        \            }\n\n            Set<Integer> secretRoots = new HashSet<>();\n\
        \            for (int p : currentParticipants) {\n                if (knownSecret[p])\
        \ {\n                    secretRoots.add(uf.find(p));\n                }\n \
        \           }\n\n            for (int p : currentParticipants) {\n         \
        \       if (secretRoots.contains(uf.find(p))) {\n                    knownSecret[p]\
        \ = true;\n                }\n            }\n        }\n\n        List<Integer>\
        \ result = new ArrayList<>();\n        for (int i = 0; i < n; i++) {\n     \
        \       if (knownSecret[i]) {\n                result.add(i);\n            }\n\
        \        }\n        return result;\n    }\n}"
      python: "import collections\n\nclass UnionFind:\n    def __init__(self, n):\n\
        \        self.parent = list(range(n))\n        self.rank = [0] * n\n\n    def\
        \ find(self, i):\n        if self.parent[i] == i:\n            return i\n  \
        \      self.parent[i] = self.find(self.parent[i])\n        return self.parent[i]\n\
        \n    def union(self, i, j):\n        root_i = self.find(i)\n        root_j\
        \ = self.find(j)\n\n        if root_i != root_j:\n            if self.rank[root_i]\
        \ < self.rank[root_j]:\n                self.parent[root_i] = root_j\n     \
        \       elif self.rank[root_j] < self.rank[root_i]:\n                self.parent[root_j]\
        \ = root_i\n            else:\n                self.parent[root_j] = root_i\n\
        \                self.rank[root_i] += 1\n            return True\n        return\
        \ False\n\nclass Solution:\n    def findAllPeople(self, n: int, meetings: list[list[int]],\
        \ firstPerson: int) -> list[int]:\n        known_secret = [False] * n\n    \
        \    known_secret[0] = True\n        known_secret[firstPerson] = True\n\n  \
        \      time_to_meetings = collections.defaultdict(list)\n        for p1, p2,\
        \ time in meetings:\n            time_to_meetings[time].append((p1, p2))\n\n\
        \        sorted_times = sorted(time_to_meetings.keys())\n\n        for current_time\
        \ in sorted_times:\n            uf = UnionFind(n)\n            current_participants\
        \ = set()\n\n            for p1, p2 in time_to_meetings[current_time]:\n   \
        \             uf.union(p1, p2)\n                current_participants.add(p1)\n\
        \                current_participants.add(p2)\n\n            secret_roots =\
        \ set()\n            for p in current_participants:\n                if known_secret[p]:\n\
        \                    secret_roots.add(uf.find(p))\n\n            for p in current_participants:\n\
        \                if uf.find(p) in secret_roots:\n                    known_secret[p]\
        \ = True\n\n        result = [i for i, knows in enumerate(known_secret) if knows]\n\
        \        return result"
      python3: "import collections\n\nclass UnionFind:\n    def __init__(self, n):\n\
        \        self.parent = list(range(n))\n        self.rank = [0] * n\n\n    def\
        \ find(self, i):\n        if self.parent[i] == i:\n            return i\n  \
        \      self.parent[i] = self.find(self.parent[i])\n        return self.parent[i]\n\
        \n    def union(self, i, j):\n        root_i = self.find(i)\n        root_j\
        \ = self.find(j)\n\n        if root_i != root_j:\n            if self.rank[root_i]\
        \ < self.rank[root_j]:\n                self.parent[root_i] = root_j\n     \
        \       elif self.rank[root_j] < self.rank[root_i]:\n                self.parent[root_j]\
        \ = root_i\n            else:\n                self.parent[root_j] = root_i\n\
        \                self.rank[root_i] += 1\n            return True\n        return\
        \ False\n\nclass Solution:\n    def findAllPeople(self, n: int, meetings: list[list[int]],\
        \ firstPerson: int) -> list[int]:\n        known_secret = [False] * n\n    \
        \    known_secret[0] = True\n        known_secret[firstPerson] = True\n\n  \
        \      time_to_meetings = collections.defaultdict(list)\n        for p1, p2,\
        \ time in meetings:\n            time_to_meetings[time].append((p1, p2))\n\n\
        \        sorted_times = sorted(time_to_meetings.keys())\n\n        for current_time\
        \ in sorted_times:\n            uf = UnionFind(n)\n            current_participants\
        \ = set()\n\n            for p1, p2 in time_to_meetings[current_time]:\n   \
        \             uf.union(p1, p2)\n                current_participants.add(p1)\n\
        \                current_participants.add(p2)\n\n            secret_roots =\
        \ set()\n            for p in current_participants:\n                if known_secret[p]:\n\
        \                    secret_roots.add(uf.find(p))\n\n            for p in current_participants:\n\
        \                if uf.find(p) in secret_roots:\n                    known_secret[p]\
        \ = True\n\n        result = [i for i, knows in enumerate(known_secret) if knows]\n\
        \        return result"
      c: "#include <stdlib.h>\n#include <stdbool.h>\n#include <string.h>\n#include <stdio.h>\n\
        \n// Define a struct for Union-Find\ntypedef struct {\n    int* parent;\n  \
        \  int* rank;\n    int n;\n} UnionFind;\n\n// Initialize Union-Find structure\n\
        void uf_init(UnionFind* uf, int n) {\n    uf->n = n;\n    uf->parent = (int*)malloc(n\
        \ * sizeof(int));\n    uf->rank = (int*)calloc(n, sizeof(int)); // calloc initializes\
        \ to 0\n    for (int i = 0; i < n; i++) {\n        uf->parent[i] = i;\n    }\n\
        }\n\n// Free Union-Find resources\nvoid uf_free(UnionFind* uf) {\n    free(uf->parent);\n\
        \    free(uf->rank);\n}\n\n// Find operation with path compression\nint uf_find(UnionFind*\
        \ uf, int i) {\n    if (uf->parent[i] == i) {\n        return i;\n    }\n  \
        \  return uf->parent[i] = uf_find(uf, uf->parent[i]);\n}\n\n// Union operation\
        \ by rank\nvoid uf_unite(UnionFind* uf, int i, int j) {\n    int root_i = uf_find(uf,\
        \ i);\n    int root_j = uf_find(uf, j);\n\n    if (root_i != root_j) {\n   \
        \     if (uf->rank[root_i] < uf->rank[root_j]) {\n            uf->parent[root_i]\
        \ = root_j;\n        } else if (uf->rank[root_j] < uf->rank[root_i]) {\n   \
        \         uf->parent[root_j] = root_i;\n        } else {\n            uf->parent[root_j]\
        \ = root_i;\n            uf->rank[root_i]++;\n        }\n    }\n}\n\n// Struct\
        \ to represent a meeting\ntypedef struct {\n    int p1, p2, time;\n} Meeting;\n\
        \n// Comparison function for sorting meetings by time\nint compareMeetings(const\
        \ void* a, const void* b) {\n    return ((Meeting*)a)->time - ((Meeting*)b)->time;\n\
        }\n\n// Helper for dynamic array (similar to std::vector)\ntypedef struct {\n\
        \    int* data;\n    int size;\n    int capacity;\n} IntVector;\n\nvoid int_vector_init(IntVector*\
        \ vec) {\n    vec->size = 0;\n    vec->capacity = 10;\n    vec->data = (int*)malloc(vec->capacity\
        \ * sizeof(int));\n}\n\nvoid int_vector_add(IntVector* vec, int val) {\n   \
        \ if (vec->size == vec->capacity) {\n        vec->capacity *= 2;\n        vec->data\
        \ = (int*)realloc(vec->data, vec->capacity * sizeof(int));\n    }\n    vec->data[vec->size++]\
        \ = val;\n}\n\nvoid int_vector_free(IntVector* vec) {\n    free(vec->data);\n\
        }\n\n// Helper for hash set (simplified for integers)\ntypedef struct {\n  \
        \  bool* exists;\n    int max_val;\n} IntHashSet;\n\nvoid int_hash_set_init(IntHashSet*\
        \ set, int max_val) {\n    set->max_val = max_val;\n    set->exists = (bool*)calloc(max_val\
        \ + 1, sizeof(bool));\n}\n\nvoid int_hash_set_add(IntHashSet* set, int val)\
        \ {\n    if (val >= 0 && val <= set->max_val) {\n        set->exists[val] =\
        \ true;\n    }\n}\n\nbool int_hash_set_contains(IntHashSet* set, int val) {\n\
        \    if (val >= 0 && val <= set->max_val) {\n        return set->exists[val];\n\
        \    }\n    return false;\n}\n\nvoid int_hash_set_free(IntHashSet* set) {\n\
        \    free(set->exists);\n}\n\n/**\n * Note: The returned array must be malloced,\
        \ and you should ensure that it is freed by the caller.\n */\nint* findAllPeople(int\
        \ n, int** meetings, int meetingsSize, int* meetingsColSize, int firstPerson,\
        \ int* returnSize) {\n    bool* known_secret = (bool*)calloc(n, sizeof(bool));\n\
        \    known_secret[0] = true;\n    known_secret[firstPerson] = true;\n\n    //\
        \ Convert meetings to a more convenient struct array for sorting\n    Meeting*\
        \ meeting_structs = (Meeting*)malloc(meetingsSize * sizeof(Meeting));\n    for\
        \ (int i = 0; i < meetingsSize; i++) {\n        meeting_structs[i].p1 = meetings[i][0];\n\
        \        meeting_structs[i].p2 = meetings[i][1];\n        meeting_structs[i].time\
        \ = meetings[i][2];\n    }\n\n    qsort(meeting_structs, meetingsSize, sizeof(Meeting),\
        \ compareMeetings);\n\n    int current_meeting_idx = 0;\n    while (current_meeting_idx\
        \ < meetingsSize) {\n        int current_time = meeting_structs[current_meeting_idx].time;\n\
        \n        UnionFind uf;\n        uf_init(&uf, n);\n\n        IntHashSet current_participants_set;\n\
        \        int_hash_set_init(&current_participants_set, n - 1);\n\n        IntVector\
        \ current_participants_list;\n        int_vector_init(&current_participants_list);\n\
        \n        int temp_idx = current_meeting_idx;\n        while (temp_idx < meetingsSize\
        \ && meeting_structs[temp_idx].time == current_time) {\n            int p1 =\
        \ meeting_structs[temp_idx].p1;\n            int p2 = meeting_structs[temp_idx].p2;\n\
        \            uf_unite(&uf, p1, p2);\n\n            if (!int_hash_set_contains(&current_participants_set,\
        \ p1)) {\n                int_hash_set_add(&current_participants_set, p1);\n\
        \                int_vector_add(&current_participants_list, p1);\n         \
        \   }\n            if (!int_hash_set_contains(&current_participants_set, p2))\
        \ {\n                int_hash_set_add(&current_participants_set, p2);\n    \
        \            int_vector_add(&current_participants_list, p2);\n            }\n\
        \            temp_idx++;\n        }\n\n        IntHashSet secret_roots;\n  \
        \      int_hash_set_init(&secret_roots, n - 1);\n\n        for (int i = 0; i\
        \ < current_participants_list.size; i++) {\n            int p = current_participants_list.data[i];\n\
        \            if (known_secret[p]) {\n                int_hash_set_add(&secret_roots,\
        \ uf_find(&uf, p));\n            }\n        }\n\n        for (int i = 0; i <\
        \ current_participants_list.size; i++) {\n            int p = current_participants_list.data[i];\n\
        \            if (int_hash_set_contains(&secret_roots, uf_find(&uf, p))) {\n\
        \                known_secret[p] = true;\n            }\n        }\n\n     \
        \   uf_free(&uf);\n        int_hash_set_free(&current_participants_set);\n \
        \       int_vector_free(&current_participants_list);\n        int_hash_set_free(&secret_roots);\n\
        \n        current_meeting_idx = temp_idx;\n    }\n\n    free(meeting_structs);\n\
        \n    IntVector result_vec;\n    int_vector_init(&result_vec);\n    for (int\
        \ i = 0; i < n; i++) {\n        if (known_secret[i]) {\n            int_vector_add(&result_vec,\
        \ i);\n        }\n    }\n    free(known_secret);\n\n    *returnSize = result_vec.size;\n\
        \    return result_vec.data;\n}"
      csharp: "using System; \nusing System.Collections.Generic; \nusing System.Linq;\
        \ \n\npublic class UnionFind \n{\n    private int[] parent;\n    private int[]\
        \ rank;\n\n    public UnionFind(int n)\n    {\n        parent = new int[n];\n\
        \        rank = new int[n];\n        for (int i = 0; i < n; i++)\n        {\n\
        \            parent[i] = i;\n        }\n    }\n\n    public int Find(int i)\n\
        \    {\n        if (parent[i] == i)\n        {\n            return i;\n    \
        \    }\n        return parent[i] = Find(parent[i]);\n    }\n\n    public void\
        \ Unite(int i, int j)\n    {\n        int root_i = Find(i);\n        int root_j\
        \ = Find(j);\n\n        if (root_i != root_j)\n        {\n            if (rank[root_i]\
        \ < rank[root_j])\n            {\n                parent[root_i] = root_j;\n\
        \            }\n            else if (rank[root_j] < rank[root_i])\n        \
        \    {\n                parent[root_j] = root_i;\n            }\n          \
        \  else\n            {\n                parent[root_j] = root_i;\n         \
        \       rank[root_i]++;\n            }\n        }\n    }\n}\n\npublic class\
        \ Solution \n{\n    public IList<int> FindAllPeople(int n, int[][] meetings,\
        \ int firstPerson) \n    {\n        bool[] knownSecret = new bool[n];\n    \
        \    knownSecret[0] = true;\n        knownSecret[firstPerson] = true;\n\n  \
        \      // Group meetings by time using a SortedDictionary to ensure time-based\
        \ iteration\n        SortedDictionary<int, List<int[]>> timeToMeetings = new\
        \ SortedDictionary<int, List<int[]>>();\n        foreach (int[] meeting in meetings)\n\
        \        {\n            int time = meeting[2];\n            if (!timeToMeetings.ContainsKey(time))\n\
        \            {\n                timeToMeetings[time] = new List<int[]>();\n\
        \            }\n            timeToMeetings[time].Add(new int[] { meeting[0],\
        \ meeting[1] });\n        }\n\n        foreach (var entry in timeToMeetings)\n\
        \        {\n            // int currentTime = entry.Key; // Not strictly needed,\
        \ but good for clarity\n            List<int[]> currentMeetings = entry.Value;\n\
        \n            UnionFind uf = new UnionFind(n);\n            HashSet<int> currentParticipants\
        \ = new HashSet<int>();\n\n            foreach (int[] meetingPair in currentMeetings)\n\
        \            {\n                uf.Unite(meetingPair[0], meetingPair[1]);\n\
        \                currentParticipants.Add(meetingPair[0]);\n                currentParticipants.Add(meetingPair[1]);\n\
        \            }\n\n            HashSet<int> secretRoots = new HashSet<int>();\n\
        \            foreach (int p in currentParticipants)\n            {\n       \
        \         if (knownSecret[p])\n                {\n                    secretRoots.Add(uf.Find(p));\n\
        \                }\n            }\n\n            foreach (int p in currentParticipants)\n\
        \            {\n                if (secretRoots.Contains(uf.Find(p)))\n    \
        \            {\n                    knownSecret[p] = true;\n               \
        \ }\n            }\n        }\n\n        List<int> result = new List<int>();\n\
        \        for (int i = 0; i < n; i++)\n        {\n            if (knownSecret[i])\n\
        \            {\n                result.Add(i);\n            }\n        }\n \
        \       return result;\n    }\n}"
      javascript: "class UnionFind {\n    constructor(n) {\n        this.parent = Array.from({\
        \ length: n }, (_, i) => i);\n        this.rank = new Array(n).fill(0);\n  \
        \  }\n\n    find(i) {\n        if (this.parent[i] === i) {\n            return\
        \ i;\n        }\n        this.parent[i] = this.find(this.parent[i]);\n     \
        \   return this.parent[i];\n    }\n\n    union(i, j) {\n        let root_i =\
        \ this.find(i);\n        let root_j = this.find(j);\n\n        if (root_i !==\
        \ root_j) {\n            if (this.rank[root_i] < this.rank[root_j]) {\n    \
        \            this.parent[root_i] = root_j;\n            } else if (this.rank[root_j]\
        \ < this.rank[root_i]) {\n                this.parent[root_j] = root_i;\n  \
        \          } else {\n                this.parent[root_j] = root_i;\n       \
        \         this.rank[root_i]++;\n            }\n            return true;\n  \
        \      }\n        return false;\n    }\n}\n\n/**\n * @param {number} n\n * @param\
        \ {number[][]} meetings\n * @param {number} firstPerson\n * @return {number[]}\n\
        \ */\nvar findAllPeople = function(n, meetings, firstPerson) {\n    let knownSecret\
        \ = new Array(n).fill(false);\n    knownSecret[0] = true;\n    knownSecret[firstPerson]\
        \ = true;\n\n    let timeToMeetings = new Map();\n    for (const [p1, p2, time]\
        \ of meetings) {\n        if (!timeToMeetings.has(time)) {\n            timeToMeetings.set(time,\
        \ []);\n        }\n        timeToMeetings.get(time).push([p1, p2]);\n    }\n\
        \n    // Sort times to process chronologically\n    const sortedTimes = Array.from(timeToMeetings.keys()).sort((a,\
        \ b) => a - b);\n\n    for (const currentTime of sortedTimes) {\n        const\
        \ uf = new UnionFind(n);\n        const currentParticipants = new Set();\n\n\
        \        for (const [p1, p2] of timeToMeetings.get(currentTime)) {\n       \
        \     uf.union(p1, p2);\n            currentParticipants.add(p1);\n        \
        \    currentParticipants.add(p2);\n        }\n\n        const secretRoots =\
        \ new Set();\n        for (const p of currentParticipants) {\n            if\
        \ (knownSecret[p]) {\n                secretRoots.add(uf.find(p));\n       \
        \     }\n        }\n\n        for (const p of currentParticipants) {\n     \
        \       if (secretRoots.has(uf.find(p))) {\n                knownSecret[p] =\
        \ true;\n            }\n        }\n    }\n\n    const result = [];\n    for\
        \ (let i = 0; i < n; i++) {\n        if (knownSecret[i]) {\n            result.push(i);\n\
        \        }\n    }\n    return result;\n};"
      typescript: "class UnionFind {\n    parent: number[];\n    rank: number[];\n\n\
        \    constructor(n: number) {\n        this.parent = Array.from({ length: n\
        \ }, (_, i) => i);\n        this.rank = new Array(n).fill(0);\n    }\n\n   \
        \ find(i: number): number {\n        if (this.parent[i] === i) {\n         \
        \   return i;\n        }\n        this.parent[i] = this.find(this.parent[i]);\n\
        \        return this.parent[i];\n    }\n\n    union(i: number, j: number): boolean\
        \ {\n        let root_i = this.find(i);\n        let root_j = this.find(j);\n\
        \n        if (root_i !== root_j) {\n            if (this.rank[root_i] < this.rank[root_j])\
        \ {\n                this.parent[root_i] = root_j;\n            } else if (this.rank[root_j]\
        \ < this.rank[root_i]) {\n                this.parent[root_j] = root_i;\n  \
        \          } else {\n                this.parent[root_j] = root_i;\n       \
        \         this.rank[root_i]++;\n            }\n            return true;\n  \
        \      }\n        return false;\n    }\n}\n\nfunction findAllPeople(n: number,\
        \ meetings: number[][], firstPerson: number): number[] {\n    const knownSecret:\
        \ boolean[] = new Array(n).fill(false);\n    knownSecret[0] = true;\n    knownSecret[firstPerson]\
        \ = true;\n\n    const timeToMeetings: Map<number, number[][]> = new Map();\n\
        \    for (const [p1, p2, time] of meetings) {\n        if (!timeToMeetings.has(time))\
        \ {\n            timeToMeetings.set(time, []);\n        }\n        timeToMeetings.get(time)!.push([p1,\
        \ p2]);\n    }\n\n    const sortedTimes = Array.from(timeToMeetings.keys()).sort((a,\
        \ b) => a - b);\n\n    for (const currentTime of sortedTimes) {\n        const\
        \ uf = new UnionFind(n);\n        const currentParticipants: Set<number> = new\
        \ Set();\n\n        for (const [p1, p2] of timeToMeetings.get(currentTime)!)\n\
        \        {\n            uf.union(p1, p2);\n            currentParticipants.add(p1);\n\
        \            currentParticipants.add(p2);\n        }\n\n        const secretRoots:\
        \ Set<number> = new Set();\n        for (const p of currentParticipants) {\n\
        \            if (knownSecret[p]) {\n                secretRoots.add(uf.find(p));\n\
        \            }\n        }\n\n        for (const p of currentParticipants) {\n\
        \            if (secretRoots.has(uf.find(p))) {\n                knownSecret[p]\
        \ = true;\n            }\n        }\n    }\n\n    const result: number[] = [];\n\
        \    for (let i = 0; i < n; i++) {\n        if (knownSecret[i]) {\n        \
        \    result.push(i);\n        }\n    }\n    return result;\n}"
      php: "<?php\n\nclass UnionFind {\n    private $parent;\n    private $rank;\n\n\
        \    public function __construct(int $n) {\n        $this->parent = range(0,\
        \ $n - 1);\n        $this->rank = array_fill(0, $n, 0);\n    }\n\n    public\
        \ function find(int $i): int {\n        if ($this->parent[$i] === $i) {\n  \
        \          return $i;\n        }\n        return $this->parent[$i] = $this->find($this->parent[$i]);\n\
        \    }\n\n    public function unite(int $i, int $j): void {\n        $root_i\
        \ = $this->find($i);\n        $root_j = $this->find($j);\n\n        if ($root_i\
        \ !== $root_j) {\n            if ($this->rank[$root_i] < $this->rank[$root_j])\
        \ {\n                $this->parent[$root_i] = $root_j;\n            } elseif\
        \ ($this->rank[$root_j] < $this->rank[$root_i]) {\n                $this->parent[$root_j]\
        \ = $root_i;\n            } else {\n                $this->parent[$root_j] =\
        \ $root_i;\n                $this->rank[$root_i]++;\n            }\n       \
        \ }\n    }\n}\n\nclass Solution {\n    /**\n     * @param int $n\n     * @param\
        \ int[][] $meetings\n     * @param int $firstPerson\n     * @return int[]\n\
        \     */\n    function findAllPeople(int $n, array $meetings, int $firstPerson):\
        \ array {\n        $knownSecret = array_fill(0, $n, false);\n        $knownSecret[0]\
        \ = true;\n        $knownSecret[$firstPerson] = true;\n\n        $timeToMeetings\
        \ = [];\n        foreach ($meetings as $meeting) {\n            list($p1, $p2,\
        \ $time) = $meeting;\n            if (!isset($timeToMeetings[$time])) {\n  \
        \              $timeToMeetings[$time] = [];\n            }\n            $timeToMeetings[$time][]\
        \ = [$p1, $p2];\n        }\n\n        ksort($timeToMeetings); // Sort by time\
        \ keys\n\n        foreach ($timeToMeetings as $currentTime => $currentMeetings)\
        \ {\n            $uf = new UnionFind($n);\n            $currentParticipants\
        \ = []; // Using array as a set for simplicity, checking with isset\n\n    \
        \        foreach ($currentMeetings as $meetingPair) {\n                list($p1,\
        \ $p2) = $meetingPair;\n                $uf->unite($p1, $p2);\n            \
        \    $currentParticipants[$p1] = true;\n                $currentParticipants[$p2]\
        \ = true;\n            }\n\n            $secretRoots = [];\n            foreach\
        \ (array_keys($currentParticipants) as $p) {\n                if ($knownSecret[$p])\
        \ {\n                    $secretRoots[$uf->find($p)] = true;\n             \
        \   }\n            }\n\n            foreach (array_keys($currentParticipants)\
        \ as $p) {\n                if (isset($secretRoots[$uf->find($p)])) {\n    \
        \                $knownSecret[$p] = true;\n                }\n            }\n\
        \        }\n\n        $result = [];\n        for ($i = 0; $i < $n; $i++) {\n\
        \            if ($knownSecret[$i]) {\n                $result[] = $i;\n    \
        \        }\n        }\n        return $result;\n    }\n}\n\n?>"
      swift: "class UnionFind {\n    var parent: [Int]\n    var rank: [Int]\n\n    init(_\
        \ n: Int) {\n        parent = Array(0..<n)\n        rank = Array(repeating:\
        \ 0, count: n)\n    }\n\n    func find(_ i: Int) -> Int {\n        if parent[i]\
        \ == i {\n            return i\n        }\n        parent[i] = find(parent[i])\n\
        \        return parent[i]\n    }\n\n    func unite(_ i: Int, _ j: Int) {\n \
        \       let root_i = find(i)\n        let root_j = find(j)\n\n        if root_i\
        \ != root_j {\n            if rank[root_i] < rank[root_j] {\n              \
        \  parent[root_i] = root_j\n            } else if rank[root_j] < rank[root_i]\
        \ {\n                parent[root_j] = root_i\n            } else {\n       \
        \         parent[root_j] = root_i\n                rank[root_i] += 1\n     \
        \       }\n        }\n    }\n}\n\nclass Solution {\n    func findAllPeople(_\
        \ n: Int, _ meetings: [[Int]], _ firstPerson: Int) -> [Int] {\n        var knownSecret\
        \ = Array(repeating: false, count: n)\n        knownSecret[0] = true\n     \
        \   knownSecret[firstPerson] = true\n\n        var timeToMeetings: [Int: [[Int]]]\
        \ = [:]\n        for meeting in meetings {\n            let p1 = meeting[0]\n\
        \            let p2 = meeting[1]\n            let time = meeting[2]\n      \
        \      timeToMeetings[time, default: []].append([p1, p2])\n        }\n\n   \
        \     let sortedTimes = timeToMeetings.keys.sorted()\n\n        for currentTime\
        \ in sortedTimes {\n            let uf = UnionFind(n)\n            var currentParticipants:\
        \ Set<Int> = []\n\n            for meetingPair in timeToMeetings[currentTime]!\
        \ {\n                let p1 = meetingPair[0]\n                let p2 = meetingPair[1]\n\
        \                uf.unite(p1, p2)\n                currentParticipants.insert(p1)\n\
        \                currentParticipants.insert(p2)\n            }\n\n         \
        \   var secretRoots: Set<Int> = []\n            for p in currentParticipants\
        \ {\n                if knownSecret[p] {\n                    secretRoots.insert(uf.find(p))\n\
        \                }\n            }\n\n            for p in currentParticipants\
        \ {\n                if secretRoots.contains(uf.find(p)) {\n               \
        \     knownSecret[p] = true\n                }\n            }\n        }\n\n\
        \        var result: [Int] = []\n        for i in 0..<n {\n            if knownSecret[i]\
        \ {\n                result.append(i)\n            }\n        }\n        return\
        \ result\n    }\n}"
      kotlin: "import java.util.*\n\nclass UnionFind(private val n: Int) {\n    val\
        \ parent: IntArray = IntArray(n) { it }\n    val rank: IntArray = IntArray(n)\
        \ { 0 }\n\n    fun find(i: Int): Int {\n        if (parent[i] == i) {\n    \
        \        return i\n        }\n        parent[i] = find(parent[i])\n        return\
        \ parent[i]\n    }\n\n    fun unite(i: Int, j: Int) {\n        val root_i =\
        \ find(i)\n        val root_j = find(j)\n\n        if (root_i != root_j) {\n\
        \            if (rank[root_i] < rank[root_j]) {\n                parent[root_i]\
        \ = root_j\n            } else if (rank[root_j] < rank[root_i]) {\n        \
        \        parent[root_j] = root_i\n            } else {\n                parent[root_j]\
        \ = root_i\n                rank[root_i]++\n            }\n        }\n    }\n\
        }\n\nclass Solution {\n    fun findAllPeople(n: Int, meetings: Array<IntArray>,\
        \ firstPerson: Int): List<Int> {\n        val knownSecret = BooleanArray(n)\
        \ { false }\n        knownSecret[0] = true\n        knownSecret[firstPerson]\
        \ = true\n\n        val timeToMeetings = TreeMap<Int, MutableList<IntArray>>()\
        \ // TreeMap to sort by time\n        for (meeting in meetings) {\n        \
        \    timeToMeetings.computeIfAbsent(meeting[2]) { mutableListOf() }.add(intArrayOf(meeting[0],\
        \ meeting[1]))\n        }\n\n        for ((currentTime, currentMeetings) in\
        \ timeToMeetings) {\n            val uf = UnionFind(n)\n            val currentParticipants\
        \ = HashSet<Int>()\n\n            for (meetingPair in currentMeetings) {\n \
        \               uf.unite(meetingPair[0], meetingPair[1])\n                currentParticipants.add(meetingPair[0])\n\
        \                currentParticipants.add(meetingPair[1])\n            }\n\n\
        \            val secretRoots = HashSet<Int>()\n            for (p in currentParticipants)\
        \ {\n                if (knownSecret[p]) {\n                    secretRoots.add(uf.find(p))\n\
        \                }\n            }\n\n            for (p in currentParticipants)\
        \ {\n                if (secretRoots.contains(uf.find(p))) {\n             \
        \       knownSecret[p] = true\n                }\n            }\n        }\n\
        \n        val result = mutableListOf<Int>()\n        for (i in 0 until n) {\n\
        \            if (knownSecret[i]) {\n                result.add(i)\n        \
        \    }\n        }\n        return result\n    }\n}"
      dart: "class UnionFind {\n  late List<int> parent;\n  late List<int> rank;\n\n\
        \  UnionFind(int n) {\n    parent = List<int>.generate(n, (i) => i);\n    rank\
        \ = List<int>.filled(n, 0);\n  }\n\n  int find(int i) {\n    if (parent[i] ==\
        \ i) {\n      return i;\n    }\n    parent[i] = find(parent[i]);\n    return\
        \ parent[i];\n  }\n\n  void unite(int i, int j) {\n    int root_i = find(i);\n\
        \    int root_j = find(j);\n\n    if (root_i != root_j) {\n      if (rank[root_i]\
        \ < rank[root_j]) {\n        parent[root_i] = root_j;\n      } else if (rank[root_j]\
        \ < rank[root_i]) {\n        parent[root_j] = root_i;\n      } else {\n    \
        \    parent[root_j] = root_i;\n        rank[root_i]++;\n      }\n    }\n  }\n\
        }\n\nclass Solution {\n  List<int> findAllPeople(int n, List<List<int>> meetings,\
        \ int firstPerson) {\n    List<bool> knownSecret = List<bool>.filled(n, false);\n\
        \    knownSecret[0] = true;\n    knownSecret[firstPerson] = true;\n\n    Map<int,\
        \ List<List<int>>> timeToMeetings = {};\n    for (var meeting in meetings) {\n\
        \      int p1 = meeting[0];\n      int p2 = meeting[1];\n      int time = meeting[2];\n\
        \      timeToMeetings.putIfAbsent(time, () => []).add([p1, p2]);\n    }\n\n\
        \    // Sort times to process chronologically\n    List<int> sortedTimes = timeToMeetings.keys.toList()..sort();\n\
        \n    for (int currentTime in sortedTimes) {\n      UnionFind uf = UnionFind(n);\n\
        \      Set<int> currentParticipants = {};\n\n      for (var meetingPair in timeToMeetings[currentTime]!)\
        \ {\n        uf.unite(meetingPair[0], meetingPair[1]);\n        currentParticipants.add(meetingPair[0]);\n\
        \        currentParticipants.add(meetingPair[1]);\n      }\n\n      Set<int>\
        \ secretRoots = {};\n      for (int p in currentParticipants) {\n        if\
        \ (knownSecret[p]) {\n          secretRoots.add(uf.find(p));\n        }\n  \
        \    }\n\n      for (int p in currentParticipants) {\n        if (secretRoots.contains(uf.find(p)))\
        \ {\n          knownSecret[p] = true;\n        }\n      }\n    }\n\n    List<int>\
        \ result = [];\n    for (int i = 0; i < n; i++) {\n      if (knownSecret[i])\
        \ {\n        result.add(i);\n      }\n    }\n    return result;\n  }\n}"
      go: "package main\n\nimport (\n\t\"sort\"\n)\n\ntype UnionFind struct {\n\tparent\
        \ []int\n\trank   []int\n}\n\nfunc NewUnionFind(n int) *UnionFind {\n\tparent\
        \ := make([]int, n)\n\trank := make([]int, n)\n\tfor i := 0; i < n; i++ {\n\t\
        \tparent[i] = i\n\t}\n\treturn &UnionFind{parent: parent, rank: rank}\n}\n\n\
        func (uf *UnionFind) Find(i int) int {\n\tif uf.parent[i] == i {\n\t\treturn\
        \ i\n\t}\n\tuf.parent[i] = uf.Find(uf.parent[i])\n\treturn uf.parent[i]\n}\n\
        \nfunc (uf *UnionFind) Unite(i, j int) {\n\troot_i := uf.Find(i)\n\troot_j :=\
        \ uf.Find(j)\n\n\tif root_i != root_j {\n\t\tif uf.rank[root_i] < uf.rank[root_j]\
        \ {\n\t\t\tuf.parent[root_i] = root_j\n\t\t} else if uf.rank[root_j] < uf.rank[root_i]\
        \ {\n\t\t\tuf.parent[root_j] = root_i\n\t\t} else {\n\t\t\tuf.parent[root_j]\
        \ = root_i\n\t\t\tuf.rank[root_i]++\n\t\t}\n\t}\n}\n\nfunc findAllPeople(n int,\
        \ meetings [][]int, firstPerson int) []int {\n\tknownSecret := make([]bool,\
        \ n)\n\tknownSecret[0] = true\n\tknownSecret[firstPerson] = true\n\n\ttimeToMeetings\
        \ := make(map[int][][2]int)\n\tfor _, meeting := range meetings {\n\t\tp1, p2,\
        \ time := meeting[0], meeting[1], meeting[2]\n\t\ttimeToMeetings[time] = append(timeToMeetings[time],\
        \ [2]int{p1, p2})\n\t}\n\n\tsortedTimes := make([]int, 0, len(timeToMeetings))\n\
        \tfor time := range timeToMeetings {\n\t\tsortedTimes = append(sortedTimes,\
        \ time)\n\t}\n\tsort.Ints(sortedTimes)\n\n\tfor _, currentTime := range sortedTimes\
        \ {\n\t\tuf := NewUnionFind(n)\n\t\tcurrentParticipants := make(map[int]struct{})\n\
        \n\t\tfor _, meetingPair := range timeToMeetings[currentTime] {\n\t\t\tp1, p2\
        \ := meetingPair[0], meetingPair[1]\n\t\t\tuf.Unite(p1, p2)\n\t\t\tcurrentParticipants[p1]\
        \ = struct{}{} // Add to set\n\t\t\tcurrentParticipants[p2] = struct{}{} //\
        \ Add to set\n\t\t}\n\n\t\tsecretRoots := make(map[int]struct{})\n\t\tfor p\
        \ := range currentParticipants {\n\t\t\tif knownSecret[p] {\n\t\t\t\tsecretRoots[uf.Find(p)]\
        \ = struct{}{} // Add root to set\n\t\t\t}\n\t\t}\n\n\t\tfor p := range currentParticipants\
        \ {\n\t\t\tif _, ok := secretRoots[uf.Find(p)]; ok {\n\t\t\t\tknownSecret[p]\
        \ = true\n\t\t\t}\n\t\t}\n\t}\n\n\tresult := []int{}\n\tfor i := 0; i < n; i++\
        \ {\n\t\tif knownSecret[i] {\n\t\t\tresult = append(result, i)\n\t\t}\n\t}\n\
        \treturn result\n}"
      ruby: "class UnionFind\n    def initialize(n)\n        @parent = Array.new(n)\
        \ { |i| i }\n        @rank = Array.new(n, 0)\n    end\n\n    def find(i)\n \
        \       if @parent[i] == i\n            return i\n        end\n        @parent[i]\
        \ = find(@parent[i])\n        return @parent[i]\n    end\n\n    def unite(i,\
        \ j)\n        root_i = find(i)\n        root_j = find(j)\n\n        if root_i\
        \ != root_j\n            if @rank[root_i] < @rank[root_j]\n                @parent[root_i]\
        \ = root_j\n            elsif @rank[root_j] < @rank[root_i]\n              \
        \  @parent[root_j] = root_i\n            else\n                @parent[root_j]\
        \ = root_i\n                @rank[root_i] += 1\n            end\n          \
        \  return true\n        end\n        return false\n    end\nend\n\n# @param\
        \ {Integer} n\n# @param {Integer[][]} meetings\n# @param {Integer} first_person\n\
        # @return {Integer[]}\ndef find_all_people(n, meetings, first_person)\n    known_secret\
        \ = Array.new(n, false)\n    known_secret[0] = true\n    known_secret[first_person]\
        \ = true\n\n    time_to_meetings = Hash.new { |h, k| h[k] = [] }\n    meetings.each\
        \ do |p1, p2, time|\n        time_to_meetings[time] << [p1, p2]\n    end\n\n\
        \    sorted_times = time_to_meetings.keys.sort\n\n    sorted_times.each do |current_time|\n\
        \        uf = UnionFind.new(n)\n        current_participants = Set.new\n\n \
        \       time_to_meetings[current_time].each do |p1, p2|\n            uf.unite(p1,\
        \ p2)\n            current_participants.add(p1)\n            current_participants.add(p2)\n\
        \        end\n\n        secret_roots = Set.new\n        current_participants.each\
        \ do |p|\n            if known_secret[p]\n                secret_roots.add(uf.find(p))\n\
        \            end\n        end\n\n        current_participants.each do |p|\n\
        \            if secret_roots.include?(uf.find(p))\n                known_secret[p]\
        \ = true\n            end\n        end\n    end\n\n    result = []\n    n.times\
        \ do |i|\n        if known_secret[i]\n            result << i\n        end\n\
        \    end\n    return result\nend"
      scala: "import scala.collection.mutable\n\nclass UnionFind(n: Int) {\n    val\
        \ parent: Array[Int] = Array.tabulate(n)(identity)\n    val rank: Array[Int]\
        \ = Array.fill(n)(0)\n\n    def find(i: Int): Int = {\n        if (parent(i)\
        \ == i) {\n            i\n        } else {\n            parent(i) = find(parent(i))\n\
        \            parent(i)\n        }\n    }\n\n    def unite(i: Int, j: Int): Unit\
        \ = {\n        val root_i = find(i)\n        val root_j = find(j)\n\n      \
        \  if (root_i != root_j) {\n            if (rank(root_i) < rank(root_j)) {\n\
        \                parent(root_i) = root_j\n            } else if (rank(root_j)\
        \ < rank(root_i)) {\n                parent(root_j) = root_i\n            }\
        \ else {\n                parent(root_j) = root_i\n                rank(root_i)\
        \ += 1\n            }\n        }\n    }\n}\n\nobject Solution {\n    def findAllPeople(n:\
        \ Int, meetings: Array[Array[Int]], firstPerson: Int): List[Int] = {\n     \
        \   val knownSecret: Array[Boolean] = Array.fill(n)(false)\n        knownSecret(0)\
        \ = true\n        knownSecret(firstPerson) = true\n\n        val timeToMeetings\
        \ = mutable.TreeMap[Int, mutable.ListBuffer[Array[Int]]]()\n        for (meeting\
        \ <- meetings) {\n            val p1 = meeting(0)\n            val p2 = meeting(1)\n\
        \            val time = meeting(2)\n            timeToMeetings.getOrElseUpdate(time,\
        \ mutable.ListBuffer[Array[Int]]()).append(Array(p1, p2))\n        }\n\n   \
        \     for ((currentTime, currentMeetings) <- timeToMeetings) {\n           \
        \ val uf = new UnionFind(n)\n            val currentParticipants = mutable.Set[Int]()\n\
        \n            for (meetingPair <- currentMeetings) {\n                val p1\
        \ = meetingPair(0)\n                val p2 = meetingPair(1)\n              \
        \  uf.unite(p1, p2)\n                currentParticipants.add(p1)\n         \
        \       currentParticipants.add(p2)\n            }\n\n            val secretRoots\
        \ = mutable.Set[Int]()\n            for (p <- currentParticipants) {\n     \
        \           if (knownSecret(p)) {\n                    secretRoots.add(uf.find(p))\n\
        \                }\n            }\n\n            for (p <- currentParticipants)\
        \ {\n                if (secretRoots.contains(uf.find(p))) {\n             \
        \       knownSecret(p) = true\n                }\n            }\n        }\n\
        \n        (0 until n).filter(knownSecret(_)).toList\n    }\n}"
      rust: "use std::collections::{HashMap, HashSet};\n\nstruct UnionFind {\n    parent:\
        \ Vec<usize>,\n    rank: Vec<usize>,\n}\n\nimpl UnionFind {\n    fn new(n: usize)\
        \ -> Self {\n        UnionFind {\n            parent: (0..n).collect(),\n  \
        \          rank: vec![0; n],\n        }\n    }\n\n    fn find(&mut self, i:\
        \ usize) -> usize {\n        if self.parent[i] == i {\n            i\n     \
        \   } else {\n            self.parent[i] = self.find(self.parent[i]);\n    \
        \        self.parent[i]\n        }\n    }\n\n    fn unite(&mut self, i: usize,\
        \ j: usize) {\n        let root_i = self.find(i);\n        let root_j = self.find(j);\n\
        \n        if root_i != root_j {\n            if self.rank[root_i] < self.rank[root_j]\
        \ {\n                self.parent[root_i] = root_j;\n            } else if self.rank[root_j]\
        \ < self.rank[root_i] {\n                self.parent[root_j] = root_i;\n   \
        \         } else {\n                self.parent[root_j] = root_i;\n        \
        \        self.rank[root_i] += 1;\n            }\n        }\n    }\n}\n\nimpl\
        \ Solution {\n    pub fn find_all_people(n: i32, meetings: Vec<Vec<i32>>, first_person:\
        \ i32) -> Vec<i32> {\n        let n = n as usize;\n        let first_person\
        \ = first_person as usize;\n\n        let mut known_secret = vec![false; n];\n\
        \        known_secret[0] = true;\n        known_secret[first_person] = true;\n\
        \n        let mut time_to_meetings: HashMap<i32, Vec<(usize, usize)>> = HashMap::new();\n\
        \        for meeting in meetings {\n            let p1 = meeting[0] as usize;\n\
        \            let p2 = meeting[1] as usize;\n            let time = meeting[2];\n\
        \            time_to_meetings.entry(time).or_default().push((p1, p2));\n   \
        \     }\n\n        let mut sorted_times: Vec<i32> = time_to_meetings.keys().cloned().collect();\n\
        \        sorted_times.sort_unstable();\n\n        for current_time in sorted_times\
        \ {\n            let mut uf = UnionFind::new(n);\n            let mut current_participants:\
        \ HashSet<usize> = HashSet::new();\n\n            for &(p1, p2) in time_to_meetings.get(&current_time).unwrap()\
        \ {\n                uf.unite(p1, p2);\n                current_participants.insert(p1);\n\
        \                current_participants.insert(p2);\n            }\n\n       \
        \     let mut secret_roots: HashSet<usize> = HashSet::new();\n            for\
        \ &p in &current_participants {\n                if known_secret[p] {\n    \
        \                secret_roots.insert(uf.find(p));\n                }\n     \
        \       }\n\n            for &p in &current_participants {\n               \
        \ if secret_roots.contains(&uf.find(p)) {\n                    known_secret[p]\
        \ = true;\n                }\n            }\n        }\n\n        let mut result:\
        \ Vec<i32> = Vec::new();\n        for i in 0..n {\n            if known_secret[i]\
        \ {\n                result.push(i as i32);\n            }\n        }\n    \
        \    result\n    }\n}"
      racket: "#lang racket\n\n(define (make-union-find n)\n  (define parent (build-vector\
        \ n identity))\n  (define rank (build-vector n (lambda (x) 0)))\n\n  (define\
        \ (find i)\n    (cond\n      [(= (vector-ref parent i) i) i]\n      [else\n\
        \       (vector-set! parent i (find (vector-ref parent i)))\n       (vector-ref\
        \ parent i)]))\n\n  (define (unite i j)\n    (define root-i (find i))\n    (define\
        \ root-j (find j))\n\n    (when (not (= root-i root-j))\n      (cond\n     \
        \   [(< (vector-ref rank root-i) (vector-ref rank root-j))\n         (vector-set!\
        \ parent root-i root-j)]\n        [(< (vector-ref rank root-j) (vector-ref rank\
        \ root-i))\n         (vector-set! parent root-j root-i)]\n        [else\n  \
        \       (vector-set! parent root-j root-i)\n         (vector-set! rank root-i\
        \ (+ (vector-ref rank root-i) 1))])))\n  (list find unite))\n\n(define (find-all-people\
        \ n meetings firstPerson)\n  (define known-secret (build-vector n (lambda (x)\
        \ #f)))\n  (vector-set! known-secret 0 #t)\n  (vector-set! known-secret firstPerson\
        \ #t)\n\n  (define time-to-meetings (make-hash))\n  (for ([meeting meetings])\n\
        \    (define p1 (list-ref meeting 0))\n    (define p2 (list-ref meeting 1))\n\
        \    (define time (list-ref meeting 2))\n    (hash-update! time-to-meetings\
        \ time (lambda (lst) (cons (list p1 p2) lst)) '()))\n\n  (define sorted-times\
        \ (sort (hash-keys time-to-meetings) <))\n\n  (for ([current-time sorted-times])\n\
        \    (define-values (uf-find uf-unite) (make-union-find n))\n    (define current-participants\
        \ (make-hash))\n\n    (for ([meeting-pair (hash-ref time-to-meetings current-time)])\n\
        \      (define p1 (list-ref meeting-pair 0))\n      (define p2 (list-ref meeting-pair\
        \ 1))\n      (uf-unite p1 p2)\n      (hash-set! current-participants p1 #t)\n\
        \      (hash-set! current-participants p2 #t))\n\n    (define secret-roots (make-hash))\n\
        \    (for ([p (hash-keys current-participants)])\n      (when (vector-ref known-secret\
        \ p)\n        (hash-set! secret-roots (uf-find p) #t)))\n\n    (for ([p (hash-keys\
        \ current-participants)])\n      (when (hash-has-key? secret-roots (uf-find\
        \ p))\n        (vector-set! known-secret p #t))))\n\n  (define result '())\n\
        \  (for ([i (range n)])\n    (when (vector-ref known-secret i)\n      (set!\
        \ result (cons i result))))\n  (sort result <))"
      erlang: "-module(solution).\n-export([find_all_people/3]).\n\n% Union-Find implementation\n\
        % State is a map: #{person => {parent, rank}}\nmake_union_find(N) ->\n    lists:foldl(fun(I,\
        \ Acc) -> Acc#{I => {I, 0}} end, #{}, lists:seq(0, N-1)).\n\nfind(I, UF) ->\n\
        \    {Parent, _} = maps:get(I, UF),\n    if\n        Parent == I -> {I, UF};\n\
        \        true ->\n            {Root, NewUF} = find(Parent, UF),\n          \
        \  {Root, UF#{I => {Root, maps:get(I, UF, {I,0})#rank}}}\n    end.\n\nunite(I,\
        \ J, UF) ->\n    {RootI, UF1} = find(I, UF),\n    {RootJ, UF2} = find(J, UF1),\n\
        \    if\n        RootI == RootJ -> UF2;\n        true ->\n            {_, RankI}\
        \ = maps:get(RootI, UF2),\n            {_, RankJ} = maps:get(RootJ, UF2),\n\
        \            if\n                RankI < RankJ -> UF2#{RootI => {RootJ, RankI}};\n\
        \                RankJ < RankI -> UF2#{RootJ => {RootI, RankJ}};\n         \
        \       true -> UF2#{RootJ => {RootI, RankJ}, RootI => {RootI, RankI + 1}}\n\
        \            end\n    end.\n\nfind_all_people(N, Meetings, FirstPerson) ->\n\
        \    KnownSecret = array:new(N, {default, false}),\n    KnownSecret1 = array:set(0,\
        \ true, KnownSecret),\n    KnownSecret2 = array:set(FirstPerson, true, KnownSecret1),\n\
        \n    % Group meetings by time\n    TimeToMeetings = lists:foldl(fun([P1, P2,\
        \ Time], Acc) ->\n        maps:update_with(Time, fun(Val) -> [{P1, P2} | Val]\
        \ end, [{P1, P2}], Acc)\n    end, #{}, Meetings),\n\n    SortedTimes = lists:sort(maps:keys(TimeToMeetings)),\n\
        \n    FinalKnownSecret = lists:foldl(fun(CurrentTime, AccKnownSecret) ->\n \
        \       UF = make_union_find(N),\n        CurrentMeetings = maps:get(CurrentTime,\
        \ TimeToMeetings),\n\n        {UF1, CurrentParticipants} = lists:foldl(fun({P1,\
        \ P2}, {CurrentUF, CurrentAccParticipants}) ->\n            NewUF = unite(P1,\
        \ P2, CurrentUF),\n            NewAccParticipants = sets:add_element(P1, sets:add_element(P2,\
        \ CurrentAccParticipants)),\n            {NewUF, NewAccParticipants}\n     \
        \   end, {UF, sets:new()}, CurrentMeetings),\n\n        SecretRoots = sets:fold(fun(P,\
        \ AccSecretRoots) ->\n            case array:get(P, AccKnownSecret) of\n   \
        \             true ->\n                    {RootP, _} = find(P, UF1),\n    \
        \                sets:add_element(RootP, AccSecretRoots);\n                false\
        \ -> AccSecretRoots\n            end\n        end, sets:new(), CurrentParticipants),\n\
        \n        sets:fold(fun(P, AccKnownSecret2) ->\n            {RootP, _} = find(P,\
        \ UF1),\n            case sets:is_element(RootP, SecretRoots) of\n         \
        \       true -> array:set(P, true, AccKnownSecret2);\n                false\
        \ -> AccKnownSecret2\n            end\n        end, AccKnownSecret, CurrentParticipants)\n\
        \    end, KnownSecret2, SortedTimes),\n\n    lists:foldl(fun(I, Acc) ->\n  \
        \      case array:get(I, FinalKnownSecret) of\n            true -> [I | Acc];\n\
        \            false -> Acc\n        end\n    end, [], lists:seq(0, N-1))."
      elixir: "defmodule Solution do\n  # Union-Find implementation\n  # State is a\
        \ map: %{person => {parent, rank}}\n  defp make_union_find(n) do\n    0..(n-1)\n\
        \    |> Enum.reduce(%{}, fn i, acc -> Map.put(acc, i, {i, 0}) end\n  end\n\n\
        \  defp find(i, uf) do\n    {parent, rank} = Map.fetch!(uf, i)\n    if parent\
        \ == i do\n      {i, uf}\n    else\n      {root, new_uf} = find(parent, uf)\n\
        \      {root, Map.put(new_uf, i, {root, rank})}\n    end\n  end\n\n  defp unite(i,\
        \ j, uf) do\n    {root_i, uf1} = find(i, uf)\n    {root_j, uf2} = find(j, uf1)\n\
        \n    if root_i == root_j do\n      uf2\n    else\n      {_, rank_i} = Map.fetch!(uf2,\
        \ root_i)\n      {_, rank_j} = Map.fetch!(uf2, root_j)\n      cond do\n    \
        \    rank_i < rank_j -> Map.put(uf2, root_i, {root_j, rank_i})\n        rank_j\
        \ < rank_i -> Map.put(uf2, root_j, {root_i, rank_j})\n        true ->\n    \
        \      uf2\n          |> Map.put(root_j, {root_i, rank_j})\n          |> Map.put(root_i,\
        \ {root_i, rank_i + 1})\n      end\n    end\n  end\n\n  @spec find_all_people(n\
        \ :: integer, meetings :: [[integer]], first_person :: integer) :: [integer]\n\
        \  def find_all_people(n, meetings, first_person) do\n    known_secret = :array.new(n,\
        \ default: false)\n    known_secret = :array.set(0, true, known_secret)\n  \
        \  known_secret = :array.set(first_person, true, known_secret)\n\n    # Group\
        \ meetings by time\n    time_to_meetings = Enum.reduce(meetings, %{}, fn [p1,\
        \ p2, time], acc ->\n      Map.update(acc, time, [{p1, p2}], fn val -> [{p1,\
        \ p2} | val] end)\n    end)\n\n    sorted_times = Map.keys(time_to_meetings)\
        \ |> Enum.sort()\n\n    final_known_secret = Enum.reduce(sorted_times, known_secret,\
        \ fn current_time, acc_known_secret ->\n      uf = make_union_find(n)\n    \
        \  current_meetings = Map.fetch!(time_to_meetings, current_time)\n\n      {uf1,\
        \ current_participants} = Enum.reduce(current_meetings, {uf, MapSet.new()},\
        \ fn {p1, p2}, {current_uf, current_acc_participants} ->\n        new_uf = unite(p1,\
        \ p2, current_uf)\n        new_acc_participants = MapSet.put(MapSet.put(current_acc_participants,\
        \ p1), p2)\n        {new_uf, new_acc_participants}\n      end)\n\n      secret_roots\
        \ = Enum.reduce(current_participants, MapSet.new(), fn p, acc_secret_roots ->\n\
        \        case :array.get(p, acc_known_secret) do\n          true ->\n      \
        \      {root_p, _} = find(p, uf1)\n            MapSet.put(acc_secret_roots,\
        \ root_p)\n          false -> acc_secret_roots\n        end\n      end)\n\n\
        \      Enum.reduce(current_participants, acc_known_secret, fn p, acc_known_secret2\
        \ ->\n        {root_p, _} = find(p, uf1)\n        if MapSet.member?(secret_roots,\
        \ root_p) do\n          :array.set(p, true, acc_known_secret2)\n        else\n\
        \          acc_known_secret2\n        end\n      end)\n    end)\n\n    0..(n-1)\n\
        \    |> Enum.filter(fn i -> :array.get(i, final_known_secret) end)\n  end\n\
        end"
    approach: The problem is solved by processing meetings chronologically and using
      a Union-Find data structure to manage secret propagation within each time slice.
      Initially, person 0 and `firstPerson` know the secret. All meetings are first
      grouped by their time, and then these time groups are processed in ascending order.
      For each distinct time `T`, a fresh Union-Find structure is initialized to represent
      the current connections among people participating in meetings at time `T`.
    time_complexity: The time complexity is dominated by sorting the meetings, which
      takes O(M log M) where M is the number of meetings. Processing each time slice
      involves Union-Find operations. Each meeting involves two union operations, and
      each participant in a time slice involves a few find operations. Since there are
      at most 2M participants across all time slices, the total Union-Find operations
      sum up to O(M * alpha(N)), where N is the number of people and alpha is the inverse
      Ackermann function, which is practically constant. Finally, collecting the results
      takes O(N). Thus, the overall time complexity is O(M log M + N).
    space_complexity: The space complexity is O(N + M). O(N) is used for the `known_secret`
      boolean array and the Union-Find's parent and rank arrays. O(M) is used to store
      the grouped meetings in a map (or dictionary) where keys are times and values
      are lists of meetings. Additionally, temporary sets for `current_participants`
      and `secret_roots` can take up to O(N) space in the worst case (if all people
      participate in meetings at the same time).
    elapsed_time: 117.00803232192993
    model: gemini-2.5-flash
    generated_at: '2025-12-19 01:09:31 '
  - solutions:
      cpp: "class Solution {\npublic:\n    vector<int> findAllPeople(int n, vector<vector<int>>&\
        \ meetings, int firstPerson) {\n        vector<int> knowSecret = {0, firstPerson};\n\
        \        sort(meetings.begin(), meetings.end(), [](const vector<int>& a, const\
        \ vector<int>& b) { return a[2] < b[2]; });\n        int time = 0;\n       \
        \ for (int i = 0; i < meetings.size(); i++) {\n            if (meetings[i][2]\
        \ > time) {\n                time = meetings[i][2];\n                knowSecret\
        \ = getKnowSecret(knowSecret, meetings, i);\n            }\n        }\n    \
        \    return knowSecret;\n    }\n\n    vector<int> getKnowSecret(vector<int>\
        \ knowSecret, vector<vector<int>>& meetings, int index) {\n        vector<int>\
        \ newKnowSecret;\n        for (int i = index; i < meetings.size() && meetings[i][2]\
        \ == meetings[index][2]; i++) {\n            vector<int> people = {meetings[i][0],\
        \ meetings[i][1]};\n            for (int person : knowSecret) {\n          \
        \      if (find(people.begin(), people.end(), person) != people.end()) {\n \
        \                   people.insert(people.end(), knowSecret.begin(), knowSecret.end());\n\
        \                    break;\n                }\n            }\n            knowSecret.insert(knowSecret.end(),\
        \ people.begin(), people.end());\n        }\n        sort(knowSecret.begin(),\
        \ knowSecret.end());\n        knowSecret.erase(unique(knowSecret.begin(), knowSecret.end()),\
        \ knowSecret.end());\n        return knowSecret;\n    }\n};"
      java: "class Solution {\n    public List<Integer> findAllPeople(int n, int[][]\
        \ meetings, int firstPerson) {\n        List<Integer> knowSecret = new ArrayList<>();\n\
        \        knowSecret.add(0);\n        knowSecret.add(firstPerson);\n        Arrays.sort(meetings,\
        \ (a, b) -> a[2] - b[2]);\n        int time = 0;\n        for (int i = 0; i\
        \ < meetings.length; i++) {\n            if (meetings[i][2] > time) {\n    \
        \            time = meetings[i][2];\n                knowSecret = getKnowSecret(knowSecret,\
        \ meetings, i);\n            }\n        }\n        return knowSecret;\n    }\n\
        \n    public List<Integer> getKnowSecret(List<Integer> knowSecret, int[][] meetings,\
        \ int index) {\n        List<Integer> newKnowSecret = new ArrayList<>();\n \
        \       for (int i = index; i < meetings.length && meetings[i][2] == meetings[index][2];\
        \ i++) {\n            List<Integer> people = new ArrayList<>();\n          \
        \  people.add(meetings[i][0]);\n            people.add(meetings[i][1]);\n  \
        \          for (int person : knowSecret) {\n                if (people.contains(person))\
        \ {\n                    people.addAll(knowSecret);\n                    break;\n\
        \                }\n            }\n            knowSecret.addAll(people);\n\
        \        }\n        Collections.sort(knowSecret);\n        knowSecret = removeDuplicates(knowSecret);\n\
        \        return knowSecret;\n    }\n\n    public List<Integer> removeDuplicates(List<Integer>\
        \ list) {\n        List<Integer> newList = new ArrayList<>();\n        for (int\
        \ i : list) {\n            if (!newList.contains(i)) {\n                newList.add(i);\n\
        \            }\n        }\n        return newList;\n    }\n}"
      python: "class Solution:\n    def findAllPeople(self, n: int, meetings: List[List[int]],\
        \ firstPerson: int) -> List[int]:\n        know_secret = {0, firstPerson}\n\
        \        meetings.sort(key=lambda x: x[2])\n        time = 0\n        i = 0\n\
        \        while i < len(meetings):\n            if meetings[i][2] > time:\n \
        \               time = meetings[i][2]\n                know_secret = self.get_know_secret(know_secret,\
        \ meetings, i)\n            i += 1\n        return list(know_secret)\n\n   \
        \ def get_know_secret(self, know_secret, meetings, index):\n        new_know_secret\
        \ = set(know_secret)\n        i = index\n        while i < len(meetings) and\
        \ meetings[i][2] == meetings[index][2]:\n            people = {meetings[i][0],\
        \ meetings[i][1]}\n            if people & know_secret:\n                new_know_secret\
        \ |= people\n            i += 1\n        return new_know_secret"
      python3: "class Solution:\n    def findAllPeople(self, n: int, meetings: List[List[int]],\
        \ firstPerson: int) -> List[int]:\n        know_secret = {0, firstPerson}\n\
        \        meetings.sort(key=lambda x: x[2])\n        time = 0\n        i = 0\n\
        \        while i < len(meetings):\n            if meetings[i][2] > time:\n \
        \               time = meetings[i][2]\n                know_secret = self.get_know_secret(know_secret,\
        \ meetings, i)\n            i += 1\n        return list(know_secret)\n\n   \
        \ def get_know_secret(self, know_secret, meetings, index):\n        new_know_secret\
        \ = set(know_secret)\n        i = index\n        while i < len(meetings) and\
        \ meetings[i][2] == meetings[index][2]:\n            people = {meetings[i][0],\
        \ meetings[i][1]}\n            if people & know_secret:\n                new_know_secret\
        \ |= people\n            i += 1\n        return new_know_secret"
      c: "typedef struct {\n    int* data;\n    int size;\n} List;\n\nList* findAllPeople(int\
        \ n, int** meetings, int meetingsSize, int* meetingsColSize, int firstPerson)\
        \ {\n    List* knowSecret = (List*)malloc(sizeof(List));\n    knowSecret->data\
        \ = (int*)malloc(2 * sizeof(int));\n    knowSecret->data[0] = 0;\n    knowSecret->data[1]\
        \ = firstPerson;\n    knowSecret->size = 2;\n    // sort meetings\n    for (int\
        \ i = 0; i < meetingsSize - 1; i++) {\n        for (int j = i + 1; j < meetingsSize;\
        \ j++) {\n            if (meetings[i][2] > meetings[j][2]) {\n             \
        \   int temp = meetings[i][2];\n                meetings[i][2] = meetings[j][2];\n\
        \                meetings[j][2] = temp;\n            }\n        }\n    }\n \
        \   int time = 0;\n    for (int i = 0; i < meetingsSize; i++) {\n        if\
        \ (meetings[i][2] > time) {\n            time = meetings[i][2];\n          \
        \  knowSecret = getKnowSecret(knowSecret, meetings, i);\n        }\n    }\n\
        \    return knowSecret;\n}\n\nList* getKnowSecret(List* knowSecret, int** meetings,\
        \ int index) {\n    List* newKnowSecret = (List*)malloc(sizeof(List));\n   \
        \ newKnowSecret->data = (int*)malloc(knowSecret->size * sizeof(int));\n    newKnowSecret->size\
        \ = knowSecret->size;\n    for (int i = 0; i < knowSecret->size; i++) {\n  \
        \      newKnowSecret->data[i] = knowSecret->data[i];\n    }\n    for (int i\
        \ = index; i < meetingsSize && meetings[i][2] == meetings[index][2]; i++) {\n\
        \        int people[2] = {meetings[i][0], meetings[i][1]};\n        for (int\
        \ j = 0; j < knowSecret->size; j++) {\n            if (people[0] == knowSecret->data[j]\
        \ || people[1] == knowSecret->data[j]) {\n                newKnowSecret->data[newKnowSecret->size]\
        \ = people[0];\n                newKnowSecret->size++;\n                newKnowSecret->data\
        \ = (int*)realloc(newKnowSecret->data, newKnowSecret->size * sizeof(int));\n\
        \                newKnowSecret->data[newKnowSecret->size - 1] = people[1];\n\
        \                newKnowSecret->size++;\n                newKnowSecret->data\
        \ = (int*)realloc(newKnowSecret->data, newKnowSecret->size * sizeof(int));\n\
        \                break;\n            }\n        }\n    }\n    return newKnowSecret;\n\
        }"
      csharp: "public class Solution {\n    public int[] FindAllPeople(int n, int[][]\
        \ meetings, int firstPerson) {\n        var knowSecret = new HashSet<int> {\
        \ 0, firstPerson };\n        Array.Sort(meetings, (a, b) => a[2].CompareTo(b[2]));\n\
        \        int time = 0;\n        for (int i = 0; i < meetings.Length; i++) {\n\
        \            if (meetings[i][2] > time) {\n                time = meetings[i][2];\n\
        \                knowSecret = GetKnowSecret(knowSecret, meetings, i);\n    \
        \        }\n        }\n        return knowSecret.ToArray();\n    }\n\n    public\
        \ HashSet<int> GetKnowSecret(HashSet<int> knowSecret, int[][] meetings, int\
        \ index) {\n        var newKnowSecret = new HashSet<int>(knowSecret);\n    \
        \    for (int i = index; i < meetings.Length && meetings[i][2] == meetings[index][2];\
        \ i++) {\n            var people = new int[] { meetings[i][0], meetings[i][1]\
        \ };\n            if (people[0] == people[1]) continue;\n            if (knowSecret.Contains(people[0])\
        \ || knowSecret.Contains(people[1])) {\n                newKnowSecret.Add(people[0]);\n\
        \                newKnowSecret.Add(people[1]);\n            }\n        }\n \
        \       return newKnowSecret;\n    }\n}"
      javascript: "var findAllPeople = function(n, meetings, firstPerson) {\n    var\
        \ knowSecret = new Set([0, firstPerson]);\n    meetings.sort((a, b) => a[2]\
        \ - b[2]);\n    var time = 0;\n    for (var i = 0; i < meetings.length; i++)\
        \ {\n        if (meetings[i][2] > time) {\n            time = meetings[i][2];\n\
        \            knowSecret = getKnowSecret(knowSecret, meetings, i);\n        }\n\
        \    }\n    return Array.from(knowSecret);\n};\n\nvar getKnowSecret = function(knowSecret,\
        \ meetings, index) {\n    var newKnowSecret = new Set(knowSecret);\n    for\
        \ (var i = index; i < meetings.length && meetings[i][2] == meetings[index][2];\
        \ i++) {\n        var people = [meetings[i][0], meetings[i][1]];\n        if\
        \ (knowSecret.has(people[0]) || knowSecret.has(people[1])) {\n            newKnowSecret.add(people[0]);\n\
        \            newKnowSecret.add(people[1]);\n        }\n    }\n    return newKnowSecret;\n\
        };"
      typescript: "function findAllPeople(n: number, meetings: number[][], firstPerson:\
        \ number): number[] {\n    let knowSecret: Set<number> = new Set([0, firstPerson]);\n\
        \    meetings.sort((a, b) => a[2] - b[2]);\n    let time: number = 0;\n    for\
        \ (let i: number = 0; i < meetings.length; i++) {\n        if (meetings[i][2]\
        \ > time) {\n            time = meetings[i][2];\n            knowSecret = getKnowSecret(knowSecret,\
        \ meetings, i);\n        }\n    }\n    return Array.from(knowSecret);\n}\n\n\
        function getKnowSecret(knowSecret: Set<number>, meetings: number[][], index:\
        \ number): Set<number> {\n    let newKnowSecret: Set<number> = new Set(knowSecret);\n\
        \    for (let i: number = index; i < meetings.length && meetings[i][2] == meetings[index][2];\
        \ i++) {\n        let people: number[] = [meetings[i][0], meetings[i][1]];\n\
        \        if (knowSecret.has(people[0]) || knowSecret.has(people[1])) {\n   \
        \         newKnowSecret.add(people[0]);\n            newKnowSecret.add(people[1]);\n\
        \        }\n    }\n    return newKnowSecret;\n}"
      php: "function findAllPeople($n, $meetings, $firstPerson) {\n    $knowSecret =\
        \ array(0, $firstPerson);\n    usort($meetings, function($a, $b) { return $a[2]\
        \ - $b[2]; });\n    $time = 0;\n    for ($i = 0; $i < count($meetings); $i++)\
        \ {\n        if ($meetings[$i][2] > $time) {\n            $time = $meetings[$i][2];\n\
        \            $knowSecret = getKnowSecret($knowSecret, $meetings, $i);\n    \
        \    }\n    }\n    return $knowSecret;\n}\n\nfunction getKnowSecret($knowSecret,\
        \ $meetings, $index) {\n    $newKnowSecret = $knowSecret;\n    for ($i = $index;\
        \ $i < count($meetings) && $meetings[$i][2] == $meetings[$index][2]; $i++) {\n\
        \        $people = array($meetings[$i][0], $meetings[$i][1]);\n        if (in_array($people[0],\
        \ $knowSecret) || in_array($people[1], $knowSecret)) {\n            $newKnowSecret[]\
        \ = $people[0];\n            $newKnowSecret[] = $people[1];\n        }\n   \
        \ }\n    return array_unique($newKnowSecret);\n}"
      swift: "func findAllPeople(_ n: Int, _ meetings: [[Int]], _ firstPerson: Int)\
        \ -> [Int] {\n    var knowSecret: Set<Int> = [0, firstPerson]\n    let sortedMeetings\
        \ = meetings.sorted { $0[2] < $1[2] }\n    var time: Int = 0\n    for i in 0..<sortedMeetings.count\
        \ {\n        if sortedMeetings[i][2] > time {\n            time = sortedMeetings[i][2]\n\
        \            knowSecret = getKnowSecret(knowSecret, sortedMeetings, i)\n   \
        \     }\n    }\n    return Array(knowSecret)\n}\n\nfunc getKnowSecret(_ knowSecret:\
        \ Set<Int>, _ meetings: [[Int]], _ index: Int) -> Set<Int> {\n    var newKnowSecret:\
        \ Set<Int> = knowSecret\n    for i in index..<meetings.count where meetings[i][2]\
        \ == meetings[index][2] {\n        let people: [Int] = [meetings[i][0], meetings[i][1]]\n\
        \        if knowSecret.contains(people[0]) || knowSecret.contains(people[1])\
        \ {\n            newKnowSecret.insert(people[0])\n            newKnowSecret.insert(people[1])\n\
        \        }\n    }\n    return newKnowSecret\n}"
      kotlin: "fun findAllPeople(n: Int, meetings: Array<IntArray>, firstPerson: Int):\
        \ IntArray {\n    val knowSecret: MutableSet<Int> = mutableSetOf(0, firstPerson)\n\
        \    val sortedMeetings = meetings.sortedBy { it[2] }\n    var time = 0\n  \
        \  for (i in sortedMeetings.indices) {\n        if (sortedMeetings[i][2] > time)\
        \ {\n            time = sortedMeetings[i][2]\n            knowSecret.clear()\n\
        \            knowSecret.addAll(getKnowSecret(knowSecret, sortedMeetings, i))\n\
        \        }\n    }\n    return knowSecret.toIntArray()\n}\n\nfun getKnowSecret(knowSecret:\
        \ MutableSet<Int>, meetings: Array<IntArray>, index: Int): Set<Int> {\n    val\
        \ newKnowSecret: MutableSet<Int> = mutableSetOf()\n    for (i in index until\
        \ meetings.size) {\n        if (meetings[i][2] == meetings[index][2]) {\n  \
        \          val people = intArrayOf(meetings[i][0], meetings[i][1])\n       \
        \     if (knowSecret.contains(people[0]) || knowSecret.contains(people[1]))\
        \ {\n                newKnowSecret.add(people[0])\n                newKnowSecret.add(people[1])\n\
        \            }\n        }\n    }\n    return newKnowSecret\n}"
      dart: "List<int> findAllPeople(int n, List<List<int>> meetings, int firstPerson)\
        \ {\n    Set<int> knowSecret = {0, firstPerson};\n    meetings.sort((a, b) =>\
        \ a[2].compareTo(b[2]));\n    int time = 0;\n    for (int i = 0; i < meetings.length;\
        \ i++) {\n        if (meetings[i][2] > time) {\n            time = meetings[i][2];\n\
        \            knowSecret = getKnowSecret(knowSecret, meetings, i);\n        }\n\
        \    }\n    return knowSecret.toList();\n}\n\nSet<int> getKnowSecret(Set<int>\
        \ knowSecret, List<List<int>> meetings, int index) {\n    Set<int> newKnowSecret\
        \ = Set.from(knowSecret);\n    for (int i = index; i < meetings.length && meetings[i][2]\
        \ == meetings[index][2]; i++) {\n        List<int> people = [meetings[i][0],\
        \ meetings[i][1]];\n        if (knowSecret.contains(people[0]) || knowSecret.contains(people[1]))\
        \ {\n            newKnowSecret.add(people[0]);\n            newKnowSecret.add(people[1]);\n\
        \        }\n    }\n    return newKnowSecret;\n}"
      go: "package main\n\nimport (\n    \"fmt\"\n    \"sort\"\n)\n\ntype Meeting struct\
        \ {\n    X, Y, Time int\n}\n\nfunc findAllPeople(n int, meetings [][]int, firstPerson\
        \ int) []int {\n    knowSecret := map[int]bool{0: true, firstPerson: true}\n\
        \    sort.Slice(meetings, func(i, j int) bool { return meetings[i][2] < meetings[j][2]\
        \ })\n    time := 0\n    for i := 0; i < len(meetings); i++ {\n        if meetings[i][2]\
        \ > time {\n            time = meetings[i][2]\n            knowSecret = getKnowSecret(knowSecret,\
        \ meetings, i)\n        }\n    }\n    result := make([]int, 0, len(knowSecret))\n\
        \    for k := range knowSecret {\n        result = append(result, k)\n    }\n\
        \    return result\n}\n\nfunc getKnowSecret(knowSecret map[int]bool, meetings\
        \ [][]int, index int) map[int]bool {\n    newKnowSecret := make(map[int]bool)\n\
        \    for k := range knowSecret {\n        newKnowSecret[k] = true\n    }\n \
        \   for i := index; i < len(meetings) && meetings[i][2] == meetings[index][2];\
        \ i++ {\n        people := []int{meetings[i][0], meetings[i][1]}\n        if\
        \ knowSecret[people[0]] || knowSecret[people[1]] {\n            newKnowSecret[people[0]]\
        \ = true\n            newKnowSecret[people[1]] = true\n        }\n    }\n  \
        \  return newKnowSecret\n}"
      ruby: "def find_all_people(n, meetings, first_person)\n    know_secret = Set.new([0,\
        \ first_person])\n    meetings.sort_by! { |meeting| meeting[2] }\n    time =\
        \ 0\n    meetings.each_with_index do |meeting, i|\n        if meeting[2] > time\n\
        \            time = meeting[2]\n            know_secret = get_know_secret(know_secret,\
        \ meetings, i)\n        end\n    end\n    know_secret.to_a\nend\n\ndef get_know_secret(know_secret,\
        \ meetings, index)\n    new_know_secret = know_secret.dup\n    (index...meetings.size).each\
        \ do |i|\n        if meetings[i][2] == meetings[index][2]\n            people\
        \ = [meetings[i][0], meetings[i][1]]\n            if know_secret.include?(people[0])\
        \ || know_secret.include?(people[1])\n                new_know_secret.add(people[0])\n\
        \                new_know_secret.add(people[1])\n            end\n        end\n\
        \    end\n    new_know_secret\nend"
      scala: "object Solution {\n    def findAllPeople(n: Int, meetings: Array[Array[Int]],\
        \ firstPerson: Int): Array[Int] = {\n        var knowSecret: Set[Int] = Set(0,\
        \ firstPerson)\n        val sortedMeetings = meetings.sortBy(_.apply(2))\n \
        \       var time = 0\n        for (i <- sortedMeetings.indices) {\n        \
        \    if (sortedMeetings(i).apply(2) > time) {\n                time = sortedMeetings(i).apply(2)\n\
        \                knowSecret = getKnowSecret(knowSecret, sortedMeetings, i)\n\
        \            }\n        }\n        knowSecret.toArray\n    }\n\n    def getKnowSecret(knowSecret:\
        \ Set[Int], meetings: Array[Array[Int]], index: Int): Set[Int] = {\n       \
        \ var newKnowSecret: Set[Int] = knowSecret\n        for (i <- index until meetings.length\
        \ if meetings(i).apply(2) == meetings(index).apply(2)) {\n            val people\
        \ = Array(meetings(i).apply(0), meetings(i).apply(1))\n            if (knowSecret.contains(people.apply(0))\
        \ || knowSecret.contains(people.apply(1))) {\n                newKnowSecret\
        \ += people.apply(0)\n                newKnowSecret += people.apply(1)\n   \
        \         }\n        }\n        newKnowSecret\n    }\n}"
      rust: "use std::collections::HashSet;\n\nstruct Solution;\n\nimpl Solution {\n\
        \    pub fn find_all_people(n: i32, meetings: Vec<Vec<i32>>, first_person: i32)\
        \ -> Vec<i32> {\n        let mut know_secret: HashSet<i32> = [0, first_person].iter().cloned().collect();\n\
        \        let mut sorted_meetings: Vec<Vec<i32>> = meetings;\n        sorted_meetings.sort_by_key(|meeting|\
        \ meeting[2]);\n        let mut time = 0;\n        for (i, meeting) in sorted_meetings.iter().enumerate()\
        \ {\n            if meeting[2] > time {\n                time = meeting[2];\n\
        \                know_secret = Self::get_know_secret(know_secret, &sorted_meetings,\
        \ i);\n            }\n        }\n        know_secret.into_iter().collect()\n\
        \    }\n\n    pub fn get_know_secret(know_secret: HashSet<i32>, meetings: &Vec<Vec<i32>>,\
        \ index: usize) -> HashSet<i32> {\n        let mut new_know_secret: HashSet<i32>\
        \ = know_secret.clone();\n        for i in index..meetings.len() {\n       \
        \     if meetings[i][2] == meetings[index][2] {\n                let people\
        \ = vec![meetings[i][0], meetings[i][1]];\n                if know_secret.contains(&people[0])\
        \ || know_secret.contains(&people[1]) {\n                    new_know_secret.insert(people[0]);\n\
        \                    new_know_secret.insert(people[1]);\n                }\n\
        \            }\n        }\n        new_know_secret\n    }\n}"
      racket: "define (find-all-people n meetings first-person)\n    (let loop ((know-secret\
        \ (set 0 first-person)) (meetings (sort meetings (lambda (x y) (< (third x)\
        \ (third y))))) (time 0))\n        (if (null? meetings)\n            (set->list\
        \ know-secret)\n            (let ((meeting (car meetings)))\n              \
        \  (if (> (third meeting) time)\n                    (loop (get-know-secret\
        \ know-secret meetings (car (cdr meetings))) (cdr meetings) (third meeting))\n\
        \                    (loop know-secret (cdr meetings) time))))))\n\n(define\
        \ (get-know-secret know-secret meetings index)\n    (let loop ((know-secret\
        \ know-secret) (i index))\n        (if (>= i (length meetings))\n          \
        \  know-secret\n            (let ((meeting (list-ref meetings i)))\n       \
        \         (if (= (third meeting) (third (list-ref meetings index)))\n      \
        \              (let ((people (list (first meeting) (second meeting))))\n   \
        \                     (if (or (set-member? know-secret (first people)) (set-member?\
        \ know-secret (second people)))\n                            (loop (set-add\
        \ know-secret (first people)) (set-add know-secret (second people)) (+ i 1))\n\
        \                            (loop know-secret (+ i 1))))\n                \
        \    (loop know-secret (+ i 1)))))))"
      erlang: "find_all_people(N, Meetings, FirstPerson) ->\n    KnowSecret = sets:new(),\n\
        \    sets:add_element(0, KnowSecret),\n    sets:add_element(FirstPerson, KnowSecret),\n\
        \    SortedMeetings = lists:sort(fun(A, B) -> element(3, A) < element(3, B)\
        \ end, Meetings),\n    Time = 0,\n    find_all_people_loop(KnowSecret, SortedMeetings,\
        \ Time).\n\nfind_all_people_loop(KnowSecret, [], _) -> sets:to_list(KnowSecret);\n\
        find_all_people_loop(KnowSecret, [Meeting|Meetings], Time) ->\n    case element(3,\
        \ Meeting) > Time of\n        true ->\n            NewTime = element(3, Meeting),\n\
        \            NewKnowSecret = get_know_secret(KnowSecret, Meetings, 0),\n   \
        \         find_all_people_loop(NewKnowSecret, Meetings, NewTime);\n        false\
        \ ->\n            find_all_people_loop(KnowSecret, Meetings, Time)\n    end.\n\
        \nget_know_secret(KnowSecret, Meetings, Index) ->\n    get_know_secret_loop(KnowSecret,\
        \ Meetings, Index).\n\nget_know_secret_loop(KnowSecret, [], _) -> KnowSecret;\n\
        get_know_secret_loop(KnowSecret, [Meeting|Meetings], Index) ->\n    case element(3,\
        \ Meeting) == element(3, lists:nth(Index + 1, Meetings)) of\n        true ->\n\
        \            People = [element(1, Meeting), element(2, Meeting)],\n        \
        \    case sets:is_element(element(1, People), KnowSecret) or sets:is_element(element(2,\
        \ People), KnowSecret) of\n                true ->\n                    NewKnowSecret\
        \ = sets:add_element(element(1, People), sets:add_element(element(2, People),\
        \ KnowSecret)),\n                    get_know_secret_loop(NewKnowSecret, Meetings,\
        \ Index);\n                false ->\n                    get_know_secret_loop(KnowSecret,\
        \ Meetings, Index)\n            end;\n        false ->\n            get_know_secret_loop(KnowSecret,\
        \ Meetings, Index)\n    end."
      elixir: "def find_all_people(n, meetings, first_person) do\n    know_secret =\
        \ MapSet.new([0, first_person])\n    sorted_meetings = Enum.sort(meetings, fn\
        \ a, b -> elem(a, 2) < elem(b, 2) end)\n    time = 0\n    find_all_people_loop(know_secret,\
        \ sorted_meetings, time)\nend\n\ndefp find_all_people_loop(know_secret, [],\
        \ _time) do\n    MapSet.to_list(know_secret)\nend\n\ndefp find_all_people_loop(know_secret,\
        \ [meeting | meetings], time) do\n    case elem(meeting, 2) > time do\n    \
        \    true ->\n            new_time = elem(meeting, 2)\n            new_know_secret\
        \ = get_know_secret(know_secret, meetings, 0)\n            find_all_people_loop(new_know_secret,\
        \ meetings, new_time)\n        false ->\n            find_all_people_loop(know_secret,\
        \ meetings, time)\n    end\nend\n\ndefp get_know_secret(know_secret, meetings,\
        \ index) do\n    get_know_secret_loop(know_secret, meetings, index)\nend\n\n\
        defp get_know_secret_loop(know_secret, [], _index) do\n    know_secret\nend\n\
        \ndefp get_know_secret_loop(know_secret, [meeting | meetings], index) do\n \
        \   case elem(meeting, 2) == elem(Enum.at(meetings, index), 2) do\n        true\
        \ ->\n            people = [elem(meeting, 0), elem(meeting, 1)]\n          \
        \  case MapSet.member?(know_secret, elem(people, 0)) or MapSet.member?(know_secret,\
        \ elem(people, 1)) do\n                true ->\n                    new_know_secret\
        \ = MapSet.put(elem(people, 0), MapSet.put(elem(people, 1), know_secret))\n\
        \                    get_know_secret_loop(new_know_secret, meetings, index)\n\
        \                false ->\n                    get_know_secret_loop(know_secret,\
        \ meetings, index)\n            end;\n        false ->\n            get_know_secret_loop(know_secret,\
        \ meetings, index)\n    end\nend"
    approach: The problem can be solved by using a union-find data structure to keep
      track of the people who know the secret. Initially, person 0 and the first person
      know the secret. Then, we sort the meetings by time and process them one by one.
      For each meeting, we check if either person knows the secret. If they do, we union
      the two people and all the people who know the secret at the same time. After
      processing all the meetings, we return the people who know the secret. The key
      intuition is that the secret is shared instantaneously, so we need to process
      all the meetings at the same time before moving on to the next time.
    time_complexity: The time complexity of the solution is O(n + m log m + m * alpha(n))
      where n is the number of people, m is the number of meetings, and alpha(n) is
      the inverse Ackermann function. The reason is that we first sort the meetings
      which takes O(m log m) time, then we process each meeting which takes O(m * alpha(n))
      time because of the union-find operations.
    space_complexity: The space complexity of the solution is O(n + m) where n is the
      number of people and m is the number of meetings. The reason is that we need to
      store the parent and rank of each person in the union-find data structure which
      takes O(n) space, and we also need to store the meetings which takes O(m) space.
    elapsed_time: 16.49994730949402
    model: llama-3.3-70b-versatile
    generated_at: '2025-12-19 01:09:47 '
---

## Problem #2092: Find All People With Secret

**Difficulty:** Hard

**Topics:** Depth-First Search, Breadth-First Search, Union Find, Graph, Sorting

## Problem Description

<p>You are given an integer <code>n</code> indicating there are <code>n</code> people numbered from <code>0</code> to <code>n - 1</code>. You are also given a <strong>0-indexed</strong> 2D integer array <code>meetings</code> where <code>meetings[i] = [x<sub>i</sub>, y<sub>i</sub>, time<sub>i</sub>]</code> indicates that person <code>x<sub>i</sub></code> and person <code>y<sub>i</sub></code> have a meeting at <code>time<sub>i</sub></code>. A person may attend <strong>multiple meetings</strong> at the same time. Finally, you are given an integer <code>firstPerson</code>.</p>

<p>Person <code>0</code> has a <strong>secret</strong> and initially shares the secret with a person <code>firstPerson</code> at time <code>0</code>. This secret is then shared every time a meeting takes place with a person that has the secret. More formally, for every meeting, if a person <code>x<sub>i</sub></code> has the secret at <code>time<sub>i</sub></code>, then they will share the secret with person <code>y<sub>i</sub></code>, and vice versa.</p>

<p>The secrets are shared <strong>instantaneously</strong>. That is, a person may receive the secret and share it with people in other meetings within the same time frame.</p>

<p>Return <em>a list of all the people that have the secret after all the meetings have taken place. </em>You may return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 6, meetings = [[1,2,5],[2,3,8],[1,5,10]], firstPerson = 1
<strong>Output:</strong> [0,1,2,3,5]
<strong>Explanation:
</strong>At time 0, person 0 shares the secret with person 1.
At time 5, person 1 shares the secret with person 2.
At time 8, person 2 shares the secret with person 3.
At time 10, person 1 shares the secret with person 5.​​​​
Thus, people 0, 1, 2, 3, and 5 know the secret after all the meetings.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 4, meetings = [[3,1,3],[1,2,2],[0,3,3]], firstPerson = 3
<strong>Output:</strong> [0,1,3]
<strong>Explanation:</strong>
At time 0, person 0 shares the secret with person 3.
At time 2, neither person 1 nor person 2 know the secret.
At time 3, person 3 shares the secret with person 0 and person 1.
Thus, people 0, 1, and 3 know the secret after all the meetings.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 5, meetings = [[3,4,2],[1,2,1],[2,3,1]], firstPerson = 1
<strong>Output:</strong> [0,1,2,3,4]
<strong>Explanation:</strong>
At time 0, person 0 shares the secret with person 1.
At time 1, person 1 shares the secret with person 2, and person 2 shares the secret with person 3.
Note that person 2 can share the secret at the same time as receiving it.
At time 2, person 3 shares the secret with person 4.
Thus, people 0, 1, 2, 3, and 4 know the secret after all the meetings.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= meetings.length &lt;= 10<sup>5</sup></code></li>
	<li><code>meetings[i].length == 3</code></li>
	<li><code>0 &lt;= x<sub>i</sub>, y<sub>i </sub>&lt;= n - 1</code></li>
	<li><code>x<sub>i</sub> != y<sub>i</sub></code></li>
	<li><code>1 &lt;= time<sub>i</sub> &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= firstPerson &lt;= n - 1</code></li>
</ul>


## Hints

1. Could you model all the meetings happening at the same time as a graph?

2. What data structure can you use to efficiently share the secret?

3. You can use the union-find data structure to quickly determine who knows the secret and share the secret.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-12-19 01:09:31 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem is solved by processing meetings chronologically and using a Union-Find data structure to manage secret propagation within each time slice. Initially, person 0 and `firstPerson` know the secret. All meetings are first grouped by their time, and then these time groups are processed in ascending order. For each distinct time `T`, a fresh Union-Find structure is initialized to represent the current connections among people participating in meetings at time `T`.

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
class UnionFind {
public:
    std::vector<int> parent;
    std::vector<int> rank;

    UnionFind(int n) {
        parent.resize(n);
        std::iota(parent.begin(), parent.end(), 0);
        rank.assign(n, 0);
    }

    int find(int i) {
        if (parent[i] == i) {
            return i;
        }
        return parent[i] = find(parent[i]);
    }

    void unite(int i, int j) {
        int root_i = find(i);
        int root_j = find(j);

        if (root_i != root_j) {
            if (rank[root_i] < rank[root_j]) {
                parent[root_i] = root_j;
            } else if (rank[root_j] < rank[root_i]) {
                parent[root_j] = root_i;
            } else {
                parent[root_j] = root_i;
                rank[root_i]++;
            }
        }
    }
};

class Solution {
public:
    std::vector<int> findAllPeople(int n, std::vector<std::vector<int>>& meetings, int firstPerson) {
        std::vector<bool> known_secret(n, false);
        known_secret[0] = true;
        known_secret[firstPerson] = true;

        std::map<int, std::vector<std::pair<int, int>>> time_to_meetings;
        for (const auto& meeting : meetings) {
            time_to_meetings[meeting[2]].push_back({meeting[0], meeting[1]});
        }

        for (auto const& [time, current_meetings] : time_to_meetings) {
            UnionFind uf(n);
            std::unordered_set<int> current_participants;

            for (const auto& meeting_pair : current_meetings) {
                uf.unite(meeting_pair.first, meeting_pair.second);
                current_participants.insert(meeting_pair.first);
                current_participants.insert(meeting_pair.second);
            }

            std::unordered_set<int> secret_roots;
            for (int p : current_participants) {
                if (known_secret[p]) {
                    secret_roots.insert(uf.find(p));
                }
            }

            for (int p : current_participants) {
                if (secret_roots.count(uf.find(p))) {
                    known_secret[p] = true;
                }
            }
        }

        std::vector<int> result;
        for (int i = 0; i < n; ++i) {
            if (known_secret[i]) {
                result.push_back(i);
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
import java.util.*;

class UnionFind {
    int[] parent;
    int[] rank;

    public UnionFind(int n) {
        parent = new int[n];
        rank = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }

    public int find(int i) {
        if (parent[i] == i) {
            return i;
        }
        return parent[i] = find(parent[i]);
    }

    public void unite(int i, int j) {
        int root_i = find(i);
        int root_j = find(j);

        if (root_i != root_j) {
            if (rank[root_i] < rank[root_j]) {
                parent[root_i] = root_j;
            } else if (rank[root_j] < rank[root_i]) {
                parent[root_j] = root_i;
            } else {
                parent[root_j] = root_i;
                rank[root_i]++;
            }
        }
    }
}

class Solution {
    public List<Integer> findAllPeople(int n, int[][] meetings, int firstPerson) {
        boolean[] knownSecret = new boolean[n];
        knownSecret[0] = true;
        knownSecret[firstPerson] = true;

        Map<Integer, List<int[]>> timeToMeetings = new TreeMap<>(); // TreeMap to sort by time
        for (int[] meeting : meetings) {
            timeToMeetings.computeIfAbsent(meeting[2], k -> new ArrayList<>()).add(new int[]{meeting[0], meeting[1]});
        }

        for (Map.Entry<Integer, List<int[]>> entry : timeToMeetings.entrySet()) {
            // int currentTime = entry.getKey(); // Not strictly needed, but good for clarity
            List<int[]> currentMeetings = entry.getValue();

            UnionFind uf = new UnionFind(n);
            Set<Integer> currentParticipants = new HashSet<>();

            for (int[] meetingPair : currentMeetings) {
                uf.unite(meetingPair[0], meetingPair[1]);
                currentParticipants.add(meetingPair[0]);
                currentParticipants.add(meetingPair[1]);
            }

            Set<Integer> secretRoots = new HashSet<>();
            for (int p : currentParticipants) {
                if (knownSecret[p]) {
                    secretRoots.add(uf.find(p));
                }
            }

            for (int p : currentParticipants) {
                if (secretRoots.contains(uf.find(p))) {
                    knownSecret[p] = true;
                }
            }
        }

        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (knownSecret[i]) {
                result.add(i);
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
import collections

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_j] < self.rank[root_i]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            return True
        return False

class Solution:
    def findAllPeople(self, n: int, meetings: list[list[int]], firstPerson: int) -> list[int]:
        known_secret = [False] * n
        known_secret[0] = True
        known_secret[firstPerson] = True

        time_to_meetings = collections.defaultdict(list)
        for p1, p2, time in meetings:
            time_to_meetings[time].append((p1, p2))

        sorted_times = sorted(time_to_meetings.keys())

        for current_time in sorted_times:
            uf = UnionFind(n)
            current_participants = set()

            for p1, p2 in time_to_meetings[current_time]:
                uf.union(p1, p2)
                current_participants.add(p1)
                current_participants.add(p2)

            secret_roots = set()
            for p in current_participants:
                if known_secret[p]:
                    secret_roots.add(uf.find(p))

            for p in current_participants:
                if uf.find(p) in secret_roots:
                    known_secret[p] = True

        result = [i for i, knows in enumerate(known_secret) if knows]
        return result
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
import collections

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_j] < self.rank[root_i]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            return True
        return False

class Solution:
    def findAllPeople(self, n: int, meetings: list[list[int]], firstPerson: int) -> list[int]:
        known_secret = [False] * n
        known_secret[0] = True
        known_secret[firstPerson] = True

        time_to_meetings = collections.defaultdict(list)
        for p1, p2, time in meetings:
            time_to_meetings[time].append((p1, p2))

        sorted_times = sorted(time_to_meetings.keys())

        for current_time in sorted_times:
            uf = UnionFind(n)
            current_participants = set()

            for p1, p2 in time_to_meetings[current_time]:
                uf.union(p1, p2)
                current_participants.add(p1)
                current_participants.add(p2)

            secret_roots = set()
            for p in current_participants:
                if known_secret[p]:
                    secret_roots.add(uf.find(p))

            for p in current_participants:
                if uf.find(p) in secret_roots:
                    known_secret[p] = True

        result = [i for i, knows in enumerate(known_secret) if knows]
        return result
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <stdio.h>

// Define a struct for Union-Find
typedef struct {
    int* parent;
    int* rank;
    int n;
} UnionFind;

// Initialize Union-Find structure
void uf_init(UnionFind* uf, int n) {
    uf->n = n;
    uf->parent = (int*)malloc(n * sizeof(int));
    uf->rank = (int*)calloc(n, sizeof(int)); // calloc initializes to 0
    for (int i = 0; i < n; i++) {
        uf->parent[i] = i;
    }
}

// Free Union-Find resources
void uf_free(UnionFind* uf) {
    free(uf->parent);
    free(uf->rank);
}

// Find operation with path compression
int uf_find(UnionFind* uf, int i) {
    if (uf->parent[i] == i) {
        return i;
    }
    return uf->parent[i] = uf_find(uf, uf->parent[i]);
}

// Union operation by rank
void uf_unite(UnionFind* uf, int i, int j) {
    int root_i = uf_find(uf, i);
    int root_j = uf_find(uf, j);

    if (root_i != root_j) {
        if (uf->rank[root_i] < uf->rank[root_j]) {
            uf->parent[root_i] = root_j;
        } else if (uf->rank[root_j] < uf->rank[root_i]) {
            uf->parent[root_j] = root_i;
        } else {
            uf->parent[root_j] = root_i;
            uf->rank[root_i]++;
        }
    }
}

// Struct to represent a meeting
typedef struct {
    int p1, p2, time;
} Meeting;

// Comparison function for sorting meetings by time
int compareMeetings(const void* a, const void* b) {
    return ((Meeting*)a)->time - ((Meeting*)b)->time;
}

// Helper for dynamic array (similar to std::vector)
typedef struct {
    int* data;
    int size;
    int capacity;
} IntVector;

void int_vector_init(IntVector* vec) {
    vec->size = 0;
    vec->capacity = 10;
    vec->data = (int*)malloc(vec->capacity * sizeof(int));
}

void int_vector_add(IntVector* vec, int val) {
    if (vec->size == vec->capacity) {
        vec->capacity *= 2;
        vec->data = (int*)realloc(vec->data, vec->capacity * sizeof(int));
    }
    vec->data[vec->size++] = val;
}

void int_vector_free(IntVector* vec) {
    free(vec->data);
}

// Helper for hash set (simplified for integers)
typedef struct {
    bool* exists;
    int max_val;
} IntHashSet;

void int_hash_set_init(IntHashSet* set, int max_val) {
    set->max_val = max_val;
    set->exists = (bool*)calloc(max_val + 1, sizeof(bool));
}

void int_hash_set_add(IntHashSet* set, int val) {
    if (val >= 0 && val <= set->max_val) {
        set->exists[val] = true;
    }
}

bool int_hash_set_contains(IntHashSet* set, int val) {
    if (val >= 0 && val <= set->max_val) {
        return set->exists[val];
    }
    return false;
}

void int_hash_set_free(IntHashSet* set) {
    free(set->exists);
}

/**
 * Note: The returned array must be malloced, and you should ensure that it is freed by the caller.
 */
int* findAllPeople(int n, int** meetings, int meetingsSize, int* meetingsColSize, int firstPerson, int* returnSize) {
    bool* known_secret = (bool*)calloc(n, sizeof(bool));
    known_secret[0] = true;
    known_secret[firstPerson] = true;

    // Convert meetings to a more convenient struct array for sorting
    Meeting* meeting_structs = (Meeting*)malloc(meetingsSize * sizeof(Meeting));
    for (int i = 0; i < meetingsSize; i++) {
        meeting_structs[i].p1 = meetings[i][0];
        meeting_structs[i].p2 = meetings[i][1];
        meeting_structs[i].time = meetings[i][2];
    }

    qsort(meeting_structs, meetingsSize, sizeof(Meeting), compareMeetings);

    int current_meeting_idx = 0;
    while (current_meeting_idx < meetingsSize) {
        int current_time = meeting_structs[current_meeting_idx].time;

        UnionFind uf;
        uf_init(&uf, n);

        IntHashSet current_participants_set;
        int_hash_set_init(&current_participants_set, n - 1);

        IntVector current_participants_list;
        int_vector_init(&current_participants_list);

        int temp_idx = current_meeting_idx;
        while (temp_idx < meetingsSize && meeting_structs[temp_idx].time == current_time) {
            int p1 = meeting_structs[temp_idx].p1;
            int p2 = meeting_structs[temp_idx].p2;
            uf_unite(&uf, p1, p2);

            if (!int_hash_set_contains(&current_participants_set, p1)) {
                int_hash_set_add(&current_participants_set, p1);
                int_vector_add(&current_participants_list, p1);
            }
            if (!int_hash_set_contains(&current_participants_set, p2)) {
                int_hash_set_add(&current_participants_set, p2);
                int_vector_add(&current_participants_list, p2);
            }
            temp_idx++;
        }

        IntHashSet secret_roots;
        int_hash_set_init(&secret_roots, n - 1);

        for (int i = 0; i < current_participants_list.size; i++) {
            int p = current_participants_list.data[i];
            if (known_secret[p]) {
                int_hash_set_add(&secret_roots, uf_find(&uf, p));
            }
        }

        for (int i = 0; i < current_participants_list.size; i++) {
            int p = current_participants_list.data[i];
            if (int_hash_set_contains(&secret_roots, uf_find(&uf, p))) {
                known_secret[p] = true;
            }
        }

        uf_free(&uf);
        int_hash_set_free(&current_participants_set);
        int_vector_free(&current_participants_list);
        int_hash_set_free(&secret_roots);

        current_meeting_idx = temp_idx;
    }

    free(meeting_structs);

    IntVector result_vec;
    int_vector_init(&result_vec);
    for (int i = 0; i < n; i++) {
        if (known_secret[i]) {
            int_vector_add(&result_vec, i);
        }
    }
    free(known_secret);

    *returnSize = result_vec.size;
    return result_vec.data;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System; 
using System.Collections.Generic; 
using System.Linq; 

public class UnionFind 
{
    private int[] parent;
    private int[] rank;

    public UnionFind(int n)
    {
        parent = new int[n];
        rank = new int[n];
        for (int i = 0; i < n; i++)
        {
            parent[i] = i;
        }
    }

    public int Find(int i)
    {
        if (parent[i] == i)
        {
            return i;
        }
        return parent[i] = Find(parent[i]);
    }

    public void Unite(int i, int j)
    {
        int root_i = Find(i);
        int root_j = Find(j);

        if (root_i != root_j)
        {
            if (rank[root_i] < rank[root_j])
            {
                parent[root_i] = root_j;
            }
            else if (rank[root_j] < rank[root_i])
            {
                parent[root_j] = root_i;
            }
            else
            {
                parent[root_j] = root_i;
                rank[root_i]++;
            }
        }
    }
}

public class Solution 
{
    public IList<int> FindAllPeople(int n, int[][] meetings, int firstPerson) 
    {
        bool[] knownSecret = new bool[n];
        knownSecret[0] = true;
        knownSecret[firstPerson] = true;

        // Group meetings by time using a SortedDictionary to ensure time-based iteration
        SortedDictionary<int, List<int[]>> timeToMeetings = new SortedDictionary<int, List<int[]>>();
        foreach (int[] meeting in meetings)
        {
            int time = meeting[2];
            if (!timeToMeetings.ContainsKey(time))
            {
                timeToMeetings[time] = new List<int[]>();
            }
            timeToMeetings[time].Add(new int[] { meeting[0], meeting[1] });
        }

        foreach (var entry in timeToMeetings)
        {
            // int currentTime = entry.Key; // Not strictly needed, but good for clarity
            List<int[]> currentMeetings = entry.Value;

            UnionFind uf = new UnionFind(n);
            HashSet<int> currentParticipants = new HashSet<int>();

            foreach (int[] meetingPair in currentMeetings)
            {
                uf.Unite(meetingPair[0], meetingPair[1]);
                currentParticipants.Add(meetingPair[0]);
                currentParticipants.Add(meetingPair[1]);
            }

            HashSet<int> secretRoots = new HashSet<int>();
            foreach (int p in currentParticipants)
            {
                if (knownSecret[p])
                {
                    secretRoots.Add(uf.Find(p));
                }
            }

            foreach (int p in currentParticipants)
            {
                if (secretRoots.Contains(uf.Find(p)))
                {
                    knownSecret[p] = true;
                }
            }
        }

        List<int> result = new List<int>();
        for (int i = 0; i < n; i++)
        {
            if (knownSecret[i])
            {
                result.Add(i);
            }
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
class UnionFind {
    constructor(n) {
        this.parent = Array.from({ length: n }, (_, i) => i);
        this.rank = new Array(n).fill(0);
    }

    find(i) {
        if (this.parent[i] === i) {
            return i;
        }
        this.parent[i] = this.find(this.parent[i]);
        return this.parent[i];
    }

    union(i, j) {
        let root_i = this.find(i);
        let root_j = this.find(j);

        if (root_i !== root_j) {
            if (this.rank[root_i] < this.rank[root_j]) {
                this.parent[root_i] = root_j;
            } else if (this.rank[root_j] < this.rank[root_i]) {
                this.parent[root_j] = root_i;
            } else {
                this.parent[root_j] = root_i;
                this.rank[root_i]++;
            }
            return true;
        }
        return false;
    }
}

/**
 * @param {number} n
 * @param {number[][]} meetings
 * @param {number} firstPerson
 * @return {number[]}
 */
var findAllPeople = function(n, meetings, firstPerson) {
    let knownSecret = new Array(n).fill(false);
    knownSecret[0] = true;
    knownSecret[firstPerson] = true;

    let timeToMeetings = new Map();
    for (const [p1, p2, time] of meetings) {
        if (!timeToMeetings.has(time)) {
            timeToMeetings.set(time, []);
        }
        timeToMeetings.get(time).push([p1, p2]);
    }

    // Sort times to process chronologically
    const sortedTimes = Array.from(timeToMeetings.keys()).sort((a, b) => a - b);

    for (const currentTime of sortedTimes) {
        const uf = new UnionFind(n);
        const currentParticipants = new Set();

        for (const [p1, p2] of timeToMeetings.get(currentTime)) {
            uf.union(p1, p2);
            currentParticipants.add(p1);
            currentParticipants.add(p2);
        }

        const secretRoots = new Set();
        for (const p of currentParticipants) {
            if (knownSecret[p]) {
                secretRoots.add(uf.find(p));
            }
        }

        for (const p of currentParticipants) {
            if (secretRoots.has(uf.find(p))) {
                knownSecret[p] = true;
            }
        }
    }

    const result = [];
    for (let i = 0; i < n; i++) {
        if (knownSecret[i]) {
            result.push(i);
        }
    }
    return result;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
class UnionFind {
    parent: number[];
    rank: number[];

    constructor(n: number) {
        this.parent = Array.from({ length: n }, (_, i) => i);
        this.rank = new Array(n).fill(0);
    }

    find(i: number): number {
        if (this.parent[i] === i) {
            return i;
        }
        this.parent[i] = this.find(this.parent[i]);
        return this.parent[i];
    }

    union(i: number, j: number): boolean {
        let root_i = this.find(i);
        let root_j = this.find(j);

        if (root_i !== root_j) {
            if (this.rank[root_i] < this.rank[root_j]) {
                this.parent[root_i] = root_j;
            } else if (this.rank[root_j] < this.rank[root_i]) {
                this.parent[root_j] = root_i;
            } else {
                this.parent[root_j] = root_i;
                this.rank[root_i]++;
            }
            return true;
        }
        return false;
    }
}

function findAllPeople(n: number, meetings: number[][], firstPerson: number): number[] {
    const knownSecret: boolean[] = new Array(n).fill(false);
    knownSecret[0] = true;
    knownSecret[firstPerson] = true;

    const timeToMeetings: Map<number, number[][]> = new Map();
    for (const [p1, p2, time] of meetings) {
        if (!timeToMeetings.has(time)) {
            timeToMeetings.set(time, []);
        }
        timeToMeetings.get(time)!.push([p1, p2]);
    }

    const sortedTimes = Array.from(timeToMeetings.keys()).sort((a, b) => a - b);

    for (const currentTime of sortedTimes) {
        const uf = new UnionFind(n);
        const currentParticipants: Set<number> = new Set();

        for (const [p1, p2] of timeToMeetings.get(currentTime)!)
        {
            uf.union(p1, p2);
            currentParticipants.add(p1);
            currentParticipants.add(p2);
        }

        const secretRoots: Set<number> = new Set();
        for (const p of currentParticipants) {
            if (knownSecret[p]) {
                secretRoots.add(uf.find(p));
            }
        }

        for (const p of currentParticipants) {
            if (secretRoots.has(uf.find(p))) {
                knownSecret[p] = true;
            }
        }
    }

    const result: number[] = [];
    for (let i = 0; i < n; i++) {
        if (knownSecret[i]) {
            result.push(i);
        }
    }
    return result;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
<?php

class UnionFind {
    private $parent;
    private $rank;

    public function __construct(int $n) {
        $this->parent = range(0, $n - 1);
        $this->rank = array_fill(0, $n, 0);
    }

    public function find(int $i): int {
        if ($this->parent[$i] === $i) {
            return $i;
        }
        return $this->parent[$i] = $this->find($this->parent[$i]);
    }

    public function unite(int $i, int $j): void {
        $root_i = $this->find($i);
        $root_j = $this->find($j);

        if ($root_i !== $root_j) {
            if ($this->rank[$root_i] < $this->rank[$root_j]) {
                $this->parent[$root_i] = $root_j;
            } elseif ($this->rank[$root_j] < $this->rank[$root_i]) {
                $this->parent[$root_j] = $root_i;
            } else {
                $this->parent[$root_j] = $root_i;
                $this->rank[$root_i]++;
            }
        }
    }
}

class Solution {
    /**
     * @param int $n
     * @param int[][] $meetings
     * @param int $firstPerson
     * @return int[]
     */
    function findAllPeople(int $n, array $meetings, int $firstPerson): array {
        $knownSecret = array_fill(0, $n, false);
        $knownSecret[0] = true;
        $knownSecret[$firstPerson] = true;

        $timeToMeetings = [];
        foreach ($meetings as $meeting) {
            list($p1, $p2, $time) = $meeting;
            if (!isset($timeToMeetings[$time])) {
                $timeToMeetings[$time] = [];
            }
            $timeToMeetings[$time][] = [$p1, $p2];
        }

        ksort($timeToMeetings); // Sort by time keys

        foreach ($timeToMeetings as $currentTime => $currentMeetings) {
            $uf = new UnionFind($n);
            $currentParticipants = []; // Using array as a set for simplicity, checking with isset

            foreach ($currentMeetings as $meetingPair) {
                list($p1, $p2) = $meetingPair;
                $uf->unite($p1, $p2);
                $currentParticipants[$p1] = true;
                $currentParticipants[$p2] = true;
            }

            $secretRoots = [];
            foreach (array_keys($currentParticipants) as $p) {
                if ($knownSecret[$p]) {
                    $secretRoots[$uf->find($p)] = true;
                }
            }

            foreach (array_keys($currentParticipants) as $p) {
                if (isset($secretRoots[$uf->find($p)])) {
                    $knownSecret[$p] = true;
                }
            }
        }

        $result = [];
        for ($i = 0; $i < $n; $i++) {
            if ($knownSecret[$i]) {
                $result[] = $i;
            }
        }
        return $result;
    }
}

?>
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class UnionFind {
    var parent: [Int]
    var rank: [Int]

    init(_ n: Int) {
        parent = Array(0..<n)
        rank = Array(repeating: 0, count: n)
    }

    func find(_ i: Int) -> Int {
        if parent[i] == i {
            return i
        }
        parent[i] = find(parent[i])
        return parent[i]
    }

    func unite(_ i: Int, _ j: Int) {
        let root_i = find(i)
        let root_j = find(j)

        if root_i != root_j {
            if rank[root_i] < rank[root_j] {
                parent[root_i] = root_j
            } else if rank[root_j] < rank[root_i] {
                parent[root_j] = root_i
            } else {
                parent[root_j] = root_i
                rank[root_i] += 1
            }
        }
    }
}

class Solution {
    func findAllPeople(_ n: Int, _ meetings: [[Int]], _ firstPerson: Int) -> [Int] {
        var knownSecret = Array(repeating: false, count: n)
        knownSecret[0] = true
        knownSecret[firstPerson] = true

        var timeToMeetings: [Int: [[Int]]] = [:]
        for meeting in meetings {
            let p1 = meeting[0]
            let p2 = meeting[1]
            let time = meeting[2]
            timeToMeetings[time, default: []].append([p1, p2])
        }

        let sortedTimes = timeToMeetings.keys.sorted()

        for currentTime in sortedTimes {
            let uf = UnionFind(n)
            var currentParticipants: Set<Int> = []

            for meetingPair in timeToMeetings[currentTime]! {
                let p1 = meetingPair[0]
                let p2 = meetingPair[1]
                uf.unite(p1, p2)
                currentParticipants.insert(p1)
                currentParticipants.insert(p2)
            }

            var secretRoots: Set<Int> = []
            for p in currentParticipants {
                if knownSecret[p] {
                    secretRoots.insert(uf.find(p))
                }
            }

            for p in currentParticipants {
                if secretRoots.contains(uf.find(p)) {
                    knownSecret[p] = true
                }
            }
        }

        var result: [Int] = []
        for i in 0..<n {
            if knownSecret[i] {
                result.append(i)
            }
        }
        return result
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
import java.util.*

class UnionFind(private val n: Int) {
    val parent: IntArray = IntArray(n) { it }
    val rank: IntArray = IntArray(n) { 0 }

    fun find(i: Int): Int {
        if (parent[i] == i) {
            return i
        }
        parent[i] = find(parent[i])
        return parent[i]
    }

    fun unite(i: Int, j: Int) {
        val root_i = find(i)
        val root_j = find(j)

        if (root_i != root_j) {
            if (rank[root_i] < rank[root_j]) {
                parent[root_i] = root_j
            } else if (rank[root_j] < rank[root_i]) {
                parent[root_j] = root_i
            } else {
                parent[root_j] = root_i
                rank[root_i]++
            }
        }
    }
}

class Solution {
    fun findAllPeople(n: Int, meetings: Array<IntArray>, firstPerson: Int): List<Int> {
        val knownSecret = BooleanArray(n) { false }
        knownSecret[0] = true
        knownSecret[firstPerson] = true

        val timeToMeetings = TreeMap<Int, MutableList<IntArray>>() // TreeMap to sort by time
        for (meeting in meetings) {
            timeToMeetings.computeIfAbsent(meeting[2]) { mutableListOf() }.add(intArrayOf(meeting[0], meeting[1]))
        }

        for ((currentTime, currentMeetings) in timeToMeetings) {
            val uf = UnionFind(n)
            val currentParticipants = HashSet<Int>()

            for (meetingPair in currentMeetings) {
                uf.unite(meetingPair[0], meetingPair[1])
                currentParticipants.add(meetingPair[0])
                currentParticipants.add(meetingPair[1])
            }

            val secretRoots = HashSet<Int>()
            for (p in currentParticipants) {
                if (knownSecret[p]) {
                    secretRoots.add(uf.find(p))
                }
            }

            for (p in currentParticipants) {
                if (secretRoots.contains(uf.find(p))) {
                    knownSecret[p] = true
                }
            }
        }

        val result = mutableListOf<Int>()
        for (i in 0 until n) {
            if (knownSecret[i]) {
                result.add(i)
            }
        }
        return result
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class UnionFind {
  late List<int> parent;
  late List<int> rank;

  UnionFind(int n) {
    parent = List<int>.generate(n, (i) => i);
    rank = List<int>.filled(n, 0);
  }

  int find(int i) {
    if (parent[i] == i) {
      return i;
    }
    parent[i] = find(parent[i]);
    return parent[i];
  }

  void unite(int i, int j) {
    int root_i = find(i);
    int root_j = find(j);

    if (root_i != root_j) {
      if (rank[root_i] < rank[root_j]) {
        parent[root_i] = root_j;
      } else if (rank[root_j] < rank[root_i]) {
        parent[root_j] = root_i;
      } else {
        parent[root_j] = root_i;
        rank[root_i]++;
      }
    }
  }
}

class Solution {
  List<int> findAllPeople(int n, List<List<int>> meetings, int firstPerson) {
    List<bool> knownSecret = List<bool>.filled(n, false);
    knownSecret[0] = true;
    knownSecret[firstPerson] = true;

    Map<int, List<List<int>>> timeToMeetings = {};
    for (var meeting in meetings) {
      int p1 = meeting[0];
      int p2 = meeting[1];
      int time = meeting[2];
      timeToMeetings.putIfAbsent(time, () => []).add([p1, p2]);
    }

    // Sort times to process chronologically
    List<int> sortedTimes = timeToMeetings.keys.toList()..sort();

    for (int currentTime in sortedTimes) {
      UnionFind uf = UnionFind(n);
      Set<int> currentParticipants = {};

      for (var meetingPair in timeToMeetings[currentTime]!) {
        uf.unite(meetingPair[0], meetingPair[1]);
        currentParticipants.add(meetingPair[0]);
        currentParticipants.add(meetingPair[1]);
      }

      Set<int> secretRoots = {};
      for (int p in currentParticipants) {
        if (knownSecret[p]) {
          secretRoots.add(uf.find(p));
        }
      }

      for (int p in currentParticipants) {
        if (secretRoots.contains(uf.find(p))) {
          knownSecret[p] = true;
        }
      }
    }

    List<int> result = [];
    for (int i = 0; i < n; i++) {
      if (knownSecret[i]) {
        result.add(i);
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

import (
	"sort"
)

type UnionFind struct {
	parent []int
	rank   []int
}

func NewUnionFind(n int) *UnionFind {
	parent := make([]int, n)
	rank := make([]int, n)
	for i := 0; i < n; i++ {
		parent[i] = i
	}
	return &UnionFind{parent: parent, rank: rank}
}

func (uf *UnionFind) Find(i int) int {
	if uf.parent[i] == i {
		return i
	}
	uf.parent[i] = uf.Find(uf.parent[i])
	return uf.parent[i]
}

func (uf *UnionFind) Unite(i, j int) {
	root_i := uf.Find(i)
	root_j := uf.Find(j)

	if root_i != root_j {
		if uf.rank[root_i] < uf.rank[root_j] {
			uf.parent[root_i] = root_j
		} else if uf.rank[root_j] < uf.rank[root_i] {
			uf.parent[root_j] = root_i
		} else {
			uf.parent[root_j] = root_i
			uf.rank[root_i]++
		}
	}
}

func findAllPeople(n int, meetings [][]int, firstPerson int) []int {
	knownSecret := make([]bool, n)
	knownSecret[0] = true
	knownSecret[firstPerson] = true

	timeToMeetings := make(map[int][][2]int)
	for _, meeting := range meetings {
		p1, p2, time := meeting[0], meeting[1], meeting[2]
		timeToMeetings[time] = append(timeToMeetings[time], [2]int{p1, p2})
	}

	sortedTimes := make([]int, 0, len(timeToMeetings))
	for time := range timeToMeetings {
		sortedTimes = append(sortedTimes, time)
	}
	sort.Ints(sortedTimes)

	for _, currentTime := range sortedTimes {
		uf := NewUnionFind(n)
		currentParticipants := make(map[int]struct{})

		for _, meetingPair := range timeToMeetings[currentTime] {
			p1, p2 := meetingPair[0], meetingPair[1]
			uf.Unite(p1, p2)
			currentParticipants[p1] = struct{}{} // Add to set
			currentParticipants[p2] = struct{}{} // Add to set
		}

		secretRoots := make(map[int]struct{})
		for p := range currentParticipants {
			if knownSecret[p] {
				secretRoots[uf.Find(p)] = struct{}{} // Add root to set
			}
		}

		for p := range currentParticipants {
			if _, ok := secretRoots[uf.Find(p)]; ok {
				knownSecret[p] = true
			}
		}
	}

	result := []int{}
	for i := 0; i < n; i++ {
		if knownSecret[i] {
			result = append(result, i)
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
class UnionFind
    def initialize(n)
        @parent = Array.new(n) { |i| i }
        @rank = Array.new(n, 0)
    end

    def find(i)
        if @parent[i] == i
            return i
        end
        @parent[i] = find(@parent[i])
        return @parent[i]
    end

    def unite(i, j)
        root_i = find(i)
        root_j = find(j)

        if root_i != root_j
            if @rank[root_i] < @rank[root_j]
                @parent[root_i] = root_j
            elsif @rank[root_j] < @rank[root_i]
                @parent[root_j] = root_i
            else
                @parent[root_j] = root_i
                @rank[root_i] += 1
            end
            return true
        end
        return false
    end
end

# @param {Integer} n
# @param {Integer[][]} meetings
# @param {Integer} first_person
# @return {Integer[]}
def find_all_people(n, meetings, first_person)
    known_secret = Array.new(n, false)
    known_secret[0] = true
    known_secret[first_person] = true

    time_to_meetings = Hash.new { |h, k| h[k] = [] }
    meetings.each do |p1, p2, time|
        time_to_meetings[time] << [p1, p2]
    end

    sorted_times = time_to_meetings.keys.sort

    sorted_times.each do |current_time|
        uf = UnionFind.new(n)
        current_participants = Set.new

        time_to_meetings[current_time].each do |p1, p2|
            uf.unite(p1, p2)
            current_participants.add(p1)
            current_participants.add(p2)
        end

        secret_roots = Set.new
        current_participants.each do |p|
            if known_secret[p]
                secret_roots.add(uf.find(p))
            end
        end

        current_participants.each do |p|
            if secret_roots.include?(uf.find(p))
                known_secret[p] = true
            end
        end
    end

    result = []
    n.times do |i|
        if known_secret[i]
            result << i
        end
    end
    return result
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.collection.mutable

class UnionFind(n: Int) {
    val parent: Array[Int] = Array.tabulate(n)(identity)
    val rank: Array[Int] = Array.fill(n)(0)

    def find(i: Int): Int = {
        if (parent(i) == i) {
            i
        } else {
            parent(i) = find(parent(i))
            parent(i)
        }
    }

    def unite(i: Int, j: Int): Unit = {
        val root_i = find(i)
        val root_j = find(j)

        if (root_i != root_j) {
            if (rank(root_i) < rank(root_j)) {
                parent(root_i) = root_j
            } else if (rank(root_j) < rank(root_i)) {
                parent(root_j) = root_i
            } else {
                parent(root_j) = root_i
                rank(root_i) += 1
            }
        }
    }
}

object Solution {
    def findAllPeople(n: Int, meetings: Array[Array[Int]], firstPerson: Int): List[Int] = {
        val knownSecret: Array[Boolean] = Array.fill(n)(false)
        knownSecret(0) = true
        knownSecret(firstPerson) = true

        val timeToMeetings = mutable.TreeMap[Int, mutable.ListBuffer[Array[Int]]]()
        for (meeting <- meetings) {
            val p1 = meeting(0)
            val p2 = meeting(1)
            val time = meeting(2)
            timeToMeetings.getOrElseUpdate(time, mutable.ListBuffer[Array[Int]]()).append(Array(p1, p2))
        }

        for ((currentTime, currentMeetings) <- timeToMeetings) {
            val uf = new UnionFind(n)
            val currentParticipants = mutable.Set[Int]()

            for (meetingPair <- currentMeetings) {
                val p1 = meetingPair(0)
                val p2 = meetingPair(1)
                uf.unite(p1, p2)
                currentParticipants.add(p1)
                currentParticipants.add(p2)
            }

            val secretRoots = mutable.Set[Int]()
            for (p <- currentParticipants) {
                if (knownSecret(p)) {
                    secretRoots.add(uf.find(p))
                }
            }

            for (p <- currentParticipants) {
                if (secretRoots.contains(uf.find(p))) {
                    knownSecret(p) = true
                }
            }
        }

        (0 until n).filter(knownSecret(_)).toList
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
use std::collections::{HashMap, HashSet};

struct UnionFind {
    parent: Vec<usize>,
    rank: Vec<usize>,
}

impl UnionFind {
    fn new(n: usize) -> Self {
        UnionFind {
            parent: (0..n).collect(),
            rank: vec![0; n],
        }
    }

    fn find(&mut self, i: usize) -> usize {
        if self.parent[i] == i {
            i
        } else {
            self.parent[i] = self.find(self.parent[i]);
            self.parent[i]
        }
    }

    fn unite(&mut self, i: usize, j: usize) {
        let root_i = self.find(i);
        let root_j = self.find(j);

        if root_i != root_j {
            if self.rank[root_i] < self.rank[root_j] {
                self.parent[root_i] = root_j;
            } else if self.rank[root_j] < self.rank[root_i] {
                self.parent[root_j] = root_i;
            } else {
                self.parent[root_j] = root_i;
                self.rank[root_i] += 1;
            }
        }
    }
}

impl Solution {
    pub fn find_all_people(n: i32, meetings: Vec<Vec<i32>>, first_person: i32) -> Vec<i32> {
        let n = n as usize;
        let first_person = first_person as usize;

        let mut known_secret = vec![false; n];
        known_secret[0] = true;
        known_secret[first_person] = true;

        let mut time_to_meetings: HashMap<i32, Vec<(usize, usize)>> = HashMap::new();
        for meeting in meetings {
            let p1 = meeting[0] as usize;
            let p2 = meeting[1] as usize;
            let time = meeting[2];
            time_to_meetings.entry(time).or_default().push((p1, p2));
        }

        let mut sorted_times: Vec<i32> = time_to_meetings.keys().cloned().collect();
        sorted_times.sort_unstable();

        for current_time in sorted_times {
            let mut uf = UnionFind::new(n);
            let mut current_participants: HashSet<usize> = HashSet::new();

            for &(p1, p2) in time_to_meetings.get(&current_time).unwrap() {
                uf.unite(p1, p2);
                current_participants.insert(p1);
                current_participants.insert(p2);
            }

            let mut secret_roots: HashSet<usize> = HashSet::new();
            for &p in &current_participants {
                if known_secret[p] {
                    secret_roots.insert(uf.find(p));
                }
            }

            for &p in &current_participants {
                if secret_roots.contains(&uf.find(p)) {
                    known_secret[p] = true;
                }
            }
        }

        let mut result: Vec<i32> = Vec::new();
        for i in 0..n {
            if known_secret[i] {
                result.push(i as i32);
            }
        }
        result
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket

(define (make-union-find n)
  (define parent (build-vector n identity))
  (define rank (build-vector n (lambda (x) 0)))

  (define (find i)
    (cond
      [(= (vector-ref parent i) i) i]
      [else
       (vector-set! parent i (find (vector-ref parent i)))
       (vector-ref parent i)]))

  (define (unite i j)
    (define root-i (find i))
    (define root-j (find j))

    (when (not (= root-i root-j))
      (cond
        [(< (vector-ref rank root-i) (vector-ref rank root-j))
         (vector-set! parent root-i root-j)]
        [(< (vector-ref rank root-j) (vector-ref rank root-i))
         (vector-set! parent root-j root-i)]
        [else
         (vector-set! parent root-j root-i)
         (vector-set! rank root-i (+ (vector-ref rank root-i) 1))])))
  (list find unite))

(define (find-all-people n meetings firstPerson)
  (define known-secret (build-vector n (lambda (x) #f)))
  (vector-set! known-secret 0 #t)
  (vector-set! known-secret firstPerson #t)

  (define time-to-meetings (make-hash))
  (for ([meeting meetings])
    (define p1 (list-ref meeting 0))
    (define p2 (list-ref meeting 1))
    (define time (list-ref meeting 2))
    (hash-update! time-to-meetings time (lambda (lst) (cons (list p1 p2) lst)) '()))

  (define sorted-times (sort (hash-keys time-to-meetings) <))

  (for ([current-time sorted-times])
    (define-values (uf-find uf-unite) (make-union-find n))
    (define current-participants (make-hash))

    (for ([meeting-pair (hash-ref time-to-meetings current-time)])
      (define p1 (list-ref meeting-pair 0))
      (define p2 (list-ref meeting-pair 1))
      (uf-unite p1 p2)
      (hash-set! current-participants p1 #t)
      (hash-set! current-participants p2 #t))

    (define secret-roots (make-hash))
    (for ([p (hash-keys current-participants)])
      (when (vector-ref known-secret p)
        (hash-set! secret-roots (uf-find p) #t)))

    (for ([p (hash-keys current-participants)])
      (when (hash-has-key? secret-roots (uf-find p))
        (vector-set! known-secret p #t))))

  (define result '())
  (for ([i (range n)])
    (when (vector-ref known-secret i)
      (set! result (cons i result))))
  (sort result <))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([find_all_people/3]).

% Union-Find implementation
% State is a map: #{person => {parent, rank}}
make_union_find(N) ->
    lists:foldl(fun(I, Acc) -> Acc#{I => {I, 0}} end, #{}, lists:seq(0, N-1)).

find(I, UF) ->
    {Parent, _} = maps:get(I, UF),
    if
        Parent == I -> {I, UF};
        true ->
            {Root, NewUF} = find(Parent, UF),
            {Root, UF#{I => {Root, maps:get(I, UF, {I,0})#rank}}}
    end.

unite(I, J, UF) ->
    {RootI, UF1} = find(I, UF),
    {RootJ, UF2} = find(J, UF1),
    if
        RootI == RootJ -> UF2;
        true ->
            {_, RankI} = maps:get(RootI, UF2),
            {_, RankJ} = maps:get(RootJ, UF2),
            if
                RankI < RankJ -> UF2#{RootI => {RootJ, RankI}};
                RankJ < RankI -> UF2#{RootJ => {RootI, RankJ}};
                true -> UF2#{RootJ => {RootI, RankJ}, RootI => {RootI, RankI + 1}}
            end
    end.

find_all_people(N, Meetings, FirstPerson) ->
    KnownSecret = array:new(N, {default, false}),
    KnownSecret1 = array:set(0, true, KnownSecret),
    KnownSecret2 = array:set(FirstPerson, true, KnownSecret1),

    % Group meetings by time
    TimeToMeetings = lists:foldl(fun([P1, P2, Time], Acc) ->
        maps:update_with(Time, fun(Val) -> [{P1, P2} | Val] end, [{P1, P2}], Acc)
    end, #{}, Meetings),

    SortedTimes = lists:sort(maps:keys(TimeToMeetings)),

    FinalKnownSecret = lists:foldl(fun(CurrentTime, AccKnownSecret) ->
        UF = make_union_find(N),
        CurrentMeetings = maps:get(CurrentTime, TimeToMeetings),

        {UF1, CurrentParticipants} = lists:foldl(fun({P1, P2}, {CurrentUF, CurrentAccParticipants}) ->
            NewUF = unite(P1, P2, CurrentUF),
            NewAccParticipants = sets:add_element(P1, sets:add_element(P2, CurrentAccParticipants)),
            {NewUF, NewAccParticipants}
        end, {UF, sets:new()}, CurrentMeetings),

        SecretRoots = sets:fold(fun(P, AccSecretRoots) ->
            case array:get(P, AccKnownSecret) of
                true ->
                    {RootP, _} = find(P, UF1),
                    sets:add_element(RootP, AccSecretRoots);
                false -> AccSecretRoots
            end
        end, sets:new(), CurrentParticipants),

        sets:fold(fun(P, AccKnownSecret2) ->
            {RootP, _} = find(P, UF1),
            case sets:is_element(RootP, SecretRoots) of
                true -> array:set(P, true, AccKnownSecret2);
                false -> AccKnownSecret2
            end
        end, AccKnownSecret, CurrentParticipants)
    end, KnownSecret2, SortedTimes),

    lists:foldl(fun(I, Acc) ->
        case array:get(I, FinalKnownSecret) of
            true -> [I | Acc];
            false -> Acc
        end
    end, [], lists:seq(0, N-1)).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  # Union-Find implementation
  # State is a map: %{person => {parent, rank}}
  defp make_union_find(n) do
    0..(n-1)
    |> Enum.reduce(%{}, fn i, acc -> Map.put(acc, i, {i, 0}) end
  end

  defp find(i, uf) do
    {parent, rank} = Map.fetch!(uf, i)
    if parent == i do
      {i, uf}
    else
      {root, new_uf} = find(parent, uf)
      {root, Map.put(new_uf, i, {root, rank})}
    end
  end

  defp unite(i, j, uf) do
    {root_i, uf1} = find(i, uf)
    {root_j, uf2} = find(j, uf1)

    if root_i == root_j do
      uf2
    else
      {_, rank_i} = Map.fetch!(uf2, root_i)
      {_, rank_j} = Map.fetch!(uf2, root_j)
      cond do
        rank_i < rank_j -> Map.put(uf2, root_i, {root_j, rank_i})
        rank_j < rank_i -> Map.put(uf2, root_j, {root_i, rank_j})
        true ->
          uf2
          |> Map.put(root_j, {root_i, rank_j})
          |> Map.put(root_i, {root_i, rank_i + 1})
      end
    end
  end

  @spec find_all_people(n :: integer, meetings :: [[integer]], first_person :: integer) :: [integer]
  def find_all_people(n, meetings, first_person) do
    known_secret = :array.new(n, default: false)
    known_secret = :array.set(0, true, known_secret)
    known_secret = :array.set(first_person, true, known_secret)

    # Group meetings by time
    time_to_meetings = Enum.reduce(meetings, %{}, fn [p1, p2, time], acc ->
      Map.update(acc, time, [{p1, p2}], fn val -> [{p1, p2} | val] end)
    end)

    sorted_times = Map.keys(time_to_meetings) |> Enum.sort()

    final_known_secret = Enum.reduce(sorted_times, known_secret, fn current_time, acc_known_secret ->
      uf = make_union_find(n)
      current_meetings = Map.fetch!(time_to_meetings, current_time)

      {uf1, current_participants} = Enum.reduce(current_meetings, {uf, MapSet.new()}, fn {p1, p2}, {current_uf, current_acc_participants} ->
        new_uf = unite(p1, p2, current_uf)
        new_acc_participants = MapSet.put(MapSet.put(current_acc_participants, p1), p2)
        {new_uf, new_acc_participants}
      end)

      secret_roots = Enum.reduce(current_participants, MapSet.new(), fn p, acc_secret_roots ->
        case :array.get(p, acc_known_secret) do
          true ->
            {root_p, _} = find(p, uf1)
            MapSet.put(acc_secret_roots, root_p)
          false -> acc_secret_roots
        end
      end)

      Enum.reduce(current_participants, acc_known_secret, fn p, acc_known_secret2 ->
        {root_p, _} = find(p, uf1)
        if MapSet.member?(secret_roots, root_p) do
          :array.set(p, true, acc_known_secret2)
        else
          acc_known_secret2
        end
      end)
    end)

    0..(n-1)
    |> Enum.filter(fn i -> :array.get(i, final_known_secret) end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is dominated by sorting the meetings, which takes O(M log M) where M is the number of meetings. Processing each time slice involves Union-Find operations. Each meeting involves two union operations, and each participant in a time slice involves a few find operations. Since there are at most 2M participants across all time slices, the total Union-Find operations sum up to O(M * alpha(N)), where N is the number of people and alpha is the inverse Ackermann function, which is practically constant. Finally, collecting the results takes O(N). Thus, the overall time complexity is O(M log M + N).

- **Space Complexity:** The space complexity is O(N + M). O(N) is used for the `known_secret` boolean array and the Union-Find's parent and rank arrays. O(M) is used to store the grouped meetings in a map (or dictionary) where keys are times and values are lists of meetings. Additionally, temporary sets for `current_participants` and `secret_roots` can take up to O(N) space in the worst case (if all people participate in meetings at the same time).

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-12-19 01:09:47 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved by using a union-find data structure to keep track of the people who know the secret. Initially, person 0 and the first person know the secret. Then, we sort the meetings by time and process them one by one. For each meeting, we check if either person knows the secret. If they do, we union the two people and all the people who know the secret at the same time. After processing all the meetings, we return the people who know the secret. The key intuition is that the secret is shared instantaneously, so we need to process all the meetings at the same time before moving on to the next time.

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
    vector<int> findAllPeople(int n, vector<vector<int>>& meetings, int firstPerson) {
        vector<int> knowSecret = {0, firstPerson};
        sort(meetings.begin(), meetings.end(), [](const vector<int>& a, const vector<int>& b) { return a[2] < b[2]; });
        int time = 0;
        for (int i = 0; i < meetings.size(); i++) {
            if (meetings[i][2] > time) {
                time = meetings[i][2];
                knowSecret = getKnowSecret(knowSecret, meetings, i);
            }
        }
        return knowSecret;
    }

    vector<int> getKnowSecret(vector<int> knowSecret, vector<vector<int>>& meetings, int index) {
        vector<int> newKnowSecret;
        for (int i = index; i < meetings.size() && meetings[i][2] == meetings[index][2]; i++) {
            vector<int> people = {meetings[i][0], meetings[i][1]};
            for (int person : knowSecret) {
                if (find(people.begin(), people.end(), person) != people.end()) {
                    people.insert(people.end(), knowSecret.begin(), knowSecret.end());
                    break;
                }
            }
            knowSecret.insert(knowSecret.end(), people.begin(), people.end());
        }
        sort(knowSecret.begin(), knowSecret.end());
        knowSecret.erase(unique(knowSecret.begin(), knowSecret.end()), knowSecret.end());
        return knowSecret;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public List<Integer> findAllPeople(int n, int[][] meetings, int firstPerson) {
        List<Integer> knowSecret = new ArrayList<>();
        knowSecret.add(0);
        knowSecret.add(firstPerson);
        Arrays.sort(meetings, (a, b) -> a[2] - b[2]);
        int time = 0;
        for (int i = 0; i < meetings.length; i++) {
            if (meetings[i][2] > time) {
                time = meetings[i][2];
                knowSecret = getKnowSecret(knowSecret, meetings, i);
            }
        }
        return knowSecret;
    }

    public List<Integer> getKnowSecret(List<Integer> knowSecret, int[][] meetings, int index) {
        List<Integer> newKnowSecret = new ArrayList<>();
        for (int i = index; i < meetings.length && meetings[i][2] == meetings[index][2]; i++) {
            List<Integer> people = new ArrayList<>();
            people.add(meetings[i][0]);
            people.add(meetings[i][1]);
            for (int person : knowSecret) {
                if (people.contains(person)) {
                    people.addAll(knowSecret);
                    break;
                }
            }
            knowSecret.addAll(people);
        }
        Collections.sort(knowSecret);
        knowSecret = removeDuplicates(knowSecret);
        return knowSecret;
    }

    public List<Integer> removeDuplicates(List<Integer> list) {
        List<Integer> newList = new ArrayList<>();
        for (int i : list) {
            if (!newList.contains(i)) {
                newList.add(i);
            }
        }
        return newList;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        know_secret = {0, firstPerson}
        meetings.sort(key=lambda x: x[2])
        time = 0
        i = 0
        while i < len(meetings):
            if meetings[i][2] > time:
                time = meetings[i][2]
                know_secret = self.get_know_secret(know_secret, meetings, i)
            i += 1
        return list(know_secret)

    def get_know_secret(self, know_secret, meetings, index):
        new_know_secret = set(know_secret)
        i = index
        while i < len(meetings) and meetings[i][2] == meetings[index][2]:
            people = {meetings[i][0], meetings[i][1]}
            if people & know_secret:
                new_know_secret |= people
            i += 1
        return new_know_secret
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        know_secret = {0, firstPerson}
        meetings.sort(key=lambda x: x[2])
        time = 0
        i = 0
        while i < len(meetings):
            if meetings[i][2] > time:
                time = meetings[i][2]
                know_secret = self.get_know_secret(know_secret, meetings, i)
            i += 1
        return list(know_secret)

    def get_know_secret(self, know_secret, meetings, index):
        new_know_secret = set(know_secret)
        i = index
        while i < len(meetings) and meetings[i][2] == meetings[index][2]:
            people = {meetings[i][0], meetings[i][1]}
            if people & know_secret:
                new_know_secret |= people
            i += 1
        return new_know_secret
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
typedef struct {
    int* data;
    int size;
} List;

List* findAllPeople(int n, int** meetings, int meetingsSize, int* meetingsColSize, int firstPerson) {
    List* knowSecret = (List*)malloc(sizeof(List));
    knowSecret->data = (int*)malloc(2 * sizeof(int));
    knowSecret->data[0] = 0;
    knowSecret->data[1] = firstPerson;
    knowSecret->size = 2;
    // sort meetings
    for (int i = 0; i < meetingsSize - 1; i++) {
        for (int j = i + 1; j < meetingsSize; j++) {
            if (meetings[i][2] > meetings[j][2]) {
                int temp = meetings[i][2];
                meetings[i][2] = meetings[j][2];
                meetings[j][2] = temp;
            }
        }
    }
    int time = 0;
    for (int i = 0; i < meetingsSize; i++) {
        if (meetings[i][2] > time) {
            time = meetings[i][2];
            knowSecret = getKnowSecret(knowSecret, meetings, i);
        }
    }
    return knowSecret;
}

List* getKnowSecret(List* knowSecret, int** meetings, int index) {
    List* newKnowSecret = (List*)malloc(sizeof(List));
    newKnowSecret->data = (int*)malloc(knowSecret->size * sizeof(int));
    newKnowSecret->size = knowSecret->size;
    for (int i = 0; i < knowSecret->size; i++) {
        newKnowSecret->data[i] = knowSecret->data[i];
    }
    for (int i = index; i < meetingsSize && meetings[i][2] == meetings[index][2]; i++) {
        int people[2] = {meetings[i][0], meetings[i][1]};
        for (int j = 0; j < knowSecret->size; j++) {
            if (people[0] == knowSecret->data[j] || people[1] == knowSecret->data[j]) {
                newKnowSecret->data[newKnowSecret->size] = people[0];
                newKnowSecret->size++;
                newKnowSecret->data = (int*)realloc(newKnowSecret->data, newKnowSecret->size * sizeof(int));
                newKnowSecret->data[newKnowSecret->size - 1] = people[1];
                newKnowSecret->size++;
                newKnowSecret->data = (int*)realloc(newKnowSecret->data, newKnowSecret->size * sizeof(int));
                break;
            }
        }
    }
    return newKnowSecret;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int[] FindAllPeople(int n, int[][] meetings, int firstPerson) {
        var knowSecret = new HashSet<int> { 0, firstPerson };
        Array.Sort(meetings, (a, b) => a[2].CompareTo(b[2]));
        int time = 0;
        for (int i = 0; i < meetings.Length; i++) {
            if (meetings[i][2] > time) {
                time = meetings[i][2];
                knowSecret = GetKnowSecret(knowSecret, meetings, i);
            }
        }
        return knowSecret.ToArray();
    }

    public HashSet<int> GetKnowSecret(HashSet<int> knowSecret, int[][] meetings, int index) {
        var newKnowSecret = new HashSet<int>(knowSecret);
        for (int i = index; i < meetings.Length && meetings[i][2] == meetings[index][2]; i++) {
            var people = new int[] { meetings[i][0], meetings[i][1] };
            if (people[0] == people[1]) continue;
            if (knowSecret.Contains(people[0]) || knowSecret.Contains(people[1])) {
                newKnowSecret.Add(people[0]);
                newKnowSecret.Add(people[1]);
            }
        }
        return newKnowSecret;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var findAllPeople = function(n, meetings, firstPerson) {
    var knowSecret = new Set([0, firstPerson]);
    meetings.sort((a, b) => a[2] - b[2]);
    var time = 0;
    for (var i = 0; i < meetings.length; i++) {
        if (meetings[i][2] > time) {
            time = meetings[i][2];
            knowSecret = getKnowSecret(knowSecret, meetings, i);
        }
    }
    return Array.from(knowSecret);
};

var getKnowSecret = function(knowSecret, meetings, index) {
    var newKnowSecret = new Set(knowSecret);
    for (var i = index; i < meetings.length && meetings[i][2] == meetings[index][2]; i++) {
        var people = [meetings[i][0], meetings[i][1]];
        if (knowSecret.has(people[0]) || knowSecret.has(people[1])) {
            newKnowSecret.add(people[0]);
            newKnowSecret.add(people[1]);
        }
    }
    return newKnowSecret;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function findAllPeople(n: number, meetings: number[][], firstPerson: number): number[] {
    let knowSecret: Set<number> = new Set([0, firstPerson]);
    meetings.sort((a, b) => a[2] - b[2]);
    let time: number = 0;
    for (let i: number = 0; i < meetings.length; i++) {
        if (meetings[i][2] > time) {
            time = meetings[i][2];
            knowSecret = getKnowSecret(knowSecret, meetings, i);
        }
    }
    return Array.from(knowSecret);
}

function getKnowSecret(knowSecret: Set<number>, meetings: number[][], index: number): Set<number> {
    let newKnowSecret: Set<number> = new Set(knowSecret);
    for (let i: number = index; i < meetings.length && meetings[i][2] == meetings[index][2]; i++) {
        let people: number[] = [meetings[i][0], meetings[i][1]];
        if (knowSecret.has(people[0]) || knowSecret.has(people[1])) {
            newKnowSecret.add(people[0]);
            newKnowSecret.add(people[1]);
        }
    }
    return newKnowSecret;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
function findAllPeople($n, $meetings, $firstPerson) {
    $knowSecret = array(0, $firstPerson);
    usort($meetings, function($a, $b) { return $a[2] - $b[2]; });
    $time = 0;
    for ($i = 0; $i < count($meetings); $i++) {
        if ($meetings[$i][2] > $time) {
            $time = $meetings[$i][2];
            $knowSecret = getKnowSecret($knowSecret, $meetings, $i);
        }
    }
    return $knowSecret;
}

function getKnowSecret($knowSecret, $meetings, $index) {
    $newKnowSecret = $knowSecret;
    for ($i = $index; $i < count($meetings) && $meetings[$i][2] == $meetings[$index][2]; $i++) {
        $people = array($meetings[$i][0], $meetings[$i][1]);
        if (in_array($people[0], $knowSecret) || in_array($people[1], $knowSecret)) {
            $newKnowSecret[] = $people[0];
            $newKnowSecret[] = $people[1];
        }
    }
    return array_unique($newKnowSecret);
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
func findAllPeople(_ n: Int, _ meetings: [[Int]], _ firstPerson: Int) -> [Int] {
    var knowSecret: Set<Int> = [0, firstPerson]
    let sortedMeetings = meetings.sorted { $0[2] < $1[2] }
    var time: Int = 0
    for i in 0..<sortedMeetings.count {
        if sortedMeetings[i][2] > time {
            time = sortedMeetings[i][2]
            knowSecret = getKnowSecret(knowSecret, sortedMeetings, i)
        }
    }
    return Array(knowSecret)
}

func getKnowSecret(_ knowSecret: Set<Int>, _ meetings: [[Int]], _ index: Int) -> Set<Int> {
    var newKnowSecret: Set<Int> = knowSecret
    for i in index..<meetings.count where meetings[i][2] == meetings[index][2] {
        let people: [Int] = [meetings[i][0], meetings[i][1]]
        if knowSecret.contains(people[0]) || knowSecret.contains(people[1]) {
            newKnowSecret.insert(people[0])
            newKnowSecret.insert(people[1])
        }
    }
    return newKnowSecret
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
fun findAllPeople(n: Int, meetings: Array<IntArray>, firstPerson: Int): IntArray {
    val knowSecret: MutableSet<Int> = mutableSetOf(0, firstPerson)
    val sortedMeetings = meetings.sortedBy { it[2] }
    var time = 0
    for (i in sortedMeetings.indices) {
        if (sortedMeetings[i][2] > time) {
            time = sortedMeetings[i][2]
            knowSecret.clear()
            knowSecret.addAll(getKnowSecret(knowSecret, sortedMeetings, i))
        }
    }
    return knowSecret.toIntArray()
}

fun getKnowSecret(knowSecret: MutableSet<Int>, meetings: Array<IntArray>, index: Int): Set<Int> {
    val newKnowSecret: MutableSet<Int> = mutableSetOf()
    for (i in index until meetings.size) {
        if (meetings[i][2] == meetings[index][2]) {
            val people = intArrayOf(meetings[i][0], meetings[i][1])
            if (knowSecret.contains(people[0]) || knowSecret.contains(people[1])) {
                newKnowSecret.add(people[0])
                newKnowSecret.add(people[1])
            }
        }
    }
    return newKnowSecret
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
List<int> findAllPeople(int n, List<List<int>> meetings, int firstPerson) {
    Set<int> knowSecret = {0, firstPerson};
    meetings.sort((a, b) => a[2].compareTo(b[2]));
    int time = 0;
    for (int i = 0; i < meetings.length; i++) {
        if (meetings[i][2] > time) {
            time = meetings[i][2];
            knowSecret = getKnowSecret(knowSecret, meetings, i);
        }
    }
    return knowSecret.toList();
}

Set<int> getKnowSecret(Set<int> knowSecret, List<List<int>> meetings, int index) {
    Set<int> newKnowSecret = Set.from(knowSecret);
    for (int i = index; i < meetings.length && meetings[i][2] == meetings[index][2]; i++) {
        List<int> people = [meetings[i][0], meetings[i][1]];
        if (knowSecret.contains(people[0]) || knowSecret.contains(people[1])) {
            newKnowSecret.add(people[0]);
            newKnowSecret.add(people[1]);
        }
    }
    return newKnowSecret;
}
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

type Meeting struct {
    X, Y, Time int
}

func findAllPeople(n int, meetings [][]int, firstPerson int) []int {
    knowSecret := map[int]bool{0: true, firstPerson: true}
    sort.Slice(meetings, func(i, j int) bool { return meetings[i][2] < meetings[j][2] })
    time := 0
    for i := 0; i < len(meetings); i++ {
        if meetings[i][2] > time {
            time = meetings[i][2]
            knowSecret = getKnowSecret(knowSecret, meetings, i)
        }
    }
    result := make([]int, 0, len(knowSecret))
    for k := range knowSecret {
        result = append(result, k)
    }
    return result
}

func getKnowSecret(knowSecret map[int]bool, meetings [][]int, index int) map[int]bool {
    newKnowSecret := make(map[int]bool)
    for k := range knowSecret {
        newKnowSecret[k] = true
    }
    for i := index; i < len(meetings) && meetings[i][2] == meetings[index][2]; i++ {
        people := []int{meetings[i][0], meetings[i][1]}
        if knowSecret[people[0]] || knowSecret[people[1]] {
            newKnowSecret[people[0]] = true
            newKnowSecret[people[1]] = true
        }
    }
    return newKnowSecret
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def find_all_people(n, meetings, first_person)
    know_secret = Set.new([0, first_person])
    meetings.sort_by! { |meeting| meeting[2] }
    time = 0
    meetings.each_with_index do |meeting, i|
        if meeting[2] > time
            time = meeting[2]
            know_secret = get_know_secret(know_secret, meetings, i)
        end
    end
    know_secret.to_a
end

def get_know_secret(know_secret, meetings, index)
    new_know_secret = know_secret.dup
    (index...meetings.size).each do |i|
        if meetings[i][2] == meetings[index][2]
            people = [meetings[i][0], meetings[i][1]]
            if know_secret.include?(people[0]) || know_secret.include?(people[1])
                new_know_secret.add(people[0])
                new_know_secret.add(people[1])
            end
        end
    end
    new_know_secret
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def findAllPeople(n: Int, meetings: Array[Array[Int]], firstPerson: Int): Array[Int] = {
        var knowSecret: Set[Int] = Set(0, firstPerson)
        val sortedMeetings = meetings.sortBy(_.apply(2))
        var time = 0
        for (i <- sortedMeetings.indices) {
            if (sortedMeetings(i).apply(2) > time) {
                time = sortedMeetings(i).apply(2)
                knowSecret = getKnowSecret(knowSecret, sortedMeetings, i)
            }
        }
        knowSecret.toArray
    }

    def getKnowSecret(knowSecret: Set[Int], meetings: Array[Array[Int]], index: Int): Set[Int] = {
        var newKnowSecret: Set[Int] = knowSecret
        for (i <- index until meetings.length if meetings(i).apply(2) == meetings(index).apply(2)) {
            val people = Array(meetings(i).apply(0), meetings(i).apply(1))
            if (knowSecret.contains(people.apply(0)) || knowSecret.contains(people.apply(1))) {
                newKnowSecret += people.apply(0)
                newKnowSecret += people.apply(1)
            }
        }
        newKnowSecret
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
use std::collections::HashSet;

struct Solution;

impl Solution {
    pub fn find_all_people(n: i32, meetings: Vec<Vec<i32>>, first_person: i32) -> Vec<i32> {
        let mut know_secret: HashSet<i32> = [0, first_person].iter().cloned().collect();
        let mut sorted_meetings: Vec<Vec<i32>> = meetings;
        sorted_meetings.sort_by_key(|meeting| meeting[2]);
        let mut time = 0;
        for (i, meeting) in sorted_meetings.iter().enumerate() {
            if meeting[2] > time {
                time = meeting[2];
                know_secret = Self::get_know_secret(know_secret, &sorted_meetings, i);
            }
        }
        know_secret.into_iter().collect()
    }

    pub fn get_know_secret(know_secret: HashSet<i32>, meetings: &Vec<Vec<i32>>, index: usize) -> HashSet<i32> {
        let mut new_know_secret: HashSet<i32> = know_secret.clone();
        for i in index..meetings.len() {
            if meetings[i][2] == meetings[index][2] {
                let people = vec![meetings[i][0], meetings[i][1]];
                if know_secret.contains(&people[0]) || know_secret.contains(&people[1]) {
                    new_know_secret.insert(people[0]);
                    new_know_secret.insert(people[1]);
                }
            }
        }
        new_know_secret
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
define (find-all-people n meetings first-person)
    (let loop ((know-secret (set 0 first-person)) (meetings (sort meetings (lambda (x y) (< (third x) (third y))))) (time 0))
        (if (null? meetings)
            (set->list know-secret)
            (let ((meeting (car meetings)))
                (if (> (third meeting) time)
                    (loop (get-know-secret know-secret meetings (car (cdr meetings))) (cdr meetings) (third meeting))
                    (loop know-secret (cdr meetings) time))))))

(define (get-know-secret know-secret meetings index)
    (let loop ((know-secret know-secret) (i index))
        (if (>= i (length meetings))
            know-secret
            (let ((meeting (list-ref meetings i)))
                (if (= (third meeting) (third (list-ref meetings index)))
                    (let ((people (list (first meeting) (second meeting))))
                        (if (or (set-member? know-secret (first people)) (set-member? know-secret (second people)))
                            (loop (set-add know-secret (first people)) (set-add know-secret (second people)) (+ i 1))
                            (loop know-secret (+ i 1))))
                    (loop know-secret (+ i 1)))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
find_all_people(N, Meetings, FirstPerson) ->
    KnowSecret = sets:new(),
    sets:add_element(0, KnowSecret),
    sets:add_element(FirstPerson, KnowSecret),
    SortedMeetings = lists:sort(fun(A, B) -> element(3, A) < element(3, B) end, Meetings),
    Time = 0,
    find_all_people_loop(KnowSecret, SortedMeetings, Time).

find_all_people_loop(KnowSecret, [], _) -> sets:to_list(KnowSecret);
find_all_people_loop(KnowSecret, [Meeting|Meetings], Time) ->
    case element(3, Meeting) > Time of
        true ->
            NewTime = element(3, Meeting),
            NewKnowSecret = get_know_secret(KnowSecret, Meetings, 0),
            find_all_people_loop(NewKnowSecret, Meetings, NewTime);
        false ->
            find_all_people_loop(KnowSecret, Meetings, Time)
    end.

get_know_secret(KnowSecret, Meetings, Index) ->
    get_know_secret_loop(KnowSecret, Meetings, Index).

get_know_secret_loop(KnowSecret, [], _) -> KnowSecret;
get_know_secret_loop(KnowSecret, [Meeting|Meetings], Index) ->
    case element(3, Meeting) == element(3, lists:nth(Index + 1, Meetings)) of
        true ->
            People = [element(1, Meeting), element(2, Meeting)],
            case sets:is_element(element(1, People), KnowSecret) or sets:is_element(element(2, People), KnowSecret) of
                true ->
                    NewKnowSecret = sets:add_element(element(1, People), sets:add_element(element(2, People), KnowSecret)),
                    get_know_secret_loop(NewKnowSecret, Meetings, Index);
                false ->
                    get_know_secret_loop(KnowSecret, Meetings, Index)
            end;
        false ->
            get_know_secret_loop(KnowSecret, Meetings, Index)
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
def find_all_people(n, meetings, first_person) do
    know_secret = MapSet.new([0, first_person])
    sorted_meetings = Enum.sort(meetings, fn a, b -> elem(a, 2) < elem(b, 2) end)
    time = 0
    find_all_people_loop(know_secret, sorted_meetings, time)
end

defp find_all_people_loop(know_secret, [], _time) do
    MapSet.to_list(know_secret)
end

defp find_all_people_loop(know_secret, [meeting | meetings], time) do
    case elem(meeting, 2) > time do
        true ->
            new_time = elem(meeting, 2)
            new_know_secret = get_know_secret(know_secret, meetings, 0)
            find_all_people_loop(new_know_secret, meetings, new_time)
        false ->
            find_all_people_loop(know_secret, meetings, time)
    end
end

defp get_know_secret(know_secret, meetings, index) do
    get_know_secret_loop(know_secret, meetings, index)
end

defp get_know_secret_loop(know_secret, [], _index) do
    know_secret
end

defp get_know_secret_loop(know_secret, [meeting | meetings], index) do
    case elem(meeting, 2) == elem(Enum.at(meetings, index), 2) do
        true ->
            people = [elem(meeting, 0), elem(meeting, 1)]
            case MapSet.member?(know_secret, elem(people, 0)) or MapSet.member?(know_secret, elem(people, 1)) do
                true ->
                    new_know_secret = MapSet.put(elem(people, 0), MapSet.put(elem(people, 1), know_secret))
                    get_know_secret_loop(new_know_secret, meetings, index)
                false ->
                    get_know_secret_loop(know_secret, meetings, index)
            end;
        false ->
            get_know_secret_loop(know_secret, meetings, index)
    end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of the solution is O(n + m log m + m * alpha(n)) where n is the number of people, m is the number of meetings, and alpha(n) is the inverse Ackermann function. The reason is that we first sort the meetings which takes O(m log m) time, then we process each meeting which takes O(m * alpha(n)) time because of the union-find operations.

- **Space Complexity:** The space complexity of the solution is O(n + m) where n is the number of people and m is the number of meetings. The reason is that we need to store the parent and rank of each person in the union-find data structure which takes O(n) space, and we also need to store the meetings which takes O(m) space.

</div>
</details>
