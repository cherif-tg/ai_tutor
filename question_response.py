from pypdf import PdfReader
from transformers import pipeline
#Load the File
reader = PdfReader("docs\Support de cours POO EPL.pdf")
document_text = ""

for page in reader.pages:
    document_text += page.extract_text()
    
qa_pipeline = pipeline(
    task = "question-answering",
    model = "distilbert/distilbert-base-cased-distilled-squad"
)

question = input("../")
result = qa_pipeline(question = question,
                     context=document_text)

print(f"Answer:{result['answer']}")
