import operator


OUTCOME_RETURNS_BY_FUND = {
    'stock_market': (3110, 731),
    'deposit': (800, 800),
}

MARKET_OUTCOMES = [0.74, 0.26]


def calc_expected_return(fund_returns, market_outcomes):
    """Calculates the expected return of a fund under different
    market outcomes.
    """
    expected_return = 0
    for ret, outcome in zip(fund_returns, market_outcomes):
        expected_return += ret * outcome

    return expected_return


def main():
    orbf = OUTCOME_RETURNS_BY_FUND
    out = MARKET_OUTCOMES

    expected_returns_by_fund = {}
    for fund, returns in orbf.items():
        expected_return = calc_expected_return(returns, out)
        expected_returns_by_fund[fund] = expected_return

    print("Expected returns by fund: {}".format(expected_returns_by_fund))
    best_fund = max(
        expected_returns_by_fund.items(),
        key=operator.itemgetter(1)
    )
    print('You should invest in {}'.format(best_fund))


if __name__ == "__main__":
    main()
