import json

import requests
import urllib3

from voting.fetch_votes import fetch_vote_count
from voting.fetch_voting_form import fetch_voting_form
from voting.send_vote import send_vote


def vote(email, anticaptcha_service_key=None, verbose=False):
    """ Extract voting url and form form_data from voting page, in order to preserve any csrf tokens or
        checks

        Parameters
        ----------
        email : str
            Email to use for voting

        anticaptcha_service_key : str
            API key for anticaptcha service

        verbose: bool
            Whether to display voting_url, form_data and vote response from server


        Returns
        -------
        votes_before: int
            Number of votes for Grainmate before this vote was sent in

        votes_after: str
            Number of votes for Grainmate after this vote was sent in

     """

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    session = requests.Session()

    votes_before = fetch_vote_count(session)

    voting_url, form_data = fetch_voting_form(session, email, anticaptcha_service_key)
    response = send_vote(session, voting_url, form_data)

    votes_after = fetch_vote_count(session)

    if verbose:
        display_voting_results(voting_url, form_data, response)

    return votes_before, votes_after


def display_voting_results(voting_url, form_data, response):
    print('------------------------------------------------')
    print('Voting url')
    print(voting_url)
    print()
    print('Form data')
    print(json.dumps(form_data, indent=4))
    print()
    print('Response code')
    print(response.status_code)
    print()
    print('Writing response to file...')
    file = open("response.html", "w")
    file.write(response.text)
    file.close()
    print('Response written to file, response.html...')
