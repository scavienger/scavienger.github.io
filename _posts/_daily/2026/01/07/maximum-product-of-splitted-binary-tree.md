---
layout: post
title: "Maximum Product of Splitted Binary Tree"
date: 2026-01-07 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Tree", "Depth-First Search", "Binary Tree"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/
ai_solutions:
  - solutions:
      cpp: "/**\n * Definition for a binary tree node.\n * struct TreeNode {\n *   \
        \  int val;\n *     TreeNode *left;\n *     TreeNode *right;\n *     TreeNode()\
        \ : val(0), left(nullptr), right(nullptr) {}\n *     TreeNode(int x) : val(x),\
        \ left(nullptr), right(nullptr) {}\n *     TreeNode(int x, TreeNode *left, TreeNode\
        \ *right) : val(x), left(left), right(right) {}\n * };\n */\nclass Solution\
        \ {\npublic:\n    std::vector<long long> all_subtree_sums;\n\n    long long\
        \ dfs(TreeNode* node) {\n        if (!node) {\n            return 0;\n     \
        \   }\n\n        long long left_sum = dfs(node->left);\n        long long right_sum\
        \ = dfs(node->right);\n\n        long long current_subtree_sum = node->val +\
        \ left_sum + right_sum;\n        all_subtree_sums.push_back(current_subtree_sum);\n\
        \n        return current_subtree_sum;\n    }\n\n    int maxProduct(TreeNode*\
        \ root) {\n        all_subtree_sums.clear(); // Clear for multiple test cases\n\
        \        long long total_sum = dfs(root);\n\n        long long max_prod = 0;\n\
        \        long long MOD = 1e9 + 7;\n\n        for (long long s : all_subtree_sums)\
        \ {\n            max_prod = std::max(max_prod, s * (total_sum - s));\n     \
        \   }\n\n        return max_prod % MOD;\n    }\n};"
      java: "/**\n * Definition for a binary tree node.\n * public class TreeNode {\n\
        \ *     int val;\n *     TreeNode left;\n *     TreeNode right;\n *     TreeNode()\
        \ {}\n *     TreeNode(int val) { this.val = val; }\n *     TreeNode(int val,\
        \ TreeNode left, TreeNode right) {\n *         this.val = val;\n *         this.left\
        \ = left;\n *         this.right = right;\n *     }\n * }\n */\nclass Solution\
        \ {\n    List<Long> allSubtreeSums = new ArrayList<>();\n\n    private long\
        \ dfs(TreeNode node) {\n        if (node == null) {\n            return 0;\n\
        \        }\n\n        long leftSum = dfs(node.left);\n        long rightSum\
        \ = dfs(node.right);\n\n        long currentSubtreeSum = node.val + leftSum\
        \ + rightSum;\n        allSubtreeSums.add(currentSubtreeSum);\n\n        return\
        \ currentSubtreeSum;\n    }\n\n    public int maxProduct(TreeNode root) {\n\
        \        allSubtreeSums.clear(); // Clear for multiple test cases\n        long\
        \ totalSum = dfs(root);\n\n        long maxProd = 0;\n        long MOD = 1_000_000_007;\n\
        \n        for (long s : allSubtreeSums) {\n            maxProd = Math.max(maxProd,\
        \ s * (totalSum - s));\n        }\n\n        return (int)(maxProd % MOD);\n\
        \    }\n}"
      python: "# Definition for a binary tree node.\n# class TreeNode(object):\n#  \
        \   def __init__(self, val=0, left=None, right=None):\n#         self.val =\
        \ val\n#         self.left = left\n#         self.right = right\nclass Solution(object):\n\
        \    def maxProduct(self, root):\n        \"\"\"\n        :type root: Optional[TreeNode]\n\
        \        :rtype: int\n        \"\"\"\n        all_subtree_sums = []\n\n    \
        \    def dfs(node):\n            if not node:\n                return 0\n\n\
        \            left_sum = dfs(node.left)\n            right_sum = dfs(node.right)\n\
        \n            current_subtree_sum = node.val + left_sum + right_sum\n      \
        \      all_subtree_sums.append(current_subtree_sum)\n\n            return current_subtree_sum\n\
        \n        total_sum = dfs(root)\n\n        max_prod = 0\n        MOD = 10**9\
        \ + 7\n\n        for s in all_subtree_sums:\n            max_prod = max(max_prod,\
        \ s * (total_sum - s))\n\n        return max_prod % MOD"
      python3: "# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self,\
        \ val=0, left=None, right=None):\n#         self.val = val\n#         self.left\
        \ = left\n#         self.right = right\nclass Solution:\n    def maxProduct(self,\
        \ root: Optional[TreeNode]) -> int:\n        all_subtree_sums = []\n\n     \
        \   def dfs(node):\n            if not node:\n                return 0\n\n \
        \           left_sum = dfs(node.left)\n            right_sum = dfs(node.right)\n\
        \n            current_subtree_sum = node.val + left_sum + right_sum\n      \
        \      all_subtree_sums.append(current_subtree_sum)\n\n            return current_subtree_sum\n\
        \n        total_sum = dfs(root)\n\n        max_prod = 0\n        MOD = 10**9\
        \ + 7\n\n        for s in all_subtree_sums:\n            max_prod = max(max_prod,\
        \ s * (total_sum - s))\n\n        return max_prod % MOD"
      c: "/**\n * Definition for a binary tree node.\n * struct TreeNode {\n *     int\
        \ val;\n *     struct TreeNode *left;\n *     struct TreeNode *right;\n * };\n\
        \ */\n\n// Global variables to store subtree sums and their count\n// Max nodes\
        \ 5 * 10^4, so an array of this size is sufficient.\n#define MAX_NODES 50001\
        \ \nlong long g_all_subtree_sums[MAX_NODES];\nint g_subtree_sums_count;\n\n\
        long long dfs_c(struct TreeNode* node) {\n    if (node == NULL) {\n        return\
        \ 0;\n    }\n\n    long long left_sum = dfs_c(node->left);\n    long long right_sum\
        \ = dfs_c(node->right);\n\n    long long current_subtree_sum = (long long)node->val\
        \ + left_sum + right_sum;\n    g_all_subtree_sums[g_subtree_sums_count++] =\
        \ current_subtree_sum;\n\n    return current_subtree_sum;\n}\n\nint maxProduct(struct\
        \ TreeNode* root) {\n    g_subtree_sums_count = 0; // Reset for each test case\n\
        \    long long total_sum = dfs_c(root);\n\n    long long max_prod = 0;\n   \
        \ long long MOD = 1000000007; // 10^9 + 7\n\n    for (int i = 0; i < g_subtree_sums_count;\
        \ ++i) {\n        long long s = g_all_subtree_sums[i];\n        long long current_prod\
        \ = s * (total_sum - s);\n        if (current_prod > max_prod) {\n         \
        \   max_prod = current_prod;\n        }\n    }\n\n    return (int)(max_prod\
        \ % MOD);\n}"
      csharp: "/**\n * Definition for a binary tree node.\n * public class TreeNode\
        \ {\n *     public int val;\n *     public TreeNode left;\n *     public TreeNode\
        \ right;\n *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null)\
        \ {\n *         this.val = val;\n *         this.left = left;\n *         this.right\
        \ = right;\n *     }\n * }\n */\npublic class Solution {\n    private List<long>\
        \ allSubtreeSums;\n    private const int MOD = 1_000_000_007;\n\n    public\
        \ int MaxProduct(TreeNode root) {\n        allSubtreeSums = new List<long>();\n\
        \n        long totalSum = DfsCalculateSums(root);\n\n        long maxProduct\
        \ = 0;\n        foreach (long s in allSubtreeSums) {\n            maxProduct\
        \ = Math.Max(maxProduct, s * (totalSum - s));\n        }\n\n        return (int)(maxProduct\
        \ % MOD);\n    }\n\n    private long DfsCalculateSums(TreeNode node) {\n   \
        \     if (node == null) {\n            return 0;\n        }\n\n        long\
        \ leftSum = DfsCalculateSums(node.left);\n        long rightSum = DfsCalculateSums(node.right);\n\
        \n        long currentSubtreeSum = node.val + leftSum + rightSum;\n        allSubtreeSums.Add(currentSubtreeSum);\n\
        \        return currentSubtreeSum;\n    }\n}"
      javascript: "/**\n * Definition for a binary tree node.\n * function TreeNode(val,\
        \ left, right) {\n *     this.val = (val===undefined ? 0 : val)\n *     this.left\
        \ = (left===undefined ? null : left)\n *     this.right = (right===undefined\
        \ ? null : right)\n * }\n */\n/**\n * @param {TreeNode} root\n * @return {number}\n\
        \ */\nvar maxProduct = function(root) {\n    const allSubtreeSums = [];\n  \
        \  const MOD = 1_000_000_007;\n\n    const dfsCalculateSums = (node) => {\n\
        \        if (node === null) {\n            return 0n;\n        }\n\n       \
        \ const leftSum = dfsCalculateSums(node.left);\n        const rightSum = dfsCalculateSums(node.right);\n\
        \n        const currentSubtreeSum = BigInt(node.val) + leftSum + rightSum;\n\
        \        allSubtreeSums.push(currentSubtreeSum);\n        return currentSubtreeSum;\n\
        \    };\n\n    const totalSum = dfsCalculateSums(root);\n\n    let maxProductVal\
        \ = 0n;\n\n    for (const s of allSubtreeSums) {\n        const currentProduct\
        \ = s * (totalSum - s);\n        if (currentProduct > maxProductVal) {\n   \
        \         maxProductVal = currentProduct;\n        }\n    }\n\n    return Number(maxProductVal\
        \ % BigInt(MOD));\n};"
      typescript: "/**\n * Definition for a binary tree node.\n * class TreeNode {\n\
        \ *     val: number\n *     left: TreeNode | null\n *     right: TreeNode |\
        \ null\n *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode\
        \ | null) {\n *         this.val = (val===undefined ? 0 : val)\n *         this.left\
        \ = (left===undefined ? null : left)\n *         this.right = (right===undefined\
        \ ? null : right)\n *     }\n * }\n */\n\nfunction maxProduct(root: TreeNode\
        \ | null): number {\n    const allSubtreeSums: bigint[] = [];\n    const MOD:\
        \ number = 1_000_000_007;\n\n    const dfsCalculateSums = (node: TreeNode |\
        \ null): bigint => {\n        if (node === null) {\n            return 0n;\n\
        \        }\n\n        const leftSum: bigint = dfsCalculateSums(node.left);\n\
        \        const rightSum: bigint = dfsCalculateSums(node.right);\n\n        const\
        \ currentSubtreeSum: bigint = BigInt(node.val) + leftSum + rightSum;\n     \
        \   allSubtreeSums.push(currentSubtreeSum);\n        return currentSubtreeSum;\n\
        \    };\n\n    const totalSum: bigint = dfsCalculateSums(root);\n\n    let maxProductVal:\
        \ bigint = 0n;\n\n    for (const s of allSubtreeSums) {\n        const currentProduct:\
        \ bigint = s * (totalSum - s);\n        if (currentProduct > maxProductVal)\
        \ {\n            maxProductVal = currentProduct;\n        }\n    }\n\n    return\
        \ Number(maxProductVal % BigInt(MOD));\n};"
      php: "/**\n * Definition for a binary tree node.\n * class TreeNode {\n *    \
        \ public $val = null;\n *     public $left = null;\n *     public $right = null;\n\
        \ *     function __construct($val = 0, $left = null, $right = null) {\n *  \
        \       $this->val = $val;\n *         $this->left = $left;\n *         $this->right\
        \ = $right;\n *     }\n * }\n */\nclass Solution {\n    /**\n     * @var int[]\n\
        \     */\n    private $allSubtreeSums;\n    private const MOD = 1_000_000_007;\n\
        \n    /**\n     * @param TreeNode $root\n     * @return Integer\n     */\n \
        \   function maxProduct($root) {\n        $this->allSubtreeSums = [];\n\n  \
        \      $totalSum = $this->dfsCalculateSums($root);\n\n        $maxProduct =\
        \ 0;\n        foreach ($this->allSubtreeSums as $s) {\n            $maxProduct\
        \ = max($maxProduct, $s * ($totalSum - $s));\n        }\n\n        return $maxProduct\
        \ % self::MOD;\n    }\n\n    /**\n     * @param TreeNode $node\n     * @return\
        \ int\n     */\n    private function dfsCalculateSums($node) {\n        if ($node\
        \ === null) {\n            return 0;\n        }\n\n        $leftSum = $this->dfsCalculateSums($node->left);\n\
        \        $rightSum = $this->dfsCalculateSums($node->right);\n\n        $currentSubtreeSum\
        \ = $node->val + $leftSum + $rightSum;\n        $this->allSubtreeSums[] = $currentSubtreeSum;\n\
        \        return $currentSubtreeSum;\n    }\n}"
      swift: "/**\n * Definition for a binary tree node.\n * public class TreeNode {\n\
        \ *     public var val: Int\n *     public var left: TreeNode?\n *     public\
        \ var right: TreeNode?\n *     public init() { self.val = 0; self.left = nil;\
        \ self.right = nil; }\n *     public init(_ val: Int) { self.val = val; self.left\
        \ = nil; self.right = nil; }\n *     public init(_ val: Int, _ left: TreeNode?,\
        \ _ right: TreeNode?) {\n *         self.val = val\n *         self.left = left\n\
        \ *         self.right = right\n *     }\n * }\n */\nclass Solution {\n    private\
        \ var allSubtreeSums: [Int] = []\n    private let MOD = 1_000_000_007\n\n  \
        \  func maxProduct(_ root: TreeNode?) -> Int {\n        allSubtreeSums = []\n\
        \n        let totalSum = dfsCalculateSums(root)\n\n        var maxProduct: Int\
        \ = 0\n        for s in allSubtreeSums {\n            maxProduct = max(maxProduct,\
        \ s * (totalSum - s))\n        }\n\n        return maxProduct % MOD\n    }\n\
        \n    private func dfsCalculateSums(_ node: TreeNode?) -> Int {\n        guard\
        \ let node = node else {\n            return 0\n        }\n\n        let leftSum\
        \ = dfsCalculateSums(node.left)\n        let rightSum = dfsCalculateSums(node.right)\n\
        \n        let currentSubtreeSum = node.val + leftSum + rightSum\n        allSubtreeSums.append(currentSubtreeSum)\n\
        \        return currentSubtreeSum\n    }\n}"
      kotlin: "class Solution {\n    fun maxProduct(root: TreeNode?): Int {\n      \
        \  val allSubtreeSums = mutableListOf<Long>()\n        val MOD = 1_000_000_007\n\
        \n        val totalSum = dfs(root, allSubtreeSums)\n\n        var maxProd: Long\
        \ = 0\n\n        for (s in allSubtreeSums) {\n            val currentProd =\
        \ s * (totalSum - s)\n            if (currentProd > maxProd) {\n           \
        \     maxProd = currentProd\n            }\n        }\n\n        return (maxProd\
        \ % MOD).toInt()\n    }\n\n    fun dfs(node: TreeNode?, allSubtreeSums: MutableList<Long>):\
        \ Long {\n        if (node == null) {\n            return 0L\n        }\n\n\
        \        val leftSum = dfs(node.left, allSubtreeSums)\n        val rightSum\
        \ = dfs(node.right, allSubtreeSums)\n\n        val currentSubtreeSum = node.`val`.toLong()\
        \ + leftSum + rightSum\n        allSubtreeSums.add(currentSubtreeSum)\n    \
        \    return currentSubtreeSum\n    }\n}"
      dart: "/**\n * Definition for a binary tree node.\n * class TreeNode {\n *   int\
        \ val;\n *   TreeNode? left;\n *   TreeNode? right;\n *   TreeNode([this.val\
        \ = 0, this.left, this.right]);\n * }\n */\nclass Solution {\n  int maxProduct(TreeNode?\
        \ root) {\n    List<int> allSubtreeSums = [];\n    final int MOD = 1000000007;\n\
        \n    int dfs(TreeNode? node) {\n      if (node == null) {\n        return 0;\n\
        \      }\n\n      int leftSum = dfs(node.left);\n      int rightSum = dfs(node.right);\n\
        \n      int currentSubtreeSum = node.val + leftSum + rightSum;\n      allSubtreeSums.add(currentSubtreeSum);\n\
        \      return currentSubtreeSum;\n    }\n\n    int totalSum = dfs(root);\n\n\
        \    int maxProd = 0;\n\n    for (int s in allSubtreeSums) {\n      int currentProd\
        \ = s * (totalSum - s);\n      if (currentProd > maxProd) {\n        maxProd\
        \ = currentProd;\n      }\n    }\n\n    return (maxProd % MOD);\n  }\n}"
      go: "/**\n * Definition for a binary tree node.\n * type TreeNode struct {\n *\
        \     Val int\n *     Left *TreeNode\n *     Right *TreeNode\n * }\n */\nfunc\
        \ maxProduct(root *TreeNode) int {\n    allSubtreeSums := []int64{}\n    MOD\
        \ := int64(1_000_000_007)\n\n    var dfs func(*TreeNode) int64\n    dfs = func(node\
        \ *TreeNode) int64 {\n        if node == nil {\n            return 0\n     \
        \   }\n\n        leftSum := dfs(node.Left)\n        rightSum := dfs(node.Right)\n\
        \n        currentSubtreeSum := int64(node.Val) + leftSum + rightSum\n      \
        \  allSubtreeSums = append(allSubtreeSums, currentSubtreeSum)\n        return\
        \ currentSubtreeSum\n    }\n\n    totalSum := dfs(root)\n\n    var maxProd int64\
        \ = 0\n\n    for _, s := range allSubtreeSums {\n        currentProd := s *\
        \ (totalSum - s)\n        if currentProd > maxProd {\n            maxProd =\
        \ currentProd\n        }\n    }\n\n    return int(maxProd % MOD)\n}"
      ruby: "# Definition for a binary tree node.\n# class TreeNode\n#     attr_accessor\
        \ :val, :left, :right\n#     def initialize(val = 0, left = nil, right = nil)\n\
        #         @val = val\n#         @left = left\n#         @right = right\n#  \
        \   end\n# end\n# @param {TreeNode} root\n# @return {Integer}\ndef max_product(root)\n\
        \    all_subtree_sums = []\n    mod = 1_000_000_007\n\n    dfs = lambda do |node|\n\
        \        return 0 if node.nil?\n\n        left_sum = dfs.call(node.left)\n \
        \       right_sum = dfs.call(node.right)\n\n        current_subtree_sum = node.val\
        \ + left_sum + right_sum\n        all_subtree_sums << current_subtree_sum\n\
        \        current_subtree_sum\n    end\n\n    total_sum = dfs.call(root)\n\n\
        \    max_prod = 0\n\n    all_subtree_sums.each do |s|\n        current_prod\
        \ = s * (total_sum - s)\n        max_prod = current_prod if current_prod > max_prod\n\
        \    end\n\n    (max_prod % mod)\nend"
      scala: "/**\n * Definition for a binary tree node.\n * class TreeNode(_value:\
        \ Int = 0, _left: TreeNode = null, _right: TreeNode = null) {\n *   var value:\
        \ Int = _value\n *   var left: TreeNode = _left\n *   var right: TreeNode =\
        \ _right\n * }\n */\nobject Solution {\n    def maxProduct(root: TreeNode):\
        \ Int = {\n        val allSubtreeSums = collection.mutable.ListBuffer[Long]()\n\
        \        val MOD = 1_000_000_007L\n\n        def dfs(node: TreeNode): Long =\
        \ {\n            if (node == null) {\n                return 0L\n          \
        \  }\n\n            val leftSum = dfs(node.left)\n            val rightSum =\
        \ dfs(node.right)\n\n            val currentSubtreeSum = node.value.toLong +\
        \ leftSum + rightSum\n            allSubtreeSums += currentSubtreeSum\n    \
        \        currentSubtreeSum\n        }\n\n        val totalSum = dfs(root)\n\n\
        \        var maxProd: Long = 0L\n\n        for (s <- allSubtreeSums) {\n   \
        \         val currentProd = s * (totalSum - s)\n            if (currentProd\
        \ > maxProd) {\n                maxProd = currentProd\n            }\n     \
        \   }\n\n        (maxProd % MOD).toInt\n    }\n}"
      rust: "use std::rc::Rc;\nuse std::cell::RefCell;\n\n// Definition for a binary\
        \ tree node.\n// #[derive(Debug, PartialEq, Eq)]\n// pub struct TreeNode {\n\
        //   pub val: i32,\n//   pub left: Option<Rc<RefCell<TreeNode>> >,\n//   pub\
        \ right: Option<Rc<RefCell<TreeNode>> >,\n// }\n// \n// impl TreeNode {\n//\
        \   #[inline]\n//   pub fn new(val: i32) -> Self {\n//     TreeNode {\n//  \
        \     val,\n//       left: None,\n//       right: None\n//     }\n//   }\n//\
        \ }\nimpl Solution {\n    pub fn max_product(root: Option<Rc<RefCell<TreeNode>>>)\
        \ -> i32 {\n        let mut max_prod: i64 = 0;\n        let modulo: i64 = 1_000_000_007;\n\
        \n        // First pass: calculate total sum of the entire tree\n        let\
        \ total_sum = Self::calculate_total_sum(root.clone());\n\n        // Second\
        \ pass: traverse the tree, calculate subtree sums, and update max_prod\n   \
        \     Self::dfs_maximize_product(root, total_sum, &mut max_prod);\n\n      \
        \  (max_prod % modulo) as i32\n    }\n\n    // Helper function to calculate\
        \ the total sum of all nodes in the tree\n    fn calculate_total_sum(node: Option<Rc<RefCell<TreeNode>>>)\
        \ -> i64 {\n        if let Some(n_rc) = node {\n            let n = n_rc.borrow();\n\
        \            (n.val as i64)\n                + Self::calculate_total_sum(n.left.clone())\n\
        \                + Self::calculate_total_sum(n.right.clone())\n        } else\
        \ {\n            0\n        }\n    }\n\n    // Helper function to perform DFS,\
        \ calculate subtree sums, and update the maximum product\n    fn dfs_maximize_product(\n\
        \        node: Option<Rc<RefCell<TreeNode>>>,\n        total_sum: i64,\n   \
        \     max_prod: &mut i64,\n    ) -> i64 {\n        if let Some(n_rc) = node\
        \ {\n            let n = n_rc.borrow();\n            let left_sum = Self::dfs_maximize_product(n.left.clone(),\
        \ total_sum, max_prod);\n            let right_sum = Self::dfs_maximize_product(n.right.clone(),\
        \ total_sum, max_prod);\n            let current_subtree_sum = (n.val as i64)\
        \ + left_sum + right_sum;\n\n            // Calculate the product for this split\
        \ and update max_prod\n            let product = current_subtree_sum * (total_sum\
        \ - current_subtree_sum);\n            if product > *max_prod {\n          \
        \      *max_prod = product;\n            }\n\n            current_subtree_sum\n\
        \        } else {\n            0\n        }\n    }\n}"
      racket: "; Definition for a binary tree node.\n#|\n\n; val : integer?\n; left\
        \ : (or/c tree-node? #f)\n; right : (or/c tree-node? #f)\n(struct tree-node\n\
        \  (val left right) #:mutable #:transparent)\n\n; constructor\n(define (make-tree-node\
        \ [val 0])\n  (tree-node val #f #f))\n\n|#\n\n(define/contract (max-product\
        \ root)\n  (-> (or/c tree-node? #f) exact-integer?)\n  (define MOD 1000000007)\n\
        \  (define max-prod 0) ; Mutable variable to store the maximum product\n\n \
        \ ; First pass: calculate the total sum of all nodes in the tree\n  (define\
        \ (calculate-total-sum node)\n    (if (not node)\n        0\n        (+ (tree-node-val\
        \ node)\n           (calculate-total-sum (tree-node-left node))\n          \
        \ (calculate-total-sum (tree-node-right node)))))\n\n  (define total-sum (calculate-total-sum\
        \ root))\n\n  ; Second pass: perform DFS, calculate subtree sums, and update\
        \ max-prod\n  (define (dfs-maximize-product node)\n    (if (not node)\n    \
        \    0\n        (let* ([left-sum (dfs-maximize-product (tree-node-left node))]\n\
        \               [right-sum (dfs-maximize-product (tree-node-right node))]\n\
        \               [current-subtree-sum (+ (tree-node-val node) left-sum right-sum)])\n\
        \n          ; Calculate the product for this split and update max-prod\n   \
        \       (set! max-prod (max max-prod (* current-subtree-sum (- total-sum current-subtree-sum))))\n\
        \n          current-subtree-sum)))\n\n  (dfs-maximize-product root)\n  (modulo\
        \ max-prod MOD))"
      erlang: "%% Definition for a binary tree node.\n%%\n%% -record(tree_node, {val\
        \ = 0 :: integer(),\n%%                     left = null  :: 'null' | #tree_node{},\n\
        %%                     right = null :: 'null' | #tree_node{}}).\n\n-spec max_product(Root\
        \ :: #tree_node{} | null) -> integer().\nmax_product(Root) ->\n  MOD = 1_000_000_007,\n\
        \n  % First pass: calculate the total sum of all nodes in the tree\n  TotalSum\
        \ = calculate_total_sum(Root),\n\n  % Second pass: perform DFS, calculate subtree\
        \ sums, and update max_prod\n  % The max_prod is accumulated and passed through\
        \ the recursive calls\n  {_FinalSubtreeSum, MaxProd} = dfs_maximize_product(Root,\
        \ TotalSum, 0),\n\n  MaxProd rem MOD.\n\n% Helper function to calculate the\
        \ total sum of all nodes in the tree\ncalculate_total_sum(null) -> 0;\ncalculate_total_sum(#tree_node{val\
        \ = Val, left = Left, right = Right}) ->\n  Val + calculate_total_sum(Left)\
        \ + calculate_total_sum(Right).\n\n% Helper function to perform DFS, calculate\
        \ subtree sums, and update the maximum product\n% Returns {CurrentSubtreeSum,\
        \ MaxProductSoFar}\ndfs_maximize_product(null, _TotalSum, MaxProdAcc) ->\n \
        \ {0, MaxProdAcc};\ndfs_maximize_product(#tree_node{val = Val, left = Left,\
        \ right = Right}, TotalSum, MaxProdAcc) ->\n  {LeftSum, MaxProdAfterLeft} =\
        \ dfs_maximize_product(Left, TotalSum, MaxProdAcc),\n  {RightSum, MaxProdAfterRight}\
        \ = dfs_maximize_product(Right, TotalSum, MaxProdAfterLeft),\n\n  CurrentSubtreeSum\
        \ = Val + LeftSum + RightSum,\n  CurrentProduct = CurrentSubtreeSum * (TotalSum\
        \ - CurrentSubtreeSum),\n\n  % Update MaxProdAcc with the maximum product found\
        \ so far\n  NewMaxProd = max(MaxProdAfterRight, CurrentProduct),\n\n  {CurrentSubtreeSum,\
        \ NewMaxProd}."
      elixir: "# Definition for a binary tree node.\n#\n# defmodule TreeNode do\n# \
        \  @type t :: %__MODULE__{\n#           val: integer,\n#           left: TreeNode.t()\
        \ | nil,\n#           right: TreeNode.t() | nil\n#         }\n#   defstruct\
        \ val: 0, left: nil, right: nil\n# end\n\ndefmodule Solution do\n  @spec max_product(root\
        \ :: TreeNode.t | nil) :: integer\n  def max_product(root) do\n    mod = 1_000_000_007\n\
        \n    # First pass: calculate the total sum of all nodes in the tree\n    total_sum\
        \ = calculate_total_sum(root)\n\n    # Second pass: perform DFS, calculate subtree\
        \ sums, and update max_prod\n    # The max_prod is accumulated and passed through\
        \ the recursive calls\n    {_final_subtree_sum, max_prod} = dfs_maximize_product(root,\
        \ total_sum, 0)\n\n    rem(max_prod, mod)\n  end\n\n  # Helper function to calculate\
        \ the total sum of all nodes in the tree\n  defp calculate_total_sum(nil), do:\
        \ 0\n  defp calculate_total_sum(%TreeNode{val: val, left: left, right: right})\
        \ do\n    val + calculate_total_sum(left) + calculate_total_sum(right)\n  end\n\
        \n  # Helper function to perform DFS, calculate subtree sums, and update the\
        \ maximum product\n  # Returns {current_subtree_sum, max_product_so_far}\n \
        \ defp dfs_maximize_product(nil, _total_sum, max_prod_acc) do\n    {0, max_prod_acc}\n\
        \  end\n  defp dfs_maximize_product(%TreeNode{val: val, left: left, right: right},\
        \ total_sum, max_prod_acc) do\n    {left_sum, max_prod_after_left} = dfs_maximize_product(left,\
        \ total_sum, max_prod_acc)\n    {right_sum, max_prod_after_right} = dfs_maximize_product(right,\
        \ total_sum, max_prod_after_left)\n\n    current_subtree_sum = val + left_sum\
        \ + right_sum\n    current_product = current_subtree_sum * (total_sum - current_subtree_sum)\n\
        \n    # Update max_prod_acc with the maximum product found so far\n    new_max_prod\
        \ = max(max_prod_after_right, current_product)\n\n    {current_subtree_sum,\
        \ new_max_prod}\n  end\nend"
    approach: 'The problem asks us to find the maximum product of sums of two subtrees
      formed by removing a single edge from the given binary tree. We need to return
      this maximum product modulo 10^9 + 7, ensuring that the maximization happens before
      applying the modulo. The core idea is that if we remove an edge, the tree splits
      into two parts: one is the subtree rooted at the child node of the removed edge,
      and the other is the rest of the original tree. If we know the sum of the entire
      tree (let''s call it `total_sum`) and the sum of any subtree (let''s call it `subtree_sum`),
      then the sum of the other part will be `total_sum - subtree_sum`. The product
      for this specific split would be `subtree_sum * (total_sum - subtree_sum).`


      To find the maximum product, we perform a Depth First Search (DFS) traversal on
      the tree. During this traversal, for every node, we calculate the sum of the subtree
      rooted at that node. These subtree sums are collected into a list. The DFS function
      returns the sum of the current subtree, which is `node.val + sum(left_child_subtree)
      + sum(right_child_subtree)`. After the DFS completes, the sum returned by the
      initial call on the root node will be the `total_sum` of the entire tree. We then
      iterate through the collected list of all subtree sums. For each `s` in this list,
      we calculate the product `s * (total_sum - s)` and update our `max_product` if
      the current product is greater. Since the product can be very large, we use 64-bit
      integers (or `BigInt` in JavaScript/TypeScript) for sums and products to avoid
      overflow before taking the final modulo.'
    time_complexity: The time complexity is O(N), where N is the number of nodes in
      the binary tree. This is because we perform a single Depth First Search (DFS)
      traversal to calculate all subtree sums, visiting each node exactly once. After
      collecting all N subtree sums, we iterate through this list once to find the maximum
      product, which also takes O(N) time. Thus, the total time complexity is dominated
      by these two linear passes.
    space_complexity: The space complexity is O(N). This is primarily due to storing
      all N subtree sums in a list or array. Additionally, the recursion stack for the
      DFS traversal can go up to a depth of N in the worst case (for a skewed tree)
      or O(log N) in the best case (for a balanced tree). Therefore, the overall space
      complexity is O(N).
    elapsed_time: 136.951242685318
    model: gemini-2.5-flash
    generated_at: '2026-01-07 01:11:51 '
  - solutions:
      cpp: "class Solution {\npublic:\n    int maxProduct(TreeNode* root) {\n      \
        \  long long total = 0;\n        vector<long long> sums;\n        total = getTotalSum(root,\
        \ sums);\n        long long maxProduct = 0;\n        for (long long sum : sums)\
        \ {\n            maxProduct = max(maxProduct, sum * (total - sum));\n      \
        \  }\n        return maxProduct % (1000000007);\n    }\n\n    long long getTotalSum(TreeNode*\
        \ root, vector<long long>& sums) {\n        if (root == nullptr) return 0;\n\
        \        long long sum = root->val + getTotalSum(root->left, sums) + getTotalSum(root->right,\
        \ sums);\n        sums.push_back(sum);\n        return sum;\n    }\n};"
      java: "class Solution {\n    public int maxProduct(TreeNode root) {\n        long\
        \ total = 0;\n        List<Long> sums = new ArrayList<>();\n        total =\
        \ getTotalSum(root, sums);\n        long maxProduct = 0;\n        for (long\
        \ sum : sums) {\n            maxProduct = Math.max(maxProduct, sum * (total\
        \ - sum));\n        }\n        return (int)(maxProduct % (1000000007));\n  \
        \  }\n\n    private long getTotalSum(TreeNode root, List<Long> sums) {\n   \
        \     if (root == null) return 0;\n        long sum = root.val + getTotalSum(root.left,\
        \ sums) + getTotalSum(root.right, sums);\n        sums.add(sum);\n        return\
        \ sum;\n    }\n}"
      python: "class Solution:\n    def maxProduct(self, root):\n        total = [0]\n\
        \        sums = []\n        self.getTotalSum(root, sums)\n        total[0] =\
        \ sum(sums)\n        maxProduct = 0\n        for sum in sums:\n            maxProduct\
        \ = max(maxProduct, sum * (total[0] - sum))\n        return maxProduct % (10**9\
        \ + 7)\n\n    def getTotalSum(self, root, sums):\n        if not root:\n   \
        \         return 0\n        sum = root.val + self.getTotalSum(root.left, sums)\
        \ + self.getTotalSum(root.right, sums)\n        sums.append(sum)\n        return\
        \ sum"
      python3: "class Solution:\n    def maxProduct(self, root: Optional[TreeNode])\
        \ -> int:\n        total = [0]\n        sums = []\n        self.getTotalSum(root,\
        \ sums)\n        total[0] = sum(sums)\n        maxProduct = 0\n        for sum\
        \ in sums:\n            maxProduct = max(maxProduct, sum * (total[0] - sum))\n\
        \        return maxProduct % (10**9 + 7)\n\n    def getTotalSum(self, root,\
        \ sums):\n        if not root:\n            return 0\n        sum = root.val\
        \ + self.getTotalSum(root.left, sums) + self.getTotalSum(root.right, sums)\n\
        \        sums.append(sum)\n        return sum"
      c: "int maxProduct(struct TreeNode* root) {\n    long long total = 0;\n    long\
        \ long* sums = NULL;\n    int size = 0;\n    total = getTotalSum(root, &sums,\
        \ &size);\n    long long maxProduct = 0;\n    for (int i = 0; i < size; i++)\
        \ {\n        maxProduct = (maxProduct > sums[i] * (total - sums[i])) ? maxProduct\
        \ : sums[i] * (total - sums[i]);\n    }\n    free(sums);\n    return maxProduct\
        \ % 1000000007;\n}\n\nlong long getTotalSum(struct TreeNode* root, long long**\
        \ sums, int* size) {\n    if (root == NULL) return 0;\n    long long sum = root->val\
        \ + getTotalSum(root->left, sums, size) + getTotalSum(root->right, sums, size);\n\
        \    (*sums) = realloc((*sums), ((*size) + 1) * sizeof(long long));\n    (*sums)[(*size)]\
        \ = sum;\n    (*size)++;\n    return sum;\n}"
      csharp: "public class Solution {\n    public int MaxProduct(TreeNode root) {\n\
        \        long total = TotalSum(root);\n        long max = 0;\n        long res\
        \ = SubtreeSum(root, total, ref max);\n        return (int)(max % (Math.Pow(10,\
        \ 9) + 7));\n    }\n    private long TotalSum(TreeNode root) {\n        if (root\
        \ == null) return 0;\n        return root.val + TotalSum(root.left) + TotalSum(root.right);\n\
        \    }\n    private long SubtreeSum(TreeNode root, long total, ref long max)\
        \ {\n        if (root == null) return 0;\n        long sum = root.val + SubtreeSum(root.left,\
        \ total, ref max) + SubtreeSum(root.right, total, ref max);\n        max = Math.Max(max,\
        \ sum * (total - sum));\n        return sum;\n    }\n}"
      javascript: "var maxProduct = function(root) {\n    let total = totalSum(root);\n\
        \    let max = 0;\n    subtreeSum(root, total, max);\n    return max % (Math.pow(10,\
        \ 9) + 7);\n};\nfunction totalSum(root) {\n    if (!root) return 0;\n    return\
        \ root.val + totalSum(root.left) + totalSum(root.right);\n}\nfunction subtreeSum(root,\
        \ total, max) {\n    if (!root) return 0;\n    let sum = root.val + subtreeSum(root.left,\
        \ total, max) + subtreeSum(root.right, total, max);\n    max = Math.max(max,\
        \ sum * (total - sum));\n    return sum;\n}"
      typescript: "function maxProduct(root: TreeNode | null): number {\n    let total:\
        \ number = totalSum(root);\n    let max: number = 0;\n    subtreeSum(root, total,\
        \ max);\n    return max % (Math.pow(10, 9) + 7);\n}\nfunction totalSum(root:\
        \ TreeNode | null): number {\n    if (!root) return 0;\n    return root.val\
        \ + totalSum(root.left) + totalSum(root.right);\n}\nfunction subtreeSum(root:\
        \ TreeNode | null, total: number, max: number): number {\n    if (!root) return\
        \ 0;\n    let sum: number = root.val + subtreeSum(root.left, total, max) + subtreeSum(root.right,\
        \ total, max);\n    max = Math.max(max, sum * (total - sum));\n    return sum;\n\
        }"
      php: "class Solution {\n    function maxProduct($root) {\n        $total = $this->totalSum($root);\n\
        \        $max = 0;\n        $this->subtreeSum($root, $total, $max);\n      \
        \  return $max % (pow(10, 9) + 7);\n    }\n    function totalSum($root) {\n\
        \        if (!$root) return 0;\n        return $root->val + $this->totalSum($root->left)\
        \ + $this->totalSum($root->right);\n    }\n    function subtreeSum($root, $total,\
        \ &$max) {\n        if (!$root) return 0;\n        $sum = $root->val + $this->subtreeSum($root->left,\
        \ $total, $max) + $this->subtreeSum($root->right, $total, $max);\n        $max\
        \ = max($max, $sum * ($total - $sum));\n        return $sum;\n    }\n}"
      swift: "class Solution {\n    func maxProduct(_ root: TreeNode?) -> Int {\n  \
        \      let total = totalSum(root)\n        var max: Int64 = 0\n        _ = subtreeSum(root,\
        \ total, &max)\n        return Int(max % (Int64(pow(10, 9)) + 7))\n    }\n \
        \   func totalSum(_ root: TreeNode?) -> Int64 {\n        guard let root = root\
        \ else { return 0 }\n        return Int64(root.val) + totalSum(root.left) +\
        \ totalSum(root.right)\n    }\n    func subtreeSum(_ root: TreeNode?, _ total:\
        \ Int64, _ max: inout Int64) -> Int64 {\n        guard let root = root else\
        \ { return 0 }\n        let sum = Int64(root.val) + subtreeSum(root.left, total,\
        \ &max) + subtreeSum(root.right, total, &max)\n        max = max(max, sum *\
        \ (total - sum))\n        return sum\n    }\n}"
      kotlin: "class Solution {\n    fun maxProduct(root: TreeNode?): Int {\n      \
        \  val MOD = 1000000007\n        var totalSum = 0\n        var maxProduct =\
        \ 0\n        totalSum = sum(root)\n        sum(root, totalSum, { a, b -> maxProduct\
        \ = Math.max(maxProduct, a * b) })\n        return maxProduct % MOD\n    }\n\
        \    fun sum(root: TreeNode?, totalSum: Int = 0, callback: (Int, Int) -> Unit\
        \ = { _, _ -> }): Int {\n        if (root == null) return 0\n        val sum\
        \ = root.`val` + sum(root.left, totalSum, callback) + sum(root.right, totalSum,\
        \ callback)\n        callback(sum, totalSum - sum)\n        return sum\n   \
        \ }\n}"
      dart: "class Solution {\n  int maxProduct(TreeNode? root) {\n    final mod = 1000000007;\n\
        \    int totalSum = 0;\n    int maxProduct = 0;\n    totalSum = sum(root);\n\
        \    sum(root, totalSum, (a, b) => maxProduct = max(maxProduct, a * b));\n \
        \   return maxProduct % mod;\n  }\n  int sum(TreeNode? root, [int totalSum =\
        \ 0, Function? callback]) {\n    if (root == null) return 0;\n    final sum\
        \ = root.val + sum(root.left, totalSum, callback) + sum(root.right, totalSum,\
        \ callback);\n    if (callback != null) callback(sum, totalSum - sum);\n   \
        \ return sum;\n  }\n}"
      go: "func maxProduct(root *TreeNode) int {\n    mod := 1000000007\n    var totalSum\
        \ int\n    var maxProduct int\n    totalSum = sum(root)\n    sum(root, &totalSum,\
        \ &maxProduct)\n    return maxProduct % mod\n}\nfunc sum(root *TreeNode, totalSum\
        \ *int, maxProduct *int) int {\n    if root == nil {\n        return 0\n   \
        \ }\n    sum := root.Val + sum(root.Left, totalSum, maxProduct) + sum(root.Right,\
        \ totalSum, maxProduct)\n    product := sum * (*totalSum - sum)\n    if product\
        \ > *maxProduct {\n        *maxProduct = product\n    }\n    return sum\n}"
      ruby: "def max_product(root)\n    mod = 1000000007\n    total_sum = 0\n    max_product\
        \ = 0\n    total_sum = sum(root)\n    sum(root, total_sum, max_product)\n  \
        \  max_product % mod\nend\n\ndef sum(root, total_sum = 0, max_product = 0)\n\
        \    return 0 if root.nil?\n    sum = root.val + sum(root.left, total_sum, max_product)\
        \ + sum(root.right, total_sum, max_product)\n    product = sum * (total_sum\
        \ - sum)\n    max_product = [max_product, product].max\n    sum\nend"
      scala: "object Solution {\n    def maxProduct(root: TreeNode): Int = {\n     \
        \   val mod = 1000000007\n        var totalSum = 0\n        var maxProduct =\
        \ 0\n        totalSum = sum(root)\n        sum(root, totalSum, (a, b) => maxProduct\
        \ = Math.max(maxProduct, a * b))\n        maxProduct % mod\n    }\n    def sum(root:\
        \ TreeNode, totalSum: Int = 0, callback: (Int, Int) => Unit = (a, b) => ()):\
        \ Int = {\n        if (root == null) return 0\n        val sum = root.value\
        \ + sum(root.left, totalSum, callback) + sum(root.right, totalSum, callback)\n\
        \        callback(sum, totalSum - sum)\n        sum\n    }\n}"
      rust: "use std::rc::Rc;\nuse std::cell::RefCell;\nimpl Solution {\n    pub fn\
        \ max_product(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {\n        let total_sum\
        \ = Self::get_total_sum(&root);\n        let mut max_product = 0;\n        Self::get_max_product(&root,\
        \ total_sum, &mut max_product);\n        max_product as i32 % 1000000007\n \
        \   }\n\n    fn get_total_sum(root: &Option<Rc<RefCell<TreeNode>>>) -> i64 {\n\
        \        match root {\n            Some(node) => node.borrow().val as i64 +\
        \ Self::get_total_sum(&node.borrow().left) + Self::get_total_sum(&node.borrow().right),\n\
        \            None => 0,\n        }\n    }\n\n    fn get_max_product(root: &Option<Rc<RefCell<TreeNode>>>,\
        \ total_sum: i64, max_product: &mut i64) {\n        match root {\n         \
        \   Some(node) => {\n                let left_sum = Self::get_total_sum(&node.borrow().left);\n\
        \                let right_sum = Self::get_total_sum(&node.borrow().right);\n\
        \                let current_sum = left_sum + right_sum + node.borrow().val\
        \ as i64;\n                *max_product = (*max_product).max((total_sum - current_sum)\
        \ * current_sum);\n                Self::get_max_product(&node.borrow().left,\
        \ total_sum, max_product);\n                Self::get_max_product(&node.borrow().right,\
        \ total_sum, max_product);\n            }\n            None => (),\n       \
        \ }\n    }\n}"
      racket: "define/contract (max-product root)\n  (-> (or/c tree-node? #f) exact-integer?)\n\
        \  (let ([total-sum (get-total-sum root)])\n    (let ([max-product 0])\n   \
        \   (get-max-product root total-sum max-product)\n      (modulo max-product\
        \ 1000000007)))\n\n(define (get-total-sum root)\n  (if (tree-node? root)\n \
        \     (+ (tree-node-val root) (get-total-sum (tree-node-left root)) (get-total-sum\
        \ (tree-node-right root)))\n      0))\n\n(define (get-max-product root total-sum\
        \ max-product)\n  (if (tree-node? root)\n      (let ([left-sum (get-total-sum\
        \ (tree-node-left root))]\n            [right-sum (get-total-sum (tree-node-right\
        \ root))]\n            [current-sum (+ left-sum right-sum (tree-node-val root))])\n\
        \        (set! max-product (max max-product (* (- total-sum current-sum) current-sum)))\n\
        \        (get-max-product (tree-node-left root) total-sum max-product)\n   \
        \     (get-max-product (tree-node-right root) total-sum max-product))\n    \
        \  max-product))"
      erlang: "max_product(Root) ->\n  TotalSum = get_total_sum(Root),\n  MaxProduct\
        \ = get_max_product(Root, TotalSum, 0),\n  MaxProduct rem 1000000007.\n\nget_total_sum(null)\
        \ -> 0;\nget_total_sum(#tree_node{val = Val, left = Left, right = Right}) ->\n\
        \  Val + get_total_sum(Left) + get_total_sum(Right).\n\nget_max_product(null,\
        \ _TotalSum, MaxProduct) -> MaxProduct;\nget_max_product(#tree_node{val = Val,\
        \ left = Left, right = Right}, TotalSum, MaxProduct) ->\n  LeftSum = get_total_sum(Left),\n\
        \  RightSum = get_total_sum(Right),\n  CurrentSum = LeftSum + RightSum + Val,\n\
        \  NewMaxProduct = max(MaxProduct, (TotalSum - CurrentSum) * CurrentSum),\n\
        \  get_max_product(Left, TotalSum, NewMaxProduct),\n  get_max_product(Right,\
        \ TotalSum, NewMaxProduct)."
      elixir: "defmodule Solution do\n  @spec max_product(root :: TreeNode.t | nil)\
        \ :: integer\n  def max_product(root) do\n    total_sum = get_total_sum(root)\n\
        \    max_product = get_max_product(root, total_sum, 0)\n    rem(max_product,\
        \ 1_000_000_007)\n  end\n\n  defp get_total_sum(nil), do: 0\n  defp get_total_sum(%TreeNode{val:\
        \ val, left: left, right: right}) do\n    val + get_total_sum(left) + get_total_sum(right)\n\
        \  end\n\n  defp get_max_product(nil, _total_sum, max_product), do: max_product\n\
        \  defp get_max_product(%TreeNode{val: val, left: left, right: right}, total_sum,\
        \ max_product) do\n    left_sum = get_total_sum(left)\n    right_sum = get_total_sum(right)\n\
        \    current_sum = left_sum + right_sum + val\n    new_max_product = max(max_product,\
        \ (total_sum - current_sum) * current_sum)\n    get_max_product(left, total_sum,\
        \ new_max_product)\n    get_max_product(right, total_sum, new_max_product)\n\
        \  end\nend"
    approach: "The problem is solved by first calculating the total sum of the binary\
      \ tree. Then, we calculate the sum of each subtree and store it in a list. Finally,\
      \ we iterate over the list to find the maximum product of two subtrees. The key\
      \ intuition here is that the maximum product will occur when the two subtrees\
      \ have sums that are as close as possible to each other. This is because the product\
      \ of two numbers is maximized when the numbers are as close as possible to each\
      \ other, given a fixed sum. \n  The algorithm works by first calculating the total\
      \ sum of the binary tree using a depth-first search (DFS) traversal. Then, we\
      \ calculate the sum of each subtree using another DFS traversal and store it in\
      \ a list. Finally, we iterate over the list to find the maximum product of two\
      \ subtrees. We use the formula (total_sum - subtree_sum) * subtree_sum to calculate\
      \ the product of the two subtrees, where total_sum is the total sum of the binary\
      \ tree and subtree_sum is the sum of the current subtree."
    time_complexity: The time complexity of the algorithm is O(n), where n is the number
      of nodes in the binary tree. This is because we perform two DFS traversals over
      the binary tree, each of which takes O(n) time. The first traversal calculates
      the total sum of the binary tree, and the second traversal calculates the sum
      of each subtree and finds the maximum product of two subtrees.
    space_complexity: The space complexity of the algorithm is O(n), where n is the
      number of nodes in the binary tree. This is because we store the sum of each subtree
      in a list, which takes O(n) space. We also use a recursive call stack to perform
      the DFS traversals, which takes O(h) space, where h is the height of the binary
      tree. However, in the worst case, the binary tree is skewed and h = n, so the
      space complexity is O(n).
    elapsed_time: 12.04398226737976
    model: llama-3.3-70b-versatile
    generated_at: '2026-01-07 01:12:18 '
