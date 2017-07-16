
First Question:
If you have only one room, what is the maximum number of meetings you can scheduled into that room.

Solution:
1. sort the meetings by finishing time, this is because we greedily choose the meeting that finishes first.
2. go through all the meetings in order of finishing time, schedule the meeting into the room if the room is not occupied at its start time, and increase the count by one.
3. no of count will be the max number of meetings you can schedule into the room.


Second Question:
You are given a set of meetings with start time and end time, what is the minimum number of meeting rooms you need to have to hold all the meetings.


A better solution using the greedy approach
1. We sort the meetings by start time
2. Then step through all the meetings in order of start time, keep a set of meeting rooms, if all the rooms are occupied, then we schedule a new room. To check all the previous scheduled meetings, we keep a priority queue by finishing time of all the scheduled meetings. Assume there are d number of rooms, then checking takes logd time.
3. count the number of rooms.