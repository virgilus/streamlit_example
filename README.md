# streamlit_example
A simple template showing what should look like a git repo in data science.

## data

Inside this repo your dataframe is very small, only 227 lines, so it can remain inside the "data" folder. But usually your data is to big to do this. In this case dO **NOT** forget to add this rep inside your `.gitignore` file! Otherwise, all your data might be sent to your remote git repository.

## notebooks

Contains all your notebooks. Use one notebook for each person. Do **NOT** work on the same notebook, in case of conflicts, git doesn't handle this.

## countries_analytics

This folder will contain the package for your project.

### __init__.py

This file will tell python your current folder is a package. Each time you import a module, python will also run the __init__.py file.

We can use this behaviour to make sure that anytime we use a function from our package, it can access to the same environment custom variables, such as the ones we added in our .env file.

### make_dataset.py and process_data.py

Just some basic modules containing various functions for our package.

## .env

Contains custom environment variables, like API_KEY or DEBUG_MODE, that all our scripts can use.

## .gitignore

This file has been generated by GitHub and contains already loads of files we don't want to commit. We added data, so our data are not pushed on our remote repository.

We also added some junk files such as '.DS_Store' (mac) and 'Thumbs.db' (windows).

## main.py

This script is the script that does the job the project is intended to. We added ```if __name__ == 'main':``` to make sure everything will be executed only if it's the script you ran.

Don't get confused between:
- 'main', the name of the main branch in git.
- 'main.py', the name of our file (we can choose any other name).
- '__main__', which is the internal name that python gives to every script you run explicitly.

## requirements.txt

Contains all the packages with their versions we need to install.

## setup.py, setup.cfg, pyproject.toml

Those files don't exist in this current repo, but you might encounter them in other programs. They are used to turn your project into a proper python package. You don't need to do it for now.