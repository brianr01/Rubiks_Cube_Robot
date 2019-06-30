from class_menu_manager import *

class menus_manager:
    def __init__(self, menus, starting_menu):
        self.menus = {}
        for menu_name in menus:
            menu = menu_manager(menus[menu_name]['frames'], menus[menu_name]['buttons'])
            self.menus[menu_name] = menu

        self.current_menu_name = starting_menu
        

    def set_current_menu(self, menu):
        if menu in self.menus:
            self.current_menu_name = menu
        else:
            raise Exception('The menu name provided was not valid')
    
    def update(self, cursor_x, cursor_y, event):
        self.menus[self.current_menu_name].update(cursor_x, cursor_y, event)


    def render(self, frame, new_frame_info_for_current_menu):
        frame = self.menus[self.current_menu_name].render(frame, new_frame_info_for_current_menu)
        return frame
