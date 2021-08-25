import os.path

class Date:

    def __init__(self, name, activity_type, pricepoint, dress_code, effort, location):
        self.name = name
        self.pricepoint = int(pricepoint)
        self.activity_type = activity_type
        self.dress_code = dress_code
        self.effort = effort
        self.location = location
        self.dress_code_scale = ["casual", "smart casual", "semi formal", "formal"]

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name.lower()

    def get_activity_type(self):
        return self.activity_type.lower()

    def get_pricepoint(self):
        return self.pricepoint

    def get_dress_code(self):
        return self.dress_code.lower()

    def get_acceptable_dress_codes(self, user_dress_code):
        if user_dress_code:
            return self.dress_code_scale[:self.dress_code_scale.index(user_dress_code) + 1]
        return self.dress_code_scale

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


def decide_date(activity_type, pricepoint, dress_code, effort, location):
    dates = load_dates()
    results = []

    # TODO: Add process user input function, possibly overload decide_date function to allow for min_price missing

    if "-" in pricepoint:
        min_price, max_price = map(int, pricepoint.split("-"))
    elif pricepoint:
        min_price = 0
        max_price = int(pricepoint)
    else:
        min_price = 0
        max_price = 10000

    for date in dates:
        if (((date.get_effort() == effort) or not effort) and
        ((date.get_activity_type() == activity_type) or not activity_type) and
        ((date.get_pricepoint() <= max_price) and (date.get_pricepoint() >= min_price) or not pricepoint) and
        ((dress_code in date.get_acceptable_dress_codes(dress_code)) or not dress_code) and
        ((date.get_location() == location) or not location)):
            results.append(date)

    return results

def main():
    if not os.path.isfile("dates.csv"):
        raise Exception("No dates file exists")
    activity_type = input("What type of activity do you want to do? ").lower()
    pricepoint = input("What is your pricepoint? ")
    dress_code = input("What is your dress code? ").lower()
    effort = input("What is your effort? ").lower()
    location = input("What is your location? ").lower()
    results = decide_date(activity_type, pricepoint, dress_code, effort, location)

    for r in results:
        print (r)

if __name__ == "__main__":
    main()
