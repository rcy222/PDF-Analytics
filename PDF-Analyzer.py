import csv
import requests
import os
from os import walk
import subprocess
import collections

#credit https://stackoverflow.com/questions/32546245/python-return-top-5-words-with-highest-frequency
def top10_words(text):
    counts = collections.Counter(text.split())
    return counts.most_common(10)

#credit https://stackoverflow.com/questions/43936273/download-pdfs-links-listed-in-csv-with-python-request-module
def download_pdf():
    
    with open("data\link.csv", "r") as csvfile:
        pdfreader = csv.reader(csvfile)
        for link in pdfreader:
            #check last 4 digit
            if str(link[0].split("/")[-1][-4:]) == ".pdf":
                print("-"*72)
                #obtain PDF name
                pdf_file = link[0].split('/')[-1]
                with open(os.path.join(os.path.dirname(__file__), "data", pdf_file), 'wb') as pdf:
                    try:
                    # Try to request PDF from URL
                        print('Downloading {}...'.format(link[0]))
                        a = requests.get(link[0], stream=True)
                        for block in a.iter_content(512):
                            if not block:
                                break
                            pdf.write(block)
                        print("Download Successful")
                    except requests.exceptions.RequestException as e:  # This will catch ONLY Requests exceptions
                        print('THIS IS NOT A WEBSITE')
                        print(e)  # This should tell you more details about the error
            else:
                quit("The csv file contain a link that is not a pdf file, please double check and try again")
#return a list of pdf in the directory
def list_pdf():
    mypath = os.path.join(os.path.dirname(__file__), "data")
    f = []
    process_pdf = []
    #list all file in directory
    #credit https://stackoverflow.com/questions/6706122/directory-listing-in-python
    for (dirpath, dirnames, filenames) in walk(mypath):
            f.extend(filenames)
            break
    for file_extension in range(len(f)):    
        if f[file_extension][-4:] == ".pdf":
            process_pdf.append(f[file_extension])
    return process_pdf
#Parse PDF
def parse_pdf(pdf_list=[]):
    root_path = os.path.join(os.path.dirname(__file__))
    data_path = os.path.join(os.path.dirname(__file__), "data")
    for each_pdf in pdf_list:
        command = '"' + data_path + '\\' + each_pdf + '"' + ' "' + root_path + '"'
        print("-"*72)
        print("Processing "+ each_pdf)
        #Copy files to project dir and process, then remove the paresed text
        subprocess.call("copy " + command, shell=True)
        try:
            subprocess.call("pdftotext "+ each_pdf + " " + each_pdf +"_parsed.txt", shell = True)
            print("PDF Parsed")
        except Exception as e: 
            print("Error Parsing PDF, please try another method, such as Py2PDF")
        subprocess.call("del "+ each_pdf, shell = True)
        with open(each_pdf+"_parsed.txt", "r") as pdf_text:
            pdf_content = pdf_text.read().replace("\n","")
        print("Word count = " + str("{:,}".format(len(pdf_content))))
        print("The Top 10 Words Are:")
        print(top10_words(pdf_content))
        subprocess.call("del "+ each_pdf+"_parsed.txt", shell = True)

def run():
    download_pdf()
    pdf_list = list_pdf()
    parse_pdf(pdf_list)

# only prompt the user for input if this script is run from the command-line
# this allows us to import and test this application's component functions
if __name__ == "__main__":
    run()