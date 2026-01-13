---
layout: post
title: "Separate Squares I"
date: 2026-01-13 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Binary Search"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/separate-squares-i/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    double separateSquares(std::vector<std::vector<int>>&\
        \ squares) {\n        auto check = [&](double h) {\n            double total_area_below\
        \ = 0.0;\n            double total_area_above = 0.0;\n\n            for (const\
        \ auto& square : squares) {\n                long long y_ll = square[1];\n \
        \               long long l_ll = square[2];\n\n                double bottom\
        \ = static_cast<double>(y_ll);\n                double top = static_cast<double>(y_ll\
        \ + l_ll);\n                double width = static_cast<double>(l_ll);\n\n  \
        \              if (h <= bottom) {\n                    total_area_above += width\
        \ * width;\n                } else if (h >= top) {\n                    total_area_below\
        \ += width * width;\n                } else {\n                    double height_below\
        \ = h - bottom;\n                    double height_above = top - h;\n      \
        \              total_area_below += width * height_below;\n                 \
        \   total_area_above += width * height_above;\n                }\n         \
        \   }\n            return total_area_below - total_area_above;\n        };\n\
        \n        double low = 0.0;\n        double high = 2e9 + 1.0; \n\n        for\
        \ (int i = 0; i < 100; ++i) {\n            double mid = low + (high - low) /\
        \ 2.0;\n            double diff = check(mid);\n\n            if (diff >= 0)\
        \ {\n                high = mid;\n            } else {\n                low\
        \ = mid;\n            }\n        }\n\n        return high;\n    }\n};"
      java: "class Solution {\n    public double separateSquares(int[][] squares) {\n\
        \        double low = 0.0;\n        double high = 2e9 + 1.0; \n\n        for\
        \ (int i = 0; i < 100; ++i) {\n            double mid = low + (high - low) /\
        \ 2.0;\n            double diff = check(mid, squares);\n\n            if (diff\
        \ >= 0) {\n                high = mid;\n            } else {\n             \
        \   low = mid;\n            }\n        }\n\n        return high;\n    }\n\n\
        \    private double check(double h, int[][] squares) {\n        double total_area_below\
        \ = 0.0;\n        double total_area_above = 0.0;\n\n        for (int[] square\
        \ : squares) {\n            int y_int = square[1];\n            int l_int =\
        \ square[2];\n\n            double bottom = (double)y_int;\n            double\
        \ top = (double)(y_int + l_int);\n            double width = (double)l_int;\n\
        \n            if (h <= bottom) {\n                total_area_above += width\
        \ * width;\n            } else if (h >= top) {\n                total_area_below\
        \ += width * width;\n            } else {\n                double height_below\
        \ = h - bottom;\n                double height_above = top - h;\n          \
        \      total_area_below += width * height_below;\n                total_area_above\
        \ += width * height_above;\n            }\n        }\n        return total_area_below\
        \ - total_area_above;\n    }\n}"
      python: "class Solution(object):\n    def separateSquares(self, squares):\n  \
        \      \"\"\"\n        :type squares: List[List[int]]\n        :rtype: float\n\
        \        \"\"\"\n\n        def check(h):\n            total_area_below = 0.0\n\
        \            total_area_above = 0.0\n\n            for square in squares:\n\
        \                x, y, l = square\n                bottom = float(y)\n     \
        \           top = float(y + l)\n                width = float(l)\n\n       \
        \         if h <= bottom:\n                    total_area_above += width * width\n\
        \                elif h >= top:\n                    total_area_below += width\
        \ * width\n                else:\n                    height_below = h - bottom\n\
        \                    height_above = top - h\n                    total_area_below\
        \ += width * height_below\n                    total_area_above += width * height_above\n\
        \n            return total_area_below - total_area_above\n\n        low = 0.0\n\
        \        high = 2 * 10**9 + 1.0 \n\n        for _ in range(100): \n        \
        \    mid = low + (high - low) / 2.0\n            diff = check(mid)\n\n     \
        \       if diff >= 0:\n                high = mid\n            else:\n     \
        \           low = mid\n\n        return high"
      python3: "class Solution:\n    def separateSquares(self, squares: List[List[int]])\
        \ -> float:\n\n        def check(h: float) -> float:\n            total_area_below\
        \ = 0.0\n            total_area_above = 0.0\n\n            for x, y, l in squares:\n\
        \                bottom = float(y)\n                top = float(y + l)\n   \
        \             width = float(l)\n\n                if h <= bottom:\n        \
        \            total_area_above += width * width\n                elif h >= top:\n\
        \                    total_area_below += width * width\n                else:\n\
        \                    height_below = h - bottom\n                    height_above\
        \ = top - h\n                    total_area_below += width * height_below\n\
        \                    total_area_above += width * height_above\n\n          \
        \  return total_area_below - total_area_above\n\n        low = 0.0\n       \
        \ high = 2 * 10**9 + 1.0 \n\n        for _ in range(100): \n            mid\
        \ = low + (high - low) / 2.0\n            diff = check(mid)\n\n            if\
        \ diff >= 0:\n                high = mid\n            else:\n              \
        \  low = mid\n\n        return high"
      c: "double check_c(double h, int** squares, int squaresSize) {\n    double total_area_below\
        \ = 0.0;\n    double total_area_above = 0.0;\n\n    for (int i = 0; i < squaresSize;\
        \ ++i) {\n        int y_int = squares[i][1];\n        int l_int = squares[i][2];\n\
        \n        double bottom = (double)y_int;\n        double top = (double)(y_int\
        \ + l_int);\n        double width = (double)l_int;\n\n        if (h <= bottom)\
        \ {\n            total_area_above += width * width;\n        } else if (h >=\
        \ top) {\n            total_area_below += width * width;\n        } else {\n\
        \            double height_below = h - bottom;\n            double height_above\
        \ = top - h;\n            total_area_below += width * height_below;\n      \
        \      total_area_above += width * height_above;\n        }\n    }\n    return\
        \ total_area_below - total_area_above;\n}\n\ndouble separateSquares(int** squares,\
        \ int squaresSize, int* squaresColSize) {\n    double low = 0.0;\n    double\
        \ high = 2e9 + 1.0; \n\n    for (int i = 0; i < 100; ++i) {\n        double\
        \ mid = low + (high - low) / 2.0;\n        double diff = check_c(mid, squares,\
        \ squaresSize);\n\n        if (diff >= 0) {\n            high = mid;\n     \
        \   } else {\n            low = mid;\n        }\n    }\n\n    return high;\n\
        }"
      csharp: "public class Solution {\n    public double SeparateSquares(int[][] squares)\
        \ {\n\n        double low = 0.0;\n        double high = 2e9 + 1.0; \n\n    \
        \    for (int i = 0; i < 100; ++i) {\n            double mid = low + (high -\
        \ low) / 2.0;\n            double diff = Check(mid, squares);\n\n          \
        \  if (diff >= 0) {\n                high = mid;\n            } else {\n   \
        \             low = mid;\n            }\n        }\n\n        return high;\n\
        \    }\n\n    private double Check(double h, int[][] squares) {\n        double\
        \ total_area_below = 0.0;\n        double total_area_above = 0.0;\n\n      \
        \  foreach (int[] square in squares) {\n            int y_int = square[1];\n\
        \            int l_int = square[2];\n\n            double bottom = (double)y_int;\n\
        \            double top = (double)(y_int + l_int);\n            double width\
        \ = (double)l_int;\n\n            if (h <= bottom) {\n                total_area_above\
        \ += width * width;\n            } else if (h >= top) {\n                total_area_below\
        \ += width * width;\n            } else {\n                double height_below\
        \ = h - bottom;\n                double height_above = top - h;\n          \
        \      total_area_below += width * height_below;\n                total_area_above\
        \ += width * height_above;\n            }\n        }\n        return total_area_below\
        \ - total_area_above;\n    }\n}"
      javascript: "/**\n * @param {number[][]} squares\n * @return {number}\n */\nvar\
        \ separateSquares = function(squares) {\n\n    const check = (h) => {\n    \
        \    let total_area_below = 0.0;\n        let total_area_above = 0.0;\n\n  \
        \      for (const square of squares) {\n            const y_int = square[1];\n\
        \            const l_int = square[2];\n\n            const bottom = y_int; \n\
        \            const top = y_int + l_int;\n            const width = l_int;\n\n\
        \            if (h <= bottom) {\n                total_area_above += width *\
        \ width;\n            } else if (h >= top) {\n                total_area_below\
        \ += width * width;\n            } else {\n                const height_below\
        \ = h - bottom;\n                const height_above = top - h;\n           \
        \     total_area_below += width * height_below;\n                total_area_above\
        \ += width * height_above;\n            }\n        }\n        return total_area_below\
        \ - total_area_above;\n    };\n\n    let low = 0.0;\n    let high = 2e9 + 1.0;\
        \ \n\n    for (let i = 0; i < 100; ++i) {\n        const mid = low + (high -\
        \ low) / 2.0;\n        const diff = check(mid);\n\n        if (diff >= 0) {\n\
        \            high = mid;\n        } else {\n            low = mid;\n       \
        \ }\n    }\n\n    return high;\n};"
      typescript: "function separateSquares(squares: number[][]): number {\n\n    const\
        \ check = (h: number): number => {\n        let total_area_below: number = 0.0;\n\
        \        let total_area_above: number = 0.0;\n\n        for (const square of\
        \ squares) {\n            const y_int: number = square[1];\n            const\
        \ l_int: number = square[2];\n\n            const bottom: number = y_int;\n\
        \            const top: number = y_int + l_int;\n            const width: number\
        \ = l_int;\n\n            if (h <= bottom) {\n                total_area_above\
        \ += width * width;\n            } else if (h >= top) {\n                total_area_below\
        \ += width * width;\n            } else {\n                const height_below:\
        \ number = h - bottom;\n                const height_above: number = top - h;\n\
        \                total_area_below += width * height_below;\n               \
        \ total_area_above += width * height_above;\n            }\n        }\n    \
        \    return total_area_below - total_area_above;\n    };\n\n    let low: number\
        \ = 0.0;\n    let high: number = 2e9 + 1.0; \n\n    for (let i = 0; i < 100;\
        \ ++i) {\n        const mid: number = low + (high - low) / 2.0;\n        const\
        \ diff: number = check(mid);\n\n        if (diff >= 0) {\n            high =\
        \ mid;\n        } else {\n            low = mid;\n        }\n    }\n\n    return\
        \ high;\n};"
      php: "class Solution {\n\n    /**\n     * @param Integer[][] $squares\n     *\
        \ @return Float\n     */\n    function separateSquares($squares) {\n\n     \
        \   $check = function($h) use ($squares) {\n            $total_area_below =\
        \ 0.0;\n            $total_area_above = 0.0;\n\n            foreach ($squares\
        \ as $square) {\n                $y_int = $square[1];\n                $l_int\
        \ = $square[2];\n\n                $bottom = (float)$y_int;\n              \
        \  $top = (float)($y_int + $l_int);\n                $width = (float)$l_int;\n\
        \n                if ($h <= $bottom) {\n                    $total_area_above\
        \ += $width * $width;\n                } elseif ($h >= $top) {\n           \
        \         $total_area_below += $width * $width;\n                } else {\n\
        \                    $height_below = $h - $bottom;\n                    $height_above\
        \ = $top - $h;\n                    $total_area_below += $width * $height_below;\n\
        \                    $total_area_above += $width * $height_above;\n        \
        \        }\n            }\n            return $total_area_below - $total_area_above;\n\
        \        };\n\n        $low = 0.0;\n        $high = 2e9 + 1.0; \n\n        for\
        \ ($i = 0; $i < 100; ++$i) {\n            $mid = $low + ($high - $low) / 2.0;\n\
        \            $diff = $check($mid);\n\n            if ($diff >= 0) {\n      \
        \          $high = $mid;\n            } else {\n                $low = $mid;\n\
        \            }\n        }\n\n        return $high;\n    }\n}"
      swift: "class Solution {\n    func separateSquares(_ squares: [[Int]]) -> Double\
        \ {\n\n        let check = { (h: Double) -> Double in\n            var total_area_below:\
        \ Double = 0.0\n            var total_area_above: Double = 0.0\n\n         \
        \   for square in squares {\n                let y_int = square[1]\n       \
        \         let l_int = square[2]\n\n                let bottom = Double(y_int)\n\
        \                let top = Double(y_int + l_int)\n                let width\
        \ = Double(l_int)\n\n                if h <= bottom {\n                    total_area_above\
        \ += width * width\n                } else if h >= top {\n                 \
        \   total_area_below += width * width\n                } else {\n          \
        \          let height_below = h - bottom\n                    let height_above\
        \ = top - h\n                    total_area_below += width * height_below\n\
        \                    total_area_above += width * height_above\n            \
        \    }\n            }\n            return total_area_below - total_area_above\n\
        \        }\n\n        var low: Double = 0.0\n        var high: Double = 2e9\
        \ + 1.0 \n\n        for _ in 0..<100 {\n            let mid = low + (high -\
        \ low) / 2.0\n            let diff = check(mid)\n\n            if diff >= 0\
        \ {\n                high = mid\n            } else {\n                low =\
        \ mid\n            }\n        }\n\n        return high\n    }\n}"
      kotlin: "class Solution {\n    fun separateSquares(squares: Array<IntArray>):\
        \ Double {\n        var totalArea = 0.0\n        for (square in squares) {\n\
        \            val l = square[2].toDouble()\n            totalArea += l * l\n\
        \        }\n\n        val targetAreaBelow = totalArea / 2.0\n\n        var low\
        \ = 0.0\n        var high = 2_000_000_000.0 + 1.0\n\n        for (i in 0 until\
        \ 100) {\n            val mid = (low + high) / 2.0\n            var currentAreaBelow\
        \ = 0.0\n\n            for (square in squares) {\n                val y = square[1].toDouble()\n\
        \                val l = square[2].toDouble()\n                val yBottom =\
        \ y\n                val yTop = y + l\n\n                if (yBottom >= mid)\
        \ {\n                    continue\n                } else if (yTop <= mid) {\n\
        \                    currentAreaBelow += l * l\n                } else {\n \
        \                   val heightBelow = mid - yBottom\n                    currentAreaBelow\
        \ += l * heightBelow\n                }\n            }\n\n            if (currentAreaBelow\
        \ < targetAreaBelow) {\n                low = mid\n            } else {\n  \
        \              high = mid\n            }\n        }\n        return high\n \
        \   }\n}"
      dart: "import 'dart:math';\n\nclass Solution {\n  double separateSquares(List<List<int>>\
        \ squares) {\n    double totalArea = 0.0;\n    for (var square in squares) {\n\
        \      double l = square[2].toDouble();\n      totalArea += l * l;\n    }\n\n\
        \    double targetAreaBelow = totalArea / 2.0;\n\n    double low = 0.0;\n  \
        \  double high = 2000000000.0 + 1.0;\n\n    for (int i = 0; i < 100; i++) {\n\
        \      double mid = (low + high) / 2.0;\n      double currentAreaBelow = 0.0;\n\
        \n      for (var square in squares) {\n        double y = square[1].toDouble();\n\
        \        double l = square[2].toDouble();\n        double yBottom = y;\n   \
        \     double yTop = y + l;\n\n        if (yBottom >= mid) {\n          continue;\n\
        \        } else if (yTop <= mid) {\n          currentAreaBelow += l * l;\n \
        \       } else {\n          double heightBelow = mid - yBottom;\n          currentAreaBelow\
        \ += l * heightBelow;\n        }\n      }\n\n      if (currentAreaBelow < targetAreaBelow)\
        \ {\n        low = mid;\n      } else {\n        high = mid;\n      }\n    }\n\
        \    return high;\n  }\n}"
      go: "func separateSquares(squares [][]int) float64 {\n    totalArea := 0.0\n \
        \   for _, square := range squares {\n        l := float64(square[2])\n    \
        \    totalArea += l * l\n    }\n\n    targetAreaBelow := totalArea / 2.0\n\n\
        \    low := 0.0\n    high := 2000000000.0 + 1.0\n\n    for i := 0; i < 100;\
        \ i++ {\n        mid := (low + high) / 2.0\n        currentAreaBelow := 0.0\n\
        \n        for _, square := range squares {\n            y := float64(square[1])\n\
        \            l := float64(square[2])\n            yBottom := y\n           \
        \ yTop := y + l\n\n            if yBottom >= mid {\n                continue\n\
        \            } else if yTop <= mid {\n                currentAreaBelow += l\
        \ * l\n            } else {\n                heightBelow := mid - yBottom\n\
        \                currentAreaBelow += l * heightBelow\n            }\n      \
        \  }\n\n        if currentAreaBelow < targetAreaBelow {\n            low = mid\n\
        \        } else {\n            high = mid\n        }\n    }\n    return high\n\
        }"
      ruby: "# @param {Integer[][]} squares\n# @return {Float}\ndef separate_squares(squares)\n\
        \    total_area = 0.0\n    squares.each do |square|\n        l = square[2].to_f\n\
        \        total_area += l * l\n    end\n\n    target_area_below = total_area\
        \ / 2.0\n\n    low = 0.0\n    high = 2_000_000_000.0 + 1.0\n\n    100.times\
        \ do\n        mid = (low + high) / 2.0\n        current_area_below = 0.0\n\n\
        \        squares.each do |square|\n            y = square[1].to_f\n        \
        \    l = square[2].to_f\n            y_bottom = y\n            y_top = y + l\n\
        \n            if y_bottom >= mid\n                next\n            elsif y_top\
        \ <= mid\n                current_area_below += l * l\n            else\n  \
        \              height_below = mid - y_bottom\n                current_area_below\
        \ += l * height_below\n            end\n        end\n\n        if current_area_below\
        \ < target_area_below\n            low = mid\n        else\n            high\
        \ = mid\n        end\n    end\n    high\nend"
      scala: "object Solution {\n    def separateSquares(squares: Array[Array[Int]]):\
        \ Double = {\n        var totalArea = 0.0\n        for (square <- squares) {\n\
        \            val l = square(2).toDouble\n            totalArea += l * l\n  \
        \      }\n\n        val targetAreaBelow = totalArea / 2.0\n\n        var low\
        \ = 0.0\n        var high = 2_000_000_000.0 + 1.0\n\n        for (_ <- 0 until\
        \ 100) {\n            val mid = (low + high) / 2.0\n            var currentAreaBelow\
        \ = 0.0\n\n            for (square <- squares) {\n                val y = square(1).toDouble\n\
        \                val l = square(2).toDouble\n                val yBottom = y\n\
        \                val yTop = y + l\n\n                if (yBottom >= mid) {\n\
        \n                } else if (yTop <= mid) {\n                    currentAreaBelow\
        \ += l * l\n                } else {\n                    val heightBelow =\
        \ mid - yBottom\n                    currentAreaBelow += l * heightBelow\n \
        \               }\n            }\n\n            if (currentAreaBelow < targetAreaBelow)\
        \ {\n                low = mid\n            } else {\n                high =\
        \ mid\n            }\n        }\n        high\n    }\n}"
      rust: "impl Solution {\n    pub fn separate_squares(squares: Vec<Vec<i32>>) ->\
        \ f64 {\n        let mut total_area = 0.0;\n        for square in &squares {\n\
        \            let l = square[2] as f64;\n            total_area += l * l;\n \
        \       }\n\n        let target_area_below = total_area / 2.0;\n\n        let\
        \ mut low = 0.0;\n        let mut high = 2_000_000_000.0 + 1.0;\n\n        for\
        \ _ in 0..100 {\n            let mid = (low + high) / 2.0;\n            let\
        \ mut current_area_below = 0.0;\n\n            for square in &squares {\n  \
        \              let y = square[1] as f64;\n                let l = square[2]\
        \ as f64;\n                let y_bottom = y;\n                let y_top = y\
        \ + l;\n\n                if y_bottom >= mid {\n                    continue;\n\
        \                } else if y_top <= mid {\n                    current_area_below\
        \ += l * l;\n                } else {\n                    let height_below\
        \ = mid - y_bottom;\n                    current_area_below += l * height_below;\n\
        \                }\n            }\n\n            if current_area_below < target_area_below\
        \ {\n                low = mid;\n            } else {\n                high\
        \ = mid;\n            }\n        }\n        high\n    }\n}"
      racket: "(define/contract (separate-squares squares)\n  (-> (listof (listof exact-integer?))\
        \ flonum?)\n  (let* ([total-area (for/sum ([square squares])\n             \
        \          (let ([l (list-ref square 2)])\n                         (* (exact->flonum\
        \ l) (exact->flonum l))))]\n         [target-area-below (/ total-area 2.0)]\n\
        \         [low 0.0]\n         [high (+ 2000000000.0 1.0)])\n\n    (for ([_ (in-range\
        \ 100)])\n      (let* ([mid (/ (+ low high) 2.0)]\n             [current-area-below\
        \ (for/sum ([square squares])\n                                   (let* ([y\
        \ (list-ref square 1)]\n                                          [l (list-ref\
        \ square 2)]\n                                          [y-flonum (exact->flonum\
        \ y)]\n                                          [l-flonum (exact->flonum l)]\n\
        \                                          [y-bottom y-flonum]\n           \
        \                               [y-top (+ y-flonum l-flonum)])\n           \
        \                          (cond\n                                       [(>=\
        \ y-bottom mid) 0.0]\n                                       [(<= y-top mid)\
        \ (* l-flonum l-flonum)]\n                                       [else\n   \
        \                                     (let ([height-below (- mid y-bottom)])\n\
        \                                          (* l-flonum height-below))]))])\n\
        \        (if (< current-area-below target-area-below)\n            (set! low\
        \ mid)\n            (set! high mid))))\n    high))"
      erlang: "-spec separate_squares(Squares :: [[integer()]]) -> float().\nseparate_squares(Squares)\
        \ ->\n    TotalArea = lists:foldl(fun(Square, Acc) ->\n        L = float(element(3,\
        \ list_to_tuple(Square))),\n        Acc + (L * L)\n    end, 0.0, Squares),\n\
        \n    TargetAreaBelow = TotalArea / 2.0,\n\n    Low = 0.0,\n    High = 2000000000.0\
        \ + 1.0,\n\n    binary_search(Squares, TargetAreaBelow, Low, High, 100).\n\n\
        binary_search(_Squares, _TargetAreaBelow, _Low, High, 0) ->\n    High;\nbinary_search(Squares,\
        \ TargetAreaBelow, Low, High, Iterations) ->\n    Mid = (Low + High) / 2.0,\n\
        \    CurrentAreaBelow = lists:foldl(fun(Square, Acc) ->\n        Y = float(element(2,\
        \ list_to_tuple(Square))),\n        L = float(element(3, list_to_tuple(Square))),\n\
        \        YBottom = Y,\n        YTop = Y + L,\n\n        if\n            YBottom\
        \ >= Mid ->\n                Acc;\n            YTop =< Mid ->\n            \
        \    Acc + (L * L);\n            true ->\n                HeightBelow = Mid\
        \ - YBottom,\n                Acc + (L * HeightBelow)\n        end\n    end,\
        \ 0.0, Squares),\n\n    if\n        CurrentAreaBelow < TargetAreaBelow ->\n\
        \            binary_search(Squares, TargetAreaBelow, Mid, High, Iterations -\
        \ 1);\n        true ->\n            binary_search(Squares, TargetAreaBelow,\
        \ Low, Mid, Iterations - 1)\n    end."
      elixir: "defmodule Solution do\n  @spec separate_squares(squares :: [[integer]])\
        \ :: float\n  def separate_squares(squares) do\n    total_area = Enum.reduce(squares,\
        \ 0.0, fn [_x, _y, l], acc ->\n      l_float = l |> Kernel.to_float()\n    \
        \  acc + l_float * l_float\n    end)\n\n    target_area_below = total_area /\
        \ 2.0\n\n    low = 0.0\n    high = 2_000_000_000.0 + 1.0\n\n    binary_search(squares,\
        \ target_area_below, low, high, 100)\n  end\n\n  defp binary_search(_squares,\
        \ _target_area_below, _low, high, 0), do: high\n  defp binary_search(squares,\
        \ target_area_below, low, high, iterations) do\n    mid = (low + high) / 2.0\n\
        \    current_area_below = Enum.reduce(squares, 0.0, fn [_x, y, l], acc ->\n\
        \      y_float = y |> Kernel.to_float()\n      l_float = l |> Kernel.to_float()\n\
        \      y_bottom = y_float\n      y_top = y_float + l_float\n\n      cond do\n\
        \        y_bottom >= mid ->\n          acc\n        y_top <= mid ->\n      \
        \    acc + l_float * l_float\n        true ->\n          height_below = mid\
        \ - y_bottom\n          acc + l_float * height_below\n      end\n    end)\n\n\
        \    if current_area_below < target_area_below do\n      binary_search(squares,\
        \ target_area_below, mid, high, iterations - 1)\n    else\n      binary_search(squares,\
        \ target_area_below, low, mid, iterations - 1)\n    end\n  end\nend"
    approach: 'The problem asks for a specific y-coordinate ''h'' such that the total
      area of squares below ''h'' equals the total area of squares above ''h''. This
      can be formulated as finding a root for a monotonic function. Let F(h) be the
      difference between the total area of square portions below the line y=h and the
      total area of square portions above the line y=h. For each square [x_i, y_i, l_i],
      its contribution to the area below ''h'' is l_i * max(0, min(h, y_i + l_i) - y_i),
      and its contribution to the area above ''h'' is l_i * max(0, (y_i + l_i) - max(h,
      y_i)). As ''h'' increases, the area below ''h'' increases (or stays constant)
      and the area above ''h'' decreases (or stays constant), making F(h) a monotonically
      increasing function. This property allows us to use binary search on the value
      of ''h''.


      We perform a binary search over the possible range of y-coordinates. The lower
      bound for ''h'' can be 0.0, and a safe upper bound is 2 * 10^9 + 1.0 (since y_i
      and l_i can each be up to 10^9). In each iteration, we calculate mid = low + (high
      - low) / 2.0 and evaluate F(mid). If F(mid) is greater than or equal to zero,
      it means ''mid'' is either the solution or too high, so we update high = mid to
      search in the lower half (this ensures we find the minimum ''h'' if a range of
      solutions exists). If F(mid) is less than zero, ''mid'' is too low, so we update
      low = mid to search in the upper half. We repeat this for a fixed number of iterations
      (e.g., 100) to achieve the required precision of 10^-5.'
    time_complexity: The binary search performs a fixed number of iterations (e.g.,
      100) to achieve the desired precision. In each iteration, the 'check' function
      iterates through all N squares. Therefore, the total time complexity is O(N *
      log(Range / Epsilon)), where N is the number of squares, Range is the search space
      for 'h', and Epsilon is the desired precision. Since log(Range / Epsilon) is a
      constant number of iterations (around 50-100 for the given constraints and precision),
      the time complexity effectively simplifies to O(N).
    space_complexity: The algorithm uses a few variables to store the binary search
      bounds and accumulated areas within the 'check' function. It does not use any
      additional data structures whose size depends on N beyond the input array itself.
      Therefore, the space complexity is O(1).
    elapsed_time: 115.85633039474487
    model: gemini-2.5-flash
    generated_at: '2026-01-13 01:08:25 '
  - solutions:
      cpp: "class Solution {\npublic:\n    double separateSquares(vector<vector<int>>&\
        \ squares) {\n        double minY = INT_MAX, maxY = INT_MIN;\n        double\
        \ totalArea = 0;\n        for (auto& square : squares) {\n            minY =\
        \ min(minY, (double)square[1]);\n            maxY = max(maxY, (double)square[1]\
        \ + square[2]);\n            totalArea += square[2] * square[2];\n        }\n\
        \        double low = minY, high = maxY;\n        while (high - low > 1e-6)\
        \ {\n            double mid = (low + high) / 2;\n            double areaBelow\
        \ = 0;\n            for (auto& square : squares) {\n                double overlap\
        \ = max(0.0, min((double)square[1] + square[2], mid) - max((double)square[1],\
        \ mid));\n                areaBelow += overlap * square[2];\n            }\n\
        \            if (areaBelow * 2 > totalArea) {\n                high = mid;\n\
        \            } else {\n                low = mid;\n            }\n        }\n\
        \        return (low + high) / 2;\n    }\n};"
      java: "class Solution {\n    public double separateSquares(int[][] squares) {\n\
        \        double minY = Integer.MAX_VALUE, maxY = Integer.MIN_VALUE;\n      \
        \  double totalArea = 0;\n        for (int[] square : squares) {\n         \
        \   minY = Math.min(minY, (double)square[1]);\n            maxY = Math.max(maxY,\
        \ (double)square[1] + square[2]);\n            totalArea += square[2] * square[2];\n\
        \        }\n        double low = minY, high = maxY;\n        while (high - low\
        \ > 1e-6) {\n            double mid = (low + high) / 2;\n            double\
        \ areaBelow = 0;\n            for (int[] square : squares) {\n             \
        \   double overlap = Math.max(0.0, Math.min((double)square[1] + square[2], mid)\
        \ - Math.max((double)square[1], mid));\n                areaBelow += overlap\
        \ * square[2];\n            }\n            if (areaBelow * 2 > totalArea) {\n\
        \                high = mid;\n            } else {\n                low = mid;\n\
        \            }\n        }\n        return (low + high) / 2;\n    }\n}"
      python: "class Solution(object):\n    def separateSquares(self, squares):\n  \
        \      minY = float('inf')\n        maxY = float('-inf')\n        totalArea\
        \ = 0\n        for square in squares:\n            minY = min(minY, square[1])\n\
        \            maxY = max(maxY, square[1] + square[2])\n            totalArea\
        \ += square[2] * square[2]\n        low, high = minY, maxY\n        while high\
        \ - low > 1e-6:\n            mid = (low + high) / 2\n            areaBelow =\
        \ 0\n            for square in squares:\n                overlap = max(0.0,\
        \ min(square[1] + square[2], mid) - max(square[1], mid))\n                areaBelow\
        \ += overlap * square[2]\n            if areaBelow * 2 > totalArea:\n      \
        \          high = mid\n            else:\n                low = mid\n      \
        \  return (low + high) / 2"
      python3: "class Solution:\n    def separateSquares(self, squares: list[list[int]])\
        \ -> float:\n        minY = float('inf')\n        maxY = float('-inf')\n   \
        \     totalArea = 0\n        for square in squares:\n            minY = min(minY,\
        \ square[1])\n            maxY = max(maxY, square[1] + square[2])\n        \
        \    totalArea += square[2] * square[2]\n        low, high = minY, maxY\n  \
        \      while high - low > 1e-6:\n            mid = (low + high) / 2\n      \
        \      areaBelow = 0\n            for square in squares:\n                overlap\
        \ = max(0.0, min(square[1] + square[2], mid) - max(square[1], mid))\n      \
        \          areaBelow += overlap * square[2]\n            if areaBelow * 2 >\
        \ totalArea:\n                high = mid\n            else:\n              \
        \  low = mid\n        return (low + high) / 2"
      c: "double separateSquares(int** squares, int squaresSize, int* squaresColSize)\
        \ {\n    double minY = INT_MAX, maxY = INT_MIN;\n    double totalArea = 0;\n\
        \    for (int i = 0; i < squaresSize; i++) {\n        minY = (minY < squares[i][1])\
        \ ? minY : squares[i][1];\n        maxY = (maxY > squares[i][1] + squares[i][2])\
        \ ? maxY : squares[i][1] + squares[i][2];\n        totalArea += squares[i][2]\
        \ * squares[i][2];\n    }\n    double low = minY, high = maxY;\n    while (high\
        \ - low > 1e-6) {\n        double mid = (low + high) / 2;\n        double areaBelow\
        \ = 0;\n        for (int i = 0; i < squaresSize; i++) {\n            double\
        \ overlap = (squares[i][1] + squares[i][2] < mid) ? squares[i][2] : (mid - squares[i][1]);\n\
        \            areaBelow += overlap * squares[i][2];\n        }\n        if (areaBelow\
        \ * 2 > totalArea) {\n            high = mid;\n        } else {\n          \
        \  low = mid;\n        }\n    }\n    return (low + high) / 2;\n}"
      csharp: "public class Solution {\n    public double SeparateSquares(int[][] squares)\
        \ {\n        double minY = int.MaxValue, maxY = int.MinValue;\n        double\
        \ totalArea = 0;\n        for (int i = 0; i < squares.Length; i++) {\n     \
        \       minY = Math.Min(minY, squares[i][1]);\n            maxY = Math.Max(maxY,\
        \ squares[i][1] + squares[i][2]);\n            totalArea += squares[i][2] *\
        \ squares[i][2];\n        }\n        double low = minY, high = maxY;\n     \
        \   while (high - low > 1e-6) {\n            double mid = (low + high) / 2;\n\
        \            double areaBelow = 0;\n            for (int i = 0; i < squares.Length;\
        \ i++) {\n                double overlap = Math.Max(0.0, Math.Min(squares[i][1]\
        \ + squares[i][2], mid) - Math.Max(squares[i][1], mid));\n                areaBelow\
        \ += overlap * squares[i][2];\n            }\n            if (areaBelow * 2\
        \ > totalArea) {\n                high = mid;\n            } else {\n      \
        \          low = mid;\n            }\n        }\n        return (low + high)\
        \ / 2;\n    }\n}"
      javascript: "var separateSquares = function(squares) {\n    let minY = Infinity,\
        \ maxY = -Infinity;\n    let totalArea = 0;\n    for (let square of squares)\
        \ {\n        minY = Math.min(minY, square[1]);\n        maxY = Math.max(maxY,\
        \ square[1] + square[2]);\n        totalArea += square[2] * square[2];\n   \
        \ }\n    let low = minY, high = maxY;\n    while (high - low > 1e-6) {\n   \
        \     let mid = (low + high) / 2;\n        let areaBelow = 0;\n        for (let\
        \ square of squares) {\n            let overlap = Math.max(0.0, Math.min(square[1]\
        \ + square[2], mid) - Math.max(square[1], mid));\n            areaBelow += overlap\
        \ * square[2];\n        }\n        if (areaBelow * 2 > totalArea) {\n      \
        \      high = mid;\n        } else {\n            low = mid;\n        }\n  \
        \  }\n    return (low + high) / 2;\n};"
      typescript: "function separateSquares(squares: number[][]): number {\n    let\
        \ minY: number = Infinity, maxY: number = -Infinity;\n    let totalArea: number\
        \ = 0;\n    for (let square of squares) {\n        minY = Math.min(minY, square[1]);\n\
        \        maxY = Math.max(maxY, square[1] + square[2]);\n        totalArea +=\
        \ square[2] * square[2];\n    }\n    let low: number = minY, high: number =\
        \ maxY;\n    while (high - low > 1e-6) {\n        let mid: number = (low + high)\
        \ / 2;\n        let areaBelow: number = 0;\n        for (let square of squares)\
        \ {\n            let overlap: number = Math.max(0.0, Math.min(square[1] + square[2],\
        \ mid) - Math.max(square[1], mid));\n            areaBelow += overlap * square[2];\n\
        \        }\n        if (areaBelow * 2 > totalArea) {\n            high = mid;\n\
        \        } else {\n            low = mid;\n        }\n    }\n    return (low\
        \ + high) / 2;\n}"
      php: "class Solution {\n    function separateSquares($squares) {\n        $minY\
        \ = PHP_INT_MAX;\n        $maxY = PHP_INT_MIN;\n        $totalArea = 0;\n  \
        \      foreach ($squares as $square) {\n            $minY = min($minY, $square[1]);\n\
        \            $maxY = max($maxY, $square[1] + $square[2]);\n            $totalArea\
        \ += $square[2] * $square[2];\n        }\n        $low = $minY;\n        $high\
        \ = $maxY;\n        while ($high - $low > 1e-6) {\n            $mid = ($low\
        \ + $high) / 2;\n            $areaBelow = 0;\n            foreach ($squares\
        \ as $square) {\n                $overlap = max(0.0, min($square[1] + $square[2],\
        \ $mid) - max($square[1], $mid));\n                $areaBelow += $overlap *\
        \ $square[2];\n            }\n            if ($areaBelow * 2 > $totalArea) {\n\
        \                $high = $mid;\n            } else {\n                $low =\
        \ $mid;\n            }\n        }\n        return ($low + $high) / 2;\n    }\n\
        }"
      swift: "class Solution {\n    func separateSquares(_ squares: [[Int]]) -> Double\
        \ {\n        var minY: Double = Double.greatestFiniteMagnitude\n        var\
        \ maxY: Double = Double.leastNormalMagnitude\n        var totalArea: Double\
        \ = 0\n        for square in squares {\n            minY = min(minY, Double(square[1]))\n\
        \            maxY = max(maxY, Double(square[1]) + Double(square[2]))\n     \
        \       totalArea += Double(square[2]) * Double(square[2])\n        }\n    \
        \    var low: Double = minY\n        var high: Double = maxY\n        while\
        \ high - low > 1e-6 {\n            let mid: Double = (low + high) / 2\n    \
        \        var areaBelow: Double = 0\n            for square in squares {\n  \
        \              let overlap: Double = max(0.0, min(Double(square[1]) + Double(square[2]),\
        \ mid) - max(Double(square[1]), mid))\n                areaBelow += overlap\
        \ * Double(square[2])\n            }\n            if areaBelow * 2 > totalArea\
        \ {\n                high = mid\n            } else {\n                low =\
        \ mid\n            }\n        }\n        return (low + high) / 2\n    }\n}"
      kotlin: "class Solution {\n    fun separateSquares(squares: Array<IntArray>):\
        \ Double {\n        var minY = Int.MAX_VALUE\n        var maxY = Int.MIN_VALUE\n\
        \        var totalArea = 0.0\n        for (square in squares) {\n          \
        \  val (x, y, l) = square\n            minY = minOf(minY, y)\n            maxY\
        \ = maxOf(maxY, y + l)\n            totalArea += l * l\n        }\n        var\
        \ low = minY.toDouble()\n        var high = maxY.toDouble()\n        while (high\
        \ - low > 1e-6) {\n            val mid = (low + high) / 2\n            var areaBelow\
        \ = 0.0\n            for (square in squares) {\n                val (x, y, l)\
        \ = square\n                val overlap = maxOf(0.0, minOf(mid, y + l) - maxOf(mid,\
        \ y))\n                areaBelow += overlap * l\n            }\n           \
        \ if (areaBelow < totalArea / 2) {\n                low = mid\n            }\
        \ else {\n                high = mid\n            }\n        }\n        return\
        \ low\n    }\n}"
      dart: "class Solution {\n  double separateSquares(List<List<int>> squares) {\n\
        \    double minY = double.maxFinite;\n    double maxY = double.negativeInfinity;\n\
        \    double totalArea = 0;\n    for (var square in squares) {\n      var x =\
        \ square[0];\n      var y = square[1];\n      var l = square[2];\n      minY\
        \ = minY < y ? minY : y;\n      maxY = maxY > y + l ? maxY : y + l;\n      totalArea\
        \ += l * l;\n    }\n    double low = minY;\n    double high = maxY;\n    while\
        \ (high - low > 1e-6) {\n      double mid = (low + high) / 2;\n      double\
        \ areaBelow = 0;\n      for (var square in squares) {\n        var x = square[0];\n\
        \        var y = square[1];\n        var l = square[2];\n        double overlap\
        \ = max(0, min(mid, y + l) - max(mid, y));\n        areaBelow += overlap * l;\n\
        \      }\n      if (areaBelow < totalArea / 2) {\n        low = mid;\n     \
        \ } else {\n        high = mid;\n      }\n    }\n    return low;\n  }\n}"
      go: "func separateSquares(squares [][]int) float64 {\n    minY := int(^uint(0)>>1)\n\
        \    maxY := int(^uint(0))\n    totalArea := 0.0\n    for _, square := range\
        \ squares {\n        x, y, l := square[0], square[1], square[2]\n        if\
        \ y < minY {\n            minY = y\n        }\n        if y+l > maxY {\n   \
        \         maxY = y + l\n        }\n        totalArea += float64(l * l)\n   \
        \ }\n    low := float64(minY)\n    high := float64(maxY)\n    for high-low >\
        \ 1e-6 {\n        mid := (low + high) / 2\n        areaBelow := 0.0\n      \
        \  for _, square := range squares {\n            x, y, l := square[0], square[1],\
        \ square[2]\n            overlap := max(0, min(mid, float64(y+l)) - max(mid,\
        \ float64(y)))\n            areaBelow += overlap * float64(l)\n        }\n \
        \       if areaBelow < totalArea/2 {\n            low = mid\n        } else\
        \ {\n            high = mid\n        }\n    }\n    return low\n}"
      ruby: "def separate_squares(squares)\n    min_y = Float::INFINITY\n    max_y =\
        \ -Float::INFINITY\n    total_area = 0\n    squares.each do |square|\n     \
        \   x, y, l = square\n        min_y = [min_y, y].min\n        max_y = [max_y,\
        \ y + l].max\n        total_area += l * l\n    end\n    low = min_y.to_f\n \
        \   high = max_y.to_f\n    while high - low > 1e-6\n        mid = (low + high)\
        \ / 2\n        area_below = 0\n        squares.each do |square|\n          \
        \  x, y, l = square\n            overlap = [0, [mid, y + l].min - [mid, y].max].max\n\
        \            area_below += overlap * l\n        end\n        if area_below <\
        \ total_area / 2\n            low = mid\n        else\n            high = mid\n\
        \        end\n    end\n    low\nend"
      scala: "object Solution {\n    def separateSquares(squares: Array[Array[Int]]):\
        \ Double = {\n        var minY = Int.MaxValue\n        var maxY = Int.MinValue\n\
        \        var totalArea = 0.0\n        for (square <- squares) {\n          \
        \  val Array(x, y, l) = square\n            minY = Math.min(minY, y)\n     \
        \       maxY = Math.max(maxY, y + l)\n            totalArea += l * l\n     \
        \   }\n        var low = minY.toDouble\n        var high = maxY.toDouble\n \
        \       while (high - low > 1e-6) {\n            val mid = (low + high) / 2\n\
        \            var areaBelow = 0.0\n            for (square <- squares) {\n  \
        \              val Array(x, y, l) = square\n                val overlap = Math.max(0,\
        \ Math.min(mid, y + l) - Math.max(mid, y))\n                areaBelow += overlap\
        \ * l\n            }\n            if (areaBelow < totalArea / 2) {\n       \
        \         low = mid\n            } else {\n                high = mid\n    \
        \        }\n        }\n        low\n    }\n}"
      rust: "impl Solution {\n    pub fn separate_squares(squares: Vec<Vec<i32>>) ->\
        \ f64 {\n        let mut min_y = i32::MAX;\n        let mut max_y = i32::MIN;\n\
        \        let mut total_area = 0.0;\n        for square in &squares {\n     \
        \       let x = square[0];\n            let y = square[1];\n            let\
        \ l = square[2];\n            min_y = min_y.min(y);\n            max_y = max_y.max(y\
        \ + l);\n            total_area += (l as f64) * (l as f64);\n        }\n   \
        \     let mut low = min_y as f64;\n        let mut high = max_y as f64;\n  \
        \      while high - low > 1e-6 {\n            let mid = (low + high) / 2.0;\n\
        \            let mut area_below = 0.0;\n            for square in &squares {\n\
        \                let x = square[0];\n                let y = square[1];\n  \
        \              let l = square[2];\n                let overlap = (mid.min((y\
        \ + l) as f64) - mid.max(y as f64)).max(0.0);\n                area_below +=\
        \ overlap * (l as f64);\n            }\n            if area_below < total_area\
        \ / 2.0 {\n                low = mid;\n            } else {\n              \
        \  high = mid;\n            }\n        }\n        low\n    }\n}"
      racket: "(define/contract (separate-squares squares)\n  (-> (listof (listof exact-integer?))\
        \ flonum?)\n  (let* ([min-y (apply min (map (lambda (s) (second s)) squares))]\n\
        \         [max-y (apply max (map (lambda (s) (+ (second s) (third s))) squares))]\n\
        \         [total-area (apply + (map (lambda (s) (expt (third s) 2)) squares))])\n\
        \    (let loop ([low min-y] [high max-y])\n      (if (> (- high low) 1e-6)\n\
        \          (let* ([mid (/ (+ low high) 2)]\n                 [area-below (apply\
        \ + (map (lambda (s)\n                                             (let ([x\
        \ (first s)] [y (second s)] [l (third s)])\n                               \
        \                (let ([overlap (max 0 (- (min mid (+ y l)) (max mid y)))])\n\
        \                                                 (* overlap l)))) squares))])\n\
        \            (if (< area-below (/ total-area 2))\n                (loop mid\
        \ high)\n                (loop low mid)))\n          low))))"
      erlang: "separate_squares(Squares) ->\n    MinY = lists:min([Y || [_, Y, _] <-\
        \ Squares]),\n    MaxY = lists:max([Y + L || [_, Y, L] <- Squares]),\n    TotalArea\
        \ = lists:sum([L * L || [_, _, L] <- Squares]),\n    separate_squares(Squares,\
        \ MinY, MaxY, TotalArea, MinY).\n\nseparate_squares(Squares, Low, High, TotalArea,\
        \ Acc) ->\n    case High - Low > 1.0e-6 of\n        true ->\n            Mid\
        \ = (Low + High) / 2,\n            AreaBelow = lists:sum([overlap(Mid, Y, L)\
        \ * L || [_, Y, L] <- Squares]),\n            case AreaBelow < TotalArea / 2\
        \ of\n                true -> separate_squares(Squares, Mid, High, TotalArea,\
        \ Mid);\n                false -> separate_squares(Squares, Low, Mid, TotalArea,\
        \ Mid)\n            end;\n        false -> Acc\n    end.\n\noverlap(Mid, Y,\
        \ L) -> max(0, min(Mid, Y + L) - max(Mid, Y))."
      elixir: "defmodule Solution do\n  @spec separate_squares(squares :: [[integer]])\
        \ :: float\n  def separate_squares(squares) do\n    min_y = Enum.min_by(squares,\
        \ fn [_, y, _] -> y end)\n    max_y = Enum.max_by(squares, fn [_, y, l] -> y\
        \ + l end)\n    total_area = Enum.sum(Enum.map(squares, fn [_, _, l] -> l *\
        \ l end))\n    separate_squares(squares, min_y, max_y, total_area, min_y)\n\
        \  end\n\n  defp separate_squares(squares, low, high, total_area, acc) do\n\
        \    cond do\n      high - low > 1.0e-6 ->\n        mid = (low + high) / 2\n\
        \        area_below = Enum.sum(Enum.map(squares, fn [_, y, l] -> overlap(mid,\
        \ y, l) * l end))\n        cond do\n          area_below < total_area / 2 ->\
        \ separate_squares(squares, mid, high, total_area, mid)\n          true -> separate_squares(squares,\
        \ low, mid, total_area, mid)\n        end\n      true -> acc\n    end\n  end\n\
        \n  defp overlap(mid, y, l) do\n    max(0, min(mid, y + l) - max(mid, y))\n\
        \  end\nend"
    approach: 'The problem can be solved by using binary search to find the minimum
      y-coordinate value of a horizontal line such that the total area of the squares
      above the line equals the total area of the squares below the line. We start by
      calculating the total area of all squares and then perform a binary search on
      the possible y-coordinates. For each y-coordinate, we calculate the area of the
      squares above and below the line and check if they are equal. If they are equal,
      we update our answer and continue the binary search to find the minimum y-coordinate.
      The key intuition here is to use the concept of binary search to efficiently find
      the minimum y-coordinate value that satisfies the condition.


      The algorithm works by first calculating the minimum and maximum y-coordinates
      of the squares. We then perform a binary search on the range of possible y-coordinates.
      For each y-coordinate, we calculate the area of the squares above and below the
      line by iterating over all squares and calculating the area of the part of each
      square that is above or below the line. We use the formula for the area of a rectangle
      to calculate the area of each part. If the areas above and below the line are
      equal, we update our answer and continue the binary search to find the minimum
      y-coordinate. We repeat this process until we find the minimum y-coordinate value
      that satisfies the condition or until the binary search range is empty.


      '
    time_complexity: 'O(n log h) where n is the number of squares and h is the height
      of the bounding box of all squares. This is because we perform a binary search
      on the possible y-coordinates and for each y-coordinate, we iterate over all squares
      to calculate the area above and below the line. The binary search reduces the
      number of iterations from O(h) to O(log h), resulting in a significant improvement
      in performance for large inputs.


      '
    space_complexity: 'O(1) because we only use a constant amount of space to store
      the minimum and maximum y-coordinates, the total area of all squares, and the
      current y-coordinate being considered in the binary search. We do not use any
      data structures that grow with the size of the input, so the space complexity
      is constant.


      '
    elapsed_time: 11.850000381469727
    model: llama-3.3-70b-versatile
    generated_at: '2026-01-13 01:08:42 '
