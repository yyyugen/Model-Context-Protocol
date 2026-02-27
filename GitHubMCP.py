import os
from mcp.server.fastmcp import FastMCP
from github import Github, GithubException
from dotenv import load_dotenv

load_dotenv()

GITHUBTOKEN = os.getenv("GITHUBTOKEN")
if not GITHUBTOKEN:
    raise ValueError("GITHUBTOKEN environment variable not set")

"""Initialize GitHub Client"""
gh = Github(GITHUBTOKEN)

"""Create MCP server"""
mcp = FastMCP("GitHub MCP")

@mcp.tool()
def list_repos() -> str:
    """List repositories for authenticated user"""
    try:
        user = gh.get_user()
        repos = user.get_repos()
        repoList = [f"- {repo.full_name}: {repo.description or 'No description'}" for repo in repos]
        return f"Repositories:\n" + "\n".join(repoList)
    except GithubException as e:
        return f"GitHub API Error: {e.data.get('message', str(e))}"
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def get_repo_info(repo_name: str) -> str:
    """
    Get detailed information about a repository
    Arg:
    repo_name: Full name of the repository (owner/repo)
    """
    try:
        repo = gh.get_repo(repo_name)
        info = f"""
                Repository: {repo.full_name}
                Description: {repo.description or 'No description'}
                Stars: {repo.stargazers_count}
                Forks: {repo.forks_count}
                Open issues: {repo.open_issues_count}
                Language: {repo.language or 'Not specified'}
                Date Created: {repo.created_at}
                Last Updated: {repo.updated_at}
                URL: {repo.html_url}
                """
        return info
    except GithubException as e:
        return f"GitHub API Error: {e.data.get('message', str(e))}"
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def list_issues(repo_name: str, state: str = "open") -> str:
    """
    List issues in a repository

    Args:
        repo_name: Full name of the repository (owner/repo)
        state: Issue state filter (open, closed, all)
    """
    try:
        repo = gh.get_repo(repo_name)
        issues = repo.get_issues(state=state)
        issueList = [f"#{issue.number}: {issue.title} ({issue.state})" for issue in list(issues)]
        return f"Issue state: {state}\n" + "\n".join(issueList)
    except GithubException as e:
        return f"GitHub API Error: {e.data.get('message', str(e))}"
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def create_issue(repo_name: str, title: str, body: str = "") -> str:
    """
    Create a new issue in a repository

    Args:
        repo_name: Full name of the repository (owner/repo)
        title: Issue title
        body: Issue description (optional)
    """
    try:
        repo = gh.get_repo(repo_name)
        issue = repo.create_issue(title=title, body=body)
        return f"Created issue #{issue.number}: {issue.title}\nURL: {issue.html_url}"
    except GithubException as e:
        return f"GitHub API Error: {e.data.get('message', str(e))}"
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def list_pull_requests(repo_name: str, state: str = "open") -> str:
    """
    List pull requests in a repository

    Args:
        repo_name: Full repository name (owner/repo)
        state: PR state filter (open, closed, all)
    """
    try:
        repo = gh.get_repo(repo_name)
        pullRequests = repo.get_pulls(state=state)
        pullRequestList = [f"#{pullRequest.number}: {pullRequest.title} ({pullRequest.state})" for pullRequest in list(pullRequests)]
        return f"Pull requests: ({state}):\n" + "\n".join(pullRequestList)
    except GithubException as e:
        return f"GitHub API Error: {e.data.get('message', str(e))}"
    except Exception as e:
        return f"Error: {str(e)}"
