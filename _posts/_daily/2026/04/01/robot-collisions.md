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
        \ = i;\n        sort(indices.begin(), indices.end(), [&](int a, int b) {\n \
        \           return positions[a] < positions[b];\n        });\n\n        vector<int>\
        \ stack;\n        for (int i : indices) {\n            if (directions[i] ==\
        \ 'R') {\n                stack.push_back(i);\n            } else {\n      \
        \          while (!stack.empty() && healths[i] > 0) {\n                    int\
        \ j = stack.back();\n                    if (healths[i] > healths[j]) {\n  \
        \                      healths[i]--;\n                        healths[j] = 0;\n\
        \                        stack.pop_back();\n                    } else if (healths[i]\
        \ < healths[j]) {\n                        healths[j]--;\n                 \
        \       healths[i] = 0;\n                    } else {\n                    \
        \    healths[i] = 0;\n                        healths[j] = 0;\n            \
        \            stack.pop_back();\n                    }\n                }\n \
        \           }\n        }\n\n        vector<int> result;\n        for (int h\
        \ : healths) {\n            if (h > 0) result.push_back(h);\n        }\n   \
        \     return result;\n    }\n};"
      java: "class Solution {\n    public List<Integer> survivedRobotsHealths(int[]\
        \ positions, int[] healths, String directions) {\n        int n = positions.length;\n\
        \        Integer[] indices = new Integer[n];\n        for (int i = 0; i < n;\
        \ i++) indices[i] = i;\n        Arrays.sort(indices, (a, b) -> Integer.compare(positions[a],\
        \ positions[b]));\n\n        Stack<Integer> stack = new Stack<>();\n       \
        \ for (int i : indices) {\n            if (directions.charAt(i) == 'R') {\n\
        \                stack.push(i);\n            } else {\n                while\
        \ (!stack.isEmpty() && healths[i] > 0) {\n                    int j = stack.peek();\n\
        \                    if (healths[i] > healths[j]) {\n                      \
        \  healths[i]--;\n                        healths[j] = 0;\n                \
        \        stack.pop();\n                    } else if (healths[i] < healths[j])\
        \ {\n                        healths[j]--;\n                        healths[i]\
        \ = 0;\n                    } else {\n                        healths[i] = 0;\n\
        \                        healths[j] = 0;\n                        stack.pop();\n\
        \                    }\n                }\n            }\n        }\n\n    \
        \    List<Integer> result = new ArrayList<>();\n        for (int h : healths)\
        \ {\n            if (h > 0) result.add(h);\n        }\n        return result;\n\
        \    }\n}"
      python: "class Solution(object):\n    def survivedRobotsHealths(self, positions,\
        \ healths, directions):\n        \"\"\"\n        :type positions: List[int]\n\
        \        :type healths: List[int]\n        :type directions: str\n        :rtype:\
        \ List[int]\n        \"\"\"\n        n = len(positions)\n        indices = sorted(range(n),\
        \ key=lambda i: positions[i])\n        stack = []\n\n        for i in indices:\n\
        \            if directions[i] == 'R':\n                stack.append(i)\n   \
        \         else:\n                while stack and healths[i] > 0:\n         \
        \           j = stack[-1]\n                    if healths[i] > healths[j]:\n\
        \                        healths[i] -= 1\n                        healths[j]\
        \ = 0\n                        stack.pop()\n                    elif healths[i]\
        \ < healths[j]:\n                        healths[j] -= 1\n                 \
        \       healths[i] = 0\n                    else:\n                        healths[i]\
        \ = 0\n                        healths[j] = 0\n                        stack.pop()\n\
        \n        return [h for h in healths if h > 0]"
      python3: "class Solution:\n    def survivedRobotsHealths(self, positions: List[int],\
        \ healths: List[int], directions: str) -> List[int]:\n        n = len(positions)\n\
        \        indices = sorted(range(n), key=lambda i: positions[i])\n        stack\
        \ = []\n\n        for i in indices:\n            if directions[i] == 'R':\n\
        \                stack.append(i)\n            else:\n                while stack\
        \ and healths[i] > 0:\n                    j = stack[-1]\n                 \
        \   if healths[i] > healths[j]:\n                        healths[i] -= 1\n \
        \                       healths[j] = 0\n                        stack.pop()\n\
        \                    elif healths[i] < healths[j]:\n                       \
        \ healths[j] -= 1\n                        healths[i] = 0\n                \
        \    else:\n                        healths[i] = 0\n                       \
        \ healths[j] = 0\n                        stack.pop()\n\n        return [h for\
        \ h in healths if h > 0]"
      c: "typedef struct {\n    int pos, health, id;\n    char dir;\n} Robot;\n\nint\
        \ compareRobots(const void* a, const void* b) {\n    return ((Robot*)a)->pos\
        \ - ((Robot*)b)->pos;\n}\n\nint* survivedRobotsHealths(int* positions, int positionsSize,\
        \ int* healths, int healthsSize, char* directions, int* returnSize) {\n    int\
        \ n = positionsSize;\n    Robot* robots = (Robot*)malloc(n * sizeof(Robot));\n\
        \    for (int i = 0; i < n; i++) {\n        robots[i].pos = positions[i];\n\
        \        robots[i].health = healths[i];\n        robots[i].dir = directions[i];\n\
        \        robots[i].id = i;\n    }\n    qsort(robots, n, sizeof(Robot), compareRobots);\n\
        \n    int* stack = (int*)malloc(n * sizeof(int));\n    int top = -1;\n    int*\
        \ finalHealths = (int*)malloc(n * sizeof(int));\n    memset(finalHealths, 0,\
        \ n * sizeof(int));\n\n    for (int i = 0; i < n; i++) {\n        if (robots[i].dir\
        \ == 'R') {\n            stack[++top] = i;\n        } else {\n            while\
        \ (top >= 0 && robots[i].health > 0) {\n                int j = stack[top];\n\
        \                if (robots[i].health > robots[j].health) {\n              \
        \      robots[i].health--;\n                    robots[j].health = 0;\n    \
        \                top--;\n                } else if (robots[i].health < robots[j].health)\
        \ {\n                    robots[j].health--;\n                    robots[i].health\
        \ = 0;\n                } else {\n                    robots[i].health = 0;\n\
        \                    robots[j].health = 0;\n                    top--;\n   \
        \             }\n            }\n        }\n    }\n\n    for (int i = 0; i <\
        \ n; i++) {\n        finalHealths[robots[i].id] = robots[i].health;\n    }\n\
        \n    int count = 0;\n    for (int i = 0; i < n; i++) {\n        if (finalHealths[i]\
        \ > 0) count++;\n    }\n\n    int* result = (int*)malloc(count * sizeof(int));\n\
        \    int k = 0;\n    for (int i = 0; i < n; i++) {\n        if (finalHealths[i]\
        \ > 0) result[k++] = finalHealths[i];\n    }\n\n    free(robots);\n    free(stack);\n\
        \    free(finalHealths);\n    *returnSize = count;\n    return result;\n}"
      csharp: "public class Solution {\n    public IList<int> SurvivedRobotsHealths(int[]\
        \ positions, int[] healths, string directions) {\n        int n = positions.Length;\n\
        \        int[] indices = Enumerable.Range(0, n).ToArray();\n        Array.Sort(indices,\
        \ (a, b) => positions[a].CompareTo(positions[b]));\n\n        Stack<int> stack\
        \ = new Stack<int>();\n        for (int k = 0; k < n; k++) {\n            int\
        \ i = indices[k];\n            if (directions[i] == 'R') {\n               \
        \ stack.Push(i);\n            } else {\n                while (stack.Count >\
        \ 0 && healths[i] > 0) {\n                    int j = stack.Peek();\n      \
        \              if (healths[i] > healths[j]) {\n                        healths[i]--;\n\
        \                        healths[j] = 0;\n                        stack.Pop();\n\
        \                    } else if (healths[i] < healths[j]) {\n               \
        \         healths[j]--;\n                        healths[i] = 0;\n         \
        \           } else {\n                        healths[i] = 0;\n            \
        \            healths[j] = 0;\n                        stack.Pop();\n       \
        \             }\n                }\n            }\n        }\n\n        List<int>\
        \ result = new List<int>();\n        foreach (int h in healths) {\n        \
        \    if (h > 0) result.Add(h);\n        }\n        return result;\n    }\n}"
      javascript: "/**\n * @param {number[]} positions\n * @param {number[]} healths\n\
        \ * @param {string} directions\n * @return {number[]}\n */\nvar survivedRobotsHealths\
        \ = function(positions, healths, directions) {\n    const n = positions.length;\n\
        \    const indices = Array.from({ length: n }, (_, i) => i);\n    indices.sort((a,\
        \ b) => positions[a] - positions[b]);\n\n    const stack = [];\n    for (const\
        \ i of indices) {\n        if (directions[i] === 'R') {\n            stack.push(i);\n\
        \        } else {\n            while (stack.length > 0 && healths[i] > 0) {\n\
        \                const j = stack[stack.length - 1];\n                if (healths[i]\
        \ > healths[j]) {\n                    healths[i]--;\n                    healths[j]\
        \ = 0;\n                    stack.pop();\n                } else if (healths[i]\
        \ < healths[j]) {\n                    healths[j]--;\n                    healths[i]\
        \ = 0;\n                } else {\n                    healths[i] = 0;\n    \
        \                healths[j] = 0;\n                    stack.pop();\n       \
        \         }\n            }\n        }\n    }\n\n    return healths.filter(h\
        \ => h > 0);\n};"
      typescript: "function survivedRobotsHealths(positions: number[], healths: number[],\
        \ directions: string): number[] {\n    const n = positions.length;\n    const\
        \ indices = Array.from({ length: n }, (_, i) => i);\n    indices.sort((a, b)\
        \ => positions[a] - positions[b]);\n\n    const h = [...healths];\n    const\
        \ stack: number[] = [];\n    for (const i of indices) {\n        if (directions[i]\
        \ === 'R') {\n            stack.push(i);\n        } else {\n            while\
        \ (stack.length > 0 && h[i] > 0) {\n                const topIdx = stack[stack.length\
        \ - 1];\n                if (h[topIdx] > h[i]) {\n                    h[topIdx]\
        \ -= 1;\n                    h[i] = 0;\n                } else if (h[topIdx]\
        \ < h[i]) {\n                    h[topIdx] = 0;\n                    h[i] -=\
        \ 1;\n                    stack.pop();\n                } else {\n         \
        \           h[topIdx] = 0;\n                    h[i] = 0;\n                \
        \    stack.pop();\n                }\n            }\n        }\n    }\n\n  \
        \  const result: number[] = [];\n    for (let i = 0; i < n; i++) {\n       \
        \ if (h[i] > 0) {\n            result.push(h[i]);\n        }\n    }\n    return\
        \ result;\n}"
      php: "class Solution {\n    /**\n     * @param Integer[] $positions\n     * @param\
        \ Integer[] $healths\n     * @param String $directions\n     * @return Integer[]\n\
        \     */\n    function survivedRobotsHealths($positions, $healths, $directions)\
        \ {\n        $n = count($positions);\n        $h = $healths;\n        $indices\
        \ = range(0, $n - 1);\n        usort($indices, function($a, $b) use ($positions)\
        \ {\n            return $positions[$a] <=> $positions[$b];\n        });\n\n\
        \        $stack = [];\n        foreach ($indices as $i) {\n            if ($directions[$i]\
        \ === 'R') {\n                $stack[] = $i;\n            } else {\n       \
        \         while (!empty($stack) && $h[$i] > 0) {\n                    $topIdx\
        \ = $stack[count($stack) - 1];\n                    if ($h[$topIdx] > $h[$i])\
        \ {\n                        $h[$topIdx] -= 1;\n                        $h[$i]\
        \ = 0;\n                    } else if ($h[$topIdx] < $h[$i]) {\n           \
        \             $h[$topIdx] = 0;\n                        $h[$i] -= 1;\n     \
        \                   array_pop($stack);\n                    } else {\n     \
        \                   $h[$topIdx] = 0;\n                        $h[$i] = 0;\n\
        \                        array_pop($stack);\n                    }\n       \
        \         }\n            }\n        }\n\n        $result = [];\n        for\
        \ ($i = 0; $i < $n; $i++) {\n            if ($h[$i] > 0) {\n               \
        \ $result[] = $h[$i];\n            }\n        }\n        return $result;\n \
        \   }\n}"
      swift: "class Solution {\n    func survivedRobotsHealths(_ positions: [Int], _\
        \ healths: [Int], _ directions: String) -> [Int] {\n        let n = positions.count\n\
        \        var h = healths\n        let dirs = Array(directions)\n        var\
        \ indices = Array(0..<n)\n        indices.sort { positions[$0] < positions[$1]\
        \ }\n\n        var stack = [Int]()\n        for i in indices {\n           \
        \ if dirs[i] == \"R\" {\n                stack.append(i)\n            } else\
        \ {\n                while !stack.isEmpty && h[i] > 0 {\n                  \
        \  let topIdx = stack.last!\n                    if h[topIdx] > h[i] {\n   \
        \                     h[topIdx] -= 1\n                        h[i] = 0\n   \
        \                 } else if h[topIdx] < h[i] {\n                        h[topIdx]\
        \ = 0\n                        h[i] -= 1\n                        stack.removeLast()\n\
        \                    } else {\n                        h[topIdx] = 0\n     \
        \                   h[i] = 0\n                        stack.removeLast()\n \
        \                   }\n                }\n            }\n        }\n\n     \
        \   var result = [Int]()\n        for i in 0..<n {\n            if h[i] > 0\
        \ {\n                result.append(h[i])\n            }\n        }\n       \
        \ return result\n    }\n}"
      kotlin: "class Solution {\n    fun survivedRobotsHealths(positions: IntArray,\
        \ healths: IntArray, directions: String): List<Int> {\n        val n = positions.size\n\
        \        val indices = Array(n) { it }\n        indices.sortBy { positions[it]\
        \ }\n\n        val h = healths.copyOf()\n        val stack = mutableListOf<Int>()\n\
        \n        for (i in indices) {\n            if (directions[i] == 'R') {\n  \
        \              stack.add(i)\n            } else {\n                while (stack.isNotEmpty()\
        \ && h[i] > 0) {\n                    val topIdx = stack.last()\n          \
        \          if (h[topIdx] > h[i]) {\n                        h[topIdx] -= 1\n\
        \                        h[i] = 0\n                    } else if (h[topIdx]\
        \ < h[i]) {\n                        h[topIdx] = 0\n                       \
        \ h[i] -= 1\n                        stack.removeAt(stack.size - 1)\n      \
        \              } else {\n                        h[topIdx] = 0\n           \
        \             h[i] = 0\n                        stack.removeAt(stack.size -\
        \ 1)\n                    }\n                }\n            }\n        }\n\n\
        \        val result = mutableListOf<Int>()\n        for (i in 0 until n) {\n\
        \            if (h[i] > 0) {\n                result.add(h[i])\n           \
        \ }\n        }\n        return result\n    }\n}"
      dart: "class Solution {\n  List<int> survivedRobotsHealths(List<int> positions,\
        \ List<int> healths, String directions) {\n    int n = positions.length;\n \
        \   List<int> indices = List.generate(n, (index) => index);\n    indices.sort((a,\
        \ b) => positions[a].compareTo(positions[b]));\n\n    List<int> h = List.from(healths);\n\
        \    List<int> stack = [];\n\n    for (int i in indices) {\n      if (directions[i]\
        \ == 'R') {\n        stack.add(i);\n      } else {\n        while (stack.isNotEmpty\
        \ && h[i] > 0) {\n          int topIdx = stack.last;\n          if (h[topIdx]\
        \ > h[i]) {\n            h[topIdx] -= 1;\n            h[i] = 0;\n          }\
        \ else if (h[topIdx] < h[i]) {\n            h[topIdx] = 0;\n            h[i]\
        \ -= 1;\n            stack.removeLast();\n          } else {\n            h[topIdx]\
        \ = 0;\n            h[i] = 0;\n            stack.removeLast();\n          }\n\
        \        }\n      }\n    }\n\n    List<int> result = [];\n    for (int i = 0;\
        \ i < n; i++) {\n      if (h[i] > 0) {\n        result.add(h[i]);\n      }\n\
        \    }\n    return result;\n  }\n}"
      go: "import (\n    \"sort\"\n)\n\nfunc survivedRobotsHealths(positions []int,\
        \ healths []int, directions string) []int {\n    n := len(positions)\n    indices\
        \ := make([]int, n)\n    for i := 0; i < n; i++ {\n        indices[i] = i\n\
        \    }\n    sort.Slice(indices, func(i, j int) bool {\n        return positions[indices[i]]\
        \ < positions[indices[j]]\n    })\n\n    h := make([]int, n)\n    copy(h, healths)\n\
        \    stack := []int{}\n    for _, i := range indices {\n        if directions[i]\
        \ == 'R' {\n            stack = append(stack, i)\n        } else {\n       \
        \     for len(stack) > 0 && h[i] > 0 {\n                topIdx := stack[len(stack)-1]\n\
        \                if h[topIdx] > h[i] {\n                    h[topIdx] -= 1\n\
        \                    h[i] = 0\n                } else if h[topIdx] < h[i] {\n\
        \                    h[topIdx] = 0\n                    h[i] -= 1\n        \
        \            stack = stack[:len(stack)-1]\n                } else {\n      \
        \              h[topIdx] = 0\n                    h[i] = 0\n               \
        \     stack = stack[:len(stack)-1]\n                }\n            }\n     \
        \   }\n    }\n\n    result := []int{}\n    for i := 0; i < n; i++ {\n      \
        \  if h[i] > 0 {\n            result = append(result, h[i])\n        }\n   \
        \ }\n    return result\n}"
      ruby: "def survived_robots_healths(positions, healths, directions)\n  n = positions.length\n\
        \  indices = (0...n).to_a.sort_by { |i| positions[i] }\n  stack = []\n  indices.each\
        \ do |i|\n    if directions[i] == 'R'\n      stack.push(i)\n    else\n     \
        \ while !stack.empty? && healths[i] > 0\n        j = stack.pop\n        if healths[i]\
        \ > healths[j]\n          healths[i] -= 1\n          healths[j] = 0\n      \
        \  elsif healths[i] < healths[j]\n          healths[j] -= 1\n          healths[i]\
        \ = 0\n          stack.push(j)\n        else\n          healths[i] = 0\n   \
        \       healths[j] = 0\n        end\n      end\n    end\n  end\n  healths.select\
        \ { |h| h > 0 }\nend"
      scala: "import scala.collection.mutable\n\nobject Solution {\n    def survivedRobotsHealths(positions:\
        \ Array[Int], healths: Array[Int], directions: String): List[Int] = {\n    \
        \    val n = positions.length\n        val indices = (0 until n).toArray.sortBy(positions)\n\
        \        val stack = mutable.Stack[Int]()\n        val h = healths.clone()\n\
        \n        for (i <- indices) {\n            if (directions(i) == 'R') {\n  \
        \              stack.push(i)\n            } else {\n                while (stack.nonEmpty\
        \ && h(i) > 0) {\n                    val top = stack.pop()\n              \
        \      if (h(i) > h(top)) {\n                        h(i) -= 1\n           \
        \             h(top) = 0\n                    } else if (h(i) < h(top)) {\n\
        \                        h(top) -= 1\n                        h(i) = 0\n   \
        \                     stack.push(top)\n                    } else {\n      \
        \                  h(i) = 0\n                        h(top) = 0\n          \
        \          }\n                }\n            }\n        }\n        h.filter(_\
        \ > 0).toList\n    }\n}"
      rust: "impl Solution {\n    pub fn survived_robots_healths(positions: Vec<i32>,\
        \ mut healths: Vec<i32>, directions: String) -> Vec<i32> {\n        let n =\
        \ positions.len();\n        let mut indices: Vec<usize> = (0..n).collect();\n\
        \        indices.sort_by_key(|&i| positions[i]);\n        let mut stack: Vec<usize>\
        \ = Vec::new();\n        let dirs: Vec<char> = directions.chars().collect();\n\
        \        for &i in &indices {\n            if dirs[i] == 'R' {\n           \
        \     stack.push(i);\n            } else {\n                while let Some(&top)\
        \ = stack.last() {\n                    if healths[i] > healths[top] {\n   \
        \                     healths[i] -= 1;\n                        healths[top]\
        \ = 0;\n                        stack.pop();\n                    } else if\
        \ healths[i] < healths[top] {\n                        healths[top] -= 1;\n\
        \                        healths[i] = 0;\n                        break;\n \
        \                   } else {\n                        healths[i] = 0;\n    \
        \                    healths[top] = 0;\n                        stack.pop();\n\
        \                        break;\n                    }\n                }\n\
        \            }\n        }\n        healths.into_iter().filter(|&h| h > 0).collect()\n\
        \    }\n}"
      racket: "(define/contract (survived-robots-healths positions healths directions)\n\
        \  (-> (listof exact-integer?) (listof exact-integer?) string? (listof exact-integer?))\n\
        \  (let* ([n (length positions)]\n         [dirs (string->list directions)]\n\
        \         [robots (sort (for/list ([p positions] [h healths] [d dirs] [i (in-range\
        \ n)])\n                         (list p h d i))\n                       < #:key\
        \ first)]\n         [collide (lambda (h stack)\n                    (let loop\
        \ ([h h] [stack stack])\n                      (cond\n                     \
        \   [(or (empty? stack) (<= h 0)) (values h stack)]\n                      \
        \  [else\n                         (let* ([top (first stack)]\n            \
        \                    [sh (second top)])\n                           (cond\n\
        \                             [(> h sh) (loop (- h 1) (rest stack))]\n     \
        \                        [(< h sh) (values 0 (cons (list (first top) (- sh 1)\
        \ (third top) (fourth top)) (rest stack)))]\n                             [else\
        \ (values 0 (rest stack))]))])))]\n         [final-survivors\n          (let\
        \ loop ([robots robots] [stack '()] [survivors '()])\n            (if (empty?\
        \ robots)\n                (append (map (lambda (x) (list (fourth x) (second\
        \ x))) stack) survivors)\n                (let* ([curr (first robots)]\n   \
        \                    [h (second curr)]\n                       [d (third curr)]\n\
        \                       [i (fourth curr)])\n                  (if (char=? d\
        \ #\\R)\n                      (loop (rest robots) (cons curr stack) survivors)\n\
        \                      (let-values ([(rem-h new-stack) (collide h stack)])\n\
        \                        (if (> rem-h 0)\n                            (loop\
        \ (rest robots) new-stack (cons (list i rem-h) survivors))\n               \
        \             (loop (rest robots) new-stack survivors)))))))]\n         [sorted-survivors\
        \ (sort final-survivors < #:key first)])\n    (map second sorted-survivors)))"
      erlang: "-spec survived_robots_healths(Positions :: [integer()], Healths :: [integer()],\
        \ Directions :: unicode:unicode_binary()) -> [integer()].\nsurvived_robots_healths(Positions,\
        \ Healths, Directions) ->\n  N = length(Positions),\n  Dirs = binary_to_list(Directions),\n\
        \  Indices = lists:seq(0, N - 1),\n  RobotDetails = lists:zip3(Healths, Dirs,\
        \ Indices),\n  Robots = lists:sort(lists:zip(Positions, RobotDetails)),\n  FinalMap\
        \ = process_robots(Robots, [], #{}),\n  [maps:get(I, FinalMap) || I <- Indices,\
        \ maps:is_key(I, FinalMap)].\n\nprocess_robots([], Stack, Survivors) ->\n  lists:foldl(fn({H,\
        \ _D, I}, Acc) -> Acc#{I => H} end, Survivors, Stack);\nprocess_robots([{_P,\
        \ {H, $R, I}} | Rest], Stack, Survivors) ->\n  process_robots(Rest, [{H, $R,\
        \ I} | Stack], Survivors);\nprocess_robots([{_P, {H, $L, I}} | Rest], Stack,\
        \ Survivors) ->\n  case collide(H, Stack) of\n    {0, NewStack} -> process_robots(Rest,\
        \ NewStack, Survivors);\n    {NewH, NewStack} -> process_robots(Rest, NewStack,\
        \ Survivors#{I => NewH})\n  end.\n\ncollide(H, []) -> {H, []};\ncollide(H, [{SH,\
        \ SD, SI} | SRest]) ->\n  if\n    H > SH -> collide(H - 1, SRest);\n    H <\
        \ SH -> {0, [{SH - 1, SD, SI} | SRest]};\n    true -> {0, SRest}\n  end."
      elixir: "defmodule Solution do\n  @spec survived_robots_healths(positions :: [integer],\
        \ healths :: [integer], directions :: String.t) :: [integer]\n  def survived_robots_healths(positions,\
        \ healths, directions) do\n    n = length(positions)\n    dirs = String.graphemes(directions)\n\
        \    robots = Enum.zip([positions, healths, dirs, 0..(n-1)])\n    |> Enum.sort_by(fn\
        \ {pos, _, _, _} -> pos end)\n\n    final_healths = process_robots(robots, [],\
        \ %{})\n\n    0..(n-1)\n    |> Enum.map(fn i -> Map.get(final_healths, i) end)\n\
        \    |> Enum.reject(&is_nil/1)\n  end\n\n  defp process_robots([], stack, survivors)\
        \ do\n    Enum.reduce(stack, survivors, fn {_, h, _, idx}, acc -> Map.put(acc,\
        \ idx, h) end)\n  end\n\n  defp process_robots([{_, h, \"R\", idx} | rest],\
        \ stack, survivors) do\n    process_robots(rest, [{0, h, \"R\", idx} | stack],\
        \ survivors)\n  end\n\n  defp process_robots([{_, h, \"L\", idx} | rest], stack,\
        \ survivors) do\n    {rem_h, new_stack} = collide(h, stack)\n    if rem_h >\
        \ 0 do\n      process_robots(rest, new_stack, Map.put(survivors, idx, rem_h))\n\
        \    else\n      process_robots(rest, new_stack, survivors)\n    end\n  end\n\
        \n  defp collide(h, []) do\n    {h, []}\n  end\n\n  defp collide(h, [{pos, sh,\
        \ dir, idx} | rest]) do\n    cond do\n      h > sh -> collide(h - 1, rest)\n\
        \      h < sh -> {0, [{pos, sh - 1, dir, idx} | rest]}\n      true -> {0, rest}\n\
        \    end\n  end\nend"
    approach: 'To solve this problem efficiently, we process the robots in the order
      of their positions. Since collisions only occur between a robot moving right and
      a robot to its right moving left, we sort the robots based on their spatial positions
      while maintaining their original indices to ensure the final output order is correct.
      We then use a stack-based approach to simulate the collisions, where the stack
      stores robots currently moving to the right that haven''t been destroyed yet.


      As we iterate through the sorted robots, if a robot is moving right, we push its
      index onto the stack. If a robot is moving left, we check for potential collisions
      with the robots in the stack (the nearest right-moving robots). While the stack
      is not empty and the left-moving robot still has health, we compare its health
      with the top robot of the stack. If the left-moving robot has more health, the
      right-moving robot is destroyed and the left-moving robot''s health is decremented.
      If the right-moving robot has more health, the left-moving robot is destroyed
      and the right-moving robot''s health is decremented. If healths are equal, both
      are destroyed. Finally, we collect the health of the surviving robots in their
      original input order.'
    time_complexity: O(n log n) because we must sort the robots by their positions.
      The collision simulation takes O(n) time as each robot is pushed onto and popped
      from the stack at most once.
    space_complexity: O(n) to store the indices of the robots, the sorted order, and
      the stack used for collision management.
    elapsed_time: 341.7463791370392
    model: gemini-3-flash-preview
    generated_at: '2026-04-01 02:00:27 '
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

