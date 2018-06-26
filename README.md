# PDF-Analytics
App that read PDF file from the internet and return basic analytics about the PDF
# Project Planning

## Problem Statement

PDF is a great way for human to read a report, but it is very hard for a user to compare and contrast
methodology or ideas for different documents.  This project is an attempt to draw insight into PDF
files so that we can compare and contrast differences and see if there is any similar patterns

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
      The csv file should contain only web addresses.  The last 4 characters on each link must be ".pdf" for this program to run
  2. For each PDF in the internet
      Visit its URL in a browser.
      download the PDF and save \project_dir\data.
      Read pdf from \project_dir\data
  3. Print the top 10 word counts
      

### To-be Process Description
  1. Obtain a list of directories via a csv format.
  2. Check if the website is legit.  
  3. Run a script (PDFtotext) to automatically download all the PDF files to a designated directories (\project_dir\data).
  4. PDF will be converted to text file for the machine to give out basic analytics
  5. Print word counts top 10 words results in command prompt and the parsed data will be deleted after the process.  


## Information Requirements
  1. A `Link.csv` file must be present in the project directory, data subfolder. The list of directories in the csv file 
    must be in PDF format, i.e. the last 4 character of each item on the list must be ".pdf"
  2. The `PDFtotext.exe` must be present at the project directory 
      Download instruction, credit @s2t2 
      1. Go to https://www.xpdfreader.com/download.html and click "Download the Xpdf tools"
      2. Uncompress/extract the zip file, and move the folder to a location like the Desktop or the Programs directory.
      3. Inside the unzipped folder, copy the file `bin64/pdftotext.exe` into your project repository

### Information Inputs

  1. URLs and/or file directories in csv format
  2. A `Link.csv` file containing a list of URL expected to exist in each repository
  
### Information Outputs
  1. A command prompt output containing the results of the word counts and top 10 words.

## Technology Requirements
WINDOWS ONLY

### APIs and Web Service Requirements

### Python Package Requirements
  1. The program will use os and csv to get user inputs on websites
  2. PDF parsing will be handled by PDFtotext.  The resulting parsed text will be analyzed.
  3. The walk package in os will be used to list all directories in /project_dir/data
  4. Subprocess package will be used to initiate `PDFtotext` command line utility, the subprocess package will also be used 
      to copy and delete files on the project directories.
  5. After converting to text, the list/text will be analyzed by Counter in the collections package
  6. Clean up the root directory using command line utility and subprocess


### Hardware Requirements
local machine usage only.
