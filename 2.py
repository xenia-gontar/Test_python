class Product:
    def init(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Food(Product):
  def init(self, name, price, quantity, calories, protein, fats, carbs):
    super().init(name, price, quantity, calories, protein, fats, carbs)
    self.calories = calories
    self.protein = protein
    self.fats = fats
    self.carbs = carbs
    
    
class Perish(Product):
    def init(self, name, price, quantity, calories, protein, fats, carbs, date_create, date_expire):
        super().init(name, price, quantity, calories, protein, fats, carbs)
        self.date_create = date_create
        self.date_expire = date_expire
      

class Vitamin(Product):
    def init(self, name, price, quantity, calories, protein, fats, carbs, prescription):
        super().init(name, price, quantity, protein, fats, carbs, calories)
        self.prescription = prescription


class Cart:
    def init(self, user_calories, user_protein, user_fats, user_carbs, user_prescription, current_date):
        self.user_calories = user_calories
        self.user_protein = user_protein
        self.user_fats = user_fats
        self.user_carbs = user_carbs
        self.user_calories = user_calories
        self.user_prescription = user_prescription
        self.product_list = []
        self.current_date = current_date
        
    def add_product(self, product):
        if isinstance(product, Vitamin) and product.prescription == 'Y' and self.user_prescription == 'Y':
            self.product_list.append(product)
        elif isinstance(product, Perish) and product.date_expire != self.current_date:
            self.product_list.append(product)
        elif isinstance(product, Food) and not isinstance(product, Perish):
            self.product_list.append(product)
          
        
    def count_price(self):
        total_price = 0
        for product in self.product_list:
            total_price = total_price + product.price
        return total_price

    def show_availability(self):
        non_available_products = []
        for product in self.product_list:
            if product.quantity == 0:
                non_available_products.append(product.name)
        print f'Sorry. {non_available_products} out of stock.'

    def check_overeating(self):
        total_calories = 0
        total_protein = 0
        total_fats = 0
        total_carbs = 0

        for product in self.product_list:
            total_calories = total_calories + product.calories
            total_protein =  total_protein + product.protein
            total_fats = total_fats + product.fats
            total_carbs =  total_carbs + product.carbs
        
        if (total_calories > self.user_calories) or (total_protein > self.user_protein) or (total_fats > self.user_fats) or (total_carbs > self.user_carbs):
            print "You went over your limit"

  

class Stock:
    def init(self, product_list, current_date):
        self.product_list = product_list
        self.current_date = current_date

    def get_utilised_products(self, current_date):
         utilised_products = []
        for product in self.product_list:
            if isinstance(product, Perish) and product.date_expire !=self. current_date:
                utilised_products.append(product.name)
        return utilised_products

    def get_ordered_products(self):
        non_available_products = []
        for product in self.product_list:
            if product.quantity == 0:
                non_available_products.append(product.name)
        return non_available_products
