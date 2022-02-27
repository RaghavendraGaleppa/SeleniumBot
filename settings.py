po_home_page_url = "https://pocketoption.com"
po_demo_page_url = "https://pocketoption.com/en/cabinet/demo-high-low/?try-demo=1"
po_continue_demo_trading_text = "Continue Demo trading"

po_continue_demo_trading_url = "https://pocketoption.com/en/cabinet/demo-quick-high-low/"

asset_item_selector = "div.asset-item"
asset_box_selector = "div.currencies-block__in"

a_tag = "a"

closed_button_xpath = u'//a[contains(text(), "Closed")]'
first_fail_modal_selector = "a.mfp-close"
deals_list_selector = "div.deals-list__item"

price_up_selector = "div.price-up"
timer_selector = "div.timer"
item_row_selector = "div.item-row"

trade_price_input_selector = "#put-call-buttons-chart-1 > div > div.blocks-wrap > div.block.block--bet-amount > div.block__control.control > div.control__value.value.value--several-items > div > input[type=text]"

good_job_noti_selector = "body > div.notification.notification--good-job.js-notification.js-notification--good-job > div > div.buttons > a.btn.btn-danger-light.js-close-notice"


trade_time_limit_box_selector = "#put-call-buttons-chart-1 > div > div.blocks-wrap > div.block.block--expiration-inputs > div.block__control.control > div.control__value.value.value--several-items > div"
trade_time_limit_input_selector = "#modal-root > div.drop-down-modal-wrap.no-outside > div > div > div > div:nth-child(3) > div > input[type=text]"
trade_time_limit_plus_sign = "#modal-root > div.drop-down-modal-wrap.no-outside > div > div > div > div:nth-child(3) > a.btn-plus"

stocks_bar_selector = "#quotes-list > div.tab-nav > div.tab-nav__row1 > ul > li.stock > a"

div_start_selector = "#market-watch > div > div.pb > div > div.start"
div_end_selector = '#market-watch > div > div.pb > div > div.end'

timeframe_selector = "#bar-chart > div > div > div.layout-container > div > div.top-left-block > div.top-left-block__block1 > div.items > a:nth-child(1)"

s15_timeframe_selector = "#modal-root > div.drop-down-modal-wrap.drop-down-modal-wrap-appear-done.drop-down-modal-wrap-enter-done > div > div.time-frames-block > ul > li:nth-child(3) > a"

candlestick_expiry_selector = "#modal-root > div.drop-down-modal-wrap.drop-down-modal-wrap-appear-done.drop-down-modal-wrap-enter-done > div > div.settings-block > div.settings-block__in > div:nth-child(1) > label > div.mdl-switch__thumb"

indicator_box_selector = "#bar-chart > div > div > div.layout-container > div > div.top-left-block > div.top-left-block__block1 > div.items > a.tooltip2.items__link.items__link--indicators"

zig_zag_indicator_selector = "#modal-root > div.drop-down-modal-wrap.drop-down-modal-wrap-appear-done.drop-down-modal-wrap-enter-done > div > div > div > div.all-block.tab-body-block > div > div:nth-child(3) > div:nth-child(10) > a.list-item-block"

zig_zag_editor_selector = "#bar-chart > div > div > div.layout-container > div > div.top-left-block > div.top-left-block__block2 > div.current-indicators.open > ul > li > div > a:nth-child(2)"

zig_zag_deviation = "body > div:nth-child(23) > div > div > div.m-content > div > div.fields > div:nth-child(1) > div > div.input-wrapper__input > input[type=number]"

zig_zag_depth = "body > div:nth-child(23) > div > div > div.m-content > div > div.fields > div:nth-child(2) > div > div.input-wrapper__input > input[type=number]"

zig_zag_save = "body > div:nth-child(23) > div > div > div.m-footer > div:nth-child(2) > a.btn.btn-green-light"

deviation_down_arrow = "body > div:nth-child(23) > div > div > div.m-content > div > div.fields > div:nth-child(1) > div > div.input-wrapper__arrows > div:nth-child(2)"

depth_down_arrow = "body > div:nth-child(23) > div > div > div.m-content > div > div.fields > div:nth-child(2) > div > div.input-wrapper__arrows > div:nth-child(2)"


# TRADING SETTINGS
BASE_PRICE = 1
MAX_RETRIES = 3
TRADE_EXPIRIY_TIME = 10
MODE = 4 # 1-Double, 2-Normal, 3-CarryForward, 4 - Chain Wins
MAX_WINS = 3