---

## Problem #3453: Separate Squares I

**Difficulty:** Medium

**Topics:** Array, Binary Search

## Problem Description

<p>You are given a 2D integer array <code>squares</code>. Each <code>squares[i] = [x<sub>i</sub>, y<sub>i</sub>, l<sub>i</sub>]</code> represents the coordinates of the bottom-left point and the side length of a square parallel to the x-axis.</p>

<p>Find the <strong>minimum</strong> y-coordinate value of a horizontal line such that the total area of the squares above the line <em>equals</em> the total area of the squares below the line.</p>

<p>Answers within <code>10<sup>-5</sup></code> of the actual answer will be accepted.</p>

<p><strong>Note</strong>: Squares <strong>may</strong> overlap. Overlapping areas should be counted <strong>multiple times</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">squares = [[0,0,1],[2,2,1]]</span></p>

<p><strong>Output:</strong> <span class="example-io">1.00000</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2025/01/06/4062example1drawio.png" style="width: 378px; height: 352px;" /></p>

<p>Any horizontal line between <code>y = 1</code> and <code>y = 2</code> will have 1 square unit above it and 1 square unit below it. The lowest option is 1.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">squares = [[0,0,2],[1,1,1]]</span></p>

<p><strong>Output:</strong> <span class="example-io">1.16667</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2025/01/15/4062example2drawio.png" style="width: 378px; height: 352px;" /></p>

