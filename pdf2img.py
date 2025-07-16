import fitz  # PyMuPDF

pdf_path = "example.pdf"
output_folder = "output_images/"

# Open the PDF
pdf_document = fitz.open(pdf_path)

# Iterate through pages and save as PNG
for page_number in range(len(pdf_document)):
    page = pdf_document[page_number]
    pix = page.get_pixmap()
    pix.save(f"{output_folder}page_{page_number + 1}.png")

pdf_document.close()
