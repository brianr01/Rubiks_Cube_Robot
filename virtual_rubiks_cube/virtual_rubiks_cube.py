import numpy
import kociemba #cube solving algorithm
import random
'''
             |============|
             |=U1==U2==U3=|
             |============|
             |=U4==U5==U6=|
             |============|
             |=U7==U8==U9=|
             |============|
 ============|============|============|============
 =L1==L2==L3=|=F1==F2==F3=|=R1==R2==R3=|=B1==B2==B3=
 ============|============|============|============
 =L4==L5==L6=|=F4==F5==F6=|=R4==R5==R6=|=B4==B5==B6=
 ============|============|============|============
 =L7==L8==L9=|=F7==F8==F9=|=R7==R8==R9=|=B7==B8==B9=
 ============|============|============|============
             |============|
             |=D1==D2==D3=|
             |============|
             |=D4==D5==D6=|
             |============|
             |=D7==D8==D9=|
             |============|
'''


class Virtual_Cube:
    side_order = 'urfdlb'

    edges_of_moving_face = {'u':['b3', 'b2', 'b1',
                                   'r3', 'r2', 'r1',
                                   'f3', 'f2', 'f1',
                                   'l3', 'l2', 'l1'],

                              'r':['u9', 'u6', 'u3',
                                   'b1', 'b4', 'b7',
                                   'd9', 'd6', 'd3',
                                   'f9', 'f6', 'f3'],

                              'f':['u7', 'u8', 'u9',
                                   'r1', 'r4', 'r7',
                                   'd3', 'd2', 'd1',
                                   'l9', 'l6', 'l3'],

                              'd':['f7', 'f8', 'f9',
                                   'r7', 'r8', 'r9',
                                   'b7', 'b8', 'b9',
                                   'l7', 'l8', 'l9'],

                              'l':['u1', 'u4', 'u7',
                                   'f1', 'f4', 'f7',
                                   'd1', 'd4', 'd7',
                                   'b9', 'b6', 'b3'],

                              'b':['u3', 'u2', 'u1',
                                   'l1', 'l4', 'l7',
                                   'd7', 'd8', 'd9',
                                   'r9', 'r6', 'r3']}

    solved_cube_state = {'u':['u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u'],
                         'r':['r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r'], 
                         'f':['f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f'],
                         'd':['d', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd'],
                         'l':['l', 'l', 'l', 'l', 'l', 'l', 'l', 'l', 'l'],
                         'b':['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']}

    def __init__(self):
        self.reset()

    def reset(self):
        self.cube_position = {'u':['u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u'],
                              'r':['r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r'], 
                              'f':['f', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'f'],
                              'd':['d', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd'],
                              'l':['l', 'l', 'l', 'l', 'l', 'l', 'l', 'l', 'l'],
                              'b':['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']}

    #takes an input in cube notation and executes them on the virtual cube
    def execute_algorithm(self, algorithm):
        move_list = len(algorithm)
        iteration = 0

        while True:
            if (iteration >= move_list):
                break
            if ( algorithm[iteration] == ' '):
                iteration += 1
            else:
                if (iteration + 1 < move_list):
                    if (algorithm[iteration + 1] == "'"):
                        self.turn_side(algorithm[iteration].lower(), False)
                        iteration += 3
                    elif (algorithm[iteration + 1] == "2"):
                        self.turn_side(algorithm[iteration].lower(), False)
                        self.turn_side(algorithm[iteration].lower(), False)
                        iteration += 3
                    else:
                        self.turn_side(algorithm[iteration].lower(), True)
                        iteration += 2
                else:
                    self.turn_side(algorithm[iteration].lower(), True)
                    break

    def convert_algorithm(self, algorithm):
        move_list = len(algorithm)
        iteration = 0
        converted_moves = []

        while True:
            if (iteration >= move_list):
                break
            if ( algorithm[iteration] == ' '):
                iteration += 1
            else:
                if (iteration + 1 < move_list):
                    if (algorithm[iteration + 1] == "'"):
                        converted_moves.append(algorithm[iteration].lower())
                        iteration += 3
                    elif (algorithm[iteration + 1] == "2"):
                        converted_moves.append(algorithm[iteration].lower())
                        converted_moves.append(algorithm[iteration].lower())
                        iteration += 3
                    else:
                        converted_moves.append(algorithm[iteration].upper())
                        iteration += 2
                else:
                    converted_moves.append(algorithm[iteration].upper())
                    break

        return converted_moves

    def turn_side(self, face, direction_clockwise):
        if(len(self.cube_position[face]) != 9):
            raise Exception('Array length was not 9')

        #rotate the cube face that is passed in
        unordered_cube_face = self.cube_position[face]

        #order face in spiral order instead of row order
        ordered_cube_face = [1,2,3,6,9,8,7,4]
        for i in range(0,8):
            ordered_cube_face[i] = unordered_cube_face[ordered_cube_face[i]-1]

        #rotate the face the given direction 1 time
        ordered_cube_face = self.rotate_array(ordered_cube_face, 2, direction_clockwise)

        #order face back into row order to place back in dictionary
        reordered_cube_face = [1,2,3,8,4,7,6,5]
        for i in range(0,8):
            reordered_cube_face[i] = ordered_cube_face[reordered_cube_face[i]-1]

        #insert the middle side and place back in dictionary
        reordered_cube_face.insert(4,face + '5')
        self.cube_position[face] = reordered_cube_face

        #adds all sides adjacent to the rotated face to an array to rotate
        unordered_cube_side = []
        for sticker in self.edges_of_moving_face[face]:
            current_side = sticker[0]
            current_side_sticker_number = int(sticker[1])
            unordered_cube_side.append(self.cube_position[current_side][current_side_sticker_number - 1])

        #rotates the array of adjacent parts
        ordered_cube_side = self.rotate_array(unordered_cube_side, 3, direction_clockwise)

        #places the rotated array back into the cube
        for sticker_number in range(0, len(self.edges_of_moving_face[face])):
            sticker = self.edges_of_moving_face[face][sticker_number]
            current_side = sticker[0]
            current_side_sticker_number = int(sticker[1])
            self.cube_position[current_side][current_side_sticker_number - 1] = ordered_cube_side[sticker_number]


    #this method is used to rotate a face or the sides around a face when a cube turn is made
    def rotate_array(self, array, times, direction_clockwise):
        if (direction_clockwise != False and direction_clockwise != True):
            raise Exception('direction" was not a boolean value')

        #rotates an array of cube parts in the direction passed into the function
        if (direction_clockwise == False):
            for i in range(0,times):
                array.append(array[0])
                del array[0]
        else:
            for i in range(0,times):
                array.insert(0, array[-1])
                del array[-1]

        return array

    #places the cube in the required state for the used algorithm(kociemba) and returns the solution
    def get_solution(self):
        solution = kociemba.solve(self.get_cube_position_for_kociemba())
        return solution

    def get_cube_position_for_kociemba(self):
        oriented_cube =self.get_orientated_cube()

        cube_position_for_kociemba = ''
        for side in self.side_order:
            cube_side = oriented_cube[side]
            for sticker in cube_side:
                cube_position_for_kociemba += sticker[0]

        return cube_position_for_kociemba.upper()

    def get_orientated_cube(self):

        orientation_map = self.get_orientation_map()

        orientated_cube = self.cube_position
        for side in self.side_order:
            for i in range(0, len(orientated_cube[side])):
                orientated_cube[side][i] = orientation_map[orientated_cube[side][i]]
        
        return orientated_cube
    
    def get_orientation_map(self):
        orientation_map = {}
        for side in self.cube_position:
            orientation_map[self.cube_position[side][4]] = side
        
        return orientation_map

    #takes the current cube state and prints it to the console
    def print_cube(self):
        #creates an array of spaces that has equal rows to the faces
        leading_spaces = '              '
        spaces_array = []
        for i in range(0,7):
            spaces_array.insert(i, leading_spaces)

        #create individual lines for each cube face
        cube = self.format_cube()

        #create cube faces
        divider = '|============|'
        iteration = 0
        formated_cube_faces = []
        for face in cube:
            section = []
            for row in cube[face]:
                section.append(divider)
                section.append(row)
            section.append(divider)
            formated_cube_faces.insert(iteration, section)
            iteration += iteration

        #combine each line portion
        first_third = self.create_print_rows(spaces_array, formated_cube_faces[0], spaces_array, spaces_array)
        second_third = self.create_print_rows(formated_cube_faces[2], formated_cube_faces[3], formated_cube_faces[1], formated_cube_faces[5])
        third_third = self.create_print_rows(spaces_array, formated_cube_faces[4], spaces_array, spaces_array)
        combined_array = first_third + second_third + third_third

        #print cube to console
        print('\n\n')
        for line in combined_array:
            print(line)


    #calls format_face for each side of cube
    def format_cube(self):
        sides = ['u', 'l', 'f', 'r', 'b', 'd']
        cube = {}
        for side in sides:
            cube[side] = self.format_face(side)
        return cube

    #for a given face, formats the current state into readable strings
    def format_face(self,face):
        row_1 = '|-{}--{}--{}-|'.format(self.cube_position[face][0], self.cube_position[face][1], self.cube_position[face][2])
        row_2 = '|-{}--{}--{}-|'.format(self.cube_position[face][3], self.cube_position[face][4], self.cube_position[face][5])
        row_3 = '|-{}--{}--{}-|'.format(self.cube_position[face][6], self.cube_position[face][7], self.cube_position[face][8])
        return row_1, row_2, row_3


    def create_print_rows(self, array1, array2, array3, array4):
        #add columns together
        combined_array = numpy.stack((array1, array2, array3, array4), axis =- 1)
        less_lines = []

        #combine elements in each line to reduce complexity
        for i in range(0,7):
            line = ''
            for j in range(0,4):
                line += combined_array[i][j]
            less_lines.append(line)
        return less_lines

    def get_cube_state(self):
        return self.cube_position

    def get_scramble(self, moves = 20):
        possible_moves = ["R ", "R' ", "L ", "L' ", "U ", "U' ", "D ", "D' ", "F ", "F' ", "B ", "B' "]
        scramble = ""
        for i in range(0,moves):
            scramble = scramble + possible_moves[random.randint(0,11)]

        return scramble
