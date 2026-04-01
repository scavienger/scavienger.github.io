---
layout: post
title: "Robot Collisions"
date: 2026-04-01 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Stack", "Sorting", "Simulation"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/robot-collisions/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    vector<int> survivedRobotsHealths(vector<int>&\
        \ positions, vector<int>& healths, string directions) {\n        int n = positions.size();\n\
        \        vector<int> indices(n);\n        for (int i = 0; i < n; ++i) indices[i]\
        \ = i;\n\n        sort(indices.begin(), indices.end(), [&](int a, int b) {\n\
        \            return positions[a] < positions[b];\n        });\n\n        vector<int>\
        \ stack;\n        for (int i : indices) {\n            if (directions[i] ==\
        \ 'R') {\n                stack.push_back(i);\n            } else {\n      \
        \          while (!stack.empty() && healths[i] > 0) {\n                    int\
        \ top = stack.back();\n                    if (healths[top] > healths[i]) {\n\
        \                        healths[top]--;\n                        healths[i]\
        \ = 0;\n                    } else if (healths[top] < healths[i]) {\n      \
        \                  healths[top] = 0;\n                        healths[i]--;\n\
        \                        stack.pop_back();\n                    } else {\n \
        \                       healths[top] = 0;\n                        healths[i]\
        \ = 0;\n                        stack.pop_back();\n                    }\n \
        \               }\n            }\n        }\n\n        vector<int> result;\n\
        \        for (int i = 0; i < n; ++i) {\n            if (healths[i] > 0) {\n\
        \                result.push_back(healths[i]);\n            }\n        }\n \
        \       return result;\n    }\n};"
      java: "import java.util.*;\n\nclass Solution {\n    public List<Integer> survivedRobotsHealths(int[]\
        \ positions, int[] healths, String directions) {\n        int n = positions.length;\n\
        \        Integer[] indices = new Integer[n];\n        for (int i = 0; i < n;\
        \ i++) indices[i] = i;\n\n        Arrays.sort(indices, (a, b) -> Integer.compare(positions[a],\
        \ positions[b]));\n\n        Deque<Integer> stack = new ArrayDeque<>();\n  \
        \      for (int i : indices) {\n            if (directions.charAt(i) == 'R')\
        \ {\n                stack.push(i);\n            } else {\n                while\
        \ (!stack.isEmpty() && healths[i] > 0) {\n                    int topIdx = stack.peek();\n\
        \                    if (healths[topIdx] > healths[i]) {\n                 \
        \       healths[topIdx]--;\n                        healths[i] = 0;\n      \
        \              } else if (healths[topIdx] < healths[i]) {\n                \
        \        healths[topIdx] = 0;\n                        healths[i]--;\n     \
        \                   stack.pop();\n                    } else {\n           \
        \             healths[topIdx] = 0;\n                        healths[i] = 0;\n\
        \                        stack.pop();\n                    }\n             \
        \   }\n            }\n        }\n\n        List<Integer> result = new ArrayList<>();\n\
        \        for (int i = 0; i < n; i++) {\n            if (healths[i] > 0) result.add(healths[i]);\n\
        \        }\n        return result;\n    }\n}"
      python: "class Solution(object):\n    def survivedRobotsHealths(self, positions,\
        \ healths, directions):\n        \"\"\"\n        :type positions: List[int]\n\
        \        :type healths: List[int]\n        :type directions: str\n        :rtype:\
        \ List[int]\n        \"\"\"\n        n = len(positions)\n        indices = sorted(range(n),\
        \ key=lambda i: positions[i])\n        stack = []\n\n        for i in indices:\n\
        \            if directions[i] == 'R':\n                stack.append(i)\n   \
        \         else:\n                while stack and healths[i] > 0:\n         \
        \           top_idx = stack[-1]\n                    if healths[top_idx] > healths[i]:\n\
        \                        healths[top_idx] -= 1\n                        healths[i]\
        \ = 0\n                    elif healths[top_idx] < healths[i]:\n           \
        \             healths[top_idx] = 0\n                        healths[i] -= 1\n\
        \                        stack.pop()\n                    else:\n          \
        \              healths[top_idx] = 0\n                        healths[i] = 0\n\
        \                        stack.pop()\n\n        return [h for h in healths if\
        \ h > 0]"
      python3: "class Solution:\n    def survivedRobotsHealths(self, positions: List[int],\
        \ healths: List[int], directions: str) -> List[int]:\n        n = len(positions)\n\
        \        indices = sorted(range(n), key=lambda i: positions[i])\n        stack\
        \ = []\n\n        for i in indices:\n            if directions[i] == 'R':\n\
        \                stack.append(i)\n            else:\n                while stack\
        \ and healths[i] > 0:\n                    top_idx = stack[-1]\n           \
        \         if healths[top_idx] > healths[i]:\n                        healths[top_idx]\
        \ -= 1\n                        healths[i] = 0\n                    elif healths[top_idx]\
        \ < healths[i]:\n                        healths[top_idx] = 0\n            \
        \            healths[i] -= 1\n                        stack.pop()\n        \
        \            else:\n                        healths[top_idx] = 0\n         \
        \               healths[i] = 0\n                        stack.pop()\n\n    \
        \    return [h for h in healths if h > 0]"
      c: "#include <stdlib.h>\n#include <string.h>\n\ntypedef struct {\n    int pos;\n\
        \    int id;\n} Robot;\n\nint compareRobots(const void* a, const void* b) {\n\
        \    Robot* r1 = (Robot*)a;\n    Robot* r2 = (Robot*)b;\n    return (r1->pos\
        \ > r2->pos) - (r1->pos < r2->pos);\n}\n\nint* survivedRobotsHealths(int* positions,\
        \ int positionsSize, int* healths, int healthsSize, char* directions, int* returnSize)\
        \ {\n    int n = positionsSize;\n    Robot* robots = (Robot*)malloc(sizeof(Robot)\
        \ * n);\n    for (int i = 0; i < n; i++) {\n        robots[i].pos = positions[i];\n\
        \        robots[i].id = i;\n    }\n    qsort(robots, n, sizeof(Robot), compareRobots);\n\
        \n    int* stack = (int*)malloc(sizeof(int) * n);\n    int top = -1;\n\n   \
        \ for (int j = 0; j < n; j++) {\n        int i = robots[j].id;\n        if (directions[i]\
        \ == 'R') {\n            stack[++top] = i;\n        } else {\n            while\
        \ (top >= 0 && healths[i] > 0) {\n                int topIdx = stack[top];\n\
        \                if (healths[topIdx] > healths[i]) {\n                    healths[topIdx]--;\n\
        \                    healths[i] = 0;\n                } else if (healths[topIdx]\
        \ < healths[i]) {\n                    healths[topIdx] = 0;\n              \
        \      healths[i]--;\n                    top--;\n                } else {\n\
        \                    healths[topIdx] = 0;\n                    healths[i] =\
        \ 0;\n                    top--;\n                }\n            }\n       \
        \ }\n    }\n\n    int count = 0;\n    for (int i = 0; i < n; i++) {\n      \
        \  if (healths[i] > 0) count++;\n    }\n\n    int* result = (count > 0) ? (int*)malloc(sizeof(int)\
        \ * count) : NULL;\n    int idx = 0;\n    for (int i = 0; i < n; i++) {\n  \
        \      if (healths[i] > 0) result[idx++] = healths[i];\n    }\n\n    *returnSize\
        \ = count;\n    free(robots);\n    free(stack);\n    return result;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\n\npublic class Solution\
        \ {\n    public IList<int> SurvivedRobotsHealths(int[] positions, int[] healths,\
        \ string directions) {\n        int n = positions.Length;\n        int[] indices\
        \ = new int[n];\n        for (int i = 0; i < n; i++) indices[i] = i;\n\n   \
        \     Array.Sort(indices, (a, b) => positions[a].CompareTo(positions[b]));\n\
        \n        Stack<int> stack = new Stack<int>();\n        foreach (int i in indices)\
        \ {\n            if (directions[i] == 'R') {\n                stack.Push(i);\n\
        \            } else {\n                while (stack.Count > 0 && healths[i]\
        \ > 0) {\n                    int topIdx = stack.Peek();\n                 \
        \   if (healths[topIdx] > healths[i]) {\n                        healths[topIdx]--;\n\
        \                        healths[i] = 0;\n                    } else if (healths[topIdx]\
        \ < healths[i]) {\n                        healths[topIdx] = 0;\n          \
        \              healths[i]--;\n                        stack.Pop();\n       \
        \             } else {\n                        healths[topIdx] = 0;\n     \
        \                   healths[i] = 0;\n                        stack.Pop();\n\
        \                    }\n                }\n            }\n        }\n\n    \
        \    List<int> result = new List<int>();\n        for (int i = 0; i < n; i++)\
        \ {\n            if (healths[i] > 0) result.Add(healths[i]);\n        }\n  \
        \      return result;\n    }\n}"
      javascript: "/**\n * @param {number[]} positions\n * @param {number[]} healths\n\
        \ * @param {string} directions\n * @return {number[]}\n */\nvar survivedRobotsHealths\
        \ = function(positions, healths, directions) {\n    const n = positions.length;\n\
        \    const indices = Array.from({ length: n }, (_, i) => i);\n    indices.sort((a,\
        \ b) => positions[a] - positions[b]);\n\n    const stack = [];\n    for (const\
        \ i of indices) {\n        if (directions[i] === 'R') {\n            stack.push(i);\n\
        \        } else {\n            while (stack.length > 0 && healths[i] > 0) {\n\
        \                const topIdx = stack[stack.length - 1];\n                if\
        \ (healths[topIdx] > healths[i]) {\n                    healths[topIdx]--;\n\
        \                    healths[i] = 0;\n                } else if (healths[topIdx]\
        \ < healths[i]) {\n                    healths[topIdx] = 0;\n              \
        \      healths[i]--;\n                    stack.pop();\n                } else\
        \ {\n                    healths[topIdx] = 0;\n                    healths[i]\
        \ = 0;\n                    stack.pop();\n                }\n            }\n\
        \        }\n    }\n\n    const result = [];\n    for (let i = 0; i < n; i++)\
        \ {\n        if (healths[i] > 0) result.push(healths[i]);\n    }\n    return\
        \ result;\n};"
      typescript: "function survivedRobotsHealths(positions: number[], healths: number[],\
        \ directions: string): number[] {\n    const n = positions.length;\n    const\
        \ indices = Array.from({ length: n }, (_, i) => i);\n    indices.sort((a, b)\
        \ => positions[a] - positions[b]);\n\n    const h = [...healths];\n    const\
        \ stack: number[] = [];\n\n    for (const i of indices) {\n        if (directions[i]\
        \ === 'R') {\n            stack.push(i);\n        } else {\n            while\
        \ (stack.length > 0 && h[i] > 0) {\n                const topIdx = stack[stack.length\
        \ - 1];\n                if (h[i] > h[topIdx]) {\n                    h[i] -=\
        \ 1;\n                    h[topIdx] = 0;\n                    stack.pop();\n\
        \                } else if (h[i] < h[topIdx]) {\n                    h[topIdx]\
        \ -= 1;\n                    h[i] = 0;\n                } else {\n         \
        \           h[i] = 0;\n                    h[topIdx] = 0;\n                \
        \    stack.pop();\n                }\n            }\n        }\n    }\n\n  \
        \  return h.filter(health => health > 0);\n}"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $positions\n     *\
        \ @param Integer[] $healths\n     * @param String $directions\n     * @return\
        \ Integer[]\n     */\n    function survivedRobotsHealths($positions, $healths,\
        \ $directions) {\n        $n = count($positions);\n        $indices = range(0,\
        \ $n - 1);\n        usort($indices, function($a, $b) use ($positions) {\n  \
        \          return $positions[$a] <=> $positions[$b];\n        });\n\n      \
        \  $h = $healths;\n        $stack = [];\n\n        foreach ($indices as $i)\
        \ {\n            if ($directions[$i] === 'R') {\n                $stack[] =\
        \ $i;\n            } else {\n                while (!empty($stack) && $h[$i]\
        \ > 0) {\n                    $topIdx = $stack[count($stack) - 1];\n       \
        \             if ($h[$i] > $h[$topIdx]) {\n                        $h[$i]--;\n\
        \                        $h[$topIdx] = 0;\n                        array_pop($stack);\n\
        \                    } elseif ($h[$i] < $h[$topIdx]) {\n                   \
        \     $h[$topIdx]--;\n                        $h[$i] = 0;\n                \
        \    } else {\n                        $h[$i] = 0;\n                       \
        \ $h[$topIdx] = 0;\n                        array_pop($stack);\n           \
        \         }\n                }\n            }\n        }\n\n        $result\
        \ = [];\n        for ($i = 0; $i < $n; $i++) {\n            if ($h[$i] > 0)\
        \ {\n                $result[] = $h[$i];\n            }\n        }\n       \
        \ return $result;\n    }\n}"
      swift: "class Solution {\n    func survivedRobotsHealths(_ positions: [Int], _\
        \ healths: [Int], _ directions: String) -> [Int] {\n        let n = positions.count\n\
        \        var h = healths\n        var indices = Array(0..<n)\n        indices.sort\
        \ { positions[$0] < positions[$1] }\n\n        let directionsArray = Array(directions)\n\
        \        var stack = [Int]()\n\n        for i in indices {\n            if directionsArray[i]\
        \ == \"R\" {\n                stack.append(i)\n            } else {\n      \
        \          while !stack.isEmpty && h[i] > 0 {\n                    let topIdx\
        \ = stack.last!\n                    if h[i] > h[topIdx] {\n               \
        \         h[i] -= 1\n                        h[topIdx] = 0\n               \
        \         stack.removeLast()\n                    } else if h[i] < h[topIdx]\
        \ {\n                        h[topIdx] -= 1\n                        h[i] =\
        \ 0\n                    } else {\n                        h[i] = 0\n      \
        \                  h[topIdx] = 0\n                        stack.removeLast()\n\
        \                    }\n                }\n            }\n        }\n\n    \
        \    return h.filter { $0 > 0 }\n    }\n}"
      kotlin: "import java.util.ArrayDeque\n\nclass Solution {\n    fun survivedRobotsHealths(positions:\
        \ IntArray, healths: IntArray, directions: String): List<Int> {\n        val\
        \ n = positions.size\n        val indices = Array(n) { it }\n        indices.sortBy\
        \ { positions[it] }\n\n        val h = healths.copyOf()\n        val stack =\
        \ ArrayDeque<Int>()\n\n        for (i in indices) {\n            if (directions[i]\
        \ == 'R') {\n                stack.push(i)\n            } else {\n         \
        \       while (stack.isNotEmpty() && h[i] > 0) {\n                    val topIdx\
        \ = stack.peek()\n                    if (h[i] > h[topIdx]) {\n            \
        \            h[i]--\n                        h[topIdx] = 0\n               \
        \         stack.pop()\n                    } else if (h[i] < h[topIdx]) {\n\
        \                        h[topIdx]--\n                        h[i] = 0\n   \
        \                 } else {\n                        h[i] = 0\n             \
        \           h[topIdx] = 0\n                        stack.pop()\n           \
        \         }\n                }\n            }\n        }\n\n        val result\
        \ = mutableListOf<Int>()\n        for (v in h) {\n            if (v > 0) result.add(v)\n\
        \        }\n        return result\n    }\n}"
      dart: "class Solution {\n  List<int> survivedRobotsHealths(List<int> positions,\
        \ List<int> healths, String directions) {\n    int n = positions.length;\n \
        \   List<int> indices = List.generate(n, (i) => i);\n    indices.sort((a, b)\
        \ => positions[a].compareTo(positions[b]));\n\n    List<int> h = List.from(healths);\n\
        \    List<int> stack = [];\n\n    for (int i in indices) {\n      if (directions[i]\
        \ == 'R') {\n        stack.add(i);\n      } else {\n        while (stack.isNotEmpty\
        \ && h[i] > 0) {\n          int topIdx = stack.last;\n          if (h[i] > h[topIdx])\
        \ {\n            h[i]--;\n            h[topIdx] = 0;\n            stack.removeLast();\n\
        \          } else if (h[i] < h[topIdx]) {\n            h[topIdx]--;\n      \
        \      h[i] = 0;\n          } else {\n            h[i] = 0;\n            h[topIdx]\
        \ = 0;\n            stack.removeLast();\n          }\n        }\n      }\n \
        \   }\n\n    List<int> result = [];\n    for (int v in h) {\n      if (v > 0)\
        \ result.add(v);\n    }\n    return result;\n  }\n}"
      go: "import (\n\t\"sort\"\n)\n\nfunc survivedRobotsHealths(positions []int, healths\
        \ []int, directions string) []int {\n\tn := len(positions)\n\tindices := make([]int,\
        \ n)\n\tfor i := range indices {\n\t\tindices[i] = i\n\t}\n\tsort.Slice(indices,\
        \ func(i, j int) bool {\n\t\treturn positions[indices[i]] < positions[indices[j]]\n\
        \t})\n\n\th := make([]int, n)\n\tcopy(h, healths)\n\tstack := []int{}\n\n\t\
        for _, i := range indices {\n\t\tif directions[i] == 'R' {\n\t\t\tstack = append(stack,\
        \ i)\n\t\t} else {\n\t\t\tfor len(stack) > 0 && h[i] > 0 {\n\t\t\t\ttopIdx :=\
        \ stack[len(stack)-1]\n\t\t\t\tif h[i] > h[topIdx] {\n\t\t\t\t\th[i]--\n\t\t\
        \t\t\th[topIdx] = 0\n\t\t\t\t\tstack = stack[:len(stack)-1]\n\t\t\t\t} else\
        \ if h[i] < h[topIdx] {\n\t\t\t\t\th[topIdx]--\n\t\t\t\t\th[i] = 0\n\t\t\t\t\
        } else {\n\t\t\t\t\th[i] = 0\n\t\t\t\t\th[topIdx] = 0\n\t\t\t\t\tstack = stack[:len(stack)-1]\n\
        \t\t\t\t}\n\t\t\t}\n\t\t}\n\t}\n\n\tresult := []int{}\n\tfor _, val := range\
        \ h {\n\t\tif val > 0 {\n\t\t\tresult = append(result, val)\n\t\t}\n\t}\n\t\
        return result\n}"
      ruby: "def survived_robots_healths(positions, healths, directions)\n  n = positions.size\n\
        \  indices = (0...n).to_a.sort_by { |i| positions[i] }\n  stack = []\n\n  indices.each\
        \ do |i|\n    if directions[i] == 'R'\n      stack << i\n    else\n      while\
        \ !stack.empty? && healths[i] > 0\n        top = stack.last\n        if healths[i]\
        \ > healths[top]\n          healths[top] = 0\n          healths[i] -= 1\n  \
        \        stack.pop\n        elsif healths[i] < healths[top]\n          healths[top]\
        \ -= 1\n          healths[i] = 0\n        else\n          healths[top] = 0\n\
        \          healths[i] = 0\n          stack.pop\n        end\n      end\n   \
        \ end\n  end\n  healths.reject { |h| h == 0 }\nend"
      scala: "import scala.collection.mutable\n\nobject Solution {\n  def survivedRobotsHealths(positions:\
        \ Array[Int], healths: Array[Int], directions: String): List[Int] = {\n    val\
        \ n = positions.length\n    val indices = (0 until n).toArray.sortBy(positions)\n\
        \    val stack = mutable.Stack[Int]()\n    val h = healths.clone()\n\n    for\
        \ (i <- indices) {\n      if (directions(i) == 'R') {\n        stack.push(i)\n\
        \      } else {\n        while (stack.nonEmpty && h(i) > 0) {\n          val\
        \ top = stack.top\n          if (h(i) > h(top)) {\n            h(top) = 0\n\
        \            h(i) = h(i) - 1\n            stack.pop()\n          } else if (h(i)\
        \ < h(top)) {\n            h(top) = h(top) - 1\n            h(i) = 0\n     \
        \     } else {\n            h(top) = 0\n            h(i) = 0\n            stack.pop()\n\
        \          }\n        }\n      }\n    }\n    h.filter(_ > 0).toList\n  }\n}"
      rust: "impl Solution {\n    pub fn survived_robots_healths(positions: Vec<i32>,\
        \ healths: Vec<i32>, directions: String) -> Vec<i32> {\n        let n = positions.len();\n\
        \        let mut h = healths;\n        let mut indices: Vec<usize> = (0..n).collect();\n\
        \        indices.sort_by_key(|&i| positions[i]);\n        let dir_bytes = directions.as_bytes();\n\
        \        let mut stack: Vec<usize> = Vec::new();\n\n        for &i in &indices\
        \ {\n            if dir_bytes[i] == b'R' {\n                stack.push(i);\n\
        \            } else {\n                while let Some(&top) = stack.last() {\n\
        \                    if h[i] > h[top] {\n                        h[top] = 0;\n\
        \                        h[i] -= 1;\n                        stack.pop();\n\
        \                    } else if h[i] < h[top] {\n                        h[top]\
        \ -= 1;\n                        h[i] = 0;\n                        break;\n\
        \                    } else {\n                        h[i] = 0;\n         \
        \               h[top] = 0;\n                        stack.pop();\n        \
        \                break;\n                    }\n                }\n        \
        \    }\n        }\n        h.into_iter().filter(|&val| val > 0).collect()\n\
        \    }\n}"
      racket: "(define/contract (survived-robots-healths positions healths directions)\n\
        \  (-> (listof exact-integer?) (listof exact-integer?) string? (listof exact-integer?))\n\
        \  (let* ([n (length positions)]\n         [pos-vec (list->vector positions)]\n\
        \         [health-vec (list->vector healths)]\n         [dir-vec (string->vector\
        \ directions)]\n         [indices (sort (range n) < #:key (lambda (i) (vector-ref\
        \ pos-vec i)))]\n         [stack '()])\n    (for ([i indices])\n      (if (char=?\
        \ (vector-ref dir-vec i) #\\R)\n          (set! stack (cons i stack))\n    \
        \      (let loop ()\n            (when (and (not (null? stack)) (> (vector-ref\
        \ health-vec i) 0))\n              (let* ([top (car stack)]\n              \
        \       [h-i (vector-ref health-vec i)]\n                     [h-top (vector-ref\
        \ health-vec top)])\n                (cond\n                  [(> h-i h-top)\n\
        \                   (vector-set! health-vec top 0)\n                   (vector-set!\
        \ health-vec i (- h-i 1))\n                   (set! stack (cdr stack))\n   \
        \                (loop)]\n                  [(< h-i h-top)\n               \
        \    (vector-set! health-vec top (- h-top 1))\n                   (vector-set!\
        \ health-vec i 0)]\n                  [else\n                   (vector-set!\
        \ health-vec top 0)\n                   (vector-set! health-vec i 0)\n     \
        \              (set! stack (cdr stack))]))))))\n    (filter (lambda (h) (> h\
        \ 0)) (vector->list health-vec))))"
      erlang: "-spec survived_robots_healths(Positions :: [integer()], Healths :: [integer()],\
        \ Directions :: unicode:unicode_binary()) -> [integer()].\nsurvived_robots_healths(Positions,\
        \ Healths, Directions) ->\n  N = length(Positions),\n  DirList = binary_to_list(Directions),\n\
        \  IndexedPos = lists:zip(lists:seq(0, N - 1), Positions),\n  SortedIndices\
        \ = [I || {I, _P} <- lists:keysort(2, IndexedPos)],\n  HealthMap = maps:from_list(lists:zip(lists:seq(0,\
        \ N - 1), Healths)),\n  DirVec = list_to_tuple(DirList),\n  FinalHealthMap =\
        \ process_robots(SortedIndices, [], HealthMap, DirVec),\n  [maps:get(I, FinalHealthMap)\
        \ || I <- lists:seq(0, N - 1), maps:get(I, FinalHealthMap) > 0].\n\nprocess_robots([],\
        \ _Stack, HealthMap, _DirVec) -> HealthMap;\nprocess_robots([I | Rest], Stack,\
        \ HealthMap, DirVec) ->\n  case element(I + 1, DirVec) of\n    $R -> process_robots(Rest,\
        \ [I | Stack], HealthMap, DirVec);\n    $L -> {NewStack, NewHealthMap} = collide(I,\
        \ Stack, HealthMap),\n          process_robots(Rest, NewStack, NewHealthMap,\
        \ DirVec)\n  end.\n\ncollide(I, [], HealthMap) -> {[], HealthMap};\ncollide(I,\
        \ [Top | Rest] = Stack, HealthMap) ->\n  HI = maps:get(I, HealthMap),\n  HTop\
        \ = maps:get(Top, HealthMap),\n  if\n    HI > HTop -> collide(I, Rest, maps:put(I,\
        \ HI - 1, maps:put(Top, 0, HealthMap)));\n    HI < HTop -> {Stack, maps:put(Top,\
        \ HTop - 1, maps:put(I, 0, HealthMap))};\n    true -> {Rest, maps:put(Top, 0,\
        \ maps:put(I, 0, HealthMap))}\n  end."
      elixir: "defmodule Solution do\n  @spec survived_robots_healths(positions :: [integer],\
        \ healths :: [integer], directions :: String.t) :: [integer]\n  def survived_robots_healths(positions,\
        \ healths, directions) do\n    n = length(positions)\n    dir_list = String.to_charlist(directions)\n\
        \    indexed_positions = Enum.with_index(positions) |> Enum.sort_by(fn {p, _i}\
        \ -> p end)\n    sorted_indices = Enum.map(indexed_positions, fn {_p, i} ->\
        \ i end)\n    health_map = Enum.with_index(healths) |> Enum.map(fn {h, i} ->\
        \ {i, h} end) |> Map.new()\n    dir_map = Enum.with_index(dir_list) |> Enum.map(fn\
        \ {d, i} -> {i, d} end) |> Map.new()\n    final_health_map = process_robots(sorted_indices,\
        \ [], health_map, dir_map)\n    0..(n-1)\n    |> Enum.map(fn i -> Map.get(final_health_map,\
        \ i) end)\n    |> Enum.filter(fn h -> h > 0 end)\n  end\n\n  defp process_robots([],\
        \ _stack, health_map, _dir_map), do: health_map\n  defp process_robots([i |\
        \ rest], stack, health_map, dir_map) do\n    if Map.get(dir_map, i) == ?R do\n\
        \      process_robots(rest, [i | stack], health_map, dir_map)\n    else\n  \
        \    {new_stack, new_health_map} = collide(i, stack, health_map)\n      process_robots(rest,\
        \ new_stack, new_health_map, dir_map)\n    end\n  end\n\n  defp collide(i, [],\
        \ health_map), do: {[], health_map}\n  defp collide(i, [top | rest] = stack,\
        \ health_map) do\n    h_i = Map.get(health_map, i)\n    h_top = Map.get(health_map,\
        \ top)\n    cond do\n      h_i > h_top -> collide(i, rest, health_map |> Map.put(top,\
        \ 0) |> Map.put(i, h_i - 1))\n      h_i < h_top -> {stack, health_map |> Map.put(i,\
        \ 0) |> Map.put(top, h_top - 1)}\n      true -> {rest, health_map |> Map.put(i,\
        \ 0) |> Map.put(top, 0)}\n    end\n  end\nend"
    approach: 'To handle robot collisions efficiently, we first sort the robots by their
      initial positions. Since all robots move simultaneously at the same speed, a collision
      can only occur between a robot moving to the right (''R'') and a robot to its
      right moving to the left (''L''). By processing robots in sorted order of their
      positions, we can use a stack to manage potential collisions. The stack stores
      the indices of robots moving to the right. When we encounter a robot moving to
      the left, it will potentially collide with the right-moving robots currently in
      the stack, starting with the one closest to it (the top of the stack).


      When a collision occurs, we compare the health values of the two robots. The robot
      with lower health is destroyed (removed from consideration), and the health of
      the survivor is decremented by one. If both robots have equal health, both are
      destroyed. A surviving left-moving robot continues to collide with the next right-moving
      robot on the stack until its health reaches zero or no right-moving robots remain.
      After processing all robots, the survivors are those whose health remains greater
      than zero. We then collect and return these health values in their original input
      order.'
    time_complexity: O(N log N), where N is the number of robots. This is dominated
      by the sorting step required to process robots by their initial positions. The
      collision simulation using a stack takes O(N) time because each robot index is
      pushed onto and popped from the stack at most once.
    space_complexity: O(N), as we need extra space for storing metadata (indices and
      positions) for sorting, a stack for right-moving robots, and the resulting list
      of survivor healths.
    elapsed_time: 234.9857199192047
    model: gemini-3-flash-preview
    generated_at: '2026-04-01 03:17:33 '
