import json
import argparse

# Attributes that are returned by DescribeTaskDefinition,
# but are not valid RegisterTaskDefinition inputs
IGNORED_TASK_DEFINITION_ATTRIBUTES = [
  'compatibilities',
  'taskDefinitionArn',
  'requiresAttributes',
  'revision',
  'status',
  'registeredAt',
  'deregisteredAt',
  'registeredBy'
]

def get_container_definition(task, container_name):
    for container_def in task["containerDefinitions"]:
        if container_def["name"] == container_name:
            return container_def
    return ValueError(f"Container with name {container_name} was not found.")


def remove_ignored_attributes(task):
    for attribute in IGNORED_TASK_DEFINITION_ATTRIBUTES:
        if attribute in task:
            task.pop(attribute, None)
    return task


def update_task_definition(task, container_name):
    task = remove_ignored_attributes(task)
    container_def = get_container_definition(task, container_name)
    container_def["image"] = args.image_uri
    return task


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

task = update_task_definition(task, args.container_name)

# rewrite task definition file
file = open(args.task_definition, "w")
json.dump(task, file, indent=2)
file.close()
