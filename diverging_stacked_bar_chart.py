import altair as alt
# from altair_saver import save
import numpy as np
from plasma_colors_for_bar import calculate_plasma_colors_for_bar

# alt.renderers.set_embed_options(theme='dark')


def dark_theme():
    return {'config': {'background': 'black',
                       'axis': {'titleColor': 'white',
                                'domainColor': 'white',
                                'gridColor': 'white',
                                'labelColor': 'white',
                                'tickColor': 'white'},
                       'legend': {'labelColor': 'white',
                                  'tickColor': 'white'}
                       }
            }


alt.themes.register('dark_theme', dark_theme)
alt.themes.enable('dark_theme')


# alt.renderers.enable('png')

number_of_likert_scale_points = 7

# SENS ("Before class") Data
nature_data = np.array([0, 2, 3, 5, 3, 2, 0])

# SENS Data Analysis
number_of_respondents = np.sum(nature_data)
percentage_of_respondents = 100 * nature_data / number_of_respondents

p3half = 0.5 * percentage_of_respondents[3]

percentage_start = np.array([-p3half - percentage_of_respondents[2] - percentage_of_respondents[1]
                             - percentage_of_respondents[0],
                             -p3half - percentage_of_respondents[2] - percentage_of_respondents[1],
                             -p3half - percentage_of_respondents[2],
                             -p3half,
                             p3half,
                             p3half + percentage_of_respondents[4],
                             p3half + percentage_of_respondents[4] + percentage_of_respondents[5]])

percentage_end = percentage_start[1:]
percentage_end = np.append(percentage_end,
                           p3half + percentage_of_respondents[4] + percentage_of_respondents[5]
                           + percentage_of_respondents[6])

# AWE-S ("After class") Data
# Rows = Time, Self loss, Connection, Vastness, Physical, Accommodation
# Columns = # of {Strongly disagree, disagree, slightly disagree, neither agree nor disagree,
#                 slightly agree, agree, strongly agree} respondents
factors_of_awe_data = np.array([[0, 0, 6, 3, 4, 1, 0],
                                [0, 2, 3, 7, 2, 0, 0],
                                [0, 0, 5, 4, 4, 1, 0],
                                [0, 0, 2, 5, 3, 4, 0],
                                [0, 4, 1, 6, 2, 1, 0],
                                [0, 0, 1, 4, 4, 5, 0]])

number_of_factors = len(factors_of_awe_data[:, 0])
factors_percentage_of_respondents = 100 * factors_of_awe_data / number_of_respondents
middle_index = int(number_of_likert_scale_points/2)
factors_p3half = 0.5 * factors_percentage_of_respondents[:, middle_index]

factors_percentage_start = np.zeros([number_of_factors, number_of_likert_scale_points])

factors_percentage_start[:, middle_index] = -factors_p3half
for index in range(middle_index-1, -1, -1):
    factors_percentage_start[:, index] = factors_percentage_start[:, index+1] - \
                                         factors_percentage_of_respondents[:, index]

factors_percentage_start[:, middle_index+1] = factors_p3half
for index in range(middle_index+2, number_of_likert_scale_points):
    factors_percentage_start[:, index] = factors_percentage_start[:, index-1] + \
                                         factors_percentage_of_respondents[:, index]


factors_percentage_end = factors_percentage_start[:, 1:]
last_column = np.reshape(factors_p3half +
                         factors_percentage_of_respondents[:, 4] +
                         factors_percentage_of_respondents[:, 5] +
                         factors_percentage_of_respondents[:, 6], (number_of_factors, 1))

factors_percentage_end = np.append(factors_percentage_end, last_column, axis=1)


