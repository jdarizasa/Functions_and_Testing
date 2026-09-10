[![Codespaces Prebuilds](https://github.com/jdarizasa/Functions_and_Testing/actions/workflows/codespaces/create_codespaces_prebuilds/badge.svg)](https://github.com/jdarizasa/Functions_and_Testing/actions/workflows/codespaces/create_codespaces_prebuilds)

[![CI](https://github.com/jdarizasa/Functions_and_Testing/actions/workflows/main.yml/badge.svg)](https://github.com/jdarizasa/Functions_and_Testing/actions/workflows/main.yml)

# Functions_and_Testing
This is a repo to define functions and automated testing

## Step 1: Configure development environment
* Configure Codespaces or equivalent (devcontainer)
* Create scafold for the structure of the project (Makefile, requirements)
* Optional: set virtualenv and install outside ipython

## Step 2: Get interactive debugging working
* Use ipyhton or ipdb

```python
x=1
y=2

import ipdb; ipdb.set_trace()
print(x+y)
```

## Step 3: Build a library and use it