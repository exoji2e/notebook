# Notebook

This repo contains my notebook for ICPC-competitions.

All the code is found in the `src/` folder.

You can find a single page with copyable code at [https://exoji2e.github.io/notebook/](https://exoji2e.github.io/notebook/)

Generate the jekyll site locally with:

`jekyll serve`, given that you have jekyll installed, and on your path.

notebook.pdf might not continue to be up to date. I try to only push stable versions of the pdf.

The code is somewhat tested, but I'm planning to include tests in this repo in the future.

Install dependencies for Ubuntu/Debian with:

- `sudo apt-get install make texlive-full python-pygments`
  Or for MacOS:
- `brew cask install mactex`
- `sudo easy_install Pygments`

Build pdf with `make`.

Run tests with `python3 -m unittest discover -s src`
