---
layout: post
title: "Maximum Profit from Trading Stocks with Discounts"
date: 2025-12-16 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Dynamic Programming", "Tree", "Depth-First Search"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/maximum-profit-from-trading-stocks-with-discounts/
ai_solutions:
  - solutions:
      cpp: "#include <vector>\n#include <numeric>\n#include <algorithm>\n#include <map>\n\
        #include <functional>\n\n// Using a struct for memoization return type\nstruct\
        \ DPResult {\n    std::vector<int> dp_no_parent_bought;\n    std::vector<int>\
        \ dp_parent_bought;\n};\n\nclass Solution {\npublic:\n    std::map<int, DPResult>\
        \ memo;\n    std::vector<std::vector<int>> adj;\n    const std::vector<int>*\
        \ present_ptr;\n    const std::vector<int>* future_ptr;\n    int budget_val;\n\
        \n    DPResult dfs(int u) {\n        if (memo.count(u)) {\n            return\
        \ memo[u];\n        }\n\n        // Initialize DP arrays for current node 'u'\
        \ and its processed children.\n        // -1e9 (a large negative number) represents\
        \ -float('inf') for unreachable states.\n        // 0 for cost 0 is the base\
        \ case (don't buy anything, 0 profit, 0 cost).\n\n        std::vector<int> current_dp_u_no_buy(budget_val\
        \ + 1, -1e9);\n        current_dp_u_no_buy[0] = 0;\n\n        int cost_u_normal\
        \ = (*present_ptr)[u-1];\n        int profit_u_normal = (*future_ptr)[u-1] -\
        \ cost_u_normal;\n        std::vector<int> current_dp_u_buy_normal(budget_val\
        \ + 1, -1e9);\n        if (cost_u_normal <= budget_val) {\n            current_dp_u_buy_normal[cost_u_normal]\
        \ = profit_u_normal;\n        }\n\n        std::vector<int> current_dp_u_no_buy_if_parent_bought(budget_val\
        \ + 1, -1e9);\n        current_dp_u_no_buy_if_parent_bought[0] = 0;\n\n    \
        \    int cost_u_discount = (*present_ptr)[u-1] / 2; // Integer division is floor\
        \ for positive numbers\n        int profit_u_discount = (*future_ptr)[u-1] -\
        \ cost_u_discount;\n        std::vector<int> current_dp_u_buy_discount(budget_val\
        \ + 1, -1e9);\n        if (cost_u_discount <= budget_val) {\n            current_dp_u_buy_discount[cost_u_discount]\
        \ = profit_u_discount;\n        }\n\n        for (int v : adj[u]) {\n      \
        \      DPResult res_v = dfs(v);\n\n            auto merge_dps = [&](const std::vector<int>&\
        \ dp1, const std::vector<int>& dp2) {\n                std::vector<int> new_dp(budget_val\
        \ + 1, -1e9);\n                for (int k1 = 0; k1 <= budget_val; ++k1) {\n\
        \                    if (dp1[k1] == -1e9) continue;\n                    for\
        \ (int k2 = 0; k1 + k2 <= budget_val; ++k2) {\n                        if (dp2[k2]\
        \ == -1e9) continue;\n                        new_dp[k1 + k2] = std::max(new_dp[k1\
        \ + k2], dp1[k1] + dp2[k2]);\n                    }\n                }\n   \
        \             return new_dp;\n            };\n\n            current_dp_u_no_buy\
        \ = merge_dps(current_dp_u_no_buy, res_v.dp_no_parent_bought);\n           \
        \ current_dp_u_buy_normal = merge_dps(current_dp_u_buy_normal, res_v.dp_parent_bought);\n\
        \            current_dp_u_no_buy_if_parent_bought = merge_dps(current_dp_u_no_buy_if_parent_bought,\
        \ res_v.dp_no_parent_bought);\n            current_dp_u_buy_discount = merge_dps(current_dp_u_buy_discount,\
        \ res_v.dp_parent_bought);\n        }\n\n        std::vector<int> final_dp_no_parent_bought(budget_val\
        \ + 1, -1e9);\n        for (int k = 0; k <= budget_val; ++k) {\n           \
        \ final_dp_no_parent_bought[k] = std::max(current_dp_u_no_buy[k], current_dp_u_buy_normal[k]);\n\
        \        }\n\n        std::vector<int> final_dp_parent_bought(budget_val + 1,\
        \ -1e9);\n        for (int k = 0; k <= budget_val; ++k) {\n            final_dp_parent_bought[k]\
        \ = std::max(current_dp_u_no_buy_if_parent_bought[k], current_dp_u_buy_discount[k]);\n\
        \        }\n\n        return memo[u] = {final_dp_no_parent_bought, final_dp_parent_bought};\n\
        \    }\n\n    int maxProfit(int n, std::vector<int>& present, std::vector<int>&\
        \ future, std::vector<std::vector<int>>& hierarchy, int budget) {\n        adj.resize(n\
        \ + 1);\n        for (const auto& edge : hierarchy) {\n            adj[edge[0]].push_back(edge[1]);\n\
        \        }\n\n        present_ptr = &present;\n        future_ptr = &future;\n\
        \        budget_val = budget;\n        memo.clear();\n\n        DPResult root_res\
        \ = dfs(1);\n\n        int max_overall_profit = 0;\n        for (int profit\
        \ : root_res.dp_no_parent_bought) {\n            if (profit != -1e9) { // Check\
        \ against sentinel value\n                max_overall_profit = std::max(max_overall_profit,\
        \ profit);\n            }\n        }\n\n        return max_overall_profit;\n\
        \    }\n};"
      java: "import java.util.*;\n\nclass Solution {\n    // Using a custom class for\
        \ memoization return type\n    static class DPResult {\n        int[] dp_no_parent_bought;\n\
        \        int[] dp_parent_bought;\n\n        public DPResult(int[] dp_no_parent_bought,\
        \ int[] dp_parent_bought) {\n            this.dp_no_parent_bought = dp_no_parent_bought;\n\
        \            this.dp_parent_bought = dp_parent_bought;\n        }\n    }\n\n\
        \    Map<Integer, DPResult> memo;\n    List<List<Integer>> adj;\n    int[] present_arr;\n\
        \    int[] future_arr;\n    int budget_val;\n    static final int NEG_INF =\
        \ -1_000_000_000; // A sufficiently small number for -float('inf')\n\n    private\
        \ DPResult dfs(int u) {\n        if (memo.containsKey(u)) {\n            return\
        \ memo.get(u);\n        }\n\n        int[] current_dp_u_no_buy = new int[budget_val\
        \ + 1];\n        Arrays.fill(current_dp_u_no_buy, NEG_INF);\n        current_dp_u_no_buy[0]\
        \ = 0;\n\n        int cost_u_normal = present_arr[u-1];\n        int profit_u_normal\
        \ = future_arr[u-1] - cost_u_normal;\n        int[] current_dp_u_buy_normal\
        \ = new int[budget_val + 1];\n        Arrays.fill(current_dp_u_buy_normal, NEG_INF);\n\
        \        if (cost_u_normal <= budget_val) {\n            current_dp_u_buy_normal[cost_u_normal]\
        \ = profit_u_normal;\n        }\n\n        int[] current_dp_u_no_buy_if_parent_bought\
        \ = new int[budget_val + 1];\n        Arrays.fill(current_dp_u_no_buy_if_parent_bought,\
        \ NEG_INF);\n        current_dp_u_no_buy_if_parent_bought[0] = 0;\n\n      \
        \  int cost_u_discount = present_arr[u-1] / 2; // Integer division is floor\
        \ for positive numbers\n        int profit_u_discount = future_arr[u-1] - cost_u_discount;\n\
        \        int[] current_dp_u_buy_discount = new int[budget_val + 1];\n      \
        \  Arrays.fill(current_dp_u_buy_discount, NEG_INF);\n        if (cost_u_discount\
        \ <= budget_val) {\n            current_dp_u_buy_discount[cost_u_discount] =\
        \ profit_u_discount;\n        }\n\n        for (int v : adj.get(u)) {\n    \
        \        DPResult res_v = dfs(v);\n\n            // Helper function to merge\
        \ two DP arrays (knapsack-style combination)\n            // This is inlined\
        \ for Java to avoid creating a new lambda/method object repeatedly\n       \
        \     // or passing around DP arrays as arguments.\n\n            // Merge current_dp_u_no_buy\
        \ with res_v.dp_no_parent_bought\n            int[] next_dp_u_no_buy = new int[budget_val\
        \ + 1];\n            Arrays.fill(next_dp_u_no_buy, NEG_INF);\n            for\
        \ (int k1 = 0; k1 <= budget_val; ++k1) {\n                if (current_dp_u_no_buy[k1]\
        \ == NEG_INF) continue;\n                for (int k2 = 0; k1 + k2 <= budget_val;\
        \ ++k2) {\n                    if (res_v.dp_no_parent_bought[k2] == NEG_INF)\
        \ continue;\n                    next_dp_u_no_buy[k1 + k2] = Math.max(next_dp_u_no_buy[k1\
        \ + k2], current_dp_u_no_buy[k1] + res_v.dp_no_parent_bought[k2]);\n       \
        \         }\n            }\n            current_dp_u_no_buy = next_dp_u_no_buy;\n\
        \n            // Merge current_dp_u_buy_normal with res_v.dp_parent_bought\n\
        \            int[] next_dp_u_buy_normal = new int[budget_val + 1];\n       \
        \     Arrays.fill(next_dp_u_buy_normal, NEG_INF);\n            for (int k1 =\
        \ 0; k1 <= budget_val; ++k1) {\n                if (current_dp_u_buy_normal[k1]\
        \ == NEG_INF) continue;\n                for (int k2 = 0; k1 + k2 <= budget_val;\
        \ ++k2) {\n                    if (res_v.dp_parent_bought[k2] == NEG_INF) continue;\n\
        \                    next_dp_u_buy_normal[k1 + k2] = Math.max(next_dp_u_buy_normal[k1\
        \ + k2], current_dp_u_buy_normal[k1] + res_v.dp_parent_bought[k2]);\n      \
        \          }\n            }\n            current_dp_u_buy_normal = next_dp_u_buy_normal;\n\
        \n            // Merge current_dp_u_no_buy_if_parent_bought with res_v.dp_no_parent_bought\n\
        \            int[] next_dp_u_no_buy_if_parent_bought = new int[budget_val +\
        \ 1];\n            Arrays.fill(next_dp_u_no_buy_if_parent_bought, NEG_INF);\n\
        \            for (int k1 = 0; k1 <= budget_val; ++k1) {\n                if\
        \ (current_dp_u_no_buy_if_parent_bought[k1] == NEG_INF) continue;\n        \
        \        for (int k2 = 0; k1 + k2 <= budget_val; ++k2) {\n                 \
        \   if (res_v.dp_no_parent_bought[k2] == NEG_INF) continue;\n              \
        \      next_dp_u_no_buy_if_parent_bought[k1 + k2] = Math.max(next_dp_u_no_buy_if_parent_bought[k1\
        \ + k2], current_dp_u_no_buy_if_parent_bought[k1] + res_v.dp_no_parent_bought[k2]);\n\
        \                }\n            }\n            current_dp_u_no_buy_if_parent_bought\
        \ = next_dp_u_no_buy_if_parent_bought;\n\n            // Merge current_dp_u_buy_discount\
        \ with res_v.dp_parent_bought\n            int[] next_dp_u_buy_discount = new\
        \ int[budget_val + 1];\n            Arrays.fill(next_dp_u_buy_discount, NEG_INF);\n\
        \            for (int k1 = 0; k1 <= budget_val; ++k1) {\n                if\
        \ (current_dp_u_buy_discount[k1] == NEG_INF) continue;\n                for\
        \ (int k2 = 0; k1 + k2 <= budget_val; ++k2) {\n                    if (res_v.dp_parent_bought[k2]\
        \ == NEG_INF) continue;\n                    next_dp_u_buy_discount[k1 + k2]\
        \ = Math.max(next_dp_u_buy_discount[k1 + k2], current_dp_u_buy_discount[k1]\
        \ + res_v.dp_parent_bought[k2]);\n                }\n            }\n       \
        \     current_dp_u_buy_discount = next_dp_u_buy_discount;\n        }\n\n   \
        \     int[] final_dp_no_parent_bought = new int[budget_val + 1];\n        Arrays.fill(final_dp_no_parent_bought,\
        \ NEG_INF);\n        for (int k = 0; k <= budget_val; ++k) {\n            final_dp_no_parent_bought[k]\
        \ = Math.max(current_dp_u_no_buy[k], current_dp_u_buy_normal[k]);\n        }\n\
        \n        int[] final_dp_parent_bought = new int[budget_val + 1];\n        Arrays.fill(final_dp_parent_bought,\
        \ NEG_INF);\n        for (int k = 0; k <= budget_val; ++k) {\n            final_dp_parent_bought[k]\
        \ = Math.max(current_dp_u_no_buy_if_parent_bought[k], current_dp_u_buy_discount[k]);\n\
        \        }\n\n        DPResult result = new DPResult(final_dp_no_parent_bought,\
        \ final_dp_parent_bought);\n        memo.put(u, result);\n        return result;\n\
        \    }\n\n    public int maxProfit(int n, int[] present, int[] future, int[][]\
        \ hierarchy, int budget) {\n        adj = new ArrayList<>();\n        for (int\
        \ i = 0; i <= n; ++i) {\n            adj.add(new ArrayList<>());\n        }\n\
        \        for (int[] edge : hierarchy) {\n            adj.get(edge[0]).add(edge[1]);\n\
        \        }\n\n        present_arr = present;\n        future_arr = future;\n\
        \        budget_val = budget;\n        memo = new HashMap<>();\n\n        DPResult\
        \ root_res = dfs(1);\n\n        int max_overall_profit = 0;\n        for (int\
        \ profit : root_res.dp_no_parent_bought) {\n            if (profit != NEG_INF)\
        \ {\n                max_overall_profit = Math.max(max_overall_profit, profit);\n\
        \            }\n        }\n\n        return max_overall_profit;\n    }\n}"
      python: "import collections\n\nclass Solution:\n    def maxProfit(self, n: int,\
        \ present: List[int], future: List[int], hierarchy: List[List[int]], budget:\
        \ int) -> int:\n        adj = collections.defaultdict(list)\n        for u,\
        \ v in hierarchy:\n            adj[u].append(v)\n\n        memo = {}\n\n   \
        \     # dfs(u) returns a tuple of two lists:\n        # 1. dp_no_parent_bought:\
        \ max profit in subtree u for each budget k, assuming u's parent did NOT buy.\n\
        \        # 2. dp_parent_bought: max profit in subtree u for each budget k, assuming\
        \ u's parent DID buy.\n        # Each list is of size (budget + 1).\n      \
        \  # Values are initialized to -float('inf') for unreachable states, and 0 for\
        \ cost 0.\n        def dfs(u):\n            if u in memo:\n                return\
        \ memo[u]\n\n            # These DP arrays will store the maximum profit for\
        \ node 'u' and its already processed children.\n            # They are initialized\
        \ to reflect only 'u's decision (or lack thereof).\n\n            # Scenario\
        \ 1: u's parent did NOT buy their stock.\n            #   Option A: u does NOT\
        \ buy its own stock.\n            #     Cost: 0, Profit: 0.\n            # \
        \    Children will be processed assuming u did NOT buy (so they will use their\
        \ 'no_parent_bought' state).\n            current_dp_u_no_buy = [-float('inf')]\
        \ * (budget + 1)\n            current_dp_u_no_buy[0] = 0\n\n            #  \
        \ Option B: u BUYS its own stock at normal price.\n            #     Cost: present[u-1],\
        \ Profit: future[u-1] - present[u-1].\n            #     Children will be processed\
        \ assuming u DID buy (so they will use their 'parent_bought' state).\n     \
        \       cost_u_normal = present[u-1]\n            profit_u_normal = future[u-1]\
        \ - cost_u_normal\n            current_dp_u_buy_normal = [-float('inf')] * (budget\
        \ + 1)\n            if cost_u_normal <= budget:\n                current_dp_u_buy_normal[cost_u_normal]\
        \ = profit_u_normal\n\n            # Scenario 2: u's parent DID buy their stock.\n\
        \            #   Option A: u does NOT buy its own stock.\n            #    \
        \ Cost: 0, Profit: 0.\n            #     Children will be processed assuming\
        \ u did NOT buy (so they will use their 'no_parent_bought' state).\n       \
        \     #     This is conceptually similar to current_dp_u_no_buy, but kept separate\
        \ for clarity in merging.\n            current_dp_u_no_buy_if_parent_bought\
        \ = [-float('inf')] * (budget + 1)\n            current_dp_u_no_buy_if_parent_bought[0]\
        \ = 0\n\n            #   Option B: u BUYS its own stock at discounted price.\n\
        \            #     Cost: floor(present[u-1] / 2), Profit: future[u-1] - floor(present[u-1]\
        \ / 2).\n            #     Children will be processed assuming u DID buy (so\
        \ they will use their 'parent_bought' state).\n            cost_u_discount =\
        \ present[u-1] // 2\n            profit_u_discount = future[u-1] - cost_u_discount\n\
        \            current_dp_u_buy_discount = [-float('inf')] * (budget + 1)\n  \
        \          if cost_u_discount <= budget:\n                current_dp_u_buy_discount[cost_u_discount]\
        \ = profit_u_discount\n\n            # Iterate through each child 'v' of 'u'\
        \ and merge their DP results.\n            for v in adj[u]:\n              \
        \  # Recursively get DP results for child 'v'\n                res_v_no_parent_bought,\
        \ res_v_parent_bought = dfs(v)\n\n                # Helper function to merge\
        \ two DP arrays (knapsack-style combination)\n                def merge_dps(dp1,\
        \ dp2):\n                    new_dp = [-float('inf')] * (budget + 1)\n     \
        \               for k1 in range(budget + 1):\n                        if dp1[k1]\
        \ == -float('inf'):\n                            continue\n                \
        \        for k2 in range(budget - k1 + 1):\n                            if dp2[k2]\
        \ == -float('inf'):\n                                continue\n            \
        \                new_dp[k1 + k2] = max(new_dp[k1 + k2], dp1[k1] + dp2[k2])\n\
        \                    return new_dp\n\n                # Update current_dp_u_no_buy:\
        \ u did not buy, so v also does not get discount from u.\n                current_dp_u_no_buy\
        \ = merge_dps(current_dp_u_no_buy, res_v_no_parent_bought)\n\n             \
        \   # Update current_dp_u_buy_normal: u bought normally, so v gets discount\
        \ from u.\n                current_dp_u_buy_normal = merge_dps(current_dp_u_buy_normal,\
        \ res_v_parent_bought)\n\n                # Update current_dp_u_no_buy_if_parent_bought:\
        \ u's parent bought, but u did not buy,\n                # so v does not get\
        \ discount from u.\n                current_dp_u_no_buy_if_parent_bought = merge_dps(current_dp_u_no_buy_if_parent_bought,\
        \ res_v_no_parent_bought)\n\n                # Update current_dp_u_buy_discount:\
        \ u's parent bought, and u bought discounted,\n                # so v gets discount\
        \ from u.\n                current_dp_u_buy_discount = merge_dps(current_dp_u_buy_discount,\
        \ res_v_parent_bought)\n\n            # After processing all children, combine\
        \ the options for 'u' itself.\n\n            # Final DP for when u's parent\
        \ did NOT buy:\n            # u can either not buy (current_dp_u_no_buy) or\
        \ buy normally (current_dp_u_buy_normal).\n            final_dp_no_parent_bought\
        \ = [-float('inf')] * (budget + 1)\n            for k in range(budget + 1):\n\
        \                final_dp_no_parent_bought[k] = max(current_dp_u_no_buy[k],\
        \ current_dp_u_buy_normal[k])\n\n            # Final DP for when u's parent\
        \ DID buy:\n            # u can either not buy (current_dp_u_no_buy_if_parent_bought)\
        \ or buy discounted (current_dp_u_buy_discount).\n            final_dp_parent_bought\
        \ = [-float('inf')] * (budget + 1)\n            for k in range(budget + 1):\n\
        \                final_dp_parent_bought[k] = max(current_dp_u_no_buy_if_parent_bought[k],\
        \ current_dp_u_buy_discount[k])\n\n            memo[u] = (final_dp_no_parent_bought,\
        \ final_dp_parent_bought)\n            return final_dp_no_parent_bought, final_dp_parent_bought\n\
        \n        # Employee 1 is the CEO and has no parent, so we use the 'no_parent_bought'\
        \ state for the root.\n        final_dp_root_no_parent_bought, _ = dfs(1)\n\n\
        \        # The maximum profit is the maximum value in the resulting DP array.\n\
        \        # If no profitable trades can be made within the budget, the profit\
        \ is 0.\n        max_overall_profit = 0\n        for profit in final_dp_root_no_parent_bought:\n\
        \            if profit != -float('inf'):\n                max_overall_profit\
        \ = max(max_overall_profit, profit)\n\n        return max_overall_profit"
      python3: "import collections\n\nclass Solution:\n    def maxProfit(self, n: int,\
        \ present: List[int], future: List[int], hierarchy: List[List[int]], budget:\
        \ int) -> int:\n        adj = collections.defaultdict(list)\n        for u,\
        \ v in hierarchy:\n            adj[u].append(v)\n\n        memo = {}\n\n   \
        \     # dfs(u) returns a tuple of two lists:\n        # 1. dp_no_parent_bought:\
        \ max profit in subtree u for each budget k, assuming u's parent did NOT buy.\n\
        \        # 2. dp_parent_bought: max profit in subtree u for each budget k, assuming\
        \ u's parent DID buy.\n        # Each list is of size (budget + 1).\n      \
        \  # Values are initialized to -float('inf') for unreachable states, and 0 for\
        \ cost 0.\n        def dfs(u):\n            if u in memo:\n                return\
        \ memo[u]\n\n            # These DP arrays will store the maximum profit for\
        \ node 'u' and its already processed children.\n            # They are initialized\
        \ to reflect only 'u's decision (or lack thereof).\n\n            # Scenario\
        \ 1: u's parent did NOT buy their stock.\n            #   Option A: u does NOT\
        \ buy its own stock.\n            #     Cost: 0, Profit: 0.\n            # \
        \    Children will be processed assuming u did NOT buy (so they will use their\
        \ 'no_parent_bought' state).\n            current_dp_u_no_buy = [-float('inf')]\
        \ * (budget + 1)\n            current_dp_u_no_buy[0] = 0\n\n            #  \
        \ Option B: u BUYS its own stock at normal price.\n            #     Cost: present[u-1],\
        \ Profit: future[u-1] - present[u-1].\n            #     Children will be processed\
        \ assuming u DID buy (so they will use their 'parent_bought' state).\n     \
        \       cost_u_normal = present[u-1]\n            profit_u_normal = future[u-1]\
        \ - cost_u_normal\n            current_dp_u_buy_normal = [-float('inf')] * (budget\
        \ + 1)\n            if cost_u_normal <= budget:\n                current_dp_u_buy_normal[cost_u_normal]\
        \ = profit_u_normal\n\n            # Scenario 2: u's parent DID buy their stock.\n\
        \            #   Option A: u does NOT buy its own stock.\n            #    \
        \ Cost: 0, Profit: 0.\n            #     Children will be processed assuming\
        \ u did NOT buy (so they will use their 'no_parent_bought' state).\n       \
        \     #     This is conceptually similar to current_dp_u_no_buy, but kept separate\
        \ for clarity in merging.\n            current_dp_u_no_buy_if_parent_bought\
        \ = [-float('inf')] * (budget + 1)\n            current_dp_u_no_buy_if_parent_bought[0]\
        \ = 0\n\n            #   Option B: u BUYS its own stock at discounted price.\n\
        \            #     Cost: floor(present[u-1] / 2), Profit: future[u-1] - floor(present[u-1]\
        \ / 2).\n            #     Children will be processed assuming u DID buy (so\
        \ they will use their 'parent_bought' state).\n            cost_u_discount =\
        \ present[u-1] // 2\n            profit_u_discount = future[u-1] - cost_u_discount\n\
        \            current_dp_u_buy_discount = [-float('inf')] * (budget + 1)\n  \
        \          if cost_u_discount <= budget:\n                current_dp_u_buy_discount[cost_u_discount]\
        \ = profit_u_discount\n\n            # Iterate through each child 'v' of 'u'\
        \ and merge their DP results.\n            for v in adj[u]:\n              \
        \  # Recursively get DP results for child 'v'\n                res_v_no_parent_bought,\
        \ res_v_parent_bought = dfs(v)\n\n                # Helper function to merge\
        \ two DP arrays (knapsack-style combination)\n                def merge_dps(dp1,\
        \ dp2):\n                    new_dp = [-float('inf')] * (budget + 1)\n     \
        \               for k1 in range(budget + 1):\n                        if dp1[k1]\
        \ == -float('inf'):\n                            continue\n                \
        \        for k2 in range(budget - k1 + 1):\n                            if dp2[k2]\
        \ == -float('inf'):\n                                continue\n            \
        \                new_dp[k1 + k2] = max(new_dp[k1 + k2], dp1[k1] + dp2[k2])\n\
        \                    return new_dp\n\n                # Update current_dp_u_no_buy:\
        \ u did not buy, so v also does not get discount from u.\n                current_dp_u_no_buy\
        \ = merge_dps(current_dp_u_no_buy, res_v_no_parent_bought)\n\n             \
        \   # Update current_dp_u_buy_normal: u bought normally, so v gets discount\
        \ from u.\n                current_dp_u_buy_normal = merge_dps(current_dp_u_buy_normal,\
        \ res_v_parent_bought)\n\n                # Update current_dp_u_no_buy_if_parent_bought:\
        \ u's parent bought, but u did not buy,\n                # so v does not get\
        \ discount from u.\n                current_dp_u_no_buy_if_parent_bought = merge_dps(current_dp_u_no_buy_if_parent_bought,\
        \ res_v_no_parent_bought)\n\n                # Update current_dp_u_buy_discount:\
        \ u's parent bought, and u bought discounted,\n                # so v gets discount\
        \ from u.\n                current_dp_u_buy_discount = merge_dps(current_dp_u_buy_discount,\
        \ res_v_parent_bought)\n\n            # After processing all children, combine\
        \ the options for 'u' itself.\n\n            # Final DP for when u's parent\
        \ did NOT buy:\n            # u can either not buy (current_dp_u_no_buy) or\
        \ buy normally (current_dp_u_buy_normal).\n            final_dp_no_parent_bought\
        \ = [-float('inf')] * (budget + 1)\n            for k in range(budget + 1):\n\
        \                final_dp_no_parent_bought[k] = max(current_dp_u_no_buy[k],\
        \ current_dp_u_buy_normal[k])\n\n            # Final DP for when u's parent\
        \ DID buy:\n            # u can either not buy (current_dp_u_no_buy_if_parent_bought)\
        \ or buy discounted (current_dp_u_buy_discount).\n            final_dp_parent_bought\
        \ = [-float('inf')] * (budget + 1)\n            for k in range(budget + 1):\n\
        \                final_dp_parent_bought[k] = max(current_dp_u_no_buy_if_parent_bought[k],\
        \ current_dp_u_buy_discount[k])\n\n            memo[u] = (final_dp_no_parent_bought,\
        \ final_dp_parent_bought)\n            return final_dp_no_parent_bought, final_dp_parent_bought\n\
        \n        # Employee 1 is the CEO and has no parent, so we use the 'no_parent_bought'\
        \ state for the root.\n        final_dp_root_no_parent_bought, _ = dfs(1)\n\n\
        \        # The maximum profit is the maximum value in the resulting DP array.\n\
        \        # If no profitable trades can be made within the budget, the profit\
        \ is 0.\n        max_overall_profit = 0\n        for profit in final_dp_root_no_parent_bought:\n\
        \            if profit != -float('inf'):\n                max_overall_profit\
        \ = max(max_overall_profit, profit)\n\n        return max_overall_profit"
      c: "#include <stdlib.h>\n#include <stdio.h>\n#include <string.h>\n#include <limits.h>\n\
        \n#define NEG_INF INT_MIN / 2 // Use INT_MIN/2 to avoid overflow issues with\
        \ addition\n\n// Structure to hold DP results for a subtree\ntypedef struct\
        \ {\n    int* dp_no_parent_bought;\n    int* dp_parent_bought;\n} DPResult;\n\
        \n// Adjacency list for the hierarchy\nint** adj;\nint* adj_sizes;\n\n// Input\
        \ arrays and budget, made global for easier access in DFS\nint* present_arr;\n\
        int* future_arr;\nint budget_val;\n\n// Memoization table (using a simple array\
        \ for fixed N, or hash map for sparse IDs)\n// For N <= 160, a 2D array for\
        \ memoization is feasible.\n// memo[u][0] stores dp_no_parent_bought, memo[u][1]\
        \ stores dp_parent_bought\nDPResult* memo_table;\nint N_val; // Store N for\
        \ memo_table size\n\n// Helper function to create and initialize a DP array\n\
        int* create_dp_array() {\n    int* dp = (int*)malloc(sizeof(int) * (budget_val\
        \ + 1));\n    for (int i = 0; i <= budget_val; ++i) {\n        dp[i] = NEG_INF;\n\
        \    }\n    return dp;\n}\n\n// Helper function to merge two DP arrays (knapsack-style\
        \ combination)\nint* merge_dps(const int* dp1, const int* dp2) {\n    int* new_dp\
        \ = create_dp_array();\n    for (int k1 = 0; k1 <= budget_val; ++k1) {\n   \
        \     if (dp1[k1] == NEG_INF) continue;\n        for (int k2 = 0; k1 + k2 <=\
        \ budget_val; ++k2) {\n            if (dp2[k2] == NEG_INF) continue;\n     \
        \       if (dp1[k1] + dp2[k2] > new_dp[k1 + k2]) {\n                new_dp[k1\
        \ + k2] = dp1[k1] + dp2[k2];\n            }\n        }\n    }\n    return new_dp;\n\
        }\n\nDPResult dfs(int u) {\n    if (memo_table[u].dp_no_parent_bought != NULL)\
        \ {\n        return memo_table[u];\n    }\n\n    int* current_dp_u_no_buy =\
        \ create_dp_array();\n    current_dp_u_no_buy[0] = 0;\n\n    int cost_u_normal\
        \ = present_arr[u-1];\n    int profit_u_normal = future_arr[u-1] - cost_u_normal;\n\
        \    int* current_dp_u_buy_normal = create_dp_array();\n    if (cost_u_normal\
        \ <= budget_val) {\n        current_dp_u_buy_normal[cost_u_normal] = profit_u_normal;\n\
        \    }\n\n    int* current_dp_u_no_buy_if_parent_bought = create_dp_array();\n\
        \    current_dp_u_no_buy_if_parent_bought[0] = 0;\n\n    int cost_u_discount\
        \ = present_arr[u-1] / 2; // Integer division is floor for positive numbers\n\
        \    int profit_u_discount = future_arr[u-1] - cost_u_discount;\n    int* current_dp_u_buy_discount\
        \ = create_dp_array();\n    if (cost_u_discount <= budget_val) {\n        current_dp_u_buy_discount[cost_u_discount]\
        \ = profit_u_discount;\n    }\n\n    for (int i = 0; i < adj_sizes[u]; ++i)\
        \ {\n        int v = adj[u][i];\n        DPResult res_v = dfs(v);\n\n      \
        \  int* next_dp;\n\n        next_dp = merge_dps(current_dp_u_no_buy, res_v.dp_no_parent_bought);\n\
        \        free(current_dp_u_no_buy); current_dp_u_no_buy = next_dp;\n\n     \
        \   next_dp = merge_dps(current_dp_u_buy_normal, res_v.dp_parent_bought);\n\
        \        free(current_dp_u_buy_normal); current_dp_u_buy_normal = next_dp;\n\
        \n        next_dp = merge_dps(current_dp_u_no_buy_if_parent_bought, res_v.dp_no_parent_bought);\n\
        \        free(current_dp_u_no_buy_if_parent_bought); current_dp_u_no_buy_if_parent_bought\
        \ = next_dp;\n\n        next_dp = merge_dps(current_dp_u_buy_discount, res_v.dp_parent_bought);\n\
        \        free(current_dp_u_buy_discount); current_dp_u_buy_discount = next_dp;\n\
        \    }\n\n    int* final_dp_no_parent_bought = create_dp_array();\n    for (int\
        \ k = 0; k <= budget_val; ++k) {\n        if (current_dp_u_no_buy[k] > final_dp_no_parent_bought[k])\
        \ {\n            final_dp_no_parent_bought[k] = current_dp_u_no_buy[k];\n  \
        \      }\n        if (current_dp_u_buy_normal[k] > final_dp_no_parent_bought[k])\
        \ {\n            final_dp_no_parent_bought[k] = current_dp_u_buy_normal[k];\n\
        \        }\n    }\n\n    int* final_dp_parent_bought = create_dp_array();\n\
        \    for (int k = 0; k <= budget_val; ++k) {\n        if (current_dp_u_no_buy_if_parent_bought[k]\
        \ > final_dp_parent_bought[k]) {\n            final_dp_parent_bought[k] = current_dp_u_no_buy_if_parent_bought[k];\n\
        \        }\n        if (current_dp_u_buy_discount[k] > final_dp_parent_bought[k])\
        \ {\n            final_dp_parent_bought[k] = current_dp_u_buy_discount[k];\n\
        \        }\n    }\n\n    // Free temporary DP arrays\n    free(current_dp_u_no_buy);\n\
        \    free(current_dp_u_buy_normal);\n    free(current_dp_u_no_buy_if_parent_bought);\n\
        \    free(current_dp_u_buy_discount);\n\n    memo_table[u].dp_no_parent_bought\
        \ = final_dp_no_parent_bought;\n    memo_table[u].dp_parent_bought = final_dp_parent_bought;\n\
        \    return memo_table[u];\n}\n\nint maxProfit(int n, int* present, int* future,\
        \ int hierarchy_rows, int* hierarchy_cols, int** hierarchy, int budget) {\n\
        \    N_val = n;\n    adj = (int**)malloc(sizeof(int*) * (n + 1));\n    adj_sizes\
        \ = (int*)calloc(n + 1, sizeof(int)); // Initialize to 0\n    int* temp_adj_capacity\
        \ = (int*)calloc(n + 1, sizeof(int)); // For dynamic resizing\n\n    // First\
        \ pass to count children for each node to allocate memory\n    for (int i =\
        \ 0; i < hierarchy_rows; ++i) {\n        int u = hierarchy[i][0];\n        adj_sizes[u]++;\n\
        \    }\n\n    // Allocate memory for adjacency lists\n    for (int i = 1; i\
        \ <= n; ++i) {\n        adj[i] = (int*)malloc(sizeof(int) * adj_sizes[i]);\n\
        \        adj_sizes[i] = 0; // Reset to use as current index during second pass\n\
        \    }\n\n    // Second pass to populate adjacency lists\n    for (int i = 0;\
        \ i < hierarchy_rows; ++i) {\n        int u = hierarchy[i][0];\n        int\
        \ v = hierarchy[i][1];\n        adj[u][adj_sizes[u]++] = v;\n    }\n    free(temp_adj_capacity);\n\
        \n    present_arr = present;\n    future_arr = future;\n    budget_val = budget;\n\
        \n    memo_table = (DPResult*)calloc(n + 1, sizeof(DPResult)); // Initialize\
        \ all pointers to NULL\n\n    DPResult root_res = dfs(1);\n\n    int max_overall_profit\
        \ = 0;\n    for (int i = 0; i <= budget_val; ++i) {\n        if (root_res.dp_no_parent_bought[i]\
        \ != NEG_INF) {\n            if (root_res.dp_no_parent_bought[i] > max_overall_profit)\
        \ {\n                max_overall_profit = root_res.dp_no_parent_bought[i];\n\
        \            }\n        }\n    }\n\n    // Cleanup allocated memory\n    for\
        \ (int i = 1; i <= n; ++i) {\n        if (memo_table[i].dp_no_parent_bought\
        \ != NULL) {\n            free(memo_table[i].dp_no_parent_bought);\n       \
        \     free(memo_table[i].dp_parent_bought);\n        }\n        free(adj[i]);\n\
        \    }\n    free(adj);\n    free(adj_sizes);\n    free(memo_table);\n\n    return\
        \ max_overall_profit;\n}"
      csharp: "using System; \nusing System.Collections.Generic;\nusing System.Linq;\n\
        \npublic class Solution {\n    // Using a custom class for memoization return\
        \ type\n    public class DPResult {\n        public int[] dp_no_parent_bought;\n\
        \        public int[] dp_parent_bought;\n\n        public DPResult(int[] dp_no_parent_bought,\
        \ int[] dp_parent_bought) {\n            this.dp_no_parent_bought = dp_no_parent_bought;\n\
        \            this.dp_parent_bought = dp_parent_bought;\n        }\n    }\n\n\
        \    private Dictionary<int, DPResult> memo;\n    private List<List<int>> adj;\n\
        \    private int[] present_arr;\n    private int[] future_arr;\n    private\
        \ int budget_val;\n    private const int NEG_INF = -1_000_000_000; // A sufficiently\
        \ small number for -float('inf')\n\n    private DPResult Dfs(int u) {\n    \
        \    if (memo.ContainsKey(u)) {\n            return memo[u];\n        }\n\n\
        \        int[] current_dp_u_no_buy = new int[budget_val + 1];\n        Array.Fill(current_dp_u_no_buy,\
        \ NEG_INF);\n        current_dp_u_no_buy[0] = 0;\n\n        int cost_u_normal\
        \ = present_arr[u-1];\n        int profit_u_normal = future_arr[u-1] - cost_u_normal;\n\
        \        int[] current_dp_u_buy_normal = new int[budget_val + 1];\n        Array.Fill(current_dp_u_buy_normal,\
        \ NEG_INF);\n        if (cost_u_normal <= budget_val) {\n            current_dp_u_buy_normal[cost_u_normal]\
        \ = profit_u_normal;\n        }\n\n        int[] current_dp_u_no_buy_if_parent_bought\
        \ = new int[budget_val + 1];\n        Array.Fill(current_dp_u_no_buy_if_parent_bought,\
        \ NEG_INF);\n        current_dp_u_no_buy_if_parent_bought[0] = 0;\n\n      \
        \  int cost_u_discount = present_arr[u-1] / 2; // Integer division is floor\
        \ for positive numbers\n        int profit_u_discount = future_arr[u-1] - cost_u_discount;\n\
        \        int[] current_dp_u_buy_discount = new int[budget_val + 1];\n      \
        \  Array.Fill(current_dp_u_buy_discount, NEG_INF);\n        if (cost_u_discount\
        \ <= budget_val) {\n            current_dp_u_buy_discount[cost_u_discount] =\
        \ profit_u_discount;\n        }\n\n        foreach (int v in adj[u]) {\n   \
        \         DPResult res_v = Dfs(v);\n\n            // Helper function to merge\
        \ two DP arrays (knapsack-style combination)\n            // Inlined for C#\
        \ to avoid creating new delegates/methods repeatedly.\n\n            // Merge\
        \ current_dp_u_no_buy with res_v.dp_no_parent_bought\n            int[] next_dp_u_no_buy\
        \ = new int[budget_val + 1];\n            Array.Fill(next_dp_u_no_buy, NEG_INF);\n\
        \            for (int k1 = 0; k1 <= budget_val; ++k1) {\n                if\
        \ (current_dp_u_no_buy[k1] == NEG_INF) continue;\n                for (int k2\
        \ = 0; k1 + k2 <= budget_val; ++k2) {\n                    if (res_v.dp_no_parent_bought[k2]\
        \ == NEG_INF) continue;\n                    next_dp_u_no_buy[k1 + k2] = Math.Max(next_dp_u_no_buy[k1\
        \ + k2], current_dp_u_no_buy[k1] + res_v.dp_no_parent_bought[k2]);\n       \
        \         }\n            }\n            current_dp_u_no_buy = next_dp_u_no_buy;\n\
        \n            // Merge current_dp_u_buy_normal with res_v.dp_parent_bought\n\
        \            int[] next_dp_u_buy_normal = new int[budget_val + 1];\n       \
        \     Array.Fill(next_dp_u_buy_normal, NEG_INF);\n            for (int k1 =\
        \ 0; k1 <= budget_val; ++k1) {\n                if (current_dp_u_buy_normal[k1]\
        \ == NEG_INF) continue;\n                for (int k2 = 0; k1 + k2 <= budget_val;\
        \ ++k2) {\n                    if (res_v.dp_parent_bought[k2] == NEG_INF) continue;\n\
        \                    next_dp_u_buy_normal[k1 + k2] = Math.Max(next_dp_u_buy_normal[k1\
        \ + k2], current_dp_u_buy_normal[k1] + res_v.dp_parent_bought[k2]);\n      \
        \          }\n            }\n            current_dp_u_buy_normal = next_dp_u_buy_normal;\n\
        \n            // Merge current_dp_u_no_buy_if_parent_bought with res_v.dp_no_parent_bought\n\
        \            int[] next_dp_u_no_buy_if_parent_bought = new int[budget_val +\
        \ 1];\n            Array.Fill(next_dp_u_no_buy_if_parent_bought, NEG_INF);\n\
        \            for (int k1 = 0; k1 <= budget_val; ++k1) {\n                if\
        \ (current_dp_u_no_buy_if_parent_bought[k1] == NEG_INF) continue;\n        \
        \        for (int k2 = 0; k1 + k2 <= budget_val; ++k2) {\n                 \
        \   if (res_v.dp_no_parent_bought[k2] == NEG_INF) continue;\n              \
        \      next_dp_u_no_buy_if_parent_bought[k1 + k2] = Math.Max(next_dp_u_no_buy_if_parent_bought[k1\
        \ + k2], current_dp_u_no_buy_if_parent_bought[k1] + res_v.dp_no_parent_bought[k2]);\n\
        \                }\n            }\n            current_dp_u_no_buy_if_parent_bought\
        \ = next_dp_u_no_buy_if_parent_bought;\n\n            // Merge current_dp_u_buy_discount\
        \ with res_v.dp_parent_bought\n            int[] next_dp_u_buy_discount = new\
        \ int[budget_val + 1];\n            Array.Fill(next_dp_u_buy_discount, NEG_INF);\n\
        \            for (int k1 = 0; k1 <= budget_val; ++k1) {\n                if\
        \ (current_dp_u_buy_discount[k1] == NEG_INF) continue;\n                for\
        \ (int k2 = 0; k1 + k2 <= budget_val; ++k2) {\n                    if (res_v.dp_parent_bought[k2]\
        \ == NEG_INF) continue;\n                    next_dp_u_buy_discount[k1 + k2]\
        \ = Math.Max(next_dp_u_buy_discount[k1 + k2], current_dp_u_buy_discount[k1]\
        \ + res_v.dp_parent_bought[k2]);\n                }\n            }\n       \
        \     current_dp_u_buy_discount = next_dp_u_buy_discount;\n        }\n\n   \
        \     int[] final_dp_no_parent_bought = new int[budget_val + 1];\n        Array.Fill(final_dp_no_parent_bought,\
        \ NEG_INF);\n        for (int k = 0; k <= budget_val; ++k) {\n            final_dp_no_parent_bought[k]\
        \ = Math.Max(current_dp_u_no_buy[k], current_dp_u_buy_normal[k]);\n        }\n\
        \n        int[] final_dp_parent_bought = new int[budget_val + 1];\n        Array.Fill(final_dp_parent_bought,\
        \ NEG_INF);\n        for (int k = 0; k <= budget_val; ++k) {\n            final_dp_parent_bought[k]\
        \ = Math.Max(current_dp_u_no_buy_if_parent_bought[k], current_dp_u_buy_discount[k]);\n\
        \        }\n\n        DPResult result = new DPResult(final_dp_no_parent_bought,\
        \ final_dp_parent_bought);\n        memo.Add(u, result);\n        return result;\n\
        \    }\n\n    public int MaxProfit(int n, int[] present, int[] future, int[][]\
        \ hierarchy, int budget) {\n        adj = new List<List<int>>();\n        for\
        \ (int i = 0; i <= n; ++i) {\n            adj.Add(new List<int>());\n      \
        \  }\n        foreach (int[] edge in hierarchy) {\n            adj[edge[0]].Add(edge[1]);\n\
        \        }\n\n        present_arr = present;\n        future_arr = future;\n\
        \        budget_val = budget;\n        memo = new Dictionary<int, DPResult>();\n\
        \n        DPResult root_res = Dfs(1);\n\n        int max_overall_profit = 0;\n\
        \        foreach (int profit in root_res.dp_no_parent_bought) {\n          \
        \  if (profit != NEG_INF) {\n                max_overall_profit = Math.Max(max_overall_profit,\
        \ profit);\n            }\n        }\n\n        return max_overall_profit;\n\
        \    }\n}"
      javascript: "/**\n * @param {number} n\n * @param {number[]} present\n * @param\
        \ {number[]} future\n * @param {number[][]} hierarchy\n * @param {number} budget\n\
        \ * @return {number}\n */\nvar maxProfit = function(n, present, future, hierarchy,\
        \ budget) {\n    const adj = new Array(n + 1).fill(0).map(() => []);\n    for\
        \ (const [u, v] of hierarchy) {\n        adj[u].push(v);\n    }\n\n    const\
        \ memo = new Map();\n    const NEG_INF = -Infinity;\n\n    // dfs(u) returns\
        \ an object with two arrays:\n    // { dp_no_parent_bought, dp_parent_bought\
        \ }\n    const dfs = (u) => {\n        if (memo.has(u)) {\n            return\
        \ memo.get(u);\n        }\n\n        // Initialize DP arrays for current node\
        \ 'u' and its processed children.\n        // They are initialized to reflect\
        \ only 'u's decision (or lack thereof).\n\n        // Scenario 1: u's parent\
        \ did NOT buy their stock.\n        //   Option A: u does NOT buy its own stock.\n\
        \        //     Cost: 0, Profit: 0.\n        //     Children will be processed\
        \ assuming u did NOT buy (so they will use their 'no_parent_bought' state).\n\
        \        let current_dp_u_no_buy = new Array(budget + 1).fill(NEG_INF);\n  \
        \      current_dp_u_no_buy[0] = 0;\n\n        //   Option B: u BUYS its own\
        \ stock at normal price.\n        //     Cost: present[u-1], Profit: future[u-1]\
        \ - present[u-1].\n        //     Children will be processed assuming u DID\
        \ buy (so they will use their 'parent_bought' state).\n        const cost_u_normal\
        \ = present[u-1];\n        const profit_u_normal = future[u-1] - cost_u_normal;\n\
        \        let current_dp_u_buy_normal = new Array(budget + 1).fill(NEG_INF);\n\
        \        if (cost_u_normal <= budget) {\n            current_dp_u_buy_normal[cost_u_normal]\
        \ = profit_u_normal;\n        }\n\n        // Scenario 2: u's parent DID buy\
        \ their stock.\n        //   Option A: u does NOT buy its own stock.\n     \
        \   //     Cost: 0, Profit: 0.\n        //     Children will be processed assuming\
        \ u did NOT buy (so they will use their 'no_parent_bought' state).\n       \
        \ let current_dp_u_no_buy_if_parent_bought = new Array(budget + 1).fill(NEG_INF);\n\
        \        current_dp_u_no_buy_if_parent_bought[0] = 0;\n\n        //   Option\
        \ B: u BUYS its own stock at discounted price.\n        //     Cost: Math.floor(present[u-1]\
        \ / 2), Profit: future[u-1] - Math.floor(present[u-1] / 2).\n        //    \
        \ Children will be processed assuming u DID buy (so they will use their 'parent_bought'\
        \ state).\n        const cost_u_discount = Math.floor(present[u-1] / 2);\n \
        \       const profit_u_discount = future[u-1] - cost_u_discount;\n        let\
        \ current_dp_u_buy_discount = new Array(budget + 1).fill(NEG_INF);\n       \
        \ if (cost_u_discount <= budget) {\n            current_dp_u_buy_discount[cost_u_discount]\
        \ = profit_u_discount;\n        }\n\n        // Helper function to merge two\
        \ DP arrays (knapsack-style combination)\n        const mergeDps = (dp1, dp2)\
        \ => {\n            const new_dp = new Array(budget + 1).fill(NEG_INF);\n  \
        \          for (let k1 = 0; k1 <= budget; ++k1) {\n                if (dp1[k1]\
        \ === NEG_INF) {\n                    continue;\n                }\n       \
        \         for (let k2 = 0; k1 + k2 <= budget; ++k2) {\n                    if\
        \ (dp2[k2] === NEG_INF) {\n                        continue;\n             \
        \       }\n                    new_dp[k1 + k2] = Math.max(new_dp[k1 + k2], dp1[k1]\
        \ + dp2[k2]);\n                }\n            }\n            return new_dp;\n\
        \        };\n\n        // Iterate through each child 'v' of 'u' and merge their\
        \ DP results.\n        for (const v of adj[u]) {\n            // Recursively\
        \ get DP results for child 'v'\n            const { dp_no_parent_bought: res_v_no_parent_bought,\
        \ dp_parent_bought: res_v_parent_bought } = dfs(v);\n\n            // Update\
        \ current_dp_u_no_buy: u did not buy, so v also does not get discount from u.\n\
        \            current_dp_u_no_buy = mergeDps(current_dp_u_no_buy, res_v_no_parent_bought);\n\
        \n            // Update current_dp_u_buy_normal: u bought normally, so v gets\
        \ discount from u.\n            current_dp_u_buy_normal = mergeDps(current_dp_u_buy_normal,\
        \ res_v_parent_bought);\n\n            // Update current_dp_u_no_buy_if_parent_bought:\
        \ u's parent bought, but u did not buy,\n            // so v does not get discount\
        \ from u.\n            current_dp_u_no_buy_if_parent_bought = mergeDps(current_dp_u_no_buy_if_parent_bought,\
        \ res_v_no_parent_bought);\n\n            // Update current_dp_u_buy_discount:\
        \ u's parent bought, and u bought discounted,\n            // so v gets discount\
        \ from u.\n            current_dp_u_buy_discount = mergeDps(current_dp_u_buy_discount,\
        \ res_v_parent_bought);\n        }\n\n        // After processing all children,\
        \ combine the options for 'u' itself.\n\n        // Final DP for when u's parent\
        \ did NOT buy:\n        // u can either not buy (current_dp_u_no_buy) or buy\
        \ normally (current_dp_u_buy_normal).\n        const final_dp_no_parent_bought\
        \ = new Array(budget + 1).fill(NEG_INF);\n        for (let k = 0; k <= budget;\
        \ ++k) {\n            final_dp_no_parent_bought[k] = Math.max(current_dp_u_no_buy[k],\
        \ current_dp_u_buy_normal[k]);\n        }\n\n        // Final DP for when u's\
        \ parent DID buy:\n        // u can either not buy (current_dp_u_no_buy_if_parent_bought)\
        \ or buy discounted (current_dp_u_buy_discount).\n        const final_dp_parent_bought\
        \ = new Array(budget + 1).fill(NEG_INF);\n        for (let k = 0; k <= budget;\
        \ ++k) {\n            final_dp_parent_bought[k] = Math.max(current_dp_u_no_buy_if_parent_bought[k],\
        \ current_dp_u_buy_discount[k]);\n        }\n\n        const result = { dp_no_parent_bought:\
        \ final_dp_no_parent_bought, dp_parent_bought: final_dp_parent_bought };\n \
        \       memo.set(u, result);\n        return result;\n    };\n\n    // Employee\
        \ 1 is the CEO and has no parent, so we use the 'no_parent_bought' state for\
        \ the root.\n    const { dp_no_parent_bought: final_dp_root_no_parent_bought\
        \ } = dfs(1);\n\n    // The maximum profit is the maximum value in the resulting\
        \ DP array.\n    // If no profitable trades can be made within the budget, the\
        \ profit is 0.\n    let max_overall_profit = 0;\n    for (const profit of final_dp_root_no_parent_bought)\
        \ {\n        if (profit !== NEG_INF) {\n            max_overall_profit = Math.max(max_overall_profit,\
        \ profit);\n        }\n    }\n\n    return max_overall_profit;\n};"
      typescript: "interface DPResult {\n    dp_no_parent_bought: number[];\n    dp_parent_bought:\
        \ number[];\n}\n\nfunction maxProfit(n: number, present: number[], future: number[],\
        \ hierarchy: number[][], budget: number): number {\n    const adj: number[][]\
        \ = Array.from({ length: n + 1 }, () => []);\n    for (const [u, v] of hierarchy)\
        \ {\n        adj[u].push(v);\n    }\n\n    const memo: Map<number, DPResult>\
        \ = new Map();\n    const NEG_INF = -Infinity;\n\n    const dfs = (u: number):\
        \ DPResult => {\n        if (memo.has(u)) {\n            return memo.get(u)!;\n\
        \        }\n\n        let current_dp_u_no_buy: number[] = new Array(budget +\
        \ 1).fill(NEG_INF);\n        current_dp_u_no_buy[0] = 0;\n\n        const cost_u_normal\
        \ = present[u-1];\n        const profit_u_normal = future[u-1] - cost_u_normal;\n\
        \        let current_dp_u_buy_normal: number[] = new Array(budget + 1).fill(NEG_INF);\n\
        \        if (cost_u_normal <= budget) {\n            current_dp_u_buy_normal[cost_u_normal]\
        \ = profit_u_normal;\n        }\n\n        let current_dp_u_no_buy_if_parent_bought:\
        \ number[] = new Array(budget + 1).fill(NEG_INF);\n        current_dp_u_no_buy_if_parent_bought[0]\
        \ = 0;\n\n        const cost_u_discount = Math.floor(present[u-1] / 2);\n  \
        \      const profit_u_discount = future[u-1] - cost_u_discount;\n        let\
        \ current_dp_u_buy_discount: number[] = new Array(budget + 1).fill(NEG_INF);\n\
        \        if (cost_u_discount <= budget) {\n            current_dp_u_buy_discount[cost_u_discount]\
        \ = profit_u_discount;\n        }\n\n        const mergeDps = (dp1: number[],\
        \ dp2: number[]): number[] => {\n            const new_dp: number[] = new Array(budget\
        \ + 1).fill(NEG_INF);\n            for (let k1 = 0; k1 <= budget; ++k1) {\n\
        \                if (dp1[k1] === NEG_INF) {\n                    continue;\n\
        \                }\n                for (let k2 = 0; k1 + k2 <= budget; ++k2)\
        \ {\n                    if (dp2[k2] === NEG_INF) {\n                      \
        \  continue;\n                    }\n                    new_dp[k1 + k2] = Math.max(new_dp[k1\
        \ + k2], dp1[k1] + dp2[k2]);\n                }\n            }\n           \
        \ return new_dp;\n        };\n\n        for (const v of adj[u]) {\n        \
        \    const { dp_no_parent_bought: res_v_no_parent_bought, dp_parent_bought:\
        \ res_v_parent_bought } = dfs(v);\n\n            current_dp_u_no_buy = mergeDps(current_dp_u_no_buy,\
        \ res_v_no_parent_bought);\n            current_dp_u_buy_normal = mergeDps(current_dp_u_buy_normal,\
        \ res_v_parent_bought);\n            current_dp_u_no_buy_if_parent_bought =\
        \ mergeDps(current_dp_u_no_buy_if_parent_bought, res_v_no_parent_bought);\n\
        \            current_dp_u_buy_discount = mergeDps(current_dp_u_buy_discount,\
        \ res_v_parent_bought);\n        }\n\n        const final_dp_no_parent_bought:\
        \ number[] = new Array(budget + 1).fill(NEG_INF);\n        for (let k = 0; k\
        \ <= budget; ++k) {\n            final_dp_no_parent_bought[k] = Math.max(current_dp_u_no_buy[k],\
        \ current_dp_u_buy_normal[k]);\n        }\n\n        const final_dp_parent_bought:\
        \ number[] = new Array(budget + 1).fill(NEG_INF);\n        for (let k = 0; k\
        \ <= budget; ++k) {\n            final_dp_parent_bought[k] = Math.max(current_dp_u_no_buy_if_parent_bought[k],\
        \ current_dp_u_buy_discount[k]);\n        }\n\n        const result: DPResult\
        \ = { dp_no_parent_bought: final_dp_no_parent_bought, dp_parent_bought: final_dp_parent_bought\
        \ };\n        memo.set(u, result);\n        return result;\n    };\n\n    const\
        \ { dp_no_parent_bought: final_dp_root_no_parent_bought } = dfs(1);\n\n    let\
        \ max_overall_profit = 0;\n    for (const profit of final_dp_root_no_parent_bought)\
        \ {\n        if (profit !== NEG_INF) {\n            max_overall_profit = Math.max(max_overall_profit,\
        \ profit);\n        }\n    }\n\n    return max_overall_profit;\n}"
      php: "<?php\n\nclass Solution {\n    private $adj;\n    private $present_arr;\n\
        \    private $future_arr;\n    private $budget_val;\n    private $memo;\n  \
        \  private const NEG_INF = -1000000000; // A sufficiently small number for -float('inf')\n\
        \n    /**\n     * @param Integer $n\n     * @param Integer[] $present\n    \
        \ * @param Integer[] $future\n     * @param Integer[][] $hierarchy\n     * @param\
        \ Integer $budget\n     * @return Integer\n     */\n    function maxProfit($n,\
        \ $present, $future, $hierarchy, $budget) {\n        $this->adj = array_fill(0,\
        \ $n + 1, []);\n        foreach ($hierarchy as $edge) {\n            $u = $edge[0];\n\
        \            $v = $edge[1];\n            $this->adj[$u][] = $v;\n        }\n\
        \n        $this->present_arr = $present;\n        $this->future_arr = $future;\n\
        \        $this->budget_val = $budget;\n        $this->memo = [];\n\n       \
        \ $root_res = $this->dfs(1);\n\n        $max_overall_profit = 0;\n        foreach\
        \ ($root_res['dp_no_parent_bought'] as $profit) {\n            if ($profit !==\
        \ self::NEG_INF) {\n                $max_overall_profit = max($max_overall_profit,\
        \ $profit);\n            }\n        }\n\n        return $max_overall_profit;\n\
        \    }\n\n    private function dfs($u) {\n        if (isset($this->memo[$u]))\
        \ {\n            return $this->memo[$u];\n        }\n\n        $current_dp_u_no_buy\
        \ = array_fill(0, $this->budget_val + 1, self::NEG_INF);\n        $current_dp_u_no_buy[0]\
        \ = 0;\n\n        $cost_u_normal = $this->present_arr[$u-1];\n        $profit_u_normal\
        \ = $this->future_arr[$u-1] - $cost_u_normal;\n        $current_dp_u_buy_normal\
        \ = array_fill(0, $this->budget_val + 1, self::NEG_INF);\n        if ($cost_u_normal\
        \ <= $this->budget_val) {\n            $current_dp_u_buy_normal[$cost_u_normal]\
        \ = $profit_u_normal;\n        }\n\n        $current_dp_u_no_buy_if_parent_bought\
        \ = array_fill(0, $this->budget_val + 1, self::NEG_INF);\n        $current_dp_u_no_buy_if_parent_bought[0]\
        \ = 0;\n\n        $cost_u_discount = floor($this->present_arr[$u-1] / 2); //\
        \ Integer division is floor for positive numbers\n        $profit_u_discount\
        \ = $this->future_arr[$u-1] - $cost_u_discount;\n        $current_dp_u_buy_discount\
        \ = array_fill(0, $this->budget_val + 1, self::NEG_INF);\n        if ($cost_u_discount\
        \ <= $this->budget_val) {\n            $current_dp_u_buy_discount[$cost_u_discount]\
        \ = $profit_u_discount;\n        }\n\n        foreach ($this->adj[$u] as $v)\
        \ {\n            $res_v = $this->dfs($v);\n\n            // Helper function\
        \ to merge two DP arrays (knapsack-style combination)\n            $merge_dps\
        \ = function($dp1, $dp2) {\n                $new_dp = array_fill(0, $this->budget_val\
        \ + 1, self::NEG_INF);\n                for ($k1 = 0; $k1 <= $this->budget_val;\
        \ ++$k1) {\n                    if ($dp1[$k1] === self::NEG_INF) {\n       \
        \                 continue;\n                    }\n                    for\
        \ ($k2 = 0; $k1 + $k2 <= $this->budget_val; ++$k2) {\n                     \
        \   if ($dp2[$k2] === self::NEG_INF) {\n                            continue;\n\
        \                        }\n                        $new_dp[$k1 + $k2] = max($new_dp[$k1\
        \ + $k2], $dp1[$k1] + $dp2[$k2]);\n                    }\n                }\n\
        \                return $new_dp;\n            };\n\n            $current_dp_u_no_buy\
        \ = $merge_dps($current_dp_u_no_buy, $res_v['dp_no_parent_bought']);\n     \
        \       $current_dp_u_buy_normal = $merge_dps($current_dp_u_buy_normal, $res_v['dp_parent_bought']);\n\
        \            $current_dp_u_no_buy_if_parent_bought = $merge_dps($current_dp_u_no_buy_if_parent_bought,\
        \ $res_v['dp_no_parent_bought']);\n            $current_dp_u_buy_discount =\
        \ $merge_dps($current_dp_u_buy_discount, $res_v['dp_parent_bought']);\n    \
        \    }\n\n        $final_dp_no_parent_bought = array_fill(0, $this->budget_val\
        \ + 1, self::NEG_INF);\n        for ($k = 0; $k <= $this->budget_val; ++$k)\
        \ {\n            $final_dp_no_parent_bought[$k] = max($current_dp_u_no_buy[$k],\
        \ $current_dp_u_buy_normal[$k]);\n        }\n\n        $final_dp_parent_bought\
        \ = array_fill(0, $this->budget_val + 1, self::NEG_INF);\n        for ($k =\
        \ 0; $k <= $this->budget_val; ++$k) {\n            $final_dp_parent_bought[$k]\
        \ = max($current_dp_u_no_buy_if_parent_bought[$k], $current_dp_u_buy_discount[$k]);\n\
        \        }\n\n        $result = ['dp_no_parent_bought' => $final_dp_no_parent_bought,\
        \ 'dp_parent_bought' => $final_dp_parent_bought];\n        $this->memo[$u] =\
        \ $result;\n        return $result;\n    }\n}\n\n?>"
      swift: "import Foundation\n\nclass Solution {\n    // Using a custom class for\
        \ memoization return type\n    class DPResult {\n        var dp_no_parent_bought:\
        \ [Int]\n        var dp_parent_bought: [Int]\n\n        init(dp_no_parent_bought:\
        \ [Int], dp_parent_bought: [Int]) {\n            self.dp_no_parent_bought =\
        \ dp_no_parent_bought\n            self.dp_parent_bought = dp_parent_bought\n\
        \        }\n    }\n\n    var memo: [Int: DPResult] = [:]\n    var adj: [[Int]]\
        \ = []\n    var presentArr: [Int] = []\n    var futureArr: [Int] = []\n    var\
        \ budgetVal: Int = 0\n    let NEG_INF = -1_000_000_000 // A sufficiently small\
        \ number for -float('inf')\n\n    private func dfs(_ u: Int) -> DPResult {\n\
        \        if let result = memo[u] {\n            return result\n        }\n\n\
        \        var current_dp_u_no_buy = Array(repeating: NEG_INF, count: budgetVal\
        \ + 1)\n        current_dp_u_no_buy[0] = 0\n\n        let cost_u_normal = presentArr[u-1]\n\
        \        let profit_u_normal = futureArr[u-1] - cost_u_normal\n        var current_dp_u_buy_normal\
        \ = Array(repeating: NEG_INF, count: budgetVal + 1)\n        if cost_u_normal\
        \ <= budgetVal {\n            current_dp_u_buy_normal[cost_u_normal] = profit_u_normal\n\
        \        }\n\n        var current_dp_u_no_buy_if_parent_bought = Array(repeating:\
        \ NEG_INF, count: budgetVal + 1)\n        current_dp_u_no_buy_if_parent_bought[0]\
        \ = 0\n\n        let cost_u_discount = presentArr[u-1] / 2 // Integer division\
        \ is floor for positive numbers\n        let profit_u_discount = futureArr[u-1]\
        \ - cost_u_discount\n        var current_dp_u_buy_discount = Array(repeating:\
        \ NEG_INF, count: budgetVal + 1)\n        if cost_u_discount <= budgetVal {\n\
        \            current_dp_u_buy_discount[cost_u_discount] = profit_u_discount\n\
        \        }\n\n        for v in adj[u] {\n            let res_v = dfs(v)\n\n\
        \            // Helper function to merge two DP arrays (knapsack-style combination)\n\
        \            let mergeDps = { (dp1: [Int], dp2: [Int]) -> [Int] in\n       \
        \         var new_dp = Array(repeating: self.NEG_INF, count: self.budgetVal\
        \ + 1)\n                for k1 in 0...self.budgetVal {\n                   \
        \ if dp1[k1] == self.NEG_INF {\n                        continue\n         \
        \           }\n                    for k2 in 0...(self.budgetVal - k1) {\n \
        \                       if dp2[k2] == self.NEG_INF {\n                     \
        \       continue\n                        }\n                        new_dp[k1\
        \ + k2] = max(new_dp[k1 + k2], dp1[k1] + dp2[k2])\n                    }\n \
        \               }\n                return new_dp\n            }\n\n        \
        \    current_dp_u_no_buy = mergeDps(current_dp_u_no_buy, res_v.dp_no_parent_bought)\n\
        \            current_dp_u_buy_normal = mergeDps(current_dp_u_buy_normal, res_v.dp_parent_bought)\n\
        \            current_dp_u_no_buy_if_parent_bought = mergeDps(current_dp_u_no_buy_if_parent_bought,\
        \ res_v.dp_no_parent_bought)\n            current_dp_u_buy_discount = mergeDps(current_dp_u_buy_discount,\
        \ res_v.dp_parent_bought)\n        }\n\n        var final_dp_no_parent_bought\
        \ = Array(repeating: NEG_INF, count: budgetVal + 1)\n        for k in 0...budgetVal\
        \ {\n            final_dp_no_parent_bought[k] = max(current_dp_u_no_buy[k],\
        \ current_dp_u_buy_normal[k])\n        }\n\n        var final_dp_parent_bought\
        \ = Array(repeating: NEG_INF, count: budgetVal + 1)\n        for k in 0...budgetVal\
        \ {\n            final_dp_parent_bought[k] = max(current_dp_u_no_buy_if_parent_bought[k],\
        \ current_dp_u_buy_discount[k])\n        }\n\n        let result = DPResult(dp_no_parent_bought:\
        \ final_dp_no_parent_bought, dp_parent_bought: final_dp_parent_bought)\n   \
        \     memo[u] = result\n        return result\n    }\n\n    func maxProfit(_\
        \ n: Int, _ present: [Int], _ future: [Int], _ hierarchy: [[Int]], _ budget:\
        \ Int) -> Int {\n        adj = Array(repeating: [], count: n + 1)\n        for\
        \ edge in hierarchy {\n            adj[edge[0]].append(edge[1])\n        }\n\
        \n        presentArr = present\n        futureArr = future\n        budgetVal\
        \ = budget\n        memo.removeAll()\n\n        let root_res = dfs(1)\n\n  \
        \      var max_overall_profit = 0\n        for profit in root_res.dp_no_parent_bought\
        \ {\n            if profit != NEG_INF {\n                max_overall_profit\
        \ = max(max_overall_profit, profit)\n            }\n        }\n\n        return\
        \ max_overall_profit\n    }\n}"
      kotlin: "import java.util.*\n\nclass Solution {\n    // Using a custom data class\
        \ for memoization return type\n    data class DPResult(\n        val dp_no_parent_bought:\
        \ IntArray,\n        val dp_parent_bought: IntArray\n    )\n\n    private lateinit\
        \ var memo: MutableMap<Int, DPResult>\n    private lateinit var adj: List<MutableList<Int>>\n\
        \    private lateinit var presentArr: IntArray\n    private lateinit var futureArr:\
        \ IntArray\n    private var budgetVal: Int = 0\n    private val NEG_INF = -1_000_000_000\
        \ // A sufficiently small number for -float('inf')\n\n    private fun dfs(u:\
        \ Int): DPResult {\n        if (memo.containsKey(u)) {\n            return memo[u]!!\n\
        \        }\n\n        var current_dp_u_no_buy = IntArray(budgetVal + 1) { NEG_INF\
        \ }\n        current_dp_u_no_buy[0] = 0\n\n        val cost_u_normal = presentArr[u-1]\n\
        \        val profit_u_normal = futureArr[u-1] - cost_u_normal\n        var current_dp_u_buy_normal\
        \ = IntArray(budgetVal + 1) { NEG_INF }\n        if (cost_u_normal <= budgetVal)\
        \ {\n            current_dp_u_buy_normal[cost_u_normal] = profit_u_normal\n\
        \        }\n\n        var current_dp_u_no_buy_if_parent_bought = IntArray(budgetVal\
        \ + 1) { NEG_INF }\n        current_dp_u_no_buy_if_parent_bought[0] = 0\n\n\
        \        val cost_u_discount = presentArr[u-1] / 2 // Integer division is floor\
        \ for positive numbers\n        val profit_u_discount = futureArr[u-1] - cost_u_discount\n\
        \        var current_dp_u_buy_discount = IntArray(budgetVal + 1) { NEG_INF }\n\
        \        if (cost_u_discount <= budgetVal) {\n            current_dp_u_buy_discount[cost_u_discount]\
        \ = profit_u_discount\n        }\n\n        for (v in adj[u]) {\n          \
        \  val res_v = dfs(v)\n\n            // Helper function to merge two DP arrays\
        \ (knapsack-style combination)\n            val mergeDps = { dp1: IntArray,\
        \ dp2: IntArray ->\n                val new_dp = IntArray(budgetVal + 1) { NEG_INF\
        \ }\n                for (k1 in 0..budgetVal) {\n                    if (dp1[k1]\
        \ == NEG_INF) {\n                        continue\n                    }\n \
        \                   for (k2 in 0..(budgetVal - k1)) {\n                    \
        \    if (dp2[k2] == NEG_INF) {\n                            continue\n     \
        \                   }\n                        new_dp[k1 + k2] = maxOf(new_dp[k1\
        \ + k2], dp1[k1] + dp2[k2])\n                    }\n                }\n    \
        \            new_dp\n            }\n\n            current_dp_u_no_buy = mergeDps(current_dp_u_no_buy,\
        \ res_v.dp_no_parent_bought)\n            current_dp_u_buy_normal = mergeDps(current_dp_u_buy_normal,\
        \ res_v.dp_parent_bought)\n            current_dp_u_no_buy_if_parent_bought\
        \ = mergeDps(current_dp_u_no_buy_if_parent_bought, res_v.dp_no_parent_bought)\n\
        \            current_dp_u_buy_discount = mergeDps(current_dp_u_buy_discount,\
        \ res_v.dp_parent_bought)\n        }\n\n        val final_dp_no_parent_bought\
        \ = IntArray(budgetVal + 1) { NEG_INF }\n        for (k in 0..budgetVal) {\n\
        \            final_dp_no_parent_bought[k] = maxOf(current_dp_u_no_buy[k], current_dp_u_buy_normal[k])\n\
        \        }\n\n        val final_dp_parent_bought = IntArray(budgetVal + 1) {\
        \ NEG_INF }\n        for (k in 0..budgetVal) {\n            final_dp_parent_bought[k]\
        \ = maxOf(current_dp_u_no_buy_if_parent_bought[k], current_dp_u_buy_discount[k])\n\
        \        }\n\n        val result = DPResult(final_dp_no_parent_bought, final_dp_parent_bought)\n\
        \        memo[u] = result\n        return result\n    }\n\n    fun maxProfit(n:\
        \ Int, present: IntArray, future: IntArray, hierarchy: Array<IntArray>, budget:\
        \ Int): Int {\n        adj = List(n + 1) { mutableListOf() }\n        for (edge\
        \ in hierarchy) {\n            adj[edge[0]].add(edge[1])\n        }\n\n    \
        \    presentArr = present\n        futureArr = future\n        budgetVal = budget\n\
        \        memo = mutableMapOf()\n\n        val root_res = dfs(1)\n\n        var\
        \ max_overall_profit = 0\n        for (profit in root_res.dp_no_parent_bought)\
        \ {\n            if (profit != NEG_INF) {\n                max_overall_profit\
        \ = maxOf(max_overall_profit, profit)\n            }\n        }\n\n        return\
        \ max_overall_profit\n    }\n}"
      dart: "import 'dart:collection';\nimport 'dart:math';\n\nclass Solution {\n  //\
        \ Using a custom class for memoization return type\n  class DPResult {\n   \
        \ List<int> dp_no_parent_bought;\n    List<int> dp_parent_bought;\n\n    DPResult(this.dp_no_parent_bought,\
        \ this.dp_parent_bought);\n  }\n\n  late Map<int, DPResult> memo;\n  late List<List<int>>\
        \ adj;\n  late List<int> presentArr;\n  late List<int> futureArr;\n  late int\
        \ budgetVal;\n  static const int NEG_INF = -1000000000; // A sufficiently small\
        \ number for -float('inf')\n\n  DPResult _dfs(int u) {\n    if (memo.containsKey(u))\
        \ {\n      return memo[u]!;\n    }\n\n    List<int> current_dp_u_no_buy = List.filled(budgetVal\
        \ + 1, NEG_INF);\n    current_dp_u_no_buy[0] = 0;\n\n    int cost_u_normal =\
        \ presentArr[u-1];\n    int profit_u_normal = futureArr[u-1] - cost_u_normal;\n\
        \    List<int> current_dp_u_buy_normal = List.filled(budgetVal + 1, NEG_INF);\n\
        \    if (cost_u_normal <= budgetVal) {\n      current_dp_u_buy_normal[cost_u_normal]\
        \ = profit_u_normal;\n    }\n\n    List<int> current_dp_u_no_buy_if_parent_bought\
        \ = List.filled(budgetVal + 1, NEG_INF);\n    current_dp_u_no_buy_if_parent_bought[0]\
        \ = 0;\n\n    int cost_u_discount = (presentArr[u-1] / 2).floor(); // Integer\
        \ division is floor for positive numbers\n    int profit_u_discount = futureArr[u-1]\
        \ - cost_u_discount;\n    List<int> current_dp_u_buy_discount = List.filled(budgetVal\
        \ + 1, NEG_INF);\n    if (cost_u_discount <= budgetVal) {\n      current_dp_u_buy_discount[cost_u_discount]\
        \ = profit_u_discount;\n    }\n\n    for (int v in adj[u]) {\n      DPResult\
        \ res_v = _dfs(v);\n\n      // Helper function to merge two DP arrays (knapsack-style\
        \ combination)\n      List<int> mergeDps(List<int> dp1, List<int> dp2) {\n \
        \       List<int> new_dp = List.filled(budgetVal + 1, NEG_INF);\n        for\
        \ (int k1 = 0; k1 <= budgetVal; ++k1) {\n          if (dp1[k1] == NEG_INF) {\n\
        \            continue;\n          }\n          for (int k2 = 0; k1 + k2 <= budgetVal;\
        \ ++k2) {\n            if (dp2[k2] == NEG_INF) {\n              continue;\n\
        \            }\n            new_dp[k1 + k2] = max(new_dp[k1 + k2], dp1[k1] +\
        \ dp2[k2]);\n          }\n        }\n        return new_dp;\n      }\n\n   \
        \   current_dp_u_no_buy = mergeDps(current_dp_u_no_buy, res_v.dp_no_parent_bought);\n\
        \      current_dp_u_buy_normal = mergeDps(current_dp_u_buy_normal, res_v.dp_parent_bought);\n\
        \      current_dp_u_no_buy_if_parent_bought = mergeDps(current_dp_u_no_buy_if_parent_bought,\
        \ res_v.dp_no_parent_bought);\n      current_dp_u_buy_discount = mergeDps(current_dp_u_buy_discount,\
        \ res_v.dp_parent_bought);\n    }\n\n    List<int> final_dp_no_parent_bought\
        \ = List.filled(budgetVal + 1, NEG_INF);\n    for (int k = 0; k <= budgetVal;\
        \ ++k) {\n      final_dp_no_parent_bought[k] = max(current_dp_u_no_buy[k], current_dp_u_buy_normal[k]);\n\
        \    }\n\n    List<int> final_dp_parent_bought = List.filled(budgetVal + 1,\
        \ NEG_INF);\n    for (int k = 0; k <= budgetVal; ++k) {\n      final_dp_parent_bought[k]\
        \ = max(current_dp_u_no_buy_if_parent_bought[k], current_dp_u_buy_discount[k]);\n\
        \    }\n\n    DPResult result = DPResult(final_dp_no_parent_bought, final_dp_parent_bought);\n\
        \    memo[u] = result;\n    return result;\n  }\n\n  int maxProfit(int n, List<int>\
        \ present, List<int> future, List<List<int>> hierarchy, int budget) {\n    adj\
        \ = List.generate(n + 1, (_) => []);\n    for (List<int> edge in hierarchy)\
        \ {\n      adj[edge[0]].add(edge[1]);\n    }\n\n    presentArr = present;\n\
        \    futureArr = future;\n    budgetVal = budget;\n    memo = HashMap();\n\n\
        \    DPResult root_res = _dfs(1);\n\n    int maxOverallProfit = 0;\n    for\
        \ (int profit in root_res.dp_no_parent_bought) {\n      if (profit != NEG_INF)\
        \ {\n        maxOverallProfit = max(maxOverallProfit, profit);\n      }\n  \
        \  }\n\n    return maxOverallProfit;\n  }\n}"
      go: "package main\n\nimport (\n\t\"math\"\n)\n\n// DPResult struct to hold DP\
        \ results for a subtree\ntype DPResult struct {\n\tdp_no_parent_bought []int\n\
        \tdp_parent_bought  []int\n}\n\ntype Solution struct {\n\tmemo      map[int]DPResult\n\
        \tadj       [][]int\n\tpresentArr []int\n\tfutureArr  []int\n\tbudgetVal int\n\
        }\n\nconst NEG_INF = -1_000_000_000 // A sufficiently small number for -float('inf')\n\
        \nfunc (s *Solution) dfs(u int) DPResult {\n\tif result, ok := s.memo[u]; ok\
        \ {\n\t\treturn result\n\t}\n\n\tcurrent_dp_u_no_buy := make([]int, s.budgetVal+1)\n\
        \tfor i := range current_dp_u_no_buy {\n\t\tcurrent_dp_u_no_buy[i] = NEG_INF\n\
        \t}\n\tcurrent_dp_u_no_buy[0] = 0\n\n\tcost_u_normal := s.presentArr[u-1]\n\t\
        profit_u_normal := s.futureArr[u-1] - cost_u_normal\n\tcurrent_dp_u_buy_normal\
        \ := make([]int, s.budgetVal+1)\n\tfor i := range current_dp_u_buy_normal {\n\
        \t\tcurrent_dp_u_buy_normal[i] = NEG_INF\n\t}\n\tif cost_u_normal <= s.budgetVal\
        \ {\n\t\tcurrent_dp_u_buy_normal[cost_u_normal] = profit_u_normal\n\t}\n\n\t\
        current_dp_u_no_buy_if_parent_bought := make([]int, s.budgetVal+1)\n\tfor i\
        \ := range current_dp_u_no_buy_if_parent_bought {\n\t\tcurrent_dp_u_no_buy_if_parent_bought[i]\
        \ = NEG_INF\n\t}\n\tcurrent_dp_u_no_buy_if_parent_bought[0] = 0\n\n\tcost_u_discount\
        \ := s.presentArr[u-1] / 2 // Integer division is floor for positive numbers\n\
        \tprofit_u_discount := s.futureArr[u-1] - cost_u_discount\n\tcurrent_dp_u_buy_discount\
        \ := make([]int, s.budgetVal+1)\n\tfor i := range current_dp_u_buy_discount\
        \ {\n\t\tcurrent_dp_u_buy_discount[i] = NEG_INF\n\t}\n\tif cost_u_discount <=\
        \ s.budgetVal {\n\t\tcurrent_dp_u_buy_discount[cost_u_discount] = profit_u_discount\n\
        \t}\n\n\tfor _, v := range s.adj[u] {\n\t\tres_v := s.dfs(v)\n\n\t\t// Helper\
        \ function to merge two DP arrays (knapsack-style combination)\n\t\tmergeDps\
        \ := func(dp1, dp2 []int) []int {\n\t\t\tnew_dp := make([]int, s.budgetVal+1)\n\
        \t\t\tfor i := range new_dp {\n\t\t\t\tnew_dp[i] = NEG_INF\n\t\t\t}\n\t\t\t\
        for k1 := 0; k1 <= s.budgetVal; k1++ {\n\t\t\t\tif dp1[k1] == NEG_INF {\n\t\t\
        \t\t\tcontinue\n\t\t\t\t}\n\t\t\t\tfor k2 := 0; k1+k2 <= s.budgetVal; k2++ {\n\
        \t\t\t\t\tif dp2[k2] == NEG_INF {\n\t\t\t\t\t\tcontinue\n\t\t\t\t\t}\n\t\t\t\
        \t\tnew_dp[k1+k2] = int(math.Max(float64(new_dp[k1+k2]), float64(dp1[k1]+dp2[k2])))\n\
        \t\t\t\t}\n\t\t\t}\n\t\t\treturn new_dp\n\t\t}\n\n\t\tcurrent_dp_u_no_buy =\
        \ mergeDps(current_dp_u_no_buy, res_v.dp_no_parent_bought)\n\t\tcurrent_dp_u_buy_normal\
        \ = mergeDps(current_dp_u_buy_normal, res_v.dp_parent_bought)\n\t\tcurrent_dp_u_no_buy_if_parent_bought\
        \ = mergeDps(current_dp_u_no_buy_if_parent_bought, res_v.dp_no_parent_bought)\n\
        \t\tcurrent_dp_u_buy_discount = mergeDps(current_dp_u_buy_discount, res_v.dp_parent_bought)\n\
        \t}\n\n\tfinal_dp_no_parent_bought := make([]int, s.budgetVal+1)\n\tfor i :=\
        \ range final_dp_no_parent_bought {\n\t\tfinal_dp_no_parent_bought[i] = NEG_INF\n\
        \t}\n\tfor k := 0; k <= s.budgetVal; k++ {\n\t\tfinal_dp_no_parent_bought[k]\
        \ = int(math.Max(float64(current_dp_u_no_buy[k]), float64(current_dp_u_buy_normal[k])))\n\
        \t}\n\n\tfinal_dp_parent_bought := make([]int, s.budgetVal+1)\n\tfor i := range\
        \ final_dp_parent_bought {\n\t\tfinal_dp_parent_bought[i] = NEG_INF\n\t}\n\t\
        for k := 0; k <= s.budgetVal; k++ {\n\t\tfinal_dp_parent_bought[k] = int(math.Max(float64(current_dp_u_no_buy_if_parent_bought[k]),\
        \ float64(current_dp_u_buy_discount[k])))\n\t}\n\n\tresult := DPResult{dp_no_parent_bought:\
        \ final_dp_no_parent_bought, dp_parent_bought: final_dp_parent_bought}\n\ts.memo[u]\
        \ = result\n\treturn result\n}\n\nfunc maxProfit(n int, present []int, future\
        \ []int, hierarchy [][]int, budget int) int {\n\ts := &Solution{\n\t\tmemo:\
        \      make(map[int]DPResult),\n\t\tadj:       make([][]int, n+1),\n\t\tpresentArr:\
        \ present,\n\t\tfutureArr:  future,\n\t\tbudgetVal: budget,\n\t}\n\n\tfor _,\
        \ edge := range hierarchy {\n\t\tu, v := edge[0], edge[1]\n\t\ts.adj[u] = append(s.adj[u],\
        \ v)\n\t}\n\n\troot_res := s.dfs(1)\n\n\tmax_overall_profit := 0\n\tfor _, profit\
        \ := range root_res.dp_no_parent_bought {\n\t\tif profit != NEG_INF {\n\t\t\t\
        max_overall_profit = int(math.Max(float64(max_overall_profit), float64(profit)))\n\
        \t\t}\n\t}\n\n\treturn max_overall_profit\n}"
      ruby: "class Solution\n    # Using a custom class for memoization return type\n\
        \    DPResult = Struct.new(:dp_no_parent_bought, :dp_parent_bought)\n\n    attr_accessor\
        \ :adj, :present_arr, :future_arr, :budget_val, :memo\n    NEG_INF = -1_000_000_000\
        \ # A sufficiently small number for -Float::INFINITY\n\n    def dfs(u)\n   \
        \     return memo[u] if memo.key?(u)\n\n        current_dp_u_no_buy = Array.new(budget_val\
        \ + 1, NEG_INF)\n        current_dp_u_no_buy[0] = 0\n\n        cost_u_normal\
        \ = present_arr[u-1]\n        profit_u_normal = future_arr[u-1] - cost_u_normal\n\
        \        current_dp_u_buy_normal = Array.new(budget_val + 1, NEG_INF)\n    \
        \    if cost_u_normal <= budget_val\n            current_dp_u_buy_normal[cost_u_normal]\
        \ = profit_u_normal\n        end\n\n        current_dp_u_no_buy_if_parent_bought\
        \ = Array.new(budget_val + 1, NEG_INF)\n        current_dp_u_no_buy_if_parent_bought[0]\
        \ = 0\n\n        cost_u_discount = (present_arr[u-1] / 2).floor # Integer division\
        \ is floor for positive numbers\n        profit_u_discount = future_arr[u-1]\
        \ - cost_u_discount\n        current_dp_u_buy_discount = Array.new(budget_val\
        \ + 1, NEG_INF)\n        if cost_u_discount <= budget_val\n            current_dp_u_buy_discount[cost_u_discount]\
        \ = profit_u_discount\n        end\n\n        adj[u].each do |v|\n         \
        \   res_v = dfs(v)\n\n            # Helper function to merge two DP arrays (knapsack-style\
        \ combination)\n            merge_dps = ->(dp1, dp2) do\n                new_dp\
        \ = Array.new(budget_val + 1, NEG_INF)\n                (0..budget_val).each\
        \ do |k1|\n                    next if dp1[k1] == NEG_INF\n                \
        \    (0..(budget_val - k1)).each do |k2|\n                        next if dp2[k2]\
        \ == NEG_INF\n                        new_dp[k1 + k2] = [new_dp[k1 + k2], dp1[k1]\
        \ + dp2[k2]].max\n                    end\n                end\n           \
        \     new_dp\n            end\n\n            current_dp_u_no_buy = merge_dps.call(current_dp_u_no_buy,\
        \ res_v.dp_no_parent_bought)\n            current_dp_u_buy_normal = merge_dps.call(current_dp_u_buy_normal,\
        \ res_v.dp_parent_bought)\n            current_dp_u_no_buy_if_parent_bought\
        \ = merge_dps.call(current_dp_u_no_buy_if_parent_bought, res_v.dp_no_parent_bought)\n\
        \            current_dp_u_buy_discount = merge_dps.call(current_dp_u_buy_discount,\
        \ res_v.dp_parent_bought)\n        end\n\n        final_dp_no_parent_bought\
        \ = Array.new(budget_val + 1, NEG_INF)\n        (0..budget_val).each do |k|\n\
        \            final_dp_no_parent_bought[k] = [current_dp_u_no_buy[k], current_dp_u_buy_normal[k]].max\n\
        \        end\n\n        final_dp_parent_bought = Array.new(budget_val + 1, NEG_INF)\n\
        \        (0..budget_val).each do |k|\n            final_dp_parent_bought[k]\
        \ = [current_dp_u_no_buy_if_parent_bought[k], current_dp_u_buy_discount[k]].max\n\
        \        end\n\n        result = DPResult.new(final_dp_no_parent_bought, final_dp_parent_bought)\n\
        \        memo[u] = result\n        result\n    end\n\n    def max_profit(n,\
        \ present, future, hierarchy, budget)\n        self.adj = Array.new(n + 1) {\
        \ [] }\n        hierarchy.each do |u, v|\n            adj[u] << v\n        end\n\
        \n        self.present_arr = present\n        self.future_arr = future\n   \
        \     self.budget_val = budget\n        self.memo = {}\n\n        root_res =\
        \ dfs(1)\n\n        max_overall_profit = 0\n        root_res.dp_no_parent_bought.each\
        \ do |profit|\n            if profit != NEG_INF\n                max_overall_profit\
        \ = [max_overall_profit, profit].max\n            end\n        end\n\n     \
        \   max_overall_profit\n    end\nend"
      scala: "import scala.collection.mutable\n\nclass Solution {\n  // Using a custom\
        \ case class for memoization return type\n  case class DPResult(\n    dp_no_parent_bought:\
        \ Array[Int],\n    dp_parent_bought: Array[Int]\n  )\n\n  private var adj: Array[mutable.ListBuffer[Int]]\
        \ = _\n  private var presentArr: Array[Int] = _\n  private var futureArr: Array[Int]\
        \ = _\n  private var budgetVal: Int = _\n  private val memo: mutable.Map[Int,\
        \ DPResult] = mutable.Map()\n  private val NEG_INF = -1_000_000_000 // A sufficiently\
        \ small number for -Float.Infinity\n\n  private def dfs(u: Int): DPResult =\
        \ {\n    memo.get(u) match {\n      case Some(result) => result\n      case\
        \ None =>\n        var current_dp_u_no_buy = Array.fill(budgetVal + 1)(NEG_INF)\n\
        \        current_dp_u_no_buy(0) = 0\n\n        val cost_u_normal = presentArr(u\
        \ - 1)\n        val profit_u_normal = futureArr(u - 1) - cost_u_normal\n   \
        \     var current_dp_u_buy_normal = Array.fill(budgetVal + 1)(NEG_INF)\n   \
        \     if (cost_u_normal <= budgetVal) {\n          current_dp_u_buy_normal(cost_u_normal)\
        \ = profit_u_normal\n        }\n\n        var current_dp_u_no_buy_if_parent_bought\
        \ = Array.fill(budgetVal + 1)(NEG_INF)\n        current_dp_u_no_buy_if_parent_bought(0)\
        \ = 0\n\n        val cost_u_discount = presentArr(u - 1) / 2 // Integer division\
        \ is floor for positive numbers\n        val profit_u_discount = futureArr(u\
        \ - 1) - cost_u_discount\n        var current_dp_u_buy_discount = Array.fill(budgetVal\
        \ + 1)(NEG_INF)\n        if (cost_u_discount <= budgetVal) {\n          current_dp_u_buy_discount(cost_u_discount)\
        \ = profit_u_discount\n        }\n\n        for (v <- adj(u)) {\n          val\
        \ res_v = dfs(v)\n\n          // Helper function to merge two DP arrays (knapsack-style\
        \ combination)\n          def mergeDps(dp1: Array[Int], dp2: Array[Int]): Array[Int]\
        \ = {\n            val new_dp = Array.fill(budgetVal + 1)(NEG_INF)\n       \
        \     for (k1 <- 0 to budgetVal) {\n              if (dp1(k1) == NEG_INF) {\n\
        \                // continue\n              } else {\n                for (k2\
        \ <- 0 to (budgetVal - k1)) {\n                  if (dp2(k2) == NEG_INF) {\n\
        \                    // continue\n                  } else {\n             \
        \       new_dp(k1 + k2) = math.max(new_dp(k1 + k2), dp1(k1) + dp2(k2))\n   \
        \               }\n                }\n              }\n            }\n     \
        \       new_dp\n          }\n\n          current_dp_u_no_buy = mergeDps(current_dp_u_no_buy,\
        \ res_v.dp_no_parent_bought)\n          current_dp_u_buy_normal = mergeDps(current_dp_u_buy_normal,\
        \ res_v.dp_parent_bought)\n          current_dp_u_no_buy_if_parent_bought =\
        \ mergeDps(current_dp_u_no_buy_if_parent_bought, res_v.dp_no_parent_bought)\n\
        \          current_dp_u_buy_discount = mergeDps(current_dp_u_buy_discount, res_v.dp_parent_bought)\n\
        \        }\n\n        val final_dp_no_parent_bought = Array.fill(budgetVal +\
        \ 1)(NEG_INF)\n        for (k <- 0 to budgetVal) {\n          final_dp_no_parent_bought(k)\
        \ = math.max(current_dp_u_no_buy(k), current_dp_u_buy_normal(k))\n        }\n\
        \n        val final_dp_parent_bought = Array.fill(budgetVal + 1)(NEG_INF)\n\
        \        for (k <- 0 to budgetVal) {\n          final_dp_parent_bought(k) =\
        \ math.max(current_dp_u_no_buy_if_parent_bought(k), current_dp_u_buy_discount(k))\n\
        \        }\n\n        val result = DPResult(final_dp_no_parent_bought, final_dp_parent_bought)\n\
        \        memo(u) = result\n        result\n    }\n\n  def maxProfit(n: Int,\
        \ present: Array[Int], future: Array[Int], hierarchy: Array[Array[Int]], budget:\
        \ Int): Int = {\n    adj = Array.fill(n + 1)(mutable.ListBuffer[Int]())\n  \
        \  for (edge <- hierarchy) {\n      adj(edge(0)) += edge(1)\n    }\n\n    presentArr\
        \ = present\n    futureArr = future\n    budgetVal = budget\n    memo.clear()\n\
        \n    val root_res = dfs(1)\n\n    var max_overall_profit = 0\n    for (profit\
        \ <- root_res.dp_no_parent_bought) {\n      if (profit != NEG_INF) {\n     \
        \   max_overall_profit = math.max(max_overall_profit, profit)\n      }\n   \
        \ }\n\n    max_overall_profit\n  }\n}"
      rust: "use std::collections::HashMap;\nuse std::cmp::max;\n\nconst NEG_INF: i32\
        \ = -1_000_000_000; // A sufficiently small number for -float('inf')\n\n// DPResult\
        \ struct to hold DP results for a subtree\n#[derive(Clone)] // Needed for storing\
        \ in HashMap and returning copies\nstruct DPResult {\n    dp_no_parent_bought:\
        \ Vec<i32>,\n    dp_parent_bought: Vec<i32>,\n}\n\nstruct SolutionData {\n \
        \   memo: HashMap<i32, DPResult>,\n    adj: Vec<Vec<i32>>,\n    present_arr:\
        \ Vec<i32>,\n    future_arr: Vec<i32>,\n    budget_val: i32,\n}\n\nimpl SolutionData\
        \ {\n    fn dfs(&mut self, u: i32) -> DPResult {\n        if let Some(result)\
        \ = self.memo.get(&u) {\n            return result.clone();\n        }\n\n \
        \       let mut current_dp_u_no_buy = vec![NEG_INF; (self.budget_val + 1) as\
        \ usize];\n        current_dp_u_no_buy[0] = 0;\n\n        let cost_u_normal\
        \ = self.present_arr[(u - 1) as usize];\n        let profit_u_normal = self.future_arr[(u\
        \ - 1) as usize] - cost_u_normal;\n        let mut current_dp_u_buy_normal =\
        \ vec![NEG_INF; (self.budget_val + 1) as usize];\n        if cost_u_normal <=\
        \ self.budget_val {\n            current_dp_u_buy_normal[cost_u_normal as usize]\
        \ = profit_u_normal;\n        }\n\n        let mut current_dp_u_no_buy_if_parent_bought\
        \ = vec![NEG_INF; (self.budget_val + 1) as usize];\n        current_dp_u_no_buy_if_parent_bought[0]\
        \ = 0;\n\n        let cost_u_discount = self.present_arr[(u - 1) as usize] /\
        \ 2; // Integer division is floor for positive numbers\n        let profit_u_discount\
        \ = self.future_arr[(u - 1) as usize] - cost_u_discount;\n        let mut current_dp_u_buy_discount\
        \ = vec![NEG_INF; (self.budget_val + 1) as usize];\n        if cost_u_discount\
        \ <= self.budget_val {\n            current_dp_u_buy_discount[cost_u_discount\
        \ as usize] = profit_u_discount;\n        }\n\n        for &v in &self.adj[u\
        \ as usize] {\n            let res_v = self.dfs(v);\n\n            // Helper\
        \ function to merge two DP arrays (knapsack-style combination)\n           \
        \ let merge_dps = |dp1: &[i32], dp2: &[i32]| -> Vec<i32> {\n               \
        \ let mut new_dp = vec![NEG_INF; (self.budget_val + 1) as usize];\n        \
        \        for k1 in 0..=self.budget_val {\n                    if dp1[k1 as usize]\
        \ == NEG_INF {\n                        continue;\n                    }\n \
        \                   for k2 in 0..=(self.budget_val - k1) {\n               \
        \         if dp2[k2 as usize] == NEG_INF {\n                            continue;\n\
        \                        }\n                        let total_cost = (k1 + k2)\
        \ as usize;\n                        new_dp[total_cost] = max(new_dp[total_cost],\
        \ dp1[k1 as usize] + dp2[k2 as usize]);\n                    }\n           \
        \     }\n                new_dp\n            };\n\n            current_dp_u_no_buy\
        \ = merge_dps(&current_dp_u_no_buy, &res_v.dp_no_parent_bought);\n         \
        \   current_dp_u_buy_normal = merge_dps(&current_dp_u_buy_normal, &res_v.dp_parent_bought);\n\
        \            current_dp_u_no_buy_if_parent_bought = merge_dps(&current_dp_u_no_buy_if_parent_bought,\
        \ &res_v.dp_no_parent_bought);\n            current_dp_u_buy_discount = merge_dps(&current_dp_u_buy_discount,\
        \ &res_v.dp_parent_bought);\n        }\n\n        let mut final_dp_no_parent_bought\
        \ = vec![NEG_INF; (self.budget_val + 1) as usize];\n        for k in 0..=self.budget_val\
        \ {\n            final_dp_no_parent_bought[k as usize] = max(current_dp_u_no_buy[k\
        \ as usize], current_dp_u_buy_normal[k as usize]);\n        }\n\n        let\
        \ mut final_dp_parent_bought = vec![NEG_INF; (self.budget_val + 1) as usize];\n\
        \        for k in 0..=self.budget_val {\n            final_dp_parent_bought[k\
        \ as usize] = max(current_dp_u_no_buy_if_parent_bought[k as usize], current_dp_u_buy_discount[k\
        \ as usize]);\n        }\n\n        let result = DPResult { dp_no_parent_bought:\
        \ final_dp_no_parent_bought, dp_parent_bought: final_dp_parent_bought };\n \
        \       self.memo.insert(u, result.clone());\n        result\n    }\n}\n\nimpl\
        \ Solution {\n    pub fn max_profit(n: i32, present: Vec<i32>, future: Vec<i32>,\
        \ hierarchy: Vec<Vec<i32>>, budget: i32) -> i32 {\n        let mut adj: Vec<Vec<i32>>\
        \ = vec![vec![]; (n + 1) as usize];\n        for edge in hierarchy {\n     \
        \       let u = edge[0];\n            let v = edge[1];\n            adj[u as\
        \ usize].push(v);\n        }\n\n        let mut solution_data = SolutionData\
        \ {\n            memo: HashMap::new(),\n            adj,\n            present_arr:\
        \ present,\n            future_arr: future,\n            budget_val: budget,\n\
        \        };\n\n        let root_res = solution_data.dfs(1);\n\n        let mut\
        \ max_overall_profit = 0;\n        for &profit in &root_res.dp_no_parent_bought\
        \ {\n            if profit != NEG_INF {\n                max_overall_profit\
        \ = max(max_overall_profit, profit);\n            }\n        }\n\n        max_overall_profit\n\
        \    }\n}"
      racket: "#lang racket\n\n(define (max-profit n present future hierarchy budget)\n\
        \  (define adj (make-vector (+ n 1) '()))\n  (for-each (lambda (edge)\n    \
        \          (define u (car edge))\n              (define v (cadr edge))\n   \
        \           (vector-set! adj u (cons v (vector-ref adj u))))\n            hierarchy)\n\
        \n  (define memo (make-hash))\n  (define NEG-INF -1000000000) ; A sufficiently\
        \ small number\n\n  (define (dfs u)\n    (hash-ref! memo u\n               (lambda\
        \ ()\n                 (define (make-dp-array)\n                   (build-list\
        \ (+ budget 1) (lambda (_) NEG-INF)))\n\n                 (define (merge-dps\
        \ dp1 dp2)\n                   (define new-dp (make-dp-array))\n           \
        \        (for ([k1 (in-range (+ budget 1))])\n                     (when (not\
        \ (= (list-ref dp1 k1) NEG-INF))\n                       (for ([k2 (in-range\
        \ (+ (- budget k1) 1))])\n                         (when (not (= (list-ref dp2\
        \ k2) NEG-INF))\n                           (set!-list-ref! new-dp (+ k1 k2)\n\
        \                                          (max (list-ref new-dp (+ k1 k2))\n\
        \                                               (+ (list-ref dp1 k1) (list-ref\
        \ dp2 k2))))))))\n                   new-dp)\n\n                 (define current-dp-u-no-buy\
        \ (make-dp-array))\n                 (set!-list-ref! current-dp-u-no-buy 0 0)\n\
        \n                 (define cost-u-normal (list-ref present (- u 1)))\n     \
        \            (define profit-u-normal (- (list-ref future (- u 1)) cost-u-normal))\n\
        \                 (define current-dp-u-buy-normal (make-dp-array))\n       \
        \          (when (<= cost-u-normal budget)\n                   (set!-list-ref!\
        \ current-dp-u-buy-normal cost-u-normal profit-u-normal))\n\n              \
        \   (define current-dp-u-no-buy-if-parent-bought (make-dp-array))\n        \
        \         (set!-list-ref! current-dp-u-no-buy-if-parent-bought 0 0)\n\n    \
        \             (define cost-u-discount (floor (/ (list-ref present (- u 1)) 2)))\n\
        \                 (define profit-u-discount (- (list-ref future (- u 1)) cost-u-discount))\n\
        \                 (define current-dp-u-buy-discount (make-dp-array))\n     \
        \            (when (<= cost-u-discount budget)\n                   (set!-list-ref!\
        \ current-dp-u-buy-discount cost-u-discount profit-u-discount))\n\n        \
        \         (for-each (lambda (v)\n                             (define res-v\
        \ (dfs v))\n                             (define res-v-no-parent-bought (car\
        \ res-v))\n                             (define res-v-parent-bought (cdr res-v))\n\
        \n                             (set! current-dp-u-no-buy (merge-dps current-dp-u-no-buy\
        \ res-v-no-parent-bought))\n                             (set! current-dp-u-buy-normal\
        \ (merge-dps current-dp-u-buy-normal res-v-parent-bought))\n               \
        \              (set! current-dp-u-no-buy-if-parent-bought (merge-dps current-dp-u-no-buy-if-parent-bought\
        \ res-v-no-parent-bought))\n                             (set! current-dp-u-buy-discount\
        \ (merge-dps current-dp-u-buy-discount res-v-parent-bought)))\n            \
        \               (vector-ref adj u))\n\n                 (define final-dp-no-parent-bought\
        \ (make-dp-array))\n                 (for ([k (in-range (+ budget 1))])\n  \
        \                 (set!-list-ref! final-dp-no-parent-bought k\n            \
        \                      (max (list-ref current-dp-u-no-buy k)\n             \
        \                          (list-ref current-dp-u-buy-normal k))))\n\n     \
        \            (define final-dp-parent-bought (make-dp-array))\n             \
        \    (for ([k (in-range (+ budget 1))])\n                   (set!-list-ref!\
        \ final-dp-parent-bought k\n                                  (max (list-ref\
        \ current-dp-u-no-buy-if-parent-bought k)\n                                \
        \       (list-ref current-dp-u-buy-discount k))))\n\n                 (cons\
        \ final-dp-no-parent-bought final-dp-parent-bought))))\n\n  (define root-res\
        \ (dfs 1))\n  (define final-dp-root-no-parent-bought (car root-res))\n\n  (define\
        \ max-overall-profit 0)\n  (for-each (lambda (profit)\n              (when (not\
        \ (= profit NEG-INF))\n                (set! max-overall-profit (max max-overall-profit\
        \ profit))))\n            final-dp-root-no-parent-bought)\n\n  max-overall-profit)\n\
        \n(define (set!-list-ref! lst idx val)\n  (set-car! (list-tail lst idx) val))"
      erlang: "-module(solution).\n-export([max_profit/5]).\n\n-define(NEG_INF, -1_000_000_000).\
        \ % A sufficiently small number\n\n% Helper function to create a DP array initialized\
        \ with NEG_INF, 0 at index 0\nmake_dp_array(Budget) ->\n    Arr = array:new([{fixed,\
        \ true}, {size, Budget + 1}, {default, ?NEG_INF}]),\n    array:set(0, 0, Arr).\n\
        \n% Helper function to merge two DP arrays (knapsack-style combination)\nmerge_dps(Dp1,\
        \ Dp2, Budget) ->\n    NewDp = make_dp_array(Budget),\n    merge_dps_loop(0,\
        \ Dp1, Dp2, NewDp, Budget).\n\nmerge_dps_loop(K1, Dp1, Dp2, NewDp, Budget) when\
        \ K1 =< Budget ->\n    Val1 = array:get(K1, Dp1),\n    case Val1 of\n      \
        \  ?NEG_INF -> merge_dps_loop(K1 + 1, Dp1, Dp2, NewDp, Budget);\n        _ ->\n\
        \            NewDp2 = merge_dps_inner_loop(K1, 0, Val1, Dp2, NewDp, Budget),\n\
        \            merge_dps_loop(K1 + 1, Dp1, Dp2, NewDp2, Budget)\n    end;\nmerge_dps_loop(_K1,\
        \ _Dp1, _Dp2, NewDp, _Budget) ->\n    NewDp.\n\nmerge_dps_inner_loop(K1, K2,\
        \ Val1, Dp2, NewDp, Budget) when K1 + K2 =< Budget ->\n    Val2 = array:get(K2,\
        \ Dp2),\n    case Val2 of\n        ?NEG_INF -> merge_dps_inner_loop(K1, K2 +\
        \ 1, Val1, Dp2, NewDp, Budget);\n        _ ->\n            CurrentMax = array:get(K1\
        \ + K2, NewDp),\n            NewVal = Val1 + Val2,\n            UpdatedNewDp\
        \ = array:set(K1 + K2, max(CurrentMax, NewVal), NewDp),\n            merge_dps_inner_loop(K1,\
        \ K2 + 1, Val1, Dp2, UpdatedNewDp, Budget)\n    end;\nmerge_dps_inner_loop(_K1,\
        \ _K2, _Val1, _Dp2, NewDp, _Budget) ->\n    NewDp.\n\n% DFS function\ndfs(U,\
        \ Adj, PresentArr, FutureArr, Budget, Memo) ->\n    case maps:find(U, Memo)\
        \ of\n        {ok, Result} -> {Result, Memo};\n        _ ->\n            CurrentDpUNoBuy\
        \ = make_dp_array(Budget),\n\n            CostUNormal = array:get(U - 1, PresentArr),\n\
        \            ProfitUNormal = array:get(U - 1, FutureArr) - CostUNormal,\n  \
        \          CurrentDpUBuyNormal = make_dp_array(Budget),\n            UpdatedCurrentDpUBuyNormal\
        \ = \n                if CostUNormal =< Budget -> array:set(CostUNormal, ProfitUNormal,\
        \ CurrentDpUBuyNormal);\n                true -> CurrentDpUBuyNormal\n     \
        \           end,\n\n            CurrentDpUNoBuyIfParentBought = make_dp_array(Budget),\n\
        \n            CostUDiscount = trunc(array:get(U - 1, PresentArr) / 2),\n   \
        \         ProfitUDiscount = array:get(U - 1, FutureArr) - CostUDiscount,\n \
        \           CurrentDpUBuyDiscount = make_dp_array(Budget),\n            UpdatedCurrentDpUBuyDiscount\
        \ = \n                if CostUDiscount =< Budget -> array:set(CostUDiscount,\
        \ ProfitUDiscount, CurrentDpUBuyDiscount);\n                true -> CurrentDpUBuyDiscount\n\
        \                end,\n\n            {FinalDpUNoBuy, FinalDpUBuyNormal, FinalDpUNoBuyIfParentBought,\
        \ FinalDpUBuyDiscount, UpdatedMemo} = \n                lists:foldl(\n     \
        \               fun(V, {AccDpUNoBuy, AccDpUBuyNormal, AccDpUNoBuyIfParentBought,\
        \ AccDpUBuyDiscount, CurrentMemo}) ->\n                        {ResV, NextMemo}\
        \ = dfs(V, Adj, PresentArr, FutureArr, Budget, CurrentMemo),\n             \
        \           {ResVNoParentBought, ResVParentBought} = ResV,\n\n             \
        \           NextDpUNoBuy = merge_dps(AccDpUNoBuy, ResVNoParentBought, Budget),\n\
        \                        NextDpUBuyNormal = merge_dps(AccDpUBuyNormal, ResVParentBought,\
        \ Budget),\n                        NextDpUNoBuyIfParentBought = merge_dps(AccDpUNoBuyIfParentBought,\
        \ ResVNoParentBought, Budget),\n                        NextDpUBuyDiscount =\
        \ merge_dps(AccDpUBuyDiscount, ResVParentBought, Budget),\n                \
        \        {NextDpUNoBuy, NextDpUBuyNormal, NextDpUNoBuyIfParentBought, NextDpUBuyDiscount,\
        \ NextMemo}\n                    end,\n                    {CurrentDpUNoBuy,\
        \ UpdatedCurrentDpUBuyNormal, CurrentDpUNoBuyIfParentBought, UpdatedCurrentDpUBuyDiscount,\
        \ Memo},\n                    maps:get(U, Adj, [])\n                ),\n\n \
        \           FinalDpNoParentBought = make_dp_array(Budget),\n            FinalDpNoParentBoughtResult\
        \ = \n                lists:foldl(\n                    fun(K, AccDp) ->\n \
        \                       Val1 = array:get(K, FinalDpUNoBuy),\n              \
        \          Val2 = array:get(K, FinalDpUBuyNormal),\n                       \
        \ array:set(K, max(Val1, Val2), AccDp)\n                    end,\n         \
        \           FinalDpNoParentBought,\n                    lists:seq(0, Budget)\n\
        \                ),\n\n            FinalDpParentBought = make_dp_array(Budget),\n\
        \            FinalDpParentBoughtResult = \n                lists:foldl(\n  \
        \                  fun(K, AccDp) ->\n                        Val1 = array:get(K,\
        \ FinalDpUNoBuyIfParentBought),\n                        Val2 = array:get(K,\
        \ FinalDpUBuyDiscount),\n                        array:set(K, max(Val1, Val2),\
        \ AccDp)\n                    end,\n                    FinalDpParentBought,\n\
        \                    lists:seq(0, Budget)\n                ),\n\n          \
        \  Result = {FinalDpNoParentBoughtResult, FinalDpParentBoughtResult},\n    \
        \        {Result, maps:put(U, Result, UpdatedMemo)}\n    end.\n\nmax_profit(N,\
        \ Present, Future, Hierarchy, Budget) ->\n    Adj = lists:foldl(\n        fun([U,\
        \ V], Acc) ->\n            maps:update_with(U, fun(List) -> [V | List] end,\
        \ [V], Acc)\n        end,\n        #{} ,\n        Hierarchy\n    ),\n\n    PresentArr\
        \ = array:from_list(Present),\n    FutureArr = array:from_list(Future),\n\n\
        \    {RootRes, _FinalMemo} = dfs(1, Adj, PresentArr, FutureArr, Budget, #{}),\n\
        \    {FinalDpRootNoParentBought, _} = RootRes,\n\n    MaxOverallProfit = \n\
        \        lists:foldl(\n            fun(K, AccMax) ->\n                Profit\
        \ = array:get(K, FinalDpRootNoParentBought),\n                if Profit =/=\
        \ ?NEG_INF -> max(AccMax, Profit);\n                true -> AccMax\n       \
        \         end\n            end,\n            0,\n            lists:seq(0, Budget)\n\
        \        ),\n    MaxOverallProfit."
      elixir: "defmodule Solution do\n  @neg_inf -1_000_000_000 # A sufficiently small\
        \ number\n\n  # Helper function to create a DP array initialized with @neg_inf,\
        \ 0 at index 0\n  defp make_dp_array(budget) do\n    array = :array.new([{:fixed,\
        \ true}, {:size, budget + 1}, {:default, @neg_inf}])\n    :array.set(0, 0, array)\n\
        \  end\n\n  # Helper function to merge two DP arrays (knapsack-style combination)\n\
        \  defp merge_dps(dp1, dp2, budget) do\n    new_dp = make_dp_array(budget)\n\
        \    merge_dps_loop(0, dp1, dp2, new_dp, budget)\n  end\n\n  defp merge_dps_loop(k1,\
        \ dp1, dp2, new_dp, budget) when k1 <= budget do\n    val1 = :array.get(k1,\
        \ dp1)\n    case val1 do\n      @neg_inf -> merge_dps_loop(k1 + 1, dp1, dp2,\
        \ new_dp, budget)\n      _ ->\n        new_dp2 = merge_dps_inner_loop(k1, 0,\
        \ val1, dp2, new_dp, budget)\n        merge_dps_loop(k1 + 1, dp1, dp2, new_dp2,\
        \ budget)\n    end\n  end\n  defp merge_dps_loop(_k1, _dp1, _dp2, new_dp, _budget)\
        \ do\n    new_dp\n  end\n\n  defp merge_dps_inner_loop(k1, k2, val1, dp2, new_dp,\
        \ budget) when k1 + k2 <= budget do\n    val2 = :array.get(k2, dp2)\n    case\
        \ val2 do\n      @neg_inf -> merge_dps_inner_loop(k1, k2 + 1, val1, dp2, new_dp,\
        \ budget)\n      _ ->\n        current_max = :array.get(k1 + k2, new_dp)\n \
        \       new_val = val1 + val2\n        updated_new_dp = :array.set(k1 + k2,\
        \ max(current_max, new_val), new_dp)\n        merge_dps_inner_loop(k1, k2 +\
        \ 1, val1, dp2, updated_new_dp, budget)\n    end\n  end\n  defp merge_dps_inner_loop(_k1,\
        \ _k2, _val1, _dp2, new_dp, _budget) do\n    new_dp\n  end\n\n  # DFS function\n\
        \  defp dfs(u, adj, present_arr, future_arr, budget, memo) do\n    case Map.fetch(memo,\
        \ u) do\n      {:ok, result} -> {result, memo}\n      :error ->\n        current_dp_u_no_buy\
        \ = make_dp_array(budget)\n\n        cost_u_normal = :array.get(u - 1, present_arr)\n\
        \        profit_u_normal = :array.get(u - 1, future_arr) - cost_u_normal\n \
        \       current_dp_u_buy_normal = make_dp_array(budget)\n        updated_current_dp_u_buy_normal\
        \ = \n          if cost_u_normal <= budget, do: :array.set(cost_u_normal, profit_u_normal,\
        \ current_dp_u_buy_normal),\n          else: current_dp_u_buy_normal\n\n   \
        \     current_dp_u_no_buy_if_parent_bought = make_dp_array(budget)\n\n     \
        \   cost_u_discount = div(:array.get(u - 1, present_arr), 2)\n        profit_u_discount\
        \ = :array.get(u - 1, future_arr) - cost_u_discount\n        current_dp_u_buy_discount\
        \ = make_dp_array(budget)\n        updated_current_dp_u_buy_discount = \n  \
        \        if cost_u_discount <= budget, do: :array.set(cost_u_discount, profit_u_discount,\
        \ current_dp_u_buy_discount),\n          else: current_dp_u_buy_discount\n\n\
        \        {final_dp_u_no_buy, final_dp_u_buy_normal, final_dp_u_no_buy_if_parent_bought,\
        \ final_dp_u_buy_discount, updated_memo} = \n          Enum.reduce(\n      \
        \      Map.get(adj, u, []),\n            {current_dp_u_no_buy, updated_current_dp_u_buy_normal,\
        \ current_dp_u_no_buy_if_parent_bought, updated_current_dp_u_buy_discount, memo},\n\
        \            fn v, {acc_dp_u_no_buy, acc_dp_u_buy_normal, acc_dp_u_no_buy_if_parent_bought,\
        \ acc_dp_u_buy_discount, current_memo} ->\n              {res_v, next_memo}\
        \ = dfs(v, adj, present_arr, future_arr, budget, current_memo)\n           \
        \   {res_v_no_parent_bought, res_v_parent_bought} = res_v\n\n              next_dp_u_no_buy\
        \ = merge_dps(acc_dp_u_no_buy, res_v_no_parent_bought, budget)\n           \
        \   next_dp_u_buy_normal = merge_dps(acc_dp_u_buy_normal, res_v_parent_bought,\
        \ budget)\n              next_dp_u_no_buy_if_parent_bought = merge_dps(acc_dp_u_no_buy_if_parent_bought,\
        \ res_v_no_parent_bought, budget)\n              next_dp_u_buy_discount = merge_dps(acc_dp_u_buy_discount,\
        \ res_v_parent_bought, budget)\n              {next_dp_u_no_buy, next_dp_u_buy_normal,\
        \ next_dp_u_no_buy_if_parent_bought, next_dp_u_buy_discount, next_memo}\n  \
        \          end\n          )\n\n        final_dp_no_parent_bought = make_dp_array(budget)\n\
        \        final_dp_no_parent_bought_result = \n          Enum.reduce(0..budget,\
        \ final_dp_no_parent_bought, fn k, acc_dp ->\n            val1 = :array.get(k,\
        \ final_dp_u_no_buy)\n            val2 = :array.get(k, final_dp_u_buy_normal)\n\
        \            :array.set(k, max(val1, val2), acc_dp)\n          end)\n\n    \
        \    final_dp_parent_bought = make_dp_array(budget)\n        final_dp_parent_bought_result\
        \ = \n          Enum.reduce(0..budget, final_dp_parent_bought, fn k, acc_dp\
        \ ->\n            val1 = :array.get(k, final_dp_u_no_buy_if_parent_bought)\n\
        \            val2 = :array.get(k, final_dp_u_buy_discount)\n            :array.set(k,\
        \ max(val1, val2), acc_dp)\n          end)\n\n        result = {final_dp_no_parent_bought_result,\
        \ final_dp_parent_bought_result}\n        {result, Map.put(updated_memo, u,\
        \ result)}\n    end\n  end\n\n  def max_profit(_n, present, future, hierarchy,\
        \ budget) do\n    adj = \n      Enum.reduce(hierarchy, %{}, fn [u, v], acc ->\n\
        \        Map.update(acc, u, [v], fn list -> [v | list] end)\n      end)\n\n\
        \    present_arr = :array.from_list(present)\n    future_arr = :array.from_list(future)\n\
        \n    {root_res, _final_memo} = dfs(1, adj, present_arr, future_arr, budget,\
        \ %{})\n    {final_dp_root_no_parent_bought, _} = root_res\n\n    max_overall_profit\
        \ = \n      Enum.reduce(0..budget, 0, fn k, acc_max ->\n        profit = :array.get(k,\
        \ final_dp_root_no_parent_bought)\n        if profit != @neg_inf, do: max(acc_max,\
        \ profit), else: acc_max\n      end)\n    max_overall_profit\n  end\nend"
    approach: 'The problem is a variation of the tree knapsack problem, where the decision
      for an employee to buy stock (and at what price) depends on their direct boss''s
      decision. This suggests a dynamic programming approach on the tree structure.
      For each employee (node `u`), we need to compute two DP states: one assuming `u`''s
      direct boss did not buy their stock, and another assuming `u`''s direct boss did
      buy their stock (enabling a discount for `u`). Each DP state is an array `dp[k]`
      representing the maximum profit achievable using exactly `k` budget within the
      subtree rooted at `u`.'
    time_complexity: The time complexity is O(N * Budget^2). For each of the N employees,
      the DFS function is called once. Inside the DFS, when combining results from children,
      we iterate through the budget `k1` for the current node's accumulated DP and `k2`
      for the child's DP. This nested loop runs up to `Budget * Budget` times for each
      child. Since the total sum of subtree sizes for all children of a node is at most
      N, and each merge operation takes O(Budget^2) time, the total time complexity
      for processing all nodes in the tree is O(N * Budget^2). Given N=160 and Budget=160,
      this is 160^3 = 4,096,000 operations, which is efficient enough.
    space_complexity: The space complexity is O(N * Budget). The adjacency list for
      the hierarchy takes O(N) space. The memoization table stores results for N nodes.
      Each result consists of two DP arrays, each of size `Budget + 1`. Therefore, the
      total space for memoization is O(N * Budget). Given N=160 and Budget=160, this
      is 160 * 160 = 25,600 integer entries, which is well within typical memory limits.
    elapsed_time: 192.30022978782654
    model: gemini-2.5-flash
    generated_at: '2025-12-16 01:11:11 '
  - solutions:
      cpp: "class Solution {\npublic:\n    int maxProfit(int n, vector<int>& present,\
        \ vector<int>& future, vector<vector<int>>& hierarchy, int budget) {\n     \
        \   vector<vector<int>> tree(n);\n        for (auto& edge : hierarchy) {\n \
        \           tree[edge[0] - 1].push_back(edge[1] - 1);\n        }\n        vector<int>\
        \ max_profit(n, 0), max_profit1(n, 0);\n        dfs(0, tree, present, future,\
        \ max_profit, max_profit1, budget);\n        return max_profit[0];\n    }\n\
        \    void dfs(int node, vector<vector<int>>& tree, vector<int>& present, vector<int>&\
        \ future, vector<int>& max_profit, vector<int>& max_profit1, int budget) {\n\
        \        max_profit[node] = 0;\n        max_profit1[node] = 0;\n        for\
        \ (int child : tree[node]) {\n            dfs(child, tree, present, future,\
        \ max_profit, max_profit1, budget);\n            max_profit[node] += max_profit[child];\n\
        \            max_profit1[node] += max_profit1[child];\n        }\n        if\
        \ (present[node] <= budget) {\n            max_profit[node] = max(max_profit[node],\
        \ future[node] - present[node]);\n        }\n        if (node > 0 && present[node]\
        \ / 2 <= budget) {\n            max_profit1[node] = max(max_profit1[node], future[node]\
        \ - present[node] / 2);\n        }\n    }\n};"
      java: "class Solution {\n    public int maxProfit(int n, int[] present, int[]\
        \ future, int[][] hierarchy, int budget) {\n        int[][] tree = new int[n][];\n\
        \        for (int i = 0; i < n; i++) {\n            tree[i] = new int[0];\n\
        \        }\n        for (int[] edge : hierarchy) {\n            int[] temp =\
        \ new int[tree[edge[0] - 1].length + 1];\n            System.arraycopy(tree[edge[0]\
        \ - 1], 0, temp, 0, tree[edge[0] - 1].length);\n            temp[temp.length\
        \ - 1] = edge[1] - 1;\n            tree[edge[0] - 1] = temp;\n        }\n  \
        \      int[] max_profit = new int[n], max_profit1 = new int[n];\n        dfs(0,\
        \ tree, present, future, max_profit, max_profit1, budget);\n        return max_profit[0];\n\
        \    }\n    void dfs(int node, int[][] tree, int[] present, int[] future, int[]\
        \ max_profit, int[] max_profit1, int budget) {\n        max_profit[node] = 0;\n\
        \        max_profit1[node] = 0;\n        for (int child : tree[node]) {\n  \
        \          dfs(child, tree, present, future, max_profit, max_profit1, budget);\n\
        \            max_profit[node] += max_profit[child];\n            max_profit1[node]\
        \ += max_profit1[child];\n        }\n        if (present[node] <= budget) {\n\
        \            max_profit[node] = Math.max(max_profit[node], future[node] - present[node]);\n\
        \        }\n        if (node > 0 && present[node] / 2 <= budget) {\n       \
        \     max_profit1[node] = Math.max(max_profit1[node], future[node] - present[node]\
        \ / 2);\n        }\n    }\n}"
      python: "class Solution:\n    def maxProfit(self, n: int, present: list[int],\
        \ future: list[int], hierarchy: list[list[int]], budget: int) -> int:\n    \
        \    tree = [[] for _ in range(n)]\n        for u, v in hierarchy:\n       \
        \     tree[u - 1].append(v - 1)\n        max_profit = [0] * n\n        max_profit1\
        \ = [0] * n\n        self.dfs(0, tree, present, future, max_profit, max_profit1,\
        \ budget)\n        return max_profit[0]\n    def dfs(self, node: int, tree:\
        \ list[list[int]], present: list[int], future: list[int], max_profit: list[int],\
        \ max_profit1: list[int], budget: int) -> None:\n        max_profit[node] =\
        \ 0\n        max_profit1[node] = 0\n        for child in tree[node]:\n     \
        \       self.dfs(child, tree, present, future, max_profit, max_profit1, budget)\n\
        \            max_profit[node] += max_profit[child]\n            max_profit1[node]\
        \ += max_profit1[child]\n        if present[node] <= budget:\n            max_profit[node]\
        \ = max(max_profit[node], future[node] - present[node])\n        if node > 0\
        \ and present[node] // 2 <= budget:\n            max_profit1[node] = max(max_profit1[node],\
        \ future[node] - present[node] // 2)"
      python3: "class Solution:\n    def maxProfit(self, n: int, present: list[int],\
        \ future: list[int], hierarchy: list[list[int]], budget: int) -> int:\n    \
        \    tree = [[] for _ in range(n)]\n        for u, v in hierarchy:\n       \
        \     tree[u - 1].append(v - 1)\n        max_profit = [0] * n\n        max_profit1\
        \ = [0] * n\n        self.dfs(0, tree, present, future, max_profit, max_profit1,\
        \ budget)\n        return max_profit[0]\n    def dfs(self, node: int, tree:\
        \ list[list[int]], present: list[int], future: list[int], max_profit: list[int],\
        \ max_profit1: list[int], budget: int) -> None:\n        max_profit[node] =\
        \ 0\n        max_profit1[node] = 0\n        for child in tree[node]:\n     \
        \       self.dfs(child, tree, present, future, max_profit, max_profit1, budget)\n\
        \            max_profit[node] += max_profit[child]\n            max_profit1[node]\
        \ += max_profit1[child]\n        if present[node] <= budget:\n            max_profit[node]\
        \ = max(max_profit[node], future[node] - present[node])\n        if node > 0\
        \ and present[node] // 2 <= budget:\n            max_profit1[node] = max(max_profit1[node],\
        \ future[node] - present[node] // 2)"
      c: "typedef struct {\n    int* data;\n    int size;\n} Array;\n\nArray* createArray(int\
        \ size) {\n    Array* arr = malloc(sizeof(Array));\n    arr->data = malloc(size\
        \ * sizeof(int));\n    arr->size = size;\n    return arr;\n}\n\nvoid freeArray(Array*\
        \ arr) {\n    free(arr->data);\n    free(arr);\n}\n\ntypedef struct {\n    Array**\
        \ data;\n    int size;\n} Array2D;\n\nArray2D* createArray2D(int size) {\n \
        \   Array2D* arr = malloc(sizeof(Array2D));\n    arr->data = malloc(size * sizeof(Array*));\n\
        \    arr->size = size;\n    return arr;\n}\n\nvoid freeArray2D(Array2D* arr)\
        \ {\n    for (int i = 0; i < arr->size; i++) {\n        freeArray(arr->data[i]);\n\
        \    }\n    free(arr->data);\n    free(arr);\n}\n\nint maxProfit(int n, int*\
        \ present, int* future, int** hierarchy, int hierarchySize, int budget) {\n\
        \    Array2D* tree = createArray2D(n);\n    for (int i = 0; i < n; i++) {\n\
        \        tree->data[i] = createArray(0);\n    }\n    for (int i = 0; i < hierarchySize;\
        \ i++) {\n        int u = hierarchy[i][0] - 1;\n        int v = hierarchy[i][1]\
        \ - 1;\n        tree->data[u]->size++;\n        tree->data[u]->data = realloc(tree->data[u]->data,\
        \ tree->data[u]->size * sizeof(int));\n        tree->data[u]->data[tree->data[u]->size\
        \ - 1] = v;\n    }\n    int* max_profit = malloc(n * sizeof(int));\n    int*\
        \ max_profit1 = malloc(n * sizeof(int));\n    dfs(0, tree, present, future,\
        \ max_profit, max_profit1, budget);\n    int result = max_profit[0];\n    free(max_profit);\n\
        \    free(max_profit1);\n    freeArray2D(tree);\n    return result;\n}\n\nvoid\
        \ dfs(int node, Array2D* tree, int* present, int* future, int* max_profit, int*\
        \ max_profit1, int budget) {\n    max_profit[node] = 0;\n    max_profit1[node]\
        \ = 0;\n    for (int i = 0; i < tree->data[node]->size; i++) {\n        int\
        \ child = tree->data[node]->data[i];\n        dfs(child, tree, present, future,\
        \ max_profit, max_profit1, budget);\n        max_profit[node] += max_profit[child];\n\
        \        max_profit1[node] += max_profit1[child];\n    }\n    if (present[node]\
        \ <= budget) {\n        max_profit[node] = (max_profit[node] > future[node]\
        \ - present[node]) ? max_profit[node] : future[node] - present[node];\n    }\n\
        \    if (node > 0 && present[node] / 2 <= budget) {\n        max_profit1[node]\
        \ = (max_profit1[node] > future[node] - present[node] / 2) ? max_profit1[node]\
        \ : future[node] - present[node] / 2;\n    }\n}"
      csharp: "public class Solution {\n    public int MaxProfit(int n, int[] present,\
        \ int[] future, int[][] hierarchy, int budget) {\n        List<int>[] tree =\
        \ new List<int>[n];\n        for (int i = 0; i < n; i++) {\n            tree[i]\
        \ = new List<int>();\n        }\n        foreach (int[] edge in hierarchy) {\n\
        \            tree[edge[0] - 1].Add(edge[1] - 1);\n        }\n        int[] max_profit\
        \ = new int[n];\n        int[] max_profit1 = new int[n];\n        Dfs(0, tree,\
        \ present, future, max_profit, max_profit1, budget);\n        return max_profit[0];\n\
        \    }\n    void Dfs(int node, List<int>[] tree, int[] present, int[] future,\
        \ int[] max_profit, int[] max_profit1, int budget) {\n        max_profit[node]\
        \ = 0;\n        max_profit1[node] = 0;\n        foreach (int child in tree[node])\
        \ {\n            Dfs(child, tree, present, future, max_profit, max_profit1,\
        \ budget);\n            max_profit[node] += max_profit[child];\n           \
        \ max_profit1[node] += max_profit1[child];\n        }\n        if (present[node]\
        \ <= budget) {\n            max_profit[node] = Math.Max(max_profit[node], future[node]\
        \ - present[node]);\n        }\n        if (node > 0 && present[node] / 2 <=\
        \ budget) {\n            max_profit1[node] = Math.Max(max_profit1[node], future[node]\
        \ - present[node] / 2);\n        }\n    }\n}"
      javascript: "var maxProfit = function(n, present, future, hierarchy, budget) {\n\
        \    let tree = Array(n).fill(0).map(() => []);\n    for (let [u, v] of hierarchy)\
        \ {\n        tree[u - 1].push(v - 1);\n    }\n    let max_profit = Array(n).fill(0);\n\
        \    let max_profit1 = Array(n).fill(0);\n    dfs(0, tree, present, future,\
        \ max_profit, max_profit1, budget);\n    return max_profit[0];\n};\n\nfunction\
        \ dfs(node, tree, present, future, max_profit, max_profit1, budget) {\n    max_profit[node]\
        \ = 0;\n    max_profit1[node] = 0;\n    for (let child of tree[node]) {\n  \
        \      dfs(child, tree, present, future, max_profit, max_profit1, budget);\n\
        \        max_profit[node] += max_profit[child];\n        max_profit1[node] +=\
        \ max_profit1[child];\n    }\n    if (present[node] <= budget) {\n        max_profit[node]\
        \ = Math.max(max_profit[node], future[node] - present[node]);\n    }\n    if\
        \ (node > 0 && present[node] / 2 <= budget) {\n        max_profit1[node] = Math.max(max_profit1[node],\
        \ future[node] - present[node] / 2);\n    }\n}"
      typescript: "function maxProfit(n: number, present: number[], future: number[],\
        \ hierarchy: number[][], budget: number): number {\n    let tree: number[][]\
        \ = Array(n).fill(0).map(() => []);\n    for (let [u, v] of hierarchy) {\n \
        \       tree[u - 1].push(v - 1);\n    }\n    let max_profit: number[] = Array(n).fill(0);\n\
        \    let max_profit1: number[] = Array(n).fill(0);\n    dfs(0, tree, present,\
        \ future, max_profit, max_profit1, budget);\n    return max_profit[0];\n}\n\n\
        function dfs(node: number, tree: number[][], present: number[], future: number[],\
        \ max_profit: number[], max_profit1: number[], budget: number): void {\n   \
        \ max_profit[node] = 0;\n    max_profit1[node] = 0;\n    for (let child of tree[node])\
        \ {\n        dfs(child, tree, present, future, max_profit, max_profit1, budget);\n\
        \        max_profit[node] += max_profit[child];\n        max_profit1[node] +=\
        \ max_profit1[child];\n    }\n    if (present[node] <= budget) {\n        max_profit[node]\
        \ = Math.max(max_profit[node], future[node] - present[node]);\n    }\n    if\
        \ (node > 0 && present[node] / 2 <= budget) {\n        max_profit1[node] = Math.max(max_profit1[node],\
        \ future[node] - present[node] / 2);\n    }\n}"
      php: "function maxProfit($n, $present, $future, $hierarchy, $budget) {\n    $tree\
        \ = array_fill(0, $n, []);\n    foreach ($hierarchy as $edge) {\n        $tree[$edge[0]\
        \ - 1][] = $edge[1] - 1;\n    }\n    $max_profit = array_fill(0, $n, 0);\n \
        \   $max_profit1 = array_fill(0, $n, 0);\n    dfs(0, $tree, $present, $future,\
        \ $max_profit, $max_profit1, $budget);\n    return $max_profit[0];\n}\n\nfunction\
        \ dfs($node, &$tree, $present, $future, &$max_profit, &$max_profit1, $budget)\
        \ {\n    $max_profit[$node] = 0;\n    $max_profit1[$node] = 0;\n    foreach\
        \ ($tree[$node] as $child) {\n        dfs($child, $tree, $present, $future,\
        \ $max_profit, $max_profit1, $budget);\n        $max_profit[$node] += $max_profit[$child];\n\
        \        $max_profit1[$node] += $max_profit1[$child];\n    }\n    if ($present[$node]\
        \ <= $budget) {\n        $max_profit[$node] = max($max_profit[$node], $future[$node]\
        \ - $present[$node]);\n    }\n    if ($node > 0 && $present[$node] / 2 <= $budget)\
        \ {\n        $max_profit1[$node] = max($max_profit1[$node], $future[$node] -\
        \ $present[$node] / 2);\n    }\n}"
      swift: "func maxProfit(_ n: Int, _ present: [Int], _ future: [Int], _ hierarchy:\
        \ [[Int]], _ budget: Int) -> Int {\n    var tree: [[Int]] = Array(repeating:\
        \ [], count: n)\n    for edge in hierarchy {\n        tree[edge[0] - 1].append(edge[1]\
        \ - 1)\n    }\n    var max_profit: [Int] = Array(repeating: 0, count: n)\n \
        \   var max_profit1: [Int] = Array(repeating: 0, count: n)\n    dfs(0, &tree,\
        \ present, future, &max_profit, &max_profit1, budget)\n    return max_profit[0]\n\
        }\n\nfunc dfs(_ node: Int, _ tree: inout [[Int]], _ present: [Int], _ future:\
        \ [Int], _ max_profit: inout [Int], _ max_profit1: inout [Int], _ budget: Int)\
        \ {\n    max_profit[node] = 0\n    max_profit1[node] = 0\n    for child in tree[node]\
        \ {\n        dfs(child, &tree, present, future, &max_profit, &max_profit1, budget)\n\
        \        max_profit[node] += max_profit[child]\n        max_profit1[node] +=\
        \ max_profit1[child]\n    }\n    if present[node] <= budget {\n        max_profit[node]\
        \ = max(max_profit[node], future[node] - present[node])\n    }\n    if node\
        \ > 0 && present[node] / 2 <= budget {\n        max_profit1[node] = max(max_profit1[node],\
        \ future[node] - present[node] / 2)\n    }\n}"
      kotlin: "fun maxProfit(n: Int, present: IntArray, future: IntArray, hierarchy:\
        \ Array<IntArray>, budget: Int): Int {\n    val tree: Array<MutableList<Int>>\
        \ = Array(n) { mutableListOf() }\n    for ((u, v) in hierarchy) {\n        tree[u\
        \ - 1].add(v - 1)\n    }\n    val max_profit = IntArray(n)\n    val max_profit1\
        \ = IntArray(n)\n    dfs(0, tree, present, future, max_profit, max_profit1,\
        \ budget)\n    return max_profit[0]\n}\n\nfun dfs(node: Int, tree: Array<MutableList<Int>>,\
        \ present: IntArray, future: IntArray, max_profit: IntArray, max_profit1: IntArray,\
        \ budget: Int) {\n    max_profit[node] = 0\n    max_profit1[node] = 0\n    for\
        \ (child in tree[node]) {\n        dfs(child, tree, present, future, max_profit,\
        \ max_profit1, budget)\n        max_profit[node] += max_profit[child]\n    \
        \    max_profit1[node] += max_profit1[child]\n    }\n    if (present[node] <=\
        \ budget) {\n        max_profit[node] = maxOf(max_profit[node], future[node]\
        \ - present[node])\n    }\n    if (node > 0 && present[node] / 2 <= budget)\
        \ {\n        max_profit1[node] = maxOf(max_profit1[node], future[node] - present[node]\
        \ / 2)\n    }\n}"
      dart: "int maxProfit(int n, List<int> present, List<int> future, List<List<int>>\
        \ hierarchy, int budget) {\n    List<List<int>> tree = List.generate(n, (index)\
        \ => []);\n    for (var edge in hierarchy) {\n        tree[edge[0] - 1].add(edge[1]\
        \ - 1);\n    }\n    List<int> max_profit = List.generate(n, (index) => 0);\n\
        \    List<int> max_profit1 = List.generate(n, (index) => 0);\n    dfs(0, tree,\
        \ present, future, max_profit, max_profit1, budget);\n    return max_profit[0];\n\
        }\n\nvoid dfs(int node, List<List<int>> tree, List<int> present, List<int> future,\
        \ List<int> max_profit, List<int> max_profit1, int budget) {\n    max_profit[node]\
        \ = 0;\n    max_profit1[node] = 0;\n    for (var child in tree[node]) {\n  \
        \      dfs(child, tree, present, future, max_profit, max_profit1, budget);\n\
        \        max_profit[node] += max_profit[child];\n        max_profit1[node] +=\
        \ max_profit1[child];\n    }\n    if (present[node] <= budget) {\n        max_profit[node]\
        \ = max(max_profit[node], future[node] - present[node]);\n    }\n    if (node\
        \ > 0 && present[node] / 2 <= budget) {\n        max_profit1[node] = max(max_profit1[node],\
        \ future[node] - present[node] / 2);\n    }\n}"
      go: "package main\n\nimport (\n    \"fmt\"\n)\n\ntype Solution struct{}\n\nfunc\
        \ (s *Solution) maxProfit(n int, present []int, future []int, hierarchy [][]int,\
        \ budget int) int {\n    tree := make([][]int, n)\n    for _, edge := range\
        \ hierarchy {\n        tree[edge[0]-1] = append(tree[edge[0]-1], edge[1]-1)\n\
        \    }\n    max_profit := make([]int, n)\n    max_profit1 := make([]int, n)\n\
        \    s.dfs(0, tree, present, future, max_profit, max_profit1, budget)\n    return\
        \ max_profit[0]\n}\n\nfunc (s *Solution) dfs(node int, tree [][]int, present\
        \ []int, future []int, max_profit []int, max_profit1 []int, budget int) {\n\
        \    max_profit[node] = 0\n    max_profit1[node] = 0\n    for _, child := range\
        \ tree[node] {\n        s.dfs(child, tree, present, future, max_profit, max_profit1,\
        \ budget)\n        max_profit[node] += max_profit[child]\n        max_profit1[node]\
        \ += max_profit1[child]\n    }\n    if present[node] <= budget {\n        max_profit[node]\
        \ = max(max_profit[node], future[node]-present[node])\n    }\n    if node >\
        \ 0 && present[node]/2 <= budget {\n        max_profit1[node] = max(max_profit1[node],\
        \ future[node]-present[node]/2)\n    }\n}\n\nfunc max(a, b int) int {\n    if\
        \ a > b {\n        return a\n    }\n    return b\n}"
      ruby: "def max_profit(n, present, future, hierarchy, budget)\n    tree = Array.new(n)\
        \ { [] }\n    hierarchy.each do |edge|\n        tree[edge[0] - 1] << edge[1]\
        \ - 1\n    end\n    max_profit = Array.new(n, 0)\n    max_profit1 = Array.new(n,\
        \ 0)\n    dfs(0, tree, present, future, max_profit, max_profit1, budget)\n \
        \   max_profit[0]\nend\n\ndef dfs(node, tree, present, future, max_profit, max_profit1,\
        \ budget)\n    max_profit[node] = 0\n    max_profit1[node] = 0\n    tree[node].each\
        \ do |child|\n        dfs(child, tree, present, future, max_profit, max_profit1,\
        \ budget)\n        max_profit[node] += max_profit[child]\n        max_profit1[node]\
        \ += max_profit1[child]\n    end\n    if present[node] <= budget\n        max_profit[node]\
        \ = [max_profit[node], future[node] - present[node]].max\n    end\n    if node\
        \ > 0 && present[node] / 2 <= budget\n        max_profit1[node] = [max_profit1[node],\
        \ future[node] - present[node] / 2].max\n    end\nend"
      scala: "object Solution {\n    def maxProfit(n: Int, present: Array[Int], future:\
        \ Array[Int], hierarchy: Array[Array[Int]], budget: Int): Int = {\n        val\
        \ tree: Array[Array[Int]] = Array.fill(n)(Array[Int]())\n        for (edge <-\
        \ hierarchy) {\n            tree(edge(0) - 1) = tree(edge(0) - 1) :+ (edge(1)\
        \ - 1)\n        }\n        val max_profit = Array.fill(n)(0)\n        val max_profit1\
        \ = Array.fill(n)(0)\n        dfs(0, tree, present, future, max_profit, max_profit1,\
        \ budget)\n        max_profit(0)\n    }\n\n    def dfs(node: Int, tree: Array[Array[Int]],\
        \ present: Array[Int], future: Array[Int], max_profit: Array[Int], max_profit1:\
        \ Array[Int], budget: Int): Unit = {\n        max_profit(node) = 0\n       \
        \ max_profit1(node) = 0\n        for (child <- tree(node)) {\n            dfs(child,\
        \ tree, present, future, max_profit, max_profit1, budget)\n            max_profit(node)\
        \ += max_profit(child)\n            max_profit1(node) += max_profit1(child)\n\
        \        }\n        if (present(node) <= budget) {\n            max_profit(node)\
        \ = math.max(max_profit(node), future(node) - present(node))\n        }\n  \
        \      if (node > 0 && present(node) / 2 <= budget) {\n            max_profit1(node)\
        \ = math.max(max_profit1(node), future(node) - present(node) / 2)\n        }\n\
        \    }\n}"
      rust: "struct Solution;\n\nimpl Solution {\n    pub fn max_profit(n: i32, present:\
        \ Vec<i32>, future: Vec<i32>, hierarchy: Vec<Vec<i32>>, budget: i32) -> i32\
        \ {\n        let mut tree: Vec<Vec<i32>> = vec![vec![]; n as usize];\n     \
        \   for edge in hierarchy {\n            tree[(edge[0] - 1) as usize].push(edge[1]\
        \ - 1);\n        }\n        let mut max_profit: Vec<i32> = vec![0; n as usize];\n\
        \        let mut max_profit1: Vec<i32> = vec![0; n as usize];\n        Self::dfs(0,\
        \ &mut tree, &present, &future, &mut max_profit, &mut max_profit1, budget);\n\
        \        max_profit[0]\n    }\n\n    fn dfs(node: i32, tree: &mut Vec<Vec<i32>>,\
        \ present: &Vec<i32>, future: &Vec<i32>, max_profit: &mut Vec<i32>, max_profit1:\
        \ &mut Vec<i32>, budget: i32) {\n        max_profit[node as usize] = 0;\n  \
        \      max_profit1[node as usize] = 0;\n        for child in &tree[node as usize]\
        \ {\n            Self::dfs(*child, tree, present, future, max_profit, max_profit1,\
        \ budget);\n            max_profit[node as usize] += max_profit[*child as usize];\n\
        \            max_profit1[node as usize] += max_profit1[*child as usize];\n \
        \       }\n        if present[node as usize] <= budget {\n            max_profit[node\
        \ as usize] = std::cmp::max(max_profit[node as usize], future[node as usize]\
        \ - present[node as usize]);\n        }\n        if node > 0 && present[node\
        \ as usize] / 2 <= budget {\n            max_profit1[node as usize] = std::cmp::max(max_profit1[node\
        \ as usize], future[node as usize] - present[node as usize] / 2);\n        }\n\
        \    }\n}"
      racket: "define (max-profit n present future hierarchy budget)\n    (let (\n \
        \       (tree (make-vector n '()))\n        (max_profit (make-vector n 0))\n\
        \        (max_profit1 (make-vector n 0))\n        )\n        (for-each (lambda\
        \ (edge)\n            (vector-set! tree (- (car edge) 1) (cons (- (cadr edge)\
        \ 1) (vector-ref tree (- (car edge) 1))))\n            )\n            hierarchy\n\
        \            )\n        (dfs 0 tree present future max_profit max_profit1 budget)\n\
        \        (vector-ref max_profit 0)\n        )\n\n(define (dfs node tree present\
        \ future max_profit max_profit1 budget)\n    (vector-set! max_profit node 0)\n\
        \    (vector-set! max_profit1 node 0)\n    (for-each (lambda (child)\n     \
        \   (dfs child tree present future max_profit max_profit1 budget)\n        (vector-set!\
        \ max_profit node (+ (vector-ref max_profit node) (vector-ref max_profit child)))\n\
        \        (vector-set! max_profit1 node (+ (vector-ref max_profit1 node) (vector-ref\
        \ max_profit1 child)))\n        )\n        (vector-ref tree node)\n        )\n\
        \    (if (<= (vector-ref present node) budget)\n        (vector-set! max_profit\
        \ node (max (vector-ref max_profit node) (- (vector-ref future node) (vector-ref\
        \ present node))))\n        )\n    (if (and (> node 0) (<= (/ (vector-ref present\
        \ node) 2) budget))\n        (vector-set! max_profit1 node (max (vector-ref\
        \ max_profit1 node) (- (vector-ref future node) (/ (vector-ref present node)\
        \ 2))))\n        )\n    )"
      erlang: "max_profit(N, Present, Future, Hierarchy, Budget) ->\n    Tree = array:new(N,\
        \ {default, []}),\n    lists:foreach(fun({U, V}) ->\n        array:set(U - 1,\
        \ [V - 1 | array:get(U - 1, Tree)], Tree)\n    end, Hierarchy),\n    MaxProfit\
        \ = array:new(N, {default, 0}),\n    MaxProfit1 = array:new(N, {default, 0}),\n\
        \    dfs(0, Tree, Present, Future, MaxProfit, MaxProfit1, Budget),\n    array:get(0,\
        \ MaxProfit).\n\ndfs(Node, Tree, Present, Future, MaxProfit, MaxProfit1, Budget)\
        \ ->\n    array:set(Node, 0, MaxProfit),\n    array:set(Node, 0, MaxProfit1),\n\
        \    lists:foreach(fun(Child) ->\n        dfs(Child, Tree, Present, Future,\
        \ MaxProfit, MaxProfit1, Budget),\n        array:set(Node, array:get(Node, MaxProfit)\
        \ + array:get(Child, MaxProfit), MaxProfit),\n        array:set(Node, array:get(Node,\
        \ MaxProfit1) + array:get(Child, MaxProfit1), MaxProfit1)\n    end, array:get(Node,\
        \ Tree)),\n    if array:get(Node, Present) =< Budget ->\n        array:set(Node,\
        \ max(array:get(Node, MaxProfit), array:get(Node, Future) - array:get(Node,\
        \ Present)), MaxProfit);\n    true -> ok\n    end,\n    if Node > 0 andalso\
        \ array:get(Node, Present) / 2 =< Budget ->\n        array:set(Node, max(array:get(Node,\
        \ MaxProfit1), array:get(Node, Future) - array:get(Node, Present) / 2), MaxProfit1);\n\
        \    true -> ok\n    end."
      elixir: "def max_profit(n, present, future, hierarchy, budget) do\n    tree =\
        \ Enum.reduce(hierarchy, Array.new(n, []), fn [u, v], tree ->\n        Array.update!(tree,\
        \ u - 1, &[v - 1 | Enum.at(tree, u - 1)])\n    end)\n    max_profit = Array.new(n,\
        \ 0)\n    max_profit1 = Array.new(n, 0)\n    dfs(0, tree, present, future, max_profit,\
        \ max_profit1, budget)\n    Enum.at(max_profit, 0)\nend\n\ndef dfs(node, tree,\
        \ present, future, max_profit, max_profit1, budget) do\n    max_profit = Array.update!(max_profit,\
        \ node, 0)\n    max_profit1 = Array.update!(max_profit1, node, 0)\n    Enum.each(Enum.at(tree,\
        \ node), fn child ->\n        dfs(child, tree, present, future, max_profit,\
        \ max_profit1, budget)\n        max_profit = Array.update!(max_profit, node,\
        \ Enum.at(max_profit, node) + Enum.at(max_profit, child))\n        max_profit1\
        \ = Array.update!(max_profit1, node, Enum.at(max_profit1, node) + Enum.at(max_profit1,\
        \ child))\n    end)\n    if Enum.at(present, node) <= budget do\n        max_profit\
        \ = Array.update!(max_profit, node, max(Enum.at(max_profit, node), Enum.at(future,\
        \ node) - Enum.at(present, node)))\n    end\n    if node > 0 and Enum.at(present,\
        \ node) / 2 <= budget do\n        max_profit1 = Array.update!(max_profit1, node,\
        \ max(Enum.at(max_profit1, node), Enum.at(future, node) - Enum.at(present, node)\
        \ / 2))\n    end\n    {max_profit, max_profit1}\nend"
    approach: 'The problem can be solved using a depth-first search (DFS) approach.
      We start by building the hierarchy tree from the given hierarchy list. Then, for
      each node in the tree, we calculate two values: max_profit and max_profit1. max_profit
      represents the maximum profit that can be achieved in the subtree rooted at the
      current node, assuming the parent of the current node has not bought the stock.
      max_profit1 represents the maximum profit that can be achieved in the subtree
      rooted at the current node, assuming the parent of the current node has bought
      the stock. We use these values to determine whether buying the stock for the current
      node will result in a higher profit or not.'
    time_complexity: The time complexity of this solution is O(n), where n is the number
      of employees. This is because we visit each node in the hierarchy tree once during
      the DFS traversal.
    space_complexity: The space complexity of this solution is O(n), where n is the
      number of employees. This is because we need to store the hierarchy tree and the
      max_profit and max_profit1 values for each node in the tree.
    elapsed_time: 15.717079162597656
    model: llama-3.3-70b-versatile
    generated_at: '2025-12-16 01:11:27 '
