import os
import subprocess
def main()->None:
    
    venv_dir = "venv"
    if not os.path.exists(venv_dir):
        subprocess.run(["python", "-m", "venv", venv_dir])

    # Activate the venv.
    activate_script = os.path.join(venv_dir, "bin", "activate")
    subprocess.run(["source", activate_script], shell=True)

    # Install the required packages using pip.
    subprocess.run(["pip", "install", "-r", "requirements.txt"])


if __name__ == "__main__":
    main()
    