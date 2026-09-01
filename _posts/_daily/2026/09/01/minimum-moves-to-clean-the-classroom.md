---
layout: post
title: "Minimum Moves to Clean the Classroom"
date: 2026-09-01 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Hash Table", "Bit Manipulation", "Breadth-First Search", "Matrix"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/minimum-moves-to-clean-the-classroom/
ai_solutions:
  - solutions:
      cpp: '// Generation failed for C++

        // Reason: Parsing failed'
      java: '// Generation failed for Java

        // Reason: Parsing failed'
      python: '// Generation failed for Python

        // Reason: Parsing failed'
      python3: '// Generation failed for Python3

        // Reason: Parsing failed'
      c: '// Generation failed for C

        // Reason: Parsing failed'
      csharp: "using System;\nusing System.Collections.Generic;\n\npublic class Solution\
        \ {\n    public int MinMoves(string[] classroom, int energy) {\n        int\
        \ m = classroom.Length;\n        int n = classroom[0].Length;\n        int sr\
        \ = -1, sc = -1;\n        int[,] litterMap = new int[m, n];\n        int numLitters\
        \ = 0;\n\n        for (int i = 0; i < m; i++) {\n            for (int j = 0;\
        \ j < n; j++) {\n                litterMap[i, j] = -1;\n                if (classroom[i][j]\
        \ == 'S') {\n                    sr = i; sc = j;\n                } else if\
        \ (classroom[i][j] == 'L') {\n                    litterMap[i, j] = numLitters++;\n\
        \                }\n            }\n        }\n\n        int fullMask = (1 <<\
        \ numLitters) - 1;\n        if (fullMask == 0) return 0;\n\n        int maskSize\
        \ = 1 << numLitters;\n        int[] bestEnergy = new int[m * n * maskSize];\n\
        \        Array.Fill(bestEnergy, -1);\n\n        Queue<int> queue = new Queue<int>();\n\
        \        queue.Enqueue((sr << 21) | (sc << 16) | (0 << 6) | energy);\n     \
        \   bestEnergy[(sr * n + sc) * maskSize + 0] = energy;\n\n        int steps\
        \ = 0;\n        int[] dr = { -1, 1, 0, 0 };\n        int[] dc = { 0, 0, -1,\
        \ 1 };\n\n        while (queue.Count > 0) {\n            steps++;\n        \
        \    int size = queue.Count;\n            for (int i = 0; i < size; i++) {\n\
        \                int packed = queue.Dequeue();\n                int r = packed\
        \ >> 21;\n                int c = (packed >> 16) & 0x1F;\n                int\
        \ mask = (packed >> 6) & 0x3FF;\n                int e = packed & 0x3F;\n\n\
        \                if (e == 0 && classroom[r][c] != 'R') continue;\n\n       \
        \         for (int d = 0; d < 4; d++) {\n                    int nr = r + dr[d];\n\
        \                    int nc = c + dc[d];\n\n                    if (nr >= 0\
        \ && nr < m && nc >= 0 && nc < n && classroom[nr][nc] != 'X') {\n          \
        \              int ne = e - 1;\n                        if (ne < 0) continue;\n\
        \n                        int nm = mask;\n                        if (classroom[nr][nc]\
        \ == 'L') nm |= (1 << litterMap[nr, nc]);\n                        if (nm ==\
        \ fullMask) return steps;\n                        if (classroom[nr][nc] ==\
        \ 'R') ne = energy;\n\n                        int stateIdx = (nr * n + nc)\
        \ * maskSize + nm;\n                        if (ne > bestEnergy[stateIdx]) {\n\
        \                            bestEnergy[stateIdx] = ne;\n                  \
        \          queue.Enqueue((nr << 21) | (nc << 16) | (nm << 6) | ne);\n      \
        \                  }\n                    }\n                }\n           \
        \ }\n        }\n\n        return -1;\n    }\n}"
      javascript: "/**\n * @param {string[]} classroom\n * @param {number} energy\n\
        \ * @return {number}\n */\nvar minMoves = function(classroom, energy) {\n  \
        \  const m = classroom.length;\n    const n = classroom[0].length;\n    let\
        \ sr = -1, sc = -1;\n    const litterMap = Array.from({ length: m }, () => new\
        \ Int32Array(n).fill(-1));\n    let numLitters = 0;\n\n    for (let i = 0; i\
        \ < m; i++) {\n        for (let j = 0; j < n; j++) {\n            if (classroom[i][j]\
        \ === 'S') {\n                sr = i; sc = j;\n            } else if (classroom[i][j]\
        \ === 'L') {\n                litterMap[i][j] = numLitters++;\n            }\n\
        \        }\n    }\n\n    const fullMask = (1 << numLitters) - 1;\n    if (fullMask\
        \ === 0) return 0;\n\n    const maskSize = 1 << numLitters;\n    const bestEnergy\
        \ = new Int32Array(m * n * maskSize).fill(-1);\n\n    let currentLevel = [(sr\
        \ << 21) | (sc << 16) | (0 << 6) | energy];\n    bestEnergy[(sr * n + sc) *\
        \ maskSize + 0] = energy;\n\n    let steps = 0;\n    const dr = [-1, 1, 0, 0];\n\
        \    const dc = [0, 0, -1, 1];\n\n    while (currentLevel.length > 0) {\n  \
        \      steps++;\n        const nextLevel = [];\n        for (let i = 0; i <\
        \ currentLevel.length; i++) {\n            const packed = currentLevel[i];\n\
        \            const r = packed >> 21;\n            const c = (packed >> 16) &\
        \ 0x1F;\n            const mask = (packed >> 6) & 0x3FF;\n            const\
        \ e = packed & 0x3F;\n\n            if (e === 0 && classroom[r][c] !== 'R')\
        \ continue;\n\n            for (let d = 0; d < 4; d++) {\n                const\
        \ nr = r + dr[d];\n                const nc = c + dc[d];\n\n               \
        \ if (nr >= 0 && nr < m && nc >= 0 && nc < n && classroom[nr][nc] !== 'X') {\n\
        \                    let ne = e - 1;\n                    if (ne < 0) continue;\n\
        \n                    let nm = mask;\n                    if (classroom[nr][nc]\
        \ === 'L') nm |= (1 << litterMap[nr][nc]);\n                    if (nm === fullMask)\
        \ return steps;\n                    if (classroom[nr][nc] === 'R') ne = energy;\n\
        \n                    const stateIdx = (nr * n + nc) * maskSize + nm;\n    \
        \                if (ne > bestEnergy[stateIdx]) {\n                        bestEnergy[stateIdx]\
        \ = ne;\n                        nextLevel.push((nr << 21) | (nc << 16) | (nm\
        \ << 6) | ne);\n                    }\n                }\n            }\n  \
        \      }\n        currentLevel = nextLevel;\n    }\n\n    return -1;\n};"
      typescript: "function minMoves(classroom: string[], energy: number): number {\n\
        \    const m = classroom.length;\n    const n = classroom[0].length;\n    let\
        \ sr = -1, sc = -1;\n    const litterMap: number[][] = Array.from({ length:\
        \ m }, () => new Array(n).fill(-1));\n    let numLitters = 0;\n\n    for (let\
        \ i = 0; i < m; i++) {\n        for (let j = 0; j < n; j++) {\n            if\
        \ (classroom[i][j] === 'S') {\n                sr = i; sc = j;\n           \
        \ } else if (classroom[i][j] === 'L') {\n                litterMap[i][j] = numLitters++;\n\
        \            }\n        }\n    }\n\n    const fullMask = (1 << numLitters) -\
        \ 1;\n    if (fullMask === 0) return 0;\n\n    const maskSize = 1 << numLitters;\n\
        \    const bestEnergy = new Int32Array(m * n * maskSize).fill(-1);\n\n    let\
        \ currentLevel = [(sr << 21) | (sc << 16) | (0 << 6) | energy];\n    bestEnergy[(sr\
        \ * n + sc) * maskSize + 0] = energy;\n\n    let steps = 0;\n    const dr =\
        \ [-1, 1, 0, 0];\n    const dc = [0, 0, -1, 1];\n\n    while (currentLevel.length\
        \ > 0) {\n        steps++;\n        const nextLevel: number[] = [];\n      \
        \  for (let i = 0; i < currentLevel.length; i++) {\n            const packed\
        \ = currentLevel[i];\n            const r = packed >> 21;\n            const\
        \ c = (packed >> 16) & 0x1F;\n            const mask = (packed >> 6) & 0x3FF;\n\
        \            const e = packed & 0x3F;\n\n            if (e === 0 && classroom[r][c]\
        \ !== 'R') continue;\n\n            for (let d = 0; d < 4; d++) {\n        \
        \        const nr = r + dr[d];\n                const nc = c + dc[d];\n\n  \
        \              if (nr >= 0 && nr < m && nc >= 0 && nc < n && classroom[nr][nc]\
        \ !== 'X') {\n                    let ne = e - 1;\n                    if (ne\
        \ < 0) continue;\n\n                    let nm = mask;\n                   \
        \ if (classroom[nr][nc] === 'L') nm |= (1 << litterMap[nr][nc]);\n         \
        \           if (nm === fullMask) return steps;\n                    if (classroom[nr][nc]\
        \ === 'R') ne = energy;\n\n                    const stateIdx = (nr * n + nc)\
        \ * maskSize + nm;\n                    if (ne > bestEnergy[stateIdx]) {\n \
        \                       bestEnergy[stateIdx] = ne;\n                       \
        \ nextLevel.push((nr << 21) | (nc << 16) | (nm << 6) | ne);\n              \
        \      }\n                }\n            }\n        }\n        currentLevel\
        \ = nextLevel;\n    }\n\n    return -1;\n};"
      php: "class Solution {\n\n    /**\n     * @param String[] $classroom\n     * @param\
        \ Integer $energy\n     * @return Integer\n     */\n    function minMoves($classroom,\
        \ $energy) {\n        $m = count($classroom);\n        $n = strlen($classroom[0]);\n\
        \        $sr = $sc = -1;\n        $litterMap = [];\n        $numLitters = 0;\n\
        \n        for ($i = 0; $i < $m; $i++) {\n            $litterMap[$i] = array_fill(0,\
        \ $n, -1);\n            for ($j = 0; $j < $n; $j++) {\n                if ($classroom[$i][$j]\
        \ === 'S') {\n                    $sr = $i; $sc = $j;\n                } else\
        \ if ($classroom[$i][$j] === 'L') {\n                    $litterMap[$i][$j]\
        \ = $numLitters++;\n                }\n            }\n        }\n\n        $fullMask\
        \ = (1 << $numLitters) - 1;\n        if ($fullMask === 0) return 0;\n\n    \
        \    $maskSize = 1 << $numLitters;\n        $bestEnergy = new SplFixedArray($m\
        \ * $n * $maskSize);\n        for ($i = 0; $i < $bestEnergy->getSize(); $i++)\
        \ $bestEnergy[$i] = -1;\n\n        $currentLevel = [($sr << 21) | ($sc << 16)\
        \ | (0 << 6) | $energy];\n        $bestEnergy[($sr * $n + $sc) * $maskSize +\
        \ 0] = $energy;\n\n        $steps = 0;\n        $dr = [-1, 1, 0, 0];\n     \
        \   $dc = [0, 0, -1, 1];\n\n        while (!empty($currentLevel)) {\n      \
        \      $steps++;\n            $nextLevel = [];\n            foreach ($currentLevel\
        \ as $packed) {\n                $r = $packed >> 21;\n                $c = ($packed\
        \ >> 16) & 0x1F;\n                $mask = ($packed >> 6) & 0x3FF;\n        \
        \        $e = $packed & 0x3F;\n\n                if ($e === 0 && $classroom[$r][$c]\
        \ !== 'R') continue;\n\n                for ($d = 0; $d < 4; $d++) {\n     \
        \               $nr = $r + $dr[$d];\n                    $nc = $c + $dc[$d];\n\
        \n                    if ($nr >= 0 && $nr < $m && $nc >= 0 && $nc < $n && $classroom[$nr][$nc]\
        \ !== 'X') {\n                        $ne = $e - 1;\n                      \
        \  if ($ne < 0) continue;\n\n                        $nm = $mask;\n        \
        \                if ($classroom[$nr][$nc] === 'L') $nm |= (1 << $litterMap[$nr][$nc]);\n\
        \                        if ($nm === $fullMask) return $steps;\n           \
        \             if ($classroom[$nr][$nc] === 'R') $ne = $energy;\n\n         \
        \               $stateIdx = ($nr * $n + $nc) * $maskSize + $nm;\n          \
        \              if ($ne > $bestEnergy[$stateIdx]) {\n                       \
        \     $bestEnergy[$stateIdx] = $ne;\n                            $nextLevel[]\
        \ = ($nr << 21) | ($nc << 16) | ($nm << 6) | $ne;\n                        }\n\
        \                    }\n                }\n            }\n            $currentLevel\
        \ = $nextLevel;\n        }\n\n        return -1;\n    }\n}"
      swift: "class Solution {\n    func minMoves(_ classroom: [String], _ energy: Int)\
        \ -> Int {\n        let m = classroom.count\n        let n = classroom[0].count\n\
        \        let grid = classroom.map { Array($0) }\n        var sr = -1, sc = -1\n\
        \        var litterMap = Array(repeating: Array(repeating: -1, count: n), count:\
        \ m)\n        var numLitters = 0\n\n        for i in 0..<m {\n            for\
        \ j in 0..<n {\n                if grid[i][j] == \"S\" {\n                 \
        \   sr = i; sc = j\n                } else if grid[i][j] == \"L\" {\n      \
        \              litterMap[i][j] = numLitters\n                    numLitters\
        \ += 1\n                }\n            }\n        }\n\n        let fullMask\
        \ = (1 << numLitters) - 1\n        if fullMask == 0 { return 0 }\n\n       \
        \ let maskSize = 1 << numLitters\n        var bestEnergy = Array(repeating:\
        \ Int8(-1), count: m * n * maskSize)\n\n        var currentLevel: [Int32] =\
        \ [Int32((sr << 21) | (sc << 16) | (0 << 6) | energy)]\n        bestEnergy[(sr\
        \ * n + sc) * maskSize + 0] = Int8(energy)\n\n        var steps = 0\n      \
        \  let dr = [-1, 1, 0, 0]\n        let dc = [0, 0, -1, 1]\n\n        while !currentLevel.isEmpty\
        \ {\n            steps += 1\n            var nextLevel: [Int32] = []\n     \
        \       for packed in currentLevel {\n                let r = Int(packed >>\
        \ 21)\n                let c = Int((packed >> 16) & 0x1F)\n                let\
        \ mask = Int((packed >> 6) & 0x3FF)\n                let e = Int(packed & 0x3F)\n\
        \n                if e == 0 && grid[r][c] != \"R\" { continue }\n\n        \
        \        for d in 0..<4 {\n                    let nr = r + dr[d]\n        \
        \            let nc = c + dc[d]\n\n                    if nr >= 0 && nr < m\
        \ && nc >= 0 && nc < n && grid[nr][nc] != \"X\" {\n                        var\
        \ ne = e - 1\n                        if ne < 0 { continue }\n\n           \
        \             var nm = mask\n                        if grid[nr][nc] == \"L\"\
        \ { nm |= (1 << litterMap[nr][nc]) }\n                        if nm == fullMask\
        \ { return steps }\n                        if grid[nr][nc] == \"R\" { ne =\
        \ energy }\n\n                        let stateIdx = (nr * n + nc) * maskSize\
        \ + nm\n                        if Int8(ne) > bestEnergy[stateIdx] {\n     \
        \                       bestEnergy[stateIdx] = Int8(ne)\n                  \
        \          nextLevel.append(Int32((nr << 21) | (nc << 16) | (nm << 6) | ne))\n\
        \                        }\n                    }\n                }\n     \
        \       }\n            currentLevel = nextLevel\n        }\n\n        return\
        \ -1\n    }\n}"
      kotlin: "import java.util.ArrayDeque\n\nclass Solution {\n    data class State(val\
        \ r: Int, val c: Int, val mask: Int, val e: Int, val steps: Int)\n\n    fun\
        \ minMoves(classroom: Array<String>, energy: Int): Int {\n        val m = classroom.size\n\
        \        val n = classroom[0].length\n        var sr = 0\n        var sc = 0\n\
        \        val litters = mutableListOf<Pair<Int, Int>>()\n        for (r in 0\
        \ until m) {\n            for (c in 0 until n) {\n                if (classroom[r][c]\
        \ == 'S') {\n                    sr = r\n                    sc = c\n      \
        \          } else if (classroom[r][c] == 'L') {\n                    litters.add(Pair(r,\
        \ c))\n                }\n            }\n        }\n\n        val numL = litters.size\n\
        \        val targetMask = (1 shl numL) - 1\n        if (targetMask == 0) return\
        \ 0\n\n        val litterMap = IntArray(m * n) { -1 }\n        for (i in 0 until\
        \ numL) {\n            litterMap[litters[i].first * n + litters[i].second] =\
        \ i\n        }\n\n        val bestEnergy = IntArray(m * n * (1 shl numL)) {\
        \ -1 }\n        val queue = ArrayDeque<State>()\n\n        queue.add(State(sr,\
        \ sc, 0, energy, 0))\n        bestEnergy[(sr * n + sc) * (1 shl numL) + 0] =\
        \ energy\n\n        val dr = intArrayOf(-1, 1, 0, 0)\n        val dc = intArrayOf(0,\
        \ 0, -1, 1)\n\n        while (queue.isNotEmpty()) {\n            val curr =\
        \ queue.poll()\n\n            for (i in 0 until 4) {\n                val nr\
        \ = curr.r + dr[i]\n                val nc = curr.c + dc[i]\n\n            \
        \    if (nr in 0 until m && nc in 0 until n && classroom[nr][nc] != 'X') {\n\
        \                    var ne = curr.e - 1\n                    if (ne < 0) continue\n\
        \n                    var nm = curr.mask\n                    val cell = classroom[nr][nc]\n\
        \                    if (cell == 'L') {\n                        nm = nm or\
        \ (1 shl litterMap[nr * n + nc])\n                    }\n\n                \
        \    if (nm == targetMask) return curr.steps + 1\n\n                    if (cell\
        \ == 'R') {\n                        ne = energy\n                    }\n\n\
        \                    val idx = (nr * n + nc) * (1 shl numL) + nm\n         \
        \           if (ne > bestEnergy[idx]) {\n                        bestEnergy[idx]\
        \ = ne\n                        queue.add(State(nr, nc, nm, ne, curr.steps +\
        \ 1))\n                    }\n                }\n            }\n        }\n\n\
        \        return -1\n    }\n}"
      dart: "import 'dart:collection';\n\nclass State {\n  final int r, c, mask, e,\
        \ steps;\n  State(this.r, this.c, this.mask, this.e, this.steps);\n}\n\nclass\
        \ Solution {\n  int minMoves(List<String> classroom, int energy) {\n    int\
        \ m = classroom.length;\n    int n = classroom[0].length;\n    int sr = 0, sc\
        \ = 0;\n    List<List<int>> litters = [];\n    for (int r = 0; r < m; r++) {\n\
        \      for (int c = 0; c < n; c++) {\n        if (classroom[r][c] == 'S') {\n\
        \          sr = r;\n          sc = c;\n        } else if (classroom[r][c] ==\
        \ 'L') {\n          litters.add([r, c]);\n        }\n      }\n    }\n\n    int\
        \ numL = litters.length;\n    int targetMask = (1 << numL) - 1;\n    if (targetMask\
        \ == 0) return 0;\n\n    List<int> litterMap = List.filled(m * n, -1);\n   \
        \ for (int i = 0; i < numL; i++) {\n      litterMap[litters[i][0] * n + litters[i][1]]\
        \ = i;\n    }\n\n    List<int> bestEnergy = List.filled(m * n * (1 << numL),\
        \ -1);\n    Queue<State> queue = Queue<State>();\n\n    queue.add(State(sr,\
        \ sc, 0, energy, 0));\n    bestEnergy[(sr * n + sc) * (1 << numL) + 0] = energy;\n\
        \n    List<int> dr = [-1, 1, 0, 0];\n    List<int> dc = [0, 0, -1, 1];\n\n \
        \   while (queue.isNotEmpty) {\n      State curr = queue.removeFirst();\n\n\
        \      for (int i = 0; i < 4; i++) {\n        int nr = curr.r + dr[i];\n   \
        \     int nc = curr.c + dc[i];\n\n        if (nr >= 0 && nr < m && nc >= 0 &&\
        \ nc < n && classroom[nr][nc] != 'X') {\n          int ne = curr.e - 1;\n  \
        \        if (ne < 0) continue;\n\n          int nm = curr.mask;\n          String\
        \ cell = classroom[nr][nc];\n          if (cell == 'L') {\n            nm |=\
        \ (1 << litterMap[nr * n + nc]);\n          }\n\n          if (nm == targetMask)\
        \ return curr.steps + 1;\n\n          if (cell == 'R') {\n            ne = energy;\n\
        \          }\n\n          int idx = (nr * n + nc) * (1 << numL) + nm;\n    \
        \      if (ne > bestEnergy[idx]) {\n            bestEnergy[idx] = ne;\n    \
        \        queue.add(State(nr, nc, nm, ne, curr.steps + 1));\n          }\n  \
        \      }\n      }\n    }\n\n    return -1;\n  }\n}"
      go: "func minMoves(classroom []string, energy int) int {\n    m := len(classroom)\n\
        \    n := len(classroom[0])\n    var sr, sc int\n    type pos struct{ r, c int\
        \ }\n    litters := []pos{}\n    for r := 0; r < m; r++ {\n        for c :=\
        \ 0; c < n; c++ {\n            if classroom[r][c] == 'S' {\n               \
        \ sr, sc = r, c\n            } else if classroom[r][c] == 'L' {\n          \
        \      litters = append(litters, pos{r, c})\n            }\n        }\n    }\n\
        \n    numL := len(litters)\n    targetMask := (1 << numL) - 1\n    if targetMask\
        \ == 0 {\n        return 0\n    }\n\n    litterMap := make([]int, m*n)\n   \
        \ for i := range litterMap { litterMap[i] = -1 }\n    for i, p := range litters\
        \ {\n        litterMap[p.r*n+p.c] = i\n    }\n\n    bestEnergy := make([]int,\
        \ m*n*(1<<numL))\n    for i := range bestEnergy { bestEnergy[i] = -1 }\n\n \
        \   type state struct {\n        r, c, mask, e, steps int\n    }\n    queue\
        \ := []state{{sr, sc, 0, energy, 0}}\n    bestEnergy[(sr*n+sc)*(1<<numL)] =\
        \ energy\n\n    dr := []int{-1, 1, 0, 0}\n    dc := []int{0, 0, -1, 1}\n\n \
        \   for len(queue) > 0 {\n        curr := queue[0]\n        queue = queue[1:]\n\
        \n        for i := 0; i < 4; i++ {\n            nr, nc := curr.r+dr[i], curr.c+dc[i]\n\
        \            if nr >= 0 && nr < m && nc >= 0 && nc < n && classroom[nr][nc]\
        \ != 'X' {\n                ne := curr.e - 1\n                if ne < 0 { continue\
        \ }\n\n                nm := curr.mask\n                cell := classroom[nr][nc]\n\
        \                if cell == 'L' {\n                    nm |= (1 << litterMap[nr*n+nc])\n\
        \                }\n\n                if nm == targetMask {\n              \
        \      return curr.steps + 1\n                }\n\n                if cell ==\
        \ 'R' {\n                    ne = energy\n                }\n\n            \
        \    idx := (nr*n+nc)*(1<<numL) + nm\n                if ne > bestEnergy[idx]\
        \ {\n                    bestEnergy[idx] = ne\n                    queue = append(queue,\
        \ state{nr, nc, nm, ne, curr.steps + 1})\n                }\n            }\n\
        \        }\n    }\n\n    return -1\n}"
      ruby: "# @param {String[]} classroom\n# @param {Integer} energy\n# @return {Integer}\n\
        def min_moves(classroom, energy)\n    m = classroom.length\n    n = classroom[0].length\n\
        \    sr, sc = 0, 0\n    litters = []\n    for r in 0...m\n        for c in 0...n\n\
        \            if classroom[r][c] == 'S'\n                sr, sc = r, c\n    \
        \        elsif classroom[r][c] == 'L'\n                litters << [r, c]\n \
        \           end\n        end\n    end\n\n    num_l = litters.length\n    target_mask\
        \ = (1 << num_l) - 1\n    return 0 if target_mask == 0\n\n    litter_map = Array.new(m\
        \ * n, -1)\n    litters.each_with_index do |(lr, lc), i|\n        litter_map[lr\
        \ * n + lc] = i\n    end\n\n    best_energy = Array.new(m * n * (1 << num_l),\
        \ -1)\n    queue = [[sr, sc, 0, energy, 0]]\n    best_energy[(sr * n + sc) *\
        \ (1 << num_l)] = energy\n\n    dr = [-1, 1, 0, 0]\n    dc = [0, 0, -1, 1]\n\
        \    head = 0\n\n    while head < queue.length\n        r, c, mask, e, steps\
        \ = queue[head]\n        head += 1\n\n        for i in 0...4\n            nr,\
        \ nc = r + dr[i], c + dc[i]\n            if nr >= 0 && nr < m && nc >= 0 &&\
        \ nc < n && classroom[nr][nc] != 'X'\n                ne = e - 1\n         \
        \       next if ne < 0\n\n                nm = mask\n                cell =\
        \ classroom[nr][nc]\n                if cell == 'L'\n                    nm\
        \ |= (1 << litter_map[nr * n + nc])\n                end\n\n               \
        \ return steps + 1 if nm == target_mask\n\n                ne = energy if cell\
        \ == 'R'\n                idx = (nr * n + nc) * (1 << num_l) + nm\n        \
        \        if ne > best_energy[idx]\n                    best_energy[idx] = ne\n\
        \                    queue << [nr, nc, nm, ne, steps + 1]\n                end\n\
        \            end\n        end\n    end\n\n    -1\nend"
      scala: "import scala.collection.mutable\n\nobject Solution {\n    case class State(r:\
        \ Int, c: Int, mask: Int, e: Int, steps: Int)\n\n    def minMoves(classroom:\
        \ Array[String], energy: Int): Int = {\n        val m = classroom.length\n \
        \       val n = classroom(0).length\n        var sr, sc = 0\n        val litters\
        \ = mutable.ListBuffer[(Int, Int)]()\n\n        for (r <- 0 until m; c <- 0\
        \ until n) {\n            if (classroom(r)(c) == 'S') {\n                sr\
        \ = r\n                sc = c\n            } else if (classroom(r)(c) == 'L')\
        \ {\n                litters += ((r, c))\n            }\n        }\n\n     \
        \   val numL = litters.size\n        val targetMask = (1 << numL) - 1\n    \
        \    if (targetMask == 0) return 0\n\n        val litterMap = Array.fill(m *\
        \ n)(-1)\n        for (i <- 0 until numL) {\n            litterMap(litters(i)._1\
        \ * n + litters(i)._2) = i\n        }\n\n        val bestEnergy = Array.fill(m\
        \ * n * (1 << numL))(-1)\n        val queue = mutable.Queue[State]()\n\n   \
        \     queue.enqueue(State(sr, sc, 0, energy, 0))\n        bestEnergy((sr * n\
        \ + sc) * (1 << numL)) = energy\n\n        val dr = Array(-1, 1, 0, 0)\n   \
        \     val dc = Array(0, 0, -1, 1)\n\n        while (queue.nonEmpty) {\n    \
        \        val curr = queue.dequeue()\n\n            for (i <- 0 until 4) {\n\
        \                val nr = curr.r + dr(i)\n                val nc = curr.c +\
        \ dc(i)\n\n                if (nr >= 0 && nr < m && nc >= 0 && nc < n && classroom(nr)(nc)\
        \ != 'X') {\n                    var ne = curr.e - 1\n                    if\
        \ (ne >= 0) {\n                        var nm = curr.mask\n                \
        \        val cell = classroom(nr)(nc)\n                        if (cell == 'L')\
        \ {\n                            nm |= (1 << litterMap(nr * n + nc))\n     \
        \                   }\n\n                        if (nm == targetMask) return\
        \ curr.steps + 1\n\n                        if (cell == 'R') {\n           \
        \                 ne = energy\n                        }\n\n               \
        \         val idx = (nr * n + nc) * (1 << numL) + nm\n                     \
        \   if (ne > bestEnergy(idx)) {\n                            bestEnergy(idx)\
        \ = ne\n                            queue.enqueue(State(nr, nc, nm, ne, curr.steps\
        \ + 1))\n                        }\n                    }\n                }\n\
        \            }\n        }\n\n        -1\n    }\n}"
      rust: "use std::collections::VecDeque;\n\nimpl Solution {\n    pub fn min_moves(classroom:\
        \ Vec<String>, energy: i32) -> i32 {\n        let m = classroom.len();\n   \
        \     let n = classroom[0].len();\n        let mut sr = 0;\n        let mut\
        \ sc = 0;\n        let mut litters = Vec::new();\n\n        for r in 0..m {\n\
        \            let bytes = classroom[r].as_bytes();\n            for c in 0..n\
        \ {\n                if bytes[c] == b'S' {\n                    sr = r;\n  \
        \                  sc = c;\n                } else if bytes[c] == b'L' {\n \
        \                   litters.push((r, c));\n                }\n            }\n\
        \        }\n\n        let litter_count = litters.len();\n        let target_mask\
        \ = (1 << litter_count) - 1;\n        if target_mask == 0 { return 0; }\n\n\
        \        let mut litter_map = [[-1i8; 20]; 20];\n        for (i, &(lr, lc))\
        \ in litters.iter().enumerate() {\n            litter_map[lr][lc] = i as i8;\n\
        \        }\n\n        let mut best_energy = vec![-1i8; m * n * 1024];\n    \
        \    let mut queue = VecDeque::new();\n\n        best_energy[(sr * n + sc) *\
        \ 1024] = energy as i8;\n        queue.push_back((sr, sc, 0, energy as i8, 0));\n\
        \n        let dr = [-1, 1, 0, 0];\n        let dc = [0, 0, -1, 1];\n\n     \
        \   while let Some((r, c, mask, e, steps)) = queue.pop_front() {\n         \
        \   for i in 0..4 {\n                let nr = r as i32 + dr[i];\n          \
        \      let nc = c as i32 + dc[i];\n\n                if nr >= 0 && nr < m as\
        \ i32 && nc >= 0 && nc < n as i32 {\n                    let nr = nr as usize;\n\
        \                    let nc = nc as usize;\n                    let char = classroom[nr].as_bytes()[nc];\n\
        \                    if char == b'X' { continue; }\n\n                    let\
        \ mut nmask = mask;\n                    let l_idx = litter_map[nr][nc];\n \
        \                   if l_idx != -1 {\n                        nmask |= 1 <<\
        \ l_idx;\n                    }\n\n                    if nmask == target_mask\
        \ { return steps + 1; }\n\n                    let mut ne = e - 1;\n       \
        \             if char == b'R' { ne = energy as i8; }\n\n                   \
        \ if ne > 0 {\n                        let idx = (nr * n + nc) * 1024 + nmask;\n\
        \                        if ne > best_energy[idx] {\n                      \
        \      best_energy[idx] = ne;\n                            queue.push_back((nr,\
        \ nc, nmask, ne, steps + 1));\n                        }\n                 \
        \   }\n                }\n            }\n        }\n\n        -1\n    }\n}"
      racket: "(require racket/base)\n\n(define/contract (min-moves classroom energy)\n\
        \  (-> (listof string?) exact-integer? exact-integer?)\n  (let* ([m (length\
        \ classroom)]\n         [n (string-length (car classroom))]\n         [grid\
        \ (list->vector (map (lambda (s) (list->vector (string->list s))) classroom))]\n\
        \         [litters '()]\n         [sr 0]\n         [sc 0])\n    (for ([r (in-range\
        \ m)])\n      (for ([c (in-range n)])\n        (let ([char (vector-ref (vector-ref\
        \ grid r) c)])\n          (cond\n            [(char=? char #\\S) (set! sr r)\
        \ (set! sc c)]\n            [(char=? char #\\L) (set! litters (cons (cons r\
        \ c) litters))]))))\n    (let* ([litter-count (length litters)]\n          \
        \ [target-mask (- (arithmetic-shift 1 litter-count) 1)])\n      (if (= target-mask\
        \ 0)\n          0\n          (let* ([litter-map (make-vector (* m n) -1)]\n\
        \                 [best-energy (make-vector (* m n 1024) -1)]\n            \
        \     [litters-list (reverse litters)])\n            (for ([i (in-range litter-count)]\n\
        \                  [l (in-list litters-list)])\n              (vector-set! litter-map\
        \ (+ (* (car l) n) (cdr l)) i))\n            (let ([q-front '()]\n         \
        \         [q-back '()])\n              (vector-set! best-energy (+ (* (+ (*\
        \ sr n) sc) 1024) 0) energy)\n              (set! q-back (list (list sr sc 0\
        \ energy 0)))\n              (let loop ()\n                (if (and (null? q-front)\
        \ (null? q-back))\n                    -1\n                    (begin\n    \
        \                  (when (null? q-front)\n                        (set! q-front\
        \ (reverse q-back))\n                        (set! q-back '()))\n          \
        \            (let* ([state (car q-front)]\n                             [_ (set!\
        \ q-front (cdr q-front))]\n                             [r (list-ref state 0)]\n\
        \                             [c (list-ref state 1)]\n                     \
        \        [mask (list-ref state 2)]\n                             [e (list-ref\
        \ state 3)]\n                             [steps (list-ref state 4)])\n    \
        \                    (let ([found-res (for/or ([d '((-1 0) (1 0) (0 -1) (0 1))])\n\
        \                                           (let* ([nr (+ r (car d))]\n    \
        \                                              [nc (+ c (cadr d))])\n      \
        \                                       (if (and (>= nr 0) (< nr m) (>= nc 0)\
        \ (< nc n))\n                                                 (let ([char (vector-ref\
        \ (vector-ref grid nr) nc)])\n                                             \
        \      (if (char=? char #\\X) #f\n                                         \
        \              (let* ([l-idx (vector-ref litter-map (+ (* nr n) nc))]\n    \
        \                                                          [nmask (if (= l-idx\
        \ -1) mask (bitwise-ior mask (arithmetic-shift 1 l-idx)))])\n              \
        \                                           (if (= nmask target-mask)\n    \
        \                                                         (+ steps 1)\n    \
        \                                                         (let* ([ne (if (char=?\
        \ char #\\R) energy (- e 1))])\n                                           \
        \                    (if (> ne 0)\n                                        \
        \                           (let ([idx (+ (* (+ (* nr n) nc) 1024) nmask)])\n\
        \                                                                     (if (>\
        \ ne (vector-ref best-energy idx))\n                                       \
        \                                  (begin\n                                \
        \                                           (vector-set! best-energy idx ne)\n\
        \                                                                          \
        \ (set! q-back (cons (list nr nc nmask ne (+ steps 1)) q-back))\n          \
        \                                                                 #f)\n    \
        \                                                                     #f))\n\
        \                                                                   #f))))))\n\
        \                                                 #f)))])\n                \
        \          (if found-res found-res (loop))))))))))))"
      erlang: "-spec min_moves(Classroom :: [unicode:unicode_binary()], Energy :: integer())\
        \ -> integer().\nmin_moves(Classroom, MaxEnergy) ->\n    Grid = list_to_tuple([list_to_tuple(binary_to_list(Row))\
        \ || Row <- Classroom]),\n    M = tuple_size(Grid),\n    N = tuple_size(element(1,\
        \ Grid)),\n    {SR, SC, Litters} = find_start_and_litters(Grid, M, N),\n   \
        \ TargetMask = (1 bsl length(Litters)) - 1,\n    if\n        TargetMask == 0\
        \ -> 0;\n        true ->\n            LitterMap = maps:from_list(lists:zip(Litters,\
        \ lists:seq(0, length(Litters) - 1))),\n            Tid = ets:new(best_energy,\
        \ [set]),\n            Q = queue:in({SR, SC, 0, MaxEnergy, 0}, queue:new()),\n\
        \            ets:insert(Tid, {{SR * N + SC, 0}, MaxEnergy}),\n            Res\
        \ = bfs(Q, Tid, Grid, LitterMap, TargetMask, MaxEnergy, M, N),\n           \
        \ ets:delete(Tid),\n            Res\n    end.\n\nfind_start_and_litters(Grid,\
        \ M, N) ->\n    find_start_and_litters(Grid, M, N, 0, 0, -1, -1, []).\n\nfind_start_and_litters(_Grid,\
        \ M, _N, M, _C, SR, SC, Litters) -> {SR, SC, lists:reverse(Litters)};\nfind_start_and_litters(Grid,\
        \ M, N, R, N, SR, SC, Litters) -> find_start_and_litters(Grid, M, N, R + 1,\
        \ 0, SR, SC, Litters);\nfind_start_and_litters(Grid, M, N, R, C, SR, SC, Litters)\
        \ ->\n    Char = element(C + 1, element(R + 1, Grid)),\n    {NSR, NSC, NLitters}\
        \ = if\n        Char == $S -> {R, C, Litters};\n        Char == $L -> {SR, SC,\
        \ [{R, C} | Litters]};\n        true -> {SR, SC, Litters}\n    end,\n    find_start_and_litters(Grid,\
        \ M, N, R, C + 1, NSR, NSC, NLitters).\n\nbfs(Q, Tid, Grid, LitterMap, TargetMask,\
        \ MaxEnergy, M, N) ->\n    case queue:out(Q) of\n        {empty, _} -> -1;\n\
        \        {{value, {R, C, Mask, E, Steps}}, Q2} ->\n            case process_neighbors([{R-1,\
        \ C}, {R+1, C}, {R, C-1}, {R, C+1}], Q2, Tid, Grid, LitterMap, TargetMask, MaxEnergy,\
        \ M, N, Mask, E, Steps) of\n                {NewQ, -1} -> bfs(NewQ, Tid, Grid,\
        \ LitterMap, TargetMask, MaxEnergy, M, N);\n                {_, Found} -> Found\n\
        \            end\n    end.\n\nprocess_neighbors([], Q, _Tid, _Grid, _LitterMap,\
        \ _TargetMask, _MaxEnergy, _M, _N, _Mask, _E, _Steps) -> {Q, -1};\nprocess_neighbors([{NR,\
        \ NC} | T], Q, Tid, Grid, LitterMap, TargetMask, MaxEnergy, M, N, Mask, E, Steps)\
        \ ->\n    if\n        NR >= 0, NR < M, NC >= 0, NC < N ->\n            Char\
        \ = element(NC + 1, element(NR + 1, Grid)),\n            if\n              \
        \  Char /= $X ->\n                    NMask = case maps:find({NR, NC}, LitterMap)\
        \ of\n                        {ok, Idx} -> Mask bor (1 bsl Idx);\n         \
        \               error -> Mask\n                    end,\n                  \
        \  if\n                        NMask == TargetMask -> {Q, Steps + 1};\n    \
        \                    true ->\n                            NE = if Char == $R\
        \ -> MaxEnergy; true -> E - 1 end,\n                            if\n       \
        \                         NE > 0 ->\n                                    Key\
        \ = {NR * N + NC, NMask},\n                                    ShouldUpdate\
        \ = case ets:lookup(Tid, Key) of\n                                        [{Key,\
        \ OldE}] -> NE > OldE;\n                                        [] -> true\n\
        \                                    end,\n                                \
        \    if\n                                        ShouldUpdate ->\n         \
        \                                   ets:insert(Tid, {Key, NE}),\n          \
        \                                  process_neighbors(T, queue:in({NR, NC, NMask,\
        \ NE, Steps + 1}, Q), Tid, Grid, LitterMap, TargetMask, MaxEnergy, M, N, Mask,\
        \ E, Steps);\n                                        true -> process_neighbors(T,\
        \ Q, Tid, Grid, LitterMap, TargetMask, MaxEnergy, M, N, Mask, E, Steps)\n  \
        \                                  end;\n                                true\
        \ -> process_neighbors(T, Q, Tid, Grid, LitterMap, TargetMask, MaxEnergy, M,\
        \ N, Mask, E, Steps)\n                            end\n                    end;\n\
        \                true -> process_neighbors(T, Q, Tid, Grid, LitterMap, TargetMask,\
        \ MaxEnergy, M, N, Mask, E, Steps)\n            end;\n        true -> process_neighbors(T,\
        \ Q, Tid, Grid, LitterMap, TargetMask, MaxEnergy, M, N, Mask, E, Steps)\n  \
        \  end."
      elixir: "defmodule Solution do\n  import Bitwise\n\n  @spec min_moves(classroom\
        \ :: [String.t()], energy :: integer()) :: integer()\n  def min_moves(classroom,\
        \ energy) do\n    grid_list = Enum.map(classroom, &String.to_charlist/1)\n \
        \   m = length(grid_list)\n    n = length(Enum.at(grid_list, 0))\n    grid =\
        \ grid_list |> Enum.map(&List.to_tuple/1) |> List.to_tuple()\n\n    {sr, sc,\
        \ litters} = find_all(grid, m, n)\n    target_mask = (1 <<< length(litters))\
        \ - 1\n\n    if target_mask == 0 do\n      0\n    else\n      litter_map = litters\
        \ |> Enum.with_index() |> Enum.into(%{})\n      table = :ets.new(:best_energy,\
        \ [:set])\n      q = :queue.in({sr, sc, 0, energy, 0}, :queue.new())\n     \
        \ :ets.insert(table, {{sr * n + sc, 0}, energy})\n      result = bfs(q, table,\
        \ grid, litter_map, target_mask, energy, m, n)\n      :ets.delete(table)\n \
        \     result\n    end\n  end\n\n  defp find_all(grid, m, n) do\n    Enum.reduce(0..(m\
        \ - 1), {0, 0, []}, fn r, acc_r ->\n      Enum.reduce(0..(n - 1), acc_r, fn\
        \ c, {sr, sc, litters} ->\n        char = elem(elem(grid, r), c)\n        cond\
        \ do\n          char == ?S -> {r, c, litters}\n          char == ?L -> {sr,\
        \ sc, [{r, c} | litters]}\n          true -> {sr, sc, litters}\n        end\n\
        \      end)\n    end)\n    |> (fn {sr, sc, litters} -> {sr, sc, Enum.reverse(litters)}\
        \ end).()\n  end\n\n  defp bfs(q, table, grid, litter_map, target_mask, max_energy,\
        \ m, n) do\n    case :queue.out(q) do\n      {:empty, _} -> -1\n      {{:value,\
        \ {r, c, mask, e, steps}}, q2} ->\n        case process_neighbors([{r - 1, c},\
        \ {r + 1, c}, {r, c - 1}, {r, c + 1}], q2, table, grid, litter_map, target_mask,\
        \ max_energy, m, n, mask, e, steps) do\n          {new_q, -1} -> bfs(new_q,\
        \ table, grid, litter_map, target_mask, max_energy, m, n)\n          {_, found}\
        \ -> found\n        end\n    end\n  end\n\n  defp process_neighbors([], q, _table,\
        \ _grid, _litter_map, _target_mask, _max_energy, _m, _n, _mask, _e, _steps),\
        \ do: {q, -1}\n\n  defp process_neighbors([{nr, nc} | t], q, table, grid, litter_map,\
        \ target_mask, max_energy, m, n, mask, e, steps) do\n    if nr >= 0 and nr <\
        \ m and nc >= 0 and nc < n do\n      char = elem(elem(grid, nr), nc)\n     \
        \ if char != ?X do\n        nmask = case Map.get(litter_map, {nr, nc}) do\n\
        \          nil -> mask\n          idx -> mask ||| (1 <<< idx)\n        end\n\
        \n        if nmask == target_mask do\n          {q, steps + 1}\n        else\n\
        \          ne = if char == ?R, do: max_energy, else: e - 1\n          if ne\
        \ > 0 do\n            key = {nr * n + nc, nmask}\n            should_update\
        \ = case :ets.lookup(table, key) do\n              [{^key, old_e}] -> ne > old_e\n\
        \              [] -> true\n            end\n\n            if should_update do\n\
        \              :ets.insert(table, {key, ne})\n              process_neighbors(t,\
        \ :queue.in({nr, nc, nmask, ne, steps + 1}, q), table, grid, litter_map, target_mask,\
        \ max_energy, m, n, mask, e, steps)\n            else\n              process_neighbors(t,\
        \ q, table, grid, litter_map, target_mask, max_energy, m, n, mask, e, steps)\n\
        \            end\n          else\n            process_neighbors(t, q, table,\
        \ grid, litter_map, target_mask, max_energy, m, n, mask, e, steps)\n       \
        \   end\n        end\n      else\n        process_neighbors(t, q, table, grid,\
        \ litter_map, target_mask, max_energy, m, n, mask, e, steps)\n      end\n  \
        \  else\n      process_neighbors(t, q, table, grid, litter_map, target_mask,\
        \ max_energy, m, n, mask, e, steps)\n    end\n  end\nend"
    approach: 'To find the minimum moves required to collect all litter items while
      managing energy, we use a Breadth-First Search (BFS) in the state-space $(r, c,
      \text{mask}, \text{energy})$. Here, $(r, c)$ represents the student''s coordinates,
      $\text{mask}$ is a bitmask representing the set of collected litter items (up
      to $2^{10}$), and $\text{energy}$ is the current energy level ($0 \dots \text{energy}$).
      Since each move has a uniform cost of 1, BFS correctly identifies the shortest
      path to a state where all bits in the mask are set. We optimize memory and performance
      by using a 3D array, `bestEnergy[r][c][mask]`, to store the maximum energy reached
      for each $(r, c, \text{mask})$ at any given step. If we encounter a state with
      energy $e$ that is less than or equal to a previously recorded `bestEnergy` for
      the same location and mask, we prune that path because a more energy-efficient
      path was already found in fewer or equal steps.


      The algorithm operates level-by-level (step-by-step). In each level, we explore
      all reachable adjacent cells. If a student moves into an ''R'' cell, their energy
      resets to the maximum capacity. If they move into an ''L'' cell, the corresponding
      bit in the mask is updated. If the mask becomes full (all litters collected),
      the current step count is returned. If the energy reaches zero and the student
      is not on an ''R'' cell, they cannot perform further moves from that state. This
      ensures we stay within energy constraints while exploring the minimum number of
      steps.'
    time_complexity: O(m * n * 2^K * E), where m and n are the grid dimensions, K is
      the number of litter items (at most 10), and E is the maximum energy capacity.
      Each state (position, mask, energy) is visited at most once, and each visit involves
      checking 4 neighbors.
    space_complexity: O(m * n * 2^K), which is the space required for the `bestEnergy`
      array to track the maximum energy seen for each position and mask combination.
      The level-by-level BFS queue also stores at most O(m * n * 2^K) states.
    elapsed_time: 424.44354033470154
    model: gemini-3-flash-preview
    generated_at: '2026-09-01 03:01:01 '
