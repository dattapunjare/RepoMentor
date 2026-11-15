
import streamlit as st

from github_service import (
    parse_github_url,
    get_repository_info,
    get_repository_files,
    get_file_content
)

from ai_service import explain_code


st.set_page_config(
    page_title="RepoMentor",
    page_icon="📂",
    layout="wide"
)

st.title("📂 RepoMentor")
st.subheader("AI-Powered GitHub Repository Assistant")

st.write(
    "Understand, explore and analyze GitHub repositories "
    "with the help of Artificial Intelligence."
)

st.divider()

repo_url = st.text_input(
    "Enter GitHub Repository URL",
    placeholder="https://github.com/username/repository"
)

if st.button("Analyze Repository", type="primary"):

    if not repo_url.strip():
        st.warning("Please enter a GitHub repository URL.")

    else:
        owner, repo = parse_github_url(repo_url.strip())

        if not owner or not repo:
            st.error("Invalid GitHub repository URL.")

        else:
            with st.spinner("Fetching repository information..."):
                repo_info = get_repository_info(owner, repo)
                repo_files = get_repository_files(owner, repo)

            if repo_info is None:
                st.error("Could not fetch repository information.")

            else:
                st.session_state["owner"] = owner
                st.session_state["repo"] = repo
                st.session_state["repo_info"] = repo_info
                st.session_state["repo_files"] = repo_files

                # Clear previous file and AI results
                st.session_state.pop("file_content", None)
                st.session_state.pop("ai_explanation", None)


if "repo_info" in st.session_state:

    repo_info = st.session_state["repo_info"]
    repo_files = st.session_state["repo_files"]
    owner = st.session_state["owner"]
    repo = st.session_state["repo"]

    st.success("Repository fetched successfully!")

    st.header(repo_info["full_name"])

    st.write(
        repo_info.get("description")
        or "No description available."
    )

    col1, col2, col3 = st.columns(3)

    col1.metric("⭐ Stars", repo_info.get("stargazers_count", 0))
    col2.metric("🍴 Forks", repo_info.get("forks_count", 0))
    col3.metric("🐛 Open Issues", repo_info.get("open_issues_count", 0))

    st.write(
        "**Programming Language:**",
        repo_info.get("language") or "Not specified"
    )

    st.write("**Repository URL:**", repo_info.get("html_url"))

    st.divider()

    st.header("📁 Repository Explorer")

    if repo_files is None:
        st.error("Could not fetch repository files.")

    else:
        file_items = [
            item for item in repo_files
            if item.get("type") == "blob"
        ]

        st.write(f"Total files: {len(file_items)}")

        search = st.text_input(
            "🔍 Search for a file",
            placeholder="Example: README.md"
        )

        filtered_files = [
            item["path"]
            for item in file_items
            if search.lower() in item["path"].lower()
        ]

        if filtered_files:

            selected_file = st.selectbox(
                "Select a file to explore",
                filtered_files
            )

            if st.button("View Source Code"):

                with st.spinner("Loading file content..."):
                    content = get_file_content(
                        owner, repo, selected_file
                    )

                if content is not None:
                    st.session_state["file_content"] = content
                    st.session_state["selected_file"] = selected_file
                    st.session_state.pop("ai_explanation", None)
                else:
                    st.error("Could not load this file.")

        else:
            st.info("No matching files found.")

    # Display selected source code
    if "file_content" in st.session_state:

        st.divider()

        st.subheader(
            f"📄 {st.session_state['selected_file']}"
        )

        st.code(
            st.session_state["file_content"],
            language="python"
        )

        # AI explanation
        st.divider()
        st.subheader("🤖 AI Code Explanation")

        if st.button("Explain Code with Qwen AI"):

            with st.spinner(
                "Qwen is analyzing your source code..."
            ):
                explanation = explain_code(
                    st.session_state["file_content"]
                )

                st.session_state["ai_explanation"] = explanation

        if "ai_explanation" in st.session_state:
            st.markdown(st.session_state["ai_explanation"])
