# Kidney-Disease-Classification

## Project Workflows

1. Update config.yaml
2. Update secrets.yaml - optional
3. Update params.yaml
4. Update entity
5. Update the configuration manager in src config
6. Update componentss
7. Update the pipeline
8. Update main.py
9. Update dvc.yaml
10 Update app.py

# How to run?
### STEPS:

### Step 1 : Clone the github repository

Clone the repository

```bash
https://github.com/NikiKauliAIML/Kidney-Disease-Classification.git
```

### Step 2 : Create conda enviroments and activate

Create enviroments
```bash
conda create -n kidneyenv python=3.8 y
```

Activate enviroments
```bash
conda activate kidneyenv
```
### Step 3 : install the requirements.txt file
pip install -r requirement.txt


### Build code pipeline

1. Data Injestion - Add or retrive data from colud or drive and store in zip folder
2. 


#Error Faced during code
1. Data ingestion
    permission denied error beacuse or id access - write "url.split("/")[2]" instance of "url.split("/")[-2]"