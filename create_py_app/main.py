import os
import sys
import argparse
import yaml
from create_py_app.create_files import (
    create_dir,
    create_file,
    create_file_with_project_name,
)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", required=True, type=str)
    app_name = parser.parse_args().name
    base_dir = create_dir(os.getcwd(), app_name)
    yaml_path = os.path.dirname(os.path.abspath(__file__))
    with open(yaml_path + "/file_contents.yml", "r") as f:
        yaml_data = yaml.safe_load(f)
        for key in yaml_data.keys():
            if key in ["README.md", "pyproject.toml"]:
                create_file_with_project_name(
                    base_dir, app_name, key, content=yaml_data[key]
                )
                continue
            create_file(base_dir, key, content=yaml_data[key])
    print(f"{app_name} has been created!")


if __name__ == "__main__":
    main()
