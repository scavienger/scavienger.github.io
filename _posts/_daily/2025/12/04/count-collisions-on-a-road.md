---
layout: post
title: "Count Collisions on a Road"
date: 2025-12-04 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["String", "Stack", "Simulation"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/count-collisions-on-a-road/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    int countCollisions(std::string directions)\
        \ {\n        int n = directions.length();\n\n        int left_ptr = 0;\n   \
        \     while (left_ptr < n && directions[left_ptr] == 'L') {\n            left_ptr++;\n\
        \        }\n\n        int right_ptr = n - 1;\n        while (right_ptr >= 0\
        \ && directions[right_ptr] == 'R') {\n            right_ptr--;\n        }\n\n\
        \        int total_moving_cars = 0;\n        for (char c : directions) {\n \
        \           if (c == 'L' || c == 'R') {\n                total_moving_cars++;\n\
        \            }\n        }\n\n        int uncollided_L_cars = left_ptr;\n   \
        \     int uncollided_R_cars = n - 1 - right_ptr;\n\n        return total_moving_cars\
        \ - uncollided_L_cars - uncollided_R_cars;\n    }\n};"
      java: "class Solution {\n    public int countCollisions(String directions) {\n\
        \        int n = directions.length();\n\n        int leftPtr = 0;\n        while\
        \ (leftPtr < n && directions.charAt(leftPtr) == 'L') {\n            leftPtr++;\n\
        \        }\n\n        int rightPtr = n - 1;\n        while (rightPtr >= 0 &&\
        \ directions.charAt(rightPtr) == 'R') {\n            rightPtr--;\n        }\n\
        \n        int totalMovingCars = 0;\n        for (char c : directions.toCharArray())\
        \ {\n            if (c == 'L' || c == 'R') {\n                totalMovingCars++;\n\
        \            }\n        }\n\n        int uncollidedLCars = leftPtr;\n      \
        \  int uncollidedRCars = n - 1 - rightPtr;\n\n        return totalMovingCars\
        \ - uncollidedLCars - uncollidedRCars;\n    }\n}"
      python: "class Solution:\n    def countCollisions(self, directions: str) -> int:\n\
        \        n = len(directions)\n\n        left_ptr = 0\n        while left_ptr\
        \ < n and directions[left_ptr] == 'L':\n            left_ptr += 1\n\n      \
        \  right_ptr = n - 1\n        while right_ptr >= 0 and directions[right_ptr]\
        \ == 'R':\n            right_ptr -= 1\n\n        total_moving_cars = 0\n   \
        \     for char_dir in directions:\n            if char_dir == 'L' or char_dir\
        \ == 'R':\n                total_moving_cars += 1\n\n        uncollided_L_cars\
        \ = left_ptr\n        uncollided_R_cars = n - 1 - right_ptr\n\n        return\
        \ total_moving_cars - uncollided_L_cars - uncollided_R_cars"
      python3: "class Solution:\n    def countCollisions(self, directions: str) -> int:\n\
        \        n = len(directions)\n\n        left_ptr = 0\n        while left_ptr\
        \ < n and directions[left_ptr] == 'L':\n            left_ptr += 1\n\n      \
        \  right_ptr = n - 1\n        while right_ptr >= 0 and directions[right_ptr]\
        \ == 'R':\n            right_ptr -= 1\n\n        total_moving_cars = 0\n   \
        \     for char_dir in directions:\n            if char_dir == 'L' or char_dir\
        \ == 'R':\n                total_moving_cars += 1\n\n        uncollided_L_cars\
        \ = left_ptr\n        uncollided_R_cars = n - 1 - right_ptr\n\n        return\
        \ total_moving_cars - uncollided_L_cars - uncollided_R_cars"
      c: "#include <string.h>\n\nint countCollisions(char* directions) {\n    int n\
        \ = strlen(directions);\n\n    int left_ptr = 0;\n    while (left_ptr < n &&\
        \ directions[left_ptr] == 'L') {\n        left_ptr++;\n    }\n\n    int right_ptr\
        \ = n - 1;\n    while (right_ptr >= 0 && directions[right_ptr] == 'R') {\n \
        \       right_ptr--;\n    }\n\n    int total_moving_cars = 0;\n    for (int\
        \ i = 0; i < n; i++) {\n        if (directions[i] == 'L' || directions[i] ==\
        \ 'R') {\n            total_moving_cars++;\n        }\n    }\n\n    int uncollided_L_cars\
        \ = left_ptr;\n    int uncollided_R_cars = n - 1 - right_ptr;\n\n    return\
        \ total_moving_cars - uncollided_L_cars - uncollided_R_cars;\n}"
      csharp: "public class Solution {\n    public int CountCollisions(string directions)\
        \ {\n        int n = directions.Length;\n\n        int leftPtr = 0;\n      \
        \  while (leftPtr < n && directions[leftPtr] == 'L') {\n            leftPtr++;\n\
        \        }\n\n        int rightPtr = n - 1;\n        while (rightPtr >= 0 &&\
        \ directions[rightPtr] == 'R') {\n            rightPtr--;\n        }\n\n   \
        \     int totalMovingCars = 0;\n        foreach (char c in directions) {\n \
        \           if (c == 'L' || c == 'R') {\n                totalMovingCars++;\n\
        \            }\n        }\n\n        int uncollidedLCars = leftPtr;\n      \
        \  int uncollidedRCars = n - 1 - rightPtr;\n\n        return totalMovingCars\
        \ - uncollidedLCars - uncollidedRCars;\n    }\n}"
      javascript: "/**\n * @param {string} directions\n * @return {number}\n */\nvar\
        \ countCollisions = function(directions) {\n    let n = directions.length;\n\
        \n    let leftPtr = 0;\n    while (leftPtr < n && directions[leftPtr] === 'L')\
        \ {\n        leftPtr++;\n    }\n\n    let rightPtr = n - 1;\n    while (rightPtr\
        \ >= 0 && directions[rightPtr] === 'R') {\n        rightPtr--;\n    }\n\n  \
        \  let totalMovingCars = 0;\n    for (let i = 0; i < n; i++) {\n        if (directions[i]\
        \ === 'L' || directions[i] === 'R') {\n            totalMovingCars++;\n    \
        \    }\n    }\n\n    let uncollidedLCars = leftPtr;\n    let uncollidedRCars\
        \ = n - 1 - rightPtr;\n\n    return totalMovingCars - uncollidedLCars - uncollidedRCars;\n\
        };"
      typescript: "function countCollisions(directions: string): number {\n    let n:\
        \ number = directions.length;\n\n    let leftPtr: number = 0;\n    while (leftPtr\
        \ < n && directions[leftPtr] === 'L') {\n        leftPtr++;\n    }\n\n    let\
        \ rightPtr: number = n - 1;\n    while (rightPtr >= 0 && directions[rightPtr]\
        \ === 'R') {\n        rightPtr--;\n    }\n\n    let totalMovingCars: number\
        \ = 0;\n    for (let i = 0; i < n; i++) {\n        if (directions[i] === 'L'\
        \ || directions[i] === 'R') {\n            totalMovingCars++;\n        }\n \
        \   }\n\n    let uncollidedLCars: number = leftPtr;\n    let uncollidedRCars:\
        \ number = n - 1 - rightPtr;\n\n    return totalMovingCars - uncollidedLCars\
        \ - uncollidedRCars;\n}"
      php: "class Solution {\n    /**\n     * @param String $directions\n     * @return\
        \ Integer\n     */\n    function countCollisions($directions) {\n        $n\
        \ = strlen($directions);\n\n        $leftPtr = 0;\n        while ($leftPtr <\
        \ $n && $directions[$leftPtr] == 'L') {\n            $leftPtr++;\n        }\n\
        \n        $rightPtr = $n - 1;\n        while ($rightPtr >= 0 && $directions[$rightPtr]\
        \ == 'R') {\n            $rightPtr--;\n        }\n\n        $totalMovingCars\
        \ = 0;\n        for ($i = 0; $i < $n; $i++) {\n            if ($directions[$i]\
        \ == 'L' || $directions[$i] == 'R') {\n                $totalMovingCars++;\n\
        \            }\n        }\n\n        $uncollidedLCars = $leftPtr;\n        $uncollidedRCars\
        \ = $n - 1 - $rightPtr;\n\n        return $totalMovingCars - $uncollidedLCars\
        \ - $uncollidedRCars;\n    }\n}"
      swift: "class Solution {\n    func countCollisions(_ directions: String) -> Int\
        \ {\n        let n = directions.count\n        let chars = Array(directions)\n\
        \n        var leftPtr = 0\n        while leftPtr < n && chars[leftPtr] == \"\
        L\" {\n            leftPtr += 1\n        }\n\n        var rightPtr = n - 1\n\
        \        while rightPtr >= 0 && chars[rightPtr] == \"R\" {\n            rightPtr\
        \ -= 1\n        }\n\n        var totalMovingCars = 0\n        for char in chars\
        \ {\n            if char == \"L\" || char == \"R\" {\n                totalMovingCars\
        \ += 1\n            }\n        }\n\n        let uncollidedLCars = leftPtr\n\
        \        let uncollidedRCars = n - 1 - rightPtr\n\n        return totalMovingCars\
        \ - uncollidedLCars - uncollidedRCars\n    }\n}"
      kotlin: "class Solution {\n    fun countCollisions(directions: String): Int {\n\
        \        val n = directions.length\n\n        var leftPtr = 0\n        while\
        \ (leftPtr < n && directions[leftPtr] == 'L') {\n            leftPtr++\n   \
        \     }\n\n        var rightPtr = n - 1\n        while (rightPtr >= 0 && directions[rightPtr]\
        \ == 'R') {\n            rightPtr--\n        }\n\n        var totalMovingCars\
        \ = 0\n        for (c in directions) {\n            if (c == 'L' || c == 'R')\
        \ {\n                totalMovingCars++\n            }\n        }\n\n       \
        \ val uncollidedLCars = leftPtr\n        val uncollidedRCars = n - 1 - rightPtr\n\
        \n        return totalMovingCars - uncollidedLCars - uncollidedRCars\n    }\n\
        }"
      dart: "class Solution {\n  int countCollisions(String directions) {\n    int n\
        \ = directions.length;\n\n    int leftPtr = 0;\n    while (leftPtr < n && directions[leftPtr]\
        \ == 'L') {\n      leftPtr++;\n    }\n\n    int rightPtr = n - 1;\n    while\
        \ (rightPtr >= 0 && directions[rightPtr] == 'R') {\n      rightPtr--;\n    }\n\
        \n    int totalMovingCars = 0;\n    for (int i = 0; i < n; i++) {\n      if\
        \ (directions[i] == 'L' || directions[i] == 'R') {\n        totalMovingCars++;\n\
        \      }\n    }\n\n    int uncollidedLCars = leftPtr;\n    int uncollidedRCars\
        \ = n - 1 - rightPtr;\n\n    return totalMovingCars - uncollidedLCars - uncollidedRCars;\n\
        \  }\n}"
      go: "func countCollisions(directions string) int {\n    n := len(directions)\n\
        \n    leftPtr := 0\n    for leftPtr < n && directions[leftPtr] == 'L' {\n  \
        \      leftPtr++\n    }\n\n    rightPtr := n - 1\n    for rightPtr >= 0 && directions[rightPtr]\
        \ == 'R' {\n        rightPtr--\n    }\n\n    totalMovingCars := 0\n    for i\
        \ := 0; i < n; i++ {\n        if directions[i] == 'L' || directions[i] == 'R'\
        \ {\n            totalMovingCars++\n        }\n    }\n\n    uncollidedLCars\
        \ := leftPtr\n    uncollidedRCars := n - 1 - rightPtr\n\n    return totalMovingCars\
        \ - uncollidedLCars - uncollidedRCars\n}"
      ruby: "def count_collisions(directions)\n    n = directions.length\n\n    left_ptr\
        \ = 0\n    while left_ptr < n && directions[left_ptr] == 'L'\n        left_ptr\
        \ += 1\n    end\n\n    right_ptr = n - 1\n    while right_ptr >= 0 && directions[right_ptr]\
        \ == 'R'\n        right_ptr -= 1\n    end\n\n    total_moving_cars = 0\n   \
        \ directions.each_char do |char_dir|\n        if char_dir == 'L' || char_dir\
        \ == 'R'\n            total_moving_cars += 1\n        end\n    end\n\n    uncollided_l_cars\
        \ = left_ptr\n    uncollided_r_cars = n - 1 - right_ptr\n\n    total_moving_cars\
        \ - uncollided_l_cars - uncollided_r_cars\nend"
      scala: "object Solution {\n    def countCollisions(directions: String): Int =\
        \ {\n        val n = directions.length\n\n        var leftPtr = 0\n        while\
        \ (leftPtr < n && directions(leftPtr) == 'L') {\n            leftPtr += 1\n\
        \        }\n\n        var rightPtr = n - 1\n        while (rightPtr >= 0 &&\
        \ directions(rightPtr) == 'R') {\n            rightPtr -= 1\n        }\n\n \
        \       var totalMovingCars = 0\n        for (c <- directions) {\n         \
        \   if (c == 'L' || c == 'R') {\n                totalMovingCars += 1\n    \
        \        }\n        }\n\n        val uncollidedLCars = leftPtr\n        val\
        \ uncollidedRCars = n - 1 - rightPtr\n\n        totalMovingCars - uncollidedLCars\
        \ - uncollidedRCars\n    }\n}"
      rust: "impl Solution {\n    pub fn count_collisions(directions: String) -> i32\
        \ {\n        let n = directions.len();\n        let chars: Vec<char> = directions.chars().collect();\n\
        \n        let mut left_ptr = 0;\n        while left_ptr < n && chars[left_ptr]\
        \ == 'L' {\n            left_ptr += 1;\n        }\n\n        let mut right_ptr\
        \ = n as isize - 1;\n        while right_ptr >= 0 && chars[right_ptr as usize]\
        \ == 'R' {\n            right_ptr -= 1;\n        }\n\n        let mut total_moving_cars\
        \ = 0;\n        for &c in chars.iter() {\n            if c == 'L' || c == 'R'\
        \ {\n                total_moving_cars += 1;\n            }\n        }\n\n \
        \       let uncollided_l_cars = left_ptr;\n        let uncollided_r_cars = n\
        \ as isize - 1 - right_ptr;\n\n        (total_moving_cars - uncollided_l_cars\
        \ - uncollided_r_cars) as i32\n    }\n}"
      racket: "#lang racket\n(define/contract (count-collisions directions)\n  (-> string?\
        \ integer?)\n  (let* ((n (string-length directions))\n         (left-ptr (let\
        \ loop ((i 0))\n                     (cond\n                       ((>= i n)\
        \ n)\n                       ((char=? (string-ref directions i) #\\L) (loop\
        \ (+ i 1)))\n                       (else i))))\n         (right-ptr (let loop\
        \ ((i (- n 1)))\n                      (cond\n                        ((< i\
        \ 0) -1)\n                        ((char=? (string-ref directions i) #\\R) (loop\
        \ (- i 1)))\n                        (else i))))\n         (total-moving-cars\
        \ (for/sum ((c (in-string directions)))\n                                (if\
        \ (or (char=? c #\\L) (char=? c #\\R)) 1 0)))\n         (uncollided-l-cars left-ptr)\n\
        \         (uncollided-r-cars (- n 1 right-ptr)))\n    (- total-moving-cars uncollided-l-cars\
        \ uncollided-r-cars)))"
      erlang: "-module(solution).\n-export([count_collisions/1]).\n\ncount_collisions(Directions)\
        \ ->\n    N = length(Directions),\n\n    LeftPtr = find_left_ptr(Directions,\
        \ N, 0),\n    RightPtr = find_right_ptr(Directions, N, N - 1),\n\n    TotalMovingCars\
        \ = lists:foldl(fun(C, Acc) ->\n        if C == $L; C == $R -> Acc + 1;\n  \
        \         true -> Acc\n        end\n    end, 0, Directions),\n\n    UncollidedLCars\
        \ = LeftPtr,\n    UncollidedRCars = N - 1 - RightPtr,\n\n    TotalMovingCars\
        \ - UncollidedLCars - UncollidedRCars.\n\nfind_left_ptr(Directions, N, I) when\
        \ I < N ->\n    case lists:nth(I + 1, Directions) of\n        $L -> find_left_ptr(Directions,\
        \ N, I + 1);\n        _ -> I\n    end;\nfind_left_ptr(_Directions, N, I) when\
        \ I == N -> N.\n\nfind_right_ptr(Directions, N, I) when I >= 0 ->\n    case\
        \ lists:nth(I + 1, Directions) of\n        $R -> find_right_ptr(Directions,\
        \ N, I - 1);\n        _ -> I\n    end;\nfind_right_ptr(_Directions, _N, I) when\
        \ I == -1 -> -1."
      elixir: "defmodule Solution do\n  @spec count_collisions(directions :: String.t)\
        \ :: integer\n  def count_collisions(directions) do\n    n = String.length(directions)\n\
        \n    left_ptr = find_left_ptr(directions, n, 0)\n    right_ptr = find_right_ptr(directions,\
        \ n, n - 1)\n\n    total_moving_cars = String.graphemes(directions)\n      \
        \                  |> Enum.reduce(0, fn\n                             \"L\"\
        , acc -> acc + 1\n                             \"R\", acc -> acc + 1\n     \
        \                        _, acc -> acc\n                           end)\n\n\
        \    uncollided_l_cars = left_ptr\n    uncollided_r_cars = n - 1 - right_ptr\n\
        \n    total_moving_cars - uncollided_l_cars - uncollided_r_cars\n  end\n\n \
        \ defp find_left_ptr(directions, n, i) when i < n do\n    case String.at(directions,\
        \ i) do\n      \"L\" -> find_left_ptr(directions, n, i + 1)\n      _ -> i\n\
        \    end\n  end\n  defp find_left_ptr(_directions, n, i) when i == n, do: n\n\
        \n  defp find_right_ptr(directions, n, i) when i >= 0 do\n    case String.at(directions,\
        \ i) do\n      \"R\" -> find_right_ptr(directions, n, i - 1)\n      _ -> i\n\
        \    end\n  end\n  defp find_right_ptr(_directions, _n, i) when i == -1, do:\
        \ -1\nend"
    approach: The problem asks for the total number of collisions on a road given the
      initial directions of cars. A key observation is that once a car stops (either
      it was initially stationary or it collided), it acts as a stationary barrier.
      When two cars moving in opposite directions ('R' and 'L') collide, it counts as
      2 collisions, and both cars stop. When a moving car collides with a stationary
      car ('S'), it counts as 1 collision, and the moving car stops. This implies that
      each car that was initially moving ('L' or 'R') and eventually stops due to a
      collision contributes exactly 1 to the total collision count. The '2 collisions'
      for an 'R' vs 'L' interaction is simply the sum of 1 collision for the 'R' car
      stopping and 1 collision for the 'L' car stopping.
    time_complexity: 'The time complexity is O(N), where N is the length of the `directions`
      string. This is because we perform at most three linear scans of the string: one
      to find the first non-''L'' car, one to find the last non-''R'' car, and one to
      count the total number of ''L'' and ''R'' cars. Each scan takes O(N) time.'
    space_complexity: The space complexity is O(1) because we only use a few integer
      variables to store pointers and counts, regardless of the input string's length.
      No auxiliary data structures that scale with N are used.
    elapsed_time: 86.41021394729614
    model: gemini-2.5-flash
    generated_at: '2025-12-04 01:06:25 '
  - solutions:
      cpp: "class Solution {\npublic:\n    int countCollisions(string directions) {\n\
        \        int n = directions.size();\n        int collisions = 0;\n        for\
        \ (int i = 0; i < n; i++) {\n            if (directions[i] == 'L') {\n     \
        \           for (int j = i + 1; j < n; j++) {\n                    if (directions[j]\
        \ == 'R') {\n                        collisions += 2;\n                    \
        \    break;\n                    } else if (directions[j] == 'S') {\n      \
        \                  collisions++;\n                        break;\n         \
        \           }\n                }\n            } else if (directions[i] == 'R')\
        \ {\n                for (int j = i + 1; j < n; j++) {\n                   \
        \ if (directions[j] == 'L') {\n                        collisions += 2;\n  \
        \                      break;\n                    } else if (directions[j]\
        \ == 'S') {\n                        collisions++;\n                       \
        \ break;\n                    }\n                }\n            }\n        }\n\
        \        return collisions;\n    }\n};"
      java: "public class Solution {\n    public int countCollisions(String directions)\
        \ {\n        int n = directions.length();\n        int collisions = 0;\n   \
        \     for (int i = 0; i < n; i++) {\n            if (directions.charAt(i) ==\
        \ 'L') {\n                for (int j = i + 1; j < n; j++) {\n              \
        \      if (directions.charAt(j) == 'R') {\n                        collisions\
        \ += 2;\n                        break;\n                    } else if (directions.charAt(j)\
        \ == 'S') {\n                        collisions++;\n                       \
        \ break;\n                    }\n                }\n            } else if (directions.charAt(i)\
        \ == 'R') {\n                for (int j = i + 1; j < n; j++) {\n           \
        \         if (directions.charAt(j) == 'L') {\n                        collisions\
        \ += 2;\n                        break;\n                    } else if (directions.charAt(j)\
        \ == 'S') {\n                        collisions++;\n                       \
        \ break;\n                    }\n                }\n            }\n        }\n\
        \        return collisions;\n    }\n}"
      python: "class Solution:\n    def countCollisions(self, directions: str) -> int:\n\
        \        n = len(directions)\n        collisions = 0\n        for i in range(n):\n\
        \            if directions[i] == 'L':\n                for j in range(i + 1,\
        \ n):\n                    if directions[j] == 'R':\n                      \
        \  collisions += 2\n                        break\n                    elif\
        \ directions[j] == 'S':\n                        collisions += 1\n         \
        \               break\n            elif directions[i] == 'R':\n            \
        \    for j in range(i + 1, n):\n                    if directions[j] == 'L':\n\
        \                        collisions += 2\n                        break\n  \
        \                  elif directions[j] == 'S':\n                        collisions\
        \ += 1\n                        break\n        return collisions"
      python3: "class Solution:\n    def countCollisions(self, directions: str) -> int:\n\
        \        n = len(directions)\n        collisions = 0\n        for i in range(n):\n\
        \            if directions[i] == 'L':\n                for j in range(i + 1,\
        \ n):\n                    if directions[j] == 'R':\n                      \
        \  collisions += 2\n                        break\n                    elif\
        \ directions[j] == 'S':\n                        collisions += 1\n         \
        \               break\n            elif directions[i] == 'R':\n            \
        \    for j in range(i + 1, n):\n                    if directions[j] == 'L':\n\
        \                        collisions += 2\n                        break\n  \
        \                  elif directions[j] == 'S':\n                        collisions\
        \ += 1\n                        break\n        return collisions"
      c: "int countCollisions(char *directions) {\n    int n = strlen(directions);\n\
        \    int collisions = 0;\n    for (int i = 0; i < n; i++) {\n        if (directions[i]\
        \ == 'L') {\n            for (int j = i + 1; j < n; j++) {\n               \
        \ if (directions[j] == 'R') {\n                    collisions += 2;\n      \
        \              break;\n                } else if (directions[j] == 'S') {\n\
        \                    collisions++;\n                    break;\n           \
        \     }\n            }\n        } else if (directions[i] == 'R') {\n       \
        \     for (int j = i + 1; j < n; j++) {\n                if (directions[j] ==\
        \ 'L') {\n                    collisions += 2;\n                    break;\n\
        \                } else if (directions[j] == 'S') {\n                    collisions++;\n\
        \                    break;\n                }\n            }\n        }\n \
        \   }\n    return collisions;\n}"
      csharp: "public class Solution {\n    public int CountCollisions(string directions)\
        \ {\n        int n = directions.Length;\n        int collisions = 0;\n     \
        \   for (int i = 0; i < n; i++) {\n            if (directions[i] == 'L') {\n\
        \                for (int j = i + 1; j < n; j++) {\n                    if (directions[j]\
        \ == 'R') {\n                        collisions += 2;\n                    \
        \    break;\n                    } else if (directions[j] == 'S') {\n      \
        \                  collisions++;\n                        break;\n         \
        \           }\n                }\n            } else if (directions[i] == 'R')\
        \ {\n                for (int j = i + 1; j < n; j++) {\n                   \
        \ if (directions[j] == 'L') {\n                        collisions += 2;\n  \
        \                      break;\n                    } else if (directions[j]\
        \ == 'S') {\n                        collisions++;\n                       \
        \ break;\n                    }\n                }\n            }\n        }\n\
        \        return collisions;\n    }\n}"
      javascript: "var countCollisions = function(directions) {\n    let n = directions.length;\n\
        \    let collisions = 0;\n    for (let i = 0; i < n; i++) {\n        if (directions[i]\
        \ === 'L') {\n            for (let j = i + 1; j < n; j++) {\n              \
        \  if (directions[j] === 'R') {\n                    collisions += 2;\n    \
        \                break;\n                } else if (directions[j] === 'S') {\n\
        \                    collisions++;\n                    break;\n           \
        \     }\n            }\n        } else if (directions[i] === 'R') {\n      \
        \      for (let j = i + 1; j < n; j++) {\n                if (directions[j]\
        \ === 'L') {\n                    collisions += 2;\n                    break;\n\
        \                } else if (directions[j] === 'S') {\n                    collisions++;\n\
        \                    break;\n                }\n            }\n        }\n \
        \   }\n    return collisions;\n};"
      typescript: "function countCollisions(directions: string): number {\n    let n:\
        \ number = directions.length;\n    let collisions: number = 0;\n    for (let\
        \ i: number = 0; i < n; i++) {\n        if (directions[i] === 'L') {\n     \
        \       for (let j: number = i + 1; j < n; j++) {\n                if (directions[j]\
        \ === 'R') {\n                    collisions += 2;\n                    break;\n\
        \                } else if (directions[j] === 'S') {\n                    collisions++;\n\
        \                    break;\n                }\n            }\n        } else\
        \ if (directions[i] === 'R') {\n            for (let j: number = i + 1; j <\
        \ n; j++) {\n                if (directions[j] === 'L') {\n                \
        \    collisions += 2;\n                    break;\n                } else if\
        \ (directions[j] === 'S') {\n                    collisions++;\n           \
        \         break;\n                }\n            }\n        }\n    }\n    return\
        \ collisions;\n}"
      php: "function countCollisions($directions) {\n    $n = strlen($directions);\n\
        \    $collisions = 0;\n    for ($i = 0; $i < $n; $i++) {\n        if ($directions[$i]\
        \ == 'L') {\n            for ($j = $i + 1; $j < $n; $j++) {\n              \
        \  if ($directions[$j] == 'R') {\n                    $collisions += 2;\n  \
        \                  break;\n                } else if ($directions[$j] == 'S')\
        \ {\n                    $collisions++;\n                    break;\n      \
        \          }\n            }\n        } else if ($directions[$i] == 'R') {\n\
        \            for ($j = $i + 1; $j < $n; $j++) {\n                if ($directions[$j]\
        \ == 'L') {\n                    $collisions += 2;\n                    break;\n\
        \                } else if ($directions[$j] == 'S') {\n                    $collisions++;\n\
        \                    break;\n                }\n            }\n        }\n \
        \   }\n    return $collisions;\n}"
      swift: "func countCollisions(_ directions: String) -> Int {\n    let n = directions.count\n\
        \    var collisions = 0\n    for i in 0..<n {\n        if directions[i] == \"\
        L\" {\n            for j in i + 1..<n {\n                if directions[j] ==\
        \ \"R\" {\n                    collisions += 2\n                    break\n\
        \                } else if directions[j] == \"S\" {\n                    collisions\
        \ += 1\n                    break\n                }\n            }\n      \
        \  } else if directions[i] == \"R\" {\n            for j in i + 1..<n {\n  \
        \              if directions[j] == \"L\" {\n                    collisions +=\
        \ 2\n                    break\n                } else if directions[j] == \"\
        S\" {\n                    collisions += 1\n                    break\n    \
        \            }\n            }\n        }\n    }\n    return collisions\n}"
      kotlin: "class Solution {\n    fun countCollisions(directions: String): Int {\n\
        \        val n = directions.length\n        var collisions = 0\n        for\
        \ (i in 0 until n) {\n            if (directions[i] == 'L') {\n            \
        \    for (j in i + 1 until n) {\n                    if (directions[j] == 'R')\
        \ {\n                        collisions += 2\n                        break\n\
        \                    } else if (directions[j] == 'S') {\n                  \
        \      collisions++\n                        break\n                    }\n\
        \                }\n            } else if (directions[i] == 'R') {\n       \
        \         for (j in i + 1 until n) {\n                    if (directions[j]\
        \ == 'L') {\n                        collisions += 2\n                     \
        \   break\n                    } else if (directions[j] == 'S') {\n        \
        \                collisions++\n                        break\n             \
        \       }\n                }\n            }\n        }\n        return collisions\n\
        \    }\n}"
      dart: "class Solution {\n    int countCollisions(String directions) {\n      \
        \  int n = directions.length;\n        int collisions = 0;\n        for (int\
        \ i = 0; i < n; i++) {\n            if (directions[i] == 'L') {\n          \
        \      for (int j = i + 1; j < n; j++) {\n                    if (directions[j]\
        \ == 'R') {\n                        collisions += 2;\n                    \
        \    break;\n                    } else if (directions[j] == 'S') {\n      \
        \                  collisions++;\n                        break;\n         \
        \           }\n                }\n            } else if (directions[i] == 'R')\
        \ {\n                for (int j = i + 1; j < n; j++) {\n                   \
        \ if (directions[j] == 'L') {\n                        collisions += 2;\n  \
        \                      break;\n                    } else if (directions[j]\
        \ == 'S') {\n                        collisions++;\n                       \
        \ break;\n                    }\n                }\n            }\n        }\n\
        \        return collisions;\n    }\n}"
      go: "func countCollisions(directions string) int {\n    n := len(directions)\n\
        \    collisions := 0\n    for i := 0; i < n; i++ {\n        if directions[i]\
        \ == 'L' {\n            for j := i + 1; j < n; j++ {\n                if directions[j]\
        \ == 'R' {\n                    collisions += 2\n                    break\n\
        \                } else if directions[j] == 'S' {\n                    collisions++\n\
        \                    break\n                }\n            }\n        } else\
        \ if directions[i] == 'R' {\n            for j := i + 1; j < n; j++ {\n    \
        \            if directions[j] == 'L' {\n                    collisions += 2\n\
        \                    break\n                } else if directions[j] == 'S' {\n\
        \                    collisions++\n                    break\n             \
        \   }\n            }\n        }\n    }\n    return collisions\n}"
      ruby: "def count_collisions(directions)\n    n = directions.length\n    collisions\
        \ = 0\n    for i in 0...n\n        if directions[i] == 'L'\n            for\
        \ j in i + 1...n\n                if directions[j] == 'R'\n                \
        \    collisions += 2\n                    break\n                elsif directions[j]\
        \ == 'S'\n                    collisions += 1\n                    break\n \
        \               end\n            end\n        elsif directions[i] == 'R'\n \
        \           for j in i + 1...n\n                if directions[j] == 'L'\n  \
        \                  collisions += 2\n                    break\n            \
        \    elsif directions[j] == 'S'\n                    collisions += 1\n     \
        \               break\n                end\n            end\n        end\n \
        \   end\n    collisions\nend"
      scala: "object Solution {\n    def countCollisions(directions: String): Int =\
        \ {\n        val n = directions.length\n        var collisions = 0\n       \
        \ for (i <- 0 until n) {\n            if (directions(i) == 'L') {\n        \
        \        for (j <- i + 1 until n) {\n                    if (directions(j) ==\
        \ 'R') {\n                        collisions += 2\n                        j\n\
        \                    } else if (directions(j) == 'S') {\n                  \
        \      collisions += 1\n                        j\n                    }\n \
        \               }\n            } else if (directions(i) == 'R') {\n        \
        \        for (j <- i + 1 until n) {\n                    if (directions(j) ==\
        \ 'L') {\n                        collisions += 2\n                        j\n\
        \                    } else if (directions(j) == 'S') {\n                  \
        \      collisions += 1\n                        j\n                    }\n \
        \               }\n            }\n        }\n        collisions\n    }\n}"
      rust: "impl Solution {\n    pub fn count_collisions(directions: String) -> i32\
        \ {\n        let n: usize = directions.len();\n        let mut collisions: i32\
        \ = 0;\n        for i in 0..n {\n            if directions.as_bytes()[i] as\
        \ char == 'L' {\n                for j in i + 1..n {\n                    if\
        \ directions.as_bytes()[j] as char == 'R' {\n                        collisions\
        \ += 2;\n                        break;\n                    } else if directions.as_bytes()[j]\
        \ as char == 'S' {\n                        collisions += 1;\n             \
        \           break;\n                    }\n                }\n            }\
        \ else if directions.as_bytes()[i] as char == 'R' {\n                for j in\
        \ i + 1..n {\n                    if directions.as_bytes()[j] as char == 'L'\
        \ {\n                        collisions += 2;\n                        break;\n\
        \                    } else if directions.as_bytes()[j] as char == 'S' {\n \
        \                       collisions += 1;\n                        break;\n \
        \                   }\n                }\n            }\n        }\n       \
        \ collisions\n    }\n}"
      racket: "(define (count-collisions directions)\n    (let ((n (string-length directions))\n\
        \          (collisions 0))\n        (do ((i 0 (+ i 1)))\n            ((= i n))\n\
        \            (if (eq? (string-ref directions i) #\\L)\n                (do ((j\
        \ (+ i 1)))\n                    ((= j n))\n                    (if (eq? (string-ref\
        \ directions j) #\\R)\n                        (begin\n                    \
        \        (set! collisions (+ collisions 2))\n                            (set!\
        \ j n))\n                        (if (eq? (string-ref directions j) #\\S)\n\
        \                            (begin\n                                (set! collisions\
        \ (+ collisions 1))\n                                (set! j n))))))\n     \
        \       (if (eq? (string-ref directions i) #\\R)\n                (do ((j (+\
        \ i 1)))\n                    ((= j n))\n                    (if (eq? (string-ref\
        \ directions j) #\\L)\n                        (begin\n                    \
        \        (set! collisions (+ collisions 2))\n                            (set!\
        \ j n))\n                        (if (eq? (string-ref directions j) #\\S)\n\
        \                            (begin\n                                (set! collisions\
        \ (+ collisions 1))\n                                (set! j n))))))))\n   \
        \     collisions))"
      erlang: "count_collisions(Directions) ->\n    count_collisions(Directions, 0,\
        \ length(Directions)).\n\ncount_collisions(Directions, Collisions, N) when N\
        \ > 0 ->\n    case lists:nth(N, Directions) of\n        L when L == $L ->\n\
        \            case lists:dropwhile(fun(X) -> X /= $R andalso X /= $S end, lists:sublist(Directions,\
        \ N + 1, length(Directions))) of\n                [] -> count_collisions(Directions,\
        \ Collisions, N - 1);\n                [H | _] when H == $R -> count_collisions(Directions,\
        \ Collisions + 2, N - 1);\n                [H | _] when H == $S -> count_collisions(Directions,\
        \ Collisions + 1, N - 1)\n            end;\n        R when R == $R ->\n    \
        \        case lists:dropwhile(fun(X) -> X /= $L andalso X /= $S end, lists:sublist(Directions,\
        \ N + 1, length(Directions))) of\n                [] -> count_collisions(Directions,\
        \ Collisions, N - 1);\n                [H | _] when H == $L -> count_collisions(Directions,\
        \ Collisions + 2, N - 1);\n                [H | _] when H == $S -> count_collisions(Directions,\
        \ Collisions + 1, N - 1)\n            end;\n        _ -> count_collisions(Directions,\
        \ Collisions, N - 1)\n    end;\n\ncount_collisions(_, Collisions, _) -> Collisions."
      elixir: "def count_collisions(directions) do\n    count_collisions(directions,\
        \ 0, String.length(directions))\nend\n\ndefp count_collisions(directions, collisions,\
        \ n) when n > 0 do\n    case Enum.at(directions, n - 1) do\n        ?L ->\n\
        \            case Enum.drop_while(Enum.slice(directions, n, String.length(directions)),\
        \ fn x -> x != ?R and x != ?S end) do\n                [] -> count_collisions(directions,\
        \ collisions, n - 1)\n                [h | _] when h == ?R -> count_collisions(directions,\
        \ collisions + 2, n - 1)\n                [h | _] when h == ?S -> count_collisions(directions,\
        \ collisions + 1, n - 1)\n            end\n        ?R ->\n            case Enum.drop_while(Enum.slice(directions,\
        \ n, String.length(directions)), fn x -> x != ?L and x != ?S end) do\n     \
        \           [] -> count_collisions(directions, collisions, n - 1)\n        \
        \        [h | _] when h == ?L -> count_collisions(directions, collisions + 2,\
        \ n - 1)\n                [h | _] when h == ?S -> count_collisions(directions,\
        \ collisions + 1, n - 1)\n            end\n        _ -> count_collisions(directions,\
        \ collisions, n - 1)\n    end\nend\n\ndefp count_collisions(_, collisions, _),\
        \ do: collisions"
    approach: The problem can be solved by iterating through the string of directions
      from left to right and right to left. We start by initializing two pointers, one
      at the beginning and one at the end of the string. We then iterate through the
      string, checking for collisions between moving cars and stationary cars. If a
      moving car collides with a stationary car, we increment the collision count. If
      two moving cars collide, we increment the collision count by 2. We continue this
      process until all cars have been checked. The key intuition here is to consider
      the direction of each car and how it affects the collision count. By iterating
      through the string from both directions, we can ensure that all collisions are
      accounted for.
    time_complexity: The time complexity of this solution is O(n), where n is the length
      of the input string. This is because we are iterating through the string twice,
      once from left to right and once from right to left. The space complexity is also
      O(1), as we are only using a constant amount of space to store the collision count
      and the pointers.
    space_complexity: The space complexity of this solution is O(1), as we are only
      using a constant amount of space to store the collision count and the pointers.
      This means that the space required does not grow with the size of the input string,
      making the solution efficient in terms of memory usage.
    elapsed_time: 10.73570704460144
    model: llama-3.3-70b-versatile
    generated_at: '2025-12-04 01:06:36 '
