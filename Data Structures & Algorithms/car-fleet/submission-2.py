# Pseudocode:
# pair each car's position with its speed
# sort cars by position from closest to target to farthest
# create fleets = 0
# create front_time = 0
#
# loop through each car from front to back:
#     calculate time = (target - position) / speed
#
#     if time > front_time:
#         car cannot catch the nearest fleet ahead
#         it becomes a new fleet
#         increase fleets by 1
#         update front_time to this car's time
#
#     else:
#         car catches the nearest fleet ahead
#         it joins that fleet
#         do not update front_time
#
# return fleets

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        fleet = 0
        front_time = 0
        for pos, spd in cars:
            time = (target - pos) / spd
            if time > front_time:
                fleet = fleet + 1
                front_time = time
            else:
                pass
        return fleet          
        