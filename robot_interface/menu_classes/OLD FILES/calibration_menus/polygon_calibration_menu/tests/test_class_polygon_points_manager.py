import sys
from os import path

#adds the file to test to the working directory
current_directory = sys.path[0]
parent_directory = path.dirname(current_directory)
sys.path.append(parent_directory)

from class_polygon_points_manager import *


def assert_equals(expected, actual):
    if (expected != actual):
        raise Exception ("expected :" , expected, " | actual :", actual)


def test_init():
    instance = polygon_points_manager()
    expected = 'u'
    actual = instance.current_side
    assert_equals(expected, actual)

    expected = 1
    actual =  instance.current_address 
    assert_equals(expected, actual)
        
    original_polygons_state = {'u':[[], [],  [],  [],  [],  [],  [],  [],  []],
                            'f':[[], [],  [],  [],  [],  [],  [],  [],  []],
                            'r':[[], [],  [],  [],  [],  [],  [],  [],  []], 
                            'd':[[], [],  [],  [],  [],  [],  [],  [],  []],
                            'l':[[], [],  [],  [],  [],  [],  [],  [],  []],
                            'b':[[], [],  [],  [],  [],  [],  [],  [],  []]}

    expected = original_polygons_state
    actual =  instance.original_polygons_state 
    assert_equals(expected, actual)
        
    expected = original_polygons_state
    actual = instance.polygons
    assert_equals(expected, actual)
        
    expected = 'ufrdbl'
    actual = instance.side_order
    assert_equals(expected, actual)
        

def test_get_current_polygon_points():
    instance = polygon_points_manager()
    point = [100,100]
    instance.add_point_to_current_polygon(point)

    expected = [[100,100]]
    actual = instance.get_current_polygon_points()
    assert_equals(expected, actual)


def test_get_all_polygons():
    instance = polygon_points_manager()
    points = [[0,0], [100, 100], [50, 50], [0,0]]

    instance.add_point_to_current_polygon(points[0])
    instance.add_point_to_current_polygon(points[1])

    instance.set_current_polygon_to_next()
    instance.add_point_to_current_polygon(points[2])
    instance.add_point_to_current_polygon(points[3])
    expected =  {'b': [[], [], [], [], [], [], [], [], []], 
                 'd': [[], [], [], [], [], [], [], [], []], 
                 'f': [[], [], [], [], [], [], [], [], []], 
                 'l': [[], [], [], [], [], [], [], [], []], 
                 'r': [[], [], [], [], [], [], [], [], []], 
                 'u': [[[0, 0], [100, 100]], [[50, 50], [0, 0]], [], [], [], [], [], [], []]}
    actual = instance.get_all_polygons()
    assert_equals(expected, actual)

def test_add_point_to_current_polygon():
    instance = polygon_points_manager()
    point = [100,100]
    instance.add_point_to_current_polygon(point)

    expected = [[100,100]]
    actual = instance.polygons[instance.current_side][instance.current_address - 1]
    assert_equals(expected, actual)

def test_remove_point_from_current_polygon():
    instance = polygon_points_manager()
    point = [100,100]
    instance.add_point_to_current_polygon(point)
    instance.remove_point_from_current_polygon()
    expected = []
    actual = instance.polygons[instance.current_side][instance.current_address - 1]
    assert_equals(expected, actual)

def test_reset_current_polygon():
    instance = polygon_points_manager()
    points = [[0,0], [100, 100]]

    instance.add_point_to_current_polygon(points[0])
    instance.add_point_to_current_polygon(points[1])
    instance.reset_current_polygon()
    expected = []
    actual = instance.polygons[instance.current_side][instance.current_address - 1]
    assert_equals(expected, actual)

def test_set_current_polygon():
    instance = polygon_points_manager()
    instance.set_current_polygon('f', 6)

    expected = 'f'
    actual = instance.current_side
    assert_equals(expected, actual)

    expected = 6
    actual = instance.current_address
    assert_equals(expected, actual)

def test_set_current_polygon_to_next():
    instance = polygon_points_manager()
    instance.set_current_polygon_to_next()

    expected = 'u'
    actual = instance.current_side
    assert_equals(expected, actual)

    expected = 2
    actual = instance.current_address
    assert_equals(expected, actual)

def test_set_current_side_to_next():
    instance = polygon_points_manager()
    instance.set_current_side_to_next()

    expected = 'f'
    actual = instance.current_side
    assert_equals(expected, actual)

    expected = 1
    actual = instance.current_address
    assert_equals(expected, actual)

def test_set_current_polygon_to_previous():
     instance = polygon_points_manager()
     instance.set_current_polygon_to_previous() 
     expected = 'l'
     actual = instance.current_side
     assert_equals(expected, actual) 
     expected = 9
     actual = instance.current_address
     assert_equals(expected, actual)

def test_set_current_side_to_previous():
    instance = polygon_points_manager()
    instance.set_current_side_to_previous()

    expected = 'l'
    actual = instance.current_side
    assert_equals(expected, actual)

    expected = 1
    actual = instance.current_address
    assert_equals(expected, actual)




def run_tests():
    print('started')
    test_init()
    test_get_current_polygon_points()
    test_get_all_polygons()
    test_add_point_to_current_polygon()
    test_remove_point_from_current_polygon()
    test_reset_current_polygon()
    test_set_current_polygon()
    test_set_current_polygon_to_next()
    test_set_current_side_to_next()
    test_set_current_polygon_to_previous()
    test_set_current_side_to_previous()
    print('done')

run_tests()