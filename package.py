name = "pip"

version = "20.1.1"

authors = [
    "Chris Jerdonek",
    "Donald Stufft"
]

description = \
    """
    The PyPA recommended tool for installing Python packages.
    """

requires = [
    "cmake-3+",
    "python-2.7+<3"
]

variants = [
    ["platform-linux"]
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "pip-{version}".format(version=str(version))

def commands():
    env.PYTHONPATH.append("{root}")
