# PDF-Analytics
App that read PDF file from the internet and return basic analytics about the PDF
# Project Planning
PDF is the most prominent format online for legal documents, science paper or engineering brochure, 
etc.  With PDF-Analytics, a user can get a quick summery on the PDF, such as word count and the top 
10 most used words in the paper.  This is a cupcake project that will eventually evolve into a 
wedding cake that will draw summaries on the article similar to what autotldr bot on reddit 
(https://www.reddit.com/user/autotldr).

## Problem Statement

PDF is a great way for human to read a report, but it is very hard for a user to compare and contrast
methodology or ideas for different documents.  This project is an attempt to draw insight into PDF
files so that we can compare and contrast different and see if there is any similar patterns

### Primary User

User who would like to get basic analytics about a PDF document in the internet.

### User Needs Statement 

PDF is the most prominent format online for legal documents, science paper or engineering brochure, 
etc.  With PDF-Analytics, a user can get a quick summery on the PDF, such as word count and the top 
10 most used words in the paper.  This is a cupcake project that will eventually evolve into a 
wedding cake that will draw summaries on the article similar to what autotldr bot on reddit 
(https://www.reddit.com/user/autotldr).

### As-is Process Description

  1. Ask user to provide a csv file with a list of pdf addresses on local machine or the Internet
  2. For each PDF in local machine
      Parse the PDF and obtain the text from the documents
  3. For each PDF in the internet
      Visit its URL in a browser.
      download the PDF and save in a local directory.
      Repeat step 2
      

### To-be Process Description

  1. Obtain a list of directories via a csv format.
  2. Distingish between the directories and determine if it is online or local
  2. Run a script (PyPDF2 or PDFtotext) to automatically download all the PDF files to a designated directories.
  3. Print wordcount and top 10 words results to a text document  


## Information Requirements
  1. The list of directories in the csv file must be in PDF format, i.e. the last 4 character of each 
  item on the list must be ".pdf"

### Information Inputs

  1. URLs and/or file directories in csv format
  2. A `filepaths.csv` file containing a list of files or URL expected to exist in each repository.
  
### Information Outputs

  1. A `results.txt` file containing the results of the word counts and top 10 words.

## Technology Requirements

### APIs and Web Service Requirements

### Python Package Requirements
PyPDF2
PDFtotext
os
csv

### Hardware Requirements
local machine usage only.
