# Python Package Test Repo
Python Package Test Repo to test pip installation from GitHub

## Install from GitHub
Use the following command to install from git:

```bash
pip3 install git+https://github.com/albyst/python-package-test-repo
```

Then you can import and use the test package:

```python
import python_test_package

python_test_package.extremely_useful_function()
```

## Testing
Testing uses [tox](https://tox.wiki/en/latest/), so you need to install it first:

```bash
pip3 install tox
```

then you can run tests defined under the ```tests``` directory by issuing the command:

```bash
tox
```
