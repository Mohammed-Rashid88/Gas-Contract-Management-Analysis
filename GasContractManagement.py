from datetime import date
import math

def manage_gas_contract(input_dates, input_prices, output_dates, output_prices, injection_rate, storage_rate, max_volume, transaction_cost_rate):
    
    current_volume = 0
    total_purchase_cost = 0
    total_revenue = 0
    earliest_date = min(min(input_dates), min(output_dates))
    
    #  sorted list of all relevant dates
    combined_dates = sorted(set(input_dates + output_dates))
    
    for date_index in range(len(combined_dates)):
       
        current_date = combined_dates[date_index]

        if current_date in input_dates:
            # handle gas injection for input dates and calculate associated costs
            if current_volume <= max_volume - injection_rate:
                current_volume += injection_rate

                # calculate the cost of buying gas
                purchase_price = input_prices[input_dates.index(current_date)]
                total_purchase_cost += injection_rate * purchase_price
                # calculate the cost of injecting gas
                injection_cost = injection_rate * transaction_cost_rate
                total_purchase_cost += injection_cost
                print(f'Injected gas on {current_date} at a price of {purchase_price}')

            else:
                # handle cases where there's insufficient storage capacity
                print(f'Injection not feasible on {current_date} due to insufficient storage capacity')

        elif current_date in output_dates:
            # handle gas withdrawal for output dates and calculate revenue and costs
            if current_volume >= injection_rate:
                current_volume -= injection_rate
                withdrawal_price = output_prices[output_dates.index(current_date)]
                total_revenue += injection_rate * withdrawal_price
                # calculate the cost of withdrawing gas
                withdrawal_cost = injection_rate * transaction_cost_rate
                total_revenue -= withdrawal_cost
                print(f'Extracted gas on {current_date} at a price of {withdrawal_price}')
            else:
                # handle cases where there's insufficient gas stored
                print(f'Withdrawal not feasible on {current_date} due to insufficient gas volume')
                
    # calculate storage costs based on the duration of storage
    storage_duration = math.ceil((max(output_dates) - min(input_dates)).days / 30)
    total_storage_cost = storage_duration * storage_rate

    return total_storage_cost
