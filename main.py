# _*_coding:utf-8_*_

import inspect
import subprocess
import asyncio
from concurrent.futures import ProcessPoolExecutor
from threading import Semaphore
import traceback

lock = Semaphore(2)

func = inspect.getmembers(traceback, inspect.isfunction)
builtins = inspect.getmembers(traceback, inspect.isbuiltin)

func.extend(builtins)

[print(item[0]) for item in func]


