---
layout: post
title: "Maximum Level Sum of a Binary Tree"
date: 2026-01-06 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Tree", "Depth-First Search", "Breadth-First Search", "Binary Tree"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
ai_solutions:
  - solutions:
      cpp: "/**\n * Definition for a binary tree node.\n * struct TreeNode {\n *   \
        \  int val;\n *     TreeNode *left;\n *     TreeNode *right;\n *     TreeNode()\
        \ : val(0), left(nullptr), right(nullptr) {}\n *     TreeNode(int x) : val(x),\
        \ left(nullptr), right(nullptr) {}\n *     TreeNode(int x, TreeNode *left, TreeNode\
        \ *right) : val(x), left(left), right(right) {}\n * };\n */\n#include <queue>\n\
        #include <limits>\n\nclass Solution {\npublic:\n    int maxLevelSum(TreeNode*\
        \ root) {\n        // According to constraints, root is never null (1 <= N <=\
        \ 10^4).\n        // if (!root) {\n        //     return 0;\n        // }\n\n\
        \        std::queue<TreeNode*> q;\n        q.push(root);\n\n        long long\
        \ max_sum = std::numeric_limits<long long>::min();\n        int max_level =\
        \ 1;\n        int current_level = 1;\n\n        while (!q.empty()) {\n     \
        \       int level_size = q.size();\n            long long current_level_sum\
        \ = 0;\n\n            for (int i = 0; i < level_size; ++i) {\n             \
        \   TreeNode* node = q.front();\n                q.pop();\n                current_level_sum\
        \ += node->val;\n\n                if (node->left) {\n                    q.push(node->left);\n\
        \                }\n                if (node->right) {\n                   \
        \ q.push(node->right);\n                }\n            }\n\n            if (current_level_sum\
        \ > max_sum) {\n                max_sum = current_level_sum;\n             \
        \   max_level = current_level;\n            }\n            current_level++;\n\
        \        }\n\n        return max_level;\n    }\n};"
      java: "/**\n * Definition for a binary tree node.\n * public class TreeNode {\n\
        \ *     int val;\n *     TreeNode left;\n *     TreeNode right;\n *     TreeNode()\
        \ {}S\n *     TreeNode(int val) { this.val = val; }\n *     TreeNode(int val,\
        \ TreeNode left, TreeNode right) {\n *         this.val = val;\n *         this.left\
        \ = left;\n *         this.right = right;\n *     }\n * }\n */\nimport java.util.LinkedList;\n\
        import java.util.Queue;\n\nclass Solution {\n    public int maxLevelSum(TreeNode\
        \ root) {\n        // According to constraints, root is never null (1 <= N <=\
        \ 10^4).\n        // if (root == null) {\n        //     return 0;\n       \
        \ // }\n\n        Queue<TreeNode> q = new LinkedList<>();\n        q.offer(root);\n\
        \n        long max_sum = Long.MIN_VALUE;\n        int max_level = 1;\n     \
        \   int current_level = 1;\n\n        while (!q.isEmpty()) {\n            int\
        \ level_size = q.size();\n            long current_level_sum = 0;\n\n      \
        \      for (int i = 0; i < level_size; ++i) {\n                TreeNode node\
        \ = q.poll();\n                current_level_sum += node.val;\n\n          \
        \      if (node.left != null) {\n                    q.offer(node.left);\n \
        \               }\n                if (node.right != null) {\n             \
        \       q.offer(node.right);\n                }\n            }\n\n         \
        \   if (current_level_sum > max_sum) {\n                max_sum = current_level_sum;\n\
        \                max_level = current_level;\n            }\n            current_level++;\n\
        \        }\n\n        return max_level;\n    }\n}"
      python: "# Definition for a binary tree node.\n# class TreeNode(object):\n#  \
        \   def __init__(self, val=0, left=None, right=None):\n#         self.val =\
        \ val\n#         self.left = left\n#         self.right = right\nimport collections\n\
        \nclass Solution(object):\n    def maxLevelSum(self, root):\n        \"\"\"\n\
        \        :type root: Optional[TreeNode]\n        :rtype: int\n        \"\"\"\
        \n        # According to constraints, root is never null (1 <= N <= 10^4).\n\
        \        # if not root:\n        #     return 0\n\n        q = collections.deque([root])\n\
        \n        max_sum = float('-inf')\n        max_level = 1\n        current_level\
        \ = 1\n\n        while q:\n            level_size = len(q)\n            current_level_sum\
        \ = 0\n\n            for _ in range(level_size):\n                node = q.popleft()\n\
        \                current_level_sum += node.val\n\n                if node.left:\n\
        \                    q.append(node.left)\n                if node.right:\n \
        \                   q.append(node.right)\n\n            if current_level_sum\
        \ > max_sum:\n                max_sum = current_level_sum\n                max_level\
        \ = current_level\n            current_level += 1\n\n        return max_level"
      python3: "# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self,\
        \ val=0, left=None, right=None):\n#         self.val = val\n#         self.left\
        \ = left\n#         self.right = right\nimport collections\n\nclass Solution:\n\
        \    def maxLevelSum(self, root: Optional[TreeNode]) -> int:\n        # According\
        \ to constraints, root is never null (1 <= N <= 10^4).\n        # if not root:\n\
        \        #     return 0\n\n        q = collections.deque([root])\n\n       \
        \ max_sum = float('-inf')\n        max_level = 1\n        current_level = 1\n\
        \n        while q:\n            level_size = len(q)\n            current_level_sum\
        \ = 0\n\n            for _ in range(level_size):\n                node = q.popleft()\n\
        \                current_level_sum += node.val\n\n                if node.left:\n\
        \                    q.append(node.left)\n                if node.right:\n \
        \                   q.append(node.right)\n\n            if current_level_sum\
        \ > max_sum:\n                max_sum = current_level_sum\n                max_level\
        \ = current_level\n            current_level += 1\n\n        return max_level"
      c: "/**\n * Definition for a binary tree node.\n * struct TreeNode {\n *     int\
        \ val;\n *     struct TreeNode *left;\n *     struct TreeNode *right;\n * };\n\
        \ */\n#include <limits.h>\n#include <stdlib.h> // Not strictly needed for static\
        \ array, but good practice for dynamic.\n\n// Max nodes is 10^4. A static array\
        \ for queue is sufficient.\n#define MAX_NODES 10001 \n\nint maxLevelSum(struct\
        \ TreeNode* root) {\n    // According to constraints, root is never null (1\
        \ <= N <= 10^4).\n    // if (root == NULL) {\n    //     return 0;\n    // }\n\
        \n    struct TreeNode* q[MAX_NODES];\n    int head = 0;\n    int tail = 0;\n\
        \n    q[tail++] = root;\n\n    long long max_sum = LLONG_MIN; // Use long long\
        \ for sums to prevent overflow\n    int max_level = 1;\n    int current_level\
        \ = 1;\n\n    while (head < tail) {\n        int level_nodes_count = tail -\
        \ head;\n        long long current_level_sum = 0;\n\n        for (int i = 0;\
        \ i < level_nodes_count; ++i) {\n            struct TreeNode* node = q[head++];\n\
        \            current_level_sum += node->val;\n\n            if (node->left)\
        \ {\n                q[tail++] = node->left;\n            }\n            if\
        \ (node->right) {\n                q[tail++] = node->right;\n            }\n\
        \        }\n\n        if (current_level_sum > max_sum) {\n            max_sum\
        \ = current_level_sum;\n            max_level = current_level;\n        }\n\
        \        current_level++;\n    }\n\n    return max_level;\n}"
      csharp: "/**\n * Definition for a binary tree node.\n * public class TreeNode\
        \ {\n *     public int val;\n *     public TreeNode left;\n *     public TreeNode\
        \ right;\n *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null)\
        \ {\n *         this.val = val;\n *         this.left = left;\n *         this.right\
        \ = right;\n *     }\n * }\n */\npublic class Solution {\n    public int MaxLevelSum(TreeNode\
        \ root) {\n        if (root == null) {\n            return 0; // Constraints\
        \ say root is never null, but good practice.\n        }\n\n        int maxSum\
        \ = root.val;\n        int maxLevel = 1;\n        int currentLevel = 1;\n\n\
        \        Queue<TreeNode> queue = new Queue<TreeNode>();\n        queue.Enqueue(root);\n\
        \n        while (queue.Count > 0) {\n            int levelSize = queue.Count;\n\
        \            int currentLevelSum = 0;\n\n            for (int i = 0; i < levelSize;\
        \ i++) {\n                TreeNode node = queue.Dequeue();\n               \
        \ currentLevelSum += node.val;\n\n                if (node.left != null) {\n\
        \                    queue.Enqueue(node.left);\n                }\n        \
        \        if (node.right != null) {\n                    queue.Enqueue(node.right);\n\
        \                }\n            }\n\n            if (currentLevelSum > maxSum)\
        \ {\n                maxSum = currentLevelSum;\n                maxLevel = currentLevel;\n\
        \            }\n            currentLevel++;\n        }\n\n        return maxLevel;\n\
        \    }\n}"
      javascript: "/**\n * Definition for a binary tree node.\n * function TreeNode(val,\
        \ left, right) {\n *     this.val = (val===undefined ? 0 : val)\n *     this.left\
        \ = (left===undefined ? null : left)\n *     this.right = (right===undefined\
        \ ? null : right)\n * }\n */\n/**\n * @param {TreeNode} root\n * @return {number}\n\
        \ */\nvar maxLevelSum = function(root) {\n    if (!root) {\n        return 0;\n\
        \    }\n\n    let maxSum = root.val;\n    let maxLevel = 1;\n    let currentLevel\
        \ = 1;\n\n    let queue = [root];\n\n    while (queue.length > 0) {\n      \
        \  let levelSize = queue.length;\n        let currentLevelSum = 0;\n\n     \
        \   for (let i = 0; i < levelSize; i++) {\n            let node = queue.shift();\n\
        \            currentLevelSum += node.val;\n\n            if (node.left) {\n\
        \                queue.push(node.left);\n            }\n            if (node.right)\
        \ {\n                queue.push(node.right);\n            }\n        }\n\n \
        \       if (currentLevelSum > maxSum) {\n            maxSum = currentLevelSum;\n\
        \            maxLevel = currentLevel;\n        }\n        currentLevel++;\n\
        \    }\n\n    return maxLevel;\n};"
      typescript: "/**\n * Definition for a binary tree node.\n * class TreeNode {\n\
        \ *     val: number\n *     left: TreeNode | null\n *     right: TreeNode |\
        \ null\n *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode\
        \ | null) {\n *         this.val = (val===undefined ? 0 : val)\n *         this.left\
        \ = (left===undefined ? null : left)\n *         this.right = (right===undefined\
        \ ? null : right)\n *     }\n * }\n */\n\nfunction maxLevelSum(root: TreeNode\
        \ | null): number {\n    if (!root) {\n        return 0;\n    }\n\n    let maxSum:\
        \ number = root.val;\n    let maxLevel: number = 1;\n    let currentLevel: number\
        \ = 1;\n\n    let queue: TreeNode[] = [root];\n\n    while (queue.length > 0)\
        \ {\n        let levelSize: number = queue.length;\n        let currentLevelSum:\
        \ number = 0;\n\n        for (let i = 0; i < levelSize; i++) {\n           \
        \ let node: TreeNode = queue.shift()!;\n            currentLevelSum += node.val;\n\
        \n            if (node.left) {\n                queue.push(node.left);\n   \
        \         }\n            if (node.right) {\n                queue.push(node.right);\n\
        \            }\n        }\n\n        if (currentLevelSum > maxSum) {\n     \
        \       maxSum = currentLevelSum;\n            maxLevel = currentLevel;\n  \
        \      }\n        currentLevel++;\n    }\n\n    return maxLevel;\n};"
      php: "/**\n * Definition for a binary tree node.\n * class TreeNode {\n *    \
        \ public $val = null;\n *     public $left = null;\n *     public $right = null;\n\
        \ *     function __construct($val = 0, $left = null, $right = null) {\n *  \
        \       $this->val = $val;\n *         $this->left = $left;\n *         $this->right\
        \ = $right;\n *     }\n * }\n */\nclass Solution {\n\n    /**\n     * @param\
        \ TreeNode $root\n     * @return Integer\n     */\n    function maxLevelSum($root)\
        \ {\n        if ($root === null) {\n            return 0;\n        }\n\n   \
        \     $maxSum = $root->val;\n        $maxLevel = 1;\n        $currentLevel =\
        \ 1;\n\n        $queue = new SplQueue();\n        $queue->enqueue($root);\n\n\
        \        while (!$queue->isEmpty()) {\n            $levelSize = $queue->count();\n\
        \            $currentLevelSum = 0;\n\n            for ($i = 0; $i < $levelSize;\
        \ $i++) {\n                $node = $queue->dequeue();\n                $currentLevelSum\
        \ += $node->val;\n\n                if ($node->left !== null) {\n          \
        \          $queue->enqueue($node->left);\n                }\n              \
        \  if ($node->right !== null) {\n                    $queue->enqueue($node->right);\n\
        \                }\n            }\n\n            if ($currentLevelSum > $maxSum)\
        \ {\n                $maxSum = $currentLevelSum;\n                $maxLevel\
        \ = $currentLevel;\n            }\n            $currentLevel++;\n        }\n\
        \n        return $maxLevel;\n    }\n}"
      swift: "/**\n * Definition for a binary tree node.\n * public class TreeNode {\n\
        \ *     public var val: Int\n *     public var left: TreeNode?\n *     public\
        \ var right: TreeNode?\n *     public init() { self.val = 0; self.left = nil;\
        \ self.right = nil; }\n *     public init(_ val: Int) { self.val = val; self.left\
        \ = nil; self.right = nil; }\n *     public init(_ val: Int, _ left: TreeNode?,\
        \ _ right: TreeNode?) {\n *         self.val = val\n *         self.left = left\n\
        \ *         self.right = right\n *     }\n * }\n */\nclass Solution {\n    func\
        \ maxLevelSum(_ root: TreeNode?) -> Int {\n        guard let root = root else\
        \ {\n            return 0 // Constraints say root is never null, but good practice.\n\
        \        }\n\n        var maxSum = root.val\n        var maxLevel = 1\n    \
        \    var currentLevel = 1\n\n        var queue: [TreeNode] = [root]\n\n    \
        \    while !queue.isEmpty {\n            let levelSize = queue.count\n     \
        \       var currentLevelSum = 0\n\n            for _ in 0..<levelSize {\n  \
        \              let node = queue.removeFirst()\n                currentLevelSum\
        \ += node.val\n\n                if let leftChild = node.left {\n          \
        \          queue.append(leftChild)\n                }\n                if let\
        \ rightChild = node.right {\n                    queue.append(rightChild)\n\
        \                }\n            }\n\n            if currentLevelSum > maxSum\
        \ {\n                maxSum = currentLevelSum\n                maxLevel = currentLevel\n\
        \            }\n            currentLevel += 1\n        }\n\n        return maxLevel\n\
        \    }\n}"
      kotlin: "import java.util.LinkedList\nimport java.util.Queue\n\n/**\n * Example:\n\
        \ * var ti = TreeNode(5)\n * var v = ti.`val`\n * Definition for a binary tree\
        \ node.\n * class TreeNode(var `val`: Int) {\n *     var left: TreeNode? = null\n\
        \ *     var right: TreeNode? = null\n * }\n */\nclass Solution {\n    fun maxLevelSum(root:\
        \ TreeNode?): Int {\n        if (root == null) {\n            return 0\n   \
        \     }\n\n        var maxSum = Int.MIN_VALUE\n        var maxLevel = 1\n  \
        \      var currentLevel = 1\n\n        val queue: Queue<TreeNode> = LinkedList()\n\
        \        queue.offer(root)\n\n        while (queue.isNotEmpty()) {\n       \
        \     val levelSize = queue.size\n            var currentLevelSum = 0\n\n  \
        \          for (i in 0 until levelSize) {\n                val node = queue.poll()\n\
        \                currentLevelSum += node.`val`\n\n                node.left?.let\
        \ { queue.offer(it) }\n                node.right?.let { queue.offer(it) }\n\
        \            }\n\n            if (currentLevelSum > maxSum) {\n            \
        \    maxSum = currentLevelSum\n                maxLevel = currentLevel\n   \
        \         }\n            currentLevel++\n        }\n        return maxLevel\n\
        \    }\n}"
      dart: "import 'dart:collection';\n\n/**\n * Definition for a binary tree node.\n\
        \ * class TreeNode {\n *   int val;\n *   TreeNode? left;\n *   TreeNode? right;\n\
        \ *   TreeNode([this.val = 0, this.left, this.right]);\n * }\n */\nclass Solution\
        \ {\n  int maxLevelSum(TreeNode? root) {\n    if (root == null) {\n      return\
        \ 0;\n    }\n\n    int maxSum = -2147483648; // A very small integer, equivalent\
        \ to Int.MIN_VALUE\n    int maxLevel = 1;\n    int currentLevel = 1;\n\n   \
        \ Queue<TreeNode> queue = Queue<TreeNode>();\n    queue.add(root);\n\n    while\
        \ (queue.isNotEmpty) {\n      int levelSize = queue.length;\n      int currentLevelSum\
        \ = 0;\n\n      for (int i = 0; i < levelSize; i++) {\n        TreeNode node\
        \ = queue.removeFirst();\n        currentLevelSum += node.val;\n\n        if\
        \ (node.left != null) {\n          queue.add(node.left!); // Use ! for null\
        \ safety after check\n        }\n        if (node.right != null) {\n       \
        \   queue.add(node.right!); // Use ! for null safety after check\n        }\n\
        \      }\n\n      if (currentLevelSum > maxSum) {\n        maxSum = currentLevelSum;\n\
        \        maxLevel = currentLevel;\n      }\n      currentLevel++;\n    }\n \
        \   return maxLevel;\n  }\n}"
      go: "import (\n\t\"container/list\"\n\t\"math\"\n)\n\n/**\n * Definition for a\
        \ binary tree node.\n * type TreeNode struct {\n *     Val int\n *     Left\
        \ *TreeNode\n *     Right *TreeNode\n * }\n */\nfunc maxLevelSum(root *TreeNode)\
        \ int {\n    if root == nil {\n        return 0\n    }\n\n    maxSum := math.MinInt64\n\
        \    maxLevel := 1\n    currentLevel := 1\n\n    queue := list.New()\n    queue.PushBack(root)\n\
        \n    for queue.Len() > 0 {\n        levelSize := queue.Len()\n        currentLevelSum\
        \ := 0\n\n        for i := 0; i < levelSize; i++ {\n            element := queue.Remove(queue.Front())\n\
        \            node := element.(*TreeNode)\n            currentLevelSum += node.Val\n\
        \n            if node.Left != nil {\n                queue.PushBack(node.Left)\n\
        \            }\n            if node.Right != nil {\n                queue.PushBack(node.Right)\n\
        \            }\n        }\n\n        if currentLevelSum > maxSum {\n       \
        \     maxSum = currentLevelSum\n            maxLevel = currentLevel\n      \
        \  }\n        currentLevel++\n    }\n    return maxLevel\n}"
      ruby: "# Definition for a binary tree node.\n# class TreeNode\n#     attr_accessor\
        \ :val, :left, :right\n#     def initialize(val = 0, left = nil, right = nil)\n\
        #         @val = val\n#         @left = left\n#         @right = right\n#  \
        \   end\n# end\n# @param {TreeNode} root\n# @return {Integer}\ndef max_level_sum(root)\n\
        \    return 0 if root.nil?\n\n    max_sum = -Float::INFINITY\n    max_level\
        \ = 1\n    current_level = 1\n\n    queue = []\n    queue.push(root)\n\n   \
        \ while !queue.empty?\n        level_size = queue.length\n        current_level_sum\
        \ = 0\n\n        level_size.times do\n            node = queue.shift # Dequeue\
        \ from front\n            current_level_sum += node.val\n\n            queue.push(node.left)\
        \ if node.left\n            queue.push(node.right) if node.right\n        end\n\
        \n        if current_level_sum > max_sum\n            max_sum = current_level_sum\n\
        \            max_level = current_level\n        end\n        current_level +=\
        \ 1\n    end\n    max_level\nend"
      scala: "import scala.collection.mutable\n\n/**\n * Definition for a binary tree\
        \ node.\n * class TreeNode(_value: Int = 0, _left: TreeNode = null, _right:\
        \ TreeNode = null) {\n *   var value: Int = _value\n *   var left: TreeNode\
        \ = _left\n *   var right: TreeNode = _right\n * }\n */\nobject Solution {\n\
        \    def maxLevelSum(root: TreeNode): Int = {\n        if (root == null) {\n\
        \            return 0\n        }\n\n        var maxSum: Int = Int.MinValue\n\
        \        var maxLevel: Int = 1\n        var currentLevel: Int = 1\n\n      \
        \  val queue = mutable.Queue[TreeNode]()\n        queue.enqueue(root)\n\n  \
        \      while (queue.nonEmpty) {\n            val levelSize = queue.size\n  \
        \          var currentLevelSum: Int = 0\n\n            for (_ <- 0 until levelSize)\
        \ {\n                val node = queue.dequeue()\n                currentLevelSum\
        \ += node.value\n\n                if (node.left != null) {\n              \
        \      queue.enqueue(node.left)\n                }\n                if (node.right\
        \ != null) {\n                    queue.enqueue(node.right)\n              \
        \  }\n            }\n\n            if (currentLevelSum > maxSum) {\n       \
        \         maxSum = currentLevelSum\n                maxLevel = currentLevel\n\
        \            }\n            currentLevel += 1\n        }\n        maxLevel\n\
        \    }\n}"
      rust: "use std::rc::Rc;\nuse std::cell::RefCell;\nuse std::collections::VecDeque;\n\
        \nimpl Solution {\n    pub fn max_level_sum(root: Option<Rc<RefCell<TreeNode>>>)\
        \ -> i32 {\n        let mut max_sum = i32::MIN;\n        let mut max_level =\
        \ 0; // Will be 1-indexed\n        let mut current_level = 1;\n\n        let\
        \ mut q: VecDeque<Rc<RefCell<TreeNode>>> = VecDeque::new();\n        if let\
        \ Some(node) = root {\n            q.push_back(node);\n        } else {\n  \
        \          // According to constraints, root is never null, but good practice.\n\
        \            return 0;\n        }\n\n        while !q.is_empty() {\n       \
        \     let level_size = q.len();\n            let mut current_level_sum = 0;\n\
        \n            for _ in 0..level_size {\n                if let Some(node_rc)\
        \ = q.pop_front() {\n                    let node = node_rc.borrow();\n    \
        \                current_level_sum += node.val;\n\n                    if let\
        \ Some(left_child) = node.left.clone() {\n                        q.push_back(left_child);\n\
        \                    }\n                    if let Some(right_child) = node.right.clone()\
        \ {\n                        q.push_back(right_child);\n                   \
        \ }\n                }\n            }\n\n            if current_level_sum >\
        \ max_sum {\n                max_sum = current_level_sum;\n                max_level\
        \ = current_level;\n            }\n            current_level += 1;\n       \
        \ }\n\n        max_level\n    }\n}"
      racket: "; Definition for a binary tree node.\n#|\n\n; val : integer?\n; left\
        \ : (or/c tree-node? #f)\n; right : (or/c tree-node? #f)\n(struct tree-node\n\
        \  (val left right) #:mutable #:transparent)\n\n; constructor\n(define (make-tree-node\
        \ [val 0])\n  (tree-node val #f #f))\n\n|#\n\n(define/contract (max-level-sum\
        \ root)\n  (-> (or/c tree-node? #f) exact-integer?)\n  (if (not root)\n    \
        \  0 ; According to constraints, root is never #f, but good practice.\n    \
        \  (let loop ((q (list root))\n                 (max-sum -1000000001) ; Initialize\
        \ with a value smaller than any possible sum\n                 (max-level 0)\n\
        \                 (current-level 1))\n        (if (empty? q)\n            max-level\n\
        \            (let* ((level-size (length q))\n                   (current-level-nodes\
        \ (take q level-size))\n                   (next-q (drop q level-size))\n  \
        \                 (current-level-sum (for/sum ([node current-level-nodes])\n\
        \                                        (tree-node-val node))))\n         \
        \     (let ((new-max-sum (if (> current-level-sum max-sum)\n               \
        \                      current-level-sum\n                                 \
        \    max-sum))\n                    (new-max-level (if (> current-level-sum\
        \ max-sum)\n                                       current-level\n         \
        \                              max-level)))\n                (let ((next-q-children\
        \ (for/fold ((children '()))\n                                             \
        \     ([node current-level-nodes])\n                                       \
        \ (let ((left (tree-node-left node))\n                                     \
        \         (right (tree-node-right node)))\n                                \
        \          (append children\n                                              \
        \    (if left (list left) '())\n                                           \
        \       (if right (list right) '()))))))\n                  (loop (append next-q\
        \ next-q-children)\n                        new-max-sum\n                  \
        \      new-max-level\n                        (+ current-level 1)))))))))"
      erlang: "%% Definition for a binary tree node.\n%%\n%% -record(tree_node, {val\
        \ = 0 :: integer(),\n%%                     left = null  :: 'null' | #tree_node{},\n\
        %%                     right = null :: 'null' | #tree_node{}}).\n\n-spec max_level_sum(Root\
        \ :: #tree_node{} | null) -> integer().\nmax_level_sum(Root) ->\n  case Root\
        \ of\n    null -> 0; % Constraints say root is never null\n    _ -> bfs_level([Root],\
        \ -1000000001, 0, 1) % Queue, MaxSum, MaxLevel, CurrentLevel\n  end.\n\nbfs_level([],\
        \ _MaxSum, MaxLevel, _CurrentLevel) ->\n  MaxLevel;\nbfs_level(CurrentLevelNodes,\
        \ MaxSum, MaxLevel, CurrentLevel) ->\n  CurrentLevelSum = lists:sum([Node#tree_node.val\
        \ || Node <- CurrentLevelNodes]),\n\n  {NewMaxSum, NewMaxLevel} = \n    if CurrentLevelSum\
        \ > MaxSum -> {CurrentLevelSum, CurrentLevel};\n       true -> {MaxSum, MaxLevel}\n\
        \    end,\n\n  NextLevelNodes = lists:foldl(fun(Node, Acc) ->\n            \
        \                     Left = Node#tree_node.left,\n                        \
        \         Right = Node#tree_node.right,\n                                 Acc1\
        \ = case Left of null -> Acc; _ -> Acc ++ [Left] end,\n                    \
        \             case Right of null -> Acc1; _ -> Acc1 ++ [Right] end\n       \
        \                        end, [], CurrentLevelNodes),\n\n  bfs_level(NextLevelNodes,\
        \ NewMaxSum, NewMaxLevel, CurrentLevel + 1)."
      elixir: "# Definition for a binary tree node.\n#\n# defmodule TreeNode do\n# \
        \  @type t :: %__MODULE__{}\n#   defstruct val: 0, left: nil, right: nil\n#\
        \ end\n\ndefmodule Solution do\n  @spec max_level_sum(root :: TreeNode.t | nil)\
        \ :: integer\n  def max_level_sum(root) do\n    case root do\n      nil -> 0\
        \ # Constraints say root is never nil\n      _ -> bfs([root], -1_000_000_001,\
        \ 0, 1) # Queue, MaxSum, MaxLevel, CurrentLevel\n    end\n  end\n\n  defp bfs([],\
        \ _max_sum, max_level, _current_level), do: max_level\n  defp bfs(current_level_nodes,\
        \ max_sum, max_level, current_level) do\n    current_level_sum = Enum.sum(Enum.map(current_level_nodes,\
        \ &(&1.val)))\n\n    {new_max_sum, new_max_level} = \n      if current_level_sum\
        \ > max_sum do\n        {current_level_sum, current_level}\n      else\n   \
        \     {max_sum, max_level}\n      end\n\n    next_level_nodes = \n      Enum.flat_map(current_level_nodes,\
        \ fn node ->\n        children = []\n        children = if node.left, do: [node.left\
        \ | children], else: children\n        children = if node.right, do: [node.right\
        \ | children], else: children\n        children\n      end)\n\n    bfs(next_level_nodes,\
        \ new_max_sum, new_max_level, current_level + 1)\n  end\nend"
    approach: 'The problem requires finding the level with the maximum sum of node values,
      returning the smallest such level if multiple levels have the same maximum sum.
      This is a classic Breadth-First Search (BFS) problem, as BFS naturally processes
      a tree level by level. We use a queue to manage nodes to visit, ensuring that
      all nodes at a given level are processed before moving to the next level.


      We initialize a variable for the maximum sum found so far (`maxSum`) to a very
      small value and a variable for the corresponding level (`maxLevel`) to 1. We also
      maintain a `currentLevel` counter. The BFS starts by adding the root to the queue.
      In each iteration of the main loop, we process all nodes currently in the queue,
      which represent all nodes at the `currentLevel`. We calculate their sum (`currentLevelSum`)
      and enqueue their non-null children. After processing all nodes for the `currentLevel`,
      we compare `currentLevelSum` with `maxSum`. If `currentLevelSum` is greater, we
      update `maxSum` and `maxLevel`. We then increment `currentLevel` and repeat until
      the queue is empty. Since we iterate levels in increasing order, the first level
      encountered with the maximum sum will be the smallest, satisfying the problem''s
      requirement.'
    time_complexity: 'The time complexity is O(N), where N is the number of nodes in
      the binary tree. This is because each node is visited and processed exactly once:
      it is enqueued once and dequeued once. The operations within the loop (summing
      values, adding children to the queue) take constant time per node.'
    space_complexity: The space complexity is O(W), where W is the maximum width of
      the binary tree. In the worst-case scenario, such as a complete binary tree, the
      queue might hold up to N/2 nodes at the widest level, making the space complexity
      O(N). In the best case, for a skewed tree, the queue would only hold one node
      at a time, resulting in O(1) space.
    elapsed_time: 110.98006010055542
    model: gemini-2.5-flash
    generated_at: '2026-01-06 01:10:54 '
  - solutions:
      cpp: "class Solution {\npublic:\n    int maxLevelSum(TreeNode* root) {\n     \
        \   if (!root) return 0;\n        int maxSum = root->val;\n        int maxLevel\
        \ = 1;\n        int level = 0;\n        std::queue<TreeNode*> q;\n        q.push(root);\n\
        \        while (!q.empty()) {\n            level++;\n            int size =\
        \ q.size();\n            int sum = 0;\n            for (int i = 0; i < size;\
        \ i++) {\n                TreeNode* node = q.front();\n                q.pop();\n\
        \                sum += node->val;\n                if (node->left) q.push(node->left);\n\
        \                if (node->right) q.push(node->right);\n            }\n    \
        \        if (sum > maxSum) {\n                maxSum = sum;\n              \
        \  maxLevel = level;\n            }\n        }\n        return maxLevel;\n \
        \   }\n};"
      java: "class Solution {\n    public int maxLevelSum(TreeNode root) {\n       \
        \ if (root == null) return 0;\n        int maxSum = root.val;\n        int maxLevel\
        \ = 1;\n        int level = 0;\n        java.util.Queue<TreeNode> q = new java.util.LinkedList<>();\n\
        \        q.add(root);\n        while (!q.isEmpty()) {\n            level++;\n\
        \            int size = q.size();\n            int sum = 0;\n            for\
        \ (int i = 0; i < size; i++) {\n                TreeNode node = q.poll();\n\
        \                sum += node.val;\n                if (node.left != null) q.add(node.left);\n\
        \                if (node.right != null) q.add(node.right);\n            }\n\
        \            if (sum > maxSum) {\n                maxSum = sum;\n          \
        \      maxLevel = level;\n            }\n        }\n        return maxLevel;\n\
        \    }\n}"
      python: "class Solution(object):\n    def maxLevelSum(self, root):\n        if\
        \ not root: return 0\n        maxSum = root.val\n        maxLevel = 1\n    \
        \    level = 0\n        q = []\n        q.append(root)\n        while q:\n \
        \           level += 1\n            size = len(q)\n            sum = 0\n   \
        \         for _ in range(size):\n                node = q.pop(0)\n         \
        \       sum += node.val\n                if node.left: q.append(node.left)\n\
        \                if node.right: q.append(node.right)\n            if sum > maxSum:\n\
        \                maxSum = sum\n                maxLevel = level\n        return\
        \ maxLevel"
      python3: "class Solution:\n    def maxLevelSum(self, root: Optional[TreeNode])\
        \ -> int:\n        if not root: return 0\n        maxSum = root.val\n      \
        \  maxLevel = 1\n        level = 0\n        q = []\n        q.append(root)\n\
        \        while q:\n            level += 1\n            size = len(q)\n     \
        \       sum = 0\n            for _ in range(size):\n                node = q.pop(0)\n\
        \                sum += node.val\n                if node.left: q.append(node.left)\n\
        \                if node.right: q.append(node.right)\n            if sum > maxSum:\n\
        \                maxSum = sum\n                maxLevel = level\n        return\
        \ maxLevel"
      c: "int maxLevelSum(struct TreeNode* root) {\n    if (!root) return 0;\n    int\
        \ maxSum = root->val;\n    int maxLevel = 1;\n    int level = 0;\n    struct\
        \ TreeNode** q = malloc(10000 * sizeof(struct TreeNode*));\n    int front =\
        \ 0, rear = 0;\n    q[rear++] = root;\n    while (front < rear) {\n        level++;\n\
        \        int size = rear - front;\n        int sum = 0;\n        for (int i\
        \ = 0; i < size; i++) {\n            struct TreeNode* node = q[front++];\n \
        \           sum += node->val;\n            if (node->left) q[rear++] = node->left;\n\
        \            if (node->right) q[rear++] = node->right;\n        }\n        if\
        \ (sum > maxSum) {\n            maxSum = sum;\n            maxLevel = level;\n\
        \        }\n    }\n    free(q);\n    return maxLevel;\n}"
      csharp: "public class Solution {\n    public int MaxLevelSum(TreeNode root) {\n\
        \        if (root == null) return 0;\n        int maxSum = int.MinValue;\n \
        \       int result = 0;\n        int level = 0;\n        var queue = new Queue<TreeNode>();\n\
        \        queue.Enqueue(root);\n        while (queue.Count > 0) {\n         \
        \   level++;\n            int levelSize = queue.Count;\n            int sum\
        \ = 0;\n            for (int i = 0; i < levelSize; i++) {\n                var\
        \ node = queue.Dequeue();\n                sum += node.val;\n              \
        \  if (node.left != null) queue.Enqueue(node.left);\n                if (node.right\
        \ != null) queue.Enqueue(node.right);\n            }\n            if (sum >\
        \ maxSum) {\n                maxSum = sum;\n                result = level;\n\
        \            }\n        }\n        return result;\n    }\n}"
      javascript: "var maxLevelSum = function(root) {\n    if (!root) return 0;\n  \
        \  let maxSum = -Infinity;\n    let result = 0;\n    let level = 0;\n    let\
        \ queue = [root];\n    while (queue.length > 0) {\n        level++;\n      \
        \  let levelSize = queue.length;\n        let sum = 0;\n        for (let i =\
        \ 0; i < levelSize; i++) {\n            let node = queue.shift();\n        \
        \    sum += node.val;\n            if (node.left) queue.push(node.left);\n \
        \           if (node.right) queue.push(node.right);\n        }\n        if (sum\
        \ > maxSum) {\n            maxSum = sum;\n            result = level;\n    \
        \    }\n    }\n    return result;\n};"
      typescript: "function maxLevelSum(root: TreeNode | null): number {\n    if (!root)\
        \ return 0;\n    let maxSum = -Infinity;\n    let result = 0;\n    let level\
        \ = 0;\n    let queue: TreeNode[] = [root];\n    while (queue.length > 0) {\n\
        \        level++;\n        let levelSize = queue.length;\n        let sum =\
        \ 0;\n        for (let i = 0; i < levelSize; i++) {\n            let node =\
        \ queue.shift() as TreeNode;\n            sum += node.val;\n            if (node.left)\
        \ queue.push(node.left);\n            if (node.right) queue.push(node.right);\n\
        \        }\n        if (sum > maxSum) {\n            maxSum = sum;\n       \
        \     result = level;\n        }\n    }\n    return result;\n}"
      php: "class Solution {\n    function maxLevelSum($root) {\n        if (!$root)\
        \ return 0;\n        $maxSum = -INF;\n        $result = 0;\n        $level =\
        \ 0;\n        $queue = array($root);\n        while (count($queue) > 0) {\n\
        \            $level++;\n            $levelSize = count($queue);\n          \
        \  $sum = 0;\n            for ($i = 0; $i < $levelSize; $i++) {\n          \
        \      $node = array_shift($queue);\n                $sum += $node->val;\n \
        \               if ($node->left) array_push($queue, $node->left);\n        \
        \        if ($node->right) array_push($queue, $node->right);\n            }\n\
        \            if ($sum > $maxSum) {\n                $maxSum = $sum;\n      \
        \          $result = $level;\n            }\n        }\n        return $result;\n\
        \    }\n}"
      swift: "class Solution {\n    func maxLevelSum(_ root: TreeNode?) -> Int {\n \
        \       guard let root = root else { return 0 }\n        var maxSum = Int.min\n\
        \        var result = 0\n        var level = 0\n        var queue: [TreeNode]\
        \ = [root]\n        while !queue.isEmpty {\n            level += 1\n       \
        \     let levelSize = queue.count\n            var sum = 0\n            for\
        \ _ in 0..<levelSize {\n                let node = queue.removeFirst()\n   \
        \             sum += node.val\n                if let left = node.left { queue.append(left)\
        \ }\n                if let right = node.right { queue.append(right) }\n   \
        \         }\n            if sum > maxSum {\n                maxSum = sum\n \
        \               result = level\n            }\n        }\n        return result\n\
        \    }\n}"
      kotlin: "class Solution {\n    fun maxLevelSum(root: TreeNode?): Int {\n     \
        \   if (root == null) return 0\n        var maxSum = Int.MIN_VALUE\n       \
        \ var maxLevel = 0\n        var level = 0\n        val queue = mutableListOf(root)\n\
        \        while (queue.isNotEmpty()) {\n            level++\n            val\
        \ levelSize = queue.size\n            var sum = 0\n            for (i in 0 until\
        \ levelSize) {\n                val node = queue.removeAt(0)\n             \
        \   sum += node.`val`\n                if (node.left != null) queue.add(node.left)\n\
        \                if (node.right != null) queue.add(node.right)\n           \
        \ }\n            if (sum > maxSum) {\n                maxSum = sum\n       \
        \         maxLevel = level\n            }\n        }\n        return maxLevel\n\
        \    }\n}"
      dart: "class Solution {\n  int maxLevelSum(TreeNode? root) {\n    if (root ==\
        \ null) return 0;\n    int maxSum = -100000;\n    int maxLevel = 0;\n    int\
        \ level = 0;\n    List<TreeNode?> queue = [root];\n    while (queue.isNotEmpty)\
        \ {\n      level++;\n      int levelSize = queue.length;\n      int sum = 0;\n\
        \      for (int i = 0; i < levelSize; i++) {\n        TreeNode? node = queue.removeAt(0);\n\
        \        sum += node!.val;\n        if (node.left != null) queue.add(node.left);\n\
        \        if (node.right != null) queue.add(node.right);\n      }\n      if (sum\
        \ > maxSum) {\n        maxSum = sum;\n        maxLevel = level;\n      }\n \
        \   }\n    return maxLevel;\n  }\n}"
      go: "func maxLevelSum(root *TreeNode) int {\n    if root == nil {\n        return\
        \ 0\n    }\n    maxSum := math.MinInt32\n    maxLevel := 0\n    level := 0\n\
        \    queue := []*TreeNode{root}\n    for len(queue) > 0 {\n        level++\n\
        \        levelSize := len(queue)\n        sum := 0\n        for i := 0; i <\
        \ levelSize; i++ {\n            node := queue[0]\n            queue = queue[1:]\n\
        \            sum += node.Val\n            if node.Left != nil {\n          \
        \      queue = append(queue, node.Left)\n            }\n            if node.Right\
        \ != nil {\n                queue = append(queue, node.Right)\n            }\n\
        \        }\n        if sum > maxSum {\n            maxSum = sum\n          \
        \  maxLevel = level\n        }\n    }\n    return maxLevel\n}"
      ruby: "def max_level_sum(root)\n    return 0 if root.nil?\n    max_sum = -100000\n\
        \    max_level = 0\n    level = 0\n    queue = [root]\n    while !queue.empty?\n\
        \        level += 1\n        level_size = queue.size\n        sum = 0\n    \
        \    level_size.times do\n            node = queue.shift\n            sum +=\
        \ node.val\n            queue.push(node.left) if !node.left.nil?\n         \
        \   queue.push(node.right) if !node.right.nil?\n        end\n        if sum\
        \ > max_sum\n            max_sum = sum\n            max_level = level\n    \
        \    end\n    end\n    max_level\nend"
      scala: "object Solution {\n    def maxLevelSum(root: TreeNode): Int = {\n    \
        \    if (root == null) return 0\n        var maxSum = Int.MinValue\n       \
        \ var maxLevel = 0\n        var level = 0\n        val queue = scala.collection.mutable.Queue[TreeNode](root)\n\
        \        while (queue.nonEmpty) {\n            level += 1\n            val levelSize\
        \ = queue.size\n            var sum = 0\n            for (i <- 0 until levelSize)\
        \ {\n                val node = queue.dequeue()\n                sum += node.value\n\
        \                if (node.left != null) queue.enqueue(node.left)\n         \
        \       if (node.right != null) queue.enqueue(node.right)\n            }\n \
        \           if (sum > maxSum) {\n                maxSum = sum\n            \
        \    maxLevel = level\n            }\n        }\n        maxLevel\n    }\n}"
      rust: "use std::rc::Rc;\nuse std::cell::RefCell;\nuse std::collections::VecDeque;\n\
        \nimpl Solution {\n    pub fn max_level_sum(root: Option<Rc<RefCell<TreeNode>>>)\
        \ -> i32 {\n        if root.is_none() {\n            return 0;\n        }\n\
        \        let mut max_sum = i32::MIN;\n        let mut max_level = 0;\n     \
        \   let mut level = 0;\n        let mut queue = VecDeque::new();\n        queue.push_back(root);\n\
        \        while !queue.is_empty() {\n            level += 1;\n            let\
        \ mut sum = 0;\n            let mut size = queue.len();\n            for _ in\
        \ 0..size {\n                if let Some(node) = queue.pop_front() {\n     \
        \               sum += node.as_ref().unwrap().borrow().val;\n              \
        \      if let Some(left) = node.as_ref().unwrap().borrow().left.clone() {\n\
        \                        queue.push_back(left);\n                    }\n   \
        \                 if let Some(right) = node.as_ref().unwrap().borrow().right.clone()\
        \ {\n                        queue.push_back(right);\n                    }\n\
        \                }\n            }\n            if sum > max_sum {\n        \
        \        max_sum = sum;\n                max_level = level;\n            }\n\
        \        }\n        max_level\n    }\n}"
      racket: "define/contract (max-level-sum root)\n  (-> (or/c tree-node? #f) exact-integer?)\n\
        \  (if (not root)\n      0\n      (let* ([max-sum -100000]\n             [max-level\
        \ 0]\n             [level 0]\n             [queue (list root)])\n        (let\
        \ loop ([queue queue]\n                   [level level])\n          (if (null?\
        \ queue)\n              max-level\n              (let* ([sum 0]\n          \
        \           [size (length queue)])\n                (for ([node queue])\n  \
        \                (set! sum (+ sum (tree-node-val node))))\n                (if\
        \ (> sum max-sum)\n                    (set! max-sum sum)\n                \
        \    (set! max-level (add1 level)))\n                (loop (append (map (lambda\
        \ (node) (tree-node-left node)) queue)\n                              (map (lambda\
        \ (node) (tree-node-right node)) queue))\n                      (add1 level))))))))"
      erlang: 'max_level_sum(Root) ->

        case Root of

        null -> 0;

        #tree_node{val = Val, left = Left, right = Right} ->

        MaxSum = -100000,

        MaxLevel = 0,

        Level = 0,

        Queue = [Root],

        max_level_sum(Level, MaxSum, MaxLevel, Queue, [])

        end.


        max_level_sum(Level, MaxSum, MaxLevel, [], Acc) ->

        MaxLevel;

        max_level_sum(Level, MaxSum, MaxLevel, [Node | Queue], Acc) ->

        Val = Node#tree_node.val,

        Left = Node#tree_node.left,

        Right = Node#tree_node.right,

        Sum = lists:sum([Val | Acc]),

        case Sum > MaxSum of

        true -> max_level_sum(Level + 1, Sum, Level + 1, Queue ++ [Left, Right], []);

        false -> max_level_sum(Level + 1, MaxSum, MaxLevel, Queue ++ [Left, Right],
        [])

        end.'
      elixir: "defmodule Solution do\n  @spec max_level_sum(root :: TreeNode.t | nil)\
        \ :: integer\n  def max_level_sum(root) do\n    if is_nil(root) do\n      0\n\
        \    else\n      max_sum = -100_000\n      max_level = 0\n      level = 0\n\
        \      queue = [root]\n      max_level_sum(queue, level, max_sum, max_level)\n\
        \    end\n  end\n\n  defp max_level_sum([], _level, max_sum, max_level), do:\
        \ max_level\n\n  defp max_level_sum(queue, level, max_sum, max_level) do\n \
        \   sum = Enum.reduce(queue, 0, fn node, acc -> acc + node.val end)\n    if\
        \ sum > max_sum do\n      max_level_sum(Enum.flat_map(queue, fn node -> [node.left,\
        \ node.right] end), level + 1, sum, level + 1)\n    else\n      max_level_sum(Enum.flat_map(queue,\
        \ fn node -> [node.left, node.right] end), level + 1, max_sum, max_level)\n\
        \    end\n  end\nend"
    approach: The algorithm works by performing a level-order traversal of the binary
      tree, keeping track of the sum of node values at each level. This is achieved
      by using a queue to store nodes at each level, and then processing these nodes
      to calculate the sum of their values. The level with the maximum sum is updated
      as we traverse the tree. The key intuition here is to recognize that a level-order
      traversal allows us to efficiently process nodes level by level, making it straightforward
      to calculate the sum of node values at each level. By maintaining a running maximum
      sum and the corresponding level, we can easily identify the level with the maximum
      sum once the traversal is complete.
    time_complexity: The time complexity of this algorithm is O(N), where N is the number
      of nodes in the binary tree. This is because we visit each node exactly once during
      the level-order traversal, performing a constant amount of work for each node.
      The space complexity is also O(N) in the worst case, which occurs when the binary
      tree is a complete binary tree and we need to store all nodes at the last level
      in the queue.
    space_complexity: The space complexity of this algorithm is O(N), where N is the
      number of nodes in the binary tree. This is because in the worst case, we may
      need to store all nodes at the last level in the queue, which can happen if the
      binary tree is a complete binary tree. However, in the average case, the space
      complexity will be much less than O(N) since we only need to store nodes at the
      current level in the queue.
    elapsed_time: 11.778488397598267
    model: llama-3.3-70b-versatile
    generated_at: '2026-01-06 01:11:21 '