source = alt.pd.DataFrame([
    # {
    #     "question": "Pre-Class Awe",
    #     "type": "Strongly disagree",
    #     "value": nature_data[0],
    #     "percentage": percentage_of_respondents[0],
    #     "percentage_start": percentage_start[0],
    #     "percentage_end": percentage_end[0]
    # },
    # {
    #     "question": "Pre-Class Awe",
    #     "type": "Disagree",
    #     "value": nature_data[1],
    #     "percentage": percentage_of_respondents[1],
    #     "percentage_start": percentage_start[1],
    #     "percentage_end": percentage_end[1]
    # },
    # {
    #     "question": "Pre-Class Awe",
    #     "type": "Slightly disagree",
    #     "value": nature_data[2],
    #     "percentage": percentage_of_respondents[2],
    #     "percentage_start": percentage_start[2],
    #     "percentage_end": percentage_end[2]
    # },
    # {
    #     "question": "Pre-Class Awe",
    #     "type": "Neither agree nor disagree",
    #     "value": nature_data[3],
    #     "percentage": percentage_of_respondents[3],
    #     "percentage_start": percentage_start[3],
    #     "percentage_end": percentage_end[3]
    # },
    # {
    #     "question": "Pre-Class Awe",
    #     "type": "Slightly agree",
    #     "value": nature_data[4],
    #     "percentage": percentage_of_respondents[4],
    #     "percentage_start": percentage_start[4],
    #     "percentage_end": percentage_end[4]
    # },
    # {
    #     "question": "Pre-Class Awe",
    #     "type": "Agree",
    #     "value": nature_data[5],
    #     "percentage": percentage_of_respondents[5],
    #     "percentage_start": percentage_start[5],
    #     "percentage_end": percentage_end[5]
    # },
    # {
    #     "question": "Pre-Class Awe",
    #     "type": "Strongly agree",
    #     "value": nature_data[6],
    #     "percentage": percentage_of_respondents[6],
    #     "percentage_start": percentage_start[6],
    #     "percentage_end": percentage_end[6]
    # },
    {
        "question": "Time",
        "type": "Strongly disagree",
        "value": factors_of_awe_data[0][0],
        "percentage": factors_percentage_of_respondents[0][0],
        "percentage_start": factors_percentage_start[0][0],
        "percentage_end": factors_percentage_end[0][0]
    },
    {
        "question": "Time",
        "type": "Disagree",
        "value": factors_of_awe_data[0][1],
        "percentage": factors_percentage_of_respondents[0][1],
        "percentage_start": factors_percentage_start[0][1],
        "percentage_end": factors_percentage_end[0][1]
    },
    {
        "question": "Time",
        "type": "Slightly disagree",
        "value": factors_of_awe_data[0][2],
        "percentage": factors_percentage_of_respondents[0][2],
        "percentage_start": factors_percentage_start[0][2],
        "percentage_end": factors_percentage_end[0][2]
    },
    {
        "question": "Time",
        "type": "Neither agree nor disagree",
        "value": factors_of_awe_data[0][3],
        "percentage": factors_percentage_of_respondents[0][3],
        "percentage_start": factors_percentage_start[0][3],
        "percentage_end": factors_percentage_end[0][3]
    },
    {
        "question": "Time",
        "type": "Slightly agree",
        "value": factors_of_awe_data[0][4],
        "percentage": factors_percentage_of_respondents[0][4],
        "percentage_start": factors_percentage_start[0][4],
        "percentage_end": factors_percentage_end[0][4]
    },
    {
        "question": "Time",
        "type": "Agree",
        "value": factors_of_awe_data[0][5],
        "percentage": factors_percentage_of_respondents[0][5],
        "percentage_start": factors_percentage_start[0][5],
        "percentage_end": factors_percentage_end[0][5]
    },
    {
        "question": "Time",
        "type": "Strongly agree",
        "value": factors_of_awe_data[0][6],
        "percentage": factors_percentage_of_respondents[0][6],
        "percentage_start": factors_percentage_start[0][6],
        "percentage_end": factors_percentage_end[0][6]
    },
    {
        "question": "Self loss",
        "type": "Strongly disagree",
        "value": factors_of_awe_data[1][0],
        "percentage": factors_percentage_of_respondents[1][0],
        "percentage_start": factors_percentage_start[1][0],
        "percentage_end": factors_percentage_end[1][0]
    },
    {
        "question": "Self loss",
        "type": "Disagree",
        "value": factors_of_awe_data[1][1],
        "percentage": factors_percentage_of_respondents[1][1],
        "percentage_start": factors_percentage_start[1][1],
        "percentage_end": factors_percentage_end[1][1]
    },
    {
        "question": "Self loss",
        "type": "Slightly disagree",
        "value": factors_of_awe_data[1][2],
        "percentage": factors_percentage_of_respondents[1][2],
        "percentage_start": factors_percentage_start[1][2],
        "percentage_end": factors_percentage_end[1][2]
    },
    {
        "question": "Self loss",
        "type": "Neither agree nor disagree",
        "value": factors_of_awe_data[1][3],
        "percentage": factors_percentage_of_respondents[1][3],
        "percentage_start": factors_percentage_start[1][3],
        "percentage_end": factors_percentage_end[1][3]
    },
    {
        "question": "Self loss",
        "type": "Slightly agree",
        "value": factors_of_awe_data[1][4],
        "percentage": factors_percentage_of_respondents[1][4],
        "percentage_start": factors_percentage_start[1][4],
        "percentage_end": factors_percentage_end[1][4]
    },
    {
        "question": "Self loss",
        "type": "Agree",
        "value": factors_of_awe_data[1][5],
        "percentage": factors_percentage_of_respondents[1][5],
        "percentage_start": factors_percentage_start[1][5],
        "percentage_end": factors_percentage_end[1][5]
    },
    {
        "question": "Self loss",
        "type": "Strongly agree",
        "value": factors_of_awe_data[1][6],
        "percentage": factors_percentage_of_respondents[1][6],
        "percentage_start": factors_percentage_start[1][6],
        "percentage_end": factors_percentage_end[1][6]
    },
    {
        "question": "Connection",
        "type": "Strongly disagree",
        "value": factors_of_awe_data[2][0],
        "percentage": factors_percentage_of_respondents[2][0],
        "percentage_start": factors_percentage_start[2][0],
        "percentage_end": factors_percentage_end[2][0]
    },
    {
        "question": "Connection",
        "type": "Disagree",
        "value": factors_of_awe_data[2][1],
        "percentage": factors_percentage_of_respondents[2][1],
        "percentage_start": factors_percentage_start[2][1],
        "percentage_end": factors_percentage_end[2][1]
    },
    {
        "question": "Connection",
        "type": "Slightly disagree",
        "value": factors_of_awe_data[2][2],
        "percentage": factors_percentage_of_respondents[2][2],
        "percentage_start": factors_percentage_start[2][2],
        "percentage_end": factors_percentage_end[2][2]
    },
    {
        "question": "Connection",
        "type": "Neither agree nor disagree",
        "value": factors_of_awe_data[2][3],
        "percentage": factors_percentage_of_respondents[2][3],
        "percentage_start": factors_percentage_start[2][3],
        "percentage_end": factors_percentage_end[2][3]
    },
    {
        "question": "Connection",
        "type": "Slightly agree",
        "value": factors_of_awe_data[2][4],
        "percentage": factors_percentage_of_respondents[2][4],
        "percentage_start": factors_percentage_start[2][4],
        "percentage_end": factors_percentage_end[2][4]
    },
    {
        "question": "Connection",
        "type": "Agree",
        "value": factors_of_awe_data[2][5],
        "percentage": factors_percentage_of_respondents[2][5],
        "percentage_start": factors_percentage_start[2][5],
        "percentage_end": factors_percentage_end[2][5]
    },
    {
        "question": "Connection",
        "type": "Strongly agree",
        "value": factors_of_awe_data[2][6],
        "percentage": factors_percentage_of_respondents[2][6],
        "percentage_start": factors_percentage_start[2][6],
        "percentage_end": factors_percentage_end[2][6]
    },
    {
        "question": "Vastness",
        "type": "Strongly disagree",
        "value": factors_of_awe_data[3][0],
        "percentage": factors_percentage_of_respondents[3][0],
        "percentage_start": factors_percentage_start[3][0],
        "percentage_end": factors_percentage_end[3][0]
    },
    {
        "question": "Vastness",
        "type": "Disagree",
        "value": factors_of_awe_data[3][1],
        "percentage": factors_percentage_of_respondents[3][1],
        "percentage_start": factors_percentage_start[3][1],
        "percentage_end": factors_percentage_end[3][1]
    },
    {
        "question": "Vastness",
        "type": "Slightly disagree",
        "value": factors_of_awe_data[3][2],
        "percentage": factors_percentage_of_respondents[3][2],
        "percentage_start": factors_percentage_start[3][2],
        "percentage_end": factors_percentage_end[3][2]
    },
    {
        "question": "Vastness",
        "type": "Neither agree nor disagree",
        "value": factors_of_awe_data[3][3],
        "percentage": factors_percentage_of_respondents[3][3],
        "percentage_start": factors_percentage_start[3][3],
        "percentage_end": factors_percentage_end[3][3]
    },
    {
        "question": "Vastness",
        "type": "Slightly agree",
        "value": factors_of_awe_data[3][4],
        "percentage": factors_percentage_of_respondents[3][4],
        "percentage_start": factors_percentage_start[3][4],
        "percentage_end": factors_percentage_end[3][4]
    },
    {
        "question": "Vastness",
        "type": "Agree",
        "value": factors_of_awe_data[3][5],
        "percentage": factors_percentage_of_respondents[3][5],
        "percentage_start": factors_percentage_start[3][5],
        "percentage_end": factors_percentage_end[3][5]
    },
    {
        "question": "Vastness",
        "type": "Strongly agree",
        "value": factors_of_awe_data[3][6],
        "percentage": factors_percentage_of_respondents[3][6],
        "percentage_start": factors_percentage_start[3][6],
        "percentage_end": factors_percentage_end[3][6]
    },
    {
        "question": "Physical",
        "type": "Strongly disagree",
        "value": factors_of_awe_data[4][0],
        "percentage": factors_percentage_of_respondents[4][0],
        "percentage_start": factors_percentage_start[4][0],
        "percentage_end": factors_percentage_end[4][0]
    },
    {
        "question": "Physical",
        "type": "Disagree",
        "value": factors_of_awe_data[4][1],
        "percentage": factors_percentage_of_respondents[4][1],
        "percentage_start": factors_percentage_start[4][1],
        "percentage_end": factors_percentage_end[4][1]
    },
    {
        "question": "Physical",
        "type": "Slightly disagree",
        "value": factors_of_awe_data[4][2],
        "percentage": factors_percentage_of_respondents[4][2],
        "percentage_start": factors_percentage_start[4][2],
        "percentage_end": factors_percentage_end[4][2]
    },
    {
        "question": "Physical",
        "type": "Neither agree nor disagree",
        "value": factors_of_awe_data[4][3],
        "percentage": factors_percentage_of_respondents[4][3],
        "percentage_start": factors_percentage_start[4][3],
        "percentage_end": factors_percentage_end[4][3]
    },
    {
        "question": "Physical",
        "type": "Slightly agree",
        "value": factors_of_awe_data[4][4],
        "percentage": factors_percentage_of_respondents[4][4],
        "percentage_start": factors_percentage_start[4][4],
        "percentage_end": factors_percentage_end[4][4]
    },
    {
        "question": "Physical",
        "type": "Agree",
        "value": factors_of_awe_data[4][5],
        "percentage": factors_percentage_of_respondents[4][5],
        "percentage_start": factors_percentage_start[4][5],
        "percentage_end": factors_percentage_end[4][5]
    },
    {
        "question": "Physical",
        "type": "Strongly agree",
        "value": factors_of_awe_data[4][6],
        "percentage": factors_percentage_of_respondents[4][6],
        "percentage_start": factors_percentage_start[4][6],
        "percentage_end": factors_percentage_end[4][6]
    },
    {
        "question": "Accommodation",
        "type": "Strongly disagree",
        "value": factors_of_awe_data[5][0],
        "percentage": factors_percentage_of_respondents[5][0],
        "percentage_start": factors_percentage_start[5][0],
        "percentage_end": factors_percentage_end[5][0]
    },
    {
        "question": "Accommodation",
        "type": "Disagree",
        "value": factors_of_awe_data[5][1],
        "percentage": factors_percentage_of_respondents[5][1],
        "percentage_start": factors_percentage_start[5][1],
        "percentage_end": factors_percentage_end[5][1]
    },
    {
        "question": "Accommodation",
        "type": "Slightly disagree",
        "value": factors_of_awe_data[5][2],
        "percentage": factors_percentage_of_respondents[5][2],
        "percentage_start": factors_percentage_start[5][2],
        "percentage_end": factors_percentage_end[5][2]
    },
    {
        "question": "Accommodation",
        "type": "Neither agree nor disagree",
        "value": factors_of_awe_data[5][3],
        "percentage": factors_percentage_of_respondents[5][3],
        "percentage_start": factors_percentage_start[5][3],
        "percentage_end": factors_percentage_end[5][3]
    },
    {
        "question": "Accommodation",
        "type": "Slightly agree",
        "value": factors_of_awe_data[5][4],
        "percentage": factors_percentage_of_respondents[5][4],
        "percentage_start": factors_percentage_start[5][4],
        "percentage_end": factors_percentage_end[5][4]
    },
    {
        "question": "Accommodation",
        "type": "Agree",
        "value": factors_of_awe_data[5][5],
        "percentage": factors_percentage_of_respondents[5][5],
        "percentage_start": factors_percentage_start[5][5],
        "percentage_end": factors_percentage_end[5][5]
    },
    {
        "question": "Accommodation",
        "type": "Strongly agree",
        "value": factors_of_awe_data[5][6],
        "percentage": factors_percentage_of_respondents[5][6],
        "percentage_start": factors_percentage_start[5][6],
        "percentage_end": factors_percentage_end[5][6]
    }
])

plasma_colors = calculate_plasma_colors_for_bar(number_of_likert_scale_points)

color_scale = alt.Scale(
    domain=[
        "Strongly disagree",
        "Disagree",
        "Slightly disagree",
        "Neither agree nor disagree",
        "Slightly agree",
        "Agree",
        "Strongly agree"
    ],
    range=plasma_colors
)

y_axis = alt.Axis(
    title='Factors of Awe',
    offset=5,
    ticks=False,
    minExtent=60,
    domain=False
)

x_axis = alt.Axis(
    title='Disagree/Agree (%)',
    offset=5
)

chart = alt.Chart(source, height=256, width=512).mark_bar().encode(
    x=alt.X('percentage_start:Q', axis=x_axis),
    x2='percentage_end:Q',
    y=alt.Y('question:N', axis=y_axis),
    color=alt.Color(
        'type:N',
        legend=alt.Legend(title='Response'),
        scale=color_scale,
    )
).configure_axis(labelFontSize=18, titleFontSize=18)

chart.configure_legend(labelFontSize=18, titleFontSize=18)

chart.show()

# save(chart, 'example_chart.png')
