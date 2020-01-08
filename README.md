<h1 align="center">
  corTeX
</h1>
<p align="center">
  Continuously-integrated Open-source Reproducible TeX
</p>
<p align="center">
  <a href="https://travis-ci.org/mxochicale/my-corTeX/">
    <img src="https://img.shields.io/travis/mxochicale/my-corTeX/master.svg"/>
  </a>
  <a href="https://github.com/mxochicale/my-corTeX/raw/master-pdf/ms.pdf">
    <img src="https://img.shields.io/badge/read-the_paper-blue.svg?style=flat"/>
  </a>
</p>


## Quick start

1. [Fork](https://github.com/rodluger/corTeX/fork) this repository and [rename it](https://help.github.com/en/articles/renaming-a-repository) to your desired project's name
2. Create a [Travis-CI account](https://travis-ci.org/) account and sync it to your GitHub if you don't have one already; it may take a few minutes for Travis-CI to discover your new repo
3. Under the settings page for your repo (``https://travis-ci.org/<user>/<repo>/settings``), create two environment variables: ``GITHUB_USER`` and ``GITHUB_API_KEY``. The former is just your GitHub username, while the latter is your [secret GitHub API token](https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line). This allows Travis-CI to commit and push changes to your repository on your behalf. Treat this token as you would treat a password, and never store it anywhere on your repo! Make sure to disable **Display value in build log** so it doesn't get leaked to the world. Note that you only need to give Travis **repo** permissions
4. Hack away! Read the brief [paper](https://github.com/mxochicale/my-corTeX/raw/master-pdf/ms.pdf) explaining more details about how to use **corTeX**


## Usage

1. Edit [ms.tex](/tex/ms.tex) or [py-scripts](/tex/figures/)
2. Add, commit and push changes to the master of the repository

```
git add .
git commit -m 'message'
git push origin master
```
Then, you should wait for the CI build at [https://travis-ci.org/mxochicale/my-cortex](https://travis-ci.org/mxochicale/my-cortex).
If the CI build is successful, you will then see at the bottom of the terminal: 
```
Done. Your build exited with 0.
```

3. Your PDF file is ready!  
Voila, your PDF file is available in the master-pdf branch as [ms.pdf](https://github.com/mxochicale/my-corTeX/raw/master-pdf/ms.pdf)

