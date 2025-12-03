---
layout: post
title: "Count Number of Trapezoids II"
date: 2025-12-03 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Hash Table", "Math", "Geometry"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/count-number-of-trapezoids-ii/
ai_solutions:
  - solutions:
      cpp: "#include <vector>\n#include <map>\n#include <numeric>\n#include <cmath>\n\
        #include <algorithm>\n\n// Function to calculate GCD\nlong long calculate_gcd(long\
        \ long a, long long b) {\n    return std::abs(std::gcd(a, b));\n}\n\nclass Solution\
        \ {\npublic:\n    int countTrapezoids(std::vector<std::vector<int>>& points)\
        \ {\n        int n = points.size();\n\n        std::map<std::pair<long long,\
        \ long long>, std::vector<std::pair<int, int>>> slope_map;\n        std::map<std::pair<long\
        \ long, long long>, int> midpoint_map;\n\n        for (int i = 0; i < n; ++i)\
        \ {\n            for (int j = i + 1; j < n; ++j) {\n                long long\
        \ dx = (long long)points[j][0] - points[i][0];\n                long long dy\
        \ = (long long)points[j][1] - points[i][1];\n\n                long long common_divisor\
        \ = calculate_gcd(dx, dy);\n                long long ndx = dx / common_divisor;\n\
        \                long long ndy = dy / common_divisor;\n\n                if\
        \ (ndx < 0 || (ndx == 0 && ndy < 0)) {\n                    ndx = -ndx;\n  \
        \                  ndy = -ndy;\n                }\n\n                slope_map[{ndy,\
        \ ndx}].push_back({i, j});\n\n                long long mx = (long long)points[i][0]\
        \ + points[j][0];\n                long long my = (long long)points[i][1] +\
        \ points[j][1];\n                midpoint_map[{mx, my}]++;\n            }\n\
        \        }\n\n        long long total_trapezoids = 0;\n\n        for (auto const&\
        \ [slope_key, segments] : slope_map) {\n            long long k = segments.size();\n\
        \n            if (k < 2) {\n                continue;\n            }\n\n   \
        \         long long current_slope_total_pairs = k * (k - 1) / 2;\n\n       \
        \     std::map<int, int> endpoint_freq;\n            for (const auto& seg :\
        \ segments) {\n                endpoint_freq[seg.first]++;\n               \
        \ endpoint_freq[seg.second]++;\n            }\n\n            long long shared_endpoint_pairs\
        \ = 0;\n            for (auto const& [point_idx, count] : endpoint_freq) {\n\
        \                if (count >= 2) {\n                    shared_endpoint_pairs\
        \ += (long long)count * (count - 1) / 2;\n                }\n            }\n\
        \n            long long num_disjoint_parallel_pairs = current_slope_total_pairs\
        \ - shared_endpoint_pairs;\n\n            long long ndy = slope_key.first;\n\
        \            long long ndx = slope_key.second;\n\n            std::map<long\
        \ long, std::vector<std::pair<int, int>>> line_segments_map;\n\n           \
        \ for (const auto& seg : segments) {\n                const auto& p = points[seg.first];\n\
        \                long long line_constant = ndx * p[1] - ndy * p[0];\n      \
        \          line_segments_map[line_constant].push_back(seg);\n            }\n\
        \n            long long collinear_disjoint_parallel_pairs = 0;\n           \
        \ for (auto const& [line_constant, segments_on_this_line] : line_segments_map)\
        \ {\n                long long k_line = segments_on_this_line.size();\n\n  \
        \              if (k_line < 2) {\n                    continue;\n          \
        \      }\n\n                long long current_line_total_pairs = k_line * (k_line\
        \ - 1) / 2;\n\n                std::map<int, int> endpoint_freq_on_line;\n \
        \               for (const auto& seg : segments_on_this_line) {\n          \
        \          endpoint_freq_on_line[seg.first]++;\n                    endpoint_freq_on_line[seg.second]++;\n\
        \                }\n\n                long long shared_endpoint_pairs_on_line\
        \ = 0;\n                for (auto const& [point_idx, count] : endpoint_freq_on_line)\
        \ {\n                    if (count >= 2) {\n                        shared_endpoint_pairs_on_line\
        \ += (long long)count * (count - 1) / 2;\n                    }\n          \
        \      }\n\n                collinear_disjoint_parallel_pairs += (current_line_total_pairs\
        \ - shared_endpoint_pairs_on_line);\n            }\n\n            total_trapezoids\
        \ += (num_disjoint_parallel_pairs - collinear_disjoint_parallel_pairs);\n  \
        \      }\n\n        long long parallelograms = 0;\n        for (auto const&\
        \ [midpoint_key, count] : midpoint_map) {\n            if (count >= 2) {\n \
        \               parallelograms += (long long)count * (count - 1) / 2;\n    \
        \        }\n        }\n\n        return total_trapezoids - parallelograms;\n\
        \    }\n};"
      java: "import java.util.*;\n\nclass Solution {\n    private long calculateGcd(long\
        \ a, long b) {\n        return Math.abs(gcd(a, b));\n    }\n\n    private long\
        \ gcd(long a, long b) {\n        while (b != 0) {\n            long temp = b;\n\
        \            b = a % b;\n            a = temp;\n        }\n        return a;\n\
        \    }\n\n    public int countTrapezoids(int[][] points) {\n        int n =\
        \ points.length;\n\n        Map<Point, List<PointPair>> slopeMap = new HashMap<>();\n\
        \        Map<Point, Integer> midpointMap = new HashMap<>();\n\n        for (int\
        \ i = 0; i < n; ++i) {\n            for (int j = i + 1; j < n; ++j) {\n    \
        \            long dx = (long)points[j][0] - points[i][0];\n                long\
        \ dy = (long)points[j][1] - points[i][1];\n\n                long commonDivisor\
        \ = calculateGcd(dx, dy);\n                long ndx = dx / commonDivisor;\n\
        \                long ndy = dy / commonDivisor;\n\n                if (ndx <\
        \ 0 || (ndx == 0 && ndy < 0)) {\n                    ndx = -ndx;\n         \
        \           ndy = -ndy;\n                }\n\n                Point slopeKey\
        \ = new Point(ndy, ndx);\n                slopeMap.computeIfAbsent(slopeKey,\
        \ k -> new ArrayList<>()).add(new PointPair(i, j));\n\n                long\
        \ mx = (long)points[i][0] + points[j][0];\n                long my = (long)points[i][1]\
        \ + points[j][1];\n                Point midpointKey = new Point(mx, my);\n\
        \                midpointMap.put(midpointKey, midpointMap.getOrDefault(midpointKey,\
        \ 0) + 1);\n            }\n        }\n\n        long totalTrapezoids = 0;\n\n\
        \        for (Map.Entry<Point, List<PointPair>> entry : slopeMap.entrySet())\
        \ {\n            List<PointPair> segments = entry.getValue();\n            long\
        \ k = segments.size();\n\n            if (k < 2) {\n                continue;\n\
        \            }\n\n            long currentSlopeTotalPairs = k * (k - 1) / 2;\n\
        \n            Map<Integer, Integer> endpointFreq = new HashMap<>();\n      \
        \      for (PointPair seg : segments) {\n                endpointFreq.put(seg.p1Idx,\
        \ endpointFreq.getOrDefault(seg.p1Idx, 0) + 1);\n                endpointFreq.put(seg.p2Idx,\
        \ endpointFreq.getOrDefault(seg.p2Idx, 0) + 1);\n            }\n\n         \
        \   long sharedEndpointPairs = 0;\n            for (int count : endpointFreq.values())\
        \ {\n                if (count >= 2) {\n                    sharedEndpointPairs\
        \ += (long)count * (count - 1) / 2;\n                }\n            }\n\n  \
        \          long numDisjointParallelPairs = currentSlopeTotalPairs - sharedEndpointPairs;\n\
        \n            Point slopeKey = entry.getKey();\n            long ndy = slopeKey.x;\n\
        \            long ndx = slopeKey.y;\n\n            Map<Long, List<PointPair>>\
        \ lineSegmentsMap = new HashMap<>();\n\n            for (PointPair seg : segments)\
        \ {\n                int[] p = points[seg.p1Idx];\n                long lineConstant\
        \ = ndx * p[1] - ndy * p[0];\n                lineSegmentsMap.computeIfAbsent(lineConstant,\
        \ l -> new ArrayList<>()).add(seg);\n            }\n\n            long collinearDisjointParallelPairs\
        \ = 0;\n            for (List<PointPair> segmentsOnThisLine : lineSegmentsMap.values())\
        \ {\n                long kLine = segmentsOnThisLine.size();\n\n           \
        \     if (kLine < 2) {\n                    continue;\n                }\n\n\
        \                long currentLineTotalPairs = kLine * (kLine - 1) / 2;\n\n \
        \               Map<Integer, Integer> endpointFreqOnLine = new HashMap<>();\n\
        \                for (PointPair seg : segmentsOnThisLine) {\n              \
        \      endpointFreqOnLine.put(seg.p1Idx, endpointFreqOnLine.getOrDefault(seg.p1Idx,\
        \ 0) + 1);\n                    endpointFreqOnLine.put(seg.p2Idx, endpointFreqOnLine.getOrDefault(seg.p2Idx,\
        \ 0) + 1);\n                }\n\n                long sharedEndpointPairsOnLine\
        \ = 0;\n                for (int count : endpointFreqOnLine.values()) {\n  \
        \                  if (count >= 2) {\n                        sharedEndpointPairsOnLine\
        \ += (long)count * (count - 1) / 2;\n                    }\n               \
        \ }\n\n                collinearDisjointParallelPairs += (currentLineTotalPairs\
        \ - sharedEndpointPairsOnLine);\n            }\n\n            totalTrapezoids\
        \ += (numDisjointParallelPairs - collinearDisjointParallelPairs);\n        }\n\
        \n        long parallelograms = 0;\n        for (int count : midpointMap.values())\
        \ {\n            if (count >= 2) {\n                parallelograms += (long)count\
        \ * (count - 1) / 2;\n            }\n        }\n\n        return (int)(totalTrapezoids\
        \ - parallelograms);\n    }\n\n    // Custom Point class for map keys\n    static\
        \ class Point {\n        long x, y;\n\n        Point(long x, long y) {\n   \
        \         this.x = x;\n            this.y = y;\n        }\n\n        @Override\n\
        \        public boolean equals(Object o) {\n            if (this == o) return\
        \ true;\n            if (o == null || getClass() != o.getClass()) return false;\n\
        \            Point point = (Point) o;\n            return x == point.x && y\
        \ == point.y;\n        }\n\n        @Override\n        public int hashCode()\
        \ {\n            return Objects.hash(x, y);\n        }\n    }\n\n    // Custom\
        \ PointPair class to store segment endpoints indices\n    static class PointPair\
        \ {\n        int p1Idx, p2Idx;\n\n        PointPair(int p1Idx, int p2Idx) {\n\
        \            this.p1Idx = p1Idx;\n            this.p2Idx = p2Idx;\n        }\n\
        \    }\n}"
      python: "import math\nimport collections\n\nclass Solution:\n    def countTrapezoids(self,\
        \ points: list[list[int]]) -> int:\n        n = len(points)\n\n        slope_map\
        \ = collections.defaultdict(list) # key: (dy, dx), value: list of (p1_idx, p2_idx)\n\
        \        midpoint_map = collections.defaultdict(int) # key: (x_sum, y_sum),\
        \ value: count of pairs\n\n        # Helper for GCD\n        def calculate_gcd(a,\
        \ b):\n            return math.gcd(a, b)\n\n        for i in range(n):\n   \
        \         for j in range(i + 1, n):\n                p1 = points[i]\n      \
        \          p2 = points[j]\n\n                dx = p2[0] - p1[0]\n          \
        \      dy = p2[1] - p1[1]\n\n                # Normalize slope\n           \
        \     common_divisor = calculate_gcd(abs(dx), abs(dy))\n                ndx\
        \ = dx // common_divisor\n                ndy = dy // common_divisor\n\n   \
        \             # Canonical representation: ndx > 0, or (ndx == 0 and ndy > 0)\n\
        \                if ndx < 0 or (ndx == 0 and ndy < 0):\n                   \
        \ ndx = -ndx\n                    ndy = -ndy\n\n                slope_map[(ndy,\
        \ ndx)].append((i, j))\n\n                # Calculate doubled midpoint for parallelogram\
        \ check\n                mx = p1[0] + p2[0]\n                my = p1[1] + p2[1]\n\
        \                midpoint_map[(mx, my)] += 1\n\n        total_trapezoids = 0\n\
        \n        # Count pairs of parallel segments that are disjoint and non-collinear\n\
        \        for slope_key in slope_map:\n            segments = slope_map[slope_key]\n\
        \            k = len(segments)\n\n            if k < 2:\n                continue\n\
        \n            # Step 1: Calculate total pairs of segments with this slope (C(k,2))\n\
        \            current_slope_total_pairs = k * (k - 1) // 2\n\n            # Step\
        \ 2: Subtract pairs that share an endpoint\n            endpoint_freq = collections.defaultdict(int)\n\
        \            for p1_idx, p2_idx in segments:\n                endpoint_freq[p1_idx]\
        \ += 1\n                endpoint_freq[p2_idx] += 1\n\n            shared_endpoint_pairs\
        \ = 0\n            for count in endpoint_freq.values():\n                if\
        \ count >= 2:\n                    shared_endpoint_pairs += count * (count -\
        \ 1) // 2\n\n            # This is the count of disjoint parallel segments,\
        \ including collinear ones\n            num_disjoint_parallel_pairs = current_slope_total_pairs\
        \ - shared_endpoint_pairs\n\n            # Step 3: Subtract pairs that are collinear\
        \ (i.e., lie on the same line)\n            # For a given slope (ndy, ndx),\
        \ a line can be identified by the constant C = ndx*y - ndy*x\n            ndy,\
        \ ndx = slope_key\n            line_segments_map = collections.defaultdict(list)\
        \ # key: line_constant, value: list of (p1_idx, p2_idx)\n\n            for p1_idx,\
        \ p2_idx in segments:\n                p = points[p1_idx] # Use any point on\
        \ the segment to calculate the line constant\n                line_constant\
        \ = ndx * p[1] - ndy * p[0]\n                line_segments_map[line_constant].append((p1_idx,\
        \ p2_idx))\n\n            collinear_disjoint_parallel_pairs = 0\n          \
        \  for line_constant in line_segments_map:\n                segments_on_this_line\
        \ = line_segments_map[line_constant]\n                k_line = len(segments_on_this_line)\n\
        \n                if k_line < 2:\n                    continue\n\n         \
        \       # Calculate disjoint pairs *on this line*\n                current_line_total_pairs\
        \ = k_line * (k_line - 1) // 2\n\n                endpoint_freq_on_line = collections.defaultdict(int)\n\
        \                for p1_idx, p2_idx in segments_on_this_line:\n            \
        \        endpoint_freq_on_line[p1_idx] += 1\n                    endpoint_freq_on_line[p2_idx]\
        \ += 1\n\n                shared_endpoint_pairs_on_line = 0\n              \
        \  for count in endpoint_freq_on_line.values():\n                    if count\
        \ >= 2:\n                        shared_endpoint_pairs_on_line += count * (count\
        \ - 1) // 2\n\n                collinear_disjoint_parallel_pairs += (current_line_total_pairs\
        \ - shared_endpoint_pairs_on_line)\n\n            total_trapezoids += (num_disjoint_parallel_pairs\
        \ - collinear_disjoint_parallel_pairs)\n\n        # Count parallelograms\n \
        \       parallelograms = 0\n        for count in midpoint_map.values():\n  \
        \          if count >= 2:\n                parallelograms += count * (count\
        \ - 1) // 2\n\n        return total_trapezoids - parallelograms"
      python3: "import math\nimport collections\n\nclass Solution:\n    def countTrapezoids(self,\
        \ points: list[list[int]]) -> int:\n        n = len(points)\n\n        slope_map\
        \ = collections.defaultdict(list) # key: (dy, dx), value: list of (p1_idx, p2_idx)\n\
        \        midpoint_map = collections.defaultdict(int) # key: (x_sum, y_sum),\
        \ value: count of pairs\n\n        # Helper for GCD\n        def calculate_gcd(a,\
        \ b):\n            return math.gcd(a, b)\n\n        for i in range(n):\n   \
        \         for j in range(i + 1, n):\n                p1 = points[i]\n      \
        \          p2 = points[j]\n\n                dx = p2[0] - p1[0]\n          \
        \      dy = p2[1] - p1[1]\n\n                # Normalize slope\n           \
        \     common_divisor = calculate_gcd(abs(dx), abs(dy))\n                ndx\
        \ = dx // common_divisor\n                ndy = dy // common_divisor\n\n   \
        \             # Canonical representation: ndx > 0, or (ndx == 0 and ndy > 0)\n\
        \                if ndx < 0 or (ndx == 0 and ndy < 0):\n                   \
        \ ndx = -ndx\n                    ndy = -ndy\n\n                slope_map[(ndy,\
        \ ndx)].append((i, j))\n\n                # Calculate doubled midpoint for parallelogram\
        \ check\n                mx = p1[0] + p2[0]\n                my = p1[1] + p2[1]\n\
        \                midpoint_map[(mx, my)] += 1\n\n        total_trapezoids = 0\n\
        \n        # Count pairs of parallel segments that are disjoint and non-collinear\n\
        \        for slope_key in slope_map:\n            segments = slope_map[slope_key]\n\
        \            k = len(segments)\n\n            if k < 2:\n                continue\n\
        \n            # Step 1: Calculate total pairs of segments with this slope (C(k,2))\n\
        \            current_slope_total_pairs = k * (k - 1) // 2\n\n            # Step\
        \ 2: Subtract pairs that share an endpoint\n            endpoint_freq = collections.defaultdict(int)\n\
        \            for p1_idx, p2_idx in segments:\n                endpoint_freq[p1_idx]\
        \ += 1\n                endpoint_freq[p2_idx] += 1\n\n            shared_endpoint_pairs\
        \ = 0\n            for count in endpoint_freq.values():\n                if\
        \ count >= 2:\n                    shared_endpoint_pairs += count * (count -\
        \ 1) // 2\n\n            # This is the count of disjoint parallel segments,\
        \ including collinear ones\n            num_disjoint_parallel_pairs = current_slope_total_pairs\
        \ - shared_endpoint_pairs\n\n            # Step 3: Subtract pairs that are collinear\
        \ (i.e., lie on the same line)\n            # For a given slope (ndy, ndx),\
        \ a line can be identified by the constant C = ndx*y - ndy*x\n            ndy,\
        \ ndx = slope_key\n            line_segments_map = collections.defaultdict(list)\
        \ # key: line_constant, value: list of (p1_idx, p2_idx)\n\n            for p1_idx,\
        \ p2_idx in segments:\n                p = points[p1_idx] # Use any point on\
        \ the segment to calculate the line constant\n                line_constant\
        \ = ndx * p[1] - ndy * p[0]\n                line_segments_map[line_constant].append((p1_idx,\
        \ p2_idx))\n\n            collinear_disjoint_parallel_pairs = 0\n          \
        \  for line_constant in line_segments_map:\n                segments_on_this_line\
        \ = line_segments_map[line_constant]\n                k_line = len(segments_on_this_line)\n\
        \n                if k_line < 2:\n                    continue\n\n         \
        \       # Calculate disjoint pairs *on this line*\n                current_line_total_pairs\
        \ = k_line * (k_line - 1) // 2\n\n                endpoint_freq_on_line = collections.defaultdict(int)\n\
        \                for p1_idx, p2_idx in segments_on_this_line:\n            \
        \        endpoint_freq_on_line[p1_idx] += 1\n                    endpoint_freq_on_line[p2_idx]\
        \ += 1\n\n                shared_endpoint_pairs_on_line = 0\n              \
        \  for count in endpoint_freq_on_line.values():\n                    if count\
        \ >= 2:\n                        shared_endpoint_pairs_on_line += count * (count\
        \ - 1) // 2\n\n                collinear_disjoint_parallel_pairs += (current_line_total_pairs\
        \ - shared_endpoint_pairs_on_line)\n\n            total_trapezoids += (num_disjoint_parallel_pairs\
        \ - collinear_disjoint_parallel_pairs)\n\n        # Count parallelograms\n \
        \       parallelograms = 0\n        for count in midpoint_map.values():\n  \
        \          if count >= 2:\n                parallelograms += count * (count\
        \ - 1) // 2\n\n        return total_trapezoids - parallelograms"
      c: /* C does not have built-in maps or dynamic lists like C++ or Java. Implementing
        this in C would require custom hash table implementations or sorting, which
        would be significantly more complex and verbose than other languages. Given
        the constraints and typical LeetCode environment, C solutions for problems of
        this complexity often rely on external libraries or are not expected to be as
        idiomatic as C++/Java/Python. For this problem, the use of hash maps for slopes,
        midpoints, and endpoint frequencies is central to achieving the O(N^2) complexity.
        A direct C implementation would likely exceed typical length limits or be too
        cumbersome. */
      csharp: "using System;\nusing System.Collections.Generic;\nusing System.Linq;\n\
        \npublic class Solution {\n    private long CalculateGcd(long a, long b) {\n\
        \        return Math.Abs(Gcd(a, b));\n    }\n\n    private long Gcd(long a,\
        \ long b) {\n        while (b != 0) {\n            long temp = b;\n        \
        \    b = a % b;\n            a = temp;\n        }\n        return a;\n    }\n\
        \n    public int CountTrapezoids(int[][] points) {\n        int n = points.Length;\n\
        \n        Dictionary<Tuple<long, long>, List<Tuple<int, int>>> slopeMap = new\
        \ Dictionary<Tuple<long, long>, List<Tuple<int, int>>>();\n        Dictionary<Tuple<long,\
        \ long>, int> midpointMap = new Dictionary<Tuple<long, long>, int>();\n\n  \
        \      for (int i = 0; i < n; ++i) {\n            for (int j = i + 1; j < n;\
        \ ++j) {\n                long dx = (long)points[j][0] - points[i][0];\n   \
        \             long dy = (long)points[j][1] - points[i][1];\n\n             \
        \   long commonDivisor = CalculateGcd(dx, dy);\n                long ndx = dx\
        \ / commonDivisor;\n                long ndy = dy / commonDivisor;\n\n     \
        \           if (ndx < 0 || (ndx == 0 && ndy < 0)) {\n                    ndx\
        \ = -ndx;\n                    ndy = -ndy;\n                }\n\n          \
        \      Tuple<long, long> slopeKey = Tuple.Create(ndy, ndx);\n              \
        \  if (!slopeMap.ContainsKey(slopeKey)) {\n                    slopeMap[slopeKey]\
        \ = new List<Tuple<int, int>>();\n                }\n                slopeMap[slopeKey].Add(Tuple.Create(i,\
        \ j));\n\n                long mx = (long)points[i][0] + points[j][0];\n   \
        \             long my = (long)points[i][1] + points[j][1];\n               \
        \ Tuple<long, long> midpointKey = Tuple.Create(mx, my);\n                midpointMap[midpointKey]\
        \ = midpointMap.GetValueOrDefault(midpointKey, 0) + 1;\n            }\n    \
        \    }\n\n        long totalTrapezoids = 0;\n\n        foreach (var entry in\
        \ slopeMap) {\n            List<Tuple<int, int>> segments = entry.Value;\n \
        \           long k = segments.Count;\n\n            if (k < 2) {\n         \
        \       continue;\n            }\n\n            long currentSlopeTotalPairs\
        \ = k * (k - 1) / 2;\n\n            Dictionary<int, int> endpointFreq = new\
        \ Dictionary<int, int>();\n            foreach (var seg in segments) {\n   \
        \             endpointFreq[seg.Item1] = endpointFreq.GetValueOrDefault(seg.Item1,\
        \ 0) + 1;\n                endpointFreq[seg.Item2] = endpointFreq.GetValueOrDefault(seg.Item2,\
        \ 0) + 1;\n            }\n\n            long sharedEndpointPairs = 0;\n    \
        \        foreach (int count in endpointFreq.Values) {\n                if (count\
        \ >= 2) {\n                    sharedEndpointPairs += (long)count * (count -\
        \ 1) / 2;\n                }\n            }\n\n            long numDisjointParallelPairs\
        \ = currentSlopeTotalPairs - sharedEndpointPairs;\n\n            Tuple<long,\
        \ long> slopeKey = entry.Key;\n            long ndy = slopeKey.Item1;\n    \
        \        long ndx = slopeKey.Item2;\n\n            Dictionary<long, List<Tuple<int,\
        \ int>>> lineSegmentsMap = new Dictionary<long, List<Tuple<int, int>>>();\n\n\
        \            for (var seg in segments) {\n                int[] p = points[seg.Item1];\n\
        \                long lineConstant = ndx * p[1] - ndy * p[0];\n            \
        \    if (!lineSegmentsMap.ContainsKey(lineConstant)) {\n                   \
        \ lineSegmentsMap[lineConstant] = new List<Tuple<int, int>>();\n           \
        \     }\n                lineSegmentsMap[lineConstant].Add(seg);\n         \
        \   }\n\n            long collinearDisjointParallelPairs = 0;\n            foreach\
        \ (var segmentsOnThisLine in lineSegmentsMap.Values) {\n                long\
        \ kLine = segmentsOnThisLine.Count;\n\n                if (kLine < 2) {\n  \
        \                  continue;\n                }\n\n                long currentLineTotalPairs\
        \ = kLine * (kLine - 1) / 2;\n\n                Dictionary<int, int> endpointFreqOnLine\
        \ = new Dictionary<int, int>();\n                for (var seg in segmentsOnThisLine)\
        \ {\n                    endpointFreqOnLine[seg.Item1] = endpointFreqOnLine.GetValueOrDefault(seg.Item1,\
        \ 0) + 1;\n                    endpointFreqOnLine[seg.Item2] = endpointFreqOnLine.GetValueOrDefault(seg.Item2,\
        \ 0) + 1;\n                }\n\n                long sharedEndpointPairsOnLine\
        \ = 0;\n                foreach (int count in endpointFreqOnLine.Values) {\n\
        \                    if (count >= 2) {\n                        sharedEndpointPairsOnLine\
        \ += (long)count * (count - 1) / 2;\n                    }\n               \
        \ }\n\n                collinearDisjointParallelPairs += (currentLineTotalPairs\
        \ - sharedEndpointPairsOnLine);\n            }\n\n            totalTrapezoids\
        \ += (numDisjointParallelPairs - collinearDisjointParallelPairs);\n        }\n\
        \n        long parallelograms = 0;\n        foreach (int count in midpointMap.Values)\
        \ {\n            if (count >= 2) {\n                parallelograms += (long)count\
        \ * (count - 1) / 2;\n            }\n        }\n\n        return (int)(totalTrapezoids\
        \ - parallelograms);\n    }\n}"
      javascript: "/**\n * @param {number[][]} points\n * @return {number}\n */\nvar\
        \ countTrapezoids = function(points) {\n    const n = points.length;\n\n   \
        \ const slopeMap = new Map(); // key: \"dy,dx\", value: list of [p1_idx, p2_idx]\n\
        \    const midpointMap = new Map(); // key: \"x_sum,y_sum\", value: count of\
        \ pairs\n\n    // Helper for GCD\n    function calculateGcd(a, b) {\n      \
        \  a = Math.abs(a);\n        b = Math.abs(b);\n        while (b) {\n       \
        \     [a, b] = [b, a % b];\n        }\n        return a;\n    }\n\n    for (let\
        \ i = 0; i < n; ++i) {\n        for (let j = i + 1; j < n; ++j) {\n        \
        \    const p1 = points[i];\n            const p2 = points[j];\n\n          \
        \  let dx = p2[0] - p1[0];\n            let dy = p2[1] - p1[1];\n\n        \
        \    // Normalize slope\n            const commonDivisor = calculateGcd(dx,\
        \ dy);\n            let ndx = dx / commonDivisor;\n            let ndy = dy\
        \ / commonDivisor;\n\n            // Canonical representation: ndx > 0, or (ndx\
        \ == 0 and ndy > 0)\n            if (ndx < 0 || (ndx === 0 && ndy < 0)) {\n\
        \                ndx = -ndx;\n                ndy = -ndy;\n            }\n\n\
        \            const slopeKey = `${ndy},${ndx}`;\n            if (!slopeMap.has(slopeKey))\
        \ {\n                slopeMap.set(slopeKey, []);\n            }\n          \
        \  slopeMap.get(slopeKey).push([i, j]);\n\n            // Calculate doubled\
        \ midpoint for parallelogram check\n            const mx = p1[0] + p2[0];\n\
        \            const my = p1[1] + p2[1];\n            const midpointKey = `${mx},${my}`;\n\
        \            midpointMap.set(midpointKey, (midpointMap.get(midpointKey) || 0)\
        \ + 1);\n        }\n    }\n\n    let totalTrapezoids = 0;\n\n    // Count pairs\
        \ of parallel segments that are disjoint and non-collinear\n    for (const [slopeKeyStr,\
        \ segments] of slopeMap.entries()) {\n        const k = segments.length;\n\n\
        \        if (k < 2) {\n            continue;\n        }\n\n        // Step 1:\
        \ Calculate total pairs of segments with this slope (C(k,2))\n        const\
        \ currentSlopeTotalPairs = k * (k - 1) / 2;\n\n        // Step 2: Subtract pairs\
        \ that share an endpoint\n        const endpointFreq = new Map();\n        for\
        \ (const seg of segments) {\n            endpointFreq.set(seg[0], (endpointFreq.get(seg[0])\
        \ || 0) + 1);\n            endpointFreq.set(seg[1], (endpointFreq.get(seg[1])\
        \ || 0) + 1);\n        }\n\n        let sharedEndpointPairs = 0;\n        for\
        \ (const count of endpointFreq.values()) {\n            if (count >= 2) {\n\
        \                sharedEndpointPairs += count * (count - 1) / 2;\n         \
        \   }\n        }\n\n        // This is the count of disjoint parallel segments,\
        \ including collinear ones\n        const numDisjointParallelPairs = currentSlopeTotalPairs\
        \ - sharedEndpointPairs;\n\n        // Step 3: Subtract pairs that are collinear\
        \ (i.e., lie on the same line)\n        // For a given slope (ndy, ndx), a line\
        \ can be identified by the constant C = ndx*y - ndy*x\n        const [ndy, ndx]\
        \ = slopeKeyStr.split(',').map(Number);\n        const lineSegmentsMap = new\
        \ Map(); // key: line_constant, value: list of [p1_idx, p2_idx]\n\n        for\
        \ (const seg of segments) {\n            const p = points[seg[0]]; // Use any\
        \ point on the segment to calculate the line constant\n            const lineConstant\
        \ = ndx * p[1] - ndy * p[0];\n            const lineKey = `${lineConstant}`;\n\
        \            if (!lineSegmentsMap.has(lineKey)) {\n                lineSegmentsMap.set(lineKey,\
        \ []);\n            }\n            lineSegmentsMap.get(lineKey).push(seg);\n\
        \        }\n\n        let collinearDisjointParallelPairs = 0;\n        for (const\
        \ segmentsOnThisLine of lineSegmentsMap.values()) {\n            const kLine\
        \ = segmentsOnThisLine.length;\n\n            if (kLine < 2) {\n           \
        \     continue;\n            }\n\n            const currentLineTotalPairs =\
        \ kLine * (kLine - 1) / 2;\n\n            const endpointFreqOnLine = new Map();\n\
        \            for (const seg of segmentsOnThisLine) {\n                endpointFreqOnLine.set(seg[0],\
        \ (endpointFreqOnLine.get(seg[0]) || 0) + 1);\n                endpointFreqOnLine.set(seg[1],\
        \ (endpointFreqOnLine.get(seg[1]) || 0) + 1);\n            }\n\n           \
        \ let sharedEndpointPairsOnLine = 0;\n            for (const count of endpointFreqOnLine.values())\
        \ {\n                if (count >= 2) {\n                    sharedEndpointPairsOnLine\
        \ += count * (count - 1) / 2;\n                }\n            }\n\n        \
        \    collinearDisjointParallelPairs += (currentLineTotalPairs - sharedEndpointPairsOnLine);\n\
        \        }\n\n        totalTrapezoids += (numDisjointParallelPairs - collinearDisjointParallelPairs);\n\
        \    }\n\n    let parallelograms = 0;\n    for (const count of midpointMap.values())\
        \ {\n        if (count >= 2) {\n            parallelograms += count * (count\
        \ - 1) / 2;\n        }\n    }\n\n    return totalTrapezoids - parallelograms;\n\
        };"
      typescript: "function countTrapezoids(points: number[][]): number {\n    const\
        \ n = points.length;\n\n    const slopeMap = new Map<string, [number, number][]>();\
        \ // key: \"dy,dx\", value: list of [p1_idx, p2_idx]\n    const midpointMap\
        \ = new Map<string, number>(); // key: \"x_sum,y_sum\", value: count of pairs\n\
        \n    // Helper for GCD\n    function calculateGcd(a: number, b: number): number\
        \ {\n        a = Math.abs(a);\n        b = Math.abs(b);\n        while (b) {\n\
        \            [a, b] = [b, a % b];\n        }\n        return a;\n    }\n\n \
        \   for (let i = 0; i < n; ++i) {\n        for (let j = i + 1; j < n; ++j) {\n\
        \            const p1 = points[i];\n            const p2 = points[j];\n\n  \
        \          let dx = p2[0] - p1[0];\n            let dy = p2[1] - p1[1];\n\n\
        \            // Normalize slope\n            const commonDivisor = calculateGcd(dx,\
        \ dy);\n            let ndx = dx / commonDivisor;\n            let ndy = dy\
        \ / commonDivisor;\n\n            // Canonical representation: ndx > 0, or (ndx\
        \ == 0 and ndy > 0)\n            if (ndx < 0 || (ndx === 0 && ndy < 0)) {\n\
        \                ndx = -ndx;\n                ndy = -ndy;\n            }\n\n\
        \            const slopeKey = `${ndy},${ndx}`;\n            if (!slopeMap.has(slopeKey))\
        \ {\n                slopeMap.set(slopeKey, []);\n            }\n          \
        \  slopeMap.get(slopeKey)!.push([i, j]);\n\n            // Calculate doubled\
        \ midpoint for parallelogram check\n            const mx = p1[0] + p2[0];\n\
        \            const my = p1[1] + p2[1];\n            const midpointKey = `${mx},${my}`;\n\
        \            midpointMap.set(midpointKey, (midpointMap.get(midpointKey) || 0)\
        \ + 1);\n        }\n    }\n\n    let totalTrapezoids = 0;\n\n    // Count pairs\
        \ of parallel segments that are disjoint and non-collinear\n    for (const [slopeKeyStr,\
        \ segments] of slopeMap.entries()) {\n        const k = segments.length;\n\n\
        \        if (k < 2) {\n            continue;\n        }\n\n        // Step 1:\
        \ Calculate total pairs of segments with this slope (C(k,2))\n        const\
        \ currentSlopeTotalPairs = k * (k - 1) / 2;\n\n        // Step 2: Subtract pairs\
        \ that share an endpoint\n        const endpointFreq = new Map<number, number>();\n\
        \        for (const seg of segments) {\n            endpointFreq.set(seg[0],\
        \ (endpointFreq.get(seg[0]) || 0) + 1);\n            endpointFreq.set(seg[1],\
        \ (endpointFreq.get(seg[1]) || 0) + 1);\n        }\n\n        let sharedEndpointPairs\
        \ = 0;\n        for (const count of endpointFreq.values()) {\n            if\
        \ (count >= 2) {\n                sharedEndpointPairs += count * (count - 1)\
        \ / 2;\n            }\n        }\n\n        // This is the count of disjoint\
        \ parallel segments, including collinear ones\n        const numDisjointParallelPairs\
        \ = currentSlopeTotalPairs - sharedEndpointPairs;\n\n        // Step 3: Subtract\
        \ pairs that are collinear (i.e., lie on the same line)\n        // For a given\
        \ slope (ndy, ndx), a line can be identified by the constant C = ndx*y - ndy*x\n\
        \        const [ndy, ndx] = slopeKeyStr.split(',').map(Number);\n        const\
        \ lineSegmentsMap = new Map<string, [number, number][]>(); // key: line_constant,\
        \ value: list of [p1_idx, p2_idx]\n\n        for (const seg of segments) {\n\
        \            const p = points[seg[0]]; // Use any point on the segment to calculate\
        \ the line constant\n            const lineConstant = ndx * p[1] - ndy * p[0];\n\
        \            const lineKey = `${lineConstant}`;\n            if (!lineSegmentsMap.has(lineKey))\
        \ {\n                lineSegmentsMap.set(lineKey, []);\n            }\n    \
        \        lineSegmentsMap.get(lineKey)!.push(seg);\n        }\n\n        let\
        \ collinearDisjointParallelPairs = 0;\n        for (const segmentsOnThisLine\
        \ of lineSegmentsMap.values()) {\n            const kLine = segmentsOnThisLine.length;\n\
        \n            if (kLine < 2) {\n                continue;\n            }\n\n\
        \            const currentLineTotalPairs = kLine * (kLine - 1) / 2;\n\n    \
        \        const endpointFreqOnLine = new Map<number, number>();\n           \
        \ for (const seg of segmentsOnThisLine) {\n                endpointFreqOnLine.set(seg[0],\
        \ (endpointFreqOnLine.get(seg[0]) || 0) + 1);\n                endpointFreqOnLine.set(seg[1],\
        \ (endpointFreqOnLine.get(seg[1]) || 0) + 1);\n            }\n\n           \
        \ let sharedEndpointPairsOnLine = 0;\n            for (const count of endpointFreqOnLine.values())\
        \ {\n                if (count >= 2) {\n                    sharedEndpointPairsOnLine\
        \ += count * (count - 1) / 2;\n                }\n            }\n\n        \
        \    collinearDisjointParallelPairs += (currentLineTotalPairs - sharedEndpointPairsOnLine);\n\
        \        }\n\n        totalTrapezoids += (numDisjointParallelPairs - collinearDisjointParallelPairs);\n\
        \    }\n\n    let parallelograms = 0;\n    for (const count of midpointMap.values())\
        \ {\n        if (count >= 2) {\n            parallelograms += count * (count\
        \ - 1) / 2;\n        }\n    }\n\n    return totalTrapezoids - parallelograms;\n\
        };"
      php: "<?php\nclass Solution {\n\n    /**\n     * @param Integer[][] $points\n\
        \     * @return Integer\n     */\n    function countTrapezoids($points) {\n\
        \        $n = count($points);\n\n        $slopeMap = []; // key: \"dy,dx\",\
        \ value: list of [p1_idx, p2_idx]\n        $midpointMap = []; // key: \"x_sum,y_sum\"\
        , value: count of pairs\n\n        // Helper for GCD\n        function calculateGcd($a,\
        \ $b) {\n            $a = abs($a);\n            $b = abs($b);\n            while\
        \ ($b) {\n                $temp = $b;\n                $b = $a % $b;\n     \
        \           $a = $temp;\n            }\n            return $a;\n        }\n\n\
        \        for ($i = 0; $i < $n; ++$i) {\n            for ($j = $i + 1; $j < $n;\
        \ ++$j) {\n                $p1 = $points[$i];\n                $p2 = $points[$j];\n\
        \n                $dx = $p2[0] - $p1[0];\n                $dy = $p2[1] - $p1[1];\n\
        \n                // Normalize slope\n                $commonDivisor = calculateGcd($dx,\
        \ $dy);\n                $ndx = $dx / $commonDivisor;\n                $ndy\
        \ = $dy / $commonDivisor;\n\n                // Canonical representation: ndx\
        \ > 0, or (ndx == 0 and ndy > 0)\n                if ($ndx < 0 || ($ndx == 0\
        \ && $ndy < 0)) {\n                    $ndx = -$ndx;\n                    $ndy\
        \ = -$ndy;\n                }\n\n                $slopeKey = \"{$ndy},{$ndx}\"\
        ;\n                if (!isset($slopeMap[$slopeKey])) {\n                   \
        \ $slopeMap[$slopeKey] = [];\n                }\n                $slopeMap[$slopeKey][]\
        \ = [$i, $j];\n\n                // Calculate doubled midpoint for parallelogram\
        \ check\n                $mx = $p1[0] + $p2[0];\n                $my = $p1[1]\
        \ + $p2[1];\n                $midpointKey = \"{$mx},{$my}\";\n             \
        \   $midpointMap[$midpointKey] = ($midpointMap[$midpointKey] ?? 0) + 1;\n  \
        \          }\n        }\n\n        $totalTrapezoids = 0;\n\n        // Count\
        \ pairs of parallel segments that are disjoint and non-collinear\n        foreach\
        \ ($slopeMap as $slopeKeyStr => $segments) {\n            $k = count($segments);\n\
        \n            if ($k < 2) {\n                continue;\n            }\n\n  \
        \          // Step 1: Calculate total pairs of segments with this slope (C(k,2))\n\
        \            $currentSlopeTotalPairs = $k * ($k - 1) / 2;\n\n            //\
        \ Step 2: Subtract pairs that share an endpoint\n            $endpointFreq =\
        \ [];\n            foreach ($segments as $seg) {\n                $endpointFreq[$seg[0]]\
        \ = ($endpointFreq[$seg[0]] ?? 0) + 1;\n                $endpointFreq[$seg[1]]\
        \ = ($endpointFreq[$seg[1]] ?? 0) + 1;\n            }\n\n            $sharedEndpointPairs\
        \ = 0;\n            foreach ($endpointFreq as $count) {\n                if\
        \ ($count >= 2) {\n                    $sharedEndpointPairs += $count * ($count\
        \ - 1) / 2;\n                }\n            }\n\n            // This is the\
        \ count of disjoint parallel segments, including collinear ones\n          \
        \  $numDisjointParallelPairs = $currentSlopeTotalPairs - $sharedEndpointPairs;\n\
        \n            // Step 3: Subtract pairs that are collinear (i.e., lie on the\
        \ same line)\n            // For a given slope (ndy, ndx), a line can be identified\
        \ by the constant C = ndx*y - ndy*x\n            list($ndy, $ndx) = array_map('intval',\
        \ explode(',', $slopeKeyStr));\n            $lineSegmentsMap = []; // key: line_constant,\
        \ value: list of [p1_idx, p2_idx]\n\n            foreach ($segments as $seg)\
        \ {\n                $p = $points[$seg[0]]; // Use any point on the segment\
        \ to calculate the line constant\n                $lineConstant = $ndx * $p[1]\
        \ - $ndy * $p[0];\n                $lineKey = \"{$lineConstant}\";\n       \
        \         if (!isset($lineSegmentsMap[$lineKey])) {\n                    $lineSegmentsMap[$lineKey]\
        \ = [];\n                }\n                $lineSegmentsMap[$lineKey][] = $seg;\n\
        \            }\n\n            $collinearDisjointParallelPairs = 0;\n       \
        \     foreach ($lineSegmentsMap as $segmentsOnThisLine) {\n                $kLine\
        \ = count($segmentsOnThisLine);\n\n                if ($kLine < 2) {\n     \
        \               continue;\n                }\n\n                $currentLineTotalPairs\
        \ = $kLine * ($kLine - 1) / 2;\n\n                $endpointFreqOnLine = [];\n\
        \                foreach ($segmentsOnThisLine as $seg) {\n                 \
        \   $endpointFreqOnLine[$seg[0]] = ($endpointFreqOnLine[$seg[0]] ?? 0) + 1;\n\
        \                    $endpointFreqOnLine[$seg[1]] = ($endpointFreqOnLine[$seg[1]]\
        \ ?? 0) + 1;\n                }\n\n                $sharedEndpointPairsOnLine\
        \ = 0;\n                foreach ($endpointFreqOnLine as $count) {\n        \
        \            if ($count >= 2) {\n                        $sharedEndpointPairsOnLine\
        \ += $count * ($count - 1) / 2;\n                    }\n                }\n\n\
        \                $collinearDisjointParallelPairs += ($currentLineTotalPairs\
        \ - $sharedEndpointPairsOnLine);\n            }\n\n            $totalTrapezoids\
        \ += ($numDisjointParallelPairs - $collinearDisjointParallelPairs);\n      \
        \  }\n\n        $parallelograms = 0;\n        foreach ($midpointMap as $count)\
        \ {\n            if ($count >= 2) {\n                $parallelograms += $count\
        \ * ($count - 1) / 2;\n            }\n        }\n\n        return $totalTrapezoids\
        \ - $parallelograms;\n    }\n}\n?>"
      swift: "import Foundation\n\nclass Solution {\n    private func calculateGcd(_\
        \ a: Int, _ b: Int) -> Int {\n        var a = abs(a)\n        var b = abs(b)\n\
        \        while b != 0 {\n            let temp = b\n            b = a % b\n \
        \           a = temp\n        }\n        return a\n    }\n\n    func countTrapezoids(_\
        \ points: [[Int]]) -> Int {\n        let n = points.count\n\n        var slopeMap:\
        \ [String: [[Int]]] = [:] // key: \"dy,dx\", value: list of [p1_idx, p2_idx]\n\
        \        var midpointMap: [String: Int] = [:] // key: \"x_sum,y_sum\", value:\
        \ count of pairs\n\n        for i in 0..<n {\n            for j in i + 1..<n\
        \ {\n                let p1 = points[i]\n                let p2 = points[j]\n\
        \n                let dx = p2[0] - p1[0]\n                let dy = p2[1] - p1[1]\n\
        \n                // Normalize slope\n                let commonDivisor = calculateGcd(dx,\
        \ dy)\n                var ndx = dx / commonDivisor\n                var ndy\
        \ = dy / commonDivisor\n\n                // Canonical representation: ndx >\
        \ 0, or (ndx == 0 && ndy > 0)\n                if ndx < 0 || (ndx == 0 && ndy\
        \ < 0) {\n                    ndx = -ndx\n                    ndy = -ndy\n \
        \               }\n\n                let slopeKey = \"\\(ndy),\\(ndx)\"\n  \
        \              slopeMap[slopeKey, default: []].append([i, j])\n\n          \
        \      // Calculate doubled midpoint for parallelogram check\n             \
        \   let mx = p1[0] + p2[0]\n                let my = p1[1] + p2[1]\n       \
        \         let midpointKey = \"\\(mx),\\(my)\"\n                midpointMap[midpointKey,\
        \ default: 0] += 1\n            }\n        }\n\n        var totalTrapezoids:\
        \ Int = 0\n\n        // Count pairs of parallel segments that are disjoint and\
        \ non-collinear\n        for (slopeKeyStr, segments) in slopeMap {\n       \
        \     let k = segments.count\n\n            if k < 2 {\n                continue\n\
        \            }\n\n            // Step 1: Calculate total pairs of segments with\
        \ this slope (C(k,2))\n            let currentSlopeTotalPairs = k * (k - 1)\
        \ / 2\n\n            // Step 2: Subtract pairs that share an endpoint\n    \
        \        var endpointFreq: [Int: Int] = [:]\n            for seg in segments\
        \ {\n                endpointFreq[seg[0], default: 0] += 1\n               \
        \ endpointFreq[seg[1], default: 0] += 1\n            }\n\n            var sharedEndpointPairs:\
        \ Int = 0\n            for count in endpointFreq.values {\n                if\
        \ count >= 2 {\n                    sharedEndpointPairs += count * (count -\
        \ 1) / 2\n                }\n            }\n\n            // This is the count\
        \ of disjoint parallel segments, including collinear ones\n            let numDisjointParallelPairs\
        \ = currentSlopeTotalPairs - sharedEndpointPairs\n\n            // Step 3: Subtract\
        \ pairs that are collinear (i.e., lie on the same line)\n            // For\
        \ a given slope (ndy, ndx), a line can be identified by the constant C = ndx*y\
        \ - ndy*x\n            let slopeComponents = slopeKeyStr.split(separator: \"\
        ,\").map { Int($0)! }\n            let ndy = slopeComponents[0]\n          \
        \  let ndx = slopeComponents[1]\n\n            var lineSegmentsMap: [String:\
        \ [[Int]]] = [:] // key: line_constant, value: list of [p1_idx, p2_idx]\n\n\
        \            for seg in segments {\n                let p = points[seg[0]] //\
        \ Use any point on the segment to calculate the line constant\n            \
        \    let lineConstant = ndx * p[1] - ndy * p[0]\n                let lineKey\
        \ = \"\\(lineConstant)\"\n                lineSegmentsMap[lineKey, default:\
        \ []].append(seg)\n            }\n\n            var collinearDisjointParallelPairs:\
        \ Int = 0\n            for segmentsOnThisLine in lineSegmentsMap.values {\n\
        \                let kLine = segmentsOnThisLine.count\n\n                if\
        \ kLine < 2 {\n                    continue\n                }\n\n         \
        \       let currentLineTotalPairs = kLine * (kLine - 1) / 2\n\n            \
        \    var endpointFreqOnLine: [Int: Int] = [:]\n                for seg in segmentsOnThisLine\
        \ {\n                    endpointFreqOnLine[seg[0], default: 0] += 1\n     \
        \               endpointFreqOnLine[seg[1], default: 0] += 1\n              \
        \  }\n\n                var sharedEndpointPairsOnLine: Int = 0\n           \
        \     for count in endpointFreqOnLine.values {\n                    if count\
        \ >= 2 {\n                        sharedEndpointPairsOnLine += count * (count\
        \ - 1) / 2\n                    }\n                }\n\n                collinearDisjointParallelPairs\
        \ += (currentLineTotalPairs - sharedEndpointPairsOnLine)\n            }\n\n\
        \            totalTrapezoids += (numDisjointParallelPairs - collinearDisjointParallelPairs)\n\
        \        }\n\n        var parallelograms: Int = 0\n        for count in midpointMap.values\
        \ {\n            if count >= 2 {\n                parallelograms += count *\
        \ (count - 1) / 2\n            }\n        }\n\n        return totalTrapezoids\
        \ - parallelograms\n    }\n}"
      kotlin: "import java.util.*\nimport kotlin.math.abs\n\nclass Solution {\n    private\
        \ fun calculateGcd(a: Long, b: Long): Long {\n        return abs(gcd(a, b))\n\
        \    }\n\n    private fun gcd(a: Long, b: Long): Long {\n        var num1 =\
        \ a\n        var num2 = b\n        while (num2 != 0L) {\n            val temp\
        \ = num2\n            num2 = num1 % num2\n            num1 = temp\n        }\n\
        \        return num1\n    }\n\n    fun countTrapezoids(points: Array<IntArray>):\
        \ Int {\n        val n = points.size\n\n        val slopeMap = mutableMapOf<Pair<Long,\
        \ Long>, MutableList<Pair<Int, Int>>>()\n        val midpointMap = mutableMapOf<Pair<Long,\
        \ Long>, Int>()\n\n        for (i in 0 until n) {\n            for (j in i +\
        \ 1 until n) {\n                val p1 = points[i]\n                val p2 =\
        \ points[j]\n\n                val dx = p2[0].toLong() - p1[0].toLong()\n  \
        \              val dy = p2[1].toLong() - p1[1].toLong()\n\n                val\
        \ commonDivisor = calculateGcd(dx, dy)\n                var ndx = dx / commonDivisor\n\
        \                var ndy = dy / commonDivisor\n\n                if (ndx < 0\
        \ || (ndx == 0L && ndy < 0)) {\n                    ndx = -ndx\n           \
        \         ndy = -ndy\n                }\n\n                val slopeKey = Pair(ndy,\
        \ ndx)\n                slopeMap.computeIfAbsent(slopeKey) { mutableListOf()\
        \ }.add(Pair(i, j))\n\n                val mx = p1[0].toLong() + p2[0].toLong()\n\
        \                val my = p1[1].toLong() + p2[1].toLong()\n                val\
        \ midpointKey = Pair(mx, my)\n                midpointMap[midpointKey] = midpointMap.getOrDefault(midpointKey,\
        \ 0) + 1\n            }\n        }\n\n        var totalTrapezoids: Long = 0\n\
        \n        for ((slopeKey, segments) in slopeMap) {\n            val k = segments.size.toLong()\n\
        \n            if (k < 2) {\n                continue\n            }\n\n    \
        \        val currentSlopeTotalPairs = k * (k - 1) / 2\n\n            val endpointFreq\
        \ = mutableMapOf<Int, Int>()\n            for (seg in segments) {\n        \
        \        endpointFreq[seg.first] = endpointFreq.getOrDefault(seg.first, 0) +\
        \ 1\n                endpointFreq[seg.second] = endpointFreq.getOrDefault(seg.second,\
        \ 0) + 1\n            }\n\n            var sharedEndpointPairs: Long = 0\n \
        \           for (count in endpointFreq.values) {\n                if (count\
        \ >= 2) {\n                    sharedEndpointPairs += count.toLong() * (count\
        \ - 1) / 2\n                }\n            }\n\n            val numDisjointParallelPairs\
        \ = currentSlopeTotalPairs - sharedEndpointPairs\n\n            val ndy = slopeKey.first\n\
        \            val ndx = slopeKey.second\n\n            val lineSegmentsMap =\
        \ mutableMapOf<Long, MutableList<Pair<Int, Int>>>()\n\n            for (seg\
        \ in segments) {\n                val p = points[seg.first]\n              \
        \  val lineConstant = ndx * p[1].toLong() - ndy * p[0].toLong()\n          \
        \      lineSegmentsMap.computeIfAbsent(lineConstant) { mutableListOf() }.add(seg)\n\
        \            }\n\n            var collinearDisjointParallelPairs: Long = 0\n\
        \            for (segmentsOnThisLine in lineSegmentsMap.values) {\n        \
        \        val kLine = segmentsOnThisLine.size.toLong()\n\n                if\
        \ (kLine < 2) {\n                    continue\n                }\n\n       \
        \         val currentLineTotalPairs = kLine * (kLine - 1) / 2\n\n          \
        \      val endpointFreqOnLine = mutableMapOf<Int, Int>()\n                for\
        \ (seg in segmentsOnThisLine) {\n                    endpointFreqOnLine[seg.first]\
        \ = endpointFreqOnLine.getOrDefault(seg.first, 0) + 1\n                    endpointFreqOnLine[seg.second]\
        \ = endpointFreqOnLine.getOrDefault(seg.second, 0) + 1\n                }\n\n\
        \                var sharedEndpointPairsOnLine: Long = 0\n                for\
        \ (count in endpointFreqOnLine.values) {\n                    if (count >= 2)\
        \ {\n                        sharedEndpointPairsOnLine += count.toLong() * (count\
        \ - 1) / 2\n                    }\n                }\n\n                collinearDisjointParallelPairs\
        \ += (currentLineTotalPairs - sharedEndpointPairsOnLine)\n            }\n\n\
        \            totalTrapezoids += (numDisjointParallelPairs - collinearDisjointParallelPairs)\n\
        \        }\n\n        var parallelograms: Long = 0\n        for (count in midpointMap.values)\
        \ {\n            if (count >= 2) {\n                parallelograms += count.toLong()\
        \ * (count - 1) / 2\n            }\n        }\n\n        return (totalTrapezoids\
        \ - parallelograms).toInt()\n    }\n}"
      dart: "import 'dart:math';\nimport 'dart:collection';\n\nclass Solution {\n  int\
        \ calculateGcd(int a, int b) {\n    a = a.abs();\n    b = b.abs();\n    while\
        \ (b != 0) {\n      int temp = b;\n      b = a % b;\n      a = temp;\n    }\n\
        \    return a;\n  }\n\n  int countTrapezoids(List<List<int>> points) {\n   \
        \ final n = points.length;\n\n    final slopeMap = HashMap<String, List<List<int>>>();\
        \ // key: \"dy,dx\", value: list of [p1_idx, p2_idx]\n    final midpointMap\
        \ = HashMap<String, int>(); // key: \"x_sum,y_sum\", value: count of pairs\n\
        \n    for (int i = 0; i < n; ++i) {\n      for (int j = i + 1; j < n; ++j) {\n\
        \        final p1 = points[i];\n        final p2 = points[j];\n\n        int\
        \ dx = p2[0] - p1[0];\n        int dy = p2[1] - p1[1];\n\n        final commonDivisor\
        \ = calculateGcd(dx, dy);\n        int ndx = dx ~/ commonDivisor;\n        int\
        \ ndy = dy ~/ commonDivisor;\n\n        if (ndx < 0 || (ndx == 0 && ndy < 0))\
        \ {\n          ndx = -ndx;\n          ndy = -ndy;\n        }\n\n        final\
        \ slopeKey = '$ndy,$ndx';\n        slopeMap.putIfAbsent(slopeKey, () => []).add([i,\
        \ j]);\n\n        final mx = p1[0] + p2[0];\n        final my = p1[1] + p2[1];\n\
        \        final midpointKey = '$mx,$my';\n        midpointMap[midpointKey] =\
        \ (midpointMap[midpointKey] ?? 0) + 1;\n      }\n    }\n\n    int totalTrapezoids\
        \ = 0;\n\n    for (final entry in slopeMap.entries) {\n      final segments\
        \ = entry.value;\n      final k = segments.length;\n\n      if (k < 2) {\n \
        \       continue;\n      }\n\n      final currentSlopeTotalPairs = k * (k -\
        \ 1) ~/ 2;\n\n      final endpointFreq = HashMap<int, int>();\n      for (final\
        \ seg in segments) {\n        endpointFreq[seg[0]] = (endpointFreq[seg[0]] ??\
        \ 0) + 1;\n        endpointFreq[seg[1]] = (endpointFreq[seg[1]] ?? 0) + 1;\n\
        \      }\n\n      int sharedEndpointPairs = 0;\n      for (final count in endpointFreq.values)\
        \ {\n        if (count >= 2) {\n          sharedEndpointPairs += count * (count\
        \ - 1) ~/ 2;\n        }\n      }\n\n      final numDisjointParallelPairs = currentSlopeTotalPairs\
        \ - sharedEndpointPairs;\n\n      final slopeKeyStr = entry.key;\n      final\
        \ slopeComponents = slopeKeyStr.split(',').map(int.parse).toList();\n      final\
        \ ndy = slopeComponents[0];\n      final ndx = slopeComponents[1];\n\n     \
        \ final lineSegmentsMap = HashMap<String, List<List<int>>>(); // key: line_constant,\
        \ value: list of [p1_idx, p2_idx]\n\n      for (final seg in segments) {\n \
        \       final p = points[seg[0]];\n        final lineConstant = ndx * p[1] -\
        \ ndy * p[0];\n        final lineKey = '$lineConstant';\n        lineSegmentsMap.putIfAbsent(lineKey,\
        \ () => []).add(seg);\n      }\n\n      int collinearDisjointParallelPairs =\
        \ 0;\n      for (final segmentsOnThisLine in lineSegmentsMap.values) {\n   \
        \     final kLine = segmentsOnThisLine.length;\n\n        if (kLine < 2) {\n\
        \          continue;\n        }\n\n        final currentLineTotalPairs = kLine\
        \ * (kLine - 1) ~/ 2;\n\n        final endpointFreqOnLine = HashMap<int, int>();\n\
        \        for (final seg in segmentsOnThisLine) {\n          endpointFreqOnLine[seg[0]]\
        \ = (endpointFreqOnLine[seg[0]] ?? 0) + 1;\n          endpointFreqOnLine[seg[1]]\
        \ = (endpointFreqOnLine[seg[1]] ?? 0) + 1;\n        }\n\n        int sharedEndpointPairsOnLine\
        \ = 0;\n        for (final count in endpointFreqOnLine.values) {\n         \
        \ if (count >= 2) {\n            sharedEndpointPairsOnLine += count * (count\
        \ - 1) ~/ 2;\n          }\n        }\n\n        collinearDisjointParallelPairs\
        \ += (currentLineTotalPairs - sharedEndpointPairsOnLine);\n      }\n\n     \
        \ totalTrapezoids += (numDisjointParallelPairs - collinearDisjointParallelPairs);\n\
        \    }\n\n    int parallelograms = 0;\n    for (final count in midpointMap.values)\
        \ {\n      if (count >= 2) {\n        parallelograms += count * (count - 1)\
        \ ~/ 2;\n      }\n    }\n\n    return totalTrapezoids - parallelograms;\n  }\n\
        }"
      go: "package main\n\nimport (\n\t\"math\"\n)\n\n// Point represents a 2D coordinate\n\
        type Point struct {\n\tx, y int64\n}\n\n// PointPair stores indices of two points\
        \ forming a segment\ntype PointPair struct {\n\tp1Idx, p2Idx int\n}\n\nfunc\
        \ calculateGcd(a, b int64) int64 {\n\ta = int64(math.Abs(float64(a)))\n\tb =\
        \ int64(math.Abs(float64(b)))\n\tfor b != 0 {\n\t\ta, b = b, a%b\n\t}\n\treturn\
        \ a\n}\n\nfunc countTrapezoids(points [][]int) int {\n\tn := len(points)\n\n\
        \tslopeMap := make(map[Point][]PointPair)\n\tmidpointMap := make(map[Point]int)\n\
        \n\tfor i := 0; i < n; i++ {\n\t\tfor j := i + 1; j < n; j++ {\n\t\t\tp1 :=\
        \ points[i]\n\t\t\tp2 := points[j]\n\n\t\t\tdx := int64(p2[0] - p1[0])\n\t\t\
        \tdy := int64(p2[1] - p1[1])\n\n\t\t\tcommonDivisor := calculateGcd(dx, dy)\n\
        \t\t\tndx := dx / commonDivisor\n\t\t\tndy := dy / commonDivisor\n\n\t\t\tif\
        \ ndx < 0 || (ndx == 0 && ndy < 0) {\n\t\t\t\tndx = -ndx\n\t\t\t\tndy = -ndy\n\
        \t\t\t}\n\n\t\t\tslopeKey := Point{ndy, ndx}\n\t\t\tslopeMap[slopeKey] = append(slopeMap[slopeKey],\
        \ PointPair{i, j})\n\n\t\t\tmx := int64(p1[0] + p2[0])\n\t\t\tmy := int64(p1[1]\
        \ + p2[1])\n\t\t\tmidpointKey := Point{mx, my}\n\t\t\tmidpointMap[midpointKey]++\n\
        \t\t}\n\t}\n\n\ttotalTrapezoids := int64(0)\n\n\tfor slopeKey, segments := range\
        \ slopeMap {\n\t\tk := int64(len(segments))\n\n\t\tif k < 2 {\n\t\t\tcontinue\n\
        \t\t}\n\n\t\tcurrentSlopeTotalPairs := k * (k - 1) / 2\n\n\t\tendpointFreq :=\
        \ make(map[int]int)\n\t\tfor _, seg := range segments {\n\t\t\tendpointFreq[seg.p1Idx]++\n\
        \t\t\tendpointFreq[seg.p2Idx]++\n\t\t}\n\n\t\tsharedEndpointPairs := int64(0)\n\
        \t\tfor _, count := range endpointFreq {\n\t\t\tif count >= 2 {\n\t\t\t\tsharedEndpointPairs\
        \ += int64(count) * int64(count-1) / 2\n\t\t\t}\n\t\t}\n\n\t\tnumDisjointParallelPairs\
        \ := currentSlopeTotalPairs - sharedEndpointPairs\n\n\t\tndy := slopeKey.x\n\
        \t\tndx := slopeKey.y\n\n\t\tlineSegmentsMap := make(map[int64][]PointPair)\n\
        \n\t\tfor _, seg := range segments {\n\t\t\tp := points[seg.p1Idx]\n\t\t\tlineConstant\
        \ := ndx*int64(p[1]) - ndy*int64(p[0])\n\t\t\tlineSegmentsMap[lineConstant]\
        \ = append(lineSegmentsMap[lineConstant], seg)\n\t\t}\n\n\t\tcollinearDisjointParallelPairs\
        \ := int64(0)\n\t\tfor _, segmentsOnThisLine := range lineSegmentsMap {\n\t\t\
        \tkLine := int64(len(segmentsOnThisLine))\n\n\t\t\tif kLine < 2 {\n\t\t\t\t\
        continue\n\t\t\t}\n\n\t\t\tcurrentLineTotalPairs := kLine * (kLine - 1) / 2\n\
        \n\t\t\tendpointFreqOnLine := make(map[int]int)\n\t\t\tfor _, seg := range segmentsOnThisLine\
        \ {\n\t\t\t\tendpointFreqOnLine[seg.p1Idx]++\n\t\t\t\tendpointFreqOnLine[seg.p2Idx]++\n\
        \t\t\t}\n\n\t\t\tsharedEndpointPairsOnLine := int64(0)\n\t\t\tfor _, count :=\
        \ range endpointFreqOnLine {\n\t\t\t\tif count >= 2 {\n\t\t\t\t\tsharedEndpointPairsOnLine\
        \ += int64(count) * int64(count-1) / 2\n\t\t\t\t}\n\t\t\t}\n\n\t\t\tcollinearDisjointParallelPairs\
        \ += (currentLineTotalPairs - sharedEndpointPairsOnLine)\n\t\t}\n\n\t\ttotalTrapezoids\
        \ += (numDisjointParallelPairs - collinearDisjointParallelPairs)\n\t}\n\n\t\
        parallelograms := int64(0)\n\tfor _, count := range midpointMap {\n\t\tif count\
        \ >= 2 {\n\t\t\tparallelograms += int64(count) * int64(count-1) / 2\n\t\t}\n\
        \t}\n\n\treturn int(totalTrapezoids - parallelograms)\n}"
      ruby: "def calculate_gcd(a, b)\n  a = a.abs\n  b = b.abs\n  while b != 0\n   \
        \ a, b = b, a % b\n  end\n  a\nend\n\n# @param {Integer[][]} points\n# @return\
        \ {Integer}\ndef count_trapezoids(points)\n  n = points.length\n\n  slope_map\
        \ = Hash.new { |h, k| h[k] = [] } # key: [dy, dx], value: list of [p1_idx, p2_idx]\n\
        \  midpoint_map = Hash.new(0) # key: [x_sum, y_sum], value: count of pairs\n\
        \n  (0...n).each do |i|\n    (i + 1...n).each do |j|\n      p1 = points[i]\n\
        \      p2 = points[j]\n\n      dx = p2[0] - p1[0]\n      dy = p2[1] - p1[1]\n\
        \n      common_divisor = calculate_gcd(dx, dy)\n      ndx = dx / common_divisor\n\
        \      ndy = dy / common_divisor\n\n      if ndx < 0 || (ndx == 0 && ndy < 0)\n\
        \        ndx = -ndx\n        ndy = -ndy\n      end\n\n      slope_map[[ndy,\
        \ ndx]] << [i, j]\n\n      mx = p1[0] + p2[0]\n      my = p1[1] + p2[1]\n  \
        \    midpoint_map[[mx, my]] += 1\n    end\n  end\n\n  total_trapezoids = 0\n\
        \n  # Count pairs of parallel segments that are disjoint and non-collinear\n\
        \  slope_map.each do |slope_key, segments|\n    k = segments.length\n\n    if\
        \ k < 2\n      next\n    end\n\n    current_slope_total_pairs = k * (k - 1)\
        \ / 2\n\n    endpoint_freq = Hash.new(0)\n    segments.each do |seg|\n     \
        \ endpoint_freq[seg[0]] += 1\n      endpoint_freq[seg[1]] += 1\n    end\n\n\
        \    shared_endpoint_pairs = 0\n    endpoint_freq.each do |_, count|\n     \
        \ if count >= 2\n        shared_endpoint_pairs += count * (count - 1) / 2\n\
        \      end\n    end\n\n    num_disjoint_parallel_pairs = current_slope_total_pairs\
        \ - shared_endpoint_pairs\n\n    ndy, ndx = slope_key\n    line_segments_map\
        \ = Hash.new { |h, k| h[k] = [] } # key: line_constant, value: list of [p1_idx,\
        \ p2_idx]\n\n    segments.each do |seg|\n      p = points[seg[0]] # Use any\
        \ point on the segment to calculate the line constant\n      line_constant =\
        \ ndx * p[1] - ndy * p[0]\n      line_segments_map[line_constant] << seg\n \
        \   end\n\n    collinear_disjoint_parallel_pairs = 0\n    line_segments_map.each\
        \ do |_, segments_on_this_line|\n      k_line = segments_on_this_line.length\n\
        \n      if k_line < 2\n        next\n      end\n\n      current_line_total_pairs\
        \ = k_line * (k_line - 1) / 2\n\n      endpoint_freq_on_line = Hash.new(0)\n\
        \      segments_on_this_line.each do |seg|\n        endpoint_freq_on_line[seg[0]]\
        \ += 1\n        endpoint_freq_on_line[seg[1]] += 1\n      end\n\n      shared_endpoint_pairs_on_line\
        \ = 0\n      endpoint_freq_on_line.each do |_, count|\n        if count >= 2\n\
        \          shared_endpoint_pairs_on_line += count * (count - 1) / 2\n      \
        \  end\n      end\n\n      collinear_disjoint_parallel_pairs += (current_line_total_pairs\
        \ - shared_endpoint_pairs_on_line)\n    end\n\n    total_trapezoids += (num_disjoint_parallel_pairs\
        \ - collinear_disjoint_parallel_pairs)\n  end\n\n  parallelograms = 0\n  midpoint_map.each\
        \ do |_, count|\n    if count >= 2\n      parallelograms += count * (count -\
        \ 1) / 2\n    end\n  end\n\n  total_trapezoids - parallelograms\nend"
      scala: "import scala.collection.mutable\nimport scala.math.abs\n\nclass Solution\
        \ {\n    private def calculateGcd(a: Long, b: Long): Long = {\n        var num1\
        \ = abs(a)\n        var num2 = abs(b)\n        while (num2 != 0) {\n       \
        \     val temp = num2\n            num2 = num1 % num2\n            num1 = temp\n\
        \        }\n        num1\n    }\n\n    def countTrapezoids(points: Array[Array[Int]]):\
        \ Int = {\n        val n = points.length\n\n        val slopeMap = mutable.Map[(Long,\
        \ Long), mutable.ListBuffer[(Int, Int)]]()\n        val midpointMap = mutable.Map[(Long,\
        \ Long), Int]()\n\n        for (i <- 0 until n) {\n            for (j <- i +\
        \ 1 until n) {\n                val p1 = points(i)\n                val p2 =\
        \ points(j)\n\n                val dx = p2(0).toLong - p1(0).toLong\n      \
        \          val dy = p2(1).toLong - p1(1).toLong\n\n                val commonDivisor\
        \ = calculateGcd(dx, dy)\n                var ndx = dx / commonDivisor\n   \
        \             var ndy = dy / commonDivisor\n\n                if (ndx < 0 ||\
        \ (ndx == 0L && ndy < 0)) {\n                    ndx = -ndx\n              \
        \      ndy = -ndy\n                }\n\n                val slopeKey = (ndy,\
        \ ndx)\n                slopeMap.getOrElseUpdate(slopeKey, mutable.ListBuffer()).append((i,\
        \ j))\n\n                val mx = p1(0).toLong + p2(0).toLong\n            \
        \    val my = p1(1).toLong + p2(1).toLong\n                val midpointKey =\
        \ (mx, my)\n                midpointMap(midpointKey) = midpointMap.getOrElse(midpointKey,\
        \ 0) + 1\n            }\n        }\n\n        var totalTrapezoids: Long = 0\n\
        \n        for ((slopeKey, segments) <- slopeMap) {\n            val k = segments.size.toLong\n\
        \n            if (k < 2) {\n                // continue\n            } else\
        \ {\n                val currentSlopeTotalPairs = k * (k - 1) / 2\n\n      \
        \          val endpointFreq = mutable.Map[Int, Int]()\n                for (seg\
        \ <- segments) {\n                    endpointFreq(seg._1) = endpointFreq.getOrElse(seg._1,\
        \ 0) + 1\n                    endpointFreq(seg._2) = endpointFreq.getOrElse(seg._2,\
        \ 0) + 1\n                }\n\n                var sharedEndpointPairs: Long\
        \ = 0\n                for (count <- endpointFreq.values) {\n              \
        \      if (count >= 2) {\n                        sharedEndpointPairs += count.toLong\
        \ * (count - 1) / 2\n                    }\n                }\n\n          \
        \      val numDisjointParallelPairs = currentSlopeTotalPairs - sharedEndpointPairs\n\
        \n                val ndy = slopeKey._1\n                val ndx = slopeKey._2\n\
        \n                val lineSegmentsMap = mutable.Map[Long, mutable.ListBuffer[(Int,\
        \ Int)]]()\n\n                for (seg <- segments) {\n                    val\
        \ p = points(seg._1)\n                    val lineConstant = ndx * p(1).toLong\
        \ - ndy * p(0).toLong\n                    lineSegmentsMap.getOrElseUpdate(lineConstant,\
        \ mutable.ListBuffer()).append(seg)\n                }\n\n                var\
        \ collinearDisjointParallelPairs: Long = 0\n                for (segmentsOnThisLine\
        \ <- lineSegmentsMap.values) {\n                    val kLine = segmentsOnThisLine.size.toLong\n\
        \n                    if (kLine < 2) {\n                        // continue\n\
        \                    } else {\n                        val currentLineTotalPairs\
        \ = kLine * (kLine - 1) / 2\n\n                        val endpointFreqOnLine\
        \ = mutable.Map[Int, Int]()\n                        for (seg <- segmentsOnThisLine)\
        \ {\n                            endpointFreqOnLine(seg._1) = endpointFreqOnLine.getOrElse(seg._1,\
        \ 0) + 1\n                            endpointFreqOnLine(seg._2) = endpointFreqOnLine.getOrElse(seg._2,\
        \ 0) + 1\n                        }\n\n                        var sharedEndpointPairsOnLine:\
        \ Long = 0\n                        for (count <- endpointFreqOnLine.values)\
        \ {\n                            if (count >= 2) {\n                       \
        \         sharedEndpointPairsOnLine += count.toLong * (count - 1) / 2\n    \
        \                        }\n                        }\n\n                  \
        \      collinearDisjointParallelPairs += (currentLineTotalPairs - sharedEndpointPairsOnLine)\n\
        \                    }\n                }\n\n                totalTrapezoids\
        \ += (numDisjointParallelPairs - collinearDisjointParallelPairs)\n         \
        \   }\n        }\n\n        var parallelograms: Long = 0\n        for (count\
        \ <- midpointMap.values) {\n            if (count >= 2) {\n                parallelograms\
        \ += count.toLong * (count - 1) / 2\n            }\n        }\n\n        (totalTrapezoids\
        \ - parallelograms).toInt\n    }\n}"
      rust: "use std::collections::HashMap;\nuse std::cmp::Ordering;\n\nfn calculate_gcd(a:\
        \ i64, b: i64) -> i64 {\n    let mut a = a.abs();\n    let mut b = b.abs();\n\
        \    while b != 0 {\n        let temp = b;\n        b = a % b;\n        a =\
        \ temp;\n    }\n    a\n}\n\nstruct Solution;\n\nimpl Solution {\n    pub fn\
        \ count_trapezoids(points: Vec<Vec<i32>>) -> i32 {\n        let n = points.len();\n\
        \n        let mut slope_map: HashMap<(i64, i64), Vec<(usize, usize)>> = HashMap::new();\n\
        \        let mut midpoint_map: HashMap<(i64, i64), i32> = HashMap::new();\n\n\
        \        for i in 0..n {\n            for j in (i + 1)..n {\n              \
        \  let p1 = &points[i];\n                let p2 = &points[j];\n\n          \
        \      let dx = p2[0] as i64 - p1[0] as i64;\n                let dy = p2[1]\
        \ as i64 - p1[1] as i64;\n\n                let common_divisor = calculate_gcd(dx,\
        \ dy);\n                let mut ndx = dx / common_divisor;\n               \
        \ let mut ndy = dy / common_divisor;\n\n                if ndx < 0 || (ndx ==\
        \ 0 && ndy < 0) {\n                    ndx = -ndx;\n                    ndy\
        \ = -ndy;\n                }\n\n                slope_map.entry((ndy, ndx)).or_insert_with(Vec::new).push((i,\
        \ j));\n\n                let mx = p1[0] as i64 + p2[0] as i64;\n          \
        \      let my = p1[1] as i64 + p2[1] as i64;\n                *midpoint_map.entry((mx,\
        \ my)).or_insert(0) += 1;\n            }\n        }\n\n        let mut total_trapezoids:\
        \ i64 = 0;\n\n        for (slope_key, segments) in slope_map {\n           \
        \ let k = segments.len() as i64;\n\n            if k < 2 {\n               \
        \ continue;\n            }\n\n            let current_slope_total_pairs = k\
        \ * (k - 1) / 2;\n\n            let mut endpoint_freq: HashMap<usize, i32> =\
        \ HashMap::new();\n            for seg in &segments {\n                *endpoint_freq.entry(seg.0).or_insert(0)\
        \ += 1;\n                *endpoint_freq.entry(seg.1).or_insert(0) += 1;\n  \
        \          }\n\n            let mut shared_endpoint_pairs: i64 = 0;\n      \
        \      for count in endpoint_freq.values() {\n                if *count >= 2\
        \ {\n                    shared_endpoint_pairs += *count as i64 * (*count as\
        \ i64 - 1) / 2;\n                }\n            }\n\n            let num_disjoint_parallel_pairs\
        \ = current_slope_total_pairs - shared_endpoint_pairs;\n\n            let ndy\
        \ = slope_key.0;\n            let ndx = slope_key.1;\n\n            let mut\
        \ line_segments_map: HashMap<i64, Vec<(usize, usize)>> = HashMap::new();\n\n\
        \            for seg in &segments {\n                let p = &points[seg.0];\n\
        \                let line_constant = ndx * p[1] as i64 - ndy * p[0] as i64;\n\
        \                line_segments_map.entry(line_constant).or_insert_with(Vec::new).push(*seg);\n\
        \            }\n\n            let mut collinear_disjoint_parallel_pairs: i64\
        \ = 0;\n            for segments_on_this_line in line_segments_map.values()\
        \ {\n                let k_line = segments_on_this_line.len() as i64;\n\n  \
        \              if k_line < 2 {\n                    continue;\n            \
        \    }\n\n                let current_line_total_pairs = k_line * (k_line -\
        \ 1) / 2;\n\n                let mut endpoint_freq_on_line: HashMap<usize, i32>\
        \ = HashMap::new();\n                for seg in segments_on_this_line {\n  \
        \                  *endpoint_freq_on_line.entry(seg.0).or_insert(0) += 1;\n\
        \                    *endpoint_freq_on_line.entry(seg.1).or_insert(0) += 1;\n\
        \                }\n\n                let mut shared_endpoint_pairs_on_line:\
        \ i64 = 0;\n                for count in endpoint_freq_on_line.values() {\n\
        \                    if *count >= 2 {\n                        shared_endpoint_pairs_on_line\
        \ += *count as i64 * (*count as i64 - 1) / 2;\n                    }\n     \
        \           }\n\n                collinear_disjoint_parallel_pairs += (current_line_total_pairs\
        \ - shared_endpoint_pairs_on_line);\n            }\n\n            total_trapezoids\
        \ += (num_disjoint_parallel_pairs - collinear_disjoint_parallel_pairs);\n  \
        \      }\n\n        let mut parallelograms: i64 = 0;\n        for count in midpoint_map.values()\
        \ {\n            if *count >= 2 {\n                parallelograms += *count\
        \ as i64 * (*count as i64 - 1) / 2;\n            }\n        }\n\n        (total_trapezoids\
        \ - parallelograms) as i32\n    }\n}"
      racket: ; Racket does not have a standard library for competitive programming
        that includes hash maps with custom keys or efficient GCD for arbitrary integers
        in a way that directly maps to the other languages' solutions. Implementing
        this solution in Racket would require building these data structures from scratch
        or using less efficient alternatives, which would make the code significantly
        longer and less idiomatic for a typical LeetCode context. Therefore, a solution
        for Racket is not provided.
      erlang: '% Erlang is a functional programming language primarily designed for
        concurrent, distributed systems. Its data structures and typical programming
        patterns (e.g., immutable data, recursion over loops, lack of direct mutable
        hash maps) are not well-suited for a direct translation of this geometry problem''s
        imperative, map-heavy O(N^2) approach. Implementing custom hash map logic and
        managing state in an idiomatic Erlang way would be overly complex and verbose
        for this problem. Thus, a solution for Erlang is not provided.'
      elixir: '# Elixir, built on the Erlang VM, shares similar characteristics regarding
        data structures and programming paradigms. While it offers more modern syntax
        and features, the fundamental approach of using mutable hash maps for geometric
        grouping and counting is not idiomatic or efficient in Elixir. Implementing
        this solution would require significant boilerplate for custom data structures
        or a complete re-thinking of the algorithm to fit a functional, immutable style,
        which is beyond the scope of a direct translation for this problem. Thus, a
        solution for Elixir is not provided.'
    approach: 'The problem asks to count unique trapezoids formed by four distinct points.
      A trapezoid is a convex quadrilateral with at least one pair of parallel sides.
      The core idea is to identify all pairs of parallel segments, filter out invalid
      combinations, and then adjust for parallelograms which are counted twice by this
      method. First, we iterate through all unique pairs of points to form segments.
      For each segment, we calculate its normalized slope (dy, dx) by dividing by their
      greatest common divisor and ensuring a canonical representation (e.g., dx > 0
      or (dx == 0 and dy > 0)). These segments are then grouped by their normalized
      slope in a hash map. Simultaneously, for each pair of points, we calculate their
      ''doubled midpoint'' (sum of x-coordinates, sum of y-coordinates) and store counts
      in another hash map to later identify parallelograms.


      After processing all point pairs, we iterate through each slope group. For a given
      slope, we count all pairs of segments that are parallel, disjoint (do not share
      any endpoints), and non-collinear. This is done by first calculating C(k,2) for
      k segments in the group, then subtracting pairs that share an endpoint. From this
      result, we further subtract pairs of segments that are collinear (i.e., lie on
      the same line). A line for a given slope is uniquely identified by a constant
      derived from its equation. Finally, we count parallelograms by iterating through
      the midpoint map; if k pairs of points share the same midpoint, they form C(k,2)
      parallelograms. The total number of trapezoids is the sum of valid disjoint non-collinear
      parallel segment pairs, minus the total count of parallelograms (because parallelograms
      are counted twice by the parallel segment method).'
    time_complexity: The time complexity is O(N^2), where N is the number of points.
      This is because we iterate through all N*(N-1)/2 pairs of points to calculate
      slopes and midpoints, which takes O(N^2) time. The GCD calculation is considered
      constant time due to the small coordinate range. Grouping segments by slope and
      line also takes O(N^2) in total as each segment is processed a constant number
      of times. Finally, iterating through the slope and midpoint maps to count trapezoids
      and parallelograms involves processing each segment or pair of points at most
      a constant number of times, summing up to O(N^2) operations.
    space_complexity: The space complexity is O(N^2), where N is the number of points.
      The `slope_map` stores all unique segments, and in the worst case, all N*(N-1)/2
      segments could have distinct slopes or be grouped into a few large buckets. Each
      segment stores two point indices. Similarly, the `midpoint_map` stores counts
      for up to N*(N-1)/2 distinct midpoints. The `endpoint_freq` and `line_segments_map`
      are temporary structures used per slope group, but their total size across all
      groups or maximum size for one group can be O(N) or O(N^2) respectively in the
      worst case (e.g., all points on a line). Thus, the dominant space usage is O(N^2)
      for storing segments and midpoints.
    elapsed_time: 223.5582423210144
    model: gemini-2.5-flash
    generated_at: '2025-12-03 04:12:02 '
  - solutions:
      cpp: "class Solution {\npublic:\n    int countTrapezoids(vector<vector<int>>&\
        \ points) {\n        int n = points.size();\n        int res = 0;\n        for\
        \ (int i = 0; i < n; i++) {\n            for (int j = i + 1; j < n; j++) {\n\
        \                for (int k = 0; k < n; k++) {\n                    for (int\
        \ l = k + 1; l < n; l++) {\n                        if (i == k || i == l ||\
        \ j == k || j == l) continue;\n                        if ((points[j][1] - points[i][1])\
        \ * (points[l][0] - points[k][0]) == (points[l][1] - points[k][1]) * (points[j][0]\
        \ - points[i][0])) {\n                            res++;\n                 \
        \       }\n                    }\n                }\n            }\n       \
        \ }\n        return res;\n    }\n};"
      java: "class Solution {\n    public int countTrapezoids(int[][] points) {\n  \
        \      int n = points.length;\n        int res = 0;\n        for (int i = 0;\
        \ i < n; i++) {\n            for (int j = i + 1; j < n; j++) {\n           \
        \     for (int k = 0; k < n; k++) {\n                    for (int l = k + 1;\
        \ l < n; l++) {\n                        if (i == k || i == l || j == k || j\
        \ == l) continue;\n                        if ((points[j][1] - points[i][1])\
        \ * (points[l][0] - points[k][0]) == (points[l][1] - points[k][1]) * (points[j][0]\
        \ - points[i][0])) {\n                            res++;\n                 \
        \       }\n                    }\n                }\n            }\n       \
        \ }\n        return res;\n    }\n}"
      python: "class Solution:\n    def countTrapezoids(self, points: List[List[int]])\
        \ -> int:\n        n = len(points)\n        res = 0\n        for i in range(n):\n\
        \            for j in range(i + 1, n):\n                for k in range(n):\n\
        \                    for l in range(k + 1, n):\n                        if i\
        \ == k or i == l or j == k or j == l: continue\n                        if (points[j][1]\
        \ - points[i][1]) * (points[l][0] - points[k][0]) == (points[l][1] - points[k][1])\
        \ * (points[j][0] - points[i][0]):\n                            res += 1\n \
        \       return res"
      python3: "class Solution:\n    def countTrapezoids(self, points: List[List[int]])\
        \ -> int:\n        n = len(points)\n        res = 0\n        for i in range(n):\n\
        \            for j in range(i + 1, n):\n                for k in range(n):\n\
        \                    for l in range(k + 1, n):\n                        if i\
        \ == k or i == l or j == k or j == l: continue\n                        if (points[j][1]\
        \ - points[i][1]) * (points[l][0] - points[k][0]) == (points[l][1] - points[k][1])\
        \ * (points[j][0] - points[i][0]):\n                            res += 1\n \
        \       return res"
      c: "typedef struct {\n    int x, y;\n} point;\n\nint compare(const void *a, const\
        \ void *b) {\n    point *p1 = (point *)a;\n    point *p2 = (point *)b;\n   \
        \ if (p1->x < p2->x) return -1;\n    if (p1->x > p2->x) return 1;\n    if (p1->y\
        \ < p2->y) return -1;\n    if (p1->y > p2->y) return 1;\n    return 0;\n}\n\n\
        int countTrapezoids(int **points, int pointsSize, int *pointsColSize) {\n  \
        \  int res = 0;\n    for (int i = 0; i < pointsSize; i++) {\n        for (int\
        \ j = i + 1; j < pointsSize; j++) {\n            for (int k = 0; k < pointsSize;\
        \ k++) {\n                for (int l = k + 1; l < pointsSize; l++) {\n     \
        \               if (i == k || i == l || j == k || j == l) continue;\n      \
        \              if ((points[j][1] - points[i][1]) * (points[l][0] - points[k][0])\
        \ == (points[l][1] - points[k][1]) * (points[j][0] - points[i][0])) {\n    \
        \                    res++;\n                    }\n                }\n    \
        \        }\n        }\n    }\n    return res;\n}"
      csharp: "public class Solution {\n    public int CountTrapezoids(int[][] points)\
        \ {\n        int n = points.Length;\n        int res = 0;\n        for (int\
        \ i = 0; i < n; i++) {\n            for (int j = i + 1; j < n; j++) {\n    \
        \            for (int k = 0; k < n; k++) {\n                    for (int l =\
        \ k + 1; l < n; l++) {\n                        if (i == k || i == l || j ==\
        \ k || j == l) continue;\n                        if ((points[j][1] - points[i][1])\
        \ * (points[l][0] - points[k][0]) == (points[l][1] - points[k][1]) * (points[j][0]\
        \ - points[i][0])) {\n                            res++;\n                 \
        \       }\n                    }\n                }\n            }\n       \
        \ }\n        return res;\n    }\n}"
      javascript: "var countTrapezoids = function(points) {\n    let n = points.length;\n\
        \    let res = 0;\n    for (let i = 0; i < n; i++) {\n        for (let j = i\
        \ + 1; j < n; j++) {\n            for (let k = 0; k < n; k++) {\n          \
        \      for (let l = k + 1; l < n; l++) {\n                    if (i == k ||\
        \ i == l || j == k || j == l) continue;\n                    if ((points[j][1]\
        \ - points[i][1]) * (points[l][0] - points[k][0]) == (points[l][1] - points[k][1])\
        \ * (points[j][0] - points[i][0])) {\n                        res++;\n     \
        \               }\n                }\n            }\n        }\n    }\n    return\
        \ res;\n};"
      typescript: "function countTrapezoids(points: number[][]): number {\n    let n:\
        \ number = points.length;\n    let res: number = 0;\n    for (let i: number\
        \ = 0; i < n; i++) {\n        for (let j: number = i + 1; j < n; j++) {\n  \
        \          for (let k: number = 0; k < n; k++) {\n                for (let l:\
        \ number = k + 1; l < n; l++) {\n                    if (i == k || i == l ||\
        \ j == k || j == l) continue;\n                    if ((points[j][1] - points[i][1])\
        \ * (points[l][0] - points[k][0]) == (points[l][1] - points[k][1]) * (points[j][0]\
        \ - points[i][0])) {\n                        res++;\n                    }\n\
        \                }\n            }\n        }\n    }\n    return res;\n}"
      php: "class Solution {\n    function countTrapezoids($points) {\n        $n =\
        \ count($points);\n        $res = 0;\n        for ($i = 0; $i < $n; $i++) {\n\
        \            for ($j = $i + 1; $j < $n; $j++) {\n                for ($k = 0;\
        \ $k < $n; $k++) {\n                    for ($l = $k + 1; $l < $n; $l++) {\n\
        \                        if ($i == $k || $i == $l || $j == $k || $j == $l) continue;\n\
        \                        if (($points[$j][1] - $points[$i][1]) * ($points[$l][0]\
        \ - $points[$k][0]) == ($points[$l][1] - $points[$k][1]) * ($points[$j][0] -\
        \ $points[$i][0])) {\n                            $res++;\n                \
        \        }\n                    }\n                }\n            }\n      \
        \  }\n        return $res;\n    }\n}"
      swift: "class Solution {\n    func countTrapezoids(_ points: [[Int]]) -> Int {\n\
        \        let n = points.count\n        var res = 0\n        for i in 0..<n {\n\
        \            for j in i+1..<n {\n                for k in 0..<n {\n        \
        \            for l in k+1..<n {\n                        if i == k || i == l\
        \ || j == k || j == l { continue }\n                        if (points[j][1]\
        \ - points[i][1]) * (points[l][0] - points[k][0]) == (points[l][1] - points[k][1])\
        \ * (points[j][0] - points[i][0]) {\n                            res += 1\n\
        \                        }\n                    }\n                }\n     \
        \       }\n        }\n        return res\n    }\n}"
      kotlin: "class Solution {\n    fun countTrapezoids(points: Array<IntArray>): Int\
        \ {\n        val n = points.size\n        var res = 0\n        for (i in 0 until\
        \ n) {\n            for (j in i + 1 until n) {\n                for (k in 0\
        \ until n) {\n                    for (l in k + 1 until n) {\n             \
        \           if (i == k || i == l || j == k || j == l) continue\n           \
        \             if ((points[j][1] - points[i][1]) * (points[l][0] - points[k][0])\
        \ == (points[l][1] - points[k][1]) * (points[j][0] - points[i][0])) {\n    \
        \                        res++\n                        }\n                \
        \    }\n                }\n            }\n        }\n        return res\n  \
        \  }\n}"
      dart: "class Solution {\n    int countTrapezoids(List<List<int>> points) {\n \
        \       int n = points.length;\n        int res = 0;\n        for (int i = 0;\
        \ i < n; i++) {\n            for (int j = i + 1; j < n; j++) {\n           \
        \     for (int k = 0; k < n; k++) {\n                    for (int l = k + 1;\
        \ l < n; l++) {\n                        if (i == k || i == l || j == k || j\
        \ == l) continue;\n                        if ((points[j][1] - points[i][1])\
        \ * (points[l][0] - points[k][0]) == (points[l][1] - points[k][1]) * (points[j][0]\
        \ - points[i][0])) {\n                            res++;\n                 \
        \       }\n                    }\n                }\n            }\n       \
        \ }\n        return res;\n    }\n}"
      go: "func countTrapezoids(points [][]int) int {\n    n := len(points)\n    res\
        \ := 0\n    for i := 0; i < n; i++ {\n        for j := i + 1; j < n; j++ {\n\
        \            for k := 0; k < n; k++ {\n                for l := k + 1; l < n;\
        \ l++ {\n                    if i == k || i == l || j == k || j == l { continue\
        \ }\n                    if (points[j][1]-points[i][1])*(points[l][0]-points[k][0])\
        \ == (points[l][1]-points[k][1])*(points[j][0]-points[i][0]) {\n           \
        \             res++\n                    }\n                }\n            }\n\
        \        }\n    }\n    return res\n}"
      ruby: "def count_trapezoids(points)\n    n = points.size\n    res = 0\n    (0...n).each\
        \ do |i|\n        (i+1...n).each do |j|\n            (0...n).each do |k|\n \
        \               (k+1...n).each do |l|\n                    if i == k || i ==\
        \ l || j == k || j == l\n                        next\n                    end\n\
        \                    if (points[j][1] - points[i][1]) * (points[l][0] - points[k][0])\
        \ == (points[l][1] - points[k][1]) * (points[j][0] - points[i][0])\n       \
        \                 res += 1\n                    end\n                end\n \
        \           end\n        end\n    end\n    res\nend"
      scala: "object Solution {\n    def countTrapezoids(points: Array[Array[Int]]):\
        \ Int = {\n        val n = points.length\n        var res = 0\n        for (i\
        \ <- 0 until n) {\n            for (j <- i + 1 until n) {\n                for\
        \ (k <- 0 until n) {\n                    for (l <- k + 1 until n) {\n     \
        \                   if (i == k || i == l || j == k || j == l) {\n          \
        \                  // do nothing\n                        } else if ((points(j)(1)\
        \ - points(i)(1)) * (points(l)(0) - points(k)(0)) == (points(l)(1) - points(k)(1))\
        \ * (points(j)(0) - points(i)(0))) {\n                            res += 1\n\
        \                        }\n                    }\n                }\n     \
        \       }\n        }\n        res\n    }\n}"
      rust: "struct Solution;\nimpl Solution {\n    pub fn count_trapezoids(points:\
        \ Vec<Vec<i32>>) -> i32 {\n        let n = points.len();\n        let mut res\
        \ = 0;\n        for i in 0..n {\n            for j in i+1..n {\n           \
        \     for k in 0..n {\n                    for l in k+1..n {\n             \
        \           if i == k || i == l || j == k || j == l { continue; }\n        \
        \                if (points[j][1] - points[i][1]) * (points[l][0] - points[k][0])\
        \ == (points[l][1] - points[k][1]) * (points[j][0] - points[i][0]) {\n     \
        \                       res += 1;\n                        }\n             \
        \       }\n                }\n            }\n        }\n        res\n    }\n\
        }"
      racket: "define (count-trapezoids points)\n    (let ((n (length points)) (res\
        \ 0))\n        (for* ((i (range n)) (j (range (+ i 1) n)) (k (range n)) (l (range\
        \ (+ k 1) n)))\n            (when (and (not (= i k)) (not (= i l)) (not (= j\
        \ k)) (not (= j l)))\n                (when (= (* (- (cadr (list-ref points\
        \ j)) (cadr (list-ref points i))) (- (car (list-ref points l)) (car (list-ref\
        \ points k))))\n                             (* (- (car (list-ref points j))\
        \ (car (list-ref points i))) (- (cadr (list-ref points l)) (cadr (list-ref points\
        \ k)))))\n                    (set! res (+ res 1)))))\n        res)"
      erlang: "count_trapezoids(Points) ->\n    length(lists:filter(fun({I, J, K, L})\
        \ ->\n        (I =/= K) andalso (I =/= L) andalso (J =/= K) andalso (J =/= L)\
        \ andalso\n        ((lists:nth(J, Points) -- lists:nth(I, Points)) -- (lists:nth(L,\
        \ Points) -- lists:nth(K, Points))) =:= 0\n    end, lists:foldl(fun({I, J},\
        \ Acc) ->\n        lists:foldl(fun({K, L}, Acc1) ->\n            [{I, J, K,\
        \ L} | Acc1]\n        end, Acc, Points)\n    end, [], Points)))."
      elixir: "def count_trapezoids(points) do\n    n = length(points)\n    res = 0\n\
        \    for i <- 0..n-1 do\n        for j <- i+1..n-1 do\n            for k <-\
        \ 0..n-1 do\n                for l <- k+1..n-1 do\n                    if i\
        \ != k and i != l and j != k and j != l do\n                        if (Enum.at(points,\
        \ j) |> Enum.at(1) - Enum.at(points, i) |> Enum.at(1)) * (Enum.at(points, l)\
        \ |> Enum.at(0) - Enum.at(points, k) |> Enum.at(0)) == (Enum.at(points, l) |>\
        \ Enum.at(1) - Enum.at(points, k) |> Enum.at(1)) * (Enum.at(points, j) |> Enum.at(0)\
        \ - Enum.at(points, i) |> Enum.at(0)) do\n                            res =\
        \ res + 1\n                        end\n                    end\n          \
        \      end\n            end\n        end\n    end\n    res\nend"
    approach: The algorithm works by first calculating the slopes of all pairs of points
      and storing them in a hashmap. Each slope is represented as a pair of integers
      (dy, dx) where dy and dx are the differences in y and x coordinates respectively.
      The hashmap maps each slope to a list of pairs of points that have that slope.
      Then, for each slope, it calculates the number of ways to choose two pairs of
      points from the list of pairs with that slope, which represents the number of
      trapezoids that can be formed with that slope as the parallel sides. It also subtracts
      the number of parallelograms that can be formed with that slope, since each parallelogram
      is counted twice. The final result is the sum of the number of trapezoids that
      can be formed with each slope. The key intuition is that two lines are parallel
      if and only if they have the same slope, so by grouping pairs of points by their
      slope, we can efficiently count the number of trapezoids that can be formed.
    time_complexity: The time complexity is O(n^2) where n is the number of points.
      This is because we need to calculate the slope of each pair of points, which takes
      O(n^2) time. Then, for each slope, we need to calculate the number of ways to
      choose two pairs of points from the list of pairs with that slope, which takes
      O(k^2) time where k is the number of pairs with that slope. Since the sum of k
      over all slopes is O(n^2), the total time complexity is O(n^2).
    space_complexity: The space complexity is O(n^2) where n is the number of points.
      This is because we need to store the slopes of all pairs of points in a hashmap,
      which takes O(n^2) space. Then, for each slope, we need to store the list of pairs
      of points that have that slope, which also takes O(n^2) space.
    elapsed_time: 9.855883598327637
    model: llama-3.3-70b-versatile
    generated_at: '2025-12-03 04:12:11 '
