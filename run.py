import math
import random
import matplotlib.pyplot as plt

# Your money to start
initial_invest = 50000

# return rate
yearly_return_rate = 0.075

# monthly contribution
invest_per_month = 1500

# number of years of simulation
max_years = 30

# your age right now
age = 20

# simulate market chaos
plus_minus_return_ratio = 0
#plus_minus_return_ratio = .8

###

cumulated_interests = 0
cumulated_total = cumulated_principal = initial_invest
plotx = []
plot_y_principal = []
plot_y_interests = []
plus_minus_return_rate = plus_minus_return_ratio * yearly_return_rate

print 'Starting at ${:,.2f}'.format(cumulated_total)

for y in range(1, max_years+1):
    this_year_return_rate = yearly_return_rate + \
        random.uniform(-plus_minus_return_rate, plus_minus_return_rate)
    #print "Year {}, rate: {}".format(y, this_year_return_rate)
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

    if y < 5 or y % 5 == 0:
        print 'End of year {} ({} years old): ${:,.2f}'.format(
            y, age, cumulated_total)

    plotx.append(age)
    plot_y_interests.append(cumulated_interests)
    plot_y_principal.append(cumulated_principal)

plt.title("${:,.0f} over {} years ({}%)".format(
    cumulated_total, max_years, yearly_return_rate*100))
plt.xlabel('Age')
plt.ylabel('$')

pp = plt.bar(plotx, plot_y_principal)
pi = plt.bar(plotx, plot_y_interests, bottom=plot_y_principal)

plt.legend((pp[0], pi[0]), ('Principal', 'Interests'))

plt.show()
