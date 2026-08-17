import re

def process_voice_command(command_text: str) -> str:
    """
    Simulates a voice coding interpreter by translating natural language
    commands into basic Python code snippets.
    """
    command_text = command_text.lower().strip()

    # Command: Define Function (e.g., "define function hello_world")
    match = re.match(r"define function (\w+)", command_text)
    if match:
        func_name = match.group(1)
        # This section illustrates translating a 'voice command' to code
        return f"def {func_name}():\n    # Your code here\n    pass"

    # Command: Print Variable (e.g., "print variable my_name")
    match = re.match(r"print variable (\w+)", command_text)
    if match:
        var_name = match.group(1)
        # This section illustrates translating a 'voice command' to code
        return f"print({var_name})"

    # Command: Assign Value (e.g., "assign hello world to message", "assign 123 to my_number")
    match = re.match(r"assign (.+) to (\w+)", command_text)
    if match:
        value = match.group(1).strip()
        variable = match.group(2)
        # Basic attempt to infer string vs. number for assignment
        if value.isdigit() or (value.startswith('-') and value[1:].isdigit()):
            return f"{variable} = {value}"
        else:
            return f"{variable} = \"{value}\"" # Assume string if not a simple number

    # Command: Loop N times (e.g., "loop 5 times")
    match = re.match(r"loop (\d+) times", command_text)
    if match:
        count = match.group(1)
        # This section illustrates translating a 'voice command' to code
        return f"for i in range({count}):\n    # Loop body\n    pass"

    return "# Command not recognized. Try 'define function my_func', 'print variable x', etc."

if __name__ == "__main__":
    print("Welcome to the Voice Code Simulator!")
    print("This tool simulates generating code from voice commands.")
    print("Type 'exit' to quit.")
    print("\nExample commands:")
    print("  - define function greet_user")
    print("  - print variable user_name")
    print("  - assign 123 to my_number")
    print("  - assign hello world to my_message")
    print("  - loop 3 times")
    print("-" * 30)

    # The article emphasizes moving beyond the 'write-wait-check' cycle.
    # This simulation demonstrates generating code directly from commands,
    # akin to how voice coding aims to replace manual typing.

    while True:
        try:
            user_input = input("\nEnter voice command: ")
            if user_input.lower() == 'exit':
                break
            
            generated_code = process_voice_command(user_input)
            print("\n--- Generated Code ---")
            print(generated_code)
            print("----------------------\n")
        except EOFError: # Handle Ctrl+D or Ctrl+Z
            print("Exiting simulator.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
