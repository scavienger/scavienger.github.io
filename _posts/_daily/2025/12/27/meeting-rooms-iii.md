---
layout: post
title: "Meeting Rooms III"
date: 2025-12-27 09:00:00 +0900
categories: [LeetCode, Hard]
tags: ["Array", "Hash Table", "Sorting", "Heap (Priority Queue)", "Simulation"]
difficulty: Hard
leetcode_url: https://leetcode.com/problems/meeting-rooms-iii/
ai_solutions:
  - solutions:
      cpp: "#include <vector>\n#include <algorithm>\n#include <queue> // For priority_queue\n\
        #include <utility> // For std::pair\n\nclass Solution {\npublic:\n    int mostBooked(int\
        \ n, std::vector<std::vector<int>>& meetings) {\n        // 1. Sort meetings\
        \ by their original start times\n        std::sort(meetings.begin(), meetings.end());\n\
        \n        // Min-heap for available rooms (stores room numbers)\n        //\
        \ std::priority_queue is max-heap by default, use std::greater for min-heap\n\
        \        std::priority_queue<int, std::vector<int>, std::greater<int>> available_rooms;\n\
        \        for (int i = 0; i < n; ++i) {\n            available_rooms.push(i);\n\
        \        }\n\n        // Min-heap for occupied rooms (stores (end_time, room_number))\n\
        \        // Sorted by end_time, then room_number for ties\n        // Use long\
        \ long for end_time to prevent overflow\n        std::priority_queue<std::pair<long\
        \ long, int>, \n                            std::vector<std::pair<long long,\
        \ int>>, \n                            std::greater<std::pair<long long, int>>>\
        \ occupied_rooms;\n\n        // Array to count meetings for each room\n    \
        \    std::vector<int> room_usage_count(n, 0);\n\n        for (const auto& meeting\
        \ : meetings) {\n            long long start = meeting[0];\n            long\
        \ long end = meeting[1];\n            long long duration = end - start;\n\n\
        \            // Free up rooms whose meetings have ended by the current meeting's\
        \ start time\n            while (!occupied_rooms.empty() && occupied_rooms.top().first\
        \ <= start) {\n                int room_num = occupied_rooms.top().second;\n\
        \                occupied_rooms.pop();\n                available_rooms.push(room_num);\n\
        \            }\n\n            int room_num_to_assign;\n            long long\
        \ new_end_time;\n\n            if (!available_rooms.empty()) {\n           \
        \     // If there are available rooms, take the one with the lowest number\n\
        \                room_num_to_assign = available_rooms.top();\n             \
        \   available_rooms.pop();\n                new_end_time = end; // Meeting starts\
        \ at its original start time\n            } else {\n                // No available\
        \ rooms, delay the current meeting\n                // Take the room that will\
        \ become free earliest\n                std::pair<long long, int> earliest_free_room\
        \ = occupied_rooms.top();\n                occupied_rooms.pop();\n\n       \
        \         long long earliest_free_time = earliest_free_room.first;\n       \
        \         room_num_to_assign = earliest_free_room.second;\n\n              \
        \  // The delayed meeting starts when this room becomes free\n             \
        \   // Its new end time is earliest_free_time + duration\n                new_end_time\
        \ = earliest_free_time + duration;\n            }\n\n            // Assign the\
        \ meeting to the chosen room\n            occupied_rooms.push({new_end_time,\
        \ room_num_to_assign});\n            room_usage_count[room_num_to_assign]++;\n\
        \        }\n\n        // Find the room with the most meetings\n        int max_meetings\
        \ = -1;\n        int most_booked_room = -1;\n        for (int i = 0; i < n;\
        \ ++i) {\n            if (room_usage_count[i] > max_meetings) {\n          \
        \      max_meetings = room_usage_count[i];\n                most_booked_room\
        \ = i;\n            }\n            // If counts are equal, the problem asks\
        \ for the lowest room number,\n            // which is naturally handled by\
        \ iterating from i=0 to n-1.\n            // The first one encountered with\
        \ max_meetings will be the lowest room number.\n        }\n\n        return\
        \ most_booked_room;\n    }\n};"
      java: "import java.util.Arrays;\nimport java.util.PriorityQueue;\n\nclass Solution\
        \ {\n    public int mostBooked(int n, int[][] meetings) {\n        // 1. Sort\
        \ meetings by their original start times\n        Arrays.sort(meetings, (a,\
        \ b) -> Integer.compare(a[0], b[0]));\n\n        // Min-heap for available rooms\
        \ (stores room numbers)\n        PriorityQueue<Integer> availableRooms = new\
        \ PriorityQueue<>();\n        for (int i = 0; i < n; ++i) {\n            availableRooms.offer(i);\n\
        \        }\n\n        // Min-heap for occupied rooms (stores (end_time, room_number))\n\
        \        // Sorted by end_time, then room_number for ties\n        // Each element\
        \ is an array: [end_time, room_number]\n        PriorityQueue<long[]> occupiedRooms\
        \ = new PriorityQueue<>((a, b) -> {\n            if (a[0] != b[0]) {\n     \
        \           return Long.compare(a[0], b[0]);\n            }\n            return\
        \ Integer.compare((int)a[1], (int)b[1]);\n        });\n\n        // Array to\
        \ count meetings for each room\n        int[] roomUsageCount = new int[n];\n\
        \n        for (int[] meeting : meetings) {\n            long start = meeting[0];\n\
        \            long end = meeting[1];\n            long duration = end - start;\n\
        \n            // Free up rooms whose meetings have ended by the current meeting's\
        \ start time\n            while (!occupiedRooms.isEmpty() && occupiedRooms.peek()[0]\
        \ <= start) {\n                long[] roomInfo = occupiedRooms.poll();\n   \
        \             int roomNum = (int)roomInfo[1];\n                availableRooms.offer(roomNum);\n\
        \            }\n\n            int roomNumToAssign;\n            long newEndTime;\n\
        \n            if (!availableRooms.isEmpty()) {\n                // If there\
        \ are available rooms, take the one with the lowest number\n               \
        \ roomNumToAssign = availableRooms.poll();\n                newEndTime = end;\
        \ // Meeting starts at its original start time\n            } else {\n     \
        \           // No available rooms, delay the current meeting\n             \
        \   // Take the room that will become free earliest\n                long[]\
        \ earliestFreeRoomInfo = occupiedRooms.poll();\n\n                long earliestFreeTime\
        \ = earliestFreeRoomInfo[0];\n                roomNumToAssign = (int)earliestFreeRoomInfo[1];\n\
        \n                // The delayed meeting starts when this room becomes free\n\
        \                // Its new end time is earliest_free_time + duration\n    \
        \            newEndTime = earliestFreeTime + duration;\n            }\n\n  \
        \          // Assign the meeting to the chosen room\n            occupiedRooms.offer(new\
        \ long[]{newEndTime, roomNumToAssign});\n            roomUsageCount[roomNumToAssign]++;\n\
        \        }\n\n        // Find the room with the most meetings\n        int maxMeetings\
        \ = -1;\n        int mostBookedRoom = -1;\n        for (int i = 0; i < n; ++i)\
        \ {\n            if (roomUsageCount[i] > maxMeetings) {\n                maxMeetings\
        \ = roomUsageCount[i];\n                mostBookedRoom = i;\n            }\n\
        \            // If counts are equal, the problem asks for the lowest room number,\n\
        \            // which is naturally handled by iterating from i=0 to n-1.\n \
        \           // The first one encountered with max_meetings will be the lowest\
        \ room number.\n        }\n\n        return mostBookedRoom;\n    }\n}"
      python: "import heapq\n\nclass Solution:\n    def mostBooked(self, n: int, meetings:\
        \ list[list[int]]) -> int:\n        # 1. Sort meetings by their original start\
        \ times\n        meetings.sort()\n\n        # Min-heap for available rooms (stores\
        \ room numbers)\n        # Initially all rooms are available\n        available_rooms\
        \ = list(range(n))\n        heapq.heapify(available_rooms)\n\n        # Min-heap\
        \ for occupied rooms (stores (end_time, room_number))\n        # Sorted by end_time,\
        \ then room_number for ties\n        occupied_rooms = [] # (end_time, room_number)\n\
        \n        # Array to count meetings for each room\n        room_usage_count\
        \ = [0] * n\n\n        for start, end in meetings:\n            duration = end\
        \ - start\n\n            # Free up rooms whose meetings have ended by the current\
        \ meeting's start time\n            while occupied_rooms and occupied_rooms[0][0]\
        \ <= start:\n                _, room_num = heapq.heappop(occupied_rooms)\n \
        \               heapq.heappush(available_rooms, room_num)\n\n            room_num_to_assign:\
        \ int\n            new_end_time: int\n\n            if available_rooms:\n  \
        \              # If there are available rooms, take the one with the lowest\
        \ number\n                room_num_to_assign = heapq.heappop(available_rooms)\n\
        \                new_end_time = end # Meeting starts at its original start time\n\
        \            else:\n                # No available rooms, delay the current\
        \ meeting\n                # Take the room that will become free earliest\n\
        \                earliest_free_time, room_num_to_assign = heapq.heappop(occupied_rooms)\n\
        \n                # The delayed meeting starts when this room becomes free\n\
        \                # Its new end time is earliest_free_time + duration\n     \
        \           new_end_time = earliest_free_time + duration\n\n            # Assign\
        \ the meeting to the chosen room\n            heapq.heappush(occupied_rooms,\
        \ (new_end_time, room_num_to_assign))\n            room_usage_count[room_num_to_assign]\
        \ += 1\n\n        # Find the room with the most meetings\n        max_meetings\
        \ = -1\n        most_booked_room = -1\n        for i in range(n):\n        \
        \    if room_usage_count[i] > max_meetings:\n                max_meetings =\
        \ room_usage_count[i]\n                most_booked_room = i\n            # If\
        \ counts are equal, the problem asks for the lowest room number,\n         \
        \   # which is naturally handled by iterating from i=0 to n-1.\n           \
        \ # The first one encountered with max_meetings will be the lowest room number.\n\
        \n        return most_booked_room"
      python3: "import heapq\n\nclass Solution:\n    def mostBooked(self, n: int, meetings:\
        \ list[list[int]]) -> int:\n        # 1. Sort meetings by their original start\
        \ times\n        meetings.sort()\n\n        # Min-heap for available rooms (stores\
        \ room numbers)\n        # Initially all rooms are available\n        available_rooms\
        \ = list(range(n))\n        heapq.heapify(available_rooms)\n\n        # Min-heap\
        \ for occupied rooms (stores (end_time, room_number))\n        # Sorted by end_time,\
        \ then room_number for ties\n        occupied_rooms = [] # (end_time, room_number)\n\
        \n        # Array to count meetings for each room\n        room_usage_count\
        \ = [0] * n\n\n        for start, end in meetings:\n            duration = end\
        \ - start\n\n            # Free up rooms whose meetings have ended by the current\
        \ meeting's start time\n            while occupied_rooms and occupied_rooms[0][0]\
        \ <= start:\n                _, room_num = heapq.heappop(occupied_rooms)\n \
        \               heapq.heappush(available_rooms, room_num)\n\n            room_num_to_assign:\
        \ int\n            new_end_time: int\n\n            if available_rooms:\n  \
        \              # If there are available rooms, take the one with the lowest\
        \ number\n                room_num_to_assign = heapq.heappop(available_rooms)\n\
        \                new_end_time = end # Meeting starts at its original start time\n\
        \            else:\n                # No available rooms, delay the current\
        \ meeting\n                # Take the room that will become free earliest\n\
        \                earliest_free_time, room_num_to_assign = heapq.heappop(occupied_rooms)\n\
        \n                # The delayed meeting starts when this room becomes free\n\
        \                # Its new end time is earliest_free_time + duration\n     \
        \           new_end_time = earliest_free_time + duration\n\n            # Assign\
        \ the meeting to the chosen room\n            heapq.heappush(occupied_rooms,\
        \ (new_end_time, room_num_to_assign))\n            room_usage_count[room_num_to_assign]\
        \ += 1\n\n        # Find the room with the most meetings\n        max_meetings\
        \ = -1\n        most_booked_room = -1\n        for i in range(n):\n        \
        \    if room_usage_count[i] > max_meetings:\n                max_meetings =\
        \ room_usage_count[i]\n                most_booked_room = i\n            # If\
        \ counts are equal, the problem asks for the lowest room number,\n         \
        \   # which is naturally handled by iterating from i=0 to n-1.\n           \
        \ # The first one encountered with max_meetings will be the lowest room number.\n\
        \n        return most_booked_room"
      c: "#include <stdlib.h>\n#include <string.h> \n\n// Define a struct for meetings\
        \ to sort them\ntypedef struct {\n    int start;\n    int end;\n} Meeting;\n\
        \n// Comparator for sorting meetings by start time\nint compareMeetings(const\
        \ void* a, const void* b) {\n    return ((Meeting*)a)->start - ((Meeting*)b)->start;\n\
        }\n\n// --- Min-Heap for integers (room numbers) ---\ntypedef struct {\n   \
        \ int* data;\n    int size;\n    int capacity;\n} IntMinHeap;\n\nvoid initIntMinHeap(IntMinHeap*\
        \ heap, int capacity) {\n    heap->data = (int*)malloc(sizeof(int) * capacity);\n\
        \    heap->size = 0;\n    heap->capacity = capacity;\n}\n\nvoid freeIntMinHeap(IntMinHeap*\
        \ heap) {\n    free(heap->data);\n}\n\nvoid swapInt(int* a, int* b) {\n    int\
        \ temp = *a;\n    *a = *b;\n    *b = temp;\n}\n\nvoid intHeapifyUp(IntMinHeap*\
        \ heap, int idx) {\n    int parent = (idx - 1) / 2;\n    while (idx > 0 && heap->data[idx]\
        \ < heap->data[parent]) {\n        swapInt(&heap->data[idx], &heap->data[parent]);\n\
        \        idx = parent;\n        parent = (idx - 1) / 2;\n    }\n}\n\nvoid intHeapifyDown(IntMinHeap*\
        \ heap, int idx) {\n    int smallest = idx;\n    int left = 2 * idx + 1;\n \
        \   int right = 2 * idx + 2;\n\n    if (left < heap->size && heap->data[left]\
        \ < heap->data[smallest]) {\n        smallest = left;\n    }\n    if (right\
        \ < heap->size && heap->data[right] < heap->data[smallest]) {\n        smallest\
        \ = right;\n    }\n\n    if (smallest != idx) {\n        swapInt(&heap->data[idx],\
        \ &heap->data[smallest]);\n        intHeapifyDown(heap, smallest);\n    }\n\
        }\n\nvoid intMinHeapPush(IntMinHeap* heap, int val) {\n    if (heap->size ==\
        \ heap->capacity) {\n        return; \n    }\n    heap->data[heap->size] = val;\n\
        \    heap->size++;\n    intHeapifyUp(heap, heap->size - 1);\n}\n\nint intMinHeapPop(IntMinHeap*\
        \ heap) {\n    if (heap->size == 0) return -1; \n    int root = heap->data[0];\n\
        \    heap->data[0] = heap->data[heap->size - 1];\n    heap->size--;\n    intHeapifyDown(heap,\
        \ 0);\n    return root;\n}\n\nint intMinHeapPeek(IntMinHeap* heap) {\n    if\
        \ (heap->size == 0) return -1;\n    return heap->data[0];\n}\n\nint intMinHeapIsEmpty(IntMinHeap*\
        \ heap) {\n    return heap->size == 0;\n}\n\n// --- Min-Heap for (long long\
        \ end_time, int room_number) pairs ---\ntypedef struct {\n    long long end_time;\n\
        \    int room_num;\n} RoomEvent;\n\ntypedef struct {\n    RoomEvent* data;\n\
        \    int size;\n    int capacity;\n} RoomEventMinHeap;\n\nvoid initRoomEventMinHeap(RoomEventMinHeap*\
        \ heap, int capacity) {\n    heap->data = (RoomEvent*)malloc(sizeof(RoomEvent)\
        \ * capacity);\n    heap->size = 0;\n    heap->capacity = capacity;\n}\n\nvoid\
        \ freeRoomEventMinHeap(RoomEventMinHeap* heap) {\n    free(heap->data);\n}\n\
        \nvoid swapRoomEvent(RoomEvent* a, RoomEvent* b) {\n    RoomEvent temp = *a;\n\
        \    *a = *b;\n    *b = temp;\n}\n\n// Comparator for RoomEvent: end_time then\
        \ room_num\nint compareRoomEvents(RoomEvent a, RoomEvent b) {\n    if (a.end_time\
        \ != b.end_time) {\n        return a.end_time < b.end_time; // true if a has\
        \ higher priority (smaller end_time)\n    }\n    return a.room_num < b.room_num;\
        \ // true if a has higher priority (smaller room_num)\n}\n\nvoid roomEventHeapifyUp(RoomEventMinHeap*\
        \ heap, int idx) {\n    int parent = (idx - 1) / 2;\n    while (idx > 0 && compareRoomEvents(heap->data[idx],\
        \ heap->data[parent])) {\n        swapRoomEvent(&heap->data[idx], &heap->data[parent]);\n\
        \        idx = parent;\n        parent = (idx - 1) / 2;\n    }\n}\n\nvoid roomEventHeapifyDown(RoomEventMinHeap*\
        \ heap, int idx) {\n    int smallest = idx;\n    int left = 2 * idx + 1;\n \
        \   int right = 2 * idx + 2;\n\n    if (left < heap->size && compareRoomEvents(heap->data[left],\
        \ heap->data[smallest])) {\n        smallest = left;\n    }\n    if (right <\
        \ heap->size && compareRoomEvents(heap->data[right], heap->data[smallest]))\
        \ {\n        smallest = right;\n    }\n\n    if (smallest != idx) {\n      \
        \  swapRoomEvent(&heap->data[idx], &heap->data[smallest]);\n        roomEventHeapifyDown(heap,\
        \ smallest);\n    }\n}\n\nvoid roomEventMinHeapPush(RoomEventMinHeap* heap,\
        \ RoomEvent val) {\n    if (heap->size == heap->capacity) {\n        return;\n\
        \    }\n    heap->data[heap->size] = val;\n    heap->size++;\n    roomEventHeapifyUp(heap,\
        \ heap->size - 1);\n}\n\nRoomEvent roomEventMinHeapPop(RoomEventMinHeap* heap)\
        \ {\n    RoomEvent default_event = {-1, -1}; // Error value\n    if (heap->size\
        \ == 0) return default_event;\n    RoomEvent root = heap->data[0];\n    heap->data[0]\
        \ = heap->data[heap->size - 1];\n    heap->size--;\n    roomEventHeapifyDown(heap,\
        \ 0);\n    return root;\n}\n\nRoomEvent roomEventMinHeapPeek(RoomEventMinHeap*\
        \ heap) {\n    RoomEvent default_event = {-1, -1}; // Error value\n    if (heap->size\
        \ == 0) return default_event;\n    return heap->data[0];\n}\n\nint roomEventMinHeapIsEmpty(RoomEventMinHeap*\
        \ heap) {\n    return heap->size == 0;\n}\n\n\nint mostBooked(int n, int** meetings,\
        \ int meetingsSize, int* meetingsColSize) {\n    // Convert 2D int array to\
        \ Meeting struct array for easier sorting\n    Meeting* meeting_structs = (Meeting*)malloc(sizeof(Meeting)\
        \ * meetingsSize);\n    for (int i = 0; i < meetingsSize; ++i) {\n        meeting_structs[i].start\
        \ = meetings[i][0];\n        meeting_structs[i].end = meetings[i][1];\n    }\n\
        \n    // 1. Sort meetings by their original start times\n    qsort(meeting_structs,\
        \ meetingsSize, sizeof(Meeting), compareMeetings);\n\n    // Min-heap for available\
        \ rooms (stores room numbers)\n    IntMinHeap available_rooms;\n    initIntMinHeap(&available_rooms,\
        \ n);\n    for (int i = 0; i < n; ++i) {\n        intMinHeapPush(&available_rooms,\
        \ i);\n    }\n\n    // Min-heap for occupied rooms (stores (end_time, room_number))\n\
        \    RoomEventMinHeap occupied_rooms;\n    initRoomEventMinHeap(&occupied_rooms,\
        \ n);\n\n    // Array to count meetings for each room\n    int* room_usage_count\
        \ = (int*)calloc(n, sizeof(int)); // calloc initializes to 0\n\n    for (int\
        \ i = 0; i < meetingsSize; ++i) {\n        long long start = meeting_structs[i].start;\n\
        \        long long end = meeting_structs[i].end;\n        long long duration\
        \ = end - start;\n\n        // Free up rooms whose meetings have ended by the\
        \ current meeting's start time\n        while (!roomEventMinHeapIsEmpty(&occupied_rooms)\
        \ && roomEventMinHeapPeek(&occupied_rooms).end_time <= start) {\n          \
        \  RoomEvent room_event = roomEventMinHeapPop(&occupied_rooms);\n          \
        \  int room_num = room_event.room_num;\n            intMinHeapPush(&available_rooms,\
        \ room_num);\n        }\n\n        int room_num_to_assign;\n        long long\
        \ new_end_time;\n\n        if (!intMinHeapIsEmpty(&available_rooms)) {\n   \
        \         // If there are available rooms, take the one with the lowest number\n\
        \            room_num_to_assign = intMinHeapPop(&available_rooms);\n       \
        \     new_end_time = end; // Meeting starts at its original start time\n   \
        \     } else {\n            // No available rooms, delay the current meeting\n\
        \            // Take the room that will become free earliest\n            RoomEvent\
        \ earliest_free_room = roomEventMinHeapPop(&occupied_rooms);\n\n           \
        \ long long earliest_free_time = earliest_free_room.end_time;\n            room_num_to_assign\
        \ = earliest_free_room.room_num;\n\n            // The delayed meeting starts\
        \ when this room becomes free\n            // Its new end time is earliest_free_time\
        \ + duration\n            new_end_time = earliest_free_time + duration;\n  \
        \      }\n\n        // Assign the meeting to the chosen room\n        RoomEvent\
        \ new_event = {new_end_time, room_num_to_assign};\n        roomEventMinHeapPush(&occupied_rooms,\
        \ new_event);\n        room_usage_count[room_num_to_assign]++;\n    }\n\n  \
        \  // Find the room with the most meetings\n    int max_meetings = -1;\n   \
        \ int most_booked_room = -1;\n    for (int i = 0; i < n; ++i) {\n        if\
        \ (room_usage_count[i] > max_meetings) {\n            max_meetings = room_usage_count[i];\n\
        \            most_booked_room = i;\n        }\n    }\n\n    // Clean up allocated\
        \ memory\n    free(meeting_structs);\n    freeIntMinHeap(&available_rooms);\n\
        \    freeRoomEventMinHeap(&occupied_rooms);\n    free(room_usage_count);\n\n\
        \    return most_booked_room;\n}"
      csharp: "using System;\nusing System.Collections.Generic;\nusing System.Linq;\n\
        \npublic class Solution {\n    public int MostBooked(int n, int[][] meetings)\
        \ {\n        // 1. Sort meetings by their original start times\n        Array.Sort(meetings,\
        \ (a, b) => a[0].CompareTo(b[0]));\n\n        // Min-heap for available rooms\
        \ (stores room numbers)\n        var availableRooms = new SortedSet<int>();\
        \ // Acts as a min-heap for room numbers\n        for (int i = 0; i < n; ++i)\
        \ {\n            availableRooms.Add(i);\n        }\n\n        // Min-heap for\
        \ occupied rooms (stores (end_time, room_number))\n        // Sorted by end_time,\
        \ then room_number for ties\n        // Using a custom comparer for PriorityQueue\n\
        \        var occupiedRooms = new PriorityQueue<(long endTime, int roomNum),\
        \ (long endTime, int roomNum)>(\n            Comparer<(long endTime, int roomNum)>.Create((a,\
        \ b) => {\n                int cmp = a.endTime.CompareTo(b.endTime);\n     \
        \           if (cmp != 0) return cmp;\n                return a.roomNum.CompareTo(b.roomNum);\n\
        \            })\n        );\n\n        // Array to count meetings for each room\n\
        \        int[] roomUsageCount = new int[n];\n\n        foreach (var meeting\
        \ in meetings) {\n            long start = meeting[0];\n            long end\
        \ = meeting[1];\n            long duration = end - start;\n\n            //\
        \ Free up rooms whose meetings have ended by the current meeting's start time\n\
        \            while (occupiedRooms.Count > 0 && occupiedRooms.Peek().endTime\
        \ <= start) {\n                var roomInfo = occupiedRooms.Dequeue();\n   \
        \             int roomNum = roomInfo.roomNum;\n                availableRooms.Add(roomNum);\n\
        \            }\n\n            int roomNumToAssign;\n            long newEndTime;\n\
        \n            if (availableRooms.Count > 0) {\n                // If there are\
        \ available rooms, take the one with the lowest number\n                roomNumToAssign\
        \ = availableRooms.Min;\n                availableRooms.Remove(roomNumToAssign);\n\
        \                newEndTime = end; // Meeting starts at its original start time\n\
        \            } else {\n                // No available rooms, delay the current\
        \ meeting\n                // Take the room that will become free earliest\n\
        \                var earliestFreeRoomInfo = occupiedRooms.Dequeue();\n\n   \
        \             long earliestFreeTime = earliestFreeRoomInfo.endTime;\n      \
        \          roomNumToAssign = earliestFreeRoomInfo.roomNum;\n\n             \
        \   // The delayed meeting starts when this room becomes free\n            \
        \    // Its new end time is earliest_free_time + duration\n                newEndTime\
        \ = earliestFreeTime + duration;\n            }\n\n            // Assign the\
        \ meeting to the chosen room\n            occupiedRooms.Enqueue((newEndTime,\
        \ roomNumToAssign), (newEndTime, roomNumToAssign));\n            roomUsageCount[roomNumToAssign]++;\n\
        \        }\n\n        // Find the room with the most meetings\n        int maxMeetings\
        \ = -1;\n        int mostBookedRoom = -1;\n        for (int i = 0; i < n; ++i)\
        \ {\n            if (roomUsageCount[i] > maxMeetings) {\n                maxMeetings\
        \ = roomUsageCount[i];\n                mostBookedRoom = i;\n            }\n\
        \            // If counts are equal, the problem asks for the lowest room number,\n\
        \            // which is naturally handled by iterating from i=0 to n-1.\n \
        \           // The first one encountered with max_meetings will be the lowest\
        \ room number.\n        }\n\n        return mostBookedRoom;\n    }\n}"
      javascript: "class MinHeap {\n    constructor(comparator = (a, b) => a < b) {\n\
        \        this.heap = [];\n        this.comparator = comparator;\n    }\n\n \
        \   size() {\n        return this.heap.length;\n    }\n\n    isEmpty() {\n \
        \       return this.size() === 0;\n    }\n\n    peek() {\n        return this.heap[0];\n\
        \    }\n\n    push(value) {\n        this.heap.push(value);\n        this._bubbleUp(this.heap.length\
        \ - 1);\n    }\n\n    pop() {\n        if (this.isEmpty()) return undefined;\n\
        \        const root = this.heap[0];\n        const last = this.heap.pop();\n\
        \        if (!this.isEmpty()) {\n            this.heap[0] = last;\n        \
        \    this._bubbleDown(0);\n        }\n        return root;\n    }\n\n    _bubbleUp(index)\
        \ {\n        while (index > 0) {\n            const parentIndex = Math.floor((index\
        \ - 1) / 2);\n            if (this.comparator(this.heap[index], this.heap[parentIndex]))\
        \ {\n                [this.heap[index], this.heap[parentIndex]] = [this.heap[parentIndex],\
        \ this.heap[index]];\n                index = parentIndex;\n            } else\
        \ {\n                break;\n            }\n        }\n    }\n\n    _bubbleDown(index)\
        \ {\n        const lastIndex = this.heap.length - 1;\n        while (true) {\n\
        \            let leftChildIndex = 2 * index + 1;\n            let rightChildIndex\
        \ = 2 * index + 2;\n            let smallestIndex = index;\n\n            if\
        \ (leftChildIndex <= lastIndex && this.comparator(this.heap[leftChildIndex],\
        \ this.heap[smallestIndex])) {\n                smallestIndex = leftChildIndex;\n\
        \            }\n\n            if (rightChildIndex <= lastIndex && this.comparator(this.heap[rightChildIndex],\
        \ this.heap[smallestIndex])) {\n                smallestIndex = rightChildIndex;\n\
        \            }\n\n            if (smallestIndex !== index) {\n             \
        \   [this.heap[index], this.heap[smallestIndex]] = [this.heap[smallestIndex],\
        \ this.heap[index]];\n                index = smallestIndex;\n            }\
        \ else {\n                break;\n            }\n        }\n    }\n}\n\nclass\
        \ Solution {\n    mostBooked(n, meetings) {\n        // 1. Sort meetings by\
        \ their original start times\n        meetings.sort((a, b) => a[0] - b[0]);\n\
        \n        // Min-heap for available rooms (stores room numbers)\n        const\
        \ availableRooms = new MinHeap((a, b) => a < b); // Default comparator for numbers\n\
        \        for (let i = 0; i < n; ++i) {\n            availableRooms.push(i);\n\
        \        }\n\n        // Min-heap for occupied rooms (stores [end_time, room_number])\n\
        \        // Sorted by end_time, then room_number for ties\n        const occupiedRooms\
        \ = new MinHeap((a, b) => {\n            if (a[0] !== b[0]) {\n            \
        \    return a[0] < b[0];\n            }\n            return a[1] < b[1];\n \
        \       });\n\n        // Array to count meetings for each room\n        const\
        \ roomUsageCount = new Array(n).fill(0);\n\n        for (const meeting of meetings)\
        \ {\n            const start = meeting[0];\n            const end = meeting[1];\n\
        \            const duration = end - start;\n\n            // Free up rooms whose\
        \ meetings have ended by the current meeting's start time\n            while\
        \ (!occupiedRooms.isEmpty() && occupiedRooms.peek()[0] <= start) {\n       \
        \         const roomInfo = occupiedRooms.pop();\n                const roomNum\
        \ = roomInfo[1];\n                availableRooms.push(roomNum);\n          \
        \  }\n\n            let roomNumToAssign;\n            let newEndTime;\n\n  \
        \          if (!availableRooms.isEmpty()) {\n                // If there are\
        \ available rooms, take the one with the lowest number\n                roomNumToAssign\
        \ = availableRooms.pop();\n                newEndTime = end; // Meeting starts\
        \ at its original start time\n            } else {\n                // No available\
        \ rooms, delay the current meeting\n                // Take the room that will\
        \ become free earliest\n                const earliestFreeRoomInfo = occupiedRooms.pop();\n\
        \n                const earliestFreeTime = earliestFreeRoomInfo[0];\n      \
        \          roomNumToAssign = earliestFreeRoomInfo[1];\n\n                //\
        \ The delayed meeting starts when this room becomes free\n                //\
        \ Its new end time is earliest_free_time + duration\n                newEndTime\
        \ = earliestFreeTime + duration;\n            }\n\n            // Assign the\
        \ meeting to the chosen room\n            occupiedRooms.push([newEndTime, roomNumToAssign]);\n\
        \            roomUsageCount[roomNumToAssign]++;\n        }\n\n        // Find\
        \ the room with the most meetings\n        let maxMeetings = -1;\n        let\
        \ mostBookedRoom = -1;\n        for (let i = 0; i < n; ++i) {\n            if\
        \ (roomUsageCount[i] > maxMeetings) {\n                maxMeetings = roomUsageCount[i];\n\
        \                mostBookedRoom = i;\n            }\n            // If counts\
        \ are equal, the problem asks for the lowest room number,\n            // which\
        \ is naturally handled by iterating from i=0 to n-1.\n            // The first\
        \ one encountered with max_meetings will be the lowest room number.\n      \
        \  }\n\n        return mostBookedRoom;\n    }\n}"
      typescript: "class MinHeap<T> {\n    private heap: T[];\n    private comparator:\
        \ (a: T, b: T) => boolean;\n\n    constructor(comparator: (a: T, b: T) => boolean)\
        \ {\n        this.heap = [];\n        this.comparator = comparator;\n    }\n\
        \n    size(): number {\n        return this.heap.length;\n    }\n\n    isEmpty():\
        \ boolean {\n        return this.size() === 0;\n    }\n\n    peek(): T | undefined\
        \ {\n        return this.heap[0];\n    }\n\n    push(value: T): void {\n   \
        \     this.heap.push(value);\n        this._bubbleUp(this.heap.length - 1);\n\
        \    }\n\n    pop(): T | undefined {\n        if (this.isEmpty()) return undefined;\n\
        \        const root = this.heap[0];\n        const last = this.heap.pop();\n\
        \        if (!this.isEmpty() && last !== undefined) {\n            this.heap[0]\
        \ = last;\n            this._bubbleDown(0);\n        }\n        return root;\n\
        \    }\n\n    private _bubbleUp(index: number): void {\n        while (index\
        \ > 0) {\n            const parentIndex = Math.floor((index - 1) / 2);\n   \
        \         if (this.comparator(this.heap[index], this.heap[parentIndex])) {\n\
        \                [this.heap[index], this.heap[parentIndex]] = [this.heap[parentIndex],\
        \ this.heap[index]];\n                index = parentIndex;\n            } else\
        \ {\n                break;\n            }\n        }\n    }\n\n    private\
        \ _bubbleDown(index: number): void {\n        const lastIndex = this.heap.length\
        \ - 1;\n        while (true) {\n            let leftChildIndex = 2 * index +\
        \ 1;\n            let rightChildIndex = 2 * index + 2;\n            let smallestIndex\
        \ = index;\n\n            if (leftChildIndex <= lastIndex && this.comparator(this.heap[leftChildIndex],\
        \ this.heap[smallestIndex])) {\n                smallestIndex = leftChildIndex;\n\
        \            }\n\n            if (rightChildIndex <= lastIndex && this.comparator(this.heap[rightChildIndex],\
        \ this.heap[smallestIndex])) {\n                smallestIndex = rightChildIndex;\n\
        \            }\n\n            if (smallestIndex !== index) {\n             \
        \   [this.heap[index], this.heap[smallestIndex]] = [this.heap[smallestIndex],\
        \ this.heap[index]];\n                index = smallestIndex;\n            }\
        \ else {\n                break;\n            }\n        }\n    }\n}\n\nclass\
        \ Solution {\n    mostBooked(n: number, meetings: number[][]): number {\n  \
        \      // 1. Sort meetings by their original start times\n        meetings.sort((a,\
        \ b) => a[0] - b[0]);\n\n        // Min-heap for available rooms (stores room\
        \ numbers)\n        const availableRooms = new MinHeap<number>((a, b) => a <\
        \ b); // Default comparator for numbers\n        for (let i = 0; i < n; ++i)\
        \ {\n            availableRooms.push(i);\n        }\n\n        // Min-heap for\
        \ occupied rooms (stores [end_time, room_number])\n        // Sorted by end_time,\
        \ then room_number for ties\n        const occupiedRooms = new MinHeap<[number,\
        \ number]>((a, b) => {\n            if (a[0] !== b[0]) {\n                return\
        \ a[0] < b[0];\n            }\n            return a[1] < b[1];\n        });\n\
        \n        // Array to count meetings for each room\n        const roomUsageCount:\
        \ number[] = new Array(n).fill(0);\n\n        for (const meeting of meetings)\
        \ {\n            const start = meeting[0];\n            const end = meeting[1];\n\
        \            const duration = end - start;\n\n            // Free up rooms whose\
        \ meetings have ended by the current meeting's start time\n            while\
        \ (!occupiedRooms.isEmpty() && (occupiedRooms.peek() as [number, number])[0]\
        \ <= start) {\n                const roomInfo = occupiedRooms.pop() as [number,\
        \ number];\n                const roomNum = roomInfo[1];\n                availableRooms.push(roomNum);\n\
        \            }\n\n            let roomNumToAssign: number;\n            let\
        \ newEndTime: number;\n\n            if (!availableRooms.isEmpty()) {\n    \
        \            // If there are available rooms, take the one with the lowest number\n\
        \                roomNumToAssign = availableRooms.pop() as number;\n       \
        \         newEndTime = end; // Meeting starts at its original start time\n \
        \           } else {\n                // No available rooms, delay the current\
        \ meeting\n                // Take the room that will become free earliest\n\
        \                const earliestFreeRoomInfo = occupiedRooms.pop() as [number,\
        \ number];\n\n                const earliestFreeTime = earliestFreeRoomInfo[0];\n\
        \                roomNumToAssign = earliestFreeRoomInfo[1];\n\n            \
        \    // The delayed meeting starts when this room becomes free\n           \
        \     // Its new end time is earliest_free_time + duration\n               \
        \ newEndTime = earliestFreeTime + duration;\n            }\n\n            //\
        \ Assign the meeting to the chosen room\n            occupiedRooms.push([newEndTime,\
        \ roomNumToAssign]);\n            roomUsageCount[roomNumToAssign]++;\n     \
        \   }\n\n        // Find the room with the most meetings\n        let maxMeetings\
        \ = -1;\n        let mostBookedRoom = -1;\n        for (let i = 0; i < n; ++i)\
        \ {\n            if (roomUsageCount[i] > maxMeetings) {\n                maxMeetings\
        \ = roomUsageCount[i];\n                mostBookedRoom = i;\n            }\n\
        \            // If counts are equal, the problem asks for the lowest room number,\n\
        \            // which is naturally handled by iterating from i=0 to n-1.\n \
        \           // The first one encountered with max_meetings will be the lowest\
        \ room number.\n        }\n\n        return mostBookedRoom;\n    }\n}"
      php: "<?php\n\nclass MinHeap implements IteratorAggregate, Countable {\n    private\
        \ array $heap = [];\n    private Closure $comparator;\n\n    public function\
        \ __construct(Closure $comparator) {\n        $this->comparator = $comparator;\n\
        \    }\n\n    public function count(): int {\n        return count($this->heap);\n\
        \    }\n\n    public function isEmpty(): bool {\n        return $this->count()\
        \ === 0;\n    }\n\n    public function peek(): mixed {\n        return $this->heap[0]\
        \ ?? null;\n    }\n\n    public function push(mixed $value): void {\n      \
        \  $this->heap[] = $value;\n        $this->bubbleUp($this->count() - 1);\n \
        \   }\n\n    public function pop(): mixed {\n        if ($this->isEmpty()) return\
        \ null;\n        $root = $this->heap[0];\n        $last = array_pop($this->heap);\n\
        \        if (!$this->isEmpty()) {\n            $this->heap[0] = $last;\n   \
        \         $this->bubbleDown(0);\n        }\n        return $root;\n    }\n\n\
        \    private function bubbleUp(int $index): void {\n        while ($index >\
        \ 0) {\n            $parentIndex = floor(($index - 1) / 2);\n            if\
        \ (($this->comparator)($this->heap[$index], $this->heap[$parentIndex])) {\n\
        \                [$this->heap[$index], $this->heap[$parentIndex]] = [$this->heap[$parentIndex],\
        \ $this->heap[$index]];\n                $index = $parentIndex;\n          \
        \  } else {\n                break;\n            }\n        }\n    }\n\n   \
        \ private function bubbleDown(int $index): void {\n        $lastIndex = $this->count()\
        \ - 1;\n        while (true) {\n            $leftChildIndex = 2 * $index + 1;\n\
        \            $rightChildIndex = 2 * $index + 2;\n            $smallestIndex\
        \ = $index;\n\n            if ($leftChildIndex <= $lastIndex && ($this->comparator)($this->heap[$leftChildIndex],\
        \ $this->heap[$smallestIndex])) {\n                $smallestIndex = $leftChildIndex;\n\
        \            }\n\n            if ($rightChildIndex <= $lastIndex && ($this->comparator)($this->heap[$rightChildIndex],\
        \ $this->heap[$smallestIndex])) {\n                $smallestIndex = $rightChildIndex;\n\
        \            }\n\n            if ($smallestIndex !== $index) {\n           \
        \     [$this->heap[$index], $this->heap[$smallestIndex]] = [$this->heap[$smallestIndex],\
        \ $this->heap[$index]];\n                $index = $smallestIndex;\n        \
        \    } else {\n                break;\n            }\n        }\n    }\n\n \
        \   public function getIterator(): Traversable {\n        return new ArrayIterator($this->heap);\n\
        \    }\n}\n\nclass Solution {\n    /**\n     * @param Integer $n\n     * @param\
        \ Integer[][] $meetings\n     * @return Integer\n     */\n    function mostBooked(int\
        \ $n, array $meetings): int {\n        // 1. Sort meetings by their original\
        \ start times\n        usort($meetings, fn($a, $b) => $a[0] - $b[0]);\n\n  \
        \      // Min-heap for available rooms (stores room numbers)\n        $availableRooms\
        \ = new MinHeap(fn($a, $b) => $a < $b);\n        for ($i = 0; $i < $n; ++$i)\
        \ {\n            $availableRooms->push($i);\n        }\n\n        // Min-heap\
        \ for occupied rooms (stores [end_time, room_number])\n        // Sorted by\
        \ end_time, then room_number for ties\n        $occupiedRooms = new MinHeap(fn($a,\
        \ $b) => {\n            if ($a[0] !== $b[0]) {\n                return $a[0]\
        \ < $b[0];\n            }\n            return $a[1] < $b[1];\n        });\n\n\
        \        // Array to count meetings for each room\n        $roomUsageCount =\
        \ array_fill(0, $n, 0);\n\n        foreach ($meetings as $meeting) {\n     \
        \       $start = $meeting[0];\n            $end = $meeting[1];\n           \
        \ $duration = $end - $start;\n\n            // Free up rooms whose meetings\
        \ have ended by the current meeting's start time\n            while (!$occupiedRooms->isEmpty()\
        \ && $occupiedRooms->peek()[0] <= $start) {\n                $roomInfo = $occupiedRooms->pop();\n\
        \                $roomNum = $roomInfo[1];\n                $availableRooms->push($roomNum);\n\
        \            }\n\n            $roomNumToAssign;\n            $newEndTime;\n\n\
        \            if (!$availableRooms->isEmpty()) {\n                // If there\
        \ are available rooms, take the one with the lowest number\n               \
        \ $roomNumToAssign = $availableRooms->pop();\n                $newEndTime =\
        \ $end; // Meeting starts at its original start time\n            } else {\n\
        \                // No available rooms, delay the current meeting\n        \
        \        // Take the room that will become free earliest\n                $earliestFreeRoomInfo\
        \ = $occupiedRooms->pop();\n\n                $earliestFreeTime = $earliestFreeRoomInfo[0];\n\
        \                $roomNumToAssign = $earliestFreeRoomInfo[1];\n\n          \
        \      // The delayed meeting starts when this room becomes free\n         \
        \       // Its new end time is earliest_free_time + duration\n             \
        \   $newEndTime = $earliestFreeTime + $duration;\n            }\n\n        \
        \    // Assign the meeting to the chosen room\n            $occupiedRooms->push([$newEndTime,\
        \ $roomNumToAssign]);\n            $roomUsageCount[$roomNumToAssign]++;\n  \
        \      }\n\n        // Find the room with the most meetings\n        $maxMeetings\
        \ = -1;\n        $mostBookedRoom = -1;\n        for ($i = 0; $i < $n; ++$i)\
        \ {\n            if ($roomUsageCount[$i] > $maxMeetings) {\n               \
        \ $maxMeetings = $roomUsageCount[$i];\n                $mostBookedRoom = $i;\n\
        \            }\n            // If counts are equal, the problem asks for the\
        \ lowest room number,\n            // which is naturally handled by iterating\
        \ from i=0 to n-1.\n            // The first one encountered with max_meetings\
        \ will be the lowest room number.\n        }\n\n        return $mostBookedRoom;\n\
        \    }\n}"
      swift: "import Foundation\n\n// MinHeap implementation for Swift\nstruct MinHeap<T>\
        \ {\n    private var nodes: [T] = []\n    private let areInIncreasingOrder:\
        \ (T, T) -> Bool\n\n    var isEmpty: Bool { return nodes.isEmpty }\n    var\
        \ count: Int { return nodes.count }\n\n    init(sort: @escaping (T, T) -> Bool)\
        \ {\n        self.areInIncreasingOrder = sort\n    }\n\n    func peek() -> T?\
        \ {\n        return nodes.first\n    }\n\n    mutating func push(_ element:\
        \ T) {\n        nodes.append(element)\n        bubbleUp(nodes.count - 1)\n \
        \   }\n\n    mutating func pop() -> T? {\n        guard !isEmpty else { return\
        \ nil }\n        if nodes.count == 1 {\n            return nodes.removeLast()\n\
        \        }\n        let root = nodes[0]\n        nodes[0] = nodes.removeLast()\n\
        \        bubbleDown(0)\n        return root\n    }\n\n    private mutating func\
        \ bubbleUp(_ index: Int) {\n        var childIndex = index\n        var parentIndex\
        \ = self.parentIndex(of: childIndex)\n        while childIndex > 0 && areInIncreasingOrder(nodes[childIndex],\
        \ nodes[parentIndex]) {\n            nodes.swapAt(childIndex, parentIndex)\n\
        \            childIndex = parentIndex\n            parentIndex = self.parentIndex(of:\
        \ childIndex)\n        }\n    }\n\n    private mutating func bubbleDown(_ index:\
        \ Int) {\n        var parentIndex = index\n        while true {\n          \
        \  let leftChildIndex = self.leftChildIndex(of: parentIndex)\n            let\
        \ rightChildIndex = self.rightChildIndex(of: parentIndex)\n            var candidateIndex\
        \ = parentIndex\n\n            if leftChildIndex < nodes.count && areInIncreasingOrder(nodes[leftChildIndex],\
        \ nodes[candidateIndex]) {\n                candidateIndex = leftChildIndex\n\
        \            }\n            if rightChildIndex < nodes.count && areInIncreasingOrder(nodes[rightChildIndex],\
        \ nodes[candidateIndex]) {\n                candidateIndex = rightChildIndex\n\
        \            }\n\n            if candidateIndex == parentIndex {\n         \
        \       return\n            }\n            nodes.swapAt(parentIndex, candidateIndex)\n\
        \            parentIndex = candidateIndex\n        }\n    }\n\n    private func\
        \ parentIndex(of i: Int) -> Int { (i - 1) / 2 }\n    private func leftChildIndex(of\
        \ i: Int) -> Int { 2 * i + 1 }\n    private func rightChildIndex(of i: Int)\
        \ -> Int { 2 * i + 2 }\n}\n\nclass Solution {\n    func mostBooked(_ n: Int,\
        \ _ meetings: [[Int]]) -> Int {\n        // 1. Sort meetings by their original\
        \ start times\n        var sortedMeetings = meetings.sorted { $0[0] < $1[0]\
        \ }\n\n        // Min-heap for available rooms (stores room numbers)\n     \
        \   var availableRooms = MinHeap<Int> { $0 < $1 }\n        for i in 0..<n {\n\
        \            availableRooms.push(i)\n        }\n\n        // Min-heap for occupied\
        \ rooms (stores (end_time, room_number))\n        // Sorted by end_time, then\
        \ room_number for ties\n        var occupiedRooms = MinHeap<(endTime: Int, roomNum:\
        \ Int)> { a, b in\n            if a.endTime != b.endTime {\n               \
        \ return a.endTime < b.endTime\n            }\n            return a.roomNum\
        \ < b.roomNum\n        }\n\n        // Array to count meetings for each room\n\
        \        var roomUsageCount = Array(repeating: 0, count: n)\n\n        for meeting\
        \ in sortedMeetings {\n            let start = meeting[0]\n            let end\
        \ = meeting[1]\n            let duration = end - start\n\n            // Free\
        \ up rooms whose meetings have ended by the current meeting's start time\n \
        \           while let peeked = occupiedRooms.peek(), peeked.endTime <= start\
        \ {\n                let roomInfo = occupiedRooms.pop()!\n                let\
        \ roomNum = roomInfo.roomNum\n                availableRooms.push(roomNum)\n\
        \            }\n\n            var roomNumToAssign: Int\n            var newEndTime:\
        \ Int\n\n            if !availableRooms.isEmpty {\n                // If there\
        \ are available rooms, take the one with the lowest number\n               \
        \ roomNumToAssign = availableRooms.pop()!\n                newEndTime = end\
        \ // Meeting starts at its original start time\n            } else {\n     \
        \           // No available rooms, delay the current meeting\n             \
        \   // Take the room that will become free earliest\n                let earliestFreeRoomInfo\
        \ = occupiedRooms.pop()!\n\n                let earliestFreeTime = earliestFreeRoomInfo.endTime\n\
        \                roomNumToAssign = earliestFreeRoomInfo.roomNum\n\n        \
        \        // The delayed meeting starts when this room becomes free\n       \
        \         // Its new end time is earliest_free_time + duration\n           \
        \     newEndTime = earliestFreeTime + duration\n            }\n\n          \
        \  // Assign the meeting to the chosen room\n            occupiedRooms.push((newEndTime,\
        \ roomNumToAssign))\n            roomUsageCount[roomNumToAssign] += 1\n    \
        \    }\n\n        // Find the room with the most meetings\n        var maxMeetings\
        \ = -1\n        var mostBookedRoom = -1\n        for i in 0..<n {\n        \
        \    if roomUsageCount[i] > maxMeetings {\n                maxMeetings = roomUsageCount[i]\n\
        \                mostBookedRoom = i\n            }\n            // If counts\
        \ are equal, the problem asks for the lowest room number,\n            // which\
        \ is naturally handled by iterating from i=0 to n-1.\n            // The first\
        \ one encountered with max_meetings will be the lowest room number.\n      \
        \  }\n\n        return mostBookedRoom\n    }\n}"
      kotlin: "import java.util.Arrays\nimport java.util.PriorityQueue\n\nclass Solution\
        \ {\n    fun mostBooked(n: Int, meetings: Array<IntArray>): Int {\n        //\
        \ 1. Sort meetings by their original start times\n        meetings.sortBy {\
        \ it[0] }\n\n        // Min-heap for available rooms (stores room numbers)\n\
        \        val availableRooms = PriorityQueue<Int>()\n        for (i in 0 until\
        \ n) {\n            availableRooms.offer(i)\n        }\n\n        // Min-heap\
        \ for occupied rooms (stores (end_time, room_number))\n        // Sorted by\
        \ end_time, then room_number for ties\n        // Each element is an array:\
        \ [end_time, room_number]\n        val occupiedRooms = PriorityQueue<LongArray>\
        \ { a, b ->\n            val cmp = a[0].compareTo(b[0])\n            if (cmp\
        \ != 0) cmp else a[1].compareTo(b[1])\n        }\n\n        // Array to count\
        \ meetings for each room\n        val roomUsageCount = IntArray(n)\n\n     \
        \   for (meeting in meetings) {\n            val start = meeting[0].toLong()\n\
        \            val end = meeting[1].toLong()\n            val duration = end -\
        \ start\n\n            // Free up rooms whose meetings have ended by the current\
        \ meeting's start time\n            while (occupiedRooms.isNotEmpty() && occupiedRooms.peek()[0]\
        \ <= start) {\n                val roomInfo = occupiedRooms.poll()\n       \
        \         val roomNum = roomInfo[1].toInt()\n                availableRooms.offer(roomNum)\n\
        \            }\n\n            val roomNumToAssign: Int\n            val newEndTime:\
        \ Long\n\n            if (availableRooms.isNotEmpty()) {\n                //\
        \ If there are available rooms, take the one with the lowest number\n      \
        \          roomNumToAssign = availableRooms.poll()!!\n                newEndTime\
        \ = end // Meeting starts at its original start time\n            } else {\n\
        \                // No available rooms, delay the current meeting\n        \
        \        // Take the room that will become free earliest\n                val\
        \ earliestFreeRoomInfo = occupiedRooms.poll()!!\n\n                val earliestFreeTime\
        \ = earliestFreeRoomInfo[0]\n                roomNumToAssign = earliestFreeRoomInfo[1].toInt()\n\
        \n                // The delayed meeting starts when this room becomes free\n\
        \                // Its new end time is earliest_free_time + duration\n    \
        \            newEndTime = earliestFreeTime + duration\n            }\n\n   \
        \         // Assign the meeting to the chosen room\n            occupiedRooms.offer(longArrayOf(newEndTime,\
        \ roomNumToAssign.toLong()))\n            roomUsageCount[roomNumToAssign]++\n\
        \        }\n\n        // Find the room with the most meetings\n        var maxMeetings\
        \ = -1\n        var mostBookedRoom = -1\n        for (i in 0 until n) {\n  \
        \          if (roomUsageCount[i] > maxMeetings) {\n                maxMeetings\
        \ = roomUsageCount[i]\n                mostBookedRoom = i\n            }\n \
        \           // If counts are equal, the problem asks for the lowest room number,\n\
        \            // which is naturally handled by iterating from i=0 to n-1.\n \
        \           // The first one encountered with max_meetings will be the lowest\
        \ room number.\n        }\n\n        return mostBookedRoom\n    }\n}"
      dart: "import 'dart:collection';\n\nclass Solution {\n  int mostBooked(int n,\
        \ List<List<int>> meetings) {\n    // 1. Sort meetings by their original start\
        \ times\n    meetings.sort((a, b) => a[0].compareTo(b[0]));\n\n    // Min-heap\
        \ for available rooms (stores room numbers)\n    final availableRooms = PriorityQueue<int>();\n\
        \    for (int i = 0; i < n; ++i) {\n      availableRooms.add(i);\n    }\n\n\
        \    // Min-heap for occupied rooms (stores [end_time, room_number])\n    //\
        \ Sorted by end_time, then room_number for ties\n    final occupiedRooms = PriorityQueue<List<int>>((a,\
        \ b) {\n      if (a[0] != b[0]) {\n        return a[0].compareTo(b[0]);\n  \
        \    }\n      return a[1].compareTo(b[1]);\n    });\n\n    // Array to count\
        \ meetings for each room\n    final roomUsageCount = List<int>.filled(n, 0);\n\
        \n    for (final meeting in meetings) {\n      final int start = meeting[0];\n\
        \      final int end = meeting[1];\n      final int duration = end - start;\n\
        \n      // Free up rooms whose meetings have ended by the current meeting's\
        \ start time\n      while (occupiedRooms.isNotEmpty && occupiedRooms.first[0]\
        \ <= start) {\n        final roomInfo = occupiedRooms.removeFirst();\n     \
        \   final roomNum = roomInfo[1];\n        availableRooms.add(roomNum);\n   \
        \   }\n\n      int roomNumToAssign;\n      int newEndTime;\n\n      if (availableRooms.isNotEmpty)\
        \ {\n        // If there are available rooms, take the one with the lowest number\n\
        \        roomNumToAssign = availableRooms.removeFirst();\n        newEndTime\
        \ = end; // Meeting starts at its original start time\n      } else {\n    \
        \    // No available rooms, delay the current meeting\n        // Take the room\
        \ that will become free earliest\n        final earliestFreeRoomInfo = occupiedRooms.removeFirst();\n\
        \n        final int earliestFreeTime = earliestFreeRoomInfo[0];\n        roomNumToAssign\
        \ = earliestFreeRoomInfo[1];\n\n        // The delayed meeting starts when this\
        \ room becomes free\n        // Its new end time is earliest_free_time + duration\n\
        \        newEndTime = earliestFreeTime + duration;\n      }\n\n      // Assign\
        \ the meeting to the chosen room\n      occupiedRooms.add([newEndTime, roomNumToAssign]);\n\
        \      roomUsageCount[roomNumToAssign]++;\n    }\n\n    // Find the room with\
        \ the most meetings\n    int maxMeetings = -1;\n    int mostBookedRoom = -1;\n\
        \    for (int i = 0; i < n; ++i) {\n      if (roomUsageCount[i] > maxMeetings)\
        \ {\n        maxMeetings = roomUsageCount[i];\n        mostBookedRoom = i;\n\
        \      }\n      // If counts are equal, the problem asks for the lowest room\
        \ number,\n      // which is naturally handled by iterating from i=0 to n-1.\n\
        \      // The first one encountered with max_meetings will be the lowest room\
        \ number.\n    }\n\n    return mostBookedRoom;\n  }\n}"
      go: "import (\n\t\"container/heap\"\n\t\"sort\"\n)\n\n// An IntMinHeap is a min-heap\
        \ of ints.\ntype IntMinHeap []int\n\nfunc (h IntMinHeap) Len() int         \
        \  { return len(h) }\nfunc (h IntMinHeap) Less(i, j int) bool { return h[i]\
        \ < h[j] }\nfunc (h IntMinHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i]\
        \ }\n\nfunc (h *IntMinHeap) Push(x interface{}) {\n\t*h = append(*h, x.(int))\n\
        }\n\nfunc (h *IntMinHeap) Pop() interface{} {\n\told := *h\n\tn := len(old)\n\
        \tx := old[n-1]\n\t*h = old[0 : n-1]\n\treturn x\n}\n\n// RoomEvent represents\
        \ an occupied room with its end time and room number.\ntype RoomEvent struct\
        \ {\n\tEndTime int64\n\tRoomNum int\n}\n\n// A RoomEventMinHeap is a min-heap\
        \ of RoomEvents.\ntype RoomEventMinHeap []RoomEvent\n\nfunc (h RoomEventMinHeap)\
        \ Len() int {\n\treturn len(h)\n}\n\nfunc (h RoomEventMinHeap) Less(i, j int)\
        \ bool {\n\tif h[i].EndTime != h[j].EndTime {\n\t\treturn h[i].EndTime < h[j].EndTime\n\
        \t}\n\treturn h[i].RoomNum < h[j].RoomNum\n}\n\nfunc (h RoomEventMinHeap) Swap(i,\
        \ j int) {\n\th[i], h[j] = h[j], h[i]\n}\n\nfunc (h *RoomEventMinHeap) Push(x\
        \ interface{}) {\n\t*h = append(*h, x.(RoomEvent))\n}\n\nfunc (h *RoomEventMinHeap)\
        \ Pop() interface{} {\n\told := *h\n\tn := len(old)\n\tx := old[n-1]\n\t*h =\
        \ old[0 : n-1]\n\treturn x\n}\n\nfunc mostBooked(n int, meetings [][]int) int\
        \ {\n\t// 1. Sort meetings by their original start times\n\tsort.Slice(meetings,\
        \ func(i, j int) bool {\n\t\treturn meetings[i][0] < meetings[j][0]\n\t})\n\n\
        \t// Min-heap for available rooms (stores room numbers)\n\tavailableRooms :=\
        \ &IntMinHeap{}\n\theap.Init(availableRooms)\n\tfor i := 0; i < n; i++ {\n\t\
        \theap.Push(availableRooms, i)\n\t}\n\n\t// Min-heap for occupied rooms (stores\
        \ (end_time, room_number))\n\toccupiedRooms := &RoomEventMinHeap{}\n\theap.Init(occupiedRooms)\n\
        \n\t// Array to count meetings for each room\n\troomUsageCount := make([]int,\
        \ n)\n\n\tfor _, meeting := range meetings {\n\t\tstart := int64(meeting[0])\n\
        \t\tend := int64(meeting[1])\n\t\tduration := end - start\n\n\t\t// Free up\
        \ rooms whose meetings have ended by the current meeting's start time\n\t\t\
        for occupiedRooms.Len() > 0 && occupiedRooms.Peek().(RoomEvent).EndTime <= start\
        \ {\n\t\t\troomEvent := heap.Pop(occupiedRooms).(RoomEvent)\n\t\t\theap.Push(availableRooms,\
        \ roomEvent.RoomNum)\n\t\t}\n\n\t\tvar roomNumToAssign int\n\t\tvar newEndTime\
        \ int64\n\n\t\tif availableRooms.Len() > 0 {\n\t\t\t// If there are available\
        \ rooms, take the one with the lowest number\n\t\t\troomNumToAssign = heap.Pop(availableRooms).(int)\n\
        \t\t\tnewEndTime = end // Meeting starts at its original start time\n\t\t} else\
        \ {\n\t\t\t// No available rooms, delay the current meeting\n\t\t\t// Take the\
        \ room that will become free earliest\n\t\t\tearliestFreeRoomEvent := heap.Pop(occupiedRooms).(RoomEvent)\n\
        \n\t\t\t// The delayed meeting starts when this room becomes free\n\t\t\t//\
        \ Its new end time is earliest_free_time + duration\n\t\t\tnewEndTime = earliestFreeRoomEvent.EndTime\
        \ + duration\n\t\t\troomNumToAssign = earliestFreeRoomEvent.RoomNum\n\t\t}\n\
        \n\t\t// Assign the meeting to the chosen room\n\theap.Push(occupiedRooms, RoomEvent{EndTime:\
        \ newEndTime, RoomNum: roomNumToAssign})\n\t\troomUsageCount[roomNumToAssign]++\n\
        \t}\n\n\t// Find the room with the most meetings\n\tmaxMeetings := -1\n\tmostBookedRoom\
        \ := -1\n\tfor i := 0; i < n; i++ {\n\t\tif roomUsageCount[i] > maxMeetings\
        \ {\n\t\t\tmaxMeetings = roomUsageCount[i]\n\t\t\tmostBookedRoom = i\n\t\t}\n\
        \t\t// If counts are equal, the problem asks for the lowest room number,\n\t\
        \t// which is naturally handled by iterating from i=0 to n-1.\n\t\t// The first\
        \ one encountered with max_meetings will be the lowest room number.\n\t}\n\n\
        \treturn mostBookedRoom\n}"
      ruby: "require 'set'\n\nclass MinHeap\n  def initialize(&comparator)\n    @heap\
        \ = []\n    @comparator = comparator || Proc.new { |a, b| a <=> b }\n  end\n\
        \n  def size\n    @heap.size\n  end\n\n  def empty?\n    @heap.empty?\n  end\n\
        \n  def peek\n    @heap.first\n  end\n\n  def push(value)\n    @heap << value\n\
        \    bubble_up(@heap.size - 1)\n  end\n\n  def pop\n    return nil if empty?\n\
        \    root = @heap.first\n    last = @heap.pop\n    unless empty?\n      @heap[0]\
        \ = last\n      bubble_down(0)\n    end\n    root\n  end\n\n  private\n\n  def\
        \ bubble_up(index)\n    while index > 0\n      parent_index = (index - 1) /\
        \ 2\n      if @comparator.call(@heap[index], @heap[parent_index]) < 0\n    \
        \    @heap[index], @heap[parent_index] = @heap[parent_index], @heap[index]\n\
        \        index = parent_index\n      else\n        break\n      end\n    end\n\
        \  end\n\n  def bubble_down(index)\n    last_index = @heap.size - 1\n    loop\
        \ do\n      left_child_index = 2 * index + 1\n      right_child_index = 2 *\
        \ index + 2\n      smallest_index = index\n\n      if left_child_index <= last_index\
        \ && @comparator.call(@heap[left_child_index], @heap[smallest_index]) < 0\n\
        \        smallest_index = left_child_index\n      end\n\n      if right_child_index\
        \ <= last_index && @comparator.call(@heap[right_child_index], @heap[smallest_index])\
        \ < 0\n        smallest_index = right_child_index\n      end\n\n      if smallest_index\
        \ != index\n        @heap[index], @heap[smallest_index] = @heap[smallest_index],\
        \ @heap[index]\n        index = smallest_index\n      else\n        break\n\
        \      end\n    end\n  end\nend\n\nclass Solution\n  def most_booked(n, meetings)\n\
        \    # 1. Sort meetings by their original start times\n    meetings.sort_by!\
        \ { |m| m[0] }\n\n    # Min-heap for available rooms (stores room numbers)\n\
        \    available_rooms = MinHeap.new { |a, b| a <=> b }\n    n.times { |i| available_rooms.push(i)\
        \ }\n\n    # Min-heap for occupied rooms (stores [end_time, room_number])\n\
        \    # Sorted by end_time, then room_number for ties\n    occupied_rooms = MinHeap.new\
        \ do |a, b|\n      if a[0] != b[0]\n        a[0] <=> b[0]\n      else\n    \
        \    a[1] <=> b[1]\n      end\n    end\n\n    # Array to count meetings for\
        \ each room\n    room_usage_count = Array.new(n, 0)\n\n    meetings.each do\
        \ |start, ending|\n      duration = ending - start\n\n      # Free up rooms\
        \ whose meetings have ended by the current meeting's start time\n      while\
        \ !occupied_rooms.empty? && occupied_rooms.peek[0] <= start\n        room_info\
        \ = occupied_rooms.pop\n        room_num = room_info[1]\n        available_rooms.push(room_num)\n\
        \      end\n\n      room_num_to_assign = nil\n      new_end_time = nil\n\n \
        \     if !available_rooms.empty?\n        # If there are available rooms, take\
        \ the one with the lowest number\n        room_num_to_assign = available_rooms.pop\n\
        \        new_end_time = ending # Meeting starts at its original start time\n\
        \      else\n        # No available rooms, delay the current meeting\n     \
        \   # Take the room that will become free earliest\n        earliest_free_room_info\
        \ = occupied_rooms.pop\n\n        earliest_free_time = earliest_free_room_info[0]\n\
        \        room_num_to_assign = earliest_free_room_info[1]\n\n        # The delayed\
        \ meeting starts when this room becomes free\n        # Its new end time is\
        \ earliest_free_time + duration\n        new_end_time = earliest_free_time +\
        \ duration\n      end\n\n      # Assign the meeting to the chosen room\n   \
        \   occupied_rooms.push([new_end_time, room_num_to_assign])\n      room_usage_count[room_num_to_assign]\
        \ += 1\n    end\n\n    # Find the room with the most meetings\n    max_meetings\
        \ = -1\n    most_booked_room = -1\n    n.times do |i|\n      if room_usage_count[i]\
        \ > max_meetings\n        max_meetings = room_usage_count[i]\n        most_booked_room\
        \ = i\n      end\n      # If counts are equal, the problem asks for the lowest\
        \ room number,\n      # which is naturally handled by iterating from i=0 to\
        \ n-1.\n      # The first one encountered with max_meetings will be the lowest\
        \ room number.\n    end\n\n    most_booked_room\n  end\nend"
      scala: "import scala.collection.mutable\n\nclass Solution {\n    def mostBooked(n:\
        \ Int, meetings: Array[Array[Int]]): Int = {\n        // 1. Sort meetings by\
        \ their original start times\n        val sortedMeetings = meetings.sortBy(_(0))\n\
        \n        // Min-heap for available rooms (stores room numbers)\n        val\
        \ availableRooms = new mutable.PriorityQueue[Int]()(Ordering.Int.reverse)\n\
        \        for (i <- 0 until n) {\n            availableRooms.enqueue(i)\n   \
        \     }\n\n        // Min-heap for occupied rooms (stores (end_time, room_number))\n\
        \        // Sorted by end_time, then room_number for ties\n        // Custom\
        \ ordering for tuples: first by end_time (Long), then by room_number (Int)\n\
        \        implicit val occupiedRoomOrdering: Ordering[(Long, Int)] = Ordering.by(t\
        \ => (t._1, t._2))\n        val occupiedRooms = new mutable.PriorityQueue[(Long,\
        \ Int)]()\n\n        // Array to count meetings for each room\n        val roomUsageCount\
        \ = Array.fill(n)(0)\n\n        for (meeting <- sortedMeetings) {\n        \
        \    val start = meeting(0).toLong\n            val end = meeting(1).toLong\n\
        \            val duration = end - start\n\n            // Free up rooms whose\
        \ meetings have ended by the current meeting's start time\n            while\
        \ (occupiedRooms.nonEmpty && occupiedRooms.head._1 <= start) {\n           \
        \     val (_, roomNum) = occupiedRooms.dequeue()\n                availableRooms.enqueue(roomNum)\n\
        \            }\n\n            var roomNumToAssign: Int = -1\n            var\
        \ newEndTime: Long = -1L\n\n            if (availableRooms.nonEmpty) {\n   \
        \             // If there are available rooms, take the one with the lowest\
        \ number\n                roomNumToAssign = availableRooms.dequeue()\n     \
        \           newEndTime = end // Meeting starts at its original start time\n\
        \            } else {\n                // No available rooms, delay the current\
        \ meeting\n                // Take the room that will become free earliest\n\
        \                val (earliestFreeTime, roomNum) = occupiedRooms.dequeue()\n\
        \n                roomNumToAssign = roomNum\n\n                // The delayed\
        \ meeting starts when this room becomes free\n                // Its new end\
        \ time is earliest_free_time + duration\n                newEndTime = earliestFreeTime\
        \ + duration\n            }\n\n            // Assign the meeting to the chosen\
        \ room\n            occupiedRooms.enqueue((newEndTime, roomNumToAssign))\n \
        \           roomUsageCount(roomNumToAssign) += 1\n        }\n\n        // Find\
        \ the room with the most meetings\n        var maxMeetings = -1\n        var\
        \ mostBookedRoom = -1\n        for (i <- 0 until n) {\n            if (roomUsageCount(i)\
        \ > maxMeetings) {\n                maxMeetings = roomUsageCount(i)\n      \
        \          mostBookedRoom = i\n            }\n            // If counts are equal,\
        \ the problem asks for the lowest room number,\n            // which is naturally\
        \ handled by iterating from i=0 to n-1.\n            // The first one encountered\
        \ with max_meetings will be the lowest room number.\n        }\n\n        mostBookedRoom\n\
        \    }\n}"
      rust: "use std::collections::BinaryHeap;\nuse std::cmp::Reverse;\n\nstruct Meeting\
        \ { \n    start: i32, \n    end: i32, \n}\n\nimpl PartialEq for Meeting {\n\
        \    fn eq(&self, other: &Self) -> bool {\n        self.start == other.start\n\
        \    }\n}\n\nimpl Eq for Meeting {}\n\nimpl PartialOrd for Meeting {\n    fn\
        \ partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {\n       \
        \ self.start.partial_cmp(&other.start)\n    }\n}\n\nimpl Ord for Meeting {\n\
        \    fn cmp(&self, other: &Self) -> std::cmp::Ordering {\n        self.start.cmp(&other.start)\n\
        \    }\n}\n\n#[derive(PartialEq, Eq, PartialOrd, Ord)]\nstruct RoomEvent {\n\
        \    end_time: i64,\n    room_num: i32,\n}\n\nimpl RoomEvent {\n    fn new(end_time:\
        \ i64, room_num: i32) -> Self {\n        RoomEvent { end_time, room_num }\n\
        \    }\n}\n\nimpl Solution {\n    pub fn most_booked(n: i32, meetings: Vec<Vec<i32>>)\
        \ -> i32 {\n        // 1. Sort meetings by their original start times\n    \
        \    let mut meetings_structs: Vec<Meeting> = meetings.into_iter().map(|m| Meeting\
        \ { start: m[0], end: m[1] }).collect();\n        meetings_structs.sort_unstable();\n\
        \n        // Min-heap for available rooms (stores room numbers)\n        let\
        \ mut available_rooms: BinaryHeap<Reverse<i32>> = BinaryHeap::new();\n     \
        \   for i in 0..n {\n            available_rooms.push(Reverse(i));\n       \
        \ }\n\n        // Min-heap for occupied rooms (stores (end_time, room_number))\n\
        \        // Sorted by end_time, then room_number for ties\n        let mut occupied_rooms:\
        \ BinaryHeap<Reverse<RoomEvent>> = BinaryHeap::new();\n\n        // Array to\
        \ count meetings for each room\n        let mut room_usage_count: Vec<i32> =\
        \ vec![0; n as usize];\n\n        for meeting in meetings_structs {\n      \
        \      let start = meeting.start as i64;\n            let end = meeting.end\
        \ as i64;\n            let duration = end - start;\n\n            // Free up\
        \ rooms whose meetings have ended by the current meeting's start time\n    \
        \        while let Some(Reverse(event)) = occupied_rooms.peek() {\n        \
        \        if event.end_time <= start {\n                    let Reverse(room_event)\
        \ = occupied_rooms.pop().unwrap();\n                    available_rooms.push(Reverse(room_event.room_num));\n\
        \                } else {\n                    break;\n                }\n \
        \           }\n\n            let room_num_to_assign: i32;\n            let new_end_time:\
        \ i64;\n\n            if let Some(Reverse(room_num)) = available_rooms.pop()\
        \ {\n                // If there are available rooms, take the one with the\
        \ lowest number\n                room_num_to_assign = room_num;\n          \
        \      new_end_time = end; // Meeting starts at its original start time\n  \
        \          } else {\n                // No available rooms, delay the current\
        \ meeting\n                // Take the room that will become free earliest\n\
        \                let Reverse(earliest_free_room_event) = occupied_rooms.pop().unwrap();\n\
        \n                let earliest_free_time = earliest_free_room_event.end_time;\n\
        \                room_num_to_assign = earliest_free_room_event.room_num;\n\n\
        \                // The delayed meeting starts when this room becomes free\n\
        \                // Its new end time is earliest_free_time + duration\n    \
        \            new_end_time = earliest_free_time + duration;\n            }\n\n\
        \            // Assign the meeting to the chosen room\n            occupied_rooms.push(Reverse(RoomEvent::new(new_end_time,\
        \ room_num_to_assign)));\n            room_usage_count[room_num_to_assign as\
        \ usize] += 1;\n        }\n\n        // Find the room with the most meetings\n\
        \        let mut max_meetings = -1;\n        let mut most_booked_room = -1;\n\
        \        for i in 0..n {\n            if room_usage_count[i as usize] > max_meetings\
        \ {\n                max_meetings = room_usage_count[i as usize];\n        \
        \        most_booked_room = i;\n            }\n            // If counts are\
        \ equal, the problem asks for the lowest room number,\n            // which\
        \ is naturally handled by iterating from i=0 to n-1.\n            // The first\
        \ one encountered with max_meetings will be the lowest room number.\n      \
        \  }\n\n        most_booked_room\n    }\n}"
      racket: "#lang racket\n\n(require data/heap)\n\n(define (most-booked n meetings)\n\
        \  ;; 1. Sort meetings by their original start times\n  (define sorted-meetings\
        \ (sort meetings (lambda (a b) (< (car a) (car b)))))\n\n  ;; Min-heap for available\
        \ rooms (stores room numbers)\n  (define available-rooms (make-heap (lambda\
        \ (a b) (< a b))))\n  (for ([i (in-range n)])\n    (heap-add! available-rooms\
        \ i))\n\n  ;; Min-heap for occupied rooms (stores (end_time, room_number))\n\
        \  ;; Sorted by end_time, then room_number for ties\n  (define occupied-rooms\n\
        \    (make-heap (lambda (a b)\n                 (let ([end-time-a (car a)]\n\
        \                       [end-time-b (car b)])\n                   (if (not (=\
        \ end-time-a end-time-b))\n                       (< end-time-a end-time-b)\n\
        \                       (< (cadr a) (cadr b)))))))\n\n  ;; Array to count meetings\
        \ for each room\n  (define room-usage-count (make-vector n 0))\n\n  (for ([meeting\
        \ sorted-meetings])\n    (define start (car meeting))\n    (define end (cadr\
        \ meeting))\n    (define duration (- end start))\n\n    ;; Free up rooms whose\
        \ meetings have ended by the current meeting's start time\n    (while (and (not\
        \ (heap-empty? occupied-rooms))\n                (<= (car (heap-min occupied-rooms))\
        \ start))\n      (define room-info (heap-extract-min! occupied-rooms))\n   \
        \   (define room-num (cadr room-info))\n      (heap-add! available-rooms room-num))\n\
        \n    (define room-num-to-assign #f)\n    (define new-end-time #f)\n\n    (if\
        \ (not (heap-empty? available-rooms))\n        (begin\n          ;; If there\
        \ are available rooms, take the one with the lowest number\n          (set!\
        \ room-num-to-assign (heap-extract-min! available-rooms))\n          (set! new-end-time\
        \ end)) ;; Meeting starts at its original start time\n        (begin\n     \
        \     ;; No available rooms, delay the current meeting\n          ;; Take the\
        \ room that will become free earliest\n          (define earliest-free-room-info\
        \ (heap-extract-min! occupied-rooms))\n\n          (define earliest-free-time\
        \ (car earliest-free-room-info))\n          (set! room-num-to-assign (cadr earliest-free-room-info))\n\
        \n          ;; The delayed meeting starts when this room becomes free\n    \
        \      ;; Its new end time is earliest-free-time + duration\n          (set!\
        \ new-end-time (+ earliest-free-time duration))))\n\n    ;; Assign the meeting\
        \ to the chosen room\n    (heap-add! occupied-rooms (list new-end-time room-num-to-assign))\n\
        \    (vector-set! room-usage-count room-num-to-assign (+ (vector-ref room-usage-count\
        \ room-num-to-assign) 1)))\n\n  ;; Find the room with the most meetings\n  (define\
        \ max-meetings -1)\n  (define most-booked-room -1)\n  (for ([i (in-range n)])\n\
        \    (when (> (vector-ref room-usage-count i) max-meetings)\n      (set! max-meetings\
        \ (vector-ref room-usage-count i))\n      (set! most-booked-room i)))\n\n  most-booked-room)"
      erlang: "-module(solution).\n-export([most_booked/2]).\n\n%% Helper for min-heap\
        \ (priority queue) functionality\n%% Using gb_trees as a balanced binary tree,\
        \ which can simulate a min-heap\n%% Keys are {priority, value} tuples for ordering.\n\
        \n%% Comparator for available rooms (room numbers)\n-spec available_room_comparator(integer(),\
        \ integer()) -> boolean().\navailable_room_comparator(RoomA, RoomB) ->\n   \
        \ RoomA < RoomB.\n\n%% Comparator for occupied rooms ({end_time, room_number})\n\
        -spec occupied_room_comparator({integer(), integer()}, {integer(), integer()})\
        \ -> boolean().\noccupied_room_comparator({EndTimeA, RoomNumA}, {EndTimeB, RoomNumB})\
        \ ->\n    if\n        EndTimeA =/= EndTimeB -> EndTimeA < EndTimeB;\n      \
        \  true -> RoomNumA < RoomNumB\n    end.\n\n-spec most_booked(integer(), list(list(integer())))\
        \ -> integer().\nmost_booked(N, Meetings) ->\n    %% 1. Sort meetings by their\
        \ original start times\n    SortedMeetings = lists:sort(fun(A, B) -> hd(A) <\
        \ hd(B) end, Meetings),\n\n    %% Min-heap for available rooms (stores room\
        \ numbers)\n    AvailableRooms = lists:foldl(fun(I, Acc) -> gb_trees:insert({I,\
        \ I}, Acc) end, gb_trees:empty(), lists:seq(0, N - 1)),\n\n    %% Min-heap for\
        \ occupied rooms (stores {end_time, room_number})\n    OccupiedRooms = gb_trees:empty(),\n\
        \n    %% Array to count meetings for each room\n    RoomUsageCount = array:new([{size,\
        \ N}, {fixed, true}, {default, 0}]),\n\n    {_FinalAvailableRooms, _FinalOccupiedRooms,\
        \ FinalRoomUsageCount} = lists:foldl(\n        fun(Meeting, {CurrentAvailableRooms,\
        \ CurrentOccupiedRooms, CurrentRoomUsageCount}) ->\n            [Start, End]\
        \ = Meeting,\n            Duration = End - Start,\n\n            %% Free up\
        \ rooms whose meetings have ended by the current meeting's start time\n    \
        \        {UpdatedAvailableRooms, UpdatedOccupiedRooms} = free_up_rooms(Start,\
        \ CurrentAvailableRooms, CurrentOccupiedRooms),\n\n            RoomNumToAssign\
        \ = -1,\n            NewEndTime = -1,\n\n            if\n                gb_trees:is_empty(UpdatedAvailableRooms)\
        \ == false ->\n                    %% If there are available rooms, take the\
        \ one with the lowest number\n                    {{_Priority, RoomNum}, TempAvailableRooms}\
        \ = gb_trees:take_smallest(UpdatedAvailableRooms),\n                    RoomNumToAssign\
        \ = RoomNum,\n                    NewEndTime = End,\n                    {TempAvailableRooms,\
        \ UpdatedOccupiedRooms};\n                true ->\n                    %% No\
        \ available rooms, delay the current meeting\n                    %% Take the\
        \ room that will become free earliest\n                    {{EarliestFreeTime,\
        \ RoomNum}, TempOccupiedRooms} = gb_trees:take_smallest(UpdatedOccupiedRooms),\n\
        \                    RoomNumToAssign = RoomNum,\n                    NewEndTime\
        \ = EarliestFreeTime + Duration,\n                    {UpdatedAvailableRooms,\
        \ TempOccupiedRooms}\n            end,\n\n            %% Assign the meeting\
        \ to the chosen room\n            NewOccupiedRooms = gb_trees:insert({NewEndTime,\
        \ RoomNumToAssign}, {NewEndTime, RoomNumToAssign}, UpdatedOccupiedRooms),\n\
        \            UpdatedRoomUsageCount = array:set(RoomNumToAssign, array:get(RoomNumToAssign,\
        \ CurrentRoomUsageCount) + 1, CurrentRoomUsageCount),\n\n            {UpdatedAvailableRooms,\
        \ NewOccupiedRooms, UpdatedRoomUsageCount}\n        end,\n        {AvailableRooms,\
        \ OccupiedRooms, RoomUsageCount},\n        SortedMeetings\n    ),\n\n    %%\
        \ Find the room with the most meetings\n    MaxMeetings = -1,\n    MostBookedRoom\
        \ = -1,\n    {_MaxMeetings, _MostBookedRoom} = lists:foldl(\n        fun(I,\
        \ {CurrentMaxMeetings, CurrentMostBookedRoom}) ->\n            Count = array:get(I,\
        \ FinalRoomUsageCount),\n            if\n                Count > CurrentMaxMeetings\
        \ -> {Count, I};\n                true -> {CurrentMaxMeetings, CurrentMostBookedRoom}\n\
        \            end\n        end,\n        {MaxMeetings, MostBookedRoom},\n   \
        \     lists:seq(0, N - 1)\n    ),\n    _MostBookedRoom.\n\n\nfree_up_rooms(CurrentStartTime,\
        \ AvailableRooms, OccupiedRooms) ->\n    if\n        gb_trees:is_empty(OccupiedRooms)\
        \ == false andalso element(1, gb_trees:smallest(OccupiedRooms)) =< CurrentStartTime\
        \ ->\n            {{_EndTime, RoomNum}, TempOccupiedRooms} = gb_trees:take_smallest(OccupiedRooms),\n\
        \            NewAvailableRooms = gb_trees:insert({RoomNum, RoomNum}, AvailableRooms),\n\
        \            free_up_rooms(CurrentStartTime, NewAvailableRooms, TempOccupiedRooms);\n\
        \        true ->\n            {AvailableRooms, OccupiedRooms}\n    end."
      elixir: "defmodule Solution do\n  @spec most_booked(n :: integer, meetings ::\
        \ [[integer]]) :: integer\n  def most_booked(n, meetings) do\n    # 1. Sort\
        \ meetings by their original start times\n    sorted_meetings = Enum.sort(meetings,\
        \ fn [s1, _], [s2, _] -> s1 < s2 end)\n\n    # Min-heap for available rooms\
        \ (stores room numbers)\n    # Using :gb_trees as a balanced binary tree, which\
        \ can simulate a min-heap\n    # Keys are {priority, value} tuples for ordering.\n\
        \    available_rooms = Enum.reduce(0..(n - 1), :gb_trees.empty(), fn i, acc\
        \ ->\n      :gb_trees.insert({i, i}, acc)\n    end)\n\n    # Min-heap for occupied\
        \ rooms (stores {end_time, room_number})\n    occupied_rooms = :gb_trees.empty()\n\
        \n    # Array to count meetings for each room\n    room_usage_count = :array.new([{size:\
        \ n, fixed: true, default: 0}])\n\n    {_final_available_rooms, _final_occupied_rooms,\
        \ final_room_usage_count} = Enum.reduce(\n      sorted_meetings,\n      {available_rooms,\
        \ occupied_rooms, room_usage_count},\n      fn [start, ending], {current_available_rooms,\
        \ current_occupied_rooms, current_room_usage_count} ->\n        duration = ending\
        \ - start\n\n        # Free up rooms whose meetings have ended by the current\
        \ meeting's start time\n        {updated_available_rooms, updated_occupied_rooms}\
        \ = free_up_rooms(start, current_available_rooms, current_occupied_rooms)\n\n\
        \        {room_num_to_assign, new_end_time, temp_available_rooms, temp_occupied_rooms}\
        \ = \n          if :gb_trees.is_empty(updated_available_rooms) == false do\n\
        \            # If there are available rooms, take the one with the lowest number\n\
        \            {{_priority, room_num}, temp_available_rooms} = :gb_trees.take_smallest(updated_available_rooms)\n\
        \            {room_num, ending, temp_available_rooms, updated_occupied_rooms}\n\
        \          else\n            # No available rooms, delay the current meeting\n\
        \            # Take the room that will become free earliest\n            {{earliest_free_time,\
        \ room_num}, temp_occupied_rooms} = :gb_trees.take_smallest(updated_occupied_rooms)\n\
        \            new_end_time = earliest_free_time + duration\n            {room_num,\
        \ new_end_time, updated_available_rooms, temp_occupied_rooms}\n          end\n\
        \n        # Assign the meeting to the chosen room\n        new_occupied_rooms\
        \ = :gb_trees.insert({new_end_time, room_num_to_assign}, {new_end_time, room_num_to_assign},\
        \ temp_occupied_rooms)\n        updated_room_usage_count = :array.set(room_num_to_assign,\
        \ :array.get(room_num_to_assign, current_room_usage_count) + 1, current_room_usage_count)\n\
        \n        {temp_available_rooms, new_occupied_rooms, updated_room_usage_count}\n\
        \      end\n    )\n\n    # Find the room with the most meetings\n    max_meetings\
        \ = -1\n    most_booked_room = -1\n    {_max_meetings, final_most_booked_room}\
        \ = Enum.reduce(\n      0..(n - 1),\n      {max_meetings, most_booked_room},\n\
        \      fn i, {current_max_meetings, current_most_booked_room} ->\n        count\
        \ = :array.get(i, final_room_usage_count)\n        if count > current_max_meetings\
        \ do\n          {count, i}\n        else\n          {current_max_meetings, current_most_booked_room}\n\
        \        end\n      end\n    )\n    final_most_booked_room\n  end\n\n  defp\
        \ free_up_rooms(current_start_time, available_rooms, occupied_rooms) do\n  \
        \  if :gb_trees.is_empty(occupied_rooms) == false and :gb_trees.smallest(occupied_rooms)\
        \ |> elem(0) <= current_start_time do\n      {{_end_time, room_num}, temp_occupied_rooms}\
        \ = :gb_trees.take_smallest(occupied_rooms)\n      new_available_rooms = :gb_trees.insert({room_num,\
        \ room_num}, available_rooms)\n      free_up_rooms(current_start_time, new_available_rooms,\
        \ temp_occupied_rooms)\n    else\n      {available_rooms, occupied_rooms}\n\
        \    end\n  end\nend"
    approach: 'The problem requires simulating the allocation of meetings to rooms based
      on specific rules. The core idea is to process meetings in the order of their
      original start times. This necessitates sorting the input `meetings` array by
      `start_i`. To efficiently manage room availability, two min-priority queues (min-heaps)
      are used: one for `available_rooms` (storing room numbers) and another for `occupied_rooms`
      (storing `[end_time, room_number]` for meetings currently in progress). A `room_usage_count`
      array tracks how many meetings each room has hosted.'
    time_complexity: The time complexity is dominated by sorting the meetings, which
      takes O(M log M) time, where M is the number of meetings. The subsequent iteration
      through M meetings involves heap operations. Each meeting triggers at most one
      push and one pop operation on either the `available_rooms` or `occupied_rooms`
      heap. Additionally, the `while` loop to free up rooms processes each `(end_time,
      room_number)` pair at most once across all meetings. Since each heap operation
      takes O(log N) time (where N is the number of rooms), the total time for heap
      operations is O((M + N) log N). Finally, finding the most booked room takes O(N)
      time. Combining these, the overall time complexity is O(M log M + (M + N) log
      N).
    space_complexity: The space complexity is determined by the data structures used.
      Storing the sorted meetings (if a copy is made) takes O(M) space. The `available_rooms`
      and `occupied_rooms` heaps can each hold up to N elements, contributing O(N) space.
      The `room_usage_count` array also takes O(N) space. Therefore, the total space
      complexity is O(M + N).
    elapsed_time: 125.79604625701904
    model: gemini-2.5-flash
    generated_at: '2025-12-27 01:07:46 '
  - solutions:
      cpp: "class Solution {\npublic:\n    int mostBooked(int n, vector<vector<int>>&\
        \ meetings) {\n        sort(meetings.begin(), meetings.end());\n        priority_queue<int,\
        \ vector<int>, greater<int>> free_rooms;\n        priority_queue<pair<int, int>,\
        \ vector<pair<int, int>>, greater<pair<int, int>>> end_times;\n        vector<int>\
        \ room_usage(n, 0);\n        for (int i = 0; i < n; i++) {\n            free_rooms.push(i);\n\
        \        }\n        for (auto& meeting : meetings) {\n            int start\
        \ = meeting[0], end = meeting[1];\n            while (!end_times.empty() &&\
        \ end_times.top().first <= start) {\n                free_rooms.push(end_times.top().second);\n\
        \                end_times.pop();\n            }\n            if (!free_rooms.empty())\
        \ {\n                int room = free_rooms.top();\n                free_rooms.pop();\n\
        \                room_usage[room]++;\n                end_times.push({end, room});\n\
        \            } else {\n                int room = end_times.top().second;\n\
        \                int new_end = end_times.top().first + (end - start);\n    \
        \            end_times.pop();\n                room_usage[room]++;\n       \
        \         end_times.push({new_end, room});\n            }\n        }\n     \
        \   int max_usage = 0, max_room = 0;\n        for (int i = 0; i < n; i++) {\n\
        \            if (room_usage[i] > max_usage) {\n                max_usage = room_usage[i];\n\
        \                max_room = i;\n            }\n        }\n        return max_room;\n\
        \    }\n};"
      java: "class Solution {\n    public int mostBooked(int n, int[][] meetings) {\n\
        \        Arrays.sort(meetings, (a, b) -> a[0] - b[0]);\n        PriorityQueue<Integer>\
        \ freeRooms = new PriorityQueue<>();\n        PriorityQueue<int[]> endTimes\
        \ = new PriorityQueue<>((a, b) -> a[0] - b[0]);\n        int[] roomUsage = new\
        \ int[n];\n        for (int i = 0; i < n; i++) {\n            freeRooms.add(i);\n\
        \        }\n        for (int[] meeting : meetings) {\n            int start\
        \ = meeting[0], end = meeting[1];\n            while (!endTimes.isEmpty() &&\
        \ endTimes.peek()[0] <= start) {\n                freeRooms.add(endTimes.poll()[1]);\n\
        \            }\n            if (!freeRooms.isEmpty()) {\n                int\
        \ room = freeRooms.poll();\n                roomUsage[room]++;\n           \
        \     endTimes.add(new int[] {end, room});\n            } else {\n         \
        \       int[] top = endTimes.poll();\n                int newEnd = top[0] +\
        \ (end - start);\n                roomUsage[top[1]]++;\n                endTimes.add(new\
        \ int[] {newEnd, top[1]});\n            }\n        }\n        int maxUsage =\
        \ 0, maxRoom = 0;\n        for (int i = 0; i < n; i++) {\n            if (roomUsage[i]\
        \ > maxUsage) {\n                maxUsage = roomUsage[i];\n                maxRoom\
        \ = i;\n            }\n        }\n        return maxRoom;\n    }\n}"
      python: "class Solution:\n    def mostBooked(self, n: int, meetings: List[List[int]])\
        \ -> int:\n        meetings.sort(key=lambda x: x[0])\n        free_rooms = list(range(n))\n\
        \        end_times = []\n        room_usage = [0] * n\n        for start, end\
        \ in meetings:\n            while end_times and end_times[0][0] <= start:\n\
        \                heapq.heappop(end_times)\n                free_rooms.append(end_times[0][1])\n\
        \            if free_rooms:\n                room = free_rooms.pop(0)\n    \
        \            room_usage[room] += 1\n                heapq.heappush(end_times,\
        \ (end, room))\n            else:\n                top = heapq.heappop(end_times)\n\
        \                new_end = top[0] + (end - start)\n                room_usage[top[1]]\
        \ += 1\n                heapq.heappush(end_times, (new_end, top[1]))\n     \
        \   max_usage = max(room_usage)\n        for i in range(n):\n            if\
        \ room_usage[i] == max_usage:\n                return i"
      python3: "class Solution:\n    def mostBooked(self, n: int, meetings: List[List[int]])\
        \ -> int:\n        meetings.sort(key=lambda x: x[0])\n        free_rooms = list(range(n))\n\
        \        end_times = []\n        room_usage = [0] * n\n        for start, end\
        \ in meetings:\n            while end_times and end_times[0][0] <= start:\n\
        \                heapq.heappop(end_times)\n                free_rooms.append(end_times[0][1])\n\
        \            if free_rooms:\n                room = free_rooms.pop(0)\n    \
        \            room_usage[room] += 1\n                heapq.heappush(end_times,\
        \ (end, room))\n            else:\n                top = heapq.heappop(end_times)\n\
        \                new_end = top[0] + (end - start)\n                room_usage[top[1]]\
        \ += 1\n                heapq.heappush(end_times, (new_end, top[1]))\n     \
        \   max_usage = max(room_usage)\n        for i in range(n):\n            if\
        \ room_usage[i] == max_usage:\n                return i"
      c: Not available for this problem
      csharp: Not available for this problem
      javascript: Not available for this problem
      typescript: Not available for this problem
      php: Not available for this problem
      swift: Not available for this problem
      kotlin: Not available for this problem
      dart: Not available for this problem
      go: Not available for this problem
      ruby: Not available for this problem
      scala: Not available for this problem
      rust: Not available for this problem
      racket: Not available for this problem
      erlang: Not available for this problem
      elixir: Not available for this problem
    approach: The problem can be solved by using two min heaps, one to keep track of
      the free rooms and the other to keep track of the end times of the meetings. The
      meetings are first sorted based on their start times. Then, for each meeting,
      we check if there are any free rooms. If there are, we use the room with the smallest
      number. Otherwise, we assign the meeting to the room whose meeting will end the
      soonest. We also keep track of the number of times each room is used in an array.
      The room with the maximum usage is the answer. The key intuition here is to always
      assign the meeting to the room that will be free the earliest, which ensures that
      the meetings are held as soon as possible.
    time_complexity: The time complexity of the solution is O(n log n + m log n) where
      n is the number of rooms and m is the number of meetings. This is because we are
      sorting the meetings based on their start times, which takes O(m log m) time.
      Then, for each meeting, we are using the two min heaps to find the free room or
      the room that will be free the earliest, which takes O(log n) time. Therefore,
      the total time complexity is O(n log n + m log n).
    space_complexity: The space complexity of the solution is O(n + m) where n is the
      number of rooms and m is the number of meetings. This is because we are using
      two min heaps to keep track of the free rooms and the end times of the meetings,
      which takes O(n + m) space. We are also using an array to keep track of the number
      of times each room is used, which takes O(n) space. Therefore, the total space
      complexity is O(n + m).
    elapsed_time: 3.514883279800415
    model: llama-3.3-70b-versatile
    generated_at: '2025-12-27 01:07:49 '