---

## Problem #1161: Maximum Level Sum of a Binary Tree

**Difficulty:** Medium

**Topics:** Tree, Depth-First Search, Breadth-First Search, Binary Tree

## Problem Description

<p>Given the <code>root</code> of a binary tree, the level of its root is <code>1</code>, the level of its children is <code>2</code>, and so on.</p>

<p>Return the <strong>smallest</strong> level <code>x</code> such that the sum of all the values of nodes at level <code>x</code> is <strong>maximal</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/05/03/capture.JPG" style="width: 200px; height: 175px;" />
<pre>
<strong>Input:</strong> root = [1,7,0,7,-8,null,null]
<strong>Output:</strong> 2
<strong>Explanation: </strong>
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = [989,null,10250,98693,-89388,null,null,null,-32127]
<strong>Output:</strong> 2
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 10<sup>4</sup>]</code>.</li>
	<li><code>-10<sup>5</sup> &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
</ul>


## Hints

1. Calculate the sum for each level then find the level with the maximum sum.

2. How can you traverse the tree ?

3. How can you sum up the values for every level ?

4. Use DFS or BFS to traverse the tree keeping the level of each node, and sum up those values with a map or a frequency array.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2026-01-06 01:10:54 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem requires finding the level with the maximum sum of node values, returning the smallest such level if multiple levels have the same maximum sum. This is a classic Breadth-First Search (BFS) problem, as BFS naturally processes a tree level by level. We use a queue to manage nodes to visit, ensuring that all nodes at a given level are processed before moving to the next level.

