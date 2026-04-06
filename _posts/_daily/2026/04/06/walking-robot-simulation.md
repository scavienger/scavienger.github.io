---
layout: post
title: "Walking Robot Simulation"
date: 2026-04-06 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Hash Table", "Simulation"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/walking-robot-simulation/
ai_solutions:
  - solutions:
      cpp: "#include <vector>\n#include <unordered_set>\n#include <algorithm>\n\nusing\
        \ namespace std;\n\nclass Solution {\npublic:\n    int robotSim(vector<int>&\
        \ commands, vector<vector<int>>& obstacles) {\n        unordered_set<long long>\
        \ obstacleSet;\n        for (const auto& obs : obstacles) {\n            obstacleSet.insert(((long\
        \ long)obs[0] + 30000) << 16 | ((long long)obs[1] + 30000));\n        }\n\n\
        \        int dx[] = {0, 1, 0, -1};\n        int dy[] = {1, 0, -1, 0};\n    \
        \    int x = 0, y = 0, di = 0;\n        int maxDistSq = 0;\n\n        for (int\
        \ cmd : commands) {\n            if (cmd == -2) {\n                di = (di\
        \ + 3) % 4;\n            } else if (cmd == -1) {\n                di = (di +\
        \ 1) % 4;\n            } else {\n                for (int k = 0; k < cmd; ++k)\
        \ {\n                    int nx = x + dx[di];\n                    int ny =\
        \ y + dy[di];\n                    long long nextKey = ((long long)nx + 30000)\
        \ << 16 | ((long long)ny + 30000);\n                    if (obstacleSet.find(nextKey)\
        \ == obstacleSet.end()) {\n                        x = nx;\n               \
        \         y = ny;\n                        maxDistSq = max(maxDistSq, x * x\
        \ + y * y);\n                    } else {\n                        break;\n\
        \                    }\n                }\n            }\n        }\n\n    \
        \    return maxDistSq;\n    }\n};"
      java: "import java.util.*;\n\nclass Solution {\n    public int robotSim(int[]\
        \ commands, int[][] obstacles) {\n        Set<Long> obstacleSet = new HashSet<>();\n\
        \        for (int[] obs : obstacles) {\n            long ox = (long)obs[0] +\
        \ 30000;\n            long oy = (long)obs[1] + 30000;\n            obstacleSet.add((ox\
        \ << 16) | oy);\n        }\n\n        int[] dx = {0, 1, 0, -1};\n        int[]\
        \ dy = {1, 0, -1, 0};\n        int x = 0, y = 0, di = 0;\n        int maxDistSq\
        \ = 0;\n\n        for (int cmd : commands) {\n            if (cmd == -2) {\n\
        \                di = (di + 3) % 4;\n            } else if (cmd == -1) {\n \
        \               di = (di + 1) % 4;\n            } else {\n                for\
        \ (int k = 0; k < cmd; k++) {\n                    int nx = x + dx[di];\n  \
        \                  int ny = y + dy[di];\n                    long nextKey =\
        \ (((long)nx + 30000) << 16) | ((long)ny + 30000);\n                    if (!obstacleSet.contains(nextKey))\
        \ {\n                        x = nx;\n                        y = ny;\n    \
        \                    maxDistSq = Math.max(maxDistSq, x * x + y * y);\n     \
        \               } else {\n                        break;\n                 \
        \   }\n                }\n            }\n        }\n        return maxDistSq;\n\
        \    }\n}"
      python: "class Solution(object):\n    def robotSim(self, commands, obstacles):\n\
        \        \"\"\"\n        :type commands: List[int]\n        :type obstacles:\
        \ List[List[int]]\n        :rtype: int\n        \"\"\"\n        obstacle_set\
        \ = set(tuple(obs) for obs in obstacles)\n        dx = [0, 1, 0, -1]\n     \
        \   dy = [1, 0, -1, 0]\n        x, y, di = 0, 0, 0\n        max_dist_sq = 0\n\
        \n        for cmd in commands:\n            if cmd == -2:\n                di\
        \ = (di + 3) % 4\n            elif cmd == -1:\n                di = (di + 1)\
        \ % 4\n            else:\n                for _ in range(cmd):\n           \
        \         nx = x + dx[di]\n                    ny = y + dy[di]\n           \
        \         if (nx, ny) not in obstacle_set:\n                        x, y = nx,\
        \ ny\n                        max_dist_sq = max(max_dist_sq, x * x + y * y)\n\
        \                    else:\n                        break\n        return max_dist_sq"
      python3: "class Solution:\n    def robotSim(self, commands: List[int], obstacles:\
        \ List[List[int]]) -> int:\n        obstacle_set = set(map(tuple, obstacles))\n\
        \        dx = [0, 1, 0, -1]\n        dy = [1, 0, -1, 0]\n        x, y, di =\
        \ 0, 0, 0\n        max_dist_sq = 0\n\n        for cmd in commands:\n       \
        \     if cmd == -2:\n                di = (di + 3) % 4\n            elif cmd\
        \ == -1:\n                di = (di + 1) % 4\n            else:\n           \
        \     for _ in range(cmd):\n                    nx = x + dx[di]\n          \
        \          ny = y + dy[di]\n                    if (nx, ny) not in obstacle_set:\n\
        \                        x, y = nx, ny\n                        max_dist_sq\
        \ = max(max_dist_sq, x * x + y * y)\n                    else:\n           \
        \             break\n        return max_dist_sq"
      c: "#include <stdlib.h>\n#include <string.h>\n\n#define HASH_SIZE 20003\n\ntypedef\
        \ struct Node {\n    int x, y;\n    struct Node* next;\n} Node;\n\nint robotSim(int*\
        \ commands, int commandsSize, int** obstacles, int obstaclesSize, int* obstaclesColSize)\
        \ {\n    Node** table = (Node**)calloc(HASH_SIZE, sizeof(Node*));\n    Node*\
        \ pool = (Node*)malloc(obstaclesSize * sizeof(Node));\n\n    for (int i = 0;\
        \ i < obstaclesSize; i++) {\n        int ox = obstacles[i][0];\n        int\
        \ oy = obstacles[i][1];\n        long long val = (((long long)ox + 30000) *\
        \ 60001LL + (oy + 30000));\n        int h = (int)(val % HASH_SIZE);\n      \
        \  pool[i].x = ox;\n        pool[i].y = oy;\n        pool[i].next = table[h];\n\
        \        table[h] = &pool[i];\n    }\n\n    int dx[] = {0, 1, 0, -1};\n    int\
        \ dy[] = {1, 0, -1, 0};\n    int x = 0, y = 0, di = 0;\n    int maxDistSq =\
        \ 0;\n\n    for (int i = 0; i < commandsSize; i++) {\n        int cmd = commands[i];\n\
        \        if (cmd == -1) {\n            di = (di + 1) % 4;\n        } else if\
        \ (cmd == -2) {\n            di = (di + 3) % 4;\n        } else {\n        \
        \    for (int k = 0; k < cmd; k++) {\n                int nx = x + dx[di];\n\
        \                int ny = y + dy[di];\n                long long val = (((long\
        \ long)nx + 30000) * 60001LL + (ny + 30000));\n                int h = (int)(val\
        \ % HASH_SIZE);\n                int blocked = 0;\n                Node* curr\
        \ = table[h];\n                while (curr) {\n                    if (curr->x\
        \ == nx && curr->y == ny) {\n                        blocked = 1;\n        \
        \                break;\n                    }\n                    curr = curr->next;\n\
        \                }\n                if (!blocked) {\n                    x =\
        \ nx;\n                    y = ny;\n                    int d2 = x * x + y *\
        \ y;\n                    if (d2 > maxDistSq) maxDistSq = d2;\n            \
        \    } else {\n                    break;\n                }\n            }\n\
        \        }\n    }\n\n    free(pool);\n    free(table);\n    return maxDistSq;\n\
        }"
      csharp: "using System;\nusing System.Collections.Generic;\n\npublic class Solution\
        \ {\n    public int RobotSim(int[] commands, int[][] obstacles) {\n        HashSet<long>\
        \ obstacleSet = new HashSet<long>();\n        foreach (int[] obs in obstacles)\
        \ {\n            long ox = obs[0];\n            long oy = obs[1];\n        \
        \    obstacleSet.Add((ox << 32) | (oy & 0xFFFFFFFFL));\n        }\n\n      \
        \  int[] dx = { 0, 1, 0, -1 };\n        int[] dy = { 1, 0, -1, 0 };\n\n    \
        \    long x = 0, y = 0;\n        int di = 0;\n        long maxDistSq = 0;\n\n\
        \        foreach (int cmd in commands) {\n            if (cmd == -2) {\n   \
        \             di = (di + 3) % 4;\n            } else if (cmd == -1) {\n    \
        \            di = (di + 1) % 4;\n            } else {\n                for (int\
        \ i = 0; i < cmd; i++) {\n                    long nx = x + dx[di];\n      \
        \              long ny = y + dy[di];\n                    if (obstacleSet.Contains((nx\
        \ << 32) | (ny & 0xFFFFFFFFL))) {\n                        break;\n        \
        \            }\n                    x = nx;\n                    y = ny;\n \
        \                   maxDistSq = Math.Max(maxDistSq, x * x + y * y);\n      \
        \          }\n            }\n        }\n\n        return (int)maxDistSq;\n \
        \   }\n}"
      javascript: "/**\n * @param {number[]} commands\n * @param {number[][]} obstacles\n\
        \ * @return {number}\n */\nvar robotSim = function(commands, obstacles) {\n\
        \    const obstacleSet = new Set();\n    for (let i = 0; i < obstacles.length;\
        \ i++) {\n        obstacleSet.add(obstacles[i][0] + \",\" + obstacles[i][1]);\n\
        \    }\n\n    const dx = [0, 1, 0, -1];\n    const dy = [1, 0, -1, 0];\n\n \
        \   let x = 0, y = 0, di = 0;\n    let maxDistSq = 0;\n\n    for (let i = 0;\
        \ i < commands.length; i++) {\n        const cmd = commands[i];\n        if\
        \ (cmd === -2) {\n            di = (di + 3) % 4;\n        } else if (cmd ===\
        \ -1) {\n            di = (di + 1) % 4;\n        } else {\n            for (let\
        \ k = 0; k < cmd; k++) {\n                const nx = x + dx[di];\n         \
        \       const ny = y + dy[di];\n                if (obstacleSet.has(nx + \"\
        ,\" + ny)) {\n                    break;\n                }\n              \
        \  x = nx;\n                y = ny;\n                maxDistSq = Math.max(maxDistSq,\
        \ x * x + y * y);\n            }\n        }\n    }\n\n    return maxDistSq;\n\
        };"
      typescript: "function robotSim(commands: number[], obstacles: number[][]): number\
        \ {\n    const obstacleSet: Set<string> = new Set();\n    for (const obs of\
        \ obstacles) {\n        obstacleSet.add(`${obs[0]},${obs[1]}`);\n    }\n\n \
        \   const dx: number[] = [0, 1, 0, -1];\n    const dy: number[] = [1, 0, -1,\
        \ 0];\n\n    let x: number = 0;\n    let y: number = 0;\n    let di: number\
        \ = 0;\n    let maxDistSq: number = 0;\n\n    for (const cmd of commands) {\n\
        \        if (cmd === -2) {\n            di = (di + 3) % 4;\n        } else if\
        \ (cmd === -1) {\n            di = (di + 1) % 4;\n        } else {\n       \
        \     for (let k = 0; k < cmd; k++) {\n                const nx: number = x\
        \ + dx[di];\n                const ny: number = y + dy[di];\n              \
        \  if (obstacleSet.has(`${nx},${ny}`)) {\n                    break;\n     \
        \           }\n                x = nx;\n                y = ny;\n          \
        \      maxDistSq = Math.max(maxDistSq, x * x + y * y);\n            }\n    \
        \    }\n    }\n\n    return maxDistSq;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[] $commands\n     * @param\
        \ Integer[][] $obstacles\n     * @return Integer\n     */\n    function robotSim($commands,\
        \ $obstacles) {\n        $obstacleSet = [];\n        foreach ($obstacles as\
        \ $obs) {\n            $obstacleSet[$obs[0] . ',' . $obs[1]] = true;\n     \
        \   }\n\n        $dx = [0, 1, 0, -1];\n        $dy = [1, 0, -1, 0];\n\n    \
        \    $x = 0;\n        $y = 0;\n        $di = 0;\n        $maxDistSq = 0;\n\n\
        \        foreach ($commands as $cmd) {\n            if ($cmd == -2) {\n    \
        \            $di = ($di + 3) % 4;\n            } else if ($cmd == -1) {\n  \
        \              $di = ($di + 1) % 4;\n            } else {\n                for\
        \ ($i = 0; $i < $cmd; $i++) {\n                    $nx = $x + $dx[$di];\n  \
        \                  $ny = $y + $dy[$di];\n                    if (isset($obstacleSet[$nx\
        \ . ',' . $ny])) {\n                        break;\n                    }\n\
        \                    $x = $nx;\n                    $y = $ny;\n            \
        \        $maxDistSq = max($maxDistSq, $x * $x + $y * $y);\n                }\n\
        \            }\n        }\n\n        return (int)$maxDistSq;\n    }\n}"
      swift: "class Solution {\n    func robotSim(_ commands: [Int], _ obstacles: [[Int]])\
        \ -> Int {\n        var obstacleSet = Set<String>()\n        for obs in obstacles\
        \ {\n            obstacleSet.insert(\"\\(obs[0]),\\(obs[1])\")\n        }\n\n\
        \        let dx = [0, 1, 0, -1]\n        let dy = [1, 0, -1, 0]\n\n        var\
        \ x = 0\n        var y = 0\n        var di = 0\n        var maxDistSq = 0\n\n\
        \        for cmd in commands {\n            if cmd == -2 {\n               \
        \ di = (di + 3) % 4\n            } else if cmd == -1 {\n                di =\
        \ (di + 1) % 4\n            } else {\n                for _ in 0..<cmd {\n \
        \                   let nx = x + dx[di]\n                    let ny = y + dy[di]\n\
        \                    if obstacleSet.contains(\"\\(nx),\\(ny)\") {\n        \
        \                break\n                    }\n                    x = nx\n\
        \                    y = ny\n                    maxDistSq = max(maxDistSq,\
        \ x * x + y * y)\n                }\n            }\n        }\n\n        return\
        \ maxDistSq\n    }\n}"
      kotlin: "class Solution {\n    fun robotSim(commands: IntArray, obstacles: Array<IntArray>):\
        \ Int {\n        val dx = intArrayOf(0, 1, 0, -1)\n        val dy = intArrayOf(1,\
        \ 0, -1, 0)\n        var x = 0\n        var y = 0\n        var dir = 0\n   \
        \     var maxDist = 0\n\n        val obstacleSet = obstacles.map { (it[0].toLong()\
        \ shl 32) or (it[1].toLong() and 0xFFFFFFFFL) }.toSet()\n\n        for (cmd\
        \ in commands) {\n            if (cmd == -1) {\n                dir = (dir +\
        \ 1) % 4\n            } else if (cmd == -2) {\n                dir = (dir +\
        \ 3) % 4\n            } else {\n                for (i in 1..cmd) {\n      \
        \              val nx = x + dx[dir]\n                    val ny = y + dy[dir]\n\
        \                    val key = (nx.toLong() shl 32) or (ny.toLong() and 0xFFFFFFFFL)\n\
        \                    if (obstacleSet.contains(key)) break\n                \
        \    x = nx\n                    y = ny\n                    maxDist = maxOf(maxDist,\
        \ x * x + y * y)\n                }\n            }\n        }\n        return\
        \ maxDist\n    }\n}"
      dart: "class Solution {\n  int robotSim(List<int> commands, List<List<int>> obstacles)\
        \ {\n    int x = 0, y = 0, dir = 0, maxDist = 0;\n    final dx = [0, 1, 0, -1];\n\
        \    final dy = [1, 0, -1, 0];\n\n    final Set<int> obs = obstacles.map((o)\
        \ => (o[0] << 32) | (o[1] & 0xFFFFFFFF)).toSet();\n\n    for (var cmd in commands)\
        \ {\n      if (cmd == -1) {\n        dir = (dir + 1) % 4;\n      } else if (cmd\
        \ == -2) {\n        dir = (dir + 3) % 4;\n      } else {\n        for (int i\
        \ = 0; i < cmd; i++) {\n          int nx = x + dx[dir];\n          int ny =\
        \ y + dy[dir];\n          int key = (nx << 32) | (ny & 0xFFFFFFFF);\n      \
        \    if (obs.contains(key)) break;\n          x = nx;\n          y = ny;\n \
        \         int d = x * x + y * y;\n          if (d > maxDist) maxDist = d;\n\
        \        }\n      }\n    }\n    return maxDist;\n  }\n}"
      go: "func robotSim(commands []int, obstacles [][]int) int {\n    dx := []int{0,\
        \ 1, 0, -1}\n    dy := []int{1, 0, -1, 0}\n    x, y, dir, maxDist := 0, 0, 0,\
        \ 0\n\n    obsMap := make(map[[2]int]struct{})\n    for _, o := range obstacles\
        \ {\n        obsMap[[2]int{o[0], o[1]}] = struct{}{}\n    }\n\n    for _, cmd\
        \ := range commands {\n        if cmd == -1 {\n            dir = (dir + 1) %\
        \ 4\n        } else if cmd == -2 {\n            dir = (dir + 3) % 4\n      \
        \  } else {\n            for i := 0; i < cmd; i++ {\n                nx, ny\
        \ := x+dx[dir], y+dy[dir]\n                if _, ok := obsMap[[2]int{nx, ny}];\
        \ ok {\n                    break\n                }\n                x, y =\
        \ nx, ny\n                dist := x*x + y*y\n                if dist > maxDist\
        \ {\n                    maxDist = dist\n                }\n            }\n\
        \        }\n    }\n    return maxDist\n}"
      ruby: "# @param {Integer[]} commands\n# @param {Integer[][]} obstacles\n# @return\
        \ {Integer}\ndef robot_sim(commands, obstacles)\n  dx = [0, 1, 0, -1]\n  dy\
        \ = [1, 0, -1, 0]\n  x, y, dir, max_dist = 0, 0, 0, 0\n\n  obs = {}\n  obstacles.each\
        \ { |o| obs[[o[0], o[1]]] = true }\n\n  commands.each do |cmd|\n    if cmd ==\
        \ -1\n      dir = (dir + 1) % 4\n    elsif cmd == -2\n      dir = (dir + 3)\
        \ % 4\n    else\n      cmd.times do\n        nx = x + dx[dir]\n        ny =\
        \ y + dy[dir]\n        if obs[[nx, ny]]\n          break\n        end\n    \
        \    x, y = nx, ny\n        max_dist = [max_dist, x * x + y * y].max\n     \
        \ end\n    end\n  end\n  max_dist\nend"
      scala: "object Solution {\n    def robotSim(commands: Array[Int], obstacles: Array[Array[Int]]):\
        \ Int = {\n        val dx = Array(0, 1, 0, -1)\n        val dy = Array(1, 0,\
        \ -1, 0)\n        var x = 0\n        var y = 0\n        var dir = 0\n      \
        \  var maxDist = 0\n\n        val obs = obstacles.map(o => (o(0), o(1))).toSet\n\
        \n        for (cmd <- commands) {\n            if (cmd == -1) {\n          \
        \      dir = (dir + 1) % 4\n            } else if (cmd == -2) {\n          \
        \      dir = (dir + 3) % 4\n            } else {\n                var step =\
        \ 0\n                var blocked = false\n                while (step < cmd\
        \ && !blocked) {\n                    val nx = x + dx(dir)\n               \
        \     val ny = y + dy(dir)\n                    if (obs.contains((nx, ny)))\
        \ {\n                        blocked = true\n                    } else {\n\
        \                        x = nx\n                        y = ny\n          \
        \              maxDist = Math.max(maxDist, x * x + y * y)\n                \
        \        step += 1\n                    }\n                }\n            }\n\
        \        }\n        maxDist\n    }\n}"
      rust: "use std::collections::HashSet;\n\nimpl Solution {\n    pub fn robot_sim(commands:\
        \ Vec<i32>, obstacles: Vec<Vec<i32>>) -> i32 {\n        let mut obstacle_set\
        \ = HashSet::with_capacity(obstacles.len());\n        for obs in obstacles {\n\
        \            if obs.len() == 2 {\n                obstacle_set.insert((obs[0],\
        \ obs[1]));\n            }\n        }\n\n        let dirs = [(0, 1), (1, 0),\
        \ (0, -1), (-1, 0)];\n        let mut x: i32 = 0;\n        let mut y: i32 =\
        \ 0;\n        let mut d: usize = 0;\n        let mut max_dist: i32 = 0;\n\n\
        \        for cmd in commands {\n            match cmd {\n                -1\
        \ => d = (d + 1) % 4,\n                -2 => d = (d + 3) % 4,\n            \
        \    k => {\n                    for _ in 0..k {\n                        let\
        \ nx = x + dirs[d].0;\n                        let ny = y + dirs[d].1;\n   \
        \                     if obstacle_set.contains(&(nx, ny)) {\n              \
        \              break;\n                        }\n                        x\
        \ = nx;\n                        y = ny;\n                        max_dist =\
        \ max_dist.max(x * x + y * y);\n                    }\n                }\n \
        \           }\n        }\n        max_dist\n    }\n}"
      racket: "(require racket/set)\n\n(define/contract (robot-sim commands obstacles)\n\
        \  (-> (listof exact-integer?) (listof (listof exact-integer?)) exact-integer?)\n\
        \  (let ([obs-set (for/set ([o obstacles]) (cons (car o) (cadr o)))]\n     \
        \   [dirs '((0 . 1) (1 . 0) (0 . -1) (-1 . 0))])\n    (let loop ([cmds commands]\
        \ [x 0] [y 0] [d 0] [max-d 0])\n      (if (null? cmds)\n          max-d\n  \
        \        (let ([cmd (car cmds)])\n            (cond\n              [(= cmd -1)\
        \ (loop (cdr cmds) x y (modulo (+ d 1) 4) max-d)]\n              [(= cmd -2)\
        \ (loop (cdr cmds) x y (modulo (+ d 3) 4) max-d)]\n              [else\n   \
        \            (let move ([k cmd] [cx x] [cy y] [cm max-d])\n                \
        \ (if (= k 0)\n                     (loop (cdr cmds) cx cy d cm)\n         \
        \            (let* ([dir (list-ref dirs d)]\n                            [nx\
        \ (+ cx (car dir))]\n                            [ny (+ cy (cdr dir))])\n  \
        \                     (if (set-member? obs-set (cons nx ny))\n             \
        \              (loop (cdr cmds) cx cy d cm)\n                           (move\
        \ (- k 1) nx ny (max cm (+ (* nx nx) (* ny ny))))))))]))))))"
      erlang: "-spec robot_sim(Commands :: [integer()], Obstacles :: [[integer()]])\
        \ -> integer().\nrobot_sim(Commands, Obstacles) ->\n    ObsSet = sets:from_list([{lists:nth(1,\
        \ O), lists:nth(2, O)} || O <- Obstacles]),\n    Dirs = [{0, 1}, {1, 0}, {0,\
        \ -1}, {-1, 0}],\n    simulate(Commands, 0, 0, 0, 0, ObsSet, Dirs).\n\nsimulate([],\
        \ _X, _Y, _D, MaxDist, _ObsSet, _Dirs) ->\n    MaxDist;\nsimulate([Cmd | T],\
        \ X, Y, D, MaxDist, ObsSet, Dirs) ->\n    case Cmd of\n        -1 -> simulate(T,\
        \ X, Y, (D + 1) rem 4, MaxDist, ObsSet, Dirs);\n        -2 -> simulate(T, X,\
        \ Y, (D + 3) rem 4, MaxDist, ObsSet, Dirs);\n        _ ->\n            {NX,\
        \ NY, NMaxDist} = move(Cmd, X, Y, D, MaxDist, ObsSet, Dirs),\n            simulate(T,\
        \ NX, NY, D, NMaxDist, ObsSet, Dirs)\n    end.\n\nmove(0, X, Y, _D, MaxDist,\
        \ _ObsSet, _Dirs) ->\n    {X, Y, MaxDist};\nmove(K, X, Y, D, MaxDist, ObsSet,\
        \ Dirs) ->\n    {DX, DY} = lists:nth(D + 1, Dirs),\n    NX = X + DX,\n    NY\
        \ = Y + DY,\n    case sets:is_element({NX, NY}, ObsSet) of\n        true ->\
        \ {X, Y, MaxDist};\n        false ->\n            CurDist = NX * NX + NY * NY,\n\
        \            move(K - 1, NX, NY, D, max(MaxDist, CurDist), ObsSet, Dirs)\n \
        \   end."
      elixir: "defmodule Solution do\n  @spec robot_sim(commands :: [integer], obstacles\
        \ :: [[integer]]) :: integer\n  def robot_sim(commands, obstacles) do\n    obs_set\
        \ = MapSet.new(obstacles, fn [x, y] -> {x, y} end)\n    dirs = { {0, 1}, {1,\
        \ 0}, {0, -1}, {-1, 0} }\n\n    {_, _, _, max_dist} = Enum.reduce(commands,\
        \ {0, 0, 0, 0}, fn cmd, {x, y, d, max_d} ->\n      case cmd do\n        -1 ->\
        \ {x, y, rem(d + 1, 4), max_d}\n        -2 -> {x, y, rem(d + 3, 4), max_d}\n\
        \        k ->\n          {dx, dy} = elem(dirs, d)\n          {nx, ny, nm} =\
        \ Enum.reduce_while(1..k, {x, y, max_d}, fn _, {cx, cy, cm} ->\n           \
        \ nx = cx + dx\n            ny = cy + dy\n            if MapSet.member?(obs_set,\
        \ {nx, ny}) do\n              {:halt, {cx, cy, cm}}\n            else\n    \
        \          nm = max(cm, nx * nx + ny * ny)\n              {:cont, {nx, ny, nm}}\n\
        \            end\n          end)\n          {nx, ny, d, nm}\n      end\n   \
        \ end)\n\n    max_dist\n  end\nend"
    approach: 'The robot''s movement is simulated step-by-step to handle potential obstacle
      collisions. To efficiently check for obstacles, the input list of obstacle coordinates
      is converted into a hash set of coordinate pairs, allowing for average constant-time
      lookups. The robot''s orientation is maintained using a direction index that maps
      to specific movement vectors: (0, 1) for North, (1, 0) for East, (0, -1) for South,
      and (-1, 0) for West. Turning commands modify this index using modular arithmetic
      to ensure it remains within the bounds of the direction array.'
    time_complexity: O(N + M) where N is the number of obstacles and M is the number
      of commands. Initializing the hash set takes O(N) time. The simulation processes
      each command once, and since each movement command is restricted to at most 9
      steps, the total number of movement iterations is proportional to M, resulting
      in an overall linear time complexity.
    space_complexity: O(N) where N is the number of obstacles. This space is required
      to store the obstacle coordinates in a hash set to provide fast collision detection.
      The memory used for current coordinates, direction index, and the maximum distance
      tracking is constant.
    elapsed_time: 220.35223197937012
    model: gemini-3-flash-preview
    generated_at: '2026-04-06 01:54:32 '
