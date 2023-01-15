
import datetime
import sys
import time

import git
# need to install gitpython , pip3 install GitPython
def show_git_status(git_dir):
  repo = git.Repo.init(path=git_dir)
  # current branch
  print(f"active branch: {repo.active_branch.name}")
  # if local has been changed 
  print(f"local changes: {repo.is_dirty()}")
  recent_commit = False
  rufus_commit = False
  # get the latest commit
  commit = repo.head.commit
  if commit:
    author_name = commit.author.name.strip()
    authored_date = commit.authored_date
    last_week_begin = time.mktime((datetime.datetime.now() - datetime.timedelta(days=7)).timetuple())
    if authored_date >= last_week_begin:
      recent_commit = True
    rufus_commit = "Rufus".lower() == author_name.lower()

  print(f"recent commit: {recent_commit}")
  print(f"blame Rufus: {rufus_commit}")


def test():
  # repalce the git_dir by your own repo link
  show_git_status(git_dir="/Users/xinran/Desktop/rufus") 


def run_as_command():
  show_git_status(sys.argv[1])


if __name__ == '__main__':
  run_as_command()
