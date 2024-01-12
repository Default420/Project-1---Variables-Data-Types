# -*- coding: utf-8 -*-
"""Copy of Applied_Tech_Project_1_Question_copy_v1.2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ddHT5CGZ8dK0PTHXmmu8x6FMgpDpBBiW

### Instructions

#### Goal of the Project

This project is designed for you to practice and solve the activities that are based on the concepts covered in the following lessons:

 1. Variables and Data-Types

---

#### Getting Started:

1. Click on the following link to open the Colab file for this project.

   https://colab.research.google.com/drive/1tDpcC4RFE-ux53Q0ZM6ai7R9GhObvXQF  

2. Create a duplicate copy of the Colab file as described below.

  - Click on the **File menu**. A new drop-down list will appear.

   <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/lesson-0/0_file_menu.png' width=500>

  - Click on the **Save a copy in Drive** option. A duplicate copy will get created. It will open up in the new tab on your web browser.

  <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/lesson-0/1_create_colab_duplicate_copy.png' width=500>

3. After creating the duplicate copy of the notebook, please rename it in the **YYYY-MM-DD_StudentName_Project1** format.

4. Now, write your code in the prescribed code cells.

---

### Activities

#### Activity 1: Printing name and hobby

Here you need to get the name and favourite hobby from the user and display it

For example:

             Enter your name : Sam
             Enter your favourite hobby : cycling
             Hello Sam, your favourite hobby is cycling

Follow the steps given below to achieve the desired result:

  - **Step 1:** Ask the user to enter his/her name using the `input()` function and store it in the `name` variable.

  - **Step 2:** Ask the user to enter his/her favourite hobby using the `input()` function and store it in the `hobby` variable.

  - **Step 3:** Print the values of `name` and `hobby` variables using the `print()` function.

**Hint**: `print("Hello", name,", your favourite hobby is", hobby)`
"""

# Write your code here
# Step 1: Get name from user and store it in variable 'name'
name = input("Enter your name:")
# Step 2: Get hobby from user and store it in variable 'hobby'
hobby = input("Enter a hobby:")
# Step 3: Print name and hobby
print(name)
print(hobby)

"""---

#### Activity 2: Display the total marks scored in 3 subjects

Calculate the total marks scored in 3 subjects (100 marks each) and display the score out of 300 marks.

For example:

    english = 56
    maths = 73
    science = 79
    Total Marks = 208

Follow the steps given below to achieve the desired result:

- **Step 1:** Declare three variables `english`, `maths` and `science` respectively and store any numerical values in it.

- **Step 2:** Calculate the total marks by adding the values stored in the variables using the `+` operator. Store the result in the variable `total`.

- **Step 3:** Print the total score.
"""

# Write your code here
# Step 1: Declare three variables 'english', 'maths' and 'science' respectively and store any numerical values in it
english = 56
math = 73
science = 79
# Step 2: store their sum in 'total' variable
total = english + math + science
# Step 3: Use the 'print()' function to display the total marks
print("Total marks:",total)

"""---

### Submitting the Project:

1. After finishing the project, click on the **Share** button on the top right corner of the notebook. A new dialog box will appear.

  <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/project-share-images/2_share_button.png' width=500>

2. In the dialog box, make sure that '**Anyone on the Internet with this link can view**' option is selected and then click on the **Copy link** button.

   <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/project-share-images/3_copy_link.png' width=500>

3. The link of the duplicate copy (named as **YYYY-MM-DD_StudentName_Project1**) of the notebook will get copied

   <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/project-share-images/4_copy_link_confirmation.png' width=500>

4. Go to your dashboard and click on the **My Projects** option.
   
   <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/project-share-images/5_student_dashboard.png' width=800>

  <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/project-share-images/6_my_projects.png' width=800>

5. Click on the **View Project** button for the project you want to submit.

   <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/project-share-images/7_view_project.png' width=800>

6. Click on the **Submit Project Here** button.

   <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/project-share-images/8_submit_project.png' width=800>

7. Paste the link to the project file named as **YYYY-MM-DD_StudentName_Project1** in the URL box and then click on the **Submit** button.

   <img src='https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/images/project-share-images/9_enter_project_url.png' width=800>

---
"""