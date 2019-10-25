class Node():
    def __init__(self, current_state, h_cost, parent=None, g_cost=0, h_cost2=None):
        self.state = current_state
        self.parent = parent
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.f_cost = g_cost + h_cost
        self.h_cost2 = h_cost2
        if(h_cost2 != None):
            self.f_cost2 = g_cost + h_cost2
        else:
            self.f_cost2 = None
        

    def update(self, parent, g_cost, h_cost, h_cost2=None):
        self.parent = parent
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.f_cost = self.g_cost + self.h_cost
        if(self.h_cost2 != None):
            self.f_cost2 = self.g_cost + self.h_cost2

    def __eq__(self, node):
        for tile in node.state.keys():
            if(self.state[tile]!=node.state[tile]):
                return False
        return True
                

    def __lt__(self, node):
        return (self.g_cost<node.g_cost, self.h_cost<node.h_cost, self.f_cost<node.f_cost)
    
    def get_empty_tile(self):
        pass