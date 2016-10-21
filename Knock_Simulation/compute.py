__author__ = 'Matt Trapani and Travis Estes'
from math import *
from numpy import *

def compute(ccrfr, delta, sigma, initial_stock_price, barrier, strike, duration, h, knock):
    # convert inputs to float
    ccrfr = float(ccrfr)
    delta = float(delta)
    sigma = float(sigma)
    initial_stock_price = float(initial_stock_price)
    barrier = float(barrier)
    duration = float(duration)
    strike = float(strike)
    h = int(h)
    total = 0
    # generate 10,000 random walks
    for i in range(1, 10001):
        stock_rate_of_return = 0
        hit = False
        # 1 walk of h steps, where h is the number of steps
        for j in range(1, h + 1):
            z_score = random.normal(0, 1)
            stock_rate_of_return += (ccrfr-delta-0.5*(sigma*sigma))*(duration/h)+(sigma*sqrt(duration/h)*z_score)
            stock_price = initial_stock_price*exp(stock_rate_of_return)
            if stock_price >= barrier and not hit:
                hit = True
        # check if the barrier is hit, if the stock price is greater than
        # or equal to the strike, and knock = "in"
        # set payoff to stock_price - strike
        if hit and stock_price >= strike and knock == "in":
            payoff = stock_price - strike
        # else if the barrier is hit, and knock is "out"
        # set payoff to 0
        elif hit and knock == "out":
            payoff = 0
        # else if barrier is not hit and knock is "out" and stock_price
        # is greater than or equal to strike
        # then, set payoff to stock_price - strike
        elif not hit and knock == "out" and stock_price >= strike:
            payoff = stock_price - strike
        # this catches the three cases, when (1) it's a knock in long call,
        # the barrier was hit, but the stock_price is less than the strike
        # 2) it's a knock in but the barrier wasn't hit, and 3)
        # it's a knock out, the barrier was not hit, but the stock_price is
        # less than the strike
        else:
            payoff = 0
        total += payoff
    # returns the discounted premium
    return (total/10000)*exp(-ccrfr*duration)

if __name__ == "__main__":
    print(compute("0.05", "0.03", "0.3", "60", "65", "70", "0.25", "500", "in"))
