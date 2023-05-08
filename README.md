# Useful?

## Run the example
```sh
./cli.py -c samples/abc.txt
```

## Commands that should be git pre-hooks

### Run mypy
```sh
find . -name '*.py' | xargs mypy
```

### Run yapf
```sh
find . -name '*.py' | xargs yapf --style='{based_on_style: google, indent_width: 2}' -i
```