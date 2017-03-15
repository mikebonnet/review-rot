import yaml
import os
import github
import gitlab
from github.GithubException import UnknownObjectException
from gitlab.exceptions import GitlabGetError


with open('test_githubtest.yaml', 'r') as f:
    config = yaml.load(f)


# github

def mock_get_user(user_name):
    raise UnknownObjectException('args', 'kwargs')


def mock_get_user_(user_name):
    res = github.NamedUser.NamedUser('args', 'kwargs',
                                     {'login': user_name}, 'kwargs**')
    return res


def mock_get_repos():
    repo = github.Repository.Repository('args', 'args*', 'kwargs', 'kwargs*')
    res = []
    res.append(repo)
    return res


def mock_github_get_reviews(uname, repo_name, state_=None, value=None, duration=None):
    msg = config['msg']
    return msg


def mock_get_repo(repo_name):
    raise UnknownObjectException('args', 'kwargs')


def mock_get_repo_(repo_name):
    repo = github.Repository.Repository('args', 'args*', 'kwargs', 'kwargs*')
    return repo


def mock_get_pulls():
    return []

# gitlab

def mock_projects_get(user_name, repo_name):
    raise GitlabGetError()


def mock_projects_get_(user_name, repo_name):
    res = gitlab.Project({'args':'args*'})


def mock_auth():
    return True


def mock_groups_search(user_name):
    return []


def mock_gitlab_get_reviews(uname, project, state_=None, value=None, duration=None):
    msg = config['msg']
    return msg
