import nox


@nox.session(python=["3.11", "3.10", "3.8"])
def tests(session):
    args = session.posargs or ["--cov"]
    session.run("poetry", "install", external=True)
    session.run("pytest", *args)