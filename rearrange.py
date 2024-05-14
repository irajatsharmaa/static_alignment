def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def parse_branch_conditions(branch_conditions_lines):
    branch_conditions = []
    for line in branch_conditions_lines:
        if 'Branch Condition:' in line:
            parts = line.split(',')
            condition = parts[0].split(':')[1].strip()
            target = parts[1].split(':')[1].strip()
            branch_conditions.append((condition, target))
    return branch_conditions

def find_instruction_index(assembly_lines, instruction):
    for index, line in enumerate(assembly_lines):
        if instruction in line:
            return index
    return None

def rearrange_assembly(assembly_lines, branch_conditions):
    rearranged_blocks = []
    for condition, target in branch_conditions:
        target_index = find_instruction_index(assembly_lines, target)
        branch_index = find_instruction_index(assembly_lines, condition)

        # Create a block of 4 instructions
        block = ['NOP'] * 4  # Initialize with NOPs
        if target_index is not None:
            block[0] = assembly_lines[target_index].strip()
        if branch_index is not None:
            block[-1] = assembly_lines[branch_index].strip()
            # Fill the middle instructions if possible
            for i in range(1, 3):
                if branch_index - i >= 0:
                    block[-i-1] = assembly_lines[branch_index - i].strip()

        rearranged_blocks.append(block)
    return rearranged_blocks

def write_to_file(blocks, output_file):
    with open(output_file, 'w') as file:
        for block in blocks:
            file.write('\n'.join(block) + '\n\n')

# Read the input files
branch_conditions_lines = read_file('branch_conditions.txt')
assembly_lines = read_file('output.txt')

# Parse the branch conditions and rearrange the assembly
branch_conditions = parse_branch_conditions(branch_conditions_lines)
rearranged_blocks = rearrange_assembly(assembly_lines, branch_conditions)

# Write the rearranged blocks to the output file
write_to_file(rearranged_blocks, 'rearranged_assembly.txt')
