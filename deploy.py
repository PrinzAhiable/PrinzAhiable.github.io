import subprocess

def run_command(command):
    print(f"\nRunning: {command}")
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"❌ Command failed: {command}")
        exit(1)

def deploy():
    run_command("npm run build")
    run_command("git add .")
    run_command("git add dist -f")
    run_command("git commit -m \"Add to github and deploy\"")
    run_command("git subtree push --prefix dist origin gh-pages")
    run_command("git push")

if __name__ == "__main__":
    deploy()
