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

## data-generator.py
- You could find the explaination of the code as comment in data-generator.py
- Note that data-generator.py is used to balence the given kaggle data. Since kaggle already have a lot of 0 hand data. So only hands from 1 to 9 can be added.
- Follow the instrcution from the program, insert the file name if your file is allocated in the same folder or insert the file path for the .csv file that you would like to have more data.
- The program would print out the number of each sets of each set.
- Input the number of poker card hands you want from 0 to 9.
- Wait for completion
- Output the file name that you would like to export. E.g. balence.csv

## oracles.py
- This script is used to identify the hands from the given csv file and it is coded by explicit rules of poker game
- You could find the explaination of the code as comment in oracles.py
- Follow the instruction from the program, insert the csv file name you want to identify. If your file is allocated in the same folder just type the name, otherwise insert the file path of the file.
- The program would scan the target csv file, print the row ID of the cards and its corresponding hands
- Output the file name that you would like to export. E.g. oracle_submission.csv

**Do note that these were all designed to work with the Jupyter Notebook for a clearer presentation of results, therefore there aren't that many print labels describing what is printed**
