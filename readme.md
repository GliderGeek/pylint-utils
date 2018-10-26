# pylintrc

pylint is a great linter, which thoroughly analyses your code. Running it for the first time on an existing codebase can be intimidating though, because it outputs hundreds of errors! Through all the errors, you don't see the important ones and skip pylint alltogether.

pylintrc is a small cli which makes it easier to implement pylint in an existing codebase. It helps creating a configuration file which checks the errors you find important and skips the rest.

# Install
```
pip install pylintrc
```

# Basic usage
```
$ pylintrc disable MODULES_OR_PACKAGES
```

Or just type `pylintrc disable --help` for instructions

# Future plans
- Add tests
- Load current pylintrc file
- Add ignore command, which make it easy to ignore specific files
