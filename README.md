# Python Package Test Repo
Python Package Test Repo to test pip installation from GitHub

## Install from GitHub
Use the following command to install from git:

```bash
pip3 install git+https://github.com/albyst/python-package-test-repo
```

It is also possible to specify a “git ref” such as branch name, a commit hash or a tag name (more info can be found in [official documentation](https://pip.pypa.io/en/stable/topics/vcs-support/#vcs-support)):

```bash
MyProject @ git+https://git.example.com/MyProject.git@master
MyProject @ git+https://git.example.com/MyProject.git@v1.0
MyProject @ git+https://git.example.com/MyProject.git@da39a3ee5e6b4b0d3255bfef95601890afd80709
MyProject @ git+https://git.example.com/MyProject.git@refs/pull/123/head
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