---

## Problem #3568: Minimum Moves to Clean the Classroom

**Difficulty:** Medium

**Topics:** Array, Hash Table, Bit Manipulation, Breadth-First Search, Matrix

## Problem Description

<p data-end="324" data-start="147">You are given an <code>m x n</code> grid <code>classroom</code> where a student volunteer is tasked with cleaning up litter scattered around the room. Each cell in the grid is one of the following:</p>

<ul>
	<li><code>&#39;S&#39;</code>: Starting position of the student</li>
	<li><code>&#39;L&#39;</code>: Litter that must be collected (once collected, the cell becomes empty)</li>
	<li><code>&#39;R&#39;</code>: Reset area that restores the student&#39;s energy to full capacity, regardless of their current energy level (can be used multiple times)</li>
	<li><code>&#39;X&#39;</code>: Obstacle the student cannot pass through</li>
	<li><code>&#39;.&#39;</code>: Empty space</li>
</ul>

<p>You are also given an integer <code>energy</code>, representing the student&#39;s maximum energy capacity. The student starts with this energy from the starting position <code>&#39;S&#39;</code>.</p>

<p>Each move to an adjacent cell (up, down, left, or right) costs 1 unit of energy. If the energy reaches 0, the student can only continue if they are on a reset area <code>&#39;R&#39;</code>, which resets the energy to its <strong>maximum</strong> capacity <code>energy</code>.</p>

