def relationship_status(from_member, to_member,social_graph):
    from_user_following = social_graph[from_member]["following"]
    to_user_following = social_graph[to_member]["following"]
    
    if from_member in to_user_following and to_member in from_user_following:
        message = "friends" 
    elif to_member in from_user_following:
        message = "follower"
    elif from_member in to_user_following: 
        message = "followed by" 
    else: 
        message = "no relationship"

    return message



def tic_tac_toe(board):
    board_size = len(board)

#horizontal
    for row in board:
        if row.count("X") == board_size:
            return "X"
        elif row.count ("O")== board_size:
            return "O"

#vertical
    number_x = 0
    number_o = 0
 
    for col in range(board_size):
        for row in range(board_size):
            if board[row][col] == "X":
                number_x += 1
            if board[row][col] == "O":
                number_o += 1
        if number_x == board_size:
            return "X"
        elif number_o == board_size:
            return "O"
        number_x = 0
        number_o = 0

#diagonal top left to bottom right
    number_x = 0
    number_o = 0
 
    for row in range(board_size):
        if board[row][row] == "X":
            number_x += 1
        if board[row][row] == "O":
            number_o += 1
        if number_x == board_size:
            return "X"
        elif number_o == board_size:
            return "O"

#diagonal top right to bottom left
    number_x = 0
    number_o = 0
    for row in range(board_size):
        if board[row][board_size-1-row] == "X":
            number_x += 1
        if board[row][board_size-1-row] == "O":
            number_o += 1
        if number_x == board_size:
            return "X"
        elif number_o == board_size:
            return "O"
    
    return "NO WINNER"



def eta(first_stop, second_stop, route_map):
    travel_time = 0
    current_stop = first_stop
    visited = set()  

    while current_stop != second_stop:
        for (from_stop, to_stop) in route_map:
            if from_stop == current_stop and (current_stop, to_stop) not in visited:
                travel_time += route_map[(from_stop, to_stop)]["travel_time_mins"]
                visited.add((current_stop, to_stop))
                current_stop = to_stop
                break

    return travel_time











