#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   main.py                                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/26 16:38:17 by varandri            #+#    #+#            #
#   Updated: 2026/05/29 15:43:35 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from .mlx import Mlx, c_void_p
from typing import Any, Callable


class PyMlx:
    def __init__(self) -> None:
        self._mlx: Mlx = Mlx()
        self._ptr: c_void_p = self._mlx.mlx_init()

    def set_ptr(self, ptr: c_void_p) -> None:
        self._ptr = ptr

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

    def get_data_addr(
        self, image: c_void_p
    ) -> tuple[Any, int, int, int]:
        return self._mlx.mlx_get_data_addr(image)

    def put_image_to_window(
        self, win: c_void_p, img: c_void_p, x: int, y: int
    ) -> int:
        return self._mlx.mlx_put_image_to_window(
            self._ptr, win, img, x, y
        )

    def png_file_to_image(self, path: str) -> tuple[Any, int, int]:
        return self._mlx.mlx_png_file_to_image(self._ptr, path)

    def xpm_file_to_image(self, path: str) -> tuple[Any, int, int]:
        return self._mlx.mlx_xpm_file_to_image(self._ptr, path)

    def key_hook(
        self, win: c_void_p, callback: Callable[..., Any],
        params: list[Any] = [None]
    ) -> Any:
        return self._mlx.mlx_key_hook(win, callback, *params)

    def mouse_hook(
        self, win: c_void_p, callback: Callable[..., Any],
        params: list[Any] = [None]
    ) -> Any:
        return self._mlx.mlx_mouse_hook(win, callback, *params)

    def expose_hook(
        self, win: c_void_p, callback: Callable[..., Any], params: list[Any]
    ) -> Any:
        return self._mlx.mlx_expose_hook(win, callback, *params)

    def loop_hook(
            self, callback: Callable[[list[Any]], Any], params: list[Any]
    ) -> Any:
        return self._mlx.mlx_loop_hook(self._ptr, callback, params)

    def loop(self) -> int:
        return self._mlx.mlx_loop(self._ptr)

    def hook(
        self, win: c_void_p, x_event: int, x_mask: int,
        callback: Callable[..., Any], params: list[Any] = [None]
    ) -> Any:
        return self._mlx.mlx_hook(win, x_event, x_mask, callback, *params)

    # def mass_loop_hook(
    #     self, callbacks: list[Callable[..., Any]],
    #     params: list[list[Any]]
    # ) -> Any:
    #     ret_values: list[Any] = []
    #     if len(callbacks) != len(params):
    #         raise ValueError(
    #             "Missing either one of the following values: "
    #             " callback, params"
    #         )
    #     x: int = len(callbacks)
    #     for i in range(x):
    #         ret_values.append(
    #             self.loop_hook(callbacks[i], params[i])
    #         )
    #     return ret_values

    def mouse_hide(self) -> int:
        return self._mlx.mlx_mouse_hide(self._ptr)

    def mouse_show(self) -> int:
        return self._mlx.mlx_mouse_show(self._ptr)

    def mouse_move(self, x: int, y: int) -> int:
        return self._mlx.mlx_mouse_move(self._ptr, x, y)

    def mouse_get_pos(self, win: c_void_p) -> tuple[Any, int, int]:
        return self._mlx.mlx_mouse_get_pos(win)

    def key_autorepeatoff(self) -> int:
        return self._mlx.mlx_do_key_autorepeatoff(self._ptr)

    def key_autorepeaton(self) -> int:
        return self._mlx.mlx_do_key_autorepeaton(self._ptr)

    def sync(self, cmd: Any, ptr: c_void_p) -> int:
        return self._mlx.mlx_sync(self._ptr, cmd, ptr)

    def global_sync(self) -> int:
        return self._mlx.mlx_do_sync(self._ptr)

    def destroy_image(
        self, img: c_void_p
    ) -> int:
        return self._mlx.mlx_destroy_image(self._ptr, img)

    def destroy_window(self, win: c_void_p) -> int:
        return self._mlx.mlx_destroy_window(
            self._ptr, win
        )

    def loop_exit(self) -> int:
        return self._mlx.mlx_loop_exit(self._ptr)

    def release(self) -> int:
        return self._mlx.mlx_release(
            self._ptr
        )
