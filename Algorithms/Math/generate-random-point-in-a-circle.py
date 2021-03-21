# question link: https://leetcode.com/problems/generate-random-point-in-a-circle/

import math
import random
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> List[float]:
        r = (random.random()) ** 0.5 * self.radius
        theta = random.random() * 2 * math.pi
        new_x = self.x + r * math.cos(theta)
        new_y = self.y + r * math.sin(theta)
        return [new_x, new_y]
