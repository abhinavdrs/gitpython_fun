from git import Repo


repo_path = '/Users/abhinav/PycharmProjects/github_automation/gitpython_fun'

repo = Repo(repo_path)
assert not repo.bare

assert not repo.is_dirty()