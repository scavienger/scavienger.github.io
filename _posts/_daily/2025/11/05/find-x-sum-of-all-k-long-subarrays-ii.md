---
layout: post
title: "Find X-Sum of All K-Long Subarrays II"
date: 2025-11-05 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Hash Table", "Sliding Window", "Heap (Priority Queue)"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-ii/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    vector<long long> findXSum(vector<int>& nums,\
        \ int k, int x) {\n        using Entry = pair<int, int>;\n        set<Entry>\
        \ top, rest;\n        unordered_map<int, int> freq;\n        long long sum =\
        \ 0;\n\n        auto addToTop = [&](Entry e) {\n            top.insert(e);\n\
        \            sum += 1LL * e.first * e.second;\n        };\n        auto addToRest\
        \ = [&](Entry e) {\n            rest.insert(e);\n        };\n        auto removeFromTop\
        \ = [&](Entry e) {\n            top.erase(e);\n            sum -= 1LL * e.first\
        \ * e.second;\n        };\n        auto removeFromRest = [&](Entry e) {\n  \
        \          rest.erase(e);\n        };\n        auto rebalance = [&]() {\n  \
        \          while ((int)top.size() > x) {\n                auto it = top.begin();\n\
        \                Entry e = *it;\n                removeFromTop(e);\n       \
        \         addToRest(e);\n            }\n            while ((int)top.size() <\
        \ x && !rest.empty()) {\n                auto it = prev(rest.end());\n     \
        \           Entry e = *it;\n                removeFromRest(e);\n           \
        \     addToTop(e);\n            }\n            while (!top.empty() && !rest.empty()\
        \ && *top.begin() < *prev(rest.end())) {\n                Entry low = *top.begin();\n\
        \                Entry high = *prev(rest.end());\n                removeFromTop(low);\n\
        \                removeFromRest(high);\n                addToTop(high);\n  \
        \              addToRest(low);\n            }\n        };\n        auto change\
        \ = [&](int value, int delta) {\n            auto it = freq.find(value);\n \
        \           if (it != freq.end() && it->second > 0) {\n                Entry\
        \ oldEntry = {it->second, value};\n                if (top.count(oldEntry))\
        \ removeFromTop(oldEntry);\n                else removeFromRest(oldEntry);\n\
        \            }\n            int next = (it == freq.end() ? 0 : it->second) +\
        \ delta;\n            if (next == 0) {\n                freq.erase(value);\n\
        \            } else {\n                freq[value] = next;\n               \
        \ Entry newEntry = {next, value};\n                if (!top.empty() && newEntry\
        \ >= *top.begin()) addToTop(newEntry);\n                else addToRest(newEntry);\n\
        \            }\n            rebalance();\n        };\n\n        for (int i =\
        \ 0; i < k; ++i) change(nums[i], 1);\n        vector<long long> answer;\n  \
        \      answer.reserve(nums.size() - k + 1);\n        answer.push_back(sum);\n\
        \        for (int i = k; i < (int)nums.size(); ++i) {\n            change(nums[i\
        \ - k], -1);\n            change(nums[i], 1);\n            answer.push_back(sum);\n\
        \        }\n        return answer;\n    }\n};"
      java: "class Solution {\n    public long[] findXSum(int[] nums, int k, int x)\
        \ {\n        TreeSet<long[]> top = new TreeSet<>((a, b) -> {\n            int\
        \ c = Long.compare(a[0], b[0]);\n            if (c != 0) return c;\n       \
        \     return Long.compare(a[1], b[1]);\n        });\n        TreeSet<long[]>\
        \ rest = new TreeSet<>((a, b) -> {\n            int c = Long.compare(a[0], b[0]);\n\
        \            if (c != 0) return c;\n            return Long.compare(a[1], b[1]);\n\
        \        });\n        HashMap<Integer, Integer> freq = new HashMap<>();\n  \
        \      long[] sum = new long[1];\n\n        class Window {\n            void\
        \ addTop(long[] e) {\n                top.add(e);\n                sum[0] +=\
        \ e[0] * e[1];\n            }\n            void addRest(long[] e) {\n      \
        \          rest.add(e);\n            }\n            void removeTop(long[] e)\
        \ {\n                top.remove(e);\n                sum[0] -= e[0] * e[1];\n\
        \            }\n            void removeRest(long[] e) {\n                rest.remove(e);\n\
        \            }\n            void rebalance() {\n                while (top.size()\
        \ > x) {\n                    long[] e = top.first();\n                    removeTop(e);\n\
        \                    addRest(e);\n                }\n                while (top.size()\
        \ < x && !rest.isEmpty()) {\n                    long[] e = rest.last();\n \
        \                   removeRest(e);\n                    addTop(e);\n       \
        \         }\n                while (!top.isEmpty() && !rest.isEmpty() && compare(top.first(),\
        \ rest.last()) < 0) {\n                    long[] low = top.first();\n     \
        \               long[] high = rest.last();\n                    removeTop(low);\n\
        \                    removeRest(high);\n                    addTop(high);\n\
        \                    addRest(low);\n                }\n            }\n     \
        \       int compare(long[] a, long[] b) {\n                int c = Long.compare(a[0],\
        \ b[0]);\n                if (c != 0) return c;\n                return Long.compare(a[1],\
        \ b[1]);\n            }\n            void change(int value, int delta) {\n \
        \               Integer old = freq.get(value);\n                if (old != null\
        \ && old > 0) {\n                    long[] e = new long[]{old, value};\n  \
        \                  if (top.remove(e)) sum[0] -= e[0] * e[1];\n             \
        \       else rest.remove(e);\n                }\n                int next =\
        \ (old == null ? 0 : old) + delta;\n                if (next == 0) {\n     \
        \               freq.remove(value);\n                } else {\n            \
        \        freq.put(value, next);\n                    long[] e = new long[]{next,\
        \ value};\n                    if (!top.isEmpty() && compare(e, top.first())\
        \ >= 0) addTop(e);\n                    else addRest(e);\n                }\n\
        \                rebalance();\n            }\n        }\n\n        Window window\
        \ = new Window();\n        for (int i = 0; i < k; i++) window.change(nums[i],\
        \ 1);\n        long[] answer = new long[nums.length - k + 1];\n        answer[0]\
        \ = sum[0];\n        for (int i = k; i < nums.length; i++) {\n            window.change(nums[i\
        \ - k], -1);\n            window.change(nums[i], 1);\n            answer[i -\
        \ k + 1] = sum[0];\n        }\n        return answer;\n    }\n}"
      python: "class Solution(object):\n    def findXSum(self, nums, k, x):\n      \
        \  \"\"\"\n        :type nums: List[int]\n        :type k: int\n        :type\
        \ x: int\n        :rtype: List[int]\n        \"\"\"\n        import heapq\n\n\
        \        freq = {}\n        top = set()\n        rest = set()\n        total\
        \ = 0\n\n        def key(value):\n            return (freq[value], value)\n\n\
        \        def add_top(entry):\n            nonlocal total\n            top.add(entry)\n\
        \            total += entry[0] * entry[1]\n\n        def remove_top(entry):\n\
        \            nonlocal total\n            top.remove(entry)\n            total\
        \ -= entry[0] * entry[1]\n\n        def rebalance():\n            while len(top)\
        \ > x:\n                entry = min(top)\n                remove_top(entry)\n\
        \                rest.add(entry)\n            while len(top) < x and rest:\n\
        \                entry = max(rest)\n                rest.remove(entry)\n   \
        \             add_top(entry)\n            while top and rest and min(top) <\
        \ max(rest):\n                low = min(top)\n                high = max(rest)\n\
        \                remove_top(low)\n                rest.remove(high)\n      \
        \          add_top(high)\n                rest.add(low)\n\n        def change(value,\
        \ delta):\n            old = freq.get(value, 0)\n            if old:\n     \
        \           entry = (old, value)\n                if entry in top:\n       \
        \             remove_top(entry)\n                else:\n                   \
        \ rest.remove(entry)\n            new = old + delta\n            if new:\n \
        \               freq[value] = new\n                entry = (new, value)\n  \
        \              if top and entry >= min(top):\n                    add_top(entry)\n\
        \                else:\n                    rest.add(entry)\n            else:\n\
        \                freq.pop(value, None)\n            rebalance()\n\n        for\
        \ value in nums[:k]:\n            change(value, 1)\n        answer = [total]\n\
        \        for i in range(k, len(nums)):\n            change(nums[i - k], -1)\n\
        \            change(nums[i], 1)\n            answer.append(total)\n        return\
        \ answer"
      python3: "class Solution:\n    def findXSum(self, nums: List[int], k: int, x:\
        \ int) -> List[int]:\n        import heapq\n\n        freq = {}\n        top\
        \ = set()\n        rest = set()\n        total = 0\n\n        def key(value):\n\
        \            return (freq[value], value)\n\n        def add_top(value):\n  \
        \          nonlocal total\n            top.add(value)\n            total +=\
        \ freq[value] * value\n\n        def add_rest(value):\n            rest.add(value)\n\
        \n        def promote_best():\n            value = max(rest, key=key)\n    \
        \        rest.remove(value)\n            add_top(value)\n\n        def demote_worst():\n\
        \            nonlocal total\n            value = min(top, key=key)\n       \
        \     top.remove(value)\n            total -= freq[value] * value\n        \
        \    rest.add(value)\n\n        def change(value, delta):\n            nonlocal\
        \ total\n            if value in freq:\n                if value in top:\n \
        \                   top.remove(value)\n                    total -= freq[value]\
        \ * value\n                else:\n                    rest.remove(value)\n \
        \               new_count = freq[value] + delta\n            else:\n       \
        \         new_count = delta\n\n            if new_count:\n                freq[value]\
        \ = new_count\n                if len(top) < x:\n                    add_top(value)\n\
        \                elif not rest or (new_count, value) > min((freq[v], v) for\
        \ v in top):\n                    add_top(value)\n                else:\n  \
        \                  add_rest(value)\n            else:\n                del freq[value]\n\
        \n            while len(top) > x:\n                demote_worst()\n        \
        \    while len(top) < x and rest:\n                promote_best()\n        \
        \    while top and rest:\n                worst = min(top, key=key)\n      \
        \          best = max(rest, key=key)\n                if key(worst) >= key(best):\n\
        \                    break\n                top.remove(worst)\n            \
        \    total -= freq[worst] * worst\n                rest.remove(best)\n     \
        \           add_top(best)\n                rest.add(worst)\n\n        for value\
        \ in nums[:k]:\n            change(value, 1)\n\n        answer = [total]\n \
        \       for i in range(k, len(nums)):\n            change(nums[i - k], -1)\n\
        \            change(nums[i], 1)\n            answer.append(total)\n        return\
        \ answer"
      typescript: "function findXSum(nums: number[], k: number, x: number): number[]\
        \ {\n    const freq = new Map<number, number>();\n    const top: [number, number][]\
        \ = [];\n    const rest: [number, number][] = [];\n    let total = 0;\n\n  \
        \  const compare = (a: [number, number], b: [number, number]): number =>\n \
        \       a[0] - b[0] || a[1] - b[1];\n\n    const insert = (set: [number, number][],\
        \ entry: [number, number]): void => {\n        let left = 0;\n        let right\
        \ = set.length;\n        while (left < right) {\n            const mid = (left\
        \ + right) >>> 1;\n            if (compare(set[mid], entry) < 0) left = mid\
        \ + 1;\n            else right = mid;\n        }\n        set.splice(left, 0,\
        \ entry);\n    };\n\n    const remove = (set: [number, number][], entry: [number,\
        \ number]): void => {\n        let left = 0;\n        let right = set.length;\n\
        \        while (left < right) {\n            const mid = (left + right) >>>\
        \ 1;\n            if (compare(set[mid], entry) < 0) left = mid + 1;\n      \
        \      else right = mid;\n        }\n        set.splice(left, 1);\n    };\n\n\
        \    const change = (value: number, delta: number): void => {\n        const\
        \ old = freq.get(value) ?? 0;\n        if (old > 0) {\n            const entry:\
        \ [number, number] = [old, value];\n            const index = top.findIndex(item\
        \ => compare(item, entry) === 0);\n            if (index >= 0) {\n         \
        \       top.splice(index, 1);\n                total -= old * value;\n     \
        \       } else {\n                remove(rest, entry);\n            }\n    \
        \    }\n\n        const next = old + delta;\n        if (next > 0) {\n     \
        \       freq.set(value, next);\n            const entry: [number, number] =\
        \ [next, value];\n            if (top.length < x || compare(entry, top[0]) >\
        \ 0) {\n                insert(top, entry);\n                total += next *\
        \ value;\n            } else {\n                insert(rest, entry);\n     \
        \       }\n        } else {\n            freq.delete(value);\n        }\n\n\
        \        while (top.length > x) {\n            const entry = top.shift()!;\n\
        \            total -= entry[0] * entry[1];\n            insert(rest, entry);\n\
        \        }\n        while (top.length < x && rest.length > 0) {\n          \
        \  const entry = rest.pop()!;\n            insert(top, entry);\n           \
        \ total += entry[0] * entry[1];\n        }\n        while (top.length > 0 &&\
        \ rest.length > 0 && compare(top[0], rest[rest.length - 1]) < 0) {\n       \
        \     const low = top.shift()!;\n            const high = rest.pop()!;\n   \
        \         total += high[0] * high[1] - low[0] * low[1];\n            insert(top,\
        \ high);\n            insert(rest, low);\n        }\n    };\n\n    for (let\
        \ i = 0; i < k; i++) change(nums[i], 1);\n    const answer = [total];\n    for\
        \ (let i = k; i < nums.length; i++) {\n        change(nums[i - k], -1);\n  \
        \      change(nums[i], 1);\n        answer.push(total);\n    }\n    return answer;\n\
        };"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $nums\n     * @param\
        \ Integer $k\n     * @param Integer $x\n     * @return Integer[]\n     */\n\
        \    function findXSum($nums, $k, $x) {\n        $freq = [];\n        $top =\
        \ [];\n        $rest = [];\n        $total = 0;\n\n        $compare = function\
        \ ($a, $b) {\n            return $a[0] <=> $b[0] ?: ($a[1] <=> $b[1]);\n   \
        \     };\n        $insert = function (&$set, $entry) use ($compare) {\n    \
        \        $left = 0;\n            $right = count($set);\n            while ($left\
        \ < $right) {\n                $mid = intdiv($left + $right, 2);\n         \
        \       if ($compare($set[$mid], $entry) < 0) $left = $mid + 1;\n          \
        \      else $right = $mid;\n            }\n            array_splice($set, $left,\
        \ 0, [$entry]);\n        };\n        $remove = function (&$set, $entry) use\
        \ ($compare) {\n            $left = 0;\n            $right = count($set);\n\
        \            while ($left < $right) {\n                $mid = intdiv($left +\
        \ $right, 2);\n                if ($compare($set[$mid], $entry) < 0) $left =\
        \ $mid + 1;\n                else $right = $mid;\n            }\n          \
        \  array_splice($set, $left, 1);\n        };\n\n        $change = function ($value,\
        \ $delta) use (&$freq, &$top, &$rest, &$total, $x, $compare, $insert, $remove)\
        \ {\n            $old = $freq[$value] ?? 0;\n            if ($old > 0) {\n \
        \               $entry = [$old, $value];\n                $left = 0;\n     \
        \           $right = count($top);\n                while ($left < $right) {\n\
        \                    $mid = intdiv($left + $right, 2);\n                   \
        \ if ($compare($top[$mid], $entry) < 0) $left = $mid + 1;\n                \
        \    else $right = $mid;\n                }\n                if ($left < count($top)\
        \ && $compare($top[$left], $entry) === 0) {\n                    array_splice($top,\
        \ $left, 1);\n                    $total -= $old * $value;\n               \
        \ } else {\n                    $remove($rest, $entry);\n                }\n\
        \            }\n\n            $next = $old + $delta;\n            if ($next\
        \ > 0) {\n                $freq[$value] = $next;\n                $entry = [$next,\
        \ $value];\n                if (count($top) < $x || $compare($entry, $top[0])\
        \ > 0) {\n                    $insert($top, $entry);\n                    $total\
        \ += $next * $value;\n                } else {\n                    $insert($rest,\
        \ $entry);\n                }\n            } else {\n                unset($freq[$value]);\n\
        \            }\n\n            while (count($top) > $x) {\n                $entry\
        \ = array_shift($top);\n                $total -= $entry[0] * $entry[1];\n \
        \               $insert($rest, $entry);\n            }\n            while (count($top)\
        \ < $x && count($rest) > 0) {\n                $entry = array_pop($rest);\n\
        \                $insert($top, $entry);\n                $total += $entry[0]\
        \ * $entry[1];\n            }\n            while (count($top) > 0 && count($rest)\
        \ > 0 && $compare($top[0], $rest[count($rest) - 1]) < 0) {\n               \
        \ $low = array_shift($top);\n                $high = array_pop($rest);\n   \
        \             $total += $high[0] * $high[1] - $low[0] * $low[1];\n         \
        \       $insert($top, $high);\n                $insert($rest, $low);\n     \
        \       }\n        };\n\n        for ($i = 0; $i < $k; $i++) $change($nums[$i],\
        \ 1);\n        $answer = [$total];\n        for ($i = $k; $i < count($nums);\
        \ $i++) {\n            $change($nums[$i - $k], -1);\n            $change($nums[$i],\
        \ 1);\n            $answer[] = $total;\n        }\n        return $answer;\n\
        \    }\n}"
      swift: "class Solution {\n    func findXSum(_ nums: [Int], _ k: Int, _ x: Int)\
        \ -> [Int] {\n        var freq: [Int: Int] = [:]\n        var top: [(Int, Int)]\
        \ = []\n        var rest: [(Int, Int)] = []\n        var total = 0\n\n     \
        \   func compare(_ a: (Int, Int), _ b: (Int, Int)) -> Int {\n            if\
        \ a.0 != b.0 { return a.0 < b.0 ? -1 : 1 }\n            if a.1 != b.1 { return\
        \ a.1 < b.1 ? -1 : 1 }\n            return 0\n        }\n\n        func insert(_\
        \ set: inout [(Int, Int)], _ entry: (Int, Int)) {\n            var left = 0\n\
        \            var right = set.count\n            while left < right {\n     \
        \           let mid = (left + right) / 2\n                if compare(set[mid],\
        \ entry) < 0 { left = mid + 1 }\n                else { right = mid }\n    \
        \        }\n            set.insert(entry, at: left)\n        }\n\n        func\
        \ remove(_ set: inout [(Int, Int)], _ entry: (Int, Int)) {\n            var\
        \ left = 0\n            var right = set.count\n            while left < right\
        \ {\n                let mid = (left + right) / 2\n                if compare(set[mid],\
        \ entry) < 0 { left = mid + 1 }\n                else { right = mid }\n    \
        \        }\n            set.remove(at: left)\n        }\n\n        func change(_\
        \ value: Int, _ delta: Int) {\n            let old = freq[value] ?? 0\n    \
        \        if old > 0 {\n                let entry = (old, value)\n          \
        \      var left = 0\n                var right = top.count\n               \
        \ while left < right {\n                    let mid = (left + right) / 2\n \
        \                   if compare(top[mid], entry) < 0 { left = mid + 1 }\n   \
        \                 else { right = mid }\n                }\n                if\
        \ left < top.count && compare(top[left], entry) == 0 {\n                   \
        \ top.remove(at: left)\n                    total -= old * value\n         \
        \       } else {\n                    remove(&rest, entry)\n               \
        \ }\n            }\n\n            let next = old + delta\n            if next\
        \ > 0 {\n                freq[value] = next\n                let entry = (next,\
        \ value)\n                if top.count < x || compare(entry, top[0]) > 0 {\n\
        \                    insert(&top, entry)\n                    total += next\
        \ * value\n                } else {\n                    insert(&rest, entry)\n\
        \                }\n            } else {\n                freq.removeValue(forKey:\
        \ value)\n            }\n\n            while top.count > x {\n             \
        \   let entry = top.removeFirst()\n                total -= entry.0 * entry.1\n\
        \                insert(&rest, entry)\n            }\n            while top.count\
        \ < x && !rest.isEmpty {\n                let entry = rest.removeLast()\n  \
        \              insert(&top, entry)\n                total += entry.0 * entry.1\n\
        \            }\n            while !top.isEmpty && !rest.isEmpty && compare(top[0],\
        \ rest[rest.count - 1]) < 0 {\n                let low = top.removeFirst()\n\
        \                let high = rest.removeLast()\n                total += high.0\
        \ * high.1 - low.0 * low.1\n                insert(&top, high)\n           \
        \     insert(&rest, low)\n            }\n        }\n\n        for i in 0..<k\
        \ { change(nums[i], 1) }\n        var answer = [total]\n        if k < nums.count\
        \ {\n            for i in k..<nums.count {\n                change(nums[i -\
        \ k], -1)\n                change(nums[i], 1)\n                answer.append(total)\n\
        \            }\n        }\n        return answer\n    }\n}"
      kotlin: "class Solution {\n    fun findXSum(nums: IntArray, k: Int, x: Int): LongArray\
        \ {\n        val freq = HashMap<Int, Int>()\n        val top = java.util.TreeSet<Pair<Int,\
        \ Int>>(compareBy<Pair<Int, Int>> { it.first }.thenBy { it.second })\n     \
        \   val rest = java.util.TreeSet<Pair<Int, Int>>(compareBy<Pair<Int, Int>> {\
        \ it.first }.thenBy { it.second })\n        var total = 0L\n\n        fun change(value:\
        \ Int, delta: Int) {\n            val old = freq[value] ?: 0\n            if\
        \ (old > 0) {\n                val entry = Pair(old, value)\n              \
        \  if (top.remove(entry)) {\n                    total -= old.toLong() * value\n\
        \                } else {\n                    rest.remove(entry)\n        \
        \        }\n            }\n\n            val next = old + delta\n          \
        \  if (next > 0) {\n                freq[value] = next\n                val\
        \ entry = Pair(next, value)\n                if (top.size < x || entry > top.first())\
        \ {\n                    top.add(entry)\n                    total += next.toLong()\
        \ * value\n                } else {\n                    rest.add(entry)\n \
        \               }\n            } else {\n                freq.remove(value)\n\
        \            }\n\n            while (top.size > x) {\n                val entry\
        \ = top.pollFirst()\n                total -= entry.first.toLong() * entry.second\n\
        \                rest.add(entry)\n            }\n            while (top.size\
        \ < x && rest.isNotEmpty()) {\n                val entry = rest.pollLast()\n\
        \                top.add(entry)\n                total += entry.first.toLong()\
        \ * entry.second\n            }\n            while (top.isNotEmpty() && rest.isNotEmpty()\
        \ && top.first() < rest.last()) {\n                val low = top.pollFirst()\n\
        \                val high = rest.pollLast()\n                total += high.first.toLong()\
        \ * high.second - low.first.toLong() * low.second\n                top.add(high)\n\
        \                rest.add(low)\n            }\n        }\n\n        for (i in\
        \ 0 until k) change(nums[i], 1)\n        val answer = LongArray(nums.size -\
        \ k + 1)\n        answer[0] = total\n        for (i in k until nums.size) {\n\
        \            change(nums[i - k], -1)\n            change(nums[i], 1)\n     \
        \       answer[i - k + 1] = total\n        }\n        return answer\n    }\n\
        }"
      dart: "class Solution {\n  List<int> findXSum(List<int> nums, int k, int x) {\n\
        \    final freq = <int, int>{};\n    final top = SplayTreeSet<(int, int)>((a,\
        \ b) {\n      final byFreq = a.$1.compareTo(b.$1);\n      return byFreq != 0\
        \ ? byFreq : a.$2.compareTo(b.$2);\n    });\n    final rest = SplayTreeSet<(int,\
        \ int)>((a, b) {\n      final byFreq = a.$1.compareTo(b.$1);\n      return byFreq\
        \ != 0 ? byFreq : a.$2.compareTo(b.$2);\n    });\n    var total = 0;\n\n   \
        \ void change(int value, int delta) {\n      final old = freq[value] ?? 0;\n\
        \      if (old > 0) {\n        final entry = (old, value);\n        if (top.remove(entry))\
        \ {\n          total -= old * value;\n        } else {\n          rest.remove(entry);\n\
        \        }\n      }\n\n      final next = old + delta;\n      if (next > 0)\
        \ {\n        freq[value] = next;\n        final entry = (next, value);\n   \
        \     if (top.length < x || _compare(entry, top.first) > 0) {\n          top.add(entry);\n\
        \          total += next * value;\n        } else {\n          rest.add(entry);\n\
        \        }\n      } else {\n        freq.remove(value);\n      }\n\n      while\
        \ (top.length > x) {\n        final entry = top.first;\n        top.remove(entry);\n\
        \        total -= entry.$1 * entry.$2;\n        rest.add(entry);\n      }\n\
        \      while (top.length < x && rest.isNotEmpty) {\n        final entry = rest.last;\n\
        \        rest.remove(entry);\n        top.add(entry);\n        total += entry.$1\
        \ * entry.$2;\n      }\n      while (top.isNotEmpty && rest.isNotEmpty &&\n\
        \          _compare(top.first, rest.last) < 0) {\n        final low = top.first;\n\
        \        final high = rest.last;\n        top.remove(low);\n        rest.remove(high);\n\
        \        total += high.$1 * high.$2 - low.$1 * low.$2;\n        top.add(high);\n\
        \        rest.add(low);\n      }\n    }\n\n    for (var i = 0; i < k; i++) {\n\
        \      change(nums[i], 1);\n    }\n    final answer = <int>[total];\n    for\
        \ (var i = k; i < nums.length; i++) {\n      change(nums[i - k], -1);\n    \
        \  change(nums[i], 1);\n      answer.add(total);\n    }\n    return answer;\n\
        \  }\n\n  int _compare((int, int) a, (int, int) b) {\n    final byFreq = a.$1.compareTo(b.$1);\n\
        \    return byFreq != 0 ? byFreq : a.$2.compareTo(b.$2);\n  }\n}"
      go: "func findXSum(nums []int, k int, x int) []int64 {\n\tfreq := make(map[int]int)\n\
        \ttop := &OrderedSet{}\n\trest := &OrderedSet{}\n\tvar total int64\n\n\tchange\
        \ := func(value, delta int) {}\n\tchange = func(value, delta int) {\n\t\told\
        \ := freq[value]\n\t\tif old > 0 {\n\t\t\tentry := Pair{freq: old, value: value}\n\
        \t\t\tif top.Remove(entry) {\n\t\t\t\ttotal -= int64(old) * int64(value)\n\t\
        \t\t} else {\n\t\t\t\trest.Remove(entry)\n\t\t\t}\n\t\t}\n\n\t\tnext := old\
        \ + delta\n\t\tif next > 0 {\n\t\t\tfreq[value] = next\n\t\t\tentry := Pair{freq:\
        \ next, value: value}\n\t\t\tif top.Len() < x || comparePair(entry, top.Min())\
        \ > 0 {\n\t\t\t\ttop.Add(entry)\n\t\t\t\ttotal += int64(next) * int64(value)\n\
        \t\t\t} else {\n\t\t\t\trest.Add(entry)\n\t\t\t}\n\t\t} else {\n\t\t\tdelete(freq,\
        \ value)\n\t\t}\n\n\t\tfor top.Len() > x {\n\t\t\tentry := top.PopMin()\n\t\t\
        \ttotal -= int64(entry.freq) * int64(entry.value)\n\t\t\trest.Add(entry)\n\t\
        \t}\n\t\tfor top.Len() < x && rest.Len() > 0 {\n\t\t\tentry := rest.PopMax()\n\
        \t\t\ttop.Add(entry)\n\t\t\ttotal += int64(entry.freq) * int64(entry.value)\n\
        \t\t}\n\t\tfor top.Len() > 0 && rest.Len() > 0 && comparePair(top.Min(), rest.Max())\
        \ < 0 {\n\t\t\tlow := top.PopMin()\n\t\t\thigh := rest.PopMax()\n\t\t\ttotal\
        \ += int64(high.freq)*int64(high.value) - int64(low.freq)*int64(low.value)\n\
        \t\t\ttop.Add(high)\n\t\t\trest.Add(low)\n\t\t}\n\t}\n\n\tfor i := 0; i < k;\
        \ i++ {\n\t\tchange(nums[i], 1)\n\t}\n\tanswer := make([]int64, 0, len(nums)-k+1)\n\
        \tanswer = append(answer, total)\n\tfor i := k; i < len(nums); i++ {\n\t\tchange(nums[i-k],\
        \ -1)\n\t\tchange(nums[i], 1)\n\t\tanswer = append(answer, total)\n\t}\n\treturn\
        \ answer\n}\n\ntype Pair struct {\n\tfreq  int\n\tvalue int\n}\n\ntype Node\
        \ struct {\n\tkey         Pair\n\tpriority    uint32\n\tleft, right *Node\n\
        }\n\ntype OrderedSet struct {\n\troot *Node\n\tsize int\n}\n\nfunc comparePair(a,\
        \ b Pair) int {\n\tif a.freq < b.freq {\n\t\treturn -1\n\t}\n\tif a.freq > b.freq\
        \ {\n\t\treturn 1\n\t}\n\tif a.value < b.value {\n\t\treturn -1\n\t}\n\tif a.value\
        \ > b.value {\n\t\treturn 1\n\t}\n\treturn 0\n}\n\nfunc pairPriority(p Pair)\
        \ uint32 {\n\tx := uint64(uint32(p.freq))*0x9e3779b97f4a7c15 + uint64(uint32(p.value))\n\
        \tx ^= x >> 30\n\tx *= 0xbf58476d1ce4e5b9\n\tx ^= x >> 27\n\tx *= 0x94d049bb133111eb\n\
        \tx ^= x >> 31\n\treturn uint32(x)\n}\n\nfunc rotateRight(n *Node) *Node {\n\
        \tleft := n.left\n\tn.left = left.right\n\tleft.right = n\n\treturn left\n}\n\
        \nfunc rotateLeft(n *Node) *Node {\n\tright := n.right\n\tn.right = right.left\n\
        \tright.left = n\n\treturn right\n}\n\nfunc insertNode(n *Node, key Pair) *Node\
        \ {\n\tif n == nil {\n\t\treturn &Node{key: key, priority: pairPriority(key)}\n\
        \t}\n\tif comparePair(key, n.key) < 0 {\n\t\tn.left = insertNode(n.left, key)\n\
        \t\tif n.left.priority < n.priority {\n\t\t\tn = rotateRight(n)\n\t\t}\n\t}\
        \ else if comparePair(key, n.key) > 0 {\n\t\tn.right = insertNode(n.right, key)\n\
        \t\tif n.right.priority < n.priority {\n\t\t\tn = rotateLeft(n)\n\t\t}\n\t}\n\
        \treturn n\n}\n\nfunc deleteNode(n *Node, key Pair) *Node {\n\tif n == nil {\n\
        \t\treturn nil\n\t}\n\tcmp := comparePair(key, n.key)\n\tif cmp < 0 {\n\t\t\
        n.left = deleteNode(n.left, key)\n\t} else if cmp > 0 {\n\t\tn.right = deleteNode(n.right,\
        \ key)\n\t} else {\n\t\tif n.left == nil {\n\t\t\treturn n.right\n\t\t}\n\t\t\
        if n.right == nil {\n\t\t\treturn n.left\n\t\t}\n\t\tif n.left.priority < n.right.priority\
        \ {\n\t\t\tn = rotateRight(n)\n\t\t\tn.right = deleteNode(n.right, key)\n\t\t\
        } else {\n\t\t\tn = rotateLeft(n)\n\t\t\tn.left = deleteNode(n.left, key)\n\t\
        \t}\n\t}\n\treturn n\n}\n\nfunc (s *OrderedSet) Add(key Pair) {\n\tbefore :=\
        \ s.Len()\n\ts.root = insertNode(s.root, key)\n\tif s.Len() == before {\n\t\t\
        return\n\t}\n\ts.size++\n}\n\nfunc (s *OrderedSet) Remove(key Pair) bool {\n\
        \tif !s.Contains(key) {\n\t\treturn false\n\t}\n\ts.root = deleteNode(s.root,\
        \ key)\n\ts.size--\n\treturn true\n}\n\nfunc (s *OrderedSet) Contains(key Pair)\
        \ bool {\n\tn := s.root\n\tfor n != nil {\n\t\tcmp := comparePair(key, n.key)\n\
        \t\tif cmp == 0 {\n\t\t\treturn true\n\t\t}\n\t\tif cmp < 0 {\n\t\t\tn = n.left\n\
        \t\t} else {\n\t\t\tn = n.right\n\t\t}\n\t}\n\treturn false\n}\n\nfunc (s *OrderedSet)\
        \ Len() int {\n\treturn s.size\n}\n\nfunc (s *OrderedSet) Min() Pair {\n\tn\
        \ := s.root\n\tfor n.left != nil {\n\t\tn = n.left\n\t}\n\treturn n.key\n}\n\
        \nfunc (s *OrderedSet) Max() Pair {\n\tn := s.root\n\tfor n.right != nil {\n\
        \t\tn = n.right\n\t}\n\treturn n.key\n}\n\nfunc (s *OrderedSet) PopMin() Pair\
        \ {\n\tkey := s.Min()\n\ts.root = deleteNode(s.root, key)\n\ts.size--\n\treturn\
        \ key\n}\n\nfunc (s *OrderedSet) PopMax() Pair {\n\tkey := s.Max()\n\ts.root\
        \ = deleteNode(s.root, key)\n\ts.size--\n\treturn key\n}"
      ruby: "# @param {Integer[]} nums\n# @param {Integer} k\n# @param {Integer} x\n\
        # @return {Integer[]}\ndef find_x_sum(nums, k, x)\n  freq = Hash.new(0)\n  top\
        \ = SortedSet.new\n  rest = SortedSet.new\n  total = 0\n\n  change = lambda\
        \ do |value, delta|\n    old = freq[value]\n    if old > 0\n      entry = [old,\
        \ value]\n      if top.delete?(entry)\n        total -= old * value\n      else\n\
        \        rest.delete(entry)\n      end\n    end\n\n    current = old + delta\n\
        \    if current > 0\n      freq[value] = current\n      entry = [current, value]\n\
        \      if top.size < x || (entry <=> top.first) > 0\n        top.add(entry)\n\
        \        total += current * value\n      else\n        rest.add(entry)\n   \
        \   end\n    else\n      freq.delete(value)\n    end\n\n    while top.size >\
        \ x\n      entry = top.first\n      top.delete(entry)\n      total -= entry[0]\
        \ * entry[1]\n      rest.add(entry)\n    end\n    while top.size < x && !rest.empty?\n\
        \      entry = rest.last\n      rest.delete(entry)\n      top.add(entry)\n \
        \     total += entry[0] * entry[1]\n    end\n    while !top.empty? && !rest.empty?\
        \ && (top.first <=> rest.last) < 0\n      low = top.first\n      high = rest.last\n\
        \      top.delete(low)\n      rest.delete(high)\n      total += high[0] * high[1]\
        \ - low[0] * low[1]\n      top.add(high)\n      rest.add(low)\n    end\n  end\n\
        \n  nums[0, k].each { |value| change.call(value, 1) }\n  answer = [total]\n\
        \  (k...nums.length).each do |i|\n    change.call(nums[i - k], -1)\n    change.call(nums[i],\
        \ 1)\n    answer << total\n  end\n  answer\nend"
      scala: "import scala.collection.mutable\n\nobject Solution {\n    def findXSum(nums:\
        \ Array[Int], k: Int, x: Int): Array[Long] = {\n        val freq = mutable.HashMap.empty[Int,\
        \ Int]\n        val ordering = Ordering[(Int, Int)]\n        val top = mutable.TreeSet.empty[(Int,\
        \ Int)](ordering)\n        val rest = mutable.TreeSet.empty[(Int, Int)](ordering)\n\
        \        var total = 0L\n\n        def change(value: Int, delta: Int): Unit\
        \ = {\n            val old = freq.getOrElse(value, 0)\n            if (old >\
        \ 0) {\n                val entry = (old, value)\n                if (top.remove(entry))\
        \ {\n                    total -= old.toLong * value\n                } else\
        \ {\n                    rest.remove(entry)\n                }\n           \
        \ }\n\n            val next = old + delta\n            if (next > 0) {\n   \
        \             freq(value) = next\n                val entry = (next, value)\n\
        \                if (top.size < x || ordering.gt(entry, top.head)) {\n     \
        \               top.add(entry)\n                    total += next.toLong * value\n\
        \                } else {\n                    rest.add(entry)\n           \
        \     }\n            } else {\n                freq.remove(value)\n        \
        \    }\n\n            while (top.size > x) {\n                val entry = top.head\n\
        \                top.remove(entry)\n                total -= entry._1.toLong\
        \ * entry._2\n                rest.add(entry)\n            }\n            while\
        \ (top.size < x && rest.nonEmpty) {\n                val entry = rest.last\n\
        \                rest.remove(entry)\n                top.add(entry)\n      \
        \          total += entry._1.toLong * entry._2\n            }\n            while\
        \ (top.nonEmpty && rest.nonEmpty && ordering.lt(top.head, rest.last)) {\n  \
        \              val low = top.head\n                val high = rest.last\n  \
        \              top.remove(low)\n                rest.remove(high)\n        \
        \        total += high._1.toLong * high._2 - low._1.toLong * low._2\n      \
        \          top.add(high)\n                rest.add(low)\n            }\n   \
        \     }\n\n        var i = 0\n        while (i < k) {\n            change(nums(i),\
        \ 1)\n            i += 1\n        }\n        val answer = new Array[Long](nums.length\
        \ - k + 1)\n        answer(0) = total\n        i = k\n        var index = 1\n\
        \        while (i < nums.length) {\n            change(nums(i - k), -1)\n  \
        \          change(nums(i), 1)\n            answer(index) = total\n         \
        \   i += 1\n            index += 1\n        }\n        answer\n    }\n}"
      rust: "impl Solution {\n    pub fn find_x_sum(nums: Vec<i32>, k: i32, x: i32)\
        \ -> Vec<i64> {\n        use std::collections::BTreeSet;\n\n        let k =\
        \ k as usize;\n        let x = x as usize;\n        let mut freq = std::collections::HashMap::<i32,\
        \ i32>::new();\n        let mut top = BTreeSet::<(i32, i32)>::new();\n     \
        \   let mut rest = BTreeSet::<(i32, i32)>::new();\n        let mut total = 0i64;\n\
        \n        let change = |value: i32,\n                      delta: i32,\n   \
        \                   freq: &mut std::collections::HashMap<i32, i32>,\n      \
        \                top: &mut BTreeSet<(i32, i32)>,\n                      rest:\
        \ &mut BTreeSet<(i32, i32)>,\n                      total: &mut i64| {\n   \
        \         let old = *freq.get(&value).unwrap_or(&0);\n            if old > 0\
        \ {\n                let entry = (old, value);\n                if top.remove(&entry)\
        \ {\n                    *total -= old as i64 * value as i64;\n            \
        \    } else {\n                    rest.remove(&entry);\n                }\n\
        \            }\n            let new = old + delta;\n            if new > 0 {\n\
        \                freq.insert(value, new);\n                let entry = (new,\
        \ value);\n                if top.len() < x || top.first().map_or(false, |smallest|\
        \ entry > *smallest) {\n                    top.insert(entry);\n           \
        \         *total += new as i64 * value as i64;\n                } else {\n \
        \                   rest.insert(entry);\n                }\n            } else\
        \ {\n                freq.remove(&value);\n            }\n            while\
        \ top.len() > x {\n                let entry = *top.first().unwrap();\n    \
        \            top.remove(&entry);\n                *total -= entry.0 as i64 *\
        \ entry.1 as i64;\n                rest.insert(entry);\n            }\n    \
        \        while top.len() < x && !rest.is_empty() {\n                let entry\
        \ = *rest.last().unwrap();\n                rest.remove(&entry);\n         \
        \       top.insert(entry);\n                *total += entry.0 as i64 * entry.1\
        \ as i64;\n            }\n            while !top.is_empty() && !rest.is_empty()\
        \ && top.first().unwrap() < rest.last().unwrap() {\n                let low\
        \ = *top.first().unwrap();\n                let high = *rest.last().unwrap();\n\
        \                top.remove(&low);\n                rest.remove(&high);\n  \
        \              *total += (high.0 as i64 * high.1 as i64) - (low.0 as i64 * low.1\
        \ as i64);\n                top.insert(high);\n                rest.insert(low);\n\
        \            }\n        };\n\n        for &value in nums.iter().take(k) {\n\
        \            change(value, 1, &mut freq, &mut top, &mut rest, &mut total);\n\
        \        }\n        let mut answer = vec![total];\n        for i in k..nums.len()\
        \ {\n            change(nums[i - k], -1, &mut freq, &mut top, &mut rest, &mut\
        \ total);\n            change(nums[i], 1, &mut freq, &mut top, &mut rest, &mut\
        \ total);\n            answer.push(total);\n        }\n        answer\n    }\n\
        }"
      racket: "(define/contract (find-x-sum nums k x)\n  (-> (listof exact-integer?)\
        \ exact-integer? exact-integer? (listof exact-integer?))\n  (let* ([arr (list->vector\
        \ nums)]\n         [n (vector-length arr)]\n         [freq (make-hash)]\n  \
        \       [top (make-hash)]\n         [rest (make-hash)]\n         [total (box\
        \ 0)])\n    (define (best-entry table)\n      (for/fold ([best #f]) ([(value\
        \ count) (in-hash table)])\n        (if (or (not best)\n                (> count\
        \ (cdr best))\n                (and (= count (cdr best)) (> value (car best))))\n\
        \            (cons value count)\n            best)))\n    (define (worst-entry\
        \ table)\n      (for/fold ([worst #f]) ([(value count) (in-hash table)])\n \
        \       (if (or (not worst)\n                (< count (cdr worst))\n       \
        \         (and (= count (cdr worst)) (< value (car worst))))\n            (cons\
        \ value count)\n            worst)))\n    (define (change value delta)\n   \
        \   (define old (hash-ref freq value 0))\n      (when (> old 0)\n        (if\
        \ (hash-has-key? top value)\n            (begin\n              (hash-remove!\
        \ top value)\n              (set-box! total (- (unbox total) (* old value))))\n\
        \            (hash-remove! rest value)))\n      (define new (+ old delta))\n\
        \      (if (> new 0)\n          (begin\n            (hash-set! freq value new)\n\
        \            (define worst-top (worst-entry top))\n            (if (or (< (hash-count\
        \ top) x)\n                    (and worst-top\n                         (or\
        \ (> new (cdr worst-top))\n                             (and (= new (cdr worst-top))\
        \ (> value (car worst-top)))))\n                    (not worst-top))\n     \
        \           (begin\n                  (hash-set! top value new)\n          \
        \        (set-box! total (+ (unbox total) (* new value))))\n               \
        \ (hash-set! rest value new)))\n          (hash-remove! freq value))\n     \
        \ (let loop ()\n        (when (> (hash-count top) x)\n          (define low\
        \ (worst-entry top))\n          (hash-remove! top (car low))\n          (hash-set!\
        \ rest (car low) (cdr low))\n          (set-box! total (- (unbox total) (* (car\
        \ low) (cdr low))))\n          (loop)))\n      (let loop ()\n        (when (and\
        \ (< (hash-count top) x) (> (hash-count rest) 0))\n          (define high (best-entry\
        \ rest))\n          (hash-remove! rest (car high))\n          (hash-set! top\
        \ (car high) (cdr high))\n          (set-box! total (+ (unbox total) (* (car\
        \ high) (cdr high))))\n          (loop)))\n      (let loop ()\n        (define\
        \ low (worst-entry top))\n        (define high (best-entry rest))\n        (when\
        \ (and low high\n                   (or (> (cdr high) (cdr low))\n         \
        \              (and (= (cdr high) (cdr low)) (> (car high) (car low)))))\n \
        \         (hash-remove! top (car low))\n          (hash-remove! rest (car high))\n\
        \          (hash-set! top (car high) (cdr high))\n          (hash-set! rest\
        \ (car low) (cdr low))\n          (set-box! total (+ (unbox total)\n       \
        \                      (* (car high) (cdr high))\n                         \
        \    (- (* (car low) (cdr low)))))\n          (loop))))\n    (for ([i (in-range\
        \ k)])\n      (change (vector-ref arr i) 1))\n    (define answer (make-vector\
        \ (+ 1 (- n k))))\n    (vector-set! answer 0 (unbox total))\n    (for ([i (in-range\
        \ k n)])\n      (change (vector-ref arr (- i k)) -1)\n      (change (vector-ref\
        \ arr i) 1)\n      (vector-set! answer (- i k -1) (unbox total)))\n    (vector->list\
        \ answer)))"
      erlang: "-spec find_x_sum(Nums :: [integer()], K :: integer(), X :: integer())\
        \ -> [integer()].\nfind_x_sum(Nums, K, X) ->\n  Arr = list_to_tuple(Nums),\n\
        \  N = tuple_size(Arr),\n  State0 = {#{}, gb_sets:empty(), gb_sets:empty(),\
        \ 0},\n  State1 = lists:foldl(fun(I, S) -> change(element(I, Arr), 1, X, S)\
        \ end,\n                       State0, lists:seq(1, K)),\n  {_, _, _, InitialTotal}\
        \ = State1,\n  Answer0 = [InitialTotal],\n  {Answer, _} = lists:foldl(\n   \
        \ fun(I, {Acc, State}) ->\n      StateA = change(element(I - K, Arr), -1, X,\
        \ State),\n      StateB = change(element(I, Arr), 1, X, StateA),\n      { {element(1,\
        \ StateB), element(2, StateB), element(3, StateB), Total}, _, _, _} = {StateB,\
        \ 0, 0, 0},\n      { [Total | Acc], StateB }\n    end,\n    {Answer0, State1},\n\
        \    lists:seq(K + 1, N)),\n  lists:reverse(Answer).\n\nchange(Value, Delta,\
        \ X, {Freq, Top, Rest, Total}) ->\n  Old = maps:get(Value, Freq, 0),\n  {Top1,\
        \ Rest1, Total1} = case Old of\n    0 -> {Top, Rest, Total};\n    _ ->\n   \
        \   Entry = {Old, Value},\n      case gb_sets:is_member(Entry, Top) of\n   \
        \     true -> {gb_sets:delete(Entry, Top), Rest, Total - Old * Value};\n   \
        \     false -> {Top, gb_sets:delete(Entry, Rest), Total}\n      end\n  end,\n\
        \  New = Old + Delta,\n  Freq1 = if New > 0 -> maps:put(Value, New, Freq); true\
        \ -> maps:remove(Value, Freq) end,\n  {Top2, Rest2, Total2} = case New > 0 of\n\
        \    false -> {Top1, Rest1, Total1};\n    true ->\n      Entry2 = {New, Value},\n\
        \      case gb_sets:size(Top1) < X orelse (gb_sets:size(Top1) > 0 andalso Entry2\
        \ > gb_sets:smallest(Top1)) of\n        true -> {gb_sets:add(Entry2, Top1),\
        \ Rest1, Total1 + New * Value};\n        false -> {Top1, gb_sets:add(Entry2,\
        \ Rest1), Total1}\n      end\n  end,\n  rebalance(Freq1, Top2, Rest2, Total2,\
        \ X).\n\nrebalance(Freq, Top, Rest, Total, X) when gb_sets:size(Top) > X ->\n\
        \  Entry = gb_sets:smallest(Top),\n  rebalance(Freq, gb_sets:delete(Entry, Top),\
        \ gb_sets:add(Entry, Rest),\n            Total - element(1, Entry) * element(2,\
        \ Entry), X);\nrebalance(Freq, Top, Rest, Total, X) when gb_sets:size(Top) <\
        \ X, gb_sets:size(Rest) > 0 ->\n  Entry = gb_sets:largest(Rest),\n  rebalance(Freq,\
        \ gb_sets:add(Entry, Top), gb_sets:delete(Entry, Rest),\n            Total +\
        \ element(1, Entry) * element(2, Entry), X);\nrebalance(Freq, Top, Rest, Total,\
        \ X) when gb_sets:size(Top) > 0, gb_sets:size(Rest) > 0 ->\n  Low = gb_sets:smallest(Top),\n\
        \  High = gb_sets:largest(Rest),\n  case Low < High of\n    true ->\n      NewTotal\
        \ = Total + element(1, High) * element(2, High) - element(1, Low) * element(2,\
        \ Low),\n      rebalance(Freq, gb_sets:add(Low, gb_sets:delete(Low, Top)),\n\
        \                gb_sets:add(High, gb_sets:delete(High, Rest)), NewTotal, X);\n\
        \    false -> {Freq, Top, Rest, Total}\n  end;\nrebalance(Freq, Top, Rest, Total,\
        \ _) -> {Freq, Top, Rest, Total}."
      elixir: "defmodule Solution do\n  @spec find_x_sum(nums :: [integer], k :: integer,\
        \ x :: integer) :: [integer]\n  def find_x_sum(nums, k, x) do\n    arr = List.to_tuple(nums)\n\
        \    n = tuple_size(arr)\n    state = { %{}, %{}, %{}, 0 }\n    state = Enum.reduce(0..(k\
        \ - 1), state, fn i, s -> change(elem(arr, i), 1, x, s) end)\n    {_, _, _,\
        \ initial_total} = state\n    {answers, _state} =\n      Enum.reduce(k..(n -\
        \ 1), {[initial_total], state}, fn i, {acc, s} ->\n        s = change(elem(arr,\
        \ i - k), -1, x, s)\n        s = change(elem(arr, i), 1, x, s)\n        {_,\
        \ _, _, total} = s\n        {[total | acc], s}\n      end)\n    Enum.reverse(answers)\n\
        \  end\n\n  defp change(value, delta, x, {freq, top, rest, total}) do\n    old\
        \ = Map.get(freq, value, 0)\n    {top, rest, total} =\n      if old > 0 do\n\
        \        if Map.has_key?(top, value) do\n          {Map.delete(top, value),\
        \ rest, total - old * value}\n        else\n          {top, Map.delete(rest,\
        \ value), total}\n        end\n      else\n        {top, rest, total}\n    \
        \  end\n\n    new = old + delta\n    freq = if new > 0, do: Map.put(freq, value,\
        \ new), else: Map.delete(freq, value)\n\n    {top, rest, total} =\n      if\
        \ new > 0 do\n        entry = {new, value}\n        worst = worst_entry(top)\n\
        \        if map_size(top) < x or is_nil(worst) or entry > worst do\n       \
        \   {Map.put(top, value, new), rest, total + new * value}\n        else\n  \
        \        {top, Map.put(rest, value, new), total}\n        end\n      else\n\
        \        {top, rest, total}\n      end\n\n    rebalance(freq, top, rest, total,\
        \ x)\n  end\n\n  defp worst_entry(map) do\n    Enum.reduce(map, nil, fn {value,\
        \ count}, best ->\n      entry = {count, value}\n      if is_nil(best) or entry\
        \ < best, do: entry, else: best\n    end)\n  end\n\n  defp best_entry(map) do\n\
        \    Enum.reduce(map, nil, fn {value, count}, best ->\n      entry = {count,\
        \ value}\n      if is_nil(best) or entry > best, do: entry, else: best\n   \
        \ end)\n  end\n\n  defp rebalance(freq, top, rest, total, x) when map_size(top)\
        \ > x do\n    {count, value} = worst_entry(top)\n    rebalance(freq, Map.delete(top,\
        \ value), Map.put(rest, value, count), total - count * value, x)\n  end\n\n\
        \  defp rebalance(freq, top, rest, total, x) when map_size(top) < x and map_size(rest)\
        \ > 0 do\n    {count, value} = best_entry(rest)\n    rebalance(freq, Map.put(top,\
        \ value, count), Map.delete(rest, value), total + count * value, x)\n  end\n\
        \n  defp rebalance(freq, top, rest, total, x) when map_size(top) > 0 and map_size(rest)\
        \ > 0 do\n    {low_count, low_value} = worst_entry(top)\n    {high_count, high_value}\
        \ = best_entry(rest)\n    if {high_count, high_value} > {low_count, low_value}\
        \ do\n      top = top |> Map.delete(low_value) |> Map.put(high_value, high_count)\n\
        \      rest = rest |> Map.delete(high_value) |> Map.put(low_value, low_count)\n\
        \      rebalance(freq, top, rest,\n        total + high_count * high_value -\
        \ low_count * low_value, x)\n    else\n      {freq, top, rest, total}\n    end\n\
        \  end\n\n  defp rebalance(freq, top, rest, total, _x), do: {freq, top, rest,\
        \ total}\nend"
      c: "#include <stdlib.h>\n\ntypedef struct {\n    int value;\n    int frequency;\n\
        \    int inTop;\n    int active;\n} Entry;\n\ntypedef struct {\n    int value;\n\
        \    int frequency;\n} Node;\n\ntypedef struct {\n    Node *data;\n    int size;\n\
        \    int capacity;\n    int isMin;\n} Heap;\n\nstatic int better(Node a, Node\
        \ b) {\n    return a.frequency > b.frequency || (a.frequency == b.frequency\
        \ && a.value > b.value);\n}\n\nstatic int worse(Node a, Node b) {\n    return\
        \ a.frequency < b.frequency || (a.frequency == b.frequency && a.value < b.value);\n\
        }\n\nstatic int precedes(Heap *heap, Node a, Node b) {\n    return heap->isMin\
        \ ? worse(a, b) : better(a, b);\n}\n\nstatic void heapPush(Heap *heap, Node\
        \ node) {\n    if (heap->size == heap->capacity) {\n        heap->capacity =\
        \ heap->capacity ? heap->capacity * 2 : 16;\n        heap->data = (Node *)realloc(heap->data,\
        \ sizeof(Node) * heap->capacity);\n    }\n    int i = heap->size++;\n    while\
        \ (i > 0) {\n        int p = (i - 1) / 2;\n        if (!precedes(heap, node,\
        \ heap->data[p])) break;\n        heap->data[i] = heap->data[p];\n        i\
        \ = p;\n    }\n    heap->data[i] = node;\n}\n\nstatic Node heapPop(Heap *heap)\
        \ {\n    Node result = heap->data[0];\n    Node last = heap->data[--heap->size];\n\
        \    if (heap->size > 0) {\n        int i = 0;\n        while (i * 2 + 1 < heap->size)\
        \ {\n            int child = i * 2 + 1;\n            if (child + 1 < heap->size\
        \ && precedes(heap, heap->data[child + 1], heap->data[child])) child++;\n  \
        \          if (!precedes(heap, heap->data[child], last)) break;\n          \
        \  heap->data[i] = heap->data[child];\n            i = child;\n        }\n \
        \       heap->data[i] = last;\n    }\n    return result;\n}\n\nstatic int findIndex(Entry\
        \ *entries, int count, int value) {\n    int lo = 0, hi = count - 1;\n    while\
        \ (lo <= hi) {\n        int mid = lo + (hi - lo) / 2;\n        if (entries[mid].value\
        \ == value) return mid;\n        if (entries[mid].value < value) lo = mid +\
        \ 1;\n        else hi = mid - 1;\n    }\n    return lo;\n}\n\nstatic int findExisting(Entry\
        \ *entries, int count, int value) {\n    int lo = 0, hi = count - 1;\n    while\
        \ (lo <= hi) {\n        int mid = lo + (hi - lo) / 2;\n        if (entries[mid].value\
        \ == value) return mid;\n        if (entries[mid].value < value) lo = mid +\
        \ 1;\n        else hi = mid - 1;\n    }\n    return -1;\n}\n\nlong long* findXSum(int*\
        \ nums, int numsSize, int k, int x, int* returnSize) {\n    int *sorted = (int\
        \ *)malloc(sizeof(int) * numsSize);\n    for (int i = 0; i < numsSize; i++)\
        \ sorted[i] = nums[i];\n    for (int i = 1; i < numsSize; i++) {\n        int\
        \ v = sorted[i], j = i - 1;\n        while (j >= 0 && sorted[j] > v) { sorted[j\
        \ + 1] = sorted[j]; j--; }\n        sorted[j + 1] = v;\n    }\n    Entry *entries\
        \ = (Entry *)calloc(numsSize, sizeof(Entry));\n    int count = 0;\n    for (int\
        \ i = 0; i < numsSize; i++) {\n        if (i == 0 || sorted[i] != sorted[i -\
        \ 1]) entries[count++].value = sorted[i];\n    }\n    free(sorted);\n\n    Heap\
        \ topMin = {0}, restMax = {0};\n    topMin.isMin = 1;\n    restMax.isMin = 0;\n\
        \    long long total = 0;\n    long long *answer = (long long *)malloc(sizeof(long\
        \ long) * (numsSize - k + 1));\n    int answerCount = 0;\n\n    for (int step\
        \ = 0; step < numsSize; step++) {\n        int value = nums[step];\n       \
        \ int index = findExisting(entries, count, value);\n        int old = entries[index].frequency;\n\
        \        if (old > 0) {\n            if (entries[index].inTop) total -= (long\
        \ long)old * value;\n            entries[index].frequency = 0;\n           \
        \ entries[index].active = 0;\n        }\n        entries[index].frequency =\
        \ old + 1;\n        entries[index].active = 1;\n        Node node = {value,\
        \ old + 1};\n        if (old > 0 && entries[index].inTop) {\n            entries[index].inTop\
        \ = 0;\n        }\n        heapPush(&restMax, node);\n\n        if (step >=\
        \ k) {\n            int out = nums[step - k];\n            int oi = findExisting(entries,\
        \ count, out);\n            int oldOut = entries[oi].frequency;\n          \
        \  if (entries[oi].inTop) total -= (long long)oldOut * out;\n            entries[oi].frequency\
        \ = oldOut - 1;\n            entries[oi].active = oldOut > 1;\n            if\
        \ (oldOut == 1) entries[oi].inTop = 0;\n            else heapPush(entries[oi].inTop\
        \ ? &topMin : &restMax, (Node){out, oldOut - 1});\n        }\n\n        int\
        \ windowStart = step >= k - 1 ? step - k + 1 : 0;\n        int windowLength\
        \ = step + 1 - windowStart;\n        int target = windowLength < x ? windowLength\
        \ : x;\n        while (topMin.size > 0) {\n            Node n = topMin.data[0];\n\
        \            int idx = findExisting(entries, count, n.value);\n            if\
        \ (!entries[idx].active || !entries[idx].inTop || entries[idx].frequency !=\
        \ n.frequency) heapPop(&topMin);\n            else break;\n        }\n     \
        \   while (restMax.size > 0) {\n            Node n = restMax.data[0];\n    \
        \        int idx = findExisting(entries, count, n.value);\n            if (!entries[idx].active\
        \ || entries[idx].inTop || entries[idx].frequency != n.frequency) heapPop(&restMax);\n\
        \            else break;\n        }\n        while (topMin.size < target &&\
        \ restMax.size > 0) {\n            Node n = heapPop(&restMax);\n           \
        \ int idx = findExisting(entries, count, n.value);\n            if (!entries[idx].active\
        \ || entries[idx].inTop || entries[idx].frequency != n.frequency) continue;\n\
        \            entries[idx].inTop = 1;\n            total += (long long)n.frequency\
        \ * n.value;\n            heapPush(&topMin, n);\n        }\n        while (topMin.size\
        \ > target) {\n            Node n = heapPop(&topMin);\n            int idx =\
        \ findExisting(entries, count, n.value);\n            if (!entries[idx].active\
        \ || !entries[idx].inTop || entries[idx].frequency != n.frequency) continue;\n\
        \            entries[idx].inTop = 0;\n            total -= (long long)n.frequency\
        \ * n.value;\n            heapPush(&restMax, n);\n        }\n        while (topMin.size\
        \ > 0 && restMax.size > 0) {\n            Node low = topMin.data[0], high =\
        \ restMax.data[0];\n            int li = findExisting(entries, count, low.value),\
        \ hi = findExisting(entries, count, high.value);\n            if (!entries[li].active\
        \ || !entries[li].inTop || entries[li].frequency != low.frequency) { heapPop(&topMin);\
        \ continue; }\n            if (!entries[hi].active || entries[hi].inTop || entries[hi].frequency\
        \ != high.frequency) { heapPop(&restMax); continue; }\n            if (!better(high,\
        \ low)) break;\n            heapPop(&topMin);\n            heapPop(&restMax);\n\
        \            entries[li].inTop = 0;\n            entries[hi].inTop = 1;\n  \
        \          total += (long long)high.frequency * high.value - (long long)low.frequency\
        \ * low.value;\n            heapPush(&restMax, low);\n            heapPush(&topMin,\
        \ high);\n        }\n        if (step >= k - 1) answer[answerCount++] = total;\n\
        \    }\n    free(entries);\n    free(topMin.data);\n    free(restMax.data);\n\
        \    *returnSize = answerCount;\n    return answer;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\n\npublic class Solution\
        \ {\n    public long[] FindXSum(int[] nums, int k, int x) {\n        var freq\
        \ = new Dictionary<int, int>();\n        var top = new SortedSet<(int frequency,\
        \ int value)>();\n        var rest = new SortedSet<(int frequency, int value)>();\n\
        \        long total = 0;\n\n        void Change(int value, int delta) {\n  \
        \          int old = freq.TryGetValue(value, out int current) ? current : 0;\n\
        \            if (old > 0) {\n                var entry = (old, value);\n   \
        \             if (top.Remove(entry)) total -= (long)old * value;\n         \
        \       else rest.Remove(entry);\n            }\n            int next = old\
        \ + delta;\n            if (next > 0) {\n                freq[value] = next;\n\
        \                var entry = (next, value);\n                if (top.Count <\
        \ x || entry.CompareTo(top.Min) > 0) {\n                    top.Add(entry);\n\
        \                    total += (long)next * value;\n                } else {\n\
        \                    rest.Add(entry);\n                }\n            } else\
        \ {\n                freq.Remove(value);\n            }\n            while (top.Count\
        \ > x) {\n                var entry = top.Min;\n                top.Remove(entry);\n\
        \                total -= (long)entry.frequency * entry.value;\n           \
        \     rest.Add(entry);\n            }\n            while (top.Count < x && rest.Count\
        \ > 0) {\n                var entry = rest.Max;\n                rest.Remove(entry);\n\
        \                top.Add(entry);\n                total += (long)entry.frequency\
        \ * entry.value;\n            }\n            while (top.Count > 0 && rest.Count\
        \ > 0 && top.Min.CompareTo(rest.Max) < 0) {\n                var low = top.Min;\n\
        \                var high = rest.Max;\n                top.Remove(low);\n  \
        \              rest.Remove(high);\n                total += (long)high.frequency\
        \ * high.value - (long)low.frequency * low.value;\n                top.Add(high);\n\
        \                rest.Add(low);\n            }\n        }\n\n        for (int\
        \ i = 0; i < k; i++) Change(nums[i], 1);\n        var answer = new long[nums.Length\
        \ - k + 1];\n        answer[0] = total;\n        for (int i = k; i < nums.Length;\
        \ i++) {\n            Change(nums[i - k], -1);\n            Change(nums[i],\
        \ 1);\n            answer[i - k + 1] = total;\n        }\n        return answer;\n\
        \    }\n}"
      javascript: "/**\n * @param {number[]} nums\n * @param {number} k\n * @param {number}\
        \ x\n * @return {number[]}\n */\nvar findXSum = function(nums, k, x) {\n   \
        \ const freq = new Map();\n    const top = new Set();\n    const rest = new\
        \ Set();\n    let total = 0;\n\n    const compare = (a, b) => {\n        const\
        \ fa = freq.get(a), fb = freq.get(b);\n        return fa - fb || a - b;\n  \
        \  };\n\n    const minValue = set => {\n        let result;\n        for (const\
        \ value of set) if (result === undefined || compare(value, result) < 0) result\
        \ = value;\n        return result;\n    };\n\n    const maxValue = set => {\n\
        \        let result;\n        for (const value of set) if (result === undefined\
        \ || compare(value, result) > 0) result = value;\n        return result;\n \
        \   };\n\n    const addTop = value => {\n        top.add(value);\n        total\
        \ += freq.get(value) * value;\n    };\n\n    const change = (value, delta) =>\
        \ {\n        const old = freq.get(value) || 0;\n        if (old > 0) {\n   \
        \         if (top.delete(value)) total -= old * value;\n            else rest.delete(value);\n\
        \        }\n        const next = old + delta;\n        if (next > 0) {\n   \
        \         freq.set(value, next);\n            if (top.size < x || (!rest.size\
        \ && compare(value, minValue(top)) > 0)) {\n                addTop(value);\n\
        \            } else if (top.size < x || compare(value, minValue(top)) > 0) {\n\
        \                addTop(value);\n            } else {\n                rest.add(value);\n\
        \            }\n        } else {\n            freq.delete(value);\n        }\n\
        \        while (top.size > x) {\n            const valueToMove = minValue(top);\n\
        \            top.delete(valueToMove);\n            total -= freq.get(valueToMove)\
        \ * valueToMove;\n            rest.add(valueToMove);\n        }\n        while\
        \ (top.size < x && rest.size > 0) {\n            const valueToMove = maxValue(rest);\n\
        \            rest.delete(valueToMove);\n            addTop(valueToMove);\n \
        \       }\n        while (top.size > 0 && rest.size > 0) {\n            const\
        \ low = minValue(top);\n            const high = maxValue(rest);\n         \
        \   if (compare(low, high) >= 0) break;\n            top.delete(low);\n    \
        \        total -= freq.get(low) * low;\n            rest.delete(high);\n   \
        \         addTop(high);\n            rest.add(low);\n        }\n    };\n\n \
        \   for (let i = 0; i < k; i++) change(nums[i], 1);\n    const answer = [total];\n\
        \    for (let i = k; i < nums.length; i++) {\n        change(nums[i - k], -1);\n\
        \        change(nums[i], 1);\n        answer.push(total);\n    }\n    return\
        \ answer;\n};"
    approach: 'Maintain the current window''s frequencies and divide its distinct values
      between two ordered sets. Order each set by the pair (frequency, value), so the
      greatest pair represents the most frequent value, with larger values breaking
      ties. Keep the best x values in the first set and all remaining values in the
      second.


      Track the weighted sum of the first set, where each value contributes value times
      frequency. As the window slides, remove the outgoing value''s old pair, update
      its frequency, and insert its new pair; do the same for the incoming value. Rebalance
      the sets so the first contains the top x values, then record its sum. Each update
      and rebalance takes logarithmic time.'
    time_complexity: O(n log n), since each window slide performs a constant number
      of ordered-set updates and rebalancing operations.
    space_complexity: O(n), for the frequency map and the ordered sets of distinct values
      in the current window.
    elapsed_time: 73.84765887260437
    model: gpt-6-luna
    generated_at: '2026-11-13 00:30:03 '
