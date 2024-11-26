import os
import json

class Student():
    
        def __init__(self):
            os.system('CLS')
            self.name = input("Please enter the student name:")
            self.section = input("Please enter the class section:")
            self.spanish_score = int(input("Please enter the spanish score:"))
            while self.spanish_score > 100 or self.spanish_score < 0:
                self.spanish_score= int(input("Invalid input, please enter a valid score for spanish:"))
            self.english_score = int(input("Please enter the english score:"))
            while self.english_score > 100 or self.english_score < 0:
                self.english_score = int(input("Invalid input, please enter a valid score for english:"))
            self.social_studies_score = int(input("Please enter the social studies score:"))
            while self.social_studies_score > 100 or self.social_studies_score < 0:
                self.social_studies_score = int(input("Invalid input, please enter a valid score for social studies:"))
            self.science_score = int(input("Please enter the science score:"))        
            while self.science_score > 100 or self.science_score < 0:
                self.science_score = int(input("Invalid input please enter a valid score for science:"))
            self.average = self.calculate_student_average(self.spanish_score,self.english_score,self.social_studies_score,self.science_score)

        def create_student_list_info(self,student_name,section,score_1,score_2,score_3,score_4):
            self.student_list = []
            self.student_list.append(student_name)
            self.student_list.append(section)
            self.student_list.append(score_1)
            self.student_list.append(score_2)
            self.student_list.append(score_3)
            self.student_list.append(score_4)
            self.student_list.append(self.calculate_student_average(score_1,score_2,score_3,score_4))
            return self.student_list

        def calculate_student_average(self,score_one,score_two,score_three,score_four):
            try:
                return(score_one + score_two + score_three + score_four)/4
            except ValueError as error:
                print(f"An error occurred in calculate_average_note due to {error}")



def top_three_best_students(input_list):
    os.system('CLS')
    print("\n\n\n###TOP 3 Best students###\n\n")
    best_average = 0
    second_average = 0
    third_average = 0
    best_student = ''
    second_student = ''
    third_student = ''
    try:    
        for index , record in enumerate(input_list):
                current_average =  record[record.index(record[6])]
                if current_average > best_average and current_average > second_average and current_average > third_average:
                    if(best_average < current_average):
                        if second_average > third_average:
                            third_average = second_average
                            third_student = second_student
                        second_average = best_average
                        second_student = best_student
                    best_average = current_average
                    best_student = record[record.index(record[0])]
                    
                elif current_average < best_average and current_average > second_average and current_average > third_average:
                    if second_average > third_average:
                        third_average = second_average
                        third_student = second_student
                    second_average = current_average
                    second_student = record[record.index(record[0])]
                elif current_average < best_average and current_average < second_average and current_average > third_average:
                    third_average = current_average
                    third_student = record[record.index(record[0])]
            
        print(f"The best average corresponds to {best_student} with an average of {best_average}, the second best average corresponds to {second_student} with an average of {second_average} and the third best average corresponds to {third_student} with an average of {third_average}")
    except ValueError as error:
        print(f"An error occurred in top_three_best_students function due to:{error}")
    except IndexError as inderr:
        print(f"An error occurred in top_three_best_students function due to:{inderr}")


def show_student_averages(input_list):
    os.system('CLS')
    try:
        print("\n\n\n###Average list per student###\n\n")
        for index , record in enumerate(input_list):
            student = record[record.index(record[0])]
            current_average = record[record.index(record[6])]
            print(f"\n* {student} with an average of {current_average}")
    except IndexError as indxerr:
        print(f"An error occurred in show_student_averages function due to:{indxerr}")    


def return_json_format(some_input):
        return json.dumps(some_input , indent=4)


def convert_list_to_dict(input_list):
    group_dict = []
    counter = 0
    for index,record in enumerate(input_list):
        new_dict = {}
        for i in range (0,len(record),7):
            new_dict["Name"] = record[i]
            new_dict["Classroom"] = record[i + 1]  
            new_dict["Spanish_Score"] = record[i + 2] 
            new_dict["English_Score"] = record[i + 3]
            new_dict["Social_Studies_Score"] = record[i + 4]
            new_dict["Science"] = record[i + 5]
            new_dict["Average"] = record[i + 6]
        group_dict.append(new_dict)
        counter = counter + 1
    return group_dict
