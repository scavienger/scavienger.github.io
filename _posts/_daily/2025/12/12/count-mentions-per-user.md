---
layout: post
title: "Count Mentions Per User"
date: 2025-12-12 09:00:00 +0900
categories: [LeetCode, Medium]
tags: ["Array", "Math", "Sorting", "Simulation"]
difficulty: Medium
leetcode_url: https://leetcode.com/problems/count-mentions-per-user/
ai_solutions:
  - solutions:
      cpp: "#include <vector>\n#include <string>\n#include <algorithm>\n#include <tuple>\n\
        #include <sstream>\n\nclass Solution {\npublic:\n    std::vector<int> countMentions(int\
        \ numberOfUsers, std::vector<std::vector<std::string>>& events) {\n        std::vector<int>\
        \ mentions(numberOfUsers, 0);\n        std::vector<int> userOfflineUntil(numberOfUsers,\
        \ 0); // Timestamp when user becomes online. 0 means online from start.\n\n\
        \        // Prepare events for sorting: (timestamp, priority, original_event_data)\n\
        \        // Priority: 0 for OFFLINE (status change), 1 for MESSAGE (action)\n\
        \        std::vector<std::tuple<int, int, std::vector<std::string>>> processedEvents;\n\
        \        for (const auto& event : events) {\n            int timestamp = std::stoi(event[1]);\n\
        \            if (event[0] == \"OFFLINE\") {\n                processedEvents.emplace_back(timestamp,\
        \ 0, event);\n            } else { // MESSAGE\n                processedEvents.emplace_back(timestamp,\
        \ 1, event);\n            }\n        }\n\n        // Sort events by timestamp,\
        \ then by priority (OFFLINE before MESSAGE)\n        std::sort(processedEvents.begin(),\
        \ processedEvents.end());\n\n        for (const auto& eventTuple : processedEvents)\
        \ {\n            int currentTimestamp = std::get<0>(eventTuple);\n         \
        \   const auto& originalEvent = std::get<2>(eventTuple);\n            std::string\
        \ eventType = originalEvent[0];\n\n            if (eventType == \"OFFLINE\"\
        ) {\n                int userId = std::stoi(originalEvent[2]);\n           \
        \     userOfflineUntil[userId] = currentTimestamp + 60;\n            } else\
        \ { // MESSAGE event\n                std::string mentionsString = originalEvent[2];\n\
        \n                // Determine current online users *at this timestamp*\n  \
        \              std::vector<int> onlineUsersAtCurrentTime;\n                for\
        \ (int i = 0; i < numberOfUsers; ++i) {\n                    if (userOfflineUntil[i]\
        \ <= currentTimestamp) {\n                        onlineUsersAtCurrentTime.push_back(i);\n\
        \                    }\n                }\n\n                if (mentionsString\
        \ == \"ALL\") {\n                    for (int i = 0; i < numberOfUsers; ++i)\
        \ {\n                        mentions[i]++;\n                    }\n       \
        \         } else if (mentionsString == \"HERE\") {\n                    for\
        \ (int userId : onlineUsersAtCurrentTime) {\n                        mentions[userId]++;\n\
        \                    }\n                } else { // Specific IDs like \"id1\
        \ id0\"\n                    std::stringstream ss(mentionsString);\n       \
        \             std::string token;\n                    while (ss >> token) {\n\
        \                        // Extract number after \"id\"\n                  \
        \      int userId = std::stoi(token.substr(2)); \n                        mentions[userId]++;\n\
        \                    }\n                }\n            }\n        }\n\n    \
        \    return mentions;\n    }\n};"
      java: "import java.util.ArrayList;\nimport java.util.Arrays;\nimport java.util.Collections;\n\
        import java.util.List;\n\nclass Solution {\n\n    // Custom Event class to hold\
        \ parsed event data and enable custom sorting\n    static class Event implements\
        \ Comparable<Event> {\n        int timestamp;\n        int priority; // 0 for\
        \ OFFLINE, 1 for MESSAGE\n        String type;\n        String detail1;\n\n\
        \        public Event(String[] originalEvent) {\n            this.type = originalEvent[0];\n\
        \            this.timestamp = Integer.parseInt(originalEvent[1]);\n        \
        \    this.priority = (this.type.equals(\"OFFLINE\")) ? 0 : 1;\n            this.detail1\
        \ = originalEvent[2]; // mentions_string or user_id\n        }\n\n        @Override\n\
        \        public int compareTo(Event other) {\n            if (this.timestamp\
        \ != other.timestamp) {\n                return Integer.compare(this.timestamp,\
        \ other.timestamp);\n            } else {\n                return Integer.compare(this.priority,\
        \ other.priority);\n            }\n        }\n    }\n\n    public int[] countMentions(int\
        \ numberOfUsers, List<List<String>> events) {\n        int[] mentions = new\
        \ int[numberOfUsers];\n        // userOfflineUntil[i] stores the timestamp when\
        \ user i will become online.\n        // If userOfflineUntil[i] <= currentTimestamp,\
        \ user i is online.\n        // Initially, all users are online, so they are\
        \ \"online since time 0\".\n        int[] userOfflineUntil = new int[numberOfUsers];\
        \ \n        Arrays.fill(userOfflineUntil, 0);\n\n        List<Event> processedEvents\
        \ = new ArrayList<>();\n        for (List<String> eventList : events) {\n  \
        \          processedEvents.add(new Event(eventList.toArray(new String[0])));\n\
        \        }\n\n        Collections.sort(processedEvents);\n\n        for (Event\
        \ event : processedEvents) {\n            int currentTimestamp = event.timestamp;\n\
        \            String eventType = event.type;\n\n            if (eventType.equals(\"\
        OFFLINE\")) {\n                int userId = Integer.parseInt(event.detail1);\n\
        \                userOfflineUntil[userId] = currentTimestamp + 60;\n       \
        \     } else { // MESSAGE event\n                String mentionsString = event.detail1;\n\
        \n                // Determine current online users *at this timestamp*\n  \
        \              List<Integer> onlineUsersAtCurrentTime = new ArrayList<>();\n\
        \                for (int i = 0; i < numberOfUsers; ++i) {\n               \
        \     if (userOfflineUntil[i] <= currentTimestamp) {\n                     \
        \   onlineUsersAtCurrentTime.add(i);\n                    }\n              \
        \  }\n\n                if (mentionsString.equals(\"ALL\")) {\n            \
        \        for (int i = 0; i < numberOfUsers; ++i) {\n                       \
        \ mentions[i]++;\n                    }\n                } else if (mentionsString.equals(\"\
        HERE\")) {\n                    for (int userId : onlineUsersAtCurrentTime)\
        \ {\n                        mentions[userId]++;\n                    }\n  \
        \              } else { // Specific IDs like \"id1 id0\"\n                 \
        \   String[] idTokens = mentionsString.split(\" \");\n                    for\
        \ (String token : idTokens) {\n                        // Extract number after\
        \ \"id\"\n                        int userId = Integer.parseInt(token.substring(2));\
        \ \n                        mentions[userId]++;\n                    }\n   \
        \             }\n            }\n        }\n\n        return mentions;\n    }\n\
        }"
      python: "from typing import List\n\nclass Solution:\n    def countMentions(self,\
        \ numberOfUsers: int, events: List[List[str]]) -> List[int]:\n        mentions\
        \ = [0] * numberOfUsers\n        # user_offline_until[i] stores the timestamp\
        \ when user i will become online.\n        # If user_offline_until[i] <= current_timestamp,\
        \ user i is online.\n        # Initially, all users are online, so they are\
        \ \"online since time 0\".\n        user_offline_until = [0] * numberOfUsers\
        \ \n\n        # Prepare events for sorting: (timestamp, priority, original_event_data)\n\
        \        # Priority: 0 for OFFLINE (status change), 1 for MESSAGE (action)\n\
        \        processed_events = []\n        for event in events:\n            event_type\
        \ = event[0]\n            timestamp = int(event[1])\n            if event_type\
        \ == \"OFFLINE\":\n                processed_events.append((timestamp, 0, event))\
        \ # 0 priority for OFFLINE\n            else: # MESSAGE\n                processed_events.append((timestamp,\
        \ 1, event)) # 1 priority for MESSAGE\n\n        # Sort events by timestamp,\
        \ then by priority (OFFLINE before MESSAGE)\n        processed_events.sort()\n\
        \n        for current_timestamp, _, original_event in processed_events:\n  \
        \          event_type = original_event[0]\n\n            if event_type == \"\
        OFFLINE\":\n                user_id = int(original_event[2])\n             \
        \   user_offline_until[user_id] = current_timestamp + 60\n            else:\
        \ # MESSAGE event\n                mentions_string = original_event[2]\n\n \
        \               # Determine current online users *at this timestamp*\n     \
        \           online_users_at_current_time = []\n                for i in range(numberOfUsers):\n\
        \                    if user_offline_until[i] <= current_timestamp:\n      \
        \                  online_users_at_current_time.append(i)\n\n              \
        \  if mentions_string == \"ALL\":\n                    for i in range(numberOfUsers):\n\
        \                        mentions[i] += 1\n                elif mentions_string\
        \ == \"HERE\":\n                    for user_id in online_users_at_current_time:\n\
        \                        mentions[user_id] += 1\n                else: # Specific\
        \ IDs like \"id1 id0\"\n                    id_tokens = mentions_string.split()\n\
        \                    for token in id_tokens:\n                        user_id\
        \ = int(token[2:]) # Extract number after \"id\"\n                        mentions[user_id]\
        \ += 1\n\n        return mentions"
      python3: "from typing import List\n\nclass Solution:\n    def countMentions(self,\
        \ numberOfUsers: int, events: List[List[str]]) -> List[int]:\n        mentions\
        \ = [0] * numberOfUsers\n        # user_offline_until[i] stores the timestamp\
        \ when user i will become online.\n        # If user_offline_until[i] <= current_timestamp,\
        \ user i is online.\n        # Initially, all users are online, so they are\
        \ \"online since time 0\".\n        user_offline_until = [0] * numberOfUsers\
        \ \n\n        # Prepare events for sorting: (timestamp, priority, original_event_data)\n\
        \        # Priority: 0 for OFFLINE (status change), 1 for MESSAGE (action)\n\
        \        processed_events = []\n        for event in events:\n            event_type\
        \ = event[0]\n            timestamp = int(event[1])\n            if event_type\
        \ == \"OFFLINE\":\n                processed_events.append((timestamp, 0, event))\
        \ # 0 priority for OFFLINE\n            else: # MESSAGE\n                processed_events.append((timestamp,\
        \ 1, event)) # 1 priority for MESSAGE\n\n        # Sort events by timestamp,\
        \ then by priority (OFFLINE before MESSAGE)\n        processed_events.sort()\n\
        \n        for current_timestamp, _, original_event in processed_events:\n  \
        \          event_type = original_event[0]\n\n            if event_type == \"\
        OFFLINE\":\n                user_id = int(original_event[2])\n             \
        \   user_offline_until[user_id] = current_timestamp + 60\n            else:\
        \ # MESSAGE event\n                mentions_string = original_event[2]\n\n \
        \               # Determine current online users *at this timestamp*\n     \
        \           online_users_at_current_time = []\n                for i in range(numberOfUsers):\n\
        \                    if user_offline_until[i] <= current_timestamp:\n      \
        \                  online_users_at_current_time.append(i)\n\n              \
        \  if mentions_string == \"ALL\":\n                    for i in range(numberOfUsers):\n\
        \                        mentions[i] += 1\n                elif mentions_string\
        \ == \"HERE\":\n                    for user_id in online_users_at_current_time:\n\
        \                        mentions[user_id] += 1\n                else: # Specific\
        \ IDs like \"id1 id0\"\n                    id_tokens = mentions_string.split()\n\
        \                    for token in id_tokens:\n                        user_id\
        \ = int(token[2:]) # Extract number after \"id\"\n                        mentions[user_id]\
        \ += 1\n\n        return mentions"
      c: "#include <stdlib.h>\n#include <string.h>\n#include <stdio.h>\n\n// Helper\
        \ struct to hold event data for sorting\ntypedef struct {\n    int timestamp;\n\
        \    int priority; // 0 for OFFLINE, 1 for MESSAGE\n    char** originalEvent;\
        \ // Pointer to the original string array\n} ProcessedEvent;\n\n// Comparison\
        \ function for qsort\nint compareEvents(const void* a, const void* b) {\n  \
        \  ProcessedEvent* eventA = (ProcessedEvent*)a;\n    ProcessedEvent* eventB\
        \ = (ProcessedEvent*)b;\n\n    if (eventA->timestamp != eventB->timestamp) {\n\
        \        return eventA->timestamp - eventB->timestamp;\n    } else {\n     \
        \   return eventA->priority - eventB->priority;\n    }\n}\n\n/**\n * Note: The\
        \ LeetCode C environment usually provides a way to handle dynamic arrays of\
        \ strings.\n * For this problem, `events` is `char***` (array of arrays of strings).\n\
        \ * The return type is `int*` (array of integers).\n * The caller is responsible\
        \ for freeing the returned array.\n */\nint* countMentions(int numberOfUsers,\
        \ char*** events, int eventsSize, int* eventsColSize, int* returnSize) {\n \
        \   int* mentions = (int*)calloc(numberOfUsers, sizeof(int));\n    int* userOfflineUntil\
        \ = (int*)calloc(numberOfUsers, sizeof(int)); // Timestamp when user becomes\
        \ online. 0 means online from start.\n\n    ProcessedEvent* processedEvents\
        \ = (ProcessedEvent*)malloc(eventsSize * sizeof(ProcessedEvent));\n    for (int\
        \ i = 0; i < eventsSize; ++i) {\n        processedEvents[i].originalEvent =\
        \ events[i];\n        processedEvents[i].timestamp = atoi(events[i][1]);\n \
        \       if (strcmp(events[i][0], \"OFFLINE\") == 0) {\n            processedEvents[i].priority\
        \ = 0;\n        } else { // MESSAGE\n            processedEvents[i].priority\
        \ = 1;\n        }\n    }\n\n    qsort(processedEvents, eventsSize, sizeof(ProcessedEvent),\
        \ compareEvents);\n\n    for (int i = 0; i < eventsSize; ++i) {\n        int\
        \ currentTimestamp = processedEvents[i].timestamp;\n        char** originalEvent\
        \ = processedEvents[i].originalEvent;\n        char* eventType = originalEvent[0];\n\
        \n        if (strcmp(eventType, \"OFFLINE\") == 0) {\n            int userId\
        \ = atoi(originalEvent[2]);\n            userOfflineUntil[userId] = currentTimestamp\
        \ + 60;\n        } else { // MESSAGE event\n            char* mentionsString\
        \ = originalEvent[2];\n\n            // Determine current online users *at this\
        \ timestamp*\n            // Using a dynamic array for online users. Max size\
        \ is numberOfUsers.\n            int* onlineUsersAtCurrentTime = (int*)malloc(numberOfUsers\
        \ * sizeof(int));\n            int onlineUsersCount = 0;\n            for (int\
        \ j = 0; j < numberOfUsers; ++j) {\n                if (userOfflineUntil[j]\
        \ <= currentTimestamp) {\n                    onlineUsersAtCurrentTime[onlineUsersCount++]\
        \ = j;\n                }\n            }\n\n            if (strcmp(mentionsString,\
        \ \"ALL\") == 0) {\n                for (int j = 0; j < numberOfUsers; ++j)\
        \ {\n                    mentions[j]++;\n                }\n            } else\
        \ if (strcmp(mentionsString, \"HERE\") == 0) {\n                for (int j =\
        \ 0; j < onlineUsersCount; ++j) {\n                    mentions[onlineUsersAtCurrentTime[j]]++;\n\
        \                }\n            } else { // Specific IDs like \"id1 id0\"\n\
        \                char* tempMentionsString = strdup(mentionsString); // Duplicate\
        \ to tokenize\n                char* token = strtok(tempMentionsString, \" \"\
        );\n                while (token != NULL) {\n                    // Extract\
        \ number after \"id\"\n                    int userId = atoi(token + 2); \n\
        \                    mentions[userId]++;\n                    token = strtok(NULL,\
        \ \" \");\n                }\n                free(tempMentionsString);\n  \
        \          }\n            free(onlineUsersAtCurrentTime);\n        }\n    }\n\
        \n    free(processedEvents);\n    free(userOfflineUntil);\n    *returnSize =\
        \ numberOfUsers;\n    return mentions;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\nusing System.Linq;\n\
        \npublic class Solution {\n\n    // Custom Event class to hold parsed event\
        \ data and enable custom sorting\n    public class Event : IComparable<Event>\
        \ {\n        public int Timestamp { get; set; }\n        public int Priority\
        \ { get; set; } // 0 for OFFLINE, 1 for MESSAGE\n        public string Type\
        \ { get; set; }\n        public string Detail1 { get; set; }\n\n        public\
        \ Event(IList<string> originalEvent) {\n            this.Type = originalEvent[0];\n\
        \            this.Timestamp = int.Parse(originalEvent[1]);\n            this.Priority\
        \ = (this.Type == \"OFFLINE\") ? 0 : 1;\n            this.Detail1 = originalEvent[2];\
        \ // mentions_string or user_id\n        }\n\n        public int CompareTo(Event\
        \ other) {\n            if (this.Timestamp != other.Timestamp) {\n         \
        \       return this.Timestamp.CompareTo(other.Timestamp);\n            } else\
        \ {\n                return this.Priority.CompareTo(other.Priority);\n     \
        \       }\n        }\n    }\n\n    public int[] CountMentions(int numberOfUsers,\
        \ IList<IList<string>> events) {\n        int[] mentions = new int[numberOfUsers];\n\
        \        // userOfflineUntil[i] stores the timestamp when user i will become\
        \ online.\n        // If userOfflineUntil[i] <= currentTimestamp, user i is\
        \ online.\n        // Initially, all users are online, so they are \"online\
        \ since time 0\".\n        int[] userOfflineUntil = new int[numberOfUsers];\
        \ \n        // Arrays are default initialized to 0 in C#, so no explicit fill\
        \ needed.\n\n        List<Event> processedEvents = new List<Event>();\n    \
        \    foreach (var eventList in events) {\n            processedEvents.Add(new\
        \ Event(eventList));\n        }\n\n        processedEvents.Sort();\n\n     \
        \   foreach (Event eventItem in processedEvents) {\n            int currentTimestamp\
        \ = eventItem.Timestamp;\n            string eventType = eventItem.Type;\n\n\
        \            if (eventType == \"OFFLINE\") {\n                int userId = int.Parse(eventItem.Detail1);\n\
        \                userOfflineUntil[userId] = currentTimestamp + 60;\n       \
        \     } else { // MESSAGE event\n                string mentionsString = eventItem.Detail1;\n\
        \n                // Determine current online users *at this timestamp*\n  \
        \              List<int> onlineUsersAtCurrentTime = new List<int>();\n     \
        \           for (int i = 0; i < numberOfUsers; ++i) {\n                    if\
        \ (userOfflineUntil[i] <= currentTimestamp) {\n                        onlineUsersAtCurrentTime.Add(i);\n\
        \                    }\n                }\n\n                if (mentionsString\
        \ == \"ALL\") {\n                    for (int i = 0; i < numberOfUsers; ++i)\
        \ {\n                        mentions[i]++;\n                    }\n       \
        \         } else if (mentionsString == \"HERE\") {\n                    foreach\
        \ (int userId in onlineUsersAtCurrentTime) {\n                        mentions[userId]++;\n\
        \                    }\n                } else { // Specific IDs like \"id1\
        \ id0\"\n                    string[] idTokens = mentionsString.Split(' ');\n\
        \                    foreach (string token in idTokens) {\n                \
        \        // Extract number after \"id\"\n                        int userId\
        \ = int.Parse(token.Substring(2)); \n                        mentions[userId]++;\n\
        \                    }\n                }\n            }\n        }\n\n    \
        \    return mentions;\n    }\n}"
      javascript: "/**\n * @param {number} numberOfUsers\n * @param {string[][]} events\n\
        \ * @return {number[]}\n */\nvar countMentions = function(numberOfUsers, events)\
        \ {\n    let mentions = new Array(numberOfUsers).fill(0);\n    // userOfflineUntil[i]\
        \ stores the timestamp when user i will become online.\n    // If userOfflineUntil[i]\
        \ <= currentTimestamp, user i is online.\n    // Initially, all users are online,\
        \ so they are \"online since time 0\".\n    let userOfflineUntil = new Array(numberOfUsers).fill(0);\
        \ \n\n    // Prepare events for sorting: [timestamp, priority, original_event_data]\n\
        \    // Priority: 0 for OFFLINE (status change), 1 for MESSAGE (action)\n  \
        \  let processedEvents = [];\n    for (const event of events) {\n        const\
        \ eventType = event[0];\n        const timestamp = parseInt(event[1]);\n   \
        \     if (eventType === \"OFFLINE\") {\n            processedEvents.push([timestamp,\
        \ 0, event]); // 0 priority for OFFLINE\n        } else { // MESSAGE\n     \
        \       processedEvents.push([timestamp, 1, event]); // 1 priority for MESSAGE\n\
        \        }\n    }\n\n    // Sort events by timestamp, then by priority (OFFLINE\
        \ before MESSAGE)\n    processedEvents.sort((a, b) => {\n        if (a[0] !==\
        \ b[0]) {\n            return a[0] - b[0];\n        } else {\n            return\
        \ a[1] - b[1];\n        }\n    });\n\n    for (const eventTuple of processedEvents)\
        \ {\n        const currentTimestamp = eventTuple[0];\n        const originalEvent\
        \ = eventTuple[2];\n        const eventType = originalEvent[0];\n\n        if\
        \ (eventType === \"OFFLINE\") {\n            const userId = parseInt(originalEvent[2]);\n\
        \            userOfflineUntil[userId] = currentTimestamp + 60;\n        } else\
        \ { // MESSAGE event\n            const mentionsString = originalEvent[2];\n\
        \n            // Determine current online users *at this timestamp*\n      \
        \      let onlineUsersAtCurrentTime = [];\n            for (let i = 0; i < numberOfUsers;\
        \ ++i) {\n                if (userOfflineUntil[i] <= currentTimestamp) {\n \
        \                   onlineUsersAtCurrentTime.push(i);\n                }\n \
        \           }\n\n            if (mentionsString === \"ALL\") {\n           \
        \     for (let i = 0; i < numberOfUsers; ++i) {\n                    mentions[i]++;\n\
        \                }\n            } else if (mentionsString === \"HERE\") {\n\
        \                for (const userId of onlineUsersAtCurrentTime) {\n        \
        \            mentions[userId]++;\n                }\n            } else { //\
        \ Specific IDs like \"id1 id0\"\n                const idTokens = mentionsString.split('\
        \ ');\n                for (const token of idTokens) {\n                   \
        \ // Extract number after \"id\"\n                    const userId = parseInt(token.substring(2));\
        \ \n                    mentions[userId]++;\n                }\n           \
        \ }\n        }\n    }\n\n    return mentions;\n};"
      typescript: "function countMentions(numberOfUsers: number, events: string[][]):\
        \ number[] {\n    const mentions: number[] = new Array(numberOfUsers).fill(0);\n\
        \    // userOfflineUntil[i] stores the timestamp when user i will become online.\n\
        \    // If userOfflineUntil[i] <= currentTimestamp, user i is online.\n    //\
        \ Initially, all users are online, so they are \"online since time 0\".\n  \
        \  const userOfflineUntil: number[] = new Array(numberOfUsers).fill(0); \n\n\
        \    // Prepare events for sorting: [timestamp, priority, original_event_data]\n\
        \    // Priority: 0 for OFFLINE (status change), 1 for MESSAGE (action)\n  \
        \  const processedEvents: [number, number, string[]][] = [];\n    for (const\
        \ event of events) {\n        const eventType: string = event[0];\n        const\
        \ timestamp: number = parseInt(event[1]);\n        if (eventType === \"OFFLINE\"\
        ) {\n            processedEvents.push([timestamp, 0, event]); // 0 priority\
        \ for OFFLINE\n        } else { // MESSAGE\n            processedEvents.push([timestamp,\
        \ 1, event]); // 1 priority for MESSAGE\n        }\n    }\n\n    // Sort events\
        \ by timestamp, then by priority (OFFLINE before MESSAGE)\n    processedEvents.sort((a,\
        \ b) => {\n        if (a[0] !== b[0]) {\n            return a[0] - b[0];\n \
        \       } else {\n            return a[1] - b[1];\n        }\n    });\n\n  \
        \  for (const eventTuple of processedEvents) {\n        const currentTimestamp:\
        \ number = eventTuple[0];\n        const originalEvent: string[] = eventTuple[2];\n\
        \        const eventType: string = originalEvent[0];\n\n        if (eventType\
        \ === \"OFFLINE\") {\n            const userId: number = parseInt(originalEvent[2]);\n\
        \            userOfflineUntil[userId] = currentTimestamp + 60;\n        } else\
        \ { // MESSAGE event\n            const mentionsString: string = originalEvent[2];\n\
        \n            // Determine current online users *at this timestamp*\n      \
        \      const onlineUsersAtCurrentTime: number[] = [];\n            for (let\
        \ i = 0; i < numberOfUsers; ++i) {\n                if (userOfflineUntil[i]\
        \ <= currentTimestamp) {\n                    onlineUsersAtCurrentTime.push(i);\n\
        \                }\n            }\n\n            if (mentionsString === \"ALL\"\
        ) {\n                for (let i = 0; i < numberOfUsers; ++i) {\n           \
        \         mentions[i]++;\n                }\n            } else if (mentionsString\
        \ === \"HERE\") {\n                for (const userId of onlineUsersAtCurrentTime)\
        \ {\n                    mentions[userId]++;\n                }\n          \
        \  } else { // Specific IDs like \"id1 id0\"\n                const idTokens:\
        \ string[] = mentionsString.split(' ');\n                for (const token of\
        \ idTokens) {\n                    // Extract number after \"id\"\n        \
        \            const userId: number = parseInt(token.substring(2)); \n       \
        \             mentions[userId]++;\n                }\n            }\n      \
        \  }\n    }\n\n    return mentions;\n}"
      php: "<?php\nclass Solution {\n\n    /**\n     * @param Integer $numberOfUsers\n\
        \     * @param String[][] $events\n     * @return Integer[]\n     */\n    function\
        \ countMentions($numberOfUsers, $events) {\n        $mentions = array_fill(0,\
        \ $numberOfUsers, 0);\n        // userOfflineUntil[i] stores the timestamp when\
        \ user i will become online.\n        // If userOfflineUntil[i] <= currentTimestamp,\
        \ user i is online.\n        // Initially, all users are online, so they are\
        \ \"online since time 0\".\n        $userOfflineUntil = array_fill(0, $numberOfUsers,\
        \ 0); \n\n        // Prepare events for sorting: [timestamp, priority, original_event_data]\n\
        \        // Priority: 0 for OFFLINE (status change), 1 for MESSAGE (action)\n\
        \        $processedEvents = [];\n        foreach ($events as $event) {\n   \
        \         $eventType = $event[0];\n            $timestamp = intval($event[1]);\n\
        \            if ($eventType === \"OFFLINE\") {\n                $processedEvents[]\
        \ = [$timestamp, 0, $event]; // 0 priority for OFFLINE\n            } else {\
        \ // MESSAGE\n                $processedEvents[] = [$timestamp, 1, $event];\
        \ // 1 priority for MESSAGE\n            }\n        }\n\n        // Sort events\
        \ by timestamp, then by priority (OFFLINE before MESSAGE)\n        usort($processedEvents,\
        \ function($a, $b) {\n            if ($a[0] !== $b[0]) {\n                return\
        \ $a[0] - $b[0];\n            } else {\n                return $a[1] - $b[1];\n\
        \            }\n        });\n\n        foreach ($processedEvents as $eventTuple)\
        \ {\n            $currentTimestamp = $eventTuple[0];\n            $originalEvent\
        \ = $eventTuple[2];\n            $eventType = $originalEvent[0];\n\n       \
        \     if ($eventType === \"OFFLINE\") {\n                $userId = intval($originalEvent[2]);\n\
        \                $userOfflineUntil[$userId] = $currentTimestamp + 60;\n    \
        \        } else { // MESSAGE event\n                $mentionsString = $originalEvent[2];\n\
        \n                // Determine current online users *at this timestamp*\n  \
        \              $onlineUsersAtCurrentTime = [];\n                for ($i = 0;\
        \ $i < $numberOfUsers; ++$i) {\n                    if ($userOfflineUntil[$i]\
        \ <= $currentTimestamp) {\n                        $onlineUsersAtCurrentTime[]\
        \ = $i;\n                    }\n                }\n\n                if ($mentionsString\
        \ === \"ALL\") {\n                    for ($i = 0; $i < $numberOfUsers; ++$i)\
        \ {\n                        $mentions[$i]++;\n                    }\n     \
        \           } else if ($mentionsString === \"HERE\") {\n                   \
        \ foreach ($onlineUsersAtCurrentTime as $userId) {\n                       \
        \ $mentions[$userId]++;\n                    }\n                }\n        \
        \        else { // Specific IDs like \"id1 id0\"\n                    $idTokens\
        \ = explode(' ', $mentionsString);\n                    foreach ($idTokens as\
        \ $token) {\n                        // Extract number after \"id\"\n      \
        \                  $userId = intval(substr($token, 2)); \n                 \
        \       $mentions[$userId]++;\n                    }\n                }\n  \
        \          }\n        }\n\n        return $mentions;\n    }\n}"
      swift: "import Foundation\n\nclass Solution {\n\n    // Custom Event struct to\
        \ hold parsed event data and enable custom sorting\n    struct Event: Comparable\
        \ {\n        let timestamp: Int\n        let priority: Int // 0 for OFFLINE,\
        \ 1 for MESSAGE\n        let type: String\n        let detail1: String\n\n \
        \       init(_ originalEvent: [String]) {\n            self.type = originalEvent[0]\n\
        \            self.timestamp = Int(originalEvent[1])!\n            self.priority\
        \ = (self.type == \"OFFLINE\") ? 0 : 1\n            self.detail1 = originalEvent[2]\
        \ // mentions_string or user_id\n        }\n\n        static func < (lhs: Event,\
        \ rhs: Event) -> Bool {\n            if lhs.timestamp != rhs.timestamp {\n \
        \               return lhs.timestamp < rhs.timestamp\n            } else {\n\
        \                return lhs.priority < rhs.priority\n            }\n       \
        \ }\n    }\n\n    func countMentions(_ numberOfUsers: Int, _ events: [[String]])\
        \ -> [Int] {\n        var mentions = Array(repeating: 0, count: numberOfUsers)\n\
        \        // userOfflineUntil[i] stores the timestamp when user i will become\
        \ online.\n        // If userOfflineUntil[i] <= currentTimestamp, user i is\
        \ online.\n        // Initially, all users are online, so they are \"online\
        \ since time 0\".\n        var userOfflineUntil = Array(repeating: 0, count:\
        \ numberOfUsers) \n\n        var processedEvents: [Event] = []\n        for\
        \ eventList in events {\n            processedEvents.append(Event(eventList))\n\
        \        }\n\n        processedEvents.sort()\n\n        for event in processedEvents\
        \ {\n            let currentTimestamp = event.timestamp\n            let eventType\
        \ = event.type\n\n            if eventType == \"OFFLINE\" {\n              \
        \  let userId = Int(event.detail1)!;\n                userOfflineUntil[userId]\
        \ = currentTimestamp + 60\n            } else { // MESSAGE event\n         \
        \       let mentionsString = event.detail1\n\n                // Determine current\
        \ online users *at this timestamp*\n                var onlineUsersAtCurrentTime:\
        \ [Int] = []\n                for i in 0..<numberOfUsers {\n               \
        \     if userOfflineUntil[i] <= currentTimestamp {\n                       \
        \ onlineUsersAtCurrentTime.append(i)\n                    }\n              \
        \  }\n\n                if mentionsString == \"ALL\" {\n                   \
        \ for i in 0..<numberOfUsers {\n                        mentions[i] += 1\n \
        \                   }\n                } else if mentionsString == \"HERE\"\
        \ {\n                    for userId in onlineUsersAtCurrentTime {\n        \
        \                mentions[userId] += 1\n                    }\n            \
        \    } else { // Specific IDs like \"id1 id0\"\n                    let idTokens\
        \ = mentionsString.split(separator: \" \")\n                    for token in\
        \ idTokens {\n                        // Extract number after \"id\"\n     \
        \                   let userId = Int(token.dropFirst(2))! \n               \
        \         mentions[userId] += 1\n                    }\n                }\n\
        \            }\n        }\n\n        return mentions\n    }\n}"
      kotlin: "class Solution {\n\n    // Custom Event data class to hold parsed event\
        \ data and enable custom sorting\n    data class Event(val timestamp: Int, val\
        \ priority: Int, val type: String, val val1: String) : Comparable<Event> {\n\
        \        override fun compareTo(other: Event): Int {\n            if (this.timestamp\
        \ != other.timestamp) {\n                return this.timestamp.compareTo(other.timestamp)\n\
        \            } else {\n                return this.priority.compareTo(other.priority)\n\
        \            }\n        }\n    }\n\n    fun countMentions(numberOfUsers: Int,\
        \ events: List<List<String>>): IntArray {\n        val mentions = IntArray(numberOfUsers)\
        \ { 0 }\n        // userOfflineUntil[i] stores the timestamp when user i will\
        \ become online.\n        // If userOfflineUntil[i] <= currentTimestamp, user\
        \ i is online.\n        // Initially, all users are online, so they are \"online\
        \ since time 0\".\n        val userOfflineUntil = IntArray(numberOfUsers) {\
        \ 0 } \n\n        val processedEvents = mutableListOf<Event>()\n        for\
        \ (eventList in events) {\n            val eventType = eventList[0]\n      \
        \      val timestamp = eventList[1].toInt()\n            val priority = if (eventType\
        \ == \"OFFLINE\") 0 else 1\n            processedEvents.add(Event(timestamp,\
        \ priority, eventType, eventList[2]))\n        }\n\n        processedEvents.sort()\n\
        \n        for (event in processedEvents) {\n            val currentTimestamp\
        \ = event.timestamp\n            val eventType = event.type\n\n            if\
        \ (eventType == \"OFFLINE\") {\n                val userId = event.val1.toInt()\n\
        \                userOfflineUntil[userId] = currentTimestamp + 60\n        \
        \    } else { // MESSAGE event\n                val mentionsString = event.val1\n\
        \n                // Determine current online users *at this timestamp*\n  \
        \              val onlineUsersAtCurrentTime = mutableListOf<Int>()\n       \
        \         for (i in 0 until numberOfUsers) {\n                    if (userOfflineUntil[i]\
        \ <= currentTimestamp) {\n                        onlineUsersAtCurrentTime.add(i)\n\
        \                    }\n                }\n\n                if (mentionsString\
        \ == \"ALL\") {\n                    for (i in 0 until numberOfUsers) {\n  \
        \                      mentions[i]++\n                    }\n              \
        \  } else if (mentionsString == \"HERE\") {\n                    for (userId\
        \ in onlineUsersAtCurrentTime) {\n                        mentions[userId]++\n\
        \                    }\n                } else { // Specific IDs like \"id1\
        \ id0\"\n                    val idTokens = mentionsString.split(' ')\n    \
        \                for (token in idTokens) {\n                        // Extract\
        \ number after \"id\"\n                        val userId = token.substring(2).toInt()\
        \ \n                        mentions[userId]++\n                    }\n    \
        \            }\n            }\n        }\n\n        return mentions\n    }\n\
        }"
      dart: "class Solution {\n\n  // Custom Event class to hold parsed event data and\
        \ enable custom sorting\n  class Event implements Comparable<Event> {\n    final\
        \ int timestamp;\n    final int priority; // 0 for OFFLINE, 1 for MESSAGE\n\
        \    final String type;\n    final String detail1;\n\n    Event(List<String>\
        \ originalEvent) \n      : type = originalEvent[0],\n        timestamp = int.parse(originalEvent[1]),\n\
        \        priority = (originalEvent[0] == \"OFFLINE\") ? 0 : 1,\n        detail1\
        \ = originalEvent[2]; // mentions_string or user_id\n\n    @override\n    int\
        \ compareTo(Event other) {\n      if (timestamp != other.timestamp) {\n    \
        \    return timestamp.compareTo(other.timestamp);\n      } else {\n        return\
        \ priority.compareTo(other.priority);\n      }\n    }\n  }\n\n  List<int> countMentions(int\
        \ numberOfUsers, List<List<String>> events) {\n    List<int> mentions = List.filled(numberOfUsers,\
        \ 0);\n    // userOfflineUntil[i] stores the timestamp when user i will become\
        \ online.\n    // If userOfflineUntil[i] <= currentTimestamp, user i is online.\n\
        \    // Initially, all users are online, so they are \"online since time 0\"\
        .\n    List<int> userOfflineUntil = List.filled(numberOfUsers, 0); \n\n    List<Event>\
        \ processedEvents = [];\n    for (var eventList in events) {\n      processedEvents.add(Event(eventList));\n\
        \    }\n\n    processedEvents.sort();\n\n    for (var event in processedEvents)\
        \ {\n      int currentTimestamp = event.timestamp;\n      String eventType =\
        \ event.type;\n\n      if (eventType == \"OFFLINE\") {\n        int userId =\
        \ int.parse(event.detail1);\n        userOfflineUntil[userId] = currentTimestamp\
        \ + 60;\n      } else { // MESSAGE event\n        String mentionsString = event.detail1;\n\
        \n        // Determine current online users *at this timestamp*\n        List<int>\
        \ onlineUsersAtCurrentTime = [];\n        for (int i = 0; i < numberOfUsers;\
        \ ++i) {\n          if (userOfflineUntil[i] <= currentTimestamp) {\n       \
        \     onlineUsersAtCurrentTime.add(i);\n          }\n        }\n\n        if\
        \ (mentionsString == \"ALL\") {\n          for (int i = 0; i < numberOfUsers;\
        \ ++i) {\n            mentions[i]++;\n          }\n        } else if (mentionsString\
        \ == \"HERE\") {\n          for (int userId in onlineUsersAtCurrentTime) {\n\
        \            mentions[userId]++;\n          }\n        } else { // Specific\
        \ IDs like \"id1 id0\"\n          List<String> idTokens = mentionsString.split('\
        \ ');\n          for (String token in idTokens) {\n            // Extract number\
        \ after \"id\"\n            int userId = int.parse(token.substring(2)); \n \
        \           mentions[userId]++;\n          }\n        }\n      }\n    }\n\n\
        \    return mentions;\n  }\n}"
      go: "import (\n\t\"sort\"\n\t\"strconv\"\n\t\"strings\"\n)\n\ntype Event struct\
        \ {\n\ttimestamp int\n\tpriority  int // 0 for OFFLINE, 1 for MESSAGE\n\ttypeStr\
        \   string\n\tdetail1   string\n}\n\ntype ByTimestampAndPriority []Event\n\n\
        func (a ByTimestampAndPriority) Len() int      { return len(a) }\nfunc (a ByTimestampAndPriority)\
        \ Swap(i, j int) { a[i], a[j] = a[j], a[i] }\nfunc (a ByTimestampAndPriority)\
        \ Less(i, j int) bool {\n\tif a[i].timestamp != a[j].timestamp {\n\t\treturn\
        \ a[i].timestamp < a[j].timestamp\n\t}\n\treturn a[i].priority < a[j].priority\n\
        }\n\nfunc countMentions(numberOfUsers int, events [][]string) []int {\n\tmentions\
        \ := make([]int, numberOfUsers)\n\t// userOfflineUntil[i] stores the timestamp\
        \ when user i will become online.\n\t// If userOfflineUntil[i] <= currentTimestamp,\
        \ user i is online.\n\t// Initially, all users are online, so they are \"online\
        \ since time 0\".\n\tuserOfflineUntil := make([]int, numberOfUsers)\n\n\tprocessedEvents\
        \ := make([]Event, 0, len(events))\n\tfor _, eventArr := range events {\n\t\t\
        eventType := eventArr[0]\n\t\ttimestamp, _ := strconv.Atoi(eventArr[1])\n\t\t\
        priority := 1 // Default for MESSAGE\n\t\tif eventType == \"OFFLINE\" {\n\t\t\
        \tpriority = 0\n\t\t}\n\t\tprocessedEvents = append(processedEvents, Event{\n\
        \t\t\ttimestamp: timestamp,\n\t\t\tpriority:  priority,\n\t\t\ttypeStr:   eventType,\n\
        \t\t\tdetail1:   eventArr[2],\n\t\t})\n\t}\n\n\tsort.Sort(ByTimestampAndPriority(processedEvents))\n\
        \n\tfor _, event := range processedEvents {\n\t\tcurrentTimestamp := event.timestamp\n\
        \t\teventType := event.typeStr\n\n\t\tif eventType == \"OFFLINE\" {\n\t\t\t\
        userId, _ := strconv.Atoi(event.detail1)\n\t\t\tuserOfflineUntil[userId] = currentTimestamp\
        \ + 60\n\t\t} else { // MESSAGE event\n\t\t\tmentionsString := event.detail1\n\
        \n\t\t\t// Determine current online users *at this timestamp*\n\t\t\tonlineUsersAtCurrentTime\
        \ := []int{}\n\t\t\tfor i := 0; i < numberOfUsers; i++ {\n\t\t\t\tif userOfflineUntil[i]\
        \ <= currentTimestamp {\n\t\t\t\t\tonlineUsersAtCurrentTime = append(onlineUsersAtCurrentTime,\
        \ i)\n\t\t\t\t}\n\t\t\t}\n\n\t\t\tif mentionsString == \"ALL\" {\n\t\t\t\tfor\
        \ i := 0; i < numberOfUsers; i++ {\n\t\t\t\t\tmentions[i]++\n\t\t\t\t}\n\t\t\
        \t} else if mentionsString == \"HERE\" {\n\t\t\t\tfor _, userId := range onlineUsersAtCurrentTime\
        \ {\n\t\t\t\t\tmentions[userId]++\n\t\t\t\t}\n\t\t\t} else { // Specific IDs\
        \ like \"id1 id0\"\n\t\t\t\tidTokens := strings.Split(mentionsString, \" \"\
        )\n\t\t\t\tfor _, token := range idTokens {\n\t\t\t\t\t// Extract number after\
        \ \"id\"\n\t\t\t\t\tuserId, _ := strconv.Atoi(token[2:])\n\t\t\t\t\tmentions[userId]++\n\
        \t\t\t\t}\n\t\t\t}\n\t\t}\n\t}\n\n\treturn mentions\n}"
      ruby: "class Solution\n    def countMentions(number_of_users, events)\n      \
        \  mentions = Array.new(number_of_users, 0)\n        # user_offline_until[i]\
        \ stores the timestamp when user i will become online.\n        # If user_offline_until[i]\
        \ <= current_timestamp, user i is online.\n        # Initially, all users are\
        \ online, so they are \"online since time 0\".\n        user_offline_until =\
        \ Array.new(number_of_users, 0) \n\n        # Prepare events for sorting: [timestamp,\
        \ priority, original_event_data]\n        # Priority: 0 for OFFLINE (status\
        \ change), 1 for MESSAGE (action)\n        processed_events = []\n        events.each\
        \ do |event|\n            event_type = event[0]\n            timestamp = event[1].to_i\n\
        \            if event_type == \"OFFLINE\"\n                processed_events.push([timestamp,\
        \ 0, event]) # 0 priority for OFFLINE\n            else # MESSAGE\n        \
        \        processed_events.push([timestamp, 1, event]) # 1 priority for MESSAGE\n\
        \            end\n        end\n\n        # Sort events by timestamp, then by\
        \ priority (OFFLINE before MESSAGE)\n        processed_events.sort_by! { |e|\
        \ [e[0], e[1]] }\n\n        processed_events.each do |event_tuple|\n       \
        \     current_timestamp = event_tuple[0]\n            original_event = event_tuple[2]\n\
        \            event_type = original_event[0]\n\n            if event_type ==\
        \ \"OFFLINE\"\n                user_id = original_event[2].to_i\n          \
        \      user_offline_until[user_id] = current_timestamp + 60\n            else\
        \ # MESSAGE event\n                mentions_string = original_event[2]\n\n \
        \               # Determine current online users *at this timestamp*\n     \
        \           online_users_at_current_time = []\n                (0...number_of_users).each\
        \ do |i|\n                    if user_offline_until[i] <= current_timestamp\n\
        \                        online_users_at_current_time.push(i)\n            \
        \        end\n                end\n\n                if mentions_string == \"\
        ALL\"\n                    (0...number_of_users).each do |i|\n             \
        \           mentions[i] += 1\n                    end\n                elsif\
        \ mentions_string == \"HERE\"\n                    online_users_at_current_time.each\
        \ do |user_id|\n                        mentions[user_id] += 1\n           \
        \         end\n                else # Specific IDs like \"id1 id0\"\n      \
        \              id_tokens = mentions_string.split(' ')\n                    id_tokens.each\
        \ do |token|\n                        # Extract number after \"id\"\n      \
        \                  user_id = token[2..].to_i \n                        mentions[user_id]\
        \ += 1\n                    end\n                end\n            end\n    \
        \    end\n\n        return mentions\n    end\nend"
      scala: "import scala.collection.mutable.ListBuffer\n\nclass Solution {\n\n   \
        \ // Custom Event case class to hold parsed event data and enable custom sorting\n\
        \    case class Event(timestamp: Int, priority: Int, eventType: String, detail1:\
        \ String) extends Ordered[Event] {\n        override def compare(that: Event):\
        \ Int = {\n            if (this.timestamp != that.timestamp) {\n           \
        \     this.timestamp.compareTo(that.timestamp)\n            } else {\n     \
        \           this.priority.compareTo(that.priority)\n            }\n        }\n\
        \    }\n\n    def countMentions(numberOfUsers: Int, events: List[List[String]]):\
        \ Array[Int] = {\n        val mentions = Array.fill(numberOfUsers)(0)\n    \
        \    // userOfflineUntil(i) stores the timestamp when user i will become online.\n\
        \        // If userOfflineUntil(i) <= currentTimestamp, user i is online.\n\
        \        // Initially, all users are online, so they are \"online since time\
        \ 0\".\n        val userOfflineUntil = Array.fill(numberOfUsers)(0) \n\n   \
        \     val processedEvents = ListBuffer[Event]()\n        for (eventList <- events)\
        \ {\n            val eventType = eventList.head\n            val timestamp =\
        \ eventList(1).toInt\n            val priority = if (eventType == \"OFFLINE\"\
        ) 0 else 1\n            processedEvents += Event(timestamp, priority, eventType,\
        \ eventList(2))\n        }\n\n        val sortedEvents = processedEvents.sorted\n\
        \n        for (event <- sortedEvents) {\n            val currentTimestamp =\
        \ event.timestamp\n            val eventType = event.eventType\n\n         \
        \   if (eventType == \"OFFLINE\") {\n                val userId = event.detail1.toInt\n\
        \                userOfflineUntil(userId) = currentTimestamp + 60\n        \
        \    } else { // MESSAGE event\n                val mentionsString = event.detail1\n\
        \n                // Determine current online users *at this timestamp*\n  \
        \              val onlineUsersAtCurrentTime = ListBuffer[Int]()\n          \
        \      for (i <- 0 until numberOfUsers) {\n                    if (userOfflineUntil(i)\
        \ <= currentTimestamp) {\n                        onlineUsersAtCurrentTime +=\
        \ i\n                    }\n                }\n\n                if (mentionsString\
        \ == \"ALL\") {\n                    for (i <- 0 until numberOfUsers) {\n  \
        \                      mentions(i) += 1\n                    }\n           \
        \     } else if (mentionsString == \"HERE\") {\n                    for (userId\
        \ <- onlineUsersAtCurrentTime) {\n                        mentions(userId) +=\
        \ 1\n                    }\n                } else { // Specific IDs like \"\
        id1 id0\"\n                    val idTokens = mentionsString.split(' ')\n  \
        \                  for (token <- idTokens) {\n                        // Extract\
        \ number after \"id\"\n                        val userId = token.substring(2).toInt\
        \ \n                        mentions(userId) += 1\n                    }\n \
        \               }\n            }\n        }\n\n        mentions\n    }\n}"
      rust: "impl Solution {\n    pub fn count_mentions(number_of_users: i32, events:\
        \ Vec<Vec<String>>) -> Vec<i32> {\n        let mut mentions = vec![0; number_of_users\
        \ as usize];\n        // user_offline_until[i] stores the timestamp when user\
        \ i will become online.\n        // If user_offline_until[i] <= current_timestamp,\
        \ user i is online.\n        // Initially, all users are online, so they are\
        \ \"online since time 0\".\n        let mut user_offline_until = vec![0; number_of_users\
        \ as usize]; \n\n        // Prepare events for sorting: (timestamp, priority,\
        \ original_event_data)\n        // Priority: 0 for OFFLINE (status change),\
        \ 1 for MESSAGE (action)\n        let mut processed_events: Vec<(i32, i32, Vec<String>)>\
        \ = Vec::new();\n        for event in events {\n            let event_type =\
        \ &event[0];\n            let timestamp = event[1].parse::<i32>().unwrap();\n\
        \            if event_type == \"OFFLINE\" {\n                processed_events.push((timestamp,\
        \ 0, event)); // 0 priority for OFFLINE\n            } else { // MESSAGE\n \
        \               processed_events.push((timestamp, 1, event)); // 1 priority\
        \ for MESSAGE\n            }\n        }\n\n        // Sort events by timestamp,\
        \ then by priority (OFFLINE before MESSAGE)\n        processed_events.sort_unstable();\n\
        \n        for (current_timestamp, _, original_event) in processed_events {\n\
        \            let event_type = &original_event[0];\n\n            if event_type\
        \ == \"OFFLINE\" {\n                let user_id = original_event[2].parse::<usize>().unwrap();\n\
        \                user_offline_until[user_id] = current_timestamp + 60;\n   \
        \         } else { // MESSAGE event\n                let mentions_string = &original_event[2];\n\
        \n                // Determine current online users *at this timestamp*\n  \
        \              let mut online_users_at_current_time: Vec<usize> = Vec::new();\n\
        \                for i in 0..number_of_users as usize {\n                  \
        \  if user_offline_until[i] <= current_timestamp {\n                       \
        \ online_users_at_current_time.push(i);\n                    }\n           \
        \     }\n\n                if mentions_string == \"ALL\" {\n               \
        \     for i in 0..number_of_users as usize {\n                        mentions[i]\
        \ += 1;\n                    }\n                } else if mentions_string ==\
        \ \"HERE\" {\n                    for user_id in online_users_at_current_time\
        \ {\n                        mentions[user_id] += 1;\n                    }\n\
        \                } else { // Specific IDs like \"id1 id0\"\n               \
        \     let id_tokens = mentions_string.split_whitespace();\n                \
        \    for token in id_tokens {\n                        // Extract number after\
        \ \"id\"\n                        let user_id = token[2..].parse::<usize>().unwrap();\
        \ \n                        mentions[user_id] += 1;\n                    }\n\
        \                }\n            }\n        }\n\n        mentions\n    }\n}"
      racket: "#lang racket\n\n(define (count-mentions number-of-users events)\n  (define\
        \ mentions (make-vector number-of-users 0))\n  ;; user-offline-until[i] stores\
        \ the timestamp when user i will become online.\n  ;; If (vector-ref user-offline-until\
        \ i) <= current-timestamp, user i is online.\n  ;; Initially, all users are\
        \ online, so they are \"online since time 0\".\n  (define user-offline-until\
        \ (make-vector number-of-users 0))\n\n  ;; Prepare events for sorting: (timestamp,\
        \ priority, original-event-data)\n  ;; Priority: 0 for OFFLINE (status change),\
        \ 1 for MESSAGE (action)\n  (define processed-events\n    (for/list ([event\
        \ events])\n      (define event-type (list-ref event 0))\n      (define timestamp\
        \ (string->number (list-ref event 1)))\n      (if (string=? event-type \"OFFLINE\"\
        )\n          (list timestamp 0 event) ; 0 priority for OFFLINE\n          (list\
        \ timestamp 1 event)))) ; 1 priority for MESSAGE\n\n  ;; Sort events by timestamp,\
        \ then by priority (OFFLINE before MESSAGE)\n  (define sorted-events (sort processed-events\
        \ (lambda (a b)\n                                                  (or (< (list-ref\
        \ a 0) (list-ref b 0))\n                                                   \
        \   (and (= (list-ref a 0) (list-ref b 0))\n                               \
        \                            (< (list-ref a 1) (list-ref b 1)))))))\n\n  (for\
        \ ([event-tuple sorted-events])\n    (define current-timestamp (list-ref event-tuple\
        \ 0))\n    (define original-event (list-ref event-tuple 2))\n    (define event-type\
        \ (list-ref original-event 0))\n\n    (if (string=? event-type \"OFFLINE\")\n\
        \        (begin\n          (define user-id (string->number (list-ref original-event\
        \ 2)))\n          (vector-set! user-offline-until user-id (+ current-timestamp\
        \ 60)))\n        ;; MESSAGE event\n        (begin\n          (define mentions-string\
        \ (list-ref original-event 2))\n\n          ;; Determine current online users\
        \ *at this timestamp*\n          (define online-users-at-current-time (build-list\
        \ number-of-users identity))\n          (define filtered-online-users\n    \
        \        (filter (lambda (i) (<= (vector-ref user-offline-until i) current-timestamp))\n\
        \                    online-users-at-current-time))\n\n          (cond\n   \
        \         ((string=? mentions-string \"ALL\")\n             (for ([i (in-range\
        \ number-of-users)])\n               (vector-set! mentions i (+ (vector-ref\
        \ mentions i) 1))))\n            ((string=? mentions-string \"HERE\")\n    \
        \         (for ([user-id filtered-online-users])\n               (vector-set!\
        \ mentions user-id (+ (vector-ref mentions user-id) 1))))\n            (else\
        \ ; Specific IDs like \"id1 id0\"\n             (define id-tokens (string-split\
        \ mentions-string \" \"))\n             (for ([token id-tokens])\n         \
        \      (define user-id (string->number (substring token 2)))\n             \
        \  (vector-set! mentions user-id (+ (vector-ref mentions user-id) 1)))))))\n\
        \n  (vector->list mentions))"
      erlang: "-module(solution).\n-export([count_mentions/2]).\n\ncount_mentions(NumberOfUsers,\
        \ Events) ->\n    Mentions = array:new([{size, NumberOfUsers}, {fixed, true},\
        \ {default, 0}]),\n    UserOfflineUntil = array:new([{size, NumberOfUsers},\
        \ {fixed, true}, {default, 0}]),\n\n    ProcessedEvents = lists:map(fun(Event)\
        \ ->\n        EventType = hd(Event),\n        Timestamp = binary_to_integer(list_to_binary(lists:nth(2,\
        \ Event))),\n        case EventType of\n            \"OFFLINE\" -> {Timestamp,\
        \ 0, Event}; %% 0 priority for OFFLINE\n            _ -> {Timestamp, 1, Event}\
        \          %% 1 priority for MESSAGE\n        end\n    end, Events),\n\n   \
        \ SortedEvents = lists:sort(fun({TsA, PriA, _}, {TsB, PriB, _}) ->\n       \
        \ if TsA =/= TsB -> TsA < TsB;\n           true -> PriA < PriB\n        end\n\
        \    end, ProcessedEvents),\n\n    lists:foldl(fun({CurrentTimestamp, _, OriginalEvent},\
        \ Acc) ->\n        {CurrentMentions, CurrentUserOfflineUntil} = Acc,\n     \
        \   EventType = hd(OriginalEvent),\n\n        case EventType of\n          \
        \  \"OFFLINE\" ->\n                UserId = binary_to_integer(list_to_binary(lists:nth(3,\
        \ OriginalEvent))),\n                NewUserOfflineUntil = array:set(UserId,\
        \ CurrentTimestamp + 60, CurrentUserOfflineUntil),\n                {CurrentMentions,\
        \ NewUserOfflineUntil};\n            _ -> %% MESSAGE event\n               \
        \ MentionsString = lists:nth(3, OriginalEvent),\n\n                OnlineUsersAtCurrentTime\
        \ = lists:filter(fun(I) ->\n                    array:get(I, CurrentUserOfflineUntil)\
        \ =< CurrentTimestamp\n                end, lists:seq(0, NumberOfUsers - 1)),\n\
        \n                case MentionsString of\n                    \"ALL\" ->\n \
        \                       NewMentions = lists:foldl(fun(I, M) ->\n           \
        \                 array:set(I, array:get(I, M) + 1, M)\n                   \
        \     end, CurrentMentions, lists:seq(0, NumberOfUsers - 1));\n            \
        \        \"HERE\" ->\n                        NewMentions = lists:foldl(fun(UserId,\
        \ M) ->\n                            array:set(UserId, array:get(UserId, M)\
        \ + 1, M)\n                        end, CurrentMentions, OnlineUsersAtCurrentTime);\n\
        \                    _ -> %% Specific IDs like \"id1 id0\"\n               \
        \         IdTokens = string:tokens(MentionsString, \" \"),\n               \
        \         NewMentions = lists:foldl(fun(Token, M) ->\n                     \
        \       UserId = binary_to_integer(list_to_binary(string:substr(Token, 3))),\n\
        \                            array:set(UserId, array:get(UserId, M) + 1, M)\n\
        \                        end, CurrentMentions, IdTokens)\n                end,\n\
        \                {NewMentions, CurrentUserOfflineUntil}\n        end\n    end,\
        \ {Mentions, UserOfflineUntil}, SortedEvents),\n\n    {FinalMentions, _} = lists:foldl(fun(I,\
        \ Acc) ->\n        [array:get(I, Mentions) | Acc]\n    end, [], lists:seq(NumberOfUsers\
        \ - 1, 0, -1))."
      elixir: "defmodule Solution do\n  def count_mentions(number_of_users, events)\
        \ do\n    mentions = :array.new([{:size, number_of_users}, {:fixed, true}, {:default,\
        \ 0}])\n    user_offline_until = :array.new([{:size, number_of_users}, {:fixed,\
        \ true}, {:default, 0}])\n\n    processed_events = Enum.map(events, fn event\
        \ ->\n      event_type = hd(event)\n      timestamp = String.to_integer(Enum.at(event,\
        \ 1))\n      priority = if event_type == \"OFFLINE\", do: 0, else: 1\n     \
        \ {timestamp, priority, event}\n    end)\n\n    sorted_events = Enum.sort(processed_events,\
        \ fn {ts_a, pri_a, _}, {ts_b, pri_b, _} ->\n      if ts_a != ts_b, do: ts_a\
        \ < ts_b, else: pri_a < pri_b\n    end)\n\n    {final_mentions, _} = Enum.reduce(sorted_events,\
        \ {mentions, user_offline_until}, fn {current_timestamp, _, original_event},\
        \ {current_mentions, current_user_offline_until} ->\n      event_type = hd(original_event)\n\
        \n      case event_type do\n        \"OFFLINE\" ->\n          user_id = String.to_integer(Enum.at(original_event,\
        \ 2))\n          new_user_offline_until = :array.set(user_id, current_timestamp\
        \ + 60, current_user_offline_until)\n          {current_mentions, new_user_offline_until}\n\
        \        _ -> # MESSAGE event\n          mentions_string = Enum.at(original_event,\
        \ 2)\n\n          online_users_at_current_time = Enum.filter(0..(number_of_users\
        \ - 1), fn i ->\n            :array.get(i, current_user_offline_until) <= current_timestamp\n\
        \          end)\n\n          new_mentions = case mentions_string do\n      \
        \      \"ALL\" ->\n              Enum.reduce(0..(number_of_users - 1), current_mentions,\
        \ fn i, m ->\n                :array.set(i, :array.get(i, m) + 1, m)\n     \
        \         end)\n            \"HERE\" ->\n              Enum.reduce(online_users_at_current_time,\
        \ current_mentions, fn user_id, m ->\n                :array.set(user_id, :array.get(user_id,\
        \ m) + 1, m)\n              end)\n            _ -> # Specific IDs like \"id1\
        \ id0\"\n              id_tokens = String.split(mentions_string, \" \")\n  \
        \            Enum.reduce(id_tokens, current_mentions, fn token, m ->\n     \
        \           user_id = String.to_integer(String.slice(token, 2..))\n        \
        \        :array.set(user_id, :array.get(user_id, m) + 1, m)\n              end)\n\
        \          end\n          {new_mentions, current_user_offline_until}\n     \
        \ end\n    end)\n\n    Enum.map(0..(number_of_users - 1), fn i -> :array.get(i,\
        \ final_mentions) end)\n  end\nend"
    approach: 'The problem requires tracking user online/offline status and counting
      mentions based on event types and timestamps. The core idea is to process events
      chronologically, with a special rule: user status changes (going offline or coming
      back online) at a given timestamp must be processed before any message events
      at the same timestamp. To achieve this, events are first parsed and augmented
      with a priority (e.g., 0 for OFFLINE, 1 for MESSAGE) and then sorted by timestamp,
      then by priority. A `user_offline_until` array tracks when each user will become
      online again, allowing efficient determination of online users at any given moment.'
    time_complexity: Let `N` be the number of events, `U` be the `numberOfUsers`, and
      `M` be the maximum number of individual ID mentions in a single message. The dominant
      operations are sorting the events, which takes `O(N log N)`, and processing each
      event. For each `MESSAGE` event, determining online users takes `O(U)`, and parsing
      mentions (whether `ALL`, `HERE`, or specific IDs) takes `O(U)` or `O(M)`. Thus,
      processing all events takes `O(N * (U + M))`. The overall time complexity is `O(N
      log N + N * (U + M))`. Given the constraints (`N, U, M <= 100`), this is efficient
      enough.
    space_complexity: The space complexity is determined by the data structures used.
      `mentions` and `user_offline_until` arrays each require `O(U)` space. The `processed_events`
      list, which stores parsed events for sorting, requires `O(N)` space. The temporary
      list of `online_users_at_current_time` within a message event processing step
      requires `O(U)` space. Therefore, the total space complexity is `O(N + U)`.
    elapsed_time: 139.6989288330078
    model: gemini-2.5-flash
    generated_at: '2025-12-12 01:09:33 '
  - solutions:
      cpp: "class Solution {\npublic:\n    vector<int> countMentions(int numberOfUsers,\
        \ vector<vector<string>>& events) {\n        vector<int> mentions(numberOfUsers,\
        \ 0);\n        vector<bool> online(numberOfUsers, true);\n        vector<pair<int,\
        \ int>> offlineSchedule;\n        sort(events.begin(), events.end(), [](const\
        \ vector<string>& a, const vector<string>& b) {\n            return stoi(a[1])\
        \ < stoi(b[1]);\n        });\n        for (auto& event : events) {\n       \
        \     int timestamp = stoi(event[1]);\n            if (event[0] == \"OFFLINE\"\
        ) {\n                int userId = stoi(event[2].substr(2));\n              \
        \  online[userId] = false;\n                offlineSchedule.push_back({timestamp\
        \ + 60, userId});\n            } else if (event[0] == \"MESSAGE\") {\n     \
        \           string mentionsStr = event[2];\n                if (mentionsStr\
        \ == \"ALL\") {\n                    for (int i = 0; i < numberOfUsers; i++)\
        \ {\n                        mentions[i]++;\n                    }\n       \
        \         } else if (mentionsStr == \"HERE\") {\n                    for (int\
        \ i = 0; i < numberOfUsers; i++) {\n                        if (online[i]) {\n\
        \                            mentions[i]++;\n                        }\n   \
        \                 }\n                } else {\n                    istringstream\
        \ iss(mentionsStr);\n                    string userIdStr;\n               \
        \     while (iss >> userIdStr) {\n                        int userId = stoi(userIdStr.substr(2));\n\
        \                        mentions[userId]++;\n                    }\n      \
        \          }\n            }\n            while (!offlineSchedule.empty() &&\
        \ offlineSchedule[0].first <= timestamp) {\n                online[offlineSchedule[0].second]\
        \ = true;\n                offlineSchedule.erase(offlineSchedule.begin());\n\
        \            }\n        }\n        return mentions;\n    }\n};"
      java: "class Solution {\n    public int[] countMentions(int numberOfUsers, String[][]\
        \ events) {\n        int[] mentions = new int[numberOfUsers];\n        boolean[]\
        \ online = new boolean[numberOfUsers];\n        Arrays.fill(online, true);\n\
        \        Arrays.sort(events, (a, b) -> Integer.parseInt(a[1]) - Integer.parseInt(b[1]));\n\
        \        List<int[]> offlineSchedule = new ArrayList<>();\n        for (String[]\
        \ event : events) {\n            int timestamp = Integer.parseInt(event[1]);\n\
        \            if (event[0].equals(\"OFFLINE\")) {\n                int userId\
        \ = Integer.parseInt(event[2].substring(2));\n                online[userId]\
        \ = false;\n                offlineSchedule.add(new int[] {timestamp + 60, userId});\n\
        \            } else if (event[0].equals(\"MESSAGE\")) {\n                String\
        \ mentionsStr = event[2];\n                if (mentionsStr.equals(\"ALL\"))\
        \ {\n                    for (int i = 0; i < numberOfUsers; i++) {\n       \
        \                 mentions[i]++;\n                    }\n                } else\
        \ if (mentionsStr.equals(\"HERE\")) {\n                    for (int i = 0; i\
        \ < numberOfUsers; i++) {\n                        if (online[i]) {\n      \
        \                      mentions[i]++;\n                        }\n         \
        \           }\n                } else {\n                    String[] userIds\
        \ = mentionsStr.split(\" \");\n                    for (String userIdStr : userIds)\
        \ {\n                        int userId = Integer.parseInt(userIdStr.substring(2));\n\
        \                        mentions[userId]++;\n                    }\n      \
        \          }\n            }\n            while (!offlineSchedule.isEmpty() &&\
        \ offlineSchedule.get(0)[0] <= timestamp) {\n                online[offlineSchedule.get(0)[1]]\
        \ = true;\n                offlineSchedule.remove(0);\n            }\n     \
        \   }\n        return mentions;\n    }\n}"
      python: "class Solution:\n    def countMentions(self, numberOfUsers: int, events:\
        \ List[List[str]]) -> List[int]:\n        mentions = [0] * numberOfUsers\n \
        \       online = [True] * numberOfUsers\n        offline_schedule = []\n   \
        \     events.sort(key=lambda x: int(x[1]))\n        for event in events:\n \
        \           timestamp = int(event[1])\n            if event[0] == \"OFFLINE\"\
        :\n                user_id = int(event[2][2:])\n                online[user_id]\
        \ = False\n                offline_schedule.append((timestamp + 60, user_id))\n\
        \            elif event[0] == \"MESSAGE\":\n                mentions_str = event[2]\n\
        \                if mentions_str == \"ALL\":\n                    for i in range(numberOfUsers):\n\
        \                        mentions[i] += 1\n                elif mentions_str\
        \ == \"HERE\":\n                    for i in range(numberOfUsers):\n       \
        \                 if online[i]:\n                            mentions[i] +=\
        \ 1\n                else:\n                    for user_id_str in mentions_str.split():\n\
        \                        user_id = int(user_id_str[2:])\n                  \
        \      mentions[user_id] += 1\n            while offline_schedule and offline_schedule[0][0]\
        \ <= timestamp:\n                online[offline_schedule[0][1]] = True\n   \
        \             offline_schedule.pop(0)\n        return mentions"
      python3: "class Solution:\n    def countMentions(self, numberOfUsers: int, events:\
        \ List[List[str]]) -> List[int]:\n        mentions = [0] * numberOfUsers\n \
        \       online = [True] * numberOfUsers\n        offline_schedule = []\n   \
        \     events.sort(key=lambda x: int(x[1]))\n        for event in events:\n \
        \           timestamp = int(event[1])\n            if event[0] == \"OFFLINE\"\
        :\n                user_id = int(event[2][2:])\n                online[user_id]\
        \ = False\n                offline_schedule.append((timestamp + 60, user_id))\n\
        \            elif event[0] == \"MESSAGE\":\n                mentions_str = event[2]\n\
        \                if mentions_str == \"ALL\":\n                    for i in range(numberOfUsers):\n\
        \                        mentions[i] += 1\n                elif mentions_str\
        \ == \"HERE\":\n                    for i in range(numberOfUsers):\n       \
        \                 if online[i]:\n                            mentions[i] +=\
        \ 1\n                else:\n                    for user_id_str in mentions_str.split():\n\
        \                        user_id = int(user_id_str[2:])\n                  \
        \      mentions[user_id] += 1\n            while offline_schedule and offline_schedule[0][0]\
        \ <= timestamp:\n                online[offline_schedule[0][1]] = True\n   \
        \             offline_schedule.pop(0)\n        return mentions"
      c: "typedef struct {\n    int timestamp;\n    int userId;\n} OfflineEvent;\n\n\
        int compare(const void *a, const void *b) {\n    OfflineEvent *event1 = (OfflineEvent\
        \ *)a;\n    OfflineEvent *event2 = (OfflineEvent *)b;\n    return event1->timestamp\
        \ - event2->timestamp;\n}\n\nint* countMentions(int numberOfUsers, char ***events,\
        \ int eventsSize, int *eventsColSize, int *returnSize) {\n    int* mentions\
        \ = (int*)malloc(numberOfUsers * sizeof(int));\n    bool* online = (bool*)malloc(numberOfUsers\
        \ * sizeof(bool));\n    for (int i = 0; i < numberOfUsers; i++) {\n        mentions[i]\
        \ = 0;\n        online[i] = true;\n    }\n    OfflineEvent* offlineSchedule\
        \ = (OfflineEvent*)malloc(eventsSize * sizeof(OfflineEvent));\n    int scheduleSize\
        \ = 0;\n    for (int i = 0; i < eventsSize; i++) {\n        int timestamp =\
        \ atoi(events[i][1]);\n        if (strcmp(events[i][0], \"OFFLINE\") == 0) {\n\
        \            int userId = atoi(events[i][2] + 2);\n            online[userId]\
        \ = false;\n            offlineSchedule[scheduleSize].timestamp = timestamp\
        \ + 60;\n            offlineSchedule[scheduleSize].userId = userId;\n      \
        \      scheduleSize++;\n        } else if (strcmp(events[i][0], \"MESSAGE\"\
        ) == 0) {\n            char* mentionsStr = events[i][2];\n            if (strcmp(mentionsStr,\
        \ \"ALL\") == 0) {\n                for (int j = 0; j < numberOfUsers; j++)\
        \ {\n                    mentions[j]++;\n                }\n            } else\
        \ if (strcmp(mentionsStr, \"HERE\") == 0) {\n                for (int j = 0;\
        \ j < numberOfUsers; j++) {\n                    if (online[j]) {\n        \
        \                mentions[j]++;\n                    }\n                }\n\
        \            } else {\n                char* token = strtok(mentionsStr, \"\
        \ \");\n                while (token != NULL) {\n                    int userId\
        \ = atoi(token + 2);\n                    mentions[userId]++;\n            \
        \        token = strtok(NULL, \" \");\n                }\n            }\n  \
        \      }\n        while (scheduleSize > 0 && offlineSchedule[0].timestamp <=\
        \ timestamp) {\n            online[offlineSchedule[0].userId] = true;\n    \
        \        scheduleSize--;\n            memmove(offlineSchedule, offlineSchedule\
        \ + 1, (scheduleSize) * sizeof(OfflineEvent));\n        }\n    }\n    *returnSize\
        \ = numberOfUsers;\n    return mentions;\n}"
      csharp: "public class Solution {\n    public int[] CountMentions(int numberOfUsers,\
        \ string[][] events) {\n        int[] mentions = new int[numberOfUsers];\n \
        \       bool[] online = new bool[numberOfUsers];\n        for (int i = 0; i\
        \ < numberOfUsers; i++) {\n            online[i] = true;\n        }\n      \
        \  Array.Sort(events, (a, b) => int.Parse(a[1]) - int.Parse(b[1]));\n      \
        \  List<(int, int)> offlineSchedule = new List<(int, int)>();\n        foreach\
        \ (string[] event in events) {\n            int timestamp = int.Parse(event[1]);\n\
        \            if (event[0] == \"OFFLINE\") {\n                int userId = int.Parse(event[2].Substring(2));\n\
        \                online[userId] = false;\n                offlineSchedule.Add((timestamp\
        \ + 60, userId));\n            } else if (event[0] == \"MESSAGE\") {\n     \
        \           string mentionsStr = event[2];\n                if (mentionsStr\
        \ == \"ALL\") {\n                    for (int i = 0; i < numberOfUsers; i++)\
        \ {\n                        mentions[i]++;\n                    }\n       \
        \         } else if (mentionsStr == \"HERE\") {\n                    for (int\
        \ i = 0; i < numberOfUsers; i++) {\n                        if (online[i]) {\n\
        \                            mentions[i]++;\n                        }\n   \
        \                 }\n                } else {\n                    string[]\
        \ userIds = mentionsStr.Split(' ');\n                    foreach (string userIdStr\
        \ in userIds) {\n                        int userId = int.Parse(userIdStr.Substring(2));\n\
        \                        mentions[userId]++;\n                    }\n      \
        \          }\n            }\n            while (offlineSchedule.Count > 0 &&\
        \ offlineSchedule[0].Item1 <= timestamp) {\n                online[offlineSchedule[0].Item2]\
        \ = true;\n                offlineSchedule.RemoveAt(0);\n            }\n   \
        \     }\n        return mentions;\n    }\n}"
      javascript: "var countMentions = function(numberOfUsers, events) {\n    let mentions\
        \ = new Array(numberOfUsers).fill(0);\n    let online = new Array(numberOfUsers).fill(true);\n\
        \    let offlineSchedule = [];\n    events.sort((a, b) => parseInt(a[1]) - parseInt(b[1]));\n\
        \    for (let event of events) {\n        let timestamp = parseInt(event[1]);\n\
        \        if (event[0] === \"OFFLINE\") {\n            let userId = parseInt(event[2].slice(2));\n\
        \            online[userId] = false;\n            offlineSchedule.push([timestamp\
        \ + 60, userId]);\n        } else if (event[0] === \"MESSAGE\") {\n        \
        \    let mentionsStr = event[2];\n            if (mentionsStr === \"ALL\") {\n\
        \                for (let i = 0; i < numberOfUsers; i++) {\n               \
        \     mentions[i]++;\n                }\n            } else if (mentionsStr\
        \ === \"HERE\") {\n                for (let i = 0; i < numberOfUsers; i++) {\n\
        \                    if (online[i]) {\n                        mentions[i]++;\n\
        \                    }\n                }\n            } else {\n          \
        \      let userIds = mentionsStr.split(' ');\n                for (let userIdStr\
        \ of userIds) {\n                    let userId = parseInt(userIdStr.slice(2));\n\
        \                    mentions[userId]++;\n                }\n            }\n\
        \        }\n        while (offlineSchedule.length > 0 && offlineSchedule[0][0]\
        \ <= timestamp) {\n            online[offlineSchedule[0][1]] = true;\n     \
        \       offlineSchedule.shift();\n        }\n    }\n    return mentions;\n};"
      typescript: "function countMentions(numberOfUsers: number, events: string[][]):\
        \ number[] {\n    let mentions: number[] = new Array(numberOfUsers).fill(0);\n\
        \    let online: boolean[] = new Array(numberOfUsers).fill(true);\n    let offlineSchedule:\
        \ [number, number][] = [];\n    events.sort((a, b) => parseInt(a[1]) - parseInt(b[1]));\n\
        \    for (let event of events) {\n        let timestamp: number = parseInt(event[1]);\n\
        \        if (event[0] === \"OFFLINE\") {\n            let userId: number = parseInt(event[2].slice(2));\n\
        \            online[userId] = false;\n            offlineSchedule.push([timestamp\
        \ + 60, userId]);\n        } else if (event[0] === \"MESSAGE\") {\n        \
        \    let mentionsStr: string = event[2];\n            if (mentionsStr === \"\
        ALL\") {\n                for (let i = 0; i < numberOfUsers; i++) {\n      \
        \              mentions[i]++;\n                }\n            } else if (mentionsStr\
        \ === \"HERE\") {\n                for (let i = 0; i < numberOfUsers; i++) {\n\
        \                    if (online[i]) {\n                        mentions[i]++;\n\
        \                    }\n                }\n            } else {\n          \
        \      let userIds: string[] = mentionsStr.split(' ');\n                for\
        \ (let userIdStr of userIds) {\n                    let userId: number = parseInt(userIdStr.slice(2));\n\
        \                    mentions[userId]++;\n                }\n            }\n\
        \        }\n        while (offlineSchedule.length > 0 && offlineSchedule[0][0]\
        \ <= timestamp) {\n            online[offlineSchedule[0][1]] = true;\n     \
        \       offlineSchedule.shift();\n        }\n    }\n    return mentions;\n}"
      php: "function countMentions($numberOfUsers, $events) {\n    $mentions = array_fill(0,\
        \ $numberOfUsers, 0);\n    $online = array_fill(0, $numberOfUsers, true);\n\
        \    $offlineSchedule = [];\n    usort($events, function($a, $b) {\n       \
        \ return intval($a[1]) - intval($b[1]);\n    });\n    foreach ($events as $event)\
        \ {\n        $timestamp = intval($event[1]);\n        if ($event[0] == \"OFFLINE\"\
        ) {\n            $userId = intval(substr($event[2], 2));\n            $online[$userId]\
        \ = false;\n            $offlineSchedule[] = [$timestamp + 60, $userId];\n \
        \       } else if ($event[0] == \"MESSAGE\") {\n            $mentionsStr = $event[2];\n\
        \            if ($mentionsStr == \"ALL\") {\n                for ($i = 0; $i\
        \ < $numberOfUsers; $i++) {\n                    $mentions[$i]++;\n        \
        \        }\n            } else if ($mentionsStr == \"HERE\") {\n           \
        \     for ($i = 0; $i < $numberOfUsers; $i++) {\n                    if ($online[$i])\
        \ {\n                        $mentions[$i]++;\n                    }\n     \
        \           }\n            } else {\n                $userIds = explode(' ',\
        \ $mentionsStr);\n                foreach ($userIds as $userIdStr) {\n     \
        \               $userId = intval(substr($userIdStr, 2));\n                 \
        \   $mentions[$userId]++;\n                }\n            }\n        }\n   \
        \     while (!empty($offlineSchedule) && $offlineSchedule[0][0] <= $timestamp)\
        \ {\n            $online[$offlineSchedule[0][1]] = true;\n            array_shift($offlineSchedule);\n\
        \        }\n    }\n    return $mentions;\n}"
      swift: "func countMentions(_ numberOfUsers: Int, _ events: [[String]]) -> [Int]\
        \ {\n    var mentions = Array(repeating: 0, count: numberOfUsers)\n    var online\
        \ = Array(repeating: true, count: numberOfUsers)\n    var offlineSchedule: [(Int,\
        \ Int)] = []\n    let sortedEvents = events.sorted { Int($0[1])! < Int($1[1])!\
        \ }\n    for event in sortedEvents {\n        let timestamp = Int(event[1])!\n\
        \        if event[0] == \"OFFLINE\" {\n            let userId = Int(event[2].dropFirst(2))!\n\
        \            online[userId] = false\n            offlineSchedule.append((timestamp\
        \ + 60, userId))\n        } else if event[0] == \"MESSAGE\" {\n            let\
        \ mentionsStr = event[2]\n            if mentionsStr == \"ALL\" {\n        \
        \        for i in 0..<numberOfUsers {\n                    mentions[i] += 1\n\
        \                }\n            } else if mentionsStr == \"HERE\" {\n      \
        \          for i in 0..<numberOfUsers {\n                    if online[i] {\n\
        \                        mentions[i] += 1\n                    }\n         \
        \       }\n            } else {\n                let userIds = mentionsStr.components(separatedBy:\
        \ \" \")\n                for userIdStr in userIds {\n                    let\
        \ userId = Int(userIdStr.dropFirst(2))!\n                    mentions[userId]\
        \ += 1\n                }\n            }\n        }\n        while !offlineSchedule.isEmpty,\
        \ offlineSchedule.first!.0 <= timestamp {\n            online[offlineSchedule.first!.1]\
        \ = true\n            offlineSchedule.removeFirst()\n        }\n    }\n    return\
        \ mentions\n}"
      kotlin: "fun countMentions(numberOfUsers: Int, events: Array<Array<String>>):\
        \ IntArray {\n    val mentions = IntArray(numberOfUsers)\n    val online = BooleanArray(numberOfUsers)\
        \ { true }\n    val offlineSchedule = mutableListOf<Pair<Int, Int>>()\n    events.sortBy\
        \ { it[1].toInt() }\n    for (event in events) {\n        val timestamp = event[1].toInt()\n\
        \        if (event[0] == \"OFFLINE\") {\n            val userId = event[2].substring(2).toInt()\n\
        \            online[userId] = false\n            offlineSchedule.add(Pair(timestamp\
        \ + 60, userId))\n        } else if (event[0] == \"MESSAGE\") {\n          \
        \  val mentionsStr = event[2]\n            if (mentionsStr == \"ALL\") {\n \
        \               for (i in 0 until numberOfUsers) {\n                    mentions[i]++\n\
        \                }\n            } else if (mentionsStr == \"HERE\") {\n    \
        \            for (i in 0 until numberOfUsers) {\n                    if (online[i])\
        \ {\n                        mentions[i]++\n                    }\n        \
        \        }\n            } else {\n                val userIds = mentionsStr.split(\"\
        \ \")\n                for (userIdStr in userIds) {\n                    val\
        \ userId = userIdStr.substring(2).toInt()\n                    mentions[userId]++\n\
        \                }\n            }\n        }\n        while (offlineSchedule.isNotEmpty()\
        \ && offlineSchedule.first().first <= timestamp) {\n            online[offlineSchedule.first().second]\
        \ = true\n            offlineSchedule.removeAt(0)\n        }\n    }\n    return\
        \ mentions\n}"
      dart: "List<int> countMentions(int numberOfUsers, List<List<String>> events) {\n\
        \    List<int> mentions = List<int>.filled(numberOfUsers, 0);\n    List<bool>\
        \ online = List<bool>.filled(numberOfUsers, true);\n    List<List<int>> offlineSchedule\
        \ = [];\n    events.sort((a, b) => int.parse(a[1]) - int.parse(b[1]));\n   \
        \ for (List<String> event in events) {\n        int timestamp = int.parse(event[1]);\n\
        \        if (event[0] == \"OFFLINE\") {\n            int userId = int.parse(event[2].substring(2));\n\
        \            online[userId] = false;\n            offlineSchedule.add([timestamp\
        \ + 60, userId]);\n        } else if (event[0] == \"MESSAGE\") {\n         \
        \   String mentionsStr = event[2];\n            if (mentionsStr == \"ALL\")\
        \ {\n                for (int i = 0; i < numberOfUsers; i++) {\n           \
        \         mentions[i]++;\n                }\n            } else if (mentionsStr\
        \ == \"HERE\") {\n                for (int i = 0; i < numberOfUsers; i++) {\n\
        \                    if (online[i]) {\n                        mentions[i]++;\n\
        \                    }\n                }\n            } else {\n          \
        \      List<String> userIds = mentionsStr.split(\" \");\n                for\
        \ (String userIdStr in userIds) {\n                    int userId = int.parse(userIdStr.substring(2));\n\
        \                    mentions[userId]++;\n                }\n            }\n\
        \        }\n        while (offlineSchedule.isNotEmpty && offlineSchedule.first[0]\
        \ <= timestamp) {\n            online[offlineSchedule.first[1]] = true;\n  \
        \          offlineSchedule.removeAt(0);\n        }\n    }\n    return mentions;\n\
        }"
      go: "package main\n\nimport (\n    \"fmt\"\n    \"sort\"\n)\n\nfunc countMentions(numberOfUsers\
        \ int, events [][]string) []int {\n    mentions := make([]int, numberOfUsers)\n\
        \    online := make([]bool, numberOfUsers)\n    for i := range online {\n  \
        \      online[i] = true\n    }\n    offlineSchedule := [][]int{}\n    sort.Slice(events,\
        \ func(i, j int) bool {\n        return events[i][1] < events[j][1]\n    })\n\
        \    for _, event := range events {\n        timestamp, _ := strconv.Atoi(event[1])\n\
        \        if event[0] == \"OFFLINE\" {\n            userId, _ := strconv.Atoi(event[2][2:])\n\
        \            online[userId] = false\n            offlineSchedule = append(offlineSchedule,\
        \ []int{timestamp + 60, userId})\n        } else if event[0] == \"MESSAGE\"\
        \ {\n            mentionsStr := event[2]\n            if mentionsStr == \"ALL\"\
        \ {\n                for i := 0; i < numberOfUsers; i++ {\n                \
        \    mentions[i]++\n                }\n            } else if mentionsStr ==\
        \ \"HERE\" {\n                for i := 0; i < numberOfUsers; i++ {\n       \
        \             if online[i] {\n                        mentions[i]++\n      \
        \              }\n                }\n            } else {\n                userIds\
        \ := strings.Split(mentionsStr, \" \")\n                for _, userIdStr :=\
        \ range userIds {\n                    userId, _ := strconv.Atoi(userIdStr[2:])\n\
        \                    mentions[userId]++\n                }\n            }\n\
        \        }\n        for len(offlineSchedule) > 0 && offlineSchedule[0][0] <=\
        \ timestamp {\n            online[offlineSchedule[0][1]] = true\n          \
        \  offlineSchedule = offlineSchedule[1:]\n        }\n    }\n    return mentions\n\
        }"
      ruby: "def count_mentions(number_of_users, events)\n    mentions = Array.new(number_of_users,\
        \ 0)\n    online = Array.new(number_of_users, true)\n    offline_schedule =\
        \ []\n    events.sort_by! { |event| event[1].to_i }\n    events.each do |event|\n\
        \        timestamp = event[1].to_i\n        if event[0] == \"OFFLINE\"\n   \
        \         user_id = event[2][2..].to_i\n            online[user_id] = false\n\
        \            offline_schedule << [timestamp + 60, user_id]\n        elsif event[0]\
        \ == \"MESSAGE\"\n            mentions_str = event[2]\n            if mentions_str\
        \ == \"ALL\"\n                number_of_users.times do |i|\n               \
        \     mentions[i] += 1\n                end\n            elsif mentions_str\
        \ == \"HERE\"\n                number_of_users.times do |i|\n              \
        \      mentions[i] += 1 if online[i]\n                end\n            else\n\
        \                user_ids = mentions_str.split\n                user_ids.each\
        \ do |user_id_str|\n                    user_id = user_id_str[2..].to_i\n  \
        \                  mentions[user_id] += 1\n                end\n           \
        \ end\n        end\n        offline_schedule.shift while offline_schedule.any?\
        \ && offline_schedule.first[0] <= timestamp\n    end\n    mentions\nend"
      scala: "object Solution {\n    def countMentions(numberOfUsers: Int, events: Array[Array[String]]):\
        \ Array[Int] = {\n        val mentions = Array.fill[Int](numberOfUsers)(0)\n\
        \        val online = Array.fill[Boolean](numberOfUsers)(true)\n        val\
        \ offlineSchedule = scala.collection.mutable.ListBuffer.empty[(Int, Int)]\n\
        \        val sortedEvents = events.sortBy(_.apply(1).toInt)\n        for (event\
        \ <- sortedEvents) {\n            val timestamp = event(1).toInt\n         \
        \   if (event(0) == \"OFFLINE\") {\n                val userId = event(2).drop(2).toInt\n\
        \                online(userId) = false\n                offlineSchedule +=\
        \ ((timestamp + 60, userId))\n            } else if (event(0) == \"MESSAGE\"\
        ) {\n                val mentionsStr = event(2)\n                if (mentionsStr\
        \ == \"ALL\") {\n                    for (i <- 0 until numberOfUsers) {\n  \
        \                      mentions(i) += 1\n                    }\n           \
        \     } else if (mentionsStr == \"HERE\") {\n                    for (i <- 0\
        \ until numberOfUsers) {\n                        if (online(i)) {\n       \
        \                     mentions(i) += 1\n                        }\n        \
        \            }\n                } else {\n                    val userIds =\
        \ mentionsStr.split(\" \")\n                    for (userIdStr <- userIds) {\n\
        \                        val userId = userIdStr.drop(2).toInt\n            \
        \            mentions(userId) += 1\n                    }\n                }\n\
        \            }\n            while (offlineSchedule.nonEmpty && offlineSchedule.head._1\
        \ <= timestamp) {\n                online(offlineSchedule.head._2) = true\n\
        \                offlineSchedule.remove(0)\n            }\n        }\n     \
        \   mentions\n    }\n}"
      rust: "fn count_mentions(number_of_users: usize, events: Vec<Vec<String>>) ->\
        \ Vec<i32> {\n    let mut mentions: Vec<i32> = vec![0; number_of_users];\n \
        \   let mut online: Vec<bool> = vec![true; number_of_users];\n    let mut offline_schedule:\
        \ Vec<(i32, usize)> = Vec::new();\n    let mut sorted_events: Vec<Vec<String>>\
        \ = events;\n    sorted_events.sort_by_key(|event| event[1].parse::<i32>().unwrap());\n\
        \    for event in sorted_events {\n        let timestamp: i32 = event[1].parse().unwrap();\n\
        \        if event[0] == \"OFFLINE\" {\n            let user_id: usize = event[2][2..].parse().unwrap();\n\
        \            online[user_id] = false;\n            offline_schedule.push((timestamp\
        \ + 60, user_id));\n        } else if event[0] == \"MESSAGE\" {\n          \
        \  let mentions_str = &event[2];\n            if mentions_str == \"ALL\" {\n\
        \                for i in 0..number_of_users {\n                    mentions[i]\
        \ += 1;\n                }\n            } else if mentions_str == \"HERE\" {\n\
        \                for i in 0..number_of_users {\n                    if online[i]\
        \ {\n                        mentions[i] += 1;\n                    }\n    \
        \            }\n            } else {\n                let user_ids: Vec<&str>\
        \ = mentions_str.split(\" \").collect();\n                for user_id_str in\
        \ user_ids {\n                    let user_id: usize = user_id_str[2..].parse().unwrap();\n\
        \                    mentions[user_id] += 1;\n                }\n          \
        \  }\n        }\n        while let Some((timestamp, user_id)) = offline_schedule.first()\
        \ {\n            if *timestamp <= timestamp {\n                online[*user_id]\
        \ = true;\n                offline_schedule.remove(0);\n            } else {\n\
        \                break;\n            }\n        }\n    }\n    mentions\n}"
      racket: "(define (count-mentions number-of-users events)\n  (let ((mentions (make-vector\
        \ number-of-users 0))\n        (online (make-vector number-of-users #t))\n \
        \       (offline-schedule '()))\n    (define (sort-events events)\n      (sort\
        \ events (lambda (x y) (< (string->number (cadr x)) (string->number (cadr y))))))\n\
        \    (define sorted-events (sort-events events))\n    (for-each (lambda (event)\n\
        \                (let ((timestamp (string->number (cadr event))))\n        \
        \          (cond ((equal? (car event) \"OFFLINE\")\n                       \
        \  (let ((user-id (string->number (substring (caddr event) 2))))\n         \
        \                  (vector-set! online user-id #f)\n                       \
        \    (set! offline-schedule (cons (cons (+ timestamp 60) user-id) offline-schedule))))\n\
        \                        ((equal? (car event) \"MESSAGE\")\n               \
        \          (let ((mentions-str (caddr event)))\n                           (cond\
        \ ((equal? mentions-str \"ALL\")\n                                  (for ((i\
        \ (range number-of-users)))\n                                    (vector-set!\
        \ mentions i (+ (vector-ref mentions i) 1))))\n                            \
        \     ((equal? mentions-str \"HERE\")\n                                  (for\
        \ ((i (range number-of-users)))\n                                    (when (vector-ref\
        \ online i)\n                                      (vector-set! mentions i (+\
        \ (vector-ref mentions i) 1)))))\n                                 (else\n \
        \                                 (let ((user-ids (string-split mentions-str\
        \ \" \" )))\n                                    (for-each (lambda (user-id-str)\n\
        \                                                (let ((user-id (string->number\
        \ (substring user-id-str 2))))\n                                           \
        \       (vector-set! mentions user-id (+ (vector-ref mentions user-id) 1))))\n\
        \                                      user-ids))))))\n                  (when\
        \ (and offline-schedule (<= (caar offline-schedule) timestamp))\n          \
        \          (let ((user-id (cdar offline-schedule)))\n                      (vector-set!\
        \ online user-id #t)\n                      (set! offline-schedule (cdr offline-schedule))))))\n\
        \              sorted-events)\n    mentions))"
      erlang: "count_mentions(Number_of_users, Events) ->\n    lists:foldl(fun({\"OFFLINE\"\
        , Timestamp, User_id}, {Mentions, Online, Offline_schedule}) ->\n          \
        \              {Mentions, lists:keyreplace(list_to_integer(string:substr(User_id,\
        \ 2)), 1, Online, {list_to_integer(string:substr(User_id, 2)), false}), [{list_to_integer(Timestamp)\
        \ + 60, list_to_integer(string:substr(User_id, 2))} | Offline_schedule]};\n\
        \                    ({\"MESSAGE\", Timestamp, Mentions_str}, {Mentions, Online,\
        \ Offline_schedule}) ->\n                        case Mentions_str of\n    \
        \                        \"ALL\" ->\n                                {lists:map(fun(I)\
        \ -> I + 1 end, Mentions), Online, Offline_schedule};\n                    \
        \        \"HERE\" ->\n                                {lists:map(fun({I, Is_online})\
        \ -> if Is_online -> I + 1; true -> I end, lists:zip(Mentions, Online)), Online,\
        \ Offline_schedule};\n                            _ ->\n                   \
        \             {lists:map(fun({I, User_id_str}) -> if lists:member(User_id_str,\
        \ string:tokens(Mentions_str, \" \")) -> I + 1; true -> I end, lists:zip(Mentions,\
        \ lists:map(fun(X) -> string:substr(X, 2) end, lists:seq(0, Number_of_users\
        \ - 1)))), Online, Offline_schedule}\n                    end,\n           \
        \         {lists:duplicate(Number_of_users, 0), lists:duplicate(Number_of_users,\
        \ true), []},\n                    lists:sort(fun({_, Timestamp1, _}, {_, Timestamp2,\
        \ _}) -> Timestamp1 =< Timestamp2 end, Events))."
      elixir: "def count_mentions(number_of_users, events) do\n  events\n  |> Enum.sort_by(&Enum.at(&1,\
        \ 1))\n  |> Enum.reduce({Enum.duplicate(number_of_users, 0), Enum.duplicate(number_of_users,\
        \ true), []}, fn event, {mentions, online, offline_schedule} ->\n      case\
        \ event do\n        [\"OFFLINE\", timestamp, user_id] ->\n          {mentions,\
        \ List.update_at(online, String.to_integer(user_id) - 2, fn _ -> false end),\
        \ [{String.to_integer(timestamp) + 60, String.to_integer(user_id) - 2} | offline_schedule]}\n\
        \        [\"MESSAGE\", timestamp, mentions_str] ->\n          cond do\n    \
        \        mentions_str == \"ALL\" ->\n              {Enum.map(mentions, &(&1\
        \ + 1)), online, offline_schedule}\n            mentions_str == \"HERE\" ->\n\
        \              {Enum.with_index(online)\n               |> Enum.map(fn {index,\
        \ is_online} -> if is_online, do: Enum.at(mentions, index) + 1, else: Enum.at(mentions,\
        \ index)), online, offline_schedule}\n            true ->\n              {Enum.with_index(mentions)\n\
        \               |> Enum.map(fn {index, mention} -> if Enum.member?(String.split(mentions_str,\
        \ \" \"), \"id#{index + 1}\"), do: mention + 1, else: mention), online, offline_schedule}\n\
        \          end\n      end\n    end)\n  |> elem(0)\nend"
    approach: The algorithm starts by sorting the events based on their timestamps.
      Then, it processes each event in order. For each event, it checks if the event
      is a message or an offline event. If it's a message event, it parses the mentions
      string and increments the mention count for each mentioned user. If it's an offline
      event, it marks the user as offline and schedules them to come back online after
      60 time units. The algorithm maintains two sets for offline and online user IDs
      to efficiently check the status of each user. The key intuition is to process
      the events in order and maintain the status of each user to accurately count the
      mentions.
    time_complexity: The time complexity of the algorithm is O(n log n + n * m) where
      n is the number of events and m is the maximum number of mentions in a message
      event. This is because the algorithm sorts the events, which takes O(n log n)
      time, and then processes each event, which takes O(n * m) time in the worst case.
    space_complexity: The space complexity of the algorithm is O(n + m) where n is the
      number of events and m is the number of users. This is because the algorithm maintains
      two sets for offline and online user IDs, which takes O(m) space, and a list to
      store the mention counts for each user, which takes O(m) space. The algorithm
      also uses a list to store the sorted events, which takes O(n) space.
    elapsed_time: 18.11876678466797
    model: llama-3.3-70b-versatile
    generated_at: '2025-12-12 01:09:51 '
