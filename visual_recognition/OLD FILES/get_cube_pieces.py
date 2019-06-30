import GetCubeColors

proper_order = 'wbrgoy'
constand_invert_pieces_sets_colors = {
                                    'wrg':[1,  17, 27],
                                    'wgo':[3,  25, 35],
                                    'wbo':[5,  11, 33],
                                    'wbr':[7,  9,  19],
                                    'boy':[13, 39, 41],
                                    'goy':[31, 37, 43],
                                    'rgy':[23, 29, 45],
                                    'bry':[15, 21, 47],
                                    
                                    'wg':[2,  26],
                                    'wo':[4,  34],
                                    'wb':[6,  10],
                                    'wr':[8,  18],
                                    'br':[16, 20],
                                    'rg':[24, 28],
                                    'go':[32, 36],
                                    'bo':[12, 40],
                                    'oy':[38, 42],
                                    'gy':[30, 44],
                                    'ry':[22, 46],
                                    'by':[14, 48],
                                    
                                    'w':[49],
                                    'b':[50],
                                    'r':[51],
                                    'g':[52],
                                    'o':[53],
                                    'y':[54]
                                    }

constant_pieces_sets_colors_to_numbers = [
    [
        {"w" :49 },
        {"b" :50},
        {"r" :51},
        {"g" :52},
        {"o" :53},
        {"y" :54}
    ],  
    [
        {"w" :2, "g" :26},
        {"w" :4, "o" :34},
        {"w" :6, "b" :10},
        {"w" :8, "r" :18},
        {"b" :16, "r" :20},
        {"r" :24, "g" :28},
        {"g" :32, "o" :36},
        {"b" :12, "o" :40},
        {"o" :38, "y" :42},
        {"g" :30, "y" :44},
        {"r" :22, "y" :46},
        {"b" :14, "y" :48},

    ],
    [
        {"w" :1, "r" :17, "g" :27},
        {"w" :3, "g" :25, "o" :35},
        {"w" :5, "b" :11, "o" :33},
        {"w" :7, "b" :9, "r" :19},
        {"b" :13, "o" :39, "y" :41},
        {"g" :31, "o" :37, "y" :43},
        {"r" :23, "g" :29, "y" :45},
        {"b" :15, "r" :21, "y" :47},
    ]
]

opposite_pieces_color = {
                    'w':'y',
                    'y':'w',
                    'b':'g',
                    'g':'b',
                    'r':'o',
                    'o':'y'
                    }
opposite_pices_number = {
                        49:54,
                        54:49,
                        50:52,
                        52:50,
                        51:53,
                        53:51
                        }
center_colors = {49:'w',50:'b',51:'r',52:'g',53:'o',54:'y'}

def correct_centers(cube_colors):
    for piece in opposite_pices_number:
        '''
        print('')
        print('------')
        print('piece',piece)
        print('opposite_pices_number[piece]-1',opposite_pices_number[piece]-1)
        print('cube_colors[opposite_pices_number[piece]-1]',cube_colors[opposite_pices_number[piece]-1])
        print('opposite_pieces_color[cube_colors[opposite_pices_number[piece]]]',opposite_pieces_color[cube_colors[opposite_pices_number[piece]-1]])
        print('')
        print('piece-1',piece-1)
        print('cube_colors[piece-1]',cube_colors[piece-1])
        print('------')
        print('')
        '''
        
        if cube_colors[piece-1] == opposite_pieces_color[cube_colors[opposite_pices_number[piece]-1]]:
            print('true')
            print(cube_colors[piece-1],opposite_pieces_color[cube_colors[opposite_pices_number[piece]-1]])
        
            
        else:
            print('false')
            print(cube_colors[piece-1],opposite_pieces_color[cube_colors[opposite_pices_number[piece]-1]])
    
def create_color_mapping(cube_colors):
    color_mapping = {}
    for key in center_colors:
        print('triggered')
        color_mapping[cube_colors[key-1]] = center_colors[key]
        print(cube_colors[key-1],':',center_colors[key])
        
        
    print("colormapping : ",color_mapping)
    return color_mapping

def apply_color_mapping(cube_colors,color_mapping):
    new_cube_position = []
    for cube_color in cube_colors:
        new_cube_position.append(color_mapping[cube_color])
    print('new_cube_position : ',new_cube_position)
    return new_cube_position


def stage_1(cube_position_in_colors,constant_pieces_sets_colors_to_numbers) : 
    new_pieces = []
    for constant_pieces_colors_to_numbers in constant_pieces_sets_colors_to_numbers:
        for piece in constant_pieces_colors_to_numbers:
            new_piece = {}
            for sticker in piece:
                new_piece[piece[sticker]] = cube_position_in_colors[piece[sticker]-1]
            
            new_pieces.append(new_piece)
        
    return new_pieces




def stage_2(pieces):
    new_pieces = {}
    for piece in pieces:
        color_set,numbers,color_to_number_dictionary = return_proper_order(piece)  

            
        new_sticker_numbers = constand_invert_pieces_sets_colors[color_set]
        
        for iteration in range(0,len(color_set)):
            piece_location = numbers[iteration]
            piece_sticker_number = new_sticker_numbers[iteration]
            new_pieces[piece_location] = str(piece_sticker_number)
    return new_pieces


def return_proper_order(dictionary):
    colors = ''
    numbers = []
    new_dictionary = {}
    for color in proper_order:
        for key in dictionary:
            if dictionary[key] == color:
                colors += dictionary[key]
                numbers.append(key)
                new_dictionary[color] = key
    return [colors,numbers,new_dictionary]
    
def main():
    #cube_position_in_colors =['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'b', 'b', 'b', 'b', 'g', 'w', 'w', 'w', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'g', 'g', 'r', 'g', 'g', 'g', 'g', 'g', 'y', 'y', 'w', 'y', 'y', 'y', 'y', 'y', 'w', 'o', 'w', 'r', 'w', 'y']
    GetCubeColors.main()
    correct_centers(cube_position_in_colors)
    color_mapping = create_color_mapping(cube_position_in_colors)
    cube_position_in_colors = apply_color_mapping(cube_position_in_colors,color_mapping)
    print('_______stage1________')    
    new_pieces = stage_1(cube_position_in_colors,constant_pieces_sets_colors_to_numbers)
    print(new_pieces)
    print('________stage1 end______')
    print('========================')
    print('________stage2 start_____')
    new_pieces = stage_2(new_pieces)
    print(new_pieces)
    return new_pieces

        

        
main()
    
        
        
        