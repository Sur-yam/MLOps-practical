import subprocess

print("Git version:")
p = subprocess.run(["git", "--version"], capture_output=True, text=True)
print(p.stdout.strip() if p.returncode == 0 else p.stderr.strip())
print("\nGit identity:")
p = subprocess.run(["git", "config", "--global", "--list"], capture_output=True, text=True)
print(p.stdout.strip() or "Identity not configured yet; see this experiment's README.")