---

## Problem #874: Walking Robot Simulation

**Difficulty:** Medium

**Topics:** Array, Hash Table, Simulation

## Problem Description

<p>A robot on an infinite XY-plane starts at point <code>(0, 0)</code> facing north. The robot receives an array of integers <code>commands</code>, which represents a sequence of moves that it needs to execute. There are only three possible types of instructions the robot can receive:</p>

<ul>
	<li><code>-2</code>: Turn left <code>90</code> degrees.</li>
	<li><code>-1</code>: Turn right <code>90</code> degrees.</li>
	<li><code>1 &lt;= k &lt;= 9</code>: Move forward <code>k</code> units, one unit at a time.</li>
</ul>

<p>Some of the grid squares are <code>obstacles</code>. The <code>i<sup>th</sup></code> obstacle is at grid point <code>obstacles[i] = (x<sub>i</sub>, y<sub>i</sub>)</code>. If the robot runs into an obstacle, it will stay in its current location (on the block adjacent to the obstacle) and move onto the next command.</p>

<p>Return the <strong>maximum squared Euclidean distance</strong> that the robot reaches at any point in its path (i.e. if the distance is <code>5</code>, return <code>25</code>).</p>

<p><strong>Note:</strong></p>

<ul>
	<li>There can be an obstacle at <code>(0, 0)</code>. If this happens, the robot will ignore the obstacle until it has moved off the origin. However, it will be unable to return to <code>(0, 0)</code> due to the obstacle.</li>
	<li>North means +Y direction.</li>
	<li>East means +X direction.</li>
	<li>South means -Y direction.</li>
	<li>West means -X direction.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">commands = [4,-1,3], obstacles = []</span></p>

