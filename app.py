# Import qrcode package
import qrcode
from PIL import Image 

# Function to adjust the logo 
def logoadjust(Logo_link):
    logo = Image.open(Logo_link)

    # taking base width
    basewidth = 300

    # adjust image size
    wpercent = (basewidth/float(logo.size[0]))
    hsize = int((float(logo.size[1])*float(wpercent)))
    logo = logo.resize((basewidth, hsize))#, Image.LANCZOS)
    return logo

# Function to generate QR code with the logo
def QRcodegen(logo, url):
    qr = qrcode.QRCode(version=10,
                    error_correction=qrcode.constants.ERROR_CORRECT_H,
                    box_size=20,
                    border=3)

    qr.add_data(url)
    qr.make(fit=True)

    # taking color name from user
    QRcolor = 'black'

    # adding color to QR code
    img = qr.make_image(fill_color=QRcolor, back_color="white").convert('RGBA')

    # set size of QR code
    pos = ((img.size[0] - logo.size[0]) // 2,
          (img.size[1] - logo.size[1]) // 2)
    img.paste(logo, pos)
    return img

# taking logo of image which user wants
Logo_link = 'linkedin_logo.png'
logo = logoadjust(Logo_link)
url = "https://www.linkedin.com/in/appan-merari/"
img = QRcodegen(logo, url)

# save the QR code generated
img.save("linkedinqr.png")

# taking logo of image which user wants
Logo_link = 'github_logo.png'
logo = logoadjust(Logo_link)
url = "https://github.com/blockchainamm"
img = QRcodegen(logo, url)

# save the QR code generated
img.save("githubqr.png")

print('QR code with logo generated!')