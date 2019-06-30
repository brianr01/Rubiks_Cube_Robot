import cv2

class button_manager:
    def __init__(self, size, location, color, text_color, text, action, parameters = None):               
        color_switcher = {
            'white': (255, 255, 255),
            'blue': (255, 25, 0),
            'red': (0, 10, 255),
            'green': (10, 255, 0),
            'orange': (0, 150, 255),
            'yellow': (7, 255, 255),
            'black': (0, 0, 0)
        }
        
        self.size = size
        self.location = (location, (location[0] + size[0], location[1] + size[1]))

        if color.lower() in color_switcher:
            self.color = color_switcher[color]
        else:
            self.color = color
                

        if text_color.lower() in color_switcher:
            self.text_color = color_switcher[text_color]
        else:
            self.text_color = text_color

        self.text = text
        self.action = action
        self.being_pressed = True
        self.parameters = parameters



    def update(self, cursor_location, event):
        if ((cursor_location[0] > self.location[0][0] and  cursor_location[0] < self.location[1][0]) and (cursor_location[1] > self.location[0][1] and cursor_location[1] < self.location[1][1])):
            if(event == 4):
                if (self.parameters == None):
                    return self.action()
                else:
                    self.action(self.parameters)


    def render(self, frame):
        #button boundry
        cv2.rectangle(frame, (self.location[0][0], self.location[0][1]), (self.location[1][0], self.location[1][1]) ,(255,255,255),-1)
        cv2.rectangle(frame, (self.location[0][0] + 1, self.location[0][1] + 1), (self.location[1][0] - 1, self.location[1][1] - 1) ,(0,0,0),-1)

        #button 
        cv2.rectangle(frame, (self.location[0][0] + 2, self.location[0][1] + 2), (self.location[1][0] - 2, self.location[1][1] - 2) ,self.color,-1)

        #button text
        cv2.putText(frame, self.text ,(self.location[0][0] + 9, self.location[0][1] + 30) ,cv2.FONT_HERSHEY_SIMPLEX , 1, self.text_color ,2 ,cv2.LINE_AA)
        return frame
    

    

        