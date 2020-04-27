from matplotlib import cm, colors


def calculate_plasma_colors_for_bar(number_of_likert_scale_points):
    plasma_colors = cm.get_cmap('plasma')
    color_range = range(1, number_of_likert_scale_points+1)

    def convert_to_unit_range(likert_number):
        normalized_value = (likert_number - 1.) / (number_of_likert_scale_points - 1.)
        return normalized_value

    color_range = [convert_to_unit_range(value) for value in color_range]

    hexadecimal_rgb_color = []

    for normalized_color_value in color_range:
        rgb_value = plasma_colors(normalized_color_value)
        hexadecimal_rgb_color.append(colors.to_hex(rgb_value))

    return hexadecimal_rgb_color


