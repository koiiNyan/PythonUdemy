# Create a function that calculates acceleration given initial velocity v1,
# final velocity v2, start time t1, and end time t2.


def acceleration(v1, v2, t1, t2):
    velocity = v2 - v1
    time = t2 - t1
    acc = velocity / time
    return acc


print(acceleration(0, 10, 0, 20))
