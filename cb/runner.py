import os
import asyncio
from .utils import copy_source
from aiodocker.docker import Docker


class Runner:
    def __init__(self):
        self.docker = Docker()

    @asyncio.coroutine
    def run(self, dsc, *args):
        with copy_source(dsc) as (d, srcdir):
            container = yield from self.docker.containers.create({
                "Cmd": ["/build/%s" % (os.path.basename(dsc))] + list(args),
                "Image": "debian-devel:unstable",
                "AttachStdin": True,
                "AttachStdout": True,
                "AttachStderr": True,
                "ExposedPorts": [],  # None!
                "Volumes": {srcdir: "/build/"},
                "Tty": True,
                "OpenStdin": False,
                "StdinOnce": False
            })
            yield from container.start({
                "Binds": ["%s:/build/" % (srcdir)],
                "Privileged": False,
                "PortBindings": [],
                "Links": [],
            })
            yield from container.wait()
            print("Finished")
            # data = yield from container.copy("/fnord")
            # print([data.extractfile(x.name).read() for x in data.members])