---

## Problem #3321: Find X-Sum of All K-Long Subarrays II

**Difficulty:** Hard

**Topics:** Array, Hash Table, Sliding Window, Heap (Priority Queue)

## Problem Description

<p>You are given an array <code>nums</code> of <code>n</code> integers and two integers <code>k</code> and <code>x</code>.</p>

<p>The <strong>x-sum</strong> of an array is calculated by the following procedure:</p>

<ul>
	<li>Count the occurrences of all elements in the array.</li>
	<li>Keep only the occurrences of the top <code>x</code> most frequent elements. If two elements have the same number of occurrences, the element with the <strong>bigger</strong> value is considered more frequent.</li>
	<li>Calculate the sum of the resulting array.</li>
</ul>

<p><strong>Note</strong> that if an array has less than <code>x</code> distinct elements, its <strong>x-sum</strong> is the sum of the array.</p>

<p>Return an integer array <code>answer</code> of length <code>n - k + 1</code> where <code>answer[i]</code> is the <strong>x-sum</strong> of the <span data-keyword="subarray-nonempty">subarray</span> <code>nums[i..i + k - 1]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,1,2,2,3,4,2,3], k = 6, x = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">[6,10,12]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>For subarray <code>[1, 1, 2, 2, 3, 4]</code>, only elements 1 and 2 will be kept in the resulting array. Hence, <code>answer[0] = 1 + 1 + 2 + 2</code>.</li>
	<li>For subarray <code>[1, 2, 2, 3, 4, 2]</code>, only elements 2 and 4 will be kept in the resulting array. Hence, <code>answer[1] = 2 + 2 + 2 + 4</code>. Note that 4 is kept in the array since it is bigger than 3 and 1 which occur the same number of times.</li>
	<li>For subarray <code>[2, 2, 3, 4, 2, 3]</code>, only elements 2 and 3 are kept in the resulting array. Hence, <code>answer[2] = 2 + 2 + 2 + 3 + 3</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,8,7,8,7,5], k = 2, x = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">[11,15,15,15,12]</span></p>

