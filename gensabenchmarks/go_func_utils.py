import sys
import contextlib
import inspect
import gensabenchmarks.go_benchmark_functions as gbf

def goclass():
    """
    Generator to get global optimization test classes/functions
    defined in SciPy
    """
    bench_members = inspect.getmembers(gbf, inspect.isclass)
    benchmark_functions = [item for item in bench_members if
            issubclass(item[1], gbf.Benchmark)]
    for name, klass in benchmark_functions:
        yield (name, klass)


class DummyFile(object):
    def write(self, x): pass
    def flush(self): pass

@contextlib.contextmanager
def nostdout():
    save_stdout = sys.stdout
    save_stderr = sys.stderr
    sys.stdout = DummyFile()
    sys.stderr = DummyFile()
    yield
    sys.stdout = save_stdout
    sys.stderr = save_stderr
