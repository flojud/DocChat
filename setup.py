from setuptools import find_packages, setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Chat_with_my_docs",
    version="0.9.0",
    packages=find_packages("src"),
    package_dir={"": "src"},
    author="flojud",
    author_email="dev.flojud@gmail.com",
    description="Chat with your docs using langchain in a streamlit app with mistral or llama in ollama.",
    keywords="llama, mistral, chat, streamlit, langchain, talk2docs",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/flojud/chat-with-my-docs",
    install_requires=requirements,
    project_urls={
        "Bug Tracker": "https://github.com/flojud/chat-with-my-docs/issues",
    },
    entry_points={
        "console_scripts": [
            "chat_with_my_docs = __main__:app",
        ],
    },
    python_requires=">=3.10",
    license="MIT",
)
