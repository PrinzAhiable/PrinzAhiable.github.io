# upload.py
import subprocess
import os

def run_command(command):
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {e}")
        exit(1)

def main():
    print("🔄 Checking if Git repo is initialized...")

    if not os.path.exists(".git"):
        print("🚨 Git not initialized. Initializing now...")
        run_command(["git", "init"])
        run_command(["git", "branch", "-M", "main"])
        run_command([
            "git", "remote", "add", "origin",
            "https://github.com/khaly123/vitechsc-services.git"
        ])
        print("✅ Git initialized.")

    print("🔁 Pulling latest changes from origin/main...")
    run_command(["git", "pull", "origin", "main", "--allow-unrelated-histories"])

    print("📁 Adding all files...")
    run_command(["git", "add", "."])

    print("📝 Enter your commit message:")
    commit_message = input("> ").strip()

    if commit_message:
        print("✅ Committing your changes...")
        run_command(["git", "commit", "-m", commit_message])
    else:
        print("⚠️ No commit message entered. Skipping commit.")
        return

    print("🚀 Pushing to origin/main...")
    run_command(["git", "push", "--set-upstream", "origin", "main"])

    print("✅ Push complete!")

if __name__ == "__main__":
    main()
