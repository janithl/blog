# Janith's Blog

A personal blog powered by Pelican.

## Setting Up

- Clone [blog repo](https://github.com/janithl/blog)
- Install python3.9 and pip: `brew install python@3.9`
- create a venv: `python3.9 -m venv ./venv`
- activate it: `source ./venv/bin/activate`
- cd into blog repo `cd blog`
- install deps: `pip3 install -r requirements.txt`
- Clone the submodules: `git submodule update --init --recursive`
- Checkout to master in the submodules and pull if not up-to-date.

## Adding New Posts

- Add new content as .md files to `/content`
- When you're ready to publish, `make publish`
- `git commit` and `git push`
- `cd output`, and `git commit` and `git push`
