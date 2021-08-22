import os.path

class Date:

    def __init__(self, name, pricepoint, dress_code, effort, location):
        self.name = name
        self.pricepoint = int(pricepoint)
        self.dress_code = dress_code
        self.effort = effort
        self.location = location

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name.lower()

    def get_pricepoint(self):
        return self.pricepoint

    def get_dress_code(self):
        return self.dress_code.lower()

    def get_effort(self):
        return self.effort.lower()

    def get_location(self):
        return self.location.lower()


def load_dates():
    reader = open("dates.csv", "r")
    dates = []
    try:
        for line in reader.readlines():
            d = Date(*line.strip().split(","))
            dates.append(d)
    finally:
        reader.close()
    return dates


def decide_date(pricepoint, dress_code, effort, location):
    dates = load_dates()
    results = []

    if "-" in pricepoint:
        min_price, max_price = map(int, pricepoint.split("-"))
    else:
        min_price = 0
        max_price = int(pricepoint)

    for date in dates:
        if (((date.get_effort() == effort) or not effort) and
        ((date.get_pricepoint() <= max_price) and (date.get_pricepoint() >= min_price) or not pricepoint) and
        ((date.get_dress_code() == dress_code) or not dress_code) and
        ((date.get_location() == location) or not location)):
            results.append(date)

    return results

def main():
    if not os.path.isfile("dates.csv"):
        raise Exception("No dates file exists")
    pricepoint = input("What is your pricepoint? ")
    dress_code = input("What is your dress code? ").lower()
    effort = input("What is your effort? ").lower()
    location = input("What is your location? ").lower()
    results = decide_date(pricepoint, dress_code, effort, location)

    for r in results:
        print (r)

if __name__ == "__main__":
    main()
