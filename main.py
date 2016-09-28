"""Create the Neo4j database representing the CKD ontology."""

# Python imports.
import json

# 3rd party imports.
import neo4j.v1 as neo

# User imports.
import conf


def main():

    # Get access to the database.
    driver = neo.GraphDatabase.driver(conf.databaseURI, auth=neo.basic_auth(conf.username, conf.password))

    # Clear the database.
    session = driver.session()
    session.run("MATCH (n) DETACH DELETE n")
    session.close()

    # ------------------------------ #
    # Create Constraints and Indices #
    # ------------------------------ #
    session = driver.session()
    constraintTransaction = session.begin_transaction()
    constraintTransaction.run("CREATE CONSTRAINT ON (c:Condition) ASSERT c.name IS UNIQUE")
    constraintTransaction.run("CREATE CONSTRAINT ON (m:Measurement) ASSERT m.name IS UNIQUE")
    constraintTransaction.run("CREATE CONSTRAINT ON (r:Reference) ASSERT r.id IS UNIQUE")
    constraintTransaction.run("CREATE CONSTRAINT ON (t:Treatment) ASSERT t.name IS UNIQUE")
    constraintTransaction.commit()
    session.close()

    # -------------- #
    # Add Conditions #
    # -------------- #
    fid = open("Conditions.json", 'r')
    conditionData = json.load(fid)
    fid.close()
    query = "WITH {json} AS data " \
            "UNWIND data as cond " \
            "CREATE (c:Condition {name: cond.name})"
    result = session.run(query, {"json": conditionData})
    session.close()


    print([i for i in result])



    # ---------------- #
    # Add Measurements #
    # ---------------- #

    # --------------- #
    # Add Medications #
    # --------------- #

    # -------------- #
    # Add References #
    # -------------- #

    # -------------- #
    # Add Treatments #
    # -------------- #

    # ----------------- #
    # Add Relationships #
    # ----------------- #


if __name__ == "__main__":
    main()
