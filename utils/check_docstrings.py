from pathlib import Path
import os

package_path = Path('./package_code')

def get_python_files() -> list[Path]:
    python_files: list[Path] = []
    for path, subdirs, files in os.walk(package_path):
        for name in files:
            if name.endswith('.py'):
                python_files.append(Path(path) / name)
    return python_files

if __name__ == '__main__':
    x = get_python_files()
    if x:
        print(x)
        sys.exit(1)
    else:
        print("No Python files found.")