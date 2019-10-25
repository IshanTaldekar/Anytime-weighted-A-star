import math
from Node import Node
from Open import Open
import copy

def calculate_hueristic(start, goal):
    heuristic = abs(start[0]-goal[0])+abs(start[1]-goal[1])
    return heuristic


def estimate(start_state, goal_state):
    heuristic = 0
    for tile in goal_state:
        if(start_state[tile] != goal_state[tile] and tile != ' '):
            heuristic += calculate_hueristic(start_state[tile], goal_state[tile])
    return heuristic

def retrace_path(start_node, node):
    path = []
    while(not(node == start_node)):
        path.append(node.state)
        node = node.parent
    path.append(node.state)
    return path

def print_path(path, goal):
    path_length = len(path)-1
    total_objects = len(goal)
    dim = int(math.sqrt(total_objects))
    possible_state_dim = []

    for x in range(dim):
        for y in range(dim):
            possible_state_dim.append((x, y))

    counter = 0
    print('\n\n')
    while(path_length>=0):
        if(counter == 0):
            print('Start state: ')
            print('-----------')
        elif(path_length == 0):
            print('Goal state: ')
            print('-----------')
        else:
            print('Move '+str(counter)+':')
            print('-----------')
        state = path[path_length]
        for location_tuple in possible_state_dim:
            if(location_tuple[0] != 0 and location_tuple[1]==0):
                print('\n')
            for key in state.keys():
                if(state[key]==location_tuple):
                    if(key == ' '):
                        print('X', end='\t')
                    else:
                        print(str(key), end='\t')
        print('\n\n')
        counter+=1
        path_length-=1
    print('Total Moves: ', len(path)-1)

def get_new_states(node):
    legal_moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    total_objects = len(node.state)
    dimension = int(math.sqrt(total_objects))
    space_state = node.state[' ']
    possible_moves = []
    for move in legal_moves:
        new_space_location = (space_state[0]+move[0], space_state[1]+move[1])
        if((new_space_location[0]>=dimension or new_space_location[0]<0) or (new_space_location[1]>=dimension or new_space_location[1]<0)):
            continue
        possible_moves.append(new_space_location)
    tiles = node.state.keys()
    potential_states = []
    if(possible_moves == []):
        return None
    for tile in tiles:
        new_state = copy.deepcopy(node.state)
        for move in possible_moves:
            new_state[tile]
            move
            if(move == new_state[tile]):
                new_state[' '] = new_state[tile]
                new_state[tile] = space_state
                potential_states.append(new_state)
    return potential_states

def astar(start, goal, movement_cost=1):
    
    start_node = Node(start, estimate(start, goal))
    goal_node = Node(goal, 0, None, -1)
    open_list = Open()

    closed_list = {}
    open_list.insert(start_node)

    while(len(open_list)>0):
        print('Astar is expanding a node')
        current_node = open_list.next()
        if(current_node == goal_node):
            solution = retrace_path(start_node, current_node)
            #print_path(solution, goal)
            return solution

        closed_list[hash(str(current_node.state))] = current_node
        new_states = get_new_states(current_node)

        if(new_states != None):
            pass

        for new_state in new_states:
            neighbor_node = Node(new_state, estimate(new_state, goal), current_node, current_node.g_cost+movement_cost)
            output = open_list.test_membership(neighbor_node)

            if (output[0]):
                node = output[1]

                if((neighbor_node < node)[0]):
                    node.update(current_node, neighbor_node.g_cost, neighbor_node.h_cost)

            elif(hash(str(neighbor_node.state)) in closed_list):
                node = closed_list.get(hash(str(current_node.state)))

                if ((neighbor_node < node)[0]):
                    closed_list.pop(hash(str(current_node.state)))
                    open_list.insert(neighbor_node)

            else:
                open_list.insert(neighbor_node)

    print('PATH NOT FOUND')
    return None


def weighted_astar(start, goal, hueristic_weight=1, movement_cost=1):

    start_node = Node(start, estimate(start, goal)*hueristic_weight)
    goal_node = Node(goal, 0, None, -1)
    open_list = Open()
    closed_list = {}
    open_list.insert(start_node)

    while(len(open_list)>0):
        current_node = open_list.next()

        if(current_node == goal_node):
            solution = retrace_path(start_node, current_node)
            #print_path(solution, goal)
            return solution

        closed_list[hash(str(current_node.state))] = current_node
        new_states = get_new_states(current_node)

        if(new_states != None):
            pass

        for new_state in new_states:
            neighbor_node = Node(new_state, weighted_estimate(new_state, goal, hueristic_weight, movement_cost), current_node, current_node.g_cost+movement_cost)
            output = open_list.test_membership(neighbor_node)

            if (output[0]):
                node = output[1]

                if((neighbor_node < node)[0]):
                    node.update(current_node, neighbor_node.g_cost, neighbor_node.h_cost)

            elif(hash(str(neighbor_node.state)) in closed_list):
                node = closed_list.get(hash(str(neighbor_node.state)))

                if ((neighbor_node < node)[0]):
                    closed_list.pop(hash(str(neighbor_node.state)))
                    open_list.insert(neighbor_node)

            else:
                open_list.insert(neighbor_node)

    print('PATH NOT FOUND')
    return None

def anytime_weighted_astar(start, goal, hueristic_weight, movement_cost=1):

    start_node = Node(start, estimate(start, goal, movement_cost), h_cost2=estimate(start, goal)*hueristic_weight)
    goal_node = Node(goal, 0, None, -1)
    open_list = Open()
    closed_list = {}
    open_list.anytime_insert(start_node)
    incumbent_node = None
    incumbent_flag = 0

    while(len(open_list)>0):
        try:
            print('Anytime Astar is expanding a node')
            current_node = open_list.next()
            
            if(incumbent_flag == 0):
                pass
            
            elif((current_node<incumbent_node)[2]):
                pass
            
            else:
                continue

            if(current_node == goal_node):
                incumbent_flag = 1
                incumbent_node = current_node
            
            closed_list[hash(str(current_node.state))] = current_node
            neighbors = get_new_states(current_node)

            if(neighbors == None):
                continue

            for neighbor in neighbors:
                neighbor_node = Node(neighbor, estimate(neighbor, goal, movement_cost), current_node, current_node.g_cost+movement_cost, (estimate(neighbor, goal))*hueristic_weight)

                if(incumbent_flag == 0):
                    pass

                elif((neighbor_node<incumbent_node)[2]):
                    pass

                else:
                    continue

                output = open_list.test_membership(neighbor_node)

                if (output[0]):
                    node = output[1]

                    if((neighbor_node < node)[0]):
                        node.update(current_node, neighbor_node.g_cost, neighbor_node.h_cost, neighbor_node.h_cost2)

                elif(hash(str(neighbor_node.state)) in closed_list):
                    node = closed_list.get(hash(str(neighbor_node.state)))

                    if ((neighbor_node < node)[0]):
                        open_list.anytime_insert(neighbor_node)
                        closed_list.pop(hash(str(neighbor_node.state)))

                else:
                    open_list.anytime_insert(neighbor_node)

        except KeyboardInterrupt:
            break

    if(len(open_list)==0):
        error = 0
    else:
        error = incumbent_node.f_cost-open_list.next().f_cost

    path = retrace_path(start_node, incumbent_node)
    #print_path(path, goal)
    return (path, error)
