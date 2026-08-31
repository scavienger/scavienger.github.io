---
layout: post
title: "Find the Minimum and Maximum Number of Nodes Between Critical Points"
date: 2026-08-31 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Linked List"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/
ai_solutions:
  - solutions:
      cpp: "/**\n * Definition for singly-linked list.\n * struct ListNode {\n *   \
        \  int val;\n *     ListNode *next;\n *     ListNode() : val(0), next(nullptr)\
        \ {}\n *     ListNode(int x) : val(x), next(nullptr) {}\n *     ListNode(int\
        \ x, ListNode *next) : val(x), next(next) {}\n * };\n */\nclass Solution {\n\
        public:\n    vector<int> nodesBetweenCriticalPoints(ListNode* head) {\n    \
        \    if (!head || !head->next || !head->next->next) return {-1, -1};\n\n   \
        \     int firstIdx = -1, lastIdx = -1, minDist = INT_MAX;\n        ListNode*\
        \ prev = head;\n        ListNode* curr = head->next;\n        int idx = 1;\n\
        \n        while (curr->next) {\n            if ((curr->val > prev->val && curr->val\
        \ > curr->next->val) || \n                (curr->val < prev->val && curr->val\
        \ < curr->next->val)) {\n                if (firstIdx == -1) {\n           \
        \         firstIdx = idx;\n                } else {\n                    minDist\
        \ = min(minDist, idx - lastIdx);\n                }\n                lastIdx\
        \ = idx;\n            }\n            prev = curr;\n            curr = curr->next;\n\
        \            idx++;\n        }\n\n        if (firstIdx == lastIdx) return {-1,\
        \ -1};\n        return {minDist, lastIdx - firstIdx};\n    }\n};"
      java: "/**\n * Definition for singly-linked list.\n * public class ListNode {\n\
        \ *     int val;\n *     ListNode next;\n *     ListNode() {}\n *     ListNode(int\
        \ val) { this.val = val; }\n *     ListNode(int val, ListNode next) { this.val\
        \ = val; this.next = next; }\n * }\n */\nclass Solution {\n    public int[]\
        \ nodesBetweenCriticalPoints(ListNode head) {\n        if (head == null || head.next\
        \ == null || head.next.next == null) return new int[]{-1, -1};\n\n        int\
        \ firstIdx = -1, lastIdx = -1, minDist = Integer.MAX_VALUE;\n        ListNode\
        \ prev = head;\n        ListNode curr = head.next;\n        int idx = 1;\n\n\
        \        while (curr.next != null) {\n            if ((curr.val > prev.val &&\
        \ curr.val > curr.next.val) || \n                (curr.val < prev.val && curr.val\
        \ < curr.next.val)) {\n                if (firstIdx == -1) {\n             \
        \       firstIdx = idx;\n                } else {\n                    minDist\
        \ = Math.min(minDist, idx - lastIdx);\n                }\n                lastIdx\
        \ = idx;\n            }\n            prev = curr;\n            curr = curr.next;\n\
        \            idx++;\n        }\n\n        if (firstIdx == lastIdx) return new\
        \ int[]{-1, -1};\n        return new int[]{minDist, lastIdx - firstIdx};\n \
        \   }\n}"
      python: "# Definition for singly-linked list.\n# class ListNode(object):\n#  \
        \   def __init__(self, val=0, next=None):\n#         self.val = val\n#     \
        \    self.next = next\nclass Solution(object):\n    def nodesBetweenCriticalPoints(self,\
        \ head):\n        \"\"\"\n        :type head: Optional[ListNode]\n        :rtype:\
        \ List[int]\n        \"\"\"\n        if not head or not head.next or not head.next.next:\n\
        \            return [-1, -1]\n\n        first_idx = -1\n        last_idx = -1\n\
        \        min_dist = float('inf')\n\n        prev = head\n        curr = head.next\n\
        \        idx = 1\n\n        while curr.next:\n            if (curr.val > prev.val\
        \ and curr.val > curr.next.val) or \\\n               (curr.val < prev.val and\
        \ curr.val < curr.next.val):\n                if first_idx == -1:\n        \
        \            first_idx = idx\n                else:\n                    min_dist\
        \ = min(min_dist, idx - last_idx)\n                last_idx = idx\n        \
        \    prev = curr\n            curr = curr.next\n            idx += 1\n\n   \
        \     if first_idx == last_idx:\n            return [-1, -1]\n\n        return\
        \ [min_dist, last_idx - first_idx]"
      python3: "# Definition for singly-linked list.\n# class ListNode:\n#     def __init__(self,\
        \ val=0, next=None):\n#         self.val = val\n#         self.next = next\n\
        class Solution:\n    def nodesBetweenCriticalPoints(self, head: Optional[ListNode])\
        \ -> List[int]:\n        if not head or not head.next or not head.next.next:\n\
        \            return [-1, -1]\n\n        first_idx = -1\n        last_idx = -1\n\
        \        min_dist = float('inf')\n\n        prev = head\n        curr = head.next\n\
        \        idx = 1\n\n        while curr.next:\n            if (curr.val > prev.val\
        \ and curr.val > curr.next.val) or \\\n               (curr.val < prev.val and\
        \ curr.val < curr.next.val):\n                if first_idx == -1:\n        \
        \            first_idx = idx\n                else:\n                    min_dist\
        \ = min(min_dist, idx - last_idx)\n                last_idx = idx\n        \
        \    prev = curr\n            curr = curr.next\n            idx += 1\n\n   \
        \     if first_idx == last_idx:\n            return [-1, -1]\n\n        return\
        \ [int(min_dist), last_idx - first_idx]"
      c: "/**\n * Definition for singly-linked list.\n * struct ListNode {\n *     int\
        \ val;\n *     struct ListNode *next;\n * };\n */\n/**\n * Note: The returned\
        \ array must be malloced, assume caller calls free().\n */\nint* nodesBetweenCriticalPoints(struct\
        \ ListNode* head, int* returnSize) {\n    *returnSize = 2;\n    int* result\
        \ = (int*)malloc(2 * sizeof(int));\n    result[0] = -1;\n    result[1] = -1;\n\
        \n    if (!head || !head->next || !head->next->next) {\n        return result;\n\
        \    }\n\n    int firstIdx = -1, lastIdx = -1, minDist = 1000000000;\n    struct\
        \ ListNode* prev = head;\n    struct ListNode* curr = head->next;\n    int idx\
        \ = 1;\n\n    while (curr->next) {\n        if ((curr->val > prev->val && curr->val\
        \ > curr->next->val) || \n            (curr->val < prev->val && curr->val <\
        \ curr->next->val)) {\n            if (firstIdx == -1) {\n                firstIdx\
        \ = idx;\n            } else {\n                int diff = idx - lastIdx;\n\
        \                if (diff < minDist) minDist = diff;\n            }\n      \
        \      lastIdx = idx;\n        }\n        prev = curr;\n        curr = curr->next;\n\
        \        idx++;\n    }\n\n    if (firstIdx != -1 && lastIdx != -1 && firstIdx\
        \ != lastIdx) {\n        result[0] = minDist;\n        result[1] = lastIdx -\
        \ firstIdx;\n    }\n\n    return result;\n}"
      csharp: "/**\n * Definition for singly-linked list.\n * public class ListNode\
        \ {\n *     public int val;\n *     public ListNode next;\n *     public ListNode(int\
        \ val=0, ListNode next=null) {\n *         this.val = val;\n *         this.next\
        \ = next;\n *     }\n * }\n */\npublic class Solution {\n    public int[] NodesBetweenCriticalPoints(ListNode\
        \ head) {\n        if (head == null || head.next == null || head.next.next ==\
        \ null) {\n            return new int[] { -1, -1 };\n        }\n\n        int\
        \ firstCP = -1;\n        int lastCP = -1;\n        int minDist = int.MaxValue;\n\
        \        int currentIndex = 1;\n\n        ListNode prev = head;\n        ListNode\
        \ curr = head.next;\n\n        while (curr.next != null) {\n            ListNode\
        \ next = curr.next;\n            bool isCP = (curr.val > prev.val && curr.val\
        \ > next.val) ||\n                        (curr.val < prev.val && curr.val <\
        \ next.val);\n\n            if (isCP) {\n                if (firstCP == -1)\
        \ {\n                    firstCP = currentIndex;\n                } else {\n\
        \                    int diff = currentIndex - lastCP;\n                   \
        \ if (diff < minDist) {\n                        minDist = diff;\n         \
        \           }\n                }\n                lastCP = currentIndex;\n \
        \           }\n\n            prev = curr;\n            curr = next;\n      \
        \      currentIndex++;\n        }\n\n        if (firstCP == lastCP) {\n    \
        \        return new int[] { -1, -1 };\n        }\n\n        return new int[]\
        \ { minDist, lastCP - firstCP };\n    }\n}"
      javascript: "/**\n * Definition for singly-linked list.\n * function ListNode(val,\
        \ next) {\n *     this.val = (val===undefined ? 0 : val)\n *     this.next =\
        \ (next===undefined ? null : next)\n * }\n */\n/**\n * @param {ListNode} head\n\
        \ * @return {number[]}\n */\nvar nodesBetweenCriticalPoints = function(head)\
        \ {\n    if (!head || !head.next || !head.next.next) return [-1, -1];\n\n  \
        \  let firstCP = -1;\n    let lastCP = -1;\n    let minDist = Infinity;\n  \
        \  let currentIndex = 1;\n\n    let prev = head;\n    let curr = head.next;\n\
        \n    while (curr.next) {\n        let next = curr.next;\n        let isCP =\
        \ (curr.val > prev.val && curr.val > next.val) ||\n                   (curr.val\
        \ < prev.val && curr.val < next.val);\n\n        if (isCP) {\n            if\
        \ (firstCP === -1) {\n                firstCP = currentIndex;\n            }\
        \ else {\n                minDist = Math.min(minDist, currentIndex - lastCP);\n\
        \            }\n            lastCP = currentIndex;\n        }\n\n        prev\
        \ = curr;\n        curr = next;\n        currentIndex++;\n    }\n\n    if (firstCP\
        \ === lastCP) return [-1, -1];\n\n    return [minDist, lastCP - firstCP];\n\
        };"
      typescript: "/**\n * Definition for singly-linked list.\n * class ListNode {\n\
        \ *     val: number\n *     next: ListNode | null\n *     constructor(val?:\
        \ number, next?: ListNode | null) {\n *         this.val = (val===undefined\
        \ ? 0 : val)\n *         this.next = (next===undefined ? null : next)\n *  \
        \   } \n * }\n */\n\nfunction nodesBetweenCriticalPoints(head: ListNode | null):\
        \ number[] {\n    if (!head || !head.next || !head.next.next) {\n        return\
        \ [-1, -1];\n    }\n\n    let firstCP: number = -1;\n    let lastCP: number\
        \ = -1;\n    let minDist: number = Infinity;\n    let currentIndex: number =\
        \ 1;\n\n    let prev: ListNode = head;\n    let curr: ListNode = head.next;\n\
        \n    while (curr.next !== null) {\n        let next: ListNode = curr.next;\n\
        \        let isCP: boolean = (curr.val > prev.val && curr.val > next.val) ||\n\
        \                            (curr.val < prev.val && curr.val < next.val);\n\
        \n        if (isCP) {\n            if (firstCP === -1) {\n                firstCP\
        \ = currentIndex;\n            } else {\n                minDist = Math.min(minDist,\
        \ currentIndex - lastCP);\n            }\n            lastCP = currentIndex;\n\
        \        }\n\n        prev = curr;\n        curr = next;\n        currentIndex++;\n\
        \    }\n\n    if (firstCP === lastCP) {\n        return [-1, -1];\n    }\n\n\
        \    return [minDist, lastCP - firstCP];\n};"
      php: "/**\n * Definition for a singly-linked list.\n * class ListNode {\n *  \
        \   public $val = 0;\n *     public $next = null;\n *     function __construct($val\
        \ = 0, $next = null) {\n *         this.val = $val;\n *         this.next =\
        \ $next;\n *     }\n * }\n */\nclass Solution {\n\n    /**\n     * @param ListNode\
        \ $head\n     * @return Integer[]\n     */\n    function nodesBetweenCriticalPoints($head)\
        \ {\n        if ($head === null || $head->next === null || $head->next->next\
        \ === null) {\n            return [-1, -1];\n        }\n\n        $firstCP =\
        \ -1;\n        $lastCP = -1;\n        $minDist = PHP_INT_MAX;\n        $currentIndex\
        \ = 1;\n\n        $prev = $head;\n        $curr = $head->next;\n\n        while\
        \ ($curr->next !== null) {\n            $next = $curr->next;\n            $isCP\
        \ = ($curr->val > $prev->val && $curr->val > $next->val) ||\n              \
        \      ($curr->val < $prev->val && $curr->val < $next->val);\n\n           \
        \ if ($isCP) {\n                if ($firstCP === -1) {\n                   \
        \ $firstCP = $currentIndex;\n                } else {\n                    $minDist\
        \ = min($minDist, $currentIndex - $lastCP);\n                }\n           \
        \     $lastCP = $currentIndex;\n            }\n\n            $prev = $curr;\n\
        \            $curr = $next;\n            $currentIndex++;\n        }\n\n   \
        \     if ($firstCP === $lastCP) {\n            return [-1, -1];\n        }\n\
        \n        return [$minDist, $lastCP - $firstCP];\n    }\n}"
      swift: "/**\n * Definition for singly-linked list.\n * public class ListNode {\n\
        \ *     public var val: Int\n *     public var next: ListNode?\n *     public\
        \ init() { self.val = 0; self.next = nil; }\n *     public init(_ val: Int)\
        \ { self.val = val; self.next = nil; }\n *     public init(_ val: Int, _ next:\
        \ ListNode?) { self.val = val; self.next = next; }\n * }\n */\nclass Solution\
        \ {\n    func nodesBetweenCriticalPoints(_ head: ListNode?) -> [Int] {\n   \
        \     guard let head = head, let nextNode = head.next, let nextNextNode = nextNode.next\
        \ else {\n            return [-1, -1]\n        }\n\n        var firstCP = -1\n\
        \        var lastCP = -1\n        var minDist = Int.max\n        var currentIndex\
        \ = 1\n\n        var prev = head\n        var curr = nextNode\n\n        while\
        \ let next = curr.next {\n            let isCP = (curr.val > prev.val && curr.val\
        \ > next.val) ||\n                       (curr.val < prev.val && curr.val <\
        \ next.val)\n\n            if isCP {\n                if firstCP == -1 {\n \
        \                   firstCP = currentIndex\n                } else {\n     \
        \               minDist = min(minDist, currentIndex - lastCP)\n            \
        \    }\n                lastCP = currentIndex\n            }\n\n           \
        \ prev = curr\n            curr = next\n            currentIndex += 1\n    \
        \    }\n\n        if firstCP == lastCP {\n            return [-1, -1]\n    \
        \    }\n\n        return [minDist, lastCP - firstCP]\n    }\n}"
      kotlin: "/**\n * Example:\n * var li = ListNode(5)\n * var v = li.`val`\n * Definition\
        \ for singly-linked list.\n * class ListNode(var `val`: Int) {\n *     var next:\
        \ ListNode? = null\n * }\n */\nclass Solution {\n    fun nodesBetweenCriticalPoints(head:\
        \ ListNode?): IntArray {\n        if (head?.next?.next == null) return intArrayOf(-1,\
        \ -1)\n\n        var firstCPIndex = -1\n        var prevCPIndex = -1\n     \
        \   var minDistance = Int.MAX_VALUE\n        var currIndex = 1\n        var\
        \ prevNode = head\n        var currNode = head.next\n\n        while (currNode?.next\
        \ != null) {\n            val nextNode = currNode.next!!\n            if ((currNode.`val`\
        \ > prevNode!!.`val` && currNode.`val` > nextNode.`val`) ||\n              \
        \  (currNode.`val` < prevNode.`val` && currNode.`val` < nextNode.`val\")) {\n\
        \n                if (firstCPIndex == -1) {\n                    firstCPIndex\
        \ = currIndex\n                } else {\n                    val dist = currIndex\
        \ - prevCPIndex\n                    if (dist < minDistance) {\n           \
        \             minDistance = dist\n                    }\n                }\n\
        \                prevCPIndex = currIndex\n            }\n            prevNode\
        \ = currNode\n            currNode = nextNode\n            currIndex++\n   \
        \     }\n\n        if (minDistance == Int.MAX_VALUE) {\n            return intArrayOf(-1,\
        \ -1)\n        }\n\n        val maxDistance = prevCPIndex - firstCPIndex\n \
        \       return intArrayOf(minDistance, maxDistance)\n    }\n}"
      dart: "/**\n * Definition for singly-linked list.\n * class ListNode {\n *   int\
        \ val;\n *   ListNode? next;\n *   ListNode([this.val = 0, this.next]);\n *\
        \ }\n */\nclass Solution {\n  List<int> nodesBetweenCriticalPoints(ListNode?\
        \ head) {\n    if (head == null || head.next == null || head.next!.next == null)\
        \ {\n      return [-1, -1];\n    }\n\n    int firstCPIndex = -1;\n    int prevCPIndex\
        \ = -1;\n    int minDistance = 1000000;\n    int currIndex = 1;\n    ListNode\
        \ prevNode = head;\n    ListNode currNode = head.next!;\n\n    while (currNode.next\
        \ != null) {\n      ListNode nextNode = currNode.next!;\n      if ((currNode.val\
        \ > prevNode.val && currNode.val > nextNode.val) ||\n          (currNode.val\
        \ < prevNode.val && currNode.val < nextNode.val)) {\n\n        if (firstCPIndex\
        \ == -1) {\n          firstCPIndex = currIndex;\n        } else {\n        \
        \  int dist = currIndex - prevCPIndex;\n          if (dist < minDistance) {\n\
        \            minDistance = dist;\n          }\n        }\n        prevCPIndex\
        \ = currIndex;\n      }\n      prevNode = currNode;\n      currNode = nextNode;\n\
        \      currIndex++;\n    }\n\n    if (minDistance == 1000000) {\n      return\
        \ [-1, -1];\n    }\n\n    return [minDistance, prevCPIndex - firstCPIndex];\n\
        \  }\n}"
      go: "/**\n * Definition for singly-linked list.\n * type ListNode struct {\n *\
        \     Val int\n *     Next *ListNode\n * }\n */\nfunc nodesBetweenCriticalPoints(head\
        \ *ListNode) []int {\n    if head == nil || head.Next == nil || head.Next.Next\
        \ == nil {\n        return []int{-1, -1}\n    }\n\n    firstCPIndex := -1\n\
        \    prevCPIndex := -1\n    minDistance := 1000000\n    currIndex := 1\n   \
        \ prevNode := head\n    currNode := head.Next\n\n    for currNode.Next != nil\
        \ {\n        nextNode := currNode.Next\n        if (currNode.Val > prevNode.Val\
        \ && currNode.Val > nextNode.Val) ||\n           (currNode.Val < prevNode.Val\
        \ && currNode.Val < nextNode.Val) {\n\n            if firstCPIndex == -1 {\n\
        \                firstCPIndex = currIndex\n            } else {\n          \
        \      dist := currIndex - prevCPIndex\n                if dist < minDistance\
        \ {\n                    minDistance = dist\n                }\n           \
        \ }\n            prevCPIndex = currIndex\n        }\n        prevNode = currNode\n\
        \        currNode = nextNode\n        currIndex++\n    }\n\n    if minDistance\
        \ == 1000000 {\n        return []int{-1, -1}\n    }\n\n    return []int{minDistance,\
        \ prevCPIndex - firstCPIndex}\n}"
      ruby: "# Definition for singly-linked list.\n# class ListNode\n#     attr_accessor\
        \ :val, :next\n#     def initialize(val = 0, _next = nil)\n#         @val =\
        \ val\n#         @next = _next\n#     end\n# end\n# @param {ListNode} head\n\
        # @return {Integer[]}\ndef nodes_between_critical_points(head)\n    if head.nil?\
        \ || head.next.nil? || head.next.next.nil?\n        return [-1, -1]\n    end\n\
        \n    first_cp_index = -1\n    prev_cp_index = -1\n    min_distance = 1000000\n\
        \    curr_index = 1\n    prev_node = head\n    curr_node = head.next\n\n   \
        \ while !curr_node.next.nil?\n        next_node = curr_node.next\n        if\
        \ (curr_node.val > prev_node.val && curr_node.val > next_node.val) ||\n    \
        \       (curr_node.val < prev_node.val && curr_node.val < next_node.val)\n\n\
        \            if first_cp_index == -1\n                first_cp_index = curr_index\n\
        \            else\n                dist = curr_index - prev_cp_index\n     \
        \           min_distance = dist if dist < min_distance\n            end\n  \
        \          prev_cp_index = curr_index\n        end\n        prev_node = curr_node\n\
        \        curr_node = next_node\n        curr_index += 1\n    end\n\n    if min_distance\
        \ == 1000000\n        return [-1, -1]\n    end\n\n    [min_distance, prev_cp_index\
        \ - first_cp_index]\nend"
      scala: "/**\n * Definition for singly-linked list.\n * class ListNode(_x: Int\
        \ = 0, _next: ListNode = null) {\n *   var next: ListNode = _next\n *   var\
        \ x: Int = _x\n * }\n */\nobject Solution {\n    def nodesBetweenCriticalPoints(head:\
        \ ListNode): Array[Int] = {\n        if (head == null || head.next == null ||\
        \ head.next.next == null) {\n            return Array(-1, -1)\n        }\n\n\
        \        var firstCPIndex = -1\n        var prevCPIndex = -1\n        var minDistance\
        \ = Int.MaxValue\n        var currIndex = 1\n        var prevNode = head\n \
        \       var currNode = head.next\n\n        while (currNode != null && currNode.next\
        \ != null) {\n            val nextNode = currNode.next\n            if ((currNode.x\
        \ > prevNode.x && currNode.x > nextNode.x) ||\n                (currNode.x <\
        \ prevNode.x && currNode.x < nextNode.x)) {\n\n                if (firstCPIndex\
        \ == -1) {\n                    firstCPIndex = currIndex\n                }\
        \ else {\n                    val dist = currIndex - prevCPIndex\n         \
        \           if (dist < minDistance) {\n                        minDistance =\
        \ dist\n                    }\n                }\n                prevCPIndex\
        \ = currIndex\n            }\n            prevNode = currNode\n            currNode\
        \ = nextNode\n            currIndex += 1\n        }\n\n        if (minDistance\
        \ == Int.MaxValue) {\n            Array(-1, -1)\n        } else {\n        \
        \    Array(minDistance, prevCPIndex - firstCPIndex)\n        }\n    }\n}"
      rust: "impl Solution {\n    pub fn nodes_between_critical_points(head: Option<Box<ListNode>>)\
        \ -> Vec<i32> {\n        let mut first_cp = -1;\n        let mut last_cp = -1;\n\
        \        let mut min_dist = i32::MAX;\n\n        if let Some(h) = head {\n \
        \           let mut prev_val = h.val;\n            let mut curr = h.next.as_ref();\n\
        \            let mut pos = 1;\n\n            while let Some(node) = curr {\n\
        \                if let Some(next_node) = node.next.as_ref() {\n           \
        \         let v = node.val;\n                    let nv = next_node.val;\n\n\
        \                    if (v > prev_val && v > nv) || (v < prev_val && v < nv)\
        \ {\n                        if first_cp == -1 {\n                         \
        \   first_cp = pos;\n                        } else {\n                    \
        \        if pos - last_cp < min_dist {\n                                min_dist\
        \ = pos - last_cp;\n                            }\n                        }\n\
        \                        last_cp = pos;\n                    }\n           \
        \         prev_val = v;\n                    curr = node.next.as_ref();\n  \
        \                  pos += 1;\n                } else {\n                   \
        \ break;\n                }\n            }\n        }\n\n        if first_cp\
        \ == -1 || first_cp == last_cp {\n            vec![-1, -1]\n        } else {\n\
        \            vec![min_dist, last_cp - first_cp]\n        }\n    }\n}"
      racket: "(define/contract (nodes-between-critical-points head)\n  (-> (or/c list-node?\
        \ #f) (listof exact-integer?))\n  (if (or (not head) (not (list-node-next head)))\n\
        \      '(-1 -1)\n      (let loop ([prev-val (list-node-val head)]\n        \
        \         [curr (list-node-next head)]\n                 [idx 1]\n         \
        \        [first-cp #f]\n                 [last-cp #f]\n                 [min-dist\
        \ #f])\n        (let ([next (list-node-next curr)])\n          (if (not next)\n\
        \              (if (and first-cp last-cp (not (= first-cp last-cp)))\n     \
        \             (list min-dist (- last-cp first-cp))\n                  '(-1 -1))\n\
        \              (let* ([curr-val (list-node-val curr)]\n                    \
        \ [next-val (list-node-val next)]\n                     [is-cp (or (and (> curr-val\
        \ prev-val) (> curr-val next-val))\n                                (and (<\
        \ curr-val prev-val) (< curr-val next-val)))])\n                (if is-cp\n\
        \                    (loop curr-val next (+ idx 1)\n                       \
        \   (if first-cp first-cp idx)\n                          idx\n            \
        \              (if (and last-cp (or (not min-dist) (< (- idx last-cp) min-dist)))\n\
        \                              (- idx last-cp)\n                           \
        \   min-dist))\n                    (loop curr-val next (+ idx 1) first-cp last-cp\
        \ min-dist))))))))"
      erlang: "nodes_between_critical_points(Head) ->\n  case Head#list_node.next of\n\
        \    null -> [-1, -1];\n    NextNode ->\n      find_cp(Head#list_node.val, NextNode,\
        \ 1, null, null, 1000000)\n  end.\n\nfind_cp(_PrevVal, #list_node{val = _V,\
        \ next = null}, _Idx, First, Last, MinDist) ->\n  if \n    First =:= null; Last\
        \ =:= null; First =:= Last -> [-1, -1];\n    true -> [MinDist, Last - First]\n\
        \  end;\nfind_cp(PrevVal, #list_node{val = V, next = NextNode}, Idx, First,\
        \ Last, MinDist) ->\n  NV = NextNode#list_node.val,\n  IsCP = ((V > PrevVal)\
        \ and (V > NV)) or ((V < PrevVal) and (V < NV)),\n  {NewFirst, NewLast, NewMinDist}\
        \ = \n    if IsCP ->\n      NF = if First =:= null -> Idx; true -> First end,\n\
        \      NM = if Last =:= null -> MinDist; true -> erlang:min(MinDist, Idx - Last)\
        \ end,\n      {NF, Idx, NM};\n    true ->\n      {First, Last, MinDist}\n  \
        \  end,\n  find_cp(V, NextNode, Idx + 1, NewFirst, NewLast, NewMinDist)."
      elixir: "defmodule Solution do\n  @spec nodes_between_critical_points(head ::\
        \ ListNode.t | nil) :: [integer]\n  def nodes_between_critical_points(head)\
        \ do\n    case head.next do\n      nil -> [-1, -1]\n      next_node -> find_cp(head.val,\
        \ next_node, 1, nil, nil, 100_000_000)\n    end\n  end\n\n  defp find_cp(_prev_val,\
        \ %ListNode{val: _v, next: nil}, _idx, first, last, min_dist) do\n    if first\
        \ == nil or last == nil or first == last do\n      [-1, -1]\n    else\n    \
        \  [min_dist, last - first]\n    end\n  end\n\n  defp find_cp(prev_val, %ListNode{val:\
        \ v, next: %ListNode{} = next_node}, idx, first, last, min_dist) do\n    nv\
        \ = next_node.val\n    is_cp = (v > prev_val and v > nv) or (v < prev_val and\
        \ v < nv)\n    {new_first, new_last, new_min_dist} = \n      if is_cp do\n \
        \       nf = if first == nil, do: idx, else: first\n        nm = if last ==\
        \ nil, do: min_dist, else: min(min_dist, idx - last)\n        {nf, idx, nm}\n\
        \      else\n        {first, last, min_dist}\n      end\n    find_cp(v, next_node,\
        \ idx + 1, new_first, new_last, new_min_dist)\n  end\nend"
    approach: 'To find the distances between critical points, we traverse the linked
      list while maintaining references to the previous, current, and next nodes. A
      node is defined as a critical point if it is either a local maximum (strictly
      greater than both neighbors) or a local minimum (strictly smaller than both neighbors).
      Since a critical point requires both a predecessor and a successor, the search
      starts from the second node and ends at the second-to-last node. We track the
      current index during the traversal to record the positions of these points.


      To optimize space, instead of storing all critical point indices, we keep track
      of the index of the first critical point found and the index of the most recently
      found critical point. The maximum distance is simply the difference between the
      index of the last critical point and the first critical point. The minimum distance
      is the smallest gap between any two consecutive critical points encountered during
      the traversal. If we find fewer than two critical points, we return [-1, -1].'
    time_complexity: O(N) where N is the number of nodes in the linked list. We perform
      a single pass through the list to identify critical points and calculate distances.
    space_complexity: O(1) excluding the output array. We only store a few integer variables
      (first index, last index, minimum distance, current index, and pointers) regardless
      of the size of the input list.
    elapsed_time: 169.7400221824646
    model: gemini-3-flash-preview
    generated_at: '2026-08-31 02:44:36 '