We initialize a variable for the maximum sum found so far (`maxSum`) to a very small value and a variable for the corresponding level (`maxLevel`) to 1. We also maintain a `currentLevel` counter. The BFS starts by adding the root to the queue. In each iteration of the main loop, we process all nodes currently in the queue, which represent all nodes at the `currentLevel`. We calculate their sum (`currentLevelSum`) and enqueue their non-null children. After processing all nodes for the `currentLevel`, we compare `currentLevelSum` with `maxSum`. If `currentLevelSum` is greater, we update `maxSum` and `maxLevel`. We then increment `currentLevel` and repeat until the queue is empty. Since we iterate levels in increasing order, the first level encountered with the maximum sum will be the smallest, satisfying the problem's requirement.

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
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
#include <queue>
#include <limits>

class Solution {
public:
    int maxLevelSum(TreeNode* root) {
        // According to constraints, root is never null (1 <= N <= 10^4).
        // if (!root) {
        //     return 0;
        // }

        std::queue<TreeNode*> q;
        q.push(root);

        long long max_sum = std::numeric_limits<long long>::min();
        int max_level = 1;
        int current_level = 1;

        while (!q.empty()) {
            int level_size = q.size();
            long long current_level_sum = 0;

            for (int i = 0; i < level_size; ++i) {
                TreeNode* node = q.front();
                q.pop();
                current_level_sum += node->val;

                if (node->left) {
                    q.push(node->left);
                }
                if (node->right) {
                    q.push(node->right);
                }
            }

            if (current_level_sum > max_sum) {
                max_sum = current_level_sum;
                max_level = current_level;
            }
            current_level++;
        }

        return max_level;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}S
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
import java.util.LinkedList;
import java.util.Queue;

class Solution {
    public int maxLevelSum(TreeNode root) {
        // According to constraints, root is never null (1 <= N <= 10^4).
        // if (root == null) {
        //     return 0;
        // }

        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);