<p>Return the <strong>minimum</strong> number of moves required to collect all litter items, or <code>-1</code> if it&#39;s impossible.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">classroom = [&quot;S.&quot;, &quot;XL&quot;], energy = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The student starts at cell <code data-end="262" data-start="254">(0, 0)</code> with 2 units of energy.</li>
	<li>Since cell <code>(1, 0)</code> contains an obstacle &#39;X&#39;, the student cannot move directly downward.</li>
	<li>A valid sequence of moves to collect all litter is as follows:
	<ul>
		<li>Move 1: From <code>(0, 0)</code> &rarr; <code>(0, 1)</code> with 1 unit of energy and 1 unit remaining.</li>
		<li>Move 2: From <code>(0, 1)</code> &rarr; <code>(1, 1)</code> to collect the litter <code>&#39;L&#39;</code>.</li>
	</ul>
	</li>
	<li>The student collects all the litter using 2 moves. Thus, the output is 2.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">classroom = [&quot;LS&quot;, &quot;RL&quot;], energy = 4</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>The student starts at cell <code data-end="262" data-start="254">(0, 1)</code> with 4 units of energy.</li>
	<li>A valid sequence of moves to collect all litter is as follows:
	<ul>
		<li>Move 1: From <code>(0, 1)</code> &rarr; <code>(0, 0)</code> to collect the first litter <code>&#39;L&#39;</code> with 1 unit of energy used and 3 units remaining.</li>
		<li>Move 2: From <code>(0, 0)</code> &rarr; <code>(1, 0)</code> to <code>&#39;R&#39;</code> to reset and restore energy back to 4.</li>
		<li>Move 3: From <code>(1, 0)</code> &rarr; <code>(1, 1)</code> to collect the second litter <code data-end="1068" data-start="1063">&#39;L&#39;</code>.</li>
	</ul>
	</li>
	<li>The student collects all the litter using 3 moves. Thus, the output is 3.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">classroom = [&quot;L.S&quot;, &quot;RXL&quot;], energy = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">-1</span></p>

