import os
import sys
import asyncio
from .runner import Runner


def cb_mkimage():
    run = Runner(os.path.expanduser("~/cb"))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run.build_image(*sys.argv[1:]))


def cb():
    run = Runner(os.path.expanduser("~/cb"))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run.run(*sys.argv[1:]))
