from seleniumbase import SB

with SB(uc=True, test=True, incognito=True) as sb:
    url = "https://seleniumbase.io/apps/invisible_recaptcha"
    sb.activate_cdp_mode(url)
    sb.sleep(1)
    sb.assert_element("img#captcha-success", timeout=3)
    sb.set_messenger_theme(location="top_left")
    sb.post_message("SeleniumBase wasn't detected", duration=3)