<p>The areas are:</p>

<ul>
	<li>Below the line: <code>7/6 * 2 (Red) + 1/6 (Blue) = 15/6 = 2.5</code>.</li>
	<li>Above the line: <code>5/6 * 2 (Red) + 5/6 (Blue) = 15/6 = 2.5</code>.</li>
</ul>

<p>Since the areas above and below the line are equal, the output is <code>7/6 = 1.16667</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= squares.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>squares[i] = [x<sub>i</sub>, y<sub>i</sub>, l<sub>i</sub>]</code></li>
	<li><code>squares[i].length == 3</code></li>
	<li><code>0 &lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= l<sub>i</sub> &lt;= 10<sup>9</sup></code></li>
	<li>The total area of all the squares will not exceed <code>10<sup>12</sup></code>.</li>
</ul>


## Hints

1. Binary search on the answer.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2026-01-13 01:08:25 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks for a specific y-coordinate 'h' such that the total area of squares below 'h' equals the total area of squares above 'h'. This can be formulated as finding a root for a monotonic function. Let F(h) be the difference between the total area of square portions below the line y=h and the total area of square portions above the line y=h. For each square [x_i, y_i, l_i], its contribution to the area below 'h' is l_i * max(0, min(h, y_i + l_i) - y_i), and its contribution to the area above 'h' is l_i * max(0, (y_i + l_i) - max(h, y_i)). As 'h' increases, the area below 'h' increases (or stays constant) and the area above 'h' decreases (or stays constant), making F(h) a monotonically increasing function. This property allows us to use binary search on the value of 'h'.

