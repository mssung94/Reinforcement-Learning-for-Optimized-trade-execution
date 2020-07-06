'''
USAGE: python run.py "AAPL" "2015-01-01" "2016-01-01" "2016-01-01" "2016-04-01"
'''

import argparse
import pandas as pd
import datetime as dt

import util as ut
import policy_learner as pl


def main(verbose = True):

    parser = argparse.ArgumentParser()
    parser.add_argument('symbol', type=str,  help="Company")
    parser.add_argument('train_start', type=str, help="Start date of Training")
    parser.add_argument('train_end', type=str, help="End date of Training")
    parser.add_argument('test_start', type=str, help="Start date of Testing")
    parser.add_argument('test_end', type=str, help="End date of Testing")
    args = parser.parse_args()

    # instantiate the strategy learner
    learner = pl.PolicyLearner(verbose = verbose)
    # set parameter for company
    sym = args.symbol

    #########
    # TRAIN #
    #########
    # set parameters for training the learner
    train_s_date = list(map(lambda x:int(x),args.train_start.split('-')))
    train_stdate =dt.datetime(train_s_date[0],train_s_date[1],train_s_date[2])
    train_e_date = list(map(lambda x:int(x),args.train_end.split('-')))
    train_enddate =dt.datetime(train_e_date[0],train_e_date[1],train_e_date[2])

    # train the learner
    learner.add_evidence(symbol = sym, sd = train_stdate, ed = train_enddate)

    ########
    # TEST #
    ########
    # set parameters for testing
    test_s_date = list(map(lambda x:int(x),args.test_start.split('-')))
    test_stdate = dt.datetime(test_s_date[0], test_s_date[1], test_s_date[2])
    test_e_date = list(map(lambda x:int(x),args.test_end.split('-')))
    test_enddate = dt.datetime(test_e_date[0], test_e_date[1], test_e_date[2])

    # test the learner
    learner.test_policy(symbol = sym, sd = test_stdate, ed = test_enddate)


if __name__=="__main__":
    main(verbose = False)