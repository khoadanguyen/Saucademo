class CheckoutSummary:
    def __init__(self, paymentInfo, shippingInfo, subTotal, tax, total):
        self.paymentInfo = paymentInfo
        self.shippingInfo = shippingInfo
        self.subTotal = subTotal
        self.tax = tax
        self.total = total
