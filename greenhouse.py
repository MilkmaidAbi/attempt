import csv

VALID_ZONES = ["A", "B", "C"]


def load_readings(filename):
    readings = []
    with open(filename, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            readings.append(row)
    return readings


def convert_to_fahrenheit(celsius):
    return float(celsius) * 5 / 9 + 32


def display_all_readings(readings):
    print("ID\tZone\tTemp(C)\tTemp(F)\tHumidity\tSoil".expandtabs(10))
    for r in readings:
        temp_f = round(convert_to_fahrenheit(r["temperature"]), 1)
        print((r["reading_id"] + "\t" + r["zone"] + "\t" + str(r["temperature"]) + "\t" + str(temp_f)
               + "\t" + str(r["humidity"]) + "\t" + str(r["soil_moisture"])).expandtabs(10))


def display_records(records):
    if len(records) == 0:
        print("No readings found")
        return
    display_all_readings(records)


def get_reading_by_id(readings, reading_id):
    for r in readings:
        if r["reading_id"] == reading_id:
            return r
        else:
            return None


# ---------------- REQ-01 ----------------
def get_readings_by_zone(readings, zone):
    result = []

    # Add your implementation here

    return result


# ---------------- REQ-02 ----------------
def calc_zone_statistics(readings, zone):
    stats = None

    # Add your implementation here

    return stats


# ---------------- REQ-03 ----------------
def get_hottest_reading(readings):
    hottest = None

    # Add your implementation here

    return hottest


# ---------------- REQ-04 ----------------
def classify_reading(reading):
    level = ""

    # Add your implementation here

    return level


def get_alert_summary(readings):
    summary = {}

    # Add your implementation here

    return summary


# ---------------- REQ-05 ----------------
def add_reading(readings, zone, temperature, humidity, soil_moisture):
    result = -1

    # Add your implementation here

    return result


# ---------------- menu (REQ-06) ----------------
def display_main_menu(readings):
    print("=" * 45)
    print("----- Smart Greenhouse Monitor -----")
    print("=" * 45)
    print("Select option")
    print("1 - Display all readings")
    print("2 - Display zone statistics")
    print("3 - Display hottest reading")
    print("4 - Display alert summary")
    print("5 - Add new reading")
    print("6 - Display readings by zone")
    print("7 - Find reading by ID")
    print("Q - Quit")
    print("=" * 45)
    option = input("Enter selection => ").strip()

    if option == "1":
        display_all_readings(readings)

    elif option == "2":
        zone = input("Zone = ")
        stats = calc_zone_statistics(readings, zone)
        if stats is None:
            print("No readings found")
        else:
            print("Count = " + str(stats["count"]))
            print("Min = " + str(stats["min"]))
            print("Max = " + str(stats["max"]))
            print("Average = " + str(stats["average"]))

    elif option == "3":
        hottest = get_hottest_reading(readings)
        if hottest is None:
            print("No readings found")
        else:
            display_records([hottest])

    elif option == "4":
        summary = get_alert_summary(readings)
        for level in ["CRITICAL", "WARNING", "NORMAL"]:
            print(level + " = " + str(summary.get(level, 0)))

    elif option == "5":
        # REQ-06: implement option 5 here
        print("Not implemented yet")
    elif option == "6":
        zone = input("Zone = ")
        display_records(get_readings_by_zone(readings, zone))

    elif option == "7":
        reading_id = input("Reading ID = ")
        reading = get_reading_by_id(readings, reading_id)
        if reading is None:
            print("No readings found")
        else:
            display_records([reading])

    elif option == "Q":
        quit()


def main():
    readings = load_readings("readings.csv")
    while True:
        display_main_menu(readings)


if __name__ == "__main__":
    main()