---

## Problem #2058: Find the Minimum and Maximum Number of Nodes Between Critical Points

**Difficulty:** Medium

**Topics:** Linked List

## Problem Description

<p>A <strong>critical point</strong> in a linked list is defined as <strong>either</strong> a <strong>local maxima</strong> or a <strong>local minima</strong>.</p>

<p>A node is a <strong>local maxima</strong> if the current node has a value <strong>strictly greater</strong> than the previous node and the next node.</p>

<p>A node is a <strong>local minima</strong> if the current node has a value <strong>strictly smaller</strong> than the previous node and the next node.</p>

<p>Note that a node can only be a local maxima/minima if there exists <strong>both</strong> a previous node and a next node.</p>

<p>Given a linked list <code>head</code>, return <em>an array of length 2 containing </em><code>[minDistance, maxDistance]</code><em> where </em><code>minDistance</code><em> is the <strong>minimum distance</strong> between <strong>any&nbsp;two distinct</strong> critical points and </em><code>maxDistance</code><em> is the <strong>maximum distance</strong> between <strong>any&nbsp;two distinct</strong> critical points. If there are <strong>fewer</strong> than two critical points, return </em><code>[-1, -1]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/10/13/a1.png" style="width: 148px; height: 55px;" />
<pre>
<strong>Input:</strong> head = [3,1]
<strong>Output:</strong> [-1,-1]
<strong>Explanation:</strong> There are no critical points in [3,1].
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/10/13/a2.png" style="width: 624px; height: 46px;" />
<pre>
<strong>Input:</strong> head = [5,3,1,2,5,1,2]
<strong>Output:</strong> [1,3]
<strong>Explanation:</strong> There are three critical points:
- [5,3,<strong><u>1</u></strong>,2,5,1,2]: The third node is a local minima because 1 is less than 3 and 2.
- [5,3,1,2,<u><strong>5</strong></u>,1,2]: The fifth node is a local maxima because 5 is greater than 2 and 1.
- [5,3,1,2,5,<u><strong>1</strong></u>,2]: The sixth node is a local minima because 1 is less than 5 and 2.
The minimum distance is between the fifth and the sixth node. minDistance = 6 - 5 = 1.
The maximum distance is between the third and the sixth node. maxDistance = 6 - 3 = 3.
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/10/14/a5.png" style="width: 624px; height: 39px;" />
<pre>
<strong>Input:</strong> head = [1,3,2,2,3,2,2,2,7]
<strong>Output:</strong> [3,3]
<strong>Explanation:</strong> There are two critical points:
- [1,<u><strong>3</strong></u>,2,2,3,2,2,2,7]: The second node is a local maxima because 3 is greater than 1 and 2.
- [1,3,2,2,<u><strong>3</strong></u>,2,2,2,7]: The fifth node is a local maxima because 3 is greater than 2 and 2.
Both the minimum and maximum distances are between the second and the fifth node.
Thus, minDistance and maxDistance is 5 - 2 = 3.
Note that the last node is not considered a local maxima because it does not have a next node.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is in the range <code>[2, 10<sup>5</sup>]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
</ul>