<p><strong>Explanation:</strong></p>

<p>No valid path collects all <code>&#39;L&#39;</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= m == classroom.length &lt;= 20</code></li>
	<li><code>1 &lt;= n == classroom[i].length &lt;= 20</code></li>
	<li><code>classroom[i][j]</code> is one of <code>&#39;S&#39;</code>, <code>&#39;L&#39;</code>, <code>&#39;R&#39;</code>, <code>&#39;X&#39;</code>, or <code>&#39;.&#39;</code></li>
	<li><code>1 &lt;= energy &lt;= 50</code></li>
	<li>There is exactly <strong>one</strong> <code>&#39;S&#39;</code> in the grid.</li>
	<li>There are <strong>at most</strong> 10 <code>&#39;L&#39;</code> cells in the grid.</li>
</ul>


## Hints

1. Use BFS with states `(x, y, mask, e, steps)`, initializing with `(sx, sy, 0, energy, 0)`, and for each move update `e` (–1 per step), update `mask` on 'L', reset `e=energy` on 'R', and return `steps` when `mask == fullMask`.

2. Maintain a 3D array `bestEnergy[x][y][mask]` storing the maximum `e` seen for each `(x,y,mask)` and skip any new state with `e <= bestEnergy[x][y][mask]` to prune.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To find the minimum moves required to collect all litter items while managing energy, we use a Breadth-First Search (BFS) in the state-space $(r, c, \text{mask}, \text{energy})$. Here, $(r, c)$ represents the student's coordinates, $\text{mask}$ is a bitmask representing the set of collected litter items (up to $2^{10}$), and $\text{energy}$ is the current energy level ($0 \dots \text{energy}$). Since each move has a uniform cost of 1, BFS correctly identifies the shortest path to a state where all bits in the mask are set. We optimize memory and performance by using a 3D array, `bestEnergy[r][c][mask]`, to store the maximum energy reached for each $(r, c, \text{mask})$ at any given step. If we encounter a state with energy $e$ that is less than or equal to a previously recorded `bestEnergy` for the same location and mask, we prune that path because a more energy-efficient path was already found in fewer or equal steps.

