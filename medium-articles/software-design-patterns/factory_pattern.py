from abc import ABC, abstractmethod

# Step 1: Define an abstract base class for PaymentProcessor
class PaymentProcessor(ABC):
    
    @abstractmethod
    def process_payment(self, amount):
        pass


# Step 2: Define concrete classes for each payment method

class CreditCardPayment(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}.")

class PayPalPayment(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}.")

class BankTransferPayment(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing bank transfer payment of ${amount}.")


# Step 3: Create the PaymentFactory class
class PaymentFactory:
    
    @staticmethod
    def get_payment_processor(payment_type):
        if payment_type == "credit_card":
            return CreditCardPayment()
        elif payment_type == "paypal":
            return PayPalPayment()
        elif payment_type == "bank_transfer":
            return BankTransferPayment()
        else:
            raise ValueError(f"Unknown payment type: {payment_type}")


# Step 4: Client code (e.g., checkout system) using the factory
def checkout(payment_type, amount):
    # Use the factory to get the correct payment processor
    payment_processor = PaymentFactory.get_payment_processor(payment_type)
    payment_processor.process_payment(amount)

# Example usage:
checkout("credit_card", 100)   # Outputs: Processing credit card payment of $100.
checkout("paypal", 50)         # Outputs: Processing PayPal payment of $50.
checkout("bank_transfer", 200) # Outputs: Processing bank transfer payment of $200.