To solve this problem efficiently, we process the robots in the order of their positions. Since collisions only occur between a robot moving right and a robot to its right moving left, we sort the robots based on their spatial positions while maintaining their original indices to ensure the final output order is correct. We then use a stack-based approach to simulate the collisions, where the stack stores robots currently moving to the right that haven't been destroyed yet.

As we iterate through the sorted robots, if a robot is moving right, we push its index onto the stack. If a robot is moving left, we check for potential collisions with the robots in the stack (the nearest right-moving robots). While the stack is not empty and the left-moving robot still has health, we compare its health with the top robot of the stack. If the left-moving robot has more health, the right-moving robot is destroyed and the left-moving robot's health is decremented. If the right-moving robot has more health, the left-moving robot is destroyed and the right-moving robot's health is decremented. If healths are equal, both are destroyed. Finally, we collect the health of the surviving robots in their original input order.

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
                    int j = stack.back();
                    if (healths[i] > healths[j]) {
                        healths[i]--;
                        healths[j] = 0;
                        stack.pop_back();
                    } else if (healths[i] < healths[j]) {
                        healths[j]--;
                        healths[i] = 0;
                    } else {
                        healths[i] = 0;
                        healths[j] = 0;
                        stack.pop_back();
                    }
                }
            }
        }

        vector<int> result;
        for (int h : healths) {
            if (h > 0) result.push_back(h);
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
    public List<Integer> survivedRobotsHealths(int[] positions, int[] healths, String directions) {
        int n = positions.length;
        Integer[] indices = new Integer[n];
        for (int i = 0; i < n; i++) indices[i] = i;
        Arrays.sort(indices, (a, b) -> Integer.compare(positions[a], positions[b]));

        Stack<Integer> stack = new Stack<>();
        for (int i : indices) {
            if (directions.charAt(i) == 'R') {
                stack.push(i);
            } else {
                while (!stack.isEmpty() && healths[i] > 0) {
                    int j = stack.peek();
                    if (healths[i] > healths[j]) {
                        healths[i]--;
                        healths[j] = 0;
                        stack.pop();
                    } else if (healths[i] < healths[j]) {
                        healths[j]--;
                        healths[i] = 0;
                    } else {
                        healths[i] = 0;
                        healths[j] = 0;
                        stack.pop();
                    }
                }
            }
        }

        List<Integer> result = new ArrayList<>();
        for (int h : healths) {
            if (h > 0) result.add(h);
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
                    j = stack[-1]
                    if healths[i] > healths[j]:
                        healths[i] -= 1
                        healths[j] = 0
                        stack.pop()
                    elif healths[i] < healths[j]:
                        healths[j] -= 1
                        healths[i] = 0
                    else:
                        healths[i] = 0
                        healths[j] = 0
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
                    j = stack[-1]
                    if healths[i] > healths[j]:
                        healths[i] -= 1
                        healths[j] = 0
                        stack.pop()
                    elif healths[i] < healths[j]:
                        healths[j] -= 1
                        healths[i] = 0
                    else:
                        healths[i] = 0
                        healths[j] = 0
                        stack.pop()

        return [h for h in healths if h > 0]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
typedef struct {
    int pos, health, id;
    char dir;
} Robot;

int compareRobots(const void* a, const void* b) {
    return ((Robot*)a)->pos - ((Robot*)b)->pos;
}

int* survivedRobotsHealths(int* positions, int positionsSize, int* healths, int healthsSize, char* directions, int* returnSize) {
    int n = positionsSize;
    Robot* robots = (Robot*)malloc(n * sizeof(Robot));
    for (int i = 0; i < n; i++) {
        robots[i].pos = positions[i];
        robots[i].health = healths[i];
        robots[i].dir = directions[i];
        robots[i].id = i;
    }
    qsort(robots, n, sizeof(Robot), compareRobots);

    int* stack = (int*)malloc(n * sizeof(int));
    int top = -1;
    int* finalHealths = (int*)malloc(n * sizeof(int));
    memset(finalHealths, 0, n * sizeof(int));

    for (int i = 0; i < n; i++) {
        if (robots[i].dir == 'R') {
            stack[++top] = i;
        } else {
            while (top >= 0 && robots[i].health > 0) {
                int j = stack[top];
                if (robots[i].health > robots[j].health) {
                    robots[i].health--;
                    robots[j].health = 0;
                    top--;
                } else if (robots[i].health < robots[j].health) {
                    robots[j].health--;
                    robots[i].health = 0;
                } else {
                    robots[i].health = 0;
                    robots[j].health = 0;
                    top--;
                }
            }
        }
    }

    for (int i = 0; i < n; i++) {
        finalHealths[robots[i].id] = robots[i].health;
    }

    int count = 0;
    for (int i = 0; i < n; i++) {
        if (finalHealths[i] > 0) count++;
    }

    int* result = (int*)malloc(count * sizeof(int));
    int k = 0;
    for (int i = 0; i < n; i++) {
        if (finalHealths[i] > 0) result[k++] = finalHealths[i];
    }

    free(robots);
    free(stack);
    free(finalHealths);
    *returnSize = count;
    return result;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public IList<int> SurvivedRobotsHealths(int[] positions, int[] healths, string directions) {
        int n = positions.Length;
        int[] indices = Enumerable.Range(0, n).ToArray();
        Array.Sort(indices, (a, b) => positions[a].CompareTo(positions[b]));

        Stack<int> stack = new Stack<int>();
        for (int k = 0; k < n; k++) {
            int i = indices[k];
            if (directions[i] == 'R') {
                stack.Push(i);
            } else {
                while (stack.Count > 0 && healths[i] > 0) {
                    int j = stack.Peek();
                    if (healths[i] > healths[j]) {
                        healths[i]--;
                        healths[j] = 0;
                        stack.Pop();
                    } else if (healths[i] < healths[j]) {
                        healths[j]--;
                        healths[i] = 0;
                    } else {
                        healths[i] = 0;
                        healths[j] = 0;
                        stack.Pop();
                    }
                }
            }
        }

        List<int> result = new List<int>();
        foreach (int h in healths) {
            if (h > 0) result.Add(h);
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
                const j = stack[stack.length - 1];
                if (healths[i] > healths[j]) {
                    healths[i]--;
                    healths[j] = 0;
                    stack.pop();
                } else if (healths[i] < healths[j]) {
                    healths[j]--;
                    healths[i] = 0;
                } else {
                    healths[i] = 0;
                    healths[j] = 0;
                    stack.pop();
                }
            }
        }
    }

    return healths.filter(h => h > 0);
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
                if (h[topIdx] > h[i]) {
                    h[topIdx] -= 1;
                    h[i] = 0;
                } else if (h[topIdx] < h[i]) {
                    h[topIdx] = 0;
                    h[i] -= 1;
                    stack.pop();
                } else {
                    h[topIdx] = 0;
                    h[i] = 0;
                    stack.pop();
                }
            }
        }
    }

    const result: number[] = [];
    for (let i = 0; i < n; i++) {
        if (h[i] > 0) {
            result.push(h[i]);
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
class Solution {
    /**
     * @param Integer[] $positions
     * @param Integer[] $healths
     * @param String $directions
     * @return Integer[]
     */
    function survivedRobotsHealths($positions, $healths, $directions) {
        $n = count($positions);
        $h = $healths;
        $indices = range(0, $n - 1);
        usort($indices, function($a, $b) use ($positions) {
            return $positions[$a] <=> $positions[$b];
        });

        $stack = [];
        foreach ($indices as $i) {
            if ($directions[$i] === 'R') {
                $stack[] = $i;
            } else {
                while (!empty($stack) && $h[$i] > 0) {
                    $topIdx = $stack[count($stack) - 1];
                    if ($h[$topIdx] > $h[$i]) {
                        $h[$topIdx] -= 1;
                        $h[$i] = 0;
                    } else if ($h[$topIdx] < $h[$i]) {
                        $h[$topIdx] = 0;
                        $h[$i] -= 1;
                        array_pop($stack);
                    } else {
                        $h[$topIdx] = 0;
                        $h[$i] = 0;
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
        let dirs = Array(directions)
        var indices = Array(0..<n)
        indices.sort { positions[$0] < positions[$1] }

        var stack = [Int]()
        for i in indices {
            if dirs[i] == "R" {
                stack.append(i)
            } else {
                while !stack.isEmpty && h[i] > 0 {
                    let topIdx = stack.last!
                    if h[topIdx] > h[i] {
                        h[topIdx] -= 1
                        h[i] = 0
                    } else if h[topIdx] < h[i] {
                        h[topIdx] = 0
                        h[i] -= 1
                        stack.removeLast()
                    } else {
                        h[topIdx] = 0
                        h[i] = 0
                        stack.removeLast()
                    }
                }
            }
        }

        var result = [Int]()
        for i in 0..<n {
            if h[i] > 0 {
                result.append(h[i])
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
class Solution {
    fun survivedRobotsHealths(positions: IntArray, healths: IntArray, directions: String): List<Int> {
        val n = positions.size
        val indices = Array(n) { it }
        indices.sortBy { positions[it] }

        val h = healths.copyOf()
        val stack = mutableListOf<Int>()

        for (i in indices) {
            if (directions[i] == 'R') {
                stack.add(i)
            } else {
                while (stack.isNotEmpty() && h[i] > 0) {
                    val topIdx = stack.last()
                    if (h[topIdx] > h[i]) {
                        h[topIdx] -= 1
                        h[i] = 0
                    } else if (h[topIdx] < h[i]) {
                        h[topIdx] = 0
                        h[i] -= 1
                        stack.removeAt(stack.size - 1)
                    } else {
                        h[topIdx] = 0
                        h[i] = 0
                        stack.removeAt(stack.size - 1)
                    }
                }
            }
        }

        val result = mutableListOf<Int>()
        for (i in 0 until n) {
            if (h[i] > 0) {
                result.add(h[i])
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
class Solution {
  List<int> survivedRobotsHealths(List<int> positions, List<int> healths, String directions) {
    int n = positions.length;
    List<int> indices = List.generate(n, (index) => index);
    indices.sort((a, b) => positions[a].compareTo(positions[b]));

    List<int> h = List.from(healths);
    List<int> stack = [];

    for (int i in indices) {
      if (directions[i] == 'R') {
        stack.add(i);
      } else {
        while (stack.isNotEmpty && h[i] > 0) {
          int topIdx = stack.last;
          if (h[topIdx] > h[i]) {
            h[topIdx] -= 1;
            h[i] = 0;
          } else if (h[topIdx] < h[i]) {
            h[topIdx] = 0;
            h[i] -= 1;
            stack.removeLast();
          } else {
            h[topIdx] = 0;
            h[i] = 0;
            stack.removeLast();
          }
        }
      }
    }

    List<int> result = [];
    for (int i = 0; i < n; i++) {
      if (h[i] > 0) {
        result.add(h[i]);
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
import (
    "sort"
)

func survivedRobotsHealths(positions []int, healths []int, directions string) []int {
    n := len(positions)
    indices := make([]int, n)
    for i := 0; i < n; i++ {
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
                if h[topIdx] > h[i] {
                    h[topIdx] -= 1
                    h[i] = 0
                } else if h[topIdx] < h[i] {
                    h[topIdx] = 0
                    h[i] -= 1
                    stack = stack[:len(stack)-1]
                } else {
                    h[topIdx] = 0
                    h[i] = 0
                    stack = stack[:len(stack)-1]
                }
            }
        }
    }

    result := []int{}
    for i := 0; i < n; i++ {
        if h[i] > 0 {
            result = append(result, h[i])
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
  n = positions.length
  indices = (0...n).to_a.sort_by { |i| positions[i] }
  stack = []
  indices.each do |i|
    if directions[i] == 'R'
      stack.push(i)
    else
      while !stack.empty? && healths[i] > 0
        j = stack.pop
        if healths[i] > healths[j]
          healths[i] -= 1
          healths[j] = 0
        elsif healths[i] < healths[j]
          healths[j] -= 1
          healths[i] = 0
          stack.push(j)
        else
          healths[i] = 0
          healths[j] = 0
        end
      end
    end
  end
  healths.select { |h| h > 0 }
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
                    val top = stack.pop()
                    if (h(i) > h(top)) {
                        h(i) -= 1
                        h(top) = 0
                    } else if (h(i) < h(top)) {
                        h(top) -= 1
                        h(i) = 0
                        stack.push(top)
                    } else {
                        h(i) = 0
                        h(top) = 0
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
    pub fn survived_robots_healths(positions: Vec<i32>, mut healths: Vec<i32>, directions: String) -> Vec<i32> {
        let n = positions.len();
        let mut indices: Vec<usize> = (0..n).collect();
        indices.sort_by_key(|&i| positions[i]);
        let mut stack: Vec<usize> = Vec::new();
        let dirs: Vec<char> = directions.chars().collect();
        for &i in &indices {
            if dirs[i] == 'R' {
                stack.push(i);
            } else {
                while let Some(&top) = stack.last() {
                    if healths[i] > healths[top] {
                        healths[i] -= 1;
                        healths[top] = 0;
                        stack.pop();
                    } else if healths[i] < healths[top] {
                        healths[top] -= 1;
                        healths[i] = 0;
                        break;
                    } else {
                        healths[i] = 0;
                        healths[top] = 0;
                        stack.pop();
                        break;
                    }
                }
            }
        }
        healths.into_iter().filter(|&h| h > 0).collect()
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
         [dirs (string->list directions)]
         [robots (sort (for/list ([p positions] [h healths] [d dirs] [i (in-range n)])
                         (list p h d i))
                       < #:key first)]
         [collide (lambda (h stack)
                    (let loop ([h h] [stack stack])
                      (cond
                        [(or (empty? stack) (<= h 0)) (values h stack)]
                        [else
                         (let* ([top (first stack)]
                                [sh (second top)])
                           (cond
                             [(> h sh) (loop (- h 1) (rest stack))]
                             [(< h sh) (values 0 (cons (list (first top) (- sh 1) (third top) (fourth top)) (rest stack)))]
                             [else (values 0 (rest stack))]))])))]
         [final-survivors
          (let loop ([robots robots] [stack '()] [survivors '()])
            (if (empty? robots)
                (append (map (lambda (x) (list (fourth x) (second x))) stack) survivors)
                (let* ([curr (first robots)]
                       [h (second curr)]
                       [d (third curr)]
                       [i (fourth curr)])
                  (if (char=? d #\R)
                      (loop (rest robots) (cons curr stack) survivors)
                      (let-values ([(rem-h new-stack) (collide h stack)])
                        (if (> rem-h 0)
                            (loop (rest robots) new-stack (cons (list i rem-h) survivors))
                            (loop (rest robots) new-stack survivors)))))))]
         [sorted-survivors (sort final-survivors < #:key first)])
    (map second sorted-survivors)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec survived_robots_healths(Positions :: [integer()], Healths :: [integer()], Directions :: unicode:unicode_binary()) -> [integer()].
survived_robots_healths(Positions, Healths, Directions) ->
  N = length(Positions),
  Dirs = binary_to_list(Directions),
  Indices = lists:seq(0, N - 1),
  RobotDetails = lists:zip3(Healths, Dirs, Indices),
  Robots = lists:sort(lists:zip(Positions, RobotDetails)),
  FinalMap = process_robots(Robots, [], #{}),
  [maps:get(I, FinalMap) || I <- Indices, maps:is_key(I, FinalMap)].

process_robots([], Stack, Survivors) ->
  lists:foldl(fn({H, _D, I}, Acc) -> Acc#{I => H} end, Survivors, Stack);
process_robots([{_P, {H, $R, I}} | Rest], Stack, Survivors) ->
  process_robots(Rest, [{H, $R, I} | Stack], Survivors);
process_robots([{_P, {H, $L, I}} | Rest], Stack, Survivors) ->
  case collide(H, Stack) of
    {0, NewStack} -> process_robots(Rest, NewStack, Survivors);
    {NewH, NewStack} -> process_robots(Rest, NewStack, Survivors#{I => NewH})
  end.

collide(H, []) -> {H, []};
collide(H, [{SH, SD, SI} | SRest]) ->
  if
    H > SH -> collide(H - 1, SRest);
    H < SH -> {0, [{SH - 1, SD, SI} | SRest]};
    true -> {0, SRest}
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
    dirs = String.graphemes(directions)
    robots = Enum.zip([positions, healths, dirs, 0..(n-1)])
    |> Enum.sort_by(fn {pos, _, _, _} -> pos end)

    final_healths = process_robots(robots, [], %{})

    0..(n-1)
    |> Enum.map(fn i -> Map.get(final_healths, i) end)
    |> Enum.reject(&is_nil/1)
  end

  defp process_robots([], stack, survivors) do
    Enum.reduce(stack, survivors, fn {_, h, _, idx}, acc -> Map.put(acc, idx, h) end)
  end

  defp process_robots([{_, h, "R", idx} | rest], stack, survivors) do
    process_robots(rest, [{0, h, "R", idx} | stack], survivors)
  end

  defp process_robots([{_, h, "L", idx} | rest], stack, survivors) do
    {rem_h, new_stack} = collide(h, stack)
    if rem_h > 0 do
      process_robots(rest, new_stack, Map.put(survivors, idx, rem_h))
    else
      process_robots(rest, new_stack, survivors)
    end
  end

  defp collide(h, []) do
    {h, []}
  end

  defp collide(h, [{pos, sh, dir, idx} | rest]) do
    cond do
      h > sh -> collide(h - 1, rest)
      h < sh -> {0, [{pos, sh - 1, dir, idx} | rest]}
      true -> {0, rest}
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n log n) because we must sort the robots by their positions. The collision simulation takes O(n) time as each robot is pushed onto and popped from the stack at most once.
- **Space Complexity:** O(n) to store the indices of the robots, the sorted order, and the stack used for collision management.
