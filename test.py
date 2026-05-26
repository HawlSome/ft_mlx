#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   test.py                                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: varandri <varandri@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/05/26 23:38:06 by varandri            #+#    #+#            #
#   Updated: 2026/05/26 23:42:52 by varandri           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ft_mlx import PyMlx
from time import sleep


if __name__ == "__main__":
    mlx = PyMlx()
    win = mlx.new_window(800, 800, "Joda")
    sleep(5)
    mlx.destroy_window(win)
    mlx.release()
