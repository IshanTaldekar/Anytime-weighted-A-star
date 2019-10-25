import numpy as np 
import matplotlib.pyplot as plt

def process_map(map):
    x_dim = len(map)
    y_dim = len(map[0])
    free_x = []
    free_y = []
    occupied_x = []
    occupied_y = []
    for map_x in range(x_dim):
        for map_y in range(y_dim):
            if(map[map_x][map_y]==' '):
                free_x.append(map_x)
                free_y.append(map_y)
                continue
            if(map[map_x][map_y]=='#'):
                occupied_x.append(map_x)
                occupied_y.append(map_y)
    return free_x, free_y, occupied_x, occupied_y

def visualize_predefined_map_and_path(map, path, image_number=None, output_filename=None):
    if(path == None):
        return 0
    x_dims = len(map)
    y_dims = len(map[0])

    path_y, path_x = zip(*path)
    free_y, free_x, occupied_y, occupied_x = process_map(map)
    plt.scatter(free_x, free_y, c="purple", alpha=0.1)
    plt.scatter(occupied_x, occupied_y, c="black", alpha=0.65)
    plt.plot(path_x, path_y, '-go', alpha=0.3)
    plt.scatter(path_x[0], path_y[0], c="red", alpha=1)
    plt.scatter(path_x[-1], path_y[-1], c="blue", alpha=1)
    plt.xticks(np.arange(0, y_dims+1, 2))
    plt.yticks(np.arange(0, x_dims+1, 2))
    plt.gca().invert_yaxis()
    if(image_number == None):
        plt.savefig('A-Star-Ouput'+'.jpg')
    elif(image_number == -1):
        pass
    elif(image_number == -2):
        user_input = input("What name would you like to save this plot under?\n")
        plt.savefig(user_input+'.jpg')
    elif(image_number == -3):
        image_number=np.random.randint(100, 1000)
        plt.savefig('A-Star-Ouput'+str(image_number)+'.png')
    elif(image_number==-4 and output_filename != None):
        plt.savefig(output_filename+'.png')
    else:
        plt.savefig('A-Star-Ouput'+str(image_number)+'.png')
    plt.show()

def commandline_output(map, path, image_number=None, output_filename=None):
    if(path == None):
        return 0
    plt.figure,
    x_dims = len(map)
    y_dims = len(map[0])
    path_y, path_x = zip(*path)
    free_y, free_x, occupied_y, occupied_x = process_map(map)
    plt.scatter(free_x, free_y, c="purple", alpha=0.1)
    plt.scatter(occupied_x, occupied_y, c="black", alpha=0.65)
    plt.plot(path_x, path_y, '-go', alpha=0.3)
    plt.scatter(path_x[0], path_y[0], c="red", alpha=1)
    plt.scatter(path_x[-1], path_y[-1], c="green", alpha=1)
    plt.xticks(np.arange(0, y_dims+1, 2))
    plt.yticks(np.arange(0, x_dims+1, 2))
    plt.gca().invert_yaxis()
    plt.savefig(output_filename+'.png')