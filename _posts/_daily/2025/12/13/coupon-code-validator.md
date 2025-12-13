---
layout: post
title: "Coupon Code Validator"
date: 2025-12-13 09:00:00 +0900
categories: [LeetCode, Easy]
tags: ["Array", "Hash Table", "String", "Sorting"]
difficulty: Easy
leetcode_url: https://leetcode.com/problems/coupon-code-validator/
ai_solutions:
  - solutions:
      cpp: "#include <vector>\n#include <string>\n#include <map>\n#include <algorithm>\n\
        #include <cctype>\n\nclass Solution {\npublic:\n    // Helper function to check\
        \ if a code is valid\n    bool isValidCode(const std::string& s) {\n       \
        \ if (s.empty()) {\n            return false;\n        }\n        for (char\
        \ c : s) {\n            if (!std::isalnum(static_cast<unsigned char>(c)) &&\
        \ c != '_') {\n                return false;\n            }\n        }\n   \
        \     return true;\n    }\n\n    std::vector<std::string> validateCoupons(std::vector<std::string>&\
        \ code, std::vector<std::string>& businessLine, std::vector<bool>& isActive)\
        \ {\n        std::map<std::string, int> businessLinePriorities = {\n       \
        \     {\"electronics\", 0},\n            {\"grocery\", 1},\n            {\"\
        pharmacy\", 2},\n            {\"restaurant\", 3}\n        };\n\n        std::vector<std::pair<std::string,\
        \ std::string>> validCoupons;\n        int n = code.size();\n\n        for (int\
        \ i = 0; i < n; ++i) {\n            // Condition 3: isActive[i] is true\n  \
        \          if (!isActive[i]) {\n                continue;\n            }\n\n\
        \            // Condition 2: businessLine[i] is one of the four categories\n\
        \            if (businessLinePriorities.find(businessLine[i]) == businessLinePriorities.end())\
        \ {\n                continue;\n            }\n\n            // Condition 1:\
        \ code[i] is non-empty and consists only of alphanumeric characters and underscores\n\
        \            if (!isValidCode(code[i])) {\n                continue;\n     \
        \       }\n\n            // If all conditions pass, add to validCoupons list\n\
        \            validCoupons.push_back({businessLine[i], code[i]});\n        }\n\
        \n        // Sort validCoupons\n        std::sort(validCoupons.begin(), validCoupons.end(),\
        \ \n            [&](const std::pair<std::string, std::string>& a, const std::pair<std::string,\
        \ std::string>& b) {\n                int priorityA = businessLinePriorities[a.first];\n\
        \                int priorityB = businessLinePriorities[b.first];\n        \
        \        if (priorityA != priorityB) {\n                    return priorityA\
        \ < priorityB;\n                }\n                return a.second < b.second;\
        \ // Lexicographical sort by code\n            }\n        );\n\n        // Extract\
        \ and return codes\n        std::vector<std::string> result;\n        for (const\
        \ auto& coupon : validCoupons) {\n            result.push_back(coupon.second);\n\
        \        }\n\n        return result;\n    }\n};"
      java: "import java.util.ArrayList;\nimport java.util.Collections;\nimport java.util.Comparator;\n\
        import java.util.HashMap;\nimport java.util.List;\nimport java.util.Map;\nimport\
        \ java.util.regex.Pattern;\n\nclass Solution {\n    // Pattern for alphanumeric\
        \ and underscore characters\n    private static final Pattern CODE_PATTERN =\
        \ Pattern.compile(\"^[a-zA-Z0-9_]+$\");\n\n    // Helper class to store coupon\
        \ data for sorting\n    private static class CouponData {\n        String businessLine;\n\
        \        String code;\n        int businessLinePriority;\n\n        CouponData(String\
        \ businessLine, String code, int businessLinePriority) {\n            this.businessLine\
        \ = businessLine;\n            this.code = code;\n            this.businessLinePriority\
        \ = businessLinePriority;\n        }\n    }\n\n    public List<String> validateCoupons(List<String>\
        \ code, List<String> businessLine, List<Boolean> isActive) {\n        Map<String,\
        \ Integer> businessLinePriorities = new HashMap<>();\n        businessLinePriorities.put(\"\
        electronics\", 0);\n        businessLinePriorities.put(\"grocery\", 1);\n  \
        \      businessLinePriorities.put(\"pharmacy\", 2);\n        businessLinePriorities.put(\"\
        restaurant\", 3);\n\n        List<CouponData> validCoupons = new ArrayList<>();\n\
        \        int n = code.size();\n\n        for (int i = 0; i < n; i++) {\n   \
        \         // Condition 3: isActive[i] is true\n            if (!isActive.get(i))\
        \ {\n                continue;\n            }\n\n            // Condition 2:\
        \ businessLine[i] is one of the four categories\n            String currentBusinessLine\
        \ = businessLine.get(i);\n            if (!businessLinePriorities.containsKey(currentBusinessLine))\
        \ {\n                continue;\n            }\n            int blPriority =\
        \ businessLinePriorities.get(currentBusinessLine);\n\n            // Condition\
        \ 1: code[i] is non-empty and consists only of alphanumeric characters and underscores\n\
        \            String currentCode = code.get(i);\n            if (currentCode.isEmpty()\
        \ || !CODE_PATTERN.matcher(currentCode).matches()) {\n                continue;\n\
        \            }\n\n            // If all conditions pass, add to validCoupons\
        \ list\n            validCoupons.add(new CouponData(currentBusinessLine, currentCode,\
        \ blPriority));\n        }\n\n        // Sort validCoupons\n        Collections.sort(validCoupons,\
        \ new Comparator<CouponData>() {\n            @Override\n            public\
        \ int compare(CouponData a, CouponData b) {\n                if (a.businessLinePriority\
        \ != b.businessLinePriority) {\n                    return Integer.compare(a.businessLinePriority,\
        \ b.businessLinePriority);\n                }\n                return a.code.compareTo(b.code);\
        \ // Lexicographical sort by code\n            }\n        });\n\n        //\
        \ Extract and return codes\n        List<String> result = new ArrayList<>();\n\
        \        for (CouponData coupon : validCoupons) {\n            result.add(coupon.code);\n\
        \        }\n\n        return result;\n    }\n}"
      python: "import re\nfrom typing import List\n\nclass Solution:\n    def validateCoupons(self,\
        \ code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:\n\
        \        valid_business_lines = {\"electronics\": 0, \"grocery\": 1, \"pharmacy\"\
        : 2, \"restaurant\": 3}\n\n        valid_coupons = []\n        n = len(code)\n\
        \n        for i in range(n):\n            # Condition 3: isActive[i] is true\n\
        \            if not isActive[i]:\n                continue\n\n            #\
        \ Condition 2: businessLine[i] is one of the four categories\n            current_business_line\
        \ = businessLine[i]\n            if current_business_line not in valid_business_lines:\n\
        \                continue\n\n            current_code = code[i]\n\n        \
        \    # Condition 1: code[i] is non-empty\n            if not current_code:\n\
        \                continue\n\n            # Condition 1: code[i] consists only\
        \ of alphanumeric characters and underscores\n            if not re.fullmatch(r'^[a-zA-Z0-9_]+$',\
        \ current_code):\n                continue\n\n            # If all conditions\
        \ pass, add to valid_coupons list\n            valid_coupons.append((current_business_line,\
        \ current_code))\n\n        # Sort valid_coupons\n        # Sort first by businessLine\
        \ priority, then by code lexicographically\n        valid_coupons.sort(key=lambda\
        \ x: (valid_business_lines[x[0]], x[1]))\n\n        # Extract and return codes\n\
        \        return [coupon_code for _, coupon_code in valid_coupons]"
      python3: "import re\nfrom typing import List\n\nclass Solution:\n    def validateCoupons(self,\
        \ code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:\n\
        \        valid_business_lines = {\"electronics\": 0, \"grocery\": 1, \"pharmacy\"\
        : 2, \"restaurant\": 3}\n\n        valid_coupons = []\n        n = len(code)\n\
        \n        for i in range(n):\n            # Condition 3: isActive[i] is true\n\
        \            if not isActive[i]:\n                continue\n\n            #\
        \ Condition 2: businessLine[i] is one of the four categories\n            current_business_line\
        \ = businessLine[i]\n            if current_business_line not in valid_business_lines:\n\
        \                continue\n\n            current_code = code[i]\n\n        \
        \    # Condition 1: code[i] is non-empty\n            if not current_code:\n\
        \                continue\n\n            # Condition 1: code[i] consists only\
        \ of alphanumeric characters and underscores\n            if not re.fullmatch(r'^[a-zA-Z0-9_]+$',\
        \ current_code):\n                continue\n\n            # If all conditions\
        \ pass, add to valid_coupons list\n            valid_coupons.append((current_business_line,\
        \ current_code))\n\n        # Sort valid_coupons\n        # Sort first by businessLine\
        \ priority, then by code lexicographically\n        valid_coupons.sort(key=lambda\
        \ x: (valid_business_lines[x[0]], x[1]))\n\n        # Extract and return codes\n\
        \        return [coupon_code for _, coupon_code in valid_coupons]"
      c: "#include <stdlib.h>\n#include <string.h>\n#include <stdbool.h>\n#include <ctype.h>\
        \ // For isalnum\n\n// Helper struct to store valid coupon data\ntypedef struct\
        \ {\n    char* businessLine; // Not strictly needed for return, but useful for\
        \ sorting logic\n    char* code;\n    int businessLinePriority;\n} ValidCoupon;\n\
        \n// Helper function to check if a code is valid\nbool isValidCode(const char*\
        \ s) {\n    if (s == NULL || s[0] == '\\0') {\n        return false;\n    }\n\
        \    for (int i = 0; s[i] != '\\0'; i++) {\n        if (!isalnum((unsigned char)s[i])\
        \ && s[i] != '_') {\n            return false;\n        }\n    }\n    return\
        \ true;\n}\n\n// Helper function to get business line priority\nint getBusinessLinePriority(const\
        \ char* bl) {\n    if (strcmp(bl, \"electronics\") == 0) return 0;\n    if (strcmp(bl,\
        \ \"grocery\") == 0) return 1;\n    if (strcmp(bl, \"pharmacy\") == 0) return\
        \ 2;\n    if (strcmp(bl, \"restaurant\") == 0) return 3;\n    return -1; //\
        \ Invalid business line\n}\n\n// Comparison function for qsort\nint compareCoupons(const\
        \ void* a, const void* b) {\n    ValidCoupon* couponA = *(ValidCoupon**)a;\n\
        \    ValidCoupon* couponB = *(ValidCoupon**)b;\n\n    // Sort by businessLine\
        \ priority first\n    if (couponA->businessLinePriority != couponB->businessLinePriority)\
        \ {\n        return couponA->businessLinePriority - couponB->businessLinePriority;\n\
        \    }\n\n    // Then sort by code lexicographically\n    return strcmp(couponA->code,\
        \ couponB->code);\n}\n\nchar** validateCoupons(char** code, int codeSize, char**\
        \ businessLine, int businessLineSize, bool* isActive, int isActiveSize, int*\
        \ returnSize) {\n    // Allocate a temporary array to store pointers to ValidCoupon\
        \ structs\n    ValidCoupon** temp_valid_coupons = (ValidCoupon**)malloc(codeSize\
        \ * sizeof(ValidCoupon*));\n    if (temp_valid_coupons == NULL) {\n        *returnSize\
        \ = 0;\n        return NULL;\n    }\n    int valid_count = 0;\n\n    for (int\
        \ i = 0; i < codeSize; i++) {\n        // Condition 3: isActive[i] is true\n\
        \        if (!isActive[i]) {\n            continue;\n        }\n\n        //\
        \ Condition 2: businessLine[i] is one of the four categories\n        int bl_priority\
        \ = getBusinessLinePriority(businessLine[i]);\n        if (bl_priority == -1)\
        \ {\n            continue;\n        }\n\n        // Condition 1: code[i] is\
        \ non-empty and consists only of alphanumeric characters and underscores\n \
        \       if (!isValidCode(code[i])) {\n            continue;\n        }\n\n \
        \       // If all conditions pass, create a new ValidCoupon struct and add to\
        \ list\n        ValidCoupon* vc = (ValidCoupon*)malloc(sizeof(ValidCoupon));\n\
        \        if (vc == NULL) {\n            // Handle memory allocation failure:\
        \ free previously allocated coupons\n            for (int j = 0; j < valid_count;\
        \ j++) {\n                free(temp_valid_coupons[j]->businessLine);\n     \
        \           free(temp_valid_coupons[j]->code);\n                free(temp_valid_coupons[j]);\n\
        \            }\n            free(temp_valid_coupons);\n            *returnSize\
        \ = 0;\n            return NULL;\n        }\n\n        // Duplicate strings\
        \ to ensure they persist beyond the input arrays' scope\n        vc->businessLine\
        \ = strdup(businessLine[i]);\n        vc->code = strdup(code[i]);\n        vc->businessLinePriority\
        \ = bl_priority;\n\n        temp_valid_coupons[valid_count++] = vc;\n    }\n\
        \n    // Sort the valid coupons using qsort\n    qsort(temp_valid_coupons, valid_count,\
        \ sizeof(ValidCoupon*), compareCoupons);\n\n    // Prepare the result array\
        \ of char*\n    char** result = (char**)malloc(valid_count * sizeof(char*));\n\
        \    if (result == NULL) {\n        // Handle memory allocation failure: free\
        \ all coupons\n        for (int j = 0; j < valid_count; j++) {\n           \
        \ free(temp_valid_coupons[j]->businessLine);\n            free(temp_valid_coupons[j]->code);\n\
        \            free(temp_valid_coupons[j]);\n        }\n        free(temp_valid_coupons);\n\
        \        *returnSize = 0;\n        return NULL;\n    }\n\n    for (int i = 0;\
        \ i < valid_count; i++) {\n        result[i] = temp_valid_coupons[i]->code;\
        \ // Transfer ownership of the code string to the result array\n        // Free\
        \ the businessLine string and the ValidCoupon struct itself\n        free(temp_valid_coupons[i]->businessLine);\n\
        \        free(temp_valid_coupons[i]);\n    }\n    free(temp_valid_coupons);\
        \ // Free the array of pointers to ValidCoupon structs\n\n    *returnSize =\
        \ valid_count;\n    return result;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\nusing System.Linq;\n\
        using System.Text.RegularExpressions;\n\npublic class Solution {\n    private\
        \ static readonly Regex CodeRegex = new Regex(\"^[a-zA-Z0-9_]+$\", RegexOptions.Compiled);\n\
        \n    public IList<string> ValidateCoupons(IList<string> code, IList<string>\
        \ businessLine, IList<bool> isActive) {\n        Dictionary<string, int> businessLinePriorities\
        \ = new Dictionary<string, int> {\n            {\"electronics\", 0},\n     \
        \       {\"grocery\", 1},\n            {\"pharmacy\", 2},\n            {\"restaurant\"\
        , 3}\n        };\n\n        List<(string BusinessLine, string Code, int Priority)>\
        \ validCoupons = new List<(string, string, int)>();\n        int n = code.Count;\n\
        \n        for (int i = 0; i < n; i++) {\n            // Condition 3: isActive[i]\
        \ is true\n            if (!isActive[i]) {\n                continue;\n    \
        \        }\n\n            // Condition 2: businessLine[i] is one of the four\
        \ categories\n            string currentBusinessLine = businessLine[i];\n  \
        \          if (!businessLinePriorities.TryGetValue(currentBusinessLine, out\
        \ int priority)) {\n                continue;\n            }\n\n           \
        \ // Condition 1: code[i] is non-empty and consists only of alphanumeric characters\
        \ and underscores\n            string currentCode = code[i];\n            if\
        \ (string.IsNullOrEmpty(currentCode) || !CodeRegex.IsMatch(currentCode)) {\n\
        \                continue;\n            }\n\n            // If all conditions\
        \ pass, add to validCoupons list\n            validCoupons.Add((currentBusinessLine,\
        \ currentCode, priority));\n        }\n\n        // Sort validCoupons\n    \
        \    validCoupons.Sort((a, b) => {\n            int priorityComparison = a.Priority.CompareTo(b.Priority);\n\
        \            if (priorityComparison != 0) {\n                return priorityComparison;\n\
        \            }\n            return string.Compare(a.Code, b.Code, StringComparison.Ordinal);\
        \ // Lexicographical sort by code\n        });\n\n        // Extract and return\
        \ codes\n        return validCoupons.Select(c => c.Code).ToList();\n    }\n}"
      javascript: "/**\n * @param {string[]} code\n * @param {string[]} businessLine\n\
        \ * @param {boolean[]} isActive\n * @return {string[]}\n */\nvar validateCoupons\
        \ = function(code, businessLine, isActive) {\n    const businessLinePriorities\
        \ = {\n        \"electronics\": 0,\n        \"grocery\": 1,\n        \"pharmacy\"\
        : 2,\n        \"restaurant\": 3\n    };\n\n    const codeRegex = /^[a-zA-Z0-9_]+$/;\n\
        \n    const validCoupons = [];\n    const n = code.length;\n\n    for (let i\
        \ = 0; i < n; i++) {\n        // Condition 3: isActive[i] is true\n        if\
        \ (!isActive[i]) {\n            continue;\n        }\n\n        // Condition\
        \ 2: businessLine[i] is one of the four categories\n        const currentBusinessLine\
        \ = businessLine[i];\n        if (!(currentBusinessLine in businessLinePriorities))\
        \ {\n            continue;\n        }\n        const priority = businessLinePriorities[currentBusinessLine];\n\
        \n        // Condition 1: code[i] is non-empty and consists only of alphanumeric\
        \ characters and underscores\n        const currentCode = code[i];\n       \
        \ if (!currentCode || !codeRegex.test(currentCode)) {\n            continue;\n\
        \        }\n\n        // If all conditions pass, add to validCoupons list\n\
        \        validCoupons.push({ businessLine: currentBusinessLine, code: currentCode,\
        \ priority: priority });\n    }\n\n    // Sort validCoupons\n    validCoupons.sort((a,\
        \ b) => {\n        if (a.priority !== b.priority) {\n            return a.priority\
        \ - b.priority;\n        }\n        return a.code.localeCompare(b.code); //\
        \ Lexicographical sort by code\n    });\n\n    // Extract and return codes\n\
        \    return validCoupons.map(coupon => coupon.code);\n};"
      typescript: "function validateCoupons(code: string[], businessLine: string[],\
        \ isActive: boolean[]): string[] {\n    const businessLinePriorities: { [key:\
        \ string]: number } = {\n        \"electronics\": 0,\n        \"grocery\": 1,\n\
        \        \"pharmacy\": 2,\n        \"restaurant\": 3\n    };\n\n    const codeRegex\
        \ = /^[a-zA-Z0-9_]+$/;\n\n    interface CouponData {\n        businessLine:\
        \ string;\n        code: string;\n        priority: number;\n    }\n\n    const\
        \ validCoupons: CouponData[] = [];\n    const n = code.length;\n\n    for (let\
        \ i = 0; i < n; i++) {\n        // Condition 3: isActive[i] is true\n      \
        \  if (!isActive[i]) {\n            continue;\n        }\n\n        // Condition\
        \ 2: businessLine[i] is one of the four categories\n        const currentBusinessLine\
        \ = businessLine[i];\n        if (!(currentBusinessLine in businessLinePriorities))\
        \ {\n            continue;\n        }\n        const priority = businessLinePriorities[currentBusinessLine];\n\
        \n        // Condition 1: code[i] is non-empty and consists only of alphanumeric\
        \ characters and underscores\n        const currentCode = code[i];\n       \
        \ if (!currentCode || !codeRegex.test(currentCode)) {\n            continue;\n\
        \        }\n\n        // If all conditions pass, add to validCoupons list\n\
        \        validCoupons.push({ businessLine: currentBusinessLine, code: currentCode,\
        \ priority: priority });\n    }\n\n    // Sort validCoupons\n    validCoupons.sort((a,\
        \ b) => {\n        if (a.priority !== b.priority) {\n            return a.priority\
        \ - b.priority;\n        }\n        return a.code.localeCompare(b.code); //\
        \ Lexicographical sort by code\n    });\n\n    // Extract and return codes\n\
        \    return validCoupons.map(coupon => coupon.code);\n}"
      php: "<?php\nclass Solution {\n\n    /**\n     * @param String[] $code\n     *\
        \ @param String[] $businessLine\n     * @param Boolean[] $isActive\n     * @return\
        \ String[]\n     */\n    function validateCoupons($code, $businessLine, $isActive)\
        \ {\n        $businessLinePriorities = [\n            \"electronics\" => 0,\n\
        \            \"grocery\" => 1,\n            \"pharmacy\" => 2,\n           \
        \ \"restaurant\" => 3\n        ];\n\n        $validCoupons = [];\n        $n\
        \ = count($code);\n\n        for ($i = 0; $i < $n; $i++) {\n            // Condition\
        \ 3: isActive[i] is true\n            if (!$isActive[$i]) {\n              \
        \  continue;\n            }\n\n            // Condition 2: businessLine[i] is\
        \ one of the four categories\n            $currentBusinessLine = $businessLine[$i];\n\
        \            if (!isset($businessLinePriorities[$currentBusinessLine])) {\n\
        \                continue;\n            }\n            $priority = $businessLinePriorities[$currentBusinessLine];\n\
        \n            // Condition 1: code[i] is non-empty and consists only of alphanumeric\
        \ characters and underscores\n            $currentCode = $code[$i];\n      \
        \      if (empty($currentCode) || !preg_match('/^[a-zA-Z0-9_]+$/', $currentCode))\
        \ {\n                continue;\n            }\n\n            // If all conditions\
        \ pass, add to validCoupons list\n            $validCoupons[] = ['businessLine'\
        \ => $currentBusinessLine, 'code' => $currentCode, 'priority' => $priority];\n\
        \        }\n\n        // Sort validCoupons\n        usort($validCoupons, function($a,\
        \ $b) {\n            if ($a['priority'] !== $b['priority']) {\n            \
        \    return $a['priority'] - $b['priority'];\n            }\n            return\
        \ strcmp($a['code'], $b['code']); // Lexicographical sort by code\n        });\n\
        \n        // Extract and return codes\n        $result = [];\n        foreach\
        \ ($validCoupons as $coupon) {\n            $result[] = $coupon['code'];\n \
        \       }\n\n        return $result;\n    }\n}\n?>"
      swift: "import Foundation\n\nclass Solution {\n    func validateCoupons(_ code:\
        \ [String], _ businessLine: [String], _ isActive: [Bool]) -> [String] {\n  \
        \      let businessLinePriorities: [String: Int] = [\n            \"electronics\"\
        : 0,\n            \"grocery\": 1,\n            \"pharmacy\": 2,\n          \
        \  \"restaurant\": 3\n        ]\n\n        struct CouponData {\n           \
        \ let businessLine: String\n            let code: String\n            let priority:\
        \ Int\n        }\n\n        var validCoupons: [CouponData] = []\n        let\
        \ n = code.count\n\n        for i in 0..<n {\n            // Condition 3: isActive[i]\
        \ is true\n            if !isActive[i] {\n                continue\n       \
        \     }\n\n            // Condition 2: businessLine[i] is one of the four categories\n\
        \            let currentBusinessLine = businessLine[i]\n            guard let\
        \ priority = businessLinePriorities[currentBusinessLine] else {\n          \
        \      continue\n            }\n\n            // Condition 1: code[i] is non-empty\
        \ and consists only of alphanumeric characters and underscores\n           \
        \ let currentCode = code[i]\n            if currentCode.isEmpty || currentCode.range(of:\
        \ \"^[a-zA-Z0-9_]+$\", options: .regularExpression) == nil {\n             \
        \   continue\n            }\n\n            // If all conditions pass, add to\
        \ validCoupons list\n            validCoupons.append(CouponData(businessLine:\
        \ currentBusinessLine, code: currentCode, priority: priority))\n        }\n\n\
        \        // Sort validCoupons\n        validCoupons.sort { (a, b) in\n     \
        \       if a.priority != b.priority {\n                return a.priority < b.priority\n\
        \            }\n            return a.code < b.code // Lexicographical sort by\
        \ code\n        }\n\n        // Extract and return codes\n        return validCoupons.map\
        \ { $0.code }\n    }\n}"
      kotlin: "class Solution {\n    fun validateCoupons(code: List<String>, businessLine:\
        \ List<String>, isActive: List<Boolean>): List<String> {\n        val businessLinePriorities\
        \ = mapOf(\n            \"electronics\" to 0,\n            \"grocery\" to 1,\n\
        \            \"pharmacy\" to 2,\n            \"restaurant\" to 3\n        )\n\
        \n        data class CouponData(\n            val businessLine: String,\n  \
        \          val code: String,\n            val priority: Int\n        )\n\n \
        \       val validCoupons = mutableListOf<CouponData>()\n        val n = code.size\n\
        \n        for (i in 0 until n) {\n            // Condition 3: isActive[i] is\
        \ true\n            if (!isActive[i]) {\n                continue\n        \
        \    }\n\n            // Condition 2: businessLine[i] is one of the four categories\n\
        \            val currentBusinessLine = businessLine[i]\n            val priority\
        \ = businessLinePriorities[currentBusinessLine]\n            if (priority ==\
        \ null) {\n                continue\n            }\n\n            // Condition\
        \ 1: code[i] is non-empty and consists only of alphanumeric characters and underscores\n\
        \            val currentCode = code[i]\n            if (currentCode.isEmpty()\
        \ || !currentCode.matches(Regex(\"^[a-zA-Z0-9_]+$\"))) {\n                continue\n\
        \            }\n\n            // If all conditions pass, add to validCoupons\
        \ list\n            validCoupons.add(CouponData(currentBusinessLine, currentCode,\
        \ priority))\n        }\n\n        // Sort validCoupons\n        validCoupons.sortWith(Comparator\
        \ {\n            a, b ->\n            val priorityComparison = a.priority.compareTo(b.priority)\n\
        \            if (priorityComparison != 0) {\n                priorityComparison\n\
        \            } else {\n                a.code.compareTo(b.code) // Lexicographical\
        \ sort by code\n            }\n        })\n\n        // Extract and return codes\n\
        \        return validCoupons.map { it.code }\n    }\n}"
      dart: "class Solution {\n  List<String> validateCoupons(List<String> code, List<String>\
        \ businessLine, List<bool> isActive) {\n    final Map<String, int> businessLinePriorities\
        \ = {\n      \"electronics\": 0,\n      \"grocery\": 1,\n      \"pharmacy\"\
        : 2,\n      \"restaurant\": 3\n    };\n\n    final RegExp codeRegex = RegExp(r'^[a-zA-Z0-9_]+$');\n\
        \n    final List<({String businessLine, String code, int priority})> validCoupons\
        \ = [];\n    final int n = code.length;\n\n    for (int i = 0; i < n; i++) {\n\
        \      // Condition 3: isActive[i] is true\n      if (!isActive[i]) {\n    \
        \    continue;\n      }\n\n      // Condition 2: businessLine[i] is one of the\
        \ four categories\n      final String currentBusinessLine = businessLine[i];\n\
        \      final int? priority = businessLinePriorities[currentBusinessLine];\n\
        \      if (priority == null) {\n        continue;\n      }\n\n      // Condition\
        \ 1: code[i] is non-empty and consists only of alphanumeric characters and underscores\n\
        \      final String currentCode = code[i];\n      if (currentCode.isEmpty ||\
        \ !codeRegex.hasMatch(currentCode)) {\n        continue;\n      }\n\n      //\
        \ If all conditions pass, add to validCoupons list\n      validCoupons.add((businessLine:\
        \ currentBusinessLine, code: currentCode, priority: priority));\n    }\n\n \
        \   // Sort validCoupons\n    validCoupons.sort((a, b) {\n      final int priorityComparison\
        \ = a.priority.compareTo(b.priority);\n      if (priorityComparison != 0) {\n\
        \        return priorityComparison;\n      }\n      return a.code.compareTo(b.code);\
        \ // Lexicographical sort by code\n    });\n\n    // Extract and return codes\n\
        \    return validCoupons.map((coupon) => coupon.code).toList();\n  }\n}"
      go: "import (\n\t\"regexp\"\n\t\"sort\"\n)\n\n// CouponData struct to hold coupon\
        \ information for sorting\ntype CouponData struct {\n\tBusinessLine string\n\
        \tCode         string\n\tPriority     int\n}\n\nvar codeRegex = regexp.MustCompile(\"\
        ^[a-zA-Z0-9_]+$\")\n\nfunc validateCoupons(code []string, businessLine []string,\
        \ isActive []bool) []string {\n\tbusinessLinePriorities := map[string]int{\n\
        \t\t\"electronics\": 0,\n\t\t\"grocery\":     1,\n\t\t\"pharmacy\":    2,\n\t\
        \t\"restaurant\":  3,\n\t}\n\n\tvar validCoupons []CouponData\n\tn := len(code)\n\
        \n\tfor i := 0; i < n; i++ {\n\t\t// Condition 3: isActive[i] is true\n\t\t\
        if !isActive[i] {\n\t\t\tcontinue\n\t\t}\n\n\t\t// Condition 2: businessLine[i]\
        \ is one of the four categories\n\t\tcurrentBusinessLine := businessLine[i]\n\
        \t\tpriority, exists := businessLinePriorities[currentBusinessLine]\n\t\tif\
        \ !exists {\n\t\t\tcontinue\n\t\t}\n\n\t\t// Condition 1: code[i] is non-empty\
        \ and consists only of alphanumeric characters and underscores\n\t\tcurrentCode\
        \ := code[i]\n\t\tif currentCode == \"\" || !codeRegex.MatchString(currentCode)\
        \ {\n\t\t\tcontinue\n\t\t}\n\n\t\t// If all conditions pass, add to validCoupons\
        \ list\n\t\tvalidCoupons = append(validCoupons, CouponData{\n\t\t\tBusinessLine:\
        \ currentBusinessLine,\n\t\t\tCode:         currentCode,\n\t\t\tPriority:  \
        \   priority,\n\t\t})\n\t}\n\n\t// Sort validCoupons\n\tsort.Slice(validCoupons,\
        \ func(i, j int) bool {\n\t\tif validCoupons[i].Priority != validCoupons[j].Priority\
        \ {\n\t\t\treturn validCoupons[i].Priority < validCoupons[j].Priority\n\t\t\
        }\n\t\treturn validCoupons[i].Code < validCoupons[j].Code // Lexicographical\
        \ sort by code\n\t})\n\n\t// Extract and return codes\n\tresult := make([]string,\
        \ len(validCoupons))\n\tfor i, coupon := range validCoupons {\n\t\tresult[i]\
        \ = coupon.Code\n\t}\n\n\treturn result\n}"
      ruby: "class Solution\n    # @param {String[]} code\n    # @param {String[]} business_line\n\
        \    # @param {Boolean[]} is_active\n    # @return {String[]}\n    def validate_coupons(code,\
        \ business_line, is_active)\n        business_line_priorities = {\n        \
        \    \"electronics\" => 0,\n            \"grocery\" => 1,\n            \"pharmacy\"\
        \ => 2,\n            \"restaurant\" => 3\n        }\n\n        code_regex =\
        \ /^[a-zA-Z0-9_]+$/\n\n        valid_coupons = []\n        n = code.length\n\
        \n        (0...n).each do |i|\n            # Condition 3: is_active[i] is true\n\
        \            next unless is_active[i]\n\n            # Condition 2: business_line[i]\
        \ is one of the four categories\n            current_business_line = business_line[i]\n\
        \            priority = business_line_priorities[current_business_line]\n  \
        \          next if priority.nil?\n\n            # Condition 1: code[i] is non-empty\
        \ and consists only of alphanumeric characters and underscores\n           \
        \ current_code = code[i]\n            next if current_code.empty? || !(current_code\
        \ =~ code_regex)\n\n            # If all conditions pass, add to valid_coupons\
        \ list\n            valid_coupons << { business_line: current_business_line,\
        \ code: current_code, priority: priority }\n        end\n\n        # Sort valid_coupons\n\
        \        valid_coupons.sort! do |a, b|\n            priority_comparison = a[:priority]\
        \ <=> b[:priority]\n            if priority_comparison != 0\n              \
        \  priority_comparison\n            else\n                a[:code] <=> b[:code]\
        \ # Lexicographical sort by code\n            end\n        end\n\n        #\
        \ Extract and return codes\n        valid_coupons.map { |coupon| coupon[:code]\
        \ }\n    end\nend"
      scala: "import scala.collection.mutable.ListBuffer\n\nclass Solution {\n    def\
        \ validateCoupons(code: List[String], businessLine: List[String], isActive:\
        \ List[Boolean]): List[String] = {\n        val businessLinePriorities: Map[String,\
        \ Int] = Map(\n            \"electronics\" -> 0,\n            \"grocery\" ->\
        \ 1,\n            \"pharmacy\" -> 2,\n            \"restaurant\" -> 3\n    \
        \    )\n\n        case class CouponData(\n            businessLine: String,\n\
        \            code: String,\n            priority: Int\n        )\n\n       \
        \ val codeRegex = \"^[a-zA-Z0-9_]+$\".r\n\n        val validCoupons = ListBuffer[CouponData]()\n\
        \        val n = code.length\n\n        for (i <- 0 until n) {\n           \
        \ // Condition 3: isActive(i) is true\n            if (!isActive(i)) {\n   \
        \             // continue\n            } else {\n                // Condition\
        \ 2: businessLine(i) is one of the four categories\n                val currentBusinessLine\
        \ = businessLine(i)\n                val priority = businessLinePriorities.get(currentBusinessLine)\n\
        \                if (priority.isEmpty) {\n                    // continue\n\
        \                } else {\n                    // Condition 1: code(i) is non-empty\
        \ and consists only of alphanumeric characters and underscores\n           \
        \         val currentCode = code(i)\n                    if (currentCode.isEmpty\
        \ || codeRegex.findFirstIn(currentCode).isEmpty) {\n                       \
        \ // continue\n                    } else {\n                        // If all\
        \ conditions pass, add to validCoupons list\n                        validCoupons\
        \ += CouponData(currentBusinessLine, currentCode, priority.get)\n          \
        \          }\n                }\n            }\n        }\n\n        // Sort\
        \ validCoupons\n        val sortedCoupons = validCoupons.sortBy(coupon => (coupon.priority,\
        \ coupon.code))\n\n        // Extract and return codes\n        sortedCoupons.map(_.code).toList\n\
        \    }\n}"
      rust: "impl Solution {\n    pub fn validate_coupons(code: Vec<String>, business_line:\
        \ Vec<String>, is_active: Vec<bool>) -> Vec<String> {\n        use std::collections::HashMap;\n\
        \n        let business_line_priorities: HashMap<String, i32> = [\n         \
        \   (\"electronics\".to_string(), 0),\n            (\"grocery\".to_string(),\
        \ 1),\n            (\"pharmacy\".to_string(), 2),\n            (\"restaurant\"\
        .to_string(), 3),\n        ].iter().cloned().collect();\n\n        #[derive(Debug,\
        \ PartialEq, Eq, PartialOrd, Ord)]\n        struct CouponData {\n          \
        \  priority: i32,\n            code: String,\n            business_line: String,\
        \ // Not strictly needed for sorting, but good for completeness\n        }\n\
        \n        let mut valid_coupons: Vec<CouponData> = Vec::new();\n        let\
        \ n = code.len();\n\n        for i in 0..n {\n            // Condition 3: is_active[i]\
        \ is true\n            if !is_active[i] {\n                continue;\n     \
        \       }\n\n            // Condition 2: business_line[i] is one of the four\
        \ categories\n            let current_business_line = &business_line[i];\n \
        \           let Some(&priority) = business_line_priorities.get(current_business_line)\
        \ else {\n                continue;\n            };\n\n            // Condition\
        \ 1: code[i] is non-empty and consists only of alphanumeric characters and underscores\n\
        \            let current_code = &code[i];\n            if current_code.is_empty()\
        \ || !current_code.chars().all(|c| c.is_ascii_alphanumeric() || c == '_') {\n\
        \                continue;\n            }\n\n            // If all conditions\
        \ pass, add to valid_coupons list\n            valid_coupons.push(CouponData\
        \ {\n                business_line: current_business_line.clone(),\n       \
        \         code: current_code.clone(),\n                priority,\n         \
        \   });\n        }\n\n        // Sort valid_coupons\n        valid_coupons.sort_unstable();\
        \ // Uses the derived Ord trait for sorting\n\n        // Extract and return\
        \ codes\n        valid_coupons.into_iter().map(|coupon| coupon.code).collect()\n\
        \    }\n}"
      racket: "#lang racket\n\n(provide (rename-out [validate-coupons validateCoupons]))\n\
        \n(define (validate-coupons code businessLine isActive)\n  (define business-line-priorities\n\
        \    (hash\n     \"electronics\" 0\n     \"grocery\" 1\n     \"pharmacy\" 2\n\
        \     \"restaurant\" 3))\n\n  (define (valid-code? s)\n    (and (not (string-empty?\
        \ s))\n         (regexp-match? #rx\"^[a-zA-Z0-9_]+$\" s)))\n\n  (define valid-coupons\
        \ (make-list-buffer))\n  (define n (vector-length code))\n\n  (for ([i (in-range\
        \ n)])\n    (when (vector-ref isActive i)\n      (define current-business-line\
        \ (vector-ref businessLine i))\n      (define priority (hash-ref business-line-priorities\
        \ current-business-line #f))\n      (when priority\n        (define current-code\
        \ (vector-ref code i))\n        (when (valid-code? current-code)\n         \
        \ (add-to-list-buffer! valid-coupons (list current-business-line current-code\
        \ priority))))))\n\n  (define sorted-coupons\n    (sort (list-buffer->list valid-coupons)\n\
        \          (lambda (a b)\n            (define priority-a (list-ref a 2))\n \
        \           (define priority-b (list-ref b 2))\n            (if (not (= priority-a\
        \ priority-b))\n                (< priority-a priority-b)\n                (string<?\
        \ (list-ref a 1) (list-ref b 1))))))\n\n  (map (lambda (coupon) (list-ref coupon\
        \ 1)) sorted-coupons))\n\n;; Helper for mutable list (not standard Racket, but\
        \ common in competitive programming contexts)\n(struct list-buffer (lst tail)\
        \ #:mutable #t)\n(define (make-list-buffer) (list-buffer '() '()))\n(define\
        \ (add-to-list-buffer! lb item)\n  (if (null? (list-buffer-lst lb))\n      (begin\n\
        \        (set-list-buffer-lst! lb (list item))\n        (set-list-buffer-tail!\
        \ lb (list-buffer-lst lb)))\n      (begin\n        (set-cdr! (list-buffer-tail\
        \ lb) (list item))\n        (set-list-buffer-tail! lb (cdr (list-buffer-tail\
        \ lb))))))\n(define (list-buffer->list lb) (list-buffer-lst lb))"
      erlang: "-module(solution).\n-export([validateCoupons/3]).\n\nvalidateCoupons(Code,\
        \ BusinessLine, IsActive) ->\n    BusinessLinePriorities = #{\"electronics\"\
        \ => 0, \"grocery\" => 1, \"pharmacy\" => 2, \"restaurant\" => 3},\n    CodeRegex\
        \ = re:compile(\"^[a-zA-Z0-9_]+$\"),\n\n    N = length(Code),\n    Indices =\
        \ lists:seq(0, N - 1),\n\n    ValidCoupons = lists:foldl(\n        fun(I, Acc)\
        \ ->\n            CurrentIsActive = lists:nth(I + 1, IsActive),\n          \
        \  CurrentBusinessLine = lists:nth(I + 1, BusinessLine),\n            CurrentCode\
        \ = lists:nth(I + 1, Code),\n\n            % Condition 3: IsActive[i] is true\n\
        \            case CurrentIsActive of\n                true ->\n            \
        \        % Condition 2: BusinessLine[i] is one of the four categories\n    \
        \                case maps:get(CurrentBusinessLine, BusinessLinePriorities,\
        \ undefined) of\n                        undefined -> Acc;\n               \
        \         Priority ->\n                            % Condition 1: Code[i] is\
        \ non-empty and consists only of alphanumeric characters and underscores\n \
        \                           case CurrentCode =/= \"\" andalso re:run(CurrentCode,\
        \ CodeRegex, [{return, binary}]) of\n                                {match,\
        \ _} ->\n                                    [{Priority, CurrentCode} | Acc];\n\
        \                                _ -> Acc\n                            end\n\
        \                    end;\n                false -> Acc\n            end\n \
        \       end, [], Indices),\n\n    % Sort validCoupons\n    % Erlang's lists:sort\
        \ sorts by the first element of a tuple, then the second, etc.\n    SortedCoupons\
        \ = lists:sort(ValidCoupons),\n\n    % Extract and return codes\n    lists:map(fun({_,\
        \ CodeVal}) -> CodeVal end, SortedCoupons)."
      elixir: "defmodule Solution do\n  @business_line_priorities %{\n    \"electronics\"\
        \ => 0,\n    \"grocery\" => 1,\n    \"pharmacy\" => 2,\n    \"restaurant\" =>\
        \ 3\n  }\n\n  @code_regex ~r/^[a-zA-Z0-9_]+$/\n\n  @spec validate_coupons(code\
        \ :: [String.t()], business_line :: [String.t()], is_active :: [boolean()])\
        \ :: [String.t()]\n  def validate_coupons(code, business_line, is_active) do\n\
        \    n = length(code)\n\n    valid_coupons = Enum.reduce(0..(n - 1), [], fn\
        \ i, acc ->\n      current_is_active = Enum.at(is_active, i)\n      current_business_line\
        \ = Enum.at(business_line, i)\n      current_code = Enum.at(code, i)\n\n   \
        \   # Condition 3: is_active[i] is true\n      if current_is_active do\n   \
        \     # Condition 2: business_line[i] is one of the four categories\n      \
        \  case Map.fetch(@business_line_priorities, current_business_line) do\n   \
        \       {:ok, priority} ->\n            # Condition 1: code[i] is non-empty\
        \ and consists only of alphanumeric characters and underscores\n           \
        \ if current_code != \"\" and String.match?(current_code, @code_regex) do\n\
        \              [{priority, current_code} | acc]\n            else\n        \
        \      acc\n            end\n          :error ->\n            acc\n        end\n\
        \      else\n        acc\n      end\n    end)\n\n    # Sort valid_coupons\n\
        \    # Elixir's Enum.sort sorts tuples by their elements from left to right\
        \ by default\n    sorted_coupons = Enum.sort(valid_coupons)\n\n    # Extract\
        \ and return codes\n    Enum.map(sorted_coupons, fn {_, code_val} -> code_val\
        \ end)\n  end\nend"
    approach: 'The solution involves a two-phase process: filtering and sorting. First,
      we iterate through all coupons, applying the three validation rules. For each
      coupon, we check if it is active, if its business line is one of the four allowed
      categories, and if its code is non-empty and consists only of alphanumeric characters
      and underscores. If a coupon satisfies all conditions, we store its business line
      and code as a pair in a temporary list. To facilitate sorting by business line,
      we use a predefined map that assigns an integer priority to each valid business
      line (e.g., "electronics" -> 0, "grocery" -> 1, etc.).'
    time_complexity: The time complexity is O(N * L_max + K * log(K) * L_max), where
      N is the total number of coupons, L_max is the maximum length of a coupon code
      or business line string, and K is the number of valid coupons. The initial filtering
      loop iterates N times, and within each iteration, string validation (e.g., regex
      or character-by-character check) takes up to O(L_max) time. Storing valid coupons
      takes O(K * L_max) space. The sorting step involves K items, and each comparison
      takes O(L_max) time due to string comparisons, leading to O(K * log(K) * L_max)
      for sorting. In the worst case, K can be N.
    space_complexity: The space complexity is O(K * L_max), where K is the number of
      valid coupons and L_max is the maximum length of a coupon code or business line
      string. This space is primarily used to store the list of valid coupons, where
      each coupon stores its business line and code. In the worst case, all N coupons
      are valid, resulting in O(N * L_max) space. The map for business line priorities
      uses O(1) space as it has a fixed number of entries.
    elapsed_time: 69.79348540306091
    model: gemini-2.5-flash
    generated_at: '2025-12-13 01:04:07 '
  - solutions:
      cpp: "class Solution {\npublic:\n    vector<string> validateCoupons(vector<string>&\
        \ code, vector<string>& businessLine, vector<bool>& isActive) {\n        vector<pair<string,\
        \ string>> validCoupons;\n        unordered_map<string, int> priority = {\"\
        electronics\", 0}, {\"grocery\", 1}, {\"pharmacy\", 2}, {\"restaurant\", 3}\n\
        \        for (int i = 0; i < code.size(); i++) {\n            if (isActive[i]\
        \ && !code[i].empty()) {\n                bool validCode = true;\n         \
        \       for (char c : code[i]) {\n                    if (!isalnum(c) && c !=\
        \ '_') {\n                        validCode = false;\n                     \
        \   break;\n                    }\n                }\n                if (validCode\
        \ && priority.find(businessLine[i]) != priority.end()) {\n                 \
        \   validCoupons.push_back({businessLine[i], code[i]});\n                }\n\
        \            }\n        }\n        sort(validCoupons.begin(), validCoupons.end(),\
        \ [&](pair<string, string>& a, pair<string, string>& b) {\n            if (priority[a.first]\
        \ == priority[b.first]) {\n                return a.second < b.second;\n   \
        \         }\n            return priority[a.first] < priority[b.first];\n   \
        \     });\n        vector<string> result;\n        for (auto& coupon : validCoupons)\
        \ {\n            result.push_back(coupon.second);\n        }\n        return\
        \ result;\n    }\n};"
      java: "import java.util.*;\npublic class Solution {\n    public List<String> validateCoupons(String[]\
        \ code, String[] businessLine, boolean[] isActive) {\n        List<String[]>\
        \ validCoupons = new ArrayList<>();\n        Map<String, Integer> priority =\
        \ new HashMap<>();\n        priority.put(\"electronics\", 0);\n        priority.put(\"\
        grocery\", 1);\n        priority.put(\"pharmacy\", 2);\n        priority.put(\"\
        restaurant\", 3);\n        for (int i = 0; i < code.length; i++) {\n       \
        \     if (isActive[i] && !code[i].isEmpty()) {\n                boolean validCode\
        \ = true;\n                for (char c : code[i].toCharArray()) {\n        \
        \            if (!Character.isLetterOrDigit(c) && c != '_') {\n            \
        \            validCode = false;\n                        break;\n          \
        \          }\n                }\n                if (validCode && priority.containsKey(businessLine[i]))\
        \ {\n                    validCoupons.add(new String[]{businessLine[i], code[i]});\n\
        \                }\n            }\n        }\n        Collections.sort(validCoupons,\
        \ (a, b) -> {\n            if (priority.get(a[0]).equals(priority.get(b[0])))\
        \ {\n                return a[1].compareTo(b[1]);\n            }\n         \
        \   return priority.get(a[0]) - priority.get(b[0]);\n        });\n        List<String>\
        \ result = new ArrayList<>();\n        for (String[] coupon : validCoupons)\
        \ {\n            result.add(coupon[1]);\n        }\n        return result;\n\
        \    }\n}"
      python: "class Solution:\n    def validateCoupons(self, code: list[str], businessLine:\
        \ list[str], isActive: list[bool]) -> list[str]:\n        validCoupons = []\n\
        \        priority = {\"electronics\": 0, \"grocery\": 1, \"pharmacy\": 2, \"\
        restaurant\": 3}\n        for i in range(len(code)):\n            if isActive[i]\
        \ and code[i] and all(c.isalnum() or c == '_' for c in code[i]) and businessLine[i]\
        \ in priority:\n                validCoupons.append((businessLine[i], code[i]))\n\
        \        validCoupons.sort(key=lambda x: (priority[x[0]], x[1]))\n        return\
        \ [coupon[1] for coupon in validCoupons]"
      python3: "class Solution:\n    def validateCoupons(self, code: list[str], businessLine:\
        \ list[str], isActive: list[bool]) -> list[str]:\n        validCoupons = []\n\
        \        priority = {\"electronics\": 0, \"grocery\": 1, \"pharmacy\": 2, \"\
        restaurant\": 3}\n        for i in range(len(code)):\n            if isActive[i]\
        \ and code[i] and all(c.isalnum() or c == '_' for c in code[i]) and businessLine[i]\
        \ in priority:\n                validCoupons.append((businessLine[i], code[i]))\n\
        \        validCoupons.sort(key=lambda x: (priority[x[0]], x[1]))\n        return\
        \ [coupon[1] for coupon in validCoupons]"
      c: "typedef struct {\n    char* businessLine;\n    char* code;\n} Coupon;\n\n\
        int compareCoupons(const void* a, const void* b) {\n    Coupon* couponA = (Coupon*)a;\n\
        \    Coupon* couponB = (Coupon*)b;\n    int priorityA = 0, priorityB = 0;\n\
        \    if (strcmp(couponA->businessLine, \"electronics\") == 0) priorityA = 0;\n\
        \    else if (strcmp(couponA->businessLine, \"grocery\") == 0) priorityA = 1;\n\
        \    else if (strcmp(couponA->businessLine, \"pharmacy\") == 0) priorityA =\
        \ 2;\n    else if (strcmp(couponA->businessLine, \"restaurant\") == 0) priorityA\
        \ = 3;\n    if (strcmp(couponB->businessLine, \"electronics\") == 0) priorityB\
        \ = 0;\n    else if (strcmp(couponB->businessLine, \"grocery\") == 0) priorityB\
        \ = 1;\n    else if (strcmp(couponB->businessLine, \"pharmacy\") == 0) priorityB\
        \ = 2;\n    else if (strcmp(couponB->businessLine, \"restaurant\") == 0) priorityB\
        \ = 3;\n    if (priorityA == priorityB) return strcmp(couponA->code, couponB->code);\n\
        \    return priorityA - priorityB;\n}\n\nchar** validateCoupons(char** code,\
        \ char** businessLine, int* isActive, int codeSize, int* returnSize) {\n   \
        \ Coupon* validCoupons = (Coupon*)malloc(codeSize * sizeof(Coupon));\n    int\
        \ validCount = 0;\n    for (int i = 0; i < codeSize; i++) {\n        if (isActive[i]\
        \ && code[i][0] != '\\0') {\n            int validCode = 1;\n            for\
        \ (char* c = code[i]; *c != '\\0'; c++) {\n                if (!isalnum(*c)\
        \ && *c != '_') {\n                    validCode = 0;\n                    break;\n\
        \                }\n            }\n            if (validCode && (strcmp(businessLine[i],\
        \ \"electronics\") == 0 || strcmp(businessLine[i], \"grocery\") == 0 || strcmp(businessLine[i],\
        \ \"pharmacy\") == 0 || strcmp(businessLine[i], \"restaurant\") == 0)) {\n \
        \               validCoupons[validCount].businessLine = businessLine[i];\n \
        \               validCoupons[validCount].code = code[i];\n                validCount++;\n\
        \            }\n        }\n    }\n    qsort(validCoupons, validCount, sizeof(Coupon),\
        \ compareCoupons);\n    char** result = (char**)malloc(validCount * sizeof(char*));\n\
        \    for (int i = 0; i < validCount; i++) {\n        result[i] = validCoupons[i].code;\n\
        \    }\n    *returnSize = validCount;\n    return result;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\nusing System.Linq;\n\
        public class Solution {\n    public string[] ValidateCoupons(string[] code,\
        \ string[] businessLine, bool[] isActive) {\n        var validCoupons = new\
        \ List<(string businessLine, string code)>();\n        var priority = new Dictionary<string,\
        \ int> { {\"electronics\", 0}, {\"grocery\", 1}, {\"pharmacy\", 2}, {\"restaurant\"\
        , 3} };\n        for (int i = 0; i < code.Length; i++) {\n            if (isActive[i]\
        \ && !string.IsNullOrEmpty(code[i]) && code[i].All(c => char.IsLetterOrDigit(c)\
        \ || c == '_') && priority.ContainsKey(businessLine[i])) {\n               \
        \ validCoupons.Add((businessLine[i], code[i]));\n            }\n        }\n\
        \        validCoupons.Sort((a, b) => {\n            if (priority[a.businessLine]\
        \ == priority[b.businessLine]) {\n                return string.Compare(a.code,\
        \ b.code);\n            }\n            return priority[a.businessLine].CompareTo(priority[b.businessLine]);\n\
        \        });\n        return validCoupons.Select(c => c.code).ToArray();\n \
        \   }\n}"
      javascript: "var validateCoupons = function(code, businessLine, isActive) {\n\
        \    var validCoupons = [];\n    var priority = {\"electronics\": 0, \"grocery\"\
        : 1, \"pharmacy\": 2, \"restaurant\": 3};\n    for (var i = 0; i < code.length;\
        \ i++) {\n        if (isActive[i] && code[i] && /^[a-zA-Z0-9_]+$/.test(code[i])\
        \ && businessLine[i] in priority) {\n            validCoupons.push([businessLine[i],\
        \ code[i]]);\n        }\n    }\n    validCoupons.sort(function(a, b) {\n   \
        \     if (priority[a[0]] == priority[b[0]]) {\n            return a[1].localeCompare(b[1]);\n\
        \        }\n        return priority[a[0]] - priority[b[0]];\n    });\n    return\
        \ validCoupons.map(function(coupon) {\n        return coupon[1];\n    });\n\
        };"
      typescript: "function validateCoupons(code: string[], businessLine: string[],\
        \ isActive: boolean[]): string[] {\n    const validCoupons: [string, string][]\
        \ = [];\n    const priority: { [key: string]: number } = {\"electronics\": 0,\
        \ \"grocery\": 1, \"pharmacy\": 2, \"restaurant\": 3};\n    for (let i = 0;\
        \ i < code.length; i++) {\n        if (isActive[i] && code[i] && /^[a-zA-Z0-9_]+$/.test(code[i])\
        \ && businessLine[i] in priority) {\n            validCoupons.push([businessLine[i],\
        \ code[i]]);\n        }\n    }\n    validCoupons.sort((a, b) => {\n        if\
        \ (priority[a[0]] === priority[b[0]]) {\n            return a[1].localeCompare(b[1]);\n\
        \        }\n        return priority[a[0]] - priority[b[0]];\n    });\n    return\
        \ validCoupons.map(coupon => coupon[1]);\n}"
      php: "$validCoupons = [];\n$priority = [\"electronics\" => 0, \"grocery\" => 1,\
        \ \"pharmacy\" => 2, \"restaurant\" => 3];\nforeach ($code as $i => $c) {\n\
        \    if ($isActive[$i] && $c && preg_match('/^[a-zA-Z0-9_]+$/', $c) && array_key_exists($businessLine[$i],\
        \ $priority)) {\n        $validCoupons[] = [$businessLine[$i], $c];\n    }\n\
        }\nusort($validCoupons, function($a, $b) {\n    if ($priority[$a[0]] == $priority[$b[0]])\
        \ {\n        return strcmp($a[1], $b[1]);\n    }\n    return $priority[$a[0]]\
        \ - $priority[$b[0]];\n});\n$result = array_map(function($coupon) {\n    return\
        \ $coupon[1];\n}, $validCoupons);\nreturn $result;"
      swift: "func validateCoupons(_ code: [String], _ businessLine: [String], _ isActive:\
        \ [Bool]) -> [String] {\n    var validCoupons: [(String, String)] = []\n   \
        \ let priority: [String: Int] = [\"electronics\": 0, \"grocery\": 1, \"pharmacy\"\
        : 2, \"restaurant\": 3]\n    for i in 0..<code.count {\n        if isActive[i]\
        \ && !code[i].isEmpty && code[i].range(of: \"^[a-zA-Z0-9_]+$\", options: .regularExpression)\
        \ != nil && priority[businessLine[i]] != nil {\n            validCoupons.append((businessLine[i],\
        \ code[i]))\n        }\n    }\n    validCoupons.sort { (a, b) -> Bool in\n \
        \       if priority[a.0] == priority[b.0] {\n            return a.1 < b.1\n\
        \        }\n        return priority[a.0]! < priority[b.0]!\n    }\n    return\
        \ validCoupons.map { $0.1 }\n}"
      kotlin: "fun validateCoupons(code: Array<String>, businessLine: Array<String>,\
        \ isActive: BooleanArray): Array<String> {\n    val validCoupons = mutableListOf<Pair<String,\
        \ String>>()\n    val priority = mapOf(\"electronics\" to 0, \"grocery\" to\
        \ 1, \"pharmacy\" to 2, \"restaurant\" to 3)\n    for (i in code.indices) {\n\
        \        if (isActive[i] && !code[i].isEmpty() && code[i].matches(Regex(\"^[a-zA-Z0-9_]+$\"\
        )) && businessLine[i] in priority) {\n            validCoupons.add(Pair(businessLine[i],\
        \ code[i]))\n        }\n    }\n    validCoupons.sortBy { (businessLine, code)\
        \ ->\n        Pair(priority[businessLine] ?: Int.MAX_VALUE, code)\n    }\n \
        \   return validCoupons.map { it.second }.toTypedArray()\n}"
      dart: "List<String> validateCoupons(List<String> code, List<String> businessLine,\
        \ List<bool> isActive) {\n    List<List<String>> validCoupons = [];\n    Map<String,\
        \ int> priority = {\"electronics\": 0, \"grocery\": 1, \"pharmacy\": 2, \"restaurant\"\
        : 3};\n    for (int i = 0; i < code.length; i++) {\n        if (isActive[i]\
        \ && code[i].isNotEmpty && RegExp(r'^[a-zA-Z0-9_]+$').hasMatch(code[i]) && priority.containsKey(businessLine[i]))\
        \ {\n            validCoupons.add([businessLine[i], code[i]]);\n        }\n\
        \    }\n    validCoupons.sort((a, b) {\n        if (priority[a[0]] == priority[b[0]])\
        \ {\n            return a[1].compareTo(b[1]);\n        }\n        return priority[a[0]]!.compareTo(priority[b[0]]!);\n\
        \    });\n    return validCoupons.map((coupon) => coupon[1]).toList();\n}"
      go: "package main\n\nimport (\n    \"fmt\"\n    \"regexp\"\n    \"sort\"\n)\n\n\
        type Coupon struct {\n    BusinessLine string\n    Code         string\n}\n\n\
        func validateCoupons(code []string, businessLine []string, isActive []bool)\
        \ []string {\n    validCoupons := []Coupon{}\n    priority := map[string]int{\n\
        \        \"electronics\": 0,\n        \"grocery\":    1,\n        \"pharmacy\"\
        :  2,\n        \"restaurant\": 3,\n    }\n    for i := range code {\n      \
        \  if isActive[i] && code[i] != \"\" && regexp.MustCompile(`^[a-zA-Z0-9_]+$`).MatchString(code[i])\
        \ && businessLine[i] != \"\" {\n            validCoupons = append(validCoupons,\
        \ Coupon{BusinessLine: businessLine[i], Code: code[i]})\n        }\n    }\n\
        \    sort.Slice(validCoupons, func(i, j int) bool {\n        if priority[validCoupons[i].BusinessLine]\
        \ == priority[validCoupons[j].BusinessLine] {\n            return validCoupons[i].Code\
        \ < validCoupons[j].Code\n        }\n        return priority[validCoupons[i].BusinessLine]\
        \ < priority[validCoupons[j].BusinessLine]\n    })\n    result := []string{}\n\
        \    for _, coupon := range validCoupons {\n        result = append(result,\
        \ coupon.Code)\n    }\n    return result\n}"
      ruby: "def validate_coupons(code, business_line, is_active)\n    valid_coupons\
        \ = []\n    priority = {\"electronics\" => 0, \"grocery\" => 1, \"pharmacy\"\
        \ => 2, \"restaurant\" => 3}\n    code.each_with_index do |c, i|\n        if\
        \ is_active[i] && !c.empty? && c =~ /^[a-zA-Z0-9_]+$/ && priority.key?(business_line[i])\n\
        \            valid_coupons << [business_line[i], c]\n        end\n    end\n\
        \    valid_coupons.sort_by! { |a| [priority[a[0]], a[1]] }\n    valid_coupons.map\
        \ { |c| c[1] }\nend"
      scala: "object Solution {\n    def validateCoupons(code: Array[String], businessLine:\
        \ Array[String], isActive: Array[Boolean]): Array[String] = {\n        val validCoupons\
        \ = code.zip(businessLine).zip(isActive).filter { case ((code, businessLine),\
        \ isActive) =>\n            isActive && !code.isEmpty && code.matches(\"^[a-zA-Z0-9_]+$\"\
        ) && businessLine.matches(\"^(electronics|grocery|pharmacy|restaurant)$\")\n\
        \        }.map { case ((code, businessLine), _) => (businessLine, code) }\n\
        \        val priority = Map(\"electronics\" -> 0, \"grocery\" -> 1, \"pharmacy\"\
        \ -> 2, \"restaurant\" -> 3)\n        validCoupons.sortBy { case (businessLine,\
        \ code) => (priority(businessLine), code) }.map { case (_, code) => code }\n\
        \    }\n}"
      rust: "use std::collections::HashMap;\n\nstruct Solution;\nimpl Solution {\n \
        \   pub fn validate_coupons(code: Vec<String>, business_line: Vec<String>, is_active:\
        \ Vec<bool>) -> Vec<String> {\n        let mut valid_coupons: Vec<(String, String)>\
        \ = Vec::new();\n        let priority: HashMap<String, i32> = [\n          \
        \  (\"electronics\".to_string(), 0),\n            (\"grocery\".to_string(),\
        \ 1),\n            (\"pharmacy\".to_string(), 2),\n            (\"restaurant\"\
        .to_string(), 3),\n        ].iter().cloned().collect();\n        for i in 0..code.len()\
        \ {\n            if is_active[i] && !code[i].is_empty() && code[i].chars().all(|c|\
        \ c.is_alphanumeric() || c == '_') && priority.contains_key(&business_line[i])\
        \ {\n                valid_coupons.push((business_line[i].clone(), code[i].clone()));\n\
        \            }\n        }\n        valid_coupons.sort_by(|a, b| {\n        \
        \    if priority[a.0] == priority[b.0] {\n                a.1.cmp(&b.1)\n  \
        \          } else {\n                priority[a.0].cmp(&priority[b.0])\n   \
        \         }\n        });\n        valid_coupons.into_iter().map(|(_, code)|\
        \ code).collect()\n    }\n}"
      racket: "(define (validate-coupons code business-line is-active)\n    (let (\n\
        \        (valid-coupons '())\n        (priority (hash \"electronics\" 0 \"grocery\"\
        \ 1 \"pharmacy\" 2 \"restaurant\" 3))\n        )\n        (for ((i (range (length\
        \ code))))\n            (when (and (list-ref is-active i) (not (string=? (list-ref\
        \ code i) \"\"))\n                       (regexp-match #rx\"^[a-zA-Z0-9_]+$\"\
        \ (list-ref code i))\n                       (hash-ref priority (list-ref business-line\
        \ i) #f))\n                (set! valid-coupons (cons (list (list-ref business-line\
        \ i) (list-ref code i)) valid-coupons)))\n            )\n        (sort valid-coupons\
        \ (lambda (a b)\n            (let (\n                (pa (hash-ref priority\
        \ (car a) +inf.0))\n                (pb (hash-ref priority (car b) +inf.0))\n\
        \                )\n                (if (= pa pb)\n                    (string<?\
        \ (cadr a) (cadr b))\n                    (< pa pb))\n                )\n  \
        \          )\n        )\n        (map cadr valid-coupons)\n        )\n    )"
      erlang: "validate_coupons(Code, BusinessLine, IsActive) ->\n    ValidCoupons =\
        \ [\n        {Business, C} ||\n            {C, Business} <- lists:zip(Code,\
        \ BusinessLine),\n            {true, Active} <- [{IsActive, true}],\n      \
        \      Active,\n            C =/= [],\n            re:run(C, \"^[a-zA-Z0-9_]+$\"\
        ) =/= nomatch,\n            lists:member(Business, [\"electronics\", \"grocery\"\
        , \"pharmacy\", \"restaurant\"])\n        ],\n    Priority = #{\n        \"\
        electronics\" => 0,\n        \"grocery\" => 1,\n        \"pharmacy\" => 2,\n\
        \        \"restaurant\" => 3\n    },\n    lists:sort(\n        fun({BusinessA,\
        \ CodeA}, {BusinessB, CodeB}) ->\n            case maps:get(BusinessA, Priority)\
        \ of\n                PrioA when PrioA =:= maps:get(BusinessB, Priority) ->\n\
        \                    CodeA =< CodeB;\n                PrioA ->\n           \
        \         PrioA =< maps:get(BusinessB, Priority)\n            end\n        end,\n\
        \        ValidCoupons\n    )."
      elixir: "def validate_coupons(code, business_line, is_active) do\n    valid_coupons\
        \ = Enum.zip(code, business_line)\n    |> Enum.with_index()\n    |> Enum.filter(fn\
        \ {_, index} -> Enum.at(is_active, index) and String.match?(Enum.at(code, index),\
        \ ~r/^[a-zA-Z0-9_]+$/)\n                                  and Enum.at(business_line,\
        \ index) in [\"electronics\", \"grocery\", \"pharmacy\", \"restaurant\"] end)\n\
        \    |> Enum.map(fn {code, business_line} -> {business_line, code} end)\n  \
        \  priority = %{\n        \"electronics\" => 0,\n        \"grocery\" => 1,\n\
        \        \"pharmacy\" => 2,\n        \"restaurant\" => 3\n    }\n    Enum.sort(valid_coupons,\
        \ fn {business_line_a, code_a}, {business_line_b, code_b} ->\n        if Map.get(priority,\
        \ business_line_a) == Map.get(priority, business_line_b) do\n            code_a\
        \ <= code_b\n        else\n            Map.get(priority, business_line_a) <=\
        \ Map.get(priority, business_line_b)\n        end\n    end)\n    |> Enum.map(fn\
        \ {_, code} -> code end)\nend"
    approach: The algorithm starts by filtering out any coupon where isActive is false,
      code is empty or contains non-alphanumeric/underscore characters, or businessLine
      is not in the allowed set. It then stores each remaining coupon as a pair (businessLine,
      code). A priority map is defined to map businessLine to a priority value, which
      is used for sorting. The list of pairs is sorted by (priority[businessLine], code)
      and the code values are returned in order. The key intuition is to use a priority
      map to efficiently sort the coupons by businessLine and then by code.
    time_complexity: The time complexity is O(n log n) due to the sorting operation,
      where n is the number of coupons. The filtering and storing operations take O(n)
      time, but the sorting operation dominates the time complexity.
    space_complexity: The space complexity is O(n) as we need to store the filtered
      coupons and the priority map. The space required does not grow exponentially with
      the input size, so it is linear.
    elapsed_time: 13.519142150878906
    model: llama-3.3-70b-versatile
    generated_at: '2025-12-13 01:04:21 '
