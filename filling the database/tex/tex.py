import os

def compile_tex_files_with_os_system():
    # Get the current directory where the notebook is located
    directory = os.getcwd()
    print(directory)
    # Iterate through all files in the current directory
    for file in os.listdir(directory):
        # Check if the file is a .tex file
        if file.endswith(".tex"):
            # Construct the pdflatex command
            command = f"pdflatex {file}"
            print(f"Running command: {command}")
            
            # Execute the command
            os.system(command)

# Call the function to compile all .tex files in the current directory
compile_tex_files_with_os_system()