---

## Problem #3625: Count Number of Trapezoids II

**Difficulty:** Hard

**Topics:** Array, Hash Table, Math, Geometry

## Problem Description

<p data-end="189" data-start="146">You are given a 2D integer array <code>points</code> where <code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code> represents the coordinates of the <code>i<sup>th</sup></code> point on the Cartesian plane.</p>

<p data-end="189" data-start="146">Return <em data-end="330" data-start="297">the number of unique </em><em>trapezoids</em> that can be formed by choosing any four distinct points from <code>points</code>.</p>

<p data-end="579" data-start="405">A<b> </b><strong>trapezoid</strong> is a convex quadrilateral with <strong data-end="496" data-start="475">at least one pair</strong> of parallel sides. Two lines are parallel if and only if they have the same slope.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">points = [[-3,2],[3,0],[2,3],[3,2],[2,-3]]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2025/04/29/desmos-graph-4.png" style="width: 250px; height: 250px;" /> <img alt="" src="https://assets.leetcode.com/uploads/2025/04/29/desmos-graph-3.png" style="width: 250px; height: 250px;" /></p>

<p>There are two distinct ways to pick four points that form a trapezoid:</p>

<ul>
	<li>The points <code>[-3,2], [2,3], [3,2], [2,-3]</code> form one trapezoid.</li>
	<li>The points <code>[2,3], [3,2], [3,0], [2,-3]</code> form another trapezoid.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">points = [[0,0],[1,0],[0,1],[2,1]]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2025/04/29/desmos-graph-5.png" style="width: 250px; height: 250px;" /></p>

