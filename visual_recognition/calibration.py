import cv2
import pickle
import time
import numpy as np
import random

thresholds = {'b':
        {'b': [
                {'upper_limit': [255, 100, 0], 'lower_limit': [255, 0, 0]},
                {'upper_limit': [255, 100, 0], 'lower_limit': [255, 0, 0]},
                {'upper_limit': [255, 100, 0], 'lower_limit': [255, 0, 0]},
                {'upper_limit': [255, 100, 0], 'lower_limit': [255, 0, 0]},
                {'upper_limit': [255, 100, 0], 'lower_limit': [255, 0, 0]},
                {'upper_limit': [255, 100, 0], 'lower_limit': [255, 0, 0]},
                {'upper_limit': [255, 100, 0], 'lower_limit': [255, 0, 0]},
                {'upper_limit': [255, 100, 0], 'lower_limit': [255, 0, 0]},
                {'upper_limit': [255, 100, 0], 'lower_limit': [255, 0, 0]}],

        'd': [{'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]},
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]},
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}],

        'f': [{'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}], 

        'l':   [{'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}], 

        'r':   [{'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]},
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}],

        'u':   [{'upper_limit': [0, 0, 175], 'lower_limit': [10, 58, 190]},
                {'upper_limit': [0, 0, 175], 'lower_limit': [10, 58, 190]},
                {'upper_limit': [0, 0, 175], 'lower_limit': [10, 58, 190]},
                {'upper_limit': [0, 0, 175], 'lower_limit': [10, 58, 190]},
                {'upper_limit': [0, 0, 175], 'lower_limit': [10, 58, 190]},
                {'upper_limit': [0, 0, 175], 'lower_limit': [10, 58, 190]}, 
                {'upper_limit': [0, 0, 175], 'lower_limit': [10, 58, 190]}, 
                {'upper_limit': [0, 0, 175], 'lower_limit': [10, 58, 190]}, 
                {'upper_limit': [0, 0, 175], 'lower_limit': [10, 58, 190]}]},

    'd': {
        'b':   [{'upper_limit': [255, 0, 255], 'lower_limit': [25, 50, 100]},
                {'upper_limit': [255, 0, 255], 'lower_limit': [25, 50, 100]}, 
                {'upper_limit': [255, 0, 255], 'lower_limit': [25, 50, 100]}, 
                {'upper_limit': [255, 0, 255], 'lower_limit': [25, 50, 100]}, 
                {'upper_limit': [255, 0, 255], 'lower_limit': [25, 50, 100]}, 
                {'upper_limit': [255, 0, 255], 'lower_limit': [25, 50, 100]}, 
                {'upper_limit': [255, 0, 255], 'lower_limit': [25, 50, 100]}, 
                {'upper_limit': [255, 0, 255], 'lower_limit': [25, 50, 100]}, 
                {'upper_limit': [255, 0, 255], 'lower_limit': [25, 50, 100]}], 

        'd':   [{'upper_limit': [100, 255, 100], 'lower_limit': [50, 0, 50]}, 
                {'upper_limit': [100, 255, 100], 'lower_limit': [50, 0, 50]}, 
                {'upper_limit': [100, 255, 100], 'lower_limit': [50, 0, 50]}, 
                {'upper_limit': [100, 255, 100], 'lower_limit': [50, 0, 50]},
                {'upper_limit': [100, 255, 100], 'lower_limit': [50, 0, 50]}, 
                {'upper_limit': [100, 255, 100], 'lower_limit': [50, 0, 50]}, 
                {'upper_limit': [100, 255, 100], 'lower_limit': [50, 0, 50]}, 
                {'upper_limit': [100, 255, 100], 'lower_limit': [50, 0, 50]}, 
                {'upper_limit': [100, 255, 100], 'lower_limit': [50, 0, 50]}],

        'f':   [{'upper_limit': [100, 255, 255], 'lower_limit': [100, 0, 0]}, 
                {'upper_limit': [100, 255, 255], 'lower_limit': [100, 0, 0]}, 
                {'upper_limit': [100, 255, 255], 'lower_limit': [100, 0, 0]}, 
                {'upper_limit': [100, 255, 255], 'lower_limit': [100, 0, 0]}, 
                {'upper_limit': [100, 255, 255], 'lower_limit': [100, 0, 0]}, 
                {'upper_limit': [100, 255, 255], 'lower_limit': [100, 0, 0]}, 
                {'upper_limit': [100, 255, 255], 'lower_limit': [100, 0, 0]}, 
                {'upper_limit': [100, 255, 255], 'lower_limit': [100, 0, 0]}, 
                {'upper_limit': [100, 255, 255], 'lower_limit': [100, 0, 0]}],

        'l':   [{'upper_limit': [255, 200, 255], 'lower_limit': [0, 0, 100]}, 
                {'upper_limit': [255, 200, 255], 'lower_limit': [0, 0, 100]}, 
                {'upper_limit': [255, 200, 255], 'lower_limit': [0, 0, 100]}, 
                {'upper_limit': [255, 200, 255], 'lower_limit': [0, 0, 100]}, 
                {'upper_limit': [255, 200, 255], 'lower_limit': [0, 0, 100]}, 
                {'upper_limit': [255, 200, 255], 'lower_limit': [0, 0, 100]}, 
                {'upper_limit': [255, 200, 255], 'lower_limit': [0, 0, 100]}, 
                {'upper_limit': [255, 200, 255], 'lower_limit': [0, 0, 100]}, 
                {'upper_limit': [255, 200, 255], 'lower_limit': [0, 0, 100]}], 

        'r':   [{'upper_limit': [255, 100, 255], 'lower_limit': [0, 100, 0]}, 
                {'upper_limit': [255, 100, 255], 'lower_limit': [0, 100, 0]}, 
                {'upper_limit': [255, 100, 255], 'lower_limit': [0, 100, 0]},
                {'upper_limit': [255, 100, 255], 'lower_limit': [0, 100, 0]}, 
                {'upper_limit': [255, 100, 255], 'lower_limit': [0, 100, 0]}, 
                {'upper_limit': [255, 100, 255], 'lower_limit': [0, 100, 0]}, 
                {'upper_limit': [255, 100, 255], 'lower_limit': [0, 100, 0]}, 
                {'upper_limit': [255, 100, 255], 'lower_limit': [0, 100, 0]}, 
                {'upper_limit': [255, 100, 255], 'lower_limit': [0, 100, 0]}],

        'u': [{'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}]},

    'f': {
        'b':   [{'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}],

        'd': [{'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}],

        'f': [{'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}],

        'l': [{'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}], 
        'r': [{'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}],

        'u': [{'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
                {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}]}, 

    'l': {
        'b': [{'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}],

        'd': [{'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}],

        'f': [{'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}], 

        'l': [{'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}], 

        'r': [{'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]},
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]},
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}],

        'u': [{'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}]},
    'r': {
        'b': [{'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}], 

        'd': [{'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]},
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}],

        'f': [{'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}],

        'l': [{'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}],

        'r': [{'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}], 

        'u': [{'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}]}, 

    'u': {
        'b': [{'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}],

        'd': [{'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}],

        'f': [{'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}],

        'l': [{'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}],

        'r': [{'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}, 
            {'upper_limit': [255, 255, 255], 'lower_limit': [0, 0, 0]}],
            
        'u': [{'upper_limit': [0, 255, 0], 'lower_limit': [100, 0, 255]}, 
              {'upper_limit': [0, 255, 0], 'lower_limit': [100, 0, 255]}, 
              {'upper_limit': [0, 255, 0], 'lower_limit': [100, 0, 255]}, 
              {'upper_limit': [0, 255, 0], 'lower_limit': [100, 0, 255]}, 
              {'upper_limit': [0, 255, 0], 'lower_limit': [100, 0, 255]}, 
              {'upper_limit': [0, 255, 0], 'lower_limit': [100, 0, 255]}, 
              {'upper_limit': [0, 255, 0], 'lower_limit': [100, 0, 255]}, 
              {'upper_limit': [0, 255, 0], 'lower_limit': [100, 0, 255]}, 
              {'upper_limit': [0, 255, 0], 'lower_limit': [100, 0, 255]}]}}


def display_calibration(cube_colors, height =  200, width = 532):
    image = np.zeros((height, width, 3),  np.uint8)
    image[:] = (100, 100, 100)
    
    x_width = int((532 - (532 % 36)) / 36)
    y_width = int(x_width * (width / height))
    y_width = int(x_width * 1.6)

    x_current = int((532 % 36)/6)

    for face in cube_colors:
        cube_faces = cube_colors[face]

        for side in cube_faces:
            cube_side = cube_faces[side]
            y_current = int(y_width / 3)
            z = 0
            for sticker in range(0, len(cube_side)):
                limit = cube_side[sticker]
                random1 = (random.randint(100,255),random.randint(100,255),random.randint(100,255))
                random2 = (random.randint(100,255),random.randint(100,255),random.randint(100,255))
                cv2.rectangle(image, (x_current, y_current), (x_current + 10, y_current+10) ,random1, -1)
                cv2.rectangle(image, (x_current+6, y_current), (x_current + 12, y_current+10) ,random2, -1)
                
                y_current += y_width

            x_current += x_width
        x_current += int(x_width / 3)



    # cv2.rectangle(image, (x0, y0), (x1, y1) ,(b, r, g),-1)

# 18x54
    return image       
      
image = display_calibration(thresholds)          
while True:
    cv2.imshow('image', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break  