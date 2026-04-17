# run generate go.
import subprocess

otherNanoFolders = "/Users/andreasokholm/src/kitex/firmware/proto"

subprocess.call(["python", "copyShemaFromNanopb.py"], cwd=otherNanoFolders)