We perform a binary search over the possible range of y-coordinates. The lower bound for 'h' can be 0.0, and a safe upper bound is 2 * 10^9 + 1.0 (since y_i and l_i can each be up to 10^9). In each iteration, we calculate mid = low + (high - low) / 2.0 and evaluate F(mid). If F(mid) is greater than or equal to zero, it means 'mid' is either the solution or too high, so we update high = mid to search in the lower half (this ensures we find the minimum 'h' if a range of solutions exists). If F(mid) is less than zero, 'mid' is too low, so we update low = mid to search in the upper half. We repeat this for a fixed number of iterations (e.g., 100) to achieve the required precision of 10^-5.

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
    double separateSquares(std::vector<std::vector<int>>& squares) {
        auto check = [&](double h) {
            double total_area_below = 0.0;
            double total_area_above = 0.0;

            for (const auto& square : squares) {
                long long y_ll = square[1];
                long long l_ll = square[2];

                double bottom = static_cast<double>(y_ll);
                double top = static_cast<double>(y_ll + l_ll);
                double width = static_cast<double>(l_ll);

                if (h <= bottom) {
                    total_area_above += width * width;
                } else if (h >= top) {
                    total_area_below += width * width;
                } else {
                    double height_below = h - bottom;
                    double height_above = top - h;
                    total_area_below += width * height_below;
                    total_area_above += width * height_above;
                }
            }
            return total_area_below - total_area_above;
        };

        double low = 0.0;
        double high = 2e9 + 1.0; 

        for (int i = 0; i < 100; ++i) {
            double mid = low + (high - low) / 2.0;
            double diff = check(mid);

            if (diff >= 0) {
                high = mid;
            } else {
                low = mid;
            }
        }

        return high;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public double separateSquares(int[][] squares) {
        double low = 0.0;
        double high = 2e9 + 1.0; 

        for (int i = 0; i < 100; ++i) {
            double mid = low + (high - low) / 2.0;
            double diff = check(mid, squares);

            if (diff >= 0) {
                high = mid;
            } else {
                low = mid;
            }
        }

        return high;
    }

    private double check(double h, int[][] squares) {
        double total_area_below = 0.0;
        double total_area_above = 0.0;

        for (int[] square : squares) {
            int y_int = square[1];
            int l_int = square[2];

            double bottom = (double)y_int;
            double top = (double)(y_int + l_int);
            double width = (double)l_int;

            if (h <= bottom) {
                total_area_above += width * width;
            } else if (h >= top) {
                total_area_below += width * width;
            } else {
                double height_below = h - bottom;
                double height_above = top - h;
                total_area_below += width * height_below;
                total_area_above += width * height_above;
            }
        }
        return total_area_below - total_area_above;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def separateSquares(self, squares):
        """
        :type squares: List[List[int]]
        :rtype: float
        """

        def check(h):
            total_area_below = 0.0
            total_area_above = 0.0

            for square in squares:
                x, y, l = square
                bottom = float(y)
                top = float(y + l)
                width = float(l)

                if h <= bottom:
                    total_area_above += width * width
                elif h >= top:
                    total_area_below += width * width
                else:
                    height_below = h - bottom
                    height_above = top - h
                    total_area_below += width * height_below
                    total_area_above += width * height_above

            return total_area_below - total_area_above

        low = 0.0
        high = 2 * 10**9 + 1.0 

        for _ in range(100): 
            mid = low + (high - low) / 2.0
            diff = check(mid)

            if diff >= 0:
                high = mid
            else:
                low = mid

        return high
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:

        def check(h: float) -> float:
            total_area_below = 0.0
            total_area_above = 0.0

            for x, y, l in squares:
                bottom = float(y)
                top = float(y + l)
                width = float(l)

                if h <= bottom:
                    total_area_above += width * width
                elif h >= top:
                    total_area_below += width * width
                else:
                    height_below = h - bottom
                    height_above = top - h
                    total_area_below += width * height_below
                    total_area_above += width * height_above

            return total_area_below - total_area_above

        low = 0.0
        high = 2 * 10**9 + 1.0 

        for _ in range(100): 
            mid = low + (high - low) / 2.0
            diff = check(mid)

            if diff >= 0:
                high = mid
            else:
                low = mid

        return high
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
double check_c(double h, int** squares, int squaresSize) {
    double total_area_below = 0.0;
    double total_area_above = 0.0;

    for (int i = 0; i < squaresSize; ++i) {
        int y_int = squares[i][1];
        int l_int = squares[i][2];

        double bottom = (double)y_int;
        double top = (double)(y_int + l_int);
        double width = (double)l_int;

        if (h <= bottom) {
            total_area_above += width * width;
        } else if (h >= top) {
            total_area_below += width * width;
        } else {
            double height_below = h - bottom;
            double height_above = top - h;
            total_area_below += width * height_below;
            total_area_above += width * height_above;
        }
    }
    return total_area_below - total_area_above;
}

double separateSquares(int** squares, int squaresSize, int* squaresColSize) {
    double low = 0.0;
    double high = 2e9 + 1.0; 

    for (int i = 0; i < 100; ++i) {
        double mid = low + (high - low) / 2.0;
        double diff = check_c(mid, squares, squaresSize);

        if (diff >= 0) {
            high = mid;
        } else {
            low = mid;
        }
    }

    return high;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public double SeparateSquares(int[][] squares) {

        double low = 0.0;
        double high = 2e9 + 1.0; 

        for (int i = 0; i < 100; ++i) {
            double mid = low + (high - low) / 2.0;
            double diff = Check(mid, squares);

            if (diff >= 0) {
                high = mid;
            } else {
                low = mid;
            }
        }

        return high;
    }

    private double Check(double h, int[][] squares) {
        double total_area_below = 0.0;
        double total_area_above = 0.0;

        foreach (int[] square in squares) {
            int y_int = square[1];
            int l_int = square[2];

            double bottom = (double)y_int;
            double top = (double)(y_int + l_int);
            double width = (double)l_int;

            if (h <= bottom) {
                total_area_above += width * width;
            } else if (h >= top) {
                total_area_below += width * width;
            } else {
                double height_below = h - bottom;
                double height_above = top - h;
                total_area_below += width * height_below;
                total_area_above += width * height_above;
            }
        }
        return total_area_below - total_area_above;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[][]} squares
 * @return {number}
 */
var separateSquares = function(squares) {

    const check = (h) => {
        let total_area_below = 0.0;
        let total_area_above = 0.0;

        for (const square of squares) {
            const y_int = square[1];
            const l_int = square[2];

            const bottom = y_int; 
            const top = y_int + l_int;
            const width = l_int;

            if (h <= bottom) {
                total_area_above += width * width;
            } else if (h >= top) {
                total_area_below += width * width;
            } else {
                const height_below = h - bottom;
                const height_above = top - h;
                total_area_below += width * height_below;
                total_area_above += width * height_above;
            }
        }
        return total_area_below - total_area_above;
    };

    let low = 0.0;
    let high = 2e9 + 1.0; 

    for (let i = 0; i < 100; ++i) {
        const mid = low + (high - low) / 2.0;
        const diff = check(mid);

        if (diff >= 0) {
            high = mid;
        } else {
            low = mid;
        }
    }

    return high;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function separateSquares(squares: number[][]): number {

    const check = (h: number): number => {
        let total_area_below: number = 0.0;
        let total_area_above: number = 0.0;

        for (const square of squares) {
            const y_int: number = square[1];
            const l_int: number = square[2];

            const bottom: number = y_int;
            const top: number = y_int + l_int;
            const width: number = l_int;

            if (h <= bottom) {
                total_area_above += width * width;
            } else if (h >= top) {
                total_area_below += width * width;
            } else {
                const height_below: number = h - bottom;
                const height_above: number = top - h;
                total_area_below += width * height_below;
                total_area_above += width * height_above;
            }
        }
        return total_area_below - total_area_above;
    };

    let low: number = 0.0;
    let high: number = 2e9 + 1.0; 

    for (let i = 0; i < 100; ++i) {
        const mid: number = low + (high - low) / 2.0;
        const diff: number = check(mid);

        if (diff >= 0) {
            high = mid;
        } else {
            low = mid;
        }
    }

    return high;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {

    /**
     * @param Integer[][] $squares
     * @return Float
     */
    function separateSquares($squares) {

        $check = function($h) use ($squares) {
            $total_area_below = 0.0;
            $total_area_above = 0.0;

            foreach ($squares as $square) {
                $y_int = $square[1];
                $l_int = $square[2];

                $bottom = (float)$y_int;
                $top = (float)($y_int + $l_int);
                $width = (float)$l_int;

                if ($h <= $bottom) {
                    $total_area_above += $width * $width;
                } elseif ($h >= $top) {
                    $total_area_below += $width * $width;
                } else {
                    $height_below = $h - $bottom;
                    $height_above = $top - $h;
                    $total_area_below += $width * $height_below;
                    $total_area_above += $width * $height_above;
                }
            }
            return $total_area_below - $total_area_above;
        };

        $low = 0.0;
        $high = 2e9 + 1.0; 

        for ($i = 0; $i < 100; ++$i) {
            $mid = $low + ($high - $low) / 2.0;
            $diff = $check($mid);

            if ($diff >= 0) {
                $high = $mid;
            } else {
                $low = $mid;
            }
        }

        return $high;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func separateSquares(_ squares: [[Int]]) -> Double {

        let check = { (h: Double) -> Double in
            var total_area_below: Double = 0.0
            var total_area_above: Double = 0.0

            for square in squares {
                let y_int = square[1]
                let l_int = square[2]

                let bottom = Double(y_int)
                let top = Double(y_int + l_int)
                let width = Double(l_int)

                if h <= bottom {
                    total_area_above += width * width
                } else if h >= top {
                    total_area_below += width * width
                } else {
                    let height_below = h - bottom
                    let height_above = top - h
                    total_area_below += width * height_below
                    total_area_above += width * height_above
                }
            }
            return total_area_below - total_area_above
        }

        var low: Double = 0.0
        var high: Double = 2e9 + 1.0 

        for _ in 0..<100 {
            let mid = low + (high - low) / 2.0
            let diff = check(mid)

            if diff >= 0 {
                high = mid
            } else {
                low = mid
            }
        }

        return high
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun separateSquares(squares: Array<IntArray>): Double {
        var totalArea = 0.0
        for (square in squares) {
            val l = square[2].toDouble()
            totalArea += l * l
        }

        val targetAreaBelow = totalArea / 2.0

        var low = 0.0
        var high = 2_000_000_000.0 + 1.0

        for (i in 0 until 100) {
            val mid = (low + high) / 2.0
            var currentAreaBelow = 0.0

            for (square in squares) {
                val y = square[1].toDouble()
                val l = square[2].toDouble()
                val yBottom = y
                val yTop = y + l

                if (yBottom >= mid) {
                    continue
                } else if (yTop <= mid) {
                    currentAreaBelow += l * l
                } else {
                    val heightBelow = mid - yBottom
                    currentAreaBelow += l * heightBelow
                }
            }

            if (currentAreaBelow < targetAreaBelow) {
                low = mid
            } else {
                high = mid
            }
        }
        return high
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
import 'dart:math';

class Solution {
  double separateSquares(List<List<int>> squares) {
    double totalArea = 0.0;
    for (var square in squares) {
      double l = square[2].toDouble();
      totalArea += l * l;
    }

    double targetAreaBelow = totalArea / 2.0;

    double low = 0.0;
    double high = 2000000000.0 + 1.0;

    for (int i = 0; i < 100; i++) {
      double mid = (low + high) / 2.0;
      double currentAreaBelow = 0.0;

      for (var square in squares) {
        double y = square[1].toDouble();
        double l = square[2].toDouble();
        double yBottom = y;
        double yTop = y + l;

        if (yBottom >= mid) {
          continue;
        } else if (yTop <= mid) {
          currentAreaBelow += l * l;
        } else {
          double heightBelow = mid - yBottom;
          currentAreaBelow += l * heightBelow;
        }
      }

      if (currentAreaBelow < targetAreaBelow) {
        low = mid;
      } else {
        high = mid;
      }
    }
    return high;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func separateSquares(squares [][]int) float64 {
    totalArea := 0.0
    for _, square := range squares {
        l := float64(square[2])
        totalArea += l * l
    }

    targetAreaBelow := totalArea / 2.0

    low := 0.0
    high := 2000000000.0 + 1.0

    for i := 0; i < 100; i++ {
        mid := (low + high) / 2.0
        currentAreaBelow := 0.0

        for _, square := range squares {
            y := float64(square[1])
            l := float64(square[2])
            yBottom := y
            yTop := y + l

            if yBottom >= mid {
                continue
            } else if yTop <= mid {
                currentAreaBelow += l * l
            } else {
                heightBelow := mid - yBottom
                currentAreaBelow += l * heightBelow
            }
        }

        if currentAreaBelow < targetAreaBelow {
            low = mid
        } else {
            high = mid
        }
    }
    return high
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# @param {Integer[][]} squares
# @return {Float}
def separate_squares(squares)
    total_area = 0.0
    squares.each do |square|
        l = square[2].to_f
        total_area += l * l
    end

    target_area_below = total_area / 2.0

    low = 0.0
    high = 2_000_000_000.0 + 1.0

    100.times do
        mid = (low + high) / 2.0
        current_area_below = 0.0

        squares.each do |square|
            y = square[1].to_f
            l = square[2].to_f
            y_bottom = y
            y_top = y + l

            if y_bottom >= mid
                next
            elsif y_top <= mid
                current_area_below += l * l
            else
                height_below = mid - y_bottom
                current_area_below += l * height_below
            end
        end

        if current_area_below < target_area_below
            low = mid
        else
            high = mid
        end
    end
    high
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def separateSquares(squares: Array[Array[Int]]): Double = {
        var totalArea = 0.0
        for (square <- squares) {
            val l = square(2).toDouble
            totalArea += l * l
        }

        val targetAreaBelow = totalArea / 2.0

        var low = 0.0
        var high = 2_000_000_000.0 + 1.0

        for (_ <- 0 until 100) {
            val mid = (low + high) / 2.0
            var currentAreaBelow = 0.0

            for (square <- squares) {
                val y = square(1).toDouble
                val l = square(2).toDouble
                val yBottom = y
                val yTop = y + l

                if (yBottom >= mid) {

                } else if (yTop <= mid) {
                    currentAreaBelow += l * l
                } else {
                    val heightBelow = mid - yBottom
                    currentAreaBelow += l * heightBelow
                }
            }

            if (currentAreaBelow < targetAreaBelow) {
                low = mid
            } else {
                high = mid
            }
        }
        high
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn separate_squares(squares: Vec<Vec<i32>>) -> f64 {
        let mut total_area = 0.0;
        for square in &squares {
            let l = square[2] as f64;
            total_area += l * l;
        }

        let target_area_below = total_area / 2.0;

        let mut low = 0.0;
        let mut high = 2_000_000_000.0 + 1.0;

        for _ in 0..100 {
            let mid = (low + high) / 2.0;
            let mut current_area_below = 0.0;

            for square in &squares {
                let y = square[1] as f64;
                let l = square[2] as f64;
                let y_bottom = y;
                let y_top = y + l;

                if y_bottom >= mid {
                    continue;
                } else if y_top <= mid {
                    current_area_below += l * l;
                } else {
                    let height_below = mid - y_bottom;
                    current_area_below += l * height_below;
                }
            }

            if current_area_below < target_area_below {
                low = mid;
            } else {
                high = mid;
            }
        }
        high
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (separate-squares squares)
  (-> (listof (listof exact-integer?)) flonum?)
  (let* ([total-area (for/sum ([square squares])
                       (let ([l (list-ref square 2)])
                         (* (exact->flonum l) (exact->flonum l))))]
         [target-area-below (/ total-area 2.0)]
         [low 0.0]
         [high (+ 2000000000.0 1.0)])

    (for ([_ (in-range 100)])
      (let* ([mid (/ (+ low high) 2.0)]
             [current-area-below (for/sum ([square squares])
                                   (let* ([y (list-ref square 1)]
                                          [l (list-ref square 2)]
                                          [y-flonum (exact->flonum y)]
                                          [l-flonum (exact->flonum l)]
                                          [y-bottom y-flonum]
                                          [y-top (+ y-flonum l-flonum)])
                                     (cond
                                       [(>= y-bottom mid) 0.0]
                                       [(<= y-top mid) (* l-flonum l-flonum)]
                                       [else
                                        (let ([height-below (- mid y-bottom)])
                                          (* l-flonum height-below))]))])
        (if (< current-area-below target-area-below)
            (set! low mid)
            (set! high mid))))
    high))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec separate_squares(Squares :: [[integer()]]) -> float().
separate_squares(Squares) ->
    TotalArea = lists:foldl(fun(Square, Acc) ->
        L = float(element(3, list_to_tuple(Square))),
        Acc + (L * L)
    end, 0.0, Squares),

    TargetAreaBelow = TotalArea / 2.0,

    Low = 0.0,
    High = 2000000000.0 + 1.0,

    binary_search(Squares, TargetAreaBelow, Low, High, 100).

binary_search(_Squares, _TargetAreaBelow, _Low, High, 0) ->
    High;
binary_search(Squares, TargetAreaBelow, Low, High, Iterations) ->
    Mid = (Low + High) / 2.0,
    CurrentAreaBelow = lists:foldl(fun(Square, Acc) ->
        Y = float(element(2, list_to_tuple(Square))),
        L = float(element(3, list_to_tuple(Square))),
        YBottom = Y,
        YTop = Y + L,

        if
            YBottom >= Mid ->
                Acc;
            YTop =< Mid ->
                Acc + (L * L);
            true ->
                HeightBelow = Mid - YBottom,
                Acc + (L * HeightBelow)
        end
    end, 0.0, Squares),

    if
        CurrentAreaBelow < TargetAreaBelow ->
            binary_search(Squares, TargetAreaBelow, Mid, High, Iterations - 1);
        true ->
            binary_search(Squares, TargetAreaBelow, Low, Mid, Iterations - 1)
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec separate_squares(squares :: [[integer]]) :: float
  def separate_squares(squares) do
    total_area = Enum.reduce(squares, 0.0, fn [_x, _y, l], acc ->
      l_float = l |> Kernel.to_float()
      acc + l_float * l_float
    end)

    target_area_below = total_area / 2.0

    low = 0.0
    high = 2_000_000_000.0 + 1.0

    binary_search(squares, target_area_below, low, high, 100)
  end

  defp binary_search(_squares, _target_area_below, _low, high, 0), do: high
  defp binary_search(squares, target_area_below, low, high, iterations) do
    mid = (low + high) / 2.0
    current_area_below = Enum.reduce(squares, 0.0, fn [_x, y, l], acc ->
      y_float = y |> Kernel.to_float()
      l_float = l |> Kernel.to_float()
      y_bottom = y_float
      y_top = y_float + l_float

      cond do
        y_bottom >= mid ->
          acc
        y_top <= mid ->
          acc + l_float * l_float
        true ->
          height_below = mid - y_bottom
          acc + l_float * height_below
      end
    end)

    if current_area_below < target_area_below do
      binary_search(squares, target_area_below, mid, high, iterations - 1)
    else
      binary_search(squares, target_area_below, low, mid, iterations - 1)
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The binary search performs a fixed number of iterations (e.g., 100) to achieve the desired precision. In each iteration, the 'check' function iterates through all N squares. Therefore, the total time complexity is O(N * log(Range / Epsilon)), where N is the number of squares, Range is the search space for 'h', and Epsilon is the desired precision. Since log(Range / Epsilon) is a constant number of iterations (around 50-100 for the given constraints and precision), the time complexity effectively simplifies to O(N).

- **Space Complexity:** The algorithm uses a few variables to store the binary search bounds and accumulated areas within the 'check' function. It does not use any additional data structures whose size depends on N beyond the input array itself. Therefore, the space complexity is O(1).

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2026-01-13 01:08:42 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved by using binary search to find the minimum y-coordinate value of a horizontal line such that the total area of the squares above the line equals the total area of the squares below the line. We start by calculating the total area of all squares and then perform a binary search on the possible y-coordinates. For each y-coordinate, we calculate the area of the squares above and below the line and check if they are equal. If they are equal, we update our answer and continue the binary search to find the minimum y-coordinate. The key intuition here is to use the concept of binary search to efficiently find the minimum y-coordinate value that satisfies the condition.

The algorithm works by first calculating the minimum and maximum y-coordinates of the squares. We then perform a binary search on the range of possible y-coordinates. For each y-coordinate, we calculate the area of the squares above and below the line by iterating over all squares and calculating the area of the part of each square that is above or below the line. We use the formula for the area of a rectangle to calculate the area of each part. If the areas above and below the line are equal, we update our answer and continue the binary search to find the minimum y-coordinate. We repeat this process until we find the minimum y-coordinate value that satisfies the condition or until the binary search range is empty.



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
    double separateSquares(vector<vector<int>>& squares) {
        double minY = INT_MAX, maxY = INT_MIN;
        double totalArea = 0;
        for (auto& square : squares) {
            minY = min(minY, (double)square[1]);
            maxY = max(maxY, (double)square[1] + square[2]);
            totalArea += square[2] * square[2];
        }
        double low = minY, high = maxY;
        while (high - low > 1e-6) {
            double mid = (low + high) / 2;
            double areaBelow = 0;
            for (auto& square : squares) {
                double overlap = max(0.0, min((double)square[1] + square[2], mid) - max((double)square[1], mid));
                areaBelow += overlap * square[2];
            }
            if (areaBelow * 2 > totalArea) {
                high = mid;
            } else {
                low = mid;
            }
        }
        return (low + high) / 2;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public double separateSquares(int[][] squares) {
        double minY = Integer.MAX_VALUE, maxY = Integer.MIN_VALUE;
        double totalArea = 0;
        for (int[] square : squares) {
            minY = Math.min(minY, (double)square[1]);
            maxY = Math.max(maxY, (double)square[1] + square[2]);
            totalArea += square[2] * square[2];
        }
        double low = minY, high = maxY;
        while (high - low > 1e-6) {
            double mid = (low + high) / 2;
            double areaBelow = 0;
            for (int[] square : squares) {
                double overlap = Math.max(0.0, Math.min((double)square[1] + square[2], mid) - Math.max((double)square[1], mid));
                areaBelow += overlap * square[2];
            }
            if (areaBelow * 2 > totalArea) {
                high = mid;
            } else {
                low = mid;
            }
        }
        return (low + high) / 2;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def separateSquares(self, squares):
        minY = float('inf')
        maxY = float('-inf')
        totalArea = 0
        for square in squares:
            minY = min(minY, square[1])
            maxY = max(maxY, square[1] + square[2])
            totalArea += square[2] * square[2]
        low, high = minY, maxY
        while high - low > 1e-6:
            mid = (low + high) / 2
            areaBelow = 0
            for square in squares:
                overlap = max(0.0, min(square[1] + square[2], mid) - max(square[1], mid))
                areaBelow += overlap * square[2]
            if areaBelow * 2 > totalArea:
                high = mid
            else:
                low = mid
        return (low + high) / 2
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def separateSquares(self, squares: list[list[int]]) -> float:
        minY = float('inf')
        maxY = float('-inf')
        totalArea = 0
        for square in squares:
            minY = min(minY, square[1])
            maxY = max(maxY, square[1] + square[2])
            totalArea += square[2] * square[2]
        low, high = minY, maxY
        while high - low > 1e-6:
            mid = (low + high) / 2
            areaBelow = 0
            for square in squares:
                overlap = max(0.0, min(square[1] + square[2], mid) - max(square[1], mid))
                areaBelow += overlap * square[2]
            if areaBelow * 2 > totalArea:
                high = mid
            else:
                low = mid
        return (low + high) / 2
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
double separateSquares(int** squares, int squaresSize, int* squaresColSize) {
    double minY = INT_MAX, maxY = INT_MIN;
    double totalArea = 0;
    for (int i = 0; i < squaresSize; i++) {
        minY = (minY < squares[i][1]) ? minY : squares[i][1];
        maxY = (maxY > squares[i][1] + squares[i][2]) ? maxY : squares[i][1] + squares[i][2];
        totalArea += squares[i][2] * squares[i][2];
    }
    double low = minY, high = maxY;
    while (high - low > 1e-6) {
        double mid = (low + high) / 2;
        double areaBelow = 0;
        for (int i = 0; i < squaresSize; i++) {
            double overlap = (squares[i][1] + squares[i][2] < mid) ? squares[i][2] : (mid - squares[i][1]);
            areaBelow += overlap * squares[i][2];
        }
        if (areaBelow * 2 > totalArea) {
            high = mid;
        } else {
            low = mid;
        }
    }
    return (low + high) / 2;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public double SeparateSquares(int[][] squares) {
        double minY = int.MaxValue, maxY = int.MinValue;
        double totalArea = 0;
        for (int i = 0; i < squares.Length; i++) {
            minY = Math.Min(minY, squares[i][1]);
            maxY = Math.Max(maxY, squares[i][1] + squares[i][2]);
            totalArea += squares[i][2] * squares[i][2];
        }
        double low = minY, high = maxY;
        while (high - low > 1e-6) {
            double mid = (low + high) / 2;
            double areaBelow = 0;
            for (int i = 0; i < squares.Length; i++) {
                double overlap = Math.Max(0.0, Math.Min(squares[i][1] + squares[i][2], mid) - Math.Max(squares[i][1], mid));
                areaBelow += overlap * squares[i][2];
            }
            if (areaBelow * 2 > totalArea) {
                high = mid;
            } else {
                low = mid;
            }
        }
        return (low + high) / 2;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var separateSquares = function(squares) {
    let minY = Infinity, maxY = -Infinity;
    let totalArea = 0;
    for (let square of squares) {
        minY = Math.min(minY, square[1]);
        maxY = Math.max(maxY, square[1] + square[2]);
        totalArea += square[2] * square[2];
    }
    let low = minY, high = maxY;
    while (high - low > 1e-6) {
        let mid = (low + high) / 2;
        let areaBelow = 0;
        for (let square of squares) {
            let overlap = Math.max(0.0, Math.min(square[1] + square[2], mid) - Math.max(square[1], mid));
            areaBelow += overlap * square[2];
        }
        if (areaBelow * 2 > totalArea) {
            high = mid;
        } else {
            low = mid;
        }
    }
    return (low + high) / 2;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function separateSquares(squares: number[][]): number {
    let minY: number = Infinity, maxY: number = -Infinity;
    let totalArea: number = 0;
    for (let square of squares) {
        minY = Math.min(minY, square[1]);
        maxY = Math.max(maxY, square[1] + square[2]);
        totalArea += square[2] * square[2];
    }
    let low: number = minY, high: number = maxY;
    while (high - low > 1e-6) {
        let mid: number = (low + high) / 2;
        let areaBelow: number = 0;
        for (let square of squares) {
            let overlap: number = Math.max(0.0, Math.min(square[1] + square[2], mid) - Math.max(square[1], mid));
            areaBelow += overlap * square[2];
        }
        if (areaBelow * 2 > totalArea) {
            high = mid;
        } else {
            low = mid;
        }
    }
    return (low + high) / 2;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function separateSquares($squares) {
        $minY = PHP_INT_MAX;
        $maxY = PHP_INT_MIN;
        $totalArea = 0;
        foreach ($squares as $square) {
            $minY = min($minY, $square[1]);
            $maxY = max($maxY, $square[1] + $square[2]);
            $totalArea += $square[2] * $square[2];
        }
        $low = $minY;
        $high = $maxY;
        while ($high - $low > 1e-6) {
            $mid = ($low + $high) / 2;
            $areaBelow = 0;
            foreach ($squares as $square) {
                $overlap = max(0.0, min($square[1] + $square[2], $mid) - max($square[1], $mid));
                $areaBelow += $overlap * $square[2];
            }
            if ($areaBelow * 2 > $totalArea) {
                $high = $mid;
            } else {
                $low = $mid;
            }
        }
        return ($low + $high) / 2;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func separateSquares(_ squares: [[Int]]) -> Double {
        var minY: Double = Double.greatestFiniteMagnitude
        var maxY: Double = Double.leastNormalMagnitude
        var totalArea: Double = 0
        for square in squares {
            minY = min(minY, Double(square[1]))
            maxY = max(maxY, Double(square[1]) + Double(square[2]))
            totalArea += Double(square[2]) * Double(square[2])
        }
        var low: Double = minY
        var high: Double = maxY
        while high - low > 1e-6 {
            let mid: Double = (low + high) / 2
            var areaBelow: Double = 0
            for square in squares {
                let overlap: Double = max(0.0, min(Double(square[1]) + Double(square[2]), mid) - max(Double(square[1]), mid))
                areaBelow += overlap * Double(square[2])
            }
            if areaBelow * 2 > totalArea {
                high = mid
            } else {
                low = mid
            }
        }
        return (low + high) / 2
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun separateSquares(squares: Array<IntArray>): Double {
        var minY = Int.MAX_VALUE
        var maxY = Int.MIN_VALUE
        var totalArea = 0.0
        for (square in squares) {
            val (x, y, l) = square
            minY = minOf(minY, y)
            maxY = maxOf(maxY, y + l)
            totalArea += l * l
        }
        var low = minY.toDouble()
        var high = maxY.toDouble()
        while (high - low > 1e-6) {
            val mid = (low + high) / 2
            var areaBelow = 0.0
            for (square in squares) {
                val (x, y, l) = square
                val overlap = maxOf(0.0, minOf(mid, y + l) - maxOf(mid, y))
                areaBelow += overlap * l
            }
            if (areaBelow < totalArea / 2) {
                low = mid
            } else {
                high = mid
            }
        }
        return low
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  double separateSquares(List<List<int>> squares) {
    double minY = double.maxFinite;
    double maxY = double.negativeInfinity;
    double totalArea = 0;
    for (var square in squares) {
      var x = square[0];
      var y = square[1];
      var l = square[2];
      minY = minY < y ? minY : y;
      maxY = maxY > y + l ? maxY : y + l;
      totalArea += l * l;
    }
    double low = minY;
    double high = maxY;
    while (high - low > 1e-6) {
      double mid = (low + high) / 2;
      double areaBelow = 0;
      for (var square in squares) {
        var x = square[0];
        var y = square[1];
        var l = square[2];
        double overlap = max(0, min(mid, y + l) - max(mid, y));
        areaBelow += overlap * l;
      }
      if (areaBelow < totalArea / 2) {
        low = mid;
      } else {
        high = mid;
      }
    }
    return low;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func separateSquares(squares [][]int) float64 {
    minY := int(^uint(0)>>1)
    maxY := int(^uint(0))
    totalArea := 0.0
    for _, square := range squares {
        x, y, l := square[0], square[1], square[2]
        if y < minY {
            minY = y
        }
        if y+l > maxY {
            maxY = y + l
        }
        totalArea += float64(l * l)
    }
    low := float64(minY)
    high := float64(maxY)
    for high-low > 1e-6 {
        mid := (low + high) / 2
        areaBelow := 0.0
        for _, square := range squares {
            x, y, l := square[0], square[1], square[2]
            overlap := max(0, min(mid, float64(y+l)) - max(mid, float64(y)))
            areaBelow += overlap * float64(l)
        }
        if areaBelow < totalArea/2 {
            low = mid
        } else {
            high = mid
        }
    }
    return low
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def separate_squares(squares)
    min_y = Float::INFINITY
    max_y = -Float::INFINITY
    total_area = 0
    squares.each do |square|
        x, y, l = square
        min_y = [min_y, y].min
        max_y = [max_y, y + l].max
        total_area += l * l
    end
    low = min_y.to_f
    high = max_y.to_f
    while high - low > 1e-6
        mid = (low + high) / 2
        area_below = 0
        squares.each do |square|
            x, y, l = square
            overlap = [0, [mid, y + l].min - [mid, y].max].max
            area_below += overlap * l
        end
        if area_below < total_area / 2
            low = mid
        else
            high = mid
        end
    end
    low
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def separateSquares(squares: Array[Array[Int]]): Double = {
        var minY = Int.MaxValue
        var maxY = Int.MinValue
        var totalArea = 0.0
        for (square <- squares) {
            val Array(x, y, l) = square
            minY = Math.min(minY, y)
            maxY = Math.max(maxY, y + l)
            totalArea += l * l
        }
        var low = minY.toDouble
        var high = maxY.toDouble
        while (high - low > 1e-6) {
            val mid = (low + high) / 2
            var areaBelow = 0.0
            for (square <- squares) {
                val Array(x, y, l) = square
                val overlap = Math.max(0, Math.min(mid, y + l) - Math.max(mid, y))
                areaBelow += overlap * l
            }
            if (areaBelow < totalArea / 2) {
                low = mid
            } else {
                high = mid
            }
        }
        low
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn separate_squares(squares: Vec<Vec<i32>>) -> f64 {
        let mut min_y = i32::MAX;
        let mut max_y = i32::MIN;
        let mut total_area = 0.0;
        for square in &squares {
            let x = square[0];
            let y = square[1];
            let l = square[2];
            min_y = min_y.min(y);
            max_y = max_y.max(y + l);
            total_area += (l as f64) * (l as f64);
        }
        let mut low = min_y as f64;
        let mut high = max_y as f64;
        while high - low > 1e-6 {
            let mid = (low + high) / 2.0;
            let mut area_below = 0.0;
            for square in &squares {
                let x = square[0];
                let y = square[1];
                let l = square[2];
                let overlap = (mid.min((y + l) as f64) - mid.max(y as f64)).max(0.0);
                area_below += overlap * (l as f64);
            }
            if area_below < total_area / 2.0 {
                low = mid;
            } else {
                high = mid;
            }
        }
        low
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (separate-squares squares)
  (-> (listof (listof exact-integer?)) flonum?)
  (let* ([min-y (apply min (map (lambda (s) (second s)) squares))]
         [max-y (apply max (map (lambda (s) (+ (second s) (third s))) squares))]
         [total-area (apply + (map (lambda (s) (expt (third s) 2)) squares))])
    (let loop ([low min-y] [high max-y])
      (if (> (- high low) 1e-6)
          (let* ([mid (/ (+ low high) 2)]
                 [area-below (apply + (map (lambda (s)
                                             (let ([x (first s)] [y (second s)] [l (third s)])
                                               (let ([overlap (max 0 (- (min mid (+ y l)) (max mid y)))])
                                                 (* overlap l)))) squares))])
            (if (< area-below (/ total-area 2))
                (loop mid high)
                (loop low mid)))
          low))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
separate_squares(Squares) ->
    MinY = lists:min([Y || [_, Y, _] <- Squares]),
    MaxY = lists:max([Y + L || [_, Y, L] <- Squares]),
    TotalArea = lists:sum([L * L || [_, _, L] <- Squares]),
    separate_squares(Squares, MinY, MaxY, TotalArea, MinY).

separate_squares(Squares, Low, High, TotalArea, Acc) ->
    case High - Low > 1.0e-6 of
        true ->
            Mid = (Low + High) / 2,
            AreaBelow = lists:sum([overlap(Mid, Y, L) * L || [_, Y, L] <- Squares]),
            case AreaBelow < TotalArea / 2 of
                true -> separate_squares(Squares, Mid, High, TotalArea, Mid);
                false -> separate_squares(Squares, Low, Mid, TotalArea, Mid)
            end;
        false -> Acc
    end.

overlap(Mid, Y, L) -> max(0, min(Mid, Y + L) - max(Mid, Y)).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec separate_squares(squares :: [[integer]]) :: float
  def separate_squares(squares) do
    min_y = Enum.min_by(squares, fn [_, y, _] -> y end)
    max_y = Enum.max_by(squares, fn [_, y, l] -> y + l end)
    total_area = Enum.sum(Enum.map(squares, fn [_, _, l] -> l * l end))
    separate_squares(squares, min_y, max_y, total_area, min_y)
  end

  defp separate_squares(squares, low, high, total_area, acc) do
    cond do
      high - low > 1.0e-6 ->
        mid = (low + high) / 2
        area_below = Enum.sum(Enum.map(squares, fn [_, y, l] -> overlap(mid, y, l) * l end))
        cond do
          area_below < total_area / 2 -> separate_squares(squares, mid, high, total_area, mid)
          true -> separate_squares(squares, low, mid, total_area, mid)
        end
      true -> acc
    end
  end

  defp overlap(mid, y, l) do
    max(0, min(mid, y + l) - max(mid, y))
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n log h) where n is the number of squares and h is the height of the bounding box of all squares. This is because we perform a binary search on the possible y-coordinates and for each y-coordinate, we iterate over all squares to calculate the area above and below the line. The binary search reduces the number of iterations from O(h) to O(log h), resulting in a significant improvement in performance for large inputs.



- **Space Complexity:** O(1) because we only use a constant amount of space to store the minimum and maximum y-coordinates, the total area of all squares, and the current y-coordinate being considered in the binary search. We do not use any data structures that grow with the size of the input, so the space complexity is constant.



</div>
</details>
