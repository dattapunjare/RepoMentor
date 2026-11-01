import requests


def parse_github_url(repo_url):
    """
    Extract owner and repository name from GitHub URL.
    """

    parts = repo_url.rstrip("/").split("/")

    if len(parts) < 2:
        return None, None

    owner = parts[-2]
    repo = parts[-1].replace(".git", "")

    return owner, repo


def get_repository_info(owner, repo):
    """
    Fetch basic repository information from GitHub.
    """

    url = f"https://api.github.com/repos/{owner}/{repo}"

    response = requests.get(url, timeout=15)

    if response.status_code == 200:
        return response.json()

    return None


def get_repository_files(owner, repo):
    """
    Fetch repository file structure.
    """

    url = (
        f"https://api.github.com/repos/"
        f"{owner}/{repo}/git/trees/HEAD?recursive=1"
    )

    response = requests.get(url, timeout=15)

    if response.status_code == 200:
        return response.json().get("tree", [])

    return None