class Checkout_Summary:
    def __init__(self, payment, shipping, sub_total, tax, total):
        self.payment = payment
        self.shipping = shipping
        self.sub_total = sub_total
        self.tax = tax
        self.total = total
