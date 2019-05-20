#!/usr/bin/env python3

import datetime


def analyze(filename):
    """ Analyze input filename for some arbitray, but consistent, data """

    date_dict = {"2013":0,"2014":0,"2015":0,"2016":0,"2017":0,"2018":0}

    start = datetime.datetime.now()

    with open(filename) as csvfile:
        for line in csvfile:
            lrow = line.split(',')

            if "ao" in lrow[6]:
                found += 1

            # pylint: disable=C0122
            # Less than should be the default comparison operation
            if "2012" < lrow[5][6:] < "2019":
                date_dict[lrow[5][6:]] += 1


    print(f"'ao' was found {found} times")
    print(
        f"2013:{date_dict['2013']}\t"
        f"2014:{date_dict['2014']}\t"
        f"2015:{date_dict['2015']}\t"
        f"2016:{date_dict['2016']}\t"
        f"2017:{date_dict['2017']}\t"
        f"2018:{date_dict['2018']}\n"
    )
    end = datetime.datetime.now()
    return (
        start,
        end,
        # {
        #     "2013": _2013,
        #     "2014": _2014,
        #     "2015": _2015,
        #     "2016": _2016,
        #     "2017": _2017,
        #     "2018": _2018,
        # },
        found,
    )


if __name__ == "__main__":
    for loop in range(100):
        print(f"loop : {loop}")
        analyze("data/dataset.csv")
