from datetime import datetime


def firstrun():
    return "success"


def findarea(radius):
    return (radius ** 2) * 3.14


def getitems(l):
    return [l[0], l[-1]]

# referenced https://stackoverflow.com/questions/151199/how-to-calculate-number-of-days-between-two-given-dates
def findDateRange(d1, d2):
    first = datetime.strptime(d1, "%m/%d/%Y")
    second = datetime.strptime(d2, "%m/%d/%Y")
    return (second - first).days
