"""Module to contain all globally accessible settings-like variables."""

# Global variables provided.
databaseURI = "bolt://localhost:7687/"
password = "root"
username = "neo4j"


def init_database_location(URI):
    """Initialise the location of the database.

    :param URI:     The URI of the Neo4j database.
    :type URI:      str

    """

    global databaseURI
    databaseURI = URI

def init_user(user=None, passW=None):
    """Initialise the username and password for the Neo4j database.

    :param user:    The username to use when logging into the database.
    :type user:     str
    :param passW:   The password to use when logging into the database.
    :type passW:    str

    """

    if user:
        global username
        username = user
    if passW:
        global password
        password = passW
