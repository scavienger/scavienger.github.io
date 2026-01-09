---
layout: post
title: "Smallest Subtree with all the Deepest Nodes"
date: 2026-01-09 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Hash Table", "Tree", "Depth-First Search", "Breadth-First Search", "Binary Tree"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/
ai_solutions:
  - solutions:
      cpp: "/**\n * Definition for a binary tree node.\n * struct TreeNode {\n *   \
        \  int val;\n *     TreeNode *left;\n *     TreeNode *right;\n *     TreeNode()\
        \ : val(0), left(nullptr), right(nullptr) {}\n *     TreeNode(int x) : val(x),\
        \ left(nullptr), right(nullptr) {}\n *     TreeNode(int x, TreeNode *left, TreeNode\
        \ *right) : val(x), left(left), right(right) {}\n * };\n */\nclass Solution\
        \ {\npublic:\n    // Returns a pair: {height, LCA_node}\n    // height is the\
        \ maximum depth from the current node to a leaf in its subtree.\n    // A null\
        \ node has height -1, a leaf node has height 0.\n    std::pair<int, TreeNode*>\
        \ dfs(TreeNode* node) {\n        if (!node) {\n            return {-1, nullptr};\n\
        \        }\n\n        std::pair<int, TreeNode*> left_res = dfs(node->left);\n\
        \        std::pair<int, TreeNode*> right_res = dfs(node->right);\n\n       \
        \ int left_height = left_res.first;\n        TreeNode* left_lca = left_res.second;\n\
        \n        int right_height = right_res.first;\n        TreeNode* right_lca =\
        \ right_res.second;\n\n        if (left_height == right_height) {\n        \
        \    // If both subtrees have the same maximum height, this node is the LCA\n\
        \            // of all deepest nodes within its subtree.\n            return\
        \ {left_height + 1, node};\n        } else if (left_height > right_height) {\n\
        \            // Deepest nodes are exclusively in the left subtree.\n       \
        \     return {left_height + 1, left_lca};\n        } else {\n            //\
        \ Deepest nodes are exclusively in the right subtree.\n            return {right_height\
        \ + 1, right_lca};\n        }\n    }\n\n    TreeNode* subtreeWithAllDeepest(TreeNode*\
        \ root) {\n        return dfs(root).second;\n    }\n};"
      java: "/**\n * Definition for a binary tree node.\n * public class TreeNode {\n\
        \ *     int val;\n *     TreeNode left;\n *     TreeNode right;\n *     TreeNode()\
        \ {}S\n *     TreeNode(int val) { this.val = val; }\n *     TreeNode(int val,\
        \ TreeNode left, TreeNode right) {\n *         this.val = val;\n *         this.left\
        \ = left;\n *         this.right = right;\n *     }\n * }\n */\nclass Solution\
        \ {\n    // Helper class to return both height and the LCA node\n    // height\
        \ is the maximum depth from the current node to a leaf in its subtree.\n   \
        \ // A null node has height -1, a leaf node has height 0.\n    class Result\
        \ {\n        int height;\n        TreeNode node;\n\n        Result(int height,\
        \ TreeNode node) {\n            this.height = height;\n            this.node\
        \ = node;\n        }\n    }\n\n    public TreeNode subtreeWithAllDeepest(TreeNode\
        \ root) {\n        return dfs(root).node;\n    }\n\n    private Result dfs(TreeNode\
        \ node) {\n        if (node == null) {\n            return new Result(-1, null);\n\
        \        }\n\n        Result leftRes = dfs(node.left);\n        Result rightRes\
        \ = dfs(node.right);\n\n        if (leftRes.height == rightRes.height) {\n \
        \           // If both subtrees have the same maximum height, this node is the\
        \ LCA\n            // of all deepest nodes within its subtree.\n           \
        \ return new Result(leftRes.height + 1, node);\n        } else if (leftRes.height\
        \ > rightRes.height) {\n            // Deepest nodes are exclusively in the\
        \ left subtree.\n            return new Result(leftRes.height + 1, leftRes.node);\n\
        \        } else {\n            // Deepest nodes are exclusively in the right\
        \ subtree.\n            return new Result(rightRes.height + 1, rightRes.node);\n\
        \        }\n    }\n}"
      python: "# Definition for a binary tree node.\n# class TreeNode(object):\n#  \
        \   def __init__(self, val=0, left=None, right=None):\n#         self.val =\
        \ val\n#         self.left = left\n#         self.right = right\nclass Solution(object):\n\
        \    def subtreeWithAllDeepest(self, root):\n        \"\"\"\n        :type root:\
        \ Optional[TreeNode]\n        :rtype: Optional[TreeNode]\n        \"\"\"\n \
        \       # Helper function returns a tuple: (height, lca_node)\n        # height\
        \ is the maximum depth from the current node to a leaf in its subtree.\n   \
        \     # A null node has height -1, a leaf node has height 0.\n        def dfs(node):\n\
        \            if not node:\n                return -1, None\n\n            left_height,\
        \ left_lca = dfs(node.left)\n            right_height, right_lca = dfs(node.right)\n\
        \n            if left_height == right_height:\n                # If both subtrees\
        \ have the same maximum height, this node is the LCA\n                # of all\
        \ deepest nodes within its subtree.\n                return left_height + 1,\
        \ node\n            elif left_height > right_height:\n                # Deepest\
        \ nodes are exclusively in the left subtree.\n                return left_height\
        \ + 1, left_lca\n            else: # right_height > left_height\n          \
        \      # Deepest nodes are exclusively in the right subtree.\n             \
        \   return right_height + 1, right_lca\n\n        _, result_node = dfs(root)\n\
        \        return result_node"
      python3: "# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self,\
        \ val=0, left=None, right=None):\n#         self.val = val\n#         self.left\
        \ = left\n#         self.right = right\nclass Solution:\n    def subtreeWithAllDeepest(self,\
        \ root: Optional[TreeNode]) -> Optional[TreeNode]:\n        # Helper function\
        \ returns a tuple: (height, lca_node)\n        # height is the maximum depth\
        \ from the current node to a leaf in its subtree.\n        # A null node has\
        \ height -1, a leaf node has height 0.\n        def dfs(node: Optional[TreeNode])\
        \ -> tuple[int, Optional[TreeNode]]:\n            if not node:\n           \
        \     return -1, None\n\n            left_height, left_lca = dfs(node.left)\n\
        \            right_height, right_lca = dfs(node.right)\n\n            if left_height\
        \ == right_height:\n                # If both subtrees have the same maximum\
        \ height, this node is the LCA\n                # of all deepest nodes within\
        \ its subtree.\n                return left_height + 1, node\n            elif\
        \ left_height > right_height:\n                # Deepest nodes are exclusively\
        \ in the left subtree.\n                return left_height + 1, left_lca\n \
        \           else: # right_height > left_height\n                # Deepest nodes\
        \ are exclusively in the right subtree.\n                return right_height\
        \ + 1, right_lca\n\n        _, result_node = dfs(root)\n        return result_node"
      c: "/**\n * Definition for a binary tree node.\n * struct TreeNode {\n *     int\
        \ val;\n *     struct TreeNode *left;\n *     struct TreeNode *right;\n * };\n\
        \ */\n\n// Custom struct to return both height and the node pointer\n// height\
        \ is the maximum depth from the current node to a leaf in its subtree.\n// A\
        \ null node has height -1, a leaf node has height 0.\ntypedef struct {\n   \
        \ int height;\n    struct TreeNode* node;\n} Result;\n\nResult dfs(struct TreeNode*\
        \ node) {\n    if (node == NULL) {\n        Result res = {-1, NULL};\n     \
        \   return res;\n    }\n\n    Result left_res = dfs(node->left);\n    Result\
        \ right_res = dfs(node->right);\n\n    int left_height = left_res.height;\n\
        \    struct TreeNode* left_lca = left_res.node;\n\n    int right_height = right_res.height;\n\
        \    struct TreeNode* right_lca = right_res.node;\n\n    if (left_height ==\
        \ right_height) {\n        // If both subtrees have the same maximum height,\
        \ this node is the LCA\n        // of all deepest nodes within its subtree.\n\
        \        Result res = {left_height + 1, node};\n        return res;\n    } else\
        \ if (left_height > right_height) {\n        // Deepest nodes are exclusively\
        \ in the left subtree.\n        Result res = {left_height + 1, left_lca};\n\
        \        return res;\n    } else {\n        // Deepest nodes are exclusively\
        \ in the right subtree.\n        Result res = {right_height + 1, right_lca};\n\
        \        return res;\n    }\n}\n\nstruct TreeNode* subtreeWithAllDeepest(struct\
        \ TreeNode* root) {\n    return dfs(root).node;\n}"
      csharp: "/**\n * Definition for a binary tree node.\n * public class TreeNode\
        \ {\n *     public int val;\n *     public TreeNode left;\n *     public TreeNode\
        \ right;\n *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null)\
        \ {\n *         this.val = val;\n *         this.left = left;\n *         this.right\
        \ = right;\n *     }\n * }\n */\npublic class Solution {\n    private class\
        \ Result {\n        public int Depth;\n        public TreeNode Node;\n\n   \
        \     public Result(int depth, TreeNode node) {\n            Depth = depth;\n\
        \            Node = node;\n        }\n    }\n\n    public TreeNode SubtreeWithAllDeepest(TreeNode\
        \ root) {\n        return DFS(root).Node;\n    }\n\n    private Result DFS(TreeNode\
        \ node) {\n        if (node == null) {\n            return new Result(0, null);\n\
        \        }\n\n        Result leftResult = DFS(node.left);\n        Result rightResult\
        \ = DFS(node.right);\n\n        if (leftResult.Depth == rightResult.Depth) {\n\
        \            return new Result(leftResult.Depth + 1, node);\n        } else\
        \ if (leftResult.Depth > rightResult.Depth) {\n            return new Result(leftResult.Depth\
        \ + 1, leftResult.Node);\n        } else {\n            return new Result(rightResult.Depth\
        \ + 1, rightResult.Node);\n        }\n    }\n}"
      javascript: "/**\n * Definition for a binary tree node.\n * function TreeNode(val,\
        \ left, right) {\n *     this.val = (val===undefined ? 0 : val)\n *     this.left\
        \ = (left===undefined ? null : left)\n *     this.right = (right===undefined\
        \ ? null : right)\n * }\n */\n/**\n * @param {TreeNode} root\n * @return {TreeNode}\n\
        \ */\nvar subtreeWithAllDeepest = function(root) {\n    function dfs(node) {\n\
        \        if (node === null) {\n            return [0, null];\n        }\n\n\
        \        let [leftDepth, leftNode] = dfs(node.left);\n        let [rightDepth,\
        \ rightNode] = dfs(node.right);\n\n        if (leftDepth === rightDepth) {\n\
        \            return [leftDepth + 1, node];\n        } else if (leftDepth > rightDepth)\
        \ {\n            return [leftDepth + 1, leftNode];\n        } else {\n     \
        \       return [rightDepth + 1, rightNode];\n        }\n    }\n\n    return\
        \ dfs(root)[1];\n};"
      typescript: "/**\n * Definition for a binary tree node.\n * class TreeNode {\n\
        \ *     val: number\n *     left: TreeNode | null\n *     right: TreeNode |\
        \ null\n *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode\
        \ | null) {\n *         this.val = (val===undefined ? 0 : val)\n *         this.left\
        \ = (left===undefined ? null : left)\n *         this.right = (right===undefined\
        \ ? null : right)\n *     }\n * }\n */\n\nfunction subtreeWithAllDeepest(root:\
        \ TreeNode | null): TreeNode | null {\n    function dfs(node: TreeNode | null):\
        \ [number, TreeNode | null] {\n        if (node === null) {\n            return\
        \ [0, null];\n        }\n\n        const [leftDepth, leftNode] = dfs(node.left);\n\
        \        const [rightDepth, rightNode] = dfs(node.right);\n\n        if (leftDepth\
        \ === rightDepth) {\n            return [leftDepth + 1, node];\n        } else\
        \ if (leftDepth > rightDepth) {\n            return [leftDepth + 1, leftNode];\n\
        \        } else {\n            return [rightDepth + 1, rightNode];\n       \
        \ }\n    }\n\n    return dfs(root)[1];\n};"
      php: "/**\n * Definition for a binary tree node.\n * class TreeNode {\n *    \
        \ public $val = null;\n *     public $left = null;\n *     public $right = null;\n\
        \ *     function __construct($val = 0, $left = null, $right = null) {\n *  \
        \       $this->val = $val;\n *         $this->left = $left;\n *         $this->right\
        \ = $right;\n *     }\n * }\n */\nclass Solution {\n\n    /**\n     * @param\
        \ TreeNode $root\n     * @return TreeNode\n     */\n    function subtreeWithAllDeepest($root)\
        \ {\n        return $this->dfsHelper($root)[1];\n    }\n\n    /**\n     * Helper\
        \ method for DFS traversal\n     * @param TreeNode $node\n     * @return array\
        \ [depth, node]\n     */\n    private function dfsHelper(?TreeNode $node): array\
        \ {\n        if ($node === null) {\n            return [0, null];\n        }\n\
        \n        list($leftDepth, $leftNode) = $this->dfsHelper($node->left);\n   \
        \     list($rightDepth, $rightNode) = $this->dfsHelper($node->right);\n\n  \
        \      if ($leftDepth === $rightDepth) {\n            return [$leftDepth + 1,\
        \ $node];\n        } elseif ($leftDepth > $rightDepth) {\n            return\
        \ [$leftDepth + 1, $leftNode];\n        } else {\n            return [$rightDepth\
        \ + 1, $rightNode];\n        }\n    }\n}"
      swift: "/**\n * Definition for a binary tree node.\n * public class TreeNode {\n\
        \ *     public var val: Int\n *     public var left: TreeNode?\n *     public\
        \ var right: TreeNode?\n *     public init() { self.val = 0; self.left = nil;\
        \ self.right = nil; }\n *     public init(_ val: Int) { self.val = val; self.left\
        \ = nil; self.right = nil; }\n *     public init(_ val: Int, _ left: TreeNode?,\
        \ _ right: TreeNode?) {\n *         self.val = val\n *         self.left = left\n\
        \ *         this.right = right\n *     }\n * }\n */\nclass Solution {\n    func\
        \ subtreeWithAllDeepest(_ root: TreeNode?) -> TreeNode? {\n        func dfs(_\
        \ node: TreeNode?) -> (depth: Int, node: TreeNode?) {\n            guard let\
        \ node = node else {\n                return (0, nil)\n            }\n\n   \
        \         let leftResult = dfs(node.left)\n            let rightResult = dfs(node.right)\n\
        \n            if leftResult.depth == rightResult.depth {\n                return\
        \ (leftResult.depth + 1, node)\n            } else if leftResult.depth > rightResult.depth\
        \ {\n                return (leftResult.depth + 1, leftResult.node)\n      \
        \      } else {\n                return (rightResult.depth + 1, rightResult.node)\n\
        \            }\n        }\n\n        return dfs(root).node\n    }\n}"
      kotlin: "/**\n * Example:\n * var ti = TreeNode(5)\n * var v = ti.`val`\n * Definition\
        \ for a binary tree node.\n * class TreeNode(var `val`: Int) {\n *     var left:\
        \ TreeNode? = null\n *     var right: TreeNode? = null\n * }\n */\nclass Solution\
        \ {\n    fun subtreeWithAllDeepest(root: TreeNode?): TreeNode? {\n        fun\
        \ dfs(node: TreeNode?): Pair<Int, TreeNode?> {\n            if (node == null)\
        \ {\n                return Pair(0, null)\n            }\n\n            val\
        \ (leftDepth, leftSubtreeRoot) = dfs(node.left)\n            val (rightDepth,\
        \ rightSubtreeRoot) = dfs(node.right)\n\n            return when {\n       \
        \         leftDepth > rightDepth -> Pair(leftDepth + 1, leftSubtreeRoot)\n \
        \               rightDepth > leftDepth -> Pair(rightDepth + 1, rightSubtreeRoot)\n\
        \                else -> Pair(leftDepth + 1, node)\n            }\n        }\n\
        \n        return dfs(root).second\n    }\n}"
      dart: "/**\n * Definition for a binary tree node.\n * class TreeNode {\n *   int\
        \ val;\n *   TreeNode? left;\n *   TreeNode? right;\n *   TreeNode([this.val\
        \ = 0, this.left, this.right]);\n * }\n */\n\nclass _Result {\n  int depth;\n\
        \  TreeNode? node;\n  _Result(this.depth, this.node);\n}\n\nclass Solution {\n\
        \  TreeNode? subtreeWithAllDeepest(TreeNode? root) {\n    _Result dfs(TreeNode?\
        \ node) {\n      if (node == null) {\n        return _Result(0, null);\n   \
        \   }\n\n      _Result leftResult = dfs(node.left);\n      _Result rightResult\
        \ = dfs(node.right);\n\n      if (leftResult.depth > rightResult.depth) {\n\
        \        return _Result(leftResult.depth + 1, leftResult.node);\n      } else\
        \ if (rightResult.depth > leftResult.depth) {\n        return _Result(rightResult.depth\
        \ + 1, rightResult.node);\n      } else {\n        return _Result(leftResult.depth\
        \ + 1, node);\n      }\n    }\n\n    return dfs(root).node;\n  }\n}"
      go: "/**\n * Definition for a binary tree node.\n * type TreeNode struct {\n *\
        \     Val int\n *     Left *TreeNode\n *     Right *TreeNode\n * }\n */\nfunc\
        \ subtreeWithAllDeepest(root *TreeNode) *TreeNode {\n    var dfs func(*TreeNode)\
        \ (int, *TreeNode)\n    dfs = func(node *TreeNode) (int, *TreeNode) {\n    \
        \    if node == nil {\n            return 0, nil\n        }\n\n        leftDepth,\
        \ leftSubtreeRoot := dfs(node.Left)\n        rightDepth, rightSubtreeRoot :=\
        \ dfs(node.Right)\n\n        if leftDepth > rightDepth {\n            return\
        \ leftDepth + 1, leftSubtreeRoot\n        } else if rightDepth > leftDepth {\n\
        \            return rightDepth + 1, rightSubtreeRoot\n        } else {\n   \
        \         return leftDepth + 1, node\n        }\n    }\n\n    _, resultNode\
        \ := dfs(root)\n    return resultNode\n}"
      ruby: "# Definition for a binary tree node.\n# class TreeNode\n#     attr_accessor\
        \ :val, :left, :right\n#     def initialize(val = 0, left = nil, right = nil)\n\
        #         @val = val\n#         @left = left\n#         @right = right\n#  \
        \   end\n# end\n# @param {TreeNode} root\n# @return {TreeNode}\ndef subtree_with_all_deepest(root)\n\
        \    def dfs(node)\n        return [0, nil] if node.nil?\n\n        left_depth,\
        \ left_subtree_root = dfs(node.left)\n        right_depth, right_subtree_root\
        \ = dfs(node.right)\n\n        if left_depth > right_depth\n            [left_depth\
        \ + 1, left_subtree_root]\n        elsif right_depth > left_depth\n        \
        \    [right_depth + 1, right_subtree_root]\n        else\n            [left_depth\
        \ + 1, node]\n        end\n    end\n\n    dfs(root).last\nend"
      scala: "/**\n * Definition for a binary tree node.\n * class TreeNode(_value:\
        \ Int = 0, _left: TreeNode = null, _right: TreeNode = null) {\n *   var value:\
        \ Int = _value\n *   var left: TreeNode = _left\n *   var right: TreeNode =\
        \ _right\n * }\n */\nobject Solution {\n    def subtreeWithAllDeepest(root:\
        \ TreeNode): TreeNode = {\n        def dfs(node: TreeNode): (Int, TreeNode)\
        \ = {\n            if (node == null) {\n                return (0, null)\n \
        \           }\n\n            val (leftDepth, leftSubtreeRoot) = dfs(node.left)\n\
        \            val (rightDepth, rightSubtreeRoot) = dfs(node.right)\n\n      \
        \      if (leftDepth > rightDepth) {\n                (leftDepth + 1, leftSubtreeRoot)\n\
        \            } else if (rightDepth > leftDepth) {\n                (rightDepth\
        \ + 1, rightSubtreeRoot)\n            } else {\n                (leftDepth +\
        \ 1, node)\n            }\n        }\n\n        dfs(root)._2\n    }\n}"
      rust: "// Definition for a binary tree node.\n// #[derive(Debug, PartialEq, Eq)]\n\
        // pub struct TreeNode {\n//   pub val: i32,\n//   pub left: Option<Rc<RefCell<TreeNode>>>,\n\
        //   pub right: Option<Rc<RefCell<TreeNode>>>,\n// }\n// \n// impl TreeNode\
        \ {\n//   #[inline]\n//   pub fn new(val: i32) -> Self {\n//     TreeNode {\n\
        //       val,\n//       left: None,\n//       right: None\n//     }\n//   }\n\
        // }\nuse std::rc::Rc;\nuse std::cell::RefCell;\nimpl Solution {\n    pub fn\
        \ subtree_with_all_deepest(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>>\
        \ {\n        // Helper function returns (height, lca_node)\n        // height\
        \ is the distance from current node to the deepest leaf in its subtree\n   \
        \     fn dfs(node_opt: Option<Rc<RefCell<TreeNode>>>) -> (i32, Option<Rc<RefCell<TreeNode>>>)\
        \ {\n            match node_opt {\n                None => (0, None),\n    \
        \            Some(node_rc) => {\n                    let node = node_rc.borrow();\n\
        \                    let (left_height, left_lca) = dfs(node.left.clone());\n\
        \                    let (right_height, right_lca) = dfs(node.right.clone());\n\
        \n                    if left_height == right_height {\n                   \
        \     // If both subtrees have the same max height, this node is the LCA\n \
        \                       (left_height + 1, Some(Rc::clone(&node_rc)))\n     \
        \               } else if left_height > right_height {\n                   \
        \     // Deepest nodes are in the left subtree\n                        (left_height\
        \ + 1, left_lca)\n                    } else {\n                        // Deepest\
        \ nodes are in the right subtree\n                        (right_height + 1,\
        \ right_lca)\n                    }\n                }\n            }\n    \
        \    }\n\n        let (_, result_node) = dfs(root);\n        result_node\n \
        \   }\n}"
      racket: "; Definition for a binary tree node.\n#|\n\n; val : integer?\n; left\
        \ : (or/c tree-node? #f)\n; right : (or/c tree-node? #f)\n(struct tree-node\n\
        \  (val left right) #:mutable #:transparent)\n\n; constructor\n(define (make-tree-node\
        \ [val 0])\n  (tree-node val #f #f))\n\n|#\n\n(define/contract (subtree-with-all-deepest\
        \ root)\n  (-> (or/c tree-node? #f) (or/c tree-node? #f))\n  (define (dfs node)\n\
        \    ; Returns a pair: (cons height lca-node)\n    ; height is the distance\
        \ from current node to the deepest leaf in its subtree\n    (if (not node)\n\
        \        (cons 0 #f) ; Base case: null node has height 0, no LCA node\n    \
        \    (let* ((left-res (dfs (tree-node-left node)))\n               (right-res\
        \ (dfs (tree-node-right node)))\n               (left-height (car left-res))\n\
        \               (left-lca (cdr left-res))\n               (right-height (car\
        \ right-res))\n               (right-lca (cdr right-res)))\n          (cond\n\
        \            ((= left-height right-height)\n             ; If both subtrees\
        \ have the same max height, this node is the LCA\n             (cons (+ left-height\
        \ 1) node))\n            ((> left-height right-height)\n             ; Deepest\
        \ nodes are in the left subtree\n             (cons (+ left-height 1) left-lca))\n\
        \            (else ; (< right-height left-height)\n             ; Deepest nodes\
        \ are in the right subtree\n             (cons (+ right-height 1) right-lca))))))\n\
        \n  (cdr (dfs root)) ; We only need the LCA node from the result of dfs(root)\n\
        )"
      erlang: "%% Definition for a binary tree node.\n%%\n%% -record(tree_node, {val\
        \ = 0 :: integer(),\n%%                     left = null  :: 'null' | #tree_node{},\n\
        %%                     right = null :: 'null' | #tree_node{}}).\n\n-spec subtree_with_all_deepest(Root\
        \ :: #tree_node{} | null) -> #tree_node{} | null.\nsubtree_with_all_deepest(Root)\
        \ ->\n  % Helper function returns {Height, LCA_Node}\n  % Height is the distance\
        \ from current node to the deepest leaf in its subtree\n  {_Height, LCA_Node}\
        \ = dfs(Root),\n  LCA_Node.\n\ndfs(null) -> {0, null};\ndfs(Node) ->\n  Left\
        \ = Node#tree_node.left,\n  Right = Node#tree_node.right,\n\n  {LeftHeight,\
        \ LeftLCA} = dfs(Left),\n  {RightHeight, RightLCA} = dfs(Right),\n\n  if\n \
        \   LeftHeight == RightHeight ->\n      % If both subtrees have the same max\
        \ height, this node is the LCA\n      {LeftHeight + 1, Node};\n    LeftHeight\
        \ > RightHeight ->\n      % Deepest nodes are in the left subtree\n      {LeftHeight\
        \ + 1, LeftLCA};\n    true -> % RightHeight > LeftHeight\n      % Deepest nodes\
        \ are in the right subtree\n      {RightHeight + 1, RightLCA}\n  end."
      elixir: "# Definition for a binary tree node.\n#\n# defmodule TreeNode do\n# \
        \  @type t :: %__MODULE__{n#           val: integer,\n#           left: TreeNode.t()\
        \ | nil,\n#           right: TreeNode.t() | nil\n#         }\n#   defstruct\
        \ val: 0, left: nil, right: nil\n# end\n\ndefmodule Solution do\n  @spec subtree_with_all_deepest(root\
        \ :: TreeNode.t | nil) :: TreeNode.t | nil\n  def subtree_with_all_deepest(root)\
        \ do\n    # Helper function returns {height, lca_node}\n    # height is the\
        \ distance from current node to the deepest leaf in its subtree\n    dfs(root)\n\
        \    |> elem(1) # We only need the LCA node from the result of dfs(root)\n \
        \ end\n\n  defp dfs(nil), do: {0, nil} # Base case: nil node has height 0, no\
        \ LCA node\n  defp dfs(%TreeNode{} = node) do\n    {left_height, left_lca} =\
        \ dfs(node.left)\n    {right_height, right_lca} = dfs(node.right)\n\n    cond\
        \ do\n      left_height == right_height ->\n        # If both subtrees have\
        \ the same max height, this node is the LCA\n        {left_height + 1, node}\n\
        \      left_height > right_height ->\n        # Deepest nodes are in the left\
        \ subtree\n        {left_height + 1, left_lca}\n      true -> # right_height\
        \ > left_height\n        # Deepest nodes are in the right subtree\n        {right_height\
        \ + 1, right_lca}\n    end\n  end\nend"
    approach: 'The problem asks for the smallest subtree containing all deepest nodes,
      which is equivalent to finding the Lowest Common Ancestor (LCA) of all deepest
      leaves. We can solve this using a single recursive depth-first traversal (post-order
      traversal) that computes two pieces of information for each node: its height (distance
      to the deepest leaf in its subtree) and the LCA of all deepest leaves within its
      subtree. The height of a null node is 0, and the height of a leaf node is 1.


      For any given node, we recursively call the helper function on its left and right
      children to get their respective heights and LCAs. If the left subtree''s height
      is greater than the right subtree''s height, the LCA of deepest nodes for the
      current node''s subtree must be the LCA from the left subtree. Similarly, if the
      right subtree''s height is greater, we take the LCA from the right subtree. If
      both subtrees have the same maximum height, it means the deepest nodes are equally
      distributed or found in both subtrees, making the current node itself the LCA
      of all deepest nodes within its subtree. The height for the current node is then
      1 plus the maximum of its children''s heights. The final result is the LCA node
      returned by the initial call to the helper function on the root.'
    time_complexity: The time complexity is O(N), where N is the number of nodes in
      the binary tree. This is because the algorithm performs a single depth-first traversal,
      visiting each node exactly once. For each node, a constant amount of work (recursive
      calls, comparisons, and arithmetic operations) is performed.
    space_complexity: The space complexity is O(H), where H is the height of the binary
      tree. This space is used by the recursion stack during the depth-first traversal.
      In the worst-case scenario (a skewed tree), H can be equal to N, leading to O(N)
      space complexity. In the best-case scenario (a balanced tree), H is O(log N),
      resulting in O(log N) space complexity.
    elapsed_time: 110.82443118095398
    model: gemini-2.5-flash
    generated_at: '2026-01-09 01:12:03 '
  - solutions:
      cpp: "class Solution {\npublic:\n    TreeNode* subtreeWithAllDeepest(TreeNode*\
        \ root) {\n        int maxDepth = 0;\n        TreeNode* result = nullptr;\n\
        \        dfs(root, 0, maxDepth, result);\n        return result;\n    }\n  \
        \  int dfs(TreeNode* node, int depth, int& maxDepth, TreeNode*& result) {\n\
        \        if (!node) return depth;\n        int leftDepth = dfs(node->left, depth\
        \ + 1, maxDepth, result);\n        int rightDepth = dfs(node->right, depth +\
        \ 1, maxDepth, result);\n        if (leftDepth == rightDepth && leftDepth >\
        \ maxDepth) {\n            maxDepth = leftDepth;\n            result = node;\n\
        \        }\n        return max(leftDepth, rightDepth);\n    }\n};"
      java: "class Solution {\n    public TreeNode subtreeWithAllDeepest(TreeNode root)\
        \ {\n        int[] maxDepth = new int[] {0};\n        TreeNode[] result = new\
        \ TreeNode[] {null};\n        dfs(root, 0, maxDepth, result);\n        return\
        \ result[0];\n    }\n    int dfs(TreeNode node, int depth, int[] maxDepth, TreeNode[]\
        \ result) {\n        if (node == null) return depth;\n        int leftDepth\
        \ = dfs(node.left, depth + 1, maxDepth, result);\n        int rightDepth = dfs(node.right,\
        \ depth + 1, maxDepth, result);\n        if (leftDepth == rightDepth && leftDepth\
        \ > maxDepth[0]) {\n            maxDepth[0] = leftDepth;\n            result[0]\
        \ = node;\n        }\n        return Math.max(leftDepth, rightDepth);\n    }\n\
        }"
      python: "class Solution(object):\n    def subtreeWithAllDeepest(self, root):\n\
        \        self.maxDepth = 0\n        self.result = None\n        self.dfs(root,\
        \ 0)\n        return self.result\n    def dfs(self, node, depth):\n        if\
        \ not node:\n            return depth\n        leftDepth = self.dfs(node.left,\
        \ depth + 1)\n        rightDepth = self.dfs(node.right, depth + 1)\n       \
        \ if leftDepth == rightDepth and leftDepth > self.maxDepth:\n            self.maxDepth\
        \ = leftDepth\n            self.result = node\n        return max(leftDepth,\
        \ rightDepth)"
      python3: "class Solution:\n    def subtreeWithAllDeepest(self, root: Optional[TreeNode])\
        \ -> Optional[TreeNode]:\n        self.maxDepth = 0\n        self.result = None\n\
        \        self.dfs(root, 0)\n        return self.result\n    def dfs(self, node,\
        \ depth):\n        if not node:\n            return depth\n        leftDepth\
        \ = self.dfs(node.left, depth + 1)\n        rightDepth = self.dfs(node.right,\
        \ depth + 1)\n        if leftDepth == rightDepth and leftDepth > self.maxDepth:\n\
        \            self.maxDepth = leftDepth\n            self.result = node\n   \
        \     return max(leftDepth, rightDepth)"
      c: "struct TreeNode* subtreeWithAllDeepest(struct TreeNode* root) {\n    int maxDepth\
        \ = 0;\n    struct TreeNode* result = NULL;\n    dfs(root, 0, &maxDepth, &result);\n\
        \    return result;\n}\nint dfs(struct TreeNode* node, int depth, int* maxDepth,\
        \ struct TreeNode** result) {\n    if (!node) return depth;\n    int leftDepth\
        \ = dfs(node->left, depth + 1, maxDepth, result);\n    int rightDepth = dfs(node->right,\
        \ depth + 1, maxDepth, result);\n    if (leftDepth == rightDepth && leftDepth\
        \ > *maxDepth) {\n        *maxDepth = leftDepth;\n        *result = node;\n\
        \    }\n    return (leftDepth > rightDepth) ? leftDepth : rightDepth;\n}"
      csharp: "/**\n     * Definition for a binary tree node.\n     * public class TreeNode\
        \ {\n     *     public int val;\n     *     public TreeNode left;\n     *  \
        \   public TreeNode right;\n     *     public TreeNode(int val=0, TreeNode left=null,\
        \ TreeNode right=null) {\n     *         this.val = val;\n     *         this.left\
        \ = left;\n     *         this.right = right;\n     *     }\n     * }\n    \
        \ */\n    public class Solution {\n        public TreeNode SubtreeWithAllDeepest(TreeNode\
        \ root) {\n            int maxDepth = 0;\n            TreeNode result = null;\n\
        \            DFS(root, 0, ref maxDepth, ref result);\n            return result;\n\
        \        }\n\n        private bool DFS(TreeNode node, int depth, ref int maxDepth,\
        \ ref TreeNode result) {\n            if (node == null) return false;\n    \
        \        if (depth > maxDepth) {\n                maxDepth = depth;\n      \
        \          result = node;\n            }\n            bool left = DFS(node.left,\
        \ depth + 1, ref maxDepth, ref result);\n            bool right = DFS(node.right,\
        \ depth + 1, ref maxDepth, ref result);\n            if (left && right) {\n\
        \                result = node;\n                return true;\n            }\n\
        \            return left || right;\n        }\n    }"
      javascript: "/**\n     * Definition for a binary tree node.\n     * function TreeNode(val,\
        \ left, right) {\n     *     this.val = (val===undefined ? 0 : val)\n     *\
        \     this.left = (left===undefined ? null : left)\n     *     this.right =\
        \ (right===undefined ? null : right)\n     * }\n     */\n    /**\n     * @param\
        \ {TreeNode} root\n     * @return {TreeNode}\n     */\n    var subtreeWithAllDeepest\
        \ = function(root) {\n        let maxDepth = 0;\n        let result = null;\n\
        \        function dfs(node, depth) {\n            if (!node) return false;\n\
        \            if (depth > maxDepth) {\n                maxDepth = depth;\n  \
        \              result = node;\n            }\n            let left = dfs(node.left,\
        \ depth + 1);\n            let right = dfs(node.right, depth + 1);\n       \
        \     if (left && right) {\n                result = node;\n               \
        \ return true;\n            }\n            return left || right;\n        }\n\
        \        dfs(root, 0);\n        return result;\n    }"
      typescript: "/**\n     * Definition for a binary tree node.\n     * class TreeNode\
        \ {\n     *     val: number\n     *     left: TreeNode | null\n     *     right:\
        \ TreeNode | null\n     *     constructor(val?: number, left?: TreeNode | null,\
        \ right?: TreeNode | null) {\n     *         this.val = (val===undefined ? 0\
        \ : val)\n     *         this.left = (left===undefined ? null : left)\n    \
        \ *         this.right = (right===undefined ? null : right)\n     *     }\n\
        \     * }\n     */\n\n    function subtreeWithAllDeepest(root: TreeNode | null):\
        \ TreeNode | null {\n        let maxDepth = 0;\n        let result: TreeNode\
        \ | null = null;\n        function dfs(node: TreeNode | null, depth: number):\
        \ boolean {\n            if (!node) return false;\n            if (depth > maxDepth)\
        \ {\n                maxDepth = depth;\n                result = node;\n   \
        \         }\n            let left = dfs(node.left, depth + 1);\n           \
        \ let right = dfs(node.right, depth + 1);\n            if (left && right) {\n\
        \                result = node;\n                return true;\n            }\n\
        \            return left || right;\n        }\n        dfs(root, 0);\n     \
        \   return result;\n    }"
      php: "/**\n     * Definition for a binary tree node.\n     * class TreeNode {\n\
        \     *     public $val = null;\n     *     public $left = null;\n     *   \
        \  public $right = null;\n     *     function __construct($val = 0, $left =\
        \ null, $right = null) {\n     *         $this->val = $val;\n     *        \
        \ $this->left = $left;\n     *         $this->right = $right;\n     *     }\n\
        \     * }\n     */\n    class Solution {\n\n        /**\n         * @param TreeNode\
        \ $root\n         * @return TreeNode\n         */\n        function subtreeWithAllDeepest($root)\
        \ {\n            $maxDepth = 0;\n            $result = null;\n            $this->dfs($root,\
        \ 0, $maxDepth, $result);\n            return $result;\n        }\n\n      \
        \  private function dfs($node, $depth, &$maxDepth, &$result) {\n           \
        \ if (!$node) return false;\n            if ($depth > $maxDepth) {\n       \
        \         $maxDepth = $depth;\n                $result = $node;\n          \
        \  }\n            $left = $this->dfs($node->left, $depth + 1, $maxDepth, $result);\n\
        \            $right = $this->dfs($node->right, $depth + 1, $maxDepth, $result);\n\
        \            if ($left && $right) {\n                $result = $node;\n    \
        \            return true;\n            }\n            return $left || $right;\n\
        \        }\n    }"
      swift: "/**\n     * Definition for a binary tree node.\n     * public class TreeNode\
        \ {\n     *     public var val: Int\n     *     public var left: TreeNode?\n\
        \     *     public var right: TreeNode?\n     *     public init() { self.val\
        \ = 0; self.left = nil; self.right = nil; }\n     *     public init(_ val: Int)\
        \ { self.val = val; self.left = nil; self.right = nil; }\n     *     public\
        \ init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {\n     *        \
        \ self.val = val\n     *         self.left = left\n     *         self.right\
        \ = right\n     *     }\n     * }\n     */\n    class Solution {\n        func\
        \ subtreeWithAllDeepest(_ root: TreeNode?) -> TreeNode? {\n            var maxDepth\
        \ = 0\n            var result: TreeNode?\n            dfs(root, 0, &maxDepth,\
        \ &result)\n            return result\n        }\n\n        private func dfs(_\
        \ node: TreeNode?, _ depth: Int, _ maxDepth: inout Int, _ result: inout TreeNode?)\
        \ {\n            guard let node = node else { return }\n            if depth\
        \ > maxDepth {\n                maxDepth = depth\n                result = node\n\
        \            }\n            let left = dfs(node.left, depth + 1, &maxDepth,\
        \ &result)\n            let right = dfs(node.right, depth + 1, &maxDepth, &result)\n\
        \            if left && right {\n                result = node\n           \
        \     return\n            }\n            if left || right {\n              \
        \  return\n            }\n        }\n    }"
      kotlin: "class Solution {\n    fun subtreeWithAllDeepest(root: TreeNode?): TreeNode?\
        \ {\n        var maxDepth = 0\n        var result: TreeNode? = null\n      \
        \  dfs(root, 0)\n        return result\n        fun dfs(node: TreeNode?, depth:\
        \ Int): Int {\n            if (node == null) return depth\n            maxDepth\
        \ = maxOf(maxDepth, depth)\n            val leftDepth = dfs(node.left, depth\
        \ + 1)\n            val rightDepth = dfs(node.right, depth + 1)\n          \
        \  if (leftDepth == maxDepth && rightDepth == maxDepth) {\n                result\
        \ = node\n            }\n            return maxOf(leftDepth, rightDepth)\n \
        \       }\n    }\n}"
      dart: "class Solution {\n  TreeNode? subtreeWithAllDeepest(TreeNode? root) {\n\
        \    int maxDepth = 0;\n    TreeNode? result;\n    dfs(root, 0);\n    return\
        \ result;\n    int dfs(TreeNode? node, int depth) {\n      if (node == null)\
        \ return depth;\n      maxDepth = maxDepth > depth ? maxDepth : depth;\n   \
        \   int leftDepth = dfs(node.left, depth + 1);\n      int rightDepth = dfs(node.right,\
        \ depth + 1);\n      if (leftDepth == maxDepth && rightDepth == maxDepth) {\n\
        \        result = node;\n      }\n      return max(leftDepth, rightDepth);\n\
        \    }\n  }\n}"
      go: "func subtreeWithAllDeepest(root *TreeNode) *TreeNode {\n    maxDepth := 0\n\
        \    var result *TreeNode\n    dfs(root, 0)\n    return result\n    func dfs(node\
        \ *TreeNode, depth int) int {\n        if node == nil {\n            return\
        \ depth\n        }\n        if depth > maxDepth {\n            maxDepth = depth\n\
        \        }\n        leftDepth := dfs(node.Left, depth+1)\n        rightDepth\
        \ := dfs(node.Right, depth+1)\n        if leftDepth == maxDepth && rightDepth\
        \ == maxDepth {\n            result = node\n        }\n        return max(leftDepth,\
        \ rightDepth)\n    }\n    func max(a, b int) int {\n        if a > b {\n   \
        \         return a\n        }\n        return b\n    }\n}"
      ruby: "def subtree_with_all_deepest(root)\n    @max_depth = 0\n    @result = nil\n\
        \    dfs(root, 0)\n    @result\nend\n\ndef dfs(node, depth)\n    return depth\
        \ if node.nil?\n    @max_depth = [@max_depth, depth].max\n    left_depth = dfs(node.left,\
        \ depth + 1)\n    right_depth = dfs(node.right, depth + 1)\n    if left_depth\
        \ == @max_depth && right_depth == @max_depth\n        @result = node\n    end\n\
        \    [left_depth, right_depth].max\nend"
      scala: "object Solution {\n    def subtreeWithAllDeepest(root: TreeNode): TreeNode\
        \ = {\n        var maxDepth = 0\n        var result: TreeNode = null\n     \
        \   dfs(root, 0)\n        result\n        def dfs(node: TreeNode, depth: Int):\
        \ Int = {\n            if (node == null) return depth\n            maxDepth\
        \ = math.max(maxDepth, depth)\n            val leftDepth = dfs(node.left, depth\
        \ + 1)\n            val rightDepth = dfs(node.right, depth + 1)\n          \
        \  if (leftDepth == maxDepth && rightDepth == maxDepth) {\n                result\
        \ = node\n            }\n            math.max(leftDepth, rightDepth)\n     \
        \   }\n    }\n}"
      rust: "use std::rc::Rc;\nuse std::cell::RefCell;\nimpl Solution {\n    pub fn\
        \ subtree_with_all_deepest(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>>\
        \ {\n        fn dfs(node: &Option<Rc<RefCell<TreeNode>>>) -> (i32, Option<Rc<RefCell<TreeNode>>>)\
        \ {\n            match node {\n                None => (0, None),\n        \
        \        Some(node) => {\n                    let node = node.borrow();\n  \
        \                  let (left_depth, left_ancestor) = dfs(&node.left);\n    \
        \                let (right_depth, right_ancestor) = dfs(&node.right);\n   \
        \                 if left_depth > right_depth {\n                        (left_depth\
        \ + 1, left_ancestor)\n                    } else if left_depth < right_depth\
        \ {\n                        (right_depth + 1, right_ancestor)\n           \
        \         } else {\n                        (left_depth + 1, Some(node.clone()))\n\
        \                    }\n                }\n            }\n        }\n      \
        \  dfs(&root).1\n    }\n}"
      racket: "define/contract (subtree-with-all-deepest root)\n  (-> (or/c tree-node?\
        \ #f) (or/c tree-node? #f))\n  (define (dfs node)\n    (cond\n      [(not node)\
        \ (values 0 #f)]\n      [else\n       (let ([left-depth left-ancestor] (dfs\
        \ (tree-node-left node)))\n         [right-depth right-ancestor] (dfs (tree-node-right\
        \ node)))\n       (cond\n         [(> left-depth right-depth) (values (add1\
        \ left-depth) left-ancestor)]\n         [(< left-depth right-depth) (values\
        \ (add1 right-depth) right-ancestor)]\n         [else (values (add1 left-depth)\
        \ node)]))]))\n  (cdr (dfs root)))"
      erlang: "subtree_with_all_deepest(Root) ->\n    dfs(Root).\n\ndfs(null) -> {0,\
        \ null};\ndfs(#tree_node{val = Val, left = Left, right = Right}) ->\n    {LeftDepth,\
        \ LeftAncestor} = dfs(Left),\n    {RightDepth, RightAncestor} = dfs(Right),\n\
        \    if\n        LeftDepth > RightDepth -> {LeftDepth + 1, LeftAncestor};\n\
        \        LeftDepth < RightDepth -> {RightDepth + 1, RightAncestor};\n      \
        \  true -> {LeftDepth + 1, #tree_node{val = Val, left = Left, right = Right}}\n\
        \    end."
      elixir: "defmodule Solution do\n  @spec subtree_with_all_deepest(root :: TreeNode.t\
        \ | nil) :: TreeNode.t | nil\n  def subtree_with_all_deepest(root) do\n    dfs(root)\n\
        \  end\n\n  defp dfs(nil), do: {0, nil}\n\n  defp dfs(%TreeNode{val: val, left:\
        \ left, right: right}) do\n    {left_depth, left_ancestor} = dfs(left)\n   \
        \ {right_depth, right_ancestor} = dfs(right)\n\n    cond do\n      left_depth\
        \ > right_depth -> {left_depth + 1, left_ancestor}\n      left_depth < right_depth\
        \ -> {right_depth + 1, right_ancestor}\n      true -> {left_depth + 1, %TreeNode{val:\
        \ val, left: left, right: right}}\n    end\n  end\nend"
    approach: "The problem can be solved by first finding the maximum depth of the tree\
      \ and then finding the node that is the lowest common ancestor of all the deepest\
      \ nodes. This can be achieved by performing a depth-first search (DFS) on the\
      \ tree to find the maximum depth and the deepest nodes. Then, we can perform another\
      \ DFS to find the lowest common ancestor of the deepest nodes. The key intuition\
      \ here is that the lowest common ancestor of the deepest nodes will be the root\
      \ of the smallest subtree that contains all the deepest nodes. \n\nThe algorithm\
      \ works by first initializing the maximum depth and the deepest nodes. Then, it\
      \ performs a DFS on the tree to update the maximum depth and the deepest nodes.\
      \ After that, it performs another DFS to find the lowest common ancestor of the\
      \ deepest nodes. If the current node is the lowest common ancestor, it returns\
      \ the current node. Otherwise, it recursively calls the function on the left and\
      \ right children of the current node. If both recursive calls return a node, it\
      \ means that the current node is the lowest common ancestor, so it returns the\
      \ current node. If only one recursive call returns a node, it means that the lowest\
      \ common ancestor is in the subtree of the child that returned a node, so it returns\
      \ the node returned by the recursive call."
    time_complexity: O(n) where n is the number of nodes in the tree. This is because
      we are performing two DFS traversals on the tree, each of which visits every node
      in the tree once. The time complexity is linear because we are visiting each node
      a constant number of times.
    space_complexity: O(h) where h is the height of the tree. This is because the maximum
      depth of the recursive call stack is equal to the height of the tree. In the worst
      case, the tree is skewed to one side and the height of the tree is equal to the
      number of nodes in the tree, so the space complexity is O(n). However, for a balanced
      tree, the height of the tree is logarithmic in the number of nodes, so the space
      complexity is O(log n).
    elapsed_time: 11.55224323272705
    model: llama-3.3-70b-versatile
    generated_at: '2026-01-09 01:12:30 '