---

## Problem #2751: Robot Collisions

**Difficulty:** Hard

**Topics:** Array, Stack, Sorting, Simulation

## Problem Description

<p>There are <code>n</code> <strong>1-indexed</strong> robots, each having a position on a line, health, and movement direction.</p>

<p>You are given <strong>0-indexed</strong> integer arrays <code>positions</code>, <code>healths</code>, and a string <code>directions</code> (<code>directions[i]</code> is either <strong>&#39;L&#39;</strong> for <strong>left</strong> or <strong>&#39;R&#39;</strong> for <strong>right</strong>). All integers in <code>positions</code> are <strong>unique</strong>.</p>

<p>All robots start moving on the line<strong> simultaneously</strong> at the <strong>same speed </strong>in their given directions. If two robots ever share the same position while moving, they will <strong>collide</strong>.</p>

<p>If two robots collide, the robot with <strong>lower health</strong> is <strong>removed</strong> from the line, and the health of the other robot <strong>decreases</strong> <strong>by one</strong>. The surviving robot continues in the <strong>same</strong> direction it was going. If both robots have the <strong>same</strong> health, they are both<strong> </strong>removed from the line.</p>

<p>Your task is to determine the <strong>health</strong> of the robots that survive the collisions, in the same <strong>order </strong>that the robots were given,<strong> </strong>i.e. final health of robot 1 (if survived), final health of robot 2 (if survived), and so on. If there are no survivors, return an empty array.</p>

<p>Return <em>an array containing the health of the remaining robots (in the order they were given in the input), after no further collisions can occur.</em></p>

<p><strong>Note:</strong> The positions may be unsorted.</p>

<div class="notranslate" style="all: initial;">&nbsp;</div>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<p><img height="169" src="https://assets.leetcode.com/uploads/2023/05/15/image-20230516011718-12.png" width="808" /></p>

<pre>
<strong>Input:</strong> positions = [5,4,3,2,1], healths = [2,17,9,15,10], directions = &quot;RRRRR&quot;
<strong>Output:</strong> [2,17,9,15,10]
<strong>Explanation:</strong> No collision occurs in this example, since all robots are moving in the same direction. So, the health of the robots in order from the first robot is returned, [2, 17, 9, 15, 10].
</pre>

<p><strong class="example">Example 2:</strong></p>

<p><img height="176" src="https://assets.leetcode.com/uploads/2023/05/15/image-20230516004433-7.png" width="717" /></p>

<pre>
<strong>Input:</strong> positions = [3,5,2,6], healths = [10,10,15,12], directions = &quot;RLRL&quot;
<strong>Output:</strong> [14]
<strong>Explanation:</strong> There are 2 collisions in this example. Firstly, robot 1 and robot 2 will collide, and since both have the same health, they will be removed from the line. Next, robot 3 and robot 4 will collide and since robot 4&#39;s health is smaller, it gets removed, and robot 3&#39;s health becomes 15 - 1 = 14. Only robot 3 remains, so we return [14].
</pre>

<p><strong class="example">Example 3:</strong></p>

<p><img height="172" src="https://assets.leetcode.com/uploads/2023/05/15/image-20230516005114-9.png" width="732" /></p>

<pre>
<strong>Input:</strong> positions = [1,2,5,6], healths = [10,10,11,11], directions = &quot;RLRL&quot;
<strong>Output:</strong> []
<strong>Explanation:</strong> Robot 1 and robot 2 will collide and since both have the same health, they are both removed. Robot 3 and 4 will collide and since both have the same health, they are both removed. So, we return an empty array, [].</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= positions.length == healths.length == directions.length == n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= positions[i], healths[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>directions[i] == &#39;L&#39;</code> or <code>directions[i] == &#39;R&#39;</code></li>
	<li>All values in <code>positions</code> are distinct</li>
</ul>


## Hints

1. Process the robots in the order of their positions to ensure that we process the collisions correctly.

2. To optimize the solution, use a stack to keep track of the surviving robots as we iterate through the positions.

3. Instead of simulating each collision, check the current robot against the top of the stack (if it exists) to determine if a collision occurs.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To handle robot collisions efficiently, we first sort the robots by their initial positions. Since all robots move simultaneously at the same speed, a collision can only occur between a robot moving to the right ('R') and a robot to its right moving to the left ('L'). By processing robots in sorted order of their positions, we can use a stack to manage potential collisions. The stack stores the indices of robots moving to the right. When we encounter a robot moving to the left, it will potentially collide with the right-moving robots currently in the stack, starting with the one closest to it (the top of the stack).

When a collision occurs, we compare the health values of the two robots. The robot with lower health is destroyed (removed from consideration), and the health of the survivor is decremented by one. If both robots have equal health, both are destroyed. A surviving left-moving robot continues to collide with the next right-moving robot on the stack until its health reaches zero or no right-moving robots remain. After processing all robots, the survivors are those whose health remains greater than zero. We then collect and return these health values in their original input order.

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
    vector<int> survivedRobotsHealths(vector<int>& positions, vector<int>& healths, string directions) {
        int n = positions.size();
        vector<int> indices(n);
        for (int i = 0; i < n; ++i) indices[i] = i;

        sort(indices.begin(), indices.end(), [&](int a, int b) {
            return positions[a] < positions[b];
        });

        vector<int> stack;
        for (int i : indices) {
            if (directions[i] == 'R') {
                stack.push_back(i);
            } else {
                while (!stack.empty() && healths[i] > 0) {
                    int top = stack.back();
                    if (healths[top] > healths[i]) {
                        healths[top]--;
                        healths[i] = 0;
                    } else if (healths[top] < healths[i]) {
                        healths[top] = 0;
                        healths[i]--;
                        stack.pop_back();
                    } else {
                        healths[top] = 0;
                        healths[i] = 0;
                        stack.pop_back();
                    }
                }
            }
        }

        vector<int> result;
        for (int i = 0; i < n; ++i) {
            if (healths[i] > 0) {
                result.push_back(healths[i]);
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

class Solution {
    public List<Integer> survivedRobotsHealths(int[] positions, int[] healths, String directions) {
        int n = positions.length;
        Integer[] indices = new Integer[n];
        for (int i = 0; i < n; i++) indices[i] = i;

        Arrays.sort(indices, (a, b) -> Integer.compare(positions[a], positions[b]));

        Deque<Integer> stack = new ArrayDeque<>();
        for (int i : indices) {
            if (directions.charAt(i) == 'R') {
                stack.push(i);
            } else {
                while (!stack.isEmpty() && healths[i] > 0) {
                    int topIdx = stack.peek();
                    if (healths[topIdx] > healths[i]) {
                        healths[topIdx]--;
                        healths[i] = 0;
                    } else if (healths[topIdx] < healths[i]) {
                        healths[topIdx] = 0;
                        healths[i]--;
                        stack.pop();
                    } else {
                        healths[topIdx] = 0;
                        healths[i] = 0;
                        stack.pop();
                    }
                }
            }
        }

        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (healths[i] > 0) result.add(healths[i]);
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
    def survivedRobotsHealths(self, positions, healths, directions):
        """
        :type positions: List[int]
        :type healths: List[int]
        :type directions: str
        :rtype: List[int]
        """
        n = len(positions)
        indices = sorted(range(n), key=lambda i: positions[i])
        stack = []

        for i in indices:
            if directions[i] == 'R':
                stack.append(i)
            else:
                while stack and healths[i] > 0:
                    top_idx = stack[-1]
                    if healths[top_idx] > healths[i]:
                        healths[top_idx] -= 1
                        healths[i] = 0
                    elif healths[top_idx] < healths[i]:
                        healths[top_idx] = 0
                        healths[i] -= 1
                        stack.pop()
                    else:
                        healths[top_idx] = 0
                        healths[i] = 0
                        stack.pop()

        return [h for h in healths if h > 0]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        indices = sorted(range(n), key=lambda i: positions[i])
        stack = []

        for i in indices:
            if directions[i] == 'R':
                stack.append(i)
            else:
                while stack and healths[i] > 0:
                    top_idx = stack[-1]
                    if healths[top_idx] > healths[i]:
                        healths[top_idx] -= 1
                        healths[i] = 0
                    elif healths[top_idx] < healths[i]:
                        healths[top_idx] = 0
                        healths[i] -= 1
                        stack.pop()
                    else:
                        healths[top_idx] = 0
                        healths[i] = 0
                        stack.pop()

        return [h for h in healths if h > 0]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <string.h>

typedef struct {
    int pos;
    int id;
} Robot;

int compareRobots(const void* a, const void* b) {
    Robot* r1 = (Robot*)a;
    Robot* r2 = (Robot*)b;
    return (r1->pos > r2->pos) - (r1->pos < r2->pos);
}

int* survivedRobotsHealths(int* positions, int positionsSize, int* healths, int healthsSize, char* directions, int* returnSize) {
    int n = positionsSize;
    Robot* robots = (Robot*)malloc(sizeof(Robot) * n);
    for (int i = 0; i < n; i++) {
        robots[i].pos = positions[i];
        robots[i].id = i;
    }
    qsort(robots, n, sizeof(Robot), compareRobots);

    int* stack = (int*)malloc(sizeof(int) * n);
    int top = -1;

    for (int j = 0; j < n; j++) {
        int i = robots[j].id;
        if (directions[i] == 'R') {
            stack[++top] = i;
        } else {
            while (top >= 0 && healths[i] > 0) {
                int topIdx = stack[top];
                if (healths[topIdx] > healths[i]) {
                    healths[topIdx]--;
                    healths[i] = 0;
                } else if (healths[topIdx] < healths[i]) {
                    healths[topIdx] = 0;
                    healths[i]--;
                    top--;
                } else {
                    healths[topIdx] = 0;
                    healths[i] = 0;
                    top--;
                }
            }
        }
    }

    int count = 0;
    for (int i = 0; i < n; i++) {
        if (healths[i] > 0) count++;
    }

    int* result = (count > 0) ? (int*)malloc(sizeof(int) * count) : NULL;
    int idx = 0;
    for (int i = 0; i < n; i++) {
        if (healths[i] > 0) result[idx++] = healths[i];
    }

    *returnSize = count;
    free(robots);
    free(stack);
    return result;
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
    public IList<int> SurvivedRobotsHealths(int[] positions, int[] healths, string directions) {
        int n = positions.Length;
        int[] indices = new int[n];
        for (int i = 0; i < n; i++) indices[i] = i;

        Array.Sort(indices, (a, b) => positions[a].CompareTo(positions[b]));

        Stack<int> stack = new Stack<int>();
        foreach (int i in indices) {
            if (directions[i] == 'R') {
                stack.Push(i);
            } else {
                while (stack.Count > 0 && healths[i] > 0) {
                    int topIdx = stack.Peek();
                    if (healths[topIdx] > healths[i]) {
                        healths[topIdx]--;
                        healths[i] = 0;
                    } else if (healths[topIdx] < healths[i]) {
                        healths[topIdx] = 0;
                        healths[i]--;
                        stack.Pop();
                    } else {
                        healths[topIdx] = 0;
                        healths[i] = 0;
                        stack.Pop();
                    }
                }
            }
        }

        List<int> result = new List<int>();
        for (int i = 0; i < n; i++) {
            if (healths[i] > 0) result.Add(healths[i]);
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
 * @param {number[]} positions
 * @param {number[]} healths
 * @param {string} directions
 * @return {number[]}
 */
var survivedRobotsHealths = function(positions, healths, directions) {
    const n = positions.length;
    const indices = Array.from({ length: n }, (_, i) => i);
    indices.sort((a, b) => positions[a] - positions[b]);

    const stack = [];
    for (const i of indices) {
        if (directions[i] === 'R') {
            stack.push(i);
        } else {
            while (stack.length > 0 && healths[i] > 0) {
                const topIdx = stack[stack.length - 1];
                if (healths[topIdx] > healths[i]) {
                    healths[topIdx]--;
                    healths[i] = 0;
                } else if (healths[topIdx] < healths[i]) {
                    healths[topIdx] = 0;
                    healths[i]--;
                    stack.pop();
                } else {
                    healths[topIdx] = 0;
                    healths[i] = 0;
                    stack.pop();
                }
            }
        }
    }

    const result = [];
    for (let i = 0; i < n; i++) {
        if (healths[i] > 0) result.push(healths[i]);
    }
    return result;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function survivedRobotsHealths(positions: number[], healths: number[], directions: string): number[] {
    const n = positions.length;
    const indices = Array.from({ length: n }, (_, i) => i);
    indices.sort((a, b) => positions[a] - positions[b]);

    const h = [...healths];
    const stack: number[] = [];

    for (const i of indices) {
        if (directions[i] === 'R') {
            stack.push(i);
        } else {
            while (stack.length > 0 && h[i] > 0) {
                const topIdx = stack[stack.length - 1];
                if (h[i] > h[topIdx]) {
                    h[i] -= 1;
                    h[topIdx] = 0;
                    stack.pop();
                } else if (h[i] < h[topIdx]) {
                    h[topIdx] -= 1;
                    h[i] = 0;
                } else {
                    h[i] = 0;
                    h[topIdx] = 0;
                    stack.pop();
                }
            }
        }
    }

    return h.filter(health => health > 0);
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[] $positions
     * @param Integer[] $healths
     * @param String $directions
     * @return Integer[]
     */
    function survivedRobotsHealths($positions, $healths, $directions) {
        $n = count($positions);
        $indices = range(0, $n - 1);
        usort($indices, function($a, $b) use ($positions) {
            return $positions[$a] <=> $positions[$b];
        });

        $h = $healths;
        $stack = [];

        foreach ($indices as $i) {
            if ($directions[$i] === 'R') {
                $stack[] = $i;
            } else {
                while (!empty($stack) && $h[$i] > 0) {
                    $topIdx = $stack[count($stack) - 1];
                    if ($h[$i] > $h[$topIdx]) {
                        $h[$i]--;
                        $h[$topIdx] = 0;
                        array_pop($stack);
                    } elseif ($h[$i] < $h[$topIdx]) {
                        $h[$topIdx]--;
                        $h[$i] = 0;
                    } else {
                        $h[$i] = 0;
                        $h[$topIdx] = 0;
                        array_pop($stack);
                    }
                }
            }
        }

        $result = [];
        for ($i = 0; $i < $n; $i++) {
            if ($h[$i] > 0) {
                $result[] = $h[$i];
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
    func survivedRobotsHealths(_ positions: [Int], _ healths: [Int], _ directions: String) -> [Int] {
        let n = positions.count
        var h = healths
        var indices = Array(0..<n)
        indices.sort { positions[$0] < positions[$1] }

        let directionsArray = Array(directions)
        var stack = [Int]()

        for i in indices {
            if directionsArray[i] == "R" {
                stack.append(i)
            } else {
                while !stack.isEmpty && h[i] > 0 {
                    let topIdx = stack.last!
                    if h[i] > h[topIdx] {
                        h[i] -= 1
                        h[topIdx] = 0
                        stack.removeLast()
                    } else if h[i] < h[topIdx] {
                        h[topIdx] -= 1
                        h[i] = 0
                    } else {
                        h[i] = 0
                        h[topIdx] = 0
                        stack.removeLast()
                    }
                }
            }
        }

        return h.filter { $0 > 0 }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
import java.util.ArrayDeque

class Solution {
    fun survivedRobotsHealths(positions: IntArray, healths: IntArray, directions: String): List<Int> {
        val n = positions.size
        val indices = Array(n) { it }
        indices.sortBy { positions[it] }

        val h = healths.copyOf()
        val stack = ArrayDeque<Int>()

        for (i in indices) {
            if (directions[i] == 'R') {
                stack.push(i)
            } else {
                while (stack.isNotEmpty() && h[i] > 0) {
                    val topIdx = stack.peek()
                    if (h[i] > h[topIdx]) {
                        h[i]--
                        h[topIdx] = 0
                        stack.pop()
                    } else if (h[i] < h[topIdx]) {
                        h[topIdx]--
                        h[i] = 0
                    } else {
                        h[i] = 0
                        h[topIdx] = 0
                        stack.pop()
                    }
                }
            }
        }

        val result = mutableListOf<Int>()
        for (v in h) {
            if (v > 0) result.add(v)
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
class Solution {
  List<int> survivedRobotsHealths(List<int> positions, List<int> healths, String directions) {
    int n = positions.length;
    List<int> indices = List.generate(n, (i) => i);
    indices.sort((a, b) => positions[a].compareTo(positions[b]));

    List<int> h = List.from(healths);
    List<int> stack = [];

    for (int i in indices) {
      if (directions[i] == 'R') {
        stack.add(i);
      } else {
        while (stack.isNotEmpty && h[i] > 0) {
          int topIdx = stack.last;
          if (h[i] > h[topIdx]) {
            h[i]--;
            h[topIdx] = 0;
            stack.removeLast();
          } else if (h[i] < h[topIdx]) {
            h[topIdx]--;
            h[i] = 0;
          } else {
            h[i] = 0;
            h[topIdx] = 0;
            stack.removeLast();
          }
        }
      }
    }

    List<int> result = [];
    for (int v in h) {
      if (v > 0) result.add(v);
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
import (
	"sort"
)

func survivedRobotsHealths(positions []int, healths []int, directions string) []int {
	n := len(positions)
	indices := make([]int, n)
	for i := range indices {
		indices[i] = i
	}
	sort.Slice(indices, func(i, j int) bool {
		return positions[indices[i]] < positions[indices[j]]
	})

	h := make([]int, n)
	copy(h, healths)
	stack := []int{}

	for _, i := range indices {
		if directions[i] == 'R' {
			stack = append(stack, i)
		} else {
			for len(stack) > 0 && h[i] > 0 {
				topIdx := stack[len(stack)-1]
				if h[i] > h[topIdx] {
					h[i]--
					h[topIdx] = 0
					stack = stack[:len(stack)-1]
				} else if h[i] < h[topIdx] {
					h[topIdx]--
					h[i] = 0
				} else {
					h[i] = 0
					h[topIdx] = 0
					stack = stack[:len(stack)-1]
				}
			}
		}
	}

	result := []int{}
	for _, val := range h {
		if val > 0 {
			result = append(result, val)
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
def survived_robots_healths(positions, healths, directions)
  n = positions.size
  indices = (0...n).to_a.sort_by { |i| positions[i] }
  stack = []

  indices.each do |i|
    if directions[i] == 'R'
      stack << i
    else
      while !stack.empty? && healths[i] > 0
        top = stack.last
        if healths[i] > healths[top]
          healths[top] = 0
          healths[i] -= 1
          stack.pop
        elsif healths[i] < healths[top]
          healths[top] -= 1
          healths[i] = 0
        else
          healths[top] = 0
          healths[i] = 0
          stack.pop
        end
      end
    end
  end
  healths.reject { |h| h == 0 }
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.collection.mutable

object Solution {
  def survivedRobotsHealths(positions: Array[Int], healths: Array[Int], directions: String): List[Int] = {
    val n = positions.length
    val indices = (0 until n).toArray.sortBy(positions)
    val stack = mutable.Stack[Int]()
    val h = healths.clone()

    for (i <- indices) {
      if (directions(i) == 'R') {
        stack.push(i)
      } else {
        while (stack.nonEmpty && h(i) > 0) {
          val top = stack.top
          if (h(i) > h(top)) {
            h(top) = 0
            h(i) = h(i) - 1
            stack.pop()
          } else if (h(i) < h(top)) {
            h(top) = h(top) - 1
            h(i) = 0
          } else {
            h(top) = 0
            h(i) = 0
            stack.pop()
          }
        }
      }
    }
    h.filter(_ > 0).toList
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn survived_robots_healths(positions: Vec<i32>, healths: Vec<i32>, directions: String) -> Vec<i32> {
        let n = positions.len();
        let mut h = healths;
        let mut indices: Vec<usize> = (0..n).collect();
        indices.sort_by_key(|&i| positions[i]);
        let dir_bytes = directions.as_bytes();
        let mut stack: Vec<usize> = Vec::new();

        for &i in &indices {
            if dir_bytes[i] == b'R' {
                stack.push(i);
            } else {
                while let Some(&top) = stack.last() {
                    if h[i] > h[top] {
                        h[top] = 0;
                        h[i] -= 1;
                        stack.pop();
                    } else if h[i] < h[top] {
                        h[top] -= 1;
                        h[i] = 0;
                        break;
                    } else {
                        h[i] = 0;
                        h[top] = 0;
                        stack.pop();
                        break;
                    }
                }
            }
        }
        h.into_iter().filter(|&val| val > 0).collect()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (survived-robots-healths positions healths directions)
  (-> (listof exact-integer?) (listof exact-integer?) string? (listof exact-integer?))
  (let* ([n (length positions)]
         [pos-vec (list->vector positions)]
         [health-vec (list->vector healths)]
         [dir-vec (string->vector directions)]
         [indices (sort (range n) < #:key (lambda (i) (vector-ref pos-vec i)))]
         [stack '()])
    (for ([i indices])
      (if (char=? (vector-ref dir-vec i) #\R)
          (set! stack (cons i stack))
          (let loop ()
            (when (and (not (null? stack)) (> (vector-ref health-vec i) 0))
              (let* ([top (car stack)]
                     [h-i (vector-ref health-vec i)]
                     [h-top (vector-ref health-vec top)])
                (cond
                  [(> h-i h-top)
                   (vector-set! health-vec top 0)
                   (vector-set! health-vec i (- h-i 1))
                   (set! stack (cdr stack))
                   (loop)]
                  [(< h-i h-top)
                   (vector-set! health-vec top (- h-top 1))
                   (vector-set! health-vec i 0)]
                  [else
                   (vector-set! health-vec top 0)
                   (vector-set! health-vec i 0)
                   (set! stack (cdr stack))]))))))
    (filter (lambda (h) (> h 0)) (vector->list health-vec))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec survived_robots_healths(Positions :: [integer()], Healths :: [integer()], Directions :: unicode:unicode_binary()) -> [integer()].
survived_robots_healths(Positions, Healths, Directions) ->
  N = length(Positions),
  DirList = binary_to_list(Directions),
  IndexedPos = lists:zip(lists:seq(0, N - 1), Positions),
  SortedIndices = [I || {I, _P} <- lists:keysort(2, IndexedPos)],
  HealthMap = maps:from_list(lists:zip(lists:seq(0, N - 1), Healths)),
  DirVec = list_to_tuple(DirList),
  FinalHealthMap = process_robots(SortedIndices, [], HealthMap, DirVec),
  [maps:get(I, FinalHealthMap) || I <- lists:seq(0, N - 1), maps:get(I, FinalHealthMap) > 0].

process_robots([], _Stack, HealthMap, _DirVec) -> HealthMap;
process_robots([I | Rest], Stack, HealthMap, DirVec) ->
  case element(I + 1, DirVec) of
    $R -> process_robots(Rest, [I | Stack], HealthMap, DirVec);
    $L -> {NewStack, NewHealthMap} = collide(I, Stack, HealthMap),
          process_robots(Rest, NewStack, NewHealthMap, DirVec)
  end.

collide(I, [], HealthMap) -> {[], HealthMap};
collide(I, [Top | Rest] = Stack, HealthMap) ->
  HI = maps:get(I, HealthMap),
  HTop = maps:get(Top, HealthMap),
  if
    HI > HTop -> collide(I, Rest, maps:put(I, HI - 1, maps:put(Top, 0, HealthMap)));
    HI < HTop -> {Stack, maps:put(Top, HTop - 1, maps:put(I, 0, HealthMap))};
    true -> {Rest, maps:put(Top, 0, maps:put(I, 0, HealthMap))}
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec survived_robots_healths(positions :: [integer], healths :: [integer], directions :: String.t) :: [integer]
  def survived_robots_healths(positions, healths, directions) do
    n = length(positions)
    dir_list = String.to_charlist(directions)
    indexed_positions = Enum.with_index(positions) |> Enum.sort_by(fn {p, _i} -> p end)
    sorted_indices = Enum.map(indexed_positions, fn {_p, i} -> i end)
    health_map = Enum.with_index(healths) |> Enum.map(fn {h, i} -> {i, h} end) |> Map.new()
    dir_map = Enum.with_index(dir_list) |> Enum.map(fn {d, i} -> {i, d} end) |> Map.new()
    final_health_map = process_robots(sorted_indices, [], health_map, dir_map)
    0..(n-1)
    |> Enum.map(fn i -> Map.get(final_health_map, i) end)
    |> Enum.filter(fn h -> h > 0 end)
  end

  defp process_robots([], _stack, health_map, _dir_map), do: health_map
  defp process_robots([i | rest], stack, health_map, dir_map) do
    if Map.get(dir_map, i) == ?R do
      process_robots(rest, [i | stack], health_map, dir_map)
    else
      {new_stack, new_health_map} = collide(i, stack, health_map)
      process_robots(rest, new_stack, new_health_map, dir_map)
    end
  end

  defp collide(i, [], health_map), do: {[], health_map}
  defp collide(i, [top | rest] = stack, health_map) do
    h_i = Map.get(health_map, i)
    h_top = Map.get(health_map, top)
    cond do
      h_i > h_top -> collide(i, rest, health_map |> Map.put(top, 0) |> Map.put(i, h_i - 1))
      h_i < h_top -> {stack, health_map |> Map.put(i, 0) |> Map.put(top, h_top - 1)}
      true -> {rest, health_map |> Map.put(i, 0) |> Map.put(top, 0)}
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N log N), where N is the number of robots. This is dominated by the sorting step required to process robots by their initial positions. The collision simulation using a stack takes O(N) time because each robot index is pushed onto and popped from the stack at most once.
- **Space Complexity:** O(N), as we need extra space for storing metadata (indices and positions) for sorting, a stack for right-moving robots, and the resulting list of survivor healths.
