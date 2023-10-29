# Moduldes

## Introduce

Idea là sử dụng poetry để manage các modules. Sau đó install các modules này vào python environment để trong jupyter notebook chúng ta có thể import nó



## Step to build local env

1. Install `pyenv`
2. Install `virtualenv`

3. Bởi vì trong zshrc file đã có config này (nếu chưa thì thêm vào)

```bash
alias brew='env PATH="${PATH//$(pyenv root)\/shims:/}" brew'

if command -v pyenv 1>/dev/null 2>&1; then
 eval "$(pyenv init --path)"
 eval "$(pyenv init -)"
 eval "$(pyenv virtualenv-init -)"
fi
```

Nên khi vào root folder, sẽ tự active `grind75-env` environment



## Create new module

```bash
poetry new some_module

# cd vao module va run install
poetry install

# Sau khi install xong, expect là module đó sẽ tồn tại trong list các module đã install
pip list
```

## Resolve problem between python env and poetry
We can set to poetry with setting to tell poetry use current existing python env
```shell
[virtualenvs]
prefer-active-python=true
```

After that, we can use both pip install or poetry add. But we only use poetry add to `pyproject.toml`