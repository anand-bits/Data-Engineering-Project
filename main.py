import random
from faker import Faker
from confluent_kafka import SerializingProducer 
from datetime import datetime  # Add this import statement

fake = Faker()

def generate_sales_transactions():
    user = fake.simple_profile()
    
    return {
        "transactionId": fake.uuid4(),
        "productId": random.choice(['product1', 'product2', 'product3', 'product4', 'product5', 'product6']),
        "productName": random.choice(['laptop', 'mobile', 'tablet', 'watch', 'headphone', 'speaker']),
        'productCategory': random.choice(['electronic', 'fashion', 'grocery', 'home', 'beauty', 'sports']),
        "price": round(random.uniform(10.0, 1000.0), 2),
        "quantity": random.randint(1, 10),
        "customerName": fake.name(),
        "customerEmail": fake.email(),
        "transactionDate": fake.date_time_this_year(),
        "paymentMethod": random.choice(['credit_card', 'debit_card', 'paypal', 'cash']),
        "shippingAddress": fake.address(),
        "isCompleted": random.choice([True, False]),
        "customerId": user['username']
    }

def main():
    topic = 'Financial_transaction'
    producer = SerializingProducer({
        'bootstrap.servers': 'localhost:9092'
    })
    
    curr_time = datetime.now()  # Corrected the datetime.now() call
    
    while (datetime.now() - curr_time).seconds < 120:
        try:
            transaction = generate_sales_transactions()
            transaction['totalAmount'] = transaction['price'] * transaction['quantity']  # Corrected variable access
            
         
            
            print("Transaction sent to Kafka:", transaction)
        except Exception as e:  # Catching all exceptions for simplicity
            print("Error occurred:", e)

if __name__ == "__main__":
    main()
