import sys
import asyncio
from .runner import Runner


def cb():
    run = Runner()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run.run(*sys.argv[1:]))
