
# Test the fetch parameter function

from __utils__ import fetch_parameters


if __name__ == "__main__":
    config_path = "config.txt"
    parameters = fetch_parameters(config_path=config_path)
    print(parameters)