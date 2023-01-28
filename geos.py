def get_url(file_name):
    parts = file_name.split("_")
    name = "-".join(parts[1].split("-")[:3])
    if name[-1].isdigit():
        name = name[:len(name) - 1]
    year = parts[3][1:5]
    day_of_year = parts[3][5:8]
    hour = parts[3][8:10]
    url = f"https://noaa-goes18.s3.amazonaws.com/{name}/{year}/{day_of_year}/{hour}/{file_name}" 
    return url

LINK_4 = "OR_ABI-L2-ACHTM1-M6_G18_s20223560805242_e20223560805300_c20223560806526.nc"
LINK_5 = "OR_ABI-L2-BRFF-M6_G18_s20223150230207_e20223150239515_c20223150241087.nc"
print(get_url(LINK_5))
