import csv
'''
csv source: https://open.canada.ca/data/en/dataset/98f1a129-f628-4ce4-b24d-6f16bf24dd64

car make choices: Acura, Alfa Romeo, Aston Martin, Audi, Bentley, BMW, Bugatti, Buick, Cadillac,
Chevrolet, Chrysler, Dodge, Ford, Genesis, GMC, Honda, Hyundai, Infiniti, Jaguar, Jeep,
Kia, Lamborghini, Land Rover, Lexus, Lincoln, Maserati, Mazda, Mercedes-Benz, MINI, Mitsubishi,
Nissan, Porsche, Ram, Rolls-Royce, Subaru, Toyota, Volkswagen, Volvo

vehicle class options: SUV: Standard, SUV: Small, Mid-size, Full-size, Compact, Subcompact, Station wagon: Small, Minivan,
Two-seater, Minicompact, Pickup truck: Small, Pickup truck: Mid-size
'''

def calc_co2(distance_travelled, make, vehicle_class):
    with open('fuel_consumption.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for line in csv_reader:
            #get fuel consumption combined (L/100 Km)
            if (line[1] == make and line[3] == vehicle_class):
                fuel_economy = line[10]
        
        try: 
            fuel_emissions = (float(fuel_economy) * 2.33) * 10 * distance_travelled
            return fuel_emissions
        except:
            return("An error occured")

def calc_co(distance_travelled, make, vehicle_class):
    with open('fuel_consumption.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for line in csv_reader:
            #get fuel consumption combined (L/100 Km)
            if (line[1] == make and line[3] == vehicle_class):
                engine_size = line[4]
        
        try: 
            grams = float(engine_size) * 1000
            moles = grams/(12*23)    #12 moles in carbon, 1 mol contain 23dm3 of volume
            emissions = moles * 10 * distance_travelled
            emissions = round(emissions, 1)
            return emissions #in grams
        except:
            return("An error occured")