---

## Problem #3606: Coupon Code Validator

**Difficulty:** Easy

**Topics:** Array, Hash Table, String, Sorting

## Problem Description

<p>You are given three arrays of length <code>n</code> that describe the properties of <code>n</code> coupons: <code>code</code>, <code>businessLine</code>, and <code>isActive</code>. The <code>i<sup>th</sup> </code>coupon has:</p>

<ul>
	<li><code>code[i]</code>: a <strong>string</strong> representing the coupon identifier.</li>
	<li><code>businessLine[i]</code>: a <strong>string</strong> denoting the business category of the coupon.</li>
	<li><code>isActive[i]</code>: a <strong>boolean</strong> indicating whether the coupon is currently active.</li>
</ul>

<p>A coupon is considered <strong>valid</strong> if all of the following conditions hold:</p>

<ol>
	<li><code>code[i]</code> is non-empty and consists only of alphanumeric characters (a-z, A-Z, 0-9) and underscores (<code>_</code>).</li>
	<li><code>businessLine[i]</code> is one of the following four categories: <code>&quot;electronics&quot;</code>, <code>&quot;grocery&quot;</code>, <code>&quot;pharmacy&quot;</code>, <code>&quot;restaurant&quot;</code>.</li>
	<li><code>isActive[i]</code> is <strong>true</strong>.</li>
