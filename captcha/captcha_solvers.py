from PIL import Image
from python3_anticaptcha import ImageToTextTask


def fetch_capture_text_using_service(captcha_file, anticaptcha_service_key):
    """ Send captcha to anticaptcha service to be solved

        Parameters
        ----------
        captcha_file : str
            File path to downloaded captcha image

        anticaptcha_service_key : str
            API key for anticaptcha service


        Returns
        -------
        captcha_text
            The text in the captcha image
     """

    captcha_text = ImageToTextTask \
        .ImageToTextTask(anticaptcha_key=anticaptcha_service_key) \
        .captcha_handler(captcha_file=captcha_file)
    print('Captcha service returned', captcha_text)
    return captcha_text


def fetch_captcha_text_manually(captcha_file):
    """ Displays captcha image for user to solve then returns the text the user entered

        Parameters
        ----------
        captcha_file : str
            File path to downloaded captcha image


        Returns
        -------
        captcha_text
            The text in the captcha image
     """

    with Image.open(captcha_file) as image:
        image.show()

        captcha_text = input('Enter the captcha text: ')
        print('Manual captcha entry returned:', captcha_text)
        return captcha_text
