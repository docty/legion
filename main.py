#!/usr/bin/env python3

import time
import random
import sys


from voting.vote import vote


def vote_multiple_times(anticaptcha_service_key=None):
    for email in email_generator():
        vote_once(email, anticaptcha_service_key)

        # TODO: Set how long to wait between votes
        minimim_wait_time = 60
        maximum_wait_time = 5 * 60
        random_wait_time = random.randint(minimim_wait_time, maximum_wait_time)

        time.sleep(random_wait_time)


def email_generator():
    # TODO: Fetch email from source then mark it as used in the source so it's not re-used next time
    # Source can be a file, google sheet, whatever suits your fancy

    new_email = None
    yield new_email


def vote_once(email, anticaptcha_service_key=None):
    votes_before, votes_after = vote(email, anticaptcha_service_key=anticaptcha_service_key)

    print('votes_before:', votes_before)
    print('votes_after:', votes_after)
    print('vote_change:', votes_after - votes_before)
    print()


if __name__ == '__main__':
    email = 'some_email+' + str(time.time()).split('.')[0] + '@gmail.com'

    if len(sys.argv) == 2:
        API_KEY = sys.argv[1]
        vote_once(email, API_KEY)
    else:
        vote_once(email)