---

## Problem #1339: Maximum Product of Splitted Binary Tree

**Difficulty:** Medium

**Topics:** Tree, Depth-First Search, Binary Tree

## Problem Description

<p>Given the <code>root</code> of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.</p>

<p>Return <em>the maximum product of the sums of the two subtrees</em>. Since the answer may be too large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p><strong>Note</strong> that you need to maximize the answer before taking the mod and not after taking it.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/01/21/sample_1_1699.png" style="width: 500px; height: 167px;" />
<pre>
<strong>Input:</strong> root = [1,2,3,4,5,6]
<strong>Output:</strong> 110
<strong>Explanation:</strong> Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/01/21/sample_2_1699.png" style="width: 500px; height: 211px;" />
<pre>
<strong>Input:</strong> root = [1,null,2,3,4,null,null,5,6]
<strong>Output:</strong> 90
<strong>Explanation:</strong> Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[2, 5 * 10<sup>4</sup>]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 10<sup>4</sup></code></li>
</ul>


## Hints

1. If we know the sum of a subtree, the answer is max( (total_sum - subtree_sum) * subtree_sum) in each node.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2026-01-07 01:11:51 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks us to find the maximum product of sums of two subtrees formed by removing a single edge from the given binary tree. We need to return this maximum product modulo 10^9 + 7, ensuring that the maximization happens before applying the modulo. The core idea is that if we remove an edge, the tree splits into two parts: one is the subtree rooted at the child node of the removed edge, and the other is the rest of the original tree. If we know the sum of the entire tree (let's call it `total_sum`) and the sum of any subtree (let's call it `subtree_sum`), then the sum of the other part will be `total_sum - subtree_sum`. The product for this specific split would be `subtree_sum * (total_sum - subtree_sum).`

