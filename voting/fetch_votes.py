from lxml import html

GRAINMATE_PAGE_URL = 'https://www.empowering-people-network.siemens-stiftung.org/en/solutions/projects/grainmate/'


def fetch_vote_count(session):
    """ Return number of votes for Grainmate from siemens page

        Parameters
        ----------
        session : object
            Python requests session object. Useful so session variables are preserved across requests


        Returns
        -------
        votes: int
            Number of votes for Grainmate
     """

    response = session.get(GRAINMATE_PAGE_URL, verify=False)
    tree = html.fromstring(response.text)
    votes_string = tree.xpath('normalize-space(//*[@id="right-content"]/div[3]/div/div/div/div/div/h3/text())')
    return int(votes_string)
