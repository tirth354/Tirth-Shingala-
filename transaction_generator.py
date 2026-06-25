import random
from datetime import datetime

def generate_transaction():

    transaction = {
        "transaction_id":
            "TXN" + str(random.randint(100000, 999999)),

        "timestamp":
            datetime.now().strftime("%d-%m-%Y %H:%M:%S"),

        "user_id":
            "USER" + str(random.randint(1000, 9999)),

        "upi_id":
            "user" + str(random.randint(1000, 9999)) + "@upi",

        "ip_address":
            f"103.{random.randint(1,255)}."
            f"{random.randint(1,255)}."
            f"{random.randint(1,255)}",

        "location":
            random.choice(
                [
                    "Ahmedabad, Gujarat",
                    "Surat, Gujarat",
                    "Mumbai, Maharashtra",
                    "Delhi, India"
                ]
            ),

        "device_id":
            "ANDROID-" + str(random.randint(10000, 99999)),

        "amount":
            random.randint(100, 20000),

        "merchant":
            random.choice(
                [
                    "Amazon",
                    "Flipkart",
                    "ABC Electronics",
                    "Reliance Store"
                ]
            ),

        "hour":
            datetime.now().hour,

        "new_device":
            random.randint(0, 1),

        "location_mismatch":
            random.randint(0, 1)
    }

    return transaction