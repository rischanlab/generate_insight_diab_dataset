# Generate insights from diabetes dataset using deviation-based approach

Dataset:  https://archive.ics.uci.edu/ml/datasets/Diabetes+130-US+hospitals+for+years+1999-2008

This result using diabetes clean version dataset: see https://github.com/rischanlab/Cleaning_diabetes_130_US_hospital_dataset

Example target and reference query that we used, 4 aggregate functions are used (avg, max, sum, count): 

### Target query: `select A, M(F) from diabetes where readmitted = 'NO' group by A` (subset readmitted = NO)
### Reference query: `select A, M(F) from diabetes group by A` (whole dataset)

Top-10 insights as shown in Figure below

![Image of Top10 Insights](https://raw.githubusercontent.com/rischanlab/generate_insight_diab_dataset/master/results_screenshoot/top-10-insights.JPG)

Example plot target and reference views from top-k 

num_emergency means emergency visits in the year before the hospitalization

## Target view I

![Image of Target view](https://raw.githubusercontent.com/rischanlab/generate_insight_diab_dataset/master/results_screenshoot/target1.JPG)

## Reference view I 

![Image of Target view](https://raw.githubusercontent.com/rischanlab/generate_insight_diab_dataset/master/results_screenshoot/ref1.JPG)


## Target view 2

![Image of Target view](https://raw.githubusercontent.com/rischanlab/generate_insight_diab_dataset/master/results_screenshoot/target2.JPG)

## Reference view 2

![Image of Target view](https://raw.githubusercontent.com/rischanlab/generate_insight_diab_dataset/master/results_screenshoot/ref2.JPG)


## Target view 3

![Image of Target view](https://raw.githubusercontent.com/rischanlab/generate_insight_diab_dataset/master/results_screenshoot/insulin_target.JPG)

## Reference view 3

![Image of Target view](https://raw.githubusercontent.com/rischanlab/generate_insight_diab_dataset/master/results_screenshoot/insilin_ref.JPG)
