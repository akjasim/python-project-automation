import sys
import os


project = sys.argv[1]
if not project:
    print("Please ensure that the project name is provided as the first argument. Also ensure that the project name doesn't contain spaces.")
    sys.exit()


# Fetching path.
path = sys.argv[2]
if not path:
    path = False

# Creating directory.    
try:
    if path:
        exact_path = os.path.join(path, project)
    else:
        exact_path = os.path.join(os.getcwd(), project)
    os.mkdir(exact_path)
    print(f'Created Directory {exact_path}')
    sys.exit(200)
except FileExistsError:
    print('Directory already exists')
    sys.exit()
except OSError:
    print('Please re-check the path. If path contains space, mention the whole path in double quotes.')
    sys.exit()