---

## Problem #3562: Maximum Profit from Trading Stocks with Discounts

**Difficulty:** Hard

**Topics:** Array, Dynamic Programming, Tree, Depth-First Search

## Problem Description

<p>You are given an integer <code>n</code>, representing the number of employees in a company. Each employee is assigned a unique ID from 1 to <code>n</code>, and employee 1 is the CEO. You are given two <strong>1-based </strong>integer arrays, <code>present</code> and <code>future</code>, each of length <code>n</code>, where:</p>

<ul>
	<li><code>present[i]</code> represents the <strong>current</strong> price at which the <code>i<sup>th</sup></code> employee can buy a stock today.</li>
	<li><code>future[i]</code> represents the <strong>expected</strong> price at which the <code>i<sup>th</sup></code> employee can sell the stock tomorrow.</li>
</ul>

<p>The company&#39;s hierarchy is represented by a 2D integer array <code>hierarchy</code>, where <code>hierarchy[i] = [u<sub>i</sub>, v<sub>i</sub>]</code> means that employee <code>u<sub>i</sub></code> is the direct boss of employee <code>v<sub>i</sub></code>.</p>

<p>Additionally, you have an integer <code>budget</code> representing the total funds available for investment.</p>

<p>However, the company has a discount policy: if an employee&#39;s direct boss purchases their own stock, then the employee can buy their stock at <strong>half</strong> the original price (<code>floor(present[v] / 2)</code>).</p>

