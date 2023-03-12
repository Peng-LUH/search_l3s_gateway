"""Installation script for flask-api-tutorial application."""
from pathlib import Path
from setuptools import setup, find_packages

DESCRIPTION = (
    "Boilerplate Flask API with Flask-RESTx, SQLAlchemy, pytest, flake8, "
    "tox configured"
)
APP_ROOT = Path(__file__).parent
README = (APP_ROOT / "README.md").read_text()
AUTHOR = "Shengrui Peng"
AUTHOR_EMAIL = "peng@l3s.de"
# PROJECT_URLS = {
#     "Documentation": "https://aaronluna.dev/series/flask-api-tutorial/",
#     "Bug Tracker": "https://github.com/a-luna/flask-api-tutorial/issues",
#     "Source Code": "https://github.com/a-luna/flask-api-tutorial",
# }
INSTALL_REQUIRES = [
    "Flask==2.2.2",
    "Flask-Bcrypt",
    "Flask-Cors",
    "Flask-Migrate",
    "flask-restx",
    "Flask-SQLAlchemy",
    "PyJWT",
    "python-dateutil",
    "python-dotenv",
    "requests",
    "urllib3",
    "werkzeug",
    "markupsafe",
    "SQLAlchemy==1.4.0",
    "pytest-flake8==1.1.0",
    "flake8==3.9.2",
    "black",
]
EXTRAS_REQUIRE = {
    "dev": [
        "black",
        "flake8==3.9.2",
        "pre-commit",
        "pydocstyle",
        "pytest",
        "pytest-black",
        "pytest-clarity",
        "pytest-dotenv",
        "pytest-flake8==1.1.0",
        "pytest-flask",
        "tox",
    ]
}

setup(
    name="l3s_gateway",
    description=DESCRIPTION,
    long_description=README,
    long_description_content_type="text/markdown",
    version="0.1",
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=AUTHOR,
    maintainer_email=AUTHOR_EMAIL,
    license="MIT",
    url="",
    project_urls=PROJECT_URLS,
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.6",
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
)
