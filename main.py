from PyPDF2 import PdfMerger, PdfFileReader
import os


def main():
    merger = PdfMerger()
    for items in os.listdir():
        if items.endswith(".pdf"):
            merger.append(items)
    merger.write("Merged_PDF.pdf")
    originalFile = PdfMerger()
    with open(merger, 'rb+') as fin:
        merger.append(PdfFileReader(fin))
    os.remove(originalFile)
    merger.close()


if __name__ == "__main__":
    main()
    print(os.listdir())
