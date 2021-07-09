from reportlab.pdfgen import canvas
from reportlab.lib.units import inch


def hello(c):
    c.drawString(300, 600, "Hello World")
    # move the origin up and to the left
    c.translate(inch, inch)
    # define a large font
    c.setFont("Helvetica", 14)
    # chose some colors
    c.setStrokeColorRGB(0.2, 0.5, 0.3)
    c.setFillColorRGB(1, 0, 1)
    # draw some lines
    c.line(0, 0, 0, 1.7 * inch)
    c.line(0, 0, 1 * inch, 0)
    # draw a rectangle
    c.rect(0.2 * inch, 0.2 * inch, 1 * inch, 1.5 * inch, fill=1)
    # make text go straight up
    c.rotate(90)
    # change color
    c.setFillColorRGB(0, 0, 0.77)
    # say hello (note after rotate the y coord needs to be negative!)
    c.drawString(0.3 * inch, -inch, "Hello World")


def text_pdf(c, text):
    while len(text)<=120:
        c.drawString(10, 780, text)
    while len(text) in range(121,241):
        c.drawString(10, 770, text)


if __name__ == '__main__':
    from views.players import view_all_players
    from tinydb import TinyDB

    db = TinyDB('../db.json')
    players_table = db.table('players')

    text = view_all_players(players_table)

    c = canvas.Canvas("../test_pdf.pdf")
    text_pdf(c, text)
    c.showPage()
    c.save()
