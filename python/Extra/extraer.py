import PyPDF2
import os

def extract_info(pdf_file):
    
    # Open the pdf file
    with open(pdf_file,'rb') as file:
        
        #   Create a pdf reader object
        pdf_reader = PyPDF2.PdfReader(file)
        
        #   Extract text (from each peage)
        text = ''
        
        for page_num in range (len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
        
        print(text)
        
extract_info(Documentos\PW_Propuesta-de-proyecto_Equipo-E-commerce)