from fpdf import FPDF

def createpdf (path_image, savepath, results):

    # Generate FPDF object and add page
    pdf = FPDF("P","mm","A4") # (orientation, unit, format)
    pdf.add_page()

    # Vision logo
    pdf.image("images/logo.png", x = 160, y = 20, w = 39, h = 26)

    # Title
    pdf.set_font("Arial", "B", 28) # (letter type, style, size)
    pdf.set_text_color(4,23,34)
    #pdf.set_draw_color(220,220,220) # give color to borders
    pdf.set_fill_color(255,255,255) # backgrund cell color
    
    pdf.set_xy(25, 40)
    pdf.cell(0, 20, "OCT Diagnostic", 0, 2, "C", True)

    # Image
    pdf.image(path_image, x = 120, y = 80, w = 59, h = 59)

    # Text
    pdf.set_font("Arial", "", 12)
    pdf.set_text_color(10,10,10)

    pdf.cell(25, 20, "", 0, 2, "L")
    pdf.cell(0, 15, f"Choroidal Neovascularization : {round(results[0]*100, 2)} %", 0, 2, "L")
    pdf.cell(0, 15, f"Diabetic Macular Edema : {round(results[1]*100, 2)} %", 0, 2, "L")
    pdf.cell(0, 15, f"Drusen : {round(results[2]*100, 2)} %", 0, 2, "L")
    pdf.cell(0, 15, f"Normal : {round(results[3]*100, 2)} %", 0, 2, "L")
    
    # Save File
    pdf.output(f"{savepath}.pdf","F")

if __name__ == '__main__':
    createpdf()