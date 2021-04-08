
# Your task will be to prepare a report summarizing the results of exams in maths, physics and biology. 
# The report should include the name of the exam, the number of candidates, the number of passed exams, the number of failed exams, 
    # and the best and the worst scores. All the data necessary to create the report is in the exam_results.csv file.
# Note that one candidate may have several results for the same exam. The number of candidates should express the number of unique 
    # people in each exam identified by Candidate ID. The final report should look like this:
'''
        Exam Name,Number of Candidates,Number of Passed Exams,Number of Failed Exams,Best Score,Worst Score
        Maths,8,4,6,90,33
        Physics,3,0,3,66,50
        Biology,5,2,3,88,23
'''

import csv
import pandas as pd

class MakeReport:
    def __init__(self):
        self.csvfile = 'exam_results.csv'
        self.header_names = ['Exam Name', 'Number of Candidates', 'Number of Passed Exams', 
                            'Number of Failed Exams', 'Best Score', 'Worst Score']

    def read_results_csv(self):
        self.current_dataframe = pd.read_csv(self.csvfile)
        print(self.current_dataframe)

    def prepare_report(self):
        self.read_results_csv()
        self.new_df = pd.DataFrame(columns=self.header_names)
        exam_names = self.current_dataframe.Exam_Name.unique()
        for exam in exam_names:
            participants = []       # Currently contains dupes
            passes, fails = 0, 0
            scores = []
            for ind in self.current_dataframe.index:
                if self.current_dataframe.Exam_Name[ind] == exam:
                    participants.append(self.current_dataframe.Candidate_ID[ind])
                    scores.append(self.current_dataframe.Score[ind])                    
                    if self.current_dataframe.Grade[ind] == 'Pass':
                        passes += 1
                    elif self.current_dataframe.Grade[ind] == 'Fail':
                        fails += 1

            num_students  = list(dict.fromkeys(participants))   # drop dupes from participants list         
            highest, lowest = max(scores), min(scores)
            data_struct = {'Exam Name': exam, 'Number of Candidates': len(num_students), 'Number of Passed Exams': passes, 
                            'Number of Failed Exams': fails, 'Best Score': highest, 'Worst Score': lowest}
            self.new_df = self.new_df.append(data_struct, ignore_index=True)
    
    def write_new_report(self):
        self.new_df.to_csv('exam_results_report.csv', index=False)




my_reader = MakeReport()
my_reader.prepare_report()
my_reader.write_new_report()