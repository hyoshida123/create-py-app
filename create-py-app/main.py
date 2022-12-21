import os
import argparse
import yaml
from create_files import create_dir, create_file


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", required=True, type=str)
    app_name = parser.parse_args().name
    base_dir = create_dir(os.getcwd(), app_name)
    with open("file_contents.yml", "r") as f:
        yaml_data = yaml.safe_load(f)
        create_file(base_dir, "main.py", content=yaml_data["main.py"])
        create_file(
            base_dir,
            "environment_variables.py",
            content=yaml_data["environment_variables.py"],
        )
        create_file(base_dir, ".env", content=yaml_data[".env"])
        create_file(
            base_dir,
            ".pre-commit-config.yaml",
            content=yaml_data[".pre-commit-config.yaml"],
        )
        create_file(base_dir, ".gitignore", content=yaml_data[".gitignore"])
        create_file(base_dir, "Dockerfile", content=yaml_data["Dockerfile"])
        create_file(base_dir, "README.md", content=yaml_data["README.md"])
        create_file(base_dir, "pyproject.toml", content=yaml_data["pyproject.toml"])
    print(f"{app_name} has been created!")


if __name__ == "__main__":
    main()
