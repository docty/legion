import time

from voting.vote import vote

if __name__ == '__main__':
    # TODO: Fetch email from google sheet instead, make sure to mark the email as used on the google sheet
    # So it's not re-used next time

    email = 'peter.o.adu+' + str(time.time()).split('.')[0] + '@gmail.com'

    anticaptcha_service_key = None
    votes_before, votes_after = vote(email)

    # Specify API key for Anticaptcha service, https://anti-captcha.com/, if you want to use it for solving the captchas
    # votes_before, votes_after = vote(email, anticaptcha_service_key=anticaptcha_service_key)

    print('votes_before:', votes_before)
    print('votes_after:', votes_after)
    print('vote_change:', votes_after - votes_before)