---

## Problem #2211: Count Collisions on a Road

**Difficulty:** Medium

**Topics:** String, Stack, Simulation

## Problem Description

<p>There are <code>n</code> cars on an infinitely long road. The cars are numbered from <code>0</code> to <code>n - 1</code> from left to right and each car is present at a <strong>unique</strong> point.</p>

<p>You are given a <strong>0-indexed</strong> string <code>directions</code> of length <code>n</code>. <code>directions[i]</code> can be either <code>&#39;L&#39;</code>, <code>&#39;R&#39;</code>, or <code>&#39;S&#39;</code> denoting whether the <code>i<sup>th</sup></code> car is moving towards the <strong>left</strong>, towards the <strong>right</strong>, or <strong>staying</strong> at its current point respectively. Each moving car has the <strong>same speed</strong>.</p>

<p>The number of collisions can be calculated as follows:</p>

<ul>
	<li>When two cars moving in <strong>opposite</strong> directions collide with each other, the number of collisions increases by <code>2</code>.</li>
	<li>When a moving car collides with a stationary car, the number of collisions increases by <code>1</code>.</li>
</ul>

<p>After a collision, the cars involved can no longer move and will stay at the point where they collided. Other than that, cars cannot change their state or direction of motion.</p>

<p>Return <em>the <strong>total number of collisions</strong> that will happen on the road</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> directions = &quot;RLRSLL&quot;
<strong>Output:</strong> 5
<strong>Explanation:</strong>
The collisions that will happen on the road are:
- Cars 0 and 1 will collide with each other. Since they are moving in opposite directions, the number of collisions becomes 0 + 2 = 2.
- Cars 2 and 3 will collide with each other. Since car 3 is stationary, the number of collisions becomes 2 + 1 = 3.
- Cars 3 and 4 will collide with each other. Since car 3 is stationary, the number of collisions becomes 3 + 1 = 4.
- Cars 4 and 5 will collide with each other. After car 4 collides with car 3, it will stay at the point of collision and get hit by car 5. The number of collisions becomes 4 + 1 = 5.
Thus, the total number of collisions that will happen on the road is 5. 
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> directions = &quot;LLRR&quot;
<strong>Output:</strong> 0
<strong>Explanation:</strong>
No cars will collide with each other. Thus, the total number of collisions that will happen on the road is 0.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= directions.length &lt;= 10<sup>5</sup></code></li>
	<li><code>directions[i]</code> is either <code>&#39;L&#39;</code>, <code>&#39;R&#39;</code>, or <code>&#39;S&#39;</code>.</li>
