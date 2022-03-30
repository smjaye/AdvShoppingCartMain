import datetime

from faker import Faker
fake = Faker(locale='en_CA')




#-----------------------Advantage Shopping App Data parameters-------------------------
app = 'advantage shopping cart'
advantage_shopping_url = 'https://advantageonlineshopping.com/#/'
advantage_shopping_homepage_title = "\xa0Advantage Shopping"
advantage_shopping_orderpage_url = 'https://advantageonlineshopping.com/#/MyOrders'

username = fake.user_name()[0:15]
password = fake.password()
first_name = fake.first_name()
last_name = fake.last_name()
full_name = f'{first_name} {last_name}'
email = fake.email()
phone_number = fake.phone_number()
city = fake.city()
country = fake.current_country()
address = fake.street_address()
state = fake.province_abbr()
postalcode = fake.postcode()

product_list = ['SPEAKERS', 'TABLETS', 'LAPTOPS', 'HEADPHONES', 'MICE']

Subject = fake.sentence(100)