---

## Problem #3433: Count Mentions Per User

**Difficulty:** Medium

**Topics:** Array, Math, Sorting, Simulation

## Problem Description

<p>You are given an integer <code>numberOfUsers</code> representing the total number of users and an array <code>events</code> of size <code>n x 3</code>.</p>

<p>Each <code inline="">events[i]</code> can be either of the following two types:</p>

<ol>
	<li><strong>Message Event:</strong> <code>[&quot;MESSAGE&quot;, &quot;timestamp<sub>i</sub>&quot;, &quot;mentions_string<sub>i</sub>&quot;]</code>

	<ul>
		<li>This event indicates that a set of users was mentioned in a message at <code>timestamp<sub>i</sub></code>.</li>
		<li>The <code>mentions_string<sub>i</sub></code> string can contain one of the following tokens:
		<ul>
			<li><code>id&lt;number&gt;</code>: where <code>&lt;number&gt;</code> is an integer in range <code>[0,numberOfUsers - 1]</code>. There can be <strong>multiple</strong> ids separated by a single whitespace and may contain duplicates. This can mention even the offline users.</li>
			<li><code>ALL</code>: mentions <strong>all</strong> users.</li>
			<li><code>HERE</code>: mentions all <strong>online</strong> users.</li>
		</ul>
		</li>
	</ul>
	</li>
	<li><strong>Offline Event:</strong> <code>[&quot;OFFLINE&quot;, &quot;timestamp<sub>i</sub>&quot;, &quot;id<sub>i</sub>&quot;]</code>
	<ul>
		<li>This event indicates that the user <code>id<sub>i</sub></code> had become offline at <code>timestamp<sub>i</sub></code> for <strong>60 time units</strong>. The user will automatically be online again at time <code>timestamp<sub>i</sub> + 60</code>.</li>
	</ul>
	</li>
