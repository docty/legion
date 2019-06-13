def send_vote(session, voting_url, form_data):
    """ Submit the vote to the siemens server

        Parameters
        ----------
        session : object
            Python requests session object. Useful so session variables are preserved across requests

        voting_url : str
            Url for submitting a vote to the siemens server

        form_data: str
            Form data extracted from the voting page

        Returns
        -------
        response: str
            Python requests response object
     """

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Origin': 'https://www.empowering-people-network.siemens-stiftung.org',
        'Upgrade-Insecure-Requests': '1',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 '
                      'Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3',
        'Referer': 'https://www.empowering-people-network.siemens-stiftung.org/en/award/shortlist2019/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
    }

    response = session.post(voting_url, headers=headers, data=form_data, verify=False)
    return response
