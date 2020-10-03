import csv
'''
#def emissions(distance_travelled, make, vehicle_class)
car make choices: Acura, Alfa Romeo, Aston Martin, Audi, Bentley, BMW, Bugatti, Buick, Cadillac,
Chevrolet, Chrysler, Dodge, Ford, Genesis, GMC, Honda, Hyundai, Infiniti, Jaguar, Jeep,
Kia, Lamborghini, Land Rover, Lexus, Lincoln, Maserati, Mazda, Mercedes-Benz, MINI, Mitsubishi,
Nissan, Porsche, Ram, Rolls-Royce, Subaru, Toyota, Volkswagen, Volvo

vehicle class options: SUV: Standard, SUV: Small, Mid-size, Full-size, Compact, Subcompact, Station wagon: Small
'''
with open('fuel_consumption.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    make = "Acura"
    vehicle_class = ""

    for line in csv_reader:
        #get fuel consumption combined (L/100 Km)
        if (line[1] == make and line[3] == vehicle_class):
            print(line[10])