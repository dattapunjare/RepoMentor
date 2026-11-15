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


def get_file_content(owner, repo, file_path):
    """
    Fetch the source code of a file from GitHub.
    """

    url = (
        f"https://api.github.com/repos/"
        f"{owner}/{repo}/contents/{file_path}"
    )

    response = requests.get(url, timeout=15)

    if response.status_code == 200:
        data = response.json()

        if data.get("type") == "file":
            import base64

            content = base64.b64decode(
                data["content"]
            ).decode("utf-8", errors="replace")

            return content

    return None
def get_all_python_files(owner, repo, file_tree):
    """
    Fetch source code from all Python files in a repository.

    Returns a dictionary:
    {
        "app.py": "source code...",
        "utils/helper.py": "source code..."
    }
    """

    python_files = {}

    for file in file_tree:

        file_path = file.get("path", "")

        # Only process Python files
        if file_path.endswith(".py"):

            content = get_file_content(
                owner,
                repo,
                file_path
            )

            if content is not None:
                python_files[file_path] = content

    return python_files