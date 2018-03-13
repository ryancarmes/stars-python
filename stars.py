star_list = [5, "Barry", 15]
def draw_stars(list):
    list = star_list
    for x in range(0, len(list)):
        star_dust = ""
        if isinstance(star_list[x], int):
            for y in range(0, list[x]):
                star_dust = star_dust + str("*")
            print star_dust
        elif isinstance(star_list[x], str):
            for y in range(0, len(list[x])):
                star_dust = star_dust + star_list[x][0]
            print star_dust.lower()

draw_stars(star_list)