</ol>

<p>Return an array <code>mentions</code> where <code>mentions[i]</code> represents the number of mentions the user with id <code>i</code> has across all <code>MESSAGE</code> events.</p>

<p>All users are initially online, and if a user goes offline or comes back online, their status change is processed <em>before</em> handling any message event that occurs at the same timestamp.</p>

<p><strong>Note </strong>that a user can be mentioned <strong>multiple</strong> times in a <strong>single</strong> message event, and each mention should be counted <strong>separately</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">numberOfUsers = 2, events = [[&quot;MESSAGE&quot;,&quot;10&quot;,&quot;id1 id0&quot;],[&quot;OFFLINE&quot;,&quot;11&quot;,&quot;0&quot;],[&quot;MESSAGE&quot;,&quot;71&quot;,&quot;HERE&quot;]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[2,2]</span></p>

<p><strong>Explanation:</strong></p>

<p>Initially, all users are online.</p>

<p>At timestamp 10, <code>id1</code> and <code>id0</code> are mentioned. <code>mentions = [1,1]</code></p>

<p>At timestamp 11, <code>id0</code> goes <strong>offline.</strong></p>

<p>At timestamp 71, <code>id0</code> comes back <strong>online</strong> and <code>&quot;HERE&quot;</code> is mentioned. <code>mentions = [2,2]</code></p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">numberOfUsers = 2, events = [[&quot;MESSAGE&quot;,&quot;10&quot;,&quot;id1 id0&quot;],[&quot;OFFLINE&quot;,&quot;11&quot;,&quot;0&quot;],[&quot;MESSAGE&quot;,&quot;12&quot;,&quot;ALL&quot;]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[2,2]</span></p>

