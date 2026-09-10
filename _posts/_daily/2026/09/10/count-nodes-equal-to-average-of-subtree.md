---
layout: post
title: "Count Nodes Equal to Average of Subtree"
date: 2026-09-10 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Tree", "Depth-First Search", "Binary Tree"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/
ai_solutions:
  - solutions:
      cpp: "/**\n * Definition for a binary tree node.\n * struct TreeNode {\n *   \
        \  int val;\n *     TreeNode *left;\n *     TreeNode *right;\n *     TreeNode()\
        \ : val(0), left(nullptr), right(nullptr) {}\n *     TreeNode(int x) : val(x),\
        \ left(nullptr), right(nullptr) {}\n *     TreeNode(int x, TreeNode *left, TreeNode\
        \ *right) : val(x), left(left), right(right) {}\n * };\n */\nclass Solution\
        \ {\npublic:\n    struct Result {\n        int sum;\n        int count;\n  \
        \  };\n\n    Result traverse(TreeNode* node, int& totalCount) {\n        if\
        \ (!node) return {0, 0};\n\n        Result left = traverse(node->left, totalCount);\n\
        \        Result right = traverse(node->right, totalCount);\n\n        int currentSum\
        \ = node->val + left.sum + right.sum;\n        int currentCount = 1 + left.count\
        \ + right.count;\n\n        if (node->val == currentSum / currentCount) {\n\
        \            totalCount++;\n        }\n\n        return {currentSum, currentCount};\n\
        \    }\n\n    int averageOfSubtree(TreeNode* root) {\n        int result = 0;\n\
        \        traverse(root, result);\n        return result;\n    }\n};"
      java: "/**\n * Definition for a binary tree node.\n * public class TreeNode {\n\
        \ *     int val;\n *     TreeNode left;\n *     TreeNode right;\n *     TreeNode()\
        \ {}\n *     TreeNode(int val) { this.val = val; }\n *     TreeNode(int val,\
        \ TreeNode left, TreeNode right) {\n *         this.val = val;\n *         this.left\
        \ = left;\n *         this.right = right;\n *     }\n * }\n */\nclass Solution\
        \ {\n    private int matchingNodes = 0;\n\n    public int averageOfSubtree(TreeNode\
        \ root) {\n        calculateSubtree(root);\n        return matchingNodes;\n\
        \    }\n\n    private int[] calculateSubtree(TreeNode node) {\n        if (node\
        \ == null) {\n            return new int[]{0, 0}; // {sum, count}\n        }\n\
        \n        int[] left = calculateSubtree(node.left);\n        int[] right = calculateSubtree(node.right);\n\
        \n        int sum = node.val + left[0] + right[0];\n        int count = 1 +\
        \ left[1] + right[1];\n\n        if (node.val == sum / count) {\n          \
        \  matchingNodes++;\n        }\n\n        return new int[]{sum, count};\n  \
        \  }\n}"
      python: "# Definition for a binary tree node.\n# class TreeNode(object):\n#  \
        \   def __init__(self, val=0, left=None, right=None):\n#         self.val =\
        \ val\n#         self.left = left\n#         self.right = right\nclass Solution(object):\n\
        \    def averageOfSubtree(self, root):\n        \"\"\"\n        :type root:\
        \ TreeNode\n        :rtype: int\n        \"\"\"\n        self.res = 0\n\n  \
        \      def dfs(node):\n            if not node:\n                return 0, 0\n\
        \n            left_sum, left_count = dfs(node.left)\n            right_sum,\
        \ right_count = dfs(node.right)\n\n            total_sum = node.val + left_sum\
        \ + right_sum\n            total_count = 1 + left_count + right_count\n\n  \
        \          if node.val == total_sum // total_count:\n                self.res\
        \ += 1\n\n            return total_sum, total_count\n\n        dfs(root)\n \
        \       return self.res"
      python3: "# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self,\
        \ val=0, left=None, right=None):\n#         self.val = val\n#         self.left\
        \ = left\n#         self.right = right\nclass Solution:\n    def averageOfSubtree(self,\
        \ root: TreeNode) -> int:\n        self.count = 0\n\n        def traverse(node):\n\
        \            if not node:\n                return 0, 0\n\n            l_sum,\
        \ l_cnt = traverse(node.left)\n            r_sum, r_cnt = traverse(node.right)\n\
        \n            curr_sum = node.val + l_sum + r_sum\n            curr_cnt = 1\
        \ + l_cnt + r_cnt\n\n            if node.val == (curr_sum // curr_cnt):\n  \
        \              self.count += 1\n\n            return curr_sum, curr_cnt\n\n\
        \        traverse(root)\n        return self.count"
      c: "/**\n * Definition for a binary tree node.\n * struct TreeNode {\n *     int\
        \ val;\n *     struct TreeNode *left;\n *     struct TreeNode *right;\n * };\n\
        \ */\n\nstruct SubtreeInfo {\n    int sum;\n    int count;\n};\n\nstruct SubtreeInfo\
        \ dfs(struct TreeNode* node, int* result) {\n    if (!node) {\n        struct\
        \ SubtreeInfo empty = {0, 0};\n        return empty;\n    }\n\n    struct SubtreeInfo\
        \ left = dfs(node->left, result);\n    struct SubtreeInfo right = dfs(node->right,\
        \ result);\n\n    int currentSum = node->val + left.sum + right.sum;\n    int\
        \ currentCount = 1 + left.count + right.count;\n\n    if (node->val == currentSum\
        \ / currentCount) {\n        (*result)++;\n    }\n\n    struct SubtreeInfo current\
        \ = {currentSum, currentCount};\n    return current;\n}\n\nint averageOfSubtree(struct\
        \ TreeNode* root) {\n    int result = 0;\n    dfs(root, &result);\n    return\
        \ result;\n}"
      csharp: "/**\n * Definition for a binary tree node.\n * public class TreeNode\
        \ {\n *     public int val;\n *     public TreeNode left;\n *     public TreeNode\
        \ right;\n *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null)\
        \ {\n *         this.val = val;\n *         this.left = left;\n *         this.right\
        \ = right;\n *     }\n * }\n */\npublic class Solution {\n    private int result\
        \ = 0;\n\n    public int AverageOfSubtree(TreeNode root) {\n        result =\
        \ 0;\n        Traverse(root);\n        return result;\n    }\n\n    private\
        \ (int sum, int count) Traverse(TreeNode node) {\n        if (node == null)\
        \ {\n            return (0, 0);\n        }\n\n        var left = Traverse(node.left);\n\
        \        var right = Traverse(node.right);\n\n        int currentSum = left.sum\
        \ + right.sum + node.val;\n        int currentCount = left.count + right.count\
        \ + 1;\n\n        if (node.val == (currentSum / currentCount)) {\n         \
        \   result++;\n        }\n\n        return (currentSum, currentCount);\n   \
        \ }\n}"
      javascript: "/**\n * Definition for a binary tree node.\n * function TreeNode(val,\
        \ left, right) {\n *     this.val = (val===undefined ? 0 : val)\n *     this.left\
        \ = (left===undefined ? null : left)\n *     this.right = (right===undefined\
        \ ? null : right)\n * }\n */\n/**\n * @param {TreeNode} root\n * @return {number}\n\
        \ */\nvar averageOfSubtree = function(root) {\n    let result = 0;\n\n    const\
        \ postOrder = (node) => {\n        if (!node) {\n            return [0, 0];\n\
        \        }\n\n        const [leftSum, leftCount] = postOrder(node.left);\n \
        \       const [rightSum, rightCount] = postOrder(node.right);\n\n        const\
        \ currentSum = leftSum + rightSum + node.val;\n        const currentCount =\
        \ leftCount + rightCount + 1;\n\n        if (node.val === Math.floor(currentSum\
        \ / currentCount)) {\n            result++;\n        }\n\n        return [currentSum,\
        \ currentCount];\n    };\n\n    postOrder(root);\n    return result;\n};"
      typescript: "/**\n * Definition for a binary tree node.\n * class TreeNode {\n\
        \ *     val: number\n *     left: TreeNode | null\n *     right: TreeNode |\
        \ null\n *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode\
        \ | null) {\n *         this.val = (val===undefined ? 0 : val)\n *         this.left\
        \ = (left===undefined ? null : left)\n *         this.right = (right===undefined\
        \ ? null : right)\n *     }\n * }\n */\n\nfunction averageOfSubtree(root: TreeNode\
        \ | null): number {\n    let result = 0;\n\n    const traverse = (node: TreeNode\
        \ | null): [number, number] => {\n        if (!node) {\n            return [0,\
        \ 0];\n        }\n\n        const [leftSum, leftCount] = traverse(node.left);\n\
        \        const [rightSum, rightCount] = traverse(node.right);\n\n        const\
        \ currentSum = leftSum + rightSum + node.val;\n        const currentCount =\
        \ leftCount + rightCount + 1;\n\n        if (node.val === Math.floor(currentSum\
        \ / currentCount)) {\n            result++;\n        }\n\n        return [currentSum,\
        \ currentCount];\n    };\n\n    traverse(root);\n    return result;\n};"
      php: "/**\n * Definition for a binary tree node.\n * class TreeNode {\n *    \
        \ public $val = null;\n *     public $left = null;\n *     public $right = null;\n\
        \ *     function __construct($val = 0, $left = null, $right = null) {\n *  \
        \       $this->val = $val;\n *         $this->left = $left;\n *         $this->right\
        \ = $right;\n *     }\n * }\n */\nclass Solution {\n\n    private $ans = 0;\n\
        \n    /**\n     * @param TreeNode $root\n     * @return Integer\n     */\n \
        \   function averageOfSubtree($root) {\n        $this->ans = 0;\n        $this->dfs($root);\n\
        \        return $this->ans;\n    }\n\n    private function dfs($node) {\n  \
        \      if ($node === null) {\n            return [0, 0];\n        }\n\n    \
        \    $left = $this->dfs($node->left);\n        $right = $this->dfs($node->right);\n\
        \n        $currentSum = $left[0] + $right[0] + $node->val;\n        $currentCount\
        \ = $left[1] + $right[1] + 1;\n\n        if ($node->val === (int)($currentSum\
        \ / $currentCount)) {\n            $this->ans++;\n        }\n\n        return\
        \ [$currentSum, $currentCount];\n    }\n}"
      swift: "/**\n * Definition for a binary tree node.\n * public class TreeNode {\n\
        \ *     public var val: Int\n *     public var left: TreeNode?\n *     public\
        \ var right: TreeNode?\n *     public init() { self.val = 0; self.left = nil;\
        \ self.right = nil; }\n *     public init(_ val: Int) { self.val = val; self.left\
        \ = nil; self.right = nil; }\n *     public init(_ val: Int, _ left: TreeNode?,\
        \ _ right: TreeNode?) {\n *         self.val = val\n *         self.left = left\n\
        \ *         self.right = right\n *     }\n * }\n */\nclass Solution {\n    private\
        \ var count = 0\n\n    func averageOfSubtree(_ root: TreeNode?) -> Int {\n \
        \       count = 0\n        _ = calculate(root)\n        return count\n    }\n\
        \n    private func calculate(_ node: TreeNode?) -> (Int, Int) {\n        guard\
        \ let node = node else {\n            return (0, 0)\n        }\n\n        let\
        \ left = calculate(node.left)\n        let right = calculate(node.right)\n\n\
        \        let currentSum = left.0 + right.0 + node.val\n        let currentCount\
        \ = left.1 + right.1 + 1\n\n        if node.val == (currentSum / currentCount)\
        \ {\n            count += 1\n        }\n\n        return (currentSum, currentCount)\n\
        \    }\n}"
      kotlin: "class Solution {\n    private var count = 0\n\n    fun averageOfSubtree(root:\
        \ TreeNode?): Int {\n        count = 0\n        calculateSubtree(root)\n   \
        \     return count\n    }\n\n    private fun calculateSubtree(node: TreeNode?):\
        \ Pair<Int, Int> {\n        if (node == null) {\n            return Pair(0,\
        \ 0)\n        }\n\n        val left = calculateSubtree(node.left)\n        val\
        \ right = calculateSubtree(node.right)\n\n        val totalSum = left.first\
        \ + right.first + node.`val`\n        val totalCount = left.second + right.second\
        \ + 1\n\n        if (totalSum / totalCount == node.`val`) {\n            count++\n\
        \        }\n\n        return Pair(totalSum, totalCount)\n    }\n}"
      dart: "class Solution {\n  int _count = 0;\n\n  int averageOfSubtree(TreeNode?\
        \ root) {\n    _count = 0;\n    _dfs(root);\n    return _count;\n  }\n\n  List<int>\
        \ _dfs(TreeNode? node) {\n    if (node == null) {\n      return [0, 0];\n  \
        \  }\n\n    List<int> left = _dfs(node.left);\n    List<int> right = _dfs(node.right);\n\
        \n    int sum = left[0] + right[0] + node.val;\n    int count = left[1] + right[1]\
        \ + 1;\n\n    if (sum ~/ count == node.val) {\n      _count++;\n    }\n\n  \
        \  return [sum, count];\n  }\n}"
      go: "func averageOfSubtree(root *TreeNode) int {\n    result := 0\n    var dfs\
        \ func(*TreeNode) (int, int)\n    dfs = func(node *TreeNode) (int, int) {\n\
        \        if node == nil {\n            return 0, 0\n        }\n\n        leftSum,\
        \ leftCount := dfs(node.Left)\n        rightSum, rightCount := dfs(node.Right)\n\
        \n        currentSum := leftSum + rightSum + node.Val\n        currentCount\
        \ := leftCount + rightCount + 1\n\n        if currentSum/currentCount == node.Val\
        \ {\n            result++\n        }\n\n        return currentSum, currentCount\n\
        \    }\n\n    dfs(root)\n    return result\n}"
      ruby: "def average_of_subtree(root)\n  @count = 0\n\n  def dfs(node)\n    return\
        \ [0, 0] if node.nil?\n\n    left_sum, left_count = dfs(node.left)\n    right_sum,\
        \ right_count = dfs(node.right)\n\n    total_sum = left_sum + right_sum + node.val\n\
        \    total_count = left_count + right_count + 1\n\n    if (total_sum / total_count)\
        \ == node.val\n      @count += 1\n    end\n\n    [total_sum, total_count]\n\
        \  end\n\n  dfs(root)\n  @count\nend"
      scala: "object Solution {\n    def averageOfSubtree(root: TreeNode): Int = {\n\
        \        var result = 0\n\n        def dfs(node: TreeNode): (Int, Int) = {\n\
        \            if (node == null) {\n                return (0, 0)\n          \
        \  }\n\n            val (leftSum, leftCount) = dfs(node.left)\n            val\
        \ (rightSum, rightCount) = dfs(node.right)\n\n            val currentSum = leftSum\
        \ + rightSum + node.value\n            val currentCount = leftCount + rightCount\
        \ + 1\n\n            if (currentSum / currentCount == node.value) {\n      \
        \          result += 1\n            }\n\n            (currentSum, currentCount)\n\
        \        }\n\n        dfs(root)\n        result\n    }\n}"
      rust: "use std::rc::Rc;\nuse std::cell::RefCell;\n\nimpl Solution {\n    pub fn\
        \ average_of_subtree(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {\n       \
        \ let mut result = 0;\n        fn dfs(node: &Option<Rc<RefCell<TreeNode>>>,\
        \ res: &mut i32) -> (i32, i32) {\n            match node {\n               \
        \ None => (0, 0),\n                Some(n) => {\n                    let n_borrow\
        \ = n.borrow();\n                    let (left_sum, left_count) = dfs(&n_borrow.left,\
        \ res);\n                    let (right_sum, right_count) = dfs(&n_borrow.right,\
        \ res);\n\n                    let current_sum = left_sum + right_sum + n_borrow.val;\n\
        \                    let current_count = left_count + right_count + 1;\n\n \
        \                   if n_borrow.val == current_sum / current_count {\n     \
        \                   *res += 1;\n                    }\n\n                  \
        \  (current_sum, current_count)\n                }\n            }\n        }\n\
        \        dfs(&root, &mut result);\n        result\n    }\n}"
      racket: "(define/contract (average-of-subtree root)\n  (-> (or/c tree-node? #f)\
        \ exact-integer?)\n  (define (dfs node)\n    (if (not node)\n        (values\
        \ 0 0 0)\n        (let-values ([(l-sum l-cnt l-match) (dfs (tree-node-left node))]\n\
        \                     [(r-sum r-cnt r-match) (dfs (tree-node-right node))])\n\
        \          (let* ([total-sum (+ l-sum r-sum (tree-node-val node))]\n       \
        \          [total-count (+ l-cnt r-cnt 1)]\n                 [is-match (if (=\
        \ (tree-node-val node) (quotient total-sum total-count)) 1 0)])\n          \
        \  (values total-sum total-count (+ l-match r-match is-match))))))\n  (let-values\
        \ ([(_s _c match-count) (dfs root)])\n    match-count))"
      erlang: "average_of_subtree(Root) ->\n  {_, _, Count} = dfs(Root),\n  Count.\n\
        \ndfs(null) ->\n  {0, 0, 0};\ndfs(Node) ->\n  {LSum, LCnt, LMatch} = dfs(Node#tree_node.left),\n\
        \  {RSum, RCnt, RMatch} = dfs(Node#tree_node.right),\n  Sum = LSum + RSum +\
        \ Node#tree_node.val,\n  Cnt = LCnt + RCnt + 1,\n  Match = LMatch + RMatch +\
        \ (if Node#tree_node.val =:= (Sum div Cnt) -> 1; true -> 0 end),\n  {Sum, Cnt,\
        \ Match}."
      elixir: "defmodule Solution do\n  @spec average_of_subtree(root :: TreeNode.t\
        \ | nil) :: integer\n  def average_of_subtree(root) do\n    {_sum, _count, matches}\
        \ = dfs(root)\n    matches\n  end\n\n  defp dfs(nil), do: {0, 0, 0}\n  defp\
        \ dfs(node) do\n    {l_sum, l_cnt, l_m} = dfs(node.left)\n    {r_sum, r_cnt,\
        \ r_m} = dfs(node.right)\n\n    current_sum = l_sum + r_sum + node.val\n   \
        \ current_count = l_cnt + r_cnt + 1\n\n    match = if node.val == div(current_sum,\
        \ current_count), do: 1, else: 0\n    {current_sum, current_count, l_m + r_m\
        \ + match}\n  end\nend"
    approach: 'To solve this problem efficiently, we perform a post-order traversal
      of the binary tree. For each node, we need two pieces of information from its
      children to compute the average: the sum of all node values in the subtree and
      the total number of nodes in that subtree. By processing the left and right subtrees
      before the current node, we can calculate the current node''s subtree sum as the
      sum of its own value plus the sums of its children, and its subtree count as 1
      plus the counts of its children.'
    time_complexity: 'O(N) with one-paragraph explanation: The algorithm visits each
      node in the binary tree exactly once during the post-order traversal. At each
      node, it performs a constant amount of work to calculate the sum, count, and average,
      resulting in a linear time complexity relative to the number of nodes $N$.'
    space_complexity: 'O(H) with one-paragraph explanation: The space complexity is
      determined by the maximum depth of the recursion stack, which corresponds to the
      height of the tree $H$. In the worst case of a skewed tree, $H$ is $O(N)$, while
      in a balanced tree, $H$ is $O(\log N)$.'
    elapsed_time: 90.67229652404785
    model: gemini-3-flash-preview
    generated_at: '2026-09-10 02:25:47 '
