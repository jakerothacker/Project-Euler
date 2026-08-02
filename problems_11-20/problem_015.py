#starting at the top left corrner how mamny ways are there to get to the bottom right moving only right and down in a 20x20 grid

def n_x_n_grid_num_of_routs(n):
    endpoint = (n,n)
    x=0
    y=1
    location_dict = {(0,0):1}
    distance_from_start = 0
    while distance_from_start < n*2:
        
        for loc in list(location_dict):
            loc_num = location_dict.pop(loc)
            if loc[x]+1 <= endpoint[x]:
                if (loc[x]+1,loc[y]) in location_dict:
                    location_dict[(loc[x]+1,loc[y])] += loc_num
                else:
                    location_dict[(loc[x]+1,loc[y])] = loc_num
            if loc[y]+1 <= endpoint[y]:
                if (loc[x],loc[y]+1) in location_dict:
                    location_dict[(loc[x],loc[y]+1)] += loc_num
                else:
                    location_dict[(loc[x],loc[y]+1)] = loc_num


        distance_from_start +=1


    return(location_dict[n,n])


print(n_x_n_grid_num_of_routs(20))