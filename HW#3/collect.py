import os
import os
for root, dirs, files in os.walk("data/", topdown=False):
    for file in files:
        if not file.startswith("."):
            print(os.path.join(file))
