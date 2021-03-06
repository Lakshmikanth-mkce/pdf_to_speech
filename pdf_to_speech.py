# -*- coding: utf-8 -*-
"""pdf_to_Speech.ipynb

Author: Lakshmikanth Rajamani
Twitter Handle: @krlakshmikanth
Many Thanks to Stack Overflow and creators of pypdf2 and gtts 


# Import required libraries
"""

!pip install pypdf2
!pip install gtts
import PyPDF2
from gtts import gTTS
import os
import requests

"""# Read PDF file"""

#file_path => Ensure the file path of PDF which needs to be converted into audio
file_path = '/content/Chetan_Bhagat_-_2_States_The_Story_of_My_Marriage.pdf'
with open(file_path,'rb') as pdf_file, open('sample.txt', 'w') as text_file:
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    number_of_pages = read_pdf.getNumPages()
    for page_number in range(number_of_pages):   
        page = read_pdf.getPage(page_number)
        page_content = page.extractText()
        text_file.write(page_content)
doc = open("sample.txt", "r").read().replace("\n", " ")

"""# gTTS (Google Text-to-Speech)"""

tts = gTTS(text = str(doc), lang='en')
tts.save('test.mp3')
