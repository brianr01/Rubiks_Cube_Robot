import cv2
import numpy as np
camera = 1
resolution = [1080,720]
cap = cv2.VideoCapture(camera)
cap.set(3,resolution[0])
cap.set(4,resolution[1])
thresholdPoints = {'u':[( 459 , 101 ) ,( 459 , 104 ) ,( 521 , 97 ) ,( 520 , 106 ) ,( 576 , 120 ) ,( 624 , 143 ) ,( 589 , 159 ) ,( 537 , 139 ) ,( 576 , 137 ) ,( 678 , 163 ) ,( 743 , 193 ) ,( 700 , 223 ) ,( 641 , 195 ) ,( 701 , 189 ) ,( 602 , 233 ) ,( 645 , 262 ) ,( 601 , 294 ) ,( 560 , 264 ) ,( 622 , 260 ) ,( 493 , 290 ) ,( 555 , 342 ) ,( 499 , 376 ) ,( 499 , 332 ) ,( 434 , 331 ) ,( 377 , 295 ) ,( 426 , 267 ) ,( 380 , 237 ) ,( 334 , 261 ) ,( 385 , 262 ) ,( 306 , 174 ) ,( 340 , 199 ) ,( 285 , 225 ) ,( 238 , 201 ) ,( 304 , 201 ) ,( 401 , 123 ) ,( 435 , 137 ) ,( 393 , 157 ) ,( 354 , 148 ) ,( 409 , 148 ) ,( 462 , 91 ) ,( 457 , 103 ) ],                   
                   'r':[( 230 , 255 ) ,( 265 , 276 ) ,( 272 , 329 ) ,( 241 , 305 ) ,( 252 , 296 ) ,( 253 , 352 ) ,( 278 , 377 ) ,( 286 , 412 ) ,( 257 , 392 ) ,( 269 , 383 ) ,( 268 , 441 ) ,( 279 , 458 ) ,( 273 , 467 ) ,( 350 , 517 ) ,( 381 , 539 ) ,( 388 , 565 ) ,( 352 , 535 ) ,( 372 , 543 ) ,( 430 , 579 ) ,( 476 , 627 ) ,( 474 , 640 ) ,( 429 , 602 ) ,( 454 , 613 ) ,( 420 , 535 ) ,( 471 , 576 ) ,( 467 , 536 ) ,( 413 , 493 ) ,( 443 , 533 ) ,( 471 , 490 ) ,( 470 , 438 ) ,( 435 , 439 ) ,( 403 , 394 ) ,( 409 , 438 ) ,( 362 , 400 ) ,( 354 , 353 ) ,( 331 , 353 ) ,( 298 , 308 ) ,( 312 , 357 ) ,( 277 , 336 ) ,( 265 , 279 ) ,( 230 , 254 ) ,( 254 , 297 ) ,( 242 , 310 ) ],
                   'b':[(537, 427), (543, 423), (546, 425), (542, 436), (528, 434), (557, 409), (645, 350), (648, 342), (660, 345), (658, 354), (642, 359), (643, 351), (652, 349), (745, 283), (747, 275), (754, 284), (744, 287), (735, 282), (742, 282), (744, 291), (737, 294), (725, 392), (721, 389), (719, 379), (728, 379), (728, 388), (722, 388), (710, 455), (720, 450), (724, 450), (723, 451), (722, 451), (631, 539), (631, 537), (635, 532), (635, 534), (634, 534), (533, 610), (534, 610), (538, 605), (542, 609), (538, 611), (542, 535), (539, 531), (546, 532), (544, 536), (541, 535), (528, 441), (528, 437), (536, 432), (544, 426), (551, 425), (540, 442), (536, 443), (532, 432), (667, 408), (641, 423), (620, 444), (608, 481), (613, 496)]}
camera0points = np.array([(515,55),(217,208),(290,472),(506,687),(746,479),(805,203)],np.int32)
camera1points = np.array([( 656 , 66 ) ,
( 941 , 206 ) ,
( 880 , 473 ) ,
( 645 , 666 ) ,
( 426 , 461 ) ,
( 368 , 198 )],np.int32)
pts = camera0points
printOut = []
def mouse_callback(event,x,y,flags,params):
    global cap,pts,printOut
    if event ==6:
        printOut.append((x,y))
    if event == 1:
        print(printOut)
        printOut = []
        cap.release()
        print('me1')
        camera = 1
        cap = cv2.VideoCapture(camera)
        cap.set(3,resolution[0])
        cap.set(4,resolution[1])
        pts = camera1points
    if event == 2:
        print(printOut)
        printOut = []
        cap.release()
        print('me0')
        camera = 0
        cap = cv2.VideoCapture(camera)
        cap.set(3,resolution[0])
        cap.set(4,resolution[1])
        pts = camera0points

while True:
    #img = np.zeros((1080,1080,3) ,dtype='uint8')
    ret, frame = cap.read()
    #lines = [(501,65),(217,208),(280,472),(506,687),(746,479),(805,203),(501,65),(501,65)]
    #for lineNumber in range(0,len(lines)-1):
    #    point = (lines[lineNumber],lines[lineNumber+1])
    #    cv2.line(frame,lines[lineNumber],lines[lineNumber+1],(255,255,255),3)
    #pts = pts.reshape((-1,1,2))
    mask = cv2.inRange(frame,255,0)
    cv2.fillPoly(mask,[pts],255)
    res = cv2.bitwise_and(frame,frame, mask= mask)                   
    cv2.setMouseCallback('frame', mouse_callback)
    for point in thresholdPoints['u']:
        cv2.circle(res,point,4,[255,255,255])
    for point in thresholdPoints['r']:
        cv2.circle(res,point,4,[255,255,255])
    for point in thresholdPoints['b']:
        cv2.circle(res,point,4,[255,255,255])
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord(' '):
        break

    
    
