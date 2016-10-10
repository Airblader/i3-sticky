# i3-sticky

Implements sticky groups, i.e., sticky tiling windows for i3.

A sticky group has a specific single-digit number (0–9). The actual sticky container must be marked with `_sticky_x` where »x« is the number of the sticky group. On each workspace the container should stick to, some placeholder container must exist and be tagged with `_sticky_x_y` where »x« is again the sticky group and »x« some suffix. The suffix will be ignored and can be freely chosen; it is simply required because marks must be unique within i3.

Run this script in the background and the sticky container will be swapped into the placeholder container whenever you switch workspaces.

(C) 2016 Ingo Bürk
Licensed under The MIT License (https://opensource.org/licenses/MIT), see LICENSE.

Requires i3 >= 4.13
