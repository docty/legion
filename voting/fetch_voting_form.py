from urllib.parse import urljoin, urldefrag

from lxml import html

from captcha.captcha_solvers import fetch_captcha_text_manually, fetch_capture_text_using_service

VOTING_PAGE_URL = 'https://www.empowering-people-network.siemens-stiftung.org/en/award/shortlist2019/'
GRAINMATE_PROJECT_ID = '925'
OTHER_PROJECT_IDS = ['930', '934']


def fetch_voting_form(session, email, anticaptcha_service_key=None):
    """ Extract voting url and form data from voting page, in order to preserve any csrf tokens or
        checks

        Parameters
        ----------
        session : object
            Python requests session object. Useful so session variables are preserved across requests

        email : str
            Email to use for voting

        anticaptcha_service_key : str
            API key for anticaptcha service


        Returns
        -------
        voting_url: str
            Url for submitting a vote to the siemens server

        form_data: str
            Form data extracted from the voting page
     """

    response = session.get(VOTING_PAGE_URL, verify=False)
    tree = html.fromstring(response.text)
    tree.xpath('normalize-space(//*[@id="right-content"]/div[3]/div/div/div/div/div/h3/text())')

    voting_path = tree.xpath('//*[@id="voting"]/div/form/@action')[0]
    voting_url = urljoin(VOTING_PAGE_URL, voting_path)
    voting_url = urldefrag(voting_url)[0]

    captcha_url = tree.xpath('//*[@id="captcha-image"]')[0].get('src')
    response = session.get(captcha_url)
    if response.status_code == 200:
        image_file_path = "captcha_image.jpeg"
        with open(image_file_path, 'wb') as image_file:
            image_file.write(response.content)

    if anticaptcha_service_key:
        captcha_text = fetch_capture_text_using_service(image_file_path, anticaptcha_service_key)
    else:
        captcha_text = fetch_captcha_text_manually(image_file_path)

    form_data = {
        'tx_epaprojects_voting[__referrer][@extension]':
            tree.xpath('//*[@id="voting"]/div/form/div[1]/input[1]/@value')[0],
        'tx_epaprojects_voting[__referrer][@vendor]':
            tree.xpath('//*[@id="voting"]/div/form/div[1]/input[2]/@value')[0],
        'tx_epaprojects_voting[__referrer][@controller]':
            tree.xpath('//*[@id="voting"]/div/form/div[1]/input[3]/@value')[0],
        'tx_epaprojects_voting[__referrer][@action]':
            tree.xpath('//*[@id="voting"]/div/form/div[1]/input[4]/@value')[0],
        'tx_epaprojects_voting[__referrer][arguments]':
            tree.xpath('//*[@id="voting"]/div/form/div[1]/input[5]/@value')[0],
        'tx_epaprojects_voting[__trustedProperties]':
            tree.xpath('//*[@id="voting"]/div/form/div[1]/input[6]/@value')[0],
        'tx_epaprojects_voting[voteDemand][projects][0]': OTHER_PROJECT_IDS[0],
        'tx_epaprojects_voting[voteDemand][projects][1]': GRAINMATE_PROJECT_ID,
        'tx_epaprojects_voting[voteDemand][projects][2]': OTHER_PROJECT_IDS[1],
        'tx_epaprojects_voting[voteDemand][email]': email,
        'tx_epaprojects_voting[voteDemand][captcha]': captcha_text,
        'tx_epaprojects_voting[voteDemand][voting]':
            tree.xpath('//*[@id="voting"]/div/form/div[4]/div[3]/div[2]/div/input[1]/@value')[0]
    }

    return voting_url, form_data