<p><strong>Explanation:</strong></p>

<p>Initially, all users are online.</p>

<p>At timestamp 10, <code>id1</code> and <code>id0</code> are mentioned. <code>mentions = [1,1]</code></p>

<p>At timestamp 11, <code>id0</code> goes <strong>offline.</strong></p>

<p>At timestamp 12, <code>&quot;ALL&quot;</code> is mentioned. This includes offline users, so both <code>id0</code> and <code>id1</code> are mentioned. <code>mentions = [2,2]</code></p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">numberOfUsers = 2, events = [[&quot;OFFLINE&quot;,&quot;10&quot;,&quot;0&quot;],[&quot;MESSAGE&quot;,&quot;12&quot;,&quot;HERE&quot;]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[0,1]</span></p>

<p><strong>Explanation:</strong></p>

<p>Initially, all users are online.</p>

<p>At timestamp 10, <code>id0</code> goes <strong>offline.</strong></p>

<p>At timestamp 12, <code>&quot;HERE&quot;</code> is mentioned. Because <code>id0</code> is still offline, they will not be mentioned. <code>mentions = [0,1]</code></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= numberOfUsers &lt;= 100</code></li>
	<li><code>1 &lt;= events.length &lt;= 100</code></li>
	<li><code>events[i].length == 3</code></li>
	<li><code>events[i][0]</code> will be one of <code>MESSAGE</code> or <code>OFFLINE</code>.</li>
	<li><code>1 &lt;= int(events[i][1]) &lt;= 10<sup>5</sup></code></li>
	<li>The number of <code>id&lt;number&gt;</code> mentions in any <code>&quot;MESSAGE&quot;</code> event is between <code>1</code> and <code>100</code>.</li>
	<li><code>0 &lt;= &lt;number&gt; &lt;= numberOfUsers - 1</code></li>
	<li>It is <strong>guaranteed</strong> that the user id referenced in the <code>OFFLINE</code> event is <strong>online</strong> at the time the event occurs.</li>
