import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

list_of_files=[
    "README.md",
    "requirements.txt",
    "run_pipeline.py",
    f"config/path.yaml",
    f"config/params.yaml",
    f"ingestion/load_with_pathway.py",
    f"chunking/narrative_chunker.py",
    f"retrieval/evidence_retriever.py",
    f"claims/backstory_parser.py",
    f"reasoning/constraint_checker.py",
    f"decision/final_classifier.py",
    f"evaluation/sanity_checker.py",
    f"dataset/dataset.csv",
    f"docs/claim_types.md",
    f"docs/contradiction_rules.md",
    f"output/output.csv"
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating Directory;{filedir} for the file: {filename}")

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")