---

## Problem #2402: Meeting Rooms III

**Difficulty:** Hard

**Topics:** Array, Hash Table, Sorting, Heap (Priority Queue), Simulation

## Problem Description

<p>You are given an integer <code>n</code>. There are <code>n</code> rooms numbered from <code>0</code> to <code>n - 1</code>.</p>

<p>You are given a 2D integer array <code>meetings</code> where <code>meetings[i] = [start<sub>i</sub>, end<sub>i</sub>]</code> means that a meeting will be held during the <strong>half-closed</strong> time interval <code>[start<sub>i</sub>, end<sub>i</sub>)</code>. All the values of <code>start<sub>i</sub></code> are <strong>unique</strong>.</p>

<p>Meetings are allocated to rooms in the following manner:</p>

<ol>
	<li>Each meeting will take place in the unused room with the <strong>lowest</strong> number.</li>
	<li>If there are no available rooms, the meeting will be delayed until a room becomes free. The delayed meeting should have the <strong>same</strong> duration as the original meeting.</li>
	<li>When a room becomes unused, meetings that have an earlier original <strong>start</strong> time should be given the room.</li>
</ol>

<p>Return<em> the <strong>number</strong> of the room that held the most meetings. </em>If there are multiple rooms, return<em> the room with the <strong>lowest</strong> number.</em></p>

