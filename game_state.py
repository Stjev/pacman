from entity.ghost import update_ghosts
import ctypes


def update_game_state(pacman, ghosts):
    update_ghosts(pacman.location, ghosts)

    for ghost in ghosts:
        if ghost.location == pacman.location:
            ctypes.windll.user32.MessageBoxW(
                0, "You lost :)", "Game over", 1)
            exit(0)
