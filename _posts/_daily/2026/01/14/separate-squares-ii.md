---
layout: post
title: "Separate Squares II"
date: 2026-01-14 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Binary Search", "Segment Tree", "Line Sweep"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/separate-squares-ii/
ai_solutions:
  - solutions:
      cpp: "class Solution {\npublic:\n    // SegmentTree class definition\n    struct\
        \ SegmentTree {\n        vector<pair<long long, double>> tree; // {count, length}\n\
        \        const vector<double>& y_coords;\n        int N_intervals;\n\n     \
        \   SegmentTree(const vector<double>& y_coords_ref) : y_coords(y_coords_ref)\
        \ {\n            N_intervals = y_coords.empty() ? 0 : y_coords.size() - 1;\n\
        \            tree.resize(4 * max(1, N_intervals), {0, 0.0});\n        }\n\n\
        \        void _update(int node_idx, int start_idx, int end_idx, int query_y1_idx,\
        \ int query_y2_idx, int val) {\n            if (start_idx >= query_y2_idx ||\
        \ end_idx <= query_y1_idx) {\n                return;\n            }\n\n   \
        \         if (query_y1_idx <= start_idx && end_idx <= query_y2_idx) {\n    \
        \            tree[node_idx].first += val;\n            } else {\n          \
        \      int mid_idx = start_idx + (end_idx - start_idx) / 2;\n              \
        \  _update(2 * node_idx, start_idx, mid_idx, query_y1_idx, query_y2_idx, val);\n\
        \                _update(2 * node_idx + 1, mid_idx, end_idx, query_y1_idx, query_y2_idx,\
        \ val);\n            }\n\n            if (tree[node_idx].first > 0) {\n    \
        \            tree[node_idx].second = y_coords[end_idx] - y_coords[start_idx];\n\
        \            } else {\n                if (start_idx + 1 == end_idx) { // Leaf\
        \ node\n                    tree[node_idx].second = 0.0;\n                }\
        \ else {\n                    tree[node_idx].second = tree[2 * node_idx].second\
        \ + tree[2 * node_idx + 1].second;\n                }\n            }\n     \
        \   }\n\n        void update(double y1, double y2, int val) {\n            if\
        \ (N_intervals == 0) return;\n            auto it1 = lower_bound(y_coords.begin(),\
        \ y_coords.end(), y1);\n            auto it2 = lower_bound(y_coords.begin(),\
        \ y_coords.end(), y2);\n            int y1_idx = distance(y_coords.begin(),\
        \ it1);\n            int y2_idx = distance(y_coords.begin(), it2);\n\n     \
        \       if (y1_idx >= y2_idx) {\n                return;\n            }\n  \
        \          _update(1, 0, N_intervals, y1_idx, y2_idx, val);\n        }\n\n \
        \       double get_total_length() {\n            if (N_intervals == 0) return\
        \ 0.0;\n            return tree[1].second;\n        }\n    };\n\n    // Rectangle\
        \ class to hold (x, y, width, height) with double height\n    struct Rect {\n\
        \        long long x;\n        double y;\n        long long width;\n       \
        \ double height;\n    };\n\n    // Event class for line sweep\n    struct Event\
        \ {\n        long long x;\n        int type; // 1 for left edge, -1 for right\
        \ edge\n        double y1, y2;\n\n        bool operator<(const Event& other)\
        \ const {\n            if (x != other.x) {\n                return x < other.x;\n\
        \            }\n            return type < other.type; // Process left edges\
        \ before right edges at same x\n        }\n    };\n\n    double calculate_unique_area(const\
        \ vector<Rect>& rects) {\n        if (rects.empty()) {\n            return 0.0;\n\
        \        }\n\n        vector<Event> events;\n        set<double> y_coords_set;\n\
        \        for (const auto& rect : rects) {\n            events.push_back({rect.x,\
        \ 1, rect.y, rect.y + rect.height});\n            events.push_back({rect.x +\
        \ rect.width, -1, rect.y, rect.y + rect.height});\n            y_coords_set.insert(rect.y);\n\
        \            y_coords_set.insert(rect.y + rect.height);\n        }\n       \
        \ sort(events.begin(), events.end());\n\n        vector<double> y_coords(y_coords_set.begin(),\
        \ y_coords_set.end());\n\n        if (y_coords.size() <= 1) {\n            return\
        \ 0.0;\n        }\n\n        SegmentTree st(y_coords);\n        double total_area\
        \ = 0.0;\n        long long prev_x = events[0].x;\n\n        for (const auto&\
        \ event : events) {\n            double current_length = st.get_total_length();\n\
        \            total_area += current_length * (event.x - prev_x);\n          \
        \  st.update(event.y1, event.y2, event.type);\n            prev_x = event.x;\n\
        \        }\n        return total_area;\n    }\n\n    double separateSquares(vector<vector<int>>&\
        \ squares) {\n        vector<Rect> original_rects;\n        double min_y_overall\
        \ = 2e9 + 7; // Use a large double value\n        double max_y_overall = -1.0;\n\
        \n        for (const auto& s : squares) {\n            long long x = s[0];\n\
        \            double y = s[1];\n            long long l = s[2];\n           \
        \ original_rects.push_back({x, y, l, l});\n            min_y_overall = min(min_y_overall,\
        \ y);\n            max_y_overall = max(max_y_overall, y + l);\n        }\n\n\
        \        double total_unique_area = calculate_unique_area(original_rects);\n\
        \        double target_area_below = total_unique_area / 2.0;\n\n        double\
        \ low = min_y_overall;\n        double high = max_y_overall;\n        double\
        \ ans = high;\n\n        for (int i = 0; i < 100; ++i) {\n            double\
        \ mid = low + (high - low) / 2.0;\n\n            vector<Rect> clipped_rects_below;\n\
        \            for (const auto& s : squares) {\n                long long x =\
        \ s[0];\n                double y_bottom = s[1];\n                long long\
        \ l = s[2];\n                double y_top = y_bottom + l;\n\n              \
        \  if (y_bottom < mid) {\n                    double clipped_y_top = min(y_top,\
        \ mid);\n                    double clipped_height = clipped_y_top - y_bottom;\n\
        \                    if (clipped_height > 0) {\n                        clipped_rects_below.push_back({x,\
        \ y_bottom, l, clipped_height});\n                    }\n                }\n\
        \            }\n\n            double area_below_mid = calculate_unique_area(clipped_rects_below);\n\
        \n            if (area_below_mid >= target_area_below) {\n                ans\
        \ = mid;\n                high = mid;\n            } else {\n              \
        \  low = mid;\n            }\n        }\n        return ans;\n    }\n};"
      java: "import java.util.*;\n\nclass Solution {\n    // SegmentTree class definition\n\
        \    static class SegmentTree {\n        private static class Node {\n     \
        \       long count; // Number of active rectangles covering this interval\n\
        \            double length; // Total length of the union of active intervals\
        \ within this node's range\n\n            Node() {\n                this.count\
        \ = 0;\n                this.length = 0.0;\n            }\n        }\n\n   \
        \     private Node[] tree;\n        private final List<Double> yCoords;\n  \
        \      private int N_intervals;\n\n        public SegmentTree(List<Double> yCoordsRef)\
        \ {\n            this.yCoords = yCoordsRef;\n            this.N_intervals =\
        \ yCoords.isEmpty() ? 0 : yCoords.size() - 1;\n            tree = new Node[4\
        \ * Math.max(1, N_intervals)];\n            for (int i = 0; i < tree.length;\
        \ i++) {\n                tree[i] = new Node();\n            }\n        }\n\n\
        \        private void _update(int nodeIdx, int startIdx, int endIdx, int queryY1Idx,\
        \ int queryY2Idx, int val) {\n            if (startIdx >= queryY2Idx || endIdx\
        \ <= queryY1Idx) {\n                return;\n            }\n\n            if\
        \ (queryY1Idx <= startIdx && endIdx <= queryY2Idx) {\n                tree[nodeIdx].count\
        \ += val;\n            } else {\n                int midIdx = startIdx + (endIdx\
        \ - startIdx) / 2;\n                _update(2 * nodeIdx, startIdx, midIdx, queryY1Idx,\
        \ queryY2Idx, val);\n                _update(2 * nodeIdx + 1, midIdx, endIdx,\
        \ queryY1Idx, queryY2Idx, val);\n            }\n\n            if (tree[nodeIdx].count\
        \ > 0) {\n                tree[nodeIdx].length = yCoords.get(endIdx) - yCoords.get(startIdx);\n\
        \            } else {\n                if (startIdx + 1 == endIdx) { // Leaf\
        \ node\n                    tree[nodeIdx].length = 0.0;\n                } else\
        \ {\n                    tree[nodeIdx].length = tree[2 * nodeIdx].length + tree[2\
        \ * nodeIdx + 1].length;\n                }\n            }\n        }\n\n  \
        \      public void update(double y1, double y2, int val) {\n            if (N_intervals\
        \ == 0) return;\n            int y1Idx = Collections.binarySearch(yCoords, y1);\n\
        \            if (y1Idx < 0) y1Idx = -y1Idx - 1;\n            int y2Idx = Collections.binarySearch(yCoords,\
        \ y2);\n            if (y2Idx < 0) y2Idx = -y2Idx - 1;\n\n            if (y1Idx\
        \ >= y2Idx) {\n                return;\n            }\n            _update(1,\
        \ 0, N_intervals, y1Idx, y2Idx, val);\n        }\n\n        public double getTotalLength()\
        \ {\n            if (N_intervals == 0) return 0.0;\n            return tree[1].length;\n\
        \        }\n    }\n\n    // Rectangle class to hold (x, y, width, height) with\
        \ double height\n    static class Rect {\n        long x;\n        double y;\n\
        \        long width;\n        double height;\n\n        Rect(long x, double\
        \ y, long width, double height) {\n            this.x = x;\n            this.y\
        \ = y;\n            this.width = width;\n            this.height = height;\n\
        \        }\n    }\n\n    // Event class for line sweep\n    static class Event\
        \ implements Comparable<Event> {\n        long x;\n        int type; // 1 for\
        \ left edge, -1 for right edge\n        double y1, y2;\n\n        Event(long\
        \ x, int type, double y1, double y2) {\n            this.x = x;\n          \
        \  this.type = type;\n            this.y1 = y1;\n            this.y2 = y2;\n\
        \        }\n\n        @Override\n        public int compareTo(Event other) {\n\
        \            if (this.x != other.x) {\n                return Long.compare(this.x,\
        \ other.x);\n            }\n            return Integer.compare(this.type, other.type);\
        \ // Process left edges before right edges at same x\n        }\n    }\n\n \
        \   private double calculateUniqueArea(List<Rect> rects) {\n        if (rects.isEmpty())\
        \ {\n            return 0.0;\n        }\n\n        List<Event> events = new\
        \ ArrayList<>();\n        Set<Double> yCoordsSet = new TreeSet<>(); // Use TreeSet\
        \ to keep sorted and unique\n        for (Rect rect : rects) {\n           \
        \ events.add(new Event(rect.x, 1, rect.y, rect.y + rect.height));\n        \
        \    events.add(new Event(rect.x + rect.width, -1, rect.y, rect.y + rect.height));\n\
        \            yCoordsSet.add(rect.y);\n            yCoordsSet.add(rect.y + rect.height);\n\
        \        }\n        Collections.sort(events);\n\n        List<Double> yCoords\
        \ = new ArrayList<>(yCoordsSet);\n\n        if (yCoords.size() <= 1) {\n   \
        \         return 0.0;\n        }\n\n        SegmentTree st = new SegmentTree(yCoords);\n\
        \        double totalArea = 0.0;\n        long prevX = events.get(0).x;\n\n\
        \        for (Event event : events) {\n            double currentLength = st.getTotalLength();\n\
        \            totalArea += currentLength * (event.x - prevX);\n            st.update(event.y1,\
        \ event.y2, event.type);\n            prevX = event.x;\n        }\n        return\
        \ totalArea;\n    }\n\n    public double separateSquares(int[][] squares) {\n\
        \        List<Rect> originalRects = new ArrayList<>();\n        double minYOverall\
        \ = Double.POSITIVE_INFINITY;\n        double maxYOverall = Double.NEGATIVE_INFINITY;\n\
        \n        for (int[] s : squares) {\n            long x = s[0];\n          \
        \  double y = s[1];\n            long l = s[2];\n            originalRects.add(new\
        \ Rect(x, y, l, l));\n            minYOverall = Math.min(minYOverall, y);\n\
        \            maxYOverall = Math.max(maxYOverall, y + l);\n        }\n\n    \
        \    double totalUniqueArea = calculateUniqueArea(originalRects);\n        double\
        \ targetAreaBelow = totalUniqueArea / 2.0;\n\n        double low = minYOverall;\n\
        \        double high = maxYOverall;\n        double ans = high;\n\n        for\
        \ (int i = 0; i < 100; ++i) {\n            double mid = low + (high - low) /\
        \ 2.0;\n\n            List<Rect> clippedRectsBelow = new ArrayList<>();\n  \
        \          for (int[] s : squares) {\n                long x = s[0];\n     \
        \           double yBottom = s[1];\n                long l = s[2];\n       \
        \         double yTop = yBottom + l;\n\n                if (yBottom < mid) {\n\
        \                    double clippedYTop = Math.min(yTop, mid);\n           \
        \         double clippedHeight = clippedYTop - yBottom;\n                  \
        \  if (clippedHeight > 0) {\n                        clippedRectsBelow.add(new\
        \ Rect(x, yBottom, l, clippedHeight));\n                    }\n            \
        \    }\n            }\n\n            double areaBelowMid = calculateUniqueArea(clippedRectsBelow);\n\
        \n            if (areaBelowMid >= targetAreaBelow) {\n                ans =\
        \ mid;\n                high = mid;\n            } else {\n                low\
        \ = mid;\n            }\n        }\n        return ans;\n    }\n}"
      python: "from bisect import bisect_left\n\nclass SegmentTree(object):\n    def\
        \ __init__(self, y_coords):\n        self.y_coords = y_coords\n        self.N\
        \ = len(y_coords) - 1\n        if self.N < 0:\n            self.N = 0\n    \
        \    self.tree = [[0, 0.0] for _ in range(4 * max(1, self.N))] # [count, length]\n\
        \n    def _update(self, node_idx, start_idx, end_idx, query_y1_idx, query_y2_idx,\
        \ val):\n        if start_idx >= query_y2_idx or end_idx <= query_y1_idx:\n\
        \            return\n\n        if query_y1_idx <= start_idx and end_idx <= query_y2_idx:\n\
        \            self.tree[node_idx][0] += val\n        else:\n            mid_idx\
        \ = (start_idx + end_idx) // 2\n            self._update(2 * node_idx, start_idx,\
        \ mid_idx, query_y1_idx, query_y2_idx, val)\n            self._update(2 * node_idx\
        \ + 1, mid_idx, end_idx, query_y1_idx, query_y2_idx, val)\n\n        if self.tree[node_idx][0]\
        \ > 0:\n            self.tree[node_idx][1] = float(self.y_coords[end_idx] -\
        \ self.y_coords[start_idx])\n        else:\n            if start_idx + 1 ==\
        \ end_idx:\n                self.tree[node_idx][1] = 0.0\n            else:\n\
        \                self.tree[node_idx][1] = self.tree[2 * node_idx][1] + self.tree[2\
        \ * node_idx + 1][1]\n\n    def update(self, y1, y2, val):\n        if self.N\
        \ == 0:\n            return\n        y1_idx = bisect_left(self.y_coords, y1)\n\
        \        y2_idx = bisect_left(self.y_coords, y2)\n\n        if y1_idx >= y2_idx:\n\
        \            return\n\n        self._update(1, 0, self.N, y1_idx, y2_idx, val);\n\
        \n    def get_total_length(self):\n        if self.N == 0:\n            return\
        \ 0.0\n        return self.tree[1][1]\n\nclass Solution(object):\n    def separateSquares(self,\
        \ squares):\n        \"\"\"\n        :type squares: List[List[int]]\n      \
        \  :rtype: float\n        \"\"\"\n\n        def calculate_unique_area(rects):\n\
        \            if not rects:\n                return 0.0\n\n            events\
        \ = []\n            y_coords_set = set()\n            for x, y, w, h in rects:\n\
        \                events.append((x, 1, y, y + h))\n                events.append((x\
        \ + w, -1, y, y + h))\n                y_coords_set.add(y)\n               \
        \ y_coords_set.add(y + h)\n\n            events.sort()\n            y_coords\
        \ = sorted(list(y_coords_set))\n\n            if len(y_coords) <= 1: \n    \
        \            return 0.0\n\n            st = SegmentTree(y_coords)\n        \
        \    total_area = 0.0\n            prev_x = events[0][0]\n\n            for\
        \ x, type, y1, y2 in events:\n                current_length = st.get_total_length()\n\
        \                total_area += current_length * (x - prev_x)\n             \
        \   st.update(y1, y2, type)\n                prev_x = x\n\n            return\
        \ total_area\n\n        original_rects = []\n        min_y_overall = float('inf')\n\
        \        max_y_overall = float('-inf')\n        for x, y, l in squares:\n  \
        \          original_rects.append((x, float(y), float(l), float(l))) # (x, y,\
        \ width, height)\n            min_y_overall = min(min_y_overall, float(y))\n\
        \            max_y_overall = max(max_y_overall, float(y + l))\n\n        total_unique_area\
        \ = calculate_unique_area(original_rects)\n\n        target_area_below = total_unique_area\
        \ / 2.0\n\n        low = float(min_y_overall)\n        high = float(max_y_overall)\n\
        \        ans = high \n\n        for _ in range(100): \n            mid = low\
        \ + (high - low) / 2.0\n\n            clipped_rects_below = []\n           \
        \ for x, y, l in squares:\n                y_bottom = float(y)\n           \
        \     y_top = float(y + l)\n\n                if y_bottom < mid: \n        \
        \            clipped_y_top = min(y_top, mid)\n                    clipped_height\
        \ = clipped_y_top - y_bottom\n                    if clipped_height > 0: # Ensure\
        \ positive height\n                        clipped_rects_below.append((x, y_bottom,\
        \ float(l), clipped_height))\n\n            area_below_mid = calculate_unique_area(clipped_rects_below);\n\
        \n            if area_below_mid >= target_area_below:\n                ans =\
        \ mid;\n                high = mid;\n            else:\n                low\
        \ = mid;\n\n        return ans;"
      python3: "from bisect import bisect_left\n\nclass SegmentTree:\n    def __init__(self,\
        \ y_coords: List[float]):\n        self.y_coords = y_coords\n        self.N\
        \ = len(y_coords) - 1\n        if self.N < 0:\n            self.N = 0\n    \
        \    self.tree = [[0, 0.0] for _ in range(4 * max(1, self.N))] # [count, length]\n\
        \n    def _update(self, node_idx: int, start_idx: int, end_idx: int, query_y1_idx:\
        \ int, query_y2_idx: int, val: int):\n        if start_idx >= query_y2_idx or\
        \ end_idx <= query_y1_idx:\n            return\n\n        if query_y1_idx <=\
        \ start_idx and end_idx <= query_y2_idx:\n            self.tree[node_idx][0]\
        \ += val\n        else:\n            mid_idx = (start_idx + end_idx) // 2\n\
        \            self._update(2 * node_idx, start_idx, mid_idx, query_y1_idx, query_y2_idx,\
        \ val)\n            self._update(2 * node_idx + 1, mid_idx, end_idx, query_y1_idx,\
        \ query_y2_idx, val)\n\n        if self.tree[node_idx][0] > 0:\n           \
        \ self.tree[node_idx][1] = float(self.y_coords[end_idx] - self.y_coords[start_idx])\n\
        \        else:\n            if start_idx + 1 == end_idx:\n                self.tree[node_idx][1]\
        \ = 0.0\n            else:\n                self.tree[node_idx][1] = self.tree[2\
        \ * node_idx][1] + self.tree[2 * node_idx + 1][1]\n\n    def update(self, y1:\
        \ float, y2: float, val: int):\n        if self.N == 0:\n            return\n\
        \        y1_idx = bisect_left(self.y_coords, y1)\n        y2_idx = bisect_left(self.y_coords,\
        \ y2)\n\n        if y1_idx >= y2_idx:\n            return\n\n        self._update(1,\
        \ 0, self.N, y1_idx, y2_idx, val)\n\n    def get_total_length(self) -> float:\n\
        \        if self.N == 0:\n            return 0.0\n        return self.tree[1][1]\n\
        \nclass Solution:\n    def separateSquares(self, squares: List[List[int]]) ->\
        \ float:\n\n        def calculate_unique_area(rects: List[Tuple[int, float,\
        \ float, float]]) -> float:\n            if not rects:\n                return\
        \ 0.0\n\n            events = [] # (x, type, y1, y2)\n            y_coords_set\
        \ = set()\n            for x, y, w, h in rects:\n                events.append((x,\
        \ 1, y, y + h))\n                events.append((x + w, -1, y, y + h))\n    \
        \            y_coords_set.add(y)\n                y_coords_set.add(y + h)\n\n\
        \            events.sort()\n            y_coords = sorted(list(y_coords_set))\n\
        \n            if len(y_coords) <= 1: \n                return 0.0\n\n      \
        \      st = SegmentTree(y_coords)\n            total_area = 0.0\n          \
        \  prev_x = events[0][0]\n\n            for x, type, y1, y2 in events:\n   \
        \             current_length = st.get_total_length()\n                total_area\
        \ += current_length * (x - prev_x)\n                st.update(y1, y2, type)\n\
        \                prev_x = x\n\n            return total_area\n\n        original_rects\
        \ = [] # (x, y, width, height)\n        min_y_overall = float('inf')\n     \
        \   max_y_overall = float('-inf')\n        for x, y, l in squares:\n       \
        \     original_rects.append((x, float(y), float(l), float(l))) # Store y, w,\
        \ h as float for consistency\n            min_y_overall = min(min_y_overall,\
        \ float(y))\n            max_y_overall = max(max_y_overall, float(y + l))\n\n\
        \        total_unique_area = calculate_unique_area(original_rects)\n\n     \
        \   target_area_below = total_unique_area / 2.0\n\n        low = float(min_y_overall)\n\
        \        high = float(max_y_overall)\n        ans = high \n\n        for _ in\
        \ range(100): \n            mid = low + (high - low) / 2.0\n\n            clipped_rects_below\
        \ = []\n            for x, y, l in squares:\n                y_bottom = float(y)\n\
        \                y_top = float(y + l)\n\n                if y_bottom < mid:\
        \ \n                    clipped_y_top = min(y_top, mid)\n                  \
        \  clipped_height = clipped_y_top - y_bottom\n                    if clipped_height\
        \ > 0: \n                        clipped_rects_below.append((x, y_bottom, float(l),\
        \ clipped_height))\n\n            area_below_mid = calculate_unique_area(clipped_rects_below)\n\
        \n            if area_below_mid >= target_area_below:\n                ans =\
        \ mid\n                high = mid\n            else:\n                low =\
        \ mid\n\n        return ans"
      c: "#include <stdlib.h>\n#include <stdio.h>\n#include <math.h>\n#include <string.h>\n\
        \n// Define a structure for Segment Tree nodes\ntypedef struct {\n    long long\
        \ count;\n    double length;\n} SegmentTreeNode;\n\n// Global variables for\
        \ Segment Tree to avoid passing them around too much\n// In a real C solution,\
        \ these would be part of a struct or passed explicitly.\nstatic SegmentTreeNode*\
        \ tree_nodes;\nstatic double* y_coords_arr;\nstatic int N_intervals_st;\n\n\
        // Helper for qsort to sort doubles\nstatic int compare_doubles(const void*\
        \ a, const void* b) {\n    double val_a = *(const double*)a;\n    double val_b\
        \ = *(const double*)b;\n    if (val_a < val_b) return -1;\n    if (val_a > val_b)\
        \ return 1;\n    return 0;\n}\n\n// Binary search for lower_bound equivalent\n\
        static int lower_bound_idx(double val, int size) {\n    int low = 0, high =\
        \ size - 1, ans = size;\n    while (low <= high) {\n        int mid = low +\
        \ (high - low) / 2;\n        if (y_coords_arr[mid] >= val) {\n            ans\
        \ = mid;\n            high = mid - 1;\n        } else {\n            low = mid\
        \ + 1;\n        }\n    }\n    return ans;\n}\n\nstatic void _update_segment_tree(int\
        \ node_idx, int start_idx, int end_idx, int query_y1_idx, int query_y2_idx,\
        \ int val) {\n    if (start_idx >= query_y2_idx || end_idx <= query_y1_idx)\
        \ {\n        return;\n    }\n\n    if (query_y1_idx <= start_idx && end_idx\
        \ <= query_y2_idx) {\n        tree_nodes[node_idx].count += val;\n    } else\
        \ {\n        int mid_idx = start_idx + (end_idx - start_idx) / 2;\n        _update_segment_tree(2\
        \ * node_idx, start_idx, mid_idx, query_y1_idx, query_y2_idx, val);\n      \
        \  _update_segment_tree(2 * node_idx + 1, mid_idx, end_idx, query_y1_idx, query_y2_idx,\
        \ val);\n    }\n\n    if (tree_nodes[node_idx].count > 0) {\n        tree_nodes[node_idx].length\
        \ = y_coords_arr[end_idx] - y_coords_arr[start_idx];\n    } else {\n       \
        \ if (start_idx + 1 == end_idx) {\n            tree_nodes[node_idx].length =\
        \ 0.0;\n        } else {\n            tree_nodes[node_idx].length = tree_nodes[2\
        \ * node_idx].length + tree_nodes[2 * node_idx + 1].length;\n        }\n   \
        \ }\n}\n\nstatic void update_segment_tree(double y1, double y2, int val) {\n\
        \    if (N_intervals_st == 0) return;\n    int y1_idx = lower_bound_idx(y1,\
        \ N_intervals_st + 1);\n    int y2_idx = lower_bound_idx(y2, N_intervals_st\
        \ + 1);\n\n    if (y1_idx >= y2_idx) {\n        return;\n    }\n    _update_segment_tree(1,\
        \ 0, N_intervals_st, y1_idx, y2_idx, val);\n}\n\nstatic double get_total_length_segment_tree()\
        \ {\n    if (N_intervals_st == 0) return 0.0;\n    return tree_nodes[1].length;\n\
        }\n\n// Rectangle structure for calculate_unique_area\ntypedef struct {\n  \
        \  long long x;\n    double y;\n    long long width;\n    double height;\n}\
        \ Rect;\n\n// Event structure for line sweep\ntypedef struct {\n    long long\
        \ x;\n    int type; // 1 for left edge, -1 for right edge\n    double y1, y2;\n\
        } Event;\n\n// Comparator for events (sort by x, then type)\nstatic int compare_events(const\
        \ void* a, const void* b) {\n    Event* event_a = (Event*)a;\n    Event* event_b\
        \ = (Event*)b;\n    if (event_a->x != event_b->x) {\n        return (event_a->x\
        \ < event_b->x) ? -1 : 1;\n    }\n    return event_a->type - event_b->type;\n\
        }\n\nstatic double calculate_unique_area(Rect* rects, int num_rects) {\n   \
        \ if (num_rects == 0) {\n        return 0.0;\n    }\n\n    Event* events = (Event*)malloc(sizeof(Event)\
        \ * num_rects * 2);\n    double* y_coords_raw = (double*)malloc(sizeof(double)\
        \ * num_rects * 2);\n    int event_count = 0;\n    int y_coord_count = 0;\n\n\
        \    for (int i = 0; i < num_rects; ++i) {\n        events[event_count++] =\
        \ (Event){rects[i].x, 1, rects[i].y, rects[i].y + rects[i].height};\n      \
        \  events[event_count++] = (Event){rects[i].x + rects[i].width, -1, rects[i].y,\
        \ rects[i].y + rects[i].height};\n        y_coords_raw[y_coord_count++] = rects[i].y;\n\
        \        y_coords_raw[y_coord_count++] = rects[i].y + rects[i].height;\n   \
        \ }\n    qsort(events, event_count, sizeof(Event), compare_events);\n\n    qsort(y_coords_raw,\
        \ y_coord_count, sizeof(double), compare_doubles);\n\n    // Remove duplicates\
        \ from y_coords_raw\n    int unique_y_count = 0;\n    if (y_coord_count > 0)\
        \ {\n        y_coords_raw[unique_y_count++] = y_coords_raw[0];\n        for\
        \ (int i = 1; i < y_coord_count; ++i) {\n            if (y_coords_raw[i] !=\
        \ y_coords_raw[i-1]) {\n                y_coords_raw[unique_y_count++] = y_coords_raw[i];\n\
        \            }\n        }\n    }\n\n    if (unique_y_count <= 1) {\n       \
        \ free(events);\n        free(y_coords_raw);\n        return 0.0;\n    }\n\n\
        \    y_coords_arr = y_coords_raw; // Set global pointer\n    N_intervals_st\
        \ = unique_y_count - 1;\n    tree_nodes = (SegmentTreeNode*)calloc(4 * (N_intervals_st\
        \ + 1), sizeof(SegmentTreeNode)); // +1 for max(1, N_intervals)\n\n    double\
        \ total_area = 0.0;\n    long long prev_x = events[0].x;\n\n    for (int i =\
        \ 0; i < event_count; ++i) {\n        double current_length = get_total_length_segment_tree();\n\
        \        total_area += current_length * (events[i].x - prev_x);\n        update_segment_tree(events[i].y1,\
        \ events[i].y2, events[i].type);\n        prev_x = events[i].x;\n    }\n\n \
        \   free(events);\n    free(y_coords_raw);\n    free(tree_nodes);\n    return\
        \ total_area;\n}\n\ndouble separateSquares(int** squares, int squaresSize, int*\
        \ squaresColSize) {\n    Rect* original_rects = (Rect*)malloc(sizeof(Rect) *\
        \ squaresSize);\n    double min_y_overall = 2e18; // Use a large double value\n\
        \    double max_y_overall = -1.0;\n\n    for (int i = 0; i < squaresSize; ++i)\
        \ {\n        long long x = squares[i][0];\n        double y = squares[i][1];\n\
        \        long long l = squares[i][2];\n        original_rects[i] = (Rect){x,\
        \ y, l, l};\n        min_y_overall = fmin(min_y_overall, y);\n        max_y_overall\
        \ = fmax(max_y_overall, y + l);\n    }\n\n    double total_unique_area = calculate_unique_area(original_rects,\
        \ squaresSize);\n    double target_area_below = total_unique_area / 2.0;\n\n\
        \    double low = min_y_overall;\n    double high = max_y_overall;\n    double\
        \ ans = high;\n\n    for (int i = 0; i < 100; ++i) {\n        double mid = low\
        \ + (high - low) / 2.0;\n\n        Rect* clipped_rects_below = (Rect*)malloc(sizeof(Rect)\
        \ * squaresSize);\n        int clipped_count = 0;\n\n        for (int j = 0;\
        \ j < squaresSize; ++j) {\n            long long x = squares[j][0];\n      \
        \      double y_bottom = squares[j][1];\n            long long l = squares[j][2];\n\
        \            double y_top = y_bottom + l;\n\n            if (y_bottom < mid)\
        \ {\n                double clipped_y_top = fmin(y_top, mid);\n            \
        \    double clipped_height = clipped_y_top - y_bottom;\n                if (clipped_height\
        \ > 0) {\n                    clipped_rects_below[clipped_count++] = (Rect){x,\
        \ y_bottom, l, clipped_height};\n                }\n            }\n        }\n\
        \n        double area_below_mid = calculate_unique_area(clipped_rects_below,\
        \ clipped_count);\n        free(clipped_rects_below);\n\n        if (area_below_mid\
        \ >= target_area_below) {\n            ans = mid;\n            high = mid;\n\
        \        } else {\n            low = mid;\n        }\n    }\n    free(original_rects);\n\
        \    return ans;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\nusing System.Linq;\n\
        \npublic class Solution {\n// SegmentTree class definition\nprivate class SegmentTree\
        \ {\nprivate class Node {\n    public long Count { get; set; }\n    public double\
        \ Length { get; set; }\n\n    public Node() {\n        Count = 0;\n        Length\
        \ = 0.0;\n    }\n}\n\nprivate Node[] tree;\nprivate readonly List<double> yCoords;\n\
        private int N_intervals;\n\npublic SegmentTree(List<double> yCoordsRef) {\n\
        \    this.yCoords = yCoordsRef;\n    this.N_intervals = yCoords.Count == 0 ?\
        \ 0 : yCoords.Count - 1;\n    tree = new Node[4 * Math.Max(1, N_intervals)];\n\
        \    for (int i = 0; i < tree.Length; i++) {\n        tree[i] = new Node();\n\
        \    }\n}\n\nprivate void _update(int nodeIdx, int startIdx, int endIdx, int\
        \ queryY1Idx, int queryY2Idx, int val) {\n    if (startIdx >= queryY2Idx ||\
        \ endIdx <= queryY1Idx) {\n        return;\n    }\n\n    if (queryY1Idx <= startIdx\
        \ && endIdx <= queryY2Idx) {\n        tree[nodeIdx].Count += val;\n    } else\
        \ {\n        int midIdx = startIdx + (endIdx - startIdx) / 2;\n        _update(2\
        \ * nodeIdx, startIdx, midIdx, queryY1Idx, queryY2Idx, val);\n        _update(2\
        \ * nodeIdx + 1, midIdx, endIdx, queryY1Idx, queryY2Idx, val);\n    }\n\n  \
        \  if (tree[nodeIdx].Count > 0) {\n        tree[nodeIdx].Length = yCoords[endIdx]\
        \ - yCoords[startIdx];\n    } else {\n        if (startIdx + 1 == endIdx) {\
        \ // Leaf node\n            tree[nodeIdx].Length = 0.0;\n        } else {\n\
        \            tree[nodeIdx].Length = tree[2 * nodeIdx].Length + tree[2 * nodeIdx\
        \ + 1].Length;\n        }\n    }\n}\n\npublic void Update(double y1, double\
        \ y2, int val) {\n    if (N_intervals == 0) return;\n    int y1Idx = yCoords.BinarySearch(y1);\n\
        \    if (y1Idx < 0) y1Idx = ~y1Idx;\n    int y2Idx = yCoords.BinarySearch(y2);\n\
        \    if (y2Idx < 0) y2Idx = ~y2Idx;\n\n    if (y1Idx >= y2Idx) {\n        return;\n\
        \    }\n    _update(1, 0, N_intervals, y1Idx, y2Idx, val);\n}\n\npublic double\
        \ GetTotalLength() {\n    if (N_intervals == 0) return 0.0;\n    return tree[1].Length;\n\
        }\n}\n\n// Rectangle class to hold (x, y, width, height) with double height\n\
        private class Rect {\npublic long X { get; set; }\npublic double Y { get; set;\
        \ }\npublic long Width { get; set; }\npublic double Height { get; set; }\n\n\
        public Rect(long x, double y, long width, double height) {\n    this.X = x;\n\
        \    this.Y = y;\n    this.Width = width;\n    this.Height = height;\n}\n}\n\
        \n// Event class for line sweep\nprivate class Event : IComparable<Event> {\n\
        public long X { get; set; }\npublic int Type { get; set; } // 1 for left edge,\
        \ -1 for right edge\npublic double Y1 { get; set; }\npublic double Y2 { get;\
        \ set; }\n\npublic Event(long x, int type, double y1, double y2) {\n    this.X\
        \ = x;\n    this.Type = type;\n    this.Y1 = y1;\n    this.Y2 = y2;\n}\n\npublic\
        \ int CompareTo(Event other) {\n    if (this.X != other.X) {\n        return\
        \ this.X.CompareTo(other.X);\n    }\n    return this.Type.CompareTo(other.Type);\
        \ // Process left edges before right edges at same x\n}\n}\n\nprivate double\
        \ CalculateUniqueArea(List<Rect> rects) {\nif (rects.Count == 0) {\n    return\
        \ 0.0;\n}\n\nList<Event> events = new List<Event>();\nSortedSet<double> yCoordsSet\
        \ = new SortedSet<double>(); // Use SortedSet to keep sorted and unique\nforeach\
        \ (Rect rect in rects) {\n    events.Add(new Event(rect.X, 1, rect.Y, rect.Y\
        \ + rect.Height));\n    events.Add(new Event(rect.X + rect.Width, -1, rect.Y,\
        \ rect.Y + rect.Height));\n    yCoordsSet.Add(rect.Y);\n    yCoordsSet.Add(rect.Y\
        \ + rect.Height);\n}\nevents.Sort();\n\nList<double> yCoords = yCoordsSet.ToList();\n\
        \nif (yCoords.Count <= 1) {\n    return 0.0;\n}\n\nSegmentTree st = new SegmentTree(yCoords);\n\
        double totalArea = 0.0;\nlong prevX = events[0].X;\n\nforeach (Event eventItem\
        \ in events) {\n    double currentLength = st.GetTotalLength();\n    totalArea\
        \ += currentLength * (eventItem.X - prevX);\n    st.Update(eventItem.Y1, eventItem.Y2,\
        \ eventItem.Type);\n    prevX = eventItem.X;\n}\nreturn totalArea;\n}\n\npublic\
        \ double SeparateSquares(int[][] squares) {\nList<Rect> originalRects = new\
        \ List<Rect>();\ndouble minYOverall = double.PositiveInfinity;\ndouble maxYOverall\
        \ = double.NegativeInfinity;\n\nfor (int[] s : squares) {\n    long x = s[0];\n\
        \    double y = s[1];\n    long l = s[2];\n    originalRects.Add(new Rect(x,\
        \ y, l, l));\n    minYOverall = Math.Min(minYOverall, y);\n    maxYOverall =\
        \ Math.Max(maxYOverall, y + l);\n}\n\ndouble totalUniqueArea = CalculateUniqueArea(originalRects);\n\
        double targetAreaBelow = totalUniqueArea / 2.0;\n\ndouble low = minYOverall;\n\
        double high = maxYOverall;\ndouble ans = high;\n\nfor (int i = 0; i < 100; ++i)\
        \ {\n    double mid = low + (high - low) / 2.0;\n\n    List<Rect> clippedRectsBelow\
        \ = new List<Rect>();\n    for (int[] s : squares) {\n        long x = s[0];\n\
        \        double yBottom = s[1];\n        long l = s[2];\n        double yTop\
        \ = yBottom + l;\n\n        if (yBottom < mid) {\n            double clippedYTop\
        \ = Math.Min(yTop, mid);\n            double clippedHeight = clippedYTop - yBottom;\n\
        \            if (clippedHeight > 0) {\n                clippedRectsBelow.Add(new\
        \ Rect(x, yBottom, l, clippedHeight));\n            }\n        }\n    }\n\n\
        \    double areaBelowMid = CalculateUniqueArea(clippedRectsBelow);\n\n    if\
        \ (areaBelowMid >= targetAreaBelow) {\n        ans = mid;\n        high = mid;\n\
        \    } else {\n        low = mid;\n    }\n}\nreturn ans;\n}\n}"
      javascript: "/**\n * @param {number[][]} squares\n * @return {number}\n */\n\n\
        class SegmentTree {\n    constructor(yCoords) {\n        this.yCoords = yCoords;\n\
        \        this.N = yCoords.length - 1;\n        if (this.N < 0) this.N = 0;\n\
        \        this.tree = Array(4 * Math.max(1, this.N)).fill(null).map(() => [0,\
        \ 0.0]); // [count, length]\n    }\n\n    _update(nodeIdx, startIdx, endIdx,\
        \ queryY1Idx, queryY2Idx, val) {\n        if (startIdx >= queryY2Idx || endIdx\
        \ <= queryY1Idx) {\n            return;\n        }\n\n        if (queryY1Idx\
        \ <= startIdx && endIdx <= queryY2Idx) {\n            this.tree[nodeIdx][0]\
        \ += val;\n        } else {\n            const midIdx = Math.floor((startIdx\
        \ + endIdx) / 2);\n            this._update(2 * nodeIdx, startIdx, midIdx, queryY1Idx,\
        \ queryY2Idx, val);\n            this._update(2 * nodeIdx + 1, midIdx, endIdx,\
        \ queryY1Idx, queryY2Idx, val);\n        }\n\n        if (this.tree[nodeIdx][0]\
        \ > 0) {\n            this.tree[nodeIdx][1] = this.yCoords[endIdx] - this.yCoords[startIdx];\n\
        \        } else {\n            if (startIdx + 1 === endIdx) {\n            \
        \    this.tree[nodeIdx][1] = 0.0;\n            } else {\n                this.tree[nodeIdx][1]\
        \ = this.tree[2 * nodeIdx][1] + this.tree[2 * nodeIdx + 1][1];\n           \
        \ }\n        }\n    }\n\n    update(y1, y2, val) {\n        if (this.N === 0)\
        \ return;\n        const y1Idx = this.binarySearch(this.yCoords, y1);\n    \
        \    const y2Idx = this.binarySearch(this.yCoords, y2);\n\n        if (y1Idx\
        \ >= y2Idx) {\n            return;\n        }\n\n        this._update(1, 0,\
        \ this.N, y1Idx, y2Idx, val);\n    }\n\n    get_total_length() {\n        if\
        \ (this.N === 0) return 0.0;\n        return this.tree[1][1];\n    }\n\n   \
        \ // Custom binary search for lower_bound\n    binarySearch(arr, target) {\n\
        \        let low = 0;\n        let high = arr.length - 1;\n        let ans =\
        \ arr.length;\n        while (low <= high) {\n            const mid = Math.floor((low\
        \ + high) / 2);\n            if (arr[mid] >= target) {\n                ans\
        \ = mid;\n                high = mid - 1;\n            } else {\n          \
        \      low = mid + 1;\n            }\n        }\n        return ans;\n    }\n\
        }\n\nvar separateSquares = function(squares) {\n\n    const calculateUniqueArea\
        \ = (rects) => {\n        if (rects.length === 0) {\n            return 0.0;\n\
        \        }\n\n        const events = []; // (x, type, y1, y2)\n        const\
        \ yCoordsSet = new Set();\n        for (const rect of rects) {\n           \
        \ const [x, y, w, h] = rect;\n            events.push([x, 1, y, y + h]);\n \
        \           events.push([x + w, -1, y, y + h]);\n            yCoordsSet.add(y);\n\
        \            yCoordsSet.add(y + h);\n        }\n        events.sort((a, b) =>\
        \ {\n            if (a[0] !== b[0]) return a[0] - b[0];\n            return\
        \ a[1] - b[1];\n        });\n\n        const yCoords = Array.from(yCoordsSet).sort((a,\
        \ b) => a - b);\n\n        if (yCoords.length <= 1) {\n            return 0.0;\n\
        \        }\n\n        const st = new SegmentTree(yCoords);\n        let totalArea\
        \ = 0.0;\n        let prevX = events[0][0];\n\n        for (const event of events)\
        \ {\n            const [x, type, y1, y2] = event;\n            const currentLength\
        \ = st.get_total_length();\n            totalArea += currentLength * (x - prevX);\n\
        \            st.update(y1, y2, type);\n            prevX = x;\n        }\n \
        \       return totalArea;\n    };\n\n    const originalRects = []; // [x, y,\
        \ width, height]\n    let minYOverall = Infinity;\n    let maxYOverall = -Infinity;\n\
        \    for (const s of squares) {\n        const [x, y, l] = s;\n        originalRects.push([x,\
        \ parseFloat(y), parseFloat(l), parseFloat(l)]);\n        minYOverall = Math.min(minYOverall,\
        \ parseFloat(y));\n        maxYOverall = Math.max(maxYOverall, parseFloat(y\
        \ + l));\n    }\n\n    const totalUniqueArea = calculateUniqueArea(originalRects);\n\
        \    const targetAreaBelow = totalUniqueArea / 2.0;\n\n    let low = minYOverall;\n\
        \    let high = maxYOverall;\n    let ans = high; \n\n    for (let i = 0; i\
        \ < 100; ++i) {\n        const mid = low + (high - low) / 2.0;\n\n        const\
        \ clippedRectsBelow = [];\n        for (const s of squares) {\n            const\
        \ [x, y, l] = s;\n            const yBottom = parseFloat(y);\n            const\
        \ yTop = parseFloat(y + l);\n\n            if (yBottom < mid) {\n          \
        \      const clippedYTop = Math.min(yTop, mid);\n                const clippedHeight\
        \ = clippedYTop - yBottom;\n                if (clippedHeight > 0) {\n     \
        \               clippedRectsBelow.push([x, yBottom, parseFloat(l), clippedHeight]);\n\
        \                }\n            }\n        }\n\n        const areaBelowMid =\
        \ calculateUniqueArea(clippedRectsBelow);\n\n        if (areaBelowMid >= targetAreaBelow)\
        \ {\n            ans = mid;\n            high = mid;\n        } else {\n   \
        \         low = mid;\n        }\n    }\n\n    return ans;\n};"
      typescript: "function separateSquares(squares: number[][]): number {\n\n    class\
        \ SegmentTree {\n        private yCoords: number[];\n        private N: number;\n\
        \        private tree: [number, number][]; // [count, length]\n\n        constructor(yCoords:\
        \ number[]) {\n            this.yCoords = yCoords;\n            this.N = yCoords.length\
        \ - 1;\n            if (this.N < 0) this.N = 0;\n            this.tree = Array(4\
        \ * Math.max(1, this.N)).fill(null).map(() => [0, 0.0]);\n        }\n\n    \
        \    private _update(nodeIdx: number, startIdx: number, endIdx: number, queryY1Idx:\
        \ number, queryY2Idx: number, val: number): void {\n            if (startIdx\
        \ >= queryY2Idx || endIdx <= queryY1Idx) {\n                return;\n      \
        \      }\n\n            if (queryY1Idx <= startIdx && endIdx <= queryY2Idx)\
        \ {\n                this.tree[nodeIdx][0] += val;\n            } else {\n \
        \               const midIdx = Math.floor((startIdx + endIdx) / 2);\n      \
        \          this._update(2 * nodeIdx, startIdx, midIdx, queryY1Idx, queryY2Idx,\
        \ val);\n                this._update(2 * nodeIdx + 1, midIdx, endIdx, queryY1Idx,\
        \ queryY2Idx, val);\n            }\n\n            if (this.tree[nodeIdx][0]\
        \ > 0) {\n                this.tree[nodeIdx][1] = this.yCoords[endIdx] - this.yCoords[startIdx];\n\
        \            } else {\n                if (startIdx + 1 === endIdx) {\n    \
        \                this.tree[nodeIdx][1] = 0.0;\n                } else {\n  \
        \                  this.tree[nodeIdx][1] = this.tree[2 * nodeIdx][1] + this.tree[2\
        \ * nodeIdx + 1][1];\n                }\n            }\n        }\n\n      \
        \  public update(y1: number, y2: number, val: number): void {\n            if\
        \ (this.N === 0) return;\n            const y1Idx = this.binarySearch(this.yCoords,\
        \ y1);\n            const y2Idx = this.binarySearch(this.yCoords, y2);\n\n \
        \           if (y1Idx >= y2Idx) {\n                return;\n            }\n\n\
        \            this._update(1, 0, this.N, y1Idx, y2Idx, val);\n        }\n\n \
        \       public getTotalLength(): number {\n            if (this.N === 0) return\
        \ 0.0;\n            return this.tree[1][1];\n        }\n\n        private binarySearch(arr:\
        \ number[], target: number): number {\n            let low = 0;\n          \
        \  let high = arr.length - 1;\n            let ans = arr.length;\n         \
        \   while (low <= high) {\n                const mid = Math.floor((low + high)\
        \ / 2);\n                if (arr[mid] >= target) {\n                    ans\
        \ = mid;\n                    high = mid - 1;\n                } else {\n  \
        \                  low = mid + 1;\n                }\n            }\n      \
        \      return ans;\n        }\n    }\n\n    type Rect = [number, number, number,\
        \ number]; // [x, y, width, height]\n    type Event = [number, number, number,\
        \ number]; // [x, type, y1, y2]\n\n    const calculateUniqueArea = (rects: Rect[]):\
        \ number => {\n        if (rects.length === 0) {\n            return 0.0;\n\
        \        }\n\n        const events: Event[] = [];\n        const yCoordsSet\
        \ = new Set<number>();\n        for (const rect of rects) {\n            const\
        \ [x, y, w, h] = rect;\n            events.push([x, 1, y, y + h]);\n       \
        \     events.push([x + w, -1, y, y + h]);\n            yCoordsSet.add(y);\n\
        \            yCoordsSet.add(y + h);\n        }\n        events.sort((a, b) =>\
        \ {\n            if (a[0] !== b[0]) return a[0] - b[0];\n            return\
        \ a[1] - b[1];\n        });\n\n        const yCoords = Array.from(yCoordsSet).sort((a,\
        \ b) => a - b);\n\n        if (yCoords.length <= 1) {\n            return 0.0;\n\
        \        }\n\n        const st = new SegmentTree(yCoords);\n        let totalArea\
        \ = 0.0;\n        let prevX = events[0][0];\n\n        for (const event of events)\
        \ {\n            const [x, type, y1, y2] = event;\n            const currentLength\
        \ = st.getTotalLength();\n            totalArea += currentLength * (x - prevX);\n\
        \            st.update(y1, y2, type);\n            prevX = x;\n        }\n \
        \       return totalArea;\n    };\n\n    const originalRects: Rect[] = [];\n\
        \    let minYOverall = Infinity;\n    let maxYOverall = -Infinity;\n    for\
        \ (const s of squares) {\n        const [x, y, l] = s;\n        originalRects.push([x,\
        \ y, l, l]);\n        minYOverall = Math.min(minYOverall, y);\n        maxYOverall\
        \ = Math.max(maxYOverall, y + l);\n    }\n\n    const totalUniqueArea = calculateUniqueArea(originalRects);\n\
        \    const targetAreaBelow = totalUniqueArea / 2.0;\n\n    let low = minYOverall;\n\
        \    let high = maxYOverall;\n    let ans = high; \n\n    for (let i = 0; i\
        \ < 100; ++i) {\n        const mid = low + (high - low) / 2.0;\n\n        const\
        \ clippedRectsBelow: Rect[] = [];\n        for (const s of squares) {\n    \
        \        const [x, y, l] = s;\n            const yBottom = y;\n            const\
        \ yTop = y + l;\n\n            if (yBottom < mid) {\n                const clippedYTop\
        \ = Math.min(yTop, mid);\n                const clippedHeight = clippedYTop\
        \ - yBottom;\n                if (clippedHeight > 0) {\n                   \
        \ clippedRectsBelow.push([x, yBottom, l, clippedHeight]);\n                }\n\
        \            }\n        }\n\n        const areaBelowMid = calculateUniqueArea(clippedRectsBelow);\n\
        \n        if (areaBelowMid >= targetAreaBelow) {\n            ans = mid;\n \
        \           high = mid;\n        } else {\n            low = mid;\n        }\n\
        \    }\n\n    return ans;\n};"
      php: "<?php\n\nclass SegmentTree {\n    private $yCoords;\n    private $N;\n \
        \   private $tree; // [count, length]\n\n    public function __construct(array\
        \ $yCoords) {\n        $this->yCoords = $yCoords;\n        $this->N = count($yCoords)\
        \ - 1;\n        if ($this->N < 0) $this->N = 0;\n        $this->tree = array_fill(0,\
        \ 4 * max(1, $this->N), [0, 0.0]);\n    }\n\n    private function _update(int\
        \ $nodeIdx, int $startIdx, int $endIdx, int $queryY1Idx, int $queryY2Idx, int\
        \ $val): void {\n        if ($startIdx >= $queryY2Idx || $endIdx <= $queryY1Idx)\
        \ {\n            return;\n        }\n\n        if ($queryY1Idx <= $startIdx\
        \ && $endIdx <= $queryY2Idx) {\n            $this->tree[$nodeIdx][0] += $val;\n\
        \        } else {\n            $midIdx = floor(($startIdx + $endIdx) / 2);\n\
        \            $this->_update(2 * $nodeIdx, $startIdx, $midIdx, $queryY1Idx, $queryY2Idx,\
        \ $val);\n            $this->_update(2 * $nodeIdx + 1, $midIdx, $endIdx, $queryY1Idx,\
        \ $queryY2Idx, $val);\n        }\n\n        if ($this->tree[$nodeIdx][0] > 0)\
        \ {\n            $this->tree[$nodeIdx][1] = (float)($this->yCoords[$endIdx]\
        \ - $this->yCoords[$startIdx]);\n        } else {\n            if ($startIdx\
        \ + 1 === $endIdx) {\n                $this->tree[$nodeIdx][1] = 0.0;\n    \
        \        } else {\n                $this->tree[$nodeIdx][1] = $this->tree[2\
        \ * $nodeIdx][1] + $this->tree[2 * $nodeIdx + 1][1];\n            }\n      \
        \  }\n    }\n\n    public function update(float $y1, float $y2, int $val): void\
        \ {\n        if ($this->N === 0) return;\n        $y1Idx = $this->binarySearch($this->yCoords,\
        \ $y1);\n        $y2Idx = $this->binarySearch($this->yCoords, $y2);\n\n    \
        \    if ($y1Idx >= $y2Idx) {\n            return;\n        }\n\n        $this->_update(1,\
        \ 0, $this->N, $y1Idx, $y2Idx, $val);\n    }\n\n    public function getTotalLength():\
        \ float {\n        if ($this->N === 0) return 0.0;\n        return $this->tree[1][1];\n\
        \    }\n\n    private function binarySearch(array $arr, float $target): int\
        \ {\n        $low = 0;\n        $high = count($arr) - 1;\n        $ans = count($arr);\n\
        \        while ($low <= $high) {\n            $mid = floor(($low + $high) /\
        \ 2);\n            if ($arr[$mid] >= $target) {\n                $ans = $mid;\n\
        \                $high = $mid - 1;\n            } else {\n                $low\
        \ = $mid + 1;\n            }\n        }\n        return $ans;\n    }\n}\n\n\
        class Solution {\n\n    /**\n     * @param Integer[][] $squares\n     * @return\
        \ Float\n     */\n    function separateSquares($squares) {\n\n        $calculateUniqueArea\
        \ = function(array $rects): float {\n            if (empty($rects)) {\n    \
        \            return 0.0;\n            }\n\n            $events = []; // [x,\
        \ type, y1, y2]\n            $yCoordsSet = [];\n            foreach ($rects\
        \ as $rect) {\n                list($x, $y, $w, $h) = $rect;\n             \
        \   $events[] = [$x, 1, $y, $y + $h];\n                $events[] = [$x + $w,\
        \ -1, $y, $y + $h];\n                $yCoordsSet[(string)$y] = $y; // Use string\
        \ key to handle float uniqueness\n                $yCoordsSet[(string)($y +\
        \ $h)] = $y + $h;\n            }\n            usort($events, function($a, $b)\
        \ {\n                if ($a[0] !== $b[0]) return $a[0] - $b[0];\n          \
        \      return $a[1] - $b[1];\n            });\n\n            $yCoords = array_values($yCoordsSet);\n\
        \            sort($yCoords, SORT_NUMERIC);\n\n            if (count($yCoords)\
        \ <= 1) {\n                return 0.0;\n            }\n\n            $st = new\
        \ SegmentTree($yCoords);\n            $totalArea = 0.0;\n            $prevX\
        \ = $events[0][0];\n\n            foreach ($events as $event) {\n          \
        \      list($x, $type, $y1, $y2) = $event;\n                $currentLength =\
        \ $st->getTotalLength();\n                $totalArea += $currentLength * ($x\
        \ - $prevX);\n                $st->update($y1, $y2, $type);\n              \
        \  $prevX = $x;\n            }\n            return $totalArea;\n        };\n\
        \n        $originalRects = []; // [x, y, width, height]\n        $minYOverall\
        \ = INF;\n        $maxYOverall = -INF;\n        foreach ($squares as $s) {\n\
        \            list($x, $y, $l) = $s;\n            $originalRects[] = [$x, (float)$y,\
        \ (float)$l, (float)$l];\n            $minYOverall = min($minYOverall, (float)$y);\n\
        \            $maxYOverall = max($maxYOverall, (float)($y + $l));\n        }\n\
        \n        $totalUniqueArea = $calculateUniqueArea($originalRects);\n\n     \
        \   $targetAreaBelow = $totalUniqueArea / 2.0;\n\n        $low = $minYOverall;\n\
        \        $high = $maxYOverall;\n        $ans = $high; \n\n        for ($i =\
        \ 0; $i < 100; ++$i) {\n            $mid = $low + ($high - $low) / 2.0;\n\n\
        \            $clippedRectsBelow = [];\n            foreach ($squares as $s)\
        \ {\n                list($x, $y, $l) = $s;\n                $yBottom = (float)$y;\n\
        \                $yTop = (float)($y + $l);\n\n                if ($yBottom <\
        \ $mid) {\n                    $clippedYTop = min($yTop, $mid);\n          \
        \          $clippedHeight = $clippedYTop - $yBottom;\n                    if\
        \ ($clippedHeight > 0) {\n                        $clippedRectsBelow[] = [$x,\
        \ $yBottom, (float)$l, $clippedHeight];\n                    }\n           \
        \     }\n            }\n\n            $areaBelowMid = $calculateUniqueArea($clippedRectsBelow);\n\
        \n            if ($areaBelowMid >= $targetAreaBelow) {\n                $ans\
        \ = $mid;\n                $high = $mid;\n            } else {\n           \
        \     $low = $mid;\n            }\n        }\n\n        return $ans;\n    }\n\
        }"
      swift: "import Foundation\n\nclass SegmentTree {\n    private var yCoords: [Double]\n\
        \    private var N: Int\n    private var tree: [[Double]] // [count, length]\n\
        \n    init(yCoords: [Double]) {\n        self.yCoords = yCoords\n        self.N\
        \ = yCoords.count - 1\n        if self.N < 0 { self.N = 0 }\n        self.tree\
        \ = Array(repeating: [0.0, 0.0], count: 4 * max(1, self.N))\n    }\n\n    private\
        \ func _update(nodeIdx: Int, startIdx: Int, endIdx: Int, queryY1Idx: Int, queryY2Idx:\
        \ Int, val: Int) {\n        if startIdx >= queryY2Idx || endIdx <= queryY1Idx\
        \ {\n            return\n        }\n\n        if queryY1Idx <= startIdx && endIdx\
        \ <= queryY2Idx {\n            self.tree[nodeIdx][0] += Double(val)\n      \
        \  } else {\n            let midIdx = (startIdx + endIdx) / 2\n            _update(nodeIdx:\
        \ 2 * nodeIdx, startIdx: startIdx, endIdx: midIdx, queryY1Idx: queryY1Idx, queryY2Idx:\
        \ queryY2Idx, val: val)\n            _update(nodeIdx: 2 * nodeIdx + 1, startIdx:\
        \ midIdx, endIdx: endIdx, queryY1Idx: queryY1Idx, queryY2Idx: queryY2Idx, val:\
        \ val)\n        }\n\n        if self.tree[nodeIdx][0] > 0 {\n            self.tree[nodeIdx][1]\
        \ = self.yCoords[endIdx] - self.yCoords[startIdx]\n        } else {\n      \
        \      if startIdx + 1 == endIdx {\n                self.tree[nodeIdx][1] =\
        \ 0.0\n            } else {\n                self.tree[nodeIdx][1] = self.tree[2\
        \ * nodeIdx][1] + self.tree[2 * nodeIdx + 1][1]\n            }\n        }\n\
        \    }\n\n    func update(y1: Double, y2: Double, val: Int) {\n        if self.N\
        \ == 0 { return }\n        let y1Idx = binarySearch(arr: self.yCoords, target:\
        \ y1)\n        let y2Idx = binarySearch(arr: self.yCoords, target: y2)\n\n \
        \       if y1Idx >= y2Idx {\n            return\n        }\n\n        _update(nodeIdx:\
        \ 1, startIdx: 0, endIdx: self.N, queryY1Idx: y1Idx, queryY2Idx: y2Idx, val:\
        \ val)\n    }\n\n    func getTotalLength() -> Double {\n        if self.N ==\
        \ 0 { return 0.0 }\n        return self.tree[1][1]\n    }\n\n    private func\
        \ binarySearch(arr: [Double], target: Double) -> Int {\n        var low = 0\n\
        \        var high = arr.count - 1\n        var ans = arr.count\n        while\
        \ low <= high {\n            let mid = (low + high) / 2\n            if arr[mid]\
        \ >= target {\n                ans = mid\n                high = mid - 1\n \
        \           } else {\n                low = mid + 1;\n            }\n      \
        \  }\n        return ans;\n    }\n}\n\nclass Solution {\n    func separateSquares(_\
        \ squares: [[Int]]) -> Double {\n\n        typealias Rect = (x: Int, y: Double,\
        \ width: Double, height: Double)\n        typealias Event = (x: Int, type: Int,\
        \ y1: Double, y2: Double)\n\n        let calculateUniqueArea = { (rects: [Rect])\
        \ -> Double in\n            if rects.isEmpty {\n                return 0.0\n\
        \            }\n\n            var events: [Event] = []\n            var yCoordsSet\
        \ = Set<Double>()\n            for rect in rects {\n                events.append((rect.x,\
        \ 1, rect.y, rect.y + rect.height))\n                events.append((rect.x +\
        \ Int(rect.width), -1, rect.y, rect.y + rect.height))\n                yCoordsSet.insert(rect.y)\n\
        \                yCoordsSet.insert(rect.y + rect.height)\n            }\n  \
        \          events.sort { (a, b) in\n                if a.x != b.x { return a.x\
        \ < b.x }\n                return a.type < b.type\n            }\n\n       \
        \     let yCoords = yCoordsSet.sorted()\n\n            if yCoords.count <= 1\
        \ {\n                return 0.0\n            }\n\n            let st = SegmentTree(yCoords:\
        \ yCoords)\n            var totalArea = 0.0\n            var prevX = events[0].x\n\
        \n            for event in events {\n                let currentLength = st.getTotalLength()\n\
        \                totalArea += currentLength * Double(event.x - prevX)\n    \
        \            st.update(y1: event.y1, y2: event.y2, val: event.type)\n      \
        \          prevX = event.x\n            }\n            return totalArea\n  \
        \      }\n\n        var originalRects: [Rect] = []\n        var minYOverall:\
        \ Double = .infinity\n        var maxYOverall: Double = -.infinity\n       \
        \ for s in squares {\n            let x = s[0]\n            let y = Double(s[1])\n\
        \            let l = Double(s[2])\n            originalRects.append((x, y, l,\
        \ l))\n            minYOverall = min(minYOverall, y)\n            maxYOverall\
        \ = max(maxYOverall, y + l)\n        }\n\n        let totalUniqueArea = calculateUniqueArea(originalRects)\n\
        \n        let targetAreaBelow = totalUniqueArea / 2.0\n\n        var low = minYOverall\n\
        \        var high = maxYOverall\n        var ans = high \n\n        for _ in\
        \ 0..<100 { \n            let mid = low + (high - low) / 2.0\n\n           \
        \ var clippedRectsBelow: [Rect] = []\n            for s in squares {\n     \
        \           let x = s[0]\n                let yBottom = Double(s[1])\n     \
        \           let l = Double(s[2])\n                let yTop = yBottom + l\n\n\
        \                if yBottom < mid {\n                    let clippedYTop = min(yTop,\
        \ mid)\n                    let clippedHeight = clippedYTop - yBottom\n    \
        \                if clippedHeight > 0 {\n                        clippedRectsBelow.append((x,\
        \ yBottom, l, clippedHeight))\n                    }\n                }\n  \
        \          }\n\n            let areaBelowMid = calculateUniqueArea(clippedRectsBelow)\n\
        \n            if areaBelowMid >= targetAreaBelow {\n                ans = mid;\n\
        \                high = mid;\n            } else {\n                low = mid;\n\
        \            }\n        }\n\n        return ans;\n    }\n}"
      kotlin: "class Solution {\n    data class Node(var count: Int = 0, var length:\
        \ Long = 0L)\n\n    private lateinit var xCoordsUnique: List<Long>\n    private\
        \ lateinit var tree: Array<Node>\n    private var xMapSize: Int = 0\n\n    private\
        \ fun update(nodeIdx: Int, nodeRangeStartIdx: Int, nodeRangeEndIdx: Int,\n \
        \                      queryStartIdx: Int, queryEndIdx: Int, delta: Int) {\n\
        \        if (queryStartIdx >= nodeRangeEndIdx || queryEndIdx <= nodeRangeStartIdx)\
        \ {\n            return\n        }\n\n        if (queryStartIdx <= nodeRangeStartIdx\
        \ && nodeRangeEndIdx <= queryEndIdx) {\n            tree[nodeIdx].count += delta\n\
        \            recalculateLength(nodeIdx, nodeRangeStartIdx, nodeRangeEndIdx)\n\
        \            return\n        }\n\n        val midIdx = nodeRangeStartIdx + (nodeRangeEndIdx\
        \ - nodeRangeStartIdx) / 2\n        update(nodeIdx * 2, nodeRangeStartIdx, midIdx,\
        \ queryStartIdx, queryEndIdx, delta)\n        update(nodeIdx * 2 + 1, midIdx,\
        \ nodeRangeEndIdx, queryStartIdx, queryEndIdx, delta)\n\n        recalculateLength(nodeIdx,\
        \ nodeRangeStartIdx, nodeRangeEndIdx)\n    }\n\n    private fun recalculateLength(nodeIdx:\
        \ Int, nodeRangeStartIdx: Int, nodeRangeEndIdx: Int) {\n        if (tree[nodeIdx].count\
        \ > 0) {\n            tree[nodeIdx].length = xCoordsUnique[nodeRangeEndIdx]\
        \ - xCoordsUnique[nodeRangeStartIdx]\n        } else {\n            if (nodeRangeStartIdx\
        \ + 1 == nodeRangeEndIdx) {\n                tree[nodeIdx].length = 0L\n   \
        \         } else {\n                tree[nodeIdx].length = tree[nodeIdx * 2].length\
        \ + tree[nodeIdx * 2 + 1].length\n            }\n        }\n    }\n\n    private\
        \ fun mapXToIdx(xVal: Long): Int {\n        return xCoordsUnique.binarySearch(xVal).let\
        \ { if (it < 0) -it - 1 else it }\n    }\n\n    fun separateSquares(squares:\
        \ Array<IntArray>): Double {\n        val xSet = mutableSetOf<Long>()\n    \
        \    val sweepEvents = mutableListOf<SweepEvent>()\n\n        for (s in squares)\
        \ {\n            val x = s[0].toLong()\n            val y = s[1].toLong()\n\
        \            val l = s[2].toLong()\n            xSet.add(x)\n            xSet.add(x\
        \ + l)\n            sweepEvents.add(SweepEvent(y, x, x + l, 1))\n          \
        \  sweepEvents.add(SweepEvent(y + l, x, x + l, -1))\n        }\n\n        xCoordsUnique\
        \ = xSet.sorted()\n        xMapSize = xCoordsUnique.size - 1\n\n        if (xMapSize\
        \ == 0) {\n            return squares.minOf { it[1] }.toDouble()\n        }\n\
        \n        sweepEvents.sortWith(compareBy<SweepEvent> { it.y }.thenBy { it.type\
        \ })\n\n        tree = Array(4 * xMapSize) { Node() }\n\n        // First pass:\
        \ Calculate total unique area\n        var totalArea: Long = 0L\n        var\
        \ prevY: Long = sweepEvents[0].y\n\n        for (event in sweepEvents) {\n \
        \           val currY = event.y\n            if (currY > prevY) {\n        \
        \        totalArea += tree[1].length * (currY - prevY)\n            }\n\n  \
        \          val xStartIdx = mapXToIdx(event.xStart)\n            val xEndIdx\
        \ = mapXToIdx(event.xEnd)\n            if (xStartIdx < xEndIdx) {\n        \
        \        update(1, 0, xMapSize, xStartIdx, xEndIdx, event.type)\n          \
        \  }\n            prevY = currY\n        }\n\n        val targetArea = totalArea.toDouble()\
        \ / 2.0\n\n        // Second pass: Find the split y-coordinate\n        tree\
        \ = Array(4 * xMapSize) { Node() }\n        var currentAreaBelowLine: Double\
        \ = 0.0\n        prevY = sweepEvents[0].y\n\n        for (event in sweepEvents)\
        \ {\n            val currY = event.y\n            if (currY > prevY) {\n   \
        \             val currentWidth = tree[1].length\n                val areaInStrip\
        \ = currentWidth * (currY - prevY)\n\n                if (currentAreaBelowLine\
        \ + areaInStrip >= targetArea) {\n                    val remainingAreaNeeded\
        \ = targetArea - currentAreaBelowLine\n                    if (currentWidth\
        \ == 0L) {\n                        return prevY.toDouble()\n              \
        \      }\n                    return prevY.toDouble() + remainingAreaNeeded\
        \ / currentWidth.toDouble()\n                }\n                currentAreaBelowLine\
        \ += areaInStrip.toDouble()\n            }\n\n            val xStartIdx = mapXToIdx(event.xStart)\n\
        \            val xEndIdx = mapXToIdx(event.xEnd)\n            if (xStartIdx\
        \ < xEndIdx) {\n                update(1, 0, xMapSize, xStartIdx, xEndIdx, event.type)\n\
        \            }\n            prevY = currY\n        }\n\n        return prevY.toDouble()\n\
        \    }\n\n    data class SweepEvent(val y: Long, val xStart: Long, val xEnd:\
        \ Long, val type: Int)\n}"
      dart: "class Solution {\n  late List<int> _xCoordsUnique;\n  late List<_Node>\
        \ _tree;\n  late int _xMapSize;\n\n  _Node _createNode() => _Node(0, 0);\n\n\
        \  void _update(int nodeIdx, int nodeRangeStartIdx, int nodeRangeEndIdx,\n \
        \     int queryStartIdx, int queryEndIdx, int delta) {\n    if (queryStartIdx\
        \ >= nodeRangeEndIdx || queryEndIdx <= nodeRangeStartIdx) {\n      return;\n\
        \    }\n\n    if (queryStartIdx <= nodeRangeStartIdx && nodeRangeEndIdx <= queryEndIdx)\
        \ {\n      _tree[nodeIdx].count += delta;\n      _recalculateLength(nodeIdx,\
        \ nodeRangeStartIdx, nodeRangeEndIdx);\n      return;\n    }\n\n    int midIdx\
        \ = nodeRangeStartIdx + (nodeRangeEndIdx - nodeRangeStartIdx) ~/ 2;\n    _update(nodeIdx\
        \ * 2, nodeRangeStartIdx, midIdx, queryStartIdx, queryEndIdx, delta);\n    _update(nodeIdx\
        \ * 2 + 1, midIdx, nodeRangeEndIdx, queryStartIdx, queryEndIdx, delta);\n\n\
        \    _recalculateLength(nodeIdx, nodeRangeStartIdx, nodeRangeEndIdx);\n  }\n\
        \n  void _recalculateLength(int nodeIdx, int nodeRangeStartIdx, int nodeRangeEndIdx)\
        \ {\n    if (_tree[nodeIdx].count > 0) {\n      _tree[nodeIdx].length = _xCoordsUnique[nodeRangeEndIdx]\
        \ - _xCoordsUnique[nodeRangeStartIdx];\n    } else {\n      if (nodeRangeStartIdx\
        \ + 1 == nodeRangeEndIdx) {\n        _tree[nodeIdx].length = 0;\n      } else\
        \ {\n        _tree[nodeIdx].length = _tree[nodeIdx * 2].length + _tree[nodeIdx\
        \ * 2 + 1].length;\n      }\n    }\n  }\n\n  int _mapXToIdx(int xVal) {\n  \
        \  int low = 0;\n    int high = _xCoordsUnique.length - 1;\n    int ans = _xCoordsUnique.length;\n\
        \    while (low <= high) {\n      int mid = low + (high - low) ~/ 2;\n     \
        \ if (_xCoordsUnique[mid] >= xVal) {\n        ans = mid;\n        high = mid\
        \ - 1;\n      } else {\n        low = mid + 1;\n      }\n    }\n    return ans;\n\
        \  }\n\n  double separateSquares(List<List<int>> squares) {\n    Set<int> xSet\
        \ = {};\n    List<_SweepEvent> sweepEvents = [];\n\n    for (var s in squares)\
        \ {\n      int x = s[0];\n      int y = s[1];\n      int l = s[2];\n      xSet.add(x);\n\
        \      xSet.add(x + l);\n      sweepEvents.add(_SweepEvent(y, x, x + l, 1));\n\
        \      sweepEvents.add(_SweepEvent(y + l, x, x + l, -1));\n    }\n\n    _xCoordsUnique\
        \ = xSet.toList()..sort();\n    _xMapSize = _xCoordsUnique.length - 1;\n\n \
        \   if (_xMapSize == 0) {\n      return squares.map((s) => s[1]).reduce((a,\
        \ b) => a < b ? a : b).toDouble();\n    }\n\n    sweepEvents.sort((a, b) {\n\
        \      if (a.y != b.y) return a.y.compareTo(b.y);\n      return a.type.compareTo(b.type);\n\
        \    });\n\n    _tree = List.generate(4 * _xMapSize, (index) => _createNode());\n\
        \n    // First pass: Calculate total unique area\n    int totalArea = 0;\n \
        \   int prevY = sweepEvents[0].y;\n\n    for (var event in sweepEvents) {\n\
        \      int currY = event.y;\n      if (currY > prevY) {\n        totalArea +=\
        \ _tree[1].length * (currY - prevY);\n      }\n\n      int xStartIdx = _mapXToIdx(event.xStart);\n\
        \      int xEndIdx = _mapXToIdx(event.xEnd);\n      if (xStartIdx < xEndIdx)\
        \ {\n        _update(1, 0, _xMapSize, xStartIdx, xEndIdx, event.type);\n   \
        \   }\n      prevY = currY;\n    }\n\n    double targetArea = totalArea.toDouble()\
        \ / 2.0;\n\n    // Second pass: Find the split y-coordinate\n    _tree = List.generate(4\
        \ * _xMapSize, (index) => _createNode());\n    double currentAreaBelowLine =\
        \ 0.0;\n    prevY = sweepEvents[0].y;\n\n    for (var event in sweepEvents)\
        \ {\n      int currY = event.y;\n      if (currY > prevY) {\n        int currentWidth\
        \ = _tree[1].length;\n        int areaInStrip = currentWidth * (currY - prevY);\n\
        \n        if (currentAreaBelowLine + areaInStrip >= targetArea) {\n        \
        \  double remainingAreaNeeded = targetArea - currentAreaBelowLine;\n       \
        \   if (currentWidth == 0) {\n            return prevY.toDouble();\n       \
        \   }\n          return prevY.toDouble() + remainingAreaNeeded / currentWidth.toDouble();\n\
        \        }\n        currentAreaBelowLine += areaInStrip.toDouble();\n      }\n\
        \n      int xStartIdx = _mapXToIdx(event.xStart);\n      int xEndIdx = _mapXToIdx(event.xEnd);\n\
        \      if (xStartIdx < xEndIdx) {\n        _update(1, 0, _xMapSize, xStartIdx,\
        \ xEndIdx, event.type);\n      }\n      prevY = currY;\n    }\n\n    return\
        \ prevY.toDouble();\n  }\n}\n\nclass _Node {\n  int count;\n  int length;\n\
        \  _Node(this.count, this.length);\n}\n\nclass _SweepEvent {\n  int y;\n  int\
        \ xStart;\n  int xEnd;\n  int type;\n  _SweepEvent(this.y, this.xStart, this.xEnd,\
        \ this.type);\n}"
      go: "package main\n\nimport (\n\t\"sort\"\n)\n\ntype Node struct {\n    count\
        \  int\n    length int\n}\n\ntype SweepEvent struct {\n    y      int\n    xStart\
        \ int\n    xEnd   int\n    typ    int // 1 for start, -1 for end\n}\n\nvar xCoordsUnique\
        \ []int\nvar tree []Node\nvar xMapSize int\n\nfunc update(nodeIdx, nodeRangeStartIdx,\
        \ nodeRangeEndIdx,\n    queryStartIdx, queryEndIdx, delta int) {\n    if queryStartIdx\
        \ >= nodeRangeEndIdx || queryEndIdx <= nodeRangeStartIdx {\n        return\n\
        \    }\n\n    if queryStartIdx <= nodeRangeStartIdx && nodeRangeEndIdx <= queryEndIdx\
        \ {\n        tree[nodeIdx].count += delta\n        recalculateLength(nodeIdx,\
        \ nodeRangeStartIdx, nodeRangeEndIdx)\n        return\n    }\n\n    midIdx :=\
        \ nodeRangeStartIdx + (nodeRangeEndIdx - nodeRangeStartIdx) / 2\n    update(nodeIdx\
        \ * 2, nodeRangeStartIdx, midIdx, queryStartIdx, queryEndIdx, delta)\n    update(nodeIdx\
        \ * 2 + 1, midIdx, nodeRangeEndIdx, queryStartIdx, queryEndIdx, delta)\n\n \
        \   recalculateLength(nodeIdx, nodeRangeStartIdx, nodeRangeEndIdx)\n}\n\nfunc\
        \ recalculateLength(nodeIdx, nodeRangeStartIdx, nodeRangeEndIdx int) {\n   \
        \ if tree[nodeIdx].count > 0 {\n        tree[nodeIdx].length = xCoordsUnique[nodeRangeEndIdx]\
        \ - xCoordsUnique[nodeRangeStartIdx]\n    } else {\n        if nodeRangeStartIdx\
        \ + 1 == nodeRangeEndIdx {\n            tree[nodeIdx].length = 0\n        }\
        \ else {\n            tree[nodeIdx].length = tree[nodeIdx * 2].length + tree[nodeIdx\
        \ * 2 + 1].length\n        }\n    }\n}\n\nfunc mapXToIdx(xVal int) int {\n \
        \   low := 0\n    high := len(xCoordsUnique) - 1\n    ans := len(xCoordsUnique)\n\
        \    for low <= high {\n        mid := low + (high - low) / 2\n        if xCoordsUnique[mid]\
        \ >= xVal {\n            ans = mid\n            high = mid - 1\n        } else\
        \ {\n            low = mid + 1\n        }\n    }\n    return ans\n}\n\nfunc\
        \ separateSquares(squares [][]int) float64 {\n    xSet := make(map[int]bool)\n\
        \    var sweepEvents []SweepEvent\n\n    for _, s := range squares {\n     \
        \   x, y, l := s[0], s[1], s[2]\n        xSet[x] = true\n        xSet[x+l] =\
        \ true\n        sweepEvents = append(sweepEvents, SweepEvent{y, x, x + l, 1})\n\
        \        sweepEvents = append(sweepEvents, SweepEvent{y + l, x, x + l, -1})\n\
        \    }\n\n    xCoordsUnique = make([]int, 0, len(xSet))\n    for xVal := range\
        \ xSet {\n        xCoordsUnique = append(xCoordsUnique, xVal)\n    }\n    sort.Ints(xCoordsUnique)\n\
        \n    xMapSize = len(xCoordsUnique) - 1\n\n    if xMapSize == 0 {\n        minY\
        \ := squares[0][1]\n        for i := 1; i < len(squares); i++ {\n          \
        \  if squares[i][1] < minY {\n                minY = squares[i][1]\n       \
        \     }\n        }\n        return float64(minY)\n    }\n\n    sort.Slice(sweepEvents,\
        \ func(i, j int) bool {\n        if sweepEvents[i].y != sweepEvents[j].y {\n\
        \            return sweepEvents[i].y < sweepEvents[j].y\n        }\n       \
        \ return sweepEvents[i].typ < sweepEvents[j].typ\n    })\n\n    tree = make([]Node,\
        \ 4 * xMapSize)\n\n    // First pass: Calculate total unique area\n    totalArea\
        \ := 0\n    prevY := sweepEvents[0].y\n\n    for _, event := range sweepEvents\
        \ {\n        currY := event.y\n        if currY > prevY {\n            totalArea\
        \ += tree[1].length * (currY - prevY)\n        }\n\n        xStartIdx := mapXToIdx(event.xStart)\n\
        \        xEndIdx := mapXToIdx(event.xEnd)\n        if xStartIdx < xEndIdx {\n\
        \            update(1, 0, xMapSize, xStartIdx, xEndIdx, event.typ)\n       \
        \ }\n        prevY = currY\n    }\n\n    targetArea := float64(totalArea) /\
        \ 2.0\n\n    // Second pass: Find the split y-coordinate\n    tree = make([]Node,\
        \ 4 * xMapSize)\n    currentAreaBelowLine := 0.0\n    prevY = sweepEvents[0].y\n\
        \n    for _, event := range sweepEvents {\n        currY := event.y\n      \
        \  if currY > prevY {\n            currentWidth := tree[1].length\n        \
        \    areaInStrip := currentWidth * (currY - prevY)\n\n            if currentAreaBelowLine\
        \ + float64(areaInStrip) >= targetArea {\n                remainingAreaNeeded\
        \ := targetArea - currentAreaBelowLine\n                if currentWidth == 0\
        \ {\n                    return float64(prevY)\n                }\n        \
        \        return float64(prevY) + remainingAreaNeeded / float64(currentWidth)\n\
        \            }\n            currentAreaBelowLine += float64(areaInStrip)\n \
        \       }\n\n        xStartIdx := mapXToIdx(event.xStart)\n        xEndIdx :=\
        \ mapXToIdx(event.xEnd)\n        if xStartIdx < xEndIdx {\n            update(1,\
        \ 0, xMapSize, xStartIdx, xEndIdx, event.typ)\n        }\n        prevY = currY\n\
        \    }\n\n    return float64(prevY)\n}"
      ruby: "require 'set'\n\n# @param {Integer[][]} squares\n# @return {Float}\ndef\
        \ separate_squares(squares)\n    x_set = Set.new\n    sweep_events = []\n\n\
        \    squares.each do |s|\n        x, y, l = s[0], s[1], s[2]\n        x_set.add(x)\n\
        \        x_set.add(x + l)\n        sweep_events << {y: y, x_start: x, x_end:\
        \ x + l, type: 1}\n        sweep_events << {y: y + l, x_start: x, x_end: x +\
        \ l, type: -1}\n    end\n\n    $x_coords_unique = x_set.to_a.sort\n    $x_map_size\
        \ = $x_coords_unique.length - 1\n\n    if $x_map_size == 0\n        return squares.map\
        \ { |s| s[1] }.min.to_f\n    end\n\n    sweep_events.sort! do |a, b|\n     \
        \   if a[:y] != b[:y]\n            a[:y] <=> b[:y]\n        else\n         \
        \   a[:type] <=> b[:type]\n        end\n    end\n\n    $tree = Array.new(4 *\
        \ $x_map_size) { {count: 0, length: 0} }\n\n    # First pass: Calculate total\
        \ unique area\n    total_area = 0\n    prev_y = sweep_events[0][:y]\n\n    sweep_events.each\
        \ do |event|\n        curr_y = event[:y]\n        if curr_y > prev_y\n     \
        \       total_area += $tree[1][:length] * (curr_y - prev_y)\n        end\n\n\
        \        x_start_idx = map_x_to_idx(event[:x_start])\n        x_end_idx = map_x_to_idx(event[:x_end])\n\
        \        if x_start_idx < x_end_idx\n            update_segment_tree(1, 0, $x_map_size,\
        \ x_start_idx, x_end_idx, event[:type])\n        end\n        prev_y = curr_y\n\
        \    end\n\n    target_area = total_area.to_f / 2.0\n\n    # Second pass: Find\
        \ the split y-coordinate\n    $tree = Array.new(4 * $x_map_size) { {count: 0,\
        \ length: 0} }\n    current_area_below_line = 0.0\n    prev_y = sweep_events[0][:y]\n\
        \n    sweep_events.each do |event|\n        curr_y = event[:y]\n        if curr_y\
        \ > prev_y\n            current_width = $tree[1][:length]\n            area_in_strip\
        \ = current_width * (curr_y - prev_y)\n\n            if current_area_below_line\
        \ + area_in_strip >= target_area\n                remaining_area_needed = target_area\
        \ - current_area_below_line\n                if current_width == 0\n       \
        \             return prev_y.to_f\n                end\n                return\
        \ prev_y.to_f + remaining_area_needed / current_width.to_f\n            end\n\
        \            current_area_below_line += area_in_strip.to_f\n        end\n\n\
        \        x_start_idx = map_x_to_idx(event[:x_start])\n        x_end_idx = map_x_to_idx(event[:x_end])\n\
        \        if x_start_idx < x_end_idx\n            update_segment_tree(1, 0, $x_map_size,\
        \ x_start_idx, x_end_idx, event[:type])\n        end\n        prev_y = curr_y\n\
        \    end\n\n    prev_y.to_f\nend\n\ndef update_segment_tree(node_idx, node_range_start_idx,\
        \ node_range_end_idx,\n                       query_start_idx, query_end_idx,\
        \ delta)\n    if query_start_idx >= node_range_end_idx || query_end_idx <= node_range_start_idx\n\
        \        return\n    end\n\n    if query_start_idx <= node_range_start_idx &&\
        \ node_range_end_idx <= query_end_idx\n        $tree[node_idx][:count] += delta\n\
        \        recalculate_length(node_idx, node_range_start_idx, node_range_end_idx)\n\
        \        return\n    end\n\n    mid_idx = node_range_start_idx + (node_range_end_idx\
        \ - node_range_start_idx) / 2\n    update_segment_tree(node_idx * 2, node_range_start_idx,\
        \ mid_idx, query_start_idx, query_end_idx, delta)\n    update_segment_tree(node_idx\
        \ * 2 + 1, mid_idx, node_range_end_idx, query_start_idx, query_end_idx, delta)\n\
        \n    recalculate_length(node_idx, node_range_start_idx, node_range_end_idx)\n\
        end\n\ndef recalculate_length(node_idx, node_range_start_idx, node_range_end_idx)\n\
        \    if $tree[node_idx][:count] > 0\n        $tree[node_idx][:length] = $x_coords_unique[node_range_end_idx]\
        \ - $x_coords_unique[node_range_start_idx]\n    else\n        if node_range_start_idx\
        \ + 1 == node_range_end_idx\n            $tree[node_idx][:length] = 0\n    \
        \    else\n            $tree[node_idx][:length] = $tree[node_idx * 2][:length]\
        \ + $tree[node_idx * 2 + 1][:length]\n        end\n    end\nend\n\ndef map_x_to_idx(x_val)\n\
        \    $x_coords_unique.bsearch_index { |x| x >= x_val }\nend"
      scala: "import scala.collection.mutable\n\nobject Solution {\n    case class Node(var\
        \ count: Int, var length: Long)\n\n    private var xCoordsUnique: Array[Long]\
        \ = _\n    private var tree: Array[Node] = _\n    private var xMapSize: Int\
        \ = _\n\n    private def update(nodeIdx: Int, nodeRangeStartIdx: Int, nodeRangeEndIdx:\
        \ Int,\n                       queryStartIdx: Int, queryEndIdx: Int, delta:\
        \ Int): Unit = {\n        if (queryStartIdx >= nodeRangeEndIdx || queryEndIdx\
        \ <= nodeRangeStartIdx) {\n            return\n        }\n\n        if (queryStartIdx\
        \ <= nodeRangeStartIdx && nodeRangeEndIdx <= queryEndIdx) {\n            tree(nodeIdx).count\
        \ += delta\n            recalculateLength(nodeIdx, nodeRangeStartIdx, nodeRangeEndIdx)\n\
        \            return\n        }\n\n        val midIdx = nodeRangeStartIdx + (nodeRangeEndIdx\
        \ - nodeRangeStartIdx) / 2\n        update(nodeIdx * 2, nodeRangeStartIdx, midIdx,\
        \ queryStartIdx, queryEndIdx, delta)\n        update(nodeIdx * 2 + 1, midIdx,\
        \ nodeRangeEndIdx, queryStartIdx, queryEndIdx, delta)\n\n        recalculateLength(nodeIdx,\
        \ nodeRangeStartIdx, nodeRangeEndIdx)\n    }\n\n    private def recalculateLength(nodeIdx:\
        \ Int, nodeRangeStartIdx: Int, nodeRangeEndIdx: Int): Unit = {\n        if (tree(nodeIdx).count\
        \ > 0) {\n            tree(nodeIdx).length = xCoordsUnique(nodeRangeEndIdx)\
        \ - xCoordsUnique(nodeRangeStartIdx)\n        } else {\n            if (nodeRangeStartIdx\
        \ + 1 == nodeRangeEndIdx) {\n                tree(nodeIdx).length = 0L\n   \
        \         } else {\n                tree(nodeIdx).length = tree(nodeIdx * 2).length\
        \ + tree(nodeIdx * 2 + 1).length\n            }\n        }\n    }\n\n    private\
        \ def mapXToIdx(xVal: Long): Int = {\n        val idx = java.util.Arrays.binarySearch(xCoordsUnique,\
        \ xVal)\n        if (idx < 0) -idx - 1 else idx\n    }\n\n    def separateSquares(squares:\
        \ Array[Array[Int]]): Double = {\n        val xSet = mutable.Set.empty[Long]\n\
        \        val sweepEvents = mutable.ArrayBuffer.empty[SweepEvent]\n\n       \
        \ for (s <- squares) {\n            val x = s(0).toLong\n            val y =\
        \ s(1).toLong\n            val l = s(2).toLong\n            xSet.add(x)\n  \
        \          xSet.add(x + l)\n            sweepEvents += SweepEvent(y, x, x +\
        \ l, 1)\n            sweepEvents += SweepEvent(y + l, x, x + l, -1)\n      \
        \  }\n\n        xCoordsUnique = xSet.toArray.sorted\n        xMapSize = xCoordsUnique.length\
        \ - 1\n\n        if (xMapSize == 0) {\n            return squares.map(_(1)).min.toDouble\n\
        \        }\n\n        sweepEvents.sortWith((a, b) => {\n            if (a.y\
        \ != b.y) a.y < b.y\n            else a.type < b.type\n        })\n\n      \
        \  tree = Array.fill(4 * xMapSize)(Node(0, 0L))\n\n        // First pass: Calculate\
        \ total unique area\n        var totalArea: Long = 0L\n        var prevY: Long\
        \ = sweepEvents.head.y\n\n        for (event <- sweepEvents) {\n           \
        \ val currY = event.y\n            if (currY > prevY) {\n                totalArea\
        \ += tree(1).length * (currY - prevY)\n            }\n\n            val xStartIdx\
        \ = mapXToIdx(event.xStart)\n            val xEndIdx = mapXToIdx(event.xEnd)\n\
        \            if (xStartIdx < xEndIdx) {\n                update(1, 0, xMapSize,\
        \ xStartIdx, xEndIdx, event.type)\n            }\n            prevY = currY\n\
        \        }\n\n        val targetArea = totalArea.toDouble / 2.0\n\n        //\
        \ Second pass: Find the split y-coordinate\n        tree = Array.fill(4 * xMapSize)(Node(0,\
        \ 0L))\n        var currentAreaBelowLine: Double = 0.0\n        prevY = sweepEvents.head.y\n\
        \n        for (event <- sweepEvents) {\n            val currY = event.y\n  \
        \          if (currY > prevY) {\n                val currentWidth = tree(1).length\n\
        \                val areaInStrip = currentWidth * (currY - prevY)\n\n      \
        \          if (currentAreaBelowLine + areaInStrip >= targetArea) {\n       \
        \             val remainingAreaNeeded = targetArea - currentAreaBelowLine\n\
        \                    if (currentWidth == 0L) {\n                        return\
        \ prevY.toDouble\n                    }\n                    return prevY.toDouble\
        \ + remainingAreaNeeded / currentWidth.toDouble\n                }\n       \
        \         currentAreaBelowLine += areaInStrip.toDouble\n            }\n\n  \
        \          val xStartIdx = mapXToIdx(event.xStart)\n            val xEndIdx\
        \ = mapXToIdx(event.xEnd)\n            if (xStartIdx < xEndIdx) {\n        \
        \        update(1, 0, xMapSize, xStartIdx, xEndIdx, event.type)\n          \
        \  }\n            prevY = currY\n        }\n\n        prevY.toDouble\n    }\n\
        \n    case class SweepEvent(y: Long, xStart: Long, xEnd: Long, `type`: Int)\n\
        }"
      rust: "use std::collections::{BTreeSet, HashMap};\n\nstruct Node {\n    count:\
        \ i32,\n    length: i64,\n}\n\nstruct SweepEvent {\n    y: i64,\n    x_start:\
        \ i64,\n    x_end: i64,\n    event_type: i32, // 1 for start, -1 for end\n}\n\
        \nstruct SegmentTree {\n    x_coords_unique: Vec<i64>,\n    tree: Vec<Node>,\n\
        \    x_map_size: usize,\n}\n\nimpl SegmentTree {\n    fn new(x_coords_unique:\
        \ Vec<i64>) -> Self {\n        let x_map_size = x_coords_unique.len() - 1;\n\
        \        let tree = vec![Node { count: 0, length: 0 }; 4 * x_map_size];\n  \
        \      SegmentTree {\n            x_coords_unique,\n            tree,\n    \
        \        x_map_size,\n        }\n    }\n\n    fn update(&mut self, node_idx:\
        \ usize, node_range_start_idx: usize, node_range_end_idx: usize,\n         \
        \     query_start_idx: usize, query_end_idx: usize, delta: i32) {\n        if\
        \ query_start_idx >= node_range_end_idx || query_end_idx <= node_range_start_idx\
        \ {\n            return;\n        }\n\n        if query_start_idx <= node_range_start_idx\
        \ && node_range_end_idx <= query_end_idx {\n            self.tree[node_idx].count\
        \ += delta;\n            self.recalculate_length(node_idx, node_range_start_idx,\
        \ node_range_end_idx);\n            return;\n        }\n\n        let mid_idx\
        \ = node_range_start_idx + (node_range_end_idx - node_range_start_idx) / 2;\n\
        \        self.update(node_idx * 2, node_range_start_idx, mid_idx, query_start_idx,\
        \ query_end_idx, delta);\n        self.update(node_idx * 2 + 1, mid_idx, node_range_end_idx,\
        \ query_start_idx, query_end_idx, delta);\n\n        self.recalculate_length(node_idx,\
        \ node_range_start_idx, node_range_end_idx);\n    }\n\n    fn recalculate_length(&mut\
        \ self, node_idx: usize, node_range_start_idx: usize, node_range_end_idx: usize)\
        \ {\n        if self.tree[node_idx].count > 0 {\n            self.tree[node_idx].length\
        \ = self.x_coords_unique[node_range_end_idx] - self.x_coords_unique[node_range_start_idx];\n\
        \        } else {\n            if node_range_start_idx + 1 == node_range_end_idx\
        \ {\n                self.tree[node_idx].length = 0;\n            } else {\n\
        \                self.tree[node_idx].length = self.tree[node_idx * 2].length\
        \ + self.tree[node_idx * 2 + 1].length;\n            }\n        }\n    }\n\n\
        \    fn map_x_to_idx(&self, x_val: i64) -> usize {\n        match self.x_coords_unique.binary_search(&x_val)\
        \ {\n            Ok(idx) => idx,\n            Err(idx) => idx,\n        }\n\
        \    }\n\n    fn get_total_length(&self) -> i64 {\n        self.tree[1].length\n\
        \    }\n}\n\nimpl Solution {\n    pub fn separate_squares(squares: Vec<Vec<i32>>)\
        \ -> f64 {\n        let mut x_set = BTreeSet::new();\n        let mut sweep_events:\
        \ Vec<SweepEvent> = Vec::new();\n\n        for s in &squares {\n           \
        \ let x = s[0] as i64;\n            let y = s[1] as i64;\n            let l\
        \ = s[2] as i64;\n            x_set.insert(x);\n            x_set.insert(x +\
        \ l);\n            sweep_events.push(SweepEvent { y, x_start: x, x_end: x +\
        \ l, event_type: 1 });\n            sweep_events.push(SweepEvent { y: y + l,\
        \ x_start: x, x_end: x + l, event_type: -1 });\n        }\n\n        let x_coords_unique:\
        \ Vec<i64> = x_set.into_iter().collect();\n\n        if x_coords_unique.len()\
        \ <= 1 {\n            return squares.iter().map(|s| s[1] as f64).min_by(|a,\
        \ b| a.partial_cmp(b).unwrap()).unwrap_or(0.0);\n        }\n\n        sweep_events.sort_by(|a,\
        \ b| {\n            if a.y != b.y {\n                a.y.cmp(&b.y)\n       \
        \     } else {\n                a.event_type.cmp(&b.event_type)\n          \
        \  }\n        });\n\n        let mut segment_tree = SegmentTree::new(x_coords_unique.clone());\n\
        \n        // First pass: Calculate total unique area\n        let mut total_area:\
        \ i64 = 0;\n        let mut prev_y: i64 = sweep_events[0].y;\n\n        for\
        \ event in &sweep_events {\n            let curr_y = event.y;\n            if\
        \ curr_y > prev_y {\n                total_area += segment_tree.get_total_length()\
        \ * (curr_y - prev_y);\n            }\n\n            let x_start_idx = segment_tree.map_x_to_idx(event.x_start);\n\
        \            let x_end_idx = segment_tree.map_x_to_idx(event.x_end);\n     \
        \       if x_start_idx < x_end_idx {\n                segment_tree.update(1,\
        \ 0, segment_tree.x_map_size, x_start_idx, x_end_idx, event.event_type);\n \
        \           }\n            prev_y = curr_y;\n        }\n\n        let target_area\
        \ = total_area as f64 / 2.0;\n\n        // Second pass: Find the split y-coordinate\n\
        \        let mut segment_tree_2 = SegmentTree::new(x_coords_unique);\n     \
        \   let mut current_area_below_line: f64 = 0.0;\n        prev_y = sweep_events[0].y;\n\
        \n        for event in &sweep_events {\n            let curr_y = event.y;\n\
        \            if curr_y > prev_y {\n                let current_width = segment_tree_2.get_total_length();\n\
        \                let area_in_strip = current_width * (curr_y - prev_y);\n\n\
        \                if current_area_below_line + area_in_strip as f64 >= target_area\
        \ {\n                    let remaining_area_needed = target_area - current_area_below_line;\n\
        \                    if current_width == 0 {\n                        return\
        \ prev_y as f64;\n                    }\n                    return prev_y as\
        \ f64 + remaining_area_needed / current_width as f64;\n                }\n \
        \               current_area_below_line += area_in_strip as f64;\n         \
        \   }\n\n            let x_start_idx = segment_tree_2.map_x_to_idx(event.x_start);\n\
        \            let x_end_idx = segment_tree_2.map_x_to_idx(event.x_end);\n   \
        \         if x_start_idx < x_end_idx {\n                segment_tree_2.update(1,\
        \ 0, segment_tree_2.x_map_size, x_start_idx, x_end_idx, event.event_type);\n\
        \            }\n            prev_y = curr_y;\n        }\n\n        prev_y as\
        \ f64\n    }\n}"
      racket: "#lang racket\n\n(struct node (count length) #:mutable #t)\n(struct sweep-event\
        \ (y x-start x-end type))\n\n(define x-coords-unique #f)\n(define tree #f)\n\
        (define x-map-size #f)\n\n(define (update-segment-tree node-idx node-range-start-idx\
        \ node-range-end-idx\n                             query-start-idx query-end-idx\
        \ delta)\n  (when (and (< query-start-idx node-range-end-idx)\n            \
        \ (> query-end-idx node-range-start-idx))\n    (if (and (<= query-start-idx\
        \ node-range-start-idx)\n             (>= query-end-idx node-range-end-idx))\n\
        \        (begin\n          (set-node-count! (vector-ref tree node-idx) (+ (node-count\
        \ (vector-ref tree node-idx)) delta))\n          (recalculate-length node-idx\
        \ node-range-start-idx node-range-end-idx))\n        (let* ((mid-idx (+ node-range-start-idx\
        \ (quotient (- node-range-end-idx node-range-start-idx) 2))))\n          (update-segment-tree\
        \ (* node-idx 2) node-range-start-idx mid-idx query-start-idx query-end-idx\
        \ delta)\n          (update-segment-tree (+ (* node-idx 2) 1) mid-idx node-range-end-idx\
        \ query-start-idx query-end-idx delta)\n          (recalculate-length node-idx\
        \ node-range-start-idx node-range-end-idx)))))\n\n(define (recalculate-length\
        \ node-idx node-range-start-idx node-range-end-idx)\n  (if (> (node-count (vector-ref\
        \ tree node-idx)) 0)\n      (set-node-length! (vector-ref tree node-idx)\n \
        \                       (- (vector-ref x-coords-unique node-range-end-idx)\n\
        \                           (vector-ref x-coords-unique node-range-start-idx)))\n\
        \      (if (= (+ node-range-start-idx 1) node-range-end-idx)\n          (set-node-length!\
        \ (vector-ref tree node-idx) 0)\n          (set-node-length! (vector-ref tree\
        \ node-idx)\n                            (+ (node-length (vector-ref tree (*\
        \ node-idx 2)))\n                               (node-length (vector-ref tree\
        \ (+ (* node-idx 2) 1))))))))\n\n(define (map-x-to-idx x-val)\n  (let loop ((low\
        \ 0) (high (- (vector-length x-coords-unique) 1)) (ans (vector-length x-coords-unique)))\n\
        \    (if (<= low high)\n        (let* ((mid (+ low (quotient (- high low) 2))))\n\
        \          (if (>= (vector-ref x-coords-unique mid) x-val)\n              (loop\
        \ low (- mid 1) mid)\n              (loop (+ mid 1) high ans)))\n        ans)))\n\
        \n(define/contract (separate-squares squares)\n  (-> (listof (listof exact-integer?))\
        \ flonum?)\n  (define x-set (make-hash))\n  (define sweep-events (make-list\
        \ 0))\n\n  (for-each (lambda (s)\n              (define x (list-ref s 0))\n\
        \              (define y (list-ref s 1))\n              (define l (list-ref\
        \ s 2))\n              (hash-set! x-set x #t)\n              (hash-set! x-set\
        \ (+ x l) #t)\n              (set! sweep-events (cons (sweep-event y x (+ x\
        \ l) 1) sweep-events))\n              (set! sweep-events (cons (sweep-event\
        \ (+ y l) x (+ x l) -1) sweep-events)))\n            squares)\n\n  (set! x-coords-unique\
        \ (list->vector (sort (hash-keys x-set) <)))\n  (set! x-map-size (- (vector-length\
        \ x-coords-unique) 1))\n\n  (when (= x-map-size 0)\n    (define min-y (apply\
        \ min (map (lambda (s) (list-ref s 1)) squares)))\n    (error 'separate-squares\
        \ \"x-map-size is 0, should not happen with l_i >= 1\"))\n\n  (set! sweep-events\
        \ (sort sweep-events (lambda (a b)\n                                       \
        \  (if (= (sweep-event-y a) (sweep-event-y b))\n                           \
        \                  (< (sweep-event-type a) (sweep-event-type b))\n         \
        \                                    (< (sweep-event-y a) (sweep-event-y b))))))\n\
        \n  (set! tree (build-vector (* 4 x-map-size) (lambda (i) (node 0 0))))\n\n\
        \  ;; First pass: Calculate total unique area\n  (define total-area 0)\n  (define\
        \ prev-y (sweep-event-y (car sweep-events)))\n\n  (for-each (lambda (event)\n\
        \              (define curr-y (sweep-event-y event))\n              (when (>\
        \ curr-y prev-y)\n                (set! total-area (+ total-area (* (node-length\
        \ (vector-ref tree 1)) (- curr-y prev-y)))))\n\n              (define x-start-idx\
        \ (map-x-to-idx (sweep-event-x-start event)))\n              (define x-end-idx\
        \ (map-x-to-idx (sweep-event-x-end event)))\n              (when (< x-start-idx\
        \ x-end-idx)\n                (update-segment-tree 1 0 x-map-size x-start-idx\
        \ x-end-idx (sweep-event-type event)))\n              (set! prev-y curr-y))\n\
        \            sweep-events)\n\n  (define target-area (/ (exact->flonum total-area)\
        \ 2.0))\n\n  ;; Second pass: Find the split y-coordinate\n  (set! tree (build-vector\
        \ (* 4 x-map-size) (lambda (i) (node 0 0))))\n  (define current-area-below-line\
        \ 0.0)\n  (set! prev-y (sweep-event-y (car sweep-events)))\n\n  (for-each (lambda\
        \ (event)\n              (define curr-y (sweep-event-y event))\n           \
        \   (when (> curr-y prev-y)\n                (define current-width (node-length\
        \ (vector-ref tree 1)))\n                (define area-in-strip (* current-width\
        \ (- curr-y prev-y)))\n\n                (when (>= (+ current-area-below-line\
        \ (exact->flonum area-in-strip)) target-area)\n                  (define remaining-area-needed\
        \ (- target-area current-area-below-line))\n                  (if (= current-width\
        \ 0)\n                      (error 'separate-squares \"current-width is 0 when\
        \ remaining-area-needed > 0\")\n                      (begin\n             \
        \           (set! x-coords-unique #f)\n                        (set! tree #f)\n\
        \                        (set! x-map-size #f)\n                        (exit\
        \ (+ (exact->flonum prev-y) (/ remaining-area-needed (exact->flonum current-width)))))))\n\
        \                (set! current-area-below-line (+ current-area-below-line (exact->flonum\
        \ area-in-strip))))\n\n              (define x-start-idx (map-x-to-idx (sweep-event-x-start\
        \ event)))\n              (define x-end-idx (map-x-to-idx (sweep-event-x-end\
        \ event)))\n              (when (< x-start-idx x-end-idx)\n                (update-segment-tree\
        \ 1 0 x-map-size x-start-idx x-end-idx (sweep-event-type event)))\n        \
        \      (set! prev-y curr-y))\n            sweep-events)\n\n  (set! x-coords-unique\
        \ #f)\n  (set! tree #f)\n  (set! x-map-size #f)\n  (exit (exact->flonum prev-y)))"
      erlang: "-spec separate_squares(Squares :: [[integer()]]) -> float().\nseparate_squares(Squares)\
        \ ->\n    XSet = sets:new(),\n    SweepEvents = [],\n\n    % Collect x-coordinates\
        \ and create sweep events\n    {FinalXSet, RawSweepEvents} = lists:foldl(fun(S,\
        \ {AccXSet, AccEvents}) ->\n        [X, Y, L] = S,\n        NewXSet = sets:add_element(X,\
        \ sets:add_element(X + L, AccXSet)),\n        NewEvents = [#{y => Y, x_start\
        \ => X, x_end => X + L, type => 1} | AccEvents] ++ \n                    [#{y\
        \ => Y + L, x_start => X, x_end => X + L, type => -1}],\n        {NewXSet, NewEvents}\n\
        \    end, {XSet, SweepEvents}, Squares),\n\n    XCoordsUniqueList = sets:to_list(FinalXSet),\n\
        \    XCoordsUnique = array:from_list(lists:sort(XCoordsUniqueList)),\n    XMapSize\
        \ = array:size(XCoordsUnique) - 1,\n\n    if XMapSize == 0 ->\n        MinY\
        \ = lists:min([S_i_1 || [_, S_i_1, _] <- Squares]),\n        float(MinY);\n\
        \    true ->\n        SortedSweepEvents = lists:sort(fun(A, B) ->\n        \
        \    case A#y of\n                B#y -> A#type < B#type;\n                _\
        \ -> A#y < B#y\n            end\n        end, RawSweepEvents),\n\n        Tree\
        \ = array:new(4 * XMapSize, [{default, #{count => 0, length => 0}}]),\n\n  \
        \      % First pass: Calculate total unique area\n        {TotalArea, _FinalTree1,\
        \ _FinalPrevY1} = lists:foldl(fun(Event, {AccArea, CurrentTree, PrevY}) ->\n\
        \            CurrY = Event#y,\n            NewAccArea = if CurrY > PrevY ->\n\
        \                RootNode = array:get(1, CurrentTree),\n                AccArea\
        \ + (RootNode#length * (CurrY - PrevY))\n            else\n                AccArea\n\
        \            end,\n\n            XStartIdx = map_x_to_idx(Event#x_start, XCoordsUnique),\n\
        \            XEndIdx = map_x_to_idx(Event#x_end, XCoordsUnique),\n         \
        \   UpdatedTree = if XStartIdx < XEndIdx ->\n                update_segment_tree(1,\
        \ 0, XMapSize, XStartIdx, XEndIdx, Event#type, CurrentTree, XCoordsUnique)\n\
        \            else\n                CurrentTree\n            end,\n         \
        \   {NewAccArea, UpdatedTree, CurrY}\n        end, {0, Tree, (hd SortedSweepEvents)#y},\
        \ SortedSweepEvents),\n\n        TargetArea = TotalArea / 2.0,\n\n        %\
        \ Second pass: Find the split y-coordinate\n        Tree2 = array:new(4 * XMapSize,\
        \ [{default, #{count => 0, length => 0}}]),\n        {_FinalAreaBelow, ResultY,\
        \ _FinalTree2, _FinalPrevY2} = lists:foldl(fun(Event, {AccAreaBelow, FoundY,\
        \ CurrentTree, PrevY}) ->\n            if FoundY =/= -1.0 -> % If already found,\
        \ just pass through\n                {AccAreaBelow, FoundY, CurrentTree, PrevY}\n\
        \            else\n                CurrY = Event#y,\n                {NewAccAreaBelow,\
        \ NewFoundY} = if CurrY > PrevY ->\n                    RootNode = array:get(1,\
        \ CurrentTree),\n                    CurrentWidth = RootNode#length,\n     \
        \               AreaInStrip = CurrentWidth * (CurrY - PrevY),\n\n          \
        \          if AccAreaBelow + AreaInStrip >= TargetArea ->\n                \
        \        RemainingAreaNeeded = TargetArea - AccAreaBelow,\n                \
        \        if CurrentWidth == 0 ->\n                            float(PrevY)\n\
        \                        else\n                            float(PrevY) + RemainingAreaNeeded\
        \ / float(CurrentWidth)\n                        end\n                    else\n\
        \                        {AccAreaBelow + AreaInStrip, -1.0}\n              \
        \      end\n                else\n                    {AccAreaBelow, -1.0}\n\
        \                end,\n\n                XStartIdx = map_x_to_idx(Event#x_start,\
        \ XCoordsUnique),\n                XEndIdx = map_x_to_idx(Event#x_end, XCoordsUnique),\n\
        \                UpdatedTree = if XStartIdx < XEndIdx ->\n                 \
        \   update_segment_tree(1, 0, XMapSize, XStartIdx, XEndIdx, Event#type, CurrentTree,\
        \ XCoordsUnique)\n                else\n                    CurrentTree\n  \
        \              end,\n                {NewAccAreaBelow, NewFoundY, UpdatedTree,\
        \ CurrY}\n            end\n        end, {0.0, -1.0, Tree2, (hd SortedSweepEvents)#y},\
        \ SortedSweepEvents),\n\n        ResultY\n    end.\n\nmap_x_to_idx(XVal, XCoordsUnique)\
        \ ->\n    array:foldl(fun(Idx, Val, Acc) ->\n        if Val >= XVal ->\n   \
        \         if Idx < Acc -> Idx else Acc end\n        else\n            Acc\n\
        \        end\n    end, array:size(XCoordsUnique), XCoordsUnique).\n\nupdate_segment_tree(NodeIdx,\
        \ NodeRangeStartIdx, NodeRangeEndIdx,\n                    QueryStartIdx, QueryEndIdx,\
        \ Delta, Tree, XCoordsUnique) ->\n    if QueryStartIdx >= NodeRangeEndIdx or\
        \ QueryEndIdx <= NodeRangeStartIdx ->\n        Tree;\n    true ->\n        Node\
        \ = array:get(NodeIdx, Tree),\n        if QueryStartIdx <= NodeRangeStartIdx\
        \ and NodeRangeEndIdx <= QueryEndIdx ->\n            NewNode = Node#{count :=\
        \ Node#count + Delta},\n            UpdatedTree = array:set(NodeIdx, NewNode,\
        \ Tree),\n            recalculate_length(NodeIdx, NodeRangeStartIdx, NodeRangeEndIdx,\
        \ UpdatedTree, XCoordsUnique)\n        else\n            MidIdx = NodeRangeStartIdx\
        \ + (NodeRangeEndIdx - NodeRangeStartIdx) div 2,\n            Tree1 = update_segment_tree(NodeIdx\
        \ * 2, NodeRangeStartIdx, MidIdx, QueryStartIdx, QueryEndIdx, Delta, Tree, XCoordsUnique),\n\
        \            Tree2 = update_segment_tree(NodeIdx * 2 + 1, MidIdx, NodeRangeEndIdx,\
        \ QueryStartIdx, QueryEndIdx, Delta, Tree1, XCoordsUnique),\n            recalculate_length(NodeIdx,\
        \ NodeRangeStartIdx, NodeRangeEndIdx, Tree2, XCoordsUnique)\n        end\n \
        \   end.\n\nrecalculate_length(NodeIdx, NodeRangeStartIdx, NodeRangeEndIdx,\
        \ Tree, XCoordsUnique) ->\n    Node = array:get(NodeIdx, Tree),\n    if Node#count\
        \ > 0 ->\n        NewLength = array:get(NodeRangeEndIdx, XCoordsUnique) - array:get(NodeRangeStartIdx,\
        \ XCoordsUnique),\n        array:set(NodeIdx, Node#{length := NewLength}, Tree)\n\
        \    else\n        if NodeRangeStartIdx + 1 == NodeRangeEndIdx ->\n        \
        \    array:set(NodeIdx, Node#{length := 0}, Tree)\n        else\n          \
        \  LeftChild = array:get(NodeIdx * 2, Tree),\n            RightChild = array:get(NodeIdx\
        \ * 2 + 1, Tree),\n            NewLength = LeftChild#length + RightChild#length,\n\
        \            array:set(NodeIdx, Node#{length := NewLength}, Tree)\n        end\n\
        \    end.\n\n-record(node, {count = 0, length = 0}).\n-record(sweepevent, {y,\
        \ x_start, x_end, type})."
      elixir: "defmodule Solution do\n  @spec separate_squares(squares :: [[integer]])\
        \ :: float\n  def separate_squares(squares) do\n    x_set = MapSet.new()\n \
        \   sweep_events = []\n\n    for s <- squares do\n      [x, y, l] = s\n    \
        \  x_set = MapSet.put(x_set, x)\n      x_set = MapSet.put(x_set, x + l)\n  \
        \    sweep_events = [ %{y: y, x_start: x, x_end: x + l, type: 1} | sweep_events\
        \ ]\n      sweep_events = [ %{y: y + l, x_start: x, x_end: x + l, type: -1}\
        \ | sweep_events ]\n    end\n\n    x_coords_unique = x_set |> MapSet.to_list()\
        \ |> Enum.sort()\n    x_map_size = length(x_coords_unique) - 1\n\n    if x_map_size\
        \ == 0 do\n      squares |> Enum.map(fn s -> List.first(tl(s)) end) |> Enum.min()\
        \ |> Kernel.float()\n    else\n      sweep_events = Enum.sort(sweep_events,\
        \ fn a, b ->\n        if a.y != b.y do\n          a.y < b.y\n        else\n\
        \          a.type < b.type\n        end\n      end)\n\n      initial_tree =\
        \ %{}\n      for i <- 1..(4 * x_map_size) do\n        initial_tree = Map.put(initial_tree,\
        \ i, %{count: 0, length: 0})\n      end\n\n      # First pass: Calculate total\
        \ unique area\n      {total_area, _final_tree, _final_prev_y} = Enum.reduce(sweep_events,\
        \ {0, initial_tree, List.first(sweep_events).y}, fn event, {acc_area, current_tree,\
        \ prev_y} ->\n        curr_y = event.y\n        new_acc_area = if curr_y > prev_y\
        \ do\n          root_node = Map.get(current_tree, 1)\n          acc_area + (root_node.length\
        \ * (curr_y - prev_y))\n        else\n          acc_area\n        end\n\n  \
        \      x_start_idx = map_x_to_idx(event.x_start, x_coords_unique)\n        x_end_idx\
        \ = map_x_to_idx(event.x_end, x_coords_unique)\n        updated_tree = if x_start_idx\
        \ < x_end_idx do\n          update_segment_tree(1, 0, x_map_size, x_start_idx,\
        \ x_end_idx, event.type, current_tree, x_coords_unique)\n        else\n    \
        \      current_tree\n        end\n        {new_acc_area, updated_tree, curr_y}\n\
        \      end)\n\n      target_area = Kernel.float(total_area) / 2.0\n\n      #\
        \ Second pass: Find the split y-coordinate\n      initial_tree_2 = %{}\n   \
        \   for i <- 1..(4 * x_map_size) do\n        initial_tree_2 = Map.put(initial_tree_2,\
        \ i, %{count: 0, length: 0})\n      end\n\n      {_final_area_below, result_y,\
        \ _final_tree_2, _final_prev_y_2} = Enum.reduce(sweep_events, {0.0, -1.0, initial_tree_2,\
        \ List.first(sweep_events).y}, fn event, {acc_area_below, found_y, current_tree,\
        \ prev_y} ->\n        if found_y != -1.0 do\n          {acc_area_below, found_y,\
        \ current_tree, prev_y}\n        else\n          curr_y = event.y\n        \
        \  {new_acc_area_below, new_found_y} = if curr_y > prev_y do\n            root_node\
        \ = Map.get(current_tree, 1)\n            current_width = root_node.length\n\
        \            area_in_strip = current_width * (curr_y - prev_y)\n\n         \
        \   if acc_area_below + Kernel.float(area_in_strip) >= target_area do\n    \
        \          remaining_area_needed = target_area - acc_area_below\n          \
        \    if current_width == 0 do\n                Kernel.float(prev_y)\n      \
        \        else\n                Kernel.float(prev_y) + remaining_area_needed\
        \ / Kernel.float(current_width)\n              end\n            else\n     \
        \         {acc_area_below + Kernel.float(area_in_strip), -1.0}\n           \
        \ end\n          else\n            {acc_area_below, -1.0}\n          end\n\n\
        \          x_start_idx = map_x_to_idx(event.x_start, x_coords_unique)\n    \
        \      x_end_idx = map_x_to_idx(event.x_end, x_coords_unique)\n          updated_tree\
        \ = if x_start_idx < x_end_idx do\n            update_segment_tree(1, 0, x_map_size,\
        \ x_start_idx, x_end_idx, event.type, current_tree, x_coords_unique)\n     \
        \     else\n            current_tree\n          end\n          {new_acc_area_below,\
        \ new_found_y, updated_tree, curr_y}\n        end\n      end)\n      result_y\n\
        \    end\n  end\n\n  defp update_segment_tree(node_idx, node_range_start_idx,\
        \ node_range_end_idx,\n                           query_start_idx, query_end_idx,\
        \ delta, tree, x_coords_unique) do\n    if query_start_idx >= node_range_end_idx\
        \ or query_end_idx <= node_range_start_idx do\n      tree\n    else\n      node\
        \ = Map.get(tree, node_idx)\n      if query_start_idx <= node_range_start_idx\
        \ and node_range_end_idx <= query_end_idx do\n        new_node = %{node | count:\
        \ node.count + delta}\n        updated_tree = Map.put(tree, node_idx, new_node)\n\
        \        recalculate_length(node_idx, node_range_start_idx, node_range_end_idx,\
        \ updated_tree, x_coords_unique)\n      else\n        mid_idx = node_range_start_idx\
        \ + div(node_range_end_idx - node_range_start_idx, 2)\n        tree1 = update_segment_tree(node_idx\
        \ * 2, node_range_start_idx, mid_idx, query_start_idx, query_end_idx, delta,\
        \ tree, x_coords_unique)\n        tree2 = update_segment_tree(node_idx * 2 +\
        \ 1, mid_idx, node_range_end_idx, query_start_idx, query_end_idx, delta, tree1,\
        \ x_coords_unique)\n        recalculate_length(node_idx, node_range_start_idx,\
        \ node_range_end_idx, tree2, x_coords_unique)\n      end\n    end\n  end\n\n\
        \  defp recalculate_length(node_idx, node_range_start_idx, node_range_end_idx,\
        \ tree, x_coords_unique) do\n    node = Map.get(tree, node_idx)\n    if node.count\
        \ > 0 do\n      new_length = Enum.at(x_coords_unique, node_range_end_idx) -\
        \ Enum.at(x_coords_unique, node_range_start_idx)\n      Map.put(tree, node_idx,\
        \ %{node | length: new_length})\n    else\n      if node_range_start_idx + 1\
        \ == node_range_end_idx do\n        Map.put(tree, node_idx, %{node | length:\
        \ 0})\n      else\n        left_child = Map.get(tree, node_idx * 2)\n      \
        \  right_child = Map.get(tree, node_idx * 2 + 1)\n        new_length = left_child.length\
        \ + right_child.length\n        Map.put(tree, node_idx, %{node | length: new_length})\n\
        \      end\n    end\n  end\n\n  defp map_x_to_idx(x_val, x_coords_unique) do\n\
        \    Enum.find_index(x_coords_unique, fn x -> x >= x_val end)\n  end\nend"
    approach: 'The problem requires finding a horizontal line `y` that divides the total
      unique area covered by a set of overlapping squares into two equal halves. This
      can be framed as finding a `y` such that the unique area below the line `y` is
      exactly half of the total unique area. Since the unique area below a line `y`
      is a monotonically increasing function of `y`, binary search is an appropriate
      technique to find this specific `y` value.


      To implement the binary search, we need a function `calculate_unique_area(rectangles)`
      that computes the total unique area covered by a given set of rectangles. This
      function is implemented using a standard line sweep algorithm combined with a
      segment tree. Events are created for the left and right vertical edges of each
      rectangle, storing `(x, type, y_bottom, y_top)`. All unique y-coordinates from
      these rectangles are collected, sorted, and used to build a segment tree. The
      segment tree maintains the total length of the union of active y-intervals at
      the current x-coordinate. As the sweep line moves from left to right, the area
      of each vertical strip `(current_x - prev_x) * active_length` is accumulated.
      The binary search iteratively refines the `y` coordinate. In each iteration, `mid
      = (low + high) / 2.0` is chosen. A new set of ''clipped'' rectangles is generated,
      representing the portions of original squares that lie below `mid`. The `calculate_unique_area`
      function is then called on these clipped rectangles. If the area below `mid` is
      greater than or equal to half of the total unique area, `mid` is a potential answer,
      and we try a smaller `y` by setting `high = mid`. Otherwise, `mid` is too low,
      and we set `low = mid`. This process is repeated for a fixed number of iterations
      (e.g., 100) to achieve the required precision.'
    time_complexity: The time complexity is dominated by the binary search and the `calculate_unique_area`
      function. The `calculate_unique_area` function involves sorting events (O(N log
      N)) and performing segment tree updates (N events, each O(log M), where M is the
      number of unique y-coordinates, M <= 2N). Thus, `calculate_unique_area` takes
      O(N log N) time. The binary search performs K iterations (e.g., 100). In each
      iteration, it constructs a new set of clipped rectangles (O(N)) and calls `calculate_unique_area`
      (O(N log N)). Therefore, the total time complexity is O(N log N + K * N log N),
      which simplifies to O(K * N log N).
    space_complexity: The space complexity is primarily determined by storing the events,
      the unique y-coordinates, and the segment tree. The events list stores up to 2N
      entries. The `y_coords` list stores up to 2N unique y-coordinates. The segment
      tree requires O(M) space, where M is the number of unique y-coordinates, so O(N)
      space. Overall, the space complexity is O(N).
    elapsed_time: 357.2766377925873
    model: gemini-2.5-flash
    generated_at: '2026-01-14 01:17:57 '
  - solutions:
      cpp: "class Solution {\npublic:\n    double separateSquares(vector<vector<int>>&\
        \ squares) {\n        sort(squares.begin(), squares.end(), [](vector<int>& a,\
        \ vector<int>& b) { return a[1] < b[1]; });\n        double low = squares[0][1],\
        \ high = squares[squares.size() - 1][1] + squares[squares.size() - 1][2];\n\
        \        while (high - low > 1e-5) {\n            double mid = (low + high)\
        \ / 2;\n            double areaAbove = 0, areaBelow = 0;\n            set<int>\
        \ counted;\n            for (auto& square : squares) {\n                if (square[1]\
        \ + square[2] > mid) {\n                    double overlap = max(0.0, min(square[1]\
        \ + square[2], mid) - max(square[1], mid));\n                    areaAbove +=\
        \ overlap * square[2];\n                }\n                if (square[1] < mid)\
        \ {\n                    double overlap = max(0.0, min(square[1] + square[2],\
        \ mid) - max(square[1], mid));\n                    areaBelow += overlap * square[2];\n\
        \                }\n            }\n            if (areaAbove > areaBelow) high\
        \ = mid;\n            else low = mid;\n        }\n        return low;\n    }\n\
        };"
      java: "class Solution {\n    public double separateSquares(int[][] squares) {\n\
        \        Arrays.sort(squares, (a, b) -> a[1] - b[1]);\n        double low =\
        \ squares[0][1], high = squares[squares.length - 1][1] + squares[squares.length\
        \ - 1][2];\n        while (high - low > 1e-5) {\n            double mid = (low\
        \ + high) / 2;\n            double areaAbove = 0, areaBelow = 0;\n         \
        \   HashSet<Integer> counted = new HashSet<>();\n            for (int[] square\
        \ : squares) {\n                if (square[1] + square[2] > mid) {\n       \
        \             double overlap = Math.max(0.0, Math.min(square[1] + square[2],\
        \ mid) - Math.max(square[1], mid));\n                    areaAbove += overlap\
        \ * square[2];\n                }\n                if (square[1] < mid) {\n\
        \                    double overlap = Math.max(0.0, Math.min(square[1] + square[2],\
        \ mid) - Math.max(square[1], mid));\n                    areaBelow += overlap\
        \ * square[2];\n                }\n            }\n            if (areaAbove\
        \ > areaBelow) high = mid;\n            else low = mid;\n        }\n       \
        \ return low;\n    }\n}"
      python: "class Solution:\n    def separateSquares(self, squares: List[List[int]])\
        \ -> float:\n        squares.sort(key=lambda x: x[1])\n        low, high = squares[0][1],\
        \ squares[-1][1] + squares[-1][2]\n        while high - low > 1e-5:\n      \
        \      mid = (low + high) / 2\n            areaAbove, areaBelow = 0, 0\n   \
        \         counted = set()\n            for square in squares:\n            \
        \    if square[1] + square[2] > mid:\n                    overlap = max(0, min(square[1]\
        \ + square[2], mid) - max(square[1], mid))\n                    areaAbove +=\
        \ overlap * square[2]\n                if square[1] < mid:\n               \
        \     overlap = max(0, min(square[1] + square[2], mid) - max(square[1], mid))\n\
        \                    areaBelow += overlap * square[2]\n            if areaAbove\
        \ > areaBelow: high = mid\n            else: low = mid\n        return low"
      python3: "class Solution:\n    def separateSquares(self, squares: List[List[int]])\
        \ -> float:\n        squares.sort(key=lambda x: x[1])\n        low, high = squares[0][1],\
        \ squares[-1][1] + squares[-1][2]\n        while high - low > 1e-5:\n      \
        \      mid = (low + high) / 2\n            areaAbove, areaBelow = 0, 0\n   \
        \         counted = set()\n            for square in squares:\n            \
        \    if square[1] + square[2] > mid:\n                    overlap = max(0, min(square[1]\
        \ + square[2], mid) - max(square[1], mid))\n                    areaAbove +=\
        \ overlap * square[2]\n                if square[1] < mid:\n               \
        \     overlap = max(0, min(square[1] + square[2], mid) - max(square[1], mid))\n\
        \                    areaBelow += overlap * square[2]\n            if areaAbove\
        \ > areaBelow: high = mid\n            else: low = mid\n        return low"
      c: "double separateSquares(int** squares, int squaresSize, int* squaresColSize)\
        \ {\n    qsort(squares, squaresSize, sizeof(int*), compare);\n    double low\
        \ = squares[0][1], high = squares[squaresSize - 1][1] + squares[squaresSize\
        \ - 1][2];\n    while (high - low > 1e-5) {\n        double mid = (low + high)\
        \ / 2;\n        double areaAbove = 0, areaBelow = 0;\n        int* counted =\
        \ (int*)malloc(squaresSize * sizeof(int));\n        for (int i = 0; i < squaresSize;\
        \ i++) {\n            if (squares[i][1] + squares[i][2] > mid) {\n         \
        \       double overlap = fmax(0.0, fmin(squares[i][1] + squares[i][2], mid)\
        \ - fmax(squares[i][1], mid));\n                areaAbove += overlap * squares[i][2];\n\
        \            }\n            if (squares[i][1] < mid) {\n                double\
        \ overlap = fmax(0.0, fmin(squares[i][1] + squares[i][2], mid) - fmax(squares[i][1],\
        \ mid));\n                areaBelow += overlap * squares[i][2];\n          \
        \  }\n        }\n        if (areaAbove > areaBelow) high = mid;\n        else\
        \ low = mid;\n    }\n    return low;\n}"
      csharp: "public class Solution {\n    public double SeparateSquares(int[][] squares)\
        \ {\n        Array.Sort(squares, (a, b) => a[1].CompareTo(b[1]));\n        double\
        \ low = squares[0][1], high = squares[squares.Length - 1][1] + squares[squares.Length\
        \ - 1][2];\n        while (high - low > 1e-5) {\n            double mid = (low\
        \ + high) / 2;\n            double areaAbove = 0, areaBelow = 0;\n         \
        \   HashSet<int> counted = new HashSet<int>();\n            for (int i = 0;\
        \ i < squares.Length; i++) {\n                if (squares[i][1] + squares[i][2]\
        \ > mid) {\n                    double overlap = Math.Max(0.0, Math.Min(squares[i][1]\
        \ + squares[i][2], mid) - Math.Max(squares[i][1], mid));\n                 \
        \   areaAbove += overlap * squares[i][2];\n                }\n             \
        \   if (squares[i][1] < mid) {\n                    double overlap = Math.Max(0.0,\
        \ Math.Min(squares[i][1] + squares[i][2], mid) - Math.Max(squares[i][1], mid));\n\
        \                    areaBelow += overlap * squares[i][2];\n               \
        \ }\n            }\n            if (areaAbove > areaBelow) high = mid;\n   \
        \         else low = mid;\n        }\n        return low;\n    }\n}"
      javascript: "var separateSquares = function(squares) {\n    squares.sort((a, b)\
        \ => a[1] - b[1]);\n    let low = squares[0][1], high = squares[squares.length\
        \ - 1][1] + squares[squares.length - 1][2];\n    while (high - low > 1e-5) {\n\
        \        let mid = (low + high) / 2;\n        let areaAbove = 0, areaBelow =\
        \ 0;\n        let counted = new Set();\n        for (let i = 0; i < squares.length;\
        \ i++) {\n            if (squares[i][1] + squares[i][2] > mid) {\n         \
        \       let overlap = Math.max(0, Math.min(squares[i][1] + squares[i][2], mid)\
        \ - Math.max(squares[i][1], mid));\n                areaAbove += overlap * squares[i][2];\n\
        \            }\n            if (squares[i][1] < mid) {\n                let\
        \ overlap = Math.max(0, Math.min(squares[i][1] + squares[i][2], mid) - Math.max(squares[i][1],\
        \ mid));\n                areaBelow += overlap * squares[i][2];\n          \
        \  }\n        }\n        if (areaAbove > areaBelow) high = mid;\n        else\
        \ low = mid;\n    }\n    return low;\n};"
      typescript: "function separateSquares(squares: number[][]): number {\n    squares.sort((a,\
        \ b) => a[1] - b[1]);\n    let low: number = squares[0][1], high: number = squares[squares.length\
        \ - 1][1] + squares[squares.length - 1][2];\n    while (high - low > 1e-5) {\n\
        \        let mid: number = (low + high) / 2;\n        let areaAbove: number\
        \ = 0, areaBelow: number = 0;\n        let counted: Set<number> = new Set();\n\
        \        for (let i: number = 0; i < squares.length; i++) {\n            if\
        \ (squares[i][1] + squares[i][2] > mid) {\n                let overlap: number\
        \ = Math.max(0, Math.min(squares[i][1] + squares[i][2], mid) - Math.max(squares[i][1],\
        \ mid));\n                areaAbove += overlap * squares[i][2];\n          \
        \  }\n            if (squares[i][1] < mid) {\n                let overlap: number\
        \ = Math.max(0, Math.min(squares[i][1] + squares[i][2], mid) - Math.max(squares[i][1],\
        \ mid));\n                areaBelow += overlap * squares[i][2];\n          \
        \  }\n        }\n        if (areaAbove > areaBelow) high = mid;\n        else\
        \ low = mid;\n    }\n    return low;\n}"
      php: "class Solution {\n    function separateSquares($squares) {\n        usort($squares,\
        \ function($a, $b) { return $a[1] - $b[1]; });\n        $low = $squares[0][1];\n\
        \        $high = $squares[count($squares) - 1][1] + $squares[count($squares)\
        \ - 1][2];\n        while ($high - $low > 1e-5) {\n            $mid = ($low\
        \ + $high) / 2;\n            $areaAbove = 0;\n            $areaBelow = 0;\n\
        \            $counted = array();\n            for ($i = 0; $i < count($squares);\
        \ $i++) {\n                if ($squares[$i][1] + $squares[$i][2] > $mid) {\n\
        \                    $overlap = max(0, min($squares[$i][1] + $squares[$i][2],\
        \ $mid) - max($squares[$i][1], $mid));\n                    $areaAbove += $overlap\
        \ * $squares[$i][2];\n                }\n                if ($squares[$i][1]\
        \ < $mid) {\n                    $overlap = max(0, min($squares[$i][1] + $squares[$i][2],\
        \ $mid) - max($squares[$i][1], $mid));\n                    $areaBelow += $overlap\
        \ * $squares[$i][2];\n                }\n            }\n            if ($areaAbove\
        \ > $areaBelow) $high = $mid;\n            else $low = $mid;\n        }\n  \
        \      return $low;\n    }\n}"
      swift: "class Solution {\n    func separateSquares(_ squares: [[Int]]) -> Double\
        \ {\n        let sortedSquares = squares.sorted { $0[1] < $1[1] }\n        var\
        \ low: Double = Double(sortedSquares[0][1])\n        var high: Double = Double(sortedSquares[sortedSquares.count\
        \ - 1][1] + sortedSquares[sortedSquares.count - 1][2])\n        while high -\
        \ low > 1e-5 {\n            let mid = (low + high) / 2\n            var areaAbove:\
        \ Double = 0\n            var areaBelow: Double = 0\n            var counted:\
        \ Set<Int> = Set()\n            for i in 0..<sortedSquares.count {\n       \
        \         if Double(sortedSquares[i][1] + sortedSquares[i][2]) > mid {\n   \
        \                 let overlap = max(0, min(Double(sortedSquares[i][1] + sortedSquares[i][2]),\
        \ mid) - max(Double(sortedSquares[i][1]), mid))\n                    areaAbove\
        \ += overlap * Double(sortedSquares[i][2])\n                }\n            \
        \    if Double(sortedSquares[i][1]) < mid {\n                    let overlap\
        \ = max(0, min(Double(sortedSquares[i][1] + sortedSquares[i][2]), mid) - max(Double(sortedSquares[i][1]),\
        \ mid))\n                    areaBelow += overlap * Double(sortedSquares[i][2])\n\
        \                }\n            }\n            if areaAbove > areaBelow {\n\
        \                high = mid\n            } else {\n                low = mid\n\
        \            }\n        }\n        return low\n    }\n}"
      kotlin: "class Solution {\n    fun separateSquares(squares: Array<IntArray>):\
        \ Double {\n        val events = mutableListOf<Triple<Double, Int, Int>>()\n\
        \        for (square in squares) {\n            val x = square[0].toDouble()\n\
        \            val y = square[1].toDouble()\n            val length = square[2].toDouble()\n\
        \            events.add(Triple(y, 1, length))\n            events.add(Triple(y\
        \ + length, -1, length))\n        }\n        events.sortBy { it.first }\n  \
        \      var areaAbove = 0.0\n        var areaBelow = 0.0\n        var y = 0.0\n\
        \        for (event in events) {\n            if (areaAbove == areaBelow) {\n\
        \                y = event.first\n            }\n            areaAbove += event.second\
        \ * event.third\n            areaBelow -= event.second * event.third\n     \
        \   }\n        return y\n    }\n}"
      dart: "class Solution {\n  double separateSquares(List<List<int>> squares) {\n\
        \    List<Triple<double, int, int>> events = [];\n    for (var square in squares)\
        \ {\n      double x = square[0].toDouble();\n      double y = square[1].toDouble();\n\
        \      double length = square[2].toDouble();\n      events.add(Triple(y, 1,\
        \ length));\n      events.add(Triple(y + length, -1, length));\n    }\n    events.sort((a,\
        \ b) => a.first.compareTo(b.first));\n    double areaAbove = 0;\n    double\
        \ areaBelow = 0;\n    double y = 0;\n    for (var event in events) {\n     \
        \ if (areaAbove == areaBelow) {\n        y = event.first;\n      }\n      areaAbove\
        \ += event.second * event.third;\n      areaBelow -= event.second * event.third;\n\
        \    }\n    return y;\n  }\n}"
      go: "func separateSquares(squares [][]int) float64 {\n    events := make([]struct{\
        \ y, delta, length float64 }, 0)\n    for _, square := range squares {\n   \
        \     x := float64(square[0])\n        y := float64(square[1])\n        length\
        \ := float64(square[2])\n        events = append(events, struct{ y, delta, length\
        \ float64 }{y, 1, length})\n        events = append(events, struct{ y, delta,\
        \ length float64 }{y + length, -1, length})\n    }\n    sort.Slice(events, func(i,\
        \ j int) bool { return events[i].y < events[j].y })\n    areaAbove := 0.0\n\
        \    areaBelow := 0.0\n    y := 0.0\n    for _, event := range events {\n  \
        \      if areaAbove == areaBelow {\n            y = event.y\n        }\n   \
        \     areaAbove += event.delta * event.length\n        areaBelow -= event.delta\
        \ * event.length\n    }\n    return y\n}"
      ruby: "def separate_squares(squares)\n    events = []\n    squares.each do |square|\n\
        \        x = square[0].to_f\n        y = square[1].to_f\n        length = square[2].to_f\n\
        \        events << [y, 1, length]\n        events << [y + length, -1, length]\n\
        \    end\n    events.sort_by! { |event| event[0] }\n    area_above = 0\n   \
        \ area_below = 0\n    y = 0\n    events.each do |event|\n        if area_above\
        \ == area_below\n            y = event[0]\n        end\n        area_above +=\
        \ event[1] * event[2]\n        area_below -= event[1] * event[2]\n    end\n\
        \    y\nend"
      scala: "object Solution {\n    def separateSquares(squares: Array[Array[Int]]):\
        \ Double = {\n        val events = scala.collection.mutable.ListBuffer[(Double,\
        \ Int, Int)]()\n        for (square <- squares) {\n            val x = square(0).toDouble\n\
        \            val y = square(1).toDouble\n            val length = square(2).toDouble\n\
        \            events += ((y, 1, length.toInt))\n            events += ((y + length,\
        \ -1, length.toInt))\n        }\n        val sortedEvents = events.sortBy(_._1)\n\
        \        var areaAbove = 0.0\n        var areaBelow = 0.0\n        var y = 0.0\n\
        \        for (event <- sortedEvents) {\n            if (areaAbove == areaBelow)\
        \ {\n                y = event._1\n            }\n            areaAbove += event._2\
        \ * event._3\n            areaBelow -= event._2 * event._3\n        }\n    \
        \    y\n    }\n}"
      rust: "impl Solution {\n    pub fn separate_squares(squares: Vec<Vec<i32>>) ->\
        \ f64 {\n        let mut events: Vec<(f64, i32, i32)> = Vec::new();\n      \
        \  for square in squares {\n            let x = square[0] as f64;\n        \
        \    let y = square[1] as f64;\n            let length = square[2] as f64;\n\
        \            events.push((y, 1, length as i32));\n            events.push((y\
        \ + length, -1, length as i32));\n        }\n        events.sort_by(|a, b| a.0.partial_cmp(&b.0).unwrap());\n\
        \        let mut area_above = 0.0;\n        let mut area_below = 0.0;\n    \
        \    let mut y = 0.0;\n        for event in events {\n            if area_above\
        \ == area_below {\n                y = event.0;\n            }\n           \
        \ area_above += event.1 as f64 * event.2 as f64;\n            area_below -=\
        \ event.1 as f64 * event.2 as f64;\n        }\n        y\n    }\n}"
      racket: "(define/contract (separate-squares squares)\n  (-> (listof (listof exact-integer?))\
        \ flonum?)\n  (let* (\n         (events (for/list (\n                      \
        \   (square squares))\n                     (let (\n                       \
        \     (x (first square))\n                            (y (second square))\n\
        \                            (length (third square)))\n                    \
        \   (list (list y 1 length)\n                             (list (+ y length)\
        \ -1 length)))))\n         (sorted-events (sort events (lambda (a b) (< (first\
        \ a) (first b)))))\n         (area-above 0)\n         (area-below 0)\n     \
        \    (y 0))\n    (for (\n         (event sorted-events))\n      (if (= area-above\
        \ area-below)\n          (set! y (first event)))\n      (set! area-above (+\
        \ area-above (* (second event) (third event))))\n      (set! area-below (- area-below\
        \ (* (second event) (third event))))))\n    y))"
      erlang: "separate_squares(Squares) ->\n    Events = [\n        begin\n       \
        \     [Y, 1, Length],\n            [Y + Length, -1, Length]\n        end\n \
        \       || [X, Y, Length] <- Squares\n    ],\n    SortedEvents = lists:sort(Events),\n\
        \    separate_squares(SortedEvents, 0, 0, 0).\n\nseparate_squares([], AreaAbove,\
        \ AreaBelow, Y) ->\n    Y;\nseparate_squares([Event | Events], AreaAbove, AreaBelow,\
        \ Y) ->\n    [Y1, Delta, Length] = Event,\n    NewAreaAbove = AreaAbove + Delta\
        \ * Length,\n    NewAreaBelow = AreaBelow - Delta * Length,\n    if\n      \
        \  AreaAbove == AreaBelow ->\n            separate_squares(Events, NewAreaAbove,\
        \ NewAreaBelow, Y1);\n        true ->\n            separate_squares(Events,\
        \ NewAreaAbove, NewAreaBelow, Y)\n    end."
      elixir: "defmodule Solution do\n  @spec separate_squares(squares :: [[integer]])\
        \ :: float\n  def separate_squares(squares) do\n    events =\n      Enum.flat_map(squares,\
        \ fn [x, y, length] ->\n        [[y, 1, length], [y + length, -1, length]]\n\
        \      end)\n      |> Enum.sort_by(&(&1 |> hd))\n    area_above = 0\n    area_below\
        \ = 0\n    y = 0\n    Enum.reduce(events, {area_above, area_below, y}, fn [y1,\
        \ delta, length], {area_above, area_below, y} ->\n      if area_above == area_below\
        \ do\n        {area_above + delta * length, area_below - delta * length, y1}\n\
        \      else\n        {area_above + delta * length, area_below - delta * length,\
        \ y}\n      end\n    end)\n    |> elem(2)\n  end\nend"
    approach: 'The problem can be solved by using a line sweep and a segment tree. The
      idea is to find the minimum y-coordinate value of a horizontal line such that
      the total area covered by squares above the line equals the total area covered
      by squares below the line. We can start by sorting the squares based on their
      y-coordinates and then iterate over the sorted squares to find the minimum y-coordinate
      value that satisfies the condition. We can use a segment tree to keep track of
      the total area covered by squares above and below the line.


      The key intuition behind this approach is that the line must lie in one of the
      squares. Therefore, we can start by finding the y-coordinate of the bottom-left
      point of each square and then iterate over the sorted y-coordinates to find the
      minimum y-coordinate value that satisfies the condition. We can use a binary search
      approach to find the minimum y-coordinate value in O(log n) time complexity, where
      n is the number of squares. This approach ensures that we find the minimum y-coordinate
      value that satisfies the condition in an efficient manner.'
    time_complexity: The time complexity of the solution is O(n log n) due to the sorting
      of the squares based on their y-coordinates. The iteration over the sorted squares
      and the binary search approach take O(n log n) time complexity. The space complexity
      is O(n) due to the use of a segment tree to keep track of the total area covered
      by squares above and below the line.
    space_complexity: The space complexity of the solution is O(n) due to the use of
      a segment tree to keep track of the total area covered by squares above and below
      the line. The segment tree requires O(n) space to store the total area covered
      by squares above and below the line. The sorting of the squares based on their
      y-coordinates also requires O(n) space. Therefore, the overall space complexity
      of the solution is O(n).
    elapsed_time: 12.167769193649292
    model: llama-3.3-70b-versatile
    generated_at: '2026-01-14 01:18:14 '