</ol>

<p>Return an array of the <strong>codes</strong> of all valid coupons, <strong>sorted</strong> first by their <strong>businessLine</strong> in the order: <code>&quot;electronics&quot;</code>, <code>&quot;grocery&quot;</code>, <code>&quot;pharmacy&quot;, &quot;restaurant&quot;</code>, and then by <strong>code</strong> in lexicographical (ascending) order within each category.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">code = [&quot;SAVE20&quot;,&quot;&quot;,&quot;PHARMA5&quot;,&quot;SAVE@20&quot;], businessLine = [&quot;restaurant&quot;,&quot;grocery&quot;,&quot;pharmacy&quot;,&quot;restaurant&quot;], isActive = [true,true,true,true]</span></p>

<p><strong>Output:</strong> <span class="example-io">[&quot;PHARMA5&quot;,&quot;SAVE20&quot;]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>First coupon is valid.</li>
	<li>Second coupon has empty code (invalid).</li>
	<li>Third coupon is valid.</li>
	<li>Fourth coupon has special character <code>@</code> (invalid).</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">code = [&quot;GROCERY15&quot;,&quot;ELECTRONICS_50&quot;,&quot;DISCOUNT10&quot;], businessLine = [&quot;grocery&quot;,&quot;electronics&quot;,&quot;invalid&quot;], isActive = [false,true,true]</span></p>

