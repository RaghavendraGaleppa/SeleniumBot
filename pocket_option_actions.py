import settings
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

stocks_opened = False


def open_asset_box(driver):
    driver.find_element(By.CSS_SELECTOR, value=settings.asset_box_selector).find_element(By.TAG_NAME, value=settings.a_tag).click()

def close_asset_box(driver):
    asset_box = driver.find_element(By.CSS_SELECTOR, value=settings.asset_box_selector)
    action = ActionChains(driver)
    action.move_to_element_with_offset(asset_box, 5, 5)
    action.click()
    action.perform()

def select_asset(driver, asset_num):

    global stocks_opened

    # Click asset box
    open_asset_box(driver)

    # CLick on stocks
    if stocks_opened == False:
        stocks_bar = driver.find_element(By.CSS_SELECTOR, value=settings.stocks_bar_selector)
        time.sleep(0.1)
        stocks_bar.click()
        stocks_opened = True

    # Select the asset
    asset_items = driver.find_elements(By.CSS_SELECTOR, value=settings.asset_item_selector)
    time.sleep(1)
    asset_items[asset_num].find_element(By.TAG_NAME, value=settings.a_tag).click()

    currency_pair, profit_pct = asset_items[asset_num].text.split('\n')
    profit_pct = int(profit_pct[:-1])

    # Close the asset box
    close_asset_box(driver)

    return currency_pair, profit_pct

def load_demo_page(driver):
    driver.get(settings.po_demo_page_url)
    driver.get(settings.po_continue_demo_trading_url)

def click_buy_button(driver):
    buy_button = driver.find_element(By.CLASS_NAME, value='btn-call')
    buy_button.click()

def click_sell_button(driver):
    sell_button = driver.find_element(By.CLASS_NAME, value='btn-put')
    sell_button.click()

def click_closed_button(driver):
    closed_button = driver.find_element(By.XPATH, value=settings.closed_button_xpath)
    closed_button.click()

def close_first_fail_modal(driver):
    try:
        first_fail_modal = driver.find_element(By.CSS_SELECTOR, value=settings.first_fail_modal_selector)
        time.sleep(0.3)
        first_fail_modal.click()
    except NoSuchElementException as e:
        pass

def click_good_job_notif(driver):
    good_job_notif = driver.find_elements(By.CSS_SELECTOR, value=settings.good_job_noti_selector)
    if len(good_job_notif) == 0:
        return 
    good_job_notif[0].click()

def get_buy_sell_info(driver):
    sells = driver.find_element(By.CSS_SELECTOR, value=settings.div_start_selector).text
    buys = driver.find_element(By.CSS_SELECTOR, value=settings.div_end_selector).text

    if int(buys[:-1]) > int(sells[:-1]):
        return 0
    return 1


def get_latest_trade_details(driver):
    """ Return the trade details such as profit/loss, opening time etc """
    click_closed_button(driver)

    latest_deals = driver.find_elements(By.CSS_SELECTOR, value=settings.deals_list_selector)
    if len(latest_deals) == 0:
        return -1

    latest_deal = driver.find_element(By.CSS_SELECTOR, value=settings.deals_list_selector)

    # Get the currency pair and profit percentage
    currency_pair, profit_pct = latest_deal.find_elements(By.CSS_SELECTOR, value=settings.item_row_selector)[0].text.split('\n')
    profit_pct = int(profit_pct[:-1])
    
    # Get the trade_price and price_up
    trade_price, price_up, _ = latest_deal.find_elements(By.CSS_SELECTOR, value=settings.item_row_selector)[-1].text.split('\n')
    trade_price = float(trade_price[1:])
    price_up = float(price_up[1:])

    time.sleep(0.3)
    latest_deal.click()
    opening_time = latest_deal.find_element(By.CSS_SELECTOR, value=settings.timer_selector).text.split('\n')[-1]
    time.sleep(0.3)
    latest_deal.click()

    profit = price_up-trade_price

    return {
            'trade_price': trade_price,
            'currency_pair': currency_pair,
            'profit_pct': profit_pct,
            'opening_time': opening_time,
            'profit': profit,
            }



def set_trade_price(driver, price):
    input_element = driver.find_element(By.CSS_SELECTOR, value=settings.trade_price_input_selector)

    for i in range(3):
        if input_element.get_attribute('value') == '':
            break
        input_element.clear()

    input_element.send_keys(price)


def clear_trade_expiry_input(driver):
    trade_time_limit_input = driver.find_element(By.CSS_SELECTOR, value=settings.trade_time_limit_input_selector)
    trade_time_limit_input.clear()


def open_trade_expiry_time(driver):
    trade_time_limit_box = driver.find_element(By.CSS_SELECTOR, value=settings.trade_time_limit_box_selector)
    trade_time_limit_box.click()

def set_trade_expiry_time(driver, time_in_secs):
    open_trade_expiry_time(driver)
    clear_trade_expiry_input(driver)
    plus_sign = driver.find_element(By.CSS_SELECTOR, value=settings.trade_time_limit_plus_sign)
    n_taps = time_in_secs - 5
    for i in range(n_taps):
        plus_sign.click()
        time.sleep(0.1)


def setup_zig_zag(driver):
    driver.find_element(By.CSS_SELECTOR, value=settings.indicator_box_selector).click()
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, value=settings.zig_zag_indicator_selector).click()
    close_asset_box(driver)

    driver.find_element(By.CSS_SELECTOR,value=settings.zig_zag_editor_selector).click()
    time.sleep(0.3)

    deviation_input = int(driver.find_element(By.CSS_SELECTOR, value=settings.zig_zag_deviation).get_attribute('value'))
    depth_input = int(driver.find_element(By.CSS_SELECTOR, value=settings.zig_zag_depth).get_attribute('value'))

    for i in range(deviation_input - 2):
        driver.find_element(By.CSS_SELECTOR, value=settings.deviation_down_arrow).click()

    for i in range(depth_input - 5):
        driver.find_element(By.CSS_SELECTOR, value=settings.depth_down_arrow).click()

    driver.find_element(By.CSS_SELECTOR, value=settings.zig_zag_save).click()



def set_timeframe(driver):
    driver.find_element(By.CSS_SELECTOR, value=settings.timeframe_selector).click()
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, value=settings.s15_timeframe_selector).click()
    driver.find_element(By.CSS_SELECTOR, value=settings.candlestick_expiry_selector).click()
    close_asset_box(driver)
