import os
import json

folder_names = [name for name in os.listdir() if os.path.isdir(name)]

print(json.dumps(folder_names))