<p><strong>Output:</strong> <span class="example-io">[&quot;ELECTRONICS_50&quot;]</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>First coupon is inactive (invalid).</li>
	<li>Second coupon is valid.</li>
	<li>Third coupon has invalid business line (invalid).</li>
</ul>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == code.length == businessLine.length == isActive.length</code></li>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>0 &lt;= code[i].length, businessLine[i].length &lt;= 100</code></li>
	<li><code>code[i]</code> and <code>businessLine[i]</code> consist of printable ASCII characters.</li>
	<li><code>isActive[i]</code> is either <code>true</code> or <code>false</code>.</li>
</ul>


## Hints

1. Filter out any coupon where `isActive[i]` is false, `code[i]` is empty or contains non‑alphanumeric/underscore chars, or `businessLine[i]` is not in the allowed set

2. Store each remaining coupon as a pair `(businessLine[i], code[i])`

3. Define a priority map, e.g. `{"electronics":0, "grocery":1, "pharmacy":2, "restaurant":3}`

4. Sort the list of pairs by `(priority[businessLine], code)` and return the `code` values in order

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-12-13 01:04:07 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The solution involves a two-phase process: filtering and sorting. First, we iterate through all coupons, applying the three validation rules. For each coupon, we check if it is active, if its business line is one of the four allowed categories, and if its code is non-empty and consists only of alphanumeric characters and underscores. If a coupon satisfies all conditions, we store its business line and code as a pair in a temporary list. To facilitate sorting by business line, we use a predefined map that assigns an integer priority to each valid business line (e.g., "electronics" -> 0, "grocery" -> 1, etc.).

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
#include <string>
#include <map>
#include <algorithm>
#include <cctype>