The algorithm operates level-by-level (step-by-step). In each level, we explore all reachable adjacent cells. If a student moves into an 'R' cell, their energy resets to the maximum capacity. If they move into an 'L' cell, the corresponding bit in the mask is updated. If the mask becomes full (all litters collected), the current step count is returned. If the energy reaches zero and the student is not on an 'R' cell, they cannot perform further moves from that state. This ensures we stay within energy constraints while exploring the minimum number of steps.

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
// Generation failed for C++
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
// Generation failed for Java
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
// Generation failed for Python
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
// Generation failed for Python3
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
// Generation failed for C
// Reason: Parsing failed
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;
using System.Collections.Generic;

public class Solution {
    public int MinMoves(string[] classroom, int energy) {
        int m = classroom.Length;
        int n = classroom[0].Length;
        int sr = -1, sc = -1;
        int[,] litterMap = new int[m, n];
        int numLitters = 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                litterMap[i, j] = -1;
                if (classroom[i][j] == 'S') {
                    sr = i; sc = j;
                } else if (classroom[i][j] == 'L') {
                    litterMap[i, j] = numLitters++;
                }
            }
        }

        int fullMask = (1 << numLitters) - 1;
        if (fullMask == 0) return 0;

        int maskSize = 1 << numLitters;
        int[] bestEnergy = new int[m * n * maskSize];
        Array.Fill(bestEnergy, -1);

        Queue<int> queue = new Queue<int>();
        queue.Enqueue((sr << 21) | (sc << 16) | (0 << 6) | energy);
        bestEnergy[(sr * n + sc) * maskSize + 0] = energy;

        int steps = 0;
        int[] dr = { -1, 1, 0, 0 };
        int[] dc = { 0, 0, -1, 1 };

        while (queue.Count > 0) {
            steps++;
            int size = queue.Count;
            for (int i = 0; i < size; i++) {
                int packed = queue.Dequeue();
                int r = packed >> 21;
                int c = (packed >> 16) & 0x1F;
                int mask = (packed >> 6) & 0x3FF;
                int e = packed & 0x3F;

                if (e == 0 && classroom[r][c] != 'R') continue;

                for (int d = 0; d < 4; d++) {
                    int nr = r + dr[d];
                    int nc = c + dc[d];

                    if (nr >= 0 && nr < m && nc >= 0 && nc < n && classroom[nr][nc] != 'X') {
                        int ne = e - 1;
                        if (ne < 0) continue;

                        int nm = mask;
                        if (classroom[nr][nc] == 'L') nm |= (1 << litterMap[nr, nc]);
                        if (nm == fullMask) return steps;
                        if (classroom[nr][nc] == 'R') ne = energy;

                        int stateIdx = (nr * n + nc) * maskSize + nm;
                        if (ne > bestEnergy[stateIdx]) {
                            bestEnergy[stateIdx] = ne;
                            queue.Enqueue((nr << 21) | (nc << 16) | (nm << 6) | ne);
                        }
                    }
                }
            }
        }

        return -1;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {string[]} classroom
 * @param {number} energy
 * @return {number}
 */