---

## Problem #3454: Separate Squares II

**Difficulty:** Hard

**Topics:** Array, Binary Search, Segment Tree, Line Sweep

## Problem Description

<p>You are given a 2D integer array <code>squares</code>. Each <code>squares[i] = [x<sub>i</sub>, y<sub>i</sub>, l<sub>i</sub>]</code> represents the coordinates of the bottom-left point and the side length of a square parallel to the x-axis.</p>

<p>Find the <strong>minimum</strong> y-coordinate value of a horizontal line such that the total area covered by squares above the line <em>equals</em> the total area covered by squares below the line.</p>

<p>Answers within <code>10<sup>-5</sup></code> of the actual answer will be accepted.</p>

<p><strong>Note</strong>: Squares <strong>may</strong> overlap. Overlapping areas should be counted <strong>only once</strong> in this version.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">squares = [[0,0,1],[2,2,1]]</span></p>

<p><strong>Output:</strong> <span class="example-io">1.00000</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2025/01/15/4065example1drawio.png" style="width: 269px; height: 203px;" /></p>

<p>Any horizontal line between <code>y = 1</code> and <code>y = 2</code> results in an equal split, with 1 square unit above and 1 square unit below. The minimum y-value is 1.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">squares = [[0,0,2],[1,1,1]]</span></p>