class Solution {
public:
    // Helper function to check if a code is valid
    bool isValidCode(const std::string& s) {
        if (s.empty()) {
            return false;
        }
        for (char c : s) {
            if (!std::isalnum(static_cast<unsigned char>(c)) && c != '_') {
                return false;
            }
        }
        return true;
    }

    std::vector<std::string> validateCoupons(std::vector<std::string>& code, std::vector<std::string>& businessLine, std::vector<bool>& isActive) {
        std::map<std::string, int> businessLinePriorities = {
            {"electronics", 0},
            {"grocery", 1},
            {"pharmacy", 2},
            {"restaurant", 3}
        };

        std::vector<std::pair<std::string, std::string>> validCoupons;
        int n = code.size();

        for (int i = 0; i < n; ++i) {
            // Condition 3: isActive[i] is true
            if (!isActive[i]) {
                continue;
            }

            // Condition 2: businessLine[i] is one of the four categories
            if (businessLinePriorities.find(businessLine[i]) == businessLinePriorities.end()) {
                continue;
            }

            // Condition 1: code[i] is non-empty and consists only of alphanumeric characters and underscores
            if (!isValidCode(code[i])) {
                continue;
            }

            // If all conditions pass, add to validCoupons list
            validCoupons.push_back({businessLine[i], code[i]});
        }

        // Sort validCoupons
        std::sort(validCoupons.begin(), validCoupons.end(), 
            [&](const std::pair<std::string, std::string>& a, const std::pair<std::string, std::string>& b) {
                int priorityA = businessLinePriorities[a.first];
                int priorityB = businessLinePriorities[b.first];
                if (priorityA != priorityB) {
                    return priorityA < priorityB;
                }
                return a.second < b.second; // Lexicographical sort by code
            }
        );

        // Extract and return codes
        std::vector<std::string> result;
        for (const auto& coupon : validCoupons) {
            result.push_back(coupon.second);
        }

        return result;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.regex.Pattern;

class Solution {
    // Pattern for alphanumeric and underscore characters
    private static final Pattern CODE_PATTERN = Pattern.compile("^[a-zA-Z0-9_]+$");

    // Helper class to store coupon data for sorting
    private static class CouponData {
        String businessLine;
        String code;
        int businessLinePriority;

        CouponData(String businessLine, String code, int businessLinePriority) {
            this.businessLine = businessLine;
            this.code = code;
            this.businessLinePriority = businessLinePriority;
        }
    }

    public List<String> validateCoupons(List<String> code, List<String> businessLine, List<Boolean> isActive) {
        Map<String, Integer> businessLinePriorities = new HashMap<>();
        businessLinePriorities.put("electronics", 0);
        businessLinePriorities.put("grocery", 1);
        businessLinePriorities.put("pharmacy", 2);
        businessLinePriorities.put("restaurant", 3);

        List<CouponData> validCoupons = new ArrayList<>();
        int n = code.size();

        for (int i = 0; i < n; i++) {
            // Condition 3: isActive[i] is true
            if (!isActive.get(i)) {
                continue;
            }

            // Condition 2: businessLine[i] is one of the four categories
            String currentBusinessLine = businessLine.get(i);
            if (!businessLinePriorities.containsKey(currentBusinessLine)) {
                continue;
            }
            int blPriority = businessLinePriorities.get(currentBusinessLine);

            // Condition 1: code[i] is non-empty and consists only of alphanumeric characters and underscores
            String currentCode = code.get(i);
            if (currentCode.isEmpty() || !CODE_PATTERN.matcher(currentCode).matches()) {
                continue;
            }

            // If all conditions pass, add to validCoupons list
            validCoupons.add(new CouponData(currentBusinessLine, currentCode, blPriority));
        }

        // Sort validCoupons
        Collections.sort(validCoupons, new Comparator<CouponData>() {
            @Override
            public int compare(CouponData a, CouponData b) {
                if (a.businessLinePriority != b.businessLinePriority) {
                    return Integer.compare(a.businessLinePriority, b.businessLinePriority);
                }
                return a.code.compareTo(b.code); // Lexicographical sort by code
            }
        });

        // Extract and return codes
        List<String> result = new ArrayList<>();
        for (CouponData coupon : validCoupons) {
            result.add(coupon.code);
        }

        return result;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
import re
from typing import List

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        valid_business_lines = {"electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3}

        valid_coupons = []
        n = len(code)

        for i in range(n):
            # Condition 3: isActive[i] is true
            if not isActive[i]:
                continue

            # Condition 2: businessLine[i] is one of the four categories
            current_business_line = businessLine[i]
            if current_business_line not in valid_business_lines:
                continue

            current_code = code[i]

            # Condition 1: code[i] is non-empty
            if not current_code:
                continue

            # Condition 1: code[i] consists only of alphanumeric characters and underscores
            if not re.fullmatch(r'^[a-zA-Z0-9_]+$', current_code):
                continue

            # If all conditions pass, add to valid_coupons list
            valid_coupons.append((current_business_line, current_code))

        # Sort valid_coupons
        # Sort first by businessLine priority, then by code lexicographically
        valid_coupons.sort(key=lambda x: (valid_business_lines[x[0]], x[1]))

        # Extract and return codes
        return [coupon_code for _, coupon_code in valid_coupons]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
import re
from typing import List

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        valid_business_lines = {"electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3}

        valid_coupons = []
        n = len(code)

        for i in range(n):
            # Condition 3: isActive[i] is true
            if not isActive[i]:
                continue

            # Condition 2: businessLine[i] is one of the four categories
            current_business_line = businessLine[i]
            if current_business_line not in valid_business_lines:
                continue

            current_code = code[i]

            # Condition 1: code[i] is non-empty
            if not current_code:
                continue

            # Condition 1: code[i] consists only of alphanumeric characters and underscores
            if not re.fullmatch(r'^[a-zA-Z0-9_]+$', current_code):
                continue

            # If all conditions pass, add to valid_coupons list
            valid_coupons.append((current_business_line, current_code))

        # Sort valid_coupons
        # Sort first by businessLine priority, then by code lexicographically
        valid_coupons.sort(key=lambda x: (valid_business_lines[x[0]], x[1]))

        # Extract and return codes
        return [coupon_code for _, coupon_code in valid_coupons]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <ctype.h> // For isalnum

// Helper struct to store valid coupon data
typedef struct {
    char* businessLine; // Not strictly needed for return, but useful for sorting logic
    char* code;
    int businessLinePriority;
} ValidCoupon;

// Helper function to check if a code is valid
bool isValidCode(const char* s) {
    if (s == NULL || s[0] == '\0') {
        return false;
    }
    for (int i = 0; s[i] != '\0'; i++) {
        if (!isalnum((unsigned char)s[i]) && s[i] != '_') {
            return false;
        }
    }
    return true;
}

// Helper function to get business line priority
int getBusinessLinePriority(const char* bl) {
    if (strcmp(bl, "electronics") == 0) return 0;
    if (strcmp(bl, "grocery") == 0) return 1;
    if (strcmp(bl, "pharmacy") == 0) return 2;
    if (strcmp(bl, "restaurant") == 0) return 3;
    return -1; // Invalid business line
}

// Comparison function for qsort
int compareCoupons(const void* a, const void* b) {
    ValidCoupon* couponA = *(ValidCoupon**)a;
    ValidCoupon* couponB = *(ValidCoupon**)b;

    // Sort by businessLine priority first
    if (couponA->businessLinePriority != couponB->businessLinePriority) {
        return couponA->businessLinePriority - couponB->businessLinePriority;
    }

    // Then sort by code lexicographically
    return strcmp(couponA->code, couponB->code);
}

char** validateCoupons(char** code, int codeSize, char** businessLine, int businessLineSize, bool* isActive, int isActiveSize, int* returnSize) {
    // Allocate a temporary array to store pointers to ValidCoupon structs
    ValidCoupon** temp_valid_coupons = (ValidCoupon**)malloc(codeSize * sizeof(ValidCoupon*));
    if (temp_valid_coupons == NULL) {
        *returnSize = 0;
        return NULL;
    }
    int valid_count = 0;

    for (int i = 0; i < codeSize; i++) {
        // Condition 3: isActive[i] is true
        if (!isActive[i]) {
            continue;
        }

        // Condition 2: businessLine[i] is one of the four categories
        int bl_priority = getBusinessLinePriority(businessLine[i]);
        if (bl_priority == -1) {
            continue;
        }

        // Condition 1: code[i] is non-empty and consists only of alphanumeric characters and underscores
        if (!isValidCode(code[i])) {
            continue;
        }

        // If all conditions pass, create a new ValidCoupon struct and add to list
        ValidCoupon* vc = (ValidCoupon*)malloc(sizeof(ValidCoupon));
        if (vc == NULL) {
            // Handle memory allocation failure: free previously allocated coupons
            for (int j = 0; j < valid_count; j++) {
                free(temp_valid_coupons[j]->businessLine);
                free(temp_valid_coupons[j]->code);
                free(temp_valid_coupons[j]);
            }
            free(temp_valid_coupons);
            *returnSize = 0;
            return NULL;
        }

        // Duplicate strings to ensure they persist beyond the input arrays' scope
        vc->businessLine = strdup(businessLine[i]);
        vc->code = strdup(code[i]);
        vc->businessLinePriority = bl_priority;

        temp_valid_coupons[valid_count++] = vc;
    }

    // Sort the valid coupons using qsort
    qsort(temp_valid_coupons, valid_count, sizeof(ValidCoupon*), compareCoupons);

    // Prepare the result array of char*
    char** result = (char**)malloc(valid_count * sizeof(char*));
    if (result == NULL) {
        // Handle memory allocation failure: free all coupons
        for (int j = 0; j < valid_count; j++) {
            free(temp_valid_coupons[j]->businessLine);
            free(temp_valid_coupons[j]->code);
            free(temp_valid_coupons[j]);
        }
        free(temp_valid_coupons);
        *returnSize = 0;
        return NULL;
    }

    for (int i = 0; i < valid_count; i++) {
        result[i] = temp_valid_coupons[i]->code; // Transfer ownership of the code string to the result array
        // Free the businessLine string and the ValidCoupon struct itself
        free(temp_valid_coupons[i]->businessLine);
        free(temp_valid_coupons[i]);
    }
    free(temp_valid_coupons); // Free the array of pointers to ValidCoupon structs

    *returnSize = valid_count;
    return result;
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
using System.Text.RegularExpressions;

public class Solution {
    private static readonly Regex CodeRegex = new Regex("^[a-zA-Z0-9_]+$", RegexOptions.Compiled);

    public IList<string> ValidateCoupons(IList<string> code, IList<string> businessLine, IList<bool> isActive) {
        Dictionary<string, int> businessLinePriorities = new Dictionary<string, int> {
            {"electronics", 0},
            {"grocery", 1},
            {"pharmacy", 2},
            {"restaurant", 3}
        };

        List<(string BusinessLine, string Code, int Priority)> validCoupons = new List<(string, string, int)>();
        int n = code.Count;

        for (int i = 0; i < n; i++) {
            // Condition 3: isActive[i] is true
            if (!isActive[i]) {
                continue;
            }

            // Condition 2: businessLine[i] is one of the four categories
            string currentBusinessLine = businessLine[i];
            if (!businessLinePriorities.TryGetValue(currentBusinessLine, out int priority)) {
                continue;
            }

            // Condition 1: code[i] is non-empty and consists only of alphanumeric characters and underscores
            string currentCode = code[i];
            if (string.IsNullOrEmpty(currentCode) || !CodeRegex.IsMatch(currentCode)) {
                continue;
            }

            // If all conditions pass, add to validCoupons list
            validCoupons.Add((currentBusinessLine, currentCode, priority));
        }

        // Sort validCoupons
        validCoupons.Sort((a, b) => {
            int priorityComparison = a.Priority.CompareTo(b.Priority);
            if (priorityComparison != 0) {
                return priorityComparison;
            }
            return string.Compare(a.Code, b.Code, StringComparison.Ordinal); // Lexicographical sort by code
        });

        // Extract and return codes
        return validCoupons.Select(c => c.Code).ToList();
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {string[]} code
 * @param {string[]} businessLine
 * @param {boolean[]} isActive
 * @return {string[]}
 */
var validateCoupons = function(code, businessLine, isActive) {
    const businessLinePriorities = {
        "electronics": 0,
        "grocery": 1,
        "pharmacy": 2,
        "restaurant": 3
    };

    const codeRegex = /^[a-zA-Z0-9_]+$/;

    const validCoupons = [];
    const n = code.length;

    for (let i = 0; i < n; i++) {
        // Condition 3: isActive[i] is true
        if (!isActive[i]) {
            continue;
        }

        // Condition 2: businessLine[i] is one of the four categories
        const currentBusinessLine = businessLine[i];
        if (!(currentBusinessLine in businessLinePriorities)) {
            continue;
        }
        const priority = businessLinePriorities[currentBusinessLine];

        // Condition 1: code[i] is non-empty and consists only of alphanumeric characters and underscores
        const currentCode = code[i];
        if (!currentCode || !codeRegex.test(currentCode)) {
            continue;
        }

        // If all conditions pass, add to validCoupons list
        validCoupons.push({ businessLine: currentBusinessLine, code: currentCode, priority: priority });
    }

    // Sort validCoupons
    validCoupons.sort((a, b) => {
        if (a.priority !== b.priority) {
            return a.priority - b.priority;
        }
        return a.code.localeCompare(b.code); // Lexicographical sort by code
    });

    // Extract and return codes
    return validCoupons.map(coupon => coupon.code);
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function validateCoupons(code: string[], businessLine: string[], isActive: boolean[]): string[] {
    const businessLinePriorities: { [key: string]: number } = {
        "electronics": 0,
        "grocery": 1,
        "pharmacy": 2,
        "restaurant": 3
    };

    const codeRegex = /^[a-zA-Z0-9_]+$/;

    interface CouponData {
        businessLine: string;
        code: string;
        priority: number;
    }

    const validCoupons: CouponData[] = [];
    const n = code.length;

    for (let i = 0; i < n; i++) {
        // Condition 3: isActive[i] is true
        if (!isActive[i]) {
            continue;
        }

        // Condition 2: businessLine[i] is one of the four categories
        const currentBusinessLine = businessLine[i];
        if (!(currentBusinessLine in businessLinePriorities)) {
            continue;
        }
        const priority = businessLinePriorities[currentBusinessLine];

        // Condition 1: code[i] is non-empty and consists only of alphanumeric characters and underscores
        const currentCode = code[i];
        if (!currentCode || !codeRegex.test(currentCode)) {
            continue;
        }

        // If all conditions pass, add to validCoupons list
        validCoupons.push({ businessLine: currentBusinessLine, code: currentCode, priority: priority });
    }

    // Sort validCoupons
    validCoupons.sort((a, b) => {
        if (a.priority !== b.priority) {
            return a.priority - b.priority;
        }
        return a.code.localeCompare(b.code); // Lexicographical sort by code
    });

    // Extract and return codes
    return validCoupons.map(coupon => coupon.code);
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
<?php
class Solution {

    /**
     * @param String[] $code
     * @param String[] $businessLine
     * @param Boolean[] $isActive
     * @return String[]
     */
    function validateCoupons($code, $businessLine, $isActive) {
        $businessLinePriorities = [
            "electronics" => 0,
            "grocery" => 1,
            "pharmacy" => 2,
            "restaurant" => 3
        ];

        $validCoupons = [];
        $n = count($code);

        for ($i = 0; $i < $n; $i++) {
            // Condition 3: isActive[i] is true
            if (!$isActive[$i]) {
                continue;
            }

            // Condition 2: businessLine[i] is one of the four categories
            $currentBusinessLine = $businessLine[$i];
            if (!isset($businessLinePriorities[$currentBusinessLine])) {
                continue;
            }
            $priority = $businessLinePriorities[$currentBusinessLine];

            // Condition 1: code[i] is non-empty and consists only of alphanumeric characters and underscores
            $currentCode = $code[$i];
            if (empty($currentCode) || !preg_match('/^[a-zA-Z0-9_]+$/', $currentCode)) {
                continue;
            }

            // If all conditions pass, add to validCoupons list
            $validCoupons[] = ['businessLine' => $currentBusinessLine, 'code' => $currentCode, 'priority' => $priority];
        }

        // Sort validCoupons
        usort($validCoupons, function($a, $b) {
            if ($a['priority'] !== $b['priority']) {
                return $a['priority'] - $b['priority'];
            }
            return strcmp($a['code'], $b['code']); // Lexicographical sort by code
        });

        // Extract and return codes
        $result = [];
        foreach ($validCoupons as $coupon) {
            $result[] = $coupon['code'];
        }

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
    func validateCoupons(_ code: [String], _ businessLine: [String], _ isActive: [Bool]) -> [String] {
        let businessLinePriorities: [String: Int] = [
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3
        ]

        struct CouponData {
            let businessLine: String
            let code: String
            let priority: Int
        }

        var validCoupons: [CouponData] = []
        let n = code.count

        for i in 0..<n {
            // Condition 3: isActive[i] is true
            if !isActive[i] {
                continue
            }

            // Condition 2: businessLine[i] is one of the four categories
            let currentBusinessLine = businessLine[i]
            guard let priority = businessLinePriorities[currentBusinessLine] else {
                continue
            }

            // Condition 1: code[i] is non-empty and consists only of alphanumeric characters and underscores
            let currentCode = code[i]
            if currentCode.isEmpty || currentCode.range(of: "^[a-zA-Z0-9_]+$", options: .regularExpression) == nil {
                continue
            }

            // If all conditions pass, add to validCoupons list
            validCoupons.append(CouponData(businessLine: currentBusinessLine, code: currentCode, priority: priority))
        }

        // Sort validCoupons
        validCoupons.sort { (a, b) in
            if a.priority != b.priority {
                return a.priority < b.priority
            }
            return a.code < b.code // Lexicographical sort by code
        }

        // Extract and return codes
        return validCoupons.map { $0.code }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {
    fun validateCoupons(code: List<String>, businessLine: List<String>, isActive: List<Boolean>): List<String> {
        val businessLinePriorities = mapOf(
            "electronics" to 0,
            "grocery" to 1,
            "pharmacy" to 2,
            "restaurant" to 3
        )

        data class CouponData(
            val businessLine: String,
            val code: String,
            val priority: Int
        )

        val validCoupons = mutableListOf<CouponData>()
        val n = code.size

        for (i in 0 until n) {
            // Condition 3: isActive[i] is true
            if (!isActive[i]) {
                continue
            }

            // Condition 2: businessLine[i] is one of the four categories
            val currentBusinessLine = businessLine[i]
            val priority = businessLinePriorities[currentBusinessLine]
            if (priority == null) {
                continue
            }

            // Condition 1: code[i] is non-empty and consists only of alphanumeric characters and underscores
            val currentCode = code[i]
            if (currentCode.isEmpty() || !currentCode.matches(Regex("^[a-zA-Z0-9_]+$"))) {
                continue
            }

            // If all conditions pass, add to validCoupons list
            validCoupons.add(CouponData(currentBusinessLine, currentCode, priority))
        }

        // Sort validCoupons
        validCoupons.sortWith(Comparator {
            a, b ->
            val priorityComparison = a.priority.compareTo(b.priority)
            if (priorityComparison != 0) {
                priorityComparison
            } else {
                a.code.compareTo(b.code) // Lexicographical sort by code
            }
        })

        // Extract and return codes
        return validCoupons.map { it.code }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {
  List<String> validateCoupons(List<String> code, List<String> businessLine, List<bool> isActive) {
    final Map<String, int> businessLinePriorities = {
      "electronics": 0,
      "grocery": 1,
      "pharmacy": 2,
      "restaurant": 3
    };

    final RegExp codeRegex = RegExp(r'^[a-zA-Z0-9_]+$');

    final List<({String businessLine, String code, int priority})> validCoupons = [];
    final int n = code.length;

    for (int i = 0; i < n; i++) {
      // Condition 3: isActive[i] is true
      if (!isActive[i]) {
        continue;
      }

      // Condition 2: businessLine[i] is one of the four categories
      final String currentBusinessLine = businessLine[i];
      final int? priority = businessLinePriorities[currentBusinessLine];
      if (priority == null) {
        continue;
      }

      // Condition 1: code[i] is non-empty and consists only of alphanumeric characters and underscores
      final String currentCode = code[i];
      if (currentCode.isEmpty || !codeRegex.hasMatch(currentCode)) {
        continue;
      }

      // If all conditions pass, add to validCoupons list
      validCoupons.add((businessLine: currentBusinessLine, code: currentCode, priority: priority));
    }

    // Sort validCoupons
    validCoupons.sort((a, b) {
      final int priorityComparison = a.priority.compareTo(b.priority);
      if (priorityComparison != 0) {
        return priorityComparison;
      }
      return a.code.compareTo(b.code); // Lexicographical sort by code
    });

    // Extract and return codes
    return validCoupons.map((coupon) => coupon.code).toList();
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import (
	"regexp"
	"sort"
)

// CouponData struct to hold coupon information for sorting
type CouponData struct {
	BusinessLine string
	Code         string
	Priority     int
}

var codeRegex = regexp.MustCompile("^[a-zA-Z0-9_]+$")

func validateCoupons(code []string, businessLine []string, isActive []bool) []string {
	businessLinePriorities := map[string]int{
		"electronics": 0,
		"grocery":     1,
		"pharmacy":    2,
		"restaurant":  3,
	}

	var validCoupons []CouponData
	n := len(code)

	for i := 0; i < n; i++ {
		// Condition 3: isActive[i] is true
		if !isActive[i] {
			continue
		}

		// Condition 2: businessLine[i] is one of the four categories
		currentBusinessLine := businessLine[i]
		priority, exists := businessLinePriorities[currentBusinessLine]
		if !exists {
			continue
		}

		// Condition 1: code[i] is non-empty and consists only of alphanumeric characters and underscores
		currentCode := code[i]
		if currentCode == "" || !codeRegex.MatchString(currentCode) {
			continue
		}

		// If all conditions pass, add to validCoupons list
		validCoupons = append(validCoupons, CouponData{
			BusinessLine: currentBusinessLine,
			Code:         currentCode,
			Priority:     priority,
		})
	}

	// Sort validCoupons
	sort.Slice(validCoupons, func(i, j int) bool {
		if validCoupons[i].Priority != validCoupons[j].Priority {
			return validCoupons[i].Priority < validCoupons[j].Priority
		}
		return validCoupons[i].Code < validCoupons[j].Code // Lexicographical sort by code
	})

	// Extract and return codes
	result := make([]string, len(validCoupons))
	for i, coupon := range validCoupons {
		result[i] = coupon.Code
	}

	return result
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
class Solution
    # @param {String[]} code
    # @param {String[]} business_line
    # @param {Boolean[]} is_active
    # @return {String[]}
    def validate_coupons(code, business_line, is_active)
        business_line_priorities = {
            "electronics" => 0,
            "grocery" => 1,
            "pharmacy" => 2,
            "restaurant" => 3
        }

        code_regex = /^[a-zA-Z0-9_]+$/

        valid_coupons = []
        n = code.length

        (0...n).each do |i|
            # Condition 3: is_active[i] is true
            next unless is_active[i]

            # Condition 2: business_line[i] is one of the four categories
            current_business_line = business_line[i]
            priority = business_line_priorities[current_business_line]
            next if priority.nil?

            # Condition 1: code[i] is non-empty and consists only of alphanumeric characters and underscores
            current_code = code[i]
            next if current_code.empty? || !(current_code =~ code_regex)

            # If all conditions pass, add to valid_coupons list
            valid_coupons << { business_line: current_business_line, code: current_code, priority: priority }
        end

        # Sort valid_coupons
        valid_coupons.sort! do |a, b|
            priority_comparison = a[:priority] <=> b[:priority]
            if priority_comparison != 0
                priority_comparison
            else
                a[:code] <=> b[:code] # Lexicographical sort by code
            end
        end

        # Extract and return codes
        valid_coupons.map { |coupon| coupon[:code] }
    end
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
import scala.collection.mutable.ListBuffer

class Solution {
    def validateCoupons(code: List[String], businessLine: List[String], isActive: List[Boolean]): List[String] = {
        val businessLinePriorities: Map[String, Int] = Map(
            "electronics" -> 0,
            "grocery" -> 1,
            "pharmacy" -> 2,
            "restaurant" -> 3
        )

        case class CouponData(
            businessLine: String,
            code: String,
            priority: Int
        )

        val codeRegex = "^[a-zA-Z0-9_]+$".r

        val validCoupons = ListBuffer[CouponData]()
        val n = code.length

        for (i <- 0 until n) {
            // Condition 3: isActive(i) is true
            if (!isActive(i)) {
                // continue
            } else {
                // Condition 2: businessLine(i) is one of the four categories
                val currentBusinessLine = businessLine(i)
                val priority = businessLinePriorities.get(currentBusinessLine)
                if (priority.isEmpty) {
                    // continue
                } else {
                    // Condition 1: code(i) is non-empty and consists only of alphanumeric characters and underscores
                    val currentCode = code(i)
                    if (currentCode.isEmpty || codeRegex.findFirstIn(currentCode).isEmpty) {
                        // continue
                    } else {
                        // If all conditions pass, add to validCoupons list
                        validCoupons += CouponData(currentBusinessLine, currentCode, priority.get)
                    }
                }
            }
        }

        // Sort validCoupons
        val sortedCoupons = validCoupons.sortBy(coupon => (coupon.priority, coupon.code))

        // Extract and return codes
        sortedCoupons.map(_.code).toList
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn validate_coupons(code: Vec<String>, business_line: Vec<String>, is_active: Vec<bool>) -> Vec<String> {
        use std::collections::HashMap;

        let business_line_priorities: HashMap<String, i32> = [
            ("electronics".to_string(), 0),
            ("grocery".to_string(), 1),
            ("pharmacy".to_string(), 2),
            ("restaurant".to_string(), 3),
        ].iter().cloned().collect();

        #[derive(Debug, PartialEq, Eq, PartialOrd, Ord)]
        struct CouponData {
            priority: i32,
            code: String,
            business_line: String, // Not strictly needed for sorting, but good for completeness
        }

        let mut valid_coupons: Vec<CouponData> = Vec::new();
        let n = code.len();

        for i in 0..n {
            // Condition 3: is_active[i] is true
            if !is_active[i] {
                continue;
            }

            // Condition 2: business_line[i] is one of the four categories
            let current_business_line = &business_line[i];
            let Some(&priority) = business_line_priorities.get(current_business_line) else {
                continue;
            };

            // Condition 1: code[i] is non-empty and consists only of alphanumeric characters and underscores
            let current_code = &code[i];
            if current_code.is_empty() || !current_code.chars().all(|c| c.is_ascii_alphanumeric() || c == '_') {
                continue;
            }

            // If all conditions pass, add to valid_coupons list
            valid_coupons.push(CouponData {
                business_line: current_business_line.clone(),
                code: current_code.clone(),
                priority,
            });
        }

        // Sort valid_coupons
        valid_coupons.sort_unstable(); // Uses the derived Ord trait for sorting

        // Extract and return codes
        valid_coupons.into_iter().map(|coupon| coupon.code).collect()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket

(provide (rename-out [validate-coupons validateCoupons]))

(define (validate-coupons code businessLine isActive)
  (define business-line-priorities
    (hash
     "electronics" 0
     "grocery" 1
     "pharmacy" 2
     "restaurant" 3))

  (define (valid-code? s)
    (and (not (string-empty? s))
         (regexp-match? #rx"^[a-zA-Z0-9_]+$" s)))

  (define valid-coupons (make-list-buffer))
  (define n (vector-length code))

  (for ([i (in-range n)])
    (when (vector-ref isActive i)
      (define current-business-line (vector-ref businessLine i))
      (define priority (hash-ref business-line-priorities current-business-line #f))
      (when priority
        (define current-code (vector-ref code i))
        (when (valid-code? current-code)
          (add-to-list-buffer! valid-coupons (list current-business-line current-code priority))))))

  (define sorted-coupons
    (sort (list-buffer->list valid-coupons)
          (lambda (a b)
            (define priority-a (list-ref a 2))
            (define priority-b (list-ref b 2))
            (if (not (= priority-a priority-b))
                (< priority-a priority-b)
                (string<? (list-ref a 1) (list-ref b 1))))))

  (map (lambda (coupon) (list-ref coupon 1)) sorted-coupons))

;; Helper for mutable list (not standard Racket, but common in competitive programming contexts)
(struct list-buffer (lst tail) #:mutable #t)
(define (make-list-buffer) (list-buffer '() '()))
(define (add-to-list-buffer! lb item)
  (if (null? (list-buffer-lst lb))
      (begin
        (set-list-buffer-lst! lb (list item))
        (set-list-buffer-tail! lb (list-buffer-lst lb)))
      (begin
        (set-cdr! (list-buffer-tail lb) (list item))
        (set-list-buffer-tail! lb (cdr (list-buffer-tail lb))))))
(define (list-buffer->list lb) (list-buffer-lst lb))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([validateCoupons/3]).

validateCoupons(Code, BusinessLine, IsActive) ->
    BusinessLinePriorities = #{"electronics" => 0, "grocery" => 1, "pharmacy" => 2, "restaurant" => 3},
    CodeRegex = re:compile("^[a-zA-Z0-9_]+$"),

    N = length(Code),
    Indices = lists:seq(0, N - 1),

    ValidCoupons = lists:foldl(
        fun(I, Acc) ->
            CurrentIsActive = lists:nth(I + 1, IsActive),
            CurrentBusinessLine = lists:nth(I + 1, BusinessLine),
            CurrentCode = lists:nth(I + 1, Code),

            % Condition 3: IsActive[i] is true
            case CurrentIsActive of
                true ->
                    % Condition 2: BusinessLine[i] is one of the four categories
                    case maps:get(CurrentBusinessLine, BusinessLinePriorities, undefined) of
                        undefined -> Acc;
                        Priority ->
                            % Condition 1: Code[i] is non-empty and consists only of alphanumeric characters and underscores
                            case CurrentCode =/= "" andalso re:run(CurrentCode, CodeRegex, [{return, binary}]) of
                                {match, _} ->
                                    [{Priority, CurrentCode} | Acc];
                                _ -> Acc
                            end
                    end;
                false -> Acc
            end
        end, [], Indices),

    % Sort validCoupons
    % Erlang's lists:sort sorts by the first element of a tuple, then the second, etc.
    SortedCoupons = lists:sort(ValidCoupons),

    % Extract and return codes
    lists:map(fun({_, CodeVal}) -> CodeVal end, SortedCoupons).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @business_line_priorities %{
    "electronics" => 0,
    "grocery" => 1,
    "pharmacy" => 2,
    "restaurant" => 3
  }

  @code_regex ~r/^[a-zA-Z0-9_]+$/

  @spec validate_coupons(code :: [String.t()], business_line :: [String.t()], is_active :: [boolean()]) :: [String.t()]
  def validate_coupons(code, business_line, is_active) do
    n = length(code)

    valid_coupons = Enum.reduce(0..(n - 1), [], fn i, acc ->
      current_is_active = Enum.at(is_active, i)
      current_business_line = Enum.at(business_line, i)
      current_code = Enum.at(code, i)

      # Condition 3: is_active[i] is true
      if current_is_active do
        # Condition 2: business_line[i] is one of the four categories
        case Map.fetch(@business_line_priorities, current_business_line) do
          {:ok, priority} ->
            # Condition 1: code[i] is non-empty and consists only of alphanumeric characters and underscores
            if current_code != "" and String.match?(current_code, @code_regex) do
              [{priority, current_code} | acc]
            else
              acc
            end
          :error ->
            acc
        end
      else
        acc
      end
    end)

    # Sort valid_coupons
    # Elixir's Enum.sort sorts tuples by their elements from left to right by default
    sorted_coupons = Enum.sort(valid_coupons)

    # Extract and return codes
    Enum.map(sorted_coupons, fn {_, code_val} -> code_val end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is O(N * L_max + K * log(K) * L_max), where N is the total number of coupons, L_max is the maximum length of a coupon code or business line string, and K is the number of valid coupons. The initial filtering loop iterates N times, and within each iteration, string validation (e.g., regex or character-by-character check) takes up to O(L_max) time. Storing valid coupons takes O(K * L_max) space. The sorting step involves K items, and each comparison takes O(L_max) time due to string comparisons, leading to O(K * log(K) * L_max) for sorting. In the worst case, K can be N.

- **Space Complexity:** The space complexity is O(K * L_max), where K is the number of valid coupons and L_max is the maximum length of a coupon code or business line string. This space is primarily used to store the list of valid coupons, where each coupon stores its business line and code. In the worst case, all N coupons are valid, resulting in O(N * L_max) space. The map for business line priorities uses O(1) space as it has a fixed number of entries.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-12-13 01:04:21 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The algorithm starts by filtering out any coupon where isActive is false, code is empty or contains non-alphanumeric/underscore characters, or businessLine is not in the allowed set. It then stores each remaining coupon as a pair (businessLine, code). A priority map is defined to map businessLine to a priority value, which is used for sorting. The list of pairs is sorted by (priority[businessLine], code) and the code values are returned in order. The key intuition is to use a priority map to efficiently sort the coupons by businessLine and then by code.

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
    vector<string> validateCoupons(vector<string>& code, vector<string>& businessLine, vector<bool>& isActive) {
        vector<pair<string, string>> validCoupons;
        unordered_map<string, int> priority = {"electronics", 0}, {"grocery", 1}, {"pharmacy", 2}, {"restaurant", 3}
        for (int i = 0; i < code.size(); i++) {
            if (isActive[i] && !code[i].empty()) {
                bool validCode = true;
                for (char c : code[i]) {
                    if (!isalnum(c) && c != '_') {
                        validCode = false;
                        break;
                    }
                }
                if (validCode && priority.find(businessLine[i]) != priority.end()) {
                    validCoupons.push_back({businessLine[i], code[i]});
                }
            }
        }
        sort(validCoupons.begin(), validCoupons.end(), [&](pair<string, string>& a, pair<string, string>& b) {
            if (priority[a.first] == priority[b.first]) {
                return a.second < b.second;
            }
            return priority[a.first] < priority[b.first];
        });
        vector<string> result;
        for (auto& coupon : validCoupons) {
            result.push_back(coupon.second);
        }
        return result;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.*;
public class Solution {
    public List<String> validateCoupons(String[] code, String[] businessLine, boolean[] isActive) {
        List<String[]> validCoupons = new ArrayList<>();
        Map<String, Integer> priority = new HashMap<>();
        priority.put("electronics", 0);
        priority.put("grocery", 1);
        priority.put("pharmacy", 2);
        priority.put("restaurant", 3);
        for (int i = 0; i < code.length; i++) {
            if (isActive[i] && !code[i].isEmpty()) {
                boolean validCode = true;
                for (char c : code[i].toCharArray()) {
                    if (!Character.isLetterOrDigit(c) && c != '_') {
                        validCode = false;
                        break;
                    }
                }
                if (validCode && priority.containsKey(businessLine[i])) {
                    validCoupons.add(new String[]{businessLine[i], code[i]});
                }
            }
        }
        Collections.sort(validCoupons, (a, b) -> {
            if (priority.get(a[0]).equals(priority.get(b[0]))) {
                return a[1].compareTo(b[1]);
            }
            return priority.get(a[0]) - priority.get(b[0]);
        });
        List<String> result = new ArrayList<>();
        for (String[] coupon : validCoupons) {
            result.add(coupon[1]);
        }
        return result;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def validateCoupons(self, code: list[str], businessLine: list[str], isActive: list[bool]) -> list[str]:
        validCoupons = []
        priority = {"electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3}
        for i in range(len(code)):
            if isActive[i] and code[i] and all(c.isalnum() or c == '_' for c in code[i]) and businessLine[i] in priority:
                validCoupons.append((businessLine[i], code[i]))
        validCoupons.sort(key=lambda x: (priority[x[0]], x[1]))
        return [coupon[1] for coupon in validCoupons]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def validateCoupons(self, code: list[str], businessLine: list[str], isActive: list[bool]) -> list[str]:
        validCoupons = []
        priority = {"electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3}
        for i in range(len(code)):
            if isActive[i] and code[i] and all(c.isalnum() or c == '_' for c in code[i]) and businessLine[i] in priority:
                validCoupons.append((businessLine[i], code[i]))
        validCoupons.sort(key=lambda x: (priority[x[0]], x[1]))
        return [coupon[1] for coupon in validCoupons]
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
typedef struct {
    char* businessLine;
    char* code;
} Coupon;

int compareCoupons(const void* a, const void* b) {
    Coupon* couponA = (Coupon*)a;
    Coupon* couponB = (Coupon*)b;
    int priorityA = 0, priorityB = 0;
    if (strcmp(couponA->businessLine, "electronics") == 0) priorityA = 0;
    else if (strcmp(couponA->businessLine, "grocery") == 0) priorityA = 1;
    else if (strcmp(couponA->businessLine, "pharmacy") == 0) priorityA = 2;
    else if (strcmp(couponA->businessLine, "restaurant") == 0) priorityA = 3;
    if (strcmp(couponB->businessLine, "electronics") == 0) priorityB = 0;
    else if (strcmp(couponB->businessLine, "grocery") == 0) priorityB = 1;
    else if (strcmp(couponB->businessLine, "pharmacy") == 0) priorityB = 2;
    else if (strcmp(couponB->businessLine, "restaurant") == 0) priorityB = 3;
    if (priorityA == priorityB) return strcmp(couponA->code, couponB->code);
    return priorityA - priorityB;
}

char** validateCoupons(char** code, char** businessLine, int* isActive, int codeSize, int* returnSize) {
    Coupon* validCoupons = (Coupon*)malloc(codeSize * sizeof(Coupon));
    int validCount = 0;
    for (int i = 0; i < codeSize; i++) {
        if (isActive[i] && code[i][0] != '\0') {
            int validCode = 1;
            for (char* c = code[i]; *c != '\0'; c++) {
                if (!isalnum(*c) && *c != '_') {
                    validCode = 0;
                    break;
                }
            }
            if (validCode && (strcmp(businessLine[i], "electronics") == 0 || strcmp(businessLine[i], "grocery") == 0 || strcmp(businessLine[i], "pharmacy") == 0 || strcmp(businessLine[i], "restaurant") == 0)) {
                validCoupons[validCount].businessLine = businessLine[i];
                validCoupons[validCount].code = code[i];
                validCount++;
            }
        }
    }
    qsort(validCoupons, validCount, sizeof(Coupon), compareCoupons);
    char** result = (char**)malloc(validCount * sizeof(char*));
    for (int i = 0; i < validCount; i++) {
        result[i] = validCoupons[i].code;
    }
    *returnSize = validCount;
    return result;
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
    public string[] ValidateCoupons(string[] code, string[] businessLine, bool[] isActive) {
        var validCoupons = new List<(string businessLine, string code)>();
        var priority = new Dictionary<string, int> { {"electronics", 0}, {"grocery", 1}, {"pharmacy", 2}, {"restaurant", 3} };
        for (int i = 0; i < code.Length; i++) {
            if (isActive[i] && !string.IsNullOrEmpty(code[i]) && code[i].All(c => char.IsLetterOrDigit(c) || c == '_') && priority.ContainsKey(businessLine[i])) {
                validCoupons.Add((businessLine[i], code[i]));
            }
        }
        validCoupons.Sort((a, b) => {
            if (priority[a.businessLine] == priority[b.businessLine]) {
                return string.Compare(a.code, b.code);
            }
            return priority[a.businessLine].CompareTo(priority[b.businessLine]);
        });
        return validCoupons.Select(c => c.code).ToArray();
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var validateCoupons = function(code, businessLine, isActive) {
    var validCoupons = [];
    var priority = {"electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3};
    for (var i = 0; i < code.length; i++) {
        if (isActive[i] && code[i] && /^[a-zA-Z0-9_]+$/.test(code[i]) && businessLine[i] in priority) {
            validCoupons.push([businessLine[i], code[i]]);
        }
    }
    validCoupons.sort(function(a, b) {
        if (priority[a[0]] == priority[b[0]]) {
            return a[1].localeCompare(b[1]);
        }
        return priority[a[0]] - priority[b[0]];
    });
    return validCoupons.map(function(coupon) {
        return coupon[1];
    });
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function validateCoupons(code: string[], businessLine: string[], isActive: boolean[]): string[] {
    const validCoupons: [string, string][] = [];
    const priority: { [key: string]: number } = {"electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3};
    for (let i = 0; i < code.length; i++) {
        if (isActive[i] && code[i] && /^[a-zA-Z0-9_]+$/.test(code[i]) && businessLine[i] in priority) {
            validCoupons.push([businessLine[i], code[i]]);
        }
    }
    validCoupons.sort((a, b) => {
        if (priority[a[0]] === priority[b[0]]) {
            return a[1].localeCompare(b[1]);
        }
        return priority[a[0]] - priority[b[0]];
    });
    return validCoupons.map(coupon => coupon[1]);
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
$validCoupons = [];
$priority = ["electronics" => 0, "grocery" => 1, "pharmacy" => 2, "restaurant" => 3];
foreach ($code as $i => $c) {
    if ($isActive[$i] && $c && preg_match('/^[a-zA-Z0-9_]+$/', $c) && array_key_exists($businessLine[$i], $priority)) {
        $validCoupons[] = [$businessLine[$i], $c];
    }
}
usort($validCoupons, function($a, $b) {
    if ($priority[$a[0]] == $priority[$b[0]]) {
        return strcmp($a[1], $b[1]);
    }
    return $priority[$a[0]] - $priority[$b[0]];
});
$result = array_map(function($coupon) {
    return $coupon[1];
}, $validCoupons);
return $result;
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
func validateCoupons(_ code: [String], _ businessLine: [String], _ isActive: [Bool]) -> [String] {
    var validCoupons: [(String, String)] = []
    let priority: [String: Int] = ["electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3]
    for i in 0..<code.count {
        if isActive[i] && !code[i].isEmpty && code[i].range(of: "^[a-zA-Z0-9_]+$", options: .regularExpression) != nil && priority[businessLine[i]] != nil {
            validCoupons.append((businessLine[i], code[i]))
        }
    }
    validCoupons.sort { (a, b) -> Bool in
        if priority[a.0] == priority[b.0] {
            return a.1 < b.1
        }
        return priority[a.0]! < priority[b.0]!
    }
    return validCoupons.map { $0.1 }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
fun validateCoupons(code: Array<String>, businessLine: Array<String>, isActive: BooleanArray): Array<String> {
    val validCoupons = mutableListOf<Pair<String, String>>()
    val priority = mapOf("electronics" to 0, "grocery" to 1, "pharmacy" to 2, "restaurant" to 3)
    for (i in code.indices) {
        if (isActive[i] && !code[i].isEmpty() && code[i].matches(Regex("^[a-zA-Z0-9_]+$")) && businessLine[i] in priority) {
            validCoupons.add(Pair(businessLine[i], code[i]))
        }
    }
    validCoupons.sortBy { (businessLine, code) ->
        Pair(priority[businessLine] ?: Int.MAX_VALUE, code)
    }
    return validCoupons.map { it.second }.toTypedArray()
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
List<String> validateCoupons(List<String> code, List<String> businessLine, List<bool> isActive) {
    List<List<String>> validCoupons = [];
    Map<String, int> priority = {"electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3};
    for (int i = 0; i < code.length; i++) {
        if (isActive[i] && code[i].isNotEmpty && RegExp(r'^[a-zA-Z0-9_]+$').hasMatch(code[i]) && priority.containsKey(businessLine[i])) {
            validCoupons.add([businessLine[i], code[i]]);
        }
    }
    validCoupons.sort((a, b) {
        if (priority[a[0]] == priority[b[0]]) {
            return a[1].compareTo(b[1]);
        }
        return priority[a[0]]!.compareTo(priority[b[0]]!);
    });
    return validCoupons.map((coupon) => coupon[1]).toList();
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
    "regexp"
    "sort"
)

type Coupon struct {
    BusinessLine string
    Code         string
}

func validateCoupons(code []string, businessLine []string, isActive []bool) []string {
    validCoupons := []Coupon{}
    priority := map[string]int{
        "electronics": 0,
        "grocery":    1,
        "pharmacy":  2,
        "restaurant": 3,
    }
    for i := range code {
        if isActive[i] && code[i] != "" && regexp.MustCompile(`^[a-zA-Z0-9_]+$`).MatchString(code[i]) && businessLine[i] != "" {
            validCoupons = append(validCoupons, Coupon{BusinessLine: businessLine[i], Code: code[i]})
        }
    }
    sort.Slice(validCoupons, func(i, j int) bool {
        if priority[validCoupons[i].BusinessLine] == priority[validCoupons[j].BusinessLine] {
            return validCoupons[i].Code < validCoupons[j].Code
        }
        return priority[validCoupons[i].BusinessLine] < priority[validCoupons[j].BusinessLine]
    })
    result := []string{}
    for _, coupon := range validCoupons {
        result = append(result, coupon.Code)
    }
    return result
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def validate_coupons(code, business_line, is_active)
    valid_coupons = []
    priority = {"electronics" => 0, "grocery" => 1, "pharmacy" => 2, "restaurant" => 3}
    code.each_with_index do |c, i|
        if is_active[i] && !c.empty? && c =~ /^[a-zA-Z0-9_]+$/ && priority.key?(business_line[i])
            valid_coupons << [business_line[i], c]
        end
    end
    valid_coupons.sort_by! { |a| [priority[a[0]], a[1]] }
    valid_coupons.map { |c| c[1] }
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def validateCoupons(code: Array[String], businessLine: Array[String], isActive: Array[Boolean]): Array[String] = {
        val validCoupons = code.zip(businessLine).zip(isActive).filter { case ((code, businessLine), isActive) =>
            isActive && !code.isEmpty && code.matches("^[a-zA-Z0-9_]+$") && businessLine.matches("^(electronics|grocery|pharmacy|restaurant)$")
        }.map { case ((code, businessLine), _) => (businessLine, code) }
        val priority = Map("electronics" -> 0, "grocery" -> 1, "pharmacy" -> 2, "restaurant" -> 3)
        validCoupons.sortBy { case (businessLine, code) => (priority(businessLine), code) }.map { case (_, code) => code }
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
use std::collections::HashMap;

struct Solution;
impl Solution {
    pub fn validate_coupons(code: Vec<String>, business_line: Vec<String>, is_active: Vec<bool>) -> Vec<String> {
        let mut valid_coupons: Vec<(String, String)> = Vec::new();
        let priority: HashMap<String, i32> = [
            ("electronics".to_string(), 0),
            ("grocery".to_string(), 1),
            ("pharmacy".to_string(), 2),
            ("restaurant".to_string(), 3),
        ].iter().cloned().collect();
        for i in 0..code.len() {
            if is_active[i] && !code[i].is_empty() && code[i].chars().all(|c| c.is_alphanumeric() || c == '_') && priority.contains_key(&business_line[i]) {
                valid_coupons.push((business_line[i].clone(), code[i].clone()));
            }
        }
        valid_coupons.sort_by(|a, b| {
            if priority[a.0] == priority[b.0] {
                a.1.cmp(&b.1)
            } else {
                priority[a.0].cmp(&priority[b.0])
            }
        });
        valid_coupons.into_iter().map(|(_, code)| code).collect()
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define (validate-coupons code business-line is-active)
    (let (
        (valid-coupons '())
        (priority (hash "electronics" 0 "grocery" 1 "pharmacy" 2 "restaurant" 3))
        )
        (for ((i (range (length code))))
            (when (and (list-ref is-active i) (not (string=? (list-ref code i) ""))
                       (regexp-match #rx"^[a-zA-Z0-9_]+$" (list-ref code i))
                       (hash-ref priority (list-ref business-line i) #f))
                (set! valid-coupons (cons (list (list-ref business-line i) (list-ref code i)) valid-coupons)))
            )
        (sort valid-coupons (lambda (a b)
            (let (
                (pa (hash-ref priority (car a) +inf.0))
                (pb (hash-ref priority (car b) +inf.0))
                )
                (if (= pa pb)
                    (string<? (cadr a) (cadr b))
                    (< pa pb))
                )
            )
        )
        (map cadr valid-coupons)
        )
    )
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
validate_coupons(Code, BusinessLine, IsActive) ->
    ValidCoupons = [
        {Business, C} ||
            {C, Business} <- lists:zip(Code, BusinessLine),
            {true, Active} <- [{IsActive, true}],
            Active,
            C =/= [],
            re:run(C, "^[a-zA-Z0-9_]+$") =/= nomatch,
            lists:member(Business, ["electronics", "grocery", "pharmacy", "restaurant"])
        ],
    Priority = #{
        "electronics" => 0,
        "grocery" => 1,
        "pharmacy" => 2,
        "restaurant" => 3
    },
    lists:sort(
        fun({BusinessA, CodeA}, {BusinessB, CodeB}) ->
            case maps:get(BusinessA, Priority) of
                PrioA when PrioA =:= maps:get(BusinessB, Priority) ->
                    CodeA =< CodeB;
                PrioA ->
                    PrioA =< maps:get(BusinessB, Priority)
            end
        end,
        ValidCoupons
    ).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
def validate_coupons(code, business_line, is_active) do
    valid_coupons = Enum.zip(code, business_line)
    |> Enum.with_index()
    |> Enum.filter(fn {_, index} -> Enum.at(is_active, index) and String.match?(Enum.at(code, index), ~r/^[a-zA-Z0-9_]+$/)
                                  and Enum.at(business_line, index) in ["electronics", "grocery", "pharmacy", "restaurant"] end)
    |> Enum.map(fn {code, business_line} -> {business_line, code} end)
    priority = %{
        "electronics" => 0,
        "grocery" => 1,
        "pharmacy" => 2,
        "restaurant" => 3
    }
    Enum.sort(valid_coupons, fn {business_line_a, code_a}, {business_line_b, code_b} ->
        if Map.get(priority, business_line_a) == Map.get(priority, business_line_b) do
            code_a <= code_b
        else
            Map.get(priority, business_line_a) <= Map.get(priority, business_line_b)
        end
    end)
    |> Enum.map(fn {_, code} -> code end)
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is O(n log n) due to the sorting operation, where n is the number of coupons. The filtering and storing operations take O(n) time, but the sorting operation dominates the time complexity.

- **Space Complexity:** The space complexity is O(n) as we need to store the filtered coupons and the priority map. The space required does not grow exponentially with the input size, so it is linear.

</div>
</details>
