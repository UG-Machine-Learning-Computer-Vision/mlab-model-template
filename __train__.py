"""
Do not edit this file
This is the file that will be used to train your model
"""
import os
import pickle
import argparse
import json
import requests
from model import train as train_model
from __utils__ import fetch_parameters
if __name__ == "__main__":
  # Run the model, pass the file location, the file type and the dataset name
  # Where inputs would be from command line
    print("Running model")
    parser=argparse.ArgumentParser(
        description="Train a model",
        prog="maldec-train",
    )

    parser.add_argument(
        "--config",
        type=str,
        help="Path to config file",
        required=False,
    )

    parser.add_argument(
        "--result_id",
        type=str,
        help="Result ID",
    )

    parser.add_argument(
        "--default",
        type=bool,
        help="Default run",
        required=False,
    )

    args=parser.parse_args()

    CONFIG_PATH = args.config
    result_id = args.result_id
    default = args.default
    if CONFIG_PATH is None:
        CONFIG_PATH = "config.txt" # type: ignore
    parameters = fetch_parameters(config_path=CONFIG_PATH)
    DATASET_PATH = str(parameters["dataset_url"]).strip() # type: ignore

    model = train_model(dataset_path=DATASET_PATH, parameters=parameters, result_id=result_id)

    if default:
        # Dump the model history in a pickle file
        with open("history.pkl", "wb") as f:
            pickle.dump(model.history, f)

    API_URL = "http://localhost:8000/api/results/train"

    # Stringify metrics
    metrics = json.dumps(model.metrics)


    data = {
        "result_id": result_id,
        "metrics": metrics,
        "history": model.history,
    }

    files = {}

    for file in model.files:
        filename = file.split("/")[-1].split(".")[0]
        files['file'] = (filename, open(file, 'rb'))

    # files = model.files

    response = requests.post(API_URL, data=data, files=files,timeout=120)

    if response.status_code == 200:
        print("Successfully uploaded results")
        for file in model.files:
            os.remove(file)
    else:
        print("Error uploading results")
        # Append error in error.txt file
        # First check if error.txt file exists
        if not os.path.exists("error.txt"):
            with open("error.txt", "w", encoding="utf-8") as f:
                f.write(f"{result_id}\n")
        else:
            with open("error.txt", "a", encoding="utf-8") as f:
                f.write(f"{result_id}\n")