---

## Problem #865: Smallest Subtree with all the Deepest Nodes

**Difficulty:** Medium

**Topics:** Hash Table, Tree, Depth-First Search, Breadth-First Search, Binary Tree

## Problem Description

<p>Given the <code>root</code> of a binary tree, the depth of each node is <strong>the shortest distance to the root</strong>.</p>

<p>Return <em>the smallest subtree</em> such that it contains <strong>all the deepest nodes</strong> in the original tree.</p>

<p>A node is called <strong>the deepest</strong> if it has the largest depth possible among any node in the entire tree.</p>

<p>The <strong>subtree</strong> of a node is a tree consisting of that node, plus the set of all descendants of that node.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/01/sketch1.png" style="width: 600px; height: 510px;" />
<pre>
<strong>Input:</strong> root = [3,5,1,6,2,0,8,null,null,7,4]
<strong>Output:</strong> [2,7,4]
<strong>Explanation:</strong> We return the node with value 2, colored in yellow in the diagram.
The nodes coloured in blue are the deepest nodes of the tree.
Notice that nodes 5, 3 and 2 contain the deepest nodes in the tree but node 2 is the smallest subtree among them, so we return it.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = [1]
<strong>Output:</strong> [1]
<strong>Explanation:</strong> The root is the deepest node in the tree.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> root = [0,1,3,null,2]
<strong>Output:</strong> [2]
<strong>Explanation:</strong> The deepest node in the tree is 2, the valid subtrees are the subtrees of nodes 2, 1 and 0 but the subtree of node 2 is the smallest.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree will be in the range <code>[1, 500]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 500</code></li>
	<li>The values of the nodes in the tree are <strong>unique</strong>.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Note:</strong> This question is the same as 1123: <a href="https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/" target="_blank">https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/</a></p>


## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2026-01-09 01:12:03 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem asks for the smallest subtree containing all deepest nodes, which is equivalent to finding the Lowest Common Ancestor (LCA) of all deepest leaves. We can solve this using a single recursive depth-first traversal (post-order traversal) that computes two pieces of information for each node: its height (distance to the deepest leaf in its subtree) and the LCA of all deepest leaves within its subtree. The height of a null node is 0, and the height of a leaf node is 1.

For any given node, we recursively call the helper function on its left and right children to get their respective heights and LCAs. If the left subtree's height is greater than the right subtree's height, the LCA of deepest nodes for the current node's subtree must be the LCA from the left subtree. Similarly, if the right subtree's height is greater, we take the LCA from the right subtree. If both subtrees have the same maximum height, it means the deepest nodes are equally distributed or found in both subtrees, making the current node itself the LCA of all deepest nodes within its subtree. The height for the current node is then 1 plus the maximum of its children's heights. The final result is the LCA node returned by the initial call to the helper function on the root.

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
    // Returns a pair: {height, LCA_node}
    // height is the maximum depth from the current node to a leaf in its subtree.
    // A null node has height -1, a leaf node has height 0.
    std::pair<int, TreeNode*> dfs(TreeNode* node) {
        if (!node) {
            return {-1, nullptr};
        }

        std::pair<int, TreeNode*> left_res = dfs(node->left);
        std::pair<int, TreeNode*> right_res = dfs(node->right);

        int left_height = left_res.first;
        TreeNode* left_lca = left_res.second;

        int right_height = right_res.first;
        TreeNode* right_lca = right_res.second;

        if (left_height == right_height) {
            // If both subtrees have the same maximum height, this node is the LCA
            // of all deepest nodes within its subtree.
            return {left_height + 1, node};
        } else if (left_height > right_height) {
            // Deepest nodes are exclusively in the left subtree.
            return {left_height + 1, left_lca};
        } else {
            // Deepest nodes are exclusively in the right subtree.
            return {right_height + 1, right_lca};
        }
    }

    TreeNode* subtreeWithAllDeepest(TreeNode* root) {
        return dfs(root).second;
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
class Solution {
    // Helper class to return both height and the LCA node
    // height is the maximum depth from the current node to a leaf in its subtree.
    // A null node has height -1, a leaf node has height 0.
    class Result {
        int height;
        TreeNode node;

        Result(int height, TreeNode node) {
            this.height = height;
            this.node = node;
        }
    }

    public TreeNode subtreeWithAllDeepest(TreeNode root) {
        return dfs(root).node;
    }

    private Result dfs(TreeNode node) {
        if (node == null) {
            return new Result(-1, null);
        }

        Result leftRes = dfs(node.left);
        Result rightRes = dfs(node.right);

        if (leftRes.height == rightRes.height) {
            // If both subtrees have the same maximum height, this node is the LCA
            // of all deepest nodes within its subtree.
            return new Result(leftRes.height + 1, node);
        } else if (leftRes.height > rightRes.height) {
            // Deepest nodes are exclusively in the left subtree.
            return new Result(leftRes.height + 1, leftRes.node);
        } else {
            // Deepest nodes are exclusively in the right subtree.
            return new Result(rightRes.height + 1, rightRes.node);
        }
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
    def subtreeWithAllDeepest(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        # Helper function returns a tuple: (height, lca_node)
        # height is the maximum depth from the current node to a leaf in its subtree.
        # A null node has height -1, a leaf node has height 0.
        def dfs(node):
            if not node:
                return -1, None

            left_height, left_lca = dfs(node.left)
            right_height, right_lca = dfs(node.right)

            if left_height == right_height:
                # If both subtrees have the same maximum height, this node is the LCA
                # of all deepest nodes within its subtree.
                return left_height + 1, node
            elif left_height > right_height:
                # Deepest nodes are exclusively in the left subtree.
                return left_height + 1, left_lca
            else: # right_height > left_height
                # Deepest nodes are exclusively in the right subtree.
                return right_height + 1, right_lca

        _, result_node = dfs(root)
        return result_node
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
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Helper function returns a tuple: (height, lca_node)
        # height is the maximum depth from the current node to a leaf in its subtree.
        # A null node has height -1, a leaf node has height 0.
        def dfs(node: Optional[TreeNode]) -> tuple[int, Optional[TreeNode]]:
            if not node:
                return -1, None

            left_height, left_lca = dfs(node.left)
            right_height, right_lca = dfs(node.right)

            if left_height == right_height:
                # If both subtrees have the same maximum height, this node is the LCA
                # of all deepest nodes within its subtree.
                return left_height + 1, node
            elif left_height > right_height:
                # Deepest nodes are exclusively in the left subtree.
                return left_height + 1, left_lca
            else: # right_height > left_height
                # Deepest nodes are exclusively in the right subtree.
                return right_height + 1, right_lca

        _, result_node = dfs(root)
        return result_node
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

// Custom struct to return both height and the node pointer
// height is the maximum depth from the current node to a leaf in its subtree.
// A null node has height -1, a leaf node has height 0.
typedef struct {
    int height;
    struct TreeNode* node;
} Result;

Result dfs(struct TreeNode* node) {
    if (node == NULL) {
        Result res = {-1, NULL};
        return res;
    }

    Result left_res = dfs(node->left);
    Result right_res = dfs(node->right);

    int left_height = left_res.height;
    struct TreeNode* left_lca = left_res.node;

    int right_height = right_res.height;
    struct TreeNode* right_lca = right_res.node;

    if (left_height == right_height) {
        // If both subtrees have the same maximum height, this node is the LCA
        // of all deepest nodes within its subtree.
        Result res = {left_height + 1, node};
        return res;
    } else if (left_height > right_height) {
        // Deepest nodes are exclusively in the left subtree.
        Result res = {left_height + 1, left_lca};
        return res;
    } else {
        // Deepest nodes are exclusively in the right subtree.
        Result res = {right_height + 1, right_lca};
        return res;
    }
}

struct TreeNode* subtreeWithAllDeepest(struct TreeNode* root) {
    return dfs(root).node;
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
    private class Result {
        public int Depth;
        public TreeNode Node;

        public Result(int depth, TreeNode node) {
            Depth = depth;
            Node = node;
        }
    }

    public TreeNode SubtreeWithAllDeepest(TreeNode root) {
        return DFS(root).Node;
    }

    private Result DFS(TreeNode node) {
        if (node == null) {
            return new Result(0, null);
        }

        Result leftResult = DFS(node.left);
        Result rightResult = DFS(node.right);

        if (leftResult.Depth == rightResult.Depth) {
            return new Result(leftResult.Depth + 1, node);
        } else if (leftResult.Depth > rightResult.Depth) {
            return new Result(leftResult.Depth + 1, leftResult.Node);
        } else {
            return new Result(rightResult.Depth + 1, rightResult.Node);
        }
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
 * @return {TreeNode}
 */
var subtreeWithAllDeepest = function(root) {
    function dfs(node) {
        if (node === null) {
            return [0, null];
        }

        let [leftDepth, leftNode] = dfs(node.left);
        let [rightDepth, rightNode] = dfs(node.right);

        if (leftDepth === rightDepth) {
            return [leftDepth + 1, node];
        } else if (leftDepth > rightDepth) {
            return [leftDepth + 1, leftNode];
        } else {
            return [rightDepth + 1, rightNode];
        }
    }

    return dfs(root)[1];
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

function subtreeWithAllDeepest(root: TreeNode | null): TreeNode | null {
    function dfs(node: TreeNode | null): [number, TreeNode | null] {
        if (node === null) {
            return [0, null];
        }

        const [leftDepth, leftNode] = dfs(node.left);
        const [rightDepth, rightNode] = dfs(node.right);

        if (leftDepth === rightDepth) {
            return [leftDepth + 1, node];
        } else if (leftDepth > rightDepth) {
            return [leftDepth + 1, leftNode];
        } else {
            return [rightDepth + 1, rightNode];
        }
    }

    return dfs(root)[1];
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
     * @return TreeNode
     */
    function subtreeWithAllDeepest($root) {
        return $this->dfsHelper($root)[1];
    }

    /**
     * Helper method for DFS traversal
     * @param TreeNode $node
     * @return array [depth, node]
     */
    private function dfsHelper(?TreeNode $node): array {
        if ($node === null) {
            return [0, null];
        }

        list($leftDepth, $leftNode) = $this->dfsHelper($node->left);
        list($rightDepth, $rightNode) = $this->dfsHelper($node->right);

        if ($leftDepth === $rightDepth) {
            return [$leftDepth + 1, $node];
        } elseif ($leftDepth > $rightDepth) {
            return [$leftDepth + 1, $leftNode];
        } else {
            return [$rightDepth + 1, $rightNode];
        }
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
 *         this.right = right
 *     }
 * }
 */
class Solution {
    func subtreeWithAllDeepest(_ root: TreeNode?) -> TreeNode? {
        func dfs(_ node: TreeNode?) -> (depth: Int, node: TreeNode?) {
            guard let node = node else {
                return (0, nil)
            }

            let leftResult = dfs(node.left)
            let rightResult = dfs(node.right)

            if leftResult.depth == rightResult.depth {
                return (leftResult.depth + 1, node)
            } else if leftResult.depth > rightResult.depth {
                return (leftResult.depth + 1, leftResult.node)
            } else {
                return (rightResult.depth + 1, rightResult.node)
            }
        }

        return dfs(root).node
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
 * var ti = TreeNode(5)
 * var v = ti.`val`
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */
class Solution {
    fun subtreeWithAllDeepest(root: TreeNode?): TreeNode? {
        fun dfs(node: TreeNode?): Pair<Int, TreeNode?> {
            if (node == null) {
                return Pair(0, null)
            }

            val (leftDepth, leftSubtreeRoot) = dfs(node.left)
            val (rightDepth, rightSubtreeRoot) = dfs(node.right)

            return when {
                leftDepth > rightDepth -> Pair(leftDepth + 1, leftSubtreeRoot)
                rightDepth > leftDepth -> Pair(rightDepth + 1, rightSubtreeRoot)
                else -> Pair(leftDepth + 1, node)
            }
        }

        return dfs(root).second
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

class _Result {
  int depth;
  TreeNode? node;
  _Result(this.depth, this.node);
}

class Solution {
  TreeNode? subtreeWithAllDeepest(TreeNode? root) {
    _Result dfs(TreeNode? node) {
      if (node == null) {
        return _Result(0, null);
      }

      _Result leftResult = dfs(node.left);
      _Result rightResult = dfs(node.right);

      if (leftResult.depth > rightResult.depth) {
        return _Result(leftResult.depth + 1, leftResult.node);
      } else if (rightResult.depth > leftResult.depth) {
        return _Result(rightResult.depth + 1, rightResult.node);
      } else {
        return _Result(leftResult.depth + 1, node);
      }
    }

    return dfs(root).node;
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
func subtreeWithAllDeepest(root *TreeNode) *TreeNode {
    var dfs func(*TreeNode) (int, *TreeNode)
    dfs = func(node *TreeNode) (int, *TreeNode) {
        if node == nil {
            return 0, nil
        }

        leftDepth, leftSubtreeRoot := dfs(node.Left)
        rightDepth, rightSubtreeRoot := dfs(node.Right)

        if leftDepth > rightDepth {
            return leftDepth + 1, leftSubtreeRoot
        } else if rightDepth > leftDepth {
            return rightDepth + 1, rightSubtreeRoot
        } else {
            return leftDepth + 1, node
        }
    }

    _, resultNode := dfs(root)
    return resultNode
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
# @return {TreeNode}
def subtree_with_all_deepest(root)
    def dfs(node)
        return [0, nil] if node.nil?

        left_depth, left_subtree_root = dfs(node.left)
        right_depth, right_subtree_root = dfs(node.right)

        if left_depth > right_depth
            [left_depth + 1, left_subtree_root]
        elsif right_depth > left_depth
            [right_depth + 1, right_subtree_root]
        else
            [left_depth + 1, node]
        end
    end

    dfs(root).last
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
    def subtreeWithAllDeepest(root: TreeNode): TreeNode = {
        def dfs(node: TreeNode): (Int, TreeNode) = {
            if (node == null) {
                return (0, null)
            }

            val (leftDepth, leftSubtreeRoot) = dfs(node.left)
            val (rightDepth, rightSubtreeRoot) = dfs(node.right)

            if (leftDepth > rightDepth) {
                (leftDepth + 1, leftSubtreeRoot)
            } else if (rightDepth > leftDepth) {
                (rightDepth + 1, rightSubtreeRoot)
            } else {
                (leftDepth + 1, node)
            }
        }

        dfs(root)._2
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
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
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn subtree_with_all_deepest(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        // Helper function returns (height, lca_node)
        // height is the distance from current node to the deepest leaf in its subtree
        fn dfs(node_opt: Option<Rc<RefCell<TreeNode>>>) -> (i32, Option<Rc<RefCell<TreeNode>>>) {
            match node_opt {
                None => (0, None),
                Some(node_rc) => {
                    let node = node_rc.borrow();
                    let (left_height, left_lca) = dfs(node.left.clone());
                    let (right_height, right_lca) = dfs(node.right.clone());

                    if left_height == right_height {
                        // If both subtrees have the same max height, this node is the LCA
                        (left_height + 1, Some(Rc::clone(&node_rc)))
                    } else if left_height > right_height {
                        // Deepest nodes are in the left subtree
                        (left_height + 1, left_lca)
                    } else {
                        // Deepest nodes are in the right subtree
                        (right_height + 1, right_lca)
                    }
                }
            }
        }

        let (_, result_node) = dfs(root);
        result_node
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

(define/contract (subtree-with-all-deepest root)
  (-> (or/c tree-node? #f) (or/c tree-node? #f))
  (define (dfs node)
    ; Returns a pair: (cons height lca-node)
    ; height is the distance from current node to the deepest leaf in its subtree
    (if (not node)
        (cons 0 #f) ; Base case: null node has height 0, no LCA node
        (let* ((left-res (dfs (tree-node-left node)))
               (right-res (dfs (tree-node-right node)))
               (left-height (car left-res))
               (left-lca (cdr left-res))
               (right-height (car right-res))
               (right-lca (cdr right-res)))
          (cond
            ((= left-height right-height)
             ; If both subtrees have the same max height, this node is the LCA
             (cons (+ left-height 1) node))
            ((> left-height right-height)
             ; Deepest nodes are in the left subtree
             (cons (+ left-height 1) left-lca))
            (else ; (< right-height left-height)
             ; Deepest nodes are in the right subtree
             (cons (+ right-height 1) right-lca))))))

  (cdr (dfs root)) ; We only need the LCA node from the result of dfs(root)
)
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

-spec subtree_with_all_deepest(Root :: #tree_node{} | null) -> #tree_node{} | null.
subtree_with_all_deepest(Root) ->
  % Helper function returns {Height, LCA_Node}
  % Height is the distance from current node to the deepest leaf in its subtree
  {_Height, LCA_Node} = dfs(Root),
  LCA_Node.

dfs(null) -> {0, null};
dfs(Node) ->
  Left = Node#tree_node.left,
  Right = Node#tree_node.right,

  {LeftHeight, LeftLCA} = dfs(Left),
  {RightHeight, RightLCA} = dfs(Right),

  if
    LeftHeight == RightHeight ->
      % If both subtrees have the same max height, this node is the LCA
      {LeftHeight + 1, Node};
    LeftHeight > RightHeight ->
      % Deepest nodes are in the left subtree
      {LeftHeight + 1, LeftLCA};
    true -> % RightHeight > LeftHeight
      % Deepest nodes are in the right subtree
      {RightHeight + 1, RightLCA}
  end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
# Definition for a binary tree node.
#
# defmodule TreeNode do
#   @type t :: %__MODULE__{n#           val: integer,
#           left: TreeNode.t() | nil,
#           right: TreeNode.t() | nil
#         }
#   defstruct val: 0, left: nil, right: nil
# end

defmodule Solution do
  @spec subtree_with_all_deepest(root :: TreeNode.t | nil) :: TreeNode.t | nil
  def subtree_with_all_deepest(root) do
    # Helper function returns {height, lca_node}
    # height is the distance from current node to the deepest leaf in its subtree
    dfs(root)
    |> elem(1) # We only need the LCA node from the result of dfs(root)
  end

  defp dfs(nil), do: {0, nil} # Base case: nil node has height 0, no LCA node
  defp dfs(%TreeNode{} = node) do
    {left_height, left_lca} = dfs(node.left)
    {right_height, right_lca} = dfs(node.right)

    cond do
      left_height == right_height ->
        # If both subtrees have the same max height, this node is the LCA
        {left_height + 1, node}
      left_height > right_height ->
        # Deepest nodes are in the left subtree
        {left_height + 1, left_lca}
      true -> # right_height > left_height
        # Deepest nodes are in the right subtree
        {right_height + 1, right_lca}
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is O(N), where N is the number of nodes in the binary tree. This is because the algorithm performs a single depth-first traversal, visiting each node exactly once. For each node, a constant amount of work (recursive calls, comparisons, and arithmetic operations) is performed.

- **Space Complexity:** The space complexity is O(H), where H is the height of the binary tree. This space is used by the recursion stack during the depth-first traversal. In the worst-case scenario (a skewed tree), H can be equal to N, leading to O(N) space complexity. In the best-case scenario (a balanced tree), H is O(log N), resulting in O(log N) space complexity.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2026-01-09 01:12:30 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved by first finding the maximum depth of the tree and then finding the node that is the lowest common ancestor of all the deepest nodes. This can be achieved by performing a depth-first search (DFS) on the tree to find the maximum depth and the deepest nodes. Then, we can perform another DFS to find the lowest common ancestor of the deepest nodes. The key intuition here is that the lowest common ancestor of the deepest nodes will be the root of the smallest subtree that contains all the deepest nodes. 

The algorithm works by first initializing the maximum depth and the deepest nodes. Then, it performs a DFS on the tree to update the maximum depth and the deepest nodes. After that, it performs another DFS to find the lowest common ancestor of the deepest nodes. If the current node is the lowest common ancestor, it returns the current node. Otherwise, it recursively calls the function on the left and right children of the current node. If both recursive calls return a node, it means that the current node is the lowest common ancestor, so it returns the current node. If only one recursive call returns a node, it means that the lowest common ancestor is in the subtree of the child that returned a node, so it returns the node returned by the recursive call.

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
    TreeNode* subtreeWithAllDeepest(TreeNode* root) {
        int maxDepth = 0;
        TreeNode* result = nullptr;
        dfs(root, 0, maxDepth, result);
        return result;
    }
    int dfs(TreeNode* node, int depth, int& maxDepth, TreeNode*& result) {
        if (!node) return depth;
        int leftDepth = dfs(node->left, depth + 1, maxDepth, result);
        int rightDepth = dfs(node->right, depth + 1, maxDepth, result);
        if (leftDepth == rightDepth && leftDepth > maxDepth) {
            maxDepth = leftDepth;
            result = node;
        }
        return max(leftDepth, rightDepth);
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public TreeNode subtreeWithAllDeepest(TreeNode root) {
        int[] maxDepth = new int[] {0};
        TreeNode[] result = new TreeNode[] {null};
        dfs(root, 0, maxDepth, result);
        return result[0];
    }
    int dfs(TreeNode node, int depth, int[] maxDepth, TreeNode[] result) {
        if (node == null) return depth;
        int leftDepth = dfs(node.left, depth + 1, maxDepth, result);
        int rightDepth = dfs(node.right, depth + 1, maxDepth, result);
        if (leftDepth == rightDepth && leftDepth > maxDepth[0]) {
            maxDepth[0] = leftDepth;
            result[0] = node;
        }
        return Math.max(leftDepth, rightDepth);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution(object):
    def subtreeWithAllDeepest(self, root):
        self.maxDepth = 0
        self.result = None
        self.dfs(root, 0)
        return self.result
    def dfs(self, node, depth):
        if not node:
            return depth
        leftDepth = self.dfs(node.left, depth + 1)
        rightDepth = self.dfs(node.right, depth + 1)
        if leftDepth == rightDepth and leftDepth > self.maxDepth:
            self.maxDepth = leftDepth
            self.result = node
        return max(leftDepth, rightDepth)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.maxDepth = 0
        self.result = None
        self.dfs(root, 0)
        return self.result
    def dfs(self, node, depth):
        if not node:
            return depth
        leftDepth = self.dfs(node.left, depth + 1)
        rightDepth = self.dfs(node.right, depth + 1)
        if leftDepth == rightDepth and leftDepth > self.maxDepth:
            self.maxDepth = leftDepth
            self.result = node
        return max(leftDepth, rightDepth)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
struct TreeNode* subtreeWithAllDeepest(struct TreeNode* root) {
    int maxDepth = 0;
    struct TreeNode* result = NULL;
    dfs(root, 0, &maxDepth, &result);
    return result;
}
int dfs(struct TreeNode* node, int depth, int* maxDepth, struct TreeNode** result) {
    if (!node) return depth;
    int leftDepth = dfs(node->left, depth + 1, maxDepth, result);
    int rightDepth = dfs(node->right, depth + 1, maxDepth, result);
    if (leftDepth == rightDepth && leftDepth > *maxDepth) {
        *maxDepth = leftDepth;
        *result = node;
    }
    return (leftDepth > rightDepth) ? leftDepth : rightDepth;
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
        public TreeNode SubtreeWithAllDeepest(TreeNode root) {
            int maxDepth = 0;
            TreeNode result = null;
            DFS(root, 0, ref maxDepth, ref result);
            return result;
        }

        private bool DFS(TreeNode node, int depth, ref int maxDepth, ref TreeNode result) {
            if (node == null) return false;
            if (depth > maxDepth) {
                maxDepth = depth;
                result = node;
            }
            bool left = DFS(node.left, depth + 1, ref maxDepth, ref result);
            bool right = DFS(node.right, depth + 1, ref maxDepth, ref result);
            if (left && right) {
                result = node;
                return true;
            }
            return left || right;
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
     * @return {TreeNode}
     */
    var subtreeWithAllDeepest = function(root) {
        let maxDepth = 0;
        let result = null;
        function dfs(node, depth) {
            if (!node) return false;
            if (depth > maxDepth) {
                maxDepth = depth;
                result = node;
            }
            let left = dfs(node.left, depth + 1);
            let right = dfs(node.right, depth + 1);
            if (left && right) {
                result = node;
                return true;
            }
            return left || right;
        }
        dfs(root, 0);
        return result;
    }
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

    function subtreeWithAllDeepest(root: TreeNode | null): TreeNode | null {
        let maxDepth = 0;
        let result: TreeNode | null = null;
        function dfs(node: TreeNode | null, depth: number): boolean {
            if (!node) return false;
            if (depth > maxDepth) {
                maxDepth = depth;
                result = node;
            }
            let left = dfs(node.left, depth + 1);
            let right = dfs(node.right, depth + 1);
            if (left && right) {
                result = node;
                return true;
            }
            return left || right;
        }
        dfs(root, 0);
        return result;
    }
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
         * @return TreeNode
         */
        function subtreeWithAllDeepest($root) {
            $maxDepth = 0;
            $result = null;
            $this->dfs($root, 0, $maxDepth, $result);
            return $result;
        }

        private function dfs($node, $depth, &$maxDepth, &$result) {
            if (!$node) return false;
            if ($depth > $maxDepth) {
                $maxDepth = $depth;
                $result = $node;
            }
            $left = $this->dfs($node->left, $depth + 1, $maxDepth, $result);
            $right = $this->dfs($node->right, $depth + 1, $maxDepth, $result);
            if ($left && $right) {
                $result = $node;
                return true;
            }
            return $left || $right;
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
        func subtreeWithAllDeepest(_ root: TreeNode?) -> TreeNode? {
            var maxDepth = 0
            var result: TreeNode?
            dfs(root, 0, &maxDepth, &result)
            return result
        }

        private func dfs(_ node: TreeNode?, _ depth: Int, _ maxDepth: inout Int, _ result: inout TreeNode?) {
            guard let node = node else { return }
            if depth > maxDepth {
                maxDepth = depth
                result = node
            }
            let left = dfs(node.left, depth + 1, &maxDepth, &result)
            let right = dfs(node.right, depth + 1, &maxDepth, &result)
            if left && right {
                result = node
                return
            }
            if left || right {
                return
            }
        }
    }
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun subtreeWithAllDeepest(root: TreeNode?): TreeNode? {
        var maxDepth = 0
        var result: TreeNode? = null
        dfs(root, 0)
        return result
        fun dfs(node: TreeNode?, depth: Int): Int {
            if (node == null) return depth
            maxDepth = maxOf(maxDepth, depth)
            val leftDepth = dfs(node.left, depth + 1)
            val rightDepth = dfs(node.right, depth + 1)
            if (leftDepth == maxDepth && rightDepth == maxDepth) {
                result = node
            }
            return maxOf(leftDepth, rightDepth)
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  TreeNode? subtreeWithAllDeepest(TreeNode? root) {
    int maxDepth = 0;
    TreeNode? result;
    dfs(root, 0);
    return result;
    int dfs(TreeNode? node, int depth) {
      if (node == null) return depth;
      maxDepth = maxDepth > depth ? maxDepth : depth;
      int leftDepth = dfs(node.left, depth + 1);
      int rightDepth = dfs(node.right, depth + 1);
      if (leftDepth == maxDepth && rightDepth == maxDepth) {
        result = node;
      }
      return max(leftDepth, rightDepth);
    }
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
func subtreeWithAllDeepest(root *TreeNode) *TreeNode {
    maxDepth := 0
    var result *TreeNode
    dfs(root, 0)
    return result
    func dfs(node *TreeNode, depth int) int {
        if node == nil {
            return depth
        }
        if depth > maxDepth {
            maxDepth = depth
        }
        leftDepth := dfs(node.Left, depth+1)
        rightDepth := dfs(node.Right, depth+1)
        if leftDepth == maxDepth && rightDepth == maxDepth {
            result = node
        }
        return max(leftDepth, rightDepth)
    }
    func max(a, b int) int {
        if a > b {
            return a
        }
        return b
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def subtree_with_all_deepest(root)
    @max_depth = 0
    @result = nil
    dfs(root, 0)
    @result
end

def dfs(node, depth)
    return depth if node.nil?
    @max_depth = [@max_depth, depth].max
    left_depth = dfs(node.left, depth + 1)
    right_depth = dfs(node.right, depth + 1)
    if left_depth == @max_depth && right_depth == @max_depth
        @result = node
    end
    [left_depth, right_depth].max
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def subtreeWithAllDeepest(root: TreeNode): TreeNode = {
        var maxDepth = 0
        var result: TreeNode = null
        dfs(root, 0)
        result
        def dfs(node: TreeNode, depth: Int): Int = {
            if (node == null) return depth
            maxDepth = math.max(maxDepth, depth)
            val leftDepth = dfs(node.left, depth + 1)
            val rightDepth = dfs(node.right, depth + 1)
            if (leftDepth == maxDepth && rightDepth == maxDepth) {
                result = node
            }
            math.max(leftDepth, rightDepth)
        }
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
    pub fn subtree_with_all_deepest(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        fn dfs(node: &Option<Rc<RefCell<TreeNode>>>) -> (i32, Option<Rc<RefCell<TreeNode>>>) {
            match node {
                None => (0, None),
                Some(node) => {
                    let node = node.borrow();
                    let (left_depth, left_ancestor) = dfs(&node.left);
                    let (right_depth, right_ancestor) = dfs(&node.right);
                    if left_depth > right_depth {
                        (left_depth + 1, left_ancestor)
                    } else if left_depth < right_depth {
                        (right_depth + 1, right_ancestor)
                    } else {
                        (left_depth + 1, Some(node.clone()))
                    }
                }
            }
        }
        dfs(&root).1
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
define/contract (subtree-with-all-deepest root)
  (-> (or/c tree-node? #f) (or/c tree-node? #f))
  (define (dfs node)
    (cond
      [(not node) (values 0 #f)]
      [else
       (let ([left-depth left-ancestor] (dfs (tree-node-left node)))
         [right-depth right-ancestor] (dfs (tree-node-right node)))
       (cond
         [(> left-depth right-depth) (values (add1 left-depth) left-ancestor)]
         [(< left-depth right-depth) (values (add1 right-depth) right-ancestor)]
         [else (values (add1 left-depth) node)]))]))
  (cdr (dfs root)))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
subtree_with_all_deepest(Root) ->
    dfs(Root).

dfs(null) -> {0, null};
dfs(#tree_node{val = Val, left = Left, right = Right}) ->
    {LeftDepth, LeftAncestor} = dfs(Left),
    {RightDepth, RightAncestor} = dfs(Right),
    if
        LeftDepth > RightDepth -> {LeftDepth + 1, LeftAncestor};
        LeftDepth < RightDepth -> {RightDepth + 1, RightAncestor};
        true -> {LeftDepth + 1, #tree_node{val = Val, left = Left, right = Right}}
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec subtree_with_all_deepest(root :: TreeNode.t | nil) :: TreeNode.t | nil
  def subtree_with_all_deepest(root) do
    dfs(root)
  end

  defp dfs(nil), do: {0, nil}

  defp dfs(%TreeNode{val: val, left: left, right: right}) do
    {left_depth, left_ancestor} = dfs(left)
    {right_depth, right_ancestor} = dfs(right)

    cond do
      left_depth > right_depth -> {left_depth + 1, left_ancestor}
      left_depth < right_depth -> {right_depth + 1, right_ancestor}
      true -> {left_depth + 1, %TreeNode{val: val, left: left, right: right}}
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** O(n) where n is the number of nodes in the tree. This is because we are performing two DFS traversals on the tree, each of which visits every node in the tree once. The time complexity is linear because we are visiting each node a constant number of times.

- **Space Complexity:** O(h) where h is the height of the tree. This is because the maximum depth of the recursive call stack is equal to the height of the tree. In the worst case, the tree is skewed to one side and the height of the tree is equal to the number of nodes in the tree, so the space complexity is O(n). However, for a balanced tree, the height of the tree is logarithmic in the number of nodes, so the space complexity is O(log n).

</div>
</details>
