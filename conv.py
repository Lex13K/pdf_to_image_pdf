from pdf2image import convert_from_path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os


def pdf_to_images(pdf_path):
    # Convert each page of the PDF to an image
    return convert_from_path(pdf_path)


def create_pdf_with_images(images, output_pdf_path):
    for i, image in enumerate(images):
        image_path = f"temp_page_{i}.jpg"
        image.save(image_path, 'JPEG')

        if i == 0:
            # Create a PDF file and set the first page size to match the first image
            c = canvas.Canvas(output_pdf_path, pagesize=(image.width, image.height))
        else:
            # Add new page with the size to match the image
            c.setPageSize((image.width, image.height))

        # Draw the image on the current page
        c.drawImage(image_path, 0, 0, width=image.width, height=image.height)
        c.showPage()

        # Remove the temporary image file
        os.remove(image_path)

    c.save()


from pdf2image import convert_from_path

def pdf_to_images(pdf_path):
    # Adjust the poppler_path according to your Poppler installation
    return convert_from_path(pdf_path, poppler_path='/opt/homebrew/bin')

pdf_path = '/Users/lexo/Desktop/Steven E. Shreve - Stochastic Calculus for Finance II.pdf'
output_pdf_path = '/Users/lexo/Desktop/converted_pdf.pdf'

# Convert the PDF to images
images = pdf_to_images(pdf_path)

# Create a new PDF with these images
create_pdf_with_images(images, output_pdf_path)

print("Conversion completed.")