To find the maximum product, we perform a Depth First Search (DFS) traversal on the tree. During this traversal, for every node, we calculate the sum of the subtree rooted at that node. These subtree sums are collected into a list. The DFS function returns the sum of the current subtree, which is `node.val + sum(left_child_subtree) + sum(right_child_subtree)`. After the DFS completes, the sum returned by the initial call on the root node will be the `total_sum` of the entire tree. We then iterate through the collected list of all subtree sums. For each `s` in this list, we calculate the product `s * (total_sum - s)` and update our `max_product` if the current product is greater. Since the product can be very large, we use 64-bit integers (or `BigInt` in JavaScript/TypeScript) for sums and products to avoid overflow before taking the final modulo.

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
class Solution {
public:
    std::vector<long long> all_subtree_sums;

    long long dfs(TreeNode* node) {
        if (!node) {
            return 0;
        }

        long long left_sum = dfs(node->left);
        long long right_sum = dfs(node->right);

        long long current_subtree_sum = node->val + left_sum + right_sum;
        all_subtree_sums.push_back(current_subtree_sum);

        return current_subtree_sum;
    }

    int maxProduct(TreeNode* root) {
        all_subtree_sums.clear(); // Clear for multiple test cases
        long long total_sum = dfs(root);

        long long max_prod = 0;
        long long MOD = 1e9 + 7;

        for (long long s : all_subtree_sums) {
            max_prod = std::max(max_prod, s * (total_sum - s));
        }

        return max_prod % MOD;
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
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    List<Long> allSubtreeSums = new ArrayList<>();

    private long dfs(TreeNode node) {
        if (node == null) {
            return 0;
        }

        long leftSum = dfs(node.left);
        long rightSum = dfs(node.right);

        long currentSubtreeSum = node.val + leftSum + rightSum;
        allSubtreeSums.add(currentSubtreeSum);

        return currentSubtreeSum;
    }

    public int maxProduct(TreeNode root) {
        allSubtreeSums.clear(); // Clear for multiple test cases
        long totalSum = dfs(root);

        long maxProd = 0;
        long MOD = 1_000_000_007;

        for (long s : allSubtreeSums) {
            maxProd = Math.max(maxProd, s * (totalSum - s));
        }

        return (int)(maxProd % MOD);
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
class Solution(object):
    def maxProduct(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        all_subtree_sums = []

        def dfs(node):
            if not node:
                return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            current_subtree_sum = node.val + left_sum + right_sum
            all_subtree_sums.append(current_subtree_sum)

            return current_subtree_sum

        total_sum = dfs(root)

        max_prod = 0
        MOD = 10**9 + 7

        for s in all_subtree_sums:
            max_prod = max(max_prod, s * (total_sum - s))

        return max_prod % MOD
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
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        all_subtree_sums = []

        def dfs(node):
            if not node:
                return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            current_subtree_sum = node.val + left_sum + right_sum
            all_subtree_sums.append(current_subtree_sum)

            return current_subtree_sum

        total_sum = dfs(root)

        max_prod = 0
        MOD = 10**9 + 7

        for s in all_subtree_sums:
            max_prod = max(max_prod, s * (total_sum - s))

        return max_prod % MOD
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

// Global variables to store subtree sums and their count
// Max nodes 5 * 10^4, so an array of this size is sufficient.
#define MAX_NODES 50001 
long long g_all_subtree_sums[MAX_NODES];
int g_subtree_sums_count;

long long dfs_c(struct TreeNode* node) {
    if (node == NULL) {
        return 0;
    }

    long long left_sum = dfs_c(node->left);
    long long right_sum = dfs_c(node->right);

    long long current_subtree_sum = (long long)node->val + left_sum + right_sum;
    g_all_subtree_sums[g_subtree_sums_count++] = current_subtree_sum;

    return current_subtree_sum;
}

int maxProduct(struct TreeNode* root) {
    g_subtree_sums_count = 0; // Reset for each test case
    long long total_sum = dfs_c(root);

    long long max_prod = 0;
    long long MOD = 1000000007; // 10^9 + 7

    for (int i = 0; i < g_subtree_sums_count; ++i) {
        long long s = g_all_subtree_sums[i];
        long long current_prod = s * (total_sum - s);
        if (current_prod > max_prod) {
            max_prod = current_prod;
        }
    }

    return (int)(max_prod % MOD);
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
    private List<long> allSubtreeSums;
    private const int MOD = 1_000_000_007;

    public int MaxProduct(TreeNode root) {
        allSubtreeSums = new List<long>();

        long totalSum = DfsCalculateSums(root);

        long maxProduct = 0;
        foreach (long s in allSubtreeSums) {
            maxProduct = Math.Max(maxProduct, s * (totalSum - s));
        }

        return (int)(maxProduct % MOD);
    }

    private long DfsCalculateSums(TreeNode node) {
        if (node == null) {
            return 0;
        }

        long leftSum = DfsCalculateSums(node.left);
        long rightSum = DfsCalculateSums(node.right);

        long currentSubtreeSum = node.val + leftSum + rightSum;
        allSubtreeSums.Add(currentSubtreeSum);
        return currentSubtreeSum;
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
var maxProduct = function(root) {
    const allSubtreeSums = [];
    const MOD = 1_000_000_007;

    const dfsCalculateSums = (node) => {
        if (node === null) {
            return 0n;
        }

        const leftSum = dfsCalculateSums(node.left);
        const rightSum = dfsCalculateSums(node.right);

        const currentSubtreeSum = BigInt(node.val) + leftSum + rightSum;
        allSubtreeSums.push(currentSubtreeSum);
        return currentSubtreeSum;
    };

    const totalSum = dfsCalculateSums(root);

    let maxProductVal = 0n;

    for (const s of allSubtreeSums) {
        const currentProduct = s * (totalSum - s);
        if (currentProduct > maxProductVal) {
            maxProductVal = currentProduct;
        }
    }

    return Number(maxProductVal % BigInt(MOD));
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

function maxProduct(root: TreeNode | null): number {
    const allSubtreeSums: bigint[] = [];
    const MOD: number = 1_000_000_007;

    const dfsCalculateSums = (node: TreeNode | null): bigint => {
        if (node === null) {
            return 0n;
        }

        const leftSum: bigint = dfsCalculateSums(node.left);
        const rightSum: bigint = dfsCalculateSums(node.right);

        const currentSubtreeSum: bigint = BigInt(node.val) + leftSum + rightSum;
        allSubtreeSums.push(currentSubtreeSum);
        return currentSubtreeSum;
    };

    const totalSum: bigint = dfsCalculateSums(root);

    let maxProductVal: bigint = 0n;

    for (const s of allSubtreeSums) {
        const currentProduct: bigint = s * (totalSum - s);
        if (currentProduct > maxProductVal) {
            maxProductVal = currentProduct;
        }
    }

    return Number(maxProductVal % BigInt(MOD));
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
     * @var int[]
     */
    private $allSubtreeSums;
    private const MOD = 1_000_000_007;

    /**
     * @param TreeNode $root
     * @return Integer
     */
    function maxProduct($root) {
        $this->allSubtreeSums = [];

        $totalSum = $this->dfsCalculateSums($root);

        $maxProduct = 0;
        foreach ($this->allSubtreeSums as $s) {
            $maxProduct = max($maxProduct, $s * ($totalSum - $s));
        }

        return $maxProduct % self::MOD;
    }

    /**
     * @param TreeNode $node
     * @return int
     */
    private function dfsCalculateSums($node) {
        if ($node === null) {
            return 0;
        }

        $leftSum = $this->dfsCalculateSums($node->left);
        $rightSum = $this->dfsCalculateSums($node->right);

        $currentSubtreeSum = $node->val + $leftSum + $rightSum;
        $this->allSubtreeSums[] = $currentSubtreeSum;
        return $currentSubtreeSum;
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
    private var allSubtreeSums: [Int] = []
    private let MOD = 1_000_000_007

    func maxProduct(_ root: TreeNode?) -> Int {
        allSubtreeSums = []

        let totalSum = dfsCalculateSums(root)

        var maxProduct: Int = 0
        for s in allSubtreeSums {
            maxProduct = max(maxProduct, s * (totalSum - s))
        }

        return maxProduct % MOD
    }

    private func dfsCalculateSums(_ node: TreeNode?) -> Int {
        guard let node = node else {
            return 0
        }

        let leftSum = dfsCalculateSums(node.left)
        let rightSum = dfsCalculateSums(node.right)

        let currentSubtreeSum = node.val + leftSum + rightSum
        allSubtreeSums.append(currentSubtreeSum)
        return currentSubtreeSum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun maxProduct(root: TreeNode?): Int {
        val allSubtreeSums = mutableListOf<Long>()
        val MOD = 1_000_000_007

        val totalSum = dfs(root, allSubtreeSums)

        var maxProd: Long = 0

        for (s in allSubtreeSums) {
            val currentProd = s * (totalSum - s)
            if (currentProd > maxProd) {
                maxProd = currentProd
            }
        }

        return (maxProd % MOD).toInt()
    }

    fun dfs(node: TreeNode?, allSubtreeSums: MutableList<Long>): Long {
        if (node == null) {
            return 0L
        }

        val leftSum = dfs(node.left, allSubtreeSums)
        val rightSum = dfs(node.right, allSubtreeSums)

        val currentSubtreeSum = node.`val`.toLong() + leftSum + rightSum
        allSubtreeSums.add(currentSubtreeSum)
        return currentSubtreeSum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
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
  int maxProduct(TreeNode? root) {
    List<int> allSubtreeSums = [];
    final int MOD = 1000000007;

    int dfs(TreeNode? node) {
      if (node == null) {
        return 0;
      }

      int leftSum = dfs(node.left);
      int rightSum = dfs(node.right);

      int currentSubtreeSum = node.val + leftSum + rightSum;
      allSubtreeSums.add(currentSubtreeSum);
      return currentSubtreeSum;
    }

    int totalSum = dfs(root);

    int maxProd = 0;

    for (int s in allSubtreeSums) {
      int currentProd = s * (totalSum - s);
      if (currentProd > maxProd) {
        maxProd = currentProd;
      }
    }

    return (maxProd % MOD);
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func maxProduct(root *TreeNode) int {
    allSubtreeSums := []int64{}
    MOD := int64(1_000_000_007)

    var dfs func(*TreeNode) int64
    dfs = func(node *TreeNode) int64 {
        if node == nil {
            return 0
        }

        leftSum := dfs(node.Left)
        rightSum := dfs(node.Right)

        currentSubtreeSum := int64(node.Val) + leftSum + rightSum
        allSubtreeSums = append(allSubtreeSums, currentSubtreeSum)
        return currentSubtreeSum
    }

    totalSum := dfs(root)

    var maxProd int64 = 0

    for _, s := range allSubtreeSums {
        currentProd := s * (totalSum - s)
        if currentProd > maxProd {
            maxProd = currentProd
        }
    }

    return int(maxProd % MOD)
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
def max_product(root)
    all_subtree_sums = []
    mod = 1_000_000_007

    dfs = lambda do |node|
        return 0 if node.nil?

        left_sum = dfs.call(node.left)
        right_sum = dfs.call(node.right)

        current_subtree_sum = node.val + left_sum + right_sum
        all_subtree_sums << current_subtree_sum
        current_subtree_sum
    end

    total_sum = dfs.call(root)

    max_prod = 0

    all_subtree_sums.each do |s|
        current_prod = s * (total_sum - s)
        max_prod = current_prod if current_prod > max_prod
    end

    (max_prod % mod)
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
/**
 * Definition for a binary tree node.
 * class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
 *   var value: Int = _value
 *   var left: TreeNode = _left
 *   var right: TreeNode = _right
 * }
 */
object Solution {
    def maxProduct(root: TreeNode): Int = {
        val allSubtreeSums = collection.mutable.ListBuffer[Long]()
        val MOD = 1_000_000_007L

        def dfs(node: TreeNode): Long = {
            if (node == null) {
                return 0L
            }

            val leftSum = dfs(node.left)
            val rightSum = dfs(node.right)

            val currentSubtreeSum = node.value.toLong + leftSum + rightSum
            allSubtreeSums += currentSubtreeSum
            currentSubtreeSum
        }

        val totalSum = dfs(root)

        var maxProd: Long = 0L

        for (s <- allSubtreeSums) {
            val currentProd = s * (totalSum - s)
            if (currentProd > maxProd) {
                maxProd = currentProd
            }
        }

        (maxProd % MOD).toInt
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

// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>> >,
//   pub right: Option<Rc<RefCell<TreeNode>> >,
// }
// 
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
impl Solution {
    pub fn max_product(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut max_prod: i64 = 0;
        let modulo: i64 = 1_000_000_007;

        // First pass: calculate total sum of the entire tree
        let total_sum = Self::calculate_total_sum(root.clone());

        // Second pass: traverse the tree, calculate subtree sums, and update max_prod
        Self::dfs_maximize_product(root, total_sum, &mut max_prod);

        (max_prod % modulo) as i32
    }

    // Helper function to calculate the total sum of all nodes in the tree
    fn calculate_total_sum(node: Option<Rc<RefCell<TreeNode>>>) -> i64 {
        if let Some(n_rc) = node {
            let n = n_rc.borrow();
            (n.val as i64)
                + Self::calculate_total_sum(n.left.clone())
                + Self::calculate_total_sum(n.right.clone())
        } else {
            0
        }
    }

    // Helper function to perform DFS, calculate subtree sums, and update the maximum product
    fn dfs_maximize_product(
        node: Option<Rc<RefCell<TreeNode>>>,
        total_sum: i64,
        max_prod: &mut i64,
    ) -> i64 {
        if let Some(n_rc) = node {
            let n = n_rc.borrow();
            let left_sum = Self::dfs_maximize_product(n.left.clone(), total_sum, max_prod);
            let right_sum = Self::dfs_maximize_product(n.right.clone(), total_sum, max_prod);
            let current_subtree_sum = (n.val as i64) + left_sum + right_sum;

            // Calculate the product for this split and update max_prod
            let product = current_subtree_sum * (total_sum - current_subtree_sum);
            if product > *max_prod {
                *max_prod = product;
            }

            current_subtree_sum
        } else {
            0
        }
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

(define/contract (max-product root)
  (-> (or/c tree-node? #f) exact-integer?)
  (define MOD 1000000007)
  (define max-prod 0) ; Mutable variable to store the maximum product

  ; First pass: calculate the total sum of all nodes in the tree
  (define (calculate-total-sum node)
    (if (not node)
        0
        (+ (tree-node-val node)
           (calculate-total-sum (tree-node-left node))
           (calculate-total-sum (tree-node-right node)))))

  (define total-sum (calculate-total-sum root))

  ; Second pass: perform DFS, calculate subtree sums, and update max-prod
  (define (dfs-maximize-product node)
    (if (not node)
        0
        (let* ([left-sum (dfs-maximize-product (tree-node-left node))]
               [right-sum (dfs-maximize-product (tree-node-right node))]
               [current-subtree-sum (+ (tree-node-val node) left-sum right-sum)])

          ; Calculate the product for this split and update max-prod
          (set! max-prod (max max-prod (* current-subtree-sum (- total-sum current-subtree-sum))))

          current-subtree-sum)))

  (dfs-maximize-product root)
  (modulo max-prod MOD))
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

-spec max_product(Root :: #tree_node{} | null) -> integer().
max_product(Root) ->
  MOD = 1_000_000_007,

  % First pass: calculate the total sum of all nodes in the tree
  TotalSum = calculate_total_sum(Root),

  % Second pass: perform DFS, calculate subtree sums, and update max_prod
  % The max_prod is accumulated and passed through the recursive calls
  {_FinalSubtreeSum, MaxProd} = dfs_maximize_product(Root, TotalSum, 0),

  MaxProd rem MOD.

% Helper function to calculate the total sum of all nodes in the tree
calculate_total_sum(null) -> 0;
calculate_total_sum(#tree_node{val = Val, left = Left, right = Right}) ->
  Val + calculate_total_sum(Left) + calculate_total_sum(Right).

% Helper function to perform DFS, calculate subtree sums, and update the maximum product
% Returns {CurrentSubtreeSum, MaxProductSoFar}
dfs_maximize_product(null, _TotalSum, MaxProdAcc) ->
  {0, MaxProdAcc};
dfs_maximize_product(#tree_node{val = Val, left = Left, right = Right}, TotalSum, MaxProdAcc) ->
  {LeftSum, MaxProdAfterLeft} = dfs_maximize_product(Left, TotalSum, MaxProdAcc),
  {RightSum, MaxProdAfterRight} = dfs_maximize_product(Right, TotalSum, MaxProdAfterLeft),

  CurrentSubtreeSum = Val + LeftSum + RightSum,
  CurrentProduct = CurrentSubtreeSum * (TotalSum - CurrentSubtreeSum),

  % Update MaxProdAcc with the maximum product found so far
  NewMaxProd = max(MaxProdAfterRight, CurrentProduct),

  {CurrentSubtreeSum, NewMaxProd}.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
# Definition for a binary tree node.
#
# defmodule TreeNode do
#   @type t :: %__MODULE__{
#           val: integer,
#           left: TreeNode.t() | nil,
#           right: TreeNode.t() | nil
#         }
#   defstruct val: 0, left: nil, right: nil
# end

defmodule Solution do
  @spec max_product(root :: TreeNode.t | nil) :: integer
  def max_product(root) do
    mod = 1_000_000_007

    # First pass: calculate the total sum of all nodes in the tree
    total_sum = calculate_total_sum(root)

    # Second pass: perform DFS, calculate subtree sums, and update max_prod
    # The max_prod is accumulated and passed through the recursive calls
    {_final_subtree_sum, max_prod} = dfs_maximize_product(root, total_sum, 0)

    rem(max_prod, mod)
  end

  # Helper function to calculate the total sum of all nodes in the tree
  defp calculate_total_sum(nil), do: 0
  defp calculate_total_sum(%TreeNode{val: val, left: left, right: right}) do
    val + calculate_total_sum(left) + calculate_total_sum(right)
  end

  # Helper function to perform DFS, calculate subtree sums, and update the maximum product
  # Returns {current_subtree_sum, max_product_so_far}
  defp dfs_maximize_product(nil, _total_sum, max_prod_acc) do
    {0, max_prod_acc}
  end
  defp dfs_maximize_product(%TreeNode{val: val, left: left, right: right}, total_sum, max_prod_acc) do
    {left_sum, max_prod_after_left} = dfs_maximize_product(left, total_sum, max_prod_acc)
    {right_sum, max_prod_after_right} = dfs_maximize_product(right, total_sum, max_prod_after_left)

    current_subtree_sum = val + left_sum + right_sum
    current_product = current_subtree_sum * (total_sum - current_subtree_sum)

    # Update max_prod_acc with the maximum product found so far
    new_max_prod = max(max_prod_after_right, current_product)

    {current_subtree_sum, new_max_prod}
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is O(N), where N is the number of nodes in the binary tree. This is because we perform a single Depth First Search (DFS) traversal to calculate all subtree sums, visiting each node exactly once. After collecting all N subtree sums, we iterate through this list once to find the maximum product, which also takes O(N) time. Thus, the total time complexity is dominated by these two linear passes.

- **Space Complexity:** The space complexity is O(N). This is primarily due to storing all N subtree sums in a list or array. Additionally, the recursion stack for the DFS traversal can go up to a depth of N in the worst case (for a skewed tree) or O(log N) in the best case (for a balanced tree). Therefore, the overall space complexity is O(N).

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2026-01-07 01:12:18 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem is solved by first calculating the total sum of the binary tree. Then, we calculate the sum of each subtree and store it in a list. Finally, we iterate over the list to find the maximum product of two subtrees. The key intuition here is that the maximum product will occur when the two subtrees have sums that are as close as possible to each other. This is because the product of two numbers is maximized when the numbers are as close as possible to each other, given a fixed sum. 
  The algorithm works by first calculating the total sum of the binary tree using a depth-first search (DFS) traversal. Then, we calculate the sum of each subtree using another DFS traversal and store it in a list. Finally, we iterate over the list to find the maximum product of two subtrees. We use the formula (total_sum - subtree_sum) * subtree_sum to calculate the product of the two subtrees, where total_sum is the total sum of the binary tree and subtree_sum is the sum of the current subtree.

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
    int maxProduct(TreeNode* root) {
        long long total = 0;
        vector<long long> sums;
        total = getTotalSum(root, sums);
        long long maxProduct = 0;
        for (long long sum : sums) {
            maxProduct = max(maxProduct, sum * (total - sum));
        }
        return maxProduct % (1000000007);
    }

    long long getTotalSum(TreeNode* root, vector<long long>& sums) {
        if (root == nullptr) return 0;
        long long sum = root->val + getTotalSum(root->left, sums) + getTotalSum(root->right, sums);
        sums.push_back(sum);
        return sum;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int maxProduct(TreeNode root) {
        long total = 0;
        List<Long> sums = new ArrayList<>();
        total = getTotalSum(root, sums);
        long maxProduct = 0;
        for (long sum : sums) {
            maxProduct = Math.max(maxProduct, sum * (total - sum));
        }
        return (int)(maxProduct % (1000000007));
    }

    private long getTotalSum(TreeNode root, List<Long> sums) {
        if (root == null) return 0;
        long sum = root.val + getTotalSum(root.left, sums) + getTotalSum(root.right, sums);
        sums.add(sum);
        return sum;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def maxProduct(self, root):
        total = [0]
        sums = []
        self.getTotalSum(root, sums)
        total[0] = sum(sums)
        maxProduct = 0
        for sum in sums:
            maxProduct = max(maxProduct, sum * (total[0] - sum))
        return maxProduct % (10**9 + 7)

    def getTotalSum(self, root, sums):
        if not root:
            return 0
        sum = root.val + self.getTotalSum(root.left, sums) + self.getTotalSum(root.right, sums)
        sums.append(sum)
        return sum
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        total = [0]
        sums = []
        self.getTotalSum(root, sums)
        total[0] = sum(sums)
        maxProduct = 0
        for sum in sums:
            maxProduct = max(maxProduct, sum * (total[0] - sum))
        return maxProduct % (10**9 + 7)

    def getTotalSum(self, root, sums):
        if not root:
            return 0
        sum = root.val + self.getTotalSum(root.left, sums) + self.getTotalSum(root.right, sums)
        sums.append(sum)
        return sum
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
int maxProduct(struct TreeNode* root) {
    long long total = 0;
    long long* sums = NULL;
    int size = 0;
    total = getTotalSum(root, &sums, &size);
    long long maxProduct = 0;
    for (int i = 0; i < size; i++) {
        maxProduct = (maxProduct > sums[i] * (total - sums[i])) ? maxProduct : sums[i] * (total - sums[i]);
    }
    free(sums);
    return maxProduct % 1000000007;
}

long long getTotalSum(struct TreeNode* root, long long** sums, int* size) {
    if (root == NULL) return 0;
    long long sum = root->val + getTotalSum(root->left, sums, size) + getTotalSum(root->right, sums, size);
    (*sums) = realloc((*sums), ((*size) + 1) * sizeof(long long));
    (*sums)[(*size)] = sum;
    (*size)++;
    return sum;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MaxProduct(TreeNode root) {
        long total = TotalSum(root);
        long max = 0;
        long res = SubtreeSum(root, total, ref max);
        return (int)(max % (Math.Pow(10, 9) + 7));
    }
    private long TotalSum(TreeNode root) {
        if (root == null) return 0;
        return root.val + TotalSum(root.left) + TotalSum(root.right);
    }
    private long SubtreeSum(TreeNode root, long total, ref long max) {
        if (root == null) return 0;
        long sum = root.val + SubtreeSum(root.left, total, ref max) + SubtreeSum(root.right, total, ref max);
        max = Math.Max(max, sum * (total - sum));
        return sum;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var maxProduct = function(root) {
    let total = totalSum(root);
    let max = 0;
    subtreeSum(root, total, max);
    return max % (Math.pow(10, 9) + 7);
};
function totalSum(root) {
    if (!root) return 0;
    return root.val + totalSum(root.left) + totalSum(root.right);
}
function subtreeSum(root, total, max) {
    if (!root) return 0;
    let sum = root.val + subtreeSum(root.left, total, max) + subtreeSum(root.right, total, max);
    max = Math.max(max, sum * (total - sum));
    return sum;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maxProduct(root: TreeNode | null): number {
    let total: number = totalSum(root);
    let max: number = 0;
    subtreeSum(root, total, max);
    return max % (Math.pow(10, 9) + 7);
}
function totalSum(root: TreeNode | null): number {
    if (!root) return 0;
    return root.val + totalSum(root.left) + totalSum(root.right);
}
function subtreeSum(root: TreeNode | null, total: number, max: number): number {
    if (!root) return 0;
    let sum: number = root.val + subtreeSum(root.left, total, max) + subtreeSum(root.right, total, max);
    max = Math.max(max, sum * (total - sum));
    return sum;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
class Solution {
    function maxProduct($root) {
        $total = $this->totalSum($root);
        $max = 0;
        $this->subtreeSum($root, $total, $max);
        return $max % (pow(10, 9) + 7);
    }
    function totalSum($root) {
        if (!$root) return 0;
        return $root->val + $this->totalSum($root->left) + $this->totalSum($root->right);
    }
    function subtreeSum($root, $total, &$max) {
        if (!$root) return 0;
        $sum = $root->val + $this->subtreeSum($root->left, $total, $max) + $this->subtreeSum($root->right, $total, $max);
        $max = max($max, $sum * ($total - $sum));
        return $sum;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
class Solution {
    func maxProduct(_ root: TreeNode?) -> Int {
        let total = totalSum(root)
        var max: Int64 = 0
        _ = subtreeSum(root, total, &max)
        return Int(max % (Int64(pow(10, 9)) + 7))
    }
    func totalSum(_ root: TreeNode?) -> Int64 {
        guard let root = root else { return 0 }
        return Int64(root.val) + totalSum(root.left) + totalSum(root.right)
    }
    func subtreeSum(_ root: TreeNode?, _ total: Int64, _ max: inout Int64) -> Int64 {
        guard let root = root else { return 0 }
        let sum = Int64(root.val) + subtreeSum(root.left, total, &max) + subtreeSum(root.right, total, &max)
        max = max(max, sum * (total - sum))
        return sum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun maxProduct(root: TreeNode?): Int {
        val MOD = 1000000007
        var totalSum = 0
        var maxProduct = 0
        totalSum = sum(root)
        sum(root, totalSum, { a, b -> maxProduct = Math.max(maxProduct, a * b) })
        return maxProduct % MOD
    }
    fun sum(root: TreeNode?, totalSum: Int = 0, callback: (Int, Int) -> Unit = { _, _ -> }): Int {
        if (root == null) return 0
        val sum = root.`val` + sum(root.left, totalSum, callback) + sum(root.right, totalSum, callback)
        callback(sum, totalSum - sum)
        return sum
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int maxProduct(TreeNode? root) {
    final mod = 1000000007;
    int totalSum = 0;
    int maxProduct = 0;
    totalSum = sum(root);
    sum(root, totalSum, (a, b) => maxProduct = max(maxProduct, a * b));
    return maxProduct % mod;
  }
  int sum(TreeNode? root, [int totalSum = 0, Function? callback]) {
    if (root == null) return 0;
    final sum = root.val + sum(root.left, totalSum, callback) + sum(root.right, totalSum, callback);
    if (callback != null) callback(sum, totalSum - sum);
    return sum;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func maxProduct(root *TreeNode) int {
    mod := 1000000007
    var totalSum int
    var maxProduct int
    totalSum = sum(root)
    sum(root, &totalSum, &maxProduct)
    return maxProduct % mod
}
func sum(root *TreeNode, totalSum *int, maxProduct *int) int {
    if root == nil {
        return 0
    }
    sum := root.Val + sum(root.Left, totalSum, maxProduct) + sum(root.Right, totalSum, maxProduct)
    product := sum * (*totalSum - sum)
    if product > *maxProduct {
        *maxProduct = product
    }
    return sum
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def max_product(root)
    mod = 1000000007
    total_sum = 0
    max_product = 0
    total_sum = sum(root)
    sum(root, total_sum, max_product)
    max_product % mod
end

def sum(root, total_sum = 0, max_product = 0)
    return 0 if root.nil?
    sum = root.val + sum(root.left, total_sum, max_product) + sum(root.right, total_sum, max_product)
    product = sum * (total_sum - sum)
    max_product = [max_product, product].max
    sum
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def maxProduct(root: TreeNode): Int = {
        val mod = 1000000007
        var totalSum = 0
        var maxProduct = 0
        totalSum = sum(root)
        sum(root, totalSum, (a, b) => maxProduct = Math.max(maxProduct, a * b))
        maxProduct % mod
    }
    def sum(root: TreeNode, totalSum: Int = 0, callback: (Int, Int) => Unit = (a, b) => ()): Int = {
        if (root == null) return 0
        val sum = root.value + sum(root.left, totalSum, callback) + sum(root.right, totalSum, callback)
        callback(sum, totalSum - sum)
        sum
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
impl Solution {
    pub fn max_product(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let total_sum = Self::get_total_sum(&root);
        let mut max_product = 0;
        Self::get_max_product(&root, total_sum, &mut max_product);
        max_product as i32 % 1000000007
    }

    fn get_total_sum(root: &Option<Rc<RefCell<TreeNode>>>) -> i64 {
        match root {
            Some(node) => node.borrow().val as i64 + Self::get_total_sum(&node.borrow().left) + Self::get_total_sum(&node.borrow().right),
            None => 0,
        }
    }

    fn get_max_product(root: &Option<Rc<RefCell<TreeNode>>>, total_sum: i64, max_product: &mut i64) {
        match root {
            Some(node) => {
                let left_sum = Self::get_total_sum(&node.borrow().left);
                let right_sum = Self::get_total_sum(&node.borrow().right);
                let current_sum = left_sum + right_sum + node.borrow().val as i64;
                *max_product = (*max_product).max((total_sum - current_sum) * current_sum);
                Self::get_max_product(&node.borrow().left, total_sum, max_product);
                Self::get_max_product(&node.borrow().right, total_sum, max_product);
            }
            None => (),
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
define/contract (max-product root)
  (-> (or/c tree-node? #f) exact-integer?)
  (let ([total-sum (get-total-sum root)])
    (let ([max-product 0])
      (get-max-product root total-sum max-product)
      (modulo max-product 1000000007)))

(define (get-total-sum root)
  (if (tree-node? root)
      (+ (tree-node-val root) (get-total-sum (tree-node-left root)) (get-total-sum (tree-node-right root)))
      0))

(define (get-max-product root total-sum max-product)
  (if (tree-node? root)
      (let ([left-sum (get-total-sum (tree-node-left root))]
            [right-sum (get-total-sum (tree-node-right root))]
            [current-sum (+ left-sum right-sum (tree-node-val root))])
        (set! max-product (max max-product (* (- total-sum current-sum) current-sum)))
        (get-max-product (tree-node-left root) total-sum max-product)
        (get-max-product (tree-node-right root) total-sum max-product))
      max-product))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
max_product(Root) ->
  TotalSum = get_total_sum(Root),
  MaxProduct = get_max_product(Root, TotalSum, 0),
  MaxProduct rem 1000000007.

get_total_sum(null) -> 0;
get_total_sum(#tree_node{val = Val, left = Left, right = Right}) ->
  Val + get_total_sum(Left) + get_total_sum(Right).

get_max_product(null, _TotalSum, MaxProduct) -> MaxProduct;
get_max_product(#tree_node{val = Val, left = Left, right = Right}, TotalSum, MaxProduct) ->
  LeftSum = get_total_sum(Left),
  RightSum = get_total_sum(Right),
  CurrentSum = LeftSum + RightSum + Val,
  NewMaxProduct = max(MaxProduct, (TotalSum - CurrentSum) * CurrentSum),
  get_max_product(Left, TotalSum, NewMaxProduct),
  get_max_product(Right, TotalSum, NewMaxProduct).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec max_product(root :: TreeNode.t | nil) :: integer
  def max_product(root) do
    total_sum = get_total_sum(root)
    max_product = get_max_product(root, total_sum, 0)
    rem(max_product, 1_000_000_007)
  end

  defp get_total_sum(nil), do: 0
  defp get_total_sum(%TreeNode{val: val, left: left, right: right}) do
    val + get_total_sum(left) + get_total_sum(right)
  end

  defp get_max_product(nil, _total_sum, max_product), do: max_product
  defp get_max_product(%TreeNode{val: val, left: left, right: right}, total_sum, max_product) do
    left_sum = get_total_sum(left)
    right_sum = get_total_sum(right)
    current_sum = left_sum + right_sum + val
    new_max_product = max(max_product, (total_sum - current_sum) * current_sum)
    get_max_product(left, total_sum, new_max_product)
    get_max_product(right, total_sum, new_max_product)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of the algorithm is O(n), where n is the number of nodes in the binary tree. This is because we perform two DFS traversals over the binary tree, each of which takes O(n) time. The first traversal calculates the total sum of the binary tree, and the second traversal calculates the sum of each subtree and finds the maximum product of two subtrees.

- **Space Complexity:** The space complexity of the algorithm is O(n), where n is the number of nodes in the binary tree. This is because we store the sum of each subtree in a list, which takes O(n) space. We also use a recursive call stack to perform the DFS traversals, which takes O(h) space, where h is the height of the binary tree. However, in the worst case, the binary tree is skewed and h = n, so the space complexity is O(n).

</div>
</details>