<p><strong>Output:</strong> <span class="example-io">25</span></p>

<p><strong>Explanation: </strong></p>

<p>The robot starts at <code>(0, 0)</code>:</p>

<ol>
	<li>Move north 4 units to <code>(0, 4)</code>.</li>
	<li>Turn right.</li>
	<li>Move east 3 units to <code>(3, 4)</code>.</li>
</ol>

<p>The furthest point the robot ever gets from the origin is <code>(3, 4)</code>, which squared is <code>3<sup>2</sup> + 4<sup>2 </sup>= 25</code> units away.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">commands = [4,-1,4,-2,4], obstacles = [[2,4]]</span></p>

<p><strong>Output:</strong> <span class="example-io">65</span></p>

<p><strong>Explanation:</strong></p>

<p>The robot starts at <code>(0, 0)</code>:</p>

<ol>
	<li>Move north 4 units to <code>(0, 4)</code>.</li>
	<li>Turn right.</li>
	<li>Move east 1 unit and get blocked by the obstacle at <code>(2, 4)</code>, robot is at <code>(1, 4)</code>.</li>
	<li>Turn left.</li>
	<li>Move north 4 units to <code>(1, 8)</code>.</li>
</ol>

<p>The furthest point the robot ever gets from the origin is <code>(1, 8)</code>, which squared is <code>1<sup>2</sup> + 8<sup>2</sup> = 65</code> units away.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">commands = [6,-1,-1,6], obstacles = [[0,0]]</span></p>