        long max_sum = Long.MIN_VALUE;
        int max_level = 1;
        int current_level = 1;

        while (!q.isEmpty()) {
            int level_size = q.size();
            long current_level_sum = 0;

            for (int i = 0; i < level_size; ++i) {
                TreeNode node = q.poll();
                current_level_sum += node.val;

                if (node.left != null) {
                    q.offer(node.left);
                }
                if (node.right != null) {
                    q.offer(node.right);
                }
            }

            if (current_level_sum > max_sum) {
                max_sum = current_level_sum;
                max_level = current_level;
            }
            current_level++;
        }

        return max_level;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections

class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # According to constraints, root is never null (1 <= N <= 10^4).
        # if not root:
        #     return 0

        q = collections.deque([root])

        max_sum = float('-inf')
        max_level = 1
        current_level = 1

        while q:
            level_size = len(q)
            current_level_sum = 0

            for _ in range(level_size):
                node = q.popleft()
                current_level_sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if current_level_sum > max_sum:
                max_sum = current_level_sum
                max_level = current_level
            current_level += 1

        return max_level
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # According to constraints, root is never null (1 <= N <= 10^4).
        # if not root:
        #     return 0

        q = collections.deque([root])

        max_sum = float('-inf')
        max_level = 1
        current_level = 1

