import nox


@nox.session(python=["3.12"], tags=["gh_tests"])
def tests(session):
    session.log("Running tests")

@nox.session( tags=["gh_tests"])
def tests2(session):
    session.log("Running tests 2")

@nox.session( tags=["gh_docs"])
def docs(session):
    session.log("Running docs 1")

@nox.session( tags=["gh_docs"])
def docs2(session):
    session.log("Running docs 2")

@nox.session( tags=["gh_docker"])
def docker(session):
    session.log("Running docker")