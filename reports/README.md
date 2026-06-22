this folder contains weekly reports, metrics, and final documentation.

# Data Cleaning Report

## Project: Multi-Agent AI System for Academic Assistance

## Tools Used
- Python 3.14
- Pandas library
- Jupyter Notebook (VS Code)

## Cleaning Steps Applied to All Datasets
1. Removed duplicate rows
2. Filled missing values with 'unknown'
3. Standardized text formatting (lowercase, trimmed whitespace)

## Before vs After Summary

| Dataset              | Raw Rows | Cleaned Rows | Rows Removed |
|----------------------|----------|--------------|--------------|
| academic_ai_excel    | 12       | 12           | 0            |
| ai_anxiety           | 15,000   | 15,000       | 0            |
| coursea_data         | 891      | 891          | 0            |
| essay_assistance     | 8        | 8            | 0            |
| python_faq           | 21,677   | 21,677       | 0            |
| qa_interactions      | 12       | 12           | 0            |
| student_por          | 649      | 649          | 0            |
| studentAssessment    | 173,912  | 173,912      | 0            |
| students_performance | 1,000    | 1,000        | 0            |
| study_schedules      | 10       | 10           | 0            |

## Observations
- No duplicate rows were found across any dataset
- Missing values were handled by filling with 'unknown'
- The largest dataset was studentAssessment with 173,912 rows
- All datasets are now stored in data/cleaned/ folder
- Total records processed: 213,183 rows across 10 datasets