---

## Problem #2265: Count Nodes Equal to Average of Subtree

**Difficulty:** Medium

**Topics:** Tree, Depth-First Search, Binary Tree

## Problem Description

<p>Given the <code>root</code> of a binary tree, return <em>the number of nodes where the value of the node is equal to the <strong>average</strong> of the values in its <strong>subtree</strong></em>.</p>

<p><strong>Note:</strong></p>

<ul>
	<li>The <strong>average</strong> of <code>n</code> elements is the <strong>sum</strong> of the <code>n</code> elements divided by <code>n</code> and <strong>rounded down</strong> to the nearest integer.</li>
	<li>A <strong>subtree</strong> of <code>root</code> is a tree consisting of <code>root</code> and all of its descendants.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img src="https://assets.leetcode.com/uploads/2022/03/15/image-20220315203925-1.png" style="width: 300px; height: 212px;" />
<pre>
<strong>Input:</strong> root = [4,8,5,0,1,null,6]
<strong>Output:</strong> 5
<strong>Explanation:</strong> 
For the node with value 4: The average of its subtree is (4 + 8 + 5 + 0 + 1 + 6) / 6 = 24 / 6 = 4.
For the node with value 5: The average of its subtree is (5 + 6) / 2 = 11 / 2 = 5.
For the node with value 0: The average of its subtree is 0 / 1 = 0.
For the node with value 1: The average of its subtree is 1 / 1 = 1.
For the node with value 6: The average of its subtree is 6 / 1 = 6.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img src="https://assets.leetcode.com/uploads/2022/03/26/image-20220326133920-1.png" style="width: 80px; height: 76px;" />
<pre>
<strong>Input:</strong> root = [1]
<strong>Output:</strong> 1
<strong>Explanation:</strong> For the node with value 1: The average of its subtree is 1 / 1 = 1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 1000]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 1000</code></li>
</ul>


