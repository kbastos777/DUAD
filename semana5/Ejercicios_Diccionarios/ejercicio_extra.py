ventas = [
	{
		'date': '30/04/21',
		'customer_email': 'marco@gmail.com',
		'items': [
			{
				'name': 'Shampoo',
				'upc': 'ITEM-453',
				'unit_price': 25.76,
			},
			{
				'name': 'Cereal',
				'upc': 'ITEM-324',
				'unit_price': 30.45,
			},
			{
				'name': 'Goma_de_mascar',
				'upc': 'ITEM-432',
				'unit_price': 15.54,
			},
		],
	},
	{
		'date': '07/02/21',
		'customer_email': 'lau@gmail.com',
		'items': [
			{
				'name': 'Shampoo',
				'upc': 'ITEM-453',
				'unit_price': 25.76,
			},
			{
				'name': 'Cereal',
				'upc': 'ITEM-324',
				'unit_price': 30.45,
			},
		],
	},
	{
		'date': '01/01/22',
		'customer_email': 'pablo@gmail.com',
		'items': [
			{
				'name': 'Cereal',
				'upc': 'ITEM-324',
				'unit_price': 30.45,
			},
			{
				'name': 'Shampoo',
				'upc': 'ITEM-453',
				'unit_price': 25.76,
			},
		],
	},
]
contador_uno = 0
contador_dos = 0
contador_tres = 0

resultado = {}
for index , record in enumerate(ventas):
		for index, record in enumerate(record["items"]):
			if record["upc"] == "ITEM-453":
				contador_uno += record["unit_price"]
				resultado[record["upc"]] = contador_uno
			elif record["upc"] == "ITEM-324":
				contador_dos += record["unit_price"]
				resultado[record["upc"]] = contador_dos
			elif record["upc"] == "ITEM-432":
				contador_tres += record["unit_price"]
				resultado[record["upc"]] = contador_tres


for upc, unit_price in resultado.items():
	print(f"{upc} : {unit_price}")