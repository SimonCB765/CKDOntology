# Names

# Definition

- Anemia is a condition where there is a deficiency of red cells or of haemoglobin in the blood. It is a common feature of CKD, and increases in prevalence as kidney disease progresses, affecting nearly all patients with stage 5 CKD [ref][AJKDAnemiaCKD].

# Causes and Consequences

- Causes
    - Iron Deficiency Anemia
        - Iron deficiency anemia increases in prevalence as kidney function decreases. It is multifactoral in cause, but includes reduction in erythropoietin and hyperuricemia leading to bone marrow suppression.
        - Iron deficiency is common in patients with CKD, and leads to a reduction in formation of red cell haemoglobin, causing hypochromic microcytic anaemia.
        - Iron availability is controlled by the liver hormone hepcidin, which regulates dietary iron absorption and iron recycling. There are several feedback loops that control hepcidin levels, including iron and EPO.  In CKD patients (particularly in end stage kidney disease patients on hemodialysis), hepcidin levels have been found to be highly elevated, presumably due to reduced renal clearance, inflammation and many of them being prescribed ESA, which deplete the circulating iron pool by increasing erythropoiesis [ref][BabittAnemiaCKD].
- Consequences
    - Relative Erythropoietin Deficiency Anemia
        - The anaemia that goes with renal failure is mainly due to a deficiency of a hormone called erythropoietin (EPO), which is produced by the kidney to stimulate red blood cell production from the bone marrow.
        - In patients with CKD, normochromic normocytic anaemia (anemia where red blood cell size and mean corpuscular hemoglobin concentration respectively are normal) mainly develops from the inhibition of renal synthesis of EPO. In addition to anemia, this may lead to circulating uremic-induced inhibitors of erythropoiesis, shortened red blood cell lifespan and increased blood loss [ref][BabittAnemiaCKD].
        - The anaemia becomes more severe as the GFR decreases.

# Diagnosis and Treatment

- Diagnostics
    - Anemia Tests
        - Hematocrit
            - This is the ratio of the volume of red blood cells to the total volume of blood. A low hematocrit is indicative of anemia.
        - Hemoglobin
        - Red Blood Cell Count
    - Iron Level Tests
        - Ferritin
            - Ferritin is the body's primary store of iron. The amount of ferritin in the blood therefore shows how much iron is stored in your body. Low levels are indicative of an iron deficiency.
        - Serum Iron
            - This is low in anemic patients.
        - Total Iron-Binding Capacity (TIBC)
            - A test that measures the blood's capacity to bind iron with transferrin, and is therefore a measure of the amount of iron the blood can carry. This is high when there is an iron deficiency as the liver produces more transferrin, presumably attempting to maximize use of the little iron that is available.
        - Transferrin Saturation (TSAT)
            - This measures the percentage of transferrin that is saturated with iron. This value is low when there is an iron deficiency as there is insufficient iron to saturate all the transferrin.
        - Unsaturated Iron Binding Capacity (UIBC)
            - Similar to the TIBC, but with the serum iron subtracted. This is high in the presence of an iron deficiency.
- Treatments
    - Erythropoiesis Stimulating Agents
    - Iron Therapy (Iron Treatment, Iron Supplement)

# References

[AJKDAnemiaCKD]: http://www.ajkd.org/article/S0272-6386(06)00454-9/abstract ""
[BabittAnemiaCKD]: http://jasn.asnjournals.org/content/23/10/1631.full "Mechanisms of Anemia in CKD"

# Relationships

### Conditions
- Anemia
- Iron Deficiency Anemia
- Relative Erythropoietin Deficiency Anemia

### Diagnostics
- Ferritin
- Hematocrit
- Hemoglobin
- Red Blood Cell Count
- Serum Iron
- Total Iron-Binding Capacity (TIBC)
- Transferrin Saturation (TSAT)
- Unsaturated Iron Binding Capacity (UIBC)

### Treatments
- Erythropoiesis Stimulating Agents
- Iron Therapy (Iron Treatment, Iron Supplement)

### Edges
- Top Level Relationships
    - Iron Deficiency Anemia -[:TypeOf]-> Anemia
    - Relative Erythropoietin Deficiency Anemia -[:TypeOf]-> Anemia
- Diagnostic Relationships
    - Ferritin -[:DecreasedBy]-> Iron Deficiency Anemia
    - Hematocrit -[:DecreasedBy]-> Nephritic Syndrome
    - Hemoglobin -[:DecreasedBy]-> Nephritic Syndrome
    - Red Blood Cell Count -[:DecreasedBy]-> Nephritic Syndrome
    - Serum Iron -[:DecreasedBy]-> Iron Deficiency Anemia
    - Total Iron-Binding Capacity -[:IncreasedBy]-> Nephritic Syndrome
    - Transferrin Saturation -[:DecreasedBy]-> Iron Deficiency Anemia
    - Unsaturated Iron Binding Capacity -[:IncreasedBy]-> Nephritic Syndrome
- Treatment Relationships
    - Erythropoiesis Stimulating Agents -[:Treats]-> Relative Erythropoietin Deficiency Anemia
    - Iron Therapy -[:Treats]-> Iron Deficiency Anemia