## Hints

1. What information do we need to calculate the average? We need the sum of the values and the number of values.

2. Create a recursive function that returns the size of a node’s subtree, and the sum of the values of its subtree.

## ✨ AI-Generated Solution (gemini-3-flash-preview)

### Approach

To solve this problem efficiently, we perform a post-order traversal of the binary tree. For each node, we need two pieces of information from its children to compute the average: the sum of all node values in the subtree and the total number of nodes in that subtree. By processing the left and right subtrees before the current node, we can calculate the current node's subtree sum as the sum of its own value plus the sums of its children, and its subtree count as 1 plus the counts of its children.

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
    struct Result {
        int sum;
        int count;
    };

    Result traverse(TreeNode* node, int& totalCount) {
        if (!node) return {0, 0};

        Result left = traverse(node->left, totalCount);
        Result right = traverse(node->right, totalCount);

        int currentSum = node->val + left.sum + right.sum;
        int currentCount = 1 + left.count + right.count;

        if (node->val == currentSum / currentCount) {
            totalCount++;
        }

        return {currentSum, currentCount};
    }

    int averageOfSubtree(TreeNode* root) {
        int result = 0;
        traverse(root, result);
        return result;
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
    private int matchingNodes = 0;

    public int averageOfSubtree(TreeNode root) {
        calculateSubtree(root);
        return matchingNodes;
    }

    private int[] calculateSubtree(TreeNode node) {
        if (node == null) {
            return new int[]{0, 0}; // {sum, count}
        }

        int[] left = calculateSubtree(node.left);
        int[] right = calculateSubtree(node.right);

        int sum = node.val + left[0] + right[0];
        int count = 1 + left[1] + right[1];

        if (node.val == sum / count) {
            matchingNodes++;
        }

        return new int[]{sum, count};
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
    def averageOfSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0

        def dfs(node):
            if not node:
                return 0, 0

            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)

            total_sum = node.val + left_sum + right_sum
            total_count = 1 + left_count + right_count

            if node.val == total_sum // total_count:
                self.res += 1

            return total_sum, total_count

        dfs(root)
        return self.res
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
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.count = 0

        def traverse(node):
            if not node:
                return 0, 0

            l_sum, l_cnt = traverse(node.left)
            r_sum, r_cnt = traverse(node.right)

            curr_sum = node.val + l_sum + r_sum
            curr_cnt = 1 + l_cnt + r_cnt

            if node.val == (curr_sum // curr_cnt):
                self.count += 1

            return curr_sum, curr_cnt

        traverse(root)
        return self.count
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

struct SubtreeInfo {
    int sum;
    int count;
};

struct SubtreeInfo dfs(struct TreeNode* node, int* result) {
    if (!node) {
        struct SubtreeInfo empty = {0, 0};
        return empty;
    }

    struct SubtreeInfo left = dfs(node->left, result);
    struct SubtreeInfo right = dfs(node->right, result);

    int currentSum = node->val + left.sum + right.sum;
    int currentCount = 1 + left.count + right.count;

    if (node->val == currentSum / currentCount) {
        (*result)++;
    }

    struct SubtreeInfo current = {currentSum, currentCount};
    return current;
}

int averageOfSubtree(struct TreeNode* root) {
    int result = 0;
    dfs(root, &result);
    return result;
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
    private int result = 0;

    public int AverageOfSubtree(TreeNode root) {
        result = 0;
        Traverse(root);
        return result;
    }

    private (int sum, int count) Traverse(TreeNode node) {
        if (node == null) {
            return (0, 0);
        }

        var left = Traverse(node.left);
        var right = Traverse(node.right);

        int currentSum = left.sum + right.sum + node.val;
        int currentCount = left.count + right.count + 1;

        if (node.val == (currentSum / currentCount)) {
            result++;
        }

        return (currentSum, currentCount);
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
var averageOfSubtree = function(root) {
    let result = 0;

    const postOrder = (node) => {
        if (!node) {
            return [0, 0];
        }

        const [leftSum, leftCount] = postOrder(node.left);
        const [rightSum, rightCount] = postOrder(node.right);

        const currentSum = leftSum + rightSum + node.val;
        const currentCount = leftCount + rightCount + 1;

        if (node.val === Math.floor(currentSum / currentCount)) {
            result++;
        }

        return [currentSum, currentCount];
    };

    postOrder(root);
    return result;
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

function averageOfSubtree(root: TreeNode | null): number {
    let result = 0;

    const traverse = (node: TreeNode | null): [number, number] => {
        if (!node) {
            return [0, 0];
        }

        const [leftSum, leftCount] = traverse(node.left);
        const [rightSum, rightCount] = traverse(node.right);

        const currentSum = leftSum + rightSum + node.val;
        const currentCount = leftCount + rightCount + 1;

        if (node.val === Math.floor(currentSum / currentCount)) {
            result++;
        }

        return [currentSum, currentCount];
    };

    traverse(root);
    return result;
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

    private $ans = 0;

    /**
     * @param TreeNode $root
     * @return Integer
     */
    function averageOfSubtree($root) {
        $this->ans = 0;
        $this->dfs($root);
        return $this->ans;
    }

    private function dfs($node) {
        if ($node === null) {
            return [0, 0];
        }

        $left = $this->dfs($node->left);
        $right = $this->dfs($node->right);

        $currentSum = $left[0] + $right[0] + $node->val;
        $currentCount = $left[1] + $right[1] + 1;

        if ($node->val === (int)($currentSum / $currentCount)) {
            $this->ans++;
        }

        return [$currentSum, $currentCount];
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
    private var count = 0

    func averageOfSubtree(_ root: TreeNode?) -> Int {
        count = 0
        _ = calculate(root)
        return count
    }

    private func calculate(_ node: TreeNode?) -> (Int, Int) {
        guard let node = node else {
            return (0, 0)
        }

        let left = calculate(node.left)
        let right = calculate(node.right)

        let currentSum = left.0 + right.0 + node.val
        let currentCount = left.1 + right.1 + 1

        if node.val == (currentSum / currentCount) {
            count += 1
        }

        return (currentSum, currentCount)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    private var count = 0

    fun averageOfSubtree(root: TreeNode?): Int {
        count = 0
        calculateSubtree(root)
        return count
    }

    private fun calculateSubtree(node: TreeNode?): Pair<Int, Int> {
        if (node == null) {
            return Pair(0, 0)
        }

        val left = calculateSubtree(node.left)
        val right = calculateSubtree(node.right)

        val totalSum = left.first + right.first + node.`val`
        val totalCount = left.second + right.second + 1

        if (totalSum / totalCount == node.`val`) {
            count++
        }

        return Pair(totalSum, totalCount)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  int _count = 0;

  int averageOfSubtree(TreeNode? root) {
    _count = 0;
    _dfs(root);
    return _count;
  }

  List<int> _dfs(TreeNode? node) {
    if (node == null) {
      return [0, 0];
    }

    List<int> left = _dfs(node.left);
    List<int> right = _dfs(node.right);

    int sum = left[0] + right[0] + node.val;
    int count = left[1] + right[1] + 1;

    if (sum ~/ count == node.val) {
      _count++;
    }

    return [sum, count];
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func averageOfSubtree(root *TreeNode) int {
    result := 0
    var dfs func(*TreeNode) (int, int)
    dfs = func(node *TreeNode) (int, int) {
        if node == nil {
            return 0, 0
        }

        leftSum, leftCount := dfs(node.Left)
        rightSum, rightCount := dfs(node.Right)

        currentSum := leftSum + rightSum + node.Val
        currentCount := leftCount + rightCount + 1

        if currentSum/currentCount == node.Val {
            result++
        }

        return currentSum, currentCount
    }

    dfs(root)
    return result
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def average_of_subtree(root)
  @count = 0

  def dfs(node)
    return [0, 0] if node.nil?

    left_sum, left_count = dfs(node.left)
    right_sum, right_count = dfs(node.right)

    total_sum = left_sum + right_sum + node.val
    total_count = left_count + right_count + 1

    if (total_sum / total_count) == node.val
      @count += 1
    end

    [total_sum, total_count]
  end

  dfs(root)
  @count
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def averageOfSubtree(root: TreeNode): Int = {
        var result = 0

        def dfs(node: TreeNode): (Int, Int) = {
            if (node == null) {
                return (0, 0)
            }

            val (leftSum, leftCount) = dfs(node.left)
            val (rightSum, rightCount) = dfs(node.right)

            val currentSum = leftSum + rightSum + node.value
            val currentCount = leftCount + rightCount + 1

            if (currentSum / currentCount == node.value) {
                result += 1
            }

            (currentSum, currentCount)
        }

        dfs(root)
        result
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
    pub fn average_of_subtree(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut result = 0;
        fn dfs(node: &Option<Rc<RefCell<TreeNode>>>, res: &mut i32) -> (i32, i32) {
            match node {
                None => (0, 0),
                Some(n) => {
                    let n_borrow = n.borrow();
                    let (left_sum, left_count) = dfs(&n_borrow.left, res);
                    let (right_sum, right_count) = dfs(&n_borrow.right, res);

                    let current_sum = left_sum + right_sum + n_borrow.val;
                    let current_count = left_count + right_count + 1;

                    if n_borrow.val == current_sum / current_count {
                        *res += 1;
                    }

                    (current_sum, current_count)
                }
            }
        }
        dfs(&root, &mut result);
        result
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define/contract (average-of-subtree root)
  (-> (or/c tree-node? #f) exact-integer?)
  (define (dfs node)
    (if (not node)
        (values 0 0 0)
        (let-values ([(l-sum l-cnt l-match) (dfs (tree-node-left node))]
                     [(r-sum r-cnt r-match) (dfs (tree-node-right node))])
          (let* ([total-sum (+ l-sum r-sum (tree-node-val node))]
                 [total-count (+ l-cnt r-cnt 1)]
                 [is-match (if (= (tree-node-val node) (quotient total-sum total-count)) 1 0)])
            (values total-sum total-count (+ l-match r-match is-match))))))
  (let-values ([(_s _c match-count) (dfs root)])
    match-count))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
average_of_subtree(Root) ->
  {_, _, Count} = dfs(Root),
  Count.

dfs(null) ->
  {0, 0, 0};
dfs(Node) ->
  {LSum, LCnt, LMatch} = dfs(Node#tree_node.left),
  {RSum, RCnt, RMatch} = dfs(Node#tree_node.right),
  Sum = LSum + RSum + Node#tree_node.val,
  Cnt = LCnt + RCnt + 1,
  Match = LMatch + RMatch + (if Node#tree_node.val =:= (Sum div Cnt) -> 1; true -> 0 end),
  {Sum, Cnt, Match}.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec average_of_subtree(root :: TreeNode.t | nil) :: integer
  def average_of_subtree(root) do
    {_sum, _count, matches} = dfs(root)
    matches
  end

  defp dfs(nil), do: {0, 0, 0}
  defp dfs(node) do
    {l_sum, l_cnt, l_m} = dfs(node.left)
    {r_sum, r_cnt, r_m} = dfs(node.right)

    current_sum = l_sum + r_sum + node.val
    current_count = l_cnt + r_cnt + 1

    match = if node.val == div(current_sum, current_count), do: 1, else: 0
    {current_sum, current_count, l_m + r_m + match}
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(N) with one-paragraph explanation: The algorithm visits each node in the binary tree exactly once during the post-order traversal. At each node, it performs a constant amount of work to calculate the sum, count, and average, resulting in a linear time complexity relative to the number of nodes $N$.
- **Space Complexity:** O(H) with one-paragraph explanation: The space complexity is determined by the maximum depth of the recursion stack, which corresponds to the height of the tree $H$. In the worst case of a skewed tree, $H$ is $O(N)$, while in a balanced tree, $H$ is $O(\log N)$.
