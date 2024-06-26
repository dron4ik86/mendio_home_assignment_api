# Bitbucket API Testing 

This repository was created as part of an automation task to demonstrate 
API testing using the Behave and Requests libraries for the Bitbucket API.

### Prerequisites (MacOS Environment)

- Install [Python](https://www.python.org/downloads/)

### Installation

Follow these steps to setup your development environment:

1. Navigate to the repository where you want to save the project.
    ```
    cd <folder name>
    ```
2. Clone the repository.
    ```
    git clone https://github.com/dron4ik86/mendio_home_assignment_api.git
    ```
3. Install the virtual environment.
    ```
    pip3 install virtualenv
    ```
4. Create a virtual environment in the project directory.
    ```
    cd <folder name>
    virtualenv venv
    ```
5. Activate the virtual environment.
    ```
    source venv/bin/activate
    ```
6. Install project dependencies.
    ```
    pip3 install -r requirements.txt
    ```
7. Please update the `.env.templat`e file with your own secret values and rename it to `.env`.


### Usage

1. Execute all tests
    ```
    behave 
    ```
2. Run specific scenarios by tags.
    ```
    behave -t @<TAG_NAME>
    ```

## Troubleshooting

### **Problem 1**:
### Issue: `zsh: command not found: virtualenv`

If you encounter the following error when trying to activate the virtual environment on macOS:
```
zsh: command not found: virtualenv
```
**Solution**:

This error occurs because the `virtualenv` command is not found in your shell's PATH. Instead, you can use Python's built-in `venv` module to create and activate a virtual environment:
```
python3 -m venv venv
```