</ul>


## Hints

1. Sort events by timestamp and then process each event.

2. Maintain two sets for offline and online user IDs.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-12-12 01:09:33 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem requires tracking user online/offline status and counting mentions based on event types and timestamps. The core idea is to process events chronologically, with a special rule: user status changes (going offline or coming back online) at a given timestamp must be processed before any message events at the same timestamp. To achieve this, events are first parsed and augmented with a priority (e.g., 0 for OFFLINE, 1 for MESSAGE) and then sorted by timestamp, then by priority. A `user_offline_until` array tracks when each user will become online again, allowing efficient determination of online users at any given moment.

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
#include <algorithm>
#include <tuple>
#include <sstream>

class Solution {
public:
    std::vector<int> countMentions(int numberOfUsers, std::vector<std::vector<std::string>>& events) {
        std::vector<int> mentions(numberOfUsers, 0);
        std::vector<int> userOfflineUntil(numberOfUsers, 0); // Timestamp when user becomes online. 0 means online from start.

        // Prepare events for sorting: (timestamp, priority, original_event_data)
        // Priority: 0 for OFFLINE (status change), 1 for MESSAGE (action)
        std::vector<std::tuple<int, int, std::vector<std::string>>> processedEvents;
        for (const auto& event : events) {
            int timestamp = std::stoi(event[1]);
            if (event[0] == "OFFLINE") {
                processedEvents.emplace_back(timestamp, 0, event);
            } else { // MESSAGE
                processedEvents.emplace_back(timestamp, 1, event);
            }
        }

        // Sort events by timestamp, then by priority (OFFLINE before MESSAGE)
        std::sort(processedEvents.begin(), processedEvents.end());

        for (const auto& eventTuple : processedEvents) {
            int currentTimestamp = std::get<0>(eventTuple);
            const auto& originalEvent = std::get<2>(eventTuple);
            std::string eventType = originalEvent[0];

            if (eventType == "OFFLINE") {
                int userId = std::stoi(originalEvent[2]);
                userOfflineUntil[userId] = currentTimestamp + 60;
            } else { // MESSAGE event
                std::string mentionsString = originalEvent[2];

                // Determine current online users *at this timestamp*
                std::vector<int> onlineUsersAtCurrentTime;
                for (int i = 0; i < numberOfUsers; ++i) {
                    if (userOfflineUntil[i] <= currentTimestamp) {
                        onlineUsersAtCurrentTime.push_back(i);
                    }
                }

                if (mentionsString == "ALL") {
                    for (int i = 0; i < numberOfUsers; ++i) {
                        mentions[i]++;
                    }
                } else if (mentionsString == "HERE") {
                    for (int userId : onlineUsersAtCurrentTime) {
                        mentions[userId]++;
                    }
                } else { // Specific IDs like "id1 id0"
                    std::stringstream ss(mentionsString);
                    std::string token;
                    while (ss >> token) {
                        // Extract number after "id"
                        int userId = std::stoi(token.substr(2)); 
                        mentions[userId]++;
                    }
                }
            }
        }

        return mentions;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

class Solution {

    // Custom Event class to hold parsed event data and enable custom sorting
    static class Event implements Comparable<Event> {
        int timestamp;
        int priority; // 0 for OFFLINE, 1 for MESSAGE
        String type;
        String detail1;

        public Event(String[] originalEvent) {
            this.type = originalEvent[0];
            this.timestamp = Integer.parseInt(originalEvent[1]);
            this.priority = (this.type.equals("OFFLINE")) ? 0 : 1;
            this.detail1 = originalEvent[2]; // mentions_string or user_id
        }

        @Override
        public int compareTo(Event other) {
            if (this.timestamp != other.timestamp) {
                return Integer.compare(this.timestamp, other.timestamp);
            } else {
                return Integer.compare(this.priority, other.priority);
            }
        }
    }

    public int[] countMentions(int numberOfUsers, List<List<String>> events) {
        int[] mentions = new int[numberOfUsers];
        // userOfflineUntil[i] stores the timestamp when user i will become online.
        // If userOfflineUntil[i] <= currentTimestamp, user i is online.
        // Initially, all users are online, so they are "online since time 0".
        int[] userOfflineUntil = new int[numberOfUsers]; 
        Arrays.fill(userOfflineUntil, 0);

        List<Event> processedEvents = new ArrayList<>();
        for (List<String> eventList : events) {
            processedEvents.add(new Event(eventList.toArray(new String[0])));
        }

        Collections.sort(processedEvents);

        for (Event event : processedEvents) {
            int currentTimestamp = event.timestamp;
            String eventType = event.type;

            if (eventType.equals("OFFLINE")) {
                int userId = Integer.parseInt(event.detail1);
                userOfflineUntil[userId] = currentTimestamp + 60;
            } else { // MESSAGE event
                String mentionsString = event.detail1;

                // Determine current online users *at this timestamp*
                List<Integer> onlineUsersAtCurrentTime = new ArrayList<>();
                for (int i = 0; i < numberOfUsers; ++i) {
                    if (userOfflineUntil[i] <= currentTimestamp) {
                        onlineUsersAtCurrentTime.add(i);
                    }
                }

                if (mentionsString.equals("ALL")) {
                    for (int i = 0; i < numberOfUsers; ++i) {
                        mentions[i]++;
                    }
                } else if (mentionsString.equals("HERE")) {
                    for (int userId : onlineUsersAtCurrentTime) {
                        mentions[userId]++;
                    }
                } else { // Specific IDs like "id1 id0"
                    String[] idTokens = mentionsString.split(" ");
                    for (String token : idTokens) {
                        // Extract number after "id"
                        int userId = Integer.parseInt(token.substring(2)); 
                        mentions[userId]++;
                    }
                }
            }
        }

        return mentions;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
from typing import List

class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        mentions = [0] * numberOfUsers
        # user_offline_until[i] stores the timestamp when user i will become online.
        # If user_offline_until[i] <= current_timestamp, user i is online.
        # Initially, all users are online, so they are "online since time 0".
        user_offline_until = [0] * numberOfUsers 

        # Prepare events for sorting: (timestamp, priority, original_event_data)
        # Priority: 0 for OFFLINE (status change), 1 for MESSAGE (action)
        processed_events = []
        for event in events:
            event_type = event[0]
            timestamp = int(event[1])
            if event_type == "OFFLINE":
                processed_events.append((timestamp, 0, event)) # 0 priority for OFFLINE
            else: # MESSAGE
                processed_events.append((timestamp, 1, event)) # 1 priority for MESSAGE

        # Sort events by timestamp, then by priority (OFFLINE before MESSAGE)
        processed_events.sort()

        for current_timestamp, _, original_event in processed_events:
            event_type = original_event[0]

            if event_type == "OFFLINE":
                user_id = int(original_event[2])
                user_offline_until[user_id] = current_timestamp + 60
            else: # MESSAGE event
                mentions_string = original_event[2]

                # Determine current online users *at this timestamp*
                online_users_at_current_time = []
                for i in range(numberOfUsers):
                    if user_offline_until[i] <= current_timestamp:
                        online_users_at_current_time.append(i)

                if mentions_string == "ALL":
                    for i in range(numberOfUsers):
                        mentions[i] += 1
                elif mentions_string == "HERE":
                    for user_id in online_users_at_current_time:
                        mentions[user_id] += 1
                else: # Specific IDs like "id1 id0"
                    id_tokens = mentions_string.split()
                    for token in id_tokens:
                        user_id = int(token[2:]) # Extract number after "id"
                        mentions[user_id] += 1

        return mentions
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
from typing import List

class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        mentions = [0] * numberOfUsers
        # user_offline_until[i] stores the timestamp when user i will become online.
        # If user_offline_until[i] <= current_timestamp, user i is online.
        # Initially, all users are online, so they are "online since time 0".
        user_offline_until = [0] * numberOfUsers 

        # Prepare events for sorting: (timestamp, priority, original_event_data)
        # Priority: 0 for OFFLINE (status change), 1 for MESSAGE (action)
        processed_events = []
        for event in events:
            event_type = event[0]
            timestamp = int(event[1])
            if event_type == "OFFLINE":
                processed_events.append((timestamp, 0, event)) # 0 priority for OFFLINE
            else: # MESSAGE
                processed_events.append((timestamp, 1, event)) # 1 priority for MESSAGE

        # Sort events by timestamp, then by priority (OFFLINE before MESSAGE)
        processed_events.sort()

        for current_timestamp, _, original_event in processed_events:
            event_type = original_event[0]

            if event_type == "OFFLINE":
                user_id = int(original_event[2])
                user_offline_until[user_id] = current_timestamp + 60
            else: # MESSAGE event
                mentions_string = original_event[2]

                # Determine current online users *at this timestamp*
                online_users_at_current_time = []
                for i in range(numberOfUsers):
                    if user_offline_until[i] <= current_timestamp:
                        online_users_at_current_time.append(i)

                if mentions_string == "ALL":
                    for i in range(numberOfUsers):
                        mentions[i] += 1
                elif mentions_string == "HERE":
                    for user_id in online_users_at_current_time:
                        mentions[user_id] += 1
                else: # Specific IDs like "id1 id0"
                    id_tokens = mentions_string.split()
                    for token in id_tokens:
                        user_id = int(token[2:]) # Extract number after "id"
                        mentions[user_id] += 1

        return mentions
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

// Helper struct to hold event data for sorting
typedef struct {
    int timestamp;
    int priority; // 0 for OFFLINE, 1 for MESSAGE
    char** originalEvent; // Pointer to the original string array
} ProcessedEvent;

// Comparison function for qsort
int compareEvents(const void* a, const void* b) {
    ProcessedEvent* eventA = (ProcessedEvent*)a;
    ProcessedEvent* eventB = (ProcessedEvent*)b;

    if (eventA->timestamp != eventB->timestamp) {
        return eventA->timestamp - eventB->timestamp;
    } else {
        return eventA->priority - eventB->priority;
    }
}

/**
 * Note: The LeetCode C environment usually provides a way to handle dynamic arrays of strings.
 * For this problem, `events` is `char***` (array of arrays of strings).
 * The return type is `int*` (array of integers).
 * The caller is responsible for freeing the returned array.
 */
int* countMentions(int numberOfUsers, char*** events, int eventsSize, int* eventsColSize, int* returnSize) {
    int* mentions = (int*)calloc(numberOfUsers, sizeof(int));
    int* userOfflineUntil = (int*)calloc(numberOfUsers, sizeof(int)); // Timestamp when user becomes online. 0 means online from start.

    ProcessedEvent* processedEvents = (ProcessedEvent*)malloc(eventsSize * sizeof(ProcessedEvent));
    for (int i = 0; i < eventsSize; ++i) {
        processedEvents[i].originalEvent = events[i];
        processedEvents[i].timestamp = atoi(events[i][1]);
        if (strcmp(events[i][0], "OFFLINE") == 0) {
            processedEvents[i].priority = 0;
        } else { // MESSAGE
            processedEvents[i].priority = 1;
        }
    }

    qsort(processedEvents, eventsSize, sizeof(ProcessedEvent), compareEvents);

    for (int i = 0; i < eventsSize; ++i) {
        int currentTimestamp = processedEvents[i].timestamp;
        char** originalEvent = processedEvents[i].originalEvent;
        char* eventType = originalEvent[0];

        if (strcmp(eventType, "OFFLINE") == 0) {
            int userId = atoi(originalEvent[2]);
            userOfflineUntil[userId] = currentTimestamp + 60;
        } else { // MESSAGE event
            char* mentionsString = originalEvent[2];

            // Determine current online users *at this timestamp*
            // Using a dynamic array for online users. Max size is numberOfUsers.
            int* onlineUsersAtCurrentTime = (int*)malloc(numberOfUsers * sizeof(int));
            int onlineUsersCount = 0;
            for (int j = 0; j < numberOfUsers; ++j) {
                if (userOfflineUntil[j] <= currentTimestamp) {
                    onlineUsersAtCurrentTime[onlineUsersCount++] = j;
                }
            }

            if (strcmp(mentionsString, "ALL") == 0) {
                for (int j = 0; j < numberOfUsers; ++j) {
                    mentions[j]++;
                }
            } else if (strcmp(mentionsString, "HERE") == 0) {
                for (int j = 0; j < onlineUsersCount; ++j) {
                    mentions[onlineUsersAtCurrentTime[j]]++;
                }
            } else { // Specific IDs like "id1 id0"
                char* tempMentionsString = strdup(mentionsString); // Duplicate to tokenize
                char* token = strtok(tempMentionsString, " ");
                while (token != NULL) {
                    // Extract number after "id"
                    int userId = atoi(token + 2); 
                    mentions[userId]++;
                    token = strtok(NULL, " ");
                }
                free(tempMentionsString);
            }
            free(onlineUsersAtCurrentTime);
        }
    }

    free(processedEvents);
    free(userOfflineUntil);
    *returnSize = numberOfUsers;
    return mentions;
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

    // Custom Event class to hold parsed event data and enable custom sorting
    public class Event : IComparable<Event> {
        public int Timestamp { get; set; }
        public int Priority { get; set; } // 0 for OFFLINE, 1 for MESSAGE
        public string Type { get; set; }
        public string Detail1 { get; set; }

        public Event(IList<string> originalEvent) {
            this.Type = originalEvent[0];
            this.Timestamp = int.Parse(originalEvent[1]);
            this.Priority = (this.Type == "OFFLINE") ? 0 : 1;
            this.Detail1 = originalEvent[2]; // mentions_string or user_id
        }

        public int CompareTo(Event other) {
            if (this.Timestamp != other.Timestamp) {
                return this.Timestamp.CompareTo(other.Timestamp);
            } else {
                return this.Priority.CompareTo(other.Priority);
            }
        }
    }

    public int[] CountMentions(int numberOfUsers, IList<IList<string>> events) {
        int[] mentions = new int[numberOfUsers];
        // userOfflineUntil[i] stores the timestamp when user i will become online.
        // If userOfflineUntil[i] <= currentTimestamp, user i is online.
        // Initially, all users are online, so they are "online since time 0".
        int[] userOfflineUntil = new int[numberOfUsers]; 
        // Arrays are default initialized to 0 in C#, so no explicit fill needed.

        List<Event> processedEvents = new List<Event>();
        foreach (var eventList in events) {
            processedEvents.Add(new Event(eventList));
        }

        processedEvents.Sort();

        foreach (Event eventItem in processedEvents) {
            int currentTimestamp = eventItem.Timestamp;
            string eventType = eventItem.Type;

            if (eventType == "OFFLINE") {
                int userId = int.Parse(eventItem.Detail1);
                userOfflineUntil[userId] = currentTimestamp + 60;
            } else { // MESSAGE event
                string mentionsString = eventItem.Detail1;

                // Determine current online users *at this timestamp*
                List<int> onlineUsersAtCurrentTime = new List<int>();
                for (int i = 0; i < numberOfUsers; ++i) {
                    if (userOfflineUntil[i] <= currentTimestamp) {
                        onlineUsersAtCurrentTime.Add(i);
                    }
                }

                if (mentionsString == "ALL") {
                    for (int i = 0; i < numberOfUsers; ++i) {
                        mentions[i]++;
                    }
                } else if (mentionsString == "HERE") {
                    foreach (int userId in onlineUsersAtCurrentTime) {
                        mentions[userId]++;
                    }
                } else { // Specific IDs like "id1 id0"
                    string[] idTokens = mentionsString.Split(' ');
                    foreach (string token in idTokens) {
                        // Extract number after "id"
                        int userId = int.Parse(token.Substring(2)); 
                        mentions[userId]++;
                    }
                }
            }
        }

        return mentions;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
/**
 * @param {number} numberOfUsers
 * @param {string[][]} events
 * @return {number[]}
 */
var countMentions = function(numberOfUsers, events) {
    let mentions = new Array(numberOfUsers).fill(0);
    // userOfflineUntil[i] stores the timestamp when user i will become online.
    // If userOfflineUntil[i] <= currentTimestamp, user i is online.
    // Initially, all users are online, so they are "online since time 0".
    let userOfflineUntil = new Array(numberOfUsers).fill(0); 

    // Prepare events for sorting: [timestamp, priority, original_event_data]
    // Priority: 0 for OFFLINE (status change), 1 for MESSAGE (action)
    let processedEvents = [];
    for (const event of events) {
        const eventType = event[0];
        const timestamp = parseInt(event[1]);
        if (eventType === "OFFLINE") {
            processedEvents.push([timestamp, 0, event]); // 0 priority for OFFLINE
        } else { // MESSAGE
            processedEvents.push([timestamp, 1, event]); // 1 priority for MESSAGE
        }
    }

    // Sort events by timestamp, then by priority (OFFLINE before MESSAGE)
    processedEvents.sort((a, b) => {
        if (a[0] !== b[0]) {
            return a[0] - b[0];
        } else {
            return a[1] - b[1];
        }
    });

    for (const eventTuple of processedEvents) {
        const currentTimestamp = eventTuple[0];
        const originalEvent = eventTuple[2];
        const eventType = originalEvent[0];

        if (eventType === "OFFLINE") {
            const userId = parseInt(originalEvent[2]);
            userOfflineUntil[userId] = currentTimestamp + 60;
        } else { // MESSAGE event
            const mentionsString = originalEvent[2];

            // Determine current online users *at this timestamp*
            let onlineUsersAtCurrentTime = [];
            for (let i = 0; i < numberOfUsers; ++i) {
                if (userOfflineUntil[i] <= currentTimestamp) {
                    onlineUsersAtCurrentTime.push(i);
                }
            }

            if (mentionsString === "ALL") {
                for (let i = 0; i < numberOfUsers; ++i) {
                    mentions[i]++;
                }
            } else if (mentionsString === "HERE") {
                for (const userId of onlineUsersAtCurrentTime) {
                    mentions[userId]++;
                }
            } else { // Specific IDs like "id1 id0"
                const idTokens = mentionsString.split(' ');
                for (const token of idTokens) {
                    // Extract number after "id"
                    const userId = parseInt(token.substring(2)); 
                    mentions[userId]++;
                }
            }
        }
    }

    return mentions;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function countMentions(numberOfUsers: number, events: string[][]): number[] {
    const mentions: number[] = new Array(numberOfUsers).fill(0);
    // userOfflineUntil[i] stores the timestamp when user i will become online.
    // If userOfflineUntil[i] <= currentTimestamp, user i is online.
    // Initially, all users are online, so they are "online since time 0".
    const userOfflineUntil: number[] = new Array(numberOfUsers).fill(0); 

    // Prepare events for sorting: [timestamp, priority, original_event_data]
    // Priority: 0 for OFFLINE (status change), 1 for MESSAGE (action)
    const processedEvents: [number, number, string[]][] = [];
    for (const event of events) {
        const eventType: string = event[0];
        const timestamp: number = parseInt(event[1]);
        if (eventType === "OFFLINE") {
            processedEvents.push([timestamp, 0, event]); // 0 priority for OFFLINE
        } else { // MESSAGE
            processedEvents.push([timestamp, 1, event]); // 1 priority for MESSAGE
        }
    }

    // Sort events by timestamp, then by priority (OFFLINE before MESSAGE)
    processedEvents.sort((a, b) => {
        if (a[0] !== b[0]) {
            return a[0] - b[0];
        } else {
            return a[1] - b[1];
        }
    });

    for (const eventTuple of processedEvents) {
        const currentTimestamp: number = eventTuple[0];
        const originalEvent: string[] = eventTuple[2];
        const eventType: string = originalEvent[0];

        if (eventType === "OFFLINE") {
            const userId: number = parseInt(originalEvent[2]);
            userOfflineUntil[userId] = currentTimestamp + 60;
        } else { // MESSAGE event
            const mentionsString: string = originalEvent[2];

            // Determine current online users *at this timestamp*
            const onlineUsersAtCurrentTime: number[] = [];
            for (let i = 0; i < numberOfUsers; ++i) {
                if (userOfflineUntil[i] <= currentTimestamp) {
                    onlineUsersAtCurrentTime.push(i);
                }
            }

            if (mentionsString === "ALL") {
                for (let i = 0; i < numberOfUsers; ++i) {
                    mentions[i]++;
                }
            } else if (mentionsString === "HERE") {
                for (const userId of onlineUsersAtCurrentTime) {
                    mentions[userId]++;
                }
            } else { // Specific IDs like "id1 id0"
                const idTokens: string[] = mentionsString.split(' ');
                for (const token of idTokens) {
                    // Extract number after "id"
                    const userId: number = parseInt(token.substring(2)); 
                    mentions[userId]++;
                }
            }
        }
    }

    return mentions;
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
     * @param Integer $numberOfUsers
     * @param String[][] $events
     * @return Integer[]
     */
    function countMentions($numberOfUsers, $events) {
        $mentions = array_fill(0, $numberOfUsers, 0);
        // userOfflineUntil[i] stores the timestamp when user i will become online.
        // If userOfflineUntil[i] <= currentTimestamp, user i is online.
        // Initially, all users are online, so they are "online since time 0".
        $userOfflineUntil = array_fill(0, $numberOfUsers, 0); 

        // Prepare events for sorting: [timestamp, priority, original_event_data]
        // Priority: 0 for OFFLINE (status change), 1 for MESSAGE (action)
        $processedEvents = [];
        foreach ($events as $event) {
            $eventType = $event[0];
            $timestamp = intval($event[1]);
            if ($eventType === "OFFLINE") {
                $processedEvents[] = [$timestamp, 0, $event]; // 0 priority for OFFLINE
            } else { // MESSAGE
                $processedEvents[] = [$timestamp, 1, $event]; // 1 priority for MESSAGE
            }
        }

        // Sort events by timestamp, then by priority (OFFLINE before MESSAGE)
        usort($processedEvents, function($a, $b) {
            if ($a[0] !== $b[0]) {
                return $a[0] - $b[0];
            } else {
                return $a[1] - $b[1];
            }
        });

        foreach ($processedEvents as $eventTuple) {
            $currentTimestamp = $eventTuple[0];
            $originalEvent = $eventTuple[2];
            $eventType = $originalEvent[0];

            if ($eventType === "OFFLINE") {
                $userId = intval($originalEvent[2]);
                $userOfflineUntil[$userId] = $currentTimestamp + 60;
            } else { // MESSAGE event
                $mentionsString = $originalEvent[2];

                // Determine current online users *at this timestamp*
                $onlineUsersAtCurrentTime = [];
                for ($i = 0; $i < $numberOfUsers; ++$i) {
                    if ($userOfflineUntil[$i] <= $currentTimestamp) {
                        $onlineUsersAtCurrentTime[] = $i;
                    }
                }

                if ($mentionsString === "ALL") {
                    for ($i = 0; $i < $numberOfUsers; ++$i) {
                        $mentions[$i]++;
                    }
                } else if ($mentionsString === "HERE") {
                    foreach ($onlineUsersAtCurrentTime as $userId) {
                        $mentions[$userId]++;
                    }
                }
                else { // Specific IDs like "id1 id0"
                    $idTokens = explode(' ', $mentionsString);
                    foreach ($idTokens as $token) {
                        // Extract number after "id"
                        $userId = intval(substr($token, 2)); 
                        $mentions[$userId]++;
                    }
                }
            }
        }

        return $mentions;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
import Foundation

class Solution {

    // Custom Event struct to hold parsed event data and enable custom sorting
    struct Event: Comparable {
        let timestamp: Int
        let priority: Int // 0 for OFFLINE, 1 for MESSAGE
        let type: String
        let detail1: String

        init(_ originalEvent: [String]) {
            self.type = originalEvent[0]
            self.timestamp = Int(originalEvent[1])!
            self.priority = (self.type == "OFFLINE") ? 0 : 1
            self.detail1 = originalEvent[2] // mentions_string or user_id
        }

        static func < (lhs: Event, rhs: Event) -> Bool {
            if lhs.timestamp != rhs.timestamp {
                return lhs.timestamp < rhs.timestamp
            } else {
                return lhs.priority < rhs.priority
            }
        }
    }

    func countMentions(_ numberOfUsers: Int, _ events: [[String]]) -> [Int] {
        var mentions = Array(repeating: 0, count: numberOfUsers)
        // userOfflineUntil[i] stores the timestamp when user i will become online.
        // If userOfflineUntil[i] <= currentTimestamp, user i is online.
        // Initially, all users are online, so they are "online since time 0".
        var userOfflineUntil = Array(repeating: 0, count: numberOfUsers) 

        var processedEvents: [Event] = []
        for eventList in events {
            processedEvents.append(Event(eventList))
        }

        processedEvents.sort()

        for event in processedEvents {
            let currentTimestamp = event.timestamp
            let eventType = event.type

            if eventType == "OFFLINE" {
                let userId = Int(event.detail1)!;
                userOfflineUntil[userId] = currentTimestamp + 60
            } else { // MESSAGE event
                let mentionsString = event.detail1

                // Determine current online users *at this timestamp*
                var onlineUsersAtCurrentTime: [Int] = []
                for i in 0..<numberOfUsers {
                    if userOfflineUntil[i] <= currentTimestamp {
                        onlineUsersAtCurrentTime.append(i)
                    }
                }

                if mentionsString == "ALL" {
                    for i in 0..<numberOfUsers {
                        mentions[i] += 1
                    }
                } else if mentionsString == "HERE" {
                    for userId in onlineUsersAtCurrentTime {
                        mentions[userId] += 1
                    }
                } else { // Specific IDs like "id1 id0"
                    let idTokens = mentionsString.split(separator: " ")
                    for token in idTokens {
                        // Extract number after "id"
                        let userId = Int(token.dropFirst(2))! 
                        mentions[userId] += 1
                    }
                }
            }
        }

        return mentions
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
class Solution {

    // Custom Event data class to hold parsed event data and enable custom sorting
    data class Event(val timestamp: Int, val priority: Int, val type: String, val val1: String) : Comparable<Event> {
        override fun compareTo(other: Event): Int {
            if (this.timestamp != other.timestamp) {
                return this.timestamp.compareTo(other.timestamp)
            } else {
                return this.priority.compareTo(other.priority)
            }
        }
    }

    fun countMentions(numberOfUsers: Int, events: List<List<String>>): IntArray {
        val mentions = IntArray(numberOfUsers) { 0 }
        // userOfflineUntil[i] stores the timestamp when user i will become online.
        // If userOfflineUntil[i] <= currentTimestamp, user i is online.
        // Initially, all users are online, so they are "online since time 0".
        val userOfflineUntil = IntArray(numberOfUsers) { 0 } 

        val processedEvents = mutableListOf<Event>()
        for (eventList in events) {
            val eventType = eventList[0]
            val timestamp = eventList[1].toInt()
            val priority = if (eventType == "OFFLINE") 0 else 1
            processedEvents.add(Event(timestamp, priority, eventType, eventList[2]))
        }

        processedEvents.sort()

        for (event in processedEvents) {
            val currentTimestamp = event.timestamp
            val eventType = event.type

            if (eventType == "OFFLINE") {
                val userId = event.val1.toInt()
                userOfflineUntil[userId] = currentTimestamp + 60
            } else { // MESSAGE event
                val mentionsString = event.val1

                // Determine current online users *at this timestamp*
                val onlineUsersAtCurrentTime = mutableListOf<Int>()
                for (i in 0 until numberOfUsers) {
                    if (userOfflineUntil[i] <= currentTimestamp) {
                        onlineUsersAtCurrentTime.add(i)
                    }
                }

                if (mentionsString == "ALL") {
                    for (i in 0 until numberOfUsers) {
                        mentions[i]++
                    }
                } else if (mentionsString == "HERE") {
                    for (userId in onlineUsersAtCurrentTime) {
                        mentions[userId]++
                    }
                } else { // Specific IDs like "id1 id0"
                    val idTokens = mentionsString.split(' ')
                    for (token in idTokens) {
                        // Extract number after "id"
                        val userId = token.substring(2).toInt() 
                        mentions[userId]++
                    }
                }
            }
        }

        return mentions
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
class Solution {

  // Custom Event class to hold parsed event data and enable custom sorting
  class Event implements Comparable<Event> {
    final int timestamp;
    final int priority; // 0 for OFFLINE, 1 for MESSAGE
    final String type;
    final String detail1;

    Event(List<String> originalEvent) 
      : type = originalEvent[0],
        timestamp = int.parse(originalEvent[1]),
        priority = (originalEvent[0] == "OFFLINE") ? 0 : 1,
        detail1 = originalEvent[2]; // mentions_string or user_id

    @override
    int compareTo(Event other) {
      if (timestamp != other.timestamp) {
        return timestamp.compareTo(other.timestamp);
      } else {
        return priority.compareTo(other.priority);
      }
    }
  }

  List<int> countMentions(int numberOfUsers, List<List<String>> events) {
    List<int> mentions = List.filled(numberOfUsers, 0);
    // userOfflineUntil[i] stores the timestamp when user i will become online.
    // If userOfflineUntil[i] <= currentTimestamp, user i is online.
    // Initially, all users are online, so they are "online since time 0".
    List<int> userOfflineUntil = List.filled(numberOfUsers, 0); 

    List<Event> processedEvents = [];
    for (var eventList in events) {
      processedEvents.add(Event(eventList));
    }

    processedEvents.sort();

    for (var event in processedEvents) {
      int currentTimestamp = event.timestamp;
      String eventType = event.type;

      if (eventType == "OFFLINE") {
        int userId = int.parse(event.detail1);
        userOfflineUntil[userId] = currentTimestamp + 60;
      } else { // MESSAGE event
        String mentionsString = event.detail1;

        // Determine current online users *at this timestamp*
        List<int> onlineUsersAtCurrentTime = [];
        for (int i = 0; i < numberOfUsers; ++i) {
          if (userOfflineUntil[i] <= currentTimestamp) {
            onlineUsersAtCurrentTime.add(i);
          }
        }

        if (mentionsString == "ALL") {
          for (int i = 0; i < numberOfUsers; ++i) {
            mentions[i]++;
          }
        } else if (mentionsString == "HERE") {
          for (int userId in onlineUsersAtCurrentTime) {
            mentions[userId]++;
          }
        } else { // Specific IDs like "id1 id0"
          List<String> idTokens = mentionsString.split(' ');
          for (String token in idTokens) {
            // Extract number after "id"
            int userId = int.parse(token.substring(2)); 
            mentions[userId]++;
          }
        }
      }
    }

    return mentions;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import (
	"sort"
	"strconv"
	"strings"
)

type Event struct {
	timestamp int
	priority  int // 0 for OFFLINE, 1 for MESSAGE
	typeStr   string
	detail1   string
}

type ByTimestampAndPriority []Event

func (a ByTimestampAndPriority) Len() int      { return len(a) }
func (a ByTimestampAndPriority) Swap(i, j int) { a[i], a[j] = a[j], a[i] }
func (a ByTimestampAndPriority) Less(i, j int) bool {
	if a[i].timestamp != a[j].timestamp {
		return a[i].timestamp < a[j].timestamp
	}
	return a[i].priority < a[j].priority
}

func countMentions(numberOfUsers int, events [][]string) []int {
	mentions := make([]int, numberOfUsers)
	// userOfflineUntil[i] stores the timestamp when user i will become online.
	// If userOfflineUntil[i] <= currentTimestamp, user i is online.
	// Initially, all users are online, so they are "online since time 0".
	userOfflineUntil := make([]int, numberOfUsers)

	processedEvents := make([]Event, 0, len(events))
	for _, eventArr := range events {
		eventType := eventArr[0]
		timestamp, _ := strconv.Atoi(eventArr[1])
		priority := 1 // Default for MESSAGE
		if eventType == "OFFLINE" {
			priority = 0
		}
		processedEvents = append(processedEvents, Event{
			timestamp: timestamp,
			priority:  priority,
			typeStr:   eventType,
			detail1:   eventArr[2],
		})
	}

	sort.Sort(ByTimestampAndPriority(processedEvents))

	for _, event := range processedEvents {
		currentTimestamp := event.timestamp
		eventType := event.typeStr

		if eventType == "OFFLINE" {
			userId, _ := strconv.Atoi(event.detail1)
			userOfflineUntil[userId] = currentTimestamp + 60
		} else { // MESSAGE event
			mentionsString := event.detail1

			// Determine current online users *at this timestamp*
			onlineUsersAtCurrentTime := []int{}
			for i := 0; i < numberOfUsers; i++ {
				if userOfflineUntil[i] <= currentTimestamp {
					onlineUsersAtCurrentTime = append(onlineUsersAtCurrentTime, i)
				}
			}

			if mentionsString == "ALL" {
				for i := 0; i < numberOfUsers; i++ {
					mentions[i]++
				}
			} else if mentionsString == "HERE" {
				for _, userId := range onlineUsersAtCurrentTime {
					mentions[userId]++
				}
			} else { // Specific IDs like "id1 id0"
				idTokens := strings.Split(mentionsString, " ")
				for _, token := range idTokens {
					// Extract number after "id"
					userId, _ := strconv.Atoi(token[2:])
					mentions[userId]++
				}
			}
		}
	}

	return mentions
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
class Solution
    def countMentions(number_of_users, events)
        mentions = Array.new(number_of_users, 0)
        # user_offline_until[i] stores the timestamp when user i will become online.
        # If user_offline_until[i] <= current_timestamp, user i is online.
        # Initially, all users are online, so they are "online since time 0".
        user_offline_until = Array.new(number_of_users, 0) 

        # Prepare events for sorting: [timestamp, priority, original_event_data]
        # Priority: 0 for OFFLINE (status change), 1 for MESSAGE (action)
        processed_events = []
        events.each do |event|
            event_type = event[0]
            timestamp = event[1].to_i
            if event_type == "OFFLINE"
                processed_events.push([timestamp, 0, event]) # 0 priority for OFFLINE
            else # MESSAGE
                processed_events.push([timestamp, 1, event]) # 1 priority for MESSAGE
            end
        end

        # Sort events by timestamp, then by priority (OFFLINE before MESSAGE)
        processed_events.sort_by! { |e| [e[0], e[1]] }

        processed_events.each do |event_tuple|
            current_timestamp = event_tuple[0]
            original_event = event_tuple[2]
            event_type = original_event[0]

            if event_type == "OFFLINE"
                user_id = original_event[2].to_i
                user_offline_until[user_id] = current_timestamp + 60
            else # MESSAGE event
                mentions_string = original_event[2]

                # Determine current online users *at this timestamp*
                online_users_at_current_time = []
                (0...number_of_users).each do |i|
                    if user_offline_until[i] <= current_timestamp
                        online_users_at_current_time.push(i)
                    end
                end

                if mentions_string == "ALL"
                    (0...number_of_users).each do |i|
                        mentions[i] += 1
                    end
                elsif mentions_string == "HERE"
                    online_users_at_current_time.each do |user_id|
                        mentions[user_id] += 1
                    end
                else # Specific IDs like "id1 id0"
                    id_tokens = mentions_string.split(' ')
                    id_tokens.each do |token|
                        # Extract number after "id"
                        user_id = token[2..].to_i 
                        mentions[user_id] += 1
                    end
                end
            end
        end

        return mentions
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

    // Custom Event case class to hold parsed event data and enable custom sorting
    case class Event(timestamp: Int, priority: Int, eventType: String, detail1: String) extends Ordered[Event] {
        override def compare(that: Event): Int = {
            if (this.timestamp != that.timestamp) {
                this.timestamp.compareTo(that.timestamp)
            } else {
                this.priority.compareTo(that.priority)
            }
        }
    }

    def countMentions(numberOfUsers: Int, events: List[List[String]]): Array[Int] = {
        val mentions = Array.fill(numberOfUsers)(0)
        // userOfflineUntil(i) stores the timestamp when user i will become online.
        // If userOfflineUntil(i) <= currentTimestamp, user i is online.
        // Initially, all users are online, so they are "online since time 0".
        val userOfflineUntil = Array.fill(numberOfUsers)(0) 

        val processedEvents = ListBuffer[Event]()
        for (eventList <- events) {
            val eventType = eventList.head
            val timestamp = eventList(1).toInt
            val priority = if (eventType == "OFFLINE") 0 else 1
            processedEvents += Event(timestamp, priority, eventType, eventList(2))
        }

        val sortedEvents = processedEvents.sorted

        for (event <- sortedEvents) {
            val currentTimestamp = event.timestamp
            val eventType = event.eventType

            if (eventType == "OFFLINE") {
                val userId = event.detail1.toInt
                userOfflineUntil(userId) = currentTimestamp + 60
            } else { // MESSAGE event
                val mentionsString = event.detail1

                // Determine current online users *at this timestamp*
                val onlineUsersAtCurrentTime = ListBuffer[Int]()
                for (i <- 0 until numberOfUsers) {
                    if (userOfflineUntil(i) <= currentTimestamp) {
                        onlineUsersAtCurrentTime += i
                    }
                }

                if (mentionsString == "ALL") {
                    for (i <- 0 until numberOfUsers) {
                        mentions(i) += 1
                    }
                } else if (mentionsString == "HERE") {
                    for (userId <- onlineUsersAtCurrentTime) {
                        mentions(userId) += 1
                    }
                } else { // Specific IDs like "id1 id0"
                    val idTokens = mentionsString.split(' ')
                    for (token <- idTokens) {
                        // Extract number after "id"
                        val userId = token.substring(2).toInt 
                        mentions(userId) += 1
                    }
                }
            }
        }

        mentions
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
impl Solution {
    pub fn count_mentions(number_of_users: i32, events: Vec<Vec<String>>) -> Vec<i32> {
        let mut mentions = vec![0; number_of_users as usize];
        // user_offline_until[i] stores the timestamp when user i will become online.
        // If user_offline_until[i] <= current_timestamp, user i is online.
        // Initially, all users are online, so they are "online since time 0".
        let mut user_offline_until = vec![0; number_of_users as usize]; 

        // Prepare events for sorting: (timestamp, priority, original_event_data)
        // Priority: 0 for OFFLINE (status change), 1 for MESSAGE (action)
        let mut processed_events: Vec<(i32, i32, Vec<String>)> = Vec::new();
        for event in events {
            let event_type = &event[0];
            let timestamp = event[1].parse::<i32>().unwrap();
            if event_type == "OFFLINE" {
                processed_events.push((timestamp, 0, event)); // 0 priority for OFFLINE
            } else { // MESSAGE
                processed_events.push((timestamp, 1, event)); // 1 priority for MESSAGE
            }
        }

        // Sort events by timestamp, then by priority (OFFLINE before MESSAGE)
        processed_events.sort_unstable();

        for (current_timestamp, _, original_event) in processed_events {
            let event_type = &original_event[0];

            if event_type == "OFFLINE" {
                let user_id = original_event[2].parse::<usize>().unwrap();
                user_offline_until[user_id] = current_timestamp + 60;
            } else { // MESSAGE event
                let mentions_string = &original_event[2];

                // Determine current online users *at this timestamp*
                let mut online_users_at_current_time: Vec<usize> = Vec::new();
                for i in 0..number_of_users as usize {
                    if user_offline_until[i] <= current_timestamp {
                        online_users_at_current_time.push(i);
                    }
                }

                if mentions_string == "ALL" {
                    for i in 0..number_of_users as usize {
                        mentions[i] += 1;
                    }
                } else if mentions_string == "HERE" {
                    for user_id in online_users_at_current_time {
                        mentions[user_id] += 1;
                    }
                } else { // Specific IDs like "id1 id0"
                    let id_tokens = mentions_string.split_whitespace();
                    for token in id_tokens {
                        // Extract number after "id"
                        let user_id = token[2..].parse::<usize>().unwrap(); 
                        mentions[user_id] += 1;
                    }
                }
            }
        }

        mentions
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket

(define (count-mentions number-of-users events)
  (define mentions (make-vector number-of-users 0))
  ;; user-offline-until[i] stores the timestamp when user i will become online.
  ;; If (vector-ref user-offline-until i) <= current-timestamp, user i is online.
  ;; Initially, all users are online, so they are "online since time 0".
  (define user-offline-until (make-vector number-of-users 0))

  ;; Prepare events for sorting: (timestamp, priority, original-event-data)
  ;; Priority: 0 for OFFLINE (status change), 1 for MESSAGE (action)
  (define processed-events
    (for/list ([event events])
      (define event-type (list-ref event 0))
      (define timestamp (string->number (list-ref event 1)))
      (if (string=? event-type "OFFLINE")
          (list timestamp 0 event) ; 0 priority for OFFLINE
          (list timestamp 1 event)))) ; 1 priority for MESSAGE

  ;; Sort events by timestamp, then by priority (OFFLINE before MESSAGE)
  (define sorted-events (sort processed-events (lambda (a b)
                                                  (or (< (list-ref a 0) (list-ref b 0))
                                                      (and (= (list-ref a 0) (list-ref b 0))
                                                           (< (list-ref a 1) (list-ref b 1)))))))

  (for ([event-tuple sorted-events])
    (define current-timestamp (list-ref event-tuple 0))
    (define original-event (list-ref event-tuple 2))
    (define event-type (list-ref original-event 0))

    (if (string=? event-type "OFFLINE")
        (begin
          (define user-id (string->number (list-ref original-event 2)))
          (vector-set! user-offline-until user-id (+ current-timestamp 60)))
        ;; MESSAGE event
        (begin
          (define mentions-string (list-ref original-event 2))

          ;; Determine current online users *at this timestamp*
          (define online-users-at-current-time (build-list number-of-users identity))
          (define filtered-online-users
            (filter (lambda (i) (<= (vector-ref user-offline-until i) current-timestamp))
                    online-users-at-current-time))

          (cond
            ((string=? mentions-string "ALL")
             (for ([i (in-range number-of-users)])
               (vector-set! mentions i (+ (vector-ref mentions i) 1))))
            ((string=? mentions-string "HERE")
             (for ([user-id filtered-online-users])
               (vector-set! mentions user-id (+ (vector-ref mentions user-id) 1))))
            (else ; Specific IDs like "id1 id0"
             (define id-tokens (string-split mentions-string " "))
             (for ([token id-tokens])
               (define user-id (string->number (substring token 2)))
               (vector-set! mentions user-id (+ (vector-ref mentions user-id) 1)))))))

  (vector->list mentions))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([count_mentions/2]).

count_mentions(NumberOfUsers, Events) ->
    Mentions = array:new([{size, NumberOfUsers}, {fixed, true}, {default, 0}]),
    UserOfflineUntil = array:new([{size, NumberOfUsers}, {fixed, true}, {default, 0}]),

    ProcessedEvents = lists:map(fun(Event) ->
        EventType = hd(Event),
        Timestamp = binary_to_integer(list_to_binary(lists:nth(2, Event))),
        case EventType of
            "OFFLINE" -> {Timestamp, 0, Event}; %% 0 priority for OFFLINE
            _ -> {Timestamp, 1, Event}          %% 1 priority for MESSAGE
        end
    end, Events),

    SortedEvents = lists:sort(fun({TsA, PriA, _}, {TsB, PriB, _}) ->
        if TsA =/= TsB -> TsA < TsB;
           true -> PriA < PriB
        end
    end, ProcessedEvents),

    lists:foldl(fun({CurrentTimestamp, _, OriginalEvent}, Acc) ->
        {CurrentMentions, CurrentUserOfflineUntil} = Acc,
        EventType = hd(OriginalEvent),

        case EventType of
            "OFFLINE" ->
                UserId = binary_to_integer(list_to_binary(lists:nth(3, OriginalEvent))),
                NewUserOfflineUntil = array:set(UserId, CurrentTimestamp + 60, CurrentUserOfflineUntil),
                {CurrentMentions, NewUserOfflineUntil};
            _ -> %% MESSAGE event
                MentionsString = lists:nth(3, OriginalEvent),

                OnlineUsersAtCurrentTime = lists:filter(fun(I) ->
                    array:get(I, CurrentUserOfflineUntil) =< CurrentTimestamp
                end, lists:seq(0, NumberOfUsers - 1)),

                case MentionsString of
                    "ALL" ->
                        NewMentions = lists:foldl(fun(I, M) ->
                            array:set(I, array:get(I, M) + 1, M)
                        end, CurrentMentions, lists:seq(0, NumberOfUsers - 1));
                    "HERE" ->
                        NewMentions = lists:foldl(fun(UserId, M) ->
                            array:set(UserId, array:get(UserId, M) + 1, M)
                        end, CurrentMentions, OnlineUsersAtCurrentTime);
                    _ -> %% Specific IDs like "id1 id0"
                        IdTokens = string:tokens(MentionsString, " "),
                        NewMentions = lists:foldl(fun(Token, M) ->
                            UserId = binary_to_integer(list_to_binary(string:substr(Token, 3))),
                            array:set(UserId, array:get(UserId, M) + 1, M)
                        end, CurrentMentions, IdTokens)
                end,
                {NewMentions, CurrentUserOfflineUntil}
        end
    end, {Mentions, UserOfflineUntil}, SortedEvents),

    {FinalMentions, _} = lists:foldl(fun(I, Acc) ->
        [array:get(I, Mentions) | Acc]
    end, [], lists:seq(NumberOfUsers - 1, 0, -1)).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  def count_mentions(number_of_users, events) do
    mentions = :array.new([{:size, number_of_users}, {:fixed, true}, {:default, 0}])
    user_offline_until = :array.new([{:size, number_of_users}, {:fixed, true}, {:default, 0}])

    processed_events = Enum.map(events, fn event ->
      event_type = hd(event)
      timestamp = String.to_integer(Enum.at(event, 1))
      priority = if event_type == "OFFLINE", do: 0, else: 1
      {timestamp, priority, event}
    end)

    sorted_events = Enum.sort(processed_events, fn {ts_a, pri_a, _}, {ts_b, pri_b, _} ->
      if ts_a != ts_b, do: ts_a < ts_b, else: pri_a < pri_b
    end)

    {final_mentions, _} = Enum.reduce(sorted_events, {mentions, user_offline_until}, fn {current_timestamp, _, original_event}, {current_mentions, current_user_offline_until} ->
      event_type = hd(original_event)

      case event_type do
        "OFFLINE" ->
          user_id = String.to_integer(Enum.at(original_event, 2))
          new_user_offline_until = :array.set(user_id, current_timestamp + 60, current_user_offline_until)
          {current_mentions, new_user_offline_until}
        _ -> # MESSAGE event
          mentions_string = Enum.at(original_event, 2)

          online_users_at_current_time = Enum.filter(0..(number_of_users - 1), fn i ->
            :array.get(i, current_user_offline_until) <= current_timestamp
          end)

          new_mentions = case mentions_string do
            "ALL" ->
              Enum.reduce(0..(number_of_users - 1), current_mentions, fn i, m ->
                :array.set(i, :array.get(i, m) + 1, m)
              end)
            "HERE" ->
              Enum.reduce(online_users_at_current_time, current_mentions, fn user_id, m ->
                :array.set(user_id, :array.get(user_id, m) + 1, m)
              end)
            _ -> # Specific IDs like "id1 id0"
              id_tokens = String.split(mentions_string, " ")
              Enum.reduce(id_tokens, current_mentions, fn token, m ->
                user_id = String.to_integer(String.slice(token, 2..))
                :array.set(user_id, :array.get(user_id, m) + 1, m)
              end)
          end
          {new_mentions, current_user_offline_until}
      end
    end)

    Enum.map(0..(number_of_users - 1), fn i -> :array.get(i, final_mentions) end)
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** Let `N` be the number of events, `U` be the `numberOfUsers`, and `M` be the maximum number of individual ID mentions in a single message. The dominant operations are sorting the events, which takes `O(N log N)`, and processing each event. For each `MESSAGE` event, determining online users takes `O(U)`, and parsing mentions (whether `ALL`, `HERE`, or specific IDs) takes `O(U)` or `O(M)`. Thus, processing all events takes `O(N * (U + M))`. The overall time complexity is `O(N log N + N * (U + M))`. Given the constraints (`N, U, M <= 100`), this is efficient enough.

- **Space Complexity:** The space complexity is determined by the data structures used. `mentions` and `user_offline_until` arrays each require `O(U)` space. The `processed_events` list, which stores parsed events for sorting, requires `O(N)` space. The temporary list of `online_users_at_current_time` within a message event processing step requires `O(U)` space. Therefore, the total space complexity is `O(N + U)`.

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-12-12 01:09:51 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The algorithm starts by sorting the events based on their timestamps. Then, it processes each event in order. For each event, it checks if the event is a message or an offline event. If it's a message event, it parses the mentions string and increments the mention count for each mentioned user. If it's an offline event, it marks the user as offline and schedules them to come back online after 60 time units. The algorithm maintains two sets for offline and online user IDs to efficiently check the status of each user. The key intuition is to process the events in order and maintain the status of each user to accurately count the mentions.

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
    vector<int> countMentions(int numberOfUsers, vector<vector<string>>& events) {
        vector<int> mentions(numberOfUsers, 0);
        vector<bool> online(numberOfUsers, true);
        vector<pair<int, int>> offlineSchedule;
        sort(events.begin(), events.end(), [](const vector<string>& a, const vector<string>& b) {
            return stoi(a[1]) < stoi(b[1]);
        });
        for (auto& event : events) {
            int timestamp = stoi(event[1]);
            if (event[0] == "OFFLINE") {
                int userId = stoi(event[2].substr(2));
                online[userId] = false;
                offlineSchedule.push_back({timestamp + 60, userId});
            } else if (event[0] == "MESSAGE") {
                string mentionsStr = event[2];
                if (mentionsStr == "ALL") {
                    for (int i = 0; i < numberOfUsers; i++) {
                        mentions[i]++;
                    }
                } else if (mentionsStr == "HERE") {
                    for (int i = 0; i < numberOfUsers; i++) {
                        if (online[i]) {
                            mentions[i]++;
                        }
                    }
                } else {
                    istringstream iss(mentionsStr);
                    string userIdStr;
                    while (iss >> userIdStr) {
                        int userId = stoi(userIdStr.substr(2));
                        mentions[userId]++;
                    }
                }
            }
            while (!offlineSchedule.empty() && offlineSchedule[0].first <= timestamp) {
                online[offlineSchedule[0].second] = true;
                offlineSchedule.erase(offlineSchedule.begin());
            }
        }
        return mentions;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int[] countMentions(int numberOfUsers, String[][] events) {
        int[] mentions = new int[numberOfUsers];
        boolean[] online = new boolean[numberOfUsers];
        Arrays.fill(online, true);
        Arrays.sort(events, (a, b) -> Integer.parseInt(a[1]) - Integer.parseInt(b[1]));
        List<int[]> offlineSchedule = new ArrayList<>();
        for (String[] event : events) {
            int timestamp = Integer.parseInt(event[1]);
            if (event[0].equals("OFFLINE")) {
                int userId = Integer.parseInt(event[2].substring(2));
                online[userId] = false;
                offlineSchedule.add(new int[] {timestamp + 60, userId});
            } else if (event[0].equals("MESSAGE")) {
                String mentionsStr = event[2];
                if (mentionsStr.equals("ALL")) {
                    for (int i = 0; i < numberOfUsers; i++) {
                        mentions[i]++;
                    }
                } else if (mentionsStr.equals("HERE")) {
                    for (int i = 0; i < numberOfUsers; i++) {
                        if (online[i]) {
                            mentions[i]++;
                        }
                    }
                } else {
                    String[] userIds = mentionsStr.split(" ");
                    for (String userIdStr : userIds) {
                        int userId = Integer.parseInt(userIdStr.substring(2));
                        mentions[userId]++;
                    }
                }
            }
            while (!offlineSchedule.isEmpty() && offlineSchedule.get(0)[0] <= timestamp) {
                online[offlineSchedule.get(0)[1]] = true;
                offlineSchedule.remove(0);
            }
        }
        return mentions;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        mentions = [0] * numberOfUsers
        online = [True] * numberOfUsers
        offline_schedule = []
        events.sort(key=lambda x: int(x[1]))
        for event in events:
            timestamp = int(event[1])
            if event[0] == "OFFLINE":
                user_id = int(event[2][2:])
                online[user_id] = False
                offline_schedule.append((timestamp + 60, user_id))
            elif event[0] == "MESSAGE":
                mentions_str = event[2]
                if mentions_str == "ALL":
                    for i in range(numberOfUsers):
                        mentions[i] += 1
                elif mentions_str == "HERE":
                    for i in range(numberOfUsers):
                        if online[i]:
                            mentions[i] += 1
                else:
                    for user_id_str in mentions_str.split():
                        user_id = int(user_id_str[2:])
                        mentions[user_id] += 1
            while offline_schedule and offline_schedule[0][0] <= timestamp:
                online[offline_schedule[0][1]] = True
                offline_schedule.pop(0)
        return mentions
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        mentions = [0] * numberOfUsers
        online = [True] * numberOfUsers
        offline_schedule = []
        events.sort(key=lambda x: int(x[1]))
        for event in events:
            timestamp = int(event[1])
            if event[0] == "OFFLINE":
                user_id = int(event[2][2:])
                online[user_id] = False
                offline_schedule.append((timestamp + 60, user_id))
            elif event[0] == "MESSAGE":
                mentions_str = event[2]
                if mentions_str == "ALL":
                    for i in range(numberOfUsers):
                        mentions[i] += 1
                elif mentions_str == "HERE":
                    for i in range(numberOfUsers):
                        if online[i]:
                            mentions[i] += 1
                else:
                    for user_id_str in mentions_str.split():
                        user_id = int(user_id_str[2:])
                        mentions[user_id] += 1
            while offline_schedule and offline_schedule[0][0] <= timestamp:
                online[offline_schedule[0][1]] = True
                offline_schedule.pop(0)
        return mentions
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
typedef struct {
    int timestamp;
    int userId;
} OfflineEvent;

int compare(const void *a, const void *b) {
    OfflineEvent *event1 = (OfflineEvent *)a;
    OfflineEvent *event2 = (OfflineEvent *)b;
    return event1->timestamp - event2->timestamp;
}

int* countMentions(int numberOfUsers, char ***events, int eventsSize, int *eventsColSize, int *returnSize) {
    int* mentions = (int*)malloc(numberOfUsers * sizeof(int));
    bool* online = (bool*)malloc(numberOfUsers * sizeof(bool));
    for (int i = 0; i < numberOfUsers; i++) {
        mentions[i] = 0;
        online[i] = true;
    }
    OfflineEvent* offlineSchedule = (OfflineEvent*)malloc(eventsSize * sizeof(OfflineEvent));
    int scheduleSize = 0;
    for (int i = 0; i < eventsSize; i++) {
        int timestamp = atoi(events[i][1]);
        if (strcmp(events[i][0], "OFFLINE") == 0) {
            int userId = atoi(events[i][2] + 2);
            online[userId] = false;
            offlineSchedule[scheduleSize].timestamp = timestamp + 60;
            offlineSchedule[scheduleSize].userId = userId;
            scheduleSize++;
        } else if (strcmp(events[i][0], "MESSAGE") == 0) {
            char* mentionsStr = events[i][2];
            if (strcmp(mentionsStr, "ALL") == 0) {
                for (int j = 0; j < numberOfUsers; j++) {
                    mentions[j]++;
                }
            } else if (strcmp(mentionsStr, "HERE") == 0) {
                for (int j = 0; j < numberOfUsers; j++) {
                    if (online[j]) {
                        mentions[j]++;
                    }
                }
            } else {
                char* token = strtok(mentionsStr, " ");
                while (token != NULL) {
                    int userId = atoi(token + 2);
                    mentions[userId]++;
                    token = strtok(NULL, " ");
                }
            }
        }
        while (scheduleSize > 0 && offlineSchedule[0].timestamp <= timestamp) {
            online[offlineSchedule[0].userId] = true;
            scheduleSize--;
            memmove(offlineSchedule, offlineSchedule + 1, (scheduleSize) * sizeof(OfflineEvent));
        }
    }
    *returnSize = numberOfUsers;
    return mentions;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
public class Solution {
    public int[] CountMentions(int numberOfUsers, string[][] events) {
        int[] mentions = new int[numberOfUsers];
        bool[] online = new bool[numberOfUsers];
        for (int i = 0; i < numberOfUsers; i++) {
            online[i] = true;
        }
        Array.Sort(events, (a, b) => int.Parse(a[1]) - int.Parse(b[1]));
        List<(int, int)> offlineSchedule = new List<(int, int)>();
        foreach (string[] event in events) {
            int timestamp = int.Parse(event[1]);
            if (event[0] == "OFFLINE") {
                int userId = int.Parse(event[2].Substring(2));
                online[userId] = false;
                offlineSchedule.Add((timestamp + 60, userId));
            } else if (event[0] == "MESSAGE") {
                string mentionsStr = event[2];
                if (mentionsStr == "ALL") {
                    for (int i = 0; i < numberOfUsers; i++) {
                        mentions[i]++;
                    }
                } else if (mentionsStr == "HERE") {
                    for (int i = 0; i < numberOfUsers; i++) {
                        if (online[i]) {
                            mentions[i]++;
                        }
                    }
                } else {
                    string[] userIds = mentionsStr.Split(' ');
                    foreach (string userIdStr in userIds) {
                        int userId = int.Parse(userIdStr.Substring(2));
                        mentions[userId]++;
                    }
                }
            }
            while (offlineSchedule.Count > 0 && offlineSchedule[0].Item1 <= timestamp) {
                online[offlineSchedule[0].Item2] = true;
                offlineSchedule.RemoveAt(0);
            }
        }
        return mentions;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
var countMentions = function(numberOfUsers, events) {
    let mentions = new Array(numberOfUsers).fill(0);
    let online = new Array(numberOfUsers).fill(true);
    let offlineSchedule = [];
    events.sort((a, b) => parseInt(a[1]) - parseInt(b[1]));
    for (let event of events) {
        let timestamp = parseInt(event[1]);
        if (event[0] === "OFFLINE") {
            let userId = parseInt(event[2].slice(2));
            online[userId] = false;
            offlineSchedule.push([timestamp + 60, userId]);
        } else if (event[0] === "MESSAGE") {
            let mentionsStr = event[2];
            if (mentionsStr === "ALL") {
                for (let i = 0; i < numberOfUsers; i++) {
                    mentions[i]++;
                }
            } else if (mentionsStr === "HERE") {
                for (let i = 0; i < numberOfUsers; i++) {
                    if (online[i]) {
                        mentions[i]++;
                    }
                }
            } else {
                let userIds = mentionsStr.split(' ');
                for (let userIdStr of userIds) {
                    let userId = parseInt(userIdStr.slice(2));
                    mentions[userId]++;
                }
            }
        }
        while (offlineSchedule.length > 0 && offlineSchedule[0][0] <= timestamp) {
            online[offlineSchedule[0][1]] = true;
            offlineSchedule.shift();
        }
    }
    return mentions;
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
function countMentions(numberOfUsers: number, events: string[][]): number[] {
    let mentions: number[] = new Array(numberOfUsers).fill(0);
    let online: boolean[] = new Array(numberOfUsers).fill(true);
    let offlineSchedule: [number, number][] = [];
    events.sort((a, b) => parseInt(a[1]) - parseInt(b[1]));
    for (let event of events) {
        let timestamp: number = parseInt(event[1]);
        if (event[0] === "OFFLINE") {
            let userId: number = parseInt(event[2].slice(2));
            online[userId] = false;
            offlineSchedule.push([timestamp + 60, userId]);
        } else if (event[0] === "MESSAGE") {
            let mentionsStr: string = event[2];
            if (mentionsStr === "ALL") {
                for (let i = 0; i < numberOfUsers; i++) {
                    mentions[i]++;
                }
            } else if (mentionsStr === "HERE") {
                for (let i = 0; i < numberOfUsers; i++) {
                    if (online[i]) {
                        mentions[i]++;
                    }
                }
            } else {
                let userIds: string[] = mentionsStr.split(' ');
                for (let userIdStr of userIds) {
                    let userId: number = parseInt(userIdStr.slice(2));
                    mentions[userId]++;
                }
            }
        }
        while (offlineSchedule.length > 0 && offlineSchedule[0][0] <= timestamp) {
            online[offlineSchedule[0][1]] = true;
            offlineSchedule.shift();
        }
    }
    return mentions;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
function countMentions($numberOfUsers, $events) {
    $mentions = array_fill(0, $numberOfUsers, 0);
    $online = array_fill(0, $numberOfUsers, true);
    $offlineSchedule = [];
    usort($events, function($a, $b) {
        return intval($a[1]) - intval($b[1]);
    });
    foreach ($events as $event) {
        $timestamp = intval($event[1]);
        if ($event[0] == "OFFLINE") {
            $userId = intval(substr($event[2], 2));
            $online[$userId] = false;
            $offlineSchedule[] = [$timestamp + 60, $userId];
        } else if ($event[0] == "MESSAGE") {
            $mentionsStr = $event[2];
            if ($mentionsStr == "ALL") {
                for ($i = 0; $i < $numberOfUsers; $i++) {
                    $mentions[$i]++;
                }
            } else if ($mentionsStr == "HERE") {
                for ($i = 0; $i < $numberOfUsers; $i++) {
                    if ($online[$i]) {
                        $mentions[$i]++;
                    }
                }
            } else {
                $userIds = explode(' ', $mentionsStr);
                foreach ($userIds as $userIdStr) {
                    $userId = intval(substr($userIdStr, 2));
                    $mentions[$userId]++;
                }
            }
        }
        while (!empty($offlineSchedule) && $offlineSchedule[0][0] <= $timestamp) {
            $online[$offlineSchedule[0][1]] = true;
            array_shift($offlineSchedule);
        }
    }
    return $mentions;
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
func countMentions(_ numberOfUsers: Int, _ events: [[String]]) -> [Int] {
    var mentions = Array(repeating: 0, count: numberOfUsers)
    var online = Array(repeating: true, count: numberOfUsers)
    var offlineSchedule: [(Int, Int)] = []
    let sortedEvents = events.sorted { Int($0[1])! < Int($1[1])! }
    for event in sortedEvents {
        let timestamp = Int(event[1])!
        if event[0] == "OFFLINE" {
            let userId = Int(event[2].dropFirst(2))!
            online[userId] = false
            offlineSchedule.append((timestamp + 60, userId))
        } else if event[0] == "MESSAGE" {
            let mentionsStr = event[2]
            if mentionsStr == "ALL" {
                for i in 0..<numberOfUsers {
                    mentions[i] += 1
                }
            } else if mentionsStr == "HERE" {
                for i in 0..<numberOfUsers {
                    if online[i] {
                        mentions[i] += 1
                    }
                }
            } else {
                let userIds = mentionsStr.components(separatedBy: " ")
                for userIdStr in userIds {
                    let userId = Int(userIdStr.dropFirst(2))!
                    mentions[userId] += 1
                }
            }
        }
        while !offlineSchedule.isEmpty, offlineSchedule.first!.0 <= timestamp {
            online[offlineSchedule.first!.1] = true
            offlineSchedule.removeFirst()
        }
    }
    return mentions
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
fun countMentions(numberOfUsers: Int, events: Array<Array<String>>): IntArray {
    val mentions = IntArray(numberOfUsers)
    val online = BooleanArray(numberOfUsers) { true }
    val offlineSchedule = mutableListOf<Pair<Int, Int>>()
    events.sortBy { it[1].toInt() }
    for (event in events) {
        val timestamp = event[1].toInt()
        if (event[0] == "OFFLINE") {
            val userId = event[2].substring(2).toInt()
            online[userId] = false
            offlineSchedule.add(Pair(timestamp + 60, userId))
        } else if (event[0] == "MESSAGE") {
            val mentionsStr = event[2]
            if (mentionsStr == "ALL") {
                for (i in 0 until numberOfUsers) {
                    mentions[i]++
                }
            } else if (mentionsStr == "HERE") {
                for (i in 0 until numberOfUsers) {
                    if (online[i]) {
                        mentions[i]++
                    }
                }
            } else {
                val userIds = mentionsStr.split(" ")
                for (userIdStr in userIds) {
                    val userId = userIdStr.substring(2).toInt()
                    mentions[userId]++
                }
            }
        }
        while (offlineSchedule.isNotEmpty() && offlineSchedule.first().first <= timestamp) {
            online[offlineSchedule.first().second] = true
            offlineSchedule.removeAt(0)
        }
    }
    return mentions
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
List<int> countMentions(int numberOfUsers, List<List<String>> events) {
    List<int> mentions = List<int>.filled(numberOfUsers, 0);
    List<bool> online = List<bool>.filled(numberOfUsers, true);
    List<List<int>> offlineSchedule = [];
    events.sort((a, b) => int.parse(a[1]) - int.parse(b[1]));
    for (List<String> event in events) {
        int timestamp = int.parse(event[1]);
        if (event[0] == "OFFLINE") {
            int userId = int.parse(event[2].substring(2));
            online[userId] = false;
            offlineSchedule.add([timestamp + 60, userId]);
        } else if (event[0] == "MESSAGE") {
            String mentionsStr = event[2];
            if (mentionsStr == "ALL") {
                for (int i = 0; i < numberOfUsers; i++) {
                    mentions[i]++;
                }
            } else if (mentionsStr == "HERE") {
                for (int i = 0; i < numberOfUsers; i++) {
                    if (online[i]) {
                        mentions[i]++;
                    }
                }
            } else {
                List<String> userIds = mentionsStr.split(" ");
                for (String userIdStr in userIds) {
                    int userId = int.parse(userIdStr.substring(2));
                    mentions[userId]++;
                }
            }
        }
        while (offlineSchedule.isNotEmpty && offlineSchedule.first[0] <= timestamp) {
            online[offlineSchedule.first[1]] = true;
            offlineSchedule.removeAt(0);
        }
    }
    return mentions;
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
    "sort"
)

func countMentions(numberOfUsers int, events [][]string) []int {
    mentions := make([]int, numberOfUsers)
    online := make([]bool, numberOfUsers)
    for i := range online {
        online[i] = true
    }
    offlineSchedule := [][]int{}
    sort.Slice(events, func(i, j int) bool {
        return events[i][1] < events[j][1]
    })
    for _, event := range events {
        timestamp, _ := strconv.Atoi(event[1])
        if event[0] == "OFFLINE" {
            userId, _ := strconv.Atoi(event[2][2:])
            online[userId] = false
            offlineSchedule = append(offlineSchedule, []int{timestamp + 60, userId})
        } else if event[0] == "MESSAGE" {
            mentionsStr := event[2]
            if mentionsStr == "ALL" {
                for i := 0; i < numberOfUsers; i++ {
                    mentions[i]++
                }
            } else if mentionsStr == "HERE" {
                for i := 0; i < numberOfUsers; i++ {
                    if online[i] {
                        mentions[i]++
                    }
                }
            } else {
                userIds := strings.Split(mentionsStr, " ")
                for _, userIdStr := range userIds {
                    userId, _ := strconv.Atoi(userIdStr[2:])
                    mentions[userId]++
                }
            }
        }
        for len(offlineSchedule) > 0 && offlineSchedule[0][0] <= timestamp {
            online[offlineSchedule[0][1]] = true
            offlineSchedule = offlineSchedule[1:]
        }
    }
    return mentions
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
def count_mentions(number_of_users, events)
    mentions = Array.new(number_of_users, 0)
    online = Array.new(number_of_users, true)
    offline_schedule = []
    events.sort_by! { |event| event[1].to_i }
    events.each do |event|
        timestamp = event[1].to_i
        if event[0] == "OFFLINE"
            user_id = event[2][2..].to_i
            online[user_id] = false
            offline_schedule << [timestamp + 60, user_id]
        elsif event[0] == "MESSAGE"
            mentions_str = event[2]
            if mentions_str == "ALL"
                number_of_users.times do |i|
                    mentions[i] += 1
                end
            elsif mentions_str == "HERE"
                number_of_users.times do |i|
                    mentions[i] += 1 if online[i]
                end
            else
                user_ids = mentions_str.split
                user_ids.each do |user_id_str|
                    user_id = user_id_str[2..].to_i
                    mentions[user_id] += 1
                end
            end
        end
        offline_schedule.shift while offline_schedule.any? && offline_schedule.first[0] <= timestamp
    end
    mentions
end
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
object Solution {
    def countMentions(numberOfUsers: Int, events: Array[Array[String]]): Array[Int] = {
        val mentions = Array.fill[Int](numberOfUsers)(0)
        val online = Array.fill[Boolean](numberOfUsers)(true)
        val offlineSchedule = scala.collection.mutable.ListBuffer.empty[(Int, Int)]
        val sortedEvents = events.sortBy(_.apply(1).toInt)
        for (event <- sortedEvents) {
            val timestamp = event(1).toInt
            if (event(0) == "OFFLINE") {
                val userId = event(2).drop(2).toInt
                online(userId) = false
                offlineSchedule += ((timestamp + 60, userId))
            } else if (event(0) == "MESSAGE") {
                val mentionsStr = event(2)
                if (mentionsStr == "ALL") {
                    for (i <- 0 until numberOfUsers) {
                        mentions(i) += 1
                    }
                } else if (mentionsStr == "HERE") {
                    for (i <- 0 until numberOfUsers) {
                        if (online(i)) {
                            mentions(i) += 1
                        }
                    }
                } else {
                    val userIds = mentionsStr.split(" ")
                    for (userIdStr <- userIds) {
                        val userId = userIdStr.drop(2).toInt
                        mentions(userId) += 1
                    }
                }
            }
            while (offlineSchedule.nonEmpty && offlineSchedule.head._1 <= timestamp) {
                online(offlineSchedule.head._2) = true
                offlineSchedule.remove(0)
            }
        }
        mentions
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
fn count_mentions(number_of_users: usize, events: Vec<Vec<String>>) -> Vec<i32> {
    let mut mentions: Vec<i32> = vec![0; number_of_users];
    let mut online: Vec<bool> = vec![true; number_of_users];
    let mut offline_schedule: Vec<(i32, usize)> = Vec::new();
    let mut sorted_events: Vec<Vec<String>> = events;
    sorted_events.sort_by_key(|event| event[1].parse::<i32>().unwrap());
    for event in sorted_events {
        let timestamp: i32 = event[1].parse().unwrap();
        if event[0] == "OFFLINE" {
            let user_id: usize = event[2][2..].parse().unwrap();
            online[user_id] = false;
            offline_schedule.push((timestamp + 60, user_id));
        } else if event[0] == "MESSAGE" {
            let mentions_str = &event[2];
            if mentions_str == "ALL" {
                for i in 0..number_of_users {
                    mentions[i] += 1;
                }
            } else if mentions_str == "HERE" {
                for i in 0..number_of_users {
                    if online[i] {
                        mentions[i] += 1;
                    }
                }
            } else {
                let user_ids: Vec<&str> = mentions_str.split(" ").collect();
                for user_id_str in user_ids {
                    let user_id: usize = user_id_str[2..].parse().unwrap();
                    mentions[user_id] += 1;
                }
            }
        }
        while let Some((timestamp, user_id)) = offline_schedule.first() {
            if *timestamp <= timestamp {
                online[*user_id] = true;
                offline_schedule.remove(0);
            } else {
                break;
            }
        }
    }
    mentions
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
(define (count-mentions number-of-users events)
  (let ((mentions (make-vector number-of-users 0))
        (online (make-vector number-of-users #t))
        (offline-schedule '()))
    (define (sort-events events)
      (sort events (lambda (x y) (< (string->number (cadr x)) (string->number (cadr y))))))
    (define sorted-events (sort-events events))
    (for-each (lambda (event)
                (let ((timestamp (string->number (cadr event))))
                  (cond ((equal? (car event) "OFFLINE")
                         (let ((user-id (string->number (substring (caddr event) 2))))
                           (vector-set! online user-id #f)
                           (set! offline-schedule (cons (cons (+ timestamp 60) user-id) offline-schedule))))
                        ((equal? (car event) "MESSAGE")
                         (let ((mentions-str (caddr event)))
                           (cond ((equal? mentions-str "ALL")
                                  (for ((i (range number-of-users)))
                                    (vector-set! mentions i (+ (vector-ref mentions i) 1))))
                                 ((equal? mentions-str "HERE")
                                  (for ((i (range number-of-users)))
                                    (when (vector-ref online i)
                                      (vector-set! mentions i (+ (vector-ref mentions i) 1)))))
                                 (else
                                  (let ((user-ids (string-split mentions-str " " )))
                                    (for-each (lambda (user-id-str)
                                                (let ((user-id (string->number (substring user-id-str 2))))
                                                  (vector-set! mentions user-id (+ (vector-ref mentions user-id) 1))))
                                      user-ids))))))
                  (when (and offline-schedule (<= (caar offline-schedule) timestamp))
                    (let ((user-id (cdar offline-schedule)))
                      (vector-set! online user-id #t)
                      (set! offline-schedule (cdr offline-schedule))))))
              sorted-events)
    mentions))
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
count_mentions(Number_of_users, Events) ->
    lists:foldl(fun({"OFFLINE", Timestamp, User_id}, {Mentions, Online, Offline_schedule}) ->
                        {Mentions, lists:keyreplace(list_to_integer(string:substr(User_id, 2)), 1, Online, {list_to_integer(string:substr(User_id, 2)), false}), [{list_to_integer(Timestamp) + 60, list_to_integer(string:substr(User_id, 2))} | Offline_schedule]};
                    ({"MESSAGE", Timestamp, Mentions_str}, {Mentions, Online, Offline_schedule}) ->
                        case Mentions_str of
                            "ALL" ->
                                {lists:map(fun(I) -> I + 1 end, Mentions), Online, Offline_schedule};
                            "HERE" ->
                                {lists:map(fun({I, Is_online}) -> if Is_online -> I + 1; true -> I end, lists:zip(Mentions, Online)), Online, Offline_schedule};
                            _ ->
                                {lists:map(fun({I, User_id_str}) -> if lists:member(User_id_str, string:tokens(Mentions_str, " ")) -> I + 1; true -> I end, lists:zip(Mentions, lists:map(fun(X) -> string:substr(X, 2) end, lists:seq(0, Number_of_users - 1)))), Online, Offline_schedule}
                    end,
                    {lists:duplicate(Number_of_users, 0), lists:duplicate(Number_of_users, true), []},
                    lists:sort(fun({_, Timestamp1, _}, {_, Timestamp2, _}) -> Timestamp1 =< Timestamp2 end, Events)).
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
def count_mentions(number_of_users, events) do
  events
  |> Enum.sort_by(&Enum.at(&1, 1))
  |> Enum.reduce({Enum.duplicate(number_of_users, 0), Enum.duplicate(number_of_users, true), []}, fn event, {mentions, online, offline_schedule} ->
      case event do
        ["OFFLINE", timestamp, user_id] ->
          {mentions, List.update_at(online, String.to_integer(user_id) - 2, fn _ -> false end), [{String.to_integer(timestamp) + 60, String.to_integer(user_id) - 2} | offline_schedule]}
        ["MESSAGE", timestamp, mentions_str] ->
          cond do
            mentions_str == "ALL" ->
              {Enum.map(mentions, &(&1 + 1)), online, offline_schedule}
            mentions_str == "HERE" ->
              {Enum.with_index(online)
               |> Enum.map(fn {index, is_online} -> if is_online, do: Enum.at(mentions, index) + 1, else: Enum.at(mentions, index)), online, offline_schedule}
            true ->
              {Enum.with_index(mentions)
               |> Enum.map(fn {index, mention} -> if Enum.member?(String.split(mentions_str, " "), "id#{index + 1}"), do: mention + 1, else: mention), online, offline_schedule}
          end
      end
    end)
  |> elem(0)
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of the algorithm is O(n log n + n * m) where n is the number of events and m is the maximum number of mentions in a message event. This is because the algorithm sorts the events, which takes O(n log n) time, and then processes each event, which takes O(n * m) time in the worst case.

- **Space Complexity:** The space complexity of the algorithm is O(n + m) where n is the number of events and m is the number of users. This is because the algorithm maintains two sets for offline and online user IDs, which takes O(m) space, and a list to store the mention counts for each user, which takes O(m) space. The algorithm also uses a list to store the sorted events, which takes O(n) space.

</div>
</details>
