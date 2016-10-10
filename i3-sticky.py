#!/usr/bin/env python3
# vim:ts=4:sw=4:expandtab
import i3ipc
import json

"""
Implements sticky groups, i.e., sticky tiling windows for i3.

A sticky group has a specific single-digit number (0–9). The actual sticky container must be marked with '_sticky_x' where »x« is the number of the sticky group. On each workspace the container should stick to, some placeholder container must exist and be tagged with '_sticky_x_y' where »x« is again the sticky group and »x« some suffix. The suffix will be ignored and can be freely chosen; it is simply required because marks must be unique within i3.

Run this script in the background and the sticky container will be swapped into the placeholder container whenever you switch workspaces.

(C) 2016 Ingo Bürk
Licensed under The MIT License (https://opensource.org/licenses/MIT), see LICENSE.

Requires i3 >= 4.13
"""

def on_workspace_focus(i3, event):
    marks = json.loads(i3.message(i3ipc.MessageType.GET_MARKS, ''))
    sticky_groups = [int(mark[len('_sticky_')]) for mark in marks if len(mark) == len('_sticky_x') and mark.startswith('_sticky_')]

    for group in sticky_groups:
        i3.command('[workspace="__focused__" con_mark="^_sticky_%d_"] swap container with mark _sticky_%d' % (group, group))

if __name__ == '__main__':
    i3 = i3ipc.Connection()
    i3.on('workspace::focus', on_workspace_focus)
    i3.main()
