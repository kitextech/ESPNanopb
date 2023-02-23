# run generate go.
import subprocess

otherNanoFolders = "/Users/andreasokholm/src/kitex/opentwt/proto"

subprocess.call(["python", "copyShemaFromNanopb.py"], cwd=otherNanoFolders)