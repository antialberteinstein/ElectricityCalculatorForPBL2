from git import Repo
import os
import shutil

repo_url = "https://github.com/antialberteinstein/ElectricityCalculatorForPBL2.git"
destination_folder = "data"

if os.path.exists(destination_folder):
    shutil.rmtree(destination_folder)

Repo.clone_from(repo_url, destination_folder)
print("Data retrieved successfully!")
