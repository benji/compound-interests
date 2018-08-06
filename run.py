import math
import random
import matplotlib.pyplot as plt

# Your money to start
#initial_invest = 40000
initial_invest = 50000

# What to use for yearly return rate?
use_historical_stock_market_rates = True
yearly_return_rate = 0.1092

# monthly contribution
invest_per_month = 1000

# number of years of simulation
max_years = 20

# your age right now
age = 25

# SP500 performance
historical_stock_return = {
    2017: 21.83,
    2016: 11.96,
    2015: 1.38,
    2014: 13.69,
    2013: 32.39,
    2012: 16.00,
    2011: 2.11,
    2010: 15.06,
    2009: 26.46,
    2008: -37.00,
    2007: 5.49,
    2006: 15.79,
    2005: 4.91,
    2004: 10.88,
    2003: 28.68,
    2002: -22.10,
    2001: -11.89,
    2000: -9.10,
    1999: 21.04,
    1998: 28.58,
    1997: 33.36,
    1996: 22.96,
    1995: 37.58,
}


stock_all_rates = historical_stock_return.values()
stock_average_rate = sum(stock_all_rates) / 100. / len(stock_all_rates)

print 'Store average rate: {:,.2f}%'.format(stock_average_rate*100)

cumulated_interests = 0
cumulated_total = cumulated_principal = initial_invest
plotx = [age]
total_principal = [cumulated_total]
total_interests = [0]
total_actual = [cumulated_total]
total_expected = [cumulated_total]

print 'Starting at ${:,.2f}'.format(cumulated_total)

for y in range(1, max_years+1):
    this_year_return_rate = yearly_return_rate

    if use_historical_stock_market_rates:
        this_year_return_rate = stock_all_rates[random.randint(
            0, len(stock_all_rates)-1)] / 100.

    print "Year {}, rate: {:,.2f}%".format(y, this_year_return_rate*100)
    monthly_return_ratio = math.exp(math.log(1+this_year_return_rate)/12) - 1

    # run a year of investment contributions+returns
    for m in range(1, 12+1):
        cumulated_principal += invest_per_month
        earned_interests = cumulated_total * monthly_return_ratio
        cumulated_interests += earned_interests

        cumulated_total = cumulated_principal + cumulated_interests
        # print 'Month {}: {} (interests: {})'.format(
        #    m, cumulated_total, earned_interests)

    age += 1

    if y < 5 or y % 5 == 0 or max_years < 10:
        print 'End of year {} ({} years old): ${:,.2f}'.format(
            y, age, cumulated_total)

    plotx.append(age)
    total_interests.append(cumulated_interests)
    total_principal.append(cumulated_principal)
    total_actual.append(cumulated_principal+cumulated_interests)

    year_expected = total_expected[len(
        total_expected)-1] * (1+stock_average_rate) + invest_per_month*12
    print year_expected
    total_expected.append(year_expected)

end_total_invested = total_principal[len(
    total_principal)-1]
end_total_actual = total_actual[len(total_actual)-1]
overall_return_rate = (end_total_actual-end_total_invested) / \
    end_total_invested/max_years

prefix = ''
if overall_return_rate >= 0:
    prefix = '+'

plt.title("${:,.0f} over {} years ({}{:,.2f}%)".format(
    cumulated_total, max_years, prefix, overall_return_rate*100))
plt.xlabel('Age')
plt.ylabel('$')

pp = plt.plot(plotx, total_principal, color='skyblue')
pi = plt.plot(plotx, total_interests, color='green')
pt = plt.plot(plotx, total_actual, color='red')
pe = plt.plot(plotx, total_expected, color='orange', linestyle='dashed')

plt.legend((pp[0], pi[0], pt[0], pe[0]),
           ('Principal', 'Interests', 'Actual', 'Expected'))

plt.show()
