# Misc

- Loading JSON data
    - http://www.markhneedham.com/blog/2015/07/23/neo4j-loading-json-documents-with-cypher/
    - https://neo4j.com/blog/cypher-load-json-from-url/



# Database Structure

## Conditions
Conditions are nodes.

- Labels
    - :Condition
- Properties
    - Name - The name of the condition.
    - AltNames - List of alternative names of the condition.
    - Description - A description of the condition.

## Measurements
Measurements are nodes.

- Labels
    - :Measurement
- Properties
    - Method - How the measurement is taken (e.g. serum, blood, fasting, total).
    - Description - A description of what the measurement measures and why you may want it measured.    

## Medications
Medications are nodes.

- Labels
    - :Medication
- Properties
    - Name - The primary identifier by which the medication is known (generic where possible).
    - PropNames - Any proprietary names for the medication.
    - GenericNames - Any generic names for the medication.
    - ModeOfAction - A description of how the medication acts and its effects.

## Treatments
Treatments are nodes.

- Labels
    - :Treatment
- Properties
    - Name - The name of the type of treatment (e.g. blood thinner, vasodilator).
    - Description - A description of what the treatment does and why it is used.

## References
References are nodes.

- Labels
    - :Reference
    - The source of the reference.
        - :Journal
        - :Website
- Properties
    - Title - Any title (such as a journal article title) associated with the reference.
    - WebAddress - A (preferably non-PDF) web address where the reference can be found.
    - Description - A brief description of the contents of the reference.

## Relationships
Relationships are edges. Recording relationships between nodes in the graph would ideally be done as a hyperedge, due to the
desire to connect the relationship with references. For example, condition A causes B according to references 1, 2, 3 and 4.
We would like to represent this by connecting the 6 nodes. This could be split into one relationship per reference like:

    A -> Description -> B
              ^
              |
            Ref 1
        
However, this would require the description for the relationship between A and B to be split across multiple nodes. Instead,
a list of references that support the single description will be kept as a property of the edge, with the references in the list
being specified using the IDs of the nodes.

- Labels
    - The tpe of the relationship
        - :TypeOf - When A is a type of B (e.g. type 1 diabetes mellitus is a type of diabetes mellitus).
        - :CauseOf - When condition A can cause condition B (e.g. end stage renal failure is a cause of kidney failure).
        - :ContributesTo - When condition A is a contributory factor for condition B (e.g. acute kidney injury contibutes to acute-on-chronic renal failure).
- Properties
    - Description - A description of the relationship (including references where needed). For example, how and why condition A causes condition B.
    - References - The IDs of the references used to determine the relationship.