from locations import Location


def h(current, end):
    return current.manhatten_distance(end)


def g(current, start):
    return h(current, start)


def a_star(start, end):
    location = Location.get_instance()

    open_set = {start}
    came_from = dict()

    gscore = {coord: 100000 for coord in location.get_valid_for_ghosts_coords()}
    fscore = dict(gscore)  # copy of this dict

    gscore[start] = 0
    fscore[start] = h(start, end)

    while len(open_set) > 0:
        # get the coordinate with the lowest value
        current = min(open_set, key=lambda x: fscore[x])

        if current == end:
            return get_first_step(start, came_from, end)

        open_set.remove(current)
        for neighbour in [coord for coord in current.get_neighbours()]:
            tentative_gScore = gscore[current] + 1

            if tentative_gScore < gscore[neighbour]:
                came_from[neighbour] = current
                gscore[neighbour] = tentative_gScore
                fscore[neighbour] = gscore[neighbour] + h(neighbour, end)
                if neighbour not in open_set:
                    open_set.add(neighbour)


def get_first_step(start, came_from, current):
    while came_from[current] != start:
        current = came_from[current]

    return current
