from entity.entity import Entity


class Ghost(Entity):
    def __init__(self, location, image):
        Entity.__init__(self, location, image)

        self.vulnerable = False


def update_ghosts(ghosts):
    for ghost in ghosts:
        ghost.move()
