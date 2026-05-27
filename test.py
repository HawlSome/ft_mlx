#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   test.py                                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/26 23:38:06 by varandri            #+#    #+#            #
#   Updated: 2026/05/27 11:54:49 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ft_mlx import PyMlx, c_void_p
# from time import sleep
# from typing import Any


def hooks(mlx: PyMlx, win: c_void_p):
    def hola(data: None) -> None:
        mlx.put_str(win, 20, 20, 0xFFFFFF, "Hola Negro!")

    def joda(data: None) -> None:
        mlx.put_str(win, 20, 20, 0xFFFFFF, "Voahosotra Joda")

    def close_window(data: None) -> None:
        mlx.destroy_window(win)
        mlx.loop_exit()

    def on_key(key: int, data: None) -> None:
        if key == 0xFF1B:
            close_window(data)
        if key == 104:
            hola(None)
        if key == 106:
            joda(None)

    mlx.hook(win, 33, 0, close_window, [None])
    mlx.key_hook(win, on_key, [None])
    # mlx.mass_key_hook(win, [on_key, on_h, on_j], [[None], [None], [None]])


# def on_key(key: int, mlx: PyMlx) -> None:
#     if key == 65307:
#         mlx.loop_exit()


if __name__ == "__main__":
    mlx = PyMlx()
    win = mlx.new_window(800, 800, "Joda")

    # mlx.key_hook(win, on_key, [mlx])
    hooks(mlx, win)
    mlx.loop()
    mlx.release()
