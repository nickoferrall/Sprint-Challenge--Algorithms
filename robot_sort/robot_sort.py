class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"

    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"

    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def get_item(self):
        self._item = self._list[self._position + 1]

    def sort(self):
        """
        Sort the robot's list.
        """
        # Fill this out
        self.set_light_on()

        self.swap_item()
        self.move_right()
        while self.light_is_on() == True:
            self.swap_item()
            while self.can_move_right():
                self.set_light_off()
                if self.compare_item() == 1:
                    self.swap_item()
                    self.set_light_on()
                    self.move_left()
                    self.swap_item()
                    self.move_right()
                    self.swap_item()
                    self.move_right()
                else:
                    self.swap_item()
                    self.move_right()

            if self.can_move_right() == False:
                if self.compare_item() == 1:
                    self.swap_item()
                    self.set_light_on()
            while self.can_move_left():
                self.move_left()
                if self.compare_item() == 1:
                    self.swap_item()
                    self.set_light_on()
                if self.can_move_left() == False:
                    if self.compare_item() == -1:
                        self.swap_item()
                    elif self._item != None and self._list[self._position] == None:
                        self.swap_item()


# if __name__ == "__main__":
#     # Test our your implementation from the command line
#     # with `python robot_sort.py`

#     l = [11, 13, 7, 17, 9, 20, 1, 21, 2, 4, 22, 16,
#          15, 10, 23, 19, 8, 3, 5, 14, 6, 0, 24, 12, 18]

#     # l = [41, 21, 58, 49, 26]
#     # l = [5, 4, 3, 2, 1]

# #  self.small_list = [5, 4, 3, 2, 1]
# #     self.medium_list = [11, 13, 7, 17, 9, 20, 1, 21, 2, 4, 22, 16, 15, 10, 23, 19, 8, 3, 5, 14, 6, 0, 24, 12, 18]
# #     self.large_list = [20, 77, 45, 16, 15, 91, 12, 6, 24, 89, 53, 19, 85, 56, 13, 74, 48, 98, 9, 92, 25, 35, 54, 44, 50, 5, 75, 34, 2, 42, 87, 49, 76, 52, 43, 23, 7, 80, 66, 14, 46, 90, 88, 40, 97, 10, 57, 63, 1, 18, 67, 79, 96, 27, 73, 28, 32, 61, 30, 8, 17, 93, 26, 51, 60, 55, 62, 31, 47, 64, 39, 22, 99, 95, 83, 70, 38, 69, 36, 41, 37, 65, 84, 3, 29, 58, 0, 94, 4, 11, 33, 86, 21, 81, 72, 82, 59, 71, 68, 78]
# #     self.large_varied_list = [1, -38, -95, 4, 23, -73, -65, -36, 85, 2, 58, -26, -55, 96, 55, -76, 64, 45, 69, 36, 69, 47, 29, -47, 13, 89, -57, -88, -87, 54, 60, 56, -98, -78, 59, 93, -41, -74, 73, -35, -23, -79, -35, 46, -18, -18, 37, -64, 14, -57, -2, 15, -85, 45, -73, -2, 79, -87, -100, 21, -51, 22, 26, -59, 81, 59, -24, 24, -81, 43, 61, 52, 38, -88, -95, 87, -57, -37, -65, -47, -3, 21, -77, 98, 25, 1, -36, 39, 78, 47, -35, -40, -69, -81, 11, -47, 21, 25, -53, -31]
# #     self.random_list = [random.randint(0, 100) for i in range(0, 100)]

# robot = SortingRobot(l)

# robot.sort()
# print(robot._list)