<p><strong>Explanation:</strong></p>

<p>Since <code>k == x</code>, <code>answer[i]</code> is equal to the sum of the subarray <code>nums[i..i + k - 1]</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>nums.length == n</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= x &lt;= k &lt;= nums.length</code></li>
</ul>


## Hints

1. Use sliding window.

2. Use two sets ordered by frequency. One of the sets will only contain the top `x` frequent elements, and the second will contain all other elements.

3. Update the two sets whenever you slide the window, and maintain a sum of the elements in the set with `x` elements

## 🤖 AI-Generated Solution (gpt-6-luna)

### Approach

Maintain the current window's frequencies and divide its distinct values between two ordered sets. Order each set by the pair (frequency, value), so the greatest pair represents the most frequent value, with larger values breaking ties. Keep the best x values in the first set and all remaining values in the second.

Track the weighted sum of the first set, where each value contributes value times frequency. As the window slides, remove the outgoing value's old pair, update its frequency, and insert its new pair; do the same for the incoming value. Rebalance the sets so the first contains the top x values, then record its sum. Each update and rebalance takes logarithmic time.

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
    vector<long long> findXSum(vector<int>& nums, int k, int x) {
        using Entry = pair<int, int>;
        set<Entry> top, rest;
        unordered_map<int, int> freq;
        long long sum = 0;

        auto addToTop = [&](Entry e) {
            top.insert(e);
            sum += 1LL * e.first * e.second;
        };
        auto addToRest = [&](Entry e) {
            rest.insert(e);
        };
        auto removeFromTop = [&](Entry e) {
            top.erase(e);
            sum -= 1LL * e.first * e.second;
        };
        auto removeFromRest = [&](Entry e) {
            rest.erase(e);
        };
        auto rebalance = [&]() {
            while ((int)top.size() > x) {
                auto it = top.begin();
                Entry e = *it;
                removeFromTop(e);
                addToRest(e);
            }
            while ((int)top.size() < x && !rest.empty()) {
                auto it = prev(rest.end());
                Entry e = *it;
                removeFromRest(e);
                addToTop(e);
            }
            while (!top.empty() && !rest.empty() && *top.begin() < *prev(rest.end())) {
                Entry low = *top.begin();
                Entry high = *prev(rest.end());
                removeFromTop(low);
                removeFromRest(high);
                addToTop(high);
                addToRest(low);
            }
        };
        auto change = [&](int value, int delta) {
            auto it = freq.find(value);
            if (it != freq.end() && it->second > 0) {
                Entry oldEntry = {it->second, value};
                if (top.count(oldEntry)) removeFromTop(oldEntry);
                else removeFromRest(oldEntry);
            }
            int next = (it == freq.end() ? 0 : it->second) + delta;
            if (next == 0) {
                freq.erase(value);
            } else {
                freq[value] = next;
                Entry newEntry = {next, value};
                if (!top.empty() && newEntry >= *top.begin()) addToTop(newEntry);
                else addToRest(newEntry);
            }
            rebalance();
        };

        for (int i = 0; i < k; ++i) change(nums[i], 1);
        vector<long long> answer;
        answer.reserve(nums.size() - k + 1);
        answer.push_back(sum);
        for (int i = k; i < (int)nums.size(); ++i) {
            change(nums[i - k], -1);
            change(nums[i], 1);
            answer.push_back(sum);
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
    public long[] findXSum(int[] nums, int k, int x) {
        TreeSet<long[]> top = new TreeSet<>((a, b) -> {
            int c = Long.compare(a[0], b[0]);
            if (c != 0) return c;
            return Long.compare(a[1], b[1]);
        });
        TreeSet<long[]> rest = new TreeSet<>((a, b) -> {
            int c = Long.compare(a[0], b[0]);
            if (c != 0) return c;
            return Long.compare(a[1], b[1]);
        });
        HashMap<Integer, Integer> freq = new HashMap<>();
        long[] sum = new long[1];

        class Window {
            void addTop(long[] e) {
                top.add(e);
                sum[0] += e[0] * e[1];
            }
            void addRest(long[] e) {
                rest.add(e);
            }
            void removeTop(long[] e) {
                top.remove(e);
                sum[0] -= e[0] * e[1];
            }
            void removeRest(long[] e) {
                rest.remove(e);
            }
            void rebalance() {
                while (top.size() > x) {
                    long[] e = top.first();
                    removeTop(e);
                    addRest(e);
                }
                while (top.size() < x && !rest.isEmpty()) {
                    long[] e = rest.last();
                    removeRest(e);
                    addTop(e);
                }
                while (!top.isEmpty() && !rest.isEmpty() && compare(top.first(), rest.last()) < 0) {
                    long[] low = top.first();
                    long[] high = rest.last();
                    removeTop(low);
                    removeRest(high);
                    addTop(high);
                    addRest(low);
                }
            }
            int compare(long[] a, long[] b) {
                int c = Long.compare(a[0], b[0]);
                if (c != 0) return c;
                return Long.compare(a[1], b[1]);
            }
            void change(int value, int delta) {
                Integer old = freq.get(value);
                if (old != null && old > 0) {
                    long[] e = new long[]{old, value};
                    if (top.remove(e)) sum[0] -= e[0] * e[1];
                    else rest.remove(e);
                }
                int next = (old == null ? 0 : old) + delta;
                if (next == 0) {
                    freq.remove(value);
                } else {
                    freq.put(value, next);
                    long[] e = new long[]{next, value};
                    if (!top.isEmpty() && compare(e, top.first()) >= 0) addTop(e);
                    else addRest(e);
                }
                rebalance();
            }
        }

        Window window = new Window();
        for (int i = 0; i < k; i++) window.change(nums[i], 1);
        long[] answer = new long[nums.length - k + 1];
        answer[0] = sum[0];
        for (int i = k; i < nums.length; i++) {
            window.change(nums[i - k], -1);
            window.change(nums[i], 1);
            answer[i - k + 1] = sum[0];
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
    def findXSum(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        import heapq

        freq = {}
        top = set()
        rest = set()
        total = 0

        def key(value):
            return (freq[value], value)

        def add_top(entry):
            nonlocal total
            top.add(entry)
            total += entry[0] * entry[1]

        def remove_top(entry):
            nonlocal total
            top.remove(entry)
            total -= entry[0] * entry[1]

        def rebalance():
            while len(top) > x:
                entry = min(top)
                remove_top(entry)
                rest.add(entry)
            while len(top) < x and rest:
                entry = max(rest)
                rest.remove(entry)
                add_top(entry)
            while top and rest and min(top) < max(rest):
                low = min(top)
                high = max(rest)
                remove_top(low)
                rest.remove(high)
                add_top(high)
                rest.add(low)

        def change(value, delta):
            old = freq.get(value, 0)
            if old:
                entry = (old, value)
                if entry in top:
                    remove_top(entry)
                else:
                    rest.remove(entry)
            new = old + delta
            if new:
                freq[value] = new
                entry = (new, value)
                if top and entry >= min(top):
                    add_top(entry)
                else:
                    rest.add(entry)
            else:
                freq.pop(value, None)
            rebalance()

        for value in nums[:k]:
            change(value, 1)
        answer = [total]
        for i in range(k, len(nums)):
            change(nums[i - k], -1)
            change(nums[i], 1)
            answer.append(total)
        return answer
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        import heapq

        freq = {}
        top = set()
        rest = set()
        total = 0

        def key(value):
            return (freq[value], value)

        def add_top(value):
            nonlocal total
            top.add(value)
            total += freq[value] * value

        def add_rest(value):
            rest.add(value)

        def promote_best():
            value = max(rest, key=key)
            rest.remove(value)
            add_top(value)

        def demote_worst():
            nonlocal total
            value = min(top, key=key)
            top.remove(value)
            total -= freq[value] * value
            rest.add(value)

        def change(value, delta):
            nonlocal total
            if value in freq:
                if value in top:
                    top.remove(value)
                    total -= freq[value] * value
                else:
                    rest.remove(value)
                new_count = freq[value] + delta
            else:
                new_count = delta

            if new_count:
                freq[value] = new_count
                if len(top) < x:
                    add_top(value)
                elif not rest or (new_count, value) > min((freq[v], v) for v in top):
                    add_top(value)
                else:
                    add_rest(value)
            else:
                del freq[value]

            while len(top) > x:
                demote_worst()
            while len(top) < x and rest:
                promote_best()
            while top and rest:
                worst = min(top, key=key)
                best = max(rest, key=key)
                if key(worst) >= key(best):
                    break
                top.remove(worst)
                total -= freq[worst] * worst
                rest.remove(best)
                add_top(best)
                rest.add(worst)

        for value in nums[:k]:
            change(value, 1)

        answer = [total]
        for i in range(k, len(nums)):
            change(nums[i - k], -1)
            change(nums[i], 1)
            answer.append(total)
        return answer
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>

typedef struct {
    int value;
    int frequency;
    int inTop;
    int active;
} Entry;

typedef struct {
    int value;
    int frequency;
} Node;

typedef struct {
    Node *data;
    int size;
    int capacity;
    int isMin;
} Heap;

static int better(Node a, Node b) {
    return a.frequency > b.frequency || (a.frequency == b.frequency && a.value > b.value);
}

static int worse(Node a, Node b) {
    return a.frequency < b.frequency || (a.frequency == b.frequency && a.value < b.value);
}

static int precedes(Heap *heap, Node a, Node b) {
    return heap->isMin ? worse(a, b) : better(a, b);
}

static void heapPush(Heap *heap, Node node) {
    if (heap->size == heap->capacity) {
        heap->capacity = heap->capacity ? heap->capacity * 2 : 16;
        heap->data = (Node *)realloc(heap->data, sizeof(Node) * heap->capacity);
    }
    int i = heap->size++;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (!precedes(heap, node, heap->data[p])) break;
        heap->data[i] = heap->data[p];
        i = p;
    }
    heap->data[i] = node;
}

static Node heapPop(Heap *heap) {
    Node result = heap->data[0];
    Node last = heap->data[--heap->size];
    if (heap->size > 0) {
        int i = 0;
        while (i * 2 + 1 < heap->size) {
            int child = i * 2 + 1;
            if (child + 1 < heap->size && precedes(heap, heap->data[child + 1], heap->data[child])) child++;
            if (!precedes(heap, heap->data[child], last)) break;
            heap->data[i] = heap->data[child];
            i = child;
        }
        heap->data[i] = last;
    }
    return result;
}

static int findIndex(Entry *entries, int count, int value) {
    int lo = 0, hi = count - 1;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        if (entries[mid].value == value) return mid;
        if (entries[mid].value < value) lo = mid + 1;
        else hi = mid - 1;
    }
    return lo;
}

static int findExisting(Entry *entries, int count, int value) {
    int lo = 0, hi = count - 1;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        if (entries[mid].value == value) return mid;
        if (entries[mid].value < value) lo = mid + 1;
        else hi = mid - 1;
    }
    return -1;
}

long long* findXSum(int* nums, int numsSize, int k, int x, int* returnSize) {
    int *sorted = (int *)malloc(sizeof(int) * numsSize);
    for (int i = 0; i < numsSize; i++) sorted[i] = nums[i];
    for (int i = 1; i < numsSize; i++) {
        int v = sorted[i], j = i - 1;
        while (j >= 0 && sorted[j] > v) { sorted[j + 1] = sorted[j]; j--; }
        sorted[j + 1] = v;
    }
    Entry *entries = (Entry *)calloc(numsSize, sizeof(Entry));
    int count = 0;
    for (int i = 0; i < numsSize; i++) {
        if (i == 0 || sorted[i] != sorted[i - 1]) entries[count++].value = sorted[i];
    }
    free(sorted);

    Heap topMin = {0}, restMax = {0};
    topMin.isMin = 1;
    restMax.isMin = 0;
    long long total = 0;
    long long *answer = (long long *)malloc(sizeof(long long) * (numsSize - k + 1));
    int answerCount = 0;

    for (int step = 0; step < numsSize; step++) {
        int value = nums[step];
        int index = findExisting(entries, count, value);
        int old = entries[index].frequency;
        if (old > 0) {
            if (entries[index].inTop) total -= (long long)old * value;
            entries[index].frequency = 0;
            entries[index].active = 0;
        }
        entries[index].frequency = old + 1;
        entries[index].active = 1;
        Node node = {value, old + 1};
        if (old > 0 && entries[index].inTop) {
            entries[index].inTop = 0;
        }
        heapPush(&restMax, node);

        if (step >= k) {
            int out = nums[step - k];
            int oi = findExisting(entries, count, out);
            int oldOut = entries[oi].frequency;
            if (entries[oi].inTop) total -= (long long)oldOut * out;
            entries[oi].frequency = oldOut - 1;
            entries[oi].active = oldOut > 1;
            if (oldOut == 1) entries[oi].inTop = 0;
            else heapPush(entries[oi].inTop ? &topMin : &restMax, (Node){out, oldOut - 1});
        }

        int windowStart = step >= k - 1 ? step - k + 1 : 0;
        int windowLength = step + 1 - windowStart;
        int target = windowLength < x ? windowLength : x;
        while (topMin.size > 0) {
            Node n = topMin.data[0];
            int idx = findExisting(entries, count, n.value);
            if (!entries[idx].active || !entries[idx].inTop || entries[idx].frequency != n.frequency) heapPop(&topMin);
            else break;
        }
        while (restMax.size > 0) {
            Node n = restMax.data[0];
            int idx = findExisting(entries, count, n.value);
            if (!entries[idx].active || entries[idx].inTop || entries[idx].frequency != n.frequency) heapPop(&restMax);
            else break;
        }
        while (topMin.size < target && restMax.size > 0) {
            Node n = heapPop(&restMax);
            int idx = findExisting(entries, count, n.value);
            if (!entries[idx].active || entries[idx].inTop || entries[idx].frequency != n.frequency) continue;
            entries[idx].inTop = 1;
            total += (long long)n.frequency * n.value;
            heapPush(&topMin, n);
        }
        while (topMin.size > target) {
            Node n = heapPop(&topMin);
            int idx = findExisting(entries, count, n.value);
            if (!entries[idx].active || !entries[idx].inTop || entries[idx].frequency != n.frequency) continue;
            entries[idx].inTop = 0;
            total -= (long long)n.frequency * n.value;
            heapPush(&restMax, n);
        }
        while (topMin.size > 0 && restMax.size > 0) {
            Node low = topMin.data[0], high = restMax.data[0];
            int li = findExisting(entries, count, low.value), hi = findExisting(entries, count, high.value);
            if (!entries[li].active || !entries[li].inTop || entries[li].frequency != low.frequency) { heapPop(&topMin); continue; }
            if (!entries[hi].active || entries[hi].inTop || entries[hi].frequency != high.frequency) { heapPop(&restMax); continue; }
            if (!better(high, low)) break;
            heapPop(&topMin);
            heapPop(&restMax);
            entries[li].inTop = 0;
            entries[hi].inTop = 1;
            total += (long long)high.frequency * high.value - (long long)low.frequency * low.value;
            heapPush(&restMax, low);
            heapPush(&topMin, high);
        }
        if (step >= k - 1) answer[answerCount++] = total;
    }
    free(entries);
    free(topMin.data);
    free(restMax.data);
    *returnSize = answerCount;
    return answer;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;
using System.Collections.Generic;

public class Solution {
    public long[] FindXSum(int[] nums, int k, int x) {
        var freq = new Dictionary<int, int>();
        var top = new SortedSet<(int frequency, int value)>();
        var rest = new SortedSet<(int frequency, int value)>();
        long total = 0;

        void Change(int value, int delta) {
            int old = freq.TryGetValue(value, out int current) ? current : 0;
            if (old > 0) {
                var entry = (old, value);
                if (top.Remove(entry)) total -= (long)old * value;
                else rest.Remove(entry);
            }
            int next = old + delta;
            if (next > 0) {
                freq[value] = next;
                var entry = (next, value);
                if (top.Count < x || entry.CompareTo(top.Min) > 0) {
                    top.Add(entry);
                    total += (long)next * value;
                } else {
                    rest.Add(entry);
                }
            } else {
                freq.Remove(value);
            }
            while (top.Count > x) {
                var entry = top.Min;
                top.Remove(entry);
                total -= (long)entry.frequency * entry.value;
                rest.Add(entry);
            }
            while (top.Count < x && rest.Count > 0) {
                var entry = rest.Max;
                rest.Remove(entry);
                top.Add(entry);
                total += (long)entry.frequency * entry.value;
            }
            while (top.Count > 0 && rest.Count > 0 && top.Min.CompareTo(rest.Max) < 0) {
                var low = top.Min;
                var high = rest.Max;
                top.Remove(low);
                rest.Remove(high);
                total += (long)high.frequency * high.value - (long)low.frequency * low.value;
                top.Add(high);
                rest.Add(low);
            }
        }

        for (int i = 0; i < k; i++) Change(nums[i], 1);
        var answer = new long[nums.Length - k + 1];
        answer[0] = total;
        for (int i = k; i < nums.Length; i++) {
            Change(nums[i - k], -1);
            Change(nums[i], 1);
            answer[i - k + 1] = total;
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
 * @param {number[]} nums
 * @param {number} k
 * @param {number} x
 * @return {number[]}
 */
var findXSum = function(nums, k, x) {
    const freq = new Map();
    const top = new Set();
    const rest = new Set();
    let total = 0;

    const compare = (a, b) => {
        const fa = freq.get(a), fb = freq.get(b);
        return fa - fb || a - b;
    };

    const minValue = set => {
        let result;
        for (const value of set) if (result === undefined || compare(value, result) < 0) result = value;
        return result;
    };

    const maxValue = set => {
        let result;
        for (const value of set) if (result === undefined || compare(value, result) > 0) result = value;
        return result;
    };

    const addTop = value => {
        top.add(value);
        total += freq.get(value) * value;
    };

    const change = (value, delta) => {
        const old = freq.get(value) || 0;
        if (old > 0) {
            if (top.delete(value)) total -= old * value;
            else rest.delete(value);
        }
        const next = old + delta;
        if (next > 0) {
            freq.set(value, next);
            if (top.size < x || (!rest.size && compare(value, minValue(top)) > 0)) {
                addTop(value);
            } else if (top.size < x || compare(value, minValue(top)) > 0) {
                addTop(value);
            } else {
                rest.add(value);
            }
        } else {
            freq.delete(value);
        }
        while (top.size > x) {
            const valueToMove = minValue(top);
            top.delete(valueToMove);
            total -= freq.get(valueToMove) * valueToMove;
            rest.add(valueToMove);
        }
        while (top.size < x && rest.size > 0) {
            const valueToMove = maxValue(rest);
            rest.delete(valueToMove);
            addTop(valueToMove);
        }
        while (top.size > 0 && rest.size > 0) {
            const low = minValue(top);
            const high = maxValue(rest);
            if (compare(low, high) >= 0) break;
            top.delete(low);
            total -= freq.get(low) * low;
            rest.delete(high);
            addTop(high);
            rest.add(low);
        }
    };

    for (let i = 0; i < k; i++) change(nums[i], 1);
    const answer = [total];
    for (let i = k; i < nums.length; i++) {
        change(nums[i - k], -1);
        change(nums[i], 1);
        answer.push(total);
    }
    return answer;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function findXSum(nums: number[], k: number, x: number): number[] {
    const freq = new Map<number, number>();
    const top: [number, number][] = [];
    const rest: [number, number][] = [];
    let total = 0;

    const compare = (a: [number, number], b: [number, number]): number =>
        a[0] - b[0] || a[1] - b[1];

    const insert = (set: [number, number][], entry: [number, number]): void => {
        let left = 0;
        let right = set.length;
        while (left < right) {
            const mid = (left + right) >>> 1;
            if (compare(set[mid], entry) < 0) left = mid + 1;
            else right = mid;
        }
        set.splice(left, 0, entry);
    };

    const remove = (set: [number, number][], entry: [number, number]): void => {
        let left = 0;
        let right = set.length;
        while (left < right) {
            const mid = (left + right) >>> 1;
            if (compare(set[mid], entry) < 0) left = mid + 1;
            else right = mid;
        }
        set.splice(left, 1);
    };

    const change = (value: number, delta: number): void => {
        const old = freq.get(value) ?? 0;
        if (old > 0) {
            const entry: [number, number] = [old, value];
            const index = top.findIndex(item => compare(item, entry) === 0);
            if (index >= 0) {
                top.splice(index, 1);
                total -= old * value;
            } else {
                remove(rest, entry);
            }
        }

        const next = old + delta;
        if (next > 0) {
            freq.set(value, next);
            const entry: [number, number] = [next, value];
            if (top.length < x || compare(entry, top[0]) > 0) {
                insert(top, entry);
                total += next * value;
            } else {
                insert(rest, entry);
            }
        } else {
            freq.delete(value);
        }

        while (top.length > x) {
            const entry = top.shift()!;
            total -= entry[0] * entry[1];
            insert(rest, entry);
        }
        while (top.length < x && rest.length > 0) {
            const entry = rest.pop()!;
            insert(top, entry);
            total += entry[0] * entry[1];
        }
        while (top.length > 0 && rest.length > 0 && compare(top[0], rest[rest.length - 1]) < 0) {
            const low = top.shift()!;
            const high = rest.pop()!;
            total += high[0] * high[1] - low[0] * low[1];
            insert(top, high);
            insert(rest, low);
        }
    };

    for (let i = 0; i < k; i++) change(nums[i], 1);
    const answer = [total];
    for (let i = k; i < nums.length; i++) {
        change(nums[i - k], -1);
        change(nums[i], 1);
        answer.push(total);
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
     * @param Integer[] $nums
     * @param Integer $k
     * @param Integer $x
     * @return Integer[]
     */
    function findXSum($nums, $k, $x) {
        $freq = [];
        $top = [];
        $rest = [];
        $total = 0;

        $compare = function ($a, $b) {
            return $a[0] <=> $b[0] ?: ($a[1] <=> $b[1]);
        };
        $insert = function (&$set, $entry) use ($compare) {
            $left = 0;
            $right = count($set);
            while ($left < $right) {
                $mid = intdiv($left + $right, 2);
                if ($compare($set[$mid], $entry) < 0) $left = $mid + 1;
                else $right = $mid;
            }
            array_splice($set, $left, 0, [$entry]);
        };
        $remove = function (&$set, $entry) use ($compare) {
            $left = 0;
            $right = count($set);
            while ($left < $right) {
                $mid = intdiv($left + $right, 2);
                if ($compare($set[$mid], $entry) < 0) $left = $mid + 1;
                else $right = $mid;
            }
            array_splice($set, $left, 1);
        };

        $change = function ($value, $delta) use (&$freq, &$top, &$rest, &$total, $x, $compare, $insert, $remove) {
            $old = $freq[$value] ?? 0;
            if ($old > 0) {
                $entry = [$old, $value];
                $left = 0;
                $right = count($top);
                while ($left < $right) {
                    $mid = intdiv($left + $right, 2);
                    if ($compare($top[$mid], $entry) < 0) $left = $mid + 1;
                    else $right = $mid;
                }
                if ($left < count($top) && $compare($top[$left], $entry) === 0) {
                    array_splice($top, $left, 1);
                    $total -= $old * $value;
                } else {
                    $remove($rest, $entry);
                }
            }

            $next = $old + $delta;
            if ($next > 0) {
                $freq[$value] = $next;
                $entry = [$next, $value];
                if (count($top) < $x || $compare($entry, $top[0]) > 0) {
                    $insert($top, $entry);
                    $total += $next * $value;
                } else {
                    $insert($rest, $entry);
                }
            } else {
                unset($freq[$value]);
            }

            while (count($top) > $x) {
                $entry = array_shift($top);
                $total -= $entry[0] * $entry[1];
                $insert($rest, $entry);
            }
            while (count($top) < $x && count($rest) > 0) {
                $entry = array_pop($rest);
                $insert($top, $entry);
                $total += $entry[0] * $entry[1];
            }
            while (count($top) > 0 && count($rest) > 0 && $compare($top[0], $rest[count($rest) - 1]) < 0) {
                $low = array_shift($top);
                $high = array_pop($rest);
                $total += $high[0] * $high[1] - $low[0] * $low[1];
                $insert($top, $high);
                $insert($rest, $low);
            }
        };

        for ($i = 0; $i < $k; $i++) $change($nums[$i], 1);
        $answer = [$total];
        for ($i = $k; $i < count($nums); $i++) {
            $change($nums[$i - $k], -1);
            $change($nums[$i], 1);
            $answer[] = $total;
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
    func findXSum(_ nums: [Int], _ k: Int, _ x: Int) -> [Int] {
        var freq: [Int: Int] = [:]
        var top: [(Int, Int)] = []
        var rest: [(Int, Int)] = []
        var total = 0

        func compare(_ a: (Int, Int), _ b: (Int, Int)) -> Int {
            if a.0 != b.0 { return a.0 < b.0 ? -1 : 1 }
            if a.1 != b.1 { return a.1 < b.1 ? -1 : 1 }
            return 0
        }

        func insert(_ set: inout [(Int, Int)], _ entry: (Int, Int)) {
            var left = 0
            var right = set.count
            while left < right {
                let mid = (left + right) / 2
                if compare(set[mid], entry) < 0 { left = mid + 1 }
                else { right = mid }
            }
            set.insert(entry, at: left)
        }

        func remove(_ set: inout [(Int, Int)], _ entry: (Int, Int)) {
            var left = 0
            var right = set.count
            while left < right {
                let mid = (left + right) / 2
                if compare(set[mid], entry) < 0 { left = mid + 1 }
                else { right = mid }
            }
            set.remove(at: left)
        }

        func change(_ value: Int, _ delta: Int) {
            let old = freq[value] ?? 0
            if old > 0 {
                let entry = (old, value)
                var left = 0
                var right = top.count
                while left < right {
                    let mid = (left + right) / 2
                    if compare(top[mid], entry) < 0 { left = mid + 1 }
                    else { right = mid }
                }
                if left < top.count && compare(top[left], entry) == 0 {
                    top.remove(at: left)
                    total -= old * value
                } else {
                    remove(&rest, entry)
                }
            }

            let next = old + delta
            if next > 0 {
                freq[value] = next
                let entry = (next, value)
                if top.count < x || compare(entry, top[0]) > 0 {
                    insert(&top, entry)
                    total += next * value
                } else {
                    insert(&rest, entry)
                }
            } else {
                freq.removeValue(forKey: value)
            }

            while top.count > x {
                let entry = top.removeFirst()
                total -= entry.0 * entry.1
                insert(&rest, entry)
            }
            while top.count < x && !rest.isEmpty {
                let entry = rest.removeLast()
                insert(&top, entry)
                total += entry.0 * entry.1
            }
            while !top.isEmpty && !rest.isEmpty && compare(top[0], rest[rest.count - 1]) < 0 {
                let low = top.removeFirst()
                let high = rest.removeLast()
                total += high.0 * high.1 - low.0 * low.1
                insert(&top, high)
                insert(&rest, low)
            }
        }

        for i in 0..<k { change(nums[i], 1) }
        var answer = [total]
        if k < nums.count {
            for i in k..<nums.count {
                change(nums[i - k], -1)
                change(nums[i], 1)
                answer.append(total)
            }
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
    fun findXSum(nums: IntArray, k: Int, x: Int): LongArray {
        val freq = HashMap<Int, Int>()
        val top = java.util.TreeSet<Pair<Int, Int>>(compareBy<Pair<Int, Int>> { it.first }.thenBy { it.second })
        val rest = java.util.TreeSet<Pair<Int, Int>>(compareBy<Pair<Int, Int>> { it.first }.thenBy { it.second })
        var total = 0L

        fun change(value: Int, delta: Int) {
            val old = freq[value] ?: 0
            if (old > 0) {
                val entry = Pair(old, value)
                if (top.remove(entry)) {
                    total -= old.toLong() * value
                } else {
                    rest.remove(entry)
                }
            }

            val next = old + delta
            if (next > 0) {
                freq[value] = next
                val entry = Pair(next, value)
                if (top.size < x || entry > top.first()) {
                    top.add(entry)
                    total += next.toLong() * value
                } else {
                    rest.add(entry)
                }
            } else {
                freq.remove(value)
            }

            while (top.size > x) {
                val entry = top.pollFirst()
                total -= entry.first.toLong() * entry.second
                rest.add(entry)
            }
            while (top.size < x && rest.isNotEmpty()) {
                val entry = rest.pollLast()
                top.add(entry)
                total += entry.first.toLong() * entry.second
            }
            while (top.isNotEmpty() && rest.isNotEmpty() && top.first() < rest.last()) {
                val low = top.pollFirst()
                val high = rest.pollLast()
                total += high.first.toLong() * high.second - low.first.toLong() * low.second
                top.add(high)
                rest.add(low)
            }
        }

        for (i in 0 until k) change(nums[i], 1)
        val answer = LongArray(nums.size - k + 1)
        answer[0] = total
        for (i in k until nums.size) {
            change(nums[i - k], -1)
            change(nums[i], 1)
            answer[i - k + 1] = total
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
  List<int> findXSum(List<int> nums, int k, int x) {
    final freq = <int, int>{};
    final top = SplayTreeSet<(int, int)>((a, b) {
      final byFreq = a.$1.compareTo(b.$1);
      return byFreq != 0 ? byFreq : a.$2.compareTo(b.$2);
    });
    final rest = SplayTreeSet<(int, int)>((a, b) {
      final byFreq = a.$1.compareTo(b.$1);
      return byFreq != 0 ? byFreq : a.$2.compareTo(b.$2);
    });
    var total = 0;

    void change(int value, int delta) {
      final old = freq[value] ?? 0;
      if (old > 0) {
        final entry = (old, value);
        if (top.remove(entry)) {
          total -= old * value;
        } else {
          rest.remove(entry);
        }
      }

      final next = old + delta;
      if (next > 0) {
        freq[value] = next;
        final entry = (next, value);
        if (top.length < x || _compare(entry, top.first) > 0) {
          top.add(entry);
          total += next * value;
        } else {
          rest.add(entry);
        }
      } else {
        freq.remove(value);
      }

      while (top.length > x) {
        final entry = top.first;
        top.remove(entry);
        total -= entry.$1 * entry.$2;
        rest.add(entry);
      }
      while (top.length < x && rest.isNotEmpty) {
        final entry = rest.last;
        rest.remove(entry);
        top.add(entry);
        total += entry.$1 * entry.$2;
      }
      while (top.isNotEmpty && rest.isNotEmpty &&
          _compare(top.first, rest.last) < 0) {
        final low = top.first;
        final high = rest.last;
        top.remove(low);
        rest.remove(high);
        total += high.$1 * high.$2 - low.$1 * low.$2;
        top.add(high);
        rest.add(low);
      }
    }

    for (var i = 0; i < k; i++) {
      change(nums[i], 1);
    }
    final answer = <int>[total];
    for (var i = k; i < nums.length; i++) {
      change(nums[i - k], -1);
      change(nums[i], 1);
      answer.add(total);
    }
    return answer;
  }

  int _compare((int, int) a, (int, int) b) {
    final byFreq = a.$1.compareTo(b.$1);
    return byFreq != 0 ? byFreq : a.$2.compareTo(b.$2);
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func findXSum(nums []int, k int, x int) []int64 {
	freq := make(map[int]int)
	top := &OrderedSet{}
	rest := &OrderedSet{}
	var total int64

	change := func(value, delta int) {}
	change = func(value, delta int) {
		old := freq[value]
		if old > 0 {
			entry := Pair{freq: old, value: value}
			if top.Remove(entry) {
				total -= int64(old) * int64(value)
			} else {
				rest.Remove(entry)
			}
		}

		next := old + delta
		if next > 0 {
			freq[value] = next
			entry := Pair{freq: next, value: value}
			if top.Len() < x || comparePair(entry, top.Min()) > 0 {
				top.Add(entry)
				total += int64(next) * int64(value)
			} else {
				rest.Add(entry)
			}
		} else {
			delete(freq, value)
		}

		for top.Len() > x {
			entry := top.PopMin()
			total -= int64(entry.freq) * int64(entry.value)
			rest.Add(entry)
		}
		for top.Len() < x && rest.Len() > 0 {
			entry := rest.PopMax()
			top.Add(entry)
			total += int64(entry.freq) * int64(entry.value)
		}
		for top.Len() > 0 && rest.Len() > 0 && comparePair(top.Min(), rest.Max()) < 0 {
			low := top.PopMin()
			high := rest.PopMax()
			total += int64(high.freq)*int64(high.value) - int64(low.freq)*int64(low.value)
			top.Add(high)
			rest.Add(low)
		}
	}

	for i := 0; i < k; i++ {
		change(nums[i], 1)
	}
	answer := make([]int64, 0, len(nums)-k+1)
	answer = append(answer, total)
	for i := k; i < len(nums); i++ {
		change(nums[i-k], -1)
		change(nums[i], 1)
		answer = append(answer, total)
	}
	return answer
}

type Pair struct {
	freq  int
	value int
}

type Node struct {
	key         Pair
	priority    uint32
	left, right *Node
}

type OrderedSet struct {
	root *Node
	size int
}

func comparePair(a, b Pair) int {
	if a.freq < b.freq {
		return -1
	}
	if a.freq > b.freq {
		return 1
	}
	if a.value < b.value {
		return -1
	}
	if a.value > b.value {
		return 1
	}
	return 0
}

func pairPriority(p Pair) uint32 {
	x := uint64(uint32(p.freq))*0x9e3779b97f4a7c15 + uint64(uint32(p.value))
	x ^= x >> 30
	x *= 0xbf58476d1ce4e5b9
	x ^= x >> 27
	x *= 0x94d049bb133111eb
	x ^= x >> 31
	return uint32(x)
}

func rotateRight(n *Node) *Node {
	left := n.left
	n.left = left.right
	left.right = n
	return left
}

func rotateLeft(n *Node) *Node {
	right := n.right
	n.right = right.left
	right.left = n
	return right
}

func insertNode(n *Node, key Pair) *Node {
	if n == nil {
		return &Node{key: key, priority: pairPriority(key)}
	}
	if comparePair(key, n.key) < 0 {
		n.left = insertNode(n.left, key)
		if n.left.priority < n.priority {
			n = rotateRight(n)
		}
	} else if comparePair(key, n.key) > 0 {
		n.right = insertNode(n.right, key)
		if n.right.priority < n.priority {
			n = rotateLeft(n)
		}
	}
	return n
}

func deleteNode(n *Node, key Pair) *Node {
	if n == nil {
		return nil
	}
	cmp := comparePair(key, n.key)
	if cmp < 0 {
		n.left = deleteNode(n.left, key)
	} else if cmp > 0 {
		n.right = deleteNode(n.right, key)
	} else {
		if n.left == nil {
			return n.right
		}
		if n.right == nil {
			return n.left
		}
		if n.left.priority < n.right.priority {
			n = rotateRight(n)
			n.right = deleteNode(n.right, key)
		} else {
			n = rotateLeft(n)
			n.left = deleteNode(n.left, key)
		}
	}
	return n
}

func (s *OrderedSet) Add(key Pair) {
	before := s.Len()
	s.root = insertNode(s.root, key)
	if s.Len() == before {
		return
	}
	s.size++
}

func (s *OrderedSet) Remove(key Pair) bool {
	if !s.Contains(key) {
		return false
	}
	s.root = deleteNode(s.root, key)
	s.size--
	return true
}

func (s *OrderedSet) Contains(key Pair) bool {
	n := s.root
	for n != nil {
		cmp := comparePair(key, n.key)
		if cmp == 0 {
			return true
		}
		if cmp < 0 {
			n = n.left
		} else {
			n = n.right
		}
	}
	return false
}

func (s *OrderedSet) Len() int {
	return s.size
}

func (s *OrderedSet) Min() Pair {
	n := s.root
	for n.left != nil {
		n = n.left
	}
	return n.key
}

func (s *OrderedSet) Max() Pair {
	n := s.root
	for n.right != nil {
		n = n.right
	}
	return n.key
}

func (s *OrderedSet) PopMin() Pair {
	key := s.Min()
	s.root = deleteNode(s.root, key)
	s.size--
	return key
}

func (s *OrderedSet) PopMax() Pair {
	key := s.Max()
	s.root = deleteNode(s.root, key)
	s.size--
	return key
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} nums
# @param {Integer} k
# @param {Integer} x
# @return {Integer[]}
def find_x_sum(nums, k, x)
  freq = Hash.new(0)
  top = SortedSet.new
  rest = SortedSet.new
  total = 0

  change = lambda do |value, delta|
    old = freq[value]
    if old > 0
      entry = [old, value]
      if top.delete?(entry)
        total -= old * value
      else
        rest.delete(entry)
      end
    end

    current = old + delta
    if current > 0
      freq[value] = current
      entry = [current, value]
      if top.size < x || (entry <=> top.first) > 0
        top.add(entry)
        total += current * value
      else
        rest.add(entry)
      end
    else
      freq.delete(value)
    end

    while top.size > x
      entry = top.first
      top.delete(entry)
      total -= entry[0] * entry[1]
      rest.add(entry)
    end
    while top.size < x && !rest.empty?
      entry = rest.last
      rest.delete(entry)
      top.add(entry)
      total += entry[0] * entry[1]
    end
    while !top.empty? && !rest.empty? && (top.first <=> rest.last) < 0
      low = top.first
      high = rest.last
      top.delete(low)
      rest.delete(high)
      total += high[0] * high[1] - low[0] * low[1]
      top.add(high)
      rest.add(low)
    end
  end

  nums[0, k].each { |value| change.call(value, 1) }
  answer = [total]
  (k...nums.length).each do |i|
    change.call(nums[i - k], -1)
    change.call(nums[i], 1)
    answer << total
  end
  answer
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.collection.mutable

object Solution {
    def findXSum(nums: Array[Int], k: Int, x: Int): Array[Long] = {
        val freq = mutable.HashMap.empty[Int, Int]
        val ordering = Ordering[(Int, Int)]
        val top = mutable.TreeSet.empty[(Int, Int)](ordering)
        val rest = mutable.TreeSet.empty[(Int, Int)](ordering)
        var total = 0L

        def change(value: Int, delta: Int): Unit = {
            val old = freq.getOrElse(value, 0)
            if (old > 0) {
                val entry = (old, value)
                if (top.remove(entry)) {
                    total -= old.toLong * value
                } else {
                    rest.remove(entry)
                }
            }

            val next = old + delta
            if (next > 0) {
                freq(value) = next
                val entry = (next, value)
                if (top.size < x || ordering.gt(entry, top.head)) {
                    top.add(entry)
                    total += next.toLong * value
                } else {
                    rest.add(entry)
                }
            } else {
                freq.remove(value)
            }

            while (top.size > x) {
                val entry = top.head
                top.remove(entry)
                total -= entry._1.toLong * entry._2
                rest.add(entry)
            }
            while (top.size < x && rest.nonEmpty) {
                val entry = rest.last
                rest.remove(entry)
                top.add(entry)
                total += entry._1.toLong * entry._2
            }
            while (top.nonEmpty && rest.nonEmpty && ordering.lt(top.head, rest.last)) {
                val low = top.head
                val high = rest.last
                top.remove(low)
                rest.remove(high)
                total += high._1.toLong * high._2 - low._1.toLong * low._2
                top.add(high)
                rest.add(low)
            }
        }

        var i = 0
        while (i < k) {
            change(nums(i), 1)
            i += 1
        }
        val answer = new Array[Long](nums.length - k + 1)
        answer(0) = total
        i = k
        var index = 1
        while (i < nums.length) {
            change(nums(i - k), -1)
            change(nums(i), 1)
            answer(index) = total
            i += 1
            index += 1
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
    pub fn find_x_sum(nums: Vec<i32>, k: i32, x: i32) -> Vec<i64> {
        use std::collections::BTreeSet;

        let k = k as usize;
        let x = x as usize;
        let mut freq = std::collections::HashMap::<i32, i32>::new();
        let mut top = BTreeSet::<(i32, i32)>::new();
        let mut rest = BTreeSet::<(i32, i32)>::new();
        let mut total = 0i64;

        let change = |value: i32,
                      delta: i32,
                      freq: &mut std::collections::HashMap<i32, i32>,
                      top: &mut BTreeSet<(i32, i32)>,
                      rest: &mut BTreeSet<(i32, i32)>,
                      total: &mut i64| {
            let old = *freq.get(&value).unwrap_or(&0);
            if old > 0 {
                let entry = (old, value);
                if top.remove(&entry) {
                    *total -= old as i64 * value as i64;
                } else {
                    rest.remove(&entry);
                }
            }
            let new = old + delta;
            if new > 0 {
                freq.insert(value, new);
                let entry = (new, value);
                if top.len() < x || top.first().map_or(false, |smallest| entry > *smallest) {
                    top.insert(entry);
                    *total += new as i64 * value as i64;
                } else {
                    rest.insert(entry);
                }
            } else {
                freq.remove(&value);
            }
            while top.len() > x {
                let entry = *top.first().unwrap();
                top.remove(&entry);
                *total -= entry.0 as i64 * entry.1 as i64;
                rest.insert(entry);
            }
            while top.len() < x && !rest.is_empty() {
                let entry = *rest.last().unwrap();
                rest.remove(&entry);
                top.insert(entry);
                *total += entry.0 as i64 * entry.1 as i64;
            }
            while !top.is_empty() && !rest.is_empty() && top.first().unwrap() < rest.last().unwrap() {
                let low = *top.first().unwrap();
                let high = *rest.last().unwrap();
                top.remove(&low);
                rest.remove(&high);
                *total += (high.0 as i64 * high.1 as i64) - (low.0 as i64 * low.1 as i64);
                top.insert(high);
                rest.insert(low);
            }
        };

        for &value in nums.iter().take(k) {
            change(value, 1, &mut freq, &mut top, &mut rest, &mut total);
        }
        let mut answer = vec![total];
        for i in k..nums.len() {
            change(nums[i - k], -1, &mut freq, &mut top, &mut rest, &mut total);
            change(nums[i], 1, &mut freq, &mut top, &mut rest, &mut total);
            answer.push(total);
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
(define/contract (find-x-sum nums k x)
  (-> (listof exact-integer?) exact-integer? exact-integer? (listof exact-integer?))
  (let* ([arr (list->vector nums)]
         [n (vector-length arr)]
         [freq (make-hash)]
         [top (make-hash)]
         [rest (make-hash)]
         [total (box 0)])
    (define (best-entry table)
      (for/fold ([best #f]) ([(value count) (in-hash table)])
        (if (or (not best)
                (> count (cdr best))
                (and (= count (cdr best)) (> value (car best))))
            (cons value count)
            best)))
    (define (worst-entry table)
      (for/fold ([worst #f]) ([(value count) (in-hash table)])
        (if (or (not worst)
                (< count (cdr worst))
                (and (= count (cdr worst)) (< value (car worst))))
            (cons value count)
            worst)))
    (define (change value delta)
      (define old (hash-ref freq value 0))
      (when (> old 0)
        (if (hash-has-key? top value)
            (begin
              (hash-remove! top value)
              (set-box! total (- (unbox total) (* old value))))
            (hash-remove! rest value)))
      (define new (+ old delta))
      (if (> new 0)
          (begin
            (hash-set! freq value new)
            (define worst-top (worst-entry top))
            (if (or (< (hash-count top) x)
                    (and worst-top
                         (or (> new (cdr worst-top))
                             (and (= new (cdr worst-top)) (> value (car worst-top)))))
                    (not worst-top))
                (begin
                  (hash-set! top value new)
                  (set-box! total (+ (unbox total) (* new value))))
                (hash-set! rest value new)))
          (hash-remove! freq value))
      (let loop ()
        (when (> (hash-count top) x)
          (define low (worst-entry top))
          (hash-remove! top (car low))
          (hash-set! rest (car low) (cdr low))
          (set-box! total (- (unbox total) (* (car low) (cdr low))))
          (loop)))
      (let loop ()
        (when (and (< (hash-count top) x) (> (hash-count rest) 0))
          (define high (best-entry rest))
          (hash-remove! rest (car high))
          (hash-set! top (car high) (cdr high))
          (set-box! total (+ (unbox total) (* (car high) (cdr high))))
          (loop)))
      (let loop ()
        (define low (worst-entry top))
        (define high (best-entry rest))
        (when (and low high
                   (or (> (cdr high) (cdr low))
                       (and (= (cdr high) (cdr low)) (> (car high) (car low)))))
          (hash-remove! top (car low))
          (hash-remove! rest (car high))
          (hash-set! top (car high) (cdr high))
          (hash-set! rest (car low) (cdr low))
          (set-box! total (+ (unbox total)
                             (* (car high) (cdr high))
                             (- (* (car low) (cdr low)))))
          (loop))))
    (for ([i (in-range k)])
      (change (vector-ref arr i) 1))
    (define answer (make-vector (+ 1 (- n k))))
    (vector-set! answer 0 (unbox total))
    (for ([i (in-range k n)])
      (change (vector-ref arr (- i k)) -1)
      (change (vector-ref arr i) 1)
      (vector-set! answer (- i k -1) (unbox total)))
    (vector->list answer)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec find_x_sum(Nums :: [integer()], K :: integer(), X :: integer()) -> [integer()].
find_x_sum(Nums, K, X) ->
  Arr = list_to_tuple(Nums),
  N = tuple_size(Arr),
  State0 = {#{}, gb_sets:empty(), gb_sets:empty(), 0},
  State1 = lists:foldl(fun(I, S) -> change(element(I, Arr), 1, X, S) end,
                       State0, lists:seq(1, K)),
  {_, _, _, InitialTotal} = State1,
  Answer0 = [InitialTotal],
  {Answer, _} = lists:foldl(
    fun(I, {Acc, State}) ->
      StateA = change(element(I - K, Arr), -1, X, State),
      StateB = change(element(I, Arr), 1, X, StateA),
      { {element(1, StateB), element(2, StateB), element(3, StateB), Total}, _, _, _} = {StateB, 0, 0, 0},
      { [Total | Acc], StateB }
    end,
    {Answer0, State1},
    lists:seq(K + 1, N)),
  lists:reverse(Answer).

change(Value, Delta, X, {Freq, Top, Rest, Total}) ->
  Old = maps:get(Value, Freq, 0),
  {Top1, Rest1, Total1} = case Old of
    0 -> {Top, Rest, Total};
    _ ->
      Entry = {Old, Value},
      case gb_sets:is_member(Entry, Top) of
        true -> {gb_sets:delete(Entry, Top), Rest, Total - Old * Value};
        false -> {Top, gb_sets:delete(Entry, Rest), Total}
      end
  end,
  New = Old + Delta,
  Freq1 = if New > 0 -> maps:put(Value, New, Freq); true -> maps:remove(Value, Freq) end,
  {Top2, Rest2, Total2} = case New > 0 of
    false -> {Top1, Rest1, Total1};
    true ->
      Entry2 = {New, Value},
      case gb_sets:size(Top1) < X orelse (gb_sets:size(Top1) > 0 andalso Entry2 > gb_sets:smallest(Top1)) of
        true -> {gb_sets:add(Entry2, Top1), Rest1, Total1 + New * Value};
        false -> {Top1, gb_sets:add(Entry2, Rest1), Total1}
      end
  end,
  rebalance(Freq1, Top2, Rest2, Total2, X).

rebalance(Freq, Top, Rest, Total, X) when gb_sets:size(Top) > X ->
  Entry = gb_sets:smallest(Top),
  rebalance(Freq, gb_sets:delete(Entry, Top), gb_sets:add(Entry, Rest),
            Total - element(1, Entry) * element(2, Entry), X);
rebalance(Freq, Top, Rest, Total, X) when gb_sets:size(Top) < X, gb_sets:size(Rest) > 0 ->
  Entry = gb_sets:largest(Rest),
  rebalance(Freq, gb_sets:add(Entry, Top), gb_sets:delete(Entry, Rest),
            Total + element(1, Entry) * element(2, Entry), X);
rebalance(Freq, Top, Rest, Total, X) when gb_sets:size(Top) > 0, gb_sets:size(Rest) > 0 ->
  Low = gb_sets:smallest(Top),
  High = gb_sets:largest(Rest),
  case Low < High of
    true ->
      NewTotal = Total + element(1, High) * element(2, High) - element(1, Low) * element(2, Low),
      rebalance(Freq, gb_sets:add(Low, gb_sets:delete(Low, Top)),
                gb_sets:add(High, gb_sets:delete(High, Rest)), NewTotal, X);
    false -> {Freq, Top, Rest, Total}
  end;
rebalance(Freq, Top, Rest, Total, _) -> {Freq, Top, Rest, Total}.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec find_x_sum(nums :: [integer], k :: integer, x :: integer) :: [integer]
  def find_x_sum(nums, k, x) do
    arr = List.to_tuple(nums)
    n = tuple_size(arr)
    state = { %{}, %{}, %{}, 0 }
    state = Enum.reduce(0..(k - 1), state, fn i, s -> change(elem(arr, i), 1, x, s) end)
    {_, _, _, initial_total} = state
    {answers, _state} =
      Enum.reduce(k..(n - 1), {[initial_total], state}, fn i, {acc, s} ->
        s = change(elem(arr, i - k), -1, x, s)
        s = change(elem(arr, i), 1, x, s)
        {_, _, _, total} = s
        {[total | acc], s}
      end)
    Enum.reverse(answers)
  end

  defp change(value, delta, x, {freq, top, rest, total}) do
    old = Map.get(freq, value, 0)
    {top, rest, total} =
      if old > 0 do
        if Map.has_key?(top, value) do
          {Map.delete(top, value), rest, total - old * value}
        else
          {top, Map.delete(rest, value), total}
        end
      else
        {top, rest, total}
      end

    new = old + delta
    freq = if new > 0, do: Map.put(freq, value, new), else: Map.delete(freq, value)

    {top, rest, total} =
      if new > 0 do
        entry = {new, value}
        worst = worst_entry(top)
        if map_size(top) < x or is_nil(worst) or entry > worst do
          {Map.put(top, value, new), rest, total + new * value}
        else
          {top, Map.put(rest, value, new), total}
        end
      else
        {top, rest, total}
      end

    rebalance(freq, top, rest, total, x)
  end

  defp worst_entry(map) do
    Enum.reduce(map, nil, fn {value, count}, best ->
      entry = {count, value}
      if is_nil(best) or entry < best, do: entry, else: best
    end)
  end

  defp best_entry(map) do
    Enum.reduce(map, nil, fn {value, count}, best ->
      entry = {count, value}
      if is_nil(best) or entry > best, do: entry, else: best
    end)
  end

  defp rebalance(freq, top, rest, total, x) when map_size(top) > x do
    {count, value} = worst_entry(top)
    rebalance(freq, Map.delete(top, value), Map.put(rest, value, count), total - count * value, x)
  end

  defp rebalance(freq, top, rest, total, x) when map_size(top) < x and map_size(rest) > 0 do
    {count, value} = best_entry(rest)
    rebalance(freq, Map.put(top, value, count), Map.delete(rest, value), total + count * value, x)
  end

  defp rebalance(freq, top, rest, total, x) when map_size(top) > 0 and map_size(rest) > 0 do
    {low_count, low_value} = worst_entry(top)
    {high_count, high_value} = best_entry(rest)
    if {high_count, high_value} > {low_count, low_value} do
      top = top |> Map.delete(low_value) |> Map.put(high_value, high_count)
      rest = rest |> Map.delete(high_value) |> Map.put(low_value, low_count)
      rebalance(freq, top, rest,
        total + high_count * high_value - low_count * low_value, x)
    else
      {freq, top, rest, total}
    end
  end

  defp rebalance(freq, top, rest, total, _x), do: {freq, top, rest, total}
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n log n), since each window slide performs a constant number of ordered-set updates and rebalancing operations.
- **Space Complexity:** O(n), for the frequency map and the ordered sets of distinct values in the current window.