<p><strong>Output:</strong> <span class="example-io">36</span></p>

<p><strong>Explanation:</strong></p>

<p>The robot starts at <code>(0, 0)</code>:</p>

<ol>
	<li>Move north 6 units to <code>(0, 6)</code>.</li>
	<li>Turn right.</li>
	<li>Turn right.</li>
	<li>Move south 5 units and get blocked by the obstacle at <code>(0,0)</code>, robot is at <code>(0, 1)</code>.</li>
</ol>

<p>The furthest point the robot ever gets from the origin is <code>(0, 6)</code>, which squared is <code>6<sup>2</sup> = 36</code> units away.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= commands.length &lt;= 10<sup>4</sup></code></li>
	<li><code>commands[i]</code> is either <code>-2</code>, <code>-1</code>, or an integer in the range <code>[1, 9]</code>.</li>
	<li><code>0 &lt;= obstacles.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-3 * 10<sup>4</sup> &lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= 3 * 10<sup>4</sup></code></li>
	<li>The answer is guaranteed to be less than <code>2<sup>31</sup></code>.</li>
</ul>


## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

The robot's movement is simulated step-by-step to handle potential obstacle collisions. To efficiently check for obstacles, the input list of obstacle coordinates is converted into a hash set of coordinate pairs, allowing for average constant-time lookups. The robot's orientation is maintained using a direction index that maps to specific movement vectors: (0, 1) for North, (1, 0) for East, (0, -1) for South, and (-1, 0) for West. Turning commands modify this index using modular arithmetic to ensure it remains within the bounds of the direction array.

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
#include <vector>
#include <unordered_set>
#include <algorithm>

