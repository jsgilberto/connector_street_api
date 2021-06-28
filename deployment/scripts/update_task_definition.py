import json
import argparse


def get_container_definition(task, container_name):
    for container_def in task["containerDefinitions"]:
        if container_def["name"] == container_name:
            return container_def
    return ValueError(f"Container with name {container_name} was not found.")


# Initiate the parser
parser = argparse.ArgumentParser()

# Add long and short arguments
parser.add_argument("--container-name", "-c", help="container name")
parser.add_argument("--image-uri", "-i", help="image URI")
parser.add_argument("--task-definition", "-t", help="Path of task definition file")


# Read arguments from the command line
args = parser.parse_args()

print(f"Container: {args.container_name}")
print(f"Image URI: {args.image_uri}")
print(f"Task Definition File: {args.task_definition}")

# read task definition file
file = open(args.task_definition, "r")
task = json.load(file)
file.close()

container_def = get_container_definition(task, args.container_name)
container_def["image"] = args.image_uri

# rewrite task definition file
file = open(args.task_definition, "w")
json.dump(task, file, indent=2)
file.close()
