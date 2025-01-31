import nox


@nox.session(python=["3.12"])
def tests(session):
    session.install("pytest")
    session.run("pytest")