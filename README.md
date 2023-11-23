# MLab Model Template
Template for models to be used on DISAL MLab

## How to use
1. [Clone this repository][clone-this-repository]
2. [Create a new branch][create-a-new-branch]
3. [Create a new folder with the name of your model][create-a-new-folder]
4. [Implement your model][implement-your-model]
5. [Implement the train and test functions in the model.py file][implement-the-train-and-test-functions-in-the-model.py-file]
6. [Freeze your requirements and add them to the requirements.txt file][freeze-your-requirements-and-add-them-to-the-requirements.txt-file]
7. [Add all needed parameters to the config.txt file][add-all-needed-parameters-to-the-config.txt-file]

### Clone this repository
[clone-this-repository]: #clone-this-repository
```bash
git clone UG-Machine-Learning-Computer-Vision/mlab-model-template <your_model_name>
```

### Create a new branch
[create-a-new-branch]: #create-a-new-branch
```bash
git checkout -b <branch_name>
```

### Create a new folder with the name of your model
[create-a-new-folder]: #create-a-new-folder
```bash
cd <your_model_name>
mkdir <your_model_name>
```

### Implement your model
[implement-your-model]: #implement-your-model
With the config file in mind, implement your model treating the parameters as variables. For example, if you have a parameter called `learning_rate`, you should use it as a variable in your code, like this:
```python
learning_rate = parameters['learning_rate']
```
The parameters would be provided through the train and test functions in the model.py file.

### Implement the train and test functions in the model.py file
[implement-the-train-and-test-functions-in-the-model.py-file]: #implement-the-train-and-test-functions-in-the-model.py-file
The train and test functions should be implemented in the model.py file. The train function should receive the parameters and the dataset_path and return the trained model. The test function should receive the parameters, the dataset_path and the trained model and return the predictions.

### Freeze your requirements and add them to the requirements.txt file
[freeze-your-requirements-and-add-them-to-the-requirements.txt-file]: #freeze-your-requirements-and-add-them-to-the-requirements.txt-file
Freeze your requirements using the following command:
```bash
pip freeze > requirements.txt
```
Then, add the requirements to the requirements.txt file.

### Add all needed parameters to the config.txt file
[add-all-needed-parameters-to-the-config.txt-file]: #add-all-needed-parameters-to-the-config.txt-file
Add all needed parameters to the config.txt file. The parameters should be added in the following format:
```bash
PARAM name type default_value
```
Where:
- `PARAM` is the parameter name
- `name` is the name of the parameter
- `type` is the type of the parameter
- `default_value` is the default value of the parameter

The types can be:
- `int`
- `float`
- `str`
- `bool`
- `list`

A list of values should be provided in the following format:
```bash
PARAM <name> list[<type>] <value1>,<value2>,<value3>
```
Where:
- `type` is the type of the values
The values would be interpreted as a list of values of the specified type.
The compatible types are:
- `int`
- `float`
- `str`
- `bool`

## Defining the train dataset

A Dataset.md should be present in the parent directory.
This would be used to define the dataset and its structure.

The folowing should be made clear in the Dataset.md file:
- The dataset structure
- The dataset format
 and any other information that might be relevant.

## Testing your model

A Test.md should be present in the parent directory.
This would be used to define how to test your model.
This should include:
- How to test your model
- How to interpret the results
- What dataset inputs should be used