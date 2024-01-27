import os
from git.repo.base import Repo

# List of repository URLs
# Specify the path to your text file
file_path = r"C:\Users\balasubramaniam.cs\OneDrive - IDP Education Ltd\Documents\Squad-7\repo list\BALA.txt"

# Open the file in read mode
with open(file_path, "r") as file:
    # Read the links line by line
    for line in file:
        # Remove leading and trailing whitespace, such as newline characters
        link = line.strip()
        
        # You can now process each link as needed
        # For example, print the link
        print(link)

        # Directory where you want to clone the repositories
        clone_directory = r"C:\Users\balasubramaniam.cs\OneDrive - IDP Education Ltd\Desktop\Squad-7\BALA"

        # Create the directory if it doesn't exist
        os.makedirs(clone_directory, exist_ok=True)

        # Loop through the repository URLs and clone each one

        repo_name = link.split("/")[-1].split(".git")[0]
        repo_path = os.path.join(clone_directory, repo_name)

        try:
            repo = Repo.clone_from(link, repo_path)
            print(f"Cloned {repo_name} to {repo_path}")
        except Exception as e:
            print(f"Failed to clone {repo_name}: {e}")

print("Cloning completed.")