<p>A <strong>half-closed interval</strong> <code>[a, b)</code> is the interval between <code>a</code> and <code>b</code> <strong>including</strong> <code>a</code> and <strong>not including</strong> <code>b</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]
<strong>Output:</strong> 0
<strong>Explanation:</strong>
- At time 0, both rooms are not being used. The first meeting starts in room 0.
- At time 1, only room 1 is not being used. The second meeting starts in room 1.
- At time 2, both rooms are being used. The third meeting is delayed.
- At time 3, both rooms are being used. The fourth meeting is delayed.
- At time 5, the meeting in room 1 finishes. The third meeting starts in room 1 for the time period [5,10).
- At time 10, the meetings in both rooms finish. The fourth meeting starts in room 0 for the time period [10,11).
Both rooms 0 and 1 held 2 meetings, so we return 0. 
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 3, meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]
<strong>Output:</strong> 1
<strong>Explanation:</strong>
- At time 1, all three rooms are not being used. The first meeting starts in room 0.
- At time 2, rooms 1 and 2 are not being used. The second meeting starts in room 1.
- At time 3, only room 2 is not being used. The third meeting starts in room 2.
- At time 4, all three rooms are being used. The fourth meeting is delayed.
- At time 5, the meeting in room 2 finishes. The fourth meeting starts in room 2 for the time period [5,10).
- At time 6, all three rooms are being used. The fifth meeting is delayed.
- At time 10, the meetings in rooms 1 and 2 finish. The fifth meeting starts in room 1 for the time period [10,12).
Room 0 held 1 meeting while rooms 1 and 2 each held 2 meetings, so we return 1. 
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>1 &lt;= meetings.length &lt;= 10<sup>5</sup></code></li>
	<li><code>meetings[i].length == 2</code></li>
	<li><code>0 &lt;= start<sub>i</sub> &lt; end<sub>i</sub> &lt;= 5 * 10<sup>5</sup></code></li>
	<li>All the values of <code>start<sub>i</sub></code> are <strong>unique</strong>.</li>
