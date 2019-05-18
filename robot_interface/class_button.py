import cv2

class button:
    def __init__(self, size, location, color, text_color, text, action, parameters = None):
        self.size = size
        self.location = (location, (location[0] + size[0], location[1] + size[1]))
        self.color = color
        self.text = text
        self.action = action
        self.being_pressed = True
        self.text_color = text_color
        self.parameters = parameters



    def update(self, cursor_location, mouse_code):
        if ((cursor_location[0] > self.location[0][0] and  cursor_location[0] < self.location[1][0]) and (cursor_location[1] > self.location[0][1] and cursor_location[1] < self.location[1][1])):
            if(mouse_code == 4):
                if (self.parameters == None):
                    return self.action()
                else:
                    self.action(self.parameters)


    def render(self, frame):
        cv2.rectangle(frame, (self.location[0][0], self.location[0][1]), (self.location[1][0], self.location[1][1]) ,(255,255,255),-1)
        cv2.rectangle(frame, (self.location[0][0] + 1, self.location[0][1] + 1), (self.location[1][0] - 1, self.location[1][1] - 1) ,(0,0,0),-1)
        cv2.rectangle(frame, (self.location[0][0] + 2, self.location[0][1] + 2), (self.location[1][0] - 2, self.location[1][1] - 2) ,self.color,-1)
        cv2.putText(frame, self.text ,(self.location[0][0] + 9, self.location[0][1] + 30) ,cv2.FONT_HERSHEY_SIMPLEX , 1, self.text_color ,2 ,cv2.LINE_AA)
        return frame
    

    

        