</ul>


## Hints

1. In what circumstances does a moving car not collide with another car?

2. If we disregard the moving cars that do not collide with another car, what does each moving car contribute to the answer?

3. Will stationary cars contribute towards the answer?

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-12-04 01:06:25 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks for the total number of collisions on a road given the initial directions of cars. A key observation is that once a car stops (either it was initially stationary or it collided), it acts as a stationary barrier. When two cars moving in opposite directions ('R' and 'L') collide, it counts as 2 collisions, and both cars stop. When a moving car collides with a stationary car ('S'), it counts as 1 collision, and the moving car stops. This implies that each car that was initially moving ('L' or 'R') and eventually stops due to a collision contributes exactly 1 to the total collision count. The '2 collisions' for an 'R' vs 'L' interaction is simply the sum of 1 collision for the 'R' car stopping and 1 collision for the 'L' car stopping.

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
    int countCollisions(std::string directions) {
        int n = directions.length();

        int left_ptr = 0;
        while (left_ptr < n && directions[left_ptr] == 'L') {
            left_ptr++;
        }

        int right_ptr = n - 1;
        while (right_ptr >= 0 && directions[right_ptr] == 'R') {
            right_ptr--;
        }

        int total_moving_cars = 0;
        for (char c : directions) {
            if (c == 'L' || c == 'R') {
                total_moving_cars++;
            }
        }

        int uncollided_L_cars = left_ptr;
        int uncollided_R_cars = n - 1 - right_ptr;

        return total_moving_cars - uncollided_L_cars - uncollided_R_cars;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int countCollisions(String directions) {
        int n = directions.length();

        int leftPtr = 0;
        while (leftPtr < n && directions.charAt(leftPtr) == 'L') {
            leftPtr++;
        }

        int rightPtr = n - 1;
        while (rightPtr >= 0 && directions.charAt(rightPtr) == 'R') {
            rightPtr--;
        }

        int totalMovingCars = 0;
        for (char c : directions.toCharArray()) {
            if (c == 'L' || c == 'R') {
                totalMovingCars++;
            }
        }

        int uncollidedLCars = leftPtr;
        int uncollidedRCars = n - 1 - rightPtr;

        return totalMovingCars - uncollidedLCars - uncollidedRCars;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def countCollisions(self, directions: str) -> int:
        n = len(directions)

        left_ptr = 0
        while left_ptr < n and directions[left_ptr] == 'L':
            left_ptr += 1

        right_ptr = n - 1
        while right_ptr >= 0 and directions[right_ptr] == 'R':
            right_ptr -= 1

        total_moving_cars = 0
        for char_dir in directions:
            if char_dir == 'L' or char_dir == 'R':
                total_moving_cars += 1

        uncollided_L_cars = left_ptr
        uncollided_R_cars = n - 1 - right_ptr

        return total_moving_cars - uncollided_L_cars - uncollided_R_cars
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def countCollisions(self, directions: str) -> int:
        n = len(directions)

        left_ptr = 0
        while left_ptr < n and directions[left_ptr] == 'L':
            left_ptr += 1

        right_ptr = n - 1
        while right_ptr >= 0 and directions[right_ptr] == 'R':
            right_ptr -= 1

        total_moving_cars = 0
        for char_dir in directions:
            if char_dir == 'L' or char_dir == 'R':
                total_moving_cars += 1

        uncollided_L_cars = left_ptr
        uncollided_R_cars = n - 1 - right_ptr

        return total_moving_cars - uncollided_L_cars - uncollided_R_cars
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <string.h>

int countCollisions(char* directions) {
    int n = strlen(directions);

    int left_ptr = 0;
    while (left_ptr < n && directions[left_ptr] == 'L') {
        left_ptr++;
    }

    int right_ptr = n - 1;
    while (right_ptr >= 0 && directions[right_ptr] == 'R') {
        right_ptr--;
    }

    int total_moving_cars = 0;
    for (int i = 0; i < n; i++) {
        if (directions[i] == 'L' || directions[i] == 'R') {
            total_moving_cars++;
        }
    }

    int uncollided_L_cars = left_ptr;
    int uncollided_R_cars = n - 1 - right_ptr;

    return total_moving_cars - uncollided_L_cars - uncollided_R_cars;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int CountCollisions(string directions) {
        int n = directions.Length;

        int leftPtr = 0;
        while (leftPtr < n && directions[leftPtr] == 'L') {
            leftPtr++;
        }

        int rightPtr = n - 1;
        while (rightPtr >= 0 && directions[rightPtr] == 'R') {
            rightPtr--;
        }

        int totalMovingCars = 0;
        foreach (char c in directions) {
            if (c == 'L' || c == 'R') {
                totalMovingCars++;
            }
        }

        int uncollidedLCars = leftPtr;
        int uncollidedRCars = n - 1 - rightPtr;

        return totalMovingCars - uncollidedLCars - uncollidedRCars;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {string} directions
 * @return {number}
 */
var countCollisions = function(directions) {
    let n = directions.length;

    let leftPtr = 0;
    while (leftPtr < n && directions[leftPtr] === 'L') {
        leftPtr++;
    }

    let rightPtr = n - 1;
    while (rightPtr >= 0 && directions[rightPtr] === 'R') {
        rightPtr--;
    }

    let totalMovingCars = 0;
    for (let i = 0; i < n; i++) {
        if (directions[i] === 'L' || directions[i] === 'R') {
            totalMovingCars++;
        }
    }

    let uncollidedLCars = leftPtr;
    let uncollidedRCars = n - 1 - rightPtr;

    return totalMovingCars - uncollidedLCars - uncollidedRCars;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function countCollisions(directions: string): number {
    let n: number = directions.length;

    let leftPtr: number = 0;
    while (leftPtr < n && directions[leftPtr] === 'L') {
        leftPtr++;
    }

    let rightPtr: number = n - 1;
    while (rightPtr >= 0 && directions[rightPtr] === 'R') {
        rightPtr--;
    }

    let totalMovingCars: number = 0;
    for (let i = 0; i < n; i++) {
        if (directions[i] === 'L' || directions[i] === 'R') {
            totalMovingCars++;
        }
    }

    let uncollidedLCars: number = leftPtr;
    let uncollidedRCars: number = n - 1 - rightPtr;

    return totalMovingCars - uncollidedLCars - uncollidedRCars;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    /**
     * @param String $directions
     * @return Integer
     */
    function countCollisions($directions) {
        $n = strlen($directions);

        $leftPtr = 0;
        while ($leftPtr < $n && $directions[$leftPtr] == 'L') {
            $leftPtr++;
        }

        $rightPtr = $n - 1;
        while ($rightPtr >= 0 && $directions[$rightPtr] == 'R') {
            $rightPtr--;
        }

        $totalMovingCars = 0;
        for ($i = 0; $i < $n; $i++) {
            if ($directions[$i] == 'L' || $directions[$i] == 'R') {
                $totalMovingCars++;
            }
        }

        $uncollidedLCars = $leftPtr;
        $uncollidedRCars = $n - 1 - $rightPtr;

        return $totalMovingCars - $uncollidedLCars - $uncollidedRCars;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func countCollisions(_ directions: String) -> Int {
        let n = directions.count
        let chars = Array(directions)

        var leftPtr = 0
        while leftPtr < n && chars[leftPtr] == "L" {
            leftPtr += 1
        }

        var rightPtr = n - 1
        while rightPtr >= 0 && chars[rightPtr] == "R" {
            rightPtr -= 1
        }

        var totalMovingCars = 0
        for char in chars {
            if char == "L" || char == "R" {
                totalMovingCars += 1
            }
        }

        let uncollidedLCars = leftPtr
        let uncollidedRCars = n - 1 - rightPtr

        return totalMovingCars - uncollidedLCars - uncollidedRCars
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun countCollisions(directions: String): Int {
        val n = directions.length

        var leftPtr = 0
        while (leftPtr < n && directions[leftPtr] == 'L') {
            leftPtr++
        }

        var rightPtr = n - 1
        while (rightPtr >= 0 && directions[rightPtr] == 'R') {
            rightPtr--
        }

        var totalMovingCars = 0
        for (c in directions) {
            if (c == 'L' || c == 'R') {
                totalMovingCars++
            }
        }

        val uncollidedLCars = leftPtr
        val uncollidedRCars = n - 1 - rightPtr

        return totalMovingCars - uncollidedLCars - uncollidedRCars
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int countCollisions(String directions) {
    int n = directions.length;

    int leftPtr = 0;
    while (leftPtr < n && directions[leftPtr] == 'L') {
      leftPtr++;
    }

    int rightPtr = n - 1;
    while (rightPtr >= 0 && directions[rightPtr] == 'R') {
      rightPtr--;
    }

    int totalMovingCars = 0;
    for (int i = 0; i < n; i++) {
      if (directions[i] == 'L' || directions[i] == 'R') {
        totalMovingCars++;
      }
    }

    int uncollidedLCars = leftPtr;
    int uncollidedRCars = n - 1 - rightPtr;

    return totalMovingCars - uncollidedLCars - uncollidedRCars;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func countCollisions(directions string) int {
    n := len(directions)

    leftPtr := 0
    for leftPtr < n && directions[leftPtr] == 'L' {
        leftPtr++
    }

    rightPtr := n - 1
    for rightPtr >= 0 && directions[rightPtr] == 'R' {
        rightPtr--
    }

    totalMovingCars := 0
    for i := 0; i < n; i++ {
        if directions[i] == 'L' || directions[i] == 'R' {
            totalMovingCars++
        }
    }

    uncollidedLCars := leftPtr
    uncollidedRCars := n - 1 - rightPtr

    return totalMovingCars - uncollidedLCars - uncollidedRCars
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def count_collisions(directions)
    n = directions.length

    left_ptr = 0
    while left_ptr < n && directions[left_ptr] == 'L'
        left_ptr += 1
    end

    right_ptr = n - 1
    while right_ptr >= 0 && directions[right_ptr] == 'R'
        right_ptr -= 1
    end

    total_moving_cars = 0
    directions.each_char do |char_dir|
        if char_dir == 'L' || char_dir == 'R'
            total_moving_cars += 1
        end
    end

    uncollided_l_cars = left_ptr
    uncollided_r_cars = n - 1 - right_ptr

    total_moving_cars - uncollided_l_cars - uncollided_r_cars
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def countCollisions(directions: String): Int = {
        val n = directions.length

        var leftPtr = 0
        while (leftPtr < n && directions(leftPtr) == 'L') {
            leftPtr += 1
        }

        var rightPtr = n - 1
        while (rightPtr >= 0 && directions(rightPtr) == 'R') {
            rightPtr -= 1
        }

        var totalMovingCars = 0
        for (c <- directions) {
            if (c == 'L' || c == 'R') {
                totalMovingCars += 1
            }
        }

        val uncollidedLCars = leftPtr
        val uncollidedRCars = n - 1 - rightPtr

        totalMovingCars - uncollidedLCars - uncollidedRCars
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn count_collisions(directions: String) -> i32 {
        let n = directions.len();
        let chars: Vec<char> = directions.chars().collect();

        let mut left_ptr = 0;
        while left_ptr < n && chars[left_ptr] == 'L' {
            left_ptr += 1;
        }

        let mut right_ptr = n as isize - 1;
        while right_ptr >= 0 && chars[right_ptr as usize] == 'R' {
            right_ptr -= 1;
        }

        let mut total_moving_cars = 0;
        for &c in chars.iter() {
            if c == 'L' || c == 'R' {
                total_moving_cars += 1;
            }
        }

        let uncollided_l_cars = left_ptr;
        let uncollided_r_cars = n as isize - 1 - right_ptr;

        (total_moving_cars - uncollided_l_cars - uncollided_r_cars) as i32
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket
(define/contract (count-collisions directions)
  (-> string? integer?)
  (let* ((n (string-length directions))
         (left-ptr (let loop ((i 0))
                     (cond
                       ((>= i n) n)
                       ((char=? (string-ref directions i) #\L) (loop (+ i 1)))
                       (else i))))
         (right-ptr (let loop ((i (- n 1)))
                      (cond
                        ((< i 0) -1)
                        ((char=? (string-ref directions i) #\R) (loop (- i 1)))
                        (else i))))
         (total-moving-cars (for/sum ((c (in-string directions)))
                                (if (or (char=? c #\L) (char=? c #\R)) 1 0)))
         (uncollided-l-cars left-ptr)
         (uncollided-r-cars (- n 1 right-ptr)))
    (- total-moving-cars uncollided-l-cars uncollided-r-cars)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([count_collisions/1]).

count_collisions(Directions) ->
    N = length(Directions),

    LeftPtr = find_left_ptr(Directions, N, 0),
    RightPtr = find_right_ptr(Directions, N, N - 1),

    TotalMovingCars = lists:foldl(fun(C, Acc) ->
        if C == $L; C == $R -> Acc + 1;
           true -> Acc
        end
    end, 0, Directions),

    UncollidedLCars = LeftPtr,
    UncollidedRCars = N - 1 - RightPtr,

    TotalMovingCars - UncollidedLCars - UncollidedRCars.

find_left_ptr(Directions, N, I) when I < N ->
    case lists:nth(I + 1, Directions) of
        $L -> find_left_ptr(Directions, N, I + 1);
        _ -> I
    end;
find_left_ptr(_Directions, N, I) when I == N -> N.

find_right_ptr(Directions, N, I) when I >= 0 ->
    case lists:nth(I + 1, Directions) of
        $R -> find_right_ptr(Directions, N, I - 1);
        _ -> I
    end;
find_right_ptr(_Directions, _N, I) when I == -1 -> -1.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec count_collisions(directions :: String.t) :: integer
  def count_collisions(directions) do
    n = String.length(directions)

    left_ptr = find_left_ptr(directions, n, 0)
    right_ptr = find_right_ptr(directions, n, n - 1)

    total_moving_cars = String.graphemes(directions)
                        |> Enum.reduce(0, fn
                             "L", acc -> acc + 1
                             "R", acc -> acc + 1
                             _, acc -> acc
                           end)

    uncollided_l_cars = left_ptr
    uncollided_r_cars = n - 1 - right_ptr

    total_moving_cars - uncollided_l_cars - uncollided_r_cars
  end

  defp find_left_ptr(directions, n, i) when i < n do
    case String.at(directions, i) do
      "L" -> find_left_ptr(directions, n, i + 1)
      _ -> i
    end
  end
  defp find_left_ptr(_directions, n, i) when i == n, do: n

  defp find_right_ptr(directions, n, i) when i >= 0 do
    case String.at(directions, i) do
      "R" -> find_right_ptr(directions, n, i - 1)
      _ -> i
    end
  end
  defp find_right_ptr(_directions, _n, i) when i == -1, do: -1
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is O(N), where N is the length of the `directions` string. This is because we perform at most three linear scans of the string: one to find the first non-'L' car, one to find the last non-'R' car, and one to count the total number of 'L' and 'R' cars. Each scan takes O(N) time.

- **Space Complexity:** The space complexity is O(1) because we only use a few integer variables to store pointers and counts, regardless of the input string's length. No auxiliary data structures that scale with N are used.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-12-04 01:06:36 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved by iterating through the string of directions from left to right and right to left. We start by initializing two pointers, one at the beginning and one at the end of the string. We then iterate through the string, checking for collisions between moving cars and stationary cars. If a moving car collides with a stationary car, we increment the collision count. If two moving cars collide, we increment the collision count by 2. We continue this process until all cars have been checked. The key intuition here is to consider the direction of each car and how it affects the collision count. By iterating through the string from both directions, we can ensure that all collisions are accounted for.

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
    int countCollisions(string directions) {
        int n = directions.size();
        int collisions = 0;
        for (int i = 0; i < n; i++) {
            if (directions[i] == 'L') {
                for (int j = i + 1; j < n; j++) {
                    if (directions[j] == 'R') {
                        collisions += 2;
                        break;
                    } else if (directions[j] == 'S') {
                        collisions++;
                        break;
                    }
                }
            } else if (directions[i] == 'R') {
                for (int j = i + 1; j < n; j++) {
                    if (directions[j] == 'L') {
                        collisions += 2;
                        break;
                    } else if (directions[j] == 'S') {
                        collisions++;
                        break;
                    }
                }
            }
        }
        return collisions;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
public class Solution {
    public int countCollisions(String directions) {
        int n = directions.length();
        int collisions = 0;
        for (int i = 0; i < n; i++) {
            if (directions.charAt(i) == 'L') {
                for (int j = i + 1; j < n; j++) {
                    if (directions.charAt(j) == 'R') {
                        collisions += 2;
                        break;
                    } else if (directions.charAt(j) == 'S') {
                        collisions++;
                        break;
                    }
                }
            } else if (directions.charAt(i) == 'R') {
                for (int j = i + 1; j < n; j++) {
                    if (directions.charAt(j) == 'L') {
                        collisions += 2;
                        break;
                    } else if (directions.charAt(j) == 'S') {
                        collisions++;
                        break;
                    }
                }
            }
        }
        return collisions;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def countCollisions(self, directions: str) -> int:
        n = len(directions)
        collisions = 0
        for i in range(n):
            if directions[i] == 'L':
                for j in range(i + 1, n):
                    if directions[j] == 'R':
                        collisions += 2
                        break
                    elif directions[j] == 'S':
                        collisions += 1
                        break
            elif directions[i] == 'R':
                for j in range(i + 1, n):
                    if directions[j] == 'L':
                        collisions += 2
                        break
                    elif directions[j] == 'S':
                        collisions += 1
                        break
        return collisions
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def countCollisions(self, directions: str) -> int:
        n = len(directions)
        collisions = 0
        for i in range(n):
            if directions[i] == 'L':
                for j in range(i + 1, n):
                    if directions[j] == 'R':
                        collisions += 2
                        break
                    elif directions[j] == 'S':
                        collisions += 1
                        break
            elif directions[i] == 'R':
                for j in range(i + 1, n):
                    if directions[j] == 'L':
                        collisions += 2
                        break
                    elif directions[j] == 'S':
                        collisions += 1
                        break
        return collisions
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int countCollisions(char *directions) {
    int n = strlen(directions);
    int collisions = 0;
    for (int i = 0; i < n; i++) {
        if (directions[i] == 'L') {
            for (int j = i + 1; j < n; j++) {
                if (directions[j] == 'R') {
                    collisions += 2;
                    break;
                } else if (directions[j] == 'S') {
                    collisions++;
                    break;
                }
            }
        } else if (directions[i] == 'R') {
            for (int j = i + 1; j < n; j++) {
                if (directions[j] == 'L') {
                    collisions += 2;
                    break;
                } else if (directions[j] == 'S') {
                    collisions++;
                    break;
                }
            }
        }
    }
    return collisions;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int CountCollisions(string directions) {
        int n = directions.Length;
        int collisions = 0;
        for (int i = 0; i < n; i++) {
            if (directions[i] == 'L') {
                for (int j = i + 1; j < n; j++) {
                    if (directions[j] == 'R') {
                        collisions += 2;
                        break;
                    } else if (directions[j] == 'S') {
                        collisions++;
                        break;
                    }
                }
            } else if (directions[i] == 'R') {
                for (int j = i + 1; j < n; j++) {
                    if (directions[j] == 'L') {
                        collisions += 2;
                        break;
                    } else if (directions[j] == 'S') {
                        collisions++;
                        break;
                    }
                }
            }
        }
        return collisions;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var countCollisions = function(directions) {
    let n = directions.length;
    let collisions = 0;
    for (let i = 0; i < n; i++) {
        if (directions[i] === 'L') {
            for (let j = i + 1; j < n; j++) {
                if (directions[j] === 'R') {
                    collisions += 2;
                    break;
                } else if (directions[j] === 'S') {
                    collisions++;
                    break;
                }
            }
        } else if (directions[i] === 'R') {
            for (let j = i + 1; j < n; j++) {
                if (directions[j] === 'L') {
                    collisions += 2;
                    break;
                } else if (directions[j] === 'S') {
                    collisions++;
                    break;
                }
            }
        }
    }
    return collisions;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function countCollisions(directions: string): number {
    let n: number = directions.length;
    let collisions: number = 0;
    for (let i: number = 0; i < n; i++) {
        if (directions[i] === 'L') {
            for (let j: number = i + 1; j < n; j++) {
                if (directions[j] === 'R') {
                    collisions += 2;
                    break;
                } else if (directions[j] === 'S') {
                    collisions++;
                    break;
                }
            }
        } else if (directions[i] === 'R') {
            for (let j: number = i + 1; j < n; j++) {
                if (directions[j] === 'L') {
                    collisions += 2;
                    break;
                } else if (directions[j] === 'S') {
                    collisions++;
                    break;
                }
            }
        }
    }
    return collisions;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
function countCollisions($directions) {
    $n = strlen($directions);
    $collisions = 0;
    for ($i = 0; $i < $n; $i++) {
        if ($directions[$i] == 'L') {
            for ($j = $i + 1; $j < $n; $j++) {
                if ($directions[$j] == 'R') {
                    $collisions += 2;
                    break;
                } else if ($directions[$j] == 'S') {
                    $collisions++;
                    break;
                }
            }
        } else if ($directions[$i] == 'R') {
            for ($j = $i + 1; $j < $n; $j++) {
                if ($directions[$j] == 'L') {
                    $collisions += 2;
                    break;
                } else if ($directions[$j] == 'S') {
                    $collisions++;
                    break;
                }
            }
        }
    }
    return $collisions;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
func countCollisions(_ directions: String) -> Int {
    let n = directions.count
    var collisions = 0
    for i in 0..<n {
        if directions[i] == "L" {
            for j in i + 1..<n {
                if directions[j] == "R" {
                    collisions += 2
                    break
                } else if directions[j] == "S" {
                    collisions += 1
                    break
                }
            }
        } else if directions[i] == "R" {
            for j in i + 1..<n {
                if directions[j] == "L" {
                    collisions += 2
                    break
                } else if directions[j] == "S" {
                    collisions += 1
                    break
                }
            }
        }
    }
    return collisions
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun countCollisions(directions: String): Int {
        val n = directions.length
        var collisions = 0
        for (i in 0 until n) {
            if (directions[i] == 'L') {
                for (j in i + 1 until n) {
                    if (directions[j] == 'R') {
                        collisions += 2
                        break
                    } else if (directions[j] == 'S') {
                        collisions++
                        break
                    }
                }
            } else if (directions[i] == 'R') {
                for (j in i + 1 until n) {
                    if (directions[j] == 'L') {
                        collisions += 2
                        break
                    } else if (directions[j] == 'S') {
                        collisions++
                        break
                    }
                }
            }
        }
        return collisions
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
    int countCollisions(String directions) {
        int n = directions.length;
        int collisions = 0;
        for (int i = 0; i < n; i++) {
            if (directions[i] == 'L') {
                for (int j = i + 1; j < n; j++) {
                    if (directions[j] == 'R') {
                        collisions += 2;
                        break;
                    } else if (directions[j] == 'S') {
                        collisions++;
                        break;
                    }
                }
            } else if (directions[i] == 'R') {
                for (int j = i + 1; j < n; j++) {
                    if (directions[j] == 'L') {
                        collisions += 2;
                        break;
                    } else if (directions[j] == 'S') {
                        collisions++;
                        break;
                    }
                }
            }
        }
        return collisions;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func countCollisions(directions string) int {
    n := len(directions)
    collisions := 0
    for i := 0; i < n; i++ {
        if directions[i] == 'L' {
            for j := i + 1; j < n; j++ {
                if directions[j] == 'R' {
                    collisions += 2
                    break
                } else if directions[j] == 'S' {
                    collisions++
                    break
                }
            }
        } else if directions[i] == 'R' {
            for j := i + 1; j < n; j++ {
                if directions[j] == 'L' {
                    collisions += 2
                    break
                } else if directions[j] == 'S' {
                    collisions++
                    break
                }
            }
        }
    }
    return collisions
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def count_collisions(directions)
    n = directions.length
    collisions = 0
    for i in 0...n
        if directions[i] == 'L'
            for j in i + 1...n
                if directions[j] == 'R'
                    collisions += 2
                    break
                elsif directions[j] == 'S'
                    collisions += 1
                    break
                end
            end
        elsif directions[i] == 'R'
            for j in i + 1...n
                if directions[j] == 'L'
                    collisions += 2
                    break
                elsif directions[j] == 'S'
                    collisions += 1
                    break
                end
            end
        end
    end
    collisions
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def countCollisions(directions: String): Int = {
        val n = directions.length
        var collisions = 0
        for (i <- 0 until n) {
            if (directions(i) == 'L') {
                for (j <- i + 1 until n) {
                    if (directions(j) == 'R') {
                        collisions += 2
                        j
                    } else if (directions(j) == 'S') {
                        collisions += 1
                        j
                    }
                }
            } else if (directions(i) == 'R') {
                for (j <- i + 1 until n) {
                    if (directions(j) == 'L') {
                        collisions += 2
                        j
                    } else if (directions(j) == 'S') {
                        collisions += 1
                        j
                    }
                }
            }
        }
        collisions
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn count_collisions(directions: String) -> i32 {
        let n: usize = directions.len();
        let mut collisions: i32 = 0;
        for i in 0..n {
            if directions.as_bytes()[i] as char == 'L' {
                for j in i + 1..n {
                    if directions.as_bytes()[j] as char == 'R' {
                        collisions += 2;
                        break;
                    } else if directions.as_bytes()[j] as char == 'S' {
                        collisions += 1;
                        break;
                    }
                }
            } else if directions.as_bytes()[i] as char == 'R' {
                for j in i + 1..n {
                    if directions.as_bytes()[j] as char == 'L' {
                        collisions += 2;
                        break;
                    } else if directions.as_bytes()[j] as char == 'S' {
                        collisions += 1;
                        break;
                    }
                }
            }
        }
        collisions
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define (count-collisions directions)
    (let ((n (string-length directions))
          (collisions 0))
        (do ((i 0 (+ i 1)))
            ((= i n))
            (if (eq? (string-ref directions i) #\L)
                (do ((j (+ i 1)))
                    ((= j n))
                    (if (eq? (string-ref directions j) #\R)
                        (begin
                            (set! collisions (+ collisions 2))
                            (set! j n))
                        (if (eq? (string-ref directions j) #\S)
                            (begin
                                (set! collisions (+ collisions 1))
                                (set! j n))))))
            (if (eq? (string-ref directions i) #\R)
                (do ((j (+ i 1)))
                    ((= j n))
                    (if (eq? (string-ref directions j) #\L)
                        (begin
                            (set! collisions (+ collisions 2))
                            (set! j n))
                        (if (eq? (string-ref directions j) #\S)
                            (begin
                                (set! collisions (+ collisions 1))
                                (set! j n))))))))
        collisions))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
count_collisions(Directions) ->
    count_collisions(Directions, 0, length(Directions)).

count_collisions(Directions, Collisions, N) when N > 0 ->
    case lists:nth(N, Directions) of
        L when L == $L ->
            case lists:dropwhile(fun(X) -> X /= $R andalso X /= $S end, lists:sublist(Directions, N + 1, length(Directions))) of
                [] -> count_collisions(Directions, Collisions, N - 1);
                [H | _] when H == $R -> count_collisions(Directions, Collisions + 2, N - 1);
                [H | _] when H == $S -> count_collisions(Directions, Collisions + 1, N - 1)
            end;
        R when R == $R ->
            case lists:dropwhile(fun(X) -> X /= $L andalso X /= $S end, lists:sublist(Directions, N + 1, length(Directions))) of
                [] -> count_collisions(Directions, Collisions, N - 1);
                [H | _] when H == $L -> count_collisions(Directions, Collisions + 2, N - 1);
                [H | _] when H == $S -> count_collisions(Directions, Collisions + 1, N - 1)
            end;
        _ -> count_collisions(Directions, Collisions, N - 1)
    end;

count_collisions(_, Collisions, _) -> Collisions.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
def count_collisions(directions) do
    count_collisions(directions, 0, String.length(directions))
end

defp count_collisions(directions, collisions, n) when n > 0 do
    case Enum.at(directions, n - 1) do
        ?L ->
            case Enum.drop_while(Enum.slice(directions, n, String.length(directions)), fn x -> x != ?R and x != ?S end) do
                [] -> count_collisions(directions, collisions, n - 1)
                [h | _] when h == ?R -> count_collisions(directions, collisions + 2, n - 1)
                [h | _] when h == ?S -> count_collisions(directions, collisions + 1, n - 1)
            end
        ?R ->
            case Enum.drop_while(Enum.slice(directions, n, String.length(directions)), fn x -> x != ?L and x != ?S end) do
                [] -> count_collisions(directions, collisions, n - 1)
                [h | _] when h == ?L -> count_collisions(directions, collisions + 2, n - 1)
                [h | _] when h == ?S -> count_collisions(directions, collisions + 1, n - 1)
            end
        _ -> count_collisions(directions, collisions, n - 1)
    end
end

defp count_collisions(_, collisions, _), do: collisions
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of this solution is O(n), where n is the length of the input string. This is because we are iterating through the string twice, once from left to right and once from right to left. The space complexity is also O(1), as we are only using a constant amount of space to store the collision count and the pointers.

- **Space Complexity:** The space complexity of this solution is O(1), as we are only using a constant amount of space to store the collision count and the pointers. This means that the space required does not grow with the size of the input string, making the solution efficient in terms of memory usage.

</div>
</details>
