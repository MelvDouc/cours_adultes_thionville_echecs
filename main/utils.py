import re
from datetime import date
from urllib.request import urlopen


def calculate_age():
    birth_date = date(1991, 12, 29)
    today = date.today()
    years_diff = today.year - birth_date.year
    months_diff = today.month - birth_date.month
    days_diff = today.day - birth_date.day

    if days_diff < 0:
        months_diff -= 1
    if months_diff < 0:
        years_diff -= 1

    return years_diff


def get_std_rating():
    page = urlopen("https://ratings.fide.com/profile/36067962")
    html = page.read().decode("utf-8")
    regex = r'<div class="profile-top-rating-data profile-top-rating-data_gray">\s*<span class="profile-top-rating-dataDesc">std</span>\s*\d{4}\s*</div>'
    try:
        element = re.findall(regex, html)[0]
        return re.findall(r'\d{4}', element)[0]
    except:
        return "entre 1900 et 2000"
