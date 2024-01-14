def replace_spaces_with_underscores(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # edit lines
    for i in range(len(lines)):
        lines[i] = lines[i].replace("    ", "__")
        lines[i] = "<p>" + lines[i].strip() + "</p>\n"

    with open(file_path, 'w') as file:
        file.writelines(lines)

# usage
replace_spaces_with_underscores('textfile.txt')