</ul>


## Hints

1. Sort meetings based on start times.

2. Use two min heaps, the first one keeps track of the numbers of all the rooms that are free. The second heap keeps track of the end times of all the meetings that are happening and the room that they are in.

3. Keep track of the number of times each room is used in an array.

4. With each meeting, check if there are any free rooms. If there are, then use the room with the smallest number. Otherwise, assign the meeting to the room whose meeting will end the soonest.

## 🤖 AI-Generated Solutions

We've generated solutions using multiple AI models. Click to expand each solution:


<details class="ai-solution-card" open markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">✨ Solution from <strong>gemini-2.5-flash</strong></span>
  <small class="solution-timestamp">(2025-12-27 01:07:46 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem requires simulating the allocation of meetings to rooms based on specific rules. The core idea is to process meetings in the order of their original start times. This necessitates sorting the input `meetings` array by `start_i`. To efficiently manage room availability, two min-priority queues (min-heaps) are used: one for `available_rooms` (storing room numbers) and another for `occupied_rooms` (storing `[end_time, room_number]` for meetings currently in progress). A `room_usage_count` array tracks how many meetings each room has hosted.

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
#include <algorithm>
#include <queue> // For priority_queue
#include <utility> // For std::pair

class Solution {
public:
    int mostBooked(int n, std::vector<std::vector<int>>& meetings) {
        // 1. Sort meetings by their original start times
        std::sort(meetings.begin(), meetings.end());

        // Min-heap for available rooms (stores room numbers)
        // std::priority_queue is max-heap by default, use std::greater for min-heap
        std::priority_queue<int, std::vector<int>, std::greater<int>> available_rooms;
        for (int i = 0; i < n; ++i) {
            available_rooms.push(i);
        }

        // Min-heap for occupied rooms (stores (end_time, room_number))
        // Sorted by end_time, then room_number for ties
        // Use long long for end_time to prevent overflow
        std::priority_queue<std::pair<long long, int>, 
                            std::vector<std::pair<long long, int>>, 
                            std::greater<std::pair<long long, int>>> occupied_rooms;

        // Array to count meetings for each room
        std::vector<int> room_usage_count(n, 0);

        for (const auto& meeting : meetings) {
            long long start = meeting[0];
            long long end = meeting[1];
            long long duration = end - start;

            // Free up rooms whose meetings have ended by the current meeting's start time
            while (!occupied_rooms.empty() && occupied_rooms.top().first <= start) {
                int room_num = occupied_rooms.top().second;
                occupied_rooms.pop();
                available_rooms.push(room_num);
            }

            int room_num_to_assign;
            long long new_end_time;

            if (!available_rooms.empty()) {
                // If there are available rooms, take the one with the lowest number
                room_num_to_assign = available_rooms.top();
                available_rooms.pop();
                new_end_time = end; // Meeting starts at its original start time
            } else {
                // No available rooms, delay the current meeting
                // Take the room that will become free earliest
                std::pair<long long, int> earliest_free_room = occupied_rooms.top();
                occupied_rooms.pop();

                long long earliest_free_time = earliest_free_room.first;
                room_num_to_assign = earliest_free_room.second;

                // The delayed meeting starts when this room becomes free
                // Its new end time is earliest_free_time + duration
                new_end_time = earliest_free_time + duration;
            }

            // Assign the meeting to the chosen room
            occupied_rooms.push({new_end_time, room_num_to_assign});
            room_usage_count[room_num_to_assign]++;
        }

        // Find the room with the most meetings
        int max_meetings = -1;
        int most_booked_room = -1;
        for (int i = 0; i < n; ++i) {
            if (room_usage_count[i] > max_meetings) {
                max_meetings = room_usage_count[i];
                most_booked_room = i;
            }
            // If counts are equal, the problem asks for the lowest room number,
            // which is naturally handled by iterating from i=0 to n-1.
            // The first one encountered with max_meetings will be the lowest room number.
        }

        return most_booked_room;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
import java.util.Arrays;
import java.util.PriorityQueue;

class Solution {
    public int mostBooked(int n, int[][] meetings) {
        // 1. Sort meetings by their original start times
        Arrays.sort(meetings, (a, b) -> Integer.compare(a[0], b[0]));

        // Min-heap for available rooms (stores room numbers)
        PriorityQueue<Integer> availableRooms = new PriorityQueue<>();
        for (int i = 0; i < n; ++i) {
            availableRooms.offer(i);
        }

        // Min-heap for occupied rooms (stores (end_time, room_number))
        // Sorted by end_time, then room_number for ties
        // Each element is an array: [end_time, room_number]
        PriorityQueue<long[]> occupiedRooms = new PriorityQueue<>((a, b) -> {
            if (a[0] != b[0]) {
                return Long.compare(a[0], b[0]);
            }
            return Integer.compare((int)a[1], (int)b[1]);
        });

        // Array to count meetings for each room
        int[] roomUsageCount = new int[n];

        for (int[] meeting : meetings) {
            long start = meeting[0];
            long end = meeting[1];
            long duration = end - start;

            // Free up rooms whose meetings have ended by the current meeting's start time
            while (!occupiedRooms.isEmpty() && occupiedRooms.peek()[0] <= start) {
                long[] roomInfo = occupiedRooms.poll();
                int roomNum = (int)roomInfo[1];
                availableRooms.offer(roomNum);
            }

            int roomNumToAssign;
            long newEndTime;

            if (!availableRooms.isEmpty()) {
                // If there are available rooms, take the one with the lowest number
                roomNumToAssign = availableRooms.poll();
                newEndTime = end; // Meeting starts at its original start time
            } else {
                // No available rooms, delay the current meeting
                // Take the room that will become free earliest
                long[] earliestFreeRoomInfo = occupiedRooms.poll();

                long earliestFreeTime = earliestFreeRoomInfo[0];
                roomNumToAssign = (int)earliestFreeRoomInfo[1];

                // The delayed meeting starts when this room becomes free
                // Its new end time is earliest_free_time + duration
                newEndTime = earliestFreeTime + duration;
            }

            // Assign the meeting to the chosen room
            occupiedRooms.offer(new long[]{newEndTime, roomNumToAssign});
            roomUsageCount[roomNumToAssign]++;
        }

        // Find the room with the most meetings
        int maxMeetings = -1;
        int mostBookedRoom = -1;
        for (int i = 0; i < n; ++i) {
            if (roomUsageCount[i] > maxMeetings) {
                maxMeetings = roomUsageCount[i];
                mostBookedRoom = i;
            }
            // If counts are equal, the problem asks for the lowest room number,
            // which is naturally handled by iterating from i=0 to n-1.
            // The first one encountered with max_meetings will be the lowest room number.
        }

        return mostBookedRoom;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
import heapq

class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        # 1. Sort meetings by their original start times
        meetings.sort()

        # Min-heap for available rooms (stores room numbers)
        # Initially all rooms are available
        available_rooms = list(range(n))
        heapq.heapify(available_rooms)

        # Min-heap for occupied rooms (stores (end_time, room_number))
        # Sorted by end_time, then room_number for ties
        occupied_rooms = [] # (end_time, room_number)

        # Array to count meetings for each room
        room_usage_count = [0] * n

        for start, end in meetings:
            duration = end - start

            # Free up rooms whose meetings have ended by the current meeting's start time
            while occupied_rooms and occupied_rooms[0][0] <= start:
                _, room_num = heapq.heappop(occupied_rooms)
                heapq.heappush(available_rooms, room_num)

            room_num_to_assign: int
            new_end_time: int

            if available_rooms:
                # If there are available rooms, take the one with the lowest number
                room_num_to_assign = heapq.heappop(available_rooms)
                new_end_time = end # Meeting starts at its original start time
            else:
                # No available rooms, delay the current meeting
                # Take the room that will become free earliest
                earliest_free_time, room_num_to_assign = heapq.heappop(occupied_rooms)

                # The delayed meeting starts when this room becomes free
                # Its new end time is earliest_free_time + duration
                new_end_time = earliest_free_time + duration

            # Assign the meeting to the chosen room
            heapq.heappush(occupied_rooms, (new_end_time, room_num_to_assign))
            room_usage_count[room_num_to_assign] += 1

        # Find the room with the most meetings
        max_meetings = -1
        most_booked_room = -1
        for i in range(n):
            if room_usage_count[i] > max_meetings:
                max_meetings = room_usage_count[i]
                most_booked_room = i
            # If counts are equal, the problem asks for the lowest room number,
            # which is naturally handled by iterating from i=0 to n-1.
            # The first one encountered with max_meetings will be the lowest room number.

        return most_booked_room
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
import heapq

class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        # 1. Sort meetings by their original start times
        meetings.sort()

        # Min-heap for available rooms (stores room numbers)
        # Initially all rooms are available
        available_rooms = list(range(n))
        heapq.heapify(available_rooms)

        # Min-heap for occupied rooms (stores (end_time, room_number))
        # Sorted by end_time, then room_number for ties
        occupied_rooms = [] # (end_time, room_number)

        # Array to count meetings for each room
        room_usage_count = [0] * n

        for start, end in meetings:
            duration = end - start

            # Free up rooms whose meetings have ended by the current meeting's start time
            while occupied_rooms and occupied_rooms[0][0] <= start:
                _, room_num = heapq.heappop(occupied_rooms)
                heapq.heappush(available_rooms, room_num)

            room_num_to_assign: int
            new_end_time: int

            if available_rooms:
                # If there are available rooms, take the one with the lowest number
                room_num_to_assign = heapq.heappop(available_rooms)
                new_end_time = end # Meeting starts at its original start time
            else:
                # No available rooms, delay the current meeting
                # Take the room that will become free earliest
                earliest_free_time, room_num_to_assign = heapq.heappop(occupied_rooms)

                # The delayed meeting starts when this room becomes free
                # Its new end time is earliest_free_time + duration
                new_end_time = earliest_free_time + duration

            # Assign the meeting to the chosen room
            heapq.heappush(occupied_rooms, (new_end_time, room_num_to_assign))
            room_usage_count[room_num_to_assign] += 1

        # Find the room with the most meetings
        max_meetings = -1
        most_booked_room = -1
        for i in range(n):
            if room_usage_count[i] > max_meetings:
                max_meetings = room_usage_count[i]
                most_booked_room = i
            # If counts are equal, the problem asks for the lowest room number,
            # which is naturally handled by iterating from i=0 to n-1.
            # The first one encountered with max_meetings will be the lowest room number.

        return most_booked_room
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
#include <stdlib.h>
#include <string.h> 

// Define a struct for meetings to sort them
typedef struct {
    int start;
    int end;
} Meeting;

// Comparator for sorting meetings by start time
int compareMeetings(const void* a, const void* b) {
    return ((Meeting*)a)->start - ((Meeting*)b)->start;
}

// --- Min-Heap for integers (room numbers) ---
typedef struct {
    int* data;
    int size;
    int capacity;
} IntMinHeap;

void initIntMinHeap(IntMinHeap* heap, int capacity) {
    heap->data = (int*)malloc(sizeof(int) * capacity);
    heap->size = 0;
    heap->capacity = capacity;
}

void freeIntMinHeap(IntMinHeap* heap) {
    free(heap->data);
}

void swapInt(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void intHeapifyUp(IntMinHeap* heap, int idx) {
    int parent = (idx - 1) / 2;
    while (idx > 0 && heap->data[idx] < heap->data[parent]) {
        swapInt(&heap->data[idx], &heap->data[parent]);
        idx = parent;
        parent = (idx - 1) / 2;
    }
}

void intHeapifyDown(IntMinHeap* heap, int idx) {
    int smallest = idx;
    int left = 2 * idx + 1;
    int right = 2 * idx + 2;

    if (left < heap->size && heap->data[left] < heap->data[smallest]) {
        smallest = left;
    }
    if (right < heap->size && heap->data[right] < heap->data[smallest]) {
        smallest = right;
    }

    if (smallest != idx) {
        swapInt(&heap->data[idx], &heap->data[smallest]);
        intHeapifyDown(heap, smallest);
    }
}

void intMinHeapPush(IntMinHeap* heap, int val) {
    if (heap->size == heap->capacity) {
        return; 
    }
    heap->data[heap->size] = val;
    heap->size++;
    intHeapifyUp(heap, heap->size - 1);
}

int intMinHeapPop(IntMinHeap* heap) {
    if (heap->size == 0) return -1; 
    int root = heap->data[0];
    heap->data[0] = heap->data[heap->size - 1];
    heap->size--;
    intHeapifyDown(heap, 0);
    return root;
}

int intMinHeapPeek(IntMinHeap* heap) {
    if (heap->size == 0) return -1;
    return heap->data[0];
}

int intMinHeapIsEmpty(IntMinHeap* heap) {
    return heap->size == 0;
}

// --- Min-Heap for (long long end_time, int room_number) pairs ---
typedef struct {
    long long end_time;
    int room_num;
} RoomEvent;

typedef struct {
    RoomEvent* data;
    int size;
    int capacity;
} RoomEventMinHeap;

void initRoomEventMinHeap(RoomEventMinHeap* heap, int capacity) {
    heap->data = (RoomEvent*)malloc(sizeof(RoomEvent) * capacity);
    heap->size = 0;
    heap->capacity = capacity;
}

void freeRoomEventMinHeap(RoomEventMinHeap* heap) {
    free(heap->data);
}

void swapRoomEvent(RoomEvent* a, RoomEvent* b) {
    RoomEvent temp = *a;
    *a = *b;
    *b = temp;
}

// Comparator for RoomEvent: end_time then room_num
int compareRoomEvents(RoomEvent a, RoomEvent b) {
    if (a.end_time != b.end_time) {
        return a.end_time < b.end_time; // true if a has higher priority (smaller end_time)
    }
    return a.room_num < b.room_num; // true if a has higher priority (smaller room_num)
}

void roomEventHeapifyUp(RoomEventMinHeap* heap, int idx) {
    int parent = (idx - 1) / 2;
    while (idx > 0 && compareRoomEvents(heap->data[idx], heap->data[parent])) {
        swapRoomEvent(&heap->data[idx], &heap->data[parent]);
        idx = parent;
        parent = (idx - 1) / 2;
    }
}

void roomEventHeapifyDown(RoomEventMinHeap* heap, int idx) {
    int smallest = idx;
    int left = 2 * idx + 1;
    int right = 2 * idx + 2;

    if (left < heap->size && compareRoomEvents(heap->data[left], heap->data[smallest])) {
        smallest = left;
    }
    if (right < heap->size && compareRoomEvents(heap->data[right], heap->data[smallest])) {
        smallest = right;
    }

    if (smallest != idx) {
        swapRoomEvent(&heap->data[idx], &heap->data[smallest]);
        roomEventHeapifyDown(heap, smallest);
    }
}

void roomEventMinHeapPush(RoomEventMinHeap* heap, RoomEvent val) {
    if (heap->size == heap->capacity) {
        return;
    }
    heap->data[heap->size] = val;
    heap->size++;
    roomEventHeapifyUp(heap, heap->size - 1);
}

RoomEvent roomEventMinHeapPop(RoomEventMinHeap* heap) {
    RoomEvent default_event = {-1, -1}; // Error value
    if (heap->size == 0) return default_event;
    RoomEvent root = heap->data[0];
    heap->data[0] = heap->data[heap->size - 1];
    heap->size--;
    roomEventHeapifyDown(heap, 0);
    return root;
}

RoomEvent roomEventMinHeapPeek(RoomEventMinHeap* heap) {
    RoomEvent default_event = {-1, -1}; // Error value
    if (heap->size == 0) return default_event;
    return heap->data[0];
}

int roomEventMinHeapIsEmpty(RoomEventMinHeap* heap) {
    return heap->size == 0;
}


int mostBooked(int n, int** meetings, int meetingsSize, int* meetingsColSize) {
    // Convert 2D int array to Meeting struct array for easier sorting
    Meeting* meeting_structs = (Meeting*)malloc(sizeof(Meeting) * meetingsSize);
    for (int i = 0; i < meetingsSize; ++i) {
        meeting_structs[i].start = meetings[i][0];
        meeting_structs[i].end = meetings[i][1];
    }

    // 1. Sort meetings by their original start times
    qsort(meeting_structs, meetingsSize, sizeof(Meeting), compareMeetings);

    // Min-heap for available rooms (stores room numbers)
    IntMinHeap available_rooms;
    initIntMinHeap(&available_rooms, n);
    for (int i = 0; i < n; ++i) {
        intMinHeapPush(&available_rooms, i);
    }

    // Min-heap for occupied rooms (stores (end_time, room_number))
    RoomEventMinHeap occupied_rooms;
    initRoomEventMinHeap(&occupied_rooms, n);

    // Array to count meetings for each room
    int* room_usage_count = (int*)calloc(n, sizeof(int)); // calloc initializes to 0

    for (int i = 0; i < meetingsSize; ++i) {
        long long start = meeting_structs[i].start;
        long long end = meeting_structs[i].end;
        long long duration = end - start;

        // Free up rooms whose meetings have ended by the current meeting's start time
        while (!roomEventMinHeapIsEmpty(&occupied_rooms) && roomEventMinHeapPeek(&occupied_rooms).end_time <= start) {
            RoomEvent room_event = roomEventMinHeapPop(&occupied_rooms);
            int room_num = room_event.room_num;
            intMinHeapPush(&available_rooms, room_num);
        }

        int room_num_to_assign;
        long long new_end_time;

        if (!intMinHeapIsEmpty(&available_rooms)) {
            // If there are available rooms, take the one with the lowest number
            room_num_to_assign = intMinHeapPop(&available_rooms);
            new_end_time = end; // Meeting starts at its original start time
        } else {
            // No available rooms, delay the current meeting
            // Take the room that will become free earliest
            RoomEvent earliest_free_room = roomEventMinHeapPop(&occupied_rooms);

            long long earliest_free_time = earliest_free_room.end_time;
            room_num_to_assign = earliest_free_room.room_num;

            // The delayed meeting starts when this room becomes free
            // Its new end time is earliest_free_time + duration
            new_end_time = earliest_free_time + duration;
        }

        // Assign the meeting to the chosen room
        RoomEvent new_event = {new_end_time, room_num_to_assign};
        roomEventMinHeapPush(&occupied_rooms, new_event);
        room_usage_count[room_num_to_assign]++;
    }

    // Find the room with the most meetings
    int max_meetings = -1;
    int most_booked_room = -1;
    for (int i = 0; i < n; ++i) {
        if (room_usage_count[i] > max_meetings) {
            max_meetings = room_usage_count[i];
            most_booked_room = i;
        }
    }

    // Clean up allocated memory
    free(meeting_structs);
    freeIntMinHeap(&available_rooms);
    freeRoomEventMinHeap(&occupied_rooms);
    free(room_usage_count);

    return most_booked_room;
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
    public int MostBooked(int n, int[][] meetings) {
        // 1. Sort meetings by their original start times
        Array.Sort(meetings, (a, b) => a[0].CompareTo(b[0]));

        // Min-heap for available rooms (stores room numbers)
        var availableRooms = new SortedSet<int>(); // Acts as a min-heap for room numbers
        for (int i = 0; i < n; ++i) {
            availableRooms.Add(i);
        }

        // Min-heap for occupied rooms (stores (end_time, room_number))
        // Sorted by end_time, then room_number for ties
        // Using a custom comparer for PriorityQueue
        var occupiedRooms = new PriorityQueue<(long endTime, int roomNum), (long endTime, int roomNum)>(
            Comparer<(long endTime, int roomNum)>.Create((a, b) => {
                int cmp = a.endTime.CompareTo(b.endTime);
                if (cmp != 0) return cmp;
                return a.roomNum.CompareTo(b.roomNum);
            })
        );

        // Array to count meetings for each room
        int[] roomUsageCount = new int[n];

        foreach (var meeting in meetings) {
            long start = meeting[0];
            long end = meeting[1];
            long duration = end - start;

            // Free up rooms whose meetings have ended by the current meeting's start time
            while (occupiedRooms.Count > 0 && occupiedRooms.Peek().endTime <= start) {
                var roomInfo = occupiedRooms.Dequeue();
                int roomNum = roomInfo.roomNum;
                availableRooms.Add(roomNum);
            }

            int roomNumToAssign;
            long newEndTime;

            if (availableRooms.Count > 0) {
                // If there are available rooms, take the one with the lowest number
                roomNumToAssign = availableRooms.Min;
                availableRooms.Remove(roomNumToAssign);
                newEndTime = end; // Meeting starts at its original start time
            } else {
                // No available rooms, delay the current meeting
                // Take the room that will become free earliest
                var earliestFreeRoomInfo = occupiedRooms.Dequeue();

                long earliestFreeTime = earliestFreeRoomInfo.endTime;
                roomNumToAssign = earliestFreeRoomInfo.roomNum;

                // The delayed meeting starts when this room becomes free
                // Its new end time is earliest_free_time + duration
                newEndTime = earliestFreeTime + duration;
            }

            // Assign the meeting to the chosen room
            occupiedRooms.Enqueue((newEndTime, roomNumToAssign), (newEndTime, roomNumToAssign));
            roomUsageCount[roomNumToAssign]++;
        }

        // Find the room with the most meetings
        int maxMeetings = -1;
        int mostBookedRoom = -1;
        for (int i = 0; i < n; ++i) {
            if (roomUsageCount[i] > maxMeetings) {
                maxMeetings = roomUsageCount[i];
                mostBookedRoom = i;
            }
            // If counts are equal, the problem asks for the lowest room number,
            // which is naturally handled by iterating from i=0 to n-1.
            // The first one encountered with max_meetings will be the lowest room number.
        }

        return mostBookedRoom;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
class MinHeap {
    constructor(comparator = (a, b) => a < b) {
        this.heap = [];
        this.comparator = comparator;
    }

    size() {
        return this.heap.length;
    }

    isEmpty() {
        return this.size() === 0;
    }

    peek() {
        return this.heap[0];
    }

    push(value) {
        this.heap.push(value);
        this._bubbleUp(this.heap.length - 1);
    }

    pop() {
        if (this.isEmpty()) return undefined;
        const root = this.heap[0];
        const last = this.heap.pop();
        if (!this.isEmpty()) {
            this.heap[0] = last;
            this._bubbleDown(0);
        }
        return root;
    }

    _bubbleUp(index) {
        while (index > 0) {
            const parentIndex = Math.floor((index - 1) / 2);
            if (this.comparator(this.heap[index], this.heap[parentIndex])) {
                [this.heap[index], this.heap[parentIndex]] = [this.heap[parentIndex], this.heap[index]];
                index = parentIndex;
            } else {
                break;
            }
        }
    }

    _bubbleDown(index) {
        const lastIndex = this.heap.length - 1;
        while (true) {
            let leftChildIndex = 2 * index + 1;
            let rightChildIndex = 2 * index + 2;
            let smallestIndex = index;

            if (leftChildIndex <= lastIndex && this.comparator(this.heap[leftChildIndex], this.heap[smallestIndex])) {
                smallestIndex = leftChildIndex;
            }

            if (rightChildIndex <= lastIndex && this.comparator(this.heap[rightChildIndex], this.heap[smallestIndex])) {
                smallestIndex = rightChildIndex;
            }

            if (smallestIndex !== index) {
                [this.heap[index], this.heap[smallestIndex]] = [this.heap[smallestIndex], this.heap[index]];
                index = smallestIndex;
            } else {
                break;
            }
        }
    }
}

class Solution {
    mostBooked(n, meetings) {
        // 1. Sort meetings by their original start times
        meetings.sort((a, b) => a[0] - b[0]);

        // Min-heap for available rooms (stores room numbers)
        const availableRooms = new MinHeap((a, b) => a < b); // Default comparator for numbers
        for (let i = 0; i < n; ++i) {
            availableRooms.push(i);
        }

        // Min-heap for occupied rooms (stores [end_time, room_number])
        // Sorted by end_time, then room_number for ties
        const occupiedRooms = new MinHeap((a, b) => {
            if (a[0] !== b[0]) {
                return a[0] < b[0];
            }
            return a[1] < b[1];
        });

        // Array to count meetings for each room
        const roomUsageCount = new Array(n).fill(0);

        for (const meeting of meetings) {
            const start = meeting[0];
            const end = meeting[1];
            const duration = end - start;

            // Free up rooms whose meetings have ended by the current meeting's start time
            while (!occupiedRooms.isEmpty() && occupiedRooms.peek()[0] <= start) {
                const roomInfo = occupiedRooms.pop();
                const roomNum = roomInfo[1];
                availableRooms.push(roomNum);
            }

            let roomNumToAssign;
            let newEndTime;

            if (!availableRooms.isEmpty()) {
                // If there are available rooms, take the one with the lowest number
                roomNumToAssign = availableRooms.pop();
                newEndTime = end; // Meeting starts at its original start time
            } else {
                // No available rooms, delay the current meeting
                // Take the room that will become free earliest
                const earliestFreeRoomInfo = occupiedRooms.pop();

                const earliestFreeTime = earliestFreeRoomInfo[0];
                roomNumToAssign = earliestFreeRoomInfo[1];

                // The delayed meeting starts when this room becomes free
                // Its new end time is earliest_free_time + duration
                newEndTime = earliestFreeTime + duration;
            }

            // Assign the meeting to the chosen room
            occupiedRooms.push([newEndTime, roomNumToAssign]);
            roomUsageCount[roomNumToAssign]++;
        }

        // Find the room with the most meetings
        let maxMeetings = -1;
        let mostBookedRoom = -1;
        for (let i = 0; i < n; ++i) {
            if (roomUsageCount[i] > maxMeetings) {
                maxMeetings = roomUsageCount[i];
                mostBookedRoom = i;
            }
            // If counts are equal, the problem asks for the lowest room number,
            // which is naturally handled by iterating from i=0 to n-1.
            // The first one encountered with max_meetings will be the lowest room number.
        }

        return mostBookedRoom;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
class MinHeap<T> {
    private heap: T[];
    private comparator: (a: T, b: T) => boolean;

    constructor(comparator: (a: T, b: T) => boolean) {
        this.heap = [];
        this.comparator = comparator;
    }

    size(): number {
        return this.heap.length;
    }

    isEmpty(): boolean {
        return this.size() === 0;
    }

    peek(): T | undefined {
        return this.heap[0];
    }

    push(value: T): void {
        this.heap.push(value);
        this._bubbleUp(this.heap.length - 1);
    }

    pop(): T | undefined {
        if (this.isEmpty()) return undefined;
        const root = this.heap[0];
        const last = this.heap.pop();
        if (!this.isEmpty() && last !== undefined) {
            this.heap[0] = last;
            this._bubbleDown(0);
        }
        return root;
    }

    private _bubbleUp(index: number): void {
        while (index > 0) {
            const parentIndex = Math.floor((index - 1) / 2);
            if (this.comparator(this.heap[index], this.heap[parentIndex])) {
                [this.heap[index], this.heap[parentIndex]] = [this.heap[parentIndex], this.heap[index]];
                index = parentIndex;
            } else {
                break;
            }
        }
    }

    private _bubbleDown(index: number): void {
        const lastIndex = this.heap.length - 1;
        while (true) {
            let leftChildIndex = 2 * index + 1;
            let rightChildIndex = 2 * index + 2;
            let smallestIndex = index;

            if (leftChildIndex <= lastIndex && this.comparator(this.heap[leftChildIndex], this.heap[smallestIndex])) {
                smallestIndex = leftChildIndex;
            }

            if (rightChildIndex <= lastIndex && this.comparator(this.heap[rightChildIndex], this.heap[smallestIndex])) {
                smallestIndex = rightChildIndex;
            }

            if (smallestIndex !== index) {
                [this.heap[index], this.heap[smallestIndex]] = [this.heap[smallestIndex], this.heap[index]];
                index = smallestIndex;
            } else {
                break;
            }
        }
    }
}

class Solution {
    mostBooked(n: number, meetings: number[][]): number {
        // 1. Sort meetings by their original start times
        meetings.sort((a, b) => a[0] - b[0]);

        // Min-heap for available rooms (stores room numbers)
        const availableRooms = new MinHeap<number>((a, b) => a < b); // Default comparator for numbers
        for (let i = 0; i < n; ++i) {
            availableRooms.push(i);
        }

        // Min-heap for occupied rooms (stores [end_time, room_number])
        // Sorted by end_time, then room_number for ties
        const occupiedRooms = new MinHeap<[number, number]>((a, b) => {
            if (a[0] !== b[0]) {
                return a[0] < b[0];
            }
            return a[1] < b[1];
        });

        // Array to count meetings for each room
        const roomUsageCount: number[] = new Array(n).fill(0);

        for (const meeting of meetings) {
            const start = meeting[0];
            const end = meeting[1];
            const duration = end - start;

            // Free up rooms whose meetings have ended by the current meeting's start time
            while (!occupiedRooms.isEmpty() && (occupiedRooms.peek() as [number, number])[0] <= start) {
                const roomInfo = occupiedRooms.pop() as [number, number];
                const roomNum = roomInfo[1];
                availableRooms.push(roomNum);
            }

            let roomNumToAssign: number;
            let newEndTime: number;

            if (!availableRooms.isEmpty()) {
                // If there are available rooms, take the one with the lowest number
                roomNumToAssign = availableRooms.pop() as number;
                newEndTime = end; // Meeting starts at its original start time
            } else {
                // No available rooms, delay the current meeting
                // Take the room that will become free earliest
                const earliestFreeRoomInfo = occupiedRooms.pop() as [number, number];

                const earliestFreeTime = earliestFreeRoomInfo[0];
                roomNumToAssign = earliestFreeRoomInfo[1];

                // The delayed meeting starts when this room becomes free
                // Its new end time is earliest_free_time + duration
                newEndTime = earliestFreeTime + duration;
            }

            // Assign the meeting to the chosen room
            occupiedRooms.push([newEndTime, roomNumToAssign]);
            roomUsageCount[roomNumToAssign]++;
        }

        // Find the room with the most meetings
        let maxMeetings = -1;
        let mostBookedRoom = -1;
        for (let i = 0; i < n; ++i) {
            if (roomUsageCount[i] > maxMeetings) {
                maxMeetings = roomUsageCount[i];
                mostBookedRoom = i;
            }
            // If counts are equal, the problem asks for the lowest room number,
            // which is naturally handled by iterating from i=0 to n-1.
            // The first one encountered with max_meetings will be the lowest room number.
        }

        return mostBookedRoom;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
<?php

class MinHeap implements IteratorAggregate, Countable {
    private array $heap = [];
    private Closure $comparator;

    public function __construct(Closure $comparator) {
        $this->comparator = $comparator;
    }

    public function count(): int {
        return count($this->heap);
    }

    public function isEmpty(): bool {
        return $this->count() === 0;
    }

    public function peek(): mixed {
        return $this->heap[0] ?? null;
    }

    public function push(mixed $value): void {
        $this->heap[] = $value;
        $this->bubbleUp($this->count() - 1);
    }

    public function pop(): mixed {
        if ($this->isEmpty()) return null;
        $root = $this->heap[0];
        $last = array_pop($this->heap);
        if (!$this->isEmpty()) {
            $this->heap[0] = $last;
            $this->bubbleDown(0);
        }
        return $root;
    }

    private function bubbleUp(int $index): void {
        while ($index > 0) {
            $parentIndex = floor(($index - 1) / 2);
            if (($this->comparator)($this->heap[$index], $this->heap[$parentIndex])) {
                [$this->heap[$index], $this->heap[$parentIndex]] = [$this->heap[$parentIndex], $this->heap[$index]];
                $index = $parentIndex;
            } else {
                break;
            }
        }
    }

    private function bubbleDown(int $index): void {
        $lastIndex = $this->count() - 1;
        while (true) {
            $leftChildIndex = 2 * $index + 1;
            $rightChildIndex = 2 * $index + 2;
            $smallestIndex = $index;

            if ($leftChildIndex <= $lastIndex && ($this->comparator)($this->heap[$leftChildIndex], $this->heap[$smallestIndex])) {
                $smallestIndex = $leftChildIndex;
            }

            if ($rightChildIndex <= $lastIndex && ($this->comparator)($this->heap[$rightChildIndex], $this->heap[$smallestIndex])) {
                $smallestIndex = $rightChildIndex;
            }

            if ($smallestIndex !== $index) {
                [$this->heap[$index], $this->heap[$smallestIndex]] = [$this->heap[$smallestIndex], $this->heap[$index]];
                $index = $smallestIndex;
            } else {
                break;
            }
        }
    }

    public function getIterator(): Traversable {
        return new ArrayIterator($this->heap);
    }
}

class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $meetings
     * @return Integer
     */
    function mostBooked(int $n, array $meetings): int {
        // 1. Sort meetings by their original start times
        usort($meetings, fn($a, $b) => $a[0] - $b[0]);

        // Min-heap for available rooms (stores room numbers)
        $availableRooms = new MinHeap(fn($a, $b) => $a < $b);
        for ($i = 0; $i < $n; ++$i) {
            $availableRooms->push($i);
        }

        // Min-heap for occupied rooms (stores [end_time, room_number])
        // Sorted by end_time, then room_number for ties
        $occupiedRooms = new MinHeap(fn($a, $b) => {
            if ($a[0] !== $b[0]) {
                return $a[0] < $b[0];
            }
            return $a[1] < $b[1];
        });

        // Array to count meetings for each room
        $roomUsageCount = array_fill(0, $n, 0);

        foreach ($meetings as $meeting) {
            $start = $meeting[0];
            $end = $meeting[1];
            $duration = $end - $start;

            // Free up rooms whose meetings have ended by the current meeting's start time
            while (!$occupiedRooms->isEmpty() && $occupiedRooms->peek()[0] <= $start) {
                $roomInfo = $occupiedRooms->pop();
                $roomNum = $roomInfo[1];
                $availableRooms->push($roomNum);
            }

            $roomNumToAssign;
            $newEndTime;

            if (!$availableRooms->isEmpty()) {
                // If there are available rooms, take the one with the lowest number
                $roomNumToAssign = $availableRooms->pop();
                $newEndTime = $end; // Meeting starts at its original start time
            } else {
                // No available rooms, delay the current meeting
                // Take the room that will become free earliest
                $earliestFreeRoomInfo = $occupiedRooms->pop();

                $earliestFreeTime = $earliestFreeRoomInfo[0];
                $roomNumToAssign = $earliestFreeRoomInfo[1];

                // The delayed meeting starts when this room becomes free
                // Its new end time is earliest_free_time + duration
                $newEndTime = $earliestFreeTime + $duration;
            }

            // Assign the meeting to the chosen room
            $occupiedRooms->push([$newEndTime, $roomNumToAssign]);
            $roomUsageCount[$roomNumToAssign]++;
        }

        // Find the room with the most meetings
        $maxMeetings = -1;
        $mostBookedRoom = -1;
        for ($i = 0; $i < $n; ++$i) {
            if ($roomUsageCount[$i] > $maxMeetings) {
                $maxMeetings = $roomUsageCount[$i];
                $mostBookedRoom = $i;
            }
            // If counts are equal, the problem asks for the lowest room number,
            // which is naturally handled by iterating from i=0 to n-1.
            // The first one encountered with max_meetings will be the lowest room number.
        }

        return $mostBookedRoom;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
import Foundation

// MinHeap implementation for Swift
struct MinHeap<T> {
    private var nodes: [T] = []
    private let areInIncreasingOrder: (T, T) -> Bool

    var isEmpty: Bool { return nodes.isEmpty }
    var count: Int { return nodes.count }

    init(sort: @escaping (T, T) -> Bool) {
        self.areInIncreasingOrder = sort
    }

    func peek() -> T? {
        return nodes.first
    }

    mutating func push(_ element: T) {
        nodes.append(element)
        bubbleUp(nodes.count - 1)
    }

    mutating func pop() -> T? {
        guard !isEmpty else { return nil }
        if nodes.count == 1 {
            return nodes.removeLast()
        }
        let root = nodes[0]
        nodes[0] = nodes.removeLast()
        bubbleDown(0)
        return root
    }

    private mutating func bubbleUp(_ index: Int) {
        var childIndex = index
        var parentIndex = self.parentIndex(of: childIndex)
        while childIndex > 0 && areInIncreasingOrder(nodes[childIndex], nodes[parentIndex]) {
            nodes.swapAt(childIndex, parentIndex)
            childIndex = parentIndex
            parentIndex = self.parentIndex(of: childIndex)
        }
    }

    private mutating func bubbleDown(_ index: Int) {
        var parentIndex = index
        while true {
            let leftChildIndex = self.leftChildIndex(of: parentIndex)
            let rightChildIndex = self.rightChildIndex(of: parentIndex)
            var candidateIndex = parentIndex

            if leftChildIndex < nodes.count && areInIncreasingOrder(nodes[leftChildIndex], nodes[candidateIndex]) {
                candidateIndex = leftChildIndex
            }
            if rightChildIndex < nodes.count && areInIncreasingOrder(nodes[rightChildIndex], nodes[candidateIndex]) {
                candidateIndex = rightChildIndex
            }

            if candidateIndex == parentIndex {
                return
            }
            nodes.swapAt(parentIndex, candidateIndex)
            parentIndex = candidateIndex
        }
    }

    private func parentIndex(of i: Int) -> Int { (i - 1) / 2 }
    private func leftChildIndex(of i: Int) -> Int { 2 * i + 1 }
    private func rightChildIndex(of i: Int) -> Int { 2 * i + 2 }
}

class Solution {
    func mostBooked(_ n: Int, _ meetings: [[Int]]) -> Int {
        // 1. Sort meetings by their original start times
        var sortedMeetings = meetings.sorted { $0[0] < $1[0] }

        // Min-heap for available rooms (stores room numbers)
        var availableRooms = MinHeap<Int> { $0 < $1 }
        for i in 0..<n {
            availableRooms.push(i)
        }

        // Min-heap for occupied rooms (stores (end_time, room_number))
        // Sorted by end_time, then room_number for ties
        var occupiedRooms = MinHeap<(endTime: Int, roomNum: Int)> { a, b in
            if a.endTime != b.endTime {
                return a.endTime < b.endTime
            }
            return a.roomNum < b.roomNum
        }

        // Array to count meetings for each room
        var roomUsageCount = Array(repeating: 0, count: n)

        for meeting in sortedMeetings {
            let start = meeting[0]
            let end = meeting[1]
            let duration = end - start

            // Free up rooms whose meetings have ended by the current meeting's start time
            while let peeked = occupiedRooms.peek(), peeked.endTime <= start {
                let roomInfo = occupiedRooms.pop()!
                let roomNum = roomInfo.roomNum
                availableRooms.push(roomNum)
            }

            var roomNumToAssign: Int
            var newEndTime: Int

            if !availableRooms.isEmpty {
                // If there are available rooms, take the one with the lowest number
                roomNumToAssign = availableRooms.pop()!
                newEndTime = end // Meeting starts at its original start time
            } else {
                // No available rooms, delay the current meeting
                // Take the room that will become free earliest
                let earliestFreeRoomInfo = occupiedRooms.pop()!

                let earliestFreeTime = earliestFreeRoomInfo.endTime
                roomNumToAssign = earliestFreeRoomInfo.roomNum

                // The delayed meeting starts when this room becomes free
                // Its new end time is earliest_free_time + duration
                newEndTime = earliestFreeTime + duration
            }

            // Assign the meeting to the chosen room
            occupiedRooms.push((newEndTime, roomNumToAssign))
            roomUsageCount[roomNumToAssign] += 1
        }

        // Find the room with the most meetings
        var maxMeetings = -1
        var mostBookedRoom = -1
        for i in 0..<n {
            if roomUsageCount[i] > maxMeetings {
                maxMeetings = roomUsageCount[i]
                mostBookedRoom = i
            }
            // If counts are equal, the problem asks for the lowest room number,
            // which is naturally handled by iterating from i=0 to n-1.
            // The first one encountered with max_meetings will be the lowest room number.
        }

        return mostBookedRoom
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
import java.util.Arrays
import java.util.PriorityQueue

class Solution {
    fun mostBooked(n: Int, meetings: Array<IntArray>): Int {
        // 1. Sort meetings by their original start times
        meetings.sortBy { it[0] }

        // Min-heap for available rooms (stores room numbers)
        val availableRooms = PriorityQueue<Int>()
        for (i in 0 until n) {
            availableRooms.offer(i)
        }

        // Min-heap for occupied rooms (stores (end_time, room_number))
        // Sorted by end_time, then room_number for ties
        // Each element is an array: [end_time, room_number]
        val occupiedRooms = PriorityQueue<LongArray> { a, b ->
            val cmp = a[0].compareTo(b[0])
            if (cmp != 0) cmp else a[1].compareTo(b[1])
        }

        // Array to count meetings for each room
        val roomUsageCount = IntArray(n)

        for (meeting in meetings) {
            val start = meeting[0].toLong()
            val end = meeting[1].toLong()
            val duration = end - start

            // Free up rooms whose meetings have ended by the current meeting's start time
            while (occupiedRooms.isNotEmpty() && occupiedRooms.peek()[0] <= start) {
                val roomInfo = occupiedRooms.poll()
                val roomNum = roomInfo[1].toInt()
                availableRooms.offer(roomNum)
            }

            val roomNumToAssign: Int
            val newEndTime: Long

            if (availableRooms.isNotEmpty()) {
                // If there are available rooms, take the one with the lowest number
                roomNumToAssign = availableRooms.poll()!!
                newEndTime = end // Meeting starts at its original start time
            } else {
                // No available rooms, delay the current meeting
                // Take the room that will become free earliest
                val earliestFreeRoomInfo = occupiedRooms.poll()!!

                val earliestFreeTime = earliestFreeRoomInfo[0]
                roomNumToAssign = earliestFreeRoomInfo[1].toInt()

                // The delayed meeting starts when this room becomes free
                // Its new end time is earliest_free_time + duration
                newEndTime = earliestFreeTime + duration
            }

            // Assign the meeting to the chosen room
            occupiedRooms.offer(longArrayOf(newEndTime, roomNumToAssign.toLong()))
            roomUsageCount[roomNumToAssign]++
        }

        // Find the room with the most meetings
        var maxMeetings = -1
        var mostBookedRoom = -1
        for (i in 0 until n) {
            if (roomUsageCount[i] > maxMeetings) {
                maxMeetings = roomUsageCount[i]
                mostBookedRoom = i
            }
            // If counts are equal, the problem asks for the lowest room number,
            // which is naturally handled by iterating from i=0 to n-1.
            // The first one encountered with max_meetings will be the lowest room number.
        }

        return mostBookedRoom
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
import 'dart:collection';

class Solution {
  int mostBooked(int n, List<List<int>> meetings) {
    // 1. Sort meetings by their original start times
    meetings.sort((a, b) => a[0].compareTo(b[0]));

    // Min-heap for available rooms (stores room numbers)
    final availableRooms = PriorityQueue<int>();
    for (int i = 0; i < n; ++i) {
      availableRooms.add(i);
    }

    // Min-heap for occupied rooms (stores [end_time, room_number])
    // Sorted by end_time, then room_number for ties
    final occupiedRooms = PriorityQueue<List<int>>((a, b) {
      if (a[0] != b[0]) {
        return a[0].compareTo(b[0]);
      }
      return a[1].compareTo(b[1]);
    });

    // Array to count meetings for each room
    final roomUsageCount = List<int>.filled(n, 0);

    for (final meeting in meetings) {
      final int start = meeting[0];
      final int end = meeting[1];
      final int duration = end - start;

      // Free up rooms whose meetings have ended by the current meeting's start time
      while (occupiedRooms.isNotEmpty && occupiedRooms.first[0] <= start) {
        final roomInfo = occupiedRooms.removeFirst();
        final roomNum = roomInfo[1];
        availableRooms.add(roomNum);
      }

      int roomNumToAssign;
      int newEndTime;

      if (availableRooms.isNotEmpty) {
        // If there are available rooms, take the one with the lowest number
        roomNumToAssign = availableRooms.removeFirst();
        newEndTime = end; // Meeting starts at its original start time
      } else {
        // No available rooms, delay the current meeting
        // Take the room that will become free earliest
        final earliestFreeRoomInfo = occupiedRooms.removeFirst();

        final int earliestFreeTime = earliestFreeRoomInfo[0];
        roomNumToAssign = earliestFreeRoomInfo[1];

        // The delayed meeting starts when this room becomes free
        // Its new end time is earliest_free_time + duration
        newEndTime = earliestFreeTime + duration;
      }

      // Assign the meeting to the chosen room
      occupiedRooms.add([newEndTime, roomNumToAssign]);
      roomUsageCount[roomNumToAssign]++;
    }

    // Find the room with the most meetings
    int maxMeetings = -1;
    int mostBookedRoom = -1;
    for (int i = 0; i < n; ++i) {
      if (roomUsageCount[i] > maxMeetings) {
        maxMeetings = roomUsageCount[i];
        mostBookedRoom = i;
      }
      // If counts are equal, the problem asks for the lowest room number,
      // which is naturally handled by iterating from i=0 to n-1.
      // The first one encountered with max_meetings will be the lowest room number.
    }

    return mostBookedRoom;
  }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
import (
	"container/heap"
	"sort"
)

// An IntMinHeap is a min-heap of ints.
type IntMinHeap []int

func (h IntMinHeap) Len() int           { return len(h) }
func (h IntMinHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntMinHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntMinHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *IntMinHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

// RoomEvent represents an occupied room with its end time and room number.
type RoomEvent struct {
	EndTime int64
	RoomNum int
}

// A RoomEventMinHeap is a min-heap of RoomEvents.
type RoomEventMinHeap []RoomEvent

func (h RoomEventMinHeap) Len() int {
	return len(h)
}

func (h RoomEventMinHeap) Less(i, j int) bool {
	if h[i].EndTime != h[j].EndTime {
		return h[i].EndTime < h[j].EndTime
	}
	return h[i].RoomNum < h[j].RoomNum
}

func (h RoomEventMinHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

func (h *RoomEventMinHeap) Push(x interface{}) {
	*h = append(*h, x.(RoomEvent))
}

func (h *RoomEventMinHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func mostBooked(n int, meetings [][]int) int {
	// 1. Sort meetings by their original start times
	sort.Slice(meetings, func(i, j int) bool {
		return meetings[i][0] < meetings[j][0]
	})

	// Min-heap for available rooms (stores room numbers)
	availableRooms := &IntMinHeap{}
	heap.Init(availableRooms)
	for i := 0; i < n; i++ {
		heap.Push(availableRooms, i)
	}

	// Min-heap for occupied rooms (stores (end_time, room_number))
	occupiedRooms := &RoomEventMinHeap{}
	heap.Init(occupiedRooms)

	// Array to count meetings for each room
	roomUsageCount := make([]int, n)

	for _, meeting := range meetings {
		start := int64(meeting[0])
		end := int64(meeting[1])
		duration := end - start

		// Free up rooms whose meetings have ended by the current meeting's start time
		for occupiedRooms.Len() > 0 && occupiedRooms.Peek().(RoomEvent).EndTime <= start {
			roomEvent := heap.Pop(occupiedRooms).(RoomEvent)
			heap.Push(availableRooms, roomEvent.RoomNum)
		}

		var roomNumToAssign int
		var newEndTime int64

		if availableRooms.Len() > 0 {
			// If there are available rooms, take the one with the lowest number
			roomNumToAssign = heap.Pop(availableRooms).(int)
			newEndTime = end // Meeting starts at its original start time
		} else {
			// No available rooms, delay the current meeting
			// Take the room that will become free earliest
			earliestFreeRoomEvent := heap.Pop(occupiedRooms).(RoomEvent)

			// The delayed meeting starts when this room becomes free
			// Its new end time is earliest_free_time + duration
			newEndTime = earliestFreeRoomEvent.EndTime + duration
			roomNumToAssign = earliestFreeRoomEvent.RoomNum
		}

		// Assign the meeting to the chosen room
	heap.Push(occupiedRooms, RoomEvent{EndTime: newEndTime, RoomNum: roomNumToAssign})
		roomUsageCount[roomNumToAssign]++
	}

	// Find the room with the most meetings
	maxMeetings := -1
	mostBookedRoom := -1
	for i := 0; i < n; i++ {
		if roomUsageCount[i] > maxMeetings {
			maxMeetings = roomUsageCount[i]
			mostBookedRoom = i
		}
		// If counts are equal, the problem asks for the lowest room number,
		// which is naturally handled by iterating from i=0 to n-1.
		// The first one encountered with max_meetings will be the lowest room number.
	}

	return mostBookedRoom
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
require 'set'

class MinHeap
  def initialize(&comparator)
    @heap = []
    @comparator = comparator || Proc.new { |a, b| a <=> b }
  end

  def size
    @heap.size
  end

  def empty?
    @heap.empty?
  end

  def peek
    @heap.first
  end

  def push(value)
    @heap << value
    bubble_up(@heap.size - 1)
  end

  def pop
    return nil if empty?
    root = @heap.first
    last = @heap.pop
    unless empty?
      @heap[0] = last
      bubble_down(0)
    end
    root
  end

  private

  def bubble_up(index)
    while index > 0
      parent_index = (index - 1) / 2
      if @comparator.call(@heap[index], @heap[parent_index]) < 0
        @heap[index], @heap[parent_index] = @heap[parent_index], @heap[index]
        index = parent_index
      else
        break
      end
    end
  end

  def bubble_down(index)
    last_index = @heap.size - 1
    loop do
      left_child_index = 2 * index + 1
      right_child_index = 2 * index + 2
      smallest_index = index

      if left_child_index <= last_index && @comparator.call(@heap[left_child_index], @heap[smallest_index]) < 0
        smallest_index = left_child_index
      end

      if right_child_index <= last_index && @comparator.call(@heap[right_child_index], @heap[smallest_index]) < 0
        smallest_index = right_child_index
      end

      if smallest_index != index
        @heap[index], @heap[smallest_index] = @heap[smallest_index], @heap[index]
        index = smallest_index
      else
        break
      end
    end
  end
end

class Solution
  def most_booked(n, meetings)
    # 1. Sort meetings by their original start times
    meetings.sort_by! { |m| m[0] }

    # Min-heap for available rooms (stores room numbers)
    available_rooms = MinHeap.new { |a, b| a <=> b }
    n.times { |i| available_rooms.push(i) }

    # Min-heap for occupied rooms (stores [end_time, room_number])
    # Sorted by end_time, then room_number for ties
    occupied_rooms = MinHeap.new do |a, b|
      if a[0] != b[0]
        a[0] <=> b[0]
      else
        a[1] <=> b[1]
      end
    end

    # Array to count meetings for each room
    room_usage_count = Array.new(n, 0)

    meetings.each do |start, ending|
      duration = ending - start

      # Free up rooms whose meetings have ended by the current meeting's start time
      while !occupied_rooms.empty? && occupied_rooms.peek[0] <= start
        room_info = occupied_rooms.pop
        room_num = room_info[1]
        available_rooms.push(room_num)
      end

      room_num_to_assign = nil
      new_end_time = nil

      if !available_rooms.empty?
        # If there are available rooms, take the one with the lowest number
        room_num_to_assign = available_rooms.pop
        new_end_time = ending # Meeting starts at its original start time
      else
        # No available rooms, delay the current meeting
        # Take the room that will become free earliest
        earliest_free_room_info = occupied_rooms.pop

        earliest_free_time = earliest_free_room_info[0]
        room_num_to_assign = earliest_free_room_info[1]

        # The delayed meeting starts when this room becomes free
        # Its new end time is earliest_free_time + duration
        new_end_time = earliest_free_time + duration
      end

      # Assign the meeting to the chosen room
      occupied_rooms.push([new_end_time, room_num_to_assign])
      room_usage_count[room_num_to_assign] += 1
    end

    # Find the room with the most meetings
    max_meetings = -1
    most_booked_room = -1
    n.times do |i|
      if room_usage_count[i] > max_meetings
        max_meetings = room_usage_count[i]
        most_booked_room = i
      end
      # If counts are equal, the problem asks for the lowest room number,
      # which is naturally handled by iterating from i=0 to n-1.
      # The first one encountered with max_meetings will be the lowest room number.
    end

    most_booked_room
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
    def mostBooked(n: Int, meetings: Array[Array[Int]]): Int = {
        // 1. Sort meetings by their original start times
        val sortedMeetings = meetings.sortBy(_(0))

        // Min-heap for available rooms (stores room numbers)
        val availableRooms = new mutable.PriorityQueue[Int]()(Ordering.Int.reverse)
        for (i <- 0 until n) {
            availableRooms.enqueue(i)
        }

        // Min-heap for occupied rooms (stores (end_time, room_number))
        // Sorted by end_time, then room_number for ties
        // Custom ordering for tuples: first by end_time (Long), then by room_number (Int)
        implicit val occupiedRoomOrdering: Ordering[(Long, Int)] = Ordering.by(t => (t._1, t._2))
        val occupiedRooms = new mutable.PriorityQueue[(Long, Int)]()

        // Array to count meetings for each room
        val roomUsageCount = Array.fill(n)(0)

        for (meeting <- sortedMeetings) {
            val start = meeting(0).toLong
            val end = meeting(1).toLong
            val duration = end - start

            // Free up rooms whose meetings have ended by the current meeting's start time
            while (occupiedRooms.nonEmpty && occupiedRooms.head._1 <= start) {
                val (_, roomNum) = occupiedRooms.dequeue()
                availableRooms.enqueue(roomNum)
            }

            var roomNumToAssign: Int = -1
            var newEndTime: Long = -1L

            if (availableRooms.nonEmpty) {
                // If there are available rooms, take the one with the lowest number
                roomNumToAssign = availableRooms.dequeue()
                newEndTime = end // Meeting starts at its original start time
            } else {
                // No available rooms, delay the current meeting
                // Take the room that will become free earliest
                val (earliestFreeTime, roomNum) = occupiedRooms.dequeue()

                roomNumToAssign = roomNum

                // The delayed meeting starts when this room becomes free
                // Its new end time is earliest_free_time + duration
                newEndTime = earliestFreeTime + duration
            }

            // Assign the meeting to the chosen room
            occupiedRooms.enqueue((newEndTime, roomNumToAssign))
            roomUsageCount(roomNumToAssign) += 1
        }

        // Find the room with the most meetings
        var maxMeetings = -1
        var mostBookedRoom = -1
        for (i <- 0 until n) {
            if (roomUsageCount(i) > maxMeetings) {
                maxMeetings = roomUsageCount(i)
                mostBookedRoom = i
            }
            // If counts are equal, the problem asks for the lowest room number,
            // which is naturally handled by iterating from i=0 to n-1.
            // The first one encountered with max_meetings will be the lowest room number.
        }

        mostBookedRoom
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
use std::collections::BinaryHeap;
use std::cmp::Reverse;

struct Meeting { 
    start: i32, 
    end: i32, 
}

impl PartialEq for Meeting {
    fn eq(&self, other: &Self) -> bool {
        self.start == other.start
    }
}

impl Eq for Meeting {}

impl PartialOrd for Meeting {
    fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
        self.start.partial_cmp(&other.start)
    }
}

impl Ord for Meeting {
    fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        self.start.cmp(&other.start)
    }
}

#[derive(PartialEq, Eq, PartialOrd, Ord)]
struct RoomEvent {
    end_time: i64,
    room_num: i32,
}

impl RoomEvent {
    fn new(end_time: i64, room_num: i32) -> Self {
        RoomEvent { end_time, room_num }
    }
}

impl Solution {
    pub fn most_booked(n: i32, meetings: Vec<Vec<i32>>) -> i32 {
        // 1. Sort meetings by their original start times
        let mut meetings_structs: Vec<Meeting> = meetings.into_iter().map(|m| Meeting { start: m[0], end: m[1] }).collect();
        meetings_structs.sort_unstable();

        // Min-heap for available rooms (stores room numbers)
        let mut available_rooms: BinaryHeap<Reverse<i32>> = BinaryHeap::new();
        for i in 0..n {
            available_rooms.push(Reverse(i));
        }

        // Min-heap for occupied rooms (stores (end_time, room_number))
        // Sorted by end_time, then room_number for ties
        let mut occupied_rooms: BinaryHeap<Reverse<RoomEvent>> = BinaryHeap::new();

        // Array to count meetings for each room
        let mut room_usage_count: Vec<i32> = vec![0; n as usize];

        for meeting in meetings_structs {
            let start = meeting.start as i64;
            let end = meeting.end as i64;
            let duration = end - start;

            // Free up rooms whose meetings have ended by the current meeting's start time
            while let Some(Reverse(event)) = occupied_rooms.peek() {
                if event.end_time <= start {
                    let Reverse(room_event) = occupied_rooms.pop().unwrap();
                    available_rooms.push(Reverse(room_event.room_num));
                } else {
                    break;
                }
            }

            let room_num_to_assign: i32;
            let new_end_time: i64;

            if let Some(Reverse(room_num)) = available_rooms.pop() {
                // If there are available rooms, take the one with the lowest number
                room_num_to_assign = room_num;
                new_end_time = end; // Meeting starts at its original start time
            } else {
                // No available rooms, delay the current meeting
                // Take the room that will become free earliest
                let Reverse(earliest_free_room_event) = occupied_rooms.pop().unwrap();

                let earliest_free_time = earliest_free_room_event.end_time;
                room_num_to_assign = earliest_free_room_event.room_num;

                // The delayed meeting starts when this room becomes free
                // Its new end time is earliest_free_time + duration
                new_end_time = earliest_free_time + duration;
            }

            // Assign the meeting to the chosen room
            occupied_rooms.push(Reverse(RoomEvent::new(new_end_time, room_num_to_assign)));
            room_usage_count[room_num_to_assign as usize] += 1;
        }

        // Find the room with the most meetings
        let mut max_meetings = -1;
        let mut most_booked_room = -1;
        for i in 0..n {
            if room_usage_count[i as usize] > max_meetings {
                max_meetings = room_usage_count[i as usize];
                most_booked_room = i;
            }
            // If counts are equal, the problem asks for the lowest room number,
            // which is naturally handled by iterating from i=0 to n-1.
            // The first one encountered with max_meetings will be the lowest room number.
        }

        most_booked_room
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
#lang racket

(require data/heap)

(define (most-booked n meetings)
  ;; 1. Sort meetings by their original start times
  (define sorted-meetings (sort meetings (lambda (a b) (< (car a) (car b)))))

  ;; Min-heap for available rooms (stores room numbers)
  (define available-rooms (make-heap (lambda (a b) (< a b))))
  (for ([i (in-range n)])
    (heap-add! available-rooms i))

  ;; Min-heap for occupied rooms (stores (end_time, room_number))
  ;; Sorted by end_time, then room_number for ties
  (define occupied-rooms
    (make-heap (lambda (a b)
                 (let ([end-time-a (car a)]
                       [end-time-b (car b)])
                   (if (not (= end-time-a end-time-b))
                       (< end-time-a end-time-b)
                       (< (cadr a) (cadr b)))))))

  ;; Array to count meetings for each room
  (define room-usage-count (make-vector n 0))

  (for ([meeting sorted-meetings])
    (define start (car meeting))
    (define end (cadr meeting))
    (define duration (- end start))

    ;; Free up rooms whose meetings have ended by the current meeting's start time
    (while (and (not (heap-empty? occupied-rooms))
                (<= (car (heap-min occupied-rooms)) start))
      (define room-info (heap-extract-min! occupied-rooms))
      (define room-num (cadr room-info))
      (heap-add! available-rooms room-num))

    (define room-num-to-assign #f)
    (define new-end-time #f)

    (if (not (heap-empty? available-rooms))
        (begin
          ;; If there are available rooms, take the one with the lowest number
          (set! room-num-to-assign (heap-extract-min! available-rooms))
          (set! new-end-time end)) ;; Meeting starts at its original start time
        (begin
          ;; No available rooms, delay the current meeting
          ;; Take the room that will become free earliest
          (define earliest-free-room-info (heap-extract-min! occupied-rooms))

          (define earliest-free-time (car earliest-free-room-info))
          (set! room-num-to-assign (cadr earliest-free-room-info))

          ;; The delayed meeting starts when this room becomes free
          ;; Its new end time is earliest-free-time + duration
          (set! new-end-time (+ earliest-free-time duration))))

    ;; Assign the meeting to the chosen room
    (heap-add! occupied-rooms (list new-end-time room-num-to-assign))
    (vector-set! room-usage-count room-num-to-assign (+ (vector-ref room-usage-count room-num-to-assign) 1)))

  ;; Find the room with the most meetings
  (define max-meetings -1)
  (define most-booked-room -1)
  (for ([i (in-range n)])
    (when (> (vector-ref room-usage-count i) max-meetings)
      (set! max-meetings (vector-ref room-usage-count i))
      (set! most-booked-room i)))

  most-booked-room)
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
-module(solution).
-export([most_booked/2]).

%% Helper for min-heap (priority queue) functionality
%% Using gb_trees as a balanced binary tree, which can simulate a min-heap
%% Keys are {priority, value} tuples for ordering.

%% Comparator for available rooms (room numbers)
-spec available_room_comparator(integer(), integer()) -> boolean().
available_room_comparator(RoomA, RoomB) ->
    RoomA < RoomB.

%% Comparator for occupied rooms ({end_time, room_number})
-spec occupied_room_comparator({integer(), integer()}, {integer(), integer()}) -> boolean().
occupied_room_comparator({EndTimeA, RoomNumA}, {EndTimeB, RoomNumB}) ->
    if
        EndTimeA =/= EndTimeB -> EndTimeA < EndTimeB;
        true -> RoomNumA < RoomNumB
    end.

-spec most_booked(integer(), list(list(integer()))) -> integer().
most_booked(N, Meetings) ->
    %% 1. Sort meetings by their original start times
    SortedMeetings = lists:sort(fun(A, B) -> hd(A) < hd(B) end, Meetings),

    %% Min-heap for available rooms (stores room numbers)
    AvailableRooms = lists:foldl(fun(I, Acc) -> gb_trees:insert({I, I}, Acc) end, gb_trees:empty(), lists:seq(0, N - 1)),

    %% Min-heap for occupied rooms (stores {end_time, room_number})
    OccupiedRooms = gb_trees:empty(),

    %% Array to count meetings for each room
    RoomUsageCount = array:new([{size, N}, {fixed, true}, {default, 0}]),

    {_FinalAvailableRooms, _FinalOccupiedRooms, FinalRoomUsageCount} = lists:foldl(
        fun(Meeting, {CurrentAvailableRooms, CurrentOccupiedRooms, CurrentRoomUsageCount}) ->
            [Start, End] = Meeting,
            Duration = End - Start,

            %% Free up rooms whose meetings have ended by the current meeting's start time
            {UpdatedAvailableRooms, UpdatedOccupiedRooms} = free_up_rooms(Start, CurrentAvailableRooms, CurrentOccupiedRooms),

            RoomNumToAssign = -1,
            NewEndTime = -1,

            if
                gb_trees:is_empty(UpdatedAvailableRooms) == false ->
                    %% If there are available rooms, take the one with the lowest number
                    {{_Priority, RoomNum}, TempAvailableRooms} = gb_trees:take_smallest(UpdatedAvailableRooms),
                    RoomNumToAssign = RoomNum,
                    NewEndTime = End,
                    {TempAvailableRooms, UpdatedOccupiedRooms};
                true ->
                    %% No available rooms, delay the current meeting
                    %% Take the room that will become free earliest
                    {{EarliestFreeTime, RoomNum}, TempOccupiedRooms} = gb_trees:take_smallest(UpdatedOccupiedRooms),
                    RoomNumToAssign = RoomNum,
                    NewEndTime = EarliestFreeTime + Duration,
                    {UpdatedAvailableRooms, TempOccupiedRooms}
            end,

            %% Assign the meeting to the chosen room
            NewOccupiedRooms = gb_trees:insert({NewEndTime, RoomNumToAssign}, {NewEndTime, RoomNumToAssign}, UpdatedOccupiedRooms),
            UpdatedRoomUsageCount = array:set(RoomNumToAssign, array:get(RoomNumToAssign, CurrentRoomUsageCount) + 1, CurrentRoomUsageCount),

            {UpdatedAvailableRooms, NewOccupiedRooms, UpdatedRoomUsageCount}
        end,
        {AvailableRooms, OccupiedRooms, RoomUsageCount},
        SortedMeetings
    ),

    %% Find the room with the most meetings
    MaxMeetings = -1,
    MostBookedRoom = -1,
    {_MaxMeetings, _MostBookedRoom} = lists:foldl(
        fun(I, {CurrentMaxMeetings, CurrentMostBookedRoom}) ->
            Count = array:get(I, FinalRoomUsageCount),
            if
                Count > CurrentMaxMeetings -> {Count, I};
                true -> {CurrentMaxMeetings, CurrentMostBookedRoom}
            end
        end,
        {MaxMeetings, MostBookedRoom},
        lists:seq(0, N - 1)
    ),
    _MostBookedRoom.


free_up_rooms(CurrentStartTime, AvailableRooms, OccupiedRooms) ->
    if
        gb_trees:is_empty(OccupiedRooms) == false andalso element(1, gb_trees:smallest(OccupiedRooms)) =< CurrentStartTime ->
            {{_EndTime, RoomNum}, TempOccupiedRooms} = gb_trees:take_smallest(OccupiedRooms),
            NewAvailableRooms = gb_trees:insert({RoomNum, RoomNum}, AvailableRooms),
            free_up_rooms(CurrentStartTime, NewAvailableRooms, TempOccupiedRooms);
        true ->
            {AvailableRooms, OccupiedRooms}
    end.
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
defmodule Solution do
  @spec most_booked(n :: integer, meetings :: [[integer]]) :: integer
  def most_booked(n, meetings) do
    # 1. Sort meetings by their original start times
    sorted_meetings = Enum.sort(meetings, fn [s1, _], [s2, _] -> s1 < s2 end)

    # Min-heap for available rooms (stores room numbers)
    # Using :gb_trees as a balanced binary tree, which can simulate a min-heap
    # Keys are {priority, value} tuples for ordering.
    available_rooms = Enum.reduce(0..(n - 1), :gb_trees.empty(), fn i, acc ->
      :gb_trees.insert({i, i}, acc)
    end)

    # Min-heap for occupied rooms (stores {end_time, room_number})
    occupied_rooms = :gb_trees.empty()

    # Array to count meetings for each room
    room_usage_count = :array.new([{size: n, fixed: true, default: 0}])

    {_final_available_rooms, _final_occupied_rooms, final_room_usage_count} = Enum.reduce(
      sorted_meetings,
      {available_rooms, occupied_rooms, room_usage_count},
      fn [start, ending], {current_available_rooms, current_occupied_rooms, current_room_usage_count} ->
        duration = ending - start

        # Free up rooms whose meetings have ended by the current meeting's start time
        {updated_available_rooms, updated_occupied_rooms} = free_up_rooms(start, current_available_rooms, current_occupied_rooms)

        {room_num_to_assign, new_end_time, temp_available_rooms, temp_occupied_rooms} = 
          if :gb_trees.is_empty(updated_available_rooms) == false do
            # If there are available rooms, take the one with the lowest number
            {{_priority, room_num}, temp_available_rooms} = :gb_trees.take_smallest(updated_available_rooms)
            {room_num, ending, temp_available_rooms, updated_occupied_rooms}
          else
            # No available rooms, delay the current meeting
            # Take the room that will become free earliest
            {{earliest_free_time, room_num}, temp_occupied_rooms} = :gb_trees.take_smallest(updated_occupied_rooms)
            new_end_time = earliest_free_time + duration
            {room_num, new_end_time, updated_available_rooms, temp_occupied_rooms}
          end

        # Assign the meeting to the chosen room
        new_occupied_rooms = :gb_trees.insert({new_end_time, room_num_to_assign}, {new_end_time, room_num_to_assign}, temp_occupied_rooms)
        updated_room_usage_count = :array.set(room_num_to_assign, :array.get(room_num_to_assign, current_room_usage_count) + 1, current_room_usage_count)

        {temp_available_rooms, new_occupied_rooms, updated_room_usage_count}
      end
    )

    # Find the room with the most meetings
    max_meetings = -1
    most_booked_room = -1
    {_max_meetings, final_most_booked_room} = Enum.reduce(
      0..(n - 1),
      {max_meetings, most_booked_room},
      fn i, {current_max_meetings, current_most_booked_room} ->
        count = :array.get(i, final_room_usage_count)
        if count > current_max_meetings do
          {count, i}
        else
          {current_max_meetings, current_most_booked_room}
        end
      end
    )
    final_most_booked_room
  end

  defp free_up_rooms(current_start_time, available_rooms, occupied_rooms) do
    if :gb_trees.is_empty(occupied_rooms) == false and :gb_trees.smallest(occupied_rooms) |> elem(0) <= current_start_time do
      {{_end_time, room_num}, temp_occupied_rooms} = :gb_trees.take_smallest(occupied_rooms)
      new_available_rooms = :gb_trees.insert({room_num, room_num}, available_rooms)
      free_up_rooms(current_start_time, new_available_rooms, temp_occupied_rooms)
    else
      {available_rooms, occupied_rooms}
    end
  end
end
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity is dominated by sorting the meetings, which takes O(M log M) time, where M is the number of meetings. The subsequent iteration through M meetings involves heap operations. Each meeting triggers at most one push and one pop operation on either the `available_rooms` or `occupied_rooms` heap. Additionally, the `while` loop to free up rooms processes each `(end_time, room_number)` pair at most once across all meetings. Since each heap operation takes O(log N) time (where N is the number of rooms), the total time for heap operations is O((M + N) log N). Finally, finding the most booked room takes O(N) time. Combining these, the overall time complexity is O(M log M + (M + N) log N).

- **Space Complexity:** The space complexity is determined by the data structures used. Storing the sorted meetings (if a copy is made) takes O(M) space. The `available_rooms` and `occupied_rooms` heaps can each hold up to N elements, contributing O(N) space. The `room_usage_count` array also takes O(N) space. Therefore, the total space complexity is O(M + N).

</div>
</details>


<details class="ai-solution-card" markdown="1">
<summary class="ai-solution-header">
  <span class="ai-model-badge">⚡ Solution from <strong>llama-3.3-70b-versatile</strong></span>
  <small class="solution-timestamp">(2025-12-27 01:07:49 )</small>
</summary>

<div class="ai-solution-content">

### Approach

The problem can be solved by using two min heaps, one to keep track of the free rooms and the other to keep track of the end times of the meetings. The meetings are first sorted based on their start times. Then, for each meeting, we check if there are any free rooms. If there are, we use the room with the smallest number. Otherwise, we assign the meeting to the room whose meeting will end the soonest. We also keep track of the number of times each room is used in an array. The room with the maximum usage is the answer. The key intuition here is to always assign the meeting to the room that will be free the earliest, which ensures that the meetings are held as soon as possible.

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
    int mostBooked(int n, vector<vector<int>>& meetings) {
        sort(meetings.begin(), meetings.end());
        priority_queue<int, vector<int>, greater<int>> free_rooms;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> end_times;
        vector<int> room_usage(n, 0);
        for (int i = 0; i < n; i++) {
            free_rooms.push(i);
        }
        for (auto& meeting : meetings) {
            int start = meeting[0], end = meeting[1];
            while (!end_times.empty() && end_times.top().first <= start) {
                free_rooms.push(end_times.top().second);
                end_times.pop();
            }
            if (!free_rooms.empty()) {
                int room = free_rooms.top();
                free_rooms.pop();
                room_usage[room]++;
                end_times.push({end, room});
            } else {
                int room = end_times.top().second;
                int new_end = end_times.top().first + (end - start);
                end_times.pop();
                room_usage[room]++;
                end_times.push({new_end, room});
            }
        }
        int max_usage = 0, max_room = 0;
        for (int i = 0; i < n; i++) {
            if (room_usage[i] > max_usage) {
                max_usage = room_usage[i];
                max_room = i;
            }
        }
        return max_room;
    }
};
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="java">

{% highlight java %}
{% raw %}
class Solution {
    public int mostBooked(int n, int[][] meetings) {
        Arrays.sort(meetings, (a, b) -> a[0] - b[0]);
        PriorityQueue<Integer> freeRooms = new PriorityQueue<>();
        PriorityQueue<int[]> endTimes = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        int[] roomUsage = new int[n];
        for (int i = 0; i < n; i++) {
            freeRooms.add(i);
        }
        for (int[] meeting : meetings) {
            int start = meeting[0], end = meeting[1];
            while (!endTimes.isEmpty() && endTimes.peek()[0] <= start) {
                freeRooms.add(endTimes.poll()[1]);
            }
            if (!freeRooms.isEmpty()) {
                int room = freeRooms.poll();
                roomUsage[room]++;
                endTimes.add(new int[] {end, room});
            } else {
                int[] top = endTimes.poll();
                int newEnd = top[0] + (end - start);
                roomUsage[top[1]]++;
                endTimes.add(new int[] {newEnd, top[1]});
            }
        }
        int maxUsage = 0, maxRoom = 0;
        for (int i = 0; i < n; i++) {
            if (roomUsage[i] > maxUsage) {
                maxUsage = roomUsage[i];
                maxRoom = i;
            }
        }
        return maxRoom;
    }
}
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python">

{% highlight python %}
{% raw %}
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        free_rooms = list(range(n))
        end_times = []
        room_usage = [0] * n
        for start, end in meetings:
            while end_times and end_times[0][0] <= start:
                heapq.heappop(end_times)
                free_rooms.append(end_times[0][1])
            if free_rooms:
                room = free_rooms.pop(0)
                room_usage[room] += 1
                heapq.heappush(end_times, (end, room))
            else:
                top = heapq.heappop(end_times)
                new_end = top[0] + (end - start)
                room_usage[top[1]] += 1
                heapq.heappush(end_times, (new_end, top[1]))
        max_usage = max(room_usage)
        for i in range(n):
            if room_usage[i] == max_usage:
                return i
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="python3">

{% highlight python %}
{% raw %}
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        free_rooms = list(range(n))
        end_times = []
        room_usage = [0] * n
        for start, end in meetings:
            while end_times and end_times[0][0] <= start:
                heapq.heappop(end_times)
                free_rooms.append(end_times[0][1])
            if free_rooms:
                room = free_rooms.pop(0)
                room_usage[room] += 1
                heapq.heappush(end_times, (end, room))
            else:
                top = heapq.heappop(end_times)
                new_end = top[0] + (end - start)
                room_usage[top[1]] += 1
                heapq.heappush(end_times, (new_end, top[1]))
        max_usage = max(room_usage)
        for i in range(n):
            if room_usage[i] == max_usage:
                return i
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="c">

{% highlight c %}
{% raw %}
Not available for this problem
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="csharp">

{% highlight csharp %}
{% raw %}
Not available for this problem
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="javascript">

{% highlight javascript %}
{% raw %}
Not available for this problem
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="typescript">

{% highlight typescript %}
{% raw %}
Not available for this problem
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="php">

{% highlight php %}
{% raw %}
Not available for this problem
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="swift">

{% highlight swift %}
{% raw %}
Not available for this problem
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="kotlin">

{% highlight kotlin %}
{% raw %}
Not available for this problem
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="dart">

{% highlight dart %}
{% raw %}
Not available for this problem
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="go">

{% highlight go %}
{% raw %}
Not available for this problem
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="ruby">

{% highlight ruby %}
{% raw %}
Not available for this problem
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="scala">

{% highlight scala %}
{% raw %}
Not available for this problem
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="rust">

{% highlight rust %}
{% raw %}
Not available for this problem
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="racket">

{% highlight racket %}
{% raw %}
Not available for this problem
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="erlang">

{% highlight erlang %}
{% raw %}
Not available for this problem
{% endraw %}
{% endhighlight %}

  </div>

  <div class="tab-panel" data-lang="elixir">

{% highlight elixir %}
{% raw %}
Not available for this problem
{% endraw %}
{% endhighlight %}

  </div>

</div>

### Complexity Analysis

- **Time Complexity:** The time complexity of the solution is O(n log n + m log n) where n is the number of rooms and m is the number of meetings. This is because we are sorting the meetings based on their start times, which takes O(m log m) time. Then, for each meeting, we are using the two min heaps to find the free room or the room that will be free the earliest, which takes O(log n) time. Therefore, the total time complexity is O(n log n + m log n).

- **Space Complexity:** The space complexity of the solution is O(n + m) where n is the number of rooms and m is the number of meetings. This is because we are using two min heaps to keep track of the free rooms and the end times of the meetings, which takes O(n + m) space. We are also using an array to keep track of the number of times each room is used, which takes O(n) space. Therefore, the total space complexity is O(n + m).

</div>
</details>
