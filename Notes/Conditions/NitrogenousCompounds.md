# Overview

In CKD kidney function declines. This result in a build up of nitrogenous compounds in the blood, in particular uric acid. This build up results in hyperuricemia and azotemia. Further complications, such as uremia and gout, can arise as the level of waste products builds up. As both gout and hyperuricemia are known to speed the progression of CKD, and potentially cause it, this can result in further damage to the kidneys and an increase in waste compounds in the blood.

# Conditions

- Azotemia
    - Causes
        - In CKD levels of nitrogen-containing compounds (e.g. urea, creatinine, nitrogenous byproducts of breaking down proteins and amino acids) in the blood increase due to decreasing kidney function.
    - Consequences
        - Uremia
            - Azotemia can lead to uremia if left untreated.
    - Diagnostics
        - Blood Urea Nitrogen (BUN)
            - Will be increased in patients with azotemia.
        - Creatinine
            - Will be increased in patients with azotemia.
    - Treatments
        - Diuretics
        - Treat Underlying Cause
- Gout
    - Causes
        - Gout is present in almost 40% of people with CKD [ref][KrishnanGout]. It is caused by the build up of uric acid in the blood, which then forms crystals in the soft tissue. People with CKD are susceptible to this as their kidneys do not filter the blood as well, leading to the build up of uric acid needed for gout.
    - Consequences
        - CKD
            - The crystals deposited in gout can cause scarring of the kidney.
        - Kidney Failure
            - The crystals deposited in gout can cause obstructions and scarring of the kidney, potentially causing kidney failure.
        - Kidney Stones (Renal Lithiasis, Nephrolithiasis, Renal Calculi)
            - The uric acid crystals deposited in gout can form stones within the kidney.
    - Diagnostics
        - 24 Hour Uric Acid Clearance
        - Joint Fluid Test
        - Serum Uric Acid
        - Uric Acid:Creatinine Ratio
    - Treatments
        - Colchicine
        - Corticosteroids
        - Diet
        - NSAIDs
        - Xanthine Oxidase Inhibitors
            - Examples
                - Purine Analogues: Allopurinol, Oxypurinol, Tisopurine, etc.
                - Others: Febuxostat, Topiroxostat, etc.
            - These drugs inhibit the activity of xanthine oxidase, an enzyme involved in purine metabolism, thereby reducing the production of uric acid.
- Hyperuricemia
    - Causes
        - Hyperuricemia is an abnormally high level of uric acid in the blood. As CKD is associated with decreased excretion of uric acid it often results in hyperuricemia. the progressive decline in GFR results in a decrease in uric acid clearance.
    - Consequences
        - CKD
            - Hyperuricemia can cause CKD to progress quicker, and is often seen to precede CKD [ref][JohnsonUricAcid].
        - Uric Acid Nephropathy (i.e. Gouty Nephropathy, Urate Nephropathy)
            - Acute Uric Acid Nephropathy
            - Chronic Urate Nephropathy
            - Uric Acid Nephrolithiasis
    - Diagnostics
        - 24 Hour Uric Acid Clearance
        - Serum Uric Acid
        - Uric Acid:Creatinine Ratio
    - Treatments
        - Dietary
        - Lifestyle
- Uremia
    - Causes
         - Uremia is a result of the buildup in the blood of waste products that are usually excreted in the urine. In CKD this is a result of the decrease in kidney function.
    - Consequences
    - Diagnostics
        - Blood Urea Nitrogen (BUN)
            - Will be increased in uremic patients.
        - Creatinine
            - Will be increased in uremic patients.
    - Treatments
        - Dialysis
        - Treat Underlying Cause

# References

[KrishnanGout]: https://www.ncbi.nlm.nih.gov/pubmed/18260174 "Gout in ambulatory care settings in the United States"
[JohnsonUricAcid]: https://www.ncbi.nlm.nih.gov/pubmed/23543594 "Uric acid and chronic kidney disease: which is chasing which?"

# Relationships

### Conditions
- Acute Uric Acid Nephropathy
- Azotemia
- Chronic Urate Nephropathy
- CKD
- Gout
- Hyperuricemia
- Kidney Failure
- Kidney Stones
- Uremia
- Uric Acid Nephrolithiasis

### Diagnostics
- 24 Hour Uric Acid Clearance
- Blood Urea Nitrogen (BUN)
- Creatinine
- Joint Fluid Test
- Serum Uric Acid
- Uric Acid:Creatinine Ratio

### Treatments
- Colchicine
- Corticosteroids
- Diuretics
- Dialysis
- NSAIDs
- Xanthine Oxidase Inhibitors

### Edges
- Primary Conditions
    - Acute Uric Acid Nephropathy -[:TypeOf]-> Uric Acid Nephropathy
    - Azotemia -[:ContributesTo]-> Uremia
    - Chronic Urate Nephropathy -[:TypeOf]-> Uric Acid Nephropathy
    - Gout -[:ContributesTo]-> CKD
    - Gout -[:ContributesTo]-> Kidney Failure
    - Gout -[:ContributesTo]-> Kidney Stones
    - Hyperuricemia -[:ContributesTo]-> CKD
    - Hyperuricemia -[:ContributesTo]-> Uric Acid Nephropathy
    - Uric Acid Nephrolithiasis -[:TypeOf]-> Uric Acid Nephropathy
- Diagnostic Relationships
    - 24 Hour Uric Acid Clearance -[:DecreasedBy]-> Gout
    - 24 Hour Uric Acid Clearance -[:DecreasedBy]-> Hyperuricemia
    - Blood Urea Nitrogen -[:IncreasedBy]-> Azotemia
    - Blood Urea Nitrogen -[:IncreasedBy]-> Uremia
    - Creatinine -[:IncreasedBy]-> Azotemia
    - Creatinine -[:IncreasedBy]-> Uremia
    - Joint Fluid Test -[:Diagnoses]-> Gout
    - Serum Uric Acid -[:IncreasedBy]-> Gout
    - Serum Uric Acid -[:IncreasedBy]-> Hyperuricemia
    - Uric Acid:Creatinine Ratio -[:DecreasedBy]-> Gout
    - Uric Acid:Creatinine Ratio -[:DecreasedBy]-> Hyperuricemia
- Treatment Relationships
    - Colchicine -[:Treats]-> Gout
    - Corticosteroids -[:Treats]-> Gout
    - Dialysis -[:Treats]-> Uremia
    - Diuretics -[:Treats]-> Azotemia
    - NSAIDs -[:Treats]-> Gout
    - Xanthine Oxidase Inhibitors -[:Treats]-> Gout