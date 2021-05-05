# eVANTAGE

# Attrition Rate Website

### This is a project which focuses on Attrition Rate among employees in any organisation and how to find sentiments among the employees in relation to the organisation in which they work.

A `(django-backend)` website is build in which people can answer some basic questions that will help in finding sentiments and if they are positive or not. A file can be uploaded
by HR department employee or the Employer himself/herself through which I would use to predict the **Attrition Rate** among employees and show the result on the website itself. Through the questions then the employer can find out where the organisation lacks and th reasoning behind the attrition rate(if it is high).

## For the working of the website:
- A person most probably Employer or HR directive will access to login into the account made for him/her.
- This person can do two things: one is go see results of the questionnaire for which the employees must have answered to see if the reviews were positive or negative, second 
   is upload a file(excel sheet) in regards to receive the data for `predicting Attrition Rate`.
   
The website has 4 main pages, the login page where only the HR or Employer can login from where he/she is directed to main page of the website. There he/she gets the above two 
options. Only the people who has login access can see results of the sentiment analysis on employees and predictions of Attrition Rate.
The website has a page for questionnaire which is accessible to all where employees can answer the questions put together by the HR/Employer.
The last is the result page where the result of the data processing is shown(both sentiment and attrition prediction.)


**IMPORTANT**:
README.txt has directives as to how to use this project's code and train model(used in sentiment analysis) using the provided data.

**Update**:
The website has been modified so that now the user can can fill up a form asking for details on an employee which is used to determine if the person would attrite. Note this is different since instead of batch - processing for data that was uploaded by Employer/ HR for finding Attrtion among employees here we take-in single employee' data and find if he/she would attrite.
