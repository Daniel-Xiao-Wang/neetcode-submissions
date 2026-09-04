class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        fleets = []

        for i in range(len(cars)):
            time = (target - cars[i][0]) / cars[i][1]
            if fleets:
                if time > fleets[-1]:
                    fleets.append(time)
            else:
                fleets.append(time)
        
        return len(fleets)
            
