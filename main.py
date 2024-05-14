import subprocess
import sys

def generate_assembly(input_file, output_file):
    # Command to generate assembly code using g++
    command = f"gcc -S -o {output_file} {input_file} "
    
    try:
        # Execute the command
        subprocess.check_call(command, shell=True)
        print(f"Assembly code generated and stored in {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while generating assembly code: {str(e)}")

if __name__ == "__main__":
    # Check if file name is provided
    if len(sys.argv) != 3:
        print("Usage: python3 script.py <input_file> <output_file>")
        sys.exit(1)

    # Input C or C++ file
    input_file = sys.argv[1]

    # Output file to store assembly code
    output_file = sys.argv[2]

    # Generate assembly code
    generate_assembly(input_file, output_file)

#python3 script.py input.cpp output.txt
