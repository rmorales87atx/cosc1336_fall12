# COSC 1336, Lab 8, Problem 2 (enhanced)
# Robert Morales

from io_util import get_int, get_float, get_bool, get_str

class Receipt:
    def __init__(self, line_width = 30):
        self.__file = None
        self.__width = line_width

    def open(self, filename = 'receipt2.txt'):
        self.__file = open(filename, 'w')
        self.print_header()

    def close(self):
        self.__file.close()

    # prints a line of n symbols
    def print_line(self, symbol = '', n = 1):
        print(symbol*n, file=self.__file)

    # prints the message, centered, with one symbol before and after
    def print_boxed_text(self, symbol, text, n):
        print("{0}{1:{fill}^{width}}{0}".format(symbol, text, fill=' ', \
                                                width=n-2), \
              file=self.__file)

    # prints a message in a box as the top of the receipt
    def print_header(self):
        ch = "*"
        self.print_line(ch, self.__width)
        self.print_boxed_text(ch, "Welcome to", self.__width)
        self.print_boxed_text(ch, "Cafe Python!", self.__width)
        self.print_line(ch, self.__width)
        self.print_line()

    # prints a single item and price
    def print_item(self, item, price, quantity = 1):
        price_label = "{:5,.2f}".format(price * quantity)
        width = self.__width - len(price_label)
        if quantity > 1:
            qty_label = "  {:3,.2f} @ {:3,.2f}".format(quantity, price)
            width -= len(qty_label)
            print(item, file=self.__file)
            print("{}{: <{width}}{}".format(qty_label, \
                                            '', price_label, \
                                            width=width), \
                  file=self.__file)
        else:
            print("{: <{width}}{}".format(item, price_label, width=width), \
                  file=self.__file)

    # prints the subtotal, tax, and total due
    def print_totals(self, subtotal, taxtotal, tax_rate = 0.0825):
        self.print_line("-", self.__width)
        self.print_item("Subtotal", subtotal)
        tax = taxtotal * tax_rate
        self.print_item("Tax", tax)
        self.print_line("-", self.__width)
        total_with_tax = subtotal + tax
        self.print_item("Total", total_with_tax)

        return total_with_tax

    # prints the amount paid and the change due
    def print_change(self, due, paid):
        self.print_line()
        self.print_item("Amount paid", paid)
        self.print_item("Change due", paid-due)

class Line:
    def __init__(self, name, price_per_unit, quantity, flags):
        self.name = name
        self.ppu = price_per_unit
        self.qty = quantity
        self.flags = flags

    def __repr__(self):
        return "Line({!r},{!r},{!r},{!r})".format(self.name, self.ppu, \
                                                  self.qty, self.flags)

    def total(self):
        return self.ppu * self.qty

    def is_taxable(self):
        return 'T' in self.flags

class Order:
    def __init__(self):
        self.lines = []

    def add_item(self, name, price, quantity = 1, flags = ''):
        self.lines.append(Line(name, price, quantity, flags))

    def void_line(self, number):
        del self.lines[number-1]

    def print_receipt(self):
        rec = Receipt()
        try:
            rec.open()

            subtotal = 0
            taxtotal = 0

            for item in self.lines:
                subtotal += item.total()
                if item.is_taxable():
                    taxtotal += item.total()
                rec.print_item(item.name, item.ppu, item.qty)

            rec.print_totals(subtotal, taxtotal)
        finally:
            rec.close()

class ItemInfo:
    def __init__(self, plu, name, price, flags):
        self.plu = plu
        self.name = name
        self.price = price
        self.flags = flags

    def __repr__(self):
        rep = "ItemInfo({!r}, {!r}, {!r}, {!r})"
        return rep.format(self.plu, self.name, self.price, self.flags)

    def is_taxable(self):
        return 'T' in self.flags

class ItemDatabase:
    def __init__(self):
        self.__items = []
        self.load_file()

    def clear(self):
        self.__items = []

    def load_file(self, filename = "items.txt"):
        with open(filename, 'r') as file:
            for line in iter(file.readline, ''):
                line = line.rstrip('\n')
                parser = iter(line.split('|'))
                code = int(next(parser))
                name = next(parser)
                price = float(next(parser))
                flags = next(parser).upper()
                self.__items.append(ItemInfo(code, name, price, flags))

    def count(self):
        return len(self.__items)

    def items(self):
        for item in self.__items:
            yield item

    def lookup(self, find_code):
        for item in self.__items:
            if item.plu == find_code:
                return item
        return None

#MAX_QUANTIY = 99
#MAX_PRICE = 9999.99

class Application:
    def __init__(self):
        self.max_plu = 1000000
        self.max_quantity = 99
        self.max_price = 9999.99

    def get_user_plu(self):
        return get_int("Enter item PLU (Ctrl+C to quit): ", \
                       limit=(0, self.max_plu))

    def get_user_item(self, plu):
        name = None

        while name is None or len(name) == 0:
            name = get_str("Enter item name: ")

        price = get_float("Enter item price: $", \
                          limit=(0, self.max_price+1))

        flags = ''

        if get_bool("Is item taxable?"):
            flags += 'T'
        if get_bool("Is this a food item?"):
            flags += 'F'

        return ItemInfo(plu, name, price, flags)

    def get_user_quantity(self, name):
        return get_float("Enter quantity of {}: ".format(name), \
                         limit=(0, self.max_quantity+1))

    def run(self):
        db = ItemDatabase()
        order = Order()

        for ent in iter(self.get_user_plu(), None)
            info = db.lookup(ent)

            if info is None:
                info = self.get_user_item(ent)

            qty = self.get_user_quantity(info.name)

            if qty is None:
                break

            if info.price * qty > 999999:
                print()
                print("Price of item is too high: ${:,.2f}, "
                      "cannot exceed ${:,.2f}.".format(info.price * qty, \
                                                       self.max_price))
                print("Entry discarded.")
                print()
            else:
                order.add_item(info.name, info.price, qty, info.flags)

        order.print_receipt()

app = Application()
app.run()