var minMoves = function(classroom, energy) {
    const m = classroom.length;
    const n = classroom[0].length;
    let sr = -1, sc = -1;
    const litterMap = Array.from({ length: m }, () => new Int32Array(n).fill(-1));
    let numLitters = 0;

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (classroom[i][j] === 'S') {
                sr = i; sc = j;
            } else if (classroom[i][j] === 'L') {
                litterMap[i][j] = numLitters++;
            }
        }
    }

    const fullMask = (1 << numLitters) - 1;
    if (fullMask === 0) return 0;

    const maskSize = 1 << numLitters;
    const bestEnergy = new Int32Array(m * n * maskSize).fill(-1);

    let currentLevel = [(sr << 21) | (sc << 16) | (0 << 6) | energy];
    bestEnergy[(sr * n + sc) * maskSize + 0] = energy;

    let steps = 0;
    const dr = [-1, 1, 0, 0];
    const dc = [0, 0, -1, 1];

    while (currentLevel.length > 0) {
        steps++;
        const nextLevel = [];
        for (let i = 0; i < currentLevel.length; i++) {
            const packed = currentLevel[i];
            const r = packed >> 21;
            const c = (packed >> 16) & 0x1F;
            const mask = (packed >> 6) & 0x3FF;
            const e = packed & 0x3F;

            if (e === 0 && classroom[r][c] !== 'R') continue;

            for (let d = 0; d < 4; d++) {
                const nr = r + dr[d];
                const nc = c + dc[d];

                if (nr >= 0 && nr < m && nc >= 0 && nc < n && classroom[nr][nc] !== 'X') {
                    let ne = e - 1;
                    if (ne < 0) continue;

                    let nm = mask;
                    if (classroom[nr][nc] === 'L') nm |= (1 << litterMap[nr][nc]);
                    if (nm === fullMask) return steps;
                    if (classroom[nr][nc] === 'R') ne = energy;

                    const stateIdx = (nr * n + nc) * maskSize + nm;
                    if (ne > bestEnergy[stateIdx]) {
                        bestEnergy[stateIdx] = ne;
                        nextLevel.push((nr << 21) | (nc << 16) | (nm << 6) | ne);
                    }
                }
            }
        }
        currentLevel = nextLevel;
    }

    return -1;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function minMoves(classroom: string[], energy: number): number {
    const m = classroom.length;
    const n = classroom[0].length;
    let sr = -1, sc = -1;
    const litterMap: number[][] = Array.from({ length: m }, () => new Array(n).fill(-1));
    let numLitters = 0;

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (classroom[i][j] === 'S') {
                sr = i; sc = j;
            } else if (classroom[i][j] === 'L') {
                litterMap[i][j] = numLitters++;
            }
        }
    }

    const fullMask = (1 << numLitters) - 1;
    if (fullMask === 0) return 0;

    const maskSize = 1 << numLitters;
    const bestEnergy = new Int32Array(m * n * maskSize).fill(-1);

    let currentLevel = [(sr << 21) | (sc << 16) | (0 << 6) | energy];
    bestEnergy[(sr * n + sc) * maskSize + 0] = energy;

    let steps = 0;
    const dr = [-1, 1, 0, 0];
    const dc = [0, 0, -1, 1];

    while (currentLevel.length > 0) {
        steps++;
        const nextLevel: number[] = [];
        for (let i = 0; i < currentLevel.length; i++) {
            const packed = currentLevel[i];
            const r = packed >> 21;
            const c = (packed >> 16) & 0x1F;
            const mask = (packed >> 6) & 0x3FF;
            const e = packed & 0x3F;

            if (e === 0 && classroom[r][c] !== 'R') continue;

            for (let d = 0; d < 4; d++) {
                const nr = r + dr[d];
                const nc = c + dc[d];

                if (nr >= 0 && nr < m && nc >= 0 && nc < n && classroom[nr][nc] !== 'X') {
                    let ne = e - 1;
                    if (ne < 0) continue;

                    let nm = mask;
                    if (classroom[nr][nc] === 'L') nm |= (1 << litterMap[nr][nc]);
                    if (nm === fullMask) return steps;
                    if (classroom[nr][nc] === 'R') ne = energy;

                    const stateIdx = (nr * n + nc) * maskSize + nm;
                    if (ne > bestEnergy[stateIdx]) {
                        bestEnergy[stateIdx] = ne;
                        nextLevel.push((nr << 21) | (nc << 16) | (nm << 6) | ne);
                    }
                }
            }
        }
        currentLevel = nextLevel;
    }

    return -1;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param String[] $classroom
     * @param Integer $energy
     * @return Integer
     */
    function minMoves($classroom, $energy) {
        $m = count($classroom);
        $n = strlen($classroom[0]);
        $sr = $sc = -1;
        $litterMap = [];
        $numLitters = 0;

        for ($i = 0; $i < $m; $i++) {
            $litterMap[$i] = array_fill(0, $n, -1);
            for ($j = 0; $j < $n; $j++) {
                if ($classroom[$i][$j] === 'S') {
                    $sr = $i; $sc = $j;
                } else if ($classroom[$i][$j] === 'L') {
                    $litterMap[$i][$j] = $numLitters++;
                }
            }
        }

        $fullMask = (1 << $numLitters) - 1;
        if ($fullMask === 0) return 0;

        $maskSize = 1 << $numLitters;
        $bestEnergy = new SplFixedArray($m * $n * $maskSize);
        for ($i = 0; $i < $bestEnergy->getSize(); $i++) $bestEnergy[$i] = -1;

        $currentLevel = [($sr << 21) | ($sc << 16) | (0 << 6) | $energy];
        $bestEnergy[($sr * $n + $sc) * $maskSize + 0] = $energy;

        $steps = 0;
        $dr = [-1, 1, 0, 0];
        $dc = [0, 0, -1, 1];

        while (!empty($currentLevel)) {
            $steps++;
            $nextLevel = [];
            foreach ($currentLevel as $packed) {
                $r = $packed >> 21;
                $c = ($packed >> 16) & 0x1F;
                $mask = ($packed >> 6) & 0x3FF;
                $e = $packed & 0x3F;

                if ($e === 0 && $classroom[$r][$c] !== 'R') continue;

                for ($d = 0; $d < 4; $d++) {
                    $nr = $r + $dr[$d];
                    $nc = $c + $dc[$d];

                    if ($nr >= 0 && $nr < $m && $nc >= 0 && $nc < $n && $classroom[$nr][$nc] !== 'X') {
                        $ne = $e - 1;
                        if ($ne < 0) continue;

                        $nm = $mask;
                        if ($classroom[$nr][$nc] === 'L') $nm |= (1 << $litterMap[$nr][$nc]);
                        if ($nm === $fullMask) return $steps;
                        if ($classroom[$nr][$nc] === 'R') $ne = $energy;

                        $stateIdx = ($nr * $n + $nc) * $maskSize + $nm;
                        if ($ne > $bestEnergy[$stateIdx]) {
                            $bestEnergy[$stateIdx] = $ne;
                            $nextLevel[] = ($nr << 21) | ($nc << 16) | ($nm << 6) | $ne;
                        }
                    }
                }
            }
            $currentLevel = $nextLevel;
        }

        return -1;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func minMoves(_ classroom: [String], _ energy: Int) -> Int {
        let m = classroom.count
        let n = classroom[0].count
        let grid = classroom.map { Array($0) }
        var sr = -1, sc = -1
        var litterMap = Array(repeating: Array(repeating: -1, count: n), count: m)
        var numLitters = 0

        for i in 0..<m {
            for j in 0..<n {
                if grid[i][j] == "S" {
                    sr = i; sc = j
                } else if grid[i][j] == "L" {
                    litterMap[i][j] = numLitters
                    numLitters += 1
                }
            }
        }

        let fullMask = (1 << numLitters) - 1
        if fullMask == 0 { return 0 }

        let maskSize = 1 << numLitters
        var bestEnergy = Array(repeating: Int8(-1), count: m * n * maskSize)

        var currentLevel: [Int32] = [Int32((sr << 21) | (sc << 16) | (0 << 6) | energy)]
        bestEnergy[(sr * n + sc) * maskSize + 0] = Int8(energy)

        var steps = 0
        let dr = [-1, 1, 0, 0]
        let dc = [0, 0, -1, 1]

        while !currentLevel.isEmpty {
            steps += 1
            var nextLevel: [Int32] = []
            for packed in currentLevel {
                let r = Int(packed >> 21)
                let c = Int((packed >> 16) & 0x1F)
                let mask = Int((packed >> 6) & 0x3FF)
                let e = Int(packed & 0x3F)

                if e == 0 && grid[r][c] != "R" { continue }

                for d in 0..<4 {
                    let nr = r + dr[d]
                    let nc = c + dc[d]

                    if nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] != "X" {
                        var ne = e - 1
                        if ne < 0 { continue }

                        var nm = mask
                        if grid[nr][nc] == "L" { nm |= (1 << litterMap[nr][nc]) }
                        if nm == fullMask { return steps }
                        if grid[nr][nc] == "R" { ne = energy }

                        let stateIdx = (nr * n + nc) * maskSize + nm
                        if Int8(ne) > bestEnergy[stateIdx] {
                            bestEnergy[stateIdx] = Int8(ne)
                            nextLevel.append(Int32((nr << 21) | (nc << 16) | (nm << 6) | ne))
                        }
                    }
                }
            }
            currentLevel = nextLevel
        }

        return -1
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
    data class State(val r: Int, val c: Int, val mask: Int, val e: Int, val steps: Int)

    fun minMoves(classroom: Array<String>, energy: Int): Int {
        val m = classroom.size
        val n = classroom[0].length
        var sr = 0
        var sc = 0
        val litters = mutableListOf<Pair<Int, Int>>()
        for (r in 0 until m) {
            for (c in 0 until n) {
                if (classroom[r][c] == 'S') {
                    sr = r
                    sc = c
                } else if (classroom[r][c] == 'L') {
                    litters.add(Pair(r, c))
                }
            }
        }

        val numL = litters.size
        val targetMask = (1 shl numL) - 1
        if (targetMask == 0) return 0

        val litterMap = IntArray(m * n) { -1 }
        for (i in 0 until numL) {
            litterMap[litters[i].first * n + litters[i].second] = i
        }

        val bestEnergy = IntArray(m * n * (1 shl numL)) { -1 }
        val queue = ArrayDeque<State>()

        queue.add(State(sr, sc, 0, energy, 0))
        bestEnergy[(sr * n + sc) * (1 shl numL) + 0] = energy

        val dr = intArrayOf(-1, 1, 0, 0)
        val dc = intArrayOf(0, 0, -1, 1)

        while (queue.isNotEmpty()) {
            val curr = queue.poll()

            for (i in 0 until 4) {
                val nr = curr.r + dr[i]
                val nc = curr.c + dc[i]

                if (nr in 0 until m && nc in 0 until n && classroom[nr][nc] != 'X') {
                    var ne = curr.e - 1
                    if (ne < 0) continue

                    var nm = curr.mask
                    val cell = classroom[nr][nc]
                    if (cell == 'L') {
                        nm = nm or (1 shl litterMap[nr * n + nc])
                    }

                    if (nm == targetMask) return curr.steps + 1

                    if (cell == 'R') {
                        ne = energy
                    }

                    val idx = (nr * n + nc) * (1 shl numL) + nm
                    if (ne > bestEnergy[idx]) {
                        bestEnergy[idx] = ne
                        queue.add(State(nr, nc, nm, ne, curr.steps + 1))
                    }
                }
            }
        }

        return -1
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
import 'dart:collection';

class State {
  final int r, c, mask, e, steps;
  State(this.r, this.c, this.mask, this.e, this.steps);
}

class Solution {
  int minMoves(List<String> classroom, int energy) {
    int m = classroom.length;
    int n = classroom[0].length;
    int sr = 0, sc = 0;
    List<List<int>> litters = [];
    for (int r = 0; r < m; r++) {
      for (int c = 0; c < n; c++) {
        if (classroom[r][c] == 'S') {
          sr = r;
          sc = c;
        } else if (classroom[r][c] == 'L') {
          litters.add([r, c]);
        }
      }
    }

    int numL = litters.length;
    int targetMask = (1 << numL) - 1;
    if (targetMask == 0) return 0;

    List<int> litterMap = List.filled(m * n, -1);
    for (int i = 0; i < numL; i++) {
      litterMap[litters[i][0] * n + litters[i][1]] = i;
    }

    List<int> bestEnergy = List.filled(m * n * (1 << numL), -1);
    Queue<State> queue = Queue<State>();

    queue.add(State(sr, sc, 0, energy, 0));
    bestEnergy[(sr * n + sc) * (1 << numL) + 0] = energy;

    List<int> dr = [-1, 1, 0, 0];
    List<int> dc = [0, 0, -1, 1];

    while (queue.isNotEmpty) {
      State curr = queue.removeFirst();

      for (int i = 0; i < 4; i++) {
        int nr = curr.r + dr[i];
        int nc = curr.c + dc[i];

        if (nr >= 0 && nr < m && nc >= 0 && nc < n && classroom[nr][nc] != 'X') {
          int ne = curr.e - 1;
          if (ne < 0) continue;

          int nm = curr.mask;
          String cell = classroom[nr][nc];
          if (cell == 'L') {
            nm |= (1 << litterMap[nr * n + nc]);
          }

          if (nm == targetMask) return curr.steps + 1;

          if (cell == 'R') {
            ne = energy;
          }

          int idx = (nr * n + nc) * (1 << numL) + nm;
          if (ne > bestEnergy[idx]) {
            bestEnergy[idx] = ne;
            queue.add(State(nr, nc, nm, ne, curr.steps + 1));
          }
        }
      }
    }

    return -1;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func minMoves(classroom []string, energy int) int {
    m := len(classroom)
    n := len(classroom[0])
    var sr, sc int
    type pos struct{ r, c int }
    litters := []pos{}
    for r := 0; r < m; r++ {
        for c := 0; c < n; c++ {
            if classroom[r][c] == 'S' {
                sr, sc = r, c
            } else if classroom[r][c] == 'L' {
                litters = append(litters, pos{r, c})
            }
        }
    }

    numL := len(litters)
    targetMask := (1 << numL) - 1
    if targetMask == 0 {
        return 0
    }

    litterMap := make([]int, m*n)
    for i := range litterMap { litterMap[i] = -1 }
    for i, p := range litters {
        litterMap[p.r*n+p.c] = i
    }

    bestEnergy := make([]int, m*n*(1<<numL))
    for i := range bestEnergy { bestEnergy[i] = -1 }

    type state struct {
        r, c, mask, e, steps int
    }
    queue := []state{{sr, sc, 0, energy, 0}}
    bestEnergy[(sr*n+sc)*(1<<numL)] = energy

    dr := []int{-1, 1, 0, 0}
    dc := []int{0, 0, -1, 1}

    for len(queue) > 0 {
        curr := queue[0]
        queue = queue[1:]

        for i := 0; i < 4; i++ {
            nr, nc := curr.r+dr[i], curr.c+dc[i]
            if nr >= 0 && nr < m && nc >= 0 && nc < n && classroom[nr][nc] != 'X' {
                ne := curr.e - 1
                if ne < 0 { continue }

                nm := curr.mask
                cell := classroom[nr][nc]
                if cell == 'L' {
                    nm |= (1 << litterMap[nr*n+nc])
                }

                if nm == targetMask {
                    return curr.steps + 1
                }

                if cell == 'R' {
                    ne = energy
                }

                idx := (nr*n+nc)*(1<<numL) + nm
                if ne > bestEnergy[idx] {
                    bestEnergy[idx] = ne
                    queue = append(queue, state{nr, nc, nm, ne, curr.steps + 1})
                }
            }
        }
    }

    return -1
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {String[]} classroom
# @param {Integer} energy
# @return {Integer}
def min_moves(classroom, energy)
    m = classroom.length
    n = classroom[0].length
    sr, sc = 0, 0
    litters = []
    for r in 0...m
        for c in 0...n
            if classroom[r][c] == 'S'
                sr, sc = r, c
            elsif classroom[r][c] == 'L'
                litters << [r, c]
            end
        end
    end

    num_l = litters.length
    target_mask = (1 << num_l) - 1
    return 0 if target_mask == 0

    litter_map = Array.new(m * n, -1)
    litters.each_with_index do |(lr, lc), i|
        litter_map[lr * n + lc] = i
    end

    best_energy = Array.new(m * n * (1 << num_l), -1)
    queue = [[sr, sc, 0, energy, 0]]
    best_energy[(sr * n + sc) * (1 << num_l)] = energy

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    head = 0

    while head < queue.length
        r, c, mask, e, steps = queue[head]
        head += 1

        for i in 0...4
            nr, nc = r + dr[i], c + dc[i]
            if nr >= 0 && nr < m && nc >= 0 && nc < n && classroom[nr][nc] != 'X'
                ne = e - 1
                next if ne < 0

                nm = mask
                cell = classroom[nr][nc]
                if cell == 'L'
                    nm |= (1 << litter_map[nr * n + nc])
                end

                return steps + 1 if nm == target_mask

                ne = energy if cell == 'R'
                idx = (nr * n + nc) * (1 << num_l) + nm
                if ne > best_energy[idx]
                    best_energy[idx] = ne
                    queue << [nr, nc, nm, ne, steps + 1]
                end
            end
        end
    end

    -1
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.collection.mutable

object Solution {
    case class State(r: Int, c: Int, mask: Int, e: Int, steps: Int)

    def minMoves(classroom: Array[String], energy: Int): Int = {
        val m = classroom.length
        val n = classroom(0).length
        var sr, sc = 0
        val litters = mutable.ListBuffer[(Int, Int)]()

        for (r <- 0 until m; c <- 0 until n) {
            if (classroom(r)(c) == 'S') {
                sr = r
                sc = c
            } else if (classroom(r)(c) == 'L') {
                litters += ((r, c))
            }
        }

        val numL = litters.size
        val targetMask = (1 << numL) - 1
        if (targetMask == 0) return 0

        val litterMap = Array.fill(m * n)(-1)
        for (i <- 0 until numL) {
            litterMap(litters(i)._1 * n + litters(i)._2) = i
        }

        val bestEnergy = Array.fill(m * n * (1 << numL))(-1)
        val queue = mutable.Queue[State]()

        queue.enqueue(State(sr, sc, 0, energy, 0))
        bestEnergy((sr * n + sc) * (1 << numL)) = energy

        val dr = Array(-1, 1, 0, 0)
        val dc = Array(0, 0, -1, 1)

        while (queue.nonEmpty) {
            val curr = queue.dequeue()

            for (i <- 0 until 4) {
                val nr = curr.r + dr(i)
                val nc = curr.c + dc(i)

                if (nr >= 0 && nr < m && nc >= 0 && nc < n && classroom(nr)(nc) != 'X') {
                    var ne = curr.e - 1
                    if (ne >= 0) {
                        var nm = curr.mask
                        val cell = classroom(nr)(nc)
                        if (cell == 'L') {
                            nm |= (1 << litterMap(nr * n + nc))
                        }

                        if (nm == targetMask) return curr.steps + 1

                        if (cell == 'R') {
                            ne = energy
                        }

                        val idx = (nr * n + nc) * (1 << numL) + nm
                        if (ne > bestEnergy(idx)) {
                            bestEnergy(idx) = ne
                            queue.enqueue(State(nr, nc, nm, ne, curr.steps + 1))
                        }
                    }
                }
            }
        }

        -1
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
use std::collections::VecDeque;

impl Solution {
    pub fn min_moves(classroom: Vec<String>, energy: i32) -> i32 {
        let m = classroom.len();
        let n = classroom[0].len();
        let mut sr = 0;
        let mut sc = 0;
        let mut litters = Vec::new();

        for r in 0..m {
            let bytes = classroom[r].as_bytes();
            for c in 0..n {
                if bytes[c] == b'S' {
                    sr = r;
                    sc = c;
                } else if bytes[c] == b'L' {
                    litters.push((r, c));
                }
            }
        }

        let litter_count = litters.len();
        let target_mask = (1 << litter_count) - 1;
        if target_mask == 0 { return 0; }

        let mut litter_map = [[-1i8; 20]; 20];
        for (i, &(lr, lc)) in litters.iter().enumerate() {
            litter_map[lr][lc] = i as i8;
        }

        let mut best_energy = vec![-1i8; m * n * 1024];
        let mut queue = VecDeque::new();

        best_energy[(sr * n + sc) * 1024] = energy as i8;
        queue.push_back((sr, sc, 0, energy as i8, 0));

        let dr = [-1, 1, 0, 0];
        let dc = [0, 0, -1, 1];

        while let Some((r, c, mask, e, steps)) = queue.pop_front() {
            for i in 0..4 {
                let nr = r as i32 + dr[i];
                let nc = c as i32 + dc[i];

                if nr >= 0 && nr < m as i32 && nc >= 0 && nc < n as i32 {
                    let nr = nr as usize;
                    let nc = nc as usize;
                    let char = classroom[nr].as_bytes()[nc];
                    if char == b'X' { continue; }

                    let mut nmask = mask;
                    let l_idx = litter_map[nr][nc];
                    if l_idx != -1 {
                        nmask |= 1 << l_idx;
                    }

                    if nmask == target_mask { return steps + 1; }

                    let mut ne = e - 1;
                    if char == b'R' { ne = energy as i8; }

                    if ne > 0 {
                        let idx = (nr * n + nc) * 1024 + nmask;
                        if ne > best_energy[idx] {
                            best_energy[idx] = ne;
                            queue.push_back((nr, nc, nmask, ne, steps + 1));
                        }
                    }
                }
            }
        }

        -1
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(require racket/base)

(define/contract (min-moves classroom energy)
  (-> (listof string?) exact-integer? exact-integer?)
  (let* ([m (length classroom)]
         [n (string-length (car classroom))]
         [grid (list->vector (map (lambda (s) (list->vector (string->list s))) classroom))]
         [litters '()]
         [sr 0]
         [sc 0])
    (for ([r (in-range m)])
      (for ([c (in-range n)])
        (let ([char (vector-ref (vector-ref grid r) c)])
          (cond
            [(char=? char #\S) (set! sr r) (set! sc c)]
            [(char=? char #\L) (set! litters (cons (cons r c) litters))]))))
    (let* ([litter-count (length litters)]
           [target-mask (- (arithmetic-shift 1 litter-count) 1)])
      (if (= target-mask 0)
          0
          (let* ([litter-map (make-vector (* m n) -1)]
                 [best-energy (make-vector (* m n 1024) -1)]
                 [litters-list (reverse litters)])
            (for ([i (in-range litter-count)]
                  [l (in-list litters-list)])
              (vector-set! litter-map (+ (* (car l) n) (cdr l)) i))
            (let ([q-front '()]
                  [q-back '()])
              (vector-set! best-energy (+ (* (+ (* sr n) sc) 1024) 0) energy)
              (set! q-back (list (list sr sc 0 energy 0)))
              (let loop ()
                (if (and (null? q-front) (null? q-back))
                    -1
                    (begin
                      (when (null? q-front)
                        (set! q-front (reverse q-back))
                        (set! q-back '()))
                      (let* ([state (car q-front)]
                             [_ (set! q-front (cdr q-front))]
                             [r (list-ref state 0)]
                             [c (list-ref state 1)]
                             [mask (list-ref state 2)]
                             [e (list-ref state 3)]
                             [steps (list-ref state 4)])
                        (let ([found-res (for/or ([d '((-1 0) (1 0) (0 -1) (0 1))])
                                           (let* ([nr (+ r (car d))]
                                                  [nc (+ c (cadr d))])
                                             (if (and (>= nr 0) (< nr m) (>= nc 0) (< nc n))
                                                 (let ([char (vector-ref (vector-ref grid nr) nc)])
                                                   (if (char=? char #\X) #f
                                                       (let* ([l-idx (vector-ref litter-map (+ (* nr n) nc))]
                                                              [nmask (if (= l-idx -1) mask (bitwise-ior mask (arithmetic-shift 1 l-idx)))])
                                                         (if (= nmask target-mask)
                                                             (+ steps 1)
                                                             (let* ([ne (if (char=? char #\R) energy (- e 1))])
                                                               (if (> ne 0)
                                                                   (let ([idx (+ (* (+ (* nr n) nc) 1024) nmask)])
                                                                     (if (> ne (vector-ref best-energy idx))
                                                                         (begin
                                                                           (vector-set! best-energy idx ne)
                                                                           (set! q-back (cons (list nr nc nmask ne (+ steps 1)) q-back))
                                                                           #f)
                                                                         #f))
                                                                   #f))))))
                                                 #f)))])
                          (if found-res found-res (loop))))))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec min_moves(Classroom :: [unicode:unicode_binary()], Energy :: integer()) -> integer().
min_moves(Classroom, MaxEnergy) ->
    Grid = list_to_tuple([list_to_tuple(binary_to_list(Row)) || Row <- Classroom]),
    M = tuple_size(Grid),
    N = tuple_size(element(1, Grid)),
    {SR, SC, Litters} = find_start_and_litters(Grid, M, N),
    TargetMask = (1 bsl length(Litters)) - 1,
    if
        TargetMask == 0 -> 0;
        true ->
            LitterMap = maps:from_list(lists:zip(Litters, lists:seq(0, length(Litters) - 1))),
            Tid = ets:new(best_energy, [set]),
            Q = queue:in({SR, SC, 0, MaxEnergy, 0}, queue:new()),
            ets:insert(Tid, {{SR * N + SC, 0}, MaxEnergy}),
            Res = bfs(Q, Tid, Grid, LitterMap, TargetMask, MaxEnergy, M, N),
            ets:delete(Tid),
            Res
    end.

find_start_and_litters(Grid, M, N) ->
    find_start_and_litters(Grid, M, N, 0, 0, -1, -1, []).

find_start_and_litters(_Grid, M, _N, M, _C, SR, SC, Litters) -> {SR, SC, lists:reverse(Litters)};
find_start_and_litters(Grid, M, N, R, N, SR, SC, Litters) -> find_start_and_litters(Grid, M, N, R + 1, 0, SR, SC, Litters);
find_start_and_litters(Grid, M, N, R, C, SR, SC, Litters) ->
    Char = element(C + 1, element(R + 1, Grid)),
    {NSR, NSC, NLitters} = if
        Char == $S -> {R, C, Litters};
        Char == $L -> {SR, SC, [{R, C} | Litters]};
        true -> {SR, SC, Litters}
    end,
    find_start_and_litters(Grid, M, N, R, C + 1, NSR, NSC, NLitters).

bfs(Q, Tid, Grid, LitterMap, TargetMask, MaxEnergy, M, N) ->
    case queue:out(Q) of
        {empty, _} -> -1;
        {{value, {R, C, Mask, E, Steps}}, Q2} ->
            case process_neighbors([{R-1, C}, {R+1, C}, {R, C-1}, {R, C+1}], Q2, Tid, Grid, LitterMap, TargetMask, MaxEnergy, M, N, Mask, E, Steps) of
                {NewQ, -1} -> bfs(NewQ, Tid, Grid, LitterMap, TargetMask, MaxEnergy, M, N);
                {_, Found} -> Found
            end
    end.

process_neighbors([], Q, _Tid, _Grid, _LitterMap, _TargetMask, _MaxEnergy, _M, _N, _Mask, _E, _Steps) -> {Q, -1};
process_neighbors([{NR, NC} | T], Q, Tid, Grid, LitterMap, TargetMask, MaxEnergy, M, N, Mask, E, Steps) ->
    if
        NR >= 0, NR < M, NC >= 0, NC < N ->
            Char = element(NC + 1, element(NR + 1, Grid)),
            if
                Char /= $X ->
                    NMask = case maps:find({NR, NC}, LitterMap) of
                        {ok, Idx} -> Mask bor (1 bsl Idx);
                        error -> Mask
                    end,
                    if
                        NMask == TargetMask -> {Q, Steps + 1};
                        true ->
                            NE = if Char == $R -> MaxEnergy; true -> E - 1 end,
                            if
                                NE > 0 ->
                                    Key = {NR * N + NC, NMask},
                                    ShouldUpdate = case ets:lookup(Tid, Key) of
                                        [{Key, OldE}] -> NE > OldE;
                                        [] -> true
                                    end,
                                    if
                                        ShouldUpdate ->
                                            ets:insert(Tid, {Key, NE}),
                                            process_neighbors(T, queue:in({NR, NC, NMask, NE, Steps + 1}, Q), Tid, Grid, LitterMap, TargetMask, MaxEnergy, M, N, Mask, E, Steps);
                                        true -> process_neighbors(T, Q, Tid, Grid, LitterMap, TargetMask, MaxEnergy, M, N, Mask, E, Steps)
                                    end;
                                true -> process_neighbors(T, Q, Tid, Grid, LitterMap, TargetMask, MaxEnergy, M, N, Mask, E, Steps)
                            end
                    end;
                true -> process_neighbors(T, Q, Tid, Grid, LitterMap, TargetMask, MaxEnergy, M, N, Mask, E, Steps)
            end;
        true -> process_neighbors(T, Q, Tid, Grid, LitterMap, TargetMask, MaxEnergy, M, N, Mask, E, Steps)
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  import Bitwise

  @spec min_moves(classroom :: [String.t()], energy :: integer()) :: integer()
  def min_moves(classroom, energy) do
    grid_list = Enum.map(classroom, &String.to_charlist/1)
    m = length(grid_list)
    n = length(Enum.at(grid_list, 0))
    grid = grid_list |> Enum.map(&List.to_tuple/1) |> List.to_tuple()

    {sr, sc, litters} = find_all(grid, m, n)
    target_mask = (1 <<< length(litters)) - 1

    if target_mask == 0 do
      0
    else
      litter_map = litters |> Enum.with_index() |> Enum.into(%{})
      table = :ets.new(:best_energy, [:set])
      q = :queue.in({sr, sc, 0, energy, 0}, :queue.new())
      :ets.insert(table, {{sr * n + sc, 0}, energy})
      result = bfs(q, table, grid, litter_map, target_mask, energy, m, n)
      :ets.delete(table)
      result
    end
  end

  defp find_all(grid, m, n) do
    Enum.reduce(0..(m - 1), {0, 0, []}, fn r, acc_r ->
      Enum.reduce(0..(n - 1), acc_r, fn c, {sr, sc, litters} ->
        char = elem(elem(grid, r), c)
        cond do
          char == ?S -> {r, c, litters}
          char == ?L -> {sr, sc, [{r, c} | litters]}
          true -> {sr, sc, litters}
        end
      end)
    end)
    |> (fn {sr, sc, litters} -> {sr, sc, Enum.reverse(litters)} end).()
  end

  defp bfs(q, table, grid, litter_map, target_mask, max_energy, m, n) do
    case :queue.out(q) do
      {:empty, _} -> -1
      {{:value, {r, c, mask, e, steps}}, q2} ->
        case process_neighbors([{r - 1, c}, {r + 1, c}, {r, c - 1}, {r, c + 1}], q2, table, grid, litter_map, target_mask, max_energy, m, n, mask, e, steps) do
          {new_q, -1} -> bfs(new_q, table, grid, litter_map, target_mask, max_energy, m, n)
          {_, found} -> found
        end
    end
  end

  defp process_neighbors([], q, _table, _grid, _litter_map, _target_mask, _max_energy, _m, _n, _mask, _e, _steps), do: {q, -1}

  defp process_neighbors([{nr, nc} | t], q, table, grid, litter_map, target_mask, max_energy, m, n, mask, e, steps) do
    if nr >= 0 and nr < m and nc >= 0 and nc < n do
      char = elem(elem(grid, nr), nc)
      if char != ?X do
        nmask = case Map.get(litter_map, {nr, nc}) do
          nil -> mask
          idx -> mask ||| (1 <<< idx)
        end

        if nmask == target_mask do
          {q, steps + 1}
        else
          ne = if char == ?R, do: max_energy, else: e - 1
          if ne > 0 do
            key = {nr * n + nc, nmask}
            should_update = case :ets.lookup(table, key) do
              [{^key, old_e}] -> ne > old_e
              [] -> true
            end

            if should_update do
              :ets.insert(table, {key, ne})
              process_neighbors(t, :queue.in({nr, nc, nmask, ne, steps + 1}, q), table, grid, litter_map, target_mask, max_energy, m, n, mask, e, steps)
            else
              process_neighbors(t, q, table, grid, litter_map, target_mask, max_energy, m, n, mask, e, steps)
            end
          else
            process_neighbors(t, q, table, grid, litter_map, target_mask, max_energy, m, n, mask, e, steps)
          end
        end
      else
        process_neighbors(t, q, table, grid, litter_map, target_mask, max_energy, m, n, mask, e, steps)
      end
    else
      process_neighbors(t, q, table, grid, litter_map, target_mask, max_energy, m, n, mask, e, steps)
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(m * n * 2^K * E), where m and n are the grid dimensions, K is the number of litter items (at most 10), and E is the maximum energy capacity. Each state (position, mask, energy) is visited at most once, and each visit involves checking 4 neighbors.
- **Space Complexity:** O(m * n * 2^K), which is the space required for the `bestEnergy` array to track the maximum energy seen for each position and mask combination. The level-by-level BFS queue also stores at most O(m * n * 2^K) states.