<p>Return the <strong>maximum</strong> profit that can be achieved without exceeding the given budget.</p>

<p><strong>Note:</strong></p>

<ul>
	<li>You may buy each stock at most <strong>once</strong>.</li>
	<li>You <strong>cannot</strong> use any profit earned from future stock prices to fund additional investments and must buy only from <code>budget</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 2, present = [1,2], future = [4,3], hierarchy = [[1,2]], budget = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">5</span></p>

<p><strong>Explanation:</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2025/04/09/screenshot-2025-04-10-at-053641.png" style="width: 200px; height: 80px;" /></p>

<ul>
	<li>Employee 1 buys the stock at price 1 and earns a profit of <code>4 - 1 = 3</code>.</li>
	<li>Since Employee 1 is the direct boss of Employee 2, Employee 2 gets a discounted price of <code>floor(2 / 2) = 1</code>.</li>
	<li>Employee 2 buys the stock at price 1 and earns a profit of <code>3 - 1 = 2</code>.</li>
	<li>The total buying cost is <code>1 + 1 = 2 &lt;= budget</code>. Thus, the maximum total profit achieved is <code>3 + 2 = 5</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 2, present = [3,4], future = [5,8], hierarchy = [[1,2]], budget = 4</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2025/04/09/screenshot-2025-04-10-at-053641.png" style="width: 200px; height: 80px;" /></p>

