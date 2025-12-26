#! usr/bin/bash

set -e 

# print_python_template: 
#   Prints template code to the generated Python file
# Arguments:
#   $1: The path to the generated Python file (string)
# Returns:
#   None 
function print_python_template() {
    echo -e "def main() -> None:" >> "$1"
    echo -e "\tprint(f\"Hello world from \'{__file__}\'!\")\n\n" >> "$1"
    echo -e "if __name__ == \"__main__\":" >> "$1"
    echo -e "\tmain()" >> "$1"
}

# print_README_template: 
#   Prints a template to the generated README markdown file 
# Arguments:
#   $1: The name of the playground environment/test (string)
#   $2: The path to the generated README markdown file (string)
#   $3: The path to the generated Python file (string)
# Returns:
#   None 
function print_README_template() {
    echo "# $1" >> "$2"
    echo -e "\n\n" >> "$2"
    echo "\`\`\`bash" >> "$2"
    echo "python $3" >> "$2"
    echo "\`\`\`" >> "$2"
}

# Get CLI argument for the playground name and define file paths 
PLAYGROUND_NAME="$1"
PYTHON_FILE_PATH="$PLAYGROUND_NAME"/"$PLAYGROUND_NAME.py"
README_FILE_PATH="$PLAYGROUND_NAME"/"$PLAYGROUND_NAME.md"

# Create the playground dir and generate the Python & README files 
mkdir "$PLAYGROUND_NAME"
touch "$PYTHON_FILE_PATH"
touch "$README_FILE_PATH"

# Print template to the README files 
print_python_template "$PYTHON_FILE_PATH"
print_README_template "$PLAYGROUND_NAME" "$README_FILE_PATH" "$PYTHON_FILE_PATH"

# Test template code 
python "$PYTHON_FILE_PATH"