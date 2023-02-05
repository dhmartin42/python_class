year = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
births = [723_165, 723_913, 729_674, 698_512, 695_233, 697_852, 696_271, 679_106, 657_076, 640_370]

def annual_births_average(year = year, births = births):
    ''' return a list of tuples with rach entry in this format
        (year, birth, running_average)
        Round the running average to the nearest integer
    '''
    running_averages = []
    running_average = 0
    for number in enumerate(births, start=1):
        running_average += number[1] // number[0]
        running_averages.append(running_average)
    # print(running_averages)
    triples = list(zip(year,births,running_averages))
    print(triples)

def right_way(year = year, births = births):
    result = []
    sum_ = 0
    for index, (year,birth) in enumerate(zip(year, births), start=1):
        sum_ += birth
        result.append((year, birth, round(sum_ / index)))
    return result

# so where i went wring is that I can add a variable to account for the start 
# index and then calculate it with one for loop. Cool!
def main():
    print(right_way())

if __name__ == "__main__":
    main()

