class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pseudocode:
        # pair each car's position with its speed
        # sort cars from closest to target to farthest
        # calculate each car's time to reach target
        # if current time is greater than front fleet time:
        #     it becomes a new fleet
        # else:
        #     it joins the fleet ahead
        # return number of fleets

        cars = sorted(zip(position, speed), reverse=True)

        fleets = 0
        front_time = 0

        for pos, spd in cars:
            time = (target - pos) / spd

            if time > front_time:
                fleets += 1
                front_time = time

        return fleets