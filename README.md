# Database Structure

A property with a * in front of it is the unique identifier by which a node is referenced.

## Conditions
Conditions are nodes.

- Labels
    - :Condition
- Properties
    - alternativeNames - List of alternative names of the condition.
    - description - A description of the condition.
    - *id - The short form name by which the condition is referenced.
    - name - The name of the condition.

## Diagnostics
Diagnostics are nodes.

- Labels
    - :Diagnostic
- Properties
    - alternativeNames - The alternative names of the diagnostic.
    - description - A description of what the diagnostic measure is and why you may want to use it.
    - method - Ways of performing the procedure that are of interest (e.g. serum, blood, fasting, total, MRI).
    - *name - The name of the entity being measured (e.g. blood glucose, eGFR, kideny biopsy).

## Relationships
Relationships are edges.

    A -[Rel]-> B

- Labels
    - The type of the relationship
        - :CausedBy - When condition A is caused by condition B (e.g. end stage renal failure is a cause of kidney failure).
        - :ContributesTo - When condition A is a contributory factor for condition B (e.g. acute kidney injury contibutes to acute-on-chronic renal failure).
        - :DecreasedBy - When measurement A decreases due to condition B.
        - :Diagnoses - When A is used to diagnose B.
        - :IncreasedBy - When measurement A increases due to condition B.
        - :Treats - When treatment A treats condition B.
        - :TypeOf - When A is a type of B (e.g. type 1 diabetes mellitus is a type of diabetes mellitus).
- Properties
    - description - A description of the relationship (including references where needed). For example, how and why condition A causes condition B.

## Treatments
Treatments are nodes.

- Labels
    - :Treatment
- Properties
    - description - A description of what the treatment does, how it does what it does, why it is used and what its effect is.
    - genericNames - Non-proprietary names for the treatment.
    - *name - The primary identifier by which the treatment is known (a non-proprietary name where possible).
    - propNames - Any proprietary names for the treatment.