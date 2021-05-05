This is a mini-project which focuses on Attrition Rate among employees 
in any organisation and how to find sentiments among the employees in
relation to the organisation in which they work.

A basic django website is build in which people can answer some basic 
questions that will help in finding sentiments and if they are positive
or not. A file can be uploaded by HR department employee or the Employer 
himself/herself through which I would predict the Attrition Rate among
employees and show the result on the website itself.
Through the questions then the employer can find out where the organisation
lacks and th reasoning behind the attrition rate(if it is high).

*IMPORTANT*
Firstly most of the models trained have been storing their data in
the form of pickle files, in the code most of the pickle related code has been
commented out. If you are running this code for the first time, then uncomment
out the pickle code and run. The folders for pickle have been made, you
just have to run the code once. Check files -> Trial.py and
Attrition/views.py.
If warning is been shown then use older version of pickle package.

Requirement.txt has some unwanted packages in them *teehee* sorry, kinda
messed my virtual envs there. But mostly you would need ml packages, nlp
packages(nltk) and django packages.

A folder named Reviews is given, it has dataset which is used to train moel for
sentiment analysis.


For the working of the website:
1. A person most probably Employer or HR directive will access to login into
the account made for him/her.
2. This person can do two things: one is go see results of the questionnaire
for which the employees must have answered to see if the reviews were positive
or negative, second is upload a file(excel sheet) in regard to data from
which I will then find Attrition Rate for that organisation or Employer.
3. The result is shown on the page result(duh!) and then files that are
uploaded are safe and only accessible to the person who has uploaded and
no one else.
4. Most of the data is stored in PostgreSQL.
