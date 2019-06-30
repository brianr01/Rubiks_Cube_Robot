#this class manages the points for calibrating all the polygons
class polygon_points_manager:

    def __init__(self):
        self.current_side = 'u'
        self.current_address = 1
        self.original_polygons_state = {'u':[[], [],  [],  [],  [],  [],  [],  [],  []],
                                        'f':[[], [],  [],  [],  [],  [],  [],  [],  []],
                                        'r':[[], [],  [],  [],  [],  [],  [],  [],  []], 
                                        'd':[[], [],  [],  [],  [],  [],  [],  [],  []],
                                        'l':[[], [],  [],  [],  [],  [],  [],  [],  []],
                                        'b':[[], [],  [],  [],  [],  [],  [],  [],  []]}

        self.polygons = self.original_polygons_state
        self.side_order = 'ufrdbl'
    
    def get_current_polygon_points(self):
        return self.polygons[self.current_side][self.current_address - 1]
    
    def get_all_polygons(self):
        return self.polygons

    def add_point_to_current_polygon(self, point):
        self.polygons[self.current_side][self.current_address - 1].append(point)

    def remove_point_from_current_polygon(self):
        del self.polygons[self.current_side][self.current_address - 1][-1]

    def reset_current_polygon(self):
        self.polygons[self.current_side][self.current_address - 1] = []
    
    def reset_all_polygons(self):
        self.polygons = self.original_polygons_state


    def set_current_polygon(self, side, address):
        self.current_side = side
        self.current_address = address

    def set_current_polygon_to_next(self):
        if (self.current_address == 9):
            self.set_current_side_to_next()
            self.current_address = 1
        else:
            self.current_address += 1
    
    def set_current_side_to_next(self):
        if (self.current_side == self.side_order[-1]):
            self.current_side = self.side_order[0]
        else:
            current_side_number = self.side_order.find(self.current_side)
            new_current_side = self.side_order[current_side_number + 1]
            self.current_side = new_current_side

    def set_current_polygon_to_previous(self):
        if (self.current_address == 1):
            self.set_current_side_to_previous()
            self.current_address = 9
        else:
            self.current_address -= 1

    def set_current_side_to_previous(self):
        if (self.current_side == self.side_order[0]):
            self.current_side = self.side_order[-1]
        else:
            current_side_number = self.side_order.find(self.current_side)
            new_current_side = self.side_order[current_side_number - 1]
            self.current_side = new_current_side
