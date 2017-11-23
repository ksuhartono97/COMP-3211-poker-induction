# COMP-3211-poker-induction
Solving a kaggle competition: https://www.kaggle.com/c/poker-rule-induction as a course project

Project is being attempted with Python.

## Usage instructions:
- Ensure that the dependencies are installed. These dependencies are:
  - pip
  - numpy
  - sklearn (pip install -U scikit-learn)
  - imblearn (pip install imblearn)
  - pandas (pip install pandas)
  - sklearn-deap (pip install sklearn-deap)
  - Jupyter Notebook (this one is optional, can either use this or just run the python file)
- You can run each of the files by doing `python <filename>` or running `jupyter notebook` in the directory then opening each of the notebooks.
  - `FinalGenerator` : is used to generate the results for submission
  - `DeapSearchParams`: is used to do the evolutionary search on the classifier parameters
  - `ClassifierComparisons`: is a comparison of different classifiers
  - `BenchmarkingRFE`: are our testing logs of for the best number of features from RFE
  - `BenchmarkOverunderSampling`: is our trials on the SMOTE and SMOTETomek

  **Do note that these were all designed to work with the Jupyter Notebook for a clearer presentation of results, therefore there aren't that many print labels describing what is printed**
