# VIM PRACTICE 3: Python
# Exercises:
#  1. Jump between functions with ]] and [[ (or /def)
#  2. Rename "itm" to "item" in one function only: visual-select lines, then :s/\<itm\>/item/g
#  3. Change the arguments of add_item with ci(
#  4. Change the string "widget" with ci" and the number 12 with ciw
#  5. Delete a whole function with dap (delete around paragraph)
#  6. Swap two lines with ddp, swap two characters with xp
#  7. Increment the numbers in PRICES with Ctrl-a (cursor on a number)
#  8. Use . to repeat: change one "== None" to "is None" with cw, then n and .
#  9. Fold the class with zf} and open it again with zo
# 10. Sort the PRICES lines: select them with V and run :sort

PRICES = {
    "widget": 12,
    "gadget": 25,
    "doohickey": 7,
    "gizmo": 40,
    "thingamajig": 15,
}


class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name, qty, price):
        if self.items.get(name) == None:
            self.items[name] = {"qty": qty, "price": price}
        else:
            self.items[name]["qty"] += qty

    def remove_item(self, name, qty):
        if self.items.get(name) == None:
            raise KeyError(f"No such item: {name}")
        self.items[name]["qty"] -= qty
        if self.items[name]["qty"] <= 0:
            del self.items[name]

    def total_value(self):
        total = 0
        for itm in self.items.values():
            total += itm["qty"] * itm["price"]
        return total

    def low_stock(self, threshold=5):
        result = []
        for name, itm in self.items.items():
            if itm["qty"] < threshold:
                result.append(name)
        return result


def main():
    inv = Inventory()
    for name, price in PRICES.items():
        inv.add_item(name, 10, price)
    inv.remove_item("widget", 8)
    print("Total value:", inv.total_value())
    print("Low stock:", inv.low_stock())


if __name__ == "__main__":
    main()
