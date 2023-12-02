import json

# Company data
companies = [
    {"id": 1, "name": "Micorosft", "industry": "Technology", "location": "Nairobi,Kenya"},
    {"id": 2, "name": "Eaagads Ltd.", "industry": "Agricultural", "location": "Kigali, Rwanda"},
    {"id": 3, "name": "Kapchorua Tea Kenya Plc.", "industry": "Agricultural", "location": "Nairobi, Kenya"},
    {"id": 4, "name": "Kakuzi Plc", "industry": "Agricultural", "location": "Abuja, Nigeria"},
    {"id": 5, "name": "Limuru Tea Co. Ltd.", "industry": "Agricultural", "location": "Kampala, Uganda"},
    {"id": 6, "name": "Sasini Plc.", "industry": "Agricultural", "location": "Kigali, Rwanda"},
    {"id": 7, "name": "Williamson Tea Kenya Plc.", "industry": "Agricultural", "location": "Nairobi, Kenya"},
    {"id": 8, "name": "Car & General (K) Ltd.", "industry": "Automobile and accessories", "location": "Nairobi, Kenya"},
    {"id": 9, "name": "ABSA Bank Kenya Plc.", "industry": "Finance", "location": "Nairobi, Kenya"},
    {"id": 10, "name": "Jumia group", "industry": "Financial services", "location": "Lagos, Nigeria"},
    {"id": 11, "name": "Andela", "industry": "Commercial and professional services", "location": "New York, United States"},
    {"id": 12, "name": "Takealot", "industry": "E-commerce and retail", "location": "Cape Town, South Africa"},
    {"id": 13, "name": "Zola Electric", "industry": "Energy and Environment Resources", "location": "Arusha, Tanzania"},
    {"id": 14, "name": "D.light", "industry": "Energy and resources", "location": "San Fransisco, United Sates of America"},
    {"id": 15, "name": "Swvl", "industry": "Transport and logistics", "location": "Cairo, Egypt"},
    {"id": 16, "name": "Konga", "industry": "E-commerce and retail", "location": "Lagos, Nigeria"},
    {"id": 17, "name": "Jumo", "industry": "Financial services", "location": "Cape Town, South Africa"},
    {"id": 18, "name": "M-kopa", "industry": "Energy and resources", "location": "Nairobi, Kenya"},
    {"id": 19, "name": "Cellulant", "industry": "Financial services", "location": "Nairobi, Kenya"},
    {"id": 20, "name": "African Leadership Academy", "industry": "Education", "location": "Cape Town, South Africa"},
    {"id": 21, "name": "Opay", "industry": "Financial services", "location": "Lagos, Nigeria"},
    {"id": 22, "name": "CarePay", "industry": "Financial services", "location": "Nairobi, Kenya"},
    {"id": 23, "name": "Powerhive", "industry": "Energy and environment resources", "location": "Nairobi, Kenya"},
    {"id": 24, "name": "Travelstart", "industry": "Travel and leisure", "location": "Cape Town, South Africa"},
    {"id": 25, "name": "Nabaki Afrika", "industry": "Construction and Real Estate", "location": "Dar es Salaam, Tanzania"},
    {"id": 26, "name": "Addis Property Marketing Group", "industry": "Construction and Real Estate", "location": "Addis Ababa, Ethiopia"},
    {"id": 27, "name": "Artniom", "industry": "Health and beauty", "location": "Abuja, Nigeria"},
    {"id": 28, "name": "Seminis East Africa", "industry": "Agricultural", "location": "Nairobi, Kenya"},
    {"id": 29, "name": "Floranet", "industry": "Agricultural", "location": "Nairobi, Kenya"},
    {"id": 30, "name": "Agribiz", "industry": "Agricultural", "location": "Ilupeju, Nigeria"},
    {"id": 31, "name": "Agriquip Agencies", "industry": "Agricultural", "location": "Nairobi, Kenya"},
    {"id": 32, "name": "Guludo Beach Lodge", "industry": "Hotels, Lodges and Toursim", "location": "Guludo, Mozambique"},
    {"id": 33, "name": "Lake Kariba", "industry": "Hotels, Lodges and Tourism", "location": "Lake Kariba, Zambia"},
    {"id": 34, "name": "Bulago", "industry": "Hotels, Lodges and Tourism", "location": "Kampala, Uganda"},
    {"id": 35, "name": "Kaingu Safari Lounge", "industry": "Hotels, Lodges and Tourism", "location": "Lusaka, Zambia"},
    {"id": 36, "name": "Boma Hotel", "industry": "Hotels, Lodges and Tourism", "location": "Entebbe, Uganda"},
    {"id": 37, "name": "Veroniach and Miencha Advocates", "industry": "Services", "location": "Nairobi, Kenya"},
    {"id": 39, "name": "General Maintenance", "industry": "Services", "location": "Baie Du Tombeau, Mauritius"},
    {"id": 40, "name": "Starffor Global", "industry": "Services", "location": "Port Louis, Mauritius"},
    {"id": 41, "name": "Magnate Venture Ltd", "industry": "Services", "location": "Nairobi, Kenya"},
    {"id": 42, "name": "Africa Furniture Importers Directory", "industry": "Home and Office Furniture", "location": "Africa, United Arab Emirates"},
    {"id": 43, "name": "Magari", "industry": "Home and Office Furniture", "location": "Nairobi, Kenya"},
    {"id": 44, "name": "Hwan Sung Ltd", "industry": "Home and Furniture", "location": "Kampala, Uganda"},
    {"id": 45, "name": "Antarc Enterprises Ltd", "industry": "Home and Furniture", "location": "Nairobi, Kenya"},
    {"id": 46, "name": "Elephant Group Limited", "industry": "Electronics and Electrical", "location": "Lagos, Nigeria"},
    {"id": 47, "name": "Arrow Altech Distribution", "industry": "Electronics and Electrical", "location": "Milnerton, South Africa"},
    {"id": 48, "name": "GAM Solar Energy and Engineering Co. Ltd", "industry": "Electronics and Electrical", "location": "Serrekunda, Gambia"},
    {"id": 49, "name": "BAJ Trading Ltd.", "industry": "Foodstuff and Beverages", "location":"Nairobi, Kenya"},
    {"id": 50, "name": "Ireland Blyth", "industry": "Foodstuff and Beverages", "location": "Port Louis, Mauritius"}
]

# Writing to JSON file
with open('companies.json', 'w') as json_file:
    json.dump(companies, json_file, indent=2)

#printing from the database
# for company in companies:
    #  print(f"ID: {company['id']}, Name: {company['name']}, Industry: {company['industry']}, Location: {company['location']}")

