import turtle


def perform_switch_case(state, t, turn):
    x = round(t.position()[0])
    y = round(t.position()[1])
    num_turns = 1  # Всего 1 виток

    if state == "INIT":
        if True:
            state = "RIGHT1"
            t.setheading(0)
            return state, turn
        return state, turn

    if state == "RIGHT1":
        t.forward(5)
        if x >= 300:
            state = "UP1"
            t.setheading(90)
            return state, turn
        return state, turn

    if state == "UP1":
        t.forward(5)
        if y >= 50:
            state = "LEFT1"
            t.setheading(180)
            return state, turn
        return state, turn

    if state == "LEFT1":
        t.forward(5)
        if x <= 0:
            state = "UP2"
            t.setheading(90)
            return state, turn
        return state, turn

    if state == "UP2":
        t.forward(5)
        if y >= 100:
            state = "RIGHT2"
            t.setheading(0)
            return state, turn
        return state, turn

    if state == "RIGHT2":
        t.forward(5)
        if x >= 300:
            state = "UP3"
            t.setheading(90)
            return state, turn
        return state, turn

    if state == "UP3":
        t.forward(5)
        if y >= 150:
            state = "LEFT2"
            t.setheading(180)
            return state, turn
        return state, turn

    if state == "LEFT2":
        t.forward(5)
        if x <= 0:
            state = "UP4"
            t.setheading(90)
            return state, turn
        return state, turn

    if state == "UP4":
        t.forward(5)
        if y >= 200:
            if turn >= num_turns:  # Выход после завершения витка
                state = "STOP"
                return state, turn
            state = "RIGHT1"
            turn = turn + 1
            t.setheading(0)
            return state, turn
        return state, turn

    return state, turn


def draw():
    start_state = "INIT"
    end_state = "STOP"
    curr_state = start_state
    t = turtle.Turtle()
    t.speed(5)
    turn = 0

    while curr_state != end_state:
        curr_state, turn = perform_switch_case(curr_state, t, turn)
    turtle.done()


if __name__ == "__main__":
    draw()