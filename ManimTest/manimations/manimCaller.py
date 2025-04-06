import os
import subprocess

def find_and_replace_in_file(source_path, destination_path, old_text, new_text):
    """
    Finds and replaces text within a file.

    Args:
        source_path (str): The path to the file.
        old_text (str): The text to be replaced.
        new_text (str): The replacement text.
    """
    try:
        # Ensure the source file exists
        if not os.path.exists(source_path):
            print(f"Error: File '{source_path}' not found.")
            return
        
        with open(source_path, 'r') as file:
            file_content = file.read()

        # Only perform replacement if old_text exists in the content
        if old_text in file_content:
            updated_content = file_content.replace(old_text, new_text)

            # Ensure destination directory exists
            destination_dir = os.path.dirname(destination_path)
            if destination_dir and not os.path.exists(destination_dir):
                os.makedirs(destination_dir)

            with open(destination_path, 'w') as file:
                file.write(updated_content)
            print(f"Successfully replaced '{old_text}' with '{new_text}' in '{source_path}'.")
        else:
            print(f"No occurrences of '{old_text}' found in '{source_path}'.")
        
    except FileNotFoundError:
        print(f"Error: File '{source_path}' not found.")
    except PermissionError:
        print(f"Error: Permission denied when accessing '{source_path}' or '{destination_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

def run_manim_scene(file_path, scene_name, quality='pl'):
    """
    Runs a Manim scene using the command line interface.

    Args:
        source_path (str): Path to the Manim script file.
        scene_name (str): Name of the scene class to render.
        quality (str, optional): Rendering quality. Defaults to 'pl' (preview low). 
                                 Other options include 'pm' (preview medium), 
                                 'ph' (preview high), 'ql' (quality low),
                                 'qm' (quality medium), and 'qh' (quality high).
    """
    command = ['manim', file_path, scene_name, f'{quality}']
    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode == 0:
        print("Manim scene rendered successfully.")
        print(result.stdout)
    else:
        print("Error rendering Manim scene:")
        print(result.stderr)

#JANK TEST TEMPLATE
def manimJankTest(x, y):
    
    find_and_replace_in_file(r"Templates\jank.py", r"Instances\jankInstance.py", "++x", str(x))
    find_and_replace_in_file(r"Instances\jankInstance.py", r"Instances\jankInstance.py", "++y", str(y))
    run_manim_scene("Instances\jankInstance.py", "Jank")

#Linear Equation Algebraic Solution
def manimLinearEq(y, m, b):
    
    find_and_replace_in_file(r"Templates\linearEq.py", r"Instances\linearEqInstance.py", "++y", str(y))
    find_and_replace_in_file(r"Instances\linearEqInstance.py", r"Instances\linearEqInstance.py", "++m", str(m))
    find_and_replace_in_file(r"Instances\linearEqInstance.py", r"Instances\linearEqInstance.py", "++b", str(b))
    run_manim_scene("Instances\linearEqInstance.py", "Linear")

#Sine Function Circle Explanation
def manimSineFunc(r):
    find_and_replace_in_file(r"Templates\sineFunc.py", r"Instances\sineInstance.py", "++r", str(r))
    run_manim_scene("Instances\sineInstance.py", "Sine")