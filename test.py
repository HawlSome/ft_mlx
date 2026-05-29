#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   test.py                                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/26 23:38:06 by varandri            #+#    #+#            #
#   Updated: 2026/05/29 15:44:05 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ft_mlx import PyMlx, c_void_p
from time import sleep
from typing import Any


class Counter:
    count = 0


def draw_pixel(
        color_value: int, start_x: int, start_y: int,
        line_width: int, line_height: int,
        grid_width: int, img: memoryview
) -> None:
    color: bytes = color_value.to_bytes(4)
    for y in range(start_y, start_y + line_height):
        for x in range(start_x, start_x + line_width):
            pixel = y * grid_width + x

            for i in range(4):
                img[pixel * 4 + i] = color[i]


def fill_cell(
        color: int, col: int, row: int,
        grid_width: int, img: memoryview
) -> None:
    """Function to fill a cell in a certain coordinate with color.

    Args:
        col (int): the colum of the cell to fill a color with.
        row (int): the row of the cell to fill a color with.
        color (int): the color to fill the chosen cell with.

    Returns:
        None.
    """
    draw_pixel(
        color,
        start_x=col * grid_width,
        start_y=row * grid_width,
        line_height=grid_width,
        line_width=grid_width,
        grid_width=grid_width,
        img=img
    )


def loop_hooks(mlx: PyMlx, win: c_void_p, foreground: c_void_p, background: c_void_p) -> None:
    lst: list[str] = ["->", "-->", "--->", "---->"]
    counter = Counter()

    def loop(params: list[Any]) -> None:
        lst: list[str]
        counter: Counter
        lst, counter = params
        sleep(0.1)

        val, _, _, _ = mlx.get_data_addr(foreground)
        fill_cell(0x00FF00FF, 0, 0, 800, val)
        draw_pixel(0x00000000, 0, 120, 120, 120, 800, val)

        mlx.clear_window(win)
        mlx.put_image_to_window(win, background, 0, 0)
        # mlx.put_image_to_window(win, foreground, 0, 0)
        mlx.put_str(win, 20, 20, 0x000000, lst[counter.count])
        counter.count += 1

        if counter.count == len(lst):
            counter.count = 0

    mlx.loop_hook(loop, [lst, counter])


def hooks(
        mlx: PyMlx, win: c_void_p,
        foreground: c_void_p, background: c_void_p
) -> None:
    def hola(data: None) -> None:
        mlx.put_image_to_window(win, background, 0, 0)
        mlx.put_image_to_window(win, foreground, 0, 0)
        # mlx.put_str(win, 20, 20, 0x000000, "Hola Negro!")

    def joda(data: None) -> None:
        mlx.put_image_to_window(win, background, 0, 0)
        mlx.put_image_to_window(win, foreground, 0, 0)
        # mlx.put_str(win, 20, 20, 0x00000000, "Voahosotra Joda")

    def close_window(data: None) -> None:
        mlx.destroy_window(win)
        mlx.loop_exit()

    def on_key(key: int, data: None) -> None:
        if key == 0xFF1B:
            close_window(data)
        if key == 104:
            mlx.clear_window(win)
            hola(None)
        if key == 106:
            mlx.clear_window(win)
            joda(None)

    mlx.hook(win, 33, 0, close_window)
    mlx.key_hook(win, on_key)
    # mlx.mass_key_hook(win, [on_key, on_h, on_j], [[None], [None], [None]])


# def on_key(key: int, mlx: PyMlx) -> None:
#     if key == 65307:
#         mlx.loop_exit()


if __name__ == "__main__":
    mlx = PyMlx()
    win = mlx.new_window(800, 800, "Joda")
    background = mlx.new_image(800, 800)
    img_value, _, _, _ = mlx.get_data_addr(background)
    fill_cell(0x0000FFFF, 0, 0, 800, img_value)
    mlx.put_image_to_window(win, background, 0, 0)

    foreground = mlx.new_image(800, 800)
    val, _, _, _ = mlx.get_data_addr(foreground)
    fill_cell(0x00FF00FF, 0, 0, 800, val)
    draw_pixel(0x00000000, 0, 120, 120, 120, 800, val)
    # mlx.put_image_to_window(win, foreground, 0, 0)

    # mlx.key_hook(win, on_key, [mlx])
    print("letsgooooooooo")
    hooks(mlx, win, foreground, background)
    loop_hooks(mlx, win, foreground, background)
    mlx.loop()
    mlx.release()
