from contextlib import contextmanager
import tempfile
import shutil
import debian.deb822
import os


@contextmanager
def copy_source(path):
    sourcedir = os.path.dirname(os.path.abspath(path))

    with open(path, 'r') as fd:
        d = debian.deb822.Dsc(fd)

    with tmpdir(suffix='.cb') as temp:
        for file_ in [os.path.join(sourcedir, x['name']) for x in d['Files']]:
            shutil.copy(file_, temp)
        shutil.copy(path, temp)

        try:
            yield (d, temp)
        finally:
            pass


@contextmanager
def tmpdir(*args, **kwargs):
    mdir = tempfile.mkdtemp(*args, **kwargs)
    try:
        yield mdir
    finally:
        shutil.rmtree(mdir)
