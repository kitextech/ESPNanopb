

# run generate go.
import subprocess

subprocess.call(['sh', './generateSchema.sh'])

destinationFolder = "/Users/andreasokholm/src/kitex/opentwt/ESP32Stepper/ESP32StepperMain/lib/ESP32Utils/src/ProtobufBridge"

files2copy = ["schema.pb.c", "schema.pb.h"]

for filename in files2copy:
    subprocess.call(['cp', './' + filename, destinationFolder + "/" + filename])

# create git tag and push
# import sys
# print(sys.argv)

gitDistFolder = destinationFolder = "/Users/andreasokholm/src/kitex/opentwt/ESP32Stepper/ESP32StepperMain/lib/ESP32Utils"

subprocess.call(["git", "tag"], cwd=gitDistFolder)


val = input("new tag name: (string without starting v to skip) ")

if (val[0] == "v"):
    mes = input("message to add: ")
    subprocess.call(["git", "tag", "-a", val, "-m", mes], cwd=gitDistFolder)
    subprocess.call(["git", "push", "origin", val], cwd=gitDistFolder)
