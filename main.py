import pyttsx3, PyPDF2

pdf_reader = PyPDF2.PdfReader('book.pdf')
speaker = pyttsx3.init()

for page in pdf_reader.pages:
    text = page.extract_text()
    clean_text = text.strip().replace('\n', ' ')
    print(clean_text)

    speaker.save_to_file(clean_text, 'story.mp3')
    speaker.runAndWait()

    speaker.stop()
