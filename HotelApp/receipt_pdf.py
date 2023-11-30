from fpdf import FPDF

def generate_pdf(customer_name, hotel_name):
    pdf = FPDF(orientation="p", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=False, margin=0)

    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=20)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt="Hotel booking receipt", align="C", ln=1)

    pdf.set_font(family="Times", style="I", size=16)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt="Thank you for your reservation!", align="L", ln=1)

    pdf.set_font(family="Times", style="I", size=12)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt="Here are you booking data:", align="L", ln=1)

    pdf.set_font(family="Times", style="B", size=12)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=f"Name: {customer_name.title()}", align="L", ln=1)

    pdf.set_font(family="Times", style="B", size=12)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=f"Hotel Name: {hotel_name}", align="L", ln=1)

    pdf.set_font(family="Times", style="B", size=16)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt="Happy Stay with us !!!", align="C", ln=1)

    pdf.output("receipt.pdf")
