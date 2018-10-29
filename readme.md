# pylintconfig

[Pylint](https://www.pylint.org/) is a great linter, which thoroughly analyses your code. Running it for the first time on an existing codebase can be intimidating though, because it outputs hundreds of errors! Through all the errors, you don't see the important ones and skip [Pylint](https://www.pylint.org/) alltogether.

pylintconfig is a small cli which makes it easier to implement [Pylint](https://www.pylint.org/) in an existing codebase. It helps creating a configuration file which checks the errors you find important and skips the rest.

# Install
```
pip install pylintconfig
```

# Basic usage

1. Generate a configuration which explicitly disables all current pylint errors:

```
pylintconfig disable MODULES_OR_PACKAGES > .pylintrc
```

2. Prune this list such that the usefull errors are enabled.

3. Generate an ignore list which explicitly ignores all files with errors:

```
pylintconfig ignore MODULES_OR_PACKAGES
```

4. Add this list to .pylintrc and you are ready to go:
- Pylint does not give errors and can be added to you CI runner
- The ignore list provides a todo list for files which need some work
- New errors will present itself if not in the ignore list or not explicitly disabled.

# Future plans
- Add tests
- Load current pylintrc file and combine it with new 