<ul>
	<li>Employee 2 buys the stock at price 4 and earns a profit of <code>8 - 4 = 4</code>.</li>
	<li>Since both employees cannot buy together, the maximum profit is 4.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 3, present = [4,6,8], future = [7,9,11], hierarchy = [[1,2],[1,3]], budget = 10</span></p>

<p><strong>Output:</strong> 10</p>

<p><strong>Explanation:</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2025/04/09/image.png" style="width: 180px; height: 153px;" /></p>

<ul>
	<li>Employee 1 buys the stock at price 4 and earns a profit of <code>7 - 4 = 3</code>.</li>
	<li>Employee 3 would get a discounted price of <code>floor(8 / 2) = 4</code> and earns a profit of <code>11 - 4 = 7</code>.</li>
	<li>Employee 1 and Employee 3 buy their stocks at a total cost of <code>4 + 4 = 8 &lt;= budget</code>. Thus, the maximum total profit achieved is <code>3 + 7 = 10</code>.</li>
</ul>
</div>

<p><strong class="example">Example 4:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 3, present = [5,2,3], future = [8,5,6], hierarchy = [[1,2],[2,3]], budget = 7</span></p>

<p><strong>Output:</strong> <span class="example-io">12</span></p>

<p><strong>Explanation:</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2025/04/09/screenshot-2025-04-10-at-054114.png" style="width: 300px; height: 85px;" /></p>