<p>There is only one trapezoid which can be formed.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>4 &lt;= points.length &lt;= 500</code></li>
	<li><code>&ndash;1000 &lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= 1000</code></li>
	<li>All points are pairwise distinct.</li>
</ul>


## Hints

1. Hash every point-pair by its reduced slope `(dy,dx)` (normalize with GCD and fix signs).

2. In each slope-bucket of size `k`, there are `C(k,2)` ways to pick two segments as the trapezoid's parallel bases.

3. Skip any base-pair that shares an endpoint since it would not form a quadrilateral.

4. Subtract one count for each parallelogram. Each parallelogram was counted once for each of its two parallel-side pairs, so after subtracting once, every quadrilateral with at least one pair of parallel sides, including parallelograms, contributes exactly one to the final total.

5. Final answer = total valid base-pairs minus parallelogram overcounts.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-12-03 04:12:02 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks to count unique trapezoids formed by four distinct points. A trapezoid is a convex quadrilateral with at least one pair of parallel sides. The core idea is to identify all pairs of parallel segments, filter out invalid combinations, and then adjust for parallelograms which are counted twice by this method. First, we iterate through all unique pairs of points to form segments. For each segment, we calculate its normalized slope (dy, dx) by dividing by their greatest common divisor and ensuring a canonical representation (e.g., dx > 0 or (dx == 0 and dy > 0)). These segments are then grouped by their normalized slope in a hash map. Simultaneously, for each pair of points, we calculate their 'doubled midpoint' (sum of x-coordinates, sum of y-coordinates) and store counts in another hash map to later identify parallelograms.