<p><strong>Output:</strong> <span class="example-io">1.00000</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2025/01/15/4065example2drawio.png" style="width: 269px; height: 203px;" /></p>

<p>Since the blue square overlaps with the red square, it will not be counted again. Thus, the line <code>y = 1</code> splits the squares into two equal parts.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= squares.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>squares[i] = [x<sub>i</sub>, y<sub>i</sub>, l<sub>i</sub>]</code></li>
	<li><code>squares[i].length == 3</code></li>
	<li><code>0 &lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= l<sub>i</sub> &lt;= 10<sup>9</sup></code></li>
	<li>The total area of all the squares will not exceed <code>10<sup>15</sup></code>.</li>
</ul>


## Hints

1. Use a line sweep and a segment tree.

2. The line must lie in one of the squares.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2026-01-14 01:17:57 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem requires finding a horizontal line `y` that divides the total unique area covered by a set of overlapping squares into two equal halves. This can be framed as finding a `y` such that the unique area below the line `y` is exactly half of the total unique area. Since the unique area below a line `y` is a monotonically increasing function of `y`, binary search is an appropriate technique to find this specific `y` value.

To implement the binary search, we need a function `calculate_unique_area(rectangles)` that computes the total unique area covered by a given set of rectangles. This function is implemented using a standard line sweep algorithm combined with a segment tree. Events are created for the left and right vertical edges of each rectangle, storing `(x, type, y_bottom, y_top)`. All unique y-coordinates from these rectangles are collected, sorted, and used to build a segment tree. The segment tree maintains the total length of the union of active y-intervals at the current x-coordinate. As the sweep line moves from left to right, the area of each vertical strip `(current_x - prev_x) * active_length` is accumulated. The binary search iteratively refines the `y` coordinate. In each iteration, `mid = (low + high) / 2.0` is chosen. A new set of 'clipped' rectangles is generated, representing the portions of original squares that lie below `mid`. The `calculate_unique_area` function is then called on these clipped rectangles. If the area below `mid` is greater than or equal to half of the total unique area, `mid` is a potential answer, and we try a smaller `y` by setting `high = mid`. Otherwise, `mid` is too low, and we set `low = mid`. This process is repeated for a fixed number of iterations (e.g., 100) to achieve the required precision.

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
    // SegmentTree class definition
    struct SegmentTree {
        vector<pair<long long, double>> tree; // {count, length}
        const vector<double>& y_coords;
        int N_intervals;

        SegmentTree(const vector<double>& y_coords_ref) : y_coords(y_coords_ref) {
            N_intervals = y_coords.empty() ? 0 : y_coords.size() - 1;
            tree.resize(4 * max(1, N_intervals), {0, 0.0});
        }

        void _update(int node_idx, int start_idx, int end_idx, int query_y1_idx, int query_y2_idx, int val) {
            if (start_idx >= query_y2_idx || end_idx <= query_y1_idx) {
                return;
            }

            if (query_y1_idx <= start_idx && end_idx <= query_y2_idx) {
                tree[node_idx].first += val;
            } else {
                int mid_idx = start_idx + (end_idx - start_idx) / 2;
                _update(2 * node_idx, start_idx, mid_idx, query_y1_idx, query_y2_idx, val);
                _update(2 * node_idx + 1, mid_idx, end_idx, query_y1_idx, query_y2_idx, val);
            }

            if (tree[node_idx].first > 0) {
                tree[node_idx].second = y_coords[end_idx] - y_coords[start_idx];
            } else {
                if (start_idx + 1 == end_idx) { // Leaf node
                    tree[node_idx].second = 0.0;
                } else {
                    tree[node_idx].second = tree[2 * node_idx].second + tree[2 * node_idx + 1].second;
                }
            }
        }

        void update(double y1, double y2, int val) {
            if (N_intervals == 0) return;
            auto it1 = lower_bound(y_coords.begin(), y_coords.end(), y1);
            auto it2 = lower_bound(y_coords.begin(), y_coords.end(), y2);
            int y1_idx = distance(y_coords.begin(), it1);
            int y2_idx = distance(y_coords.begin(), it2);

            if (y1_idx >= y2_idx) {
                return;
            }
            _update(1, 0, N_intervals, y1_idx, y2_idx, val);
        }

        double get_total_length() {
            if (N_intervals == 0) return 0.0;
            return tree[1].second;
        }
    };

    // Rectangle class to hold (x, y, width, height) with double height
    struct Rect {
        long long x;
        double y;
        long long width;
        double height;
    };

    // Event class for line sweep
    struct Event {
        long long x;
        int type; // 1 for left edge, -1 for right edge
        double y1, y2;

        bool operator<(const Event& other) const {
            if (x != other.x) {
                return x < other.x;
            }
            return type < other.type; // Process left edges before right edges at same x
        }
    };

    double calculate_unique_area(const vector<Rect>& rects) {
        if (rects.empty()) {
            return 0.0;
        }

        vector<Event> events;
        set<double> y_coords_set;
        for (const auto& rect : rects) {
            events.push_back({rect.x, 1, rect.y, rect.y + rect.height});
            events.push_back({rect.x + rect.width, -1, rect.y, rect.y + rect.height});
            y_coords_set.insert(rect.y);
            y_coords_set.insert(rect.y + rect.height);
        }
        sort(events.begin(), events.end());

        vector<double> y_coords(y_coords_set.begin(), y_coords_set.end());

        if (y_coords.size() <= 1) {
            return 0.0;
        }

        SegmentTree st(y_coords);
        double total_area = 0.0;
        long long prev_x = events[0].x;

        for (const auto& event : events) {
            double current_length = st.get_total_length();
            total_area += current_length * (event.x - prev_x);
            st.update(event.y1, event.y2, event.type);
            prev_x = event.x;
        }
        return total_area;
    }

    double separateSquares(vector<vector<int>>& squares) {
        vector<Rect> original_rects;
        double min_y_overall = 2e9 + 7; // Use a large double value
        double max_y_overall = -1.0;

        for (const auto& s : squares) {
            long long x = s[0];
            double y = s[1];
            long long l = s[2];
            original_rects.push_back({x, y, l, l});
            min_y_overall = min(min_y_overall, y);
            max_y_overall = max(max_y_overall, y + l);
        }

        double total_unique_area = calculate_unique_area(original_rects);
        double target_area_below = total_unique_area / 2.0;

        double low = min_y_overall;
        double high = max_y_overall;
        double ans = high;

        for (int i = 0; i < 100; ++i) {
            double mid = low + (high - low) / 2.0;

            vector<Rect> clipped_rects_below;
            for (const auto& s : squares) {
                long long x = s[0];
                double y_bottom = s[1];
                long long l = s[2];
                double y_top = y_bottom + l;

                if (y_bottom < mid) {
                    double clipped_y_top = min(y_top, mid);
                    double clipped_height = clipped_y_top - y_bottom;
                    if (clipped_height > 0) {
                        clipped_rects_below.push_back({x, y_bottom, l, clipped_height});
                    }
                }
            }

            double area_below_mid = calculate_unique_area(clipped_rects_below);

            if (area_below_mid >= target_area_below) {
                ans = mid;
                high = mid;
            } else {
                low = mid;
            }
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
import java.util.*;

class Solution {
    // SegmentTree class definition
    static class SegmentTree {
        private static class Node {
            long count; // Number of active rectangles covering this interval
            double length; // Total length of the union of active intervals within this node's range

            Node() {
                this.count = 0;
                this.length = 0.0;
            }
        }

        private Node[] tree;
        private final List<Double> yCoords;
        private int N_intervals;

        public SegmentTree(List<Double> yCoordsRef) {
            this.yCoords = yCoordsRef;
            this.N_intervals = yCoords.isEmpty() ? 0 : yCoords.size() - 1;
            tree = new Node[4 * Math.max(1, N_intervals)];
            for (int i = 0; i < tree.length; i++) {
                tree[i] = new Node();
            }
        }

        private void _update(int nodeIdx, int startIdx, int endIdx, int queryY1Idx, int queryY2Idx, int val) {
            if (startIdx >= queryY2Idx || endIdx <= queryY1Idx) {
                return;
            }

            if (queryY1Idx <= startIdx && endIdx <= queryY2Idx) {
                tree[nodeIdx].count += val;
            } else {
                int midIdx = startIdx + (endIdx - startIdx) / 2;
                _update(2 * nodeIdx, startIdx, midIdx, queryY1Idx, queryY2Idx, val);
                _update(2 * nodeIdx + 1, midIdx, endIdx, queryY1Idx, queryY2Idx, val);
            }

            if (tree[nodeIdx].count > 0) {
                tree[nodeIdx].length = yCoords.get(endIdx) - yCoords.get(startIdx);
            } else {
                if (startIdx + 1 == endIdx) { // Leaf node
                    tree[nodeIdx].length = 0.0;
                } else {
                    tree[nodeIdx].length = tree[2 * nodeIdx].length + tree[2 * nodeIdx + 1].length;
                }
            }
        }

        public void update(double y1, double y2, int val) {
            if (N_intervals == 0) return;
            int y1Idx = Collections.binarySearch(yCoords, y1);
            if (y1Idx < 0) y1Idx = -y1Idx - 1;
            int y2Idx = Collections.binarySearch(yCoords, y2);
            if (y2Idx < 0) y2Idx = -y2Idx - 1;

            if (y1Idx >= y2Idx) {
                return;
            }
            _update(1, 0, N_intervals, y1Idx, y2Idx, val);
        }

        public double getTotalLength() {
            if (N_intervals == 0) return 0.0;
            return tree[1].length;
        }
    }

    // Rectangle class to hold (x, y, width, height) with double height
    static class Rect {
        long x;
        double y;
        long width;
        double height;

        Rect(long x, double y, long width, double height) {
            this.x = x;
            this.y = y;
            this.width = width;
            this.height = height;
        }
    }

    // Event class for line sweep
    static class Event implements Comparable<Event> {
        long x;
        int type; // 1 for left edge, -1 for right edge
        double y1, y2;

        Event(long x, int type, double y1, double y2) {
            this.x = x;
            this.type = type;
            this.y1 = y1;
            this.y2 = y2;
        }

        @Override
        public int compareTo(Event other) {
            if (this.x != other.x) {
                return Long.compare(this.x, other.x);
            }
            return Integer.compare(this.type, other.type); // Process left edges before right edges at same x
        }
    }

    private double calculateUniqueArea(List<Rect> rects) {
        if (rects.isEmpty()) {
            return 0.0;
        }

        List<Event> events = new ArrayList<>();
        Set<Double> yCoordsSet = new TreeSet<>(); // Use TreeSet to keep sorted and unique
        for (Rect rect : rects) {
            events.add(new Event(rect.x, 1, rect.y, rect.y + rect.height));
            events.add(new Event(rect.x + rect.width, -1, rect.y, rect.y + rect.height));
            yCoordsSet.add(rect.y);
            yCoordsSet.add(rect.y + rect.height);
        }
        Collections.sort(events);

        List<Double> yCoords = new ArrayList<>(yCoordsSet);

        if (yCoords.size() <= 1) {
            return 0.0;
        }

        SegmentTree st = new SegmentTree(yCoords);
        double totalArea = 0.0;
        long prevX = events.get(0).x;

        for (Event event : events) {
            double currentLength = st.getTotalLength();
            totalArea += currentLength * (event.x - prevX);
            st.update(event.y1, event.y2, event.type);
            prevX = event.x;
        }
        return totalArea;
    }

    public double separateSquares(int[][] squares) {
        List<Rect> originalRects = new ArrayList<>();
        double minYOverall = Double.POSITIVE_INFINITY;
        double maxYOverall = Double.NEGATIVE_INFINITY;

        for (int[] s : squares) {
            long x = s[0];
            double y = s[1];
            long l = s[2];
            originalRects.add(new Rect(x, y, l, l));
            minYOverall = Math.min(minYOverall, y);
            maxYOverall = Math.max(maxYOverall, y + l);
        }

        double totalUniqueArea = calculateUniqueArea(originalRects);
        double targetAreaBelow = totalUniqueArea / 2.0;

        double low = minYOverall;
        double high = maxYOverall;
        double ans = high;

        for (int i = 0; i < 100; ++i) {
            double mid = low + (high - low) / 2.0;

            List<Rect> clippedRectsBelow = new ArrayList<>();
            for (int[] s : squares) {
                long x = s[0];
                double yBottom = s[1];
                long l = s[2];
                double yTop = yBottom + l;

                if (yBottom < mid) {
                    double clippedYTop = Math.min(yTop, mid);
                    double clippedHeight = clippedYTop - yBottom;
                    if (clippedHeight > 0) {
                        clippedRectsBelow.add(new Rect(x, yBottom, l, clippedHeight));
                    }
                }
            }

            double areaBelowMid = calculateUniqueArea(clippedRectsBelow);

            if (areaBelowMid >= targetAreaBelow) {
                ans = mid;
                high = mid;
            } else {
                low = mid;
            }
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
from bisect import bisect_left

class SegmentTree(object):
    def __init__(self, y_coords):
        self.y_coords = y_coords
        self.N = len(y_coords) - 1
        if self.N < 0:
            self.N = 0
        self.tree = [[0, 0.0] for _ in range(4 * max(1, self.N))] # [count, length]

    def _update(self, node_idx, start_idx, end_idx, query_y1_idx, query_y2_idx, val):
        if start_idx >= query_y2_idx or end_idx <= query_y1_idx:
            return

        if query_y1_idx <= start_idx and end_idx <= query_y2_idx:
            self.tree[node_idx][0] += val
        else:
            mid_idx = (start_idx + end_idx) // 2
            self._update(2 * node_idx, start_idx, mid_idx, query_y1_idx, query_y2_idx, val)
            self._update(2 * node_idx + 1, mid_idx, end_idx, query_y1_idx, query_y2_idx, val)

        if self.tree[node_idx][0] > 0:
            self.tree[node_idx][1] = float(self.y_coords[end_idx] - self.y_coords[start_idx])
        else:
            if start_idx + 1 == end_idx:
                self.tree[node_idx][1] = 0.0
            else:
                self.tree[node_idx][1] = self.tree[2 * node_idx][1] + self.tree[2 * node_idx + 1][1]

    def update(self, y1, y2, val):
        if self.N == 0:
            return
        y1_idx = bisect_left(self.y_coords, y1)
        y2_idx = bisect_left(self.y_coords, y2)

        if y1_idx >= y2_idx:
            return

        self._update(1, 0, self.N, y1_idx, y2_idx, val);

    def get_total_length(self):
        if self.N == 0:
            return 0.0
        return self.tree[1][1]

class Solution(object):
    def separateSquares(self, squares):
        """
        :type squares: List[List[int]]
        :rtype: float
        """

        def calculate_unique_area(rects):
            if not rects:
                return 0.0

            events = []
            y_coords_set = set()
            for x, y, w, h in rects:
                events.append((x, 1, y, y + h))
                events.append((x + w, -1, y, y + h))
                y_coords_set.add(y)
                y_coords_set.add(y + h)

            events.sort()
            y_coords = sorted(list(y_coords_set))

            if len(y_coords) <= 1: 
                return 0.0

            st = SegmentTree(y_coords)
            total_area = 0.0
            prev_x = events[0][0]

            for x, type, y1, y2 in events:
                current_length = st.get_total_length()
                total_area += current_length * (x - prev_x)
                st.update(y1, y2, type)
                prev_x = x

            return total_area

        original_rects = []
        min_y_overall = float('inf')
        max_y_overall = float('-inf')
        for x, y, l in squares:
            original_rects.append((x, float(y), float(l), float(l))) # (x, y, width, height)
            min_y_overall = min(min_y_overall, float(y))
            max_y_overall = max(max_y_overall, float(y + l))

        total_unique_area = calculate_unique_area(original_rects)

        target_area_below = total_unique_area / 2.0

        low = float(min_y_overall)
        high = float(max_y_overall)
        ans = high 

        for _ in range(100): 
            mid = low + (high - low) / 2.0

            clipped_rects_below = []
            for x, y, l in squares:
                y_bottom = float(y)
                y_top = float(y + l)

                if y_bottom < mid: 
                    clipped_y_top = min(y_top, mid)
                    clipped_height = clipped_y_top - y_bottom
                    if clipped_height > 0: # Ensure positive height
                        clipped_rects_below.append((x, y_bottom, float(l), clipped_height))

            area_below_mid = calculate_unique_area(clipped_rects_below);

            if area_below_mid >= target_area_below:
                ans = mid;
                high = mid;
            else:
                low = mid;

        return ans;
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
from bisect import bisect_left

class SegmentTree:
    def __init__(self, y_coords: List[float]):
        self.y_coords = y_coords
        self.N = len(y_coords) - 1
        if self.N < 0:
            self.N = 0
        self.tree = [[0, 0.0] for _ in range(4 * max(1, self.N))] # [count, length]

    def _update(self, node_idx: int, start_idx: int, end_idx: int, query_y1_idx: int, query_y2_idx: int, val: int):
        if start_idx >= query_y2_idx or end_idx <= query_y1_idx:
            return

        if query_y1_idx <= start_idx and end_idx <= query_y2_idx:
            self.tree[node_idx][0] += val
        else:
            mid_idx = (start_idx + end_idx) // 2
            self._update(2 * node_idx, start_idx, mid_idx, query_y1_idx, query_y2_idx, val)
            self._update(2 * node_idx + 1, mid_idx, end_idx, query_y1_idx, query_y2_idx, val)

        if self.tree[node_idx][0] > 0:
            self.tree[node_idx][1] = float(self.y_coords[end_idx] - self.y_coords[start_idx])
        else:
            if start_idx + 1 == end_idx:
                self.tree[node_idx][1] = 0.0
            else:
                self.tree[node_idx][1] = self.tree[2 * node_idx][1] + self.tree[2 * node_idx + 1][1]

    def update(self, y1: float, y2: float, val: int):
        if self.N == 0:
            return
        y1_idx = bisect_left(self.y_coords, y1)
        y2_idx = bisect_left(self.y_coords, y2)

        if y1_idx >= y2_idx:
            return

        self._update(1, 0, self.N, y1_idx, y2_idx, val)

    def get_total_length(self) -> float:
        if self.N == 0:
            return 0.0
        return self.tree[1][1]

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:

        def calculate_unique_area(rects: List[Tuple[int, float, float, float]]) -> float:
            if not rects:
                return 0.0

            events = [] # (x, type, y1, y2)
            y_coords_set = set()
            for x, y, w, h in rects:
                events.append((x, 1, y, y + h))
                events.append((x + w, -1, y, y + h))
                y_coords_set.add(y)
                y_coords_set.add(y + h)

            events.sort()
            y_coords = sorted(list(y_coords_set))

            if len(y_coords) <= 1: 
                return 0.0

            st = SegmentTree(y_coords)
            total_area = 0.0
            prev_x = events[0][0]

            for x, type, y1, y2 in events:
                current_length = st.get_total_length()
                total_area += current_length * (x - prev_x)
                st.update(y1, y2, type)
                prev_x = x

            return total_area

        original_rects = [] # (x, y, width, height)
        min_y_overall = float('inf')
        max_y_overall = float('-inf')
        for x, y, l in squares:
            original_rects.append((x, float(y), float(l), float(l))) # Store y, w, h as float for consistency
            min_y_overall = min(min_y_overall, float(y))
            max_y_overall = max(max_y_overall, float(y + l))

        total_unique_area = calculate_unique_area(original_rects)

        target_area_below = total_unique_area / 2.0

        low = float(min_y_overall)
        high = float(max_y_overall)
        ans = high 

        for _ in range(100): 
            mid = low + (high - low) / 2.0

            clipped_rects_below = []
            for x, y, l in squares:
                y_bottom = float(y)
                y_top = float(y + l)

                if y_bottom < mid: 
                    clipped_y_top = min(y_top, mid)
                    clipped_height = clipped_y_top - y_bottom
                    if clipped_height > 0: 
                        clipped_rects_below.append((x, y_bottom, float(l), clipped_height))

            area_below_mid = calculate_unique_area(clipped_rects_below)

            if area_below_mid >= target_area_below:
                ans = mid
                high = mid
            else:
                low = mid

        return ans
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <string.h>

// Define a structure for Segment Tree nodes
typedef struct {
    long long count;
    double length;
} SegmentTreeNode;

// Global variables for Segment Tree to avoid passing them around too much
// In a real C solution, these would be part of a struct or passed explicitly.
static SegmentTreeNode* tree_nodes;
static double* y_coords_arr;
static int N_intervals_st;

// Helper for qsort to sort doubles
static int compare_doubles(const void* a, const void* b) {
    double val_a = *(const double*)a;
    double val_b = *(const double*)b;
    if (val_a < val_b) return -1;
    if (val_a > val_b) return 1;
    return 0;
}

// Binary search for lower_bound equivalent
static int lower_bound_idx(double val, int size) {
    int low = 0, high = size - 1, ans = size;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (y_coords_arr[mid] >= val) {
            ans = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }
    return ans;
}

static void _update_segment_tree(int node_idx, int start_idx, int end_idx, int query_y1_idx, int query_y2_idx, int val) {
    if (start_idx >= query_y2_idx || end_idx <= query_y1_idx) {
        return;
    }

    if (query_y1_idx <= start_idx && end_idx <= query_y2_idx) {
        tree_nodes[node_idx].count += val;
    } else {
        int mid_idx = start_idx + (end_idx - start_idx) / 2;
        _update_segment_tree(2 * node_idx, start_idx, mid_idx, query_y1_idx, query_y2_idx, val);
        _update_segment_tree(2 * node_idx + 1, mid_idx, end_idx, query_y1_idx, query_y2_idx, val);
    }

    if (tree_nodes[node_idx].count > 0) {
        tree_nodes[node_idx].length = y_coords_arr[end_idx] - y_coords_arr[start_idx];
    } else {
        if (start_idx + 1 == end_idx) {
            tree_nodes[node_idx].length = 0.0;
        } else {
            tree_nodes[node_idx].length = tree_nodes[2 * node_idx].length + tree_nodes[2 * node_idx + 1].length;
        }
    }
}

static void update_segment_tree(double y1, double y2, int val) {
    if (N_intervals_st == 0) return;
    int y1_idx = lower_bound_idx(y1, N_intervals_st + 1);
    int y2_idx = lower_bound_idx(y2, N_intervals_st + 1);

    if (y1_idx >= y2_idx) {
        return;
    }
    _update_segment_tree(1, 0, N_intervals_st, y1_idx, y2_idx, val);
}

static double get_total_length_segment_tree() {
    if (N_intervals_st == 0) return 0.0;
    return tree_nodes[1].length;
}

// Rectangle structure for calculate_unique_area
typedef struct {
    long long x;
    double y;
    long long width;
    double height;
} Rect;

// Event structure for line sweep
typedef struct {
    long long x;
    int type; // 1 for left edge, -1 for right edge
    double y1, y2;
} Event;

// Comparator for events (sort by x, then type)
static int compare_events(const void* a, const void* b) {
    Event* event_a = (Event*)a;
    Event* event_b = (Event*)b;
    if (event_a->x != event_b->x) {
        return (event_a->x < event_b->x) ? -1 : 1;
    }
    return event_a->type - event_b->type;
}

static double calculate_unique_area(Rect* rects, int num_rects) {
    if (num_rects == 0) {
        return 0.0;
    }

    Event* events = (Event*)malloc(sizeof(Event) * num_rects * 2);
    double* y_coords_raw = (double*)malloc(sizeof(double) * num_rects * 2);
    int event_count = 0;
    int y_coord_count = 0;

    for (int i = 0; i < num_rects; ++i) {
        events[event_count++] = (Event){rects[i].x, 1, rects[i].y, rects[i].y + rects[i].height};
        events[event_count++] = (Event){rects[i].x + rects[i].width, -1, rects[i].y, rects[i].y + rects[i].height};
        y_coords_raw[y_coord_count++] = rects[i].y;
        y_coords_raw[y_coord_count++] = rects[i].y + rects[i].height;
    }
    qsort(events, event_count, sizeof(Event), compare_events);

    qsort(y_coords_raw, y_coord_count, sizeof(double), compare_doubles);

    // Remove duplicates from y_coords_raw
    int unique_y_count = 0;
    if (y_coord_count > 0) {
        y_coords_raw[unique_y_count++] = y_coords_raw[0];
        for (int i = 1; i < y_coord_count; ++i) {
            if (y_coords_raw[i] != y_coords_raw[i-1]) {
                y_coords_raw[unique_y_count++] = y_coords_raw[i];
            }
        }
    }

    if (unique_y_count <= 1) {
        free(events);
        free(y_coords_raw);
        return 0.0;
    }

    y_coords_arr = y_coords_raw; // Set global pointer
    N_intervals_st = unique_y_count - 1;
    tree_nodes = (SegmentTreeNode*)calloc(4 * (N_intervals_st + 1), sizeof(SegmentTreeNode)); // +1 for max(1, N_intervals)

    double total_area = 0.0;
    long long prev_x = events[0].x;

    for (int i = 0; i < event_count; ++i) {
        double current_length = get_total_length_segment_tree();
        total_area += current_length * (events[i].x - prev_x);
        update_segment_tree(events[i].y1, events[i].y2, events[i].type);
        prev_x = events[i].x;
    }

    free(events);
    free(y_coords_raw);
    free(tree_nodes);
    return total_area;
}

double separateSquares(int** squares, int squaresSize, int* squaresColSize) {
    Rect* original_rects = (Rect*)malloc(sizeof(Rect) * squaresSize);
    double min_y_overall = 2e18; // Use a large double value
    double max_y_overall = -1.0;

    for (int i = 0; i < squaresSize; ++i) {
        long long x = squares[i][0];
        double y = squares[i][1];
        long long l = squares[i][2];
        original_rects[i] = (Rect){x, y, l, l};
        min_y_overall = fmin(min_y_overall, y);
        max_y_overall = fmax(max_y_overall, y + l);
    }

    double total_unique_area = calculate_unique_area(original_rects, squaresSize);
    double target_area_below = total_unique_area / 2.0;

    double low = min_y_overall;
    double high = max_y_overall;
    double ans = high;

    for (int i = 0; i < 100; ++i) {
        double mid = low + (high - low) / 2.0;

        Rect* clipped_rects_below = (Rect*)malloc(sizeof(Rect) * squaresSize);
        int clipped_count = 0;

        for (int j = 0; j < squaresSize; ++j) {
            long long x = squares[j][0];
            double y_bottom = squares[j][1];
            long long l = squares[j][2];
            double y_top = y_bottom + l;

            if (y_bottom < mid) {
                double clipped_y_top = fmin(y_top, mid);
                double clipped_height = clipped_y_top - y_bottom;
                if (clipped_height > 0) {
                    clipped_rects_below[clipped_count++] = (Rect){x, y_bottom, l, clipped_height};
                }
            }
        }

        double area_below_mid = calculate_unique_area(clipped_rects_below, clipped_count);
        free(clipped_rects_below);

        if (area_below_mid >= target_area_below) {
            ans = mid;
            high = mid;
        } else {
            low = mid;
        }
    }
    free(original_rects);
    return ans;
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

public class Solution {
// SegmentTree class definition
private class SegmentTree {
private class Node {
    public long Count { get; set; }
    public double Length { get; set; }

    public Node() {
        Count = 0;
        Length = 0.0;
    }
}

private Node[] tree;
private readonly List<double> yCoords;
private int N_intervals;

public SegmentTree(List<double> yCoordsRef) {
    this.yCoords = yCoordsRef;
    this.N_intervals = yCoords.Count == 0 ? 0 : yCoords.Count - 1;
    tree = new Node[4 * Math.Max(1, N_intervals)];
    for (int i = 0; i < tree.Length; i++) {
        tree[i] = new Node();
    }
}

private void _update(int nodeIdx, int startIdx, int endIdx, int queryY1Idx, int queryY2Idx, int val) {
    if (startIdx >= queryY2Idx || endIdx <= queryY1Idx) {
        return;
    }

    if (queryY1Idx <= startIdx && endIdx <= queryY2Idx) {
        tree[nodeIdx].Count += val;
    } else {
        int midIdx = startIdx + (endIdx - startIdx) / 2;
        _update(2 * nodeIdx, startIdx, midIdx, queryY1Idx, queryY2Idx, val);
        _update(2 * nodeIdx + 1, midIdx, endIdx, queryY1Idx, queryY2Idx, val);
    }

    if (tree[nodeIdx].Count > 0) {
        tree[nodeIdx].Length = yCoords[endIdx] - yCoords[startIdx];
    } else {
        if (startIdx + 1 == endIdx) { // Leaf node
            tree[nodeIdx].Length = 0.0;
        } else {
            tree[nodeIdx].Length = tree[2 * nodeIdx].Length + tree[2 * nodeIdx + 1].Length;
        }
    }
}

public void Update(double y1, double y2, int val) {
    if (N_intervals == 0) return;
    int y1Idx = yCoords.BinarySearch(y1);
    if (y1Idx < 0) y1Idx = ~y1Idx;
    int y2Idx = yCoords.BinarySearch(y2);
    if (y2Idx < 0) y2Idx = ~y2Idx;

    if (y1Idx >= y2Idx) {
        return;
    }
    _update(1, 0, N_intervals, y1Idx, y2Idx, val);
}

public double GetTotalLength() {
    if (N_intervals == 0) return 0.0;
    return tree[1].Length;
}
}

// Rectangle class to hold (x, y, width, height) with double height
private class Rect {
public long X { get; set; }
public double Y { get; set; }
public long Width { get; set; }
public double Height { get; set; }

public Rect(long x, double y, long width, double height) {
    this.X = x;
    this.Y = y;
    this.Width = width;
    this.Height = height;
}
}

// Event class for line sweep
private class Event : IComparable<Event> {
public long X { get; set; }
public int Type { get; set; } // 1 for left edge, -1 for right edge
public double Y1 { get; set; }
public double Y2 { get; set; }

public Event(long x, int type, double y1, double y2) {
    this.X = x;
    this.Type = type;
    this.Y1 = y1;
    this.Y2 = y2;
}

public int CompareTo(Event other) {
    if (this.X != other.X) {
        return this.X.CompareTo(other.X);
    }
    return this.Type.CompareTo(other.Type); // Process left edges before right edges at same x
}
}

private double CalculateUniqueArea(List<Rect> rects) {
if (rects.Count == 0) {
    return 0.0;
}

List<Event> events = new List<Event>();
SortedSet<double> yCoordsSet = new SortedSet<double>(); // Use SortedSet to keep sorted and unique
foreach (Rect rect in rects) {
    events.Add(new Event(rect.X, 1, rect.Y, rect.Y + rect.Height));
    events.Add(new Event(rect.X + rect.Width, -1, rect.Y, rect.Y + rect.Height));
    yCoordsSet.Add(rect.Y);
    yCoordsSet.Add(rect.Y + rect.Height);
}
events.Sort();

List<double> yCoords = yCoordsSet.ToList();

if (yCoords.Count <= 1) {
    return 0.0;
}

SegmentTree st = new SegmentTree(yCoords);
double totalArea = 0.0;
long prevX = events[0].X;

foreach (Event eventItem in events) {
    double currentLength = st.GetTotalLength();
    totalArea += currentLength * (eventItem.X - prevX);
    st.Update(eventItem.Y1, eventItem.Y2, eventItem.Type);
    prevX = eventItem.X;
}
return totalArea;
}

public double SeparateSquares(int[][] squares) {
List<Rect> originalRects = new List<Rect>();
double minYOverall = double.PositiveInfinity;
double maxYOverall = double.NegativeInfinity;

for (int[] s : squares) {
    long x = s[0];
    double y = s[1];
    long l = s[2];
    originalRects.Add(new Rect(x, y, l, l));
    minYOverall = Math.Min(minYOverall, y);
    maxYOverall = Math.Max(maxYOverall, y + l);
}

double totalUniqueArea = CalculateUniqueArea(originalRects);
double targetAreaBelow = totalUniqueArea / 2.0;

double low = minYOverall;
double high = maxYOverall;
double ans = high;

for (int i = 0; i < 100; ++i) {
    double mid = low + (high - low) / 2.0;

    List<Rect> clippedRectsBelow = new List<Rect>();
    for (int[] s : squares) {
        long x = s[0];
        double yBottom = s[1];
        long l = s[2];
        double yTop = yBottom + l;

        if (yBottom < mid) {
            double clippedYTop = Math.Min(yTop, mid);
            double clippedHeight = clippedYTop - yBottom;
            if (clippedHeight > 0) {
                clippedRectsBelow.Add(new Rect(x, yBottom, l, clippedHeight));
            }
        }
    }

    double areaBelowMid = CalculateUniqueArea(clippedRectsBelow);

    if (areaBelowMid >= targetAreaBelow) {
        ans = mid;
        high = mid;
    } else {
        low = mid;
    }
}
return ans;
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

class SegmentTree {
    constructor(yCoords) {
        this.yCoords = yCoords;
        this.N = yCoords.length - 1;
        if (this.N < 0) this.N = 0;
        this.tree = Array(4 * Math.max(1, this.N)).fill(null).map(() => [0, 0.0]); // [count, length]
    }

    _update(nodeIdx, startIdx, endIdx, queryY1Idx, queryY2Idx, val) {
        if (startIdx >= queryY2Idx || endIdx <= queryY1Idx) {
            return;
        }

        if (queryY1Idx <= startIdx && endIdx <= queryY2Idx) {
            this.tree[nodeIdx][0] += val;
        } else {
            const midIdx = Math.floor((startIdx + endIdx) / 2);
            this._update(2 * nodeIdx, startIdx, midIdx, queryY1Idx, queryY2Idx, val);
            this._update(2 * nodeIdx + 1, midIdx, endIdx, queryY1Idx, queryY2Idx, val);
        }

        if (this.tree[nodeIdx][0] > 0) {
            this.tree[nodeIdx][1] = this.yCoords[endIdx] - this.yCoords[startIdx];
        } else {
            if (startIdx + 1 === endIdx) {
                this.tree[nodeIdx][1] = 0.0;
            } else {
                this.tree[nodeIdx][1] = this.tree[2 * nodeIdx][1] + this.tree[2 * nodeIdx + 1][1];
            }
        }
    }

    update(y1, y2, val) {
        if (this.N === 0) return;
        const y1Idx = this.binarySearch(this.yCoords, y1);
        const y2Idx = this.binarySearch(this.yCoords, y2);

        if (y1Idx >= y2Idx) {
            return;
        }

        this._update(1, 0, this.N, y1Idx, y2Idx, val);
    }

    get_total_length() {
        if (this.N === 0) return 0.0;
        return this.tree[1][1];
    }

    // Custom binary search for lower_bound
    binarySearch(arr, target) {
        let low = 0;
        let high = arr.length - 1;
        let ans = arr.length;
        while (low <= high) {
            const mid = Math.floor((low + high) / 2);
            if (arr[mid] >= target) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return ans;
    }
}

var separateSquares = function(squares) {

    const calculateUniqueArea = (rects) => {
        if (rects.length === 0) {
            return 0.0;
        }

        const events = []; // (x, type, y1, y2)
        const yCoordsSet = new Set();
        for (const rect of rects) {
            const [x, y, w, h] = rect;
            events.push([x, 1, y, y + h]);
            events.push([x + w, -1, y, y + h]);
            yCoordsSet.add(y);
            yCoordsSet.add(y + h);
        }
        events.sort((a, b) => {
            if (a[0] !== b[0]) return a[0] - b[0];
            return a[1] - b[1];
        });

        const yCoords = Array.from(yCoordsSet).sort((a, b) => a - b);

        if (yCoords.length <= 1) {
            return 0.0;
        }

        const st = new SegmentTree(yCoords);
        let totalArea = 0.0;
        let prevX = events[0][0];

        for (const event of events) {
            const [x, type, y1, y2] = event;
            const currentLength = st.get_total_length();
            totalArea += currentLength * (x - prevX);
            st.update(y1, y2, type);
            prevX = x;
        }
        return totalArea;
    };

    const originalRects = []; // [x, y, width, height]
    let minYOverall = Infinity;
    let maxYOverall = -Infinity;
    for (const s of squares) {
        const [x, y, l] = s;
        originalRects.push([x, parseFloat(y), parseFloat(l), parseFloat(l)]);
        minYOverall = Math.min(minYOverall, parseFloat(y));
        maxYOverall = Math.max(maxYOverall, parseFloat(y + l));
    }

    const totalUniqueArea = calculateUniqueArea(originalRects);
    const targetAreaBelow = totalUniqueArea / 2.0;

    let low = minYOverall;
    let high = maxYOverall;
    let ans = high; 

    for (let i = 0; i < 100; ++i) {
        const mid = low + (high - low) / 2.0;

        const clippedRectsBelow = [];
        for (const s of squares) {
            const [x, y, l] = s;
            const yBottom = parseFloat(y);
            const yTop = parseFloat(y + l);

            if (yBottom < mid) {
                const clippedYTop = Math.min(yTop, mid);
                const clippedHeight = clippedYTop - yBottom;
                if (clippedHeight > 0) {
                    clippedRectsBelow.push([x, yBottom, parseFloat(l), clippedHeight]);
                }
            }
        }

        const areaBelowMid = calculateUniqueArea(clippedRectsBelow);

        if (areaBelowMid >= targetAreaBelow) {
            ans = mid;
            high = mid;
        } else {
            low = mid;
        }
    }

    return ans;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function separateSquares(squares: number[][]): number {

    class SegmentTree {
        private yCoords: number[];
        private N: number;
        private tree: [number, number][]; // [count, length]

        constructor(yCoords: number[]) {
            this.yCoords = yCoords;
            this.N = yCoords.length - 1;
            if (this.N < 0) this.N = 0;
            this.tree = Array(4 * Math.max(1, this.N)).fill(null).map(() => [0, 0.0]);
        }

        private _update(nodeIdx: number, startIdx: number, endIdx: number, queryY1Idx: number, queryY2Idx: number, val: number): void {
            if (startIdx >= queryY2Idx || endIdx <= queryY1Idx) {
                return;
            }

            if (queryY1Idx <= startIdx && endIdx <= queryY2Idx) {
                this.tree[nodeIdx][0] += val;
            } else {
                const midIdx = Math.floor((startIdx + endIdx) / 2);
                this._update(2 * nodeIdx, startIdx, midIdx, queryY1Idx, queryY2Idx, val);
                this._update(2 * nodeIdx + 1, midIdx, endIdx, queryY1Idx, queryY2Idx, val);
            }

            if (this.tree[nodeIdx][0] > 0) {
                this.tree[nodeIdx][1] = this.yCoords[endIdx] - this.yCoords[startIdx];
            } else {
                if (startIdx + 1 === endIdx) {
                    this.tree[nodeIdx][1] = 0.0;
                } else {
                    this.tree[nodeIdx][1] = this.tree[2 * nodeIdx][1] + this.tree[2 * nodeIdx + 1][1];
                }
            }
        }

        public update(y1: number, y2: number, val: number): void {
            if (this.N === 0) return;
            const y1Idx = this.binarySearch(this.yCoords, y1);
            const y2Idx = this.binarySearch(this.yCoords, y2);

            if (y1Idx >= y2Idx) {
                return;
            }

            this._update(1, 0, this.N, y1Idx, y2Idx, val);
        }

        public getTotalLength(): number {
            if (this.N === 0) return 0.0;
            return this.tree[1][1];
        }

        private binarySearch(arr: number[], target: number): number {
            let low = 0;
            let high = arr.length - 1;
            let ans = arr.length;
            while (low <= high) {
                const mid = Math.floor((low + high) / 2);
                if (arr[mid] >= target) {
                    ans = mid;
                    high = mid - 1;
                } else {
                    low = mid + 1;
                }
            }
            return ans;
        }
    }

    type Rect = [number, number, number, number]; // [x, y, width, height]
    type Event = [number, number, number, number]; // [x, type, y1, y2]

    const calculateUniqueArea = (rects: Rect[]): number => {
        if (rects.length === 0) {
            return 0.0;
        }

        const events: Event[] = [];
        const yCoordsSet = new Set<number>();
        for (const rect of rects) {
            const [x, y, w, h] = rect;
            events.push([x, 1, y, y + h]);
            events.push([x + w, -1, y, y + h]);
            yCoordsSet.add(y);
            yCoordsSet.add(y + h);
        }
        events.sort((a, b) => {
            if (a[0] !== b[0]) return a[0] - b[0];
            return a[1] - b[1];
        });

        const yCoords = Array.from(yCoordsSet).sort((a, b) => a - b);

        if (yCoords.length <= 1) {
            return 0.0;
        }

        const st = new SegmentTree(yCoords);
        let totalArea = 0.0;
        let prevX = events[0][0];

        for (const event of events) {
            const [x, type, y1, y2] = event;
            const currentLength = st.getTotalLength();
            totalArea += currentLength * (x - prevX);
            st.update(y1, y2, type);
            prevX = x;
        }
        return totalArea;
    };

    const originalRects: Rect[] = [];
    let minYOverall = Infinity;
    let maxYOverall = -Infinity;
    for (const s of squares) {
        const [x, y, l] = s;
        originalRects.push([x, y, l, l]);
        minYOverall = Math.min(minYOverall, y);
        maxYOverall = Math.max(maxYOverall, y + l);
    }

    const totalUniqueArea = calculateUniqueArea(originalRects);
    const targetAreaBelow = totalUniqueArea / 2.0;

    let low = minYOverall;
    let high = maxYOverall;
    let ans = high; 

    for (let i = 0; i < 100; ++i) {
        const mid = low + (high - low) / 2.0;

        const clippedRectsBelow: Rect[] = [];
        for (const s of squares) {
            const [x, y, l] = s;
            const yBottom = y;
            const yTop = y + l;

            if (yBottom < mid) {
                const clippedYTop = Math.min(yTop, mid);
                const clippedHeight = clippedYTop - yBottom;
                if (clippedHeight > 0) {
                    clippedRectsBelow.push([x, yBottom, l, clippedHeight]);
                }
            }
        }

        const areaBelowMid = calculateUniqueArea(clippedRectsBelow);

        if (areaBelowMid >= targetAreaBelow) {
            ans = mid;
            high = mid;
        } else {
            low = mid;
        }
    }

    return ans;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
<?php

class SegmentTree {
    private $yCoords;
    private $N;
    private $tree; // [count, length]

    public function __construct(array $yCoords) {
        $this->yCoords = $yCoords;
        $this->N = count($yCoords) - 1;
        if ($this->N < 0) $this->N = 0;
        $this->tree = array_fill(0, 4 * max(1, $this->N), [0, 0.0]);
    }

    private function _update(int $nodeIdx, int $startIdx, int $endIdx, int $queryY1Idx, int $queryY2Idx, int $val): void {
        if ($startIdx >= $queryY2Idx || $endIdx <= $queryY1Idx) {
            return;
        }

        if ($queryY1Idx <= $startIdx && $endIdx <= $queryY2Idx) {
            $this->tree[$nodeIdx][0] += $val;
        } else {
            $midIdx = floor(($startIdx + $endIdx) / 2);
            $this->_update(2 * $nodeIdx, $startIdx, $midIdx, $queryY1Idx, $queryY2Idx, $val);
            $this->_update(2 * $nodeIdx + 1, $midIdx, $endIdx, $queryY1Idx, $queryY2Idx, $val);
        }

        if ($this->tree[$nodeIdx][0] > 0) {
            $this->tree[$nodeIdx][1] = (float)($this->yCoords[$endIdx] - $this->yCoords[$startIdx]);
        } else {
            if ($startIdx + 1 === $endIdx) {
                $this->tree[$nodeIdx][1] = 0.0;
            } else {
                $this->tree[$nodeIdx][1] = $this->tree[2 * $nodeIdx][1] + $this->tree[2 * $nodeIdx + 1][1];
            }
        }
    }

    public function update(float $y1, float $y2, int $val): void {
        if ($this->N === 0) return;
        $y1Idx = $this->binarySearch($this->yCoords, $y1);
        $y2Idx = $this->binarySearch($this->yCoords, $y2);

        if ($y1Idx >= $y2Idx) {
            return;
        }

        $this->_update(1, 0, $this->N, $y1Idx, $y2Idx, $val);
    }

    public function getTotalLength(): float {
        if ($this->N === 0) return 0.0;
        return $this->tree[1][1];
    }

    private function binarySearch(array $arr, float $target): int {
        $low = 0;
        $high = count($arr) - 1;
        $ans = count($arr);
        while ($low <= $high) {
            $mid = floor(($low + $high) / 2);
            if ($arr[$mid] >= $target) {
                $ans = $mid;
                $high = $mid - 1;
            } else {
                $low = $mid + 1;
            }
        }
        return $ans;
    }
}

class Solution {

    /**
     * @param Integer[][] $squares
     * @return Float
     */
    function separateSquares($squares) {

        $calculateUniqueArea = function(array $rects): float {
            if (empty($rects)) {
                return 0.0;
            }

            $events = []; // [x, type, y1, y2]
            $yCoordsSet = [];
            foreach ($rects as $rect) {
                list($x, $y, $w, $h) = $rect;
                $events[] = [$x, 1, $y, $y + $h];
                $events[] = [$x + $w, -1, $y, $y + $h];
                $yCoordsSet[(string)$y] = $y; // Use string key to handle float uniqueness
                $yCoordsSet[(string)($y + $h)] = $y + $h;
            }
            usort($events, function($a, $b) {
                if ($a[0] !== $b[0]) return $a[0] - $b[0];
                return $a[1] - $b[1];
            });

            $yCoords = array_values($yCoordsSet);
            sort($yCoords, SORT_NUMERIC);

            if (count($yCoords) <= 1) {
                return 0.0;
            }

            $st = new SegmentTree($yCoords);
            $totalArea = 0.0;
            $prevX = $events[0][0];

            foreach ($events as $event) {
                list($x, $type, $y1, $y2) = $event;
                $currentLength = $st->getTotalLength();
                $totalArea += $currentLength * ($x - $prevX);
                $st->update($y1, $y2, $type);
                $prevX = $x;
            }
            return $totalArea;
        };

        $originalRects = []; // [x, y, width, height]
        $minYOverall = INF;
        $maxYOverall = -INF;
        foreach ($squares as $s) {
            list($x, $y, $l) = $s;
            $originalRects[] = [$x, (float)$y, (float)$l, (float)$l];
            $minYOverall = min($minYOverall, (float)$y);
            $maxYOverall = max($maxYOverall, (float)($y + $l));
        }

        $totalUniqueArea = $calculateUniqueArea($originalRects);

        $targetAreaBelow = $totalUniqueArea / 2.0;

        $low = $minYOverall;
        $high = $maxYOverall;
        $ans = $high; 

        for ($i = 0; $i < 100; ++$i) {
            $mid = $low + ($high - $low) / 2.0;

            $clippedRectsBelow = [];
            foreach ($squares as $s) {
                list($x, $y, $l) = $s;
                $yBottom = (float)$y;
                $yTop = (float)($y + $l);

                if ($yBottom < $mid) {
                    $clippedYTop = min($yTop, $mid);
                    $clippedHeight = $clippedYTop - $yBottom;
                    if ($clippedHeight > 0) {
                        $clippedRectsBelow[] = [$x, $yBottom, (float)$l, $clippedHeight];
                    }
                }
            }

            $areaBelowMid = $calculateUniqueArea($clippedRectsBelow);

            if ($areaBelowMid >= $targetAreaBelow) {
                $ans = $mid;
                $high = $mid;
            } else {
                $low = $mid;
            }
        }

        return $ans;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
import Foundation

class SegmentTree {
    private var yCoords: [Double]
    private var N: Int
    private var tree: [[Double]] // [count, length]

    init(yCoords: [Double]) {
        self.yCoords = yCoords
        self.N = yCoords.count - 1
        if self.N < 0 { self.N = 0 }
        self.tree = Array(repeating: [0.0, 0.0], count: 4 * max(1, self.N))
    }

    private func _update(nodeIdx: Int, startIdx: Int, endIdx: Int, queryY1Idx: Int, queryY2Idx: Int, val: Int) {
        if startIdx >= queryY2Idx || endIdx <= queryY1Idx {
            return
        }

        if queryY1Idx <= startIdx && endIdx <= queryY2Idx {
            self.tree[nodeIdx][0] += Double(val)
        } else {
            let midIdx = (startIdx + endIdx) / 2
            _update(nodeIdx: 2 * nodeIdx, startIdx: startIdx, endIdx: midIdx, queryY1Idx: queryY1Idx, queryY2Idx: queryY2Idx, val: val)
            _update(nodeIdx: 2 * nodeIdx + 1, startIdx: midIdx, endIdx: endIdx, queryY1Idx: queryY1Idx, queryY2Idx: queryY2Idx, val: val)
        }

        if self.tree[nodeIdx][0] > 0 {
            self.tree[nodeIdx][1] = self.yCoords[endIdx] - self.yCoords[startIdx]
        } else {
            if startIdx + 1 == endIdx {
                self.tree[nodeIdx][1] = 0.0
            } else {
                self.tree[nodeIdx][1] = self.tree[2 * nodeIdx][1] + self.tree[2 * nodeIdx + 1][1]
            }
        }
    }

    func update(y1: Double, y2: Double, val: Int) {
        if self.N == 0 { return }
        let y1Idx = binarySearch(arr: self.yCoords, target: y1)
        let y2Idx = binarySearch(arr: self.yCoords, target: y2)

        if y1Idx >= y2Idx {
            return
        }

        _update(nodeIdx: 1, startIdx: 0, endIdx: self.N, queryY1Idx: y1Idx, queryY2Idx: y2Idx, val: val)
    }

    func getTotalLength() -> Double {
        if self.N == 0 { return 0.0 }
        return self.tree[1][1]
    }

    private func binarySearch(arr: [Double], target: Double) -> Int {
        var low = 0
        var high = arr.count - 1
        var ans = arr.count
        while low <= high {
            let mid = (low + high) / 2
            if arr[mid] >= target {
                ans = mid
                high = mid - 1
            } else {
                low = mid + 1;
            }
        }
        return ans;
    }
}

class Solution {
    func separateSquares(_ squares: [[Int]]) -> Double {

        typealias Rect = (x: Int, y: Double, width: Double, height: Double)
        typealias Event = (x: Int, type: Int, y1: Double, y2: Double)

        let calculateUniqueArea = { (rects: [Rect]) -> Double in
            if rects.isEmpty {
                return 0.0
            }

            var events: [Event] = []
            var yCoordsSet = Set<Double>()
            for rect in rects {
                events.append((rect.x, 1, rect.y, rect.y + rect.height))
                events.append((rect.x + Int(rect.width), -1, rect.y, rect.y + rect.height))
                yCoordsSet.insert(rect.y)
                yCoordsSet.insert(rect.y + rect.height)
            }
            events.sort { (a, b) in
                if a.x != b.x { return a.x < b.x }
                return a.type < b.type
            }

            let yCoords = yCoordsSet.sorted()

            if yCoords.count <= 1 {
                return 0.0
            }

            let st = SegmentTree(yCoords: yCoords)
            var totalArea = 0.0
            var prevX = events[0].x

            for event in events {
                let currentLength = st.getTotalLength()
                totalArea += currentLength * Double(event.x - prevX)
                st.update(y1: event.y1, y2: event.y2, val: event.type)
                prevX = event.x
            }
            return totalArea
        }

        var originalRects: [Rect] = []
        var minYOverall: Double = .infinity
        var maxYOverall: Double = -.infinity
        for s in squares {
            let x = s[0]
            let y = Double(s[1])
            let l = Double(s[2])
            originalRects.append((x, y, l, l))
            minYOverall = min(minYOverall, y)
            maxYOverall = max(maxYOverall, y + l)
        }

        let totalUniqueArea = calculateUniqueArea(originalRects)

        let targetAreaBelow = totalUniqueArea / 2.0

        var low = minYOverall
        var high = maxYOverall
        var ans = high 

        for _ in 0..<100 { 
            let mid = low + (high - low) / 2.0

            var clippedRectsBelow: [Rect] = []
            for s in squares {
                let x = s[0]
                let yBottom = Double(s[1])
                let l = Double(s[2])
                let yTop = yBottom + l

                if yBottom < mid {
                    let clippedYTop = min(yTop, mid)
                    let clippedHeight = clippedYTop - yBottom
                    if clippedHeight > 0 {
                        clippedRectsBelow.append((x, yBottom, l, clippedHeight))
                    }
                }
            }

            let areaBelowMid = calculateUniqueArea(clippedRectsBelow)

            if areaBelowMid >= targetAreaBelow {
                ans = mid;
                high = mid;
            } else {
                low = mid;
            }
        }

        return ans;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    data class Node(var count: Int = 0, var length: Long = 0L)

    private lateinit var xCoordsUnique: List<Long>
    private lateinit var tree: Array<Node>
    private var xMapSize: Int = 0

    private fun update(nodeIdx: Int, nodeRangeStartIdx: Int, nodeRangeEndIdx: Int,
                       queryStartIdx: Int, queryEndIdx: Int, delta: Int) {
        if (queryStartIdx >= nodeRangeEndIdx || queryEndIdx <= nodeRangeStartIdx) {
            return
        }

        if (queryStartIdx <= nodeRangeStartIdx && nodeRangeEndIdx <= queryEndIdx) {
            tree[nodeIdx].count += delta
            recalculateLength(nodeIdx, nodeRangeStartIdx, nodeRangeEndIdx)
            return
        }

        val midIdx = nodeRangeStartIdx + (nodeRangeEndIdx - nodeRangeStartIdx) / 2
        update(nodeIdx * 2, nodeRangeStartIdx, midIdx, queryStartIdx, queryEndIdx, delta)
        update(nodeIdx * 2 + 1, midIdx, nodeRangeEndIdx, queryStartIdx, queryEndIdx, delta)

        recalculateLength(nodeIdx, nodeRangeStartIdx, nodeRangeEndIdx)
    }

    private fun recalculateLength(nodeIdx: Int, nodeRangeStartIdx: Int, nodeRangeEndIdx: Int) {
        if (tree[nodeIdx].count > 0) {
            tree[nodeIdx].length = xCoordsUnique[nodeRangeEndIdx] - xCoordsUnique[nodeRangeStartIdx]
        } else {
            if (nodeRangeStartIdx + 1 == nodeRangeEndIdx) {
                tree[nodeIdx].length = 0L
            } else {
                tree[nodeIdx].length = tree[nodeIdx * 2].length + tree[nodeIdx * 2 + 1].length
            }
        }
    }

    private fun mapXToIdx(xVal: Long): Int {
        return xCoordsUnique.binarySearch(xVal).let { if (it < 0) -it - 1 else it }
    }

    fun separateSquares(squares: Array<IntArray>): Double {
        val xSet = mutableSetOf<Long>()
        val sweepEvents = mutableListOf<SweepEvent>()

        for (s in squares) {
            val x = s[0].toLong()
            val y = s[1].toLong()
            val l = s[2].toLong()
            xSet.add(x)
            xSet.add(x + l)
            sweepEvents.add(SweepEvent(y, x, x + l, 1))
            sweepEvents.add(SweepEvent(y + l, x, x + l, -1))
        }

        xCoordsUnique = xSet.sorted()
        xMapSize = xCoordsUnique.size - 1

        if (xMapSize == 0) {
            return squares.minOf { it[1] }.toDouble()
        }

        sweepEvents.sortWith(compareBy<SweepEvent> { it.y }.thenBy { it.type })

        tree = Array(4 * xMapSize) { Node() }

        // First pass: Calculate total unique area
        var totalArea: Long = 0L
        var prevY: Long = sweepEvents[0].y

        for (event in sweepEvents) {
            val currY = event.y
            if (currY > prevY) {
                totalArea += tree[1].length * (currY - prevY)
            }

            val xStartIdx = mapXToIdx(event.xStart)
            val xEndIdx = mapXToIdx(event.xEnd)
            if (xStartIdx < xEndIdx) {
                update(1, 0, xMapSize, xStartIdx, xEndIdx, event.type)
            }
            prevY = currY
        }

        val targetArea = totalArea.toDouble() / 2.0

        // Second pass: Find the split y-coordinate
        tree = Array(4 * xMapSize) { Node() }
        var currentAreaBelowLine: Double = 0.0
        prevY = sweepEvents[0].y

        for (event in sweepEvents) {
            val currY = event.y
            if (currY > prevY) {
                val currentWidth = tree[1].length
                val areaInStrip = currentWidth * (currY - prevY)

                if (currentAreaBelowLine + areaInStrip >= targetArea) {
                    val remainingAreaNeeded = targetArea - currentAreaBelowLine
                    if (currentWidth == 0L) {
                        return prevY.toDouble()
                    }
                    return prevY.toDouble() + remainingAreaNeeded / currentWidth.toDouble()
                }
                currentAreaBelowLine += areaInStrip.toDouble()
            }

            val xStartIdx = mapXToIdx(event.xStart)
            val xEndIdx = mapXToIdx(event.xEnd)
            if (xStartIdx < xEndIdx) {
                update(1, 0, xMapSize, xStartIdx, xEndIdx, event.type)
            }
            prevY = currY
        }

        return prevY.toDouble()
    }

    data class SweepEvent(val y: Long, val xStart: Long, val xEnd: Long, val type: Int)
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  late List<int> _xCoordsUnique;
  late List<_Node> _tree;
  late int _xMapSize;

  _Node _createNode() => _Node(0, 0);

  void _update(int nodeIdx, int nodeRangeStartIdx, int nodeRangeEndIdx,
      int queryStartIdx, int queryEndIdx, int delta) {
    if (queryStartIdx >= nodeRangeEndIdx || queryEndIdx <= nodeRangeStartIdx) {
      return;
    }

    if (queryStartIdx <= nodeRangeStartIdx && nodeRangeEndIdx <= queryEndIdx) {
      _tree[nodeIdx].count += delta;
      _recalculateLength(nodeIdx, nodeRangeStartIdx, nodeRangeEndIdx);
      return;
    }

    int midIdx = nodeRangeStartIdx + (nodeRangeEndIdx - nodeRangeStartIdx) ~/ 2;
    _update(nodeIdx * 2, nodeRangeStartIdx, midIdx, queryStartIdx, queryEndIdx, delta);
    _update(nodeIdx * 2 + 1, midIdx, nodeRangeEndIdx, queryStartIdx, queryEndIdx, delta);

    _recalculateLength(nodeIdx, nodeRangeStartIdx, nodeRangeEndIdx);
  }

  void _recalculateLength(int nodeIdx, int nodeRangeStartIdx, int nodeRangeEndIdx) {
    if (_tree[nodeIdx].count > 0) {
      _tree[nodeIdx].length = _xCoordsUnique[nodeRangeEndIdx] - _xCoordsUnique[nodeRangeStartIdx];
    } else {
      if (nodeRangeStartIdx + 1 == nodeRangeEndIdx) {
        _tree[nodeIdx].length = 0;
      } else {
        _tree[nodeIdx].length = _tree[nodeIdx * 2].length + _tree[nodeIdx * 2 + 1].length;
      }
    }
  }

  int _mapXToIdx(int xVal) {
    int low = 0;
    int high = _xCoordsUnique.length - 1;
    int ans = _xCoordsUnique.length;
    while (low <= high) {
      int mid = low + (high - low) ~/ 2;
      if (_xCoordsUnique[mid] >= xVal) {
        ans = mid;
        high = mid - 1;
      } else {
        low = mid + 1;
      }
    }
    return ans;
  }

  double separateSquares(List<List<int>> squares) {
    Set<int> xSet = {};
    List<_SweepEvent> sweepEvents = [];

    for (var s in squares) {
      int x = s[0];
      int y = s[1];
      int l = s[2];
      xSet.add(x);
      xSet.add(x + l);
      sweepEvents.add(_SweepEvent(y, x, x + l, 1));
      sweepEvents.add(_SweepEvent(y + l, x, x + l, -1));
    }

    _xCoordsUnique = xSet.toList()..sort();
    _xMapSize = _xCoordsUnique.length - 1;

    if (_xMapSize == 0) {
      return squares.map((s) => s[1]).reduce((a, b) => a < b ? a : b).toDouble();
    }

    sweepEvents.sort((a, b) {
      if (a.y != b.y) return a.y.compareTo(b.y);
      return a.type.compareTo(b.type);
    });

    _tree = List.generate(4 * _xMapSize, (index) => _createNode());

    // First pass: Calculate total unique area
    int totalArea = 0;
    int prevY = sweepEvents[0].y;

    for (var event in sweepEvents) {
      int currY = event.y;
      if (currY > prevY) {
        totalArea += _tree[1].length * (currY - prevY);
      }

      int xStartIdx = _mapXToIdx(event.xStart);
      int xEndIdx = _mapXToIdx(event.xEnd);
      if (xStartIdx < xEndIdx) {
        _update(1, 0, _xMapSize, xStartIdx, xEndIdx, event.type);
      }
      prevY = currY;
    }

    double targetArea = totalArea.toDouble() / 2.0;

    // Second pass: Find the split y-coordinate
    _tree = List.generate(4 * _xMapSize, (index) => _createNode());
    double currentAreaBelowLine = 0.0;
    prevY = sweepEvents[0].y;

    for (var event in sweepEvents) {
      int currY = event.y;
      if (currY > prevY) {
        int currentWidth = _tree[1].length;
        int areaInStrip = currentWidth * (currY - prevY);

        if (currentAreaBelowLine + areaInStrip >= targetArea) {
          double remainingAreaNeeded = targetArea - currentAreaBelowLine;
          if (currentWidth == 0) {
            return prevY.toDouble();
          }
          return prevY.toDouble() + remainingAreaNeeded / currentWidth.toDouble();
        }
        currentAreaBelowLine += areaInStrip.toDouble();
      }

      int xStartIdx = _mapXToIdx(event.xStart);
      int xEndIdx = _mapXToIdx(event.xEnd);
      if (xStartIdx < xEndIdx) {
        _update(1, 0, _xMapSize, xStartIdx, xEndIdx, event.type);
      }
      prevY = currY;
    }

    return prevY.toDouble();
  }
}

class _Node {
  int count;
  int length;
  _Node(this.count, this.length);
}

class _SweepEvent {
  int y;
  int xStart;
  int xEnd;
  int type;
  _SweepEvent(this.y, this.xStart, this.xEnd, this.type);
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

type Node struct {
    count  int
    length int
}

type SweepEvent struct {
    y      int
    xStart int
    xEnd   int
    typ    int // 1 for start, -1 for end
}

var xCoordsUnique []int
var tree []Node
var xMapSize int

func update(nodeIdx, nodeRangeStartIdx, nodeRangeEndIdx,
    queryStartIdx, queryEndIdx, delta int) {
    if queryStartIdx >= nodeRangeEndIdx || queryEndIdx <= nodeRangeStartIdx {
        return
    }

    if queryStartIdx <= nodeRangeStartIdx && nodeRangeEndIdx <= queryEndIdx {
        tree[nodeIdx].count += delta
        recalculateLength(nodeIdx, nodeRangeStartIdx, nodeRangeEndIdx)
        return
    }

    midIdx := nodeRangeStartIdx + (nodeRangeEndIdx - nodeRangeStartIdx) / 2
    update(nodeIdx * 2, nodeRangeStartIdx, midIdx, queryStartIdx, queryEndIdx, delta)
    update(nodeIdx * 2 + 1, midIdx, nodeRangeEndIdx, queryStartIdx, queryEndIdx, delta)

    recalculateLength(nodeIdx, nodeRangeStartIdx, nodeRangeEndIdx)
}

func recalculateLength(nodeIdx, nodeRangeStartIdx, nodeRangeEndIdx int) {
    if tree[nodeIdx].count > 0 {
        tree[nodeIdx].length = xCoordsUnique[nodeRangeEndIdx] - xCoordsUnique[nodeRangeStartIdx]
    } else {
        if nodeRangeStartIdx + 1 == nodeRangeEndIdx {
            tree[nodeIdx].length = 0
        } else {
            tree[nodeIdx].length = tree[nodeIdx * 2].length + tree[nodeIdx * 2 + 1].length
        }
    }
}

func mapXToIdx(xVal int) int {
    low := 0
    high := len(xCoordsUnique) - 1
    ans := len(xCoordsUnique)
    for low <= high {
        mid := low + (high - low) / 2
        if xCoordsUnique[mid] >= xVal {
            ans = mid
            high = mid - 1
        } else {
            low = mid + 1
        }
    }
    return ans
}

func separateSquares(squares [][]int) float64 {
    xSet := make(map[int]bool)
    var sweepEvents []SweepEvent

    for _, s := range squares {
        x, y, l := s[0], s[1], s[2]
        xSet[x] = true
        xSet[x+l] = true
        sweepEvents = append(sweepEvents, SweepEvent{y, x, x + l, 1})
        sweepEvents = append(sweepEvents, SweepEvent{y + l, x, x + l, -1})
    }

    xCoordsUnique = make([]int, 0, len(xSet))
    for xVal := range xSet {
        xCoordsUnique = append(xCoordsUnique, xVal)
    }
    sort.Ints(xCoordsUnique)

    xMapSize = len(xCoordsUnique) - 1

    if xMapSize == 0 {
        minY := squares[0][1]
        for i := 1; i < len(squares); i++ {
            if squares[i][1] < minY {
                minY = squares[i][1]
            }
        }
        return float64(minY)
    }

    sort.Slice(sweepEvents, func(i, j int) bool {
        if sweepEvents[i].y != sweepEvents[j].y {
            return sweepEvents[i].y < sweepEvents[j].y
        }
        return sweepEvents[i].typ < sweepEvents[j].typ
    })

    tree = make([]Node, 4 * xMapSize)

    // First pass: Calculate total unique area
    totalArea := 0
    prevY := sweepEvents[0].y

    for _, event := range sweepEvents {
        currY := event.y
        if currY > prevY {
            totalArea += tree[1].length * (currY - prevY)
        }

        xStartIdx := mapXToIdx(event.xStart)
        xEndIdx := mapXToIdx(event.xEnd)
        if xStartIdx < xEndIdx {
            update(1, 0, xMapSize, xStartIdx, xEndIdx, event.typ)
        }
        prevY = currY
    }

    targetArea := float64(totalArea) / 2.0

    // Second pass: Find the split y-coordinate
    tree = make([]Node, 4 * xMapSize)
    currentAreaBelowLine := 0.0
    prevY = sweepEvents[0].y

    for _, event := range sweepEvents {
        currY := event.y
        if currY > prevY {
            currentWidth := tree[1].length
            areaInStrip := currentWidth * (currY - prevY)

            if currentAreaBelowLine + float64(areaInStrip) >= targetArea {
                remainingAreaNeeded := targetArea - currentAreaBelowLine
                if currentWidth == 0 {
                    return float64(prevY)
                }
                return float64(prevY) + remainingAreaNeeded / float64(currentWidth)
            }
            currentAreaBelowLine += float64(areaInStrip)
        }

        xStartIdx := mapXToIdx(event.xStart)
        xEndIdx := mapXToIdx(event.xEnd)
        if xStartIdx < xEndIdx {
            update(1, 0, xMapSize, xStartIdx, xEndIdx, event.typ)
        }
        prevY = currY
    }

    return float64(prevY)
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
require 'set'

# @param {Integer[][]} squares
# @return {Float}
def separate_squares(squares)
    x_set = Set.new
    sweep_events = []

    squares.each do |s|
        x, y, l = s[0], s[1], s[2]
        x_set.add(x)
        x_set.add(x + l)
        sweep_events << {y: y, x_start: x, x_end: x + l, type: 1}
        sweep_events << {y: y + l, x_start: x, x_end: x + l, type: -1}
    end

    $x_coords_unique = x_set.to_a.sort
    $x_map_size = $x_coords_unique.length - 1

    if $x_map_size == 0
        return squares.map { |s| s[1] }.min.to_f
    end

    sweep_events.sort! do |a, b|
        if a[:y] != b[:y]
            a[:y] <=> b[:y]
        else
            a[:type] <=> b[:type]
        end
    end

    $tree = Array.new(4 * $x_map_size) { {count: 0, length: 0} }

    # First pass: Calculate total unique area
    total_area = 0
    prev_y = sweep_events[0][:y]

    sweep_events.each do |event|
        curr_y = event[:y]
        if curr_y > prev_y
            total_area += $tree[1][:length] * (curr_y - prev_y)
        end

        x_start_idx = map_x_to_idx(event[:x_start])
        x_end_idx = map_x_to_idx(event[:x_end])
        if x_start_idx < x_end_idx
            update_segment_tree(1, 0, $x_map_size, x_start_idx, x_end_idx, event[:type])
        end
        prev_y = curr_y
    end

    target_area = total_area.to_f / 2.0

    # Second pass: Find the split y-coordinate
    $tree = Array.new(4 * $x_map_size) { {count: 0, length: 0} }
    current_area_below_line = 0.0
    prev_y = sweep_events[0][:y]

    sweep_events.each do |event|
        curr_y = event[:y]
        if curr_y > prev_y
            current_width = $tree[1][:length]
            area_in_strip = current_width * (curr_y - prev_y)

            if current_area_below_line + area_in_strip >= target_area
                remaining_area_needed = target_area - current_area_below_line
                if current_width == 0
                    return prev_y.to_f
                end
                return prev_y.to_f + remaining_area_needed / current_width.to_f
            end
            current_area_below_line += area_in_strip.to_f
        end

        x_start_idx = map_x_to_idx(event[:x_start])
        x_end_idx = map_x_to_idx(event[:x_end])
        if x_start_idx < x_end_idx
            update_segment_tree(1, 0, $x_map_size, x_start_idx, x_end_idx, event[:type])
        end
        prev_y = curr_y
    end

    prev_y.to_f
end

def update_segment_tree(node_idx, node_range_start_idx, node_range_end_idx,
                       query_start_idx, query_end_idx, delta)
    if query_start_idx >= node_range_end_idx || query_end_idx <= node_range_start_idx
        return
    end

    if query_start_idx <= node_range_start_idx && node_range_end_idx <= query_end_idx
        $tree[node_idx][:count] += delta
        recalculate_length(node_idx, node_range_start_idx, node_range_end_idx)
        return
    end

    mid_idx = node_range_start_idx + (node_range_end_idx - node_range_start_idx) / 2
    update_segment_tree(node_idx * 2, node_range_start_idx, mid_idx, query_start_idx, query_end_idx, delta)
    update_segment_tree(node_idx * 2 + 1, mid_idx, node_range_end_idx, query_start_idx, query_end_idx, delta)

    recalculate_length(node_idx, node_range_start_idx, node_range_end_idx)
end

def recalculate_length(node_idx, node_range_start_idx, node_range_end_idx)
    if $tree[node_idx][:count] > 0
        $tree[node_idx][:length] = $x_coords_unique[node_range_end_idx] - $x_coords_unique[node_range_start_idx]
    else
        if node_range_start_idx + 1 == node_range_end_idx
            $tree[node_idx][:length] = 0
        else
            $tree[node_idx][:length] = $tree[node_idx * 2][:length] + $tree[node_idx * 2 + 1][:length]
        end
    end
end

def map_x_to_idx(x_val)
    $x_coords_unique.bsearch_index { |x| x >= x_val }
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.collection.mutable

object Solution {
    case class Node(var count: Int, var length: Long)

    private var xCoordsUnique: Array[Long] = _
    private var tree: Array[Node] = _
    private var xMapSize: Int = _

    private def update(nodeIdx: Int, nodeRangeStartIdx: Int, nodeRangeEndIdx: Int,
                       queryStartIdx: Int, queryEndIdx: Int, delta: Int): Unit = {
        if (queryStartIdx >= nodeRangeEndIdx || queryEndIdx <= nodeRangeStartIdx) {
            return
        }

        if (queryStartIdx <= nodeRangeStartIdx && nodeRangeEndIdx <= queryEndIdx) {
            tree(nodeIdx).count += delta
            recalculateLength(nodeIdx, nodeRangeStartIdx, nodeRangeEndIdx)
            return
        }

        val midIdx = nodeRangeStartIdx + (nodeRangeEndIdx - nodeRangeStartIdx) / 2
        update(nodeIdx * 2, nodeRangeStartIdx, midIdx, queryStartIdx, queryEndIdx, delta)
        update(nodeIdx * 2 + 1, midIdx, nodeRangeEndIdx, queryStartIdx, queryEndIdx, delta)

        recalculateLength(nodeIdx, nodeRangeStartIdx, nodeRangeEndIdx)
    }

    private def recalculateLength(nodeIdx: Int, nodeRangeStartIdx: Int, nodeRangeEndIdx: Int): Unit = {
        if (tree(nodeIdx).count > 0) {
            tree(nodeIdx).length = xCoordsUnique(nodeRangeEndIdx) - xCoordsUnique(nodeRangeStartIdx)
        } else {
            if (nodeRangeStartIdx + 1 == nodeRangeEndIdx) {
                tree(nodeIdx).length = 0L
            } else {
                tree(nodeIdx).length = tree(nodeIdx * 2).length + tree(nodeIdx * 2 + 1).length
            }
        }
    }

    private def mapXToIdx(xVal: Long): Int = {
        val idx = java.util.Arrays.binarySearch(xCoordsUnique, xVal)
        if (idx < 0) -idx - 1 else idx
    }

    def separateSquares(squares: Array[Array[Int]]): Double = {
        val xSet = mutable.Set.empty[Long]
        val sweepEvents = mutable.ArrayBuffer.empty[SweepEvent]

        for (s <- squares) {
            val x = s(0).toLong
            val y = s(1).toLong
            val l = s(2).toLong
            xSet.add(x)
            xSet.add(x + l)
            sweepEvents += SweepEvent(y, x, x + l, 1)
            sweepEvents += SweepEvent(y + l, x, x + l, -1)
        }

        xCoordsUnique = xSet.toArray.sorted
        xMapSize = xCoordsUnique.length - 1

        if (xMapSize == 0) {
            return squares.map(_(1)).min.toDouble
        }

        sweepEvents.sortWith((a, b) => {
            if (a.y != b.y) a.y < b.y
            else a.type < b.type
        })

        tree = Array.fill(4 * xMapSize)(Node(0, 0L))

        // First pass: Calculate total unique area
        var totalArea: Long = 0L
        var prevY: Long = sweepEvents.head.y

        for (event <- sweepEvents) {
            val currY = event.y
            if (currY > prevY) {
                totalArea += tree(1).length * (currY - prevY)
            }

            val xStartIdx = mapXToIdx(event.xStart)
            val xEndIdx = mapXToIdx(event.xEnd)
            if (xStartIdx < xEndIdx) {
                update(1, 0, xMapSize, xStartIdx, xEndIdx, event.type)
            }
            prevY = currY
        }

        val targetArea = totalArea.toDouble / 2.0

        // Second pass: Find the split y-coordinate
        tree = Array.fill(4 * xMapSize)(Node(0, 0L))
        var currentAreaBelowLine: Double = 0.0
        prevY = sweepEvents.head.y

        for (event <- sweepEvents) {
            val currY = event.y
            if (currY > prevY) {
                val currentWidth = tree(1).length
                val areaInStrip = currentWidth * (currY - prevY)

                if (currentAreaBelowLine + areaInStrip >= targetArea) {
                    val remainingAreaNeeded = targetArea - currentAreaBelowLine
                    if (currentWidth == 0L) {
                        return prevY.toDouble
                    }
                    return prevY.toDouble + remainingAreaNeeded / currentWidth.toDouble
                }
                currentAreaBelowLine += areaInStrip.toDouble
            }

            val xStartIdx = mapXToIdx(event.xStart)
            val xEndIdx = mapXToIdx(event.xEnd)
            if (xStartIdx < xEndIdx) {
                update(1, 0, xMapSize, xStartIdx, xEndIdx, event.type)
            }
            prevY = currY
        }

        prevY.toDouble
    }

    case class SweepEvent(y: Long, xStart: Long, xEnd: Long, `type`: Int)
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
use std::collections::{BTreeSet, HashMap};

struct Node {
    count: i32,
    length: i64,
}

struct SweepEvent {
    y: i64,
    x_start: i64,
    x_end: i64,
    event_type: i32, // 1 for start, -1 for end
}

struct SegmentTree {
    x_coords_unique: Vec<i64>,
    tree: Vec<Node>,
    x_map_size: usize,
}

impl SegmentTree {
    fn new(x_coords_unique: Vec<i64>) -> Self {
        let x_map_size = x_coords_unique.len() - 1;
        let tree = vec![Node { count: 0, length: 0 }; 4 * x_map_size];
        SegmentTree {
            x_coords_unique,
            tree,
            x_map_size,
        }
    }

    fn update(&mut self, node_idx: usize, node_range_start_idx: usize, node_range_end_idx: usize,
              query_start_idx: usize, query_end_idx: usize, delta: i32) {
        if query_start_idx >= node_range_end_idx || query_end_idx <= node_range_start_idx {
            return;
        }

        if query_start_idx <= node_range_start_idx && node_range_end_idx <= query_end_idx {
            self.tree[node_idx].count += delta;
            self.recalculate_length(node_idx, node_range_start_idx, node_range_end_idx);
            return;
        }

        let mid_idx = node_range_start_idx + (node_range_end_idx - node_range_start_idx) / 2;
        self.update(node_idx * 2, node_range_start_idx, mid_idx, query_start_idx, query_end_idx, delta);
        self.update(node_idx * 2 + 1, mid_idx, node_range_end_idx, query_start_idx, query_end_idx, delta);

        self.recalculate_length(node_idx, node_range_start_idx, node_range_end_idx);
    }

    fn recalculate_length(&mut self, node_idx: usize, node_range_start_idx: usize, node_range_end_idx: usize) {
        if self.tree[node_idx].count > 0 {
            self.tree[node_idx].length = self.x_coords_unique[node_range_end_idx] - self.x_coords_unique[node_range_start_idx];
        } else {
            if node_range_start_idx + 1 == node_range_end_idx {
                self.tree[node_idx].length = 0;
            } else {
                self.tree[node_idx].length = self.tree[node_idx * 2].length + self.tree[node_idx * 2 + 1].length;
            }
        }
    }

    fn map_x_to_idx(&self, x_val: i64) -> usize {
        match self.x_coords_unique.binary_search(&x_val) {
            Ok(idx) => idx,
            Err(idx) => idx,
        }
    }

    fn get_total_length(&self) -> i64 {
        self.tree[1].length
    }
}

impl Solution {
    pub fn separate_squares(squares: Vec<Vec<i32>>) -> f64 {
        let mut x_set = BTreeSet::new();
        let mut sweep_events: Vec<SweepEvent> = Vec::new();

        for s in &squares {
            let x = s[0] as i64;
            let y = s[1] as i64;
            let l = s[2] as i64;
            x_set.insert(x);
            x_set.insert(x + l);
            sweep_events.push(SweepEvent { y, x_start: x, x_end: x + l, event_type: 1 });
            sweep_events.push(SweepEvent { y: y + l, x_start: x, x_end: x + l, event_type: -1 });
        }

        let x_coords_unique: Vec<i64> = x_set.into_iter().collect();

        if x_coords_unique.len() <= 1 {
            return squares.iter().map(|s| s[1] as f64).min_by(|a, b| a.partial_cmp(b).unwrap()).unwrap_or(0.0);
        }

        sweep_events.sort_by(|a, b| {
            if a.y != b.y {
                a.y.cmp(&b.y)
            } else {
                a.event_type.cmp(&b.event_type)
            }
        });

        let mut segment_tree = SegmentTree::new(x_coords_unique.clone());

        // First pass: Calculate total unique area
        let mut total_area: i64 = 0;
        let mut prev_y: i64 = sweep_events[0].y;

        for event in &sweep_events {
            let curr_y = event.y;
            if curr_y > prev_y {
                total_area += segment_tree.get_total_length() * (curr_y - prev_y);
            }

            let x_start_idx = segment_tree.map_x_to_idx(event.x_start);
            let x_end_idx = segment_tree.map_x_to_idx(event.x_end);
            if x_start_idx < x_end_idx {
                segment_tree.update(1, 0, segment_tree.x_map_size, x_start_idx, x_end_idx, event.event_type);
            }
            prev_y = curr_y;
        }

        let target_area = total_area as f64 / 2.0;

        // Second pass: Find the split y-coordinate
        let mut segment_tree_2 = SegmentTree::new(x_coords_unique);
        let mut current_area_below_line: f64 = 0.0;
        prev_y = sweep_events[0].y;

        for event in &sweep_events {
            let curr_y = event.y;
            if curr_y > prev_y {
                let current_width = segment_tree_2.get_total_length();
                let area_in_strip = current_width * (curr_y - prev_y);

                if current_area_below_line + area_in_strip as f64 >= target_area {
                    let remaining_area_needed = target_area - current_area_below_line;
                    if current_width == 0 {
                        return prev_y as f64;
                    }
                    return prev_y as f64 + remaining_area_needed / current_width as f64;
                }
                current_area_below_line += area_in_strip as f64;
            }

            let x_start_idx = segment_tree_2.map_x_to_idx(event.x_start);
            let x_end_idx = segment_tree_2.map_x_to_idx(event.x_end);
            if x_start_idx < x_end_idx {
                segment_tree_2.update(1, 0, segment_tree_2.x_map_size, x_start_idx, x_end_idx, event.event_type);
            }
            prev_y = curr_y;
        }

        prev_y as f64
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket

(struct node (count length) #:mutable #t)
(struct sweep-event (y x-start x-end type))

(define x-coords-unique #f)
(define tree #f)
(define x-map-size #f)

(define (update-segment-tree node-idx node-range-start-idx node-range-end-idx
                             query-start-idx query-end-idx delta)
  (when (and (< query-start-idx node-range-end-idx)
             (> query-end-idx node-range-start-idx))
    (if (and (<= query-start-idx node-range-start-idx)
             (>= query-end-idx node-range-end-idx))
        (begin
          (set-node-count! (vector-ref tree node-idx) (+ (node-count (vector-ref tree node-idx)) delta))
          (recalculate-length node-idx node-range-start-idx node-range-end-idx))
        (let* ((mid-idx (+ node-range-start-idx (quotient (- node-range-end-idx node-range-start-idx) 2))))
          (update-segment-tree (* node-idx 2) node-range-start-idx mid-idx query-start-idx query-end-idx delta)
          (update-segment-tree (+ (* node-idx 2) 1) mid-idx node-range-end-idx query-start-idx query-end-idx delta)
          (recalculate-length node-idx node-range-start-idx node-range-end-idx)))))

(define (recalculate-length node-idx node-range-start-idx node-range-end-idx)
  (if (> (node-count (vector-ref tree node-idx)) 0)
      (set-node-length! (vector-ref tree node-idx)
                        (- (vector-ref x-coords-unique node-range-end-idx)
                           (vector-ref x-coords-unique node-range-start-idx)))
      (if (= (+ node-range-start-idx 1) node-range-end-idx)
          (set-node-length! (vector-ref tree node-idx) 0)
          (set-node-length! (vector-ref tree node-idx)
                            (+ (node-length (vector-ref tree (* node-idx 2)))
                               (node-length (vector-ref tree (+ (* node-idx 2) 1))))))))

(define (map-x-to-idx x-val)
  (let loop ((low 0) (high (- (vector-length x-coords-unique) 1)) (ans (vector-length x-coords-unique)))
    (if (<= low high)
        (let* ((mid (+ low (quotient (- high low) 2))))
          (if (>= (vector-ref x-coords-unique mid) x-val)
              (loop low (- mid 1) mid)
              (loop (+ mid 1) high ans)))
        ans)))

(define/contract (separate-squares squares)
  (-> (listof (listof exact-integer?)) flonum?)
  (define x-set (make-hash))
  (define sweep-events (make-list 0))

  (for-each (lambda (s)
              (define x (list-ref s 0))
              (define y (list-ref s 1))
              (define l (list-ref s 2))
              (hash-set! x-set x #t)
              (hash-set! x-set (+ x l) #t)
              (set! sweep-events (cons (sweep-event y x (+ x l) 1) sweep-events))
              (set! sweep-events (cons (sweep-event (+ y l) x (+ x l) -1) sweep-events)))
            squares)

  (set! x-coords-unique (list->vector (sort (hash-keys x-set) <)))
  (set! x-map-size (- (vector-length x-coords-unique) 1))

  (when (= x-map-size 0)
    (define min-y (apply min (map (lambda (s) (list-ref s 1)) squares)))
    (error 'separate-squares "x-map-size is 0, should not happen with l_i >= 1"))

  (set! sweep-events (sort sweep-events (lambda (a b)
                                         (if (= (sweep-event-y a) (sweep-event-y b))
                                             (< (sweep-event-type a) (sweep-event-type b))
                                             (< (sweep-event-y a) (sweep-event-y b))))))

  (set! tree (build-vector (* 4 x-map-size) (lambda (i) (node 0 0))))

  ;; First pass: Calculate total unique area
  (define total-area 0)
  (define prev-y (sweep-event-y (car sweep-events)))

  (for-each (lambda (event)
              (define curr-y (sweep-event-y event))
              (when (> curr-y prev-y)
                (set! total-area (+ total-area (* (node-length (vector-ref tree 1)) (- curr-y prev-y)))))

              (define x-start-idx (map-x-to-idx (sweep-event-x-start event)))
              (define x-end-idx (map-x-to-idx (sweep-event-x-end event)))
              (when (< x-start-idx x-end-idx)
                (update-segment-tree 1 0 x-map-size x-start-idx x-end-idx (sweep-event-type event)))
              (set! prev-y curr-y))
            sweep-events)

  (define target-area (/ (exact->flonum total-area) 2.0))

  ;; Second pass: Find the split y-coordinate
  (set! tree (build-vector (* 4 x-map-size) (lambda (i) (node 0 0))))
  (define current-area-below-line 0.0)
  (set! prev-y (sweep-event-y (car sweep-events)))

  (for-each (lambda (event)
              (define curr-y (sweep-event-y event))
              (when (> curr-y prev-y)
                (define current-width (node-length (vector-ref tree 1)))
                (define area-in-strip (* current-width (- curr-y prev-y)))

                (when (>= (+ current-area-below-line (exact->flonum area-in-strip)) target-area)
                  (define remaining-area-needed (- target-area current-area-below-line))
                  (if (= current-width 0)
                      (error 'separate-squares "current-width is 0 when remaining-area-needed > 0")
                      (begin
                        (set! x-coords-unique #f)
                        (set! tree #f)
                        (set! x-map-size #f)
                        (exit (+ (exact->flonum prev-y) (/ remaining-area-needed (exact->flonum current-width)))))))
                (set! current-area-below-line (+ current-area-below-line (exact->flonum area-in-strip))))

              (define x-start-idx (map-x-to-idx (sweep-event-x-start event)))
              (define x-end-idx (map-x-to-idx (sweep-event-x-end event)))
              (when (< x-start-idx x-end-idx)
                (update-segment-tree 1 0 x-map-size x-start-idx x-end-idx (sweep-event-type event)))
              (set! prev-y curr-y))
            sweep-events)

  (set! x-coords-unique #f)
  (set! tree #f)
  (set! x-map-size #f)
  (exit (exact->flonum prev-y)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-spec separate_squares(Squares :: [[integer()]]) -> float().
separate_squares(Squares) ->
    XSet = sets:new(),
    SweepEvents = [],

    % Collect x-coordinates and create sweep events
    {FinalXSet, RawSweepEvents} = lists:foldl(fun(S, {AccXSet, AccEvents}) ->
        [X, Y, L] = S,
        NewXSet = sets:add_element(X, sets:add_element(X + L, AccXSet)),
        NewEvents = [#{y => Y, x_start => X, x_end => X + L, type => 1} | AccEvents] ++ 
                    [#{y => Y + L, x_start => X, x_end => X + L, type => -1}],
        {NewXSet, NewEvents}
    end, {XSet, SweepEvents}, Squares),

    XCoordsUniqueList = sets:to_list(FinalXSet),
    XCoordsUnique = array:from_list(lists:sort(XCoordsUniqueList)),
    XMapSize = array:size(XCoordsUnique) - 1,

    if XMapSize == 0 ->
        MinY = lists:min([S_i_1 || [_, S_i_1, _] <- Squares]),
        float(MinY);
    true ->
        SortedSweepEvents = lists:sort(fun(A, B) ->
            case A#y of
                B#y -> A#type < B#type;
                _ -> A#y < B#y
            end
        end, RawSweepEvents),

        Tree = array:new(4 * XMapSize, [{default, #{count => 0, length => 0}}]),

        % First pass: Calculate total unique area
        {TotalArea, _FinalTree1, _FinalPrevY1} = lists:foldl(fun(Event, {AccArea, CurrentTree, PrevY}) ->
            CurrY = Event#y,
            NewAccArea = if CurrY > PrevY ->
                RootNode = array:get(1, CurrentTree),
                AccArea + (RootNode#length * (CurrY - PrevY))
            else
                AccArea
            end,

            XStartIdx = map_x_to_idx(Event#x_start, XCoordsUnique),
            XEndIdx = map_x_to_idx(Event#x_end, XCoordsUnique),
            UpdatedTree = if XStartIdx < XEndIdx ->
                update_segment_tree(1, 0, XMapSize, XStartIdx, XEndIdx, Event#type, CurrentTree, XCoordsUnique)
            else
                CurrentTree
            end,
            {NewAccArea, UpdatedTree, CurrY}
        end, {0, Tree, (hd SortedSweepEvents)#y}, SortedSweepEvents),

        TargetArea = TotalArea / 2.0,

        % Second pass: Find the split y-coordinate
        Tree2 = array:new(4 * XMapSize, [{default, #{count => 0, length => 0}}]),
        {_FinalAreaBelow, ResultY, _FinalTree2, _FinalPrevY2} = lists:foldl(fun(Event, {AccAreaBelow, FoundY, CurrentTree, PrevY}) ->
            if FoundY =/= -1.0 -> % If already found, just pass through
                {AccAreaBelow, FoundY, CurrentTree, PrevY}
            else
                CurrY = Event#y,
                {NewAccAreaBelow, NewFoundY} = if CurrY > PrevY ->
                    RootNode = array:get(1, CurrentTree),
                    CurrentWidth = RootNode#length,
                    AreaInStrip = CurrentWidth * (CurrY - PrevY),

                    if AccAreaBelow + AreaInStrip >= TargetArea ->
                        RemainingAreaNeeded = TargetArea - AccAreaBelow,
                        if CurrentWidth == 0 ->
                            float(PrevY)
                        else
                            float(PrevY) + RemainingAreaNeeded / float(CurrentWidth)
                        end
                    else
                        {AccAreaBelow + AreaInStrip, -1.0}
                    end
                else
                    {AccAreaBelow, -1.0}
                end,

                XStartIdx = map_x_to_idx(Event#x_start, XCoordsUnique),
                XEndIdx = map_x_to_idx(Event#x_end, XCoordsUnique),
                UpdatedTree = if XStartIdx < XEndIdx ->
                    update_segment_tree(1, 0, XMapSize, XStartIdx, XEndIdx, Event#type, CurrentTree, XCoordsUnique)
                else
                    CurrentTree
                end,
                {NewAccAreaBelow, NewFoundY, UpdatedTree, CurrY}
            end
        end, {0.0, -1.0, Tree2, (hd SortedSweepEvents)#y}, SortedSweepEvents),

        ResultY
    end.

map_x_to_idx(XVal, XCoordsUnique) ->
    array:foldl(fun(Idx, Val, Acc) ->
        if Val >= XVal ->
            if Idx < Acc -> Idx else Acc end
        else
            Acc
        end
    end, array:size(XCoordsUnique), XCoordsUnique).

update_segment_tree(NodeIdx, NodeRangeStartIdx, NodeRangeEndIdx,
                    QueryStartIdx, QueryEndIdx, Delta, Tree, XCoordsUnique) ->
    if QueryStartIdx >= NodeRangeEndIdx or QueryEndIdx <= NodeRangeStartIdx ->
        Tree;
    true ->
        Node = array:get(NodeIdx, Tree),
        if QueryStartIdx <= NodeRangeStartIdx and NodeRangeEndIdx <= QueryEndIdx ->
            NewNode = Node#{count := Node#count + Delta},
            UpdatedTree = array:set(NodeIdx, NewNode, Tree),
            recalculate_length(NodeIdx, NodeRangeStartIdx, NodeRangeEndIdx, UpdatedTree, XCoordsUnique)
        else
            MidIdx = NodeRangeStartIdx + (NodeRangeEndIdx - NodeRangeStartIdx) div 2,
            Tree1 = update_segment_tree(NodeIdx * 2, NodeRangeStartIdx, MidIdx, QueryStartIdx, QueryEndIdx, Delta, Tree, XCoordsUnique),
            Tree2 = update_segment_tree(NodeIdx * 2 + 1, MidIdx, NodeRangeEndIdx, QueryStartIdx, QueryEndIdx, Delta, Tree1, XCoordsUnique),
            recalculate_length(NodeIdx, NodeRangeStartIdx, NodeRangeEndIdx, Tree2, XCoordsUnique)
        end
    end.

recalculate_length(NodeIdx, NodeRangeStartIdx, NodeRangeEndIdx, Tree, XCoordsUnique) ->
    Node = array:get(NodeIdx, Tree),
    if Node#count > 0 ->
        NewLength = array:get(NodeRangeEndIdx, XCoordsUnique) - array:get(NodeRangeStartIdx, XCoordsUnique),
        array:set(NodeIdx, Node#{length := NewLength}, Tree)
    else
        if NodeRangeStartIdx + 1 == NodeRangeEndIdx ->
            array:set(NodeIdx, Node#{length := 0}, Tree)
        else
            LeftChild = array:get(NodeIdx * 2, Tree),
            RightChild = array:get(NodeIdx * 2 + 1, Tree),
            NewLength = LeftChild#length + RightChild#length,
            array:set(NodeIdx, Node#{length := NewLength}, Tree)
        end
    end.

-record(node, {count = 0, length = 0}).
-record(sweepevent, {y, x_start, x_end, type}).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec separate_squares(squares :: [[integer]]) :: float
  def separate_squares(squares) do
    x_set = MapSet.new()
    sweep_events = []

    for s <- squares do
      [x, y, l] = s
      x_set = MapSet.put(x_set, x)
      x_set = MapSet.put(x_set, x + l)
      sweep_events = [ %{y: y, x_start: x, x_end: x + l, type: 1} | sweep_events ]
      sweep_events = [ %{y: y + l, x_start: x, x_end: x + l, type: -1} | sweep_events ]
    end

    x_coords_unique = x_set |> MapSet.to_list() |> Enum.sort()
    x_map_size = length(x_coords_unique) - 1

    if x_map_size == 0 do
      squares |> Enum.map(fn s -> List.first(tl(s)) end) |> Enum.min() |> Kernel.float()
    else
      sweep_events = Enum.sort(sweep_events, fn a, b ->
        if a.y != b.y do
          a.y < b.y
        else
          a.type < b.type
        end
      end)

      initial_tree = %{}
      for i <- 1..(4 * x_map_size) do
        initial_tree = Map.put(initial_tree, i, %{count: 0, length: 0})
      end

      # First pass: Calculate total unique area
      {total_area, _final_tree, _final_prev_y} = Enum.reduce(sweep_events, {0, initial_tree, List.first(sweep_events).y}, fn event, {acc_area, current_tree, prev_y} ->
        curr_y = event.y
        new_acc_area = if curr_y > prev_y do
          root_node = Map.get(current_tree, 1)
          acc_area + (root_node.length * (curr_y - prev_y))
        else
          acc_area
        end

        x_start_idx = map_x_to_idx(event.x_start, x_coords_unique)
        x_end_idx = map_x_to_idx(event.x_end, x_coords_unique)
        updated_tree = if x_start_idx < x_end_idx do
          update_segment_tree(1, 0, x_map_size, x_start_idx, x_end_idx, event.type, current_tree, x_coords_unique)
        else
          current_tree
        end
        {new_acc_area, updated_tree, curr_y}
      end)

      target_area = Kernel.float(total_area) / 2.0

      # Second pass: Find the split y-coordinate
      initial_tree_2 = %{}
      for i <- 1..(4 * x_map_size) do
        initial_tree_2 = Map.put(initial_tree_2, i, %{count: 0, length: 0})
      end

      {_final_area_below, result_y, _final_tree_2, _final_prev_y_2} = Enum.reduce(sweep_events, {0.0, -1.0, initial_tree_2, List.first(sweep_events).y}, fn event, {acc_area_below, found_y, current_tree, prev_y} ->
        if found_y != -1.0 do
          {acc_area_below, found_y, current_tree, prev_y}
        else
          curr_y = event.y
          {new_acc_area_below, new_found_y} = if curr_y > prev_y do
            root_node = Map.get(current_tree, 1)
            current_width = root_node.length
            area_in_strip = current_width * (curr_y - prev_y)

            if acc_area_below + Kernel.float(area_in_strip) >= target_area do
              remaining_area_needed = target_area - acc_area_below
              if current_width == 0 do
                Kernel.float(prev_y)
              else
                Kernel.float(prev_y) + remaining_area_needed / Kernel.float(current_width)
              end
            else
              {acc_area_below + Kernel.float(area_in_strip), -1.0}
            end
          else
            {acc_area_below, -1.0}
          end

          x_start_idx = map_x_to_idx(event.x_start, x_coords_unique)
          x_end_idx = map_x_to_idx(event.x_end, x_coords_unique)
          updated_tree = if x_start_idx < x_end_idx do
            update_segment_tree(1, 0, x_map_size, x_start_idx, x_end_idx, event.type, current_tree, x_coords_unique)
          else
            current_tree
          end
          {new_acc_area_below, new_found_y, updated_tree, curr_y}
        end
      end)
      result_y
    end
  end

  defp update_segment_tree(node_idx, node_range_start_idx, node_range_end_idx,
                           query_start_idx, query_end_idx, delta, tree, x_coords_unique) do
    if query_start_idx >= node_range_end_idx or query_end_idx <= node_range_start_idx do
      tree
    else
      node = Map.get(tree, node_idx)
      if query_start_idx <= node_range_start_idx and node_range_end_idx <= query_end_idx do
        new_node = %{node | count: node.count + delta}
        updated_tree = Map.put(tree, node_idx, new_node)
        recalculate_length(node_idx, node_range_start_idx, node_range_end_idx, updated_tree, x_coords_unique)
      else
        mid_idx = node_range_start_idx + div(node_range_end_idx - node_range_start_idx, 2)
        tree1 = update_segment_tree(node_idx * 2, node_range_start_idx, mid_idx, query_start_idx, query_end_idx, delta, tree, x_coords_unique)
        tree2 = update_segment_tree(node_idx * 2 + 1, mid_idx, node_range_end_idx, query_start_idx, query_end_idx, delta, tree1, x_coords_unique)
        recalculate_length(node_idx, node_range_start_idx, node_range_end_idx, tree2, x_coords_unique)
      end
    end
  end

  defp recalculate_length(node_idx, node_range_start_idx, node_range_end_idx, tree, x_coords_unique) do
    node = Map.get(tree, node_idx)
    if node.count > 0 do
      new_length = Enum.at(x_coords_unique, node_range_end_idx) - Enum.at(x_coords_unique, node_range_start_idx)
      Map.put(tree, node_idx, %{node | length: new_length})
    else
      if node_range_start_idx + 1 == node_range_end_idx do
        Map.put(tree, node_idx, %{node | length: 0})
      else
        left_child = Map.get(tree, node_idx * 2)
        right_child = Map.get(tree, node_idx * 2 + 1)
        new_length = left_child.length + right_child.length
        Map.put(tree, node_idx, %{node | length: new_length})
      end
    end
  end

  defp map_x_to_idx(x_val, x_coords_unique) do
    Enum.find_index(x_coords_unique, fn x -> x >= x_val end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is dominated by the binary search and the `calculate_unique_area` function. The `calculate_unique_area` function involves sorting events (O(N log N)) and performing segment tree updates (N events, each O(log M), where M is the number of unique y-coordinates, M <= 2N). Thus, `calculate_unique_area` takes O(N log N) time. The binary search performs K iterations (e.g., 100). In each iteration, it constructs a new set of clipped rectangles (O(N)) and calls `calculate_unique_area` (O(N log N)). Therefore, the total time complexity is O(N log N + K * N log N), which simplifies to O(K * N log N).

- **Space Complexity:** The space complexity is primarily determined by storing the events, the unique y-coordinates, and the segment tree. The events list stores up to 2N entries. The `y_coords` list stores up to 2N unique y-coordinates. The segment tree requires O(M) space, where M is the number of unique y-coordinates, so O(N) space. Overall, the space complexity is O(N).

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2026-01-14 01:18:14 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved by using a line sweep and a segment tree. The idea is to find the minimum y-coordinate value of a horizontal line such that the total area covered by squares above the line equals the total area covered by squares below the line. We can start by sorting the squares based on their y-coordinates and then iterate over the sorted squares to find the minimum y-coordinate value that satisfies the condition. We can use a segment tree to keep track of the total area covered by squares above and below the line.

The key intuition behind this approach is that the line must lie in one of the squares. Therefore, we can start by finding the y-coordinate of the bottom-left point of each square and then iterate over the sorted y-coordinates to find the minimum y-coordinate value that satisfies the condition. We can use a binary search approach to find the minimum y-coordinate value in O(log n) time complexity, where n is the number of squares. This approach ensures that we find the minimum y-coordinate value that satisfies the condition in an efficient manner.

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
        sort(squares.begin(), squares.end(), [](vector<int>& a, vector<int>& b) { return a[1] < b[1]; });
        double low = squares[0][1], high = squares[squares.size() - 1][1] + squares[squares.size() - 1][2];
        while (high - low > 1e-5) {
            double mid = (low + high) / 2;
            double areaAbove = 0, areaBelow = 0;
            set<int> counted;
            for (auto& square : squares) {
                if (square[1] + square[2] > mid) {
                    double overlap = max(0.0, min(square[1] + square[2], mid) - max(square[1], mid));
                    areaAbove += overlap * square[2];
                }
                if (square[1] < mid) {
                    double overlap = max(0.0, min(square[1] + square[2], mid) - max(square[1], mid));
                    areaBelow += overlap * square[2];
                }
            }
            if (areaAbove > areaBelow) high = mid;
            else low = mid;
        }
        return low;
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
        Arrays.sort(squares, (a, b) -> a[1] - b[1]);
        double low = squares[0][1], high = squares[squares.length - 1][1] + squares[squares.length - 1][2];
        while (high - low > 1e-5) {
            double mid = (low + high) / 2;
            double areaAbove = 0, areaBelow = 0;
            HashSet<Integer> counted = new HashSet<>();
            for (int[] square : squares) {
                if (square[1] + square[2] > mid) {
                    double overlap = Math.max(0.0, Math.min(square[1] + square[2], mid) - Math.max(square[1], mid));
                    areaAbove += overlap * square[2];
                }
                if (square[1] < mid) {
                    double overlap = Math.max(0.0, Math.min(square[1] + square[2], mid) - Math.max(square[1], mid));
                    areaBelow += overlap * square[2];
                }
            }
            if (areaAbove > areaBelow) high = mid;
            else low = mid;
        }
        return low;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        squares.sort(key=lambda x: x[1])
        low, high = squares[0][1], squares[-1][1] + squares[-1][2]
        while high - low > 1e-5:
            mid = (low + high) / 2
            areaAbove, areaBelow = 0, 0
            counted = set()
            for square in squares:
                if square[1] + square[2] > mid:
                    overlap = max(0, min(square[1] + square[2], mid) - max(square[1], mid))
                    areaAbove += overlap * square[2]
                if square[1] < mid:
                    overlap = max(0, min(square[1] + square[2], mid) - max(square[1], mid))
                    areaBelow += overlap * square[2]
            if areaAbove > areaBelow: high = mid
            else: low = mid
        return low
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        squares.sort(key=lambda x: x[1])
        low, high = squares[0][1], squares[-1][1] + squares[-1][2]
        while high - low > 1e-5:
            mid = (low + high) / 2
            areaAbove, areaBelow = 0, 0
            counted = set()
            for square in squares:
                if square[1] + square[2] > mid:
                    overlap = max(0, min(square[1] + square[2], mid) - max(square[1], mid))
                    areaAbove += overlap * square[2]
                if square[1] < mid:
                    overlap = max(0, min(square[1] + square[2], mid) - max(square[1], mid))
                    areaBelow += overlap * square[2]
            if areaAbove > areaBelow: high = mid
            else: low = mid
        return low
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
double separateSquares(int** squares, int squaresSize, int* squaresColSize) {
    qsort(squares, squaresSize, sizeof(int*), compare);
    double low = squares[0][1], high = squares[squaresSize - 1][1] + squares[squaresSize - 1][2];
    while (high - low > 1e-5) {
        double mid = (low + high) / 2;
        double areaAbove = 0, areaBelow = 0;
        int* counted = (int*)malloc(squaresSize * sizeof(int));
        for (int i = 0; i < squaresSize; i++) {
            if (squares[i][1] + squares[i][2] > mid) {
                double overlap = fmax(0.0, fmin(squares[i][1] + squares[i][2], mid) - fmax(squares[i][1], mid));
                areaAbove += overlap * squares[i][2];
            }
            if (squares[i][1] < mid) {
                double overlap = fmax(0.0, fmin(squares[i][1] + squares[i][2], mid) - fmax(squares[i][1], mid));
                areaBelow += overlap * squares[i][2];
            }
        }
        if (areaAbove > areaBelow) high = mid;
        else low = mid;
    }
    return low;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public double SeparateSquares(int[][] squares) {
        Array.Sort(squares, (a, b) => a[1].CompareTo(b[1]));
        double low = squares[0][1], high = squares[squares.Length - 1][1] + squares[squares.Length - 1][2];
        while (high - low > 1e-5) {
            double mid = (low + high) / 2;
            double areaAbove = 0, areaBelow = 0;
            HashSet<int> counted = new HashSet<int>();
            for (int i = 0; i < squares.Length; i++) {
                if (squares[i][1] + squares[i][2] > mid) {
                    double overlap = Math.Max(0.0, Math.Min(squares[i][1] + squares[i][2], mid) - Math.Max(squares[i][1], mid));
                    areaAbove += overlap * squares[i][2];
                }
                if (squares[i][1] < mid) {
                    double overlap = Math.Max(0.0, Math.Min(squares[i][1] + squares[i][2], mid) - Math.Max(squares[i][1], mid));
                    areaBelow += overlap * squares[i][2];
                }
            }
            if (areaAbove > areaBelow) high = mid;
            else low = mid;
        }
        return low;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var separateSquares = function(squares) {
    squares.sort((a, b) => a[1] - b[1]);
    let low = squares[0][1], high = squares[squares.length - 1][1] + squares[squares.length - 1][2];
    while (high - low > 1e-5) {
        let mid = (low + high) / 2;
        let areaAbove = 0, areaBelow = 0;
        let counted = new Set();
        for (let i = 0; i < squares.length; i++) {
            if (squares[i][1] + squares[i][2] > mid) {
                let overlap = Math.max(0, Math.min(squares[i][1] + squares[i][2], mid) - Math.max(squares[i][1], mid));
                areaAbove += overlap * squares[i][2];
            }
            if (squares[i][1] < mid) {
                let overlap = Math.max(0, Math.min(squares[i][1] + squares[i][2], mid) - Math.max(squares[i][1], mid));
                areaBelow += overlap * squares[i][2];
            }
        }
        if (areaAbove > areaBelow) high = mid;
        else low = mid;
    }
    return low;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function separateSquares(squares: number[][]): number {
    squares.sort((a, b) => a[1] - b[1]);
    let low: number = squares[0][1], high: number = squares[squares.length - 1][1] + squares[squares.length - 1][2];
    while (high - low > 1e-5) {
        let mid: number = (low + high) / 2;
        let areaAbove: number = 0, areaBelow: number = 0;
        let counted: Set<number> = new Set();
        for (let i: number = 0; i < squares.length; i++) {
            if (squares[i][1] + squares[i][2] > mid) {
                let overlap: number = Math.max(0, Math.min(squares[i][1] + squares[i][2], mid) - Math.max(squares[i][1], mid));
                areaAbove += overlap * squares[i][2];
            }
            if (squares[i][1] < mid) {
                let overlap: number = Math.max(0, Math.min(squares[i][1] + squares[i][2], mid) - Math.max(squares[i][1], mid));
                areaBelow += overlap * squares[i][2];
            }
        }
        if (areaAbove > areaBelow) high = mid;
        else low = mid;
    }
    return low;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function separateSquares($squares) {
        usort($squares, function($a, $b) { return $a[1] - $b[1]; });
        $low = $squares[0][1];
        $high = $squares[count($squares) - 1][1] + $squares[count($squares) - 1][2];
        while ($high - $low > 1e-5) {
            $mid = ($low + $high) / 2;
            $areaAbove = 0;
            $areaBelow = 0;
            $counted = array();
            for ($i = 0; $i < count($squares); $i++) {
                if ($squares[$i][1] + $squares[$i][2] > $mid) {
                    $overlap = max(0, min($squares[$i][1] + $squares[$i][2], $mid) - max($squares[$i][1], $mid));
                    $areaAbove += $overlap * $squares[$i][2];
                }
                if ($squares[$i][1] < $mid) {
                    $overlap = max(0, min($squares[$i][1] + $squares[$i][2], $mid) - max($squares[$i][1], $mid));
                    $areaBelow += $overlap * $squares[$i][2];
                }
            }
            if ($areaAbove > $areaBelow) $high = $mid;
            else $low = $mid;
        }
        return $low;
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
        let sortedSquares = squares.sorted { $0[1] < $1[1] }
        var low: Double = Double(sortedSquares[0][1])
        var high: Double = Double(sortedSquares[sortedSquares.count - 1][1] + sortedSquares[sortedSquares.count - 1][2])
        while high - low > 1e-5 {
            let mid = (low + high) / 2
            var areaAbove: Double = 0
            var areaBelow: Double = 0
            var counted: Set<Int> = Set()
            for i in 0..<sortedSquares.count {
                if Double(sortedSquares[i][1] + sortedSquares[i][2]) > mid {
                    let overlap = max(0, min(Double(sortedSquares[i][1] + sortedSquares[i][2]), mid) - max(Double(sortedSquares[i][1]), mid))
                    areaAbove += overlap * Double(sortedSquares[i][2])
                }
                if Double(sortedSquares[i][1]) < mid {
                    let overlap = max(0, min(Double(sortedSquares[i][1] + sortedSquares[i][2]), mid) - max(Double(sortedSquares[i][1]), mid))
                    areaBelow += overlap * Double(sortedSquares[i][2])
                }
            }
            if areaAbove > areaBelow {
                high = mid
            } else {
                low = mid
            }
        }
        return low
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
        val events = mutableListOf<Triple<Double, Int, Int>>()
        for (square in squares) {
            val x = square[0].toDouble()
            val y = square[1].toDouble()
            val length = square[2].toDouble()
            events.add(Triple(y, 1, length))
            events.add(Triple(y + length, -1, length))
        }
        events.sortBy { it.first }
        var areaAbove = 0.0
        var areaBelow = 0.0
        var y = 0.0
        for (event in events) {
            if (areaAbove == areaBelow) {
                y = event.first
            }
            areaAbove += event.second * event.third
            areaBelow -= event.second * event.third
        }
        return y
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
    List<Triple<double, int, int>> events = [];
    for (var square in squares) {
      double x = square[0].toDouble();
      double y = square[1].toDouble();
      double length = square[2].toDouble();
      events.add(Triple(y, 1, length));
      events.add(Triple(y + length, -1, length));
    }
    events.sort((a, b) => a.first.compareTo(b.first));
    double areaAbove = 0;
    double areaBelow = 0;
    double y = 0;
    for (var event in events) {
      if (areaAbove == areaBelow) {
        y = event.first;
      }
      areaAbove += event.second * event.third;
      areaBelow -= event.second * event.third;
    }
    return y;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func separateSquares(squares [][]int) float64 {
    events := make([]struct{ y, delta, length float64 }, 0)
    for _, square := range squares {
        x := float64(square[0])
        y := float64(square[1])
        length := float64(square[2])
        events = append(events, struct{ y, delta, length float64 }{y, 1, length})
        events = append(events, struct{ y, delta, length float64 }{y + length, -1, length})
    }
    sort.Slice(events, func(i, j int) bool { return events[i].y < events[j].y })
    areaAbove := 0.0
    areaBelow := 0.0
    y := 0.0
    for _, event := range events {
        if areaAbove == areaBelow {
            y = event.y
        }
        areaAbove += event.delta * event.length
        areaBelow -= event.delta * event.length
    }
    return y
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def separate_squares(squares)
    events = []
    squares.each do |square|
        x = square[0].to_f
        y = square[1].to_f
        length = square[2].to_f
        events << [y, 1, length]
        events << [y + length, -1, length]
    end
    events.sort_by! { |event| event[0] }
    area_above = 0
    area_below = 0
    y = 0
    events.each do |event|
        if area_above == area_below
            y = event[0]
        end
        area_above += event[1] * event[2]
        area_below -= event[1] * event[2]
    end
    y
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def separateSquares(squares: Array[Array[Int]]): Double = {
        val events = scala.collection.mutable.ListBuffer[(Double, Int, Int)]()
        for (square <- squares) {
            val x = square(0).toDouble
            val y = square(1).toDouble
            val length = square(2).toDouble
            events += ((y, 1, length.toInt))
            events += ((y + length, -1, length.toInt))
        }
        val sortedEvents = events.sortBy(_._1)
        var areaAbove = 0.0
        var areaBelow = 0.0
        var y = 0.0
        for (event <- sortedEvents) {
            if (areaAbove == areaBelow) {
                y = event._1
            }
            areaAbove += event._2 * event._3
            areaBelow -= event._2 * event._3
        }
        y
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
        let mut events: Vec<(f64, i32, i32)> = Vec::new();
        for square in squares {
            let x = square[0] as f64;
            let y = square[1] as f64;
            let length = square[2] as f64;
            events.push((y, 1, length as i32));
            events.push((y + length, -1, length as i32));
        }
        events.sort_by(|a, b| a.0.partial_cmp(&b.0).unwrap());
        let mut area_above = 0.0;
        let mut area_below = 0.0;
        let mut y = 0.0;
        for event in events {
            if area_above == area_below {
                y = event.0;
            }
            area_above += event.1 as f64 * event.2 as f64;
            area_below -= event.1 as f64 * event.2 as f64;
        }
        y
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
  (let* (
         (events (for/list (
                         (square squares))
                     (let (
                            (x (first square))
                            (y (second square))
                            (length (third square)))
                       (list (list y 1 length)
                             (list (+ y length) -1 length)))))
         (sorted-events (sort events (lambda (a b) (< (first a) (first b)))))
         (area-above 0)
         (area-below 0)
         (y 0))
    (for (
         (event sorted-events))
      (if (= area-above area-below)
          (set! y (first event)))
      (set! area-above (+ area-above (* (second event) (third event))))
      (set! area-below (- area-below (* (second event) (third event))))))
    y))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
separate_squares(Squares) ->
    Events = [
        begin
            [Y, 1, Length],
            [Y + Length, -1, Length]
        end
        || [X, Y, Length] <- Squares
    ],
    SortedEvents = lists:sort(Events),
    separate_squares(SortedEvents, 0, 0, 0).

separate_squares([], AreaAbove, AreaBelow, Y) ->
    Y;
separate_squares([Event | Events], AreaAbove, AreaBelow, Y) ->
    [Y1, Delta, Length] = Event,
    NewAreaAbove = AreaAbove + Delta * Length,
    NewAreaBelow = AreaBelow - Delta * Length,
    if
        AreaAbove == AreaBelow ->
            separate_squares(Events, NewAreaAbove, NewAreaBelow, Y1);
        true ->
            separate_squares(Events, NewAreaAbove, NewAreaBelow, Y)
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
    events =
      Enum.flat_map(squares, fn [x, y, length] ->
        [[y, 1, length], [y + length, -1, length]]
      end)
      |> Enum.sort_by(&(&1 |> hd))
    area_above = 0
    area_below = 0
    y = 0
    Enum.reduce(events, {area_above, area_below, y}, fn [y1, delta, length], {area_above, area_below, y} ->
      if area_above == area_below do
        {area_above + delta * length, area_below - delta * length, y1}
      else
        {area_above + delta * length, area_below - delta * length, y}
      end
    end)
    |> elem(2)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of the solution is O(n log n) due to the sorting of the squares based on their y-coordinates. The iteration over the sorted squares and the binary search approach take O(n log n) time complexity. The space complexity is O(n) due to the use of a segment tree to keep track of the total area covered by squares above and below the line.

- **Space Complexity:** The space complexity of the solution is O(n) due to the use of a segment tree to keep track of the total area covered by squares above and below the line. The segment tree requires O(n) space to store the total area covered by squares above and below the line. The sorting of the squares based on their y-coordinates also requires O(n) space. Therefore, the overall space complexity of the solution is O(n).

</div>
</details>
