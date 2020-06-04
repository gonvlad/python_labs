from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from os import listdir

import qrcode


INPUT_FILES_DIR = ".\\samples\\input\\"
OUTPUT_FILES_DIR = ".\\samples\\output\\"

INSTAGRAM_URL = "https://www.instagram.com/gonvlad02/"
TEXT_ON_PHOTO = "Vlad Goncharov 04-06-2020"
LOGO_PATH = ".\\samples\\logo.jpg"

FONT_PATH = ".\\fonts\\a_ConceptoTitulNrWv.ttf"
FONT_COLOR = (253, 81, 209)

PADDING = 10 


def generate_qr_code(soc_netw_url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=4,
        border=1.5,
    )
    qr.add_data(soc_netw_url)
    qr.make(fit=True)

    return qr.make_image(fill_color="black", back_color="white").convert("RGBA")

def main(qr_code_img):
    try:
        logo = Image.open(LOGO_PATH).convert("RGBA")
        input_images = listdir(INPUT_FILES_DIR)

        for image_name in input_images:      
            filepath = INPUT_FILES_DIR + image_name
            loaded_image = Image.open(filepath)
            image_width, image_height = loaded_image.size

            # rotate image
            temp_image = loaded_image.transpose(Image.ROTATE_90)

            # add text field
            temp_draw = ImageDraw.Draw(temp_image)
            font = ImageFont.truetype(FONT_PATH, 20)
            text_box_width, text_box_height = temp_draw.textsize(TEXT_ON_PHOTO, font=font)
            temp_draw.text((int(image_height - text_box_width) / 2, int(image_width - text_box_height) - PADDING), TEXT_ON_PHOTO, FONT_COLOR, font=font)

            # add QR Code on the image
            temp_image.paste(qr_code_img, (PADDING, PADDING), qr_code_img)

            # add Photo on the image
            logo_width = logo.size[0]
            temp_image.paste(logo, (image_height - PADDING - logo_width, PADDING), logo)

            temp_image.save(OUTPUT_FILES_DIR + "c_" + image_name, dpi=(200, 200))
    except FileNotFoundError:
        print("=> Файл не найден!")


if __name__ == "__main__":
    qr_code_img = generate_qr_code(INSTAGRAM_URL)
    main(qr_code_img)
