#!/usr/bin/env python3

import time
import random
import sys


from voting.vote import vote


def vote_multiple_times(anticaptcha_service_key=None):
    for email in email_generator():
        vote_once(email, anticaptcha_service_key)

        # TODO: Adjust how long to wait between votes
        minimim_wait_time = 5
        maximum_wait_time = 5 * 5
        random_wait_time = random.randint(minimim_wait_time, maximum_wait_time)

        print('Sleeping for', minimim_wait_time, '-', maximum_wait_time, 'seconds before voting again...')
        print()

        time.sleep(random_wait_time)

    print('Done voting!')


def email_generator():
    # TODO: Yield emails from a file or google sheets, then mark it as used in the source so it's not re-used next time
    # If you're not familier with generators and the yield keyword, here's an explanation
    # https://www.programiz.com/python-programming/generator#create

    yield 'some_email+' + str(time.time()).split('.')[0] + '@gmail.com'
    yield 'some_email+' + str(time.time()).split('.')[0] + '@gmail.com'


def vote_once(email, anticaptcha_service_key=None):
    print('Started voting with email:', email)
    votes_before, votes_after = vote(email, anticaptcha_service_key=anticaptcha_service_key)

    print('votes_before:', votes_before)
    print('votes_after:', votes_after)
    print('vote_change:', votes_after - votes_before)
    print()


if __name__ == '__main__':
    if len(sys.argv) == 2:
        API_KEY = sys.argv[1]
        vote_multiple_times(API_KEY)
    else:
        vote_multiple_times()
