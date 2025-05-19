import os

def from_root(relative_path: str = "") -> str:
    root_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(root_dir, relative_path)
