import sys

#adds images to working directory
sys.path.append(sys.path[0] + '/robot_interface/menu_managers')
sys.path.append(sys.path[0] + '/robot_interface/menu_classes')

import class_menus_manager
import cv2
import numpy as np

import class_main_menu
import class_calibration_menu
import class_polygons_menu
import class_colors_menu
import class_acceleration_menu
import class_profiles_menu

main_frame_width  = 1080
main_frame_height = 1920

class robot_interface:
    def __init__(self, external_functions):
        self.external_functions = external_functions
        self.external_functions['change_menu'] = self.change_menu

        self.main_menu = class_main_menu.main_menu(external_functions)

        self.calibraion_menu = class_calibration_menu.calibration_menu(external_functions)

        self.polygons_menu = class_polygons_menu.polygons_menu(external_functions)

        self.colors_menu = class_colors_menu.colors_menu(external_functions)

        self.acceleration_menu = class_acceleration_menu.acceleration_menu(external_functions)

        self.profiles_menu = class_profiles_menu.profiles_menu(external_functions)

        menus = {'main':self.main_menu.menu, 'calibrate':self.calibraion_menu.menu, 'polygons':self.polygons_menu.menu, 'colors':self.colors_menu.menu, 'acceleration':self.acceleration_menu.menu, 'profiles':self.profiles_menu.menu}

        self.menus = class_menus_manager.menus_manager(menus, 'calibrate')
        self.quit = False
        self.frame = np.zeros((main_frame_height, main_frame_width, 3), np.uint8)

    def change_menu(self, menu_name):
        self.menus.set_current_menu(menu_name)

    def render(self):
        new_frame_info_for_current_menu = {}
        image = self.menus.render(np.zeros((main_frame_height, main_frame_width, 3), np.uint8), new_frame_info_for_current_menu)
        return image

    def update(self,cursor_y, cursor_x, event):
        self.menus.update(cursor_x, cursor_y, event)
