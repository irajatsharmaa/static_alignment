import subprocess
import os

def assemble_and_run(assembly_code_path):
    # Define the paths for the intermediate and final files
    asm_file = 'temp_assembly.asm'
    obj_file = 'temp_object.o'
    executable_file = 'temp_executable'

    # Read the assembly code from the text file
    with open(assembly_code_path, 'r') as file:
        assembly_code = file.read()

    # Write the assembly code to a .asm file
    with open(asm_file, 'w') as file:
        file.write(assembly_code)

    # Assemble the .asm file into an object file using NASM
    subprocess.run(['nasm', '-f', 'elf', asm_file, '-o', obj_file], check=True)

    # Link the object file into an executable using LD
    subprocess.run(['ld', '-m', 'elf_i386', obj_file, '-o', executable_file], check=True)

    # Run the executable
    subprocess.run(['./' + executable_file], check=True)

    # Clean up the intermediate files
    os.remove(asm_file)
    os.remove(obj_file)
    os.remove(executable_file)

# Replace 'path_to_assembly_code.txt' with the path to your assembly code text file
assemble_and_run('rearranged_assembly.txt')
