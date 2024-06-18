import fitz  # PyMuPDF
import os

def find_text_position(page, text):
    text_instances = page.search_for(text)
    if text_instances:
        return text_instances[0]  # Return the first occurrence
    return None

def insert_dynamic_links(page, github_position, linkedin_position):
    if github_position:
        github_link = {
            "from": fitz.Rect(github_position.x0, github_position.y0, github_position.x1, github_position.y1),
            "uri": "https://github.com/cnz1",
            "kind": fitz.LINK_URI
        }
        page.insert_link(github_link)

    if linkedin_position:
        linkedin_link = {
            "from": fitz.Rect(linkedin_position.x0, linkedin_position.y0, linkedin_position.x1, linkedin_position.y1),
            "uri": "https://www.linkedin.com/in/per-henriksson86/",
            "kind": fitz.LINK_URI
        }
        page.insert_link(linkedin_link)

def create_unique_filename(base_name, extension):
    counter = 1
    new_filename = f"{base_name}{extension}"
    while os.path.exists(new_filename):
        new_filename = f"{base_name}_{counter}{extension}"
        counter += 1
    return new_filename

# Open the original PDF
input_pdf = fitz.open("input.pdf")

# Create a new PDF to store the combined page
output_pdf = fitz.open()

# Calculate the dimensions for the new page
page1 = input_pdf[0]
page2 = input_pdf[1]
width = page1.rect.width

# Find positions of "GitHub" and "LinkedIn" to determine trim height
github_position_page2 = find_text_position(page2, "GitHub")
linkedin_position_page2 = find_text_position(page2, "LinkedIn")

if linkedin_position_page2:
    page2_trim_height = linkedin_position_page2.y1 + 28.35  # 1 cm below the bottom of the LinkedIn link (28.35 points = 1 cm)
else:
    page2_trim_height = 430  # Default value if LinkedIn position is not found

combined_height = page1.rect.height + page2_trim_height - 2  # Adjusted to remove the bottom line

# Create a new page with the combined height
combined_page = output_pdf.new_page(width=width, height=combined_height)

# Insert the first page at the top
combined_page.show_pdf_page(fitz.Rect(0, 0, width, page1.rect.height), input_pdf, 0)

# Insert the second page slightly overlapping the first page to avoid lines
combined_page.show_pdf_page(fitz.Rect(0, page1.rect.height - 1, width, page1.rect.height - 1 + page2_trim_height), input_pdf, 1, clip=fitz.Rect(0, 1, width, page2_trim_height))

# Find positions of "GitHub" and "LinkedIn" on the combined page
github_position_combined = find_text_position(combined_page, "GitHub")
linkedin_position_combined = find_text_position(combined_page, "LinkedIn")

# Insert dynamic links
insert_dynamic_links(combined_page, github_position_combined, linkedin_position_combined)

# Generate a unique output filename
output_filename = create_unique_filename("output", ".pdf")

# Save the combined PDF
output_pdf.save(output_filename)

# Close the documents
input_pdf.close()
output_pdf.close()

print(f"Combined PDF saved as {output_filename}")
