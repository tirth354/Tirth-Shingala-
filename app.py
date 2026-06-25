
import time
import pandas as pd

from transaction_generator import generate_transaction
from fraud_detector import predict_fraud

while True:

    transaction = generate_transaction()

    prediction, probability = predict_fraud(transaction)
    risk_score = probability * 100

    print("\n=========================================")
    print("UPI FRAUD ANALYSIS REPORT")
    print("=========================================")

    print(f"Transaction ID : {transaction['transaction_id']}")
    print(f"Timestamp      : {transaction['timestamp']}")
    print(f"User ID        : {transaction['user_id']}")
    print(f"UPI ID         : {transaction['upi_id']}")
    print(f"Location       : {transaction['location']}")
    print(f"Amount         : ₹{transaction['amount']}")
    print(f"Merchant       : {transaction['merchant']}")
    print(f"Risk Score     : {risk_score:.2f}%")

    if prediction == 1:
        print("Status         : ⚠ HIGH RISK FRAUD DETECTED")
    else:
        print("Status         : ✓ SAFE TRANSACTION")

    print("=========================================")

    choice = input(
        "\nType 'next' for another transaction,\n"
        "'check' to search a transaction,\n"
        "or 'exit' to quit: "
    ).lower()

    if choice == "next":
        continue

    elif choice == "check":
        txn_id = input("Enter Transaction ID: ")

        try:
            import pandas as pd

            df = pd.read_csv("transaction_log.csv")

            result = df[df["Transaction_ID"] == txn_id]

            if len(result) == 0:
                print("\n❌ Transaction not found.")

            else:
                row = result.iloc[0]

                print("\n================================")
                print("TRANSACTION STATUS")
                print("================================")
                print(f"Transaction ID : {row['Transaction_ID']}")
                print(f"Amount         : ₹{row['Amount']}")
                print(f"Risk Score     : {row['Risk_Score']}%")

                if row['Fraud'] == 1:
                    print("Status         : ⚠ FRAUD DETECTED")
                else:
                    print("Status         : ✓ SAFE TRANSACTION")

                print("================================")

        except:
            print("No transaction log found.")

    elif choice == "exit":
        print("System Closed.")
        break

    else:
        print("Invalid Choice.")
        break