from pygal_maps_world.i18n import COUNTRIES


# for country_code in sorted(COUNTRIES.keys()):
#     print(country_code, COUNTRIES[country_code])
def get_ccountry_name(country_name):
    for code, country_name1 in COUNTRIES.items():
        if country_name == country_name1:
            return code
    return None
# print(get_ccountry_name("China"))
