# -*- coding: utf-8 -*-
from maya import cmds
from maya.common.ui import LayoutManager


__TOOL_NAME = 'Sample Tool01'
__BUTTON_NAME = 'Print Hello!!'


def print_hello():
    print('Hello!!')


def show():
    if cmds.window(__TOOL_NAME, ex=True):
        cmds.deleteUI(__TOOL_NAME)

    cmds.window(__TOOL_NAME, title=__TOOL_NAME, mxb=False, mnb=False)
    with LayoutManager(cmds.columnLayout(adj=True)):
        cmds.button(__BUTTON_NAME,
                    l=__BUTTON_NAME,
                    c=lambda *args: print_hello())

    cmds.showWindow()

# startup command
# from SampleTool01.sample01 import show
# show()
