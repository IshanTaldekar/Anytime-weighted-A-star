from Node import Node
from Astar import weighted_astar, astar, anytime_weighted_astar
import time

            
start = {'5':(0, 0), '1':(0, 1), '7':(0, 2), '2':(0, 3), ' ':(1, 0), '11':(1, 1), '10':(1, 2), '3':(1, 3), '6':(2, 0), '14':(2, 1), '8':(2, 2), '4':(2, 3), '9':(3, 0), '13':(3, 1), '15':(3, 2), '12':(3, 3)}
goal = {'1':(0, 0), '2':(0, 1), '3':(0, 2), '4':(0, 3), '5':(1, 0), '6':(1, 1), '7':(1, 2), '8':(1, 3), '9':(2, 0), '10':(2, 1), '11':(2, 2), '12':(2, 3), '13':(3, 0), '14':(3, 1), '15':(3, 2), ' ':(3, 3)}

regular_a_star_time=weighted_astar_time=anytime_weighted_astar_time=0
hueristic_weight = 1.4,

timer_start = time.time()
astar(start, goal)
timer_stop = time.time()
regular_a_star_time = timer_stop-timer_start
print('Regular A* execution time: ', regular_a_star_time)
'''
timer_start = time.time()
weighted_astar(start, goal)
timer_stop = time.time()
weighted_astar_time = timer_stop-timer_start
print('Weighted A* execution time: ', weighted_astar_time)
'''
timer_start = time.time()
anytime_weighted_astar(start, goal, hueristic_weight)
timer_stop = time.time()
anytime_weighted_astar_time = timer_stop-timer_start
print('Anytime Weighted A* execution time: ', anytime_weighted_astar_time)

state=[8,10,9,11,14,1,7,15,13,4,0,12,6,2,3,5] #moves 57
state=[5,1,7,2,0,11,10,3,6,14,8,4,9,13,15,12]