<ul>
	<li>Employee 1 buys the stock at price 5 and earns a profit of <code>8 - 5 = 3</code>.</li>
	<li>Employee 2 would get a discounted price of <code>floor(2 / 2) = 1</code> and earns a profit of <code>5 - 1 = 4</code>.</li>
	<li>Employee 3 would get a discounted price of <code>floor(3 / 2) = 1</code> and earns a profit of <code>6 - 1 = 5</code>.</li>
	<li>The total cost becomes <code>5 + 1 + 1 = 7&nbsp;&lt;= budget</code>. Thus, the maximum total profit achieved is <code>3 + 4 + 5 = 12</code>.</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 160</code></li>
	<li><code>present.length, future.length == n</code></li>
	<li><code>1 &lt;= present[i], future[i] &lt;= 50</code></li>
	<li><code>hierarchy.length == n - 1</code></li>
	<li><code>hierarchy[i] == [u<sub>i</sub>, v<sub>i</sub>]</code></li>
	<li><code>1 &lt;= u<sub>i</sub>, v<sub>i</sub> &lt;= n</code></li>
	<li><code>u<sub>i</sub> != v<sub>i</sub></code></li>
	<li><code>1 &lt;= budget &lt;= 160</code></li>
	<li>There are no duplicate edges.</li>
	<li>Employee 1 is the direct or indirect boss of every employee.</li>
	<li>The input graph <code>hierarchy </code>is <strong>guaranteed</strong> to have no cycles.</li>
</ul>


## Hints

1. - Compute `max_profit[u]` and `max_profit1[u]` for each node `u`

2. - `max_profit[u]` = maximum profit in the subtree of `u` assuming the parent of `u` has not bought the stock

3. - `max_profit1[u]` = maximum profit in the subtree of `u` assuming the parent of `u` has bought the stock

4. For each node `u`, consider two cases:

5. Buy the stock for `u` (at `present[u]` price if parent did not buy, or at `floor(present[u]/2)` if parent bought), then add the best `max_profit1` values of its children

6. Skip buying for `u`, then add the best `max_profit` values of its children

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-12-16 01:11:11 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem is a variation of the tree knapsack problem, where the decision for an employee to buy stock (and at what price) depends on their direct boss's decision. This suggests a dynamic programming approach on the tree structure. For each employee (node `u`), we need to compute two DP states: one assuming `u`'s direct boss did not buy their stock, and another assuming `u`'s direct boss did buy their stock (enabling a discount for `u`). Each DP state is an array `dp[k]` representing the maximum profit achievable using exactly `k` budget within the subtree rooted at `u`.

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
#include <numeric>
#include <algorithm>
#include <map>
#include <functional>

// Using a struct for memoization return type
struct DPResult {
    std::vector<int> dp_no_parent_bought;
    std::vector<int> dp_parent_bought;
};

class Solution {
public:
    std::map<int, DPResult> memo;
    std::vector<std::vector<int>> adj;
    const std::vector<int>* present_ptr;
    const std::vector<int>* future_ptr;
    int budget_val;

    DPResult dfs(int u) {
        if (memo.count(u)) {
            return memo[u];
        }

        // Initialize DP arrays for current node 'u' and its processed children.
        // -1e9 (a large negative number) represents -float('inf') for unreachable states.
        // 0 for cost 0 is the base case (don't buy anything, 0 profit, 0 cost).

        std::vector<int> current_dp_u_no_buy(budget_val + 1, -1e9);
        current_dp_u_no_buy[0] = 0;

        int cost_u_normal = (*present_ptr)[u-1];
        int profit_u_normal = (*future_ptr)[u-1] - cost_u_normal;
        std::vector<int> current_dp_u_buy_normal(budget_val + 1, -1e9);
        if (cost_u_normal <= budget_val) {
            current_dp_u_buy_normal[cost_u_normal] = profit_u_normal;
        }

        std::vector<int> current_dp_u_no_buy_if_parent_bought(budget_val + 1, -1e9);
        current_dp_u_no_buy_if_parent_bought[0] = 0;

        int cost_u_discount = (*present_ptr)[u-1] / 2; // Integer division is floor for positive numbers
        int profit_u_discount = (*future_ptr)[u-1] - cost_u_discount;
        std::vector<int> current_dp_u_buy_discount(budget_val + 1, -1e9);
        if (cost_u_discount <= budget_val) {
            current_dp_u_buy_discount[cost_u_discount] = profit_u_discount;
        }

        for (int v : adj[u]) {
            DPResult res_v = dfs(v);

            auto merge_dps = [&](const std::vector<int>& dp1, const std::vector<int>& dp2) {
                std::vector<int> new_dp(budget_val + 1, -1e9);
                for (int k1 = 0; k1 <= budget_val; ++k1) {
                    if (dp1[k1] == -1e9) continue;
                    for (int k2 = 0; k1 + k2 <= budget_val; ++k2) {
                        if (dp2[k2] == -1e9) continue;
                        new_dp[k1 + k2] = std::max(new_dp[k1 + k2], dp1[k1] + dp2[k2]);
                    }
                }
                return new_dp;
            };

            current_dp_u_no_buy = merge_dps(current_dp_u_no_buy, res_v.dp_no_parent_bought);
            current_dp_u_buy_normal = merge_dps(current_dp_u_buy_normal, res_v.dp_parent_bought);
            current_dp_u_no_buy_if_parent_bought = merge_dps(current_dp_u_no_buy_if_parent_bought, res_v.dp_no_parent_bought);
            current_dp_u_buy_discount = merge_dps(current_dp_u_buy_discount, res_v.dp_parent_bought);
        }

        std::vector<int> final_dp_no_parent_bought(budget_val + 1, -1e9);
        for (int k = 0; k <= budget_val; ++k) {
            final_dp_no_parent_bought[k] = std::max(current_dp_u_no_buy[k], current_dp_u_buy_normal[k]);
        }

        std::vector<int> final_dp_parent_bought(budget_val + 1, -1e9);
        for (int k = 0; k <= budget_val; ++k) {
            final_dp_parent_bought[k] = std::max(current_dp_u_no_buy_if_parent_bought[k], current_dp_u_buy_discount[k]);
        }

        return memo[u] = {final_dp_no_parent_bought, final_dp_parent_bought};
    }

    int maxProfit(int n, std::vector<int>& present, std::vector<int>& future, std::vector<std::vector<int>>& hierarchy, int budget) {
        adj.resize(n + 1);
        for (const auto& edge : hierarchy) {
            adj[edge[0]].push_back(edge[1]);
        }

        present_ptr = &present;
        future_ptr = &future;
        budget_val = budget;
        memo.clear();

        DPResult root_res = dfs(1);

        int max_overall_profit = 0;
        for (int profit : root_res.dp_no_parent_bought) {
            if (profit != -1e9) { // Check against sentinel value
                max_overall_profit = std::max(max_overall_profit, profit);
            }
        }

        return max_overall_profit;
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
    // Using a custom class for memoization return type
    static class DPResult {
        int[] dp_no_parent_bought;
        int[] dp_parent_bought;

        public DPResult(int[] dp_no_parent_bought, int[] dp_parent_bought) {
            this.dp_no_parent_bought = dp_no_parent_bought;
            this.dp_parent_bought = dp_parent_bought;
        }
    }

    Map<Integer, DPResult> memo;
    List<List<Integer>> adj;
    int[] present_arr;
    int[] future_arr;
    int budget_val;
    static final int NEG_INF = -1_000_000_000; // A sufficiently small number for -float('inf')

    private DPResult dfs(int u) {
        if (memo.containsKey(u)) {
            return memo.get(u);
        }

        int[] current_dp_u_no_buy = new int[budget_val + 1];
        Arrays.fill(current_dp_u_no_buy, NEG_INF);
        current_dp_u_no_buy[0] = 0;

        int cost_u_normal = present_arr[u-1];
        int profit_u_normal = future_arr[u-1] - cost_u_normal;
        int[] current_dp_u_buy_normal = new int[budget_val + 1];
        Arrays.fill(current_dp_u_buy_normal, NEG_INF);
        if (cost_u_normal <= budget_val) {
            current_dp_u_buy_normal[cost_u_normal] = profit_u_normal;
        }

        int[] current_dp_u_no_buy_if_parent_bought = new int[budget_val + 1];
        Arrays.fill(current_dp_u_no_buy_if_parent_bought, NEG_INF);
        current_dp_u_no_buy_if_parent_bought[0] = 0;

        int cost_u_discount = present_arr[u-1] / 2; // Integer division is floor for positive numbers
        int profit_u_discount = future_arr[u-1] - cost_u_discount;
        int[] current_dp_u_buy_discount = new int[budget_val + 1];
        Arrays.fill(current_dp_u_buy_discount, NEG_INF);
        if (cost_u_discount <= budget_val) {
            current_dp_u_buy_discount[cost_u_discount] = profit_u_discount;
        }

        for (int v : adj.get(u)) {
            DPResult res_v = dfs(v);

            // Helper function to merge two DP arrays (knapsack-style combination)
            // This is inlined for Java to avoid creating a new lambda/method object repeatedly
            // or passing around DP arrays as arguments.

            // Merge current_dp_u_no_buy with res_v.dp_no_parent_bought
            int[] next_dp_u_no_buy = new int[budget_val + 1];
            Arrays.fill(next_dp_u_no_buy, NEG_INF);
            for (int k1 = 0; k1 <= budget_val; ++k1) {
                if (current_dp_u_no_buy[k1] == NEG_INF) continue;
                for (int k2 = 0; k1 + k2 <= budget_val; ++k2) {
                    if (res_v.dp_no_parent_bought[k2] == NEG_INF) continue;
                    next_dp_u_no_buy[k1 + k2] = Math.max(next_dp_u_no_buy[k1 + k2], current_dp_u_no_buy[k1] + res_v.dp_no_parent_bought[k2]);
                }
            }
            current_dp_u_no_buy = next_dp_u_no_buy;

            // Merge current_dp_u_buy_normal with res_v.dp_parent_bought
            int[] next_dp_u_buy_normal = new int[budget_val + 1];
            Arrays.fill(next_dp_u_buy_normal, NEG_INF);
            for (int k1 = 0; k1 <= budget_val; ++k1) {
                if (current_dp_u_buy_normal[k1] == NEG_INF) continue;
                for (int k2 = 0; k1 + k2 <= budget_val; ++k2) {
                    if (res_v.dp_parent_bought[k2] == NEG_INF) continue;
                    next_dp_u_buy_normal[k1 + k2] = Math.max(next_dp_u_buy_normal[k1 + k2], current_dp_u_buy_normal[k1] + res_v.dp_parent_bought[k2]);
                }
            }
            current_dp_u_buy_normal = next_dp_u_buy_normal;

            // Merge current_dp_u_no_buy_if_parent_bought with res_v.dp_no_parent_bought
            int[] next_dp_u_no_buy_if_parent_bought = new int[budget_val + 1];
            Arrays.fill(next_dp_u_no_buy_if_parent_bought, NEG_INF);
            for (int k1 = 0; k1 <= budget_val; ++k1) {
                if (current_dp_u_no_buy_if_parent_bought[k1] == NEG_INF) continue;
                for (int k2 = 0; k1 + k2 <= budget_val; ++k2) {
                    if (res_v.dp_no_parent_bought[k2] == NEG_INF) continue;
                    next_dp_u_no_buy_if_parent_bought[k1 + k2] = Math.max(next_dp_u_no_buy_if_parent_bought[k1 + k2], current_dp_u_no_buy_if_parent_bought[k1] + res_v.dp_no_parent_bought[k2]);
                }
            }
            current_dp_u_no_buy_if_parent_bought = next_dp_u_no_buy_if_parent_bought;

            // Merge current_dp_u_buy_discount with res_v.dp_parent_bought
            int[] next_dp_u_buy_discount = new int[budget_val + 1];
            Arrays.fill(next_dp_u_buy_discount, NEG_INF);
            for (int k1 = 0; k1 <= budget_val; ++k1) {
                if (current_dp_u_buy_discount[k1] == NEG_INF) continue;
                for (int k2 = 0; k1 + k2 <= budget_val; ++k2) {
                    if (res_v.dp_parent_bought[k2] == NEG_INF) continue;
                    next_dp_u_buy_discount[k1 + k2] = Math.max(next_dp_u_buy_discount[k1 + k2], current_dp_u_buy_discount[k1] + res_v.dp_parent_bought[k2]);
                }
            }
            current_dp_u_buy_discount = next_dp_u_buy_discount;
        }

        int[] final_dp_no_parent_bought = new int[budget_val + 1];
        Arrays.fill(final_dp_no_parent_bought, NEG_INF);
        for (int k = 0; k <= budget_val; ++k) {
            final_dp_no_parent_bought[k] = Math.max(current_dp_u_no_buy[k], current_dp_u_buy_normal[k]);
        }

        int[] final_dp_parent_bought = new int[budget_val + 1];
        Arrays.fill(final_dp_parent_bought, NEG_INF);
        for (int k = 0; k <= budget_val; ++k) {
            final_dp_parent_bought[k] = Math.max(current_dp_u_no_buy_if_parent_bought[k], current_dp_u_buy_discount[k]);
        }

        DPResult result = new DPResult(final_dp_no_parent_bought, final_dp_parent_bought);
        memo.put(u, result);
        return result;
    }

    public int maxProfit(int n, int[] present, int[] future, int[][] hierarchy, int budget) {
        adj = new ArrayList<>();
        for (int i = 0; i <= n; ++i) {
            adj.add(new ArrayList<>());
        }
        for (int[] edge : hierarchy) {
            adj.get(edge[0]).add(edge[1]);
        }

        present_arr = present;
        future_arr = future;
        budget_val = budget;
        memo = new HashMap<>();

        DPResult root_res = dfs(1);

        int max_overall_profit = 0;
        for (int profit : root_res.dp_no_parent_bought) {
            if (profit != NEG_INF) {
                max_overall_profit = Math.max(max_overall_profit, profit);
            }
        }

        return max_overall_profit;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
import collections

class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        adj = collections.defaultdict(list)
        for u, v in hierarchy:
            adj[u].append(v)

        memo = {}

        # dfs(u) returns a tuple of two lists:
        # 1. dp_no_parent_bought: max profit in subtree u for each budget k, assuming u's parent did NOT buy.
        # 2. dp_parent_bought: max profit in subtree u for each budget k, assuming u's parent DID buy.
        # Each list is of size (budget + 1).
        # Values are initialized to -float('inf') for unreachable states, and 0 for cost 0.
        def dfs(u):
            if u in memo:
                return memo[u]

            # These DP arrays will store the maximum profit for node 'u' and its already processed children.
            # They are initialized to reflect only 'u's decision (or lack thereof).

            # Scenario 1: u's parent did NOT buy their stock.
            #   Option A: u does NOT buy its own stock.
            #     Cost: 0, Profit: 0.
            #     Children will be processed assuming u did NOT buy (so they will use their 'no_parent_bought' state).
            current_dp_u_no_buy = [-float('inf')] * (budget + 1)
            current_dp_u_no_buy[0] = 0

            #   Option B: u BUYS its own stock at normal price.
            #     Cost: present[u-1], Profit: future[u-1] - present[u-1].
            #     Children will be processed assuming u DID buy (so they will use their 'parent_bought' state).
            cost_u_normal = present[u-1]
            profit_u_normal = future[u-1] - cost_u_normal
            current_dp_u_buy_normal = [-float('inf')] * (budget + 1)
            if cost_u_normal <= budget:
                current_dp_u_buy_normal[cost_u_normal] = profit_u_normal

            # Scenario 2: u's parent DID buy their stock.
            #   Option A: u does NOT buy its own stock.
            #     Cost: 0, Profit: 0.
            #     Children will be processed assuming u did NOT buy (so they will use their 'no_parent_bought' state).
            #     This is conceptually similar to current_dp_u_no_buy, but kept separate for clarity in merging.
            current_dp_u_no_buy_if_parent_bought = [-float('inf')] * (budget + 1)
            current_dp_u_no_buy_if_parent_bought[0] = 0

            #   Option B: u BUYS its own stock at discounted price.
            #     Cost: floor(present[u-1] / 2), Profit: future[u-1] - floor(present[u-1] / 2).
            #     Children will be processed assuming u DID buy (so they will use their 'parent_bought' state).
            cost_u_discount = present[u-1] // 2
            profit_u_discount = future[u-1] - cost_u_discount
            current_dp_u_buy_discount = [-float('inf')] * (budget + 1)
            if cost_u_discount <= budget:
                current_dp_u_buy_discount[cost_u_discount] = profit_u_discount

            # Iterate through each child 'v' of 'u' and merge their DP results.
            for v in adj[u]:
                # Recursively get DP results for child 'v'
                res_v_no_parent_bought, res_v_parent_bought = dfs(v)

                # Helper function to merge two DP arrays (knapsack-style combination)
                def merge_dps(dp1, dp2):
                    new_dp = [-float('inf')] * (budget + 1)
                    for k1 in range(budget + 1):
                        if dp1[k1] == -float('inf'):
                            continue
                        for k2 in range(budget - k1 + 1):
                            if dp2[k2] == -float('inf'):
                                continue
                            new_dp[k1 + k2] = max(new_dp[k1 + k2], dp1[k1] + dp2[k2])
                    return new_dp

                # Update current_dp_u_no_buy: u did not buy, so v also does not get discount from u.
                current_dp_u_no_buy = merge_dps(current_dp_u_no_buy, res_v_no_parent_bought)

                # Update current_dp_u_buy_normal: u bought normally, so v gets discount from u.
                current_dp_u_buy_normal = merge_dps(current_dp_u_buy_normal, res_v_parent_bought)

                # Update current_dp_u_no_buy_if_parent_bought: u's parent bought, but u did not buy,
                # so v does not get discount from u.
                current_dp_u_no_buy_if_parent_bought = merge_dps(current_dp_u_no_buy_if_parent_bought, res_v_no_parent_bought)

                # Update current_dp_u_buy_discount: u's parent bought, and u bought discounted,
                # so v gets discount from u.
                current_dp_u_buy_discount = merge_dps(current_dp_u_buy_discount, res_v_parent_bought)

            # After processing all children, combine the options for 'u' itself.

            # Final DP for when u's parent did NOT buy:
            # u can either not buy (current_dp_u_no_buy) or buy normally (current_dp_u_buy_normal).
            final_dp_no_parent_bought = [-float('inf')] * (budget + 1)
            for k in range(budget + 1):
                final_dp_no_parent_bought[k] = max(current_dp_u_no_buy[k], current_dp_u_buy_normal[k])

            # Final DP for when u's parent DID buy:
            # u can either not buy (current_dp_u_no_buy_if_parent_bought) or buy discounted (current_dp_u_buy_discount).
            final_dp_parent_bought = [-float('inf')] * (budget + 1)
            for k in range(budget + 1):
                final_dp_parent_bought[k] = max(current_dp_u_no_buy_if_parent_bought[k], current_dp_u_buy_discount[k])

            memo[u] = (final_dp_no_parent_bought, final_dp_parent_bought)
            return final_dp_no_parent_bought, final_dp_parent_bought

        # Employee 1 is the CEO and has no parent, so we use the 'no_parent_bought' state for the root.
        final_dp_root_no_parent_bought, _ = dfs(1)

        # The maximum profit is the maximum value in the resulting DP array.
        # If no profitable trades can be made within the budget, the profit is 0.
        max_overall_profit = 0
        for profit in final_dp_root_no_parent_bought:
            if profit != -float('inf'):
                max_overall_profit = max(max_overall_profit, profit)

        return max_overall_profit
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
import collections

class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        adj = collections.defaultdict(list)
        for u, v in hierarchy:
            adj[u].append(v)

        memo = {}

        # dfs(u) returns a tuple of two lists:
        # 1. dp_no_parent_bought: max profit in subtree u for each budget k, assuming u's parent did NOT buy.
        # 2. dp_parent_bought: max profit in subtree u for each budget k, assuming u's parent DID buy.
        # Each list is of size (budget + 1).
        # Values are initialized to -float('inf') for unreachable states, and 0 for cost 0.
        def dfs(u):
            if u in memo:
                return memo[u]

            # These DP arrays will store the maximum profit for node 'u' and its already processed children.
            # They are initialized to reflect only 'u's decision (or lack thereof).

            # Scenario 1: u's parent did NOT buy their stock.
            #   Option A: u does NOT buy its own stock.
            #     Cost: 0, Profit: 0.
            #     Children will be processed assuming u did NOT buy (so they will use their 'no_parent_bought' state).
            current_dp_u_no_buy = [-float('inf')] * (budget + 1)
            current_dp_u_no_buy[0] = 0

            #   Option B: u BUYS its own stock at normal price.
            #     Cost: present[u-1], Profit: future[u-1] - present[u-1].
            #     Children will be processed assuming u DID buy (so they will use their 'parent_bought' state).
            cost_u_normal = present[u-1]
            profit_u_normal = future[u-1] - cost_u_normal
            current_dp_u_buy_normal = [-float('inf')] * (budget + 1)
            if cost_u_normal <= budget:
                current_dp_u_buy_normal[cost_u_normal] = profit_u_normal

            # Scenario 2: u's parent DID buy their stock.
            #   Option A: u does NOT buy its own stock.
            #     Cost: 0, Profit: 0.
            #     Children will be processed assuming u did NOT buy (so they will use their 'no_parent_bought' state).
            #     This is conceptually similar to current_dp_u_no_buy, but kept separate for clarity in merging.
            current_dp_u_no_buy_if_parent_bought = [-float('inf')] * (budget + 1)
            current_dp_u_no_buy_if_parent_bought[0] = 0

            #   Option B: u BUYS its own stock at discounted price.
            #     Cost: floor(present[u-1] / 2), Profit: future[u-1] - floor(present[u-1] / 2).
            #     Children will be processed assuming u DID buy (so they will use their 'parent_bought' state).
            cost_u_discount = present[u-1] // 2
            profit_u_discount = future[u-1] - cost_u_discount
            current_dp_u_buy_discount = [-float('inf')] * (budget + 1)
            if cost_u_discount <= budget:
                current_dp_u_buy_discount[cost_u_discount] = profit_u_discount

            # Iterate through each child 'v' of 'u' and merge their DP results.
            for v in adj[u]:
                # Recursively get DP results for child 'v'
                res_v_no_parent_bought, res_v_parent_bought = dfs(v)

                # Helper function to merge two DP arrays (knapsack-style combination)
                def merge_dps(dp1, dp2):
                    new_dp = [-float('inf')] * (budget + 1)
                    for k1 in range(budget + 1):
                        if dp1[k1] == -float('inf'):
                            continue
                        for k2 in range(budget - k1 + 1):
                            if dp2[k2] == -float('inf'):
                                continue
                            new_dp[k1 + k2] = max(new_dp[k1 + k2], dp1[k1] + dp2[k2])
                    return new_dp

                # Update current_dp_u_no_buy: u did not buy, so v also does not get discount from u.
                current_dp_u_no_buy = merge_dps(current_dp_u_no_buy, res_v_no_parent_bought)

                # Update current_dp_u_buy_normal: u bought normally, so v gets discount from u.
                current_dp_u_buy_normal = merge_dps(current_dp_u_buy_normal, res_v_parent_bought)

                # Update current_dp_u_no_buy_if_parent_bought: u's parent bought, but u did not buy,
                # so v does not get discount from u.
                current_dp_u_no_buy_if_parent_bought = merge_dps(current_dp_u_no_buy_if_parent_bought, res_v_no_parent_bought)

                # Update current_dp_u_buy_discount: u's parent bought, and u bought discounted,
                # so v gets discount from u.
                current_dp_u_buy_discount = merge_dps(current_dp_u_buy_discount, res_v_parent_bought)

            # After processing all children, combine the options for 'u' itself.

            # Final DP for when u's parent did NOT buy:
            # u can either not buy (current_dp_u_no_buy) or buy normally (current_dp_u_buy_normal).
            final_dp_no_parent_bought = [-float('inf')] * (budget + 1)
            for k in range(budget + 1):
                final_dp_no_parent_bought[k] = max(current_dp_u_no_buy[k], current_dp_u_buy_normal[k])

            # Final DP for when u's parent DID buy:
            # u can either not buy (current_dp_u_no_buy_if_parent_bought) or buy discounted (current_dp_u_buy_discount).
            final_dp_parent_bought = [-float('inf')] * (budget + 1)
            for k in range(budget + 1):
                final_dp_parent_bought[k] = max(current_dp_u_no_buy_if_parent_bought[k], current_dp_u_buy_discount[k])

            memo[u] = (final_dp_no_parent_bought, final_dp_parent_bought)
            return final_dp_no_parent_bought, final_dp_parent_bought

        # Employee 1 is the CEO and has no parent, so we use the 'no_parent_bought' state for the root.
        final_dp_root_no_parent_bought, _ = dfs(1)

        # The maximum profit is the maximum value in the resulting DP array.
        # If no profitable trades can be made within the budget, the profit is 0.
        max_overall_profit = 0
        for profit in final_dp_root_no_parent_bought:
            if profit != -float('inf'):
                max_overall_profit = max(max_overall_profit, profit)

        return max_overall_profit
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <limits.h>

#define NEG_INF INT_MIN / 2 // Use INT_MIN/2 to avoid overflow issues with addition

// Structure to hold DP results for a subtree
typedef struct {
    int* dp_no_parent_bought;
    int* dp_parent_bought;
} DPResult;

// Adjacency list for the hierarchy
int** adj;
int* adj_sizes;

// Input arrays and budget, made global for easier access in DFS
int* present_arr;
int* future_arr;
int budget_val;

// Memoization table (using a simple array for fixed N, or hash map for sparse IDs)
// For N <= 160, a 2D array for memoization is feasible.
// memo[u][0] stores dp_no_parent_bought, memo[u][1] stores dp_parent_bought
DPResult* memo_table;
int N_val; // Store N for memo_table size

// Helper function to create and initialize a DP array
int* create_dp_array() {
    int* dp = (int*)malloc(sizeof(int) * (budget_val + 1));
    for (int i = 0; i <= budget_val; ++i) {
        dp[i] = NEG_INF;
    }
    return dp;
}

// Helper function to merge two DP arrays (knapsack-style combination)
int* merge_dps(const int* dp1, const int* dp2) {
    int* new_dp = create_dp_array();
    for (int k1 = 0; k1 <= budget_val; ++k1) {
        if (dp1[k1] == NEG_INF) continue;
        for (int k2 = 0; k1 + k2 <= budget_val; ++k2) {
            if (dp2[k2] == NEG_INF) continue;
            if (dp1[k1] + dp2[k2] > new_dp[k1 + k2]) {
                new_dp[k1 + k2] = dp1[k1] + dp2[k2];
            }
        }
    }
    return new_dp;
}

DPResult dfs(int u) {
    if (memo_table[u].dp_no_parent_bought != NULL) {
        return memo_table[u];
    }

    int* current_dp_u_no_buy = create_dp_array();
    current_dp_u_no_buy[0] = 0;

    int cost_u_normal = present_arr[u-1];
    int profit_u_normal = future_arr[u-1] - cost_u_normal;
    int* current_dp_u_buy_normal = create_dp_array();
    if (cost_u_normal <= budget_val) {
        current_dp_u_buy_normal[cost_u_normal] = profit_u_normal;
    }

    int* current_dp_u_no_buy_if_parent_bought = create_dp_array();
    current_dp_u_no_buy_if_parent_bought[0] = 0;

    int cost_u_discount = present_arr[u-1] / 2; // Integer division is floor for positive numbers
    int profit_u_discount = future_arr[u-1] - cost_u_discount;
    int* current_dp_u_buy_discount = create_dp_array();
    if (cost_u_discount <= budget_val) {
        current_dp_u_buy_discount[cost_u_discount] = profit_u_discount;
    }

    for (int i = 0; i < adj_sizes[u]; ++i) {
        int v = adj[u][i];
        DPResult res_v = dfs(v);

        int* next_dp;

        next_dp = merge_dps(current_dp_u_no_buy, res_v.dp_no_parent_bought);
        free(current_dp_u_no_buy); current_dp_u_no_buy = next_dp;

        next_dp = merge_dps(current_dp_u_buy_normal, res_v.dp_parent_bought);
        free(current_dp_u_buy_normal); current_dp_u_buy_normal = next_dp;

        next_dp = merge_dps(current_dp_u_no_buy_if_parent_bought, res_v.dp_no_parent_bought);
        free(current_dp_u_no_buy_if_parent_bought); current_dp_u_no_buy_if_parent_bought = next_dp;

        next_dp = merge_dps(current_dp_u_buy_discount, res_v.dp_parent_bought);
        free(current_dp_u_buy_discount); current_dp_u_buy_discount = next_dp;
    }

    int* final_dp_no_parent_bought = create_dp_array();
    for (int k = 0; k <= budget_val; ++k) {
        if (current_dp_u_no_buy[k] > final_dp_no_parent_bought[k]) {
            final_dp_no_parent_bought[k] = current_dp_u_no_buy[k];
        }
        if (current_dp_u_buy_normal[k] > final_dp_no_parent_bought[k]) {
            final_dp_no_parent_bought[k] = current_dp_u_buy_normal[k];
        }
    }

    int* final_dp_parent_bought = create_dp_array();
    for (int k = 0; k <= budget_val; ++k) {
        if (current_dp_u_no_buy_if_parent_bought[k] > final_dp_parent_bought[k]) {
            final_dp_parent_bought[k] = current_dp_u_no_buy_if_parent_bought[k];
        }
        if (current_dp_u_buy_discount[k] > final_dp_parent_bought[k]) {
            final_dp_parent_bought[k] = current_dp_u_buy_discount[k];
        }
    }

    // Free temporary DP arrays
    free(current_dp_u_no_buy);
    free(current_dp_u_buy_normal);
    free(current_dp_u_no_buy_if_parent_bought);
    free(current_dp_u_buy_discount);

    memo_table[u].dp_no_parent_bought = final_dp_no_parent_bought;
    memo_table[u].dp_parent_bought = final_dp_parent_bought;
    return memo_table[u];
}

int maxProfit(int n, int* present, int* future, int hierarchy_rows, int* hierarchy_cols, int** hierarchy, int budget) {
    N_val = n;
    adj = (int**)malloc(sizeof(int*) * (n + 1));
    adj_sizes = (int*)calloc(n + 1, sizeof(int)); // Initialize to 0
    int* temp_adj_capacity = (int*)calloc(n + 1, sizeof(int)); // For dynamic resizing

    // First pass to count children for each node to allocate memory
    for (int i = 0; i < hierarchy_rows; ++i) {
        int u = hierarchy[i][0];
        adj_sizes[u]++;
    }

    // Allocate memory for adjacency lists
    for (int i = 1; i <= n; ++i) {
        adj[i] = (int*)malloc(sizeof(int) * adj_sizes[i]);
        adj_sizes[i] = 0; // Reset to use as current index during second pass
    }

    // Second pass to populate adjacency lists
    for (int i = 0; i < hierarchy_rows; ++i) {
        int u = hierarchy[i][0];
        int v = hierarchy[i][1];
        adj[u][adj_sizes[u]++] = v;
    }
    free(temp_adj_capacity);

    present_arr = present;
    future_arr = future;
    budget_val = budget;

    memo_table = (DPResult*)calloc(n + 1, sizeof(DPResult)); // Initialize all pointers to NULL

    DPResult root_res = dfs(1);

    int max_overall_profit = 0;
    for (int i = 0; i <= budget_val; ++i) {
        if (root_res.dp_no_parent_bought[i] != NEG_INF) {
            if (root_res.dp_no_parent_bought[i] > max_overall_profit) {
                max_overall_profit = root_res.dp_no_parent_bought[i];
            }
        }
    }

    // Cleanup allocated memory
    for (int i = 1; i <= n; ++i) {
        if (memo_table[i].dp_no_parent_bought != NULL) {
            free(memo_table[i].dp_no_parent_bought);
            free(memo_table[i].dp_parent_bought);
        }
        free(adj[i]);
    }
    free(adj);
    free(adj_sizes);
    free(memo_table);

    return max_overall_profit;
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
    // Using a custom class for memoization return type
    public class DPResult {
        public int[] dp_no_parent_bought;
        public int[] dp_parent_bought;

        public DPResult(int[] dp_no_parent_bought, int[] dp_parent_bought) {
            this.dp_no_parent_bought = dp_no_parent_bought;
            this.dp_parent_bought = dp_parent_bought;
        }
    }

    private Dictionary<int, DPResult> memo;
    private List<List<int>> adj;
    private int[] present_arr;
    private int[] future_arr;
    private int budget_val;
    private const int NEG_INF = -1_000_000_000; // A sufficiently small number for -float('inf')

    private DPResult Dfs(int u) {
        if (memo.ContainsKey(u)) {
            return memo[u];
        }

        int[] current_dp_u_no_buy = new int[budget_val + 1];
        Array.Fill(current_dp_u_no_buy, NEG_INF);
        current_dp_u_no_buy[0] = 0;

        int cost_u_normal = present_arr[u-1];
        int profit_u_normal = future_arr[u-1] - cost_u_normal;
        int[] current_dp_u_buy_normal = new int[budget_val + 1];
        Array.Fill(current_dp_u_buy_normal, NEG_INF);
        if (cost_u_normal <= budget_val) {
            current_dp_u_buy_normal[cost_u_normal] = profit_u_normal;
        }

        int[] current_dp_u_no_buy_if_parent_bought = new int[budget_val + 1];
        Array.Fill(current_dp_u_no_buy_if_parent_bought, NEG_INF);
        current_dp_u_no_buy_if_parent_bought[0] = 0;

        int cost_u_discount = present_arr[u-1] / 2; // Integer division is floor for positive numbers
        int profit_u_discount = future_arr[u-1] - cost_u_discount;
        int[] current_dp_u_buy_discount = new int[budget_val + 1];
        Array.Fill(current_dp_u_buy_discount, NEG_INF);
        if (cost_u_discount <= budget_val) {
            current_dp_u_buy_discount[cost_u_discount] = profit_u_discount;
        }

        foreach (int v in adj[u]) {
            DPResult res_v = Dfs(v);

            // Helper function to merge two DP arrays (knapsack-style combination)
            // Inlined for C# to avoid creating new delegates/methods repeatedly.

            // Merge current_dp_u_no_buy with res_v.dp_no_parent_bought
            int[] next_dp_u_no_buy = new int[budget_val + 1];
            Array.Fill(next_dp_u_no_buy, NEG_INF);
            for (int k1 = 0; k1 <= budget_val; ++k1) {
                if (current_dp_u_no_buy[k1] == NEG_INF) continue;
                for (int k2 = 0; k1 + k2 <= budget_val; ++k2) {
                    if (res_v.dp_no_parent_bought[k2] == NEG_INF) continue;
                    next_dp_u_no_buy[k1 + k2] = Math.Max(next_dp_u_no_buy[k1 + k2], current_dp_u_no_buy[k1] + res_v.dp_no_parent_bought[k2]);
                }
            }
            current_dp_u_no_buy = next_dp_u_no_buy;

            // Merge current_dp_u_buy_normal with res_v.dp_parent_bought
            int[] next_dp_u_buy_normal = new int[budget_val + 1];
            Array.Fill(next_dp_u_buy_normal, NEG_INF);
            for (int k1 = 0; k1 <= budget_val; ++k1) {
                if (current_dp_u_buy_normal[k1] == NEG_INF) continue;
                for (int k2 = 0; k1 + k2 <= budget_val; ++k2) {
                    if (res_v.dp_parent_bought[k2] == NEG_INF) continue;
                    next_dp_u_buy_normal[k1 + k2] = Math.Max(next_dp_u_buy_normal[k1 + k2], current_dp_u_buy_normal[k1] + res_v.dp_parent_bought[k2]);
                }
            }
            current_dp_u_buy_normal = next_dp_u_buy_normal;

            // Merge current_dp_u_no_buy_if_parent_bought with res_v.dp_no_parent_bought
            int[] next_dp_u_no_buy_if_parent_bought = new int[budget_val + 1];
            Array.Fill(next_dp_u_no_buy_if_parent_bought, NEG_INF);
            for (int k1 = 0; k1 <= budget_val; ++k1) {
                if (current_dp_u_no_buy_if_parent_bought[k1] == NEG_INF) continue;
                for (int k2 = 0; k1 + k2 <= budget_val; ++k2) {
                    if (res_v.dp_no_parent_bought[k2] == NEG_INF) continue;
                    next_dp_u_no_buy_if_parent_bought[k1 + k2] = Math.Max(next_dp_u_no_buy_if_parent_bought[k1 + k2], current_dp_u_no_buy_if_parent_bought[k1] + res_v.dp_no_parent_bought[k2]);
                }
            }
            current_dp_u_no_buy_if_parent_bought = next_dp_u_no_buy_if_parent_bought;

            // Merge current_dp_u_buy_discount with res_v.dp_parent_bought
            int[] next_dp_u_buy_discount = new int[budget_val + 1];
            Array.Fill(next_dp_u_buy_discount, NEG_INF);
            for (int k1 = 0; k1 <= budget_val; ++k1) {
                if (current_dp_u_buy_discount[k1] == NEG_INF) continue;
                for (int k2 = 0; k1 + k2 <= budget_val; ++k2) {
                    if (res_v.dp_parent_bought[k2] == NEG_INF) continue;
                    next_dp_u_buy_discount[k1 + k2] = Math.Max(next_dp_u_buy_discount[k1 + k2], current_dp_u_buy_discount[k1] + res_v.dp_parent_bought[k2]);
                }
            }
            current_dp_u_buy_discount = next_dp_u_buy_discount;
        }

        int[] final_dp_no_parent_bought = new int[budget_val + 1];
        Array.Fill(final_dp_no_parent_bought, NEG_INF);
        for (int k = 0; k <= budget_val; ++k) {
            final_dp_no_parent_bought[k] = Math.Max(current_dp_u_no_buy[k], current_dp_u_buy_normal[k]);
        }

        int[] final_dp_parent_bought = new int[budget_val + 1];
        Array.Fill(final_dp_parent_bought, NEG_INF);
        for (int k = 0; k <= budget_val; ++k) {
            final_dp_parent_bought[k] = Math.Max(current_dp_u_no_buy_if_parent_bought[k], current_dp_u_buy_discount[k]);
        }

        DPResult result = new DPResult(final_dp_no_parent_bought, final_dp_parent_bought);
        memo.Add(u, result);
        return result;
    }

    public int MaxProfit(int n, int[] present, int[] future, int[][] hierarchy, int budget) {
        adj = new List<List<int>>();
        for (int i = 0; i <= n; ++i) {
            adj.Add(new List<int>());
        }
        foreach (int[] edge in hierarchy) {
            adj[edge[0]].Add(edge[1]);
        }

        present_arr = present;
        future_arr = future;
        budget_val = budget;
        memo = new Dictionary<int, DPResult>();

        DPResult root_res = Dfs(1);

        int max_overall_profit = 0;
        foreach (int profit in root_res.dp_no_parent_bought) {
            if (profit != NEG_INF) {
                max_overall_profit = Math.Max(max_overall_profit, profit);
            }
        }

        return max_overall_profit;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number} n
 * @param {number[]} present
 * @param {number[]} future
 * @param {number[][]} hierarchy
 * @param {number} budget
 * @return {number}
 */
var maxProfit = function(n, present, future, hierarchy, budget) {
    const adj = new Array(n + 1).fill(0).map(() => []);
    for (const [u, v] of hierarchy) {
        adj[u].push(v);
    }

    const memo = new Map();
    const NEG_INF = -Infinity;

    // dfs(u) returns an object with two arrays:
    // { dp_no_parent_bought, dp_parent_bought }
    const dfs = (u) => {
        if (memo.has(u)) {
            return memo.get(u);
        }

        // Initialize DP arrays for current node 'u' and its processed children.
        // They are initialized to reflect only 'u's decision (or lack thereof).

        // Scenario 1: u's parent did NOT buy their stock.
        //   Option A: u does NOT buy its own stock.
        //     Cost: 0, Profit: 0.
        //     Children will be processed assuming u did NOT buy (so they will use their 'no_parent_bought' state).
        let current_dp_u_no_buy = new Array(budget + 1).fill(NEG_INF);
        current_dp_u_no_buy[0] = 0;

        //   Option B: u BUYS its own stock at normal price.
        //     Cost: present[u-1], Profit: future[u-1] - present[u-1].
        //     Children will be processed assuming u DID buy (so they will use their 'parent_bought' state).
        const cost_u_normal = present[u-1];
        const profit_u_normal = future[u-1] - cost_u_normal;
        let current_dp_u_buy_normal = new Array(budget + 1).fill(NEG_INF);
        if (cost_u_normal <= budget) {
            current_dp_u_buy_normal[cost_u_normal] = profit_u_normal;
        }

        // Scenario 2: u's parent DID buy their stock.
        //   Option A: u does NOT buy its own stock.
        //     Cost: 0, Profit: 0.
        //     Children will be processed assuming u did NOT buy (so they will use their 'no_parent_bought' state).
        let current_dp_u_no_buy_if_parent_bought = new Array(budget + 1).fill(NEG_INF);
        current_dp_u_no_buy_if_parent_bought[0] = 0;

        //   Option B: u BUYS its own stock at discounted price.
        //     Cost: Math.floor(present[u-1] / 2), Profit: future[u-1] - Math.floor(present[u-1] / 2).
        //     Children will be processed assuming u DID buy (so they will use their 'parent_bought' state).
        const cost_u_discount = Math.floor(present[u-1] / 2);
        const profit_u_discount = future[u-1] - cost_u_discount;
        let current_dp_u_buy_discount = new Array(budget + 1).fill(NEG_INF);
        if (cost_u_discount <= budget) {
            current_dp_u_buy_discount[cost_u_discount] = profit_u_discount;
        }

        // Helper function to merge two DP arrays (knapsack-style combination)
        const mergeDps = (dp1, dp2) => {
            const new_dp = new Array(budget + 1).fill(NEG_INF);
            for (let k1 = 0; k1 <= budget; ++k1) {
                if (dp1[k1] === NEG_INF) {
                    continue;
                }
                for (let k2 = 0; k1 + k2 <= budget; ++k2) {
                    if (dp2[k2] === NEG_INF) {
                        continue;
                    }
                    new_dp[k1 + k2] = Math.max(new_dp[k1 + k2], dp1[k1] + dp2[k2]);
                }
            }
            return new_dp;
        };

        // Iterate through each child 'v' of 'u' and merge their DP results.
        for (const v of adj[u]) {
            // Recursively get DP results for child 'v'
            const { dp_no_parent_bought: res_v_no_parent_bought, dp_parent_bought: res_v_parent_bought } = dfs(v);

            // Update current_dp_u_no_buy: u did not buy, so v also does not get discount from u.
            current_dp_u_no_buy = mergeDps(current_dp_u_no_buy, res_v_no_parent_bought);

            // Update current_dp_u_buy_normal: u bought normally, so v gets discount from u.
            current_dp_u_buy_normal = mergeDps(current_dp_u_buy_normal, res_v_parent_bought);

            // Update current_dp_u_no_buy_if_parent_bought: u's parent bought, but u did not buy,
            // so v does not get discount from u.
            current_dp_u_no_buy_if_parent_bought = mergeDps(current_dp_u_no_buy_if_parent_bought, res_v_no_parent_bought);

            // Update current_dp_u_buy_discount: u's parent bought, and u bought discounted,
            // so v gets discount from u.
            current_dp_u_buy_discount = mergeDps(current_dp_u_buy_discount, res_v_parent_bought);
        }

        // After processing all children, combine the options for 'u' itself.

        // Final DP for when u's parent did NOT buy:
        // u can either not buy (current_dp_u_no_buy) or buy normally (current_dp_u_buy_normal).
        const final_dp_no_parent_bought = new Array(budget + 1).fill(NEG_INF);
        for (let k = 0; k <= budget; ++k) {
            final_dp_no_parent_bought[k] = Math.max(current_dp_u_no_buy[k], current_dp_u_buy_normal[k]);
        }

        // Final DP for when u's parent DID buy:
        // u can either not buy (current_dp_u_no_buy_if_parent_bought) or buy discounted (current_dp_u_buy_discount).
        const final_dp_parent_bought = new Array(budget + 1).fill(NEG_INF);
        for (let k = 0; k <= budget; ++k) {
            final_dp_parent_bought[k] = Math.max(current_dp_u_no_buy_if_parent_bought[k], current_dp_u_buy_discount[k]);
        }

        const result = { dp_no_parent_bought: final_dp_no_parent_bought, dp_parent_bought: final_dp_parent_bought };
        memo.set(u, result);
        return result;
    };

    // Employee 1 is the CEO and has no parent, so we use the 'no_parent_bought' state for the root.
    const { dp_no_parent_bought: final_dp_root_no_parent_bought } = dfs(1);

    // The maximum profit is the maximum value in the resulting DP array.
    // If no profitable trades can be made within the budget, the profit is 0.
    let max_overall_profit = 0;
    for (const profit of final_dp_root_no_parent_bought) {
        if (profit !== NEG_INF) {
            max_overall_profit = Math.max(max_overall_profit, profit);
        }
    }

    return max_overall_profit;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
interface DPResult {
    dp_no_parent_bought: number[];
    dp_parent_bought: number[];
}

function maxProfit(n: number, present: number[], future: number[], hierarchy: number[][], budget: number): number {
    const adj: number[][] = Array.from({ length: n + 1 }, () => []);
    for (const [u, v] of hierarchy) {
        adj[u].push(v);
    }

    const memo: Map<number, DPResult> = new Map();
    const NEG_INF = -Infinity;

    const dfs = (u: number): DPResult => {
        if (memo.has(u)) {
            return memo.get(u)!;
        }

        let current_dp_u_no_buy: number[] = new Array(budget + 1).fill(NEG_INF);
        current_dp_u_no_buy[0] = 0;

        const cost_u_normal = present[u-1];
        const profit_u_normal = future[u-1] - cost_u_normal;
        let current_dp_u_buy_normal: number[] = new Array(budget + 1).fill(NEG_INF);
        if (cost_u_normal <= budget) {
            current_dp_u_buy_normal[cost_u_normal] = profit_u_normal;
        }

        let current_dp_u_no_buy_if_parent_bought: number[] = new Array(budget + 1).fill(NEG_INF);
        current_dp_u_no_buy_if_parent_bought[0] = 0;

        const cost_u_discount = Math.floor(present[u-1] / 2);
        const profit_u_discount = future[u-1] - cost_u_discount;
        let current_dp_u_buy_discount: number[] = new Array(budget + 1).fill(NEG_INF);
        if (cost_u_discount <= budget) {
            current_dp_u_buy_discount[cost_u_discount] = profit_u_discount;
        }

        const mergeDps = (dp1: number[], dp2: number[]): number[] => {
            const new_dp: number[] = new Array(budget + 1).fill(NEG_INF);
            for (let k1 = 0; k1 <= budget; ++k1) {
                if (dp1[k1] === NEG_INF) {
                    continue;
                }
                for (let k2 = 0; k1 + k2 <= budget; ++k2) {
                    if (dp2[k2] === NEG_INF) {
                        continue;
                    }
                    new_dp[k1 + k2] = Math.max(new_dp[k1 + k2], dp1[k1] + dp2[k2]);
                }
            }
            return new_dp;
        };

        for (const v of adj[u]) {
            const { dp_no_parent_bought: res_v_no_parent_bought, dp_parent_bought: res_v_parent_bought } = dfs(v);

            current_dp_u_no_buy = mergeDps(current_dp_u_no_buy, res_v_no_parent_bought);
            current_dp_u_buy_normal = mergeDps(current_dp_u_buy_normal, res_v_parent_bought);
            current_dp_u_no_buy_if_parent_bought = mergeDps(current_dp_u_no_buy_if_parent_bought, res_v_no_parent_bought);
            current_dp_u_buy_discount = mergeDps(current_dp_u_buy_discount, res_v_parent_bought);
        }

        const final_dp_no_parent_bought: number[] = new Array(budget + 1).fill(NEG_INF);
        for (let k = 0; k <= budget; ++k) {
            final_dp_no_parent_bought[k] = Math.max(current_dp_u_no_buy[k], current_dp_u_buy_normal[k]);
        }

        const final_dp_parent_bought: number[] = new Array(budget + 1).fill(NEG_INF);
        for (let k = 0; k <= budget; ++k) {
            final_dp_parent_bought[k] = Math.max(current_dp_u_no_buy_if_parent_bought[k], current_dp_u_buy_discount[k]);
        }

        const result: DPResult = { dp_no_parent_bought: final_dp_no_parent_bought, dp_parent_bought: final_dp_parent_bought };
        memo.set(u, result);
        return result;
    };

    const { dp_no_parent_bought: final_dp_root_no_parent_bought } = dfs(1);

    let max_overall_profit = 0;
    for (const profit of final_dp_root_no_parent_bought) {
        if (profit !== NEG_INF) {
            max_overall_profit = Math.max(max_overall_profit, profit);
        }
    }

    return max_overall_profit;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
<?php

class Solution {
    private $adj;
    private $present_arr;
    private $future_arr;
    private $budget_val;
    private $memo;
    private const NEG_INF = -1000000000; // A sufficiently small number for -float('inf')

    /**
     * @param Integer $n
     * @param Integer[] $present
     * @param Integer[] $future
     * @param Integer[][] $hierarchy
     * @param Integer $budget
     * @return Integer
     */
    function maxProfit($n, $present, $future, $hierarchy, $budget) {
        $this->adj = array_fill(0, $n + 1, []);
        foreach ($hierarchy as $edge) {
            $u = $edge[0];
            $v = $edge[1];
            $this->adj[$u][] = $v;
        }

        $this->present_arr = $present;
        $this->future_arr = $future;
        $this->budget_val = $budget;
        $this->memo = [];

        $root_res = $this->dfs(1);

        $max_overall_profit = 0;
        foreach ($root_res['dp_no_parent_bought'] as $profit) {
            if ($profit !== self::NEG_INF) {
                $max_overall_profit = max($max_overall_profit, $profit);
            }
        }

        return $max_overall_profit;
    }

    private function dfs($u) {
        if (isset($this->memo[$u])) {
            return $this->memo[$u];
        }

        $current_dp_u_no_buy = array_fill(0, $this->budget_val + 1, self::NEG_INF);
        $current_dp_u_no_buy[0] = 0;

        $cost_u_normal = $this->present_arr[$u-1];
        $profit_u_normal = $this->future_arr[$u-1] - $cost_u_normal;
        $current_dp_u_buy_normal = array_fill(0, $this->budget_val + 1, self::NEG_INF);
        if ($cost_u_normal <= $this->budget_val) {
            $current_dp_u_buy_normal[$cost_u_normal] = $profit_u_normal;
        }

        $current_dp_u_no_buy_if_parent_bought = array_fill(0, $this->budget_val + 1, self::NEG_INF);
        $current_dp_u_no_buy_if_parent_bought[0] = 0;

        $cost_u_discount = floor($this->present_arr[$u-1] / 2); // Integer division is floor for positive numbers
        $profit_u_discount = $this->future_arr[$u-1] - $cost_u_discount;
        $current_dp_u_buy_discount = array_fill(0, $this->budget_val + 1, self::NEG_INF);
        if ($cost_u_discount <= $this->budget_val) {
            $current_dp_u_buy_discount[$cost_u_discount] = $profit_u_discount;
        }

        foreach ($this->adj[$u] as $v) {
            $res_v = $this->dfs($v);

            // Helper function to merge two DP arrays (knapsack-style combination)
            $merge_dps = function($dp1, $dp2) {
                $new_dp = array_fill(0, $this->budget_val + 1, self::NEG_INF);
                for ($k1 = 0; $k1 <= $this->budget_val; ++$k1) {
                    if ($dp1[$k1] === self::NEG_INF) {
                        continue;
                    }
                    for ($k2 = 0; $k1 + $k2 <= $this->budget_val; ++$k2) {
                        if ($dp2[$k2] === self::NEG_INF) {
                            continue;
                        }
                        $new_dp[$k1 + $k2] = max($new_dp[$k1 + $k2], $dp1[$k1] + $dp2[$k2]);
                    }
                }
                return $new_dp;
            };

            $current_dp_u_no_buy = $merge_dps($current_dp_u_no_buy, $res_v['dp_no_parent_bought']);
            $current_dp_u_buy_normal = $merge_dps($current_dp_u_buy_normal, $res_v['dp_parent_bought']);
            $current_dp_u_no_buy_if_parent_bought = $merge_dps($current_dp_u_no_buy_if_parent_bought, $res_v['dp_no_parent_bought']);
            $current_dp_u_buy_discount = $merge_dps($current_dp_u_buy_discount, $res_v['dp_parent_bought']);
        }

        $final_dp_no_parent_bought = array_fill(0, $this->budget_val + 1, self::NEG_INF);
        for ($k = 0; $k <= $this->budget_val; ++$k) {
            $final_dp_no_parent_bought[$k] = max($current_dp_u_no_buy[$k], $current_dp_u_buy_normal[$k]);
        }

        $final_dp_parent_bought = array_fill(0, $this->budget_val + 1, self::NEG_INF);
        for ($k = 0; $k <= $this->budget_val; ++$k) {
            $final_dp_parent_bought[$k] = max($current_dp_u_no_buy_if_parent_bought[$k], $current_dp_u_buy_discount[$k]);
        }

        $result = ['dp_no_parent_bought' => $final_dp_no_parent_bought, 'dp_parent_bought' => $final_dp_parent_bought];
        $this->memo[$u] = $result;
        return $result;
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
    // Using a custom class for memoization return type
    class DPResult {
        var dp_no_parent_bought: [Int]
        var dp_parent_bought: [Int]

        init(dp_no_parent_bought: [Int], dp_parent_bought: [Int]) {
            self.dp_no_parent_bought = dp_no_parent_bought
            self.dp_parent_bought = dp_parent_bought
        }
    }

    var memo: [Int: DPResult] = [:]
    var adj: [[Int]] = []
    var presentArr: [Int] = []
    var futureArr: [Int] = []
    var budgetVal: Int = 0
    let NEG_INF = -1_000_000_000 // A sufficiently small number for -float('inf')

    private func dfs(_ u: Int) -> DPResult {
        if let result = memo[u] {
            return result
        }

        var current_dp_u_no_buy = Array(repeating: NEG_INF, count: budgetVal + 1)
        current_dp_u_no_buy[0] = 0

        let cost_u_normal = presentArr[u-1]
        let profit_u_normal = futureArr[u-1] - cost_u_normal
        var current_dp_u_buy_normal = Array(repeating: NEG_INF, count: budgetVal + 1)
        if cost_u_normal <= budgetVal {
            current_dp_u_buy_normal[cost_u_normal] = profit_u_normal
        }

        var current_dp_u_no_buy_if_parent_bought = Array(repeating: NEG_INF, count: budgetVal + 1)
        current_dp_u_no_buy_if_parent_bought[0] = 0

        let cost_u_discount = presentArr[u-1] / 2 // Integer division is floor for positive numbers
        let profit_u_discount = futureArr[u-1] - cost_u_discount
        var current_dp_u_buy_discount = Array(repeating: NEG_INF, count: budgetVal + 1)
        if cost_u_discount <= budgetVal {
            current_dp_u_buy_discount[cost_u_discount] = profit_u_discount
        }

        for v in adj[u] {
            let res_v = dfs(v)

            // Helper function to merge two DP arrays (knapsack-style combination)
            let mergeDps = { (dp1: [Int], dp2: [Int]) -> [Int] in
                var new_dp = Array(repeating: self.NEG_INF, count: self.budgetVal + 1)
                for k1 in 0...self.budgetVal {
                    if dp1[k1] == self.NEG_INF {
                        continue
                    }
                    for k2 in 0...(self.budgetVal - k1) {
                        if dp2[k2] == self.NEG_INF {
                            continue
                        }
                        new_dp[k1 + k2] = max(new_dp[k1 + k2], dp1[k1] + dp2[k2])
                    }
                }
                return new_dp
            }

            current_dp_u_no_buy = mergeDps(current_dp_u_no_buy, res_v.dp_no_parent_bought)
            current_dp_u_buy_normal = mergeDps(current_dp_u_buy_normal, res_v.dp_parent_bought)
            current_dp_u_no_buy_if_parent_bought = mergeDps(current_dp_u_no_buy_if_parent_bought, res_v.dp_no_parent_bought)
            current_dp_u_buy_discount = mergeDps(current_dp_u_buy_discount, res_v.dp_parent_bought)
        }

        var final_dp_no_parent_bought = Array(repeating: NEG_INF, count: budgetVal + 1)
        for k in 0...budgetVal {
            final_dp_no_parent_bought[k] = max(current_dp_u_no_buy[k], current_dp_u_buy_normal[k])
        }

        var final_dp_parent_bought = Array(repeating: NEG_INF, count: budgetVal + 1)
        for k in 0...budgetVal {
            final_dp_parent_bought[k] = max(current_dp_u_no_buy_if_parent_bought[k], current_dp_u_buy_discount[k])
        }

        let result = DPResult(dp_no_parent_bought: final_dp_no_parent_bought, dp_parent_bought: final_dp_parent_bought)
        memo[u] = result
        return result
    }

    func maxProfit(_ n: Int, _ present: [Int], _ future: [Int], _ hierarchy: [[Int]], _ budget: Int) -> Int {
        adj = Array(repeating: [], count: n + 1)
        for edge in hierarchy {
            adj[edge[0]].append(edge[1])
        }

        presentArr = present
        futureArr = future
        budgetVal = budget
        memo.removeAll()

        let root_res = dfs(1)

        var max_overall_profit = 0
        for profit in root_res.dp_no_parent_bought {
            if profit != NEG_INF {
                max_overall_profit = max(max_overall_profit, profit)
            }
        }

        return max_overall_profit
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
import java.util.*

class Solution {
    // Using a custom data class for memoization return type
    data class DPResult(
        val dp_no_parent_bought: IntArray,
        val dp_parent_bought: IntArray
    )

    private lateinit var memo: MutableMap<Int, DPResult>
    private lateinit var adj: List<MutableList<Int>>
    private lateinit var presentArr: IntArray
    private lateinit var futureArr: IntArray
    private var budgetVal: Int = 0
    private val NEG_INF = -1_000_000_000 // A sufficiently small number for -float('inf')

    private fun dfs(u: Int): DPResult {
        if (memo.containsKey(u)) {
            return memo[u]!!
        }

        var current_dp_u_no_buy = IntArray(budgetVal + 1) { NEG_INF }
        current_dp_u_no_buy[0] = 0

        val cost_u_normal = presentArr[u-1]
        val profit_u_normal = futureArr[u-1] - cost_u_normal
        var current_dp_u_buy_normal = IntArray(budgetVal + 1) { NEG_INF }
        if (cost_u_normal <= budgetVal) {
            current_dp_u_buy_normal[cost_u_normal] = profit_u_normal
        }

        var current_dp_u_no_buy_if_parent_bought = IntArray(budgetVal + 1) { NEG_INF }
        current_dp_u_no_buy_if_parent_bought[0] = 0

        val cost_u_discount = presentArr[u-1] / 2 // Integer division is floor for positive numbers
        val profit_u_discount = futureArr[u-1] - cost_u_discount
        var current_dp_u_buy_discount = IntArray(budgetVal + 1) { NEG_INF }
        if (cost_u_discount <= budgetVal) {
            current_dp_u_buy_discount[cost_u_discount] = profit_u_discount
        }

        for (v in adj[u]) {
            val res_v = dfs(v)

            // Helper function to merge two DP arrays (knapsack-style combination)
            val mergeDps = { dp1: IntArray, dp2: IntArray ->
                val new_dp = IntArray(budgetVal + 1) { NEG_INF }
                for (k1 in 0..budgetVal) {
                    if (dp1[k1] == NEG_INF) {
                        continue
                    }
                    for (k2 in 0..(budgetVal - k1)) {
                        if (dp2[k2] == NEG_INF) {
                            continue
                        }
                        new_dp[k1 + k2] = maxOf(new_dp[k1 + k2], dp1[k1] + dp2[k2])
                    }
                }
                new_dp
            }

            current_dp_u_no_buy = mergeDps(current_dp_u_no_buy, res_v.dp_no_parent_bought)
            current_dp_u_buy_normal = mergeDps(current_dp_u_buy_normal, res_v.dp_parent_bought)
            current_dp_u_no_buy_if_parent_bought = mergeDps(current_dp_u_no_buy_if_parent_bought, res_v.dp_no_parent_bought)
            current_dp_u_buy_discount = mergeDps(current_dp_u_buy_discount, res_v.dp_parent_bought)
        }

        val final_dp_no_parent_bought = IntArray(budgetVal + 1) { NEG_INF }
        for (k in 0..budgetVal) {
            final_dp_no_parent_bought[k] = maxOf(current_dp_u_no_buy[k], current_dp_u_buy_normal[k])
        }

        val final_dp_parent_bought = IntArray(budgetVal + 1) { NEG_INF }
        for (k in 0..budgetVal) {
            final_dp_parent_bought[k] = maxOf(current_dp_u_no_buy_if_parent_bought[k], current_dp_u_buy_discount[k])
        }

        val result = DPResult(final_dp_no_parent_bought, final_dp_parent_bought)
        memo[u] = result
        return result
    }

    fun maxProfit(n: Int, present: IntArray, future: IntArray, hierarchy: Array<IntArray>, budget: Int): Int {
        adj = List(n + 1) { mutableListOf() }
        for (edge in hierarchy) {
            adj[edge[0]].add(edge[1])
        }

        presentArr = present
        futureArr = future
        budgetVal = budget
        memo = mutableMapOf()

        val root_res = dfs(1)

        var max_overall_profit = 0
        for (profit in root_res.dp_no_parent_bought) {
            if (profit != NEG_INF) {
                max_overall_profit = maxOf(max_overall_profit, profit)
            }
        }

        return max_overall_profit
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
import 'dart:collection';
import 'dart:math';

class Solution {
  // Using a custom class for memoization return type
  class DPResult {
    List<int> dp_no_parent_bought;
    List<int> dp_parent_bought;

    DPResult(this.dp_no_parent_bought, this.dp_parent_bought);
  }

  late Map<int, DPResult> memo;
  late List<List<int>> adj;
  late List<int> presentArr;
  late List<int> futureArr;
  late int budgetVal;
  static const int NEG_INF = -1000000000; // A sufficiently small number for -float('inf')

  DPResult _dfs(int u) {
    if (memo.containsKey(u)) {
      return memo[u]!;
    }

    List<int> current_dp_u_no_buy = List.filled(budgetVal + 1, NEG_INF);
    current_dp_u_no_buy[0] = 0;

    int cost_u_normal = presentArr[u-1];
    int profit_u_normal = futureArr[u-1] - cost_u_normal;
    List<int> current_dp_u_buy_normal = List.filled(budgetVal + 1, NEG_INF);
    if (cost_u_normal <= budgetVal) {
      current_dp_u_buy_normal[cost_u_normal] = profit_u_normal;
    }

    List<int> current_dp_u_no_buy_if_parent_bought = List.filled(budgetVal + 1, NEG_INF);
    current_dp_u_no_buy_if_parent_bought[0] = 0;

    int cost_u_discount = (presentArr[u-1] / 2).floor(); // Integer division is floor for positive numbers
    int profit_u_discount = futureArr[u-1] - cost_u_discount;
    List<int> current_dp_u_buy_discount = List.filled(budgetVal + 1, NEG_INF);
    if (cost_u_discount <= budgetVal) {
      current_dp_u_buy_discount[cost_u_discount] = profit_u_discount;
    }

    for (int v in adj[u]) {
      DPResult res_v = _dfs(v);

      // Helper function to merge two DP arrays (knapsack-style combination)
      List<int> mergeDps(List<int> dp1, List<int> dp2) {
        List<int> new_dp = List.filled(budgetVal + 1, NEG_INF);
        for (int k1 = 0; k1 <= budgetVal; ++k1) {
          if (dp1[k1] == NEG_INF) {
            continue;
          }
          for (int k2 = 0; k1 + k2 <= budgetVal; ++k2) {
            if (dp2[k2] == NEG_INF) {
              continue;
            }
            new_dp[k1 + k2] = max(new_dp[k1 + k2], dp1[k1] + dp2[k2]);
          }
        }
        return new_dp;
      }

      current_dp_u_no_buy = mergeDps(current_dp_u_no_buy, res_v.dp_no_parent_bought);
      current_dp_u_buy_normal = mergeDps(current_dp_u_buy_normal, res_v.dp_parent_bought);
      current_dp_u_no_buy_if_parent_bought = mergeDps(current_dp_u_no_buy_if_parent_bought, res_v.dp_no_parent_bought);
      current_dp_u_buy_discount = mergeDps(current_dp_u_buy_discount, res_v.dp_parent_bought);
    }

    List<int> final_dp_no_parent_bought = List.filled(budgetVal + 1, NEG_INF);
    for (int k = 0; k <= budgetVal; ++k) {
      final_dp_no_parent_bought[k] = max(current_dp_u_no_buy[k], current_dp_u_buy_normal[k]);
    }

    List<int> final_dp_parent_bought = List.filled(budgetVal + 1, NEG_INF);
    for (int k = 0; k <= budgetVal; ++k) {
      final_dp_parent_bought[k] = max(current_dp_u_no_buy_if_parent_bought[k], current_dp_u_buy_discount[k]);
    }

    DPResult result = DPResult(final_dp_no_parent_bought, final_dp_parent_bought);
    memo[u] = result;
    return result;
  }

  int maxProfit(int n, List<int> present, List<int> future, List<List<int>> hierarchy, int budget) {
    adj = List.generate(n + 1, (_) => []);
    for (List<int> edge in hierarchy) {
      adj[edge[0]].add(edge[1]);
    }

    presentArr = present;
    futureArr = future;
    budgetVal = budget;
    memo = HashMap();

    DPResult root_res = _dfs(1);

    int maxOverallProfit = 0;
    for (int profit in root_res.dp_no_parent_bought) {
      if (profit != NEG_INF) {
        maxOverallProfit = max(maxOverallProfit, profit);
      }
    }

    return maxOverallProfit;
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

// DPResult struct to hold DP results for a subtree
type DPResult struct {
	dp_no_parent_bought []int
	dp_parent_bought  []int
}

type Solution struct {
	memo      map[int]DPResult
	adj       [][]int
	presentArr []int
	futureArr  []int
	budgetVal int
}

const NEG_INF = -1_000_000_000 // A sufficiently small number for -float('inf')

func (s *Solution) dfs(u int) DPResult {
	if result, ok := s.memo[u]; ok {
		return result
	}

	current_dp_u_no_buy := make([]int, s.budgetVal+1)
	for i := range current_dp_u_no_buy {
		current_dp_u_no_buy[i] = NEG_INF
	}
	current_dp_u_no_buy[0] = 0

	cost_u_normal := s.presentArr[u-1]
	profit_u_normal := s.futureArr[u-1] - cost_u_normal
	current_dp_u_buy_normal := make([]int, s.budgetVal+1)
	for i := range current_dp_u_buy_normal {
		current_dp_u_buy_normal[i] = NEG_INF
	}
	if cost_u_normal <= s.budgetVal {
		current_dp_u_buy_normal[cost_u_normal] = profit_u_normal
	}

	current_dp_u_no_buy_if_parent_bought := make([]int, s.budgetVal+1)
	for i := range current_dp_u_no_buy_if_parent_bought {
		current_dp_u_no_buy_if_parent_bought[i] = NEG_INF
	}
	current_dp_u_no_buy_if_parent_bought[0] = 0

	cost_u_discount := s.presentArr[u-1] / 2 // Integer division is floor for positive numbers
	profit_u_discount := s.futureArr[u-1] - cost_u_discount
	current_dp_u_buy_discount := make([]int, s.budgetVal+1)
	for i := range current_dp_u_buy_discount {
		current_dp_u_buy_discount[i] = NEG_INF
	}
	if cost_u_discount <= s.budgetVal {
		current_dp_u_buy_discount[cost_u_discount] = profit_u_discount
	}

	for _, v := range s.adj[u] {
		res_v := s.dfs(v)

		// Helper function to merge two DP arrays (knapsack-style combination)
		mergeDps := func(dp1, dp2 []int) []int {
			new_dp := make([]int, s.budgetVal+1)
			for i := range new_dp {
				new_dp[i] = NEG_INF
			}
			for k1 := 0; k1 <= s.budgetVal; k1++ {
				if dp1[k1] == NEG_INF {
					continue
				}
				for k2 := 0; k1+k2 <= s.budgetVal; k2++ {
					if dp2[k2] == NEG_INF {
						continue
					}
					new_dp[k1+k2] = int(math.Max(float64(new_dp[k1+k2]), float64(dp1[k1]+dp2[k2])))
				}
			}
			return new_dp
		}

		current_dp_u_no_buy = mergeDps(current_dp_u_no_buy, res_v.dp_no_parent_bought)
		current_dp_u_buy_normal = mergeDps(current_dp_u_buy_normal, res_v.dp_parent_bought)
		current_dp_u_no_buy_if_parent_bought = mergeDps(current_dp_u_no_buy_if_parent_bought, res_v.dp_no_parent_bought)
		current_dp_u_buy_discount = mergeDps(current_dp_u_buy_discount, res_v.dp_parent_bought)
	}

	final_dp_no_parent_bought := make([]int, s.budgetVal+1)
	for i := range final_dp_no_parent_bought {
		final_dp_no_parent_bought[i] = NEG_INF
	}
	for k := 0; k <= s.budgetVal; k++ {
		final_dp_no_parent_bought[k] = int(math.Max(float64(current_dp_u_no_buy[k]), float64(current_dp_u_buy_normal[k])))
	}

	final_dp_parent_bought := make([]int, s.budgetVal+1)
	for i := range final_dp_parent_bought {
		final_dp_parent_bought[i] = NEG_INF
	}
	for k := 0; k <= s.budgetVal; k++ {
		final_dp_parent_bought[k] = int(math.Max(float64(current_dp_u_no_buy_if_parent_bought[k]), float64(current_dp_u_buy_discount[k])))
	}

	result := DPResult{dp_no_parent_bought: final_dp_no_parent_bought, dp_parent_bought: final_dp_parent_bought}
	s.memo[u] = result
	return result
}

func maxProfit(n int, present []int, future []int, hierarchy [][]int, budget int) int {
	s := &Solution{
		memo:      make(map[int]DPResult),
		adj:       make([][]int, n+1),
		presentArr: present,
		futureArr:  future,
		budgetVal: budget,
	}

	for _, edge := range hierarchy {
		u, v := edge[0], edge[1]
		s.adj[u] = append(s.adj[u], v)
	}

	root_res := s.dfs(1)

	max_overall_profit := 0
	for _, profit := range root_res.dp_no_parent_bought {
		if profit != NEG_INF {
			max_overall_profit = int(math.Max(float64(max_overall_profit), float64(profit)))
		}
	}

	return max_overall_profit
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
class Solution
    # Using a custom class for memoization return type
    DPResult = Struct.new(:dp_no_parent_bought, :dp_parent_bought)

    attr_accessor :adj, :present_arr, :future_arr, :budget_val, :memo
    NEG_INF = -1_000_000_000 # A sufficiently small number for -Float::INFINITY

    def dfs(u)
        return memo[u] if memo.key?(u)

        current_dp_u_no_buy = Array.new(budget_val + 1, NEG_INF)
        current_dp_u_no_buy[0] = 0

        cost_u_normal = present_arr[u-1]
        profit_u_normal = future_arr[u-1] - cost_u_normal
        current_dp_u_buy_normal = Array.new(budget_val + 1, NEG_INF)
        if cost_u_normal <= budget_val
            current_dp_u_buy_normal[cost_u_normal] = profit_u_normal
        end

        current_dp_u_no_buy_if_parent_bought = Array.new(budget_val + 1, NEG_INF)
        current_dp_u_no_buy_if_parent_bought[0] = 0

        cost_u_discount = (present_arr[u-1] / 2).floor # Integer division is floor for positive numbers
        profit_u_discount = future_arr[u-1] - cost_u_discount
        current_dp_u_buy_discount = Array.new(budget_val + 1, NEG_INF)
        if cost_u_discount <= budget_val
            current_dp_u_buy_discount[cost_u_discount] = profit_u_discount
        end

        adj[u].each do |v|
            res_v = dfs(v)

            # Helper function to merge two DP arrays (knapsack-style combination)
            merge_dps = ->(dp1, dp2) do
                new_dp = Array.new(budget_val + 1, NEG_INF)
                (0..budget_val).each do |k1|
                    next if dp1[k1] == NEG_INF
                    (0..(budget_val - k1)).each do |k2|
                        next if dp2[k2] == NEG_INF
                        new_dp[k1 + k2] = [new_dp[k1 + k2], dp1[k1] + dp2[k2]].max
                    end
                end
                new_dp
            end

            current_dp_u_no_buy = merge_dps.call(current_dp_u_no_buy, res_v.dp_no_parent_bought)
            current_dp_u_buy_normal = merge_dps.call(current_dp_u_buy_normal, res_v.dp_parent_bought)
            current_dp_u_no_buy_if_parent_bought = merge_dps.call(current_dp_u_no_buy_if_parent_bought, res_v.dp_no_parent_bought)
            current_dp_u_buy_discount = merge_dps.call(current_dp_u_buy_discount, res_v.dp_parent_bought)
        end

        final_dp_no_parent_bought = Array.new(budget_val + 1, NEG_INF)
        (0..budget_val).each do |k|
            final_dp_no_parent_bought[k] = [current_dp_u_no_buy[k], current_dp_u_buy_normal[k]].max
        end

        final_dp_parent_bought = Array.new(budget_val + 1, NEG_INF)
        (0..budget_val).each do |k|
            final_dp_parent_bought[k] = [current_dp_u_no_buy_if_parent_bought[k], current_dp_u_buy_discount[k]].max
        end

        result = DPResult.new(final_dp_no_parent_bought, final_dp_parent_bought)
        memo[u] = result
        result
    end

    def max_profit(n, present, future, hierarchy, budget)
        self.adj = Array.new(n + 1) { [] }
        hierarchy.each do |u, v|
            adj[u] << v
        end

        self.present_arr = present
        self.future_arr = future
        self.budget_val = budget
        self.memo = {}

        root_res = dfs(1)

        max_overall_profit = 0
        root_res.dp_no_parent_bought.each do |profit|
            if profit != NEG_INF
                max_overall_profit = [max_overall_profit, profit].max
            end
        end

        max_overall_profit
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.collection.mutable

class Solution {
  // Using a custom case class for memoization return type
  case class DPResult(
    dp_no_parent_bought: Array[Int],
    dp_parent_bought: Array[Int]
  )

  private var adj: Array[mutable.ListBuffer[Int]] = _
  private var presentArr: Array[Int] = _
  private var futureArr: Array[Int] = _
  private var budgetVal: Int = _
  private val memo: mutable.Map[Int, DPResult] = mutable.Map()
  private val NEG_INF = -1_000_000_000 // A sufficiently small number for -Float.Infinity

  private def dfs(u: Int): DPResult = {
    memo.get(u) match {
      case Some(result) => result
      case None =>
        var current_dp_u_no_buy = Array.fill(budgetVal + 1)(NEG_INF)
        current_dp_u_no_buy(0) = 0

        val cost_u_normal = presentArr(u - 1)
        val profit_u_normal = futureArr(u - 1) - cost_u_normal
        var current_dp_u_buy_normal = Array.fill(budgetVal + 1)(NEG_INF)
        if (cost_u_normal <= budgetVal) {
          current_dp_u_buy_normal(cost_u_normal) = profit_u_normal
        }

        var current_dp_u_no_buy_if_parent_bought = Array.fill(budgetVal + 1)(NEG_INF)
        current_dp_u_no_buy_if_parent_bought(0) = 0

        val cost_u_discount = presentArr(u - 1) / 2 // Integer division is floor for positive numbers
        val profit_u_discount = futureArr(u - 1) - cost_u_discount
        var current_dp_u_buy_discount = Array.fill(budgetVal + 1)(NEG_INF)
        if (cost_u_discount <= budgetVal) {
          current_dp_u_buy_discount(cost_u_discount) = profit_u_discount
        }

        for (v <- adj(u)) {
          val res_v = dfs(v)

          // Helper function to merge two DP arrays (knapsack-style combination)
          def mergeDps(dp1: Array[Int], dp2: Array[Int]): Array[Int] = {
            val new_dp = Array.fill(budgetVal + 1)(NEG_INF)
            for (k1 <- 0 to budgetVal) {
              if (dp1(k1) == NEG_INF) {
                // continue
              } else {
                for (k2 <- 0 to (budgetVal - k1)) {
                  if (dp2(k2) == NEG_INF) {
                    // continue
                  } else {
                    new_dp(k1 + k2) = math.max(new_dp(k1 + k2), dp1(k1) + dp2(k2))
                  }
                }
              }
            }
            new_dp
          }

          current_dp_u_no_buy = mergeDps(current_dp_u_no_buy, res_v.dp_no_parent_bought)
          current_dp_u_buy_normal = mergeDps(current_dp_u_buy_normal, res_v.dp_parent_bought)
          current_dp_u_no_buy_if_parent_bought = mergeDps(current_dp_u_no_buy_if_parent_bought, res_v.dp_no_parent_bought)
          current_dp_u_buy_discount = mergeDps(current_dp_u_buy_discount, res_v.dp_parent_bought)
        }

        val final_dp_no_parent_bought = Array.fill(budgetVal + 1)(NEG_INF)
        for (k <- 0 to budgetVal) {
          final_dp_no_parent_bought(k) = math.max(current_dp_u_no_buy(k), current_dp_u_buy_normal(k))
        }

        val final_dp_parent_bought = Array.fill(budgetVal + 1)(NEG_INF)
        for (k <- 0 to budgetVal) {
          final_dp_parent_bought(k) = math.max(current_dp_u_no_buy_if_parent_bought(k), current_dp_u_buy_discount(k))
        }

        val result = DPResult(final_dp_no_parent_bought, final_dp_parent_bought)
        memo(u) = result
        result
    }

  def maxProfit(n: Int, present: Array[Int], future: Array[Int], hierarchy: Array[Array[Int]], budget: Int): Int = {
    adj = Array.fill(n + 1)(mutable.ListBuffer[Int]())
    for (edge <- hierarchy) {
      adj(edge(0)) += edge(1)
    }

    presentArr = present
    futureArr = future
    budgetVal = budget
    memo.clear()

    val root_res = dfs(1)

    var max_overall_profit = 0
    for (profit <- root_res.dp_no_parent_bought) {
      if (profit != NEG_INF) {
        max_overall_profit = math.max(max_overall_profit, profit)
      }
    }

    max_overall_profit
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
use std::collections::HashMap;
use std::cmp::max;

const NEG_INF: i32 = -1_000_000_000; // A sufficiently small number for -float('inf')

// DPResult struct to hold DP results for a subtree
#[derive(Clone)] // Needed for storing in HashMap and returning copies
struct DPResult {
    dp_no_parent_bought: Vec<i32>,
    dp_parent_bought: Vec<i32>,
}

struct SolutionData {
    memo: HashMap<i32, DPResult>,
    adj: Vec<Vec<i32>>,
    present_arr: Vec<i32>,
    future_arr: Vec<i32>,
    budget_val: i32,
}

impl SolutionData {
    fn dfs(&mut self, u: i32) -> DPResult {
        if let Some(result) = self.memo.get(&u) {
            return result.clone();
        }

        let mut current_dp_u_no_buy = vec![NEG_INF; (self.budget_val + 1) as usize];
        current_dp_u_no_buy[0] = 0;

        let cost_u_normal = self.present_arr[(u - 1) as usize];
        let profit_u_normal = self.future_arr[(u - 1) as usize] - cost_u_normal;
        let mut current_dp_u_buy_normal = vec![NEG_INF; (self.budget_val + 1) as usize];
        if cost_u_normal <= self.budget_val {
            current_dp_u_buy_normal[cost_u_normal as usize] = profit_u_normal;
        }

        let mut current_dp_u_no_buy_if_parent_bought = vec![NEG_INF; (self.budget_val + 1) as usize];
        current_dp_u_no_buy_if_parent_bought[0] = 0;

        let cost_u_discount = self.present_arr[(u - 1) as usize] / 2; // Integer division is floor for positive numbers
        let profit_u_discount = self.future_arr[(u - 1) as usize] - cost_u_discount;
        let mut current_dp_u_buy_discount = vec![NEG_INF; (self.budget_val + 1) as usize];
        if cost_u_discount <= self.budget_val {
            current_dp_u_buy_discount[cost_u_discount as usize] = profit_u_discount;
        }

        for &v in &self.adj[u as usize] {
            let res_v = self.dfs(v);

            // Helper function to merge two DP arrays (knapsack-style combination)
            let merge_dps = |dp1: &[i32], dp2: &[i32]| -> Vec<i32> {
                let mut new_dp = vec![NEG_INF; (self.budget_val + 1) as usize];
                for k1 in 0..=self.budget_val {
                    if dp1[k1 as usize] == NEG_INF {
                        continue;
                    }
                    for k2 in 0..=(self.budget_val - k1) {
                        if dp2[k2 as usize] == NEG_INF {
                            continue;
                        }
                        let total_cost = (k1 + k2) as usize;
                        new_dp[total_cost] = max(new_dp[total_cost], dp1[k1 as usize] + dp2[k2 as usize]);
                    }
                }
                new_dp
            };

            current_dp_u_no_buy = merge_dps(&current_dp_u_no_buy, &res_v.dp_no_parent_bought);
            current_dp_u_buy_normal = merge_dps(&current_dp_u_buy_normal, &res_v.dp_parent_bought);
            current_dp_u_no_buy_if_parent_bought = merge_dps(&current_dp_u_no_buy_if_parent_bought, &res_v.dp_no_parent_bought);
            current_dp_u_buy_discount = merge_dps(&current_dp_u_buy_discount, &res_v.dp_parent_bought);
        }

        let mut final_dp_no_parent_bought = vec![NEG_INF; (self.budget_val + 1) as usize];
        for k in 0..=self.budget_val {
            final_dp_no_parent_bought[k as usize] = max(current_dp_u_no_buy[k as usize], current_dp_u_buy_normal[k as usize]);
        }

        let mut final_dp_parent_bought = vec![NEG_INF; (self.budget_val + 1) as usize];
        for k in 0..=self.budget_val {
            final_dp_parent_bought[k as usize] = max(current_dp_u_no_buy_if_parent_bought[k as usize], current_dp_u_buy_discount[k as usize]);
        }

        let result = DPResult { dp_no_parent_bought: final_dp_no_parent_bought, dp_parent_bought: final_dp_parent_bought };
        self.memo.insert(u, result.clone());
        result
    }
}

impl Solution {
    pub fn max_profit(n: i32, present: Vec<i32>, future: Vec<i32>, hierarchy: Vec<Vec<i32>>, budget: i32) -> i32 {
        let mut adj: Vec<Vec<i32>> = vec![vec![]; (n + 1) as usize];
        for edge in hierarchy {
            let u = edge[0];
            let v = edge[1];
            adj[u as usize].push(v);
        }

        let mut solution_data = SolutionData {
            memo: HashMap::new(),
            adj,
            present_arr: present,
            future_arr: future,
            budget_val: budget,
        };

        let root_res = solution_data.dfs(1);

        let mut max_overall_profit = 0;
        for &profit in &root_res.dp_no_parent_bought {
            if profit != NEG_INF {
                max_overall_profit = max(max_overall_profit, profit);
            }
        }

        max_overall_profit
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket

(define (max-profit n present future hierarchy budget)
  (define adj (make-vector (+ n 1) '()))
  (for-each (lambda (edge)
              (define u (car edge))
              (define v (cadr edge))
              (vector-set! adj u (cons v (vector-ref adj u))))
            hierarchy)

  (define memo (make-hash))
  (define NEG-INF -1000000000) ; A sufficiently small number

  (define (dfs u)
    (hash-ref! memo u
               (lambda ()
                 (define (make-dp-array)
                   (build-list (+ budget 1) (lambda (_) NEG-INF)))

                 (define (merge-dps dp1 dp2)
                   (define new-dp (make-dp-array))
                   (for ([k1 (in-range (+ budget 1))])
                     (when (not (= (list-ref dp1 k1) NEG-INF))
                       (for ([k2 (in-range (+ (- budget k1) 1))])
                         (when (not (= (list-ref dp2 k2) NEG-INF))
                           (set!-list-ref! new-dp (+ k1 k2)
                                          (max (list-ref new-dp (+ k1 k2))
                                               (+ (list-ref dp1 k1) (list-ref dp2 k2))))))))
                   new-dp)

                 (define current-dp-u-no-buy (make-dp-array))
                 (set!-list-ref! current-dp-u-no-buy 0 0)

                 (define cost-u-normal (list-ref present (- u 1)))
                 (define profit-u-normal (- (list-ref future (- u 1)) cost-u-normal))
                 (define current-dp-u-buy-normal (make-dp-array))
                 (when (<= cost-u-normal budget)
                   (set!-list-ref! current-dp-u-buy-normal cost-u-normal profit-u-normal))

                 (define current-dp-u-no-buy-if-parent-bought (make-dp-array))
                 (set!-list-ref! current-dp-u-no-buy-if-parent-bought 0 0)

                 (define cost-u-discount (floor (/ (list-ref present (- u 1)) 2)))
                 (define profit-u-discount (- (list-ref future (- u 1)) cost-u-discount))
                 (define current-dp-u-buy-discount (make-dp-array))
                 (when (<= cost-u-discount budget)
                   (set!-list-ref! current-dp-u-buy-discount cost-u-discount profit-u-discount))

                 (for-each (lambda (v)
                             (define res-v (dfs v))
                             (define res-v-no-parent-bought (car res-v))
                             (define res-v-parent-bought (cdr res-v))

                             (set! current-dp-u-no-buy (merge-dps current-dp-u-no-buy res-v-no-parent-bought))
                             (set! current-dp-u-buy-normal (merge-dps current-dp-u-buy-normal res-v-parent-bought))
                             (set! current-dp-u-no-buy-if-parent-bought (merge-dps current-dp-u-no-buy-if-parent-bought res-v-no-parent-bought))
                             (set! current-dp-u-buy-discount (merge-dps current-dp-u-buy-discount res-v-parent-bought)))
                           (vector-ref adj u))

                 (define final-dp-no-parent-bought (make-dp-array))
                 (for ([k (in-range (+ budget 1))])
                   (set!-list-ref! final-dp-no-parent-bought k
                                  (max (list-ref current-dp-u-no-buy k)
                                       (list-ref current-dp-u-buy-normal k))))

                 (define final-dp-parent-bought (make-dp-array))
                 (for ([k (in-range (+ budget 1))])
                   (set!-list-ref! final-dp-parent-bought k
                                  (max (list-ref current-dp-u-no-buy-if-parent-bought k)
                                       (list-ref current-dp-u-buy-discount k))))

                 (cons final-dp-no-parent-bought final-dp-parent-bought))))

  (define root-res (dfs 1))
  (define final-dp-root-no-parent-bought (car root-res))

  (define max-overall-profit 0)
  (for-each (lambda (profit)
              (when (not (= profit NEG-INF))
                (set! max-overall-profit (max max-overall-profit profit))))
            final-dp-root-no-parent-bought)

  max-overall-profit)

(define (set!-list-ref! lst idx val)
  (set-car! (list-tail lst idx) val))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([max_profit/5]).

-define(NEG_INF, -1_000_000_000). % A sufficiently small number

% Helper function to create a DP array initialized with NEG_INF, 0 at index 0
make_dp_array(Budget) ->
    Arr = array:new([{fixed, true}, {size, Budget + 1}, {default, ?NEG_INF}]),
    array:set(0, 0, Arr).

% Helper function to merge two DP arrays (knapsack-style combination)
merge_dps(Dp1, Dp2, Budget) ->
    NewDp = make_dp_array(Budget),
    merge_dps_loop(0, Dp1, Dp2, NewDp, Budget).

merge_dps_loop(K1, Dp1, Dp2, NewDp, Budget) when K1 =< Budget ->
    Val1 = array:get(K1, Dp1),
    case Val1 of
        ?NEG_INF -> merge_dps_loop(K1 + 1, Dp1, Dp2, NewDp, Budget);
        _ ->
            NewDp2 = merge_dps_inner_loop(K1, 0, Val1, Dp2, NewDp, Budget),
            merge_dps_loop(K1 + 1, Dp1, Dp2, NewDp2, Budget)
    end;
merge_dps_loop(_K1, _Dp1, _Dp2, NewDp, _Budget) ->
    NewDp.

merge_dps_inner_loop(K1, K2, Val1, Dp2, NewDp, Budget) when K1 + K2 =< Budget ->
    Val2 = array:get(K2, Dp2),
    case Val2 of
        ?NEG_INF -> merge_dps_inner_loop(K1, K2 + 1, Val1, Dp2, NewDp, Budget);
        _ ->
            CurrentMax = array:get(K1 + K2, NewDp),
            NewVal = Val1 + Val2,
            UpdatedNewDp = array:set(K1 + K2, max(CurrentMax, NewVal), NewDp),
            merge_dps_inner_loop(K1, K2 + 1, Val1, Dp2, UpdatedNewDp, Budget)
    end;
merge_dps_inner_loop(_K1, _K2, _Val1, _Dp2, NewDp, _Budget) ->
    NewDp.

% DFS function
dfs(U, Adj, PresentArr, FutureArr, Budget, Memo) ->
    case maps:find(U, Memo) of
        {ok, Result} -> {Result, Memo};
        _ ->
            CurrentDpUNoBuy = make_dp_array(Budget),

            CostUNormal = array:get(U - 1, PresentArr),
            ProfitUNormal = array:get(U - 1, FutureArr) - CostUNormal,
            CurrentDpUBuyNormal = make_dp_array(Budget),
            UpdatedCurrentDpUBuyNormal = 
                if CostUNormal =< Budget -> array:set(CostUNormal, ProfitUNormal, CurrentDpUBuyNormal);
                true -> CurrentDpUBuyNormal
                end,

            CurrentDpUNoBuyIfParentBought = make_dp_array(Budget),

            CostUDiscount = trunc(array:get(U - 1, PresentArr) / 2),
            ProfitUDiscount = array:get(U - 1, FutureArr) - CostUDiscount,
            CurrentDpUBuyDiscount = make_dp_array(Budget),
            UpdatedCurrentDpUBuyDiscount = 
                if CostUDiscount =< Budget -> array:set(CostUDiscount, ProfitUDiscount, CurrentDpUBuyDiscount);
                true -> CurrentDpUBuyDiscount
                end,

            {FinalDpUNoBuy, FinalDpUBuyNormal, FinalDpUNoBuyIfParentBought, FinalDpUBuyDiscount, UpdatedMemo} = 
                lists:foldl(
                    fun(V, {AccDpUNoBuy, AccDpUBuyNormal, AccDpUNoBuyIfParentBought, AccDpUBuyDiscount, CurrentMemo}) ->
                        {ResV, NextMemo} = dfs(V, Adj, PresentArr, FutureArr, Budget, CurrentMemo),
                        {ResVNoParentBought, ResVParentBought} = ResV,

                        NextDpUNoBuy = merge_dps(AccDpUNoBuy, ResVNoParentBought, Budget),
                        NextDpUBuyNormal = merge_dps(AccDpUBuyNormal, ResVParentBought, Budget),
                        NextDpUNoBuyIfParentBought = merge_dps(AccDpUNoBuyIfParentBought, ResVNoParentBought, Budget),
                        NextDpUBuyDiscount = merge_dps(AccDpUBuyDiscount, ResVParentBought, Budget),
                        {NextDpUNoBuy, NextDpUBuyNormal, NextDpUNoBuyIfParentBought, NextDpUBuyDiscount, NextMemo}
                    end,
                    {CurrentDpUNoBuy, UpdatedCurrentDpUBuyNormal, CurrentDpUNoBuyIfParentBought, UpdatedCurrentDpUBuyDiscount, Memo},
                    maps:get(U, Adj, [])
                ),

            FinalDpNoParentBought = make_dp_array(Budget),
            FinalDpNoParentBoughtResult = 
                lists:foldl(
                    fun(K, AccDp) ->
                        Val1 = array:get(K, FinalDpUNoBuy),
                        Val2 = array:get(K, FinalDpUBuyNormal),
                        array:set(K, max(Val1, Val2), AccDp)
                    end,
                    FinalDpNoParentBought,
                    lists:seq(0, Budget)
                ),

            FinalDpParentBought = make_dp_array(Budget),
            FinalDpParentBoughtResult = 
                lists:foldl(
                    fun(K, AccDp) ->
                        Val1 = array:get(K, FinalDpUNoBuyIfParentBought),
                        Val2 = array:get(K, FinalDpUBuyDiscount),
                        array:set(K, max(Val1, Val2), AccDp)
                    end,
                    FinalDpParentBought,
                    lists:seq(0, Budget)
                ),

            Result = {FinalDpNoParentBoughtResult, FinalDpParentBoughtResult},
            {Result, maps:put(U, Result, UpdatedMemo)}
    end.

max_profit(N, Present, Future, Hierarchy, Budget) ->
    Adj = lists:foldl(
        fun([U, V], Acc) ->
            maps:update_with(U, fun(List) -> [V | List] end, [V], Acc)
        end,
        #{} ,
        Hierarchy
    ),

    PresentArr = array:from_list(Present),
    FutureArr = array:from_list(Future),

    {RootRes, _FinalMemo} = dfs(1, Adj, PresentArr, FutureArr, Budget, #{}),
    {FinalDpRootNoParentBought, _} = RootRes,

    MaxOverallProfit = 
        lists:foldl(
            fun(K, AccMax) ->
                Profit = array:get(K, FinalDpRootNoParentBought),
                if Profit =/= ?NEG_INF -> max(AccMax, Profit);
                true -> AccMax
                end
            end,
            0,
            lists:seq(0, Budget)
        ),
    MaxOverallProfit.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @neg_inf -1_000_000_000 # A sufficiently small number

  # Helper function to create a DP array initialized with @neg_inf, 0 at index 0
  defp make_dp_array(budget) do
    array = :array.new([{:fixed, true}, {:size, budget + 1}, {:default, @neg_inf}])
    :array.set(0, 0, array)
  end

  # Helper function to merge two DP arrays (knapsack-style combination)
  defp merge_dps(dp1, dp2, budget) do
    new_dp = make_dp_array(budget)
    merge_dps_loop(0, dp1, dp2, new_dp, budget)
  end

  defp merge_dps_loop(k1, dp1, dp2, new_dp, budget) when k1 <= budget do
    val1 = :array.get(k1, dp1)
    case val1 do
      @neg_inf -> merge_dps_loop(k1 + 1, dp1, dp2, new_dp, budget)
      _ ->
        new_dp2 = merge_dps_inner_loop(k1, 0, val1, dp2, new_dp, budget)
        merge_dps_loop(k1 + 1, dp1, dp2, new_dp2, budget)
    end
  end
  defp merge_dps_loop(_k1, _dp1, _dp2, new_dp, _budget) do
    new_dp
  end

  defp merge_dps_inner_loop(k1, k2, val1, dp2, new_dp, budget) when k1 + k2 <= budget do
    val2 = :array.get(k2, dp2)
    case val2 do
      @neg_inf -> merge_dps_inner_loop(k1, k2 + 1, val1, dp2, new_dp, budget)
      _ ->
        current_max = :array.get(k1 + k2, new_dp)
        new_val = val1 + val2
        updated_new_dp = :array.set(k1 + k2, max(current_max, new_val), new_dp)
        merge_dps_inner_loop(k1, k2 + 1, val1, dp2, updated_new_dp, budget)
    end
  end
  defp merge_dps_inner_loop(_k1, _k2, _val1, _dp2, new_dp, _budget) do
    new_dp
  end

  # DFS function
  defp dfs(u, adj, present_arr, future_arr, budget, memo) do
    case Map.fetch(memo, u) do
      {:ok, result} -> {result, memo}
      :error ->
        current_dp_u_no_buy = make_dp_array(budget)

        cost_u_normal = :array.get(u - 1, present_arr)
        profit_u_normal = :array.get(u - 1, future_arr) - cost_u_normal
        current_dp_u_buy_normal = make_dp_array(budget)
        updated_current_dp_u_buy_normal = 
          if cost_u_normal <= budget, do: :array.set(cost_u_normal, profit_u_normal, current_dp_u_buy_normal),
          else: current_dp_u_buy_normal

        current_dp_u_no_buy_if_parent_bought = make_dp_array(budget)

        cost_u_discount = div(:array.get(u - 1, present_arr), 2)
        profit_u_discount = :array.get(u - 1, future_arr) - cost_u_discount
        current_dp_u_buy_discount = make_dp_array(budget)
        updated_current_dp_u_buy_discount = 
          if cost_u_discount <= budget, do: :array.set(cost_u_discount, profit_u_discount, current_dp_u_buy_discount),
          else: current_dp_u_buy_discount

        {final_dp_u_no_buy, final_dp_u_buy_normal, final_dp_u_no_buy_if_parent_bought, final_dp_u_buy_discount, updated_memo} = 
          Enum.reduce(
            Map.get(adj, u, []),
            {current_dp_u_no_buy, updated_current_dp_u_buy_normal, current_dp_u_no_buy_if_parent_bought, updated_current_dp_u_buy_discount, memo},
            fn v, {acc_dp_u_no_buy, acc_dp_u_buy_normal, acc_dp_u_no_buy_if_parent_bought, acc_dp_u_buy_discount, current_memo} ->
              {res_v, next_memo} = dfs(v, adj, present_arr, future_arr, budget, current_memo)
              {res_v_no_parent_bought, res_v_parent_bought} = res_v

              next_dp_u_no_buy = merge_dps(acc_dp_u_no_buy, res_v_no_parent_bought, budget)
              next_dp_u_buy_normal = merge_dps(acc_dp_u_buy_normal, res_v_parent_bought, budget)
              next_dp_u_no_buy_if_parent_bought = merge_dps(acc_dp_u_no_buy_if_parent_bought, res_v_no_parent_bought, budget)
              next_dp_u_buy_discount = merge_dps(acc_dp_u_buy_discount, res_v_parent_bought, budget)
              {next_dp_u_no_buy, next_dp_u_buy_normal, next_dp_u_no_buy_if_parent_bought, next_dp_u_buy_discount, next_memo}
            end
          )

        final_dp_no_parent_bought = make_dp_array(budget)
        final_dp_no_parent_bought_result = 
          Enum.reduce(0..budget, final_dp_no_parent_bought, fn k, acc_dp ->
            val1 = :array.get(k, final_dp_u_no_buy)
            val2 = :array.get(k, final_dp_u_buy_normal)
            :array.set(k, max(val1, val2), acc_dp)
          end)

        final_dp_parent_bought = make_dp_array(budget)
        final_dp_parent_bought_result = 
          Enum.reduce(0..budget, final_dp_parent_bought, fn k, acc_dp ->
            val1 = :array.get(k, final_dp_u_no_buy_if_parent_bought)
            val2 = :array.get(k, final_dp_u_buy_discount)
            :array.set(k, max(val1, val2), acc_dp)
          end)

        result = {final_dp_no_parent_bought_result, final_dp_parent_bought_result}
        {result, Map.put(updated_memo, u, result)}
    end
  end

  def max_profit(_n, present, future, hierarchy, budget) do
    adj = 
      Enum.reduce(hierarchy, %{}, fn [u, v], acc ->
        Map.update(acc, u, [v], fn list -> [v | list] end)
      end)

    present_arr = :array.from_list(present)
    future_arr = :array.from_list(future)

    {root_res, _final_memo} = dfs(1, adj, present_arr, future_arr, budget, %{})
    {final_dp_root_no_parent_bought, _} = root_res

    max_overall_profit = 
      Enum.reduce(0..budget, 0, fn k, acc_max ->
        profit = :array.get(k, final_dp_root_no_parent_bought)
        if profit != @neg_inf, do: max(acc_max, profit), else: acc_max
      end)
    max_overall_profit
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is O(N * Budget^2). For each of the N employees, the DFS function is called once. Inside the DFS, when combining results from children, we iterate through the budget `k1` for the current node's accumulated DP and `k2` for the child's DP. This nested loop runs up to `Budget * Budget` times for each child. Since the total sum of subtree sizes for all children of a node is at most N, and each merge operation takes O(Budget^2) time, the total time complexity for processing all nodes in the tree is O(N * Budget^2). Given N=160 and Budget=160, this is 160^3 = 4,096,000 operations, which is efficient enough.

- **Space Complexity:** The space complexity is O(N * Budget). The adjacency list for the hierarchy takes O(N) space. The memoization table stores results for N nodes. Each result consists of two DP arrays, each of size `Budget + 1`. Therefore, the total space for memoization is O(N * Budget). Given N=160 and Budget=160, this is 160 * 160 = 25,600 integer entries, which is well within typical memory limits.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-12-16 01:11:27 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved using a depth-first search (DFS) approach. We start by building the hierarchy tree from the given hierarchy list. Then, for each node in the tree, we calculate two values: max_profit and max_profit1. max_profit represents the maximum profit that can be achieved in the subtree rooted at the current node, assuming the parent of the current node has not bought the stock. max_profit1 represents the maximum profit that can be achieved in the subtree rooted at the current node, assuming the parent of the current node has bought the stock. We use these values to determine whether buying the stock for the current node will result in a higher profit or not.

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
    int maxProfit(int n, vector<int>& present, vector<int>& future, vector<vector<int>>& hierarchy, int budget) {
        vector<vector<int>> tree(n);
        for (auto& edge : hierarchy) {
            tree[edge[0] - 1].push_back(edge[1] - 1);
        }
        vector<int> max_profit(n, 0), max_profit1(n, 0);
        dfs(0, tree, present, future, max_profit, max_profit1, budget);
        return max_profit[0];
    }
    void dfs(int node, vector<vector<int>>& tree, vector<int>& present, vector<int>& future, vector<int>& max_profit, vector<int>& max_profit1, int budget) {
        max_profit[node] = 0;
        max_profit1[node] = 0;
        for (int child : tree[node]) {
            dfs(child, tree, present, future, max_profit, max_profit1, budget);
            max_profit[node] += max_profit[child];
            max_profit1[node] += max_profit1[child];
        }
        if (present[node] <= budget) {
            max_profit[node] = max(max_profit[node], future[node] - present[node]);
        }
        if (node > 0 && present[node] / 2 <= budget) {
            max_profit1[node] = max(max_profit1[node], future[node] - present[node] / 2);
        }
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int maxProfit(int n, int[] present, int[] future, int[][] hierarchy, int budget) {
        int[][] tree = new int[n][];
        for (int i = 0; i < n; i++) {
            tree[i] = new int[0];
        }
        for (int[] edge : hierarchy) {
            int[] temp = new int[tree[edge[0] - 1].length + 1];
            System.arraycopy(tree[edge[0] - 1], 0, temp, 0, tree[edge[0] - 1].length);
            temp[temp.length - 1] = edge[1] - 1;
            tree[edge[0] - 1] = temp;
        }
        int[] max_profit = new int[n], max_profit1 = new int[n];
        dfs(0, tree, present, future, max_profit, max_profit1, budget);
        return max_profit[0];
    }
    void dfs(int node, int[][] tree, int[] present, int[] future, int[] max_profit, int[] max_profit1, int budget) {
        max_profit[node] = 0;
        max_profit1[node] = 0;
        for (int child : tree[node]) {
            dfs(child, tree, present, future, max_profit, max_profit1, budget);
            max_profit[node] += max_profit[child];
            max_profit1[node] += max_profit1[child];
        }
        if (present[node] <= budget) {
            max_profit[node] = Math.max(max_profit[node], future[node] - present[node]);
        }
        if (node > 0 && present[node] / 2 <= budget) {
            max_profit1[node] = Math.max(max_profit1[node], future[node] - present[node] / 2);
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def maxProfit(self, n: int, present: list[int], future: list[int], hierarchy: list[list[int]], budget: int) -> int:
        tree = [[] for _ in range(n)]
        for u, v in hierarchy:
            tree[u - 1].append(v - 1)
        max_profit = [0] * n
        max_profit1 = [0] * n
        self.dfs(0, tree, present, future, max_profit, max_profit1, budget)
        return max_profit[0]
    def dfs(self, node: int, tree: list[list[int]], present: list[int], future: list[int], max_profit: list[int], max_profit1: list[int], budget: int) -> None:
        max_profit[node] = 0
        max_profit1[node] = 0
        for child in tree[node]:
            self.dfs(child, tree, present, future, max_profit, max_profit1, budget)
            max_profit[node] += max_profit[child]
            max_profit1[node] += max_profit1[child]
        if present[node] <= budget:
            max_profit[node] = max(max_profit[node], future[node] - present[node])
        if node > 0 and present[node] // 2 <= budget:
            max_profit1[node] = max(max_profit1[node], future[node] - present[node] // 2)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def maxProfit(self, n: int, present: list[int], future: list[int], hierarchy: list[list[int]], budget: int) -> int:
        tree = [[] for _ in range(n)]
        for u, v in hierarchy:
            tree[u - 1].append(v - 1)
        max_profit = [0] * n
        max_profit1 = [0] * n
        self.dfs(0, tree, present, future, max_profit, max_profit1, budget)
        return max_profit[0]
    def dfs(self, node: int, tree: list[list[int]], present: list[int], future: list[int], max_profit: list[int], max_profit1: list[int], budget: int) -> None:
        max_profit[node] = 0
        max_profit1[node] = 0
        for child in tree[node]:
            self.dfs(child, tree, present, future, max_profit, max_profit1, budget)
            max_profit[node] += max_profit[child]
            max_profit1[node] += max_profit1[child]
        if present[node] <= budget:
            max_profit[node] = max(max_profit[node], future[node] - present[node])
        if node > 0 and present[node] // 2 <= budget:
            max_profit1[node] = max(max_profit1[node], future[node] - present[node] // 2)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
typedef struct {
    int* data;
    int size;
} Array;

Array* createArray(int size) {
    Array* arr = malloc(sizeof(Array));
    arr->data = malloc(size * sizeof(int));
    arr->size = size;
    return arr;
}

void freeArray(Array* arr) {
    free(arr->data);
    free(arr);
}

typedef struct {
    Array** data;
    int size;
} Array2D;

Array2D* createArray2D(int size) {
    Array2D* arr = malloc(sizeof(Array2D));
    arr->data = malloc(size * sizeof(Array*));
    arr->size = size;
    return arr;
}

void freeArray2D(Array2D* arr) {
    for (int i = 0; i < arr->size; i++) {
        freeArray(arr->data[i]);
    }
    free(arr->data);
    free(arr);
}

int maxProfit(int n, int* present, int* future, int** hierarchy, int hierarchySize, int budget) {
    Array2D* tree = createArray2D(n);
    for (int i = 0; i < n; i++) {
        tree->data[i] = createArray(0);
    }
    for (int i = 0; i < hierarchySize; i++) {
        int u = hierarchy[i][0] - 1;
        int v = hierarchy[i][1] - 1;
        tree->data[u]->size++;
        tree->data[u]->data = realloc(tree->data[u]->data, tree->data[u]->size * sizeof(int));
        tree->data[u]->data[tree->data[u]->size - 1] = v;
    }
    int* max_profit = malloc(n * sizeof(int));
    int* max_profit1 = malloc(n * sizeof(int));
    dfs(0, tree, present, future, max_profit, max_profit1, budget);
    int result = max_profit[0];
    free(max_profit);
    free(max_profit1);
    freeArray2D(tree);
    return result;
}

void dfs(int node, Array2D* tree, int* present, int* future, int* max_profit, int* max_profit1, int budget) {
    max_profit[node] = 0;
    max_profit1[node] = 0;
    for (int i = 0; i < tree->data[node]->size; i++) {
        int child = tree->data[node]->data[i];
        dfs(child, tree, present, future, max_profit, max_profit1, budget);
        max_profit[node] += max_profit[child];
        max_profit1[node] += max_profit1[child];
    }
    if (present[node] <= budget) {
        max_profit[node] = (max_profit[node] > future[node] - present[node]) ? max_profit[node] : future[node] - present[node];
    }
    if (node > 0 && present[node] / 2 <= budget) {
        max_profit1[node] = (max_profit1[node] > future[node] - present[node] / 2) ? max_profit1[node] : future[node] - present[node] / 2;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int MaxProfit(int n, int[] present, int[] future, int[][] hierarchy, int budget) {
        List<int>[] tree = new List<int>[n];
        for (int i = 0; i < n; i++) {
            tree[i] = new List<int>();
        }
        foreach (int[] edge in hierarchy) {
            tree[edge[0] - 1].Add(edge[1] - 1);
        }
        int[] max_profit = new int[n];
        int[] max_profit1 = new int[n];
        Dfs(0, tree, present, future, max_profit, max_profit1, budget);
        return max_profit[0];
    }
    void Dfs(int node, List<int>[] tree, int[] present, int[] future, int[] max_profit, int[] max_profit1, int budget) {
        max_profit[node] = 0;
        max_profit1[node] = 0;
        foreach (int child in tree[node]) {
            Dfs(child, tree, present, future, max_profit, max_profit1, budget);
            max_profit[node] += max_profit[child];
            max_profit1[node] += max_profit1[child];
        }
        if (present[node] <= budget) {
            max_profit[node] = Math.Max(max_profit[node], future[node] - present[node]);
        }
        if (node > 0 && present[node] / 2 <= budget) {
            max_profit1[node] = Math.Max(max_profit1[node], future[node] - present[node] / 2);
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var maxProfit = function(n, present, future, hierarchy, budget) {
    let tree = Array(n).fill(0).map(() => []);
    for (let [u, v] of hierarchy) {
        tree[u - 1].push(v - 1);
    }
    let max_profit = Array(n).fill(0);
    let max_profit1 = Array(n).fill(0);
    dfs(0, tree, present, future, max_profit, max_profit1, budget);
    return max_profit[0];
};

function dfs(node, tree, present, future, max_profit, max_profit1, budget) {
    max_profit[node] = 0;
    max_profit1[node] = 0;
    for (let child of tree[node]) {
        dfs(child, tree, present, future, max_profit, max_profit1, budget);
        max_profit[node] += max_profit[child];
        max_profit1[node] += max_profit1[child];
    }
    if (present[node] <= budget) {
        max_profit[node] = Math.max(max_profit[node], future[node] - present[node]);
    }
    if (node > 0 && present[node] / 2 <= budget) {
        max_profit1[node] = Math.max(max_profit1[node], future[node] - present[node] / 2);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function maxProfit(n: number, present: number[], future: number[], hierarchy: number[][], budget: number): number {
    let tree: number[][] = Array(n).fill(0).map(() => []);
    for (let [u, v] of hierarchy) {
        tree[u - 1].push(v - 1);
    }
    let max_profit: number[] = Array(n).fill(0);
    let max_profit1: number[] = Array(n).fill(0);
    dfs(0, tree, present, future, max_profit, max_profit1, budget);
    return max_profit[0];
}

function dfs(node: number, tree: number[][], present: number[], future: number[], max_profit: number[], max_profit1: number[], budget: number): void {
    max_profit[node] = 0;
    max_profit1[node] = 0;
    for (let child of tree[node]) {
        dfs(child, tree, present, future, max_profit, max_profit1, budget);
        max_profit[node] += max_profit[child];
        max_profit1[node] += max_profit1[child];
    }
    if (present[node] <= budget) {
        max_profit[node] = Math.max(max_profit[node], future[node] - present[node]);
    }
    if (node > 0 && present[node] / 2 <= budget) {
        max_profit1[node] = Math.max(max_profit1[node], future[node] - present[node] / 2);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
function maxProfit($n, $present, $future, $hierarchy, $budget) {
    $tree = array_fill(0, $n, []);
    foreach ($hierarchy as $edge) {
        $tree[$edge[0] - 1][] = $edge[1] - 1;
    }
    $max_profit = array_fill(0, $n, 0);
    $max_profit1 = array_fill(0, $n, 0);
    dfs(0, $tree, $present, $future, $max_profit, $max_profit1, $budget);
    return $max_profit[0];
}

function dfs($node, &$tree, $present, $future, &$max_profit, &$max_profit1, $budget) {
    $max_profit[$node] = 0;
    $max_profit1[$node] = 0;
    foreach ($tree[$node] as $child) {
        dfs($child, $tree, $present, $future, $max_profit, $max_profit1, $budget);
        $max_profit[$node] += $max_profit[$child];
        $max_profit1[$node] += $max_profit1[$child];
    }
    if ($present[$node] <= $budget) {
        $max_profit[$node] = max($max_profit[$node], $future[$node] - $present[$node]);
    }
    if ($node > 0 && $present[$node] / 2 <= $budget) {
        $max_profit1[$node] = max($max_profit1[$node], $future[$node] - $present[$node] / 2);
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
func maxProfit(_ n: Int, _ present: [Int], _ future: [Int], _ hierarchy: [[Int]], _ budget: Int) -> Int {
    var tree: [[Int]] = Array(repeating: [], count: n)
    for edge in hierarchy {
        tree[edge[0] - 1].append(edge[1] - 1)
    }
    var max_profit: [Int] = Array(repeating: 0, count: n)
    var max_profit1: [Int] = Array(repeating: 0, count: n)
    dfs(0, &tree, present, future, &max_profit, &max_profit1, budget)
    return max_profit[0]
}

func dfs(_ node: Int, _ tree: inout [[Int]], _ present: [Int], _ future: [Int], _ max_profit: inout [Int], _ max_profit1: inout [Int], _ budget: Int) {
    max_profit[node] = 0
    max_profit1[node] = 0
    for child in tree[node] {
        dfs(child, &tree, present, future, &max_profit, &max_profit1, budget)
        max_profit[node] += max_profit[child]
        max_profit1[node] += max_profit1[child]
    }
    if present[node] <= budget {
        max_profit[node] = max(max_profit[node], future[node] - present[node])
    }
    if node > 0 && present[node] / 2 <= budget {
        max_profit1[node] = max(max_profit1[node], future[node] - present[node] / 2)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
fun maxProfit(n: Int, present: IntArray, future: IntArray, hierarchy: Array<IntArray>, budget: Int): Int {
    val tree: Array<MutableList<Int>> = Array(n) { mutableListOf() }
    for ((u, v) in hierarchy) {
        tree[u - 1].add(v - 1)
    }
    val max_profit = IntArray(n)
    val max_profit1 = IntArray(n)
    dfs(0, tree, present, future, max_profit, max_profit1, budget)
    return max_profit[0]
}

fun dfs(node: Int, tree: Array<MutableList<Int>>, present: IntArray, future: IntArray, max_profit: IntArray, max_profit1: IntArray, budget: Int) {
    max_profit[node] = 0
    max_profit1[node] = 0
    for (child in tree[node]) {
        dfs(child, tree, present, future, max_profit, max_profit1, budget)
        max_profit[node] += max_profit[child]
        max_profit1[node] += max_profit1[child]
    }
    if (present[node] <= budget) {
        max_profit[node] = maxOf(max_profit[node], future[node] - present[node])
    }
    if (node > 0 && present[node] / 2 <= budget) {
        max_profit1[node] = maxOf(max_profit1[node], future[node] - present[node] / 2)
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
int maxProfit(int n, List<int> present, List<int> future, List<List<int>> hierarchy, int budget) {
    List<List<int>> tree = List.generate(n, (index) => []);
    for (var edge in hierarchy) {
        tree[edge[0] - 1].add(edge[1] - 1);
    }
    List<int> max_profit = List.generate(n, (index) => 0);
    List<int> max_profit1 = List.generate(n, (index) => 0);
    dfs(0, tree, present, future, max_profit, max_profit1, budget);
    return max_profit[0];
}

void dfs(int node, List<List<int>> tree, List<int> present, List<int> future, List<int> max_profit, List<int> max_profit1, int budget) {
    max_profit[node] = 0;
    max_profit1[node] = 0;
    for (var child in tree[node]) {
        dfs(child, tree, present, future, max_profit, max_profit1, budget);
        max_profit[node] += max_profit[child];
        max_profit1[node] += max_profit1[child];
    }
    if (present[node] <= budget) {
        max_profit[node] = max(max_profit[node], future[node] - present[node]);
    }
    if (node > 0 && present[node] / 2 <= budget) {
        max_profit1[node] = max(max_profit1[node], future[node] - present[node] / 2);
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
    "fmt"
)

type Solution struct{}

func (s *Solution) maxProfit(n int, present []int, future []int, hierarchy [][]int, budget int) int {
    tree := make([][]int, n)
    for _, edge := range hierarchy {
        tree[edge[0]-1] = append(tree[edge[0]-1], edge[1]-1)
    }
    max_profit := make([]int, n)
    max_profit1 := make([]int, n)
    s.dfs(0, tree, present, future, max_profit, max_profit1, budget)
    return max_profit[0]
}

func (s *Solution) dfs(node int, tree [][]int, present []int, future []int, max_profit []int, max_profit1 []int, budget int) {
    max_profit[node] = 0
    max_profit1[node] = 0
    for _, child := range tree[node] {
        s.dfs(child, tree, present, future, max_profit, max_profit1, budget)
        max_profit[node] += max_profit[child]
        max_profit1[node] += max_profit1[child]
    }
    if present[node] <= budget {
        max_profit[node] = max(max_profit[node], future[node]-present[node])
    }
    if node > 0 && present[node]/2 <= budget {
        max_profit1[node] = max(max_profit1[node], future[node]-present[node]/2)
    }
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def max_profit(n, present, future, hierarchy, budget)
    tree = Array.new(n) { [] }
    hierarchy.each do |edge|
        tree[edge[0] - 1] << edge[1] - 1
    end
    max_profit = Array.new(n, 0)
    max_profit1 = Array.new(n, 0)
    dfs(0, tree, present, future, max_profit, max_profit1, budget)
    max_profit[0]
end

def dfs(node, tree, present, future, max_profit, max_profit1, budget)
    max_profit[node] = 0
    max_profit1[node] = 0
    tree[node].each do |child|
        dfs(child, tree, present, future, max_profit, max_profit1, budget)
        max_profit[node] += max_profit[child]
        max_profit1[node] += max_profit1[child]
    end
    if present[node] <= budget
        max_profit[node] = [max_profit[node], future[node] - present[node]].max
    end
    if node > 0 && present[node] / 2 <= budget
        max_profit1[node] = [max_profit1[node], future[node] - present[node] / 2].max
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def maxProfit(n: Int, present: Array[Int], future: Array[Int], hierarchy: Array[Array[Int]], budget: Int): Int = {
        val tree: Array[Array[Int]] = Array.fill(n)(Array[Int]())
        for (edge <- hierarchy) {
            tree(edge(0) - 1) = tree(edge(0) - 1) :+ (edge(1) - 1)
        }
        val max_profit = Array.fill(n)(0)
        val max_profit1 = Array.fill(n)(0)
        dfs(0, tree, present, future, max_profit, max_profit1, budget)
        max_profit(0)
    }

    def dfs(node: Int, tree: Array[Array[Int]], present: Array[Int], future: Array[Int], max_profit: Array[Int], max_profit1: Array[Int], budget: Int): Unit = {
        max_profit(node) = 0
        max_profit1(node) = 0
        for (child <- tree(node)) {
            dfs(child, tree, present, future, max_profit, max_profit1, budget)
            max_profit(node) += max_profit(child)
            max_profit1(node) += max_profit1(child)
        }
        if (present(node) <= budget) {
            max_profit(node) = math.max(max_profit(node), future(node) - present(node))
        }
        if (node > 0 && present(node) / 2 <= budget) {
            max_profit1(node) = math.max(max_profit1(node), future(node) - present(node) / 2)
        }
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
    pub fn max_profit(n: i32, present: Vec<i32>, future: Vec<i32>, hierarchy: Vec<Vec<i32>>, budget: i32) -> i32 {
        let mut tree: Vec<Vec<i32>> = vec![vec![]; n as usize];
        for edge in hierarchy {
            tree[(edge[0] - 1) as usize].push(edge[1] - 1);
        }
        let mut max_profit: Vec<i32> = vec![0; n as usize];
        let mut max_profit1: Vec<i32> = vec![0; n as usize];
        Self::dfs(0, &mut tree, &present, &future, &mut max_profit, &mut max_profit1, budget);
        max_profit[0]
    }

    fn dfs(node: i32, tree: &mut Vec<Vec<i32>>, present: &Vec<i32>, future: &Vec<i32>, max_profit: &mut Vec<i32>, max_profit1: &mut Vec<i32>, budget: i32) {
        max_profit[node as usize] = 0;
        max_profit1[node as usize] = 0;
        for child in &tree[node as usize] {
            Self::dfs(*child, tree, present, future, max_profit, max_profit1, budget);
            max_profit[node as usize] += max_profit[*child as usize];
            max_profit1[node as usize] += max_profit1[*child as usize];
        }
        if present[node as usize] <= budget {
            max_profit[node as usize] = std::cmp::max(max_profit[node as usize], future[node as usize] - present[node as usize]);
        }
        if node > 0 && present[node as usize] / 2 <= budget {
            max_profit1[node as usize] = std::cmp::max(max_profit1[node as usize], future[node as usize] - present[node as usize] / 2);
        }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
define (max-profit n present future hierarchy budget)
    (let (
        (tree (make-vector n '()))
        (max_profit (make-vector n 0))
        (max_profit1 (make-vector n 0))
        )
        (for-each (lambda (edge)
            (vector-set! tree (- (car edge) 1) (cons (- (cadr edge) 1) (vector-ref tree (- (car edge) 1))))
            )
            hierarchy
            )
        (dfs 0 tree present future max_profit max_profit1 budget)
        (vector-ref max_profit 0)
        )

(define (dfs node tree present future max_profit max_profit1 budget)
    (vector-set! max_profit node 0)
    (vector-set! max_profit1 node 0)
    (for-each (lambda (child)
        (dfs child tree present future max_profit max_profit1 budget)
        (vector-set! max_profit node (+ (vector-ref max_profit node) (vector-ref max_profit child)))
        (vector-set! max_profit1 node (+ (vector-ref max_profit1 node) (vector-ref max_profit1 child)))
        )
        (vector-ref tree node)
        )
    (if (<= (vector-ref present node) budget)
        (vector-set! max_profit node (max (vector-ref max_profit node) (- (vector-ref future node) (vector-ref present node))))
        )
    (if (and (> node 0) (<= (/ (vector-ref present node) 2) budget))
        (vector-set! max_profit1 node (max (vector-ref max_profit1 node) (- (vector-ref future node) (/ (vector-ref present node) 2))))
        )
    )
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
max_profit(N, Present, Future, Hierarchy, Budget) ->
    Tree = array:new(N, {default, []}),
    lists:foreach(fun({U, V}) ->
        array:set(U - 1, [V - 1 | array:get(U - 1, Tree)], Tree)
    end, Hierarchy),
    MaxProfit = array:new(N, {default, 0}),
    MaxProfit1 = array:new(N, {default, 0}),
    dfs(0, Tree, Present, Future, MaxProfit, MaxProfit1, Budget),
    array:get(0, MaxProfit).

dfs(Node, Tree, Present, Future, MaxProfit, MaxProfit1, Budget) ->
    array:set(Node, 0, MaxProfit),
    array:set(Node, 0, MaxProfit1),
    lists:foreach(fun(Child) ->
        dfs(Child, Tree, Present, Future, MaxProfit, MaxProfit1, Budget),
        array:set(Node, array:get(Node, MaxProfit) + array:get(Child, MaxProfit), MaxProfit),
        array:set(Node, array:get(Node, MaxProfit1) + array:get(Child, MaxProfit1), MaxProfit1)
    end, array:get(Node, Tree)),
    if array:get(Node, Present) =< Budget ->
        array:set(Node, max(array:get(Node, MaxProfit), array:get(Node, Future) - array:get(Node, Present)), MaxProfit);
    true -> ok
    end,
    if Node > 0 andalso array:get(Node, Present) / 2 =< Budget ->
        array:set(Node, max(array:get(Node, MaxProfit1), array:get(Node, Future) - array:get(Node, Present) / 2), MaxProfit1);
    true -> ok
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
def max_profit(n, present, future, hierarchy, budget) do
    tree = Enum.reduce(hierarchy, Array.new(n, []), fn [u, v], tree ->
        Array.update!(tree, u - 1, &[v - 1 | Enum.at(tree, u - 1)])
    end)
    max_profit = Array.new(n, 0)
    max_profit1 = Array.new(n, 0)
    dfs(0, tree, present, future, max_profit, max_profit1, budget)
    Enum.at(max_profit, 0)
end

def dfs(node, tree, present, future, max_profit, max_profit1, budget) do
    max_profit = Array.update!(max_profit, node, 0)
    max_profit1 = Array.update!(max_profit1, node, 0)
    Enum.each(Enum.at(tree, node), fn child ->
        dfs(child, tree, present, future, max_profit, max_profit1, budget)
        max_profit = Array.update!(max_profit, node, Enum.at(max_profit, node) + Enum.at(max_profit, child))
        max_profit1 = Array.update!(max_profit1, node, Enum.at(max_profit1, node) + Enum.at(max_profit1, child))
    end)
    if Enum.at(present, node) <= budget do
        max_profit = Array.update!(max_profit, node, max(Enum.at(max_profit, node), Enum.at(future, node) - Enum.at(present, node)))
    end
    if node > 0 and Enum.at(present, node) / 2 <= budget do
        max_profit1 = Array.update!(max_profit1, node, max(Enum.at(max_profit1, node), Enum.at(future, node) - Enum.at(present, node) / 2))
    end
    {max_profit, max_profit1}
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of this solution is O(n), where n is the number of employees. This is because we visit each node in the hierarchy tree once during the DFS traversal.

- **Space Complexity:** The space complexity of this solution is O(n), where n is the number of employees. This is because we need to store the hierarchy tree and the max_profit and max_profit1 values for each node in the tree.

</div>
</details>
