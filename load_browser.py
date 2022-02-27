from selenium import webdriver
from selenium.webdriver.common.by import By
import settings
import time
import pocket_option_actions as poa
import numpy as np
from collections import deque

driver = webdriver.Chrome()

def test_demo(driver):
    poa.load_demo_page(driver)

#

def run_demo(driver):

    poa.load_demo_page(driver)
    poa.set_timeframe(driver)
    poa.setup_zig_zag(driver)
    # Set the expiry time
    time.sleep(1)
    poa.set_trade_expiry_time(driver, settings.TRADE_EXPIRIY_TIME)
    i = 0
    switch = 0

    n_carries = 0 # Number of losses in a chain
    current_losses = 0 # Used for caary forwarding
    current_wins = 0
    current_profit = 0

    d = deque(maxlen=3)

    total_wins = 0
    total_losses = 0 # 
    total_profit_amount = 0
    trade_price = settings.BASE_PRICE
    total_trades_taken = 0
    first_trade = True
    
    while True:
        # Select an Asset
        currency_pair, profit_pct = poa.select_asset(driver, i)

        # Check the last trade 
        last_trade = poa.get_latest_trade_details(driver)
        
        print("="*70)
        if last_trade == -1:
            print("No Trades executed yet")

        else:
            print(last_trade)
            total_trades_taken += 1

            # If the last trade was a success
            poa.click_good_job_notif(driver)

            total_profit_amount += last_trade['profit']
            
            if last_trade['profit'] > 0:
                # Update profit value
                if settings.MODE == 3:
                    if current_wins == settings.MAX_WINS - 1:
                        #total_profit_amount += (trade_price+last_trade['profit']) - settings.BASE_PRICE
                        trade_price = settings.BASE_PRICE
                        current_wins = 0
                    else:
                        trade_price += last_trade['profit']
                        current_wins = (current_wins + 1) % settings.MAX_WINS

                elif settings.MODE == 4:
                    if n_carries == 0:
                        if current_wins == settings.MAX_WINS - 1:
                            trade_price = settings.BASE_PRICE
                            current_profit = 0
                            total_wins += 1

                        else:
                            current_profit += last_trade['profit']
                            trade_price = settings.BASE_PRICE + current_profit

                        current_wins = (current_wins + 1) % settings.MAX_WINS
                    else:
                        n_carries = 0
                        current_losses = 0
                        trade_price = settings.BASE_PRICE + current_profit

                else:
                    if n_carries == 0:
                        #total_profit_amount += last_trade['profit']
                        total_wins += 1

                    # Reset the carry parameters
                    n_carries = 0
                    current_losses = 0
                    trade_price = settings.BASE_PRICE

            # If you have lost the last trade
            elif last_trade['profit'] < 0:
                if (n_carries == settings.MAX_RETRIES - 1) and (settings.MODE != 3):

                    #total_profit_amount -= current_losses + trade_price
                    total_losses += 1
                    n_carries = 0
                    current_losses = 0
                    trade_price = settings.BASE_PRICE
                else:
                    n_carries = (n_carries+1) % settings.MAX_RETRIES
                    if settings.MODE == 1:
                        current_losses += trade_price
                        trade_price = trade_price * 2
                    elif settings.MODE == 2:
                        current_losses += trade_price
                        trade_price = current_losses/(profit_pct/100)

                    elif settings.MODE == 4:
                        current_losses += trade_price
                        trade_price = current_losses/(profit_pct/100)
                    elif settings.MODE == 3:
                        #total_profit_amount -= settings.BASE_PRICE
                        current_wins = 0
                        trade_price = settings.BASE_PRICE


        # Put the price into input bar
        poa.set_trade_price(driver, trade_price)

        # Click Buy or Sell
        #switch = 0
        switch = np.random.randint(0,2)

        #if settings.MODE == 3:
        #else:
        #    switch = poa.get_buy_sell_info(driver)

        #if sum(d) == 3:
        #    switch = 0
        #elif sum(d) == 0:
        #    switch = 1

        d.append(switch) 
        #if switch == 0:
        #    poa.click_buy_button(driver)

        #else:
        #    poa.click_sell_button(driver)


        print("="*70)
        print(f"{trade_price:.2f} || {n_carries} || {current_losses:.2f}")
        print("="*70)
        print(f"{total_trades_taken} || {total_profit_amount:.2f} || {total_wins} || {total_losses}")
        print("="*70)
        print("\n")

        # Sleep for a while
        time.sleep(settings.TRADE_EXPIRIY_TIME*2-2)

        if first_trade == True:
            poa.close_first_fail_modal(driver)
            first_trade = False

        # Update Counters
        i = (i+1) % 5
        switch = (switch + 1) % 10


