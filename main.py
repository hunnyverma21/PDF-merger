from pypdf import PdfWriter

merger = PdfWriter()
pdfs = ["Ultimate Job-Ready AI-Powered Data Analytics Course.pdf", "COMPUTER SHORTCUTS.pdf"]
for pdf in pdfs:
    merger.append(pdf)

merger.write("merged.pdf")