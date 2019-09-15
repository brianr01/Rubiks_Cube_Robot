import timeit
import time

p0 = (5,10)
p1 = (100,20)


class Acceleration:
    def __init__(self):
        self.graph_points = []
        self.current_x = 0
        self.steps_in_turn = 50

    def get_sleep_times(self):
        self.sleep_times = []
        self.reset_x()

        #iterates over each step and appends the sleep times
        for i in range(0, self.steps_in_turn - 1):
            nex_sleep_time = self.get_next_sleep_time()
            self.sleep_times.append(nex_sleep_time)

        return self.sleep_times

    def reset_x(self):
        self.current_x = 0

    def get_next_sleep_time(self):
        self.iterate_x()
        steps_per_second = self.calculate_steps_per_second()
        sleep_time = self.convert_steps_per_second_to_sleep_time(steps_per_second)

        return sleep_time

    def iterate_x(self):
        self.current_x += 1

    def calculate_steps_per_second(self):
        points_with_x_in_between = self.get_points_with_x_in_between()
        x0 = self.current_x
        x1, y1 = points_with_x_in_between[1]
        slope = self.get_slope(*points_with_x_in_between)

        #calculates the steps per second based of of the y intercept of the line with modified point-slope formula
        self.steps_per_second = (slope * (x0 - x1)) + y1

        return self.steps_per_second

    def get_points_with_x_in_between(self):
        for point_number in range(0, len(self.graph_points)):
            if (self.current_x < self.graph_points[point_number][0]):
                return [self.graph_points[point_number - 1], self.graph_points[point_number]]
        raise Exception ('The current x was not in between any existing points')

    def get_slope(self, p0, p1):
        x0, y0 = p0
        x1, y1 = p1

        #calculates the slope of a line
        slope = float(y0 - y1) / float(x0 - x1)

        return slope

    def convert_steps_per_second_to_sleep_time(self, steps_per_second):
        sleep_time = 1/float(steps_per_second)

        return sleep_time

    def add_points_to_graph(self, points):
        for point in points:
            self.add_point_to_graph(*point)

    def add_point_to_graph(self, x, y):
        self.graph_points.append([x,y])
        self.graph_points = self.graph_points.sort()

    def update_point_on_graph(self, x, y):
        index = self.get_index_of_point_with_x(self, x)
        if (index == None):
            add_point_to_graph(self, x, y)
        else:
            self.graph_points.remove(index)
            self.add_point_to_graph(x, y)

    def get_index_of_point_with_y(self , x):
        for index in range(0, self.graph_points):
            if (self.graph_points[index][0] == x):
                return index
        return None

acceleration_calibration = Acceleration()

acceleration_calibration.add_point_to_graph(0,0)
acceleration_calibration.add_point_to_graph(10,15)
acceleration_calibration.add_point_to_graph(19,9)
acceleration_calibration.add_point_to_graph(50,0)

print(acceleration_calibration.get_sleep_times())
