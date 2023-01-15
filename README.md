Rufus - simple implementation to test git status 
===

Rufus is simple tool which provide several functions on git status about a local git repository.

### environment
macOS, python3

### installation 
```
pip3 install GitPython
```

### Usage

```
git clone https://github.com/xinran0722l/rufus.git
cd rufus
```

get your local repo link by the **pwd**
```
pwd    
```
copy the link, let me name it **`repo_link`**

run the command to test your local repo status, replace the **repo_link** by your own pwd output

```
python3 main.py repo_link
```