        while q:
            level_size = len(q)
            current_level_sum = 0

            for _ in range(level_size):
                node = q.popleft()
                current_level_sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if current_level_sum > max_sum:
                max_sum = current_level_sum
                max_level = current_level
            current_level += 1

        return max_level
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
#include <limits.h>
#include <stdlib.h> // Not strictly needed for static array, but good practice for dynamic.

// Max nodes is 10^4. A static array for queue is sufficient.
#define MAX_NODES 10001 

int maxLevelSum(struct TreeNode* root) {
    // According to constraints, root is never null (1 <= N <= 10^4).
    // if (root == NULL) {
    //     return 0;
    // }

    struct TreeNode* q[MAX_NODES];
    int head = 0;
    int tail = 0;

    q[tail++] = root;

    long long max_sum = LLONG_MIN; // Use long long for sums to prevent overflow
    int max_level = 1;
    int current_level = 1;

    while (head < tail) {
        int level_nodes_count = tail - head;
        long long current_level_sum = 0;

        for (int i = 0; i < level_nodes_count; ++i) {
            struct TreeNode* node = q[head++];
            current_level_sum += node->val;

            if (node->left) {
                q[tail++] = node->left;
            }
            if (node->right) {
                q[tail++] = node->right;
            }
        }

        if (current_level_sum > max_sum) {
            max_sum = current_level_sum;
            max_level = current_level;
        }
        current_level++;
    }

    return max_level;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    public int MaxLevelSum(TreeNode root) {
        if (root == null) {
            return 0; // Constraints say root is never null, but good practice.
        }

        int maxSum = root.val;
        int maxLevel = 1;
        int currentLevel = 1;

        Queue<TreeNode> queue = new Queue<TreeNode>();
        queue.Enqueue(root);

        while (queue.Count > 0) {
            int levelSize = queue.Count;
            int currentLevelSum = 0;

            for (int i = 0; i < levelSize; i++) {
                TreeNode node = queue.Dequeue();
                currentLevelSum += node.val;

                if (node.left != null) {
                    queue.Enqueue(node.left);
                }
                if (node.right != null) {
                    queue.Enqueue(node.right);
                }
            }

            if (currentLevelSum > maxSum) {
                maxSum = currentLevelSum;
                maxLevel = currentLevel;
            }
            currentLevel++;
        }

        return maxLevel;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxLevelSum = function(root) {
    if (!root) {
        return 0;
    }

    let maxSum = root.val;
    let maxLevel = 1;
    let currentLevel = 1;

    let queue = [root];

    while (queue.length > 0) {
        let levelSize = queue.length;
        let currentLevelSum = 0;

        for (let i = 0; i < levelSize; i++) {
            let node = queue.shift();
            currentLevelSum += node.val;

            if (node.left) {
                queue.push(node.left);
            }
            if (node.right) {
                queue.push(node.right);
            }
        }

        if (currentLevelSum > maxSum) {
            maxSum = currentLevelSum;
            maxLevel = currentLevel;
        }
        currentLevel++;
    }

    return maxLevel;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function maxLevelSum(root: TreeNode | null): number {
    if (!root) {
        return 0;
    }

    let maxSum: number = root.val;
    let maxLevel: number = 1;
    let currentLevel: number = 1;

    let queue: TreeNode[] = [root];

    while (queue.length > 0) {
        let levelSize: number = queue.length;
        let currentLevelSum: number = 0;

        for (let i = 0; i < levelSize; i++) {
            let node: TreeNode = queue.shift()!;
            currentLevelSum += node.val;

            if (node.left) {
                queue.push(node.left);
            }
            if (node.right) {
                queue.push(node.right);
            }
        }

        if (currentLevelSum > maxSum) {
            maxSum = currentLevelSum;
            maxLevel = currentLevel;
        }
        currentLevel++;
    }

    return maxLevel;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     public $val = null;
 *     public $left = null;
 *     public $right = null;
 *     function __construct($val = 0, $left = null, $right = null) {
 *         $this->val = $val;
 *         $this->left = $left;
 *         $this->right = $right;
 *     }
 * }
 */
class Solution {

    /**
     * @param TreeNode $root
     * @return Integer
     */
    function maxLevelSum($root) {
        if ($root === null) {
            return 0;
        }

        $maxSum = $root->val;
        $maxLevel = 1;
        $currentLevel = 1;

        $queue = new SplQueue();
        $queue->enqueue($root);

        while (!$queue->isEmpty()) {
            $levelSize = $queue->count();
            $currentLevelSum = 0;

            for ($i = 0; $i < $levelSize; $i++) {
                $node = $queue->dequeue();
                $currentLevelSum += $node->val;

                if ($node->left !== null) {
                    $queue->enqueue($node->left);
                }
                if ($node->right !== null) {
                    $queue->enqueue($node->right);
                }
            }

            if ($currentLevelSum > $maxSum) {
                $maxSum = $currentLevelSum;
                $maxLevel = $currentLevel;
            }
            $currentLevel++;
        }

        return $maxLevel;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public var val: Int
 *     public var left: TreeNode?
 *     public var right: TreeNode?
 *     public init() { self.val = 0; self.left = nil; self.right = nil; }
 *     public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil; }
 *     public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
 *         self.val = val
 *         self.left = left
 *         self.right = right
 *     }
 * }
 */
class Solution {
    func maxLevelSum(_ root: TreeNode?) -> Int {
        guard let root = root else {
            return 0 // Constraints say root is never null, but good practice.
        }

        var maxSum = root.val
        var maxLevel = 1
        var currentLevel = 1

        var queue: [TreeNode] = [root]

        while !queue.isEmpty {
            let levelSize = queue.count
            var currentLevelSum = 0

            for _ in 0..<levelSize {
                let node = queue.removeFirst()
                currentLevelSum += node.val

                if let leftChild = node.left {
                    queue.append(leftChild)
                }
                if let rightChild = node.right {
                    queue.append(rightChild)
                }
            }

            if currentLevelSum > maxSum {
                maxSum = currentLevelSum
                maxLevel = currentLevel
            }
            currentLevel += 1
        }

        return maxLevel
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
import java.util.LinkedList
import java.util.Queue

/**
 * Example:
 * var ti = TreeNode(5)
 * var v = ti.`val`
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */
class Solution {
    fun maxLevelSum(root: TreeNode?): Int {
        if (root == null) {
            return 0
        }

        var maxSum = Int.MIN_VALUE
        var maxLevel = 1
        var currentLevel = 1

        val queue: Queue<TreeNode> = LinkedList()
        queue.offer(root)

        while (queue.isNotEmpty()) {
            val levelSize = queue.size
            var currentLevelSum = 0

            for (i in 0 until levelSize) {
                val node = queue.poll()
                currentLevelSum += node.`val`

                node.left?.let { queue.offer(it) }
                node.right?.let { queue.offer(it) }
            }

            if (currentLevelSum > maxSum) {
                maxSum = currentLevelSum
                maxLevel = currentLevel
            }
            currentLevel++
        }
        return maxLevel
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
import 'dart:collection';

/**
 * Definition for a binary tree node.
 * class TreeNode {
 *   int val;
 *   TreeNode? left;
 *   TreeNode? right;
 *   TreeNode([this.val = 0, this.left, this.right]);
 * }
 */
class Solution {
  int maxLevelSum(TreeNode? root) {
    if (root == null) {
      return 0;
    }

    int maxSum = -2147483648; // A very small integer, equivalent to Int.MIN_VALUE
    int maxLevel = 1;
    int currentLevel = 1;

    Queue<TreeNode> queue = Queue<TreeNode>();
    queue.add(root);

    while (queue.isNotEmpty) {
      int levelSize = queue.length;
      int currentLevelSum = 0;

      for (int i = 0; i < levelSize; i++) {
        TreeNode node = queue.removeFirst();
        currentLevelSum += node.val;

        if (node.left != null) {
          queue.add(node.left!); // Use ! for null safety after check
        }
        if (node.right != null) {
          queue.add(node.right!); // Use ! for null safety after check
        }
      }

      if (currentLevelSum > maxSum) {
        maxSum = currentLevelSum;
        maxLevel = currentLevel;
      }
      currentLevel++;
    }
    return maxLevel;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import (
	"container/list"
	"math"
)

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func maxLevelSum(root *TreeNode) int {
    if root == nil {
        return 0
    }

    maxSum := math.MinInt64
    maxLevel := 1
    currentLevel := 1

    queue := list.New()
    queue.PushBack(root)

    for queue.Len() > 0 {
        levelSize := queue.Len()
        currentLevelSum := 0

        for i := 0; i < levelSize; i++ {
            element := queue.Remove(queue.Front())
            node := element.(*TreeNode)
            currentLevelSum += node.Val

            if node.Left != nil {
                queue.PushBack(node.Left)
            }
            if node.Right != nil {
                queue.PushBack(node.Right)
            }
        }

        if currentLevelSum > maxSum {
            maxSum = currentLevelSum
            maxLevel = currentLevel
        }
        currentLevel++
    }
    return maxLevel
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end
# @param {TreeNode} root
# @return {Integer}
def max_level_sum(root)
    return 0 if root.nil?

    max_sum = -Float::INFINITY
    max_level = 1
    current_level = 1

    queue = []
    queue.push(root)

    while !queue.empty?
        level_size = queue.length
        current_level_sum = 0

        level_size.times do
            node = queue.shift # Dequeue from front
            current_level_sum += node.val

            queue.push(node.left) if node.left
            queue.push(node.right) if node.right
        end

        if current_level_sum > max_sum
            max_sum = current_level_sum
            max_level = current_level
        end
        current_level += 1
    end
    max_level
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.collection.mutable

/**
 * Definition for a binary tree node.
 * class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
 *   var value: Int = _value
 *   var left: TreeNode = _left
 *   var right: TreeNode = _right
 * }
 */
object Solution {
    def maxLevelSum(root: TreeNode): Int = {
        if (root == null) {
            return 0
        }

        var maxSum: Int = Int.MinValue
        var maxLevel: Int = 1
        var currentLevel: Int = 1

        val queue = mutable.Queue[TreeNode]()
        queue.enqueue(root)

        while (queue.nonEmpty) {
            val levelSize = queue.size
            var currentLevelSum: Int = 0

            for (_ <- 0 until levelSize) {
                val node = queue.dequeue()
                currentLevelSum += node.value

                if (node.left != null) {
                    queue.enqueue(node.left)
                }
                if (node.right != null) {
                    queue.enqueue(node.right)
                }
            }

            if (currentLevelSum > maxSum) {
                maxSum = currentLevelSum
                maxLevel = currentLevel
            }
            currentLevel += 1
        }
        maxLevel
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
use std::rc::Rc;
use std::cell::RefCell;
use std::collections::VecDeque;

impl Solution {
    pub fn max_level_sum(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut max_sum = i32::MIN;
        let mut max_level = 0; // Will be 1-indexed
        let mut current_level = 1;

        let mut q: VecDeque<Rc<RefCell<TreeNode>>> = VecDeque::new();
        if let Some(node) = root {
            q.push_back(node);
        } else {
            // According to constraints, root is never null, but good practice.
            return 0;
        }

        while !q.is_empty() {
            let level_size = q.len();
            let mut current_level_sum = 0;

            for _ in 0..level_size {
                if let Some(node_rc) = q.pop_front() {
                    let node = node_rc.borrow();
                    current_level_sum += node.val;

                    if let Some(left_child) = node.left.clone() {
                        q.push_back(left_child);
                    }
                    if let Some(right_child) = node.right.clone() {
                        q.push_back(right_child);
                    }
                }
            }

            if current_level_sum > max_sum {
                max_sum = current_level_sum;
                max_level = current_level;
            }
            current_level += 1;
        }

        max_level
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
; Definition for a binary tree node.
#|

; val : integer?
; left : (or/c tree-node? #f)
; right : (or/c tree-node? #f)
(struct tree-node
  (val left right) #:mutable #:transparent)

; constructor
(define (make-tree-node [val 0])
  (tree-node val #f #f))

|#

(define/contract (max-level-sum root)
  (-> (or/c tree-node? #f) exact-integer?)
  (if (not root)
      0 ; According to constraints, root is never #f, but good practice.
      (let loop ((q (list root))
                 (max-sum -1000000001) ; Initialize with a value smaller than any possible sum
                 (max-level 0)
                 (current-level 1))
        (if (empty? q)
            max-level
            (let* ((level-size (length q))
                   (current-level-nodes (take q level-size))
                   (next-q (drop q level-size))
                   (current-level-sum (for/sum ([node current-level-nodes])
                                        (tree-node-val node))))
              (let ((new-max-sum (if (> current-level-sum max-sum)
                                     current-level-sum
                                     max-sum))
                    (new-max-level (if (> current-level-sum max-sum)
                                       current-level
                                       max-level)))
                (let ((next-q-children (for/fold ((children '()))
                                                  ([node current-level-nodes])
                                        (let ((left (tree-node-left node))
                                              (right (tree-node-right node)))
                                          (append children
                                                  (if left (list left) '())
                                                  (if right (list right) '()))))))
                  (loop (append next-q next-q-children)
                        new-max-sum
                        new-max-level
                        (+ current-level 1)))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
%% Definition for a binary tree node.
%%
%% -record(tree_node, {val = 0 :: integer(),
%%                     left = null  :: 'null' | #tree_node{},
%%                     right = null :: 'null' | #tree_node{}}).

-spec max_level_sum(Root :: #tree_node{} | null) -> integer().
max_level_sum(Root) ->
  case Root of
    null -> 0; % Constraints say root is never null
    _ -> bfs_level([Root], -1000000001, 0, 1) % Queue, MaxSum, MaxLevel, CurrentLevel
  end.

bfs_level([], _MaxSum, MaxLevel, _CurrentLevel) ->
  MaxLevel;
bfs_level(CurrentLevelNodes, MaxSum, MaxLevel, CurrentLevel) ->
  CurrentLevelSum = lists:sum([Node#tree_node.val || Node <- CurrentLevelNodes]),

  {NewMaxSum, NewMaxLevel} = 
    if CurrentLevelSum > MaxSum -> {CurrentLevelSum, CurrentLevel};
       true -> {MaxSum, MaxLevel}
    end,

  NextLevelNodes = lists:foldl(fun(Node, Acc) ->
                                 Left = Node#tree_node.left,
                                 Right = Node#tree_node.right,
                                 Acc1 = case Left of null -> Acc; _ -> Acc ++ [Left] end,
                                 case Right of null -> Acc1; _ -> Acc1 ++ [Right] end
                               end, [], CurrentLevelNodes),

  bfs_level(NextLevelNodes, NewMaxSum, NewMaxLevel, CurrentLevel + 1).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
# Definition for a binary tree node.
#
# defmodule TreeNode do
#   @type t :: %__MODULE__{}
#   defstruct val: 0, left: nil, right: nil
# end

defmodule Solution do
  @spec max_level_sum(root :: TreeNode.t | nil) :: integer
  def max_level_sum(root) do
    case root do
      nil -> 0 # Constraints say root is never nil
      _ -> bfs([root], -1_000_000_001, 0, 1) # Queue, MaxSum, MaxLevel, CurrentLevel
    end
  end

  defp bfs([], _max_sum, max_level, _current_level), do: max_level
  defp bfs(current_level_nodes, max_sum, max_level, current_level) do
    current_level_sum = Enum.sum(Enum.map(current_level_nodes, &(&1.val)))

    {new_max_sum, new_max_level} = 
      if current_level_sum > max_sum do
        {current_level_sum, current_level}
      else
        {max_sum, max_level}
      end

    next_level_nodes = 
      Enum.flat_map(current_level_nodes, fn node ->
        children = []
        children = if node.left, do: [node.left | children], else: children
        children = if node.right, do: [node.right | children], else: children
        children
      end)

    bfs(next_level_nodes, new_max_sum, new_max_level, current_level + 1)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is O(N), where N is the number of nodes in the binary tree. This is because each node is visited and processed exactly once: it is enqueued once and dequeued once. The operations within the loop (summing values, adding children to the queue) take constant time per node.

- **Space Complexity:** The space complexity is O(W), where W is the maximum width of the binary tree. In the worst-case scenario, such as a complete binary tree, the queue might hold up to N/2 nodes at the widest level, making the space complexity O(N). In the best case, for a skewed tree, the queue would only hold one node at a time, resulting in O(1) space.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2026-01-06 01:11:21 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The algorithm works by performing a level-order traversal of the binary tree, keeping track of the sum of node values at each level. This is achieved by using a queue to store nodes at each level, and then processing these nodes to calculate the sum of their values. The level with the maximum sum is updated as we traverse the tree. The key intuition here is to recognize that a level-order traversal allows us to efficiently process nodes level by level, making it straightforward to calculate the sum of node values at each level. By maintaining a running maximum sum and the corresponding level, we can easily identify the level with the maximum sum once the traversal is complete.

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
    int maxLevelSum(TreeNode* root) {
        if (!root) return 0;
        int maxSum = root->val;
        int maxLevel = 1;
        int level = 0;
        std::queue<TreeNode*> q;
        q.push(root);
        while (!q.empty()) {
            level++;
            int size = q.size();
            int sum = 0;
            for (int i = 0; i < size; i++) {
                TreeNode* node = q.front();
                q.pop();
                sum += node->val;
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            if (sum > maxSum) {
                maxSum = sum;
                maxLevel = level;
            }
        }
        return maxLevel;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int maxLevelSum(TreeNode root) {
        if (root == null) return 0;
        int maxSum = root.val;
        int maxLevel = 1;
        int level = 0;
        java.util.Queue<TreeNode> q = new java.util.LinkedList<>();
        q.add(root);
        while (!q.isEmpty()) {
            level++;
            int size = q.size();
            int sum = 0;
            for (int i = 0; i < size; i++) {
                TreeNode node = q.poll();
                sum += node.val;
                if (node.left != null) q.add(node.left);
                if (node.right != null) q.add(node.right);
            }
            if (sum > maxSum) {
                maxSum = sum;
                maxLevel = level;
            }
        }
        return maxLevel;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def maxLevelSum(self, root):
        if not root: return 0
        maxSum = root.val
        maxLevel = 1
        level = 0
        q = []
        q.append(root)
        while q:
            level += 1
            size = len(q)
            sum = 0
            for _ in range(size):
                node = q.pop(0)
                sum += node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            if sum > maxSum:
                maxSum = sum
                maxLevel = level
        return maxLevel
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        maxSum = root.val
        maxLevel = 1
        level = 0
        q = []
        q.append(root)
        while q:
            level += 1
            size = len(q)
            sum = 0
            for _ in range(size):
                node = q.pop(0)
                sum += node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            if sum > maxSum:
                maxSum = sum
                maxLevel = level
        return maxLevel
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int maxLevelSum(struct TreeNode* root) {
    if (!root) return 0;
    int maxSum = root->val;
    int maxLevel = 1;
    int level = 0;
    struct TreeNode** q = malloc(10000 * sizeof(struct TreeNode*));
    int front = 0, rear = 0;
    q[rear++] = root;
    while (front < rear) {
        level++;
        int size = rear - front;
        int sum = 0;
        for (int i = 0; i < size; i++) {
            struct TreeNode* node = q[front++];
            sum += node->val;
            if (node->left) q[rear++] = node->left;
            if (node->right) q[rear++] = node->right;
        }
        if (sum > maxSum) {
            maxSum = sum;
            maxLevel = level;
        }
    }
    free(q);
    return maxLevel;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MaxLevelSum(TreeNode root) {
        if (root == null) return 0;
        int maxSum = int.MinValue;
        int result = 0;
        int level = 0;
        var queue = new Queue<TreeNode>();
        queue.Enqueue(root);
        while (queue.Count > 0) {
            level++;
            int levelSize = queue.Count;
            int sum = 0;
            for (int i = 0; i < levelSize; i++) {
                var node = queue.Dequeue();
                sum += node.val;
                if (node.left != null) queue.Enqueue(node.left);
                if (node.right != null) queue.Enqueue(node.right);
            }
            if (sum > maxSum) {
                maxSum = sum;
                result = level;
            }
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
var maxLevelSum = function(root) {
    if (!root) return 0;
    let maxSum = -Infinity;
    let result = 0;
    let level = 0;
    let queue = [root];
    while (queue.length > 0) {
        level++;
        let levelSize = queue.length;
        let sum = 0;
        for (let i = 0; i < levelSize; i++) {
            let node = queue.shift();
            sum += node.val;
            if (node.left) queue.push(node.left);
            if (node.right) queue.push(node.right);
        }
        if (sum > maxSum) {
            maxSum = sum;
            result = level;
        }
    }
    return result;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maxLevelSum(root: TreeNode | null): number {
    if (!root) return 0;
    let maxSum = -Infinity;
    let result = 0;
    let level = 0;
    let queue: TreeNode[] = [root];
    while (queue.length > 0) {
        level++;
        let levelSize = queue.length;
        let sum = 0;
        for (let i = 0; i < levelSize; i++) {
            let node = queue.shift() as TreeNode;
            sum += node.val;
            if (node.left) queue.push(node.left);
            if (node.right) queue.push(node.right);
        }
        if (sum > maxSum) {
            maxSum = sum;
            result = level;
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
    function maxLevelSum($root) {
        if (!$root) return 0;
        $maxSum = -INF;
        $result = 0;
        $level = 0;
        $queue = array($root);
        while (count($queue) > 0) {
            $level++;
            $levelSize = count($queue);
            $sum = 0;
            for ($i = 0; $i < $levelSize; $i++) {
                $node = array_shift($queue);
                $sum += $node->val;
                if ($node->left) array_push($queue, $node->left);
                if ($node->right) array_push($queue, $node->right);
            }
            if ($sum > $maxSum) {
                $maxSum = $sum;
                $result = $level;
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
    func maxLevelSum(_ root: TreeNode?) -> Int {
        guard let root = root else { return 0 }
        var maxSum = Int.min
        var result = 0
        var level = 0
        var queue: [TreeNode] = [root]
        while !queue.isEmpty {
            level += 1
            let levelSize = queue.count
            var sum = 0
            for _ in 0..<levelSize {
                let node = queue.removeFirst()
                sum += node.val
                if let left = node.left { queue.append(left) }
                if let right = node.right { queue.append(right) }
            }
            if sum > maxSum {
                maxSum = sum
                result = level
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
    fun maxLevelSum(root: TreeNode?): Int {
        if (root == null) return 0
        var maxSum = Int.MIN_VALUE
        var maxLevel = 0
        var level = 0
        val queue = mutableListOf(root)
        while (queue.isNotEmpty()) {
            level++
            val levelSize = queue.size
            var sum = 0
            for (i in 0 until levelSize) {
                val node = queue.removeAt(0)
                sum += node.`val`
                if (node.left != null) queue.add(node.left)
                if (node.right != null) queue.add(node.right)
            }
            if (sum > maxSum) {
                maxSum = sum
                maxLevel = level
            }
        }
        return maxLevel
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int maxLevelSum(TreeNode? root) {
    if (root == null) return 0;
    int maxSum = -100000;
    int maxLevel = 0;
    int level = 0;
    List<TreeNode?> queue = [root];
    while (queue.isNotEmpty) {
      level++;
      int levelSize = queue.length;
      int sum = 0;
      for (int i = 0; i < levelSize; i++) {
        TreeNode? node = queue.removeAt(0);
        sum += node!.val;
        if (node.left != null) queue.add(node.left);
        if (node.right != null) queue.add(node.right);
      }
      if (sum > maxSum) {
        maxSum = sum;
        maxLevel = level;
      }
    }
    return maxLevel;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func maxLevelSum(root *TreeNode) int {
    if root == nil {
        return 0
    }
    maxSum := math.MinInt32
    maxLevel := 0
    level := 0
    queue := []*TreeNode{root}
    for len(queue) > 0 {
        level++
        levelSize := len(queue)
        sum := 0
        for i := 0; i < levelSize; i++ {
            node := queue[0]
            queue = queue[1:]
            sum += node.Val
            if node.Left != nil {
                queue = append(queue, node.Left)
            }
            if node.Right != nil {
                queue = append(queue, node.Right)
            }
        }
        if sum > maxSum {
            maxSum = sum
            maxLevel = level
        }
    }
    return maxLevel
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def max_level_sum(root)
    return 0 if root.nil?
    max_sum = -100000
    max_level = 0
    level = 0
    queue = [root]
    while !queue.empty?
        level += 1
        level_size = queue.size
        sum = 0
        level_size.times do
            node = queue.shift
            sum += node.val
            queue.push(node.left) if !node.left.nil?
            queue.push(node.right) if !node.right.nil?
        end
        if sum > max_sum
            max_sum = sum
            max_level = level
        end
    end
    max_level
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def maxLevelSum(root: TreeNode): Int = {
        if (root == null) return 0
        var maxSum = Int.MinValue
        var maxLevel = 0
        var level = 0
        val queue = scala.collection.mutable.Queue[TreeNode](root)
        while (queue.nonEmpty) {
            level += 1
            val levelSize = queue.size
            var sum = 0
            for (i <- 0 until levelSize) {
                val node = queue.dequeue()
                sum += node.value
                if (node.left != null) queue.enqueue(node.left)
                if (node.right != null) queue.enqueue(node.right)
            }
            if (sum > maxSum) {
                maxSum = sum
                maxLevel = level
            }
        }
        maxLevel
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
use std::rc::Rc;
use std::cell::RefCell;
use std::collections::VecDeque;

impl Solution {
    pub fn max_level_sum(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        if root.is_none() {
            return 0;
        }
        let mut max_sum = i32::MIN;
        let mut max_level = 0;
        let mut level = 0;
        let mut queue = VecDeque::new();
        queue.push_back(root);
        while !queue.is_empty() {
            level += 1;
            let mut sum = 0;
            let mut size = queue.len();
            for _ in 0..size {
                if let Some(node) = queue.pop_front() {
                    sum += node.as_ref().unwrap().borrow().val;
                    if let Some(left) = node.as_ref().unwrap().borrow().left.clone() {
                        queue.push_back(left);
                    }
                    if let Some(right) = node.as_ref().unwrap().borrow().right.clone() {
                        queue.push_back(right);
                    }
                }
            }
            if sum > max_sum {
                max_sum = sum;
                max_level = level;
            }
        }
        max_level
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
define/contract (max-level-sum root)
  (-> (or/c tree-node? #f) exact-integer?)
  (if (not root)
      0
      (let* ([max-sum -100000]
             [max-level 0]
             [level 0]
             [queue (list root)])
        (let loop ([queue queue]
                   [level level])
          (if (null? queue)
              max-level
              (let* ([sum 0]
                     [size (length queue)])
                (for ([node queue])
                  (set! sum (+ sum (tree-node-val node))))
                (if (> sum max-sum)
                    (set! max-sum sum)
                    (set! max-level (add1 level)))
                (loop (append (map (lambda (node) (tree-node-left node)) queue)
                              (map (lambda (node) (tree-node-right node)) queue))
                      (add1 level))))))))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
max_level_sum(Root) ->
case Root of
null -> 0;
#tree_node{val = Val, left = Left, right = Right} ->
MaxSum = -100000,
MaxLevel = 0,
Level = 0,
Queue = [Root],
max_level_sum(Level, MaxSum, MaxLevel, Queue, [])
end.

max_level_sum(Level, MaxSum, MaxLevel, [], Acc) ->
MaxLevel;
max_level_sum(Level, MaxSum, MaxLevel, [Node | Queue], Acc) ->
Val = Node#tree_node.val,
Left = Node#tree_node.left,
Right = Node#tree_node.right,
Sum = lists:sum([Val | Acc]),
case Sum > MaxSum of
true -> max_level_sum(Level + 1, Sum, Level + 1, Queue ++ [Left, Right], []);
false -> max_level_sum(Level + 1, MaxSum, MaxLevel, Queue ++ [Left, Right], [])
end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec max_level_sum(root :: TreeNode.t | nil) :: integer
  def max_level_sum(root) do
    if is_nil(root) do
      0
    else
      max_sum = -100_000
      max_level = 0
      level = 0
      queue = [root]
      max_level_sum(queue, level, max_sum, max_level)
    end
  end

  defp max_level_sum([], _level, max_sum, max_level), do: max_level

  defp max_level_sum(queue, level, max_sum, max_level) do
    sum = Enum.reduce(queue, 0, fn node, acc -> acc + node.val end)
    if sum > max_sum do
      max_level_sum(Enum.flat_map(queue, fn node -> [node.left, node.right] end), level + 1, sum, level + 1)
    else
      max_level_sum(Enum.flat_map(queue, fn node -> [node.left, node.right] end), level + 1, max_sum, max_level)
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of this algorithm is O(N), where N is the number of nodes in the binary tree. This is because we visit each node exactly once during the level-order traversal, performing a constant amount of work for each node. The space complexity is also O(N) in the worst case, which occurs when the binary tree is a complete binary tree and we need to store all nodes at the last level in the queue.

- **Space Complexity:** The space complexity of this algorithm is O(N), where N is the number of nodes in the binary tree. This is because in the worst case, we may need to store all nodes at the last level in the queue, which can happen if the binary tree is a complete binary tree. However, in the average case, the space complexity will be much less than O(N) since we only need to store nodes at the current level in the queue.

</div>
</details>
