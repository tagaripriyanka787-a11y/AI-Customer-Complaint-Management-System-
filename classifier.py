def classify(text):
    text = text.lower()

    if "refund" in text:
        return "Refund"

    elif "delivery" in text:
        return "Delivery"

    elif "payment" in text:
        return "Payment"

    else:
        return "General"