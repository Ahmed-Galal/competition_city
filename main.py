import csv


def read_cities_csv():
	cities = []
	with open('cities.csv') as csvfile:
		cities_csv = csv.DictReader(csvfile, delimiter=',')
		for row in cities_csv:
			cities.append(row)
	return cities


def read_points_csv():
	points = []
	with open('points.csv') as csvfile:
		points_csv = csv.DictReader(csvfile, delimiter=',')
		for row in points_csv:
			points.append(row)
	return points


def get_city_obj(row):
	if (validate_positive(row["TopLeft_X"])
			and validate_positive(row["TopLeft_Y"])
			and validate_positive(row["BottomRight_X"])
			and validate_positive(row["BottomRight_Y"])):
		return row
	return None


def get_point_obj(row):
	if (validate_positive(row['Y']) and validate_positive(row['X'])):
		return row
	return None


def validate_positive(num):
	if (int(num) >= 0):
		return True
	return False


def check_point_in_city(point, city):
	if (int(city['TopLeft_Y']) <= int(point['Y']) <= int(city['BottomRight_Y'])
			and int(city['TopLeft_X']) <= int(point['X']) <= int(city['BottomRight_X'])):
		return city['Name']
	else:
		return 'None'


def points_in_cities():
	cities_csv = read_cities_csv()
	points_csv = read_points_csv()
	with open('output_points.csv', 'w', newline='') as csvfile:
		fieldnames = ["ID", "X", "Y", "CITY"]
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		for city_row in cities_csv:
			city = get_city_obj(city_row)
			if (city):
				for point_row in points_csv:
					point = get_point_obj(point_row)
					if (point):
						point['CITY'] = check_point_in_city(point, city)
						writer.writerow(point)


def main():
	points_in_cities()


if __name__ == '__main__':
	main()