## Hints

1. The maximum distance must be the distance between the first and last critical point.

2. For each adjacent critical point, calculate the difference and check if it is the minimum distance.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To find the distances between critical points, we traverse the linked list while maintaining references to the previous, current, and next nodes. A node is defined as a critical point if it is either a local maximum (strictly greater than both neighbors) or a local minimum (strictly smaller than both neighbors). Since a critical point requires both a predecessor and a successor, the search starts from the second node and ends at the second-to-last node. We track the current index during the traversal to record the positions of these points.

To optimize space, instead of storing all critical point indices, we keep track of the index of the first critical point found and the index of the most recently found critical point. The maximum distance is simply the difference between the index of the last critical point and the first critical point. The minimum distance is the smallest gap between any two consecutive critical points encountered during the traversal. If we find fewer than two critical points, we return [-1, -1].

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
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    vector<int> nodesBetweenCriticalPoints(ListNode* head) {
        if (!head || !head->next || !head->next->next) return {-1, -1};

        int firstIdx = -1, lastIdx = -1, minDist = INT_MAX;
        ListNode* prev = head;
        ListNode* curr = head->next;
        int idx = 1;

        while (curr->next) {
            if ((curr->val > prev->val && curr->val > curr->next->val) || 
                (curr->val < prev->val && curr->val < curr->next->val)) {
                if (firstIdx == -1) {
                    firstIdx = idx;
                } else {
                    minDist = min(minDist, idx - lastIdx);
                }
                lastIdx = idx;
            }
            prev = curr;
            curr = curr->next;
            idx++;
        }

        if (firstIdx == lastIdx) return {-1, -1};
        return {minDist, lastIdx - firstIdx};
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public int[] nodesBetweenCriticalPoints(ListNode head) {
        if (head == null || head.next == null || head.next.next == null) return new int[]{-1, -1};

        int firstIdx = -1, lastIdx = -1, minDist = Integer.MAX_VALUE;
        ListNode prev = head;
        ListNode curr = head.next;
        int idx = 1;

        while (curr.next != null) {
            if ((curr.val > prev.val && curr.val > curr.next.val) || 
                (curr.val < prev.val && curr.val < curr.next.val)) {
                if (firstIdx == -1) {
                    firstIdx = idx;
                } else {
                    minDist = Math.min(minDist, idx - lastIdx);
                }
                lastIdx = idx;
            }
            prev = curr;
            curr = curr.next;
            idx++;
        }

        if (firstIdx == lastIdx) return new int[]{-1, -1};
        return new int[]{minDist, lastIdx - firstIdx};
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        first_idx = -1
        last_idx = -1
        min_dist = float('inf')

        prev = head
        curr = head.next
        idx = 1

        while curr.next:
            if (curr.val > prev.val and curr.val > curr.next.val) or \
               (curr.val < prev.val and curr.val < curr.next.val):
                if first_idx == -1:
                    first_idx = idx
                else:
                    min_dist = min(min_dist, idx - last_idx)
                last_idx = idx
            prev = curr
            curr = curr.next
            idx += 1

        if first_idx == last_idx:
            return [-1, -1]

        return [min_dist, last_idx - first_idx]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        first_idx = -1
        last_idx = -1
        min_dist = float('inf')

        prev = head
        curr = head.next
        idx = 1

        while curr.next:
            if (curr.val > prev.val and curr.val > curr.next.val) or \
               (curr.val < prev.val and curr.val < curr.next.val):
                if first_idx == -1:
                    first_idx = idx
                else:
                    min_dist = min(min_dist, idx - last_idx)
                last_idx = idx
            prev = curr
            curr = curr.next
            idx += 1

        if first_idx == last_idx:
            return [-1, -1]

        return [int(min_dist), last_idx - first_idx]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* nodesBetweenCriticalPoints(struct ListNode* head, int* returnSize) {
    *returnSize = 2;
    int* result = (int*)malloc(2 * sizeof(int));
    result[0] = -1;
    result[1] = -1;

    if (!head || !head->next || !head->next->next) {
        return result;
    }

    int firstIdx = -1, lastIdx = -1, minDist = 1000000000;
    struct ListNode* prev = head;
    struct ListNode* curr = head->next;
    int idx = 1;

    while (curr->next) {
        if ((curr->val > prev->val && curr->val > curr->next->val) || 
            (curr->val < prev->val && curr->val < curr->next->val)) {
            if (firstIdx == -1) {
                firstIdx = idx;
            } else {
                int diff = idx - lastIdx;
                if (diff < minDist) minDist = diff;
            }
            lastIdx = idx;
        }
        prev = curr;
        curr = curr->next;
        idx++;
    }

    if (firstIdx != -1 && lastIdx != -1 && firstIdx != lastIdx) {
        result[0] = minDist;
        result[1] = lastIdx - firstIdx;
    }

    return result;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public int[] NodesBetweenCriticalPoints(ListNode head) {
        if (head == null || head.next == null || head.next.next == null) {
            return new int[] { -1, -1 };
        }

        int firstCP = -1;
        int lastCP = -1;
        int minDist = int.MaxValue;
        int currentIndex = 1;

        ListNode prev = head;
        ListNode curr = head.next;

        while (curr.next != null) {
            ListNode next = curr.next;
            bool isCP = (curr.val > prev.val && curr.val > next.val) ||
                        (curr.val < prev.val && curr.val < next.val);

            if (isCP) {
                if (firstCP == -1) {
                    firstCP = currentIndex;
                } else {
                    int diff = currentIndex - lastCP;
                    if (diff < minDist) {
                        minDist = diff;
                    }
                }
                lastCP = currentIndex;
            }

            prev = curr;
            curr = next;
            currentIndex++;
        }

        if (firstCP == lastCP) {
            return new int[] { -1, -1 };
        }

        return new int[] { minDist, lastCP - firstCP };
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {number[]}
 */
var nodesBetweenCriticalPoints = function(head) {
    if (!head || !head.next || !head.next.next) return [-1, -1];

    let firstCP = -1;
    let lastCP = -1;
    let minDist = Infinity;
    let currentIndex = 1;

    let prev = head;
    let curr = head.next;

    while (curr.next) {
        let next = curr.next;
        let isCP = (curr.val > prev.val && curr.val > next.val) ||
                   (curr.val < prev.val && curr.val < next.val);

        if (isCP) {
            if (firstCP === -1) {
                firstCP = currentIndex;
            } else {
                minDist = Math.min(minDist, currentIndex - lastCP);
            }
            lastCP = currentIndex;
        }

        prev = curr;
        curr = next;
        currentIndex++;
    }

    if (firstCP === lastCP) return [-1, -1];

    return [minDist, lastCP - firstCP];
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     } 
 * }
 */

function nodesBetweenCriticalPoints(head: ListNode | null): number[] {
    if (!head || !head.next || !head.next.next) {
        return [-1, -1];
    }

    let firstCP: number = -1;
    let lastCP: number = -1;
    let minDist: number = Infinity;
    let currentIndex: number = 1;

    let prev: ListNode = head;
    let curr: ListNode = head.next;

    while (curr.next !== null) {
        let next: ListNode = curr.next;
        let isCP: boolean = (curr.val > prev.val && curr.val > next.val) ||
                            (curr.val < prev.val && curr.val < next.val);

        if (isCP) {
            if (firstCP === -1) {
                firstCP = currentIndex;
            } else {
                minDist = Math.min(minDist, currentIndex - lastCP);
            }
            lastCP = currentIndex;
        }

        prev = curr;
        curr = next;
        currentIndex++;
    }

    if (firstCP === lastCP) {
        return [-1, -1];
    }

    return [minDist, lastCP - firstCP];
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
/**
 * Definition for a singly-linked list.
 * class ListNode {
 *     public $val = 0;
 *     public $next = null;
 *     function __construct($val = 0, $next = null) {
 *         this.val = $val;
 *         this.next = $next;
 *     }
 * }
 */
class Solution {

    /**
     * @param ListNode $head
     * @return Integer[]
     */
    function nodesBetweenCriticalPoints($head) {
        if ($head === null || $head->next === null || $head->next->next === null) {
            return [-1, -1];
        }

        $firstCP = -1;
        $lastCP = -1;
        $minDist = PHP_INT_MAX;
        $currentIndex = 1;

        $prev = $head;
        $curr = $head->next;

        while ($curr->next !== null) {
            $next = $curr->next;
            $isCP = ($curr->val > $prev->val && $curr->val > $next->val) ||
                    ($curr->val < $prev->val && $curr->val < $next->val);

            if ($isCP) {
                if ($firstCP === -1) {
                    $firstCP = $currentIndex;
                } else {
                    $minDist = min($minDist, $currentIndex - $lastCP);
                }
                $lastCP = $currentIndex;
            }

            $prev = $curr;
            $curr = $next;
            $currentIndex++;
        }

        if ($firstCP === $lastCP) {
            return [-1, -1];
        }

        return [$minDist, $lastCP - $firstCP];
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public var val: Int
 *     public var next: ListNode?
 *     public init() { self.val = 0; self.next = nil; }
 *     public init(_ val: Int) { self.val = val; self.next = nil; }
 *     public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }
 * }
 */
class Solution {
    func nodesBetweenCriticalPoints(_ head: ListNode?) -> [Int] {
        guard let head = head, let nextNode = head.next, let nextNextNode = nextNode.next else {
            return [-1, -1]
        }

        var firstCP = -1
        var lastCP = -1
        var minDist = Int.max
        var currentIndex = 1

        var prev = head
        var curr = nextNode

        while let next = curr.next {
            let isCP = (curr.val > prev.val && curr.val > next.val) ||
                       (curr.val < prev.val && curr.val < next.val)

            if isCP {
                if firstCP == -1 {
                    firstCP = currentIndex
                } else {
                    minDist = min(minDist, currentIndex - lastCP)
                }
                lastCP = currentIndex
            }

            prev = curr
            curr = next
            currentIndex += 1
        }

        if firstCP == lastCP {
            return [-1, -1]
        }

        return [minDist, lastCP - firstCP]
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
/**
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */
class Solution {
    fun nodesBetweenCriticalPoints(head: ListNode?): IntArray {
        if (head?.next?.next == null) return intArrayOf(-1, -1)

        var firstCPIndex = -1
        var prevCPIndex = -1
        var minDistance = Int.MAX_VALUE
        var currIndex = 1
        var prevNode = head
        var currNode = head.next

        while (currNode?.next != null) {
            val nextNode = currNode.next!!
            if ((currNode.`val` > prevNode!!.`val` && currNode.`val` > nextNode.`val`) ||
                (currNode.`val` < prevNode.`val` && currNode.`val` < nextNode.`val")) {

                if (firstCPIndex == -1) {
                    firstCPIndex = currIndex
                } else {
                    val dist = currIndex - prevCPIndex
                    if (dist < minDistance) {
                        minDistance = dist
                    }
                }
                prevCPIndex = currIndex
            }
            prevNode = currNode
            currNode = nextNode
            currIndex++
        }

        if (minDistance == Int.MAX_VALUE) {
            return intArrayOf(-1, -1)
        }

        val maxDistance = prevCPIndex - firstCPIndex
        return intArrayOf(minDistance, maxDistance)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
/**
 * Definition for singly-linked list.
 * class ListNode {
 *   int val;
 *   ListNode? next;
 *   ListNode([this.val = 0, this.next]);
 * }
 */
class Solution {
  List<int> nodesBetweenCriticalPoints(ListNode? head) {
    if (head == null || head.next == null || head.next!.next == null) {
      return [-1, -1];
    }

    int firstCPIndex = -1;
    int prevCPIndex = -1;
    int minDistance = 1000000;
    int currIndex = 1;
    ListNode prevNode = head;
    ListNode currNode = head.next!;

    while (currNode.next != null) {
      ListNode nextNode = currNode.next!;
      if ((currNode.val > prevNode.val && currNode.val > nextNode.val) ||
          (currNode.val < prevNode.val && currNode.val < nextNode.val)) {

        if (firstCPIndex == -1) {
          firstCPIndex = currIndex;
        } else {
          int dist = currIndex - prevCPIndex;
          if (dist < minDistance) {
            minDistance = dist;
          }
        }
        prevCPIndex = currIndex;
      }
      prevNode = currNode;
      currNode = nextNode;
      currIndex++;
    }

    if (minDistance == 1000000) {
      return [-1, -1];
    }

    return [minDistance, prevCPIndex - firstCPIndex];
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func nodesBetweenCriticalPoints(head *ListNode) []int {
    if head == nil || head.Next == nil || head.Next.Next == nil {
        return []int{-1, -1}
    }

    firstCPIndex := -1
    prevCPIndex := -1
    minDistance := 1000000
    currIndex := 1
    prevNode := head
    currNode := head.Next

    for currNode.Next != nil {
        nextNode := currNode.Next
        if (currNode.Val > prevNode.Val && currNode.Val > nextNode.Val) ||
           (currNode.Val < prevNode.Val && currNode.Val < nextNode.Val) {

            if firstCPIndex == -1 {
                firstCPIndex = currIndex
            } else {
                dist := currIndex - prevCPIndex
                if dist < minDistance {
                    minDistance = dist
                }
            }
            prevCPIndex = currIndex
        }
        prevNode = currNode
        currNode = nextNode
        currIndex++
    }

    if minDistance == 1000000 {
        return []int{-1, -1}
    }

    return []int{minDistance, prevCPIndex - firstCPIndex}
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val = 0, _next = nil)
#         @val = val
#         @next = _next
#     end
# end
# @param {ListNode} head
# @return {Integer[]}
def nodes_between_critical_points(head)
    if head.nil? || head.next.nil? || head.next.next.nil?
        return [-1, -1]
    end

    first_cp_index = -1
    prev_cp_index = -1
    min_distance = 1000000
    curr_index = 1
    prev_node = head
    curr_node = head.next

    while !curr_node.next.nil?
        next_node = curr_node.next
        if (curr_node.val > prev_node.val && curr_node.val > next_node.val) ||
           (curr_node.val < prev_node.val && curr_node.val < next_node.val)

            if first_cp_index == -1
                first_cp_index = curr_index
            else
                dist = curr_index - prev_cp_index
                min_distance = dist if dist < min_distance
            end
            prev_cp_index = curr_index
        end
        prev_node = curr_node
        curr_node = next_node
        curr_index += 1
    end

    if min_distance == 1000000
        return [-1, -1]
    end

    [min_distance, prev_cp_index - first_cp_index]
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
/**
 * Definition for singly-linked list.
 * class ListNode(_x: Int = 0, _next: ListNode = null) {
 *   var next: ListNode = _next
 *   var x: Int = _x
 * }
 */
object Solution {
    def nodesBetweenCriticalPoints(head: ListNode): Array[Int] = {
        if (head == null || head.next == null || head.next.next == null) {
            return Array(-1, -1)
        }

        var firstCPIndex = -1
        var prevCPIndex = -1
        var minDistance = Int.MaxValue
        var currIndex = 1
        var prevNode = head
        var currNode = head.next

        while (currNode != null && currNode.next != null) {
            val nextNode = currNode.next
            if ((currNode.x > prevNode.x && currNode.x > nextNode.x) ||
                (currNode.x < prevNode.x && currNode.x < nextNode.x)) {

                if (firstCPIndex == -1) {
                    firstCPIndex = currIndex
                } else {
                    val dist = currIndex - prevCPIndex
                    if (dist < minDistance) {
                        minDistance = dist
                    }
                }
                prevCPIndex = currIndex
            }
            prevNode = currNode
            currNode = nextNode
            currIndex += 1
        }

        if (minDistance == Int.MaxValue) {
            Array(-1, -1)
        } else {
            Array(minDistance, prevCPIndex - firstCPIndex)
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn nodes_between_critical_points(head: Option<Box<ListNode>>) -> Vec<i32> {
        let mut first_cp = -1;
        let mut last_cp = -1;
        let mut min_dist = i32::MAX;

        if let Some(h) = head {
            let mut prev_val = h.val;
            let mut curr = h.next.as_ref();
            let mut pos = 1;

            while let Some(node) = curr {
                if let Some(next_node) = node.next.as_ref() {
                    let v = node.val;
                    let nv = next_node.val;

                    if (v > prev_val && v > nv) || (v < prev_val && v < nv) {
                        if first_cp == -1 {
                            first_cp = pos;
                        } else {
                            if pos - last_cp < min_dist {
                                min_dist = pos - last_cp;
                            }
                        }
                        last_cp = pos;
                    }
                    prev_val = v;
                    curr = node.next.as_ref();
                    pos += 1;
                } else {
                    break;
                }
            }
        }

        if first_cp == -1 || first_cp == last_cp {
            vec![-1, -1]
        } else {
            vec![min_dist, last_cp - first_cp]
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (nodes-between-critical-points head)
  (-> (or/c list-node? #f) (listof exact-integer?))
  (if (or (not head) (not (list-node-next head)))
      '(-1 -1)
      (let loop ([prev-val (list-node-val head)]
                 [curr (list-node-next head)]
                 [idx 1]
                 [first-cp #f]
                 [last-cp #f]
                 [min-dist #f])
        (let ([next (list-node-next curr)])
          (if (not next)
              (if (and first-cp last-cp (not (= first-cp last-cp)))
                  (list min-dist (- last-cp first-cp))
                  '(-1 -1))
              (let* ([curr-val (list-node-val curr)]
                     [next-val (list-node-val next)]
                     [is-cp (or (and (> curr-val prev-val) (> curr-val next-val))
                                (and (< curr-val prev-val) (< curr-val next-val)))])
                (if is-cp
                    (loop curr-val next (+ idx 1)
                          (if first-cp first-cp idx)
                          idx
                          (if (and last-cp (or (not min-dist) (< (- idx last-cp) min-dist)))
                              (- idx last-cp)
                              min-dist))
                    (loop curr-val next (+ idx 1) first-cp last-cp min-dist))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
nodes_between_critical_points(Head) ->
  case Head#list_node.next of
    null -> [-1, -1];
    NextNode ->
      find_cp(Head#list_node.val, NextNode, 1, null, null, 1000000)
  end.

find_cp(_PrevVal, #list_node{val = _V, next = null}, _Idx, First, Last, MinDist) ->
  if 
    First =:= null; Last =:= null; First =:= Last -> [-1, -1];
    true -> [MinDist, Last - First]
  end;
find_cp(PrevVal, #list_node{val = V, next = NextNode}, Idx, First, Last, MinDist) ->
  NV = NextNode#list_node.val,
  IsCP = ((V > PrevVal) and (V > NV)) or ((V < PrevVal) and (V < NV)),
  {NewFirst, NewLast, NewMinDist} = 
    if IsCP ->
      NF = if First =:= null -> Idx; true -> First end,
      NM = if Last =:= null -> MinDist; true -> erlang:min(MinDist, Idx - Last) end,
      {NF, Idx, NM};
    true ->
      {First, Last, MinDist}
    end,
  find_cp(V, NextNode, Idx + 1, NewFirst, NewLast, NewMinDist).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec nodes_between_critical_points(head :: ListNode.t | nil) :: [integer]
  def nodes_between_critical_points(head) do
    case head.next do
      nil -> [-1, -1]
      next_node -> find_cp(head.val, next_node, 1, nil, nil, 100_000_000)
    end
  end

  defp find_cp(_prev_val, %ListNode{val: _v, next: nil}, _idx, first, last, min_dist) do
    if first == nil or last == nil or first == last do
      [-1, -1]
    else
      [min_dist, last - first]
    end
  end

  defp find_cp(prev_val, %ListNode{val: v, next: %ListNode{} = next_node}, idx, first, last, min_dist) do
    nv = next_node.val
    is_cp = (v > prev_val and v > nv) or (v < prev_val and v < nv)
    {new_first, new_last, new_min_dist} = 
      if is_cp do
        nf = if first == nil, do: idx, else: first
        nm = if last == nil, do: min_dist, else: min(min_dist, idx - last)
        {nf, idx, nm}
      else
        {first, last, min_dist}
      end
    find_cp(v, next_node, idx + 1, new_first, new_last, new_min_dist)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N) where N is the number of nodes in the linked list. We perform a single pass through the list to identify critical points and calculate distances.
- **Space Complexity:** O(1) excluding the output array. We only store a few integer variables (first index, last index, minimum distance, current index, and pointers) regardless of the size of the input list.
