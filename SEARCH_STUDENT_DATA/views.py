from django.shortcuts import render
from . import STUDENT_DATA as std
import warnings
warnings.filterwarnings("ignore")
from django.http import HttpResponse
from matplotlib import pyplot as plt
import numpy as np
# Create your views here.


def home(request):
    return render(request, 'STUDENT_DATA_SEARCH_PAGE.html')


"""
Q6.Make search page, where I will enter the student roll number and all the marks is displayed.
Answer:- 
        -> The request when received the roll number is extracted from the request. the request is sent to server 
         using GET method. The roll number is than searched in the main dataframe of student marks.
        -> Than the particular row is sent back to the html page using after converting to list.
        -> the list dat ais than entered into html table format using table tag and for loop in html.
        -> Below is the code for the same. 
"""

def search(request):
    data = std.df
    roll = request.GET['roll']
    roll = roll.upper()
    if roll == '':
        return render(request, 'STUDENT_DATA_SEARCH_PAGE.html', {'error': 'PLEASE ENTER THE ROLL NUMBER'})
    data_student = data[data['Rollno'] == roll]
    if data_student.empty:
        return render(request, 'STUDENT_DATA_SEARCH_PAGE.html', {'error': 'THERE IS NO SUCH ROLL NUMBER'})
    else:
        data_student = data_student.to_dict()
        # print(data_student)
        return render(request, 'STUDENT_DATA_SEARCH_PAGE.html',
                      {'student_data': data_student, 'headings1': list(data.columns)})

"""
Q4. CONTINUE
Answer:- The data of failed students was filtered and store in a a seperate dataframe df_FAIL in STUDENT_DATA.py. 
         This STUDENT_DATA.py is imported here and the data is accessed.
         
         -> First the df_FAIL is stored in data_fail.
         -> data_fail is converted to dictionary using to_dict() because to print the data in DJANGO HTML TABLE using
             for loop in django template we have to use dictionary format.
         -> The dictionary is then sent to the search page via 'render' function.
         -> There in STUDENT_DATA_SEARCH.html we use for loop (jinja format) to access the dictionary and the data 
            accessed is than  put into HTML table tag to be printed.
         -> Below is the function def fail(request) for the same.
         -> Click the list of failed students on page than the table will be shown.
"""
def fail(request):
    data_fail = std.df_FAIL
    data_fail_trans = data_fail.T
    # print(list(data_fail.columns))
    data_fail_dict = data_fail_trans.to_dict()
    # print(data_fail_dict)
    return render(request, 'STUDENT_DATA_SEARCH_PAGE.html',
                  {'student_data1': data_fail_dict, 'headings': list(data_fail.columns)})


def autopct_format(values):
    def my_format(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{v:d}'.format(v=val)
    return my_format

"""
Q5. Draw a pie chart which show the details of finally how many student get clear the course and
    how many of them are failed.
Answer:- The Pie chart is made for number of students passed and number of students failed the year. It is made using 
         matplotlib library. When you click the button on the html page to view the pie chart it will be shown.
"""
def pie(request):
    data_fail = std.df_FAIL
    index = data_fail.index
    number_of_rows = len(index)
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    status=['No. of passed students', 'No. of failed students']
    students=[300-number_of_rows,number_of_rows]
    ax.pie(students, labels=status, autopct= autopct_format(students))
    plt.show()
    return render(request, 'STUDENT_DATA_SEARCH_PAGE.html')