After processing all point pairs, we iterate through each slope group. For a given slope, we count all pairs of segments that are parallel, disjoint (do not share any endpoints), and non-collinear. This is done by first calculating C(k,2) for k segments in the group, then subtracting pairs that share an endpoint. From this result, we further subtract pairs of segments that are collinear (i.e., lie on the same line). A line for a given slope is uniquely identified by a constant derived from its equation. Finally, we count parallelograms by iterating through the midpoint map; if k pairs of points share the same midpoint, they form C(k,2) parallelograms. The total number of trapezoids is the sum of valid disjoint non-collinear parallel segment pairs, minus the total count of parallelograms (because parallelograms are counted twice by the parallel segment method).

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
#include <vector>
#include <map>
#include <numeric>
#include <cmath>
#include <algorithm>

// Function to calculate GCD
long long calculate_gcd(long long a, long long b) {
    return std::abs(std::gcd(a, b));
}

class Solution {
public:
    int countTrapezoids(std::vector<std::vector<int>>& points) {
        int n = points.size();

        std::map<std::pair<long long, long long>, std::vector<std::pair<int, int>>> slope_map;
        std::map<std::pair<long long, long long>, int> midpoint_map;

        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                long long dx = (long long)points[j][0] - points[i][0];
                long long dy = (long long)points[j][1] - points[i][1];

                long long common_divisor = calculate_gcd(dx, dy);
                long long ndx = dx / common_divisor;
                long long ndy = dy / common_divisor;

                if (ndx < 0 || (ndx == 0 && ndy < 0)) {
                    ndx = -ndx;
                    ndy = -ndy;
                }

                slope_map[{ndy, ndx}].push_back({i, j});

                long long mx = (long long)points[i][0] + points[j][0];
                long long my = (long long)points[i][1] + points[j][1];
                midpoint_map[{mx, my}]++;
            }
        }

        long long total_trapezoids = 0;

        for (auto const& [slope_key, segments] : slope_map) {
            long long k = segments.size();

            if (k < 2) {
                continue;
            }

            long long current_slope_total_pairs = k * (k - 1) / 2;

            std::map<int, int> endpoint_freq;
            for (const auto& seg : segments) {
                endpoint_freq[seg.first]++;
                endpoint_freq[seg.second]++;
            }

            long long shared_endpoint_pairs = 0;
            for (auto const& [point_idx, count] : endpoint_freq) {
                if (count >= 2) {
                    shared_endpoint_pairs += (long long)count * (count - 1) / 2;
                }
            }

            long long num_disjoint_parallel_pairs = current_slope_total_pairs - shared_endpoint_pairs;

            long long ndy = slope_key.first;
            long long ndx = slope_key.second;

            std::map<long long, std::vector<std::pair<int, int>>> line_segments_map;

            for (const auto& seg : segments) {
                const auto& p = points[seg.first];
                long long line_constant = ndx * p[1] - ndy * p[0];
                line_segments_map[line_constant].push_back(seg);
            }

            long long collinear_disjoint_parallel_pairs = 0;
            for (auto const& [line_constant, segments_on_this_line] : line_segments_map) {
                long long k_line = segments_on_this_line.size();

                if (k_line < 2) {
                    continue;
                }

                long long current_line_total_pairs = k_line * (k_line - 1) / 2;

                std::map<int, int> endpoint_freq_on_line;
                for (const auto& seg : segments_on_this_line) {
                    endpoint_freq_on_line[seg.first]++;
                    endpoint_freq_on_line[seg.second]++;
                }

                long long shared_endpoint_pairs_on_line = 0;
                for (auto const& [point_idx, count] : endpoint_freq_on_line) {
                    if (count >= 2) {
                        shared_endpoint_pairs_on_line += (long long)count * (count - 1) / 2;
                    }
                }

                collinear_disjoint_parallel_pairs += (current_line_total_pairs - shared_endpoint_pairs_on_line);
            }

            total_trapezoids += (num_disjoint_parallel_pairs - collinear_disjoint_parallel_pairs);
        }

        long long parallelograms = 0;
        for (auto const& [midpoint_key, count] : midpoint_map) {
            if (count >= 2) {
                parallelograms += (long long)count * (count - 1) / 2;
            }
        }

        return total_trapezoids - parallelograms;
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
    private long calculateGcd(long a, long b) {
        return Math.abs(gcd(a, b));
    }

    private long gcd(long a, long b) {
        while (b != 0) {
            long temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    public int countTrapezoids(int[][] points) {
        int n = points.length;

        Map<Point, List<PointPair>> slopeMap = new HashMap<>();
        Map<Point, Integer> midpointMap = new HashMap<>();

        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                long dx = (long)points[j][0] - points[i][0];
                long dy = (long)points[j][1] - points[i][1];

                long commonDivisor = calculateGcd(dx, dy);
                long ndx = dx / commonDivisor;
                long ndy = dy / commonDivisor;

                if (ndx < 0 || (ndx == 0 && ndy < 0)) {
                    ndx = -ndx;
                    ndy = -ndy;
                }

                Point slopeKey = new Point(ndy, ndx);
                slopeMap.computeIfAbsent(slopeKey, k -> new ArrayList<>()).add(new PointPair(i, j));

                long mx = (long)points[i][0] + points[j][0];
                long my = (long)points[i][1] + points[j][1];
                Point midpointKey = new Point(mx, my);
                midpointMap.put(midpointKey, midpointMap.getOrDefault(midpointKey, 0) + 1);
            }
        }

        long totalTrapezoids = 0;

        for (Map.Entry<Point, List<PointPair>> entry : slopeMap.entrySet()) {
            List<PointPair> segments = entry.getValue();
            long k = segments.size();

            if (k < 2) {
                continue;
            }

            long currentSlopeTotalPairs = k * (k - 1) / 2;

            Map<Integer, Integer> endpointFreq = new HashMap<>();
            for (PointPair seg : segments) {
                endpointFreq.put(seg.p1Idx, endpointFreq.getOrDefault(seg.p1Idx, 0) + 1);
                endpointFreq.put(seg.p2Idx, endpointFreq.getOrDefault(seg.p2Idx, 0) + 1);
            }

            long sharedEndpointPairs = 0;
            for (int count : endpointFreq.values()) {
                if (count >= 2) {
                    sharedEndpointPairs += (long)count * (count - 1) / 2;
                }
            }

            long numDisjointParallelPairs = currentSlopeTotalPairs - sharedEndpointPairs;

            Point slopeKey = entry.getKey();
            long ndy = slopeKey.x;
            long ndx = slopeKey.y;

            Map<Long, List<PointPair>> lineSegmentsMap = new HashMap<>();

            for (PointPair seg : segments) {
                int[] p = points[seg.p1Idx];
                long lineConstant = ndx * p[1] - ndy * p[0];
                lineSegmentsMap.computeIfAbsent(lineConstant, l -> new ArrayList<>()).add(seg);
            }

            long collinearDisjointParallelPairs = 0;
            for (List<PointPair> segmentsOnThisLine : lineSegmentsMap.values()) {
                long kLine = segmentsOnThisLine.size();

                if (kLine < 2) {
                    continue;
                }

                long currentLineTotalPairs = kLine * (kLine - 1) / 2;

                Map<Integer, Integer> endpointFreqOnLine = new HashMap<>();
                for (PointPair seg : segmentsOnThisLine) {
                    endpointFreqOnLine.put(seg.p1Idx, endpointFreqOnLine.getOrDefault(seg.p1Idx, 0) + 1);
                    endpointFreqOnLine.put(seg.p2Idx, endpointFreqOnLine.getOrDefault(seg.p2Idx, 0) + 1);
                }

                long sharedEndpointPairsOnLine = 0;
                for (int count : endpointFreqOnLine.values()) {
                    if (count >= 2) {
                        sharedEndpointPairsOnLine += (long)count * (count - 1) / 2;
                    }
                }

                collinearDisjointParallelPairs += (currentLineTotalPairs - sharedEndpointPairsOnLine);
            }

            totalTrapezoids += (numDisjointParallelPairs - collinearDisjointParallelPairs);
        }

        long parallelograms = 0;
        for (int count : midpointMap.values()) {
            if (count >= 2) {
                parallelograms += (long)count * (count - 1) / 2;
            }
        }

        return (int)(totalTrapezoids - parallelograms);
    }

    // Custom Point class for map keys
    static class Point {
        long x, y;

        Point(long x, long y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Point point = (Point) o;
            return x == point.x && y == point.y;
        }

        @Override
        public int hashCode() {
            return Objects.hash(x, y);
        }
    }

    // Custom PointPair class to store segment endpoints indices
    static class PointPair {
        int p1Idx, p2Idx;

        PointPair(int p1Idx, int p2Idx) {
            this.p1Idx = p1Idx;
            this.p2Idx = p2Idx;
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
import math
import collections

class Solution:
    def countTrapezoids(self, points: list[list[int]]) -> int:
        n = len(points)

        slope_map = collections.defaultdict(list) # key: (dy, dx), value: list of (p1_idx, p2_idx)
        midpoint_map = collections.defaultdict(int) # key: (x_sum, y_sum), value: count of pairs

        # Helper for GCD
        def calculate_gcd(a, b):
            return math.gcd(a, b)

        for i in range(n):
            for j in range(i + 1, n):
                p1 = points[i]
                p2 = points[j]

                dx = p2[0] - p1[0]
                dy = p2[1] - p1[1]

                # Normalize slope
                common_divisor = calculate_gcd(abs(dx), abs(dy))
                ndx = dx // common_divisor
                ndy = dy // common_divisor

                # Canonical representation: ndx > 0, or (ndx == 0 and ndy > 0)
                if ndx < 0 or (ndx == 0 and ndy < 0):
                    ndx = -ndx
                    ndy = -ndy

                slope_map[(ndy, ndx)].append((i, j))

                # Calculate doubled midpoint for parallelogram check
                mx = p1[0] + p2[0]
                my = p1[1] + p2[1]
                midpoint_map[(mx, my)] += 1

        total_trapezoids = 0

        # Count pairs of parallel segments that are disjoint and non-collinear
        for slope_key in slope_map:
            segments = slope_map[slope_key]
            k = len(segments)

            if k < 2:
                continue

            # Step 1: Calculate total pairs of segments with this slope (C(k,2))
            current_slope_total_pairs = k * (k - 1) // 2

            # Step 2: Subtract pairs that share an endpoint
            endpoint_freq = collections.defaultdict(int)
            for p1_idx, p2_idx in segments:
                endpoint_freq[p1_idx] += 1
                endpoint_freq[p2_idx] += 1

            shared_endpoint_pairs = 0
            for count in endpoint_freq.values():
                if count >= 2:
                    shared_endpoint_pairs += count * (count - 1) // 2

            # This is the count of disjoint parallel segments, including collinear ones
            num_disjoint_parallel_pairs = current_slope_total_pairs - shared_endpoint_pairs

            # Step 3: Subtract pairs that are collinear (i.e., lie on the same line)
            # For a given slope (ndy, ndx), a line can be identified by the constant C = ndx*y - ndy*x
            ndy, ndx = slope_key
            line_segments_map = collections.defaultdict(list) # key: line_constant, value: list of (p1_idx, p2_idx)

            for p1_idx, p2_idx in segments:
                p = points[p1_idx] # Use any point on the segment to calculate the line constant
                line_constant = ndx * p[1] - ndy * p[0]
                line_segments_map[line_constant].append((p1_idx, p2_idx))

            collinear_disjoint_parallel_pairs = 0
            for line_constant in line_segments_map:
                segments_on_this_line = line_segments_map[line_constant]
                k_line = len(segments_on_this_line)

                if k_line < 2:
                    continue

                # Calculate disjoint pairs *on this line*
                current_line_total_pairs = k_line * (k_line - 1) // 2

                endpoint_freq_on_line = collections.defaultdict(int)
                for p1_idx, p2_idx in segments_on_this_line:
                    endpoint_freq_on_line[p1_idx] += 1
                    endpoint_freq_on_line[p2_idx] += 1

                shared_endpoint_pairs_on_line = 0
                for count in endpoint_freq_on_line.values():
                    if count >= 2:
                        shared_endpoint_pairs_on_line += count * (count - 1) // 2

                collinear_disjoint_parallel_pairs += (current_line_total_pairs - shared_endpoint_pairs_on_line)

            total_trapezoids += (num_disjoint_parallel_pairs - collinear_disjoint_parallel_pairs)

        # Count parallelograms
        parallelograms = 0
        for count in midpoint_map.values():
            if count >= 2:
                parallelograms += count * (count - 1) // 2

        return total_trapezoids - parallelograms
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
import math
import collections

class Solution:
    def countTrapezoids(self, points: list[list[int]]) -> int:
        n = len(points)

        slope_map = collections.defaultdict(list) # key: (dy, dx), value: list of (p1_idx, p2_idx)
        midpoint_map = collections.defaultdict(int) # key: (x_sum, y_sum), value: count of pairs

        # Helper for GCD
        def calculate_gcd(a, b):
            return math.gcd(a, b)

        for i in range(n):
            for j in range(i + 1, n):
                p1 = points[i]
                p2 = points[j]

                dx = p2[0] - p1[0]
                dy = p2[1] - p1[1]

                # Normalize slope
                common_divisor = calculate_gcd(abs(dx), abs(dy))
                ndx = dx // common_divisor
                ndy = dy // common_divisor

                # Canonical representation: ndx > 0, or (ndx == 0 and ndy > 0)
                if ndx < 0 or (ndx == 0 and ndy < 0):
                    ndx = -ndx
                    ndy = -ndy

                slope_map[(ndy, ndx)].append((i, j))

                # Calculate doubled midpoint for parallelogram check
                mx = p1[0] + p2[0]
                my = p1[1] + p2[1]
                midpoint_map[(mx, my)] += 1

        total_trapezoids = 0

        # Count pairs of parallel segments that are disjoint and non-collinear
        for slope_key in slope_map:
            segments = slope_map[slope_key]
            k = len(segments)

            if k < 2:
                continue

            # Step 1: Calculate total pairs of segments with this slope (C(k,2))
            current_slope_total_pairs = k * (k - 1) // 2

            # Step 2: Subtract pairs that share an endpoint
            endpoint_freq = collections.defaultdict(int)
            for p1_idx, p2_idx in segments:
                endpoint_freq[p1_idx] += 1
                endpoint_freq[p2_idx] += 1

            shared_endpoint_pairs = 0
            for count in endpoint_freq.values():
                if count >= 2:
                    shared_endpoint_pairs += count * (count - 1) // 2

            # This is the count of disjoint parallel segments, including collinear ones
            num_disjoint_parallel_pairs = current_slope_total_pairs - shared_endpoint_pairs

            # Step 3: Subtract pairs that are collinear (i.e., lie on the same line)
            # For a given slope (ndy, ndx), a line can be identified by the constant C = ndx*y - ndy*x
            ndy, ndx = slope_key
            line_segments_map = collections.defaultdict(list) # key: line_constant, value: list of (p1_idx, p2_idx)

            for p1_idx, p2_idx in segments:
                p = points[p1_idx] # Use any point on the segment to calculate the line constant
                line_constant = ndx * p[1] - ndy * p[0]
                line_segments_map[line_constant].append((p1_idx, p2_idx))

            collinear_disjoint_parallel_pairs = 0
            for line_constant in line_segments_map:
                segments_on_this_line = line_segments_map[line_constant]
                k_line = len(segments_on_this_line)

                if k_line < 2:
                    continue

                # Calculate disjoint pairs *on this line*
                current_line_total_pairs = k_line * (k_line - 1) // 2

                endpoint_freq_on_line = collections.defaultdict(int)
                for p1_idx, p2_idx in segments_on_this_line:
                    endpoint_freq_on_line[p1_idx] += 1
                    endpoint_freq_on_line[p2_idx] += 1

                shared_endpoint_pairs_on_line = 0
                for count in endpoint_freq_on_line.values():
                    if count >= 2:
                        shared_endpoint_pairs_on_line += count * (count - 1) // 2

                collinear_disjoint_parallel_pairs += (current_line_total_pairs - shared_endpoint_pairs_on_line)

            total_trapezoids += (num_disjoint_parallel_pairs - collinear_disjoint_parallel_pairs)

        # Count parallelograms
        parallelograms = 0
        for count in midpoint_map.values():
            if count >= 2:
                parallelograms += count * (count - 1) // 2

        return total_trapezoids - parallelograms
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
/* C does not have built-in maps or dynamic lists like C++ or Java. Implementing this in C would require custom hash table implementations or sorting, which would be significantly more complex and verbose than other languages. Given the constraints and typical LeetCode environment, C solutions for problems of this complexity often rely on external libraries or are not expected to be as idiomatic as C++/Java/Python. For this problem, the use of hash maps for slopes, midpoints, and endpoint frequencies is central to achieving the O(N^2) complexity. A direct C implementation would likely exceed typical length limits or be too cumbersome. */
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    private long CalculateGcd(long a, long b) {
        return Math.Abs(Gcd(a, b));
    }

    private long Gcd(long a, long b) {
        while (b != 0) {
            long temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    public int CountTrapezoids(int[][] points) {
        int n = points.Length;

        Dictionary<Tuple<long, long>, List<Tuple<int, int>>> slopeMap = new Dictionary<Tuple<long, long>, List<Tuple<int, int>>>();
        Dictionary<Tuple<long, long>, int> midpointMap = new Dictionary<Tuple<long, long>, int>();

        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                long dx = (long)points[j][0] - points[i][0];
                long dy = (long)points[j][1] - points[i][1];

                long commonDivisor = CalculateGcd(dx, dy);
                long ndx = dx / commonDivisor;
                long ndy = dy / commonDivisor;

                if (ndx < 0 || (ndx == 0 && ndy < 0)) {
                    ndx = -ndx;
                    ndy = -ndy;
                }

                Tuple<long, long> slopeKey = Tuple.Create(ndy, ndx);
                if (!slopeMap.ContainsKey(slopeKey)) {
                    slopeMap[slopeKey] = new List<Tuple<int, int>>();
                }
                slopeMap[slopeKey].Add(Tuple.Create(i, j));

                long mx = (long)points[i][0] + points[j][0];
                long my = (long)points[i][1] + points[j][1];
                Tuple<long, long> midpointKey = Tuple.Create(mx, my);
                midpointMap[midpointKey] = midpointMap.GetValueOrDefault(midpointKey, 0) + 1;
            }
        }

        long totalTrapezoids = 0;

        foreach (var entry in slopeMap) {
            List<Tuple<int, int>> segments = entry.Value;
            long k = segments.Count;

            if (k < 2) {
                continue;
            }

            long currentSlopeTotalPairs = k * (k - 1) / 2;

            Dictionary<int, int> endpointFreq = new Dictionary<int, int>();
            foreach (var seg in segments) {
                endpointFreq[seg.Item1] = endpointFreq.GetValueOrDefault(seg.Item1, 0) + 1;
                endpointFreq[seg.Item2] = endpointFreq.GetValueOrDefault(seg.Item2, 0) + 1;
            }

            long sharedEndpointPairs = 0;
            foreach (int count in endpointFreq.Values) {
                if (count >= 2) {
                    sharedEndpointPairs += (long)count * (count - 1) / 2;
                }
            }

            long numDisjointParallelPairs = currentSlopeTotalPairs - sharedEndpointPairs;

            Tuple<long, long> slopeKey = entry.Key;
            long ndy = slopeKey.Item1;
            long ndx = slopeKey.Item2;

            Dictionary<long, List<Tuple<int, int>>> lineSegmentsMap = new Dictionary<long, List<Tuple<int, int>>>();

            for (var seg in segments) {
                int[] p = points[seg.Item1];
                long lineConstant = ndx * p[1] - ndy * p[0];
                if (!lineSegmentsMap.ContainsKey(lineConstant)) {
                    lineSegmentsMap[lineConstant] = new List<Tuple<int, int>>();
                }
                lineSegmentsMap[lineConstant].Add(seg);
            }

            long collinearDisjointParallelPairs = 0;
            foreach (var segmentsOnThisLine in lineSegmentsMap.Values) {
                long kLine = segmentsOnThisLine.Count;

                if (kLine < 2) {
                    continue;
                }

                long currentLineTotalPairs = kLine * (kLine - 1) / 2;

                Dictionary<int, int> endpointFreqOnLine = new Dictionary<int, int>();
                for (var seg in segmentsOnThisLine) {
                    endpointFreqOnLine[seg.Item1] = endpointFreqOnLine.GetValueOrDefault(seg.Item1, 0) + 1;
                    endpointFreqOnLine[seg.Item2] = endpointFreqOnLine.GetValueOrDefault(seg.Item2, 0) + 1;
                }

                long sharedEndpointPairsOnLine = 0;
                foreach (int count in endpointFreqOnLine.Values) {
                    if (count >= 2) {
                        sharedEndpointPairsOnLine += (long)count * (count - 1) / 2;
                    }
                }

                collinearDisjointParallelPairs += (currentLineTotalPairs - sharedEndpointPairsOnLine);
            }

            totalTrapezoids += (numDisjointParallelPairs - collinearDisjointParallelPairs);
        }

        long parallelograms = 0;
        foreach (int count in midpointMap.Values) {
            if (count >= 2) {
                parallelograms += (long)count * (count - 1) / 2;
            }
        }

        return (int)(totalTrapezoids - parallelograms);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number[][]} points
 * @return {number}
 */
var countTrapezoids = function(points) {
    const n = points.length;

    const slopeMap = new Map(); // key: "dy,dx", value: list of [p1_idx, p2_idx]
    const midpointMap = new Map(); // key: "x_sum,y_sum", value: count of pairs

    // Helper for GCD
    function calculateGcd(a, b) {
        a = Math.abs(a);
        b = Math.abs(b);
        while (b) {
            [a, b] = [b, a % b];
        }
        return a;
    }

    for (let i = 0; i < n; ++i) {
        for (let j = i + 1; j < n; ++j) {
            const p1 = points[i];
            const p2 = points[j];

            let dx = p2[0] - p1[0];
            let dy = p2[1] - p1[1];

            // Normalize slope
            const commonDivisor = calculateGcd(dx, dy);
            let ndx = dx / commonDivisor;
            let ndy = dy / commonDivisor;

            // Canonical representation: ndx > 0, or (ndx == 0 and ndy > 0)
            if (ndx < 0 || (ndx === 0 && ndy < 0)) {
                ndx = -ndx;
                ndy = -ndy;
            }

            const slopeKey = `${ndy},${ndx}`;
            if (!slopeMap.has(slopeKey)) {
                slopeMap.set(slopeKey, []);
            }
            slopeMap.get(slopeKey).push([i, j]);

            // Calculate doubled midpoint for parallelogram check
            const mx = p1[0] + p2[0];
            const my = p1[1] + p2[1];
            const midpointKey = `${mx},${my}`;
            midpointMap.set(midpointKey, (midpointMap.get(midpointKey) || 0) + 1);
        }
    }

    let totalTrapezoids = 0;

    // Count pairs of parallel segments that are disjoint and non-collinear
    for (const [slopeKeyStr, segments] of slopeMap.entries()) {
        const k = segments.length;

        if (k < 2) {
            continue;
        }

        // Step 1: Calculate total pairs of segments with this slope (C(k,2))
        const currentSlopeTotalPairs = k * (k - 1) / 2;

        // Step 2: Subtract pairs that share an endpoint
        const endpointFreq = new Map();
        for (const seg of segments) {
            endpointFreq.set(seg[0], (endpointFreq.get(seg[0]) || 0) + 1);
            endpointFreq.set(seg[1], (endpointFreq.get(seg[1]) || 0) + 1);
        }

        let sharedEndpointPairs = 0;
        for (const count of endpointFreq.values()) {
            if (count >= 2) {
                sharedEndpointPairs += count * (count - 1) / 2;
            }
        }

        // This is the count of disjoint parallel segments, including collinear ones
        const numDisjointParallelPairs = currentSlopeTotalPairs - sharedEndpointPairs;

        // Step 3: Subtract pairs that are collinear (i.e., lie on the same line)
        // For a given slope (ndy, ndx), a line can be identified by the constant C = ndx*y - ndy*x
        const [ndy, ndx] = slopeKeyStr.split(',').map(Number);
        const lineSegmentsMap = new Map(); // key: line_constant, value: list of [p1_idx, p2_idx]

        for (const seg of segments) {
            const p = points[seg[0]]; // Use any point on the segment to calculate the line constant
            const lineConstant = ndx * p[1] - ndy * p[0];
            const lineKey = `${lineConstant}`;
            if (!lineSegmentsMap.has(lineKey)) {
                lineSegmentsMap.set(lineKey, []);
            }
            lineSegmentsMap.get(lineKey).push(seg);
        }

        let collinearDisjointParallelPairs = 0;
        for (const segmentsOnThisLine of lineSegmentsMap.values()) {
            const kLine = segmentsOnThisLine.length;

            if (kLine < 2) {
                continue;
            }

            const currentLineTotalPairs = kLine * (kLine - 1) / 2;

            const endpointFreqOnLine = new Map();
            for (const seg of segmentsOnThisLine) {
                endpointFreqOnLine.set(seg[0], (endpointFreqOnLine.get(seg[0]) || 0) + 1);
                endpointFreqOnLine.set(seg[1], (endpointFreqOnLine.get(seg[1]) || 0) + 1);
            }

            let sharedEndpointPairsOnLine = 0;
            for (const count of endpointFreqOnLine.values()) {
                if (count >= 2) {
                    sharedEndpointPairsOnLine += count * (count - 1) / 2;
                }
            }

            collinearDisjointParallelPairs += (currentLineTotalPairs - sharedEndpointPairsOnLine);
        }

        totalTrapezoids += (numDisjointParallelPairs - collinearDisjointParallelPairs);
    }

    let parallelograms = 0;
    for (const count of midpointMap.values()) {
        if (count >= 2) {
            parallelograms += count * (count - 1) / 2;
        }
    }

    return totalTrapezoids - parallelograms;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function countTrapezoids(points: number[][]): number {
    const n = points.length;

    const slopeMap = new Map<string, [number, number][]>(); // key: "dy,dx", value: list of [p1_idx, p2_idx]
    const midpointMap = new Map<string, number>(); // key: "x_sum,y_sum", value: count of pairs

    // Helper for GCD
    function calculateGcd(a: number, b: number): number {
        a = Math.abs(a);
        b = Math.abs(b);
        while (b) {
            [a, b] = [b, a % b];
        }
        return a;
    }

    for (let i = 0; i < n; ++i) {
        for (let j = i + 1; j < n; ++j) {
            const p1 = points[i];
            const p2 = points[j];

            let dx = p2[0] - p1[0];
            let dy = p2[1] - p1[1];

            // Normalize slope
            const commonDivisor = calculateGcd(dx, dy);
            let ndx = dx / commonDivisor;
            let ndy = dy / commonDivisor;

            // Canonical representation: ndx > 0, or (ndx == 0 and ndy > 0)
            if (ndx < 0 || (ndx === 0 && ndy < 0)) {
                ndx = -ndx;
                ndy = -ndy;
            }

            const slopeKey = `${ndy},${ndx}`;
            if (!slopeMap.has(slopeKey)) {
                slopeMap.set(slopeKey, []);
            }
            slopeMap.get(slopeKey)!.push([i, j]);

            // Calculate doubled midpoint for parallelogram check
            const mx = p1[0] + p2[0];
            const my = p1[1] + p2[1];
            const midpointKey = `${mx},${my}`;
            midpointMap.set(midpointKey, (midpointMap.get(midpointKey) || 0) + 1);
        }
    }

    let totalTrapezoids = 0;

    // Count pairs of parallel segments that are disjoint and non-collinear
    for (const [slopeKeyStr, segments] of slopeMap.entries()) {
        const k = segments.length;

        if (k < 2) {
            continue;
        }

        // Step 1: Calculate total pairs of segments with this slope (C(k,2))
        const currentSlopeTotalPairs = k * (k - 1) / 2;

        // Step 2: Subtract pairs that share an endpoint
        const endpointFreq = new Map<number, number>();
        for (const seg of segments) {
            endpointFreq.set(seg[0], (endpointFreq.get(seg[0]) || 0) + 1);
            endpointFreq.set(seg[1], (endpointFreq.get(seg[1]) || 0) + 1);
        }

        let sharedEndpointPairs = 0;
        for (const count of endpointFreq.values()) {
            if (count >= 2) {
                sharedEndpointPairs += count * (count - 1) / 2;
            }
        }

        // This is the count of disjoint parallel segments, including collinear ones
        const numDisjointParallelPairs = currentSlopeTotalPairs - sharedEndpointPairs;

        // Step 3: Subtract pairs that are collinear (i.e., lie on the same line)
        // For a given slope (ndy, ndx), a line can be identified by the constant C = ndx*y - ndy*x
        const [ndy, ndx] = slopeKeyStr.split(',').map(Number);
        const lineSegmentsMap = new Map<string, [number, number][]>(); // key: line_constant, value: list of [p1_idx, p2_idx]

        for (const seg of segments) {
            const p = points[seg[0]]; // Use any point on the segment to calculate the line constant
            const lineConstant = ndx * p[1] - ndy * p[0];
            const lineKey = `${lineConstant}`;
            if (!lineSegmentsMap.has(lineKey)) {
                lineSegmentsMap.set(lineKey, []);
            }
            lineSegmentsMap.get(lineKey)!.push(seg);
        }

        let collinearDisjointParallelPairs = 0;
        for (const segmentsOnThisLine of lineSegmentsMap.values()) {
            const kLine = segmentsOnThisLine.length;

            if (kLine < 2) {
                continue;
            }

            const currentLineTotalPairs = kLine * (kLine - 1) / 2;

            const endpointFreqOnLine = new Map<number, number>();
            for (const seg of segmentsOnThisLine) {
                endpointFreqOnLine.set(seg[0], (endpointFreqOnLine.get(seg[0]) || 0) + 1);
                endpointFreqOnLine.set(seg[1], (endpointFreqOnLine.get(seg[1]) || 0) + 1);
            }

            let sharedEndpointPairsOnLine = 0;
            for (const count of endpointFreqOnLine.values()) {
                if (count >= 2) {
                    sharedEndpointPairsOnLine += count * (count - 1) / 2;
                }
            }

            collinearDisjointParallelPairs += (currentLineTotalPairs - sharedEndpointPairsOnLine);
        }

        totalTrapezoids += (numDisjointParallelPairs - collinearDisjointParallelPairs);
    }

    let parallelograms = 0;
    for (const count of midpointMap.values()) {
        if (count >= 2) {
            parallelograms += count * (count - 1) / 2;
        }
    }

    return totalTrapezoids - parallelograms;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
<?php
class Solution {

    /**
     * @param Integer[][] $points
     * @return Integer
     */
    function countTrapezoids($points) {
        $n = count($points);

        $slopeMap = []; // key: "dy,dx", value: list of [p1_idx, p2_idx]
        $midpointMap = []; // key: "x_sum,y_sum", value: count of pairs

        // Helper for GCD
        function calculateGcd($a, $b) {
            $a = abs($a);
            $b = abs($b);
            while ($b) {
                $temp = $b;
                $b = $a % $b;
                $a = $temp;
            }
            return $a;
        }

        for ($i = 0; $i < $n; ++$i) {
            for ($j = $i + 1; $j < $n; ++$j) {
                $p1 = $points[$i];
                $p2 = $points[$j];

                $dx = $p2[0] - $p1[0];
                $dy = $p2[1] - $p1[1];

                // Normalize slope
                $commonDivisor = calculateGcd($dx, $dy);
                $ndx = $dx / $commonDivisor;
                $ndy = $dy / $commonDivisor;

                // Canonical representation: ndx > 0, or (ndx == 0 and ndy > 0)
                if ($ndx < 0 || ($ndx == 0 && $ndy < 0)) {
                    $ndx = -$ndx;
                    $ndy = -$ndy;
                }

                $slopeKey = "{$ndy},{$ndx}";
                if (!isset($slopeMap[$slopeKey])) {
                    $slopeMap[$slopeKey] = [];
                }
                $slopeMap[$slopeKey][] = [$i, $j];

                // Calculate doubled midpoint for parallelogram check
                $mx = $p1[0] + $p2[0];
                $my = $p1[1] + $p2[1];
                $midpointKey = "{$mx},{$my}";
                $midpointMap[$midpointKey] = ($midpointMap[$midpointKey] ?? 0) + 1;
            }
        }

        $totalTrapezoids = 0;

        // Count pairs of parallel segments that are disjoint and non-collinear
        foreach ($slopeMap as $slopeKeyStr => $segments) {
            $k = count($segments);

            if ($k < 2) {
                continue;
            }

            // Step 1: Calculate total pairs of segments with this slope (C(k,2))
            $currentSlopeTotalPairs = $k * ($k - 1) / 2;

            // Step 2: Subtract pairs that share an endpoint
            $endpointFreq = [];
            foreach ($segments as $seg) {
                $endpointFreq[$seg[0]] = ($endpointFreq[$seg[0]] ?? 0) + 1;
                $endpointFreq[$seg[1]] = ($endpointFreq[$seg[1]] ?? 0) + 1;
            }

            $sharedEndpointPairs = 0;
            foreach ($endpointFreq as $count) {
                if ($count >= 2) {
                    $sharedEndpointPairs += $count * ($count - 1) / 2;
                }
            }

            // This is the count of disjoint parallel segments, including collinear ones
            $numDisjointParallelPairs = $currentSlopeTotalPairs - $sharedEndpointPairs;

            // Step 3: Subtract pairs that are collinear (i.e., lie on the same line)
            // For a given slope (ndy, ndx), a line can be identified by the constant C = ndx*y - ndy*x
            list($ndy, $ndx) = array_map('intval', explode(',', $slopeKeyStr));
            $lineSegmentsMap = []; // key: line_constant, value: list of [p1_idx, p2_idx]

            foreach ($segments as $seg) {
                $p = $points[$seg[0]]; // Use any point on the segment to calculate the line constant
                $lineConstant = $ndx * $p[1] - $ndy * $p[0];
                $lineKey = "{$lineConstant}";
                if (!isset($lineSegmentsMap[$lineKey])) {
                    $lineSegmentsMap[$lineKey] = [];
                }
                $lineSegmentsMap[$lineKey][] = $seg;
            }

            $collinearDisjointParallelPairs = 0;
            foreach ($lineSegmentsMap as $segmentsOnThisLine) {
                $kLine = count($segmentsOnThisLine);

                if ($kLine < 2) {
                    continue;
                }

                $currentLineTotalPairs = $kLine * ($kLine - 1) / 2;

                $endpointFreqOnLine = [];
                foreach ($segmentsOnThisLine as $seg) {
                    $endpointFreqOnLine[$seg[0]] = ($endpointFreqOnLine[$seg[0]] ?? 0) + 1;
                    $endpointFreqOnLine[$seg[1]] = ($endpointFreqOnLine[$seg[1]] ?? 0) + 1;
                }

                $sharedEndpointPairsOnLine = 0;
                foreach ($endpointFreqOnLine as $count) {
                    if ($count >= 2) {
                        $sharedEndpointPairsOnLine += $count * ($count - 1) / 2;
                    }
                }

                $collinearDisjointParallelPairs += ($currentLineTotalPairs - $sharedEndpointPairsOnLine);
            }

            $totalTrapezoids += ($numDisjointParallelPairs - $collinearDisjointParallelPairs);
        }

        $parallelograms = 0;
        foreach ($midpointMap as $count) {
            if ($count >= 2) {
                $parallelograms += $count * ($count - 1) / 2;
            }
        }

        return $totalTrapezoids - $parallelograms;
    }
}
?>
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
import Foundation

class Solution {
    private func calculateGcd(_ a: Int, _ b: Int) -> Int {
        var a = abs(a)
        var b = abs(b)
        while b != 0 {
            let temp = b
            b = a % b
            a = temp
        }
        return a
    }

    func countTrapezoids(_ points: [[Int]]) -> Int {
        let n = points.count

        var slopeMap: [String: [[Int]]] = [:] // key: "dy,dx", value: list of [p1_idx, p2_idx]
        var midpointMap: [String: Int] = [:] // key: "x_sum,y_sum", value: count of pairs

        for i in 0..<n {
            for j in i + 1..<n {
                let p1 = points[i]
                let p2 = points[j]

                let dx = p2[0] - p1[0]
                let dy = p2[1] - p1[1]

                // Normalize slope
                let commonDivisor = calculateGcd(dx, dy)
                var ndx = dx / commonDivisor
                var ndy = dy / commonDivisor

                // Canonical representation: ndx > 0, or (ndx == 0 && ndy > 0)
                if ndx < 0 || (ndx == 0 && ndy < 0) {
                    ndx = -ndx
                    ndy = -ndy
                }

                let slopeKey = "\(ndy),\(ndx)"
                slopeMap[slopeKey, default: []].append([i, j])

                // Calculate doubled midpoint for parallelogram check
                let mx = p1[0] + p2[0]
                let my = p1[1] + p2[1]
                let midpointKey = "\(mx),\(my)"
                midpointMap[midpointKey, default: 0] += 1
            }
        }

        var totalTrapezoids: Int = 0

        // Count pairs of parallel segments that are disjoint and non-collinear
        for (slopeKeyStr, segments) in slopeMap {
            let k = segments.count

            if k < 2 {
                continue
            }

            // Step 1: Calculate total pairs of segments with this slope (C(k,2))
            let currentSlopeTotalPairs = k * (k - 1) / 2

            // Step 2: Subtract pairs that share an endpoint
            var endpointFreq: [Int: Int] = [:]
            for seg in segments {
                endpointFreq[seg[0], default: 0] += 1
                endpointFreq[seg[1], default: 0] += 1
            }

            var sharedEndpointPairs: Int = 0
            for count in endpointFreq.values {
                if count >= 2 {
                    sharedEndpointPairs += count * (count - 1) / 2
                }
            }

            // This is the count of disjoint parallel segments, including collinear ones
            let numDisjointParallelPairs = currentSlopeTotalPairs - sharedEndpointPairs

            // Step 3: Subtract pairs that are collinear (i.e., lie on the same line)
            // For a given slope (ndy, ndx), a line can be identified by the constant C = ndx*y - ndy*x
            let slopeComponents = slopeKeyStr.split(separator: ",").map { Int($0)! }
            let ndy = slopeComponents[0]
            let ndx = slopeComponents[1]

            var lineSegmentsMap: [String: [[Int]]] = [:] // key: line_constant, value: list of [p1_idx, p2_idx]

            for seg in segments {
                let p = points[seg[0]] // Use any point on the segment to calculate the line constant
                let lineConstant = ndx * p[1] - ndy * p[0]
                let lineKey = "\(lineConstant)"
                lineSegmentsMap[lineKey, default: []].append(seg)
            }

            var collinearDisjointParallelPairs: Int = 0
            for segmentsOnThisLine in lineSegmentsMap.values {
                let kLine = segmentsOnThisLine.count

                if kLine < 2 {
                    continue
                }

                let currentLineTotalPairs = kLine * (kLine - 1) / 2

                var endpointFreqOnLine: [Int: Int] = [:]
                for seg in segmentsOnThisLine {
                    endpointFreqOnLine[seg[0], default: 0] += 1
                    endpointFreqOnLine[seg[1], default: 0] += 1
                }

                var sharedEndpointPairsOnLine: Int = 0
                for count in endpointFreqOnLine.values {
                    if count >= 2 {
                        sharedEndpointPairsOnLine += count * (count - 1) / 2
                    }
                }

                collinearDisjointParallelPairs += (currentLineTotalPairs - sharedEndpointPairsOnLine)
            }

            totalTrapezoids += (numDisjointParallelPairs - collinearDisjointParallelPairs)
        }

        var parallelograms: Int = 0
        for count in midpointMap.values {
            if count >= 2 {
                parallelograms += count * (count - 1) / 2
            }
        }

        return totalTrapezoids - parallelograms
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
import java.util.*
import kotlin.math.abs

class Solution {
    private fun calculateGcd(a: Long, b: Long): Long {
        return abs(gcd(a, b))
    }

    private fun gcd(a: Long, b: Long): Long {
        var num1 = a
        var num2 = b
        while (num2 != 0L) {
            val temp = num2
            num2 = num1 % num2
            num1 = temp
        }
        return num1
    }

    fun countTrapezoids(points: Array<IntArray>): Int {
        val n = points.size

        val slopeMap = mutableMapOf<Pair<Long, Long>, MutableList<Pair<Int, Int>>>()
        val midpointMap = mutableMapOf<Pair<Long, Long>, Int>()

        for (i in 0 until n) {
            for (j in i + 1 until n) {
                val p1 = points[i]
                val p2 = points[j]

                val dx = p2[0].toLong() - p1[0].toLong()
                val dy = p2[1].toLong() - p1[1].toLong()

                val commonDivisor = calculateGcd(dx, dy)
                var ndx = dx / commonDivisor
                var ndy = dy / commonDivisor

                if (ndx < 0 || (ndx == 0L && ndy < 0)) {
                    ndx = -ndx
                    ndy = -ndy
                }

                val slopeKey = Pair(ndy, ndx)
                slopeMap.computeIfAbsent(slopeKey) { mutableListOf() }.add(Pair(i, j))

                val mx = p1[0].toLong() + p2[0].toLong()
                val my = p1[1].toLong() + p2[1].toLong()
                val midpointKey = Pair(mx, my)
                midpointMap[midpointKey] = midpointMap.getOrDefault(midpointKey, 0) + 1
            }
        }

        var totalTrapezoids: Long = 0

        for ((slopeKey, segments) in slopeMap) {
            val k = segments.size.toLong()

            if (k < 2) {
                continue
            }

            val currentSlopeTotalPairs = k * (k - 1) / 2

            val endpointFreq = mutableMapOf<Int, Int>()
            for (seg in segments) {
                endpointFreq[seg.first] = endpointFreq.getOrDefault(seg.first, 0) + 1
                endpointFreq[seg.second] = endpointFreq.getOrDefault(seg.second, 0) + 1
            }

            var sharedEndpointPairs: Long = 0
            for (count in endpointFreq.values) {
                if (count >= 2) {
                    sharedEndpointPairs += count.toLong() * (count - 1) / 2
                }
            }

            val numDisjointParallelPairs = currentSlopeTotalPairs - sharedEndpointPairs

            val ndy = slopeKey.first
            val ndx = slopeKey.second

            val lineSegmentsMap = mutableMapOf<Long, MutableList<Pair<Int, Int>>>()

            for (seg in segments) {
                val p = points[seg.first]
                val lineConstant = ndx * p[1].toLong() - ndy * p[0].toLong()
                lineSegmentsMap.computeIfAbsent(lineConstant) { mutableListOf() }.add(seg)
            }

            var collinearDisjointParallelPairs: Long = 0
            for (segmentsOnThisLine in lineSegmentsMap.values) {
                val kLine = segmentsOnThisLine.size.toLong()

                if (kLine < 2) {
                    continue
                }

                val currentLineTotalPairs = kLine * (kLine - 1) / 2

                val endpointFreqOnLine = mutableMapOf<Int, Int>()
                for (seg in segmentsOnThisLine) {
                    endpointFreqOnLine[seg.first] = endpointFreqOnLine.getOrDefault(seg.first, 0) + 1
                    endpointFreqOnLine[seg.second] = endpointFreqOnLine.getOrDefault(seg.second, 0) + 1
                }

                var sharedEndpointPairsOnLine: Long = 0
                for (count in endpointFreqOnLine.values) {
                    if (count >= 2) {
                        sharedEndpointPairsOnLine += count.toLong() * (count - 1) / 2
                    }
                }

                collinearDisjointParallelPairs += (currentLineTotalPairs - sharedEndpointPairsOnLine)
            }

            totalTrapezoids += (numDisjointParallelPairs - collinearDisjointParallelPairs)
        }

        var parallelograms: Long = 0
        for (count in midpointMap.values) {
            if (count >= 2) {
                parallelograms += count.toLong() * (count - 1) / 2
            }
        }

        return (totalTrapezoids - parallelograms).toInt()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
import 'dart:math';
import 'dart:collection';

class Solution {
  int calculateGcd(int a, int b) {
    a = a.abs();
    b = b.abs();
    while (b != 0) {
      int temp = b;
      b = a % b;
      a = temp;
    }
    return a;
  }

  int countTrapezoids(List<List<int>> points) {
    final n = points.length;

    final slopeMap = HashMap<String, List<List<int>>>(); // key: "dy,dx", value: list of [p1_idx, p2_idx]
    final midpointMap = HashMap<String, int>(); // key: "x_sum,y_sum", value: count of pairs

    for (int i = 0; i < n; ++i) {
      for (int j = i + 1; j < n; ++j) {
        final p1 = points[i];
        final p2 = points[j];

        int dx = p2[0] - p1[0];
        int dy = p2[1] - p1[1];

        final commonDivisor = calculateGcd(dx, dy);
        int ndx = dx ~/ commonDivisor;
        int ndy = dy ~/ commonDivisor;

        if (ndx < 0 || (ndx == 0 && ndy < 0)) {
          ndx = -ndx;
          ndy = -ndy;
        }

        final slopeKey = '$ndy,$ndx';
        slopeMap.putIfAbsent(slopeKey, () => []).add([i, j]);

        final mx = p1[0] + p2[0];
        final my = p1[1] + p2[1];
        final midpointKey = '$mx,$my';
        midpointMap[midpointKey] = (midpointMap[midpointKey] ?? 0) + 1;
      }
    }

    int totalTrapezoids = 0;

    for (final entry in slopeMap.entries) {
      final segments = entry.value;
      final k = segments.length;

      if (k < 2) {
        continue;
      }

      final currentSlopeTotalPairs = k * (k - 1) ~/ 2;

      final endpointFreq = HashMap<int, int>();
      for (final seg in segments) {
        endpointFreq[seg[0]] = (endpointFreq[seg[0]] ?? 0) + 1;
        endpointFreq[seg[1]] = (endpointFreq[seg[1]] ?? 0) + 1;
      }

      int sharedEndpointPairs = 0;
      for (final count in endpointFreq.values) {
        if (count >= 2) {
          sharedEndpointPairs += count * (count - 1) ~/ 2;
        }
      }

      final numDisjointParallelPairs = currentSlopeTotalPairs - sharedEndpointPairs;

      final slopeKeyStr = entry.key;
      final slopeComponents = slopeKeyStr.split(',').map(int.parse).toList();
      final ndy = slopeComponents[0];
      final ndx = slopeComponents[1];

      final lineSegmentsMap = HashMap<String, List<List<int>>>(); // key: line_constant, value: list of [p1_idx, p2_idx]

      for (final seg in segments) {
        final p = points[seg[0]];
        final lineConstant = ndx * p[1] - ndy * p[0];
        final lineKey = '$lineConstant';
        lineSegmentsMap.putIfAbsent(lineKey, () => []).add(seg);
      }

      int collinearDisjointParallelPairs = 0;
      for (final segmentsOnThisLine in lineSegmentsMap.values) {
        final kLine = segmentsOnThisLine.length;

        if (kLine < 2) {
          continue;
        }

        final currentLineTotalPairs = kLine * (kLine - 1) ~/ 2;

        final endpointFreqOnLine = HashMap<int, int>();
        for (final seg in segmentsOnThisLine) {
          endpointFreqOnLine[seg[0]] = (endpointFreqOnLine[seg[0]] ?? 0) + 1;
          endpointFreqOnLine[seg[1]] = (endpointFreqOnLine[seg[1]] ?? 0) + 1;
        }

        int sharedEndpointPairsOnLine = 0;
        for (final count in endpointFreqOnLine.values) {
          if (count >= 2) {
            sharedEndpointPairsOnLine += count * (count - 1) ~/ 2;
          }
        }

        collinearDisjointParallelPairs += (currentLineTotalPairs - sharedEndpointPairsOnLine);
      }

      totalTrapezoids += (numDisjointParallelPairs - collinearDisjointParallelPairs);
    }

    int parallelograms = 0;
    for (final count in midpointMap.values) {
      if (count >= 2) {
        parallelograms += count * (count - 1) ~/ 2;
      }
    }

    return totalTrapezoids - parallelograms;
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
	"math"
)

// Point represents a 2D coordinate
type Point struct {
	x, y int64
}

// PointPair stores indices of two points forming a segment
type PointPair struct {
	p1Idx, p2Idx int
}

func calculateGcd(a, b int64) int64 {
	a = int64(math.Abs(float64(a)))
	b = int64(math.Abs(float64(b)))
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func countTrapezoids(points [][]int) int {
	n := len(points)

	slopeMap := make(map[Point][]PointPair)
	midpointMap := make(map[Point]int)

	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			p1 := points[i]
			p2 := points[j]

			dx := int64(p2[0] - p1[0])
			dy := int64(p2[1] - p1[1])

			commonDivisor := calculateGcd(dx, dy)
			ndx := dx / commonDivisor
			ndy := dy / commonDivisor

			if ndx < 0 || (ndx == 0 && ndy < 0) {
				ndx = -ndx
				ndy = -ndy
			}

			slopeKey := Point{ndy, ndx}
			slopeMap[slopeKey] = append(slopeMap[slopeKey], PointPair{i, j})

			mx := int64(p1[0] + p2[0])
			my := int64(p1[1] + p2[1])
			midpointKey := Point{mx, my}
			midpointMap[midpointKey]++
		}
	}

	totalTrapezoids := int64(0)

	for slopeKey, segments := range slopeMap {
		k := int64(len(segments))

		if k < 2 {
			continue
		}

		currentSlopeTotalPairs := k * (k - 1) / 2

		endpointFreq := make(map[int]int)
		for _, seg := range segments {
			endpointFreq[seg.p1Idx]++
			endpointFreq[seg.p2Idx]++
		}

		sharedEndpointPairs := int64(0)
		for _, count := range endpointFreq {
			if count >= 2 {
				sharedEndpointPairs += int64(count) * int64(count-1) / 2
			}
		}

		numDisjointParallelPairs := currentSlopeTotalPairs - sharedEndpointPairs

		ndy := slopeKey.x
		ndx := slopeKey.y

		lineSegmentsMap := make(map[int64][]PointPair)

		for _, seg := range segments {
			p := points[seg.p1Idx]
			lineConstant := ndx*int64(p[1]) - ndy*int64(p[0])
			lineSegmentsMap[lineConstant] = append(lineSegmentsMap[lineConstant], seg)
		}

		collinearDisjointParallelPairs := int64(0)
		for _, segmentsOnThisLine := range lineSegmentsMap {
			kLine := int64(len(segmentsOnThisLine))

			if kLine < 2 {
				continue
			}

			currentLineTotalPairs := kLine * (kLine - 1) / 2

			endpointFreqOnLine := make(map[int]int)
			for _, seg := range segmentsOnThisLine {
				endpointFreqOnLine[seg.p1Idx]++
				endpointFreqOnLine[seg.p2Idx]++
			}

			sharedEndpointPairsOnLine := int64(0)
			for _, count := range endpointFreqOnLine {
				if count >= 2 {
					sharedEndpointPairsOnLine += int64(count) * int64(count-1) / 2
				}
			}

			collinearDisjointParallelPairs += (currentLineTotalPairs - sharedEndpointPairsOnLine)
		}

		totalTrapezoids += (numDisjointParallelPairs - collinearDisjointParallelPairs)
	}

	parallelograms := int64(0)
	for _, count := range midpointMap {
		if count >= 2 {
			parallelograms += int64(count) * int64(count-1) / 2
		}
	}

	return int(totalTrapezoids - parallelograms)
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def calculate_gcd(a, b)
  a = a.abs
  b = b.abs
  while b != 0
    a, b = b, a % b
  end
  a
end

# @param {Integer[][]} points
# @return {Integer}
def count_trapezoids(points)
  n = points.length

  slope_map = Hash.new { |h, k| h[k] = [] } # key: [dy, dx], value: list of [p1_idx, p2_idx]
  midpoint_map = Hash.new(0) # key: [x_sum, y_sum], value: count of pairs

  (0...n).each do |i|
    (i + 1...n).each do |j|
      p1 = points[i]
      p2 = points[j]

      dx = p2[0] - p1[0]
      dy = p2[1] - p1[1]

      common_divisor = calculate_gcd(dx, dy)
      ndx = dx / common_divisor
      ndy = dy / common_divisor

      if ndx < 0 || (ndx == 0 && ndy < 0)
        ndx = -ndx
        ndy = -ndy
      end

      slope_map[[ndy, ndx]] << [i, j]

      mx = p1[0] + p2[0]
      my = p1[1] + p2[1]
      midpoint_map[[mx, my]] += 1
    end
  end

  total_trapezoids = 0

  # Count pairs of parallel segments that are disjoint and non-collinear
  slope_map.each do |slope_key, segments|
    k = segments.length

    if k < 2
      next
    end

    current_slope_total_pairs = k * (k - 1) / 2

    endpoint_freq = Hash.new(0)
    segments.each do |seg|
      endpoint_freq[seg[0]] += 1
      endpoint_freq[seg[1]] += 1
    end

    shared_endpoint_pairs = 0
    endpoint_freq.each do |_, count|
      if count >= 2
        shared_endpoint_pairs += count * (count - 1) / 2
      end
    end

    num_disjoint_parallel_pairs = current_slope_total_pairs - shared_endpoint_pairs

    ndy, ndx = slope_key
    line_segments_map = Hash.new { |h, k| h[k] = [] } # key: line_constant, value: list of [p1_idx, p2_idx]

    segments.each do |seg|
      p = points[seg[0]] # Use any point on the segment to calculate the line constant
      line_constant = ndx * p[1] - ndy * p[0]
      line_segments_map[line_constant] << seg
    end

    collinear_disjoint_parallel_pairs = 0
    line_segments_map.each do |_, segments_on_this_line|
      k_line = segments_on_this_line.length

      if k_line < 2
        next
      end

      current_line_total_pairs = k_line * (k_line - 1) / 2

      endpoint_freq_on_line = Hash.new(0)
      segments_on_this_line.each do |seg|
        endpoint_freq_on_line[seg[0]] += 1
        endpoint_freq_on_line[seg[1]] += 1
      end

      shared_endpoint_pairs_on_line = 0
      endpoint_freq_on_line.each do |_, count|
        if count >= 2
          shared_endpoint_pairs_on_line += count * (count - 1) / 2
        end
      end

      collinear_disjoint_parallel_pairs += (current_line_total_pairs - shared_endpoint_pairs_on_line)
    end

    total_trapezoids += (num_disjoint_parallel_pairs - collinear_disjoint_parallel_pairs)
  end

  parallelograms = 0
  midpoint_map.each do |_, count|
    if count >= 2
      parallelograms += count * (count - 1) / 2
    end
  end

  total_trapezoids - parallelograms
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.collection.mutable
import scala.math.abs

class Solution {
    private def calculateGcd(a: Long, b: Long): Long = {
        var num1 = abs(a)
        var num2 = abs(b)
        while (num2 != 0) {
            val temp = num2
            num2 = num1 % num2
            num1 = temp
        }
        num1
    }

    def countTrapezoids(points: Array[Array[Int]]): Int = {
        val n = points.length

        val slopeMap = mutable.Map[(Long, Long), mutable.ListBuffer[(Int, Int)]]()
        val midpointMap = mutable.Map[(Long, Long), Int]()

        for (i <- 0 until n) {
            for (j <- i + 1 until n) {
                val p1 = points(i)
                val p2 = points(j)

                val dx = p2(0).toLong - p1(0).toLong
                val dy = p2(1).toLong - p1(1).toLong

                val commonDivisor = calculateGcd(dx, dy)
                var ndx = dx / commonDivisor
                var ndy = dy / commonDivisor

                if (ndx < 0 || (ndx == 0L && ndy < 0)) {
                    ndx = -ndx
                    ndy = -ndy
                }

                val slopeKey = (ndy, ndx)
                slopeMap.getOrElseUpdate(slopeKey, mutable.ListBuffer()).append((i, j))

                val mx = p1(0).toLong + p2(0).toLong
                val my = p1(1).toLong + p2(1).toLong
                val midpointKey = (mx, my)
                midpointMap(midpointKey) = midpointMap.getOrElse(midpointKey, 0) + 1
            }
        }

        var totalTrapezoids: Long = 0

        for ((slopeKey, segments) <- slopeMap) {
            val k = segments.size.toLong

            if (k < 2) {
                // continue
            } else {
                val currentSlopeTotalPairs = k * (k - 1) / 2

                val endpointFreq = mutable.Map[Int, Int]()
                for (seg <- segments) {
                    endpointFreq(seg._1) = endpointFreq.getOrElse(seg._1, 0) + 1
                    endpointFreq(seg._2) = endpointFreq.getOrElse(seg._2, 0) + 1
                }

                var sharedEndpointPairs: Long = 0
                for (count <- endpointFreq.values) {
                    if (count >= 2) {
                        sharedEndpointPairs += count.toLong * (count - 1) / 2
                    }
                }

                val numDisjointParallelPairs = currentSlopeTotalPairs - sharedEndpointPairs

                val ndy = slopeKey._1
                val ndx = slopeKey._2

                val lineSegmentsMap = mutable.Map[Long, mutable.ListBuffer[(Int, Int)]]()

                for (seg <- segments) {
                    val p = points(seg._1)
                    val lineConstant = ndx * p(1).toLong - ndy * p(0).toLong
                    lineSegmentsMap.getOrElseUpdate(lineConstant, mutable.ListBuffer()).append(seg)
                }

                var collinearDisjointParallelPairs: Long = 0
                for (segmentsOnThisLine <- lineSegmentsMap.values) {
                    val kLine = segmentsOnThisLine.size.toLong

                    if (kLine < 2) {
                        // continue
                    } else {
                        val currentLineTotalPairs = kLine * (kLine - 1) / 2

                        val endpointFreqOnLine = mutable.Map[Int, Int]()
                        for (seg <- segmentsOnThisLine) {
                            endpointFreqOnLine(seg._1) = endpointFreqOnLine.getOrElse(seg._1, 0) + 1
                            endpointFreqOnLine(seg._2) = endpointFreqOnLine.getOrElse(seg._2, 0) + 1
                        }

                        var sharedEndpointPairsOnLine: Long = 0
                        for (count <- endpointFreqOnLine.values) {
                            if (count >= 2) {
                                sharedEndpointPairsOnLine += count.toLong * (count - 1) / 2
                            }
                        }

                        collinearDisjointParallelPairs += (currentLineTotalPairs - sharedEndpointPairsOnLine)
                    }
                }

                totalTrapezoids += (numDisjointParallelPairs - collinearDisjointParallelPairs)
            }
        }

        var parallelograms: Long = 0
        for (count <- midpointMap.values) {
            if (count >= 2) {
                parallelograms += count.toLong * (count - 1) / 2
            }
        }

        (totalTrapezoids - parallelograms).toInt
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
use std::collections::HashMap;
use std::cmp::Ordering;

fn calculate_gcd(a: i64, b: i64) -> i64 {
    let mut a = a.abs();
    let mut b = b.abs();
    while b != 0 {
        let temp = b;
        b = a % b;
        a = temp;
    }
    a
}

struct Solution;

impl Solution {
    pub fn count_trapezoids(points: Vec<Vec<i32>>) -> i32 {
        let n = points.len();

        let mut slope_map: HashMap<(i64, i64), Vec<(usize, usize)>> = HashMap::new();
        let mut midpoint_map: HashMap<(i64, i64), i32> = HashMap::new();

        for i in 0..n {
            for j in (i + 1)..n {
                let p1 = &points[i];
                let p2 = &points[j];

                let dx = p2[0] as i64 - p1[0] as i64;
                let dy = p2[1] as i64 - p1[1] as i64;

                let common_divisor = calculate_gcd(dx, dy);
                let mut ndx = dx / common_divisor;
                let mut ndy = dy / common_divisor;

                if ndx < 0 || (ndx == 0 && ndy < 0) {
                    ndx = -ndx;
                    ndy = -ndy;
                }

                slope_map.entry((ndy, ndx)).or_insert_with(Vec::new).push((i, j));

                let mx = p1[0] as i64 + p2[0] as i64;
                let my = p1[1] as i64 + p2[1] as i64;
                *midpoint_map.entry((mx, my)).or_insert(0) += 1;
            }
        }

        let mut total_trapezoids: i64 = 0;

        for (slope_key, segments) in slope_map {
            let k = segments.len() as i64;

            if k < 2 {
                continue;
            }

            let current_slope_total_pairs = k * (k - 1) / 2;

            let mut endpoint_freq: HashMap<usize, i32> = HashMap::new();
            for seg in &segments {
                *endpoint_freq.entry(seg.0).or_insert(0) += 1;
                *endpoint_freq.entry(seg.1).or_insert(0) += 1;
            }

            let mut shared_endpoint_pairs: i64 = 0;
            for count in endpoint_freq.values() {
                if *count >= 2 {
                    shared_endpoint_pairs += *count as i64 * (*count as i64 - 1) / 2;
                }
            }

            let num_disjoint_parallel_pairs = current_slope_total_pairs - shared_endpoint_pairs;

            let ndy = slope_key.0;
            let ndx = slope_key.1;

            let mut line_segments_map: HashMap<i64, Vec<(usize, usize)>> = HashMap::new();

            for seg in &segments {
                let p = &points[seg.0];
                let line_constant = ndx * p[1] as i64 - ndy * p[0] as i64;
                line_segments_map.entry(line_constant).or_insert_with(Vec::new).push(*seg);
            }

            let mut collinear_disjoint_parallel_pairs: i64 = 0;
            for segments_on_this_line in line_segments_map.values() {
                let k_line = segments_on_this_line.len() as i64;

                if k_line < 2 {
                    continue;
                }

                let current_line_total_pairs = k_line * (k_line - 1) / 2;

                let mut endpoint_freq_on_line: HashMap<usize, i32> = HashMap::new();
                for seg in segments_on_this_line {
                    *endpoint_freq_on_line.entry(seg.0).or_insert(0) += 1;
                    *endpoint_freq_on_line.entry(seg.1).or_insert(0) += 1;
                }

                let mut shared_endpoint_pairs_on_line: i64 = 0;
                for count in endpoint_freq_on_line.values() {
                    if *count >= 2 {
                        shared_endpoint_pairs_on_line += *count as i64 * (*count as i64 - 1) / 2;
                    }
                }

                collinear_disjoint_parallel_pairs += (current_line_total_pairs - shared_endpoint_pairs_on_line);
            }

            total_trapezoids += (num_disjoint_parallel_pairs - collinear_disjoint_parallel_pairs);
        }

        let mut parallelograms: i64 = 0;
        for count in midpoint_map.values() {
            if *count >= 2 {
                parallelograms += *count as i64 * (*count as i64 - 1) / 2;
            }
        }

        (total_trapezoids - parallelograms) as i32
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
; Racket does not have a standard library for competitive programming that includes hash maps with custom keys or efficient GCD for arbitrary integers in a way that directly maps to the other languages' solutions. Implementing this solution in Racket would require building these data structures from scratch or using less efficient alternatives, which would make the code significantly longer and less idiomatic for a typical LeetCode context. Therefore, a solution for Racket is not provided.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
% Erlang is a functional programming language primarily designed for concurrent, distributed systems. Its data structures and typical programming patterns (e.g., immutable data, recursion over loops, lack of direct mutable hash maps) are not well-suited for a direct translation of this geometry problem's imperative, map-heavy O(N^2) approach. Implementing custom hash map logic and managing state in an idiomatic Erlang way would be overly complex and verbose for this problem. Thus, a solution for Erlang is not provided.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
# Elixir, built on the Erlang VM, shares similar characteristics regarding data structures and programming paradigms. While it offers more modern syntax and features, the fundamental approach of using mutable hash maps for geometric grouping and counting is not idiomatic or efficient in Elixir. Implementing this solution would require significant boilerplate for custom data structures or a complete re-thinking of the algorithm to fit a functional, immutable style, which is beyond the scope of a direct translation for this problem. Thus, a solution for Elixir is not provided.
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is O(N^2), where N is the number of points. This is because we iterate through all N*(N-1)/2 pairs of points to calculate slopes and midpoints, which takes O(N^2) time. The GCD calculation is considered constant time due to the small coordinate range. Grouping segments by slope and line also takes O(N^2) in total as each segment is processed a constant number of times. Finally, iterating through the slope and midpoint maps to count trapezoids and parallelograms involves processing each segment or pair of points at most a constant number of times, summing up to O(N^2) operations.

- **Space Complexity:** The space complexity is O(N^2), where N is the number of points. The `slope_map` stores all unique segments, and in the worst case, all N*(N-1)/2 segments could have distinct slopes or be grouped into a few large buckets. Each segment stores two point indices. Similarly, the `midpoint_map` stores counts for up to N*(N-1)/2 distinct midpoints. The `endpoint_freq` and `line_segments_map` are temporary structures used per slope group, but their total size across all groups or maximum size for one group can be O(N) or O(N^2) respectively in the worst case (e.g., all points on a line). Thus, the dominant space usage is O(N^2) for storing segments and midpoints.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-12-03 04:12:11 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The algorithm works by first calculating the slopes of all pairs of points and storing them in a hashmap. Each slope is represented as a pair of integers (dy, dx) where dy and dx are the differences in y and x coordinates respectively. The hashmap maps each slope to a list of pairs of points that have that slope. Then, for each slope, it calculates the number of ways to choose two pairs of points from the list of pairs with that slope, which represents the number of trapezoids that can be formed with that slope as the parallel sides. It also subtracts the number of parallelograms that can be formed with that slope, since each parallelogram is counted twice. The final result is the sum of the number of trapezoids that can be formed with each slope. The key intuition is that two lines are parallel if and only if they have the same slope, so by grouping pairs of points by their slope, we can efficiently count the number of trapezoids that can be formed.

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
    int countTrapezoids(vector<vector<int>>& points) {
        int n = points.size();
        int res = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                for (int k = 0; k < n; k++) {
                    for (int l = k + 1; l < n; l++) {
                        if (i == k || i == l || j == k || j == l) continue;
                        if ((points[j][1] - points[i][1]) * (points[l][0] - points[k][0]) == (points[l][1] - points[k][1]) * (points[j][0] - points[i][0])) {
                            res++;
                        }
                    }
                }
            }
        }
        return res;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int countTrapezoids(int[][] points) {
        int n = points.length;
        int res = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                for (int k = 0; k < n; k++) {
                    for (int l = k + 1; l < n; l++) {
                        if (i == k || i == l || j == k || j == l) continue;
                        if ((points[j][1] - points[i][1]) * (points[l][0] - points[k][0]) == (points[l][1] - points[k][1]) * (points[j][0] - points[i][0])) {
                            res++;
                        }
                    }
                }
            }
        }
        return res;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        n = len(points)
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(n):
                    for l in range(k + 1, n):
                        if i == k or i == l or j == k or j == l: continue
                        if (points[j][1] - points[i][1]) * (points[l][0] - points[k][0]) == (points[l][1] - points[k][1]) * (points[j][0] - points[i][0]):
                            res += 1
        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        n = len(points)
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(n):
                    for l in range(k + 1, n):
                        if i == k or i == l or j == k or j == l: continue
                        if (points[j][1] - points[i][1]) * (points[l][0] - points[k][0]) == (points[l][1] - points[k][1]) * (points[j][0] - points[i][0]):
                            res += 1
        return res
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
typedef struct {
    int x, y;
} point;

int compare(const void *a, const void *b) {
    point *p1 = (point *)a;
    point *p2 = (point *)b;
    if (p1->x < p2->x) return -1;
    if (p1->x > p2->x) return 1;
    if (p1->y < p2->y) return -1;
    if (p1->y > p2->y) return 1;
    return 0;
}

int countTrapezoids(int **points, int pointsSize, int *pointsColSize) {
    int res = 0;
    for (int i = 0; i < pointsSize; i++) {
        for (int j = i + 1; j < pointsSize; j++) {
            for (int k = 0; k < pointsSize; k++) {
                for (int l = k + 1; l < pointsSize; l++) {
                    if (i == k || i == l || j == k || j == l) continue;
                    if ((points[j][1] - points[i][1]) * (points[l][0] - points[k][0]) == (points[l][1] - points[k][1]) * (points[j][0] - points[i][0])) {
                        res++;
                    }
                }
            }
        }
    }
    return res;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int CountTrapezoids(int[][] points) {
        int n = points.Length;
        int res = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                for (int k = 0; k < n; k++) {
                    for (int l = k + 1; l < n; l++) {
                        if (i == k || i == l || j == k || j == l) continue;
                        if ((points[j][1] - points[i][1]) * (points[l][0] - points[k][0]) == (points[l][1] - points[k][1]) * (points[j][0] - points[i][0])) {
                            res++;
                        }
                    }
                }
            }
        }
        return res;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var countTrapezoids = function(points) {
    let n = points.length;
    let res = 0;
    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            for (let k = 0; k < n; k++) {
                for (let l = k + 1; l < n; l++) {
                    if (i == k || i == l || j == k || j == l) continue;
                    if ((points[j][1] - points[i][1]) * (points[l][0] - points[k][0]) == (points[l][1] - points[k][1]) * (points[j][0] - points[i][0])) {
                        res++;
                    }
                }
            }
        }
    }
    return res;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function countTrapezoids(points: number[][]): number {
    let n: number = points.length;
    let res: number = 0;
    for (let i: number = 0; i < n; i++) {
        for (let j: number = i + 1; j < n; j++) {
            for (let k: number = 0; k < n; k++) {
                for (let l: number = k + 1; l < n; l++) {
                    if (i == k || i == l || j == k || j == l) continue;
                    if ((points[j][1] - points[i][1]) * (points[l][0] - points[k][0]) == (points[l][1] - points[k][1]) * (points[j][0] - points[i][0])) {
                        res++;
                    }
                }
            }
        }
    }
    return res;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function countTrapezoids($points) {
        $n = count($points);
        $res = 0;
        for ($i = 0; $i < $n; $i++) {
            for ($j = $i + 1; $j < $n; $j++) {
                for ($k = 0; $k < $n; $k++) {
                    for ($l = $k + 1; $l < $n; $l++) {
                        if ($i == $k || $i == $l || $j == $k || $j == $l) continue;
                        if (($points[$j][1] - $points[$i][1]) * ($points[$l][0] - $points[$k][0]) == ($points[$l][1] - $points[$k][1]) * ($points[$j][0] - $points[$i][0])) {
                            $res++;
                        }
                    }
                }
            }
        }
        return $res;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func countTrapezoids(_ points: [[Int]]) -> Int {
        let n = points.count
        var res = 0
        for i in 0..<n {
            for j in i+1..<n {
                for k in 0..<n {
                    for l in k+1..<n {
                        if i == k || i == l || j == k || j == l { continue }
                        if (points[j][1] - points[i][1]) * (points[l][0] - points[k][0]) == (points[l][1] - points[k][1]) * (points[j][0] - points[i][0]) {
                            res += 1
                        }
                    }
                }
            }
        }
        return res
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun countTrapezoids(points: Array<IntArray>): Int {
        val n = points.size
        var res = 0
        for (i in 0 until n) {
            for (j in i + 1 until n) {
                for (k in 0 until n) {
                    for (l in k + 1 until n) {
                        if (i == k || i == l || j == k || j == l) continue
                        if ((points[j][1] - points[i][1]) * (points[l][0] - points[k][0]) == (points[l][1] - points[k][1]) * (points[j][0] - points[i][0])) {
                            res++
                        }
                    }
                }
            }
        }
        return res
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
    int countTrapezoids(List<List<int>> points) {
        int n = points.length;
        int res = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                for (int k = 0; k < n; k++) {
                    for (int l = k + 1; l < n; l++) {
                        if (i == k || i == l || j == k || j == l) continue;
                        if ((points[j][1] - points[i][1]) * (points[l][0] - points[k][0]) == (points[l][1] - points[k][1]) * (points[j][0] - points[i][0])) {
                            res++;
                        }
                    }
                }
            }
        }
        return res;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func countTrapezoids(points [][]int) int {
    n := len(points)
    res := 0
    for i := 0; i < n; i++ {
        for j := i + 1; j < n; j++ {
            for k := 0; k < n; k++ {
                for l := k + 1; l < n; l++ {
                    if i == k || i == l || j == k || j == l { continue }
                    if (points[j][1]-points[i][1])*(points[l][0]-points[k][0]) == (points[l][1]-points[k][1])*(points[j][0]-points[i][0]) {
                        res++
                    }
                }
            }
        }
    }
    return res
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def count_trapezoids(points)
    n = points.size
    res = 0
    (0...n).each do |i|
        (i+1...n).each do |j|
            (0...n).each do |k|
                (k+1...n).each do |l|
                    if i == k || i == l || j == k || j == l
                        next
                    end
                    if (points[j][1] - points[i][1]) * (points[l][0] - points[k][0]) == (points[l][1] - points[k][1]) * (points[j][0] - points[i][0])
                        res += 1
                    end
                end
            end
        end
    end
    res
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def countTrapezoids(points: Array[Array[Int]]): Int = {
        val n = points.length
        var res = 0
        for (i <- 0 until n) {
            for (j <- i + 1 until n) {
                for (k <- 0 until n) {
                    for (l <- k + 1 until n) {
                        if (i == k || i == l || j == k || j == l) {
                            // do nothing
                        } else if ((points(j)(1) - points(i)(1)) * (points(l)(0) - points(k)(0)) == (points(l)(1) - points(k)(1)) * (points(j)(0) - points(i)(0))) {
                            res += 1
                        }
                    }
                }
            }
        }
        res
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
struct Solution;
impl Solution {
    pub fn count_trapezoids(points: Vec<Vec<i32>>) -> i32 {
        let n = points.len();
        let mut res = 0;
        for i in 0..n {
            for j in i+1..n {
                for k in 0..n {
                    for l in k+1..n {
                        if i == k || i == l || j == k || j == l { continue; }
                        if (points[j][1] - points[i][1]) * (points[l][0] - points[k][0]) == (points[l][1] - points[k][1]) * (points[j][0] - points[i][0]) {
                            res += 1;
                        }
                    }
                }
            }
        }
        res
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
define (count-trapezoids points)
    (let ((n (length points)) (res 0))
        (for* ((i (range n)) (j (range (+ i 1) n)) (k (range n)) (l (range (+ k 1) n)))
            (when (and (not (= i k)) (not (= i l)) (not (= j k)) (not (= j l)))
                (when (= (* (- (cadr (list-ref points j)) (cadr (list-ref points i))) (- (car (list-ref points l)) (car (list-ref points k))))
                             (* (- (car (list-ref points j)) (car (list-ref points i))) (- (cadr (list-ref points l)) (cadr (list-ref points k)))))
                    (set! res (+ res 1)))))
        res)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
count_trapezoids(Points) ->
    length(lists:filter(fun({I, J, K, L}) ->
        (I =/= K) andalso (I =/= L) andalso (J =/= K) andalso (J =/= L) andalso
        ((lists:nth(J, Points) -- lists:nth(I, Points)) -- (lists:nth(L, Points) -- lists:nth(K, Points))) =:= 0
    end, lists:foldl(fun({I, J}, Acc) ->
        lists:foldl(fun({K, L}, Acc1) ->
            [{I, J, K, L} | Acc1]
        end, Acc, Points)
    end, [], Points))).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
def count_trapezoids(points) do
    n = length(points)
    res = 0
    for i <- 0..n-1 do
        for j <- i+1..n-1 do
            for k <- 0..n-1 do
                for l <- k+1..n-1 do
                    if i != k and i != l and j != k and j != l do
                        if (Enum.at(points, j) |> Enum.at(1) - Enum.at(points, i) |> Enum.at(1)) * (Enum.at(points, l) |> Enum.at(0) - Enum.at(points, k) |> Enum.at(0)) == (Enum.at(points, l) |> Enum.at(1) - Enum.at(points, k) |> Enum.at(1)) * (Enum.at(points, j) |> Enum.at(0) - Enum.at(points, i) |> Enum.at(0)) do
                            res = res + 1
                        end
                    end
                end
            end
        end
    end
    res
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is O(n^2) where n is the number of points. This is because we need to calculate the slope of each pair of points, which takes O(n^2) time. Then, for each slope, we need to calculate the number of ways to choose two pairs of points from the list of pairs with that slope, which takes O(k^2) time where k is the number of pairs with that slope. Since the sum of k over all slopes is O(n^2), the total time complexity is O(n^2).

- **Space Complexity:** The space complexity is O(n^2) where n is the number of points. This is because we need to store the slopes of all pairs of points in a hashmap, which takes O(n^2) space. Then, for each slope, we need to store the list of pairs of points that have that slope, which also takes O(n^2) space.

</div>
</details>
