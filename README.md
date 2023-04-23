# check_todo_hook
Simple [pre-commit](https://github.com/pre-commit/pre-commit) hook for checking TODO: and FIXME: patterns in files.

You can prevent line from failing the check and displaying message by adding --later anywhere in the line **after** ```TODO:``` or ```FIXME:``` like this:
```python
def myfunc():
  # TODO: fix this --later
  pass
```
