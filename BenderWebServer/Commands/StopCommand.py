# -*- coding: utf-8 -*-
from Commands.Command import command
from Commands.Returncodes import TIMEOUT

def stop_cmd(connection):
    answer = command(connection, b"0\n", 0)
    return str(answer)
    