using namespace std;

class Solution {
public:
    int robotSim(vector<int>& commands, vector<vector<int>>& obstacles) {
        unordered_set<long long> obstacleSet;
        for (const auto& obs : obstacles) {
            obstacleSet.insert(((long long)obs[0] + 30000) << 16 | ((long long)obs[1] + 30000));
        }

        int dx[] = {0, 1, 0, -1};
        int dy[] = {1, 0, -1, 0};
        int x = 0, y = 0, di = 0;
        int maxDistSq = 0;

        for (int cmd : commands) {
            if (cmd == -2) {
                di = (di + 3) % 4;
            } else if (cmd == -1) {
                di = (di + 1) % 4;
            } else {
                for (int k = 0; k < cmd; ++k) {
                    int nx = x + dx[di];
                    int ny = y + dy[di];
                    long long nextKey = ((long long)nx + 30000) << 16 | ((long long)ny + 30000);
                    if (obstacleSet.find(nextKey) == obstacleSet.end()) {
                        x = nx;
                        y = ny;
                        maxDistSq = max(maxDistSq, x * x + y * y);
                    } else {
                        break;
                    }
                }
            }
        }

        return maxDistSq;
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
    public int robotSim(int[] commands, int[][] obstacles) {
        Set<Long> obstacleSet = new HashSet<>();
        for (int[] obs : obstacles) {
            long ox = (long)obs[0] + 30000;
            long oy = (long)obs[1] + 30000;
            obstacleSet.add((ox << 16) | oy);
        }

        int[] dx = {0, 1, 0, -1};
        int[] dy = {1, 0, -1, 0};
        int x = 0, y = 0, di = 0;
        int maxDistSq = 0;

        for (int cmd : commands) {
            if (cmd == -2) {
                di = (di + 3) % 4;
            } else if (cmd == -1) {
                di = (di + 1) % 4;
            } else {
                for (int k = 0; k < cmd; k++) {
                    int nx = x + dx[di];
                    int ny = y + dy[di];
                    long nextKey = (((long)nx + 30000) << 16) | ((long)ny + 30000);
                    if (!obstacleSet.contains(nextKey)) {
                        x = nx;
                        y = ny;
                        maxDistSq = Math.max(maxDistSq, x * x + y * y);
                    } else {
                        break;
                    }
                }
            }
        }
        return maxDistSq;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        obstacle_set = set(tuple(obs) for obs in obstacles)
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x, y, di = 0, 0, 0
        max_dist_sq = 0

        for cmd in commands:
            if cmd == -2:
                di = (di + 3) % 4
            elif cmd == -1:
                di = (di + 1) % 4
            else:
                for _ in range(cmd):
                    nx = x + dx[di]
                    ny = y + dy[di]
                    if (nx, ny) not in obstacle_set:
                        x, y = nx, ny
                        max_dist_sq = max(max_dist_sq, x * x + y * y)
                    else:
                        break
        return max_dist_sq
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacle_set = set(map(tuple, obstacles))
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x, y, di = 0, 0, 0
        max_dist_sq = 0

        for cmd in commands:
            if cmd == -2:
                di = (di + 3) % 4
            elif cmd == -1:
                di = (di + 1) % 4
            else:
                for _ in range(cmd):
                    nx = x + dx[di]
                    ny = y + dy[di]
                    if (nx, ny) not in obstacle_set:
                        x, y = nx, ny
                        max_dist_sq = max(max_dist_sq, x * x + y * y)
                    else:
                        break
        return max_dist_sq
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <string.h>

#define HASH_SIZE 20003

typedef struct Node {
    int x, y;
    struct Node* next;
} Node;

int robotSim(int* commands, int commandsSize, int** obstacles, int obstaclesSize, int* obstaclesColSize) {
    Node** table = (Node**)calloc(HASH_SIZE, sizeof(Node*));
    Node* pool = (Node*)malloc(obstaclesSize * sizeof(Node));

    for (int i = 0; i < obstaclesSize; i++) {
        int ox = obstacles[i][0];
        int oy = obstacles[i][1];
        long long val = (((long long)ox + 30000) * 60001LL + (oy + 30000));
        int h = (int)(val % HASH_SIZE);
        pool[i].x = ox;
        pool[i].y = oy;
        pool[i].next = table[h];
        table[h] = &pool[i];
    }

    int dx[] = {0, 1, 0, -1};
    int dy[] = {1, 0, -1, 0};
    int x = 0, y = 0, di = 0;
    int maxDistSq = 0;

    for (int i = 0; i < commandsSize; i++) {
        int cmd = commands[i];
        if (cmd == -1) {
            di = (di + 1) % 4;
        } else if (cmd == -2) {
            di = (di + 3) % 4;
        } else {
            for (int k = 0; k < cmd; k++) {
                int nx = x + dx[di];
                int ny = y + dy[di];
                long long val = (((long long)nx + 30000) * 60001LL + (ny + 30000));
                int h = (int)(val % HASH_SIZE);
                int blocked = 0;
                Node* curr = table[h];
                while (curr) {
                    if (curr->x == nx && curr->y == ny) {
                        blocked = 1;
                        break;
                    }
                    curr = curr->next;
                }
                if (!blocked) {
                    x = nx;
                    y = ny;
                    int d2 = x * x + y * y;
                    if (d2 > maxDistSq) maxDistSq = d2;
                } else {
                    break;
                }
            }
        }
    }

    free(pool);
    free(table);
    return maxDistSq;
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
    public int RobotSim(int[] commands, int[][] obstacles) {
        HashSet<long> obstacleSet = new HashSet<long>();
        foreach (int[] obs in obstacles) {
            long ox = obs[0];
            long oy = obs[1];
            obstacleSet.Add((ox << 32) | (oy & 0xFFFFFFFFL));
        }

        int[] dx = { 0, 1, 0, -1 };
        int[] dy = { 1, 0, -1, 0 };

        long x = 0, y = 0;
        int di = 0;
        long maxDistSq = 0;

        foreach (int cmd in commands) {
            if (cmd == -2) {
                di = (di + 3) % 4;
            } else if (cmd == -1) {
                di = (di + 1) % 4;
            } else {
                for (int i = 0; i < cmd; i++) {
                    long nx = x + dx[di];
                    long ny = y + dy[di];
                    if (obstacleSet.Contains((nx << 32) | (ny & 0xFFFFFFFFL))) {
                        break;
                    }
                    x = nx;
                    y = ny;
                    maxDistSq = Math.Max(maxDistSq, x * x + y * y);
                }
            }
        }

        return (int)maxDistSq;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[]} commands
 * @param {number[][]} obstacles
 * @return {number}
 */
var robotSim = function(commands, obstacles) {
    const obstacleSet = new Set();
    for (let i = 0; i < obstacles.length; i++) {
        obstacleSet.add(obstacles[i][0] + "," + obstacles[i][1]);
    }

    const dx = [0, 1, 0, -1];
    const dy = [1, 0, -1, 0];

    let x = 0, y = 0, di = 0;
    let maxDistSq = 0;

    for (let i = 0; i < commands.length; i++) {
        const cmd = commands[i];
        if (cmd === -2) {
            di = (di + 3) % 4;
        } else if (cmd === -1) {
            di = (di + 1) % 4;
        } else {
            for (let k = 0; k < cmd; k++) {
                const nx = x + dx[di];
                const ny = y + dy[di];
                if (obstacleSet.has(nx + "," + ny)) {
                    break;
                }
                x = nx;
                y = ny;
                maxDistSq = Math.max(maxDistSq, x * x + y * y);
            }
        }
    }

    return maxDistSq;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function robotSim(commands: number[], obstacles: number[][]): number {
    const obstacleSet: Set<string> = new Set();
    for (const obs of obstacles) {
        obstacleSet.add(`${obs[0]},${obs[1]}`);
    }

    const dx: number[] = [0, 1, 0, -1];
    const dy: number[] = [1, 0, -1, 0];

    let x: number = 0;
    let y: number = 0;
    let di: number = 0;
    let maxDistSq: number = 0;

    for (const cmd of commands) {
        if (cmd === -2) {
            di = (di + 3) % 4;
        } else if (cmd === -1) {
            di = (di + 1) % 4;
        } else {
            for (let k = 0; k < cmd; k++) {
                const nx: number = x + dx[di];
                const ny: number = y + dy[di];
                if (obstacleSet.has(`${nx},${ny}`)) {
                    break;
                }
                x = nx;
                y = ny;
                maxDistSq = Math.max(maxDistSq, x * x + y * y);
            }
        }
    }

    return maxDistSq;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[] $commands
     * @param Integer[][] $obstacles
     * @return Integer
     */
    function robotSim($commands, $obstacles) {
        $obstacleSet = [];
        foreach ($obstacles as $obs) {
            $obstacleSet[$obs[0] . ',' . $obs[1]] = true;
        }

        $dx = [0, 1, 0, -1];
        $dy = [1, 0, -1, 0];

        $x = 0;
        $y = 0;
        $di = 0;
        $maxDistSq = 0;

        foreach ($commands as $cmd) {
            if ($cmd == -2) {
                $di = ($di + 3) % 4;
            } else if ($cmd == -1) {
                $di = ($di + 1) % 4;
            } else {
                for ($i = 0; $i < $cmd; $i++) {
                    $nx = $x + $dx[$di];
                    $ny = $y + $dy[$di];
                    if (isset($obstacleSet[$nx . ',' . $ny])) {
                        break;
                    }
                    $x = $nx;
                    $y = $ny;
                    $maxDistSq = max($maxDistSq, $x * $x + $y * $y);
                }
            }
        }

        return (int)$maxDistSq;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func robotSim(_ commands: [Int], _ obstacles: [[Int]]) -> Int {
        var obstacleSet = Set<String>()
        for obs in obstacles {
            obstacleSet.insert("\(obs[0]),\(obs[1])")
        }

        let dx = [0, 1, 0, -1]
        let dy = [1, 0, -1, 0]

        var x = 0
        var y = 0
        var di = 0
        var maxDistSq = 0

        for cmd in commands {
            if cmd == -2 {
                di = (di + 3) % 4
            } else if cmd == -1 {
                di = (di + 1) % 4
            } else {
                for _ in 0..<cmd {
                    let nx = x + dx[di]
                    let ny = y + dy[di]
                    if obstacleSet.contains("\(nx),\(ny)") {
                        break
                    }
                    x = nx
                    y = ny
                    maxDistSq = max(maxDistSq, x * x + y * y)
                }
            }
        }

        return maxDistSq
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun robotSim(commands: IntArray, obstacles: Array<IntArray>): Int {
        val dx = intArrayOf(0, 1, 0, -1)
        val dy = intArrayOf(1, 0, -1, 0)
        var x = 0
        var y = 0
        var dir = 0
        var maxDist = 0

        val obstacleSet = obstacles.map { (it[0].toLong() shl 32) or (it[1].toLong() and 0xFFFFFFFFL) }.toSet()

        for (cmd in commands) {
            if (cmd == -1) {
                dir = (dir + 1) % 4
            } else if (cmd == -2) {
                dir = (dir + 3) % 4
            } else {
                for (i in 1..cmd) {
                    val nx = x + dx[dir]
                    val ny = y + dy[dir]
                    val key = (nx.toLong() shl 32) or (ny.toLong() and 0xFFFFFFFFL)
                    if (obstacleSet.contains(key)) break
                    x = nx
                    y = ny
                    maxDist = maxOf(maxDist, x * x + y * y)
                }
            }
        }
        return maxDist
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int robotSim(List<int> commands, List<List<int>> obstacles) {
    int x = 0, y = 0, dir = 0, maxDist = 0;
    final dx = [0, 1, 0, -1];
    final dy = [1, 0, -1, 0];

    final Set<int> obs = obstacles.map((o) => (o[0] << 32) | (o[1] & 0xFFFFFFFF)).toSet();

    for (var cmd in commands) {
      if (cmd == -1) {
        dir = (dir + 1) % 4;
      } else if (cmd == -2) {
        dir = (dir + 3) % 4;
      } else {
        for (int i = 0; i < cmd; i++) {
          int nx = x + dx[dir];
          int ny = y + dy[dir];
          int key = (nx << 32) | (ny & 0xFFFFFFFF);
          if (obs.contains(key)) break;
          x = nx;
          y = ny;
          int d = x * x + y * y;
          if (d > maxDist) maxDist = d;
        }
      }
    }
    return maxDist;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func robotSim(commands []int, obstacles [][]int) int {
    dx := []int{0, 1, 0, -1}
    dy := []int{1, 0, -1, 0}
    x, y, dir, maxDist := 0, 0, 0, 0

    obsMap := make(map[[2]int]struct{})
    for _, o := range obstacles {
        obsMap[[2]int{o[0], o[1]}] = struct{}{}
    }

    for _, cmd := range commands {
        if cmd == -1 {
            dir = (dir + 1) % 4
        } else if cmd == -2 {
            dir = (dir + 3) % 4
        } else {
            for i := 0; i < cmd; i++ {
                nx, ny := x+dx[dir], y+dy[dir]
                if _, ok := obsMap[[2]int{nx, ny}]; ok {
                    break
                }
                x, y = nx, ny
                dist := x*x + y*y
                if dist > maxDist {
                    maxDist = dist
                }
            }
        }
    }
    return maxDist
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[]} commands
# @param {Integer[][]} obstacles
# @return {Integer}
def robot_sim(commands, obstacles)
  dx = [0, 1, 0, -1]
  dy = [1, 0, -1, 0]
  x, y, dir, max_dist = 0, 0, 0, 0

  obs = {}
  obstacles.each { |o| obs[[o[0], o[1]]] = true }

  commands.each do |cmd|
    if cmd == -1
      dir = (dir + 1) % 4
    elsif cmd == -2
      dir = (dir + 3) % 4
    else
      cmd.times do
        nx = x + dx[dir]
        ny = y + dy[dir]
        if obs[[nx, ny]]
          break
        end
        x, y = nx, ny
        max_dist = [max_dist, x * x + y * y].max
      end
    end
  end
  max_dist
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def robotSim(commands: Array[Int], obstacles: Array[Array[Int]]): Int = {
        val dx = Array(0, 1, 0, -1)
        val dy = Array(1, 0, -1, 0)
        var x = 0
        var y = 0
        var dir = 0
        var maxDist = 0

        val obs = obstacles.map(o => (o(0), o(1))).toSet

        for (cmd <- commands) {
            if (cmd == -1) {
                dir = (dir + 1) % 4
            } else if (cmd == -2) {
                dir = (dir + 3) % 4
            } else {
                var step = 0
                var blocked = false
                while (step < cmd && !blocked) {
                    val nx = x + dx(dir)
                    val ny = y + dy(dir)
                    if (obs.contains((nx, ny))) {
                        blocked = true
                    } else {
                        x = nx
                        y = ny
                        maxDist = Math.max(maxDist, x * x + y * y)
                        step += 1
                    }
                }
            }
        }
        maxDist
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
use std::collections::HashSet;

impl Solution {
    pub fn robot_sim(commands: Vec<i32>, obstacles: Vec<Vec<i32>>) -> i32 {
        let mut obstacle_set = HashSet::with_capacity(obstacles.len());
        for obs in obstacles {
            if obs.len() == 2 {
                obstacle_set.insert((obs[0], obs[1]));
            }
        }

        let dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)];
        let mut x: i32 = 0;
        let mut y: i32 = 0;
        let mut d: usize = 0;
        let mut max_dist: i32 = 0;

        for cmd in commands {
            match cmd {
                -1 => d = (d + 1) % 4,
                -2 => d = (d + 3) % 4,
                k => {
                    for _ in 0..k {
                        let nx = x + dirs[d].0;
                        let ny = y + dirs[d].1;
                        if obstacle_set.contains(&(nx, ny)) {
                            break;
                        }
                        x = nx;
                        y = ny;
                        max_dist = max_dist.max(x * x + y * y);
                    }
                }
            }
        }
        max_dist
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(require racket/set)

(define/contract (robot-sim commands obstacles)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) exact-integer?)
  (let ([obs-set (for/set ([o obstacles]) (cons (car o) (cadr o)))]
        [dirs '((0 . 1) (1 . 0) (0 . -1) (-1 . 0))])
    (let loop ([cmds commands] [x 0] [y 0] [d 0] [max-d 0])
      (if (null? cmds)
          max-d
          (let ([cmd (car cmds)])
            (cond
              [(= cmd -1) (loop (cdr cmds) x y (modulo (+ d 1) 4) max-d)]
              [(= cmd -2) (loop (cdr cmds) x y (modulo (+ d 3) 4) max-d)]
              [else
               (let move ([k cmd] [cx x] [cy y] [cm max-d])
                 (if (= k 0)
                     (loop (cdr cmds) cx cy d cm)
                     (let* ([dir (list-ref dirs d)]
                            [nx (+ cx (car dir))]
                            [ny (+ cy (cdr dir))])
                       (if (set-member? obs-set (cons nx ny))
                           (loop (cdr cmds) cx cy d cm)
                           (move (- k 1) nx ny (max cm (+ (* nx nx) (* ny ny))))))))]))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec robot_sim(Commands :: [integer()], Obstacles :: [[integer()]]) -> integer().
robot_sim(Commands, Obstacles) ->
    ObsSet = sets:from_list([{lists:nth(1, O), lists:nth(2, O)} || O <- Obstacles]),
    Dirs = [{0, 1}, {1, 0}, {0, -1}, {-1, 0}],
    simulate(Commands, 0, 0, 0, 0, ObsSet, Dirs).

simulate([], _X, _Y, _D, MaxDist, _ObsSet, _Dirs) ->
    MaxDist;
simulate([Cmd | T], X, Y, D, MaxDist, ObsSet, Dirs) ->
    case Cmd of
        -1 -> simulate(T, X, Y, (D + 1) rem 4, MaxDist, ObsSet, Dirs);
        -2 -> simulate(T, X, Y, (D + 3) rem 4, MaxDist, ObsSet, Dirs);
        _ ->
            {NX, NY, NMaxDist} = move(Cmd, X, Y, D, MaxDist, ObsSet, Dirs),
            simulate(T, NX, NY, D, NMaxDist, ObsSet, Dirs)
    end.

move(0, X, Y, _D, MaxDist, _ObsSet, _Dirs) ->
    {X, Y, MaxDist};
move(K, X, Y, D, MaxDist, ObsSet, Dirs) ->
    {DX, DY} = lists:nth(D + 1, Dirs),
    NX = X + DX,
    NY = Y + DY,
    case sets:is_element({NX, NY}, ObsSet) of
        true -> {X, Y, MaxDist};
        false ->
            CurDist = NX * NX + NY * NY,
            move(K - 1, NX, NY, D, max(MaxDist, CurDist), ObsSet, Dirs)
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec robot_sim(commands :: [integer], obstacles :: [[integer]]) :: integer
  def robot_sim(commands, obstacles) do
    obs_set = MapSet.new(obstacles, fn [x, y] -> {x, y} end)
    dirs = { {0, 1}, {1, 0}, {0, -1}, {-1, 0} }

    {_, _, _, max_dist} = Enum.reduce(commands, {0, 0, 0, 0}, fn cmd, {x, y, d, max_d} ->
      case cmd do
        -1 -> {x, y, rem(d + 1, 4), max_d}
        -2 -> {x, y, rem(d + 3, 4), max_d}
        k ->
          {dx, dy} = elem(dirs, d)
          {nx, ny, nm} = Enum.reduce_while(1..k, {x, y, max_d}, fn _, {cx, cy, cm} ->
            nx = cx + dx
            ny = cy + dy
            if MapSet.member?(obs_set, {nx, ny}) do
              {:halt, {cx, cy, cm}}
            else
              nm = max(cm, nx * nx + ny * ny)
              {:cont, {nx, ny, nm}}
            end
          end)
          {nx, ny, d, nm}
      end
    end)

    max_dist
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N + M) where N is the number of obstacles and M is the number of commands. Initializing the hash set takes O(N) time. The simulation processes each command once, and since each movement command is restricted to at most 9 steps, the total number of movement iterations is proportional to M, resulting in an overall linear time complexity.
- **Space Complexity:** O(N) where N is the number of obstacles. This space is required to store the obstacle coordinates in a hash set to provide fast collision detection. The memory used for current coordinates, direction index, and the maximum distance tracking is constant.
