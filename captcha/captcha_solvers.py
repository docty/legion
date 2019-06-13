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
    print('Sending capture to Anticaptcha service...')

    response = ImageToTextTask \
        .ImageToTextTask(anticaptcha_key=anticaptcha_service_key) \
        .captcha_handler(captcha_file=captcha_file)

    if response['errorId'] == 0:
        captcha_text = response['solution']['text']
        print('Captcha service returned:', captcha_text)
        return captcha_text
    else:
        print('Error solving captcha', response)
        return ''


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
