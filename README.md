# Python Project Automation

This project helps python developers get up and running as quickly as possible. You write just a single line of command and we'll automate the rest.
1) Create a project directory.
2) Create a new src folder in the project directory.
3) Create a new README file inside src directory.
4) Create a virtual environment.
5) Activate virtual environment.
6) Create local and remote Github repositories.
7) Add remote origin, git add, git commit and git push.

!!! Happy Coding !!!

## Installation

#### 1) Use Github to clone the repository.

```bash
git clone https://github.com/akjasim/python-project-automation.git
```

#### 2) Install all requirements.

```bash
pip install -r requirements.txt
```

#### 3) Add project root directory into Windows System Variable Path so that you can access the script from anywhere in your PC. Google on 'how to set system path in windows', if you're not comfortable with it.

#### 4) Add environment variables. Google on 'how to add environment variable in windows', if you're not comfortable with it.

##### Note: There are two pairs below and each pair consists of variable name and variable value.

```bash
github_user  YOUR_GITHUB_USERNAME
github_pass  YOUR_GITHUB_PASSWORD
```

## Usage

#### One for all. Type in the following command in cmd and you're ready to roll.
```bash
create project_name project_directory private
```

##### project_name - Name of your project. (White spaces are not allowed.)

##### project_directory (Optional) - The directory in which the project is to be created. (If there are white spaces, surround it with double quotes.)

##### private (Optional) - Applicable for Github private repository. (By default, a public repository.)

## Example

#### Create a project named "hello" in directory "D:\Python" as a private repository with the following command in Command Prompt.
```bash
create hello "D:\Python" private
```
#### If it is a public repository, the below one is enough.
```bash
create hello "D:\Python"
```


## Contributing
Currently applicable for Windows users only. For Mac/Linux users, make necessary changes in batch script. We love to keep in touch with contributors. For major changes, please open an issue first to discuss what you would like to change.


## License
[MIT](https://choosealicense.com/licenses/mit/)
