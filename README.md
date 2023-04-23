# check_todo_hook
Simple [pre-commit](https://github.com/pre-commit/pre-commit) hook for checking TODO: and FIXME: patterns in files.

## Example
```test_file.py```
```python
def test_func():
  # TODO: do something
  pass
```
##### running git commit
```bash
$ git commit
Check todos..............................................................Failed
- hook id: check-todo-hook
- exit code: 1

test_file.py: 2: detected TODO
```


## Ignore TODOs
You can prevent line from failing the check and displaying message by adding ```--later``` anywhere in the line **after** ```TODO:``` or ```FIXME:``` like this:
```python
def myfunc():
  # TODO: fix this --later
  pass
```
