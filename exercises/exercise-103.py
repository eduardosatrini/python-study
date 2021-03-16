from utility.calc import calc
from utility.validate import validate


value = validate.coin("Enter a price: ")
calc.table_price(value, 12, 19)
