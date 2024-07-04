import PyPDF2

def split_pdf(file, directory_to_save):
    pdf = PyPDF2.PdfReader(file)
    for page in range(len(pdf.pages)):
        pdf_writer = PyPDF2.PdfWriter()
        pdf_writer.add_page(pdf.pages[page])

        output_filename = f"{directory_to_save}/page_{page+1}.pdf"

        with open(output_filename, "wb") as output_pdf:
            pdf_writer.write(output_pdf)

split_pdf("input.pdf", "output")