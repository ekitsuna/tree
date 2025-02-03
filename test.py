from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_resume(output_file):
    pdf = canvas.Canvas(output_file, pagesize=letter)
    pdf.setTitle("Resume")
    width, height = letter

    pdf.setFont("Helvetica-Bold", 20)
    pdf.drawString(50, height - 50, "Arthur Cai")
    
    pdf.setFont("Helvetica", 10)
    pdf.drawString(50, height - 80, "2565 Leach Dr | Naperville, IL, 60564 | 630/281/9984 | arthurca3607@gmail.com | www.linkedin.com/in/arthurycai")
    
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(50, height - 120, "Professional Summary")
    pdf.setFont("Helvetica", 10)
    pdf.drawString(50, height - 140, "A concise statement summarizing your experience, skills, and career objectives.")

    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(50, height - 180, "Skills")
    pdf.setFont("Helvetica", 10)
    pdf.drawString(50, height - 200, "- Technical Skills: Python, C++, Java")
    pdf.drawString(50, height - 215, "- Specialized Skills: Data Visualization, Data Analysis, Optimization")

    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(50, height - 270, "Professional Experience")
    pdf.setFont("Helvetica", 10)
    pdf.drawString(50, height - 290, "Job Title")
    pdf.drawString(50, height - 305, "Chipotle, Naperville, IL | 10/2023 – Present")
    pdf.drawString(50, height - 320, "- Key achievement 1")
    pdf.drawString(50, height - 335, "- Key achievement 2")
    pdf.drawString(50, height - 350, "- Key achievement 3")

    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(50, height - 390, "Education")
    pdf.setFont("Helvetica", 10)
    pdf.drawString(50, height - 425, "Neuqua Valley, Naperville, IL | 08/2021 – 05/2025")
    pdf.drawString(50, height - 440, "- Relevant coursework or honors")

    pdf.save()

output_file = "resume_example.pdf"
create_resume(output_file)
print(f"Resume PDF has been created: {output_file}")