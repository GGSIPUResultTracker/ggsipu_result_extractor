import ggsipu_result
import os


CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)
RESOURCE_ROOT = os.path.join(PROJECT_ROOT, "Resources")

SUBJ_TXT = os.path.join(RESOURCE_ROOT, 'CSE_Result', "1.txt")
RES_TXT = os.path.join(RESOURCE_ROOT, 'CSE_Result', "58.txt")


with open(os.path.join(RESOURCE_ROOT, 'subjects.json'), 'w') as subjf, open(SUBJ_TXT, 'r') as inputfile:
    inputdata = inputfile.read()
    if ggsipu_result.has_page_subejcts(inputdata):
        subjects = list(ggsipu_result.iter_subjects(inputdata))
        subjf.write(ggsipu_result.toJSON(subjects))

with open(os.path.join(RESOURCE_ROOT, 'results.json'), 'w') as resf, open(RES_TXT, 'r') as inputfile:
    inputdata = inputfile.read()
    if ggsipu_result.has_page_results(inputdata):
        results = list(ggsipu_result.iter_results(inputdata))
        resf.write(ggsipu_result.toJSON(results))
