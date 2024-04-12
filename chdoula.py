import subprocess
import multiprocessing

def run_script(script_name):
    subprocess.Popen(["python", script_name])

if __name__ == "__main__":

    script1_process = multiprocessing.Process(target=run_script, args=("deploy.py",))
    script2_process = multiprocessing.Process(target=run_script, args=("script.py",))

    script1_process.start()
    script2_process.start()

    script1_process.join()
    script2_process.join()
