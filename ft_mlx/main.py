# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_mlx.py                                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/26 16:38:17 by varandri            #+#    #+#            #
#   Updated: 2026/05/26 16:43:02 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from mlx import Mlx, c_void_p
from typing import Any


class PyMlx:
    def __init__(self) -> None:
        self._mlx: Mlx = Mlx()
        self._ptr: c_void_p = self._mlx.mlx_init()

    def get_ptr(self) -> c_void_p:
        return self._ptr

    def new_window(self, width: int, height: int, title: str) -> c_void_p:
        return self._mlx.mlx_new_window(
            self._ptr, width, height, title
        )

    def clear_window(self, win: c_void_p) -> int:
        return self._mlx.mlx_clear_window(
            self._ptr,
            win
        )

    def destroy_window(self, win: c_void_p) -> int:
        return self._mlx.mlx_destroy_window(
            self._ptr, win
        )

    def get_screen_size(self) -> tuple[Any, int, int]:
        return self._mlx.mlx_get_screen_size(
            self._ptr
        )

    def put_str(
        self, win: c_void_p, x: int, y: int, color: int, string: str
    ) -> int:
        return self._mlx.mlx_string_put(
            self._ptr, win, x, y, color, string
        )

    def put_pixel(
            self, win: c_void_p, x: int, y: int, color: int
    ) -> int:
        return self._mlx.mlx_pixel_put(
            self._ptr, win, x, y, color
        )

    def new_image(self, width: int, height: int) -> c_void_p:
        self._mlx.mlx_mouse_get_pos
        return self._mlx.mlx_new_image(
            self._ptr, width, height
        )

    def release(self) -> int:
        return self._mlx.mlx_release(
            self._ptr
        )
