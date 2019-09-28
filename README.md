## Demo send mail by celery job queue 

## INTRO
The repo supports sending email asynchronous via task queue/job queue celery, rabbitmq broken and flower tracking in python 3.

## Docs:
- Celery Architecture: https://wiki.openstack.org/wiki/Celery#ARCHITECTURE
- Monitoring and Management Guide Introduction: http://docs.celeryproject.org/en/latest/userguide/monitoring.html
- RabbitMQ broker: http://docs.celeryproject.org/en/latest/getting-started/brokers/rabbitmq.html
- Celery Worker: http://docs.celeryproject.org/en/latest/userguide/workers.html

## Usage

```
    # set config.test.json

    # start worker
    pipenv run celery worker -A celery_worker  --conf=flowerconfig.py

    # start Flower
    pipenv run flower -A celery_worker 

    # run demo.py file
    pipenv run python demo.py

    # open flower on localhost:5555 and track result
```

## Set up environment

### 1. Install RabbitMq on your machine.
- Install at: https://www.dyclassroom.com/howto-mac/how-to-install-rabbitmq-on-mac-using-homebrew
- Install RabbitMQ using Homebrew:```$ brew install rabbitmq```
- Add to PATH
- RabbitMQ server and CLI script are installed under `/usr/local/sbin`. Add this to PATH.

    ```export PATH=$PATH:/usr/local/sbin```
- Add the following to `.bash_profile` file.
    ```$ vi ~/.bash_profile```
- Inside the `.bash_profile` file.
    ```buildoutcfg
    #HOMEBREW RABBITMQ
    export HOMEBREW_RABBITMQ=/usr/local/Cellar/rabbitmq/3.7.11/sbin/
    export PATH=$PATH:$HOMEBREW_RABBITMQ
    ```
- Start RabbitMQ server

    ```buildoutcfg
    $ rabbitmq-server

      ##  ##
      ##  ##      RabbitMQ 3.7.11. Copyright (C) 2007-2019 Pivotal Software, Inc.
      ##########  Licensed under the MPL.  See http://www.rabbitmq.com/
      ######  ##
      ##########  Logs: /usr/local/var/log/rabbitmq/rabbit@localhost.log
                        /usr/local/var/log/rabbitmq/rabbit@localhost_upgrade.log
    
                  Starting broker...
     completed with 6 plugins.
    ```
- Access dashboard: `http://localhost:15672`.

    The default `username` and `password` is `guest` and `guest` respectively.

### 2. Install pyenv and pipenv
- Install pyenv for mac: 
```
# Install Homebrew if it isn't already available
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" 
brew install pyenv 

# Add pyenv initializer to shell startup script
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile 
source ~/.bash_profile # Reload your profile
pyenv versions
```

- Install pyenv for ubuntu: 
```
sudo apt update -y
sudo apt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
  libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
  xz-utils tk-dev libffi-dev

git clone https://github.com/pyenv/pyenv.git ~/.pyenv

echo 'export PYENV_ROOT="$HOME/.pyenv"'    >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc

# restart shell & aftermath check
exec "$SHELL"
pyenv --version
```

- Install python 3.6.7
```
pyenv install 3.6.7
pyenv global 3.6.7
python --version # should be 3.6.7
```

- Install pipenv
```
# install pipenv
curl https://raw.githubusercontent.com/kennethreitz/pipenv/master/get-pipenv.py | python
echo "
# pipenv setup"                                   >> ~/.bashrc
echo 'export PATH="~/.local:$PATH"'               >> ~/.bashrc
echo 'export PIPENV_VENV_IN_PROJECT=1'            >> ~/.bashrc # project's venv location will be in the project folder as .venv ref. https://pipenv.readthedocs.io/en/latest/advanced/#pipenv.environments.PIPENV_VENV_IN_PROJECT
echo 'export PIPENV_DEFAULT_PYTHON_VERSION=3.6.7' >> ~/.bashrc # project's venv location will be in the project folder as .venv ref. https://pipenv.readthedocs.io/en/latest/advanced/#pipenv.environments.PIPENV_VENV_IN_PROJECT
echo 'eval "$(pipenv --completion)"'              >> ~/.bashrc # shell auto-completion ref. https://pipenv.readthedocs.io/en/latest/advanced/#shell-completion

#restart shell & aftermath check
exec "$SHELL"
pipenv --version
```

- `cd` to `you_project_path` and run `pipenv sync` to install all dependencies of project.
