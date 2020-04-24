import altair as alt
from altair_saver import save
import numpy as np

alt.renderers.enable('png')

nature_data = np.array([0, 2, 3, 5, 3, 2, 0])

factors_of_awe_data = np.array([[1, 2, 3, 4, 5, 6, 7],
                                [1, 2, 3, 4, 5, 6, 7],
                                [1, 2, 3, 4, 5, 6, 7],
                                [1, 2, 3, 4, 5, 6, 7],
                                [1, 2, 3, 4, 5, 6, 7],
                                [1, 2, 3, 4, 5, 6, 7]])

number_of_respondents = np.sum(nature_data)
percentage_of_respondents = 100 * nature_data / number_of_respondents
factors_percentage_of_respondents = 100 * factors_of_awe_data / number_of_respondents

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

factors_p3half = 0.5 * factors_percentage_of_respondents[:, 3]
factors_percentage_start = np.array([])


source = alt.pd.DataFrame([
      {
        "question": "Pre-Class Awe",
        "type": "Strongly disagree",
        "value": nature_data[0],
        "percentage": percentage_of_respondents[0],
        "percentage_start": percentage_start[0],
        "percentage_end": percentage_end[0]
      },
    {
        "question": "Pre-Class Awe",
        "type": "Disagree",
        "value": nature_data[1],
        "percentage": percentage_of_respondents[1],
        "percentage_start": percentage_start[1],
        "percentage_end": percentage_end[1]
    },
    {
        "question": "Pre-Class Awe",
        "type": "Slightly disagree",
        "value": nature_data[2],
        "percentage": percentage_of_respondents[2],
        "percentage_start": percentage_start[2],
        "percentage_end": percentage_end[2]
    },
    {
        "question": "Pre-Class Awe",
        "type": "Neither agree nor disagree",
        "value": nature_data[3],
        "percentage": percentage_of_respondents[3],
        "percentage_start": percentage_start[3],
        "percentage_end": percentage_end[3]
    },
    {
         "question": "Pre-Class Awe",
         "type": "Slightly agree",
         "value": nature_data[4],
         "percentage": percentage_of_respondents[4],
         "percentage_start": percentage_start[4],
         "percentage_end": percentage_end[4]
    },
    {
         "question": "Pre-Class Awe",
         "type": "Agree",
         "value": nature_data[5],
         "percentage": percentage_of_respondents[5],
         "percentage_start": percentage_start[5],
         "percentage_end": percentage_end[5]
    },
      {
        "question": "Pre-Class Awe",
        "type": "Strongly agree",
        "value": nature_data[6],
        "percentage": percentage_of_respondents[6],
        "percentage_start": percentage_start[6],
        "percentage_end": percentage_end[6]
      }

      # {
      #   "question": "Question 2",
      #   "type": "Strongly disagree",
      #   "value": 2,
      #   "percentage": 18.2,
      #   "percentage_start": -36.4,
      #   "percentage_end": -18.2
      # },
      # {
      #   "question": "Question 2",
      #   "type": "Disagree",
      #   "value": 2,
      #   "percentage": 18.2,
      #   "percentage_start": -18.2,
      #   "percentage_end": 0
      # },
      # {
      #   "question": "Question 2",
      #   "type": "Neither agree nor disagree",
      #   "value": 0,
      #   "percentage": 0,
      #   "percentage_start": 0,
      #   "percentage_end": 0
      # },
      # {
      #   "question": "Question 2",
      #   "type": "Agree",
      #   "value": 7,
      #   "percentage": 63.6,
      #   "percentage_start": 0,
      #   "percentage_end": 63.6
      # },
      # {
      #   "question": "Question 2",
      #   "type": "Strongly agree",
      #   "value": 11,
      #   "percentage": 0,
      #   "percentage_start": 63.6,
      #   "percentage_end": 63.6
      # },

      # {
      #   "question": "Question 3",
      #   "type": "Strongly disagree",
      #   "value": 2,
      #   "percentage": 20,
      #   "percentage_start": -30,
      #   "percentage_end": -10
      # },
      # {
      #   "question": "Question 3",
      #   "type": "Disagree",
      #   "value": 0,
      #   "percentage": 0,
      #   "percentage_start": -10,
      #   "percentage_end": -10
      # },
      # {
      #   "question": "Question 3",
      #   "type": "Neither agree nor disagree",
      #   "value": 2,
      #   "percentage": 20,
      #   "percentage_start": -10,
      #   "percentage_end": 10
      # },
      # {
      #   "question": "Question 3",
      #   "type": "Agree",
      #   "value": 4,
      #   "percentage": 40,
      #   "percentage_start": 10,
      #   "percentage_end": 50
      # },
      # {
      #   "question": "Question 3",
      #   "type": "Strongly agree",
      #   "value": 2,
      #   "percentage": 20,
      #   "percentage_start": 50,
      #   "percentage_end": 70
      # },

      # {
      #   "question": "Question 4",
      #   "type": "Strongly disagree",
      #   "value": 0,
      #   "percentage": 0,
      #   "percentage_start": -15.6,
      #   "percentage_end": -15.6
      # },
      # {
      #   "question": "Question 4",
      #   "type": "Disagree",
      #   "value": 2,
      #   "percentage": 12.5,
      #   "percentage_start": -15.6,
      #   "percentage_end": -3.1
      # },
      # {
      #   "question": "Question 4",
      #   "type": "Neither agree nor disagree",
      #   "value": 1,
      #   "percentage": 6.3,
      #   "percentage_start": -3.1,
      #   "percentage_end": 3.1
      # },
      # {
      #   "question": "Question 4",
      #   "type": "Agree",
      #   "value": 7,
      #   "percentage": 43.8,
      #   "percentage_start": 3.1,
      #   "percentage_end": 46.9
      # },
      # {
      #   "question": "Question 4",
      #   "type": "Strongly agree",
      #   "value": 6,
      #   "percentage": 37.5,
      #   "percentage_start": 46.9,
      #   "percentage_end": 84.4
      # },

      # {
      #   "question": "Question 5",
      #   "type": "Strongly disagree",
      #   "value": 0,
      #   "percentage": 0,
      #   "percentage_start": -10.4,
      #   "percentage_end": -10.4
      # },
      # {
      #   "question": "Question 5",
      #   "type": "Disagree",
      #   "value": 1,
      #   "percentage": 4.2,
      #   "percentage_start": -10.4,
      #   "percentage_end": -6.3
      # },
      # {
      #   "question": "Question 5",
      #   "type": "Neither agree nor disagree",
      #   "value": 3,
      #   "percentage": 12.5,
      #   "percentage_start": -6.3,
      #   "percentage_end": 6.3
      # },
      # {
      #   "question": "Question 5",
      #   "type": "Agree",
      #   "value": 16,
      #   "percentage": 66.7,
      #   "percentage_start": 6.3,
      #   "percentage_end": 72.9
      # },
      # {
      #   "question": "Question 5",
      #   "type": "Strongly agree",
      #   "value": 4,
      #   "percentage": 16.7,
      #   "percentage_start": 72.9,
      #   "percentage_end": 89.6
      # },

      # {
      #   "question": "Question 6",
      #   "type": "Strongly disagree",
      #   "value": 1,
      #   "percentage": 6.3,
      #   "percentage_start": -18.8,
      #   "percentage_end": -12.5
      # },
      # {
      #   "question": "Question 6",
      #   "type": "Disagree",
      #   "value": 1,
      #   "percentage": 6.3,
      #   "percentage_start": -12.5,
      #   "percentage_end": -6.3
      # },
      # {
      #   "question": "Question 6",
      #   "type": "Neither agree nor disagree",
      #   "value": 2,
      #   "percentage": 12.5,
      #   "percentage_start": -6.3,
      #   "percentage_end": 6.3
      # },
      # {
      #   "question": "Question 6",
      #   "type": "Agree",
      #   "value": 9,
      #   "percentage": 56.3,
      #   "percentage_start": 6.3,
      #   "percentage_end": 62.5
      # },
      # {
      #   "question": "Question 6",
      #   "type": "Strongly agree",
      #   "value": 3,
      #   "percentage": 18.8,
      #   "percentage_start": 62.5,
      #   "percentage_end": 81.3
      # },

      # {
      #   "question": "Question 7",
      #   "type": "Strongly disagree",
      #   "value": 0,
      #   "percentage": 0,
      #   "percentage_start": -10,
      #   "percentage_end": -10
      # },
      # {
      #   "question": "Question 7",
      #   "type": "Disagree",
      #   "value": 0,
      #   "percentage": 0,
      #   "percentage_start": -10,
      #   "percentage_end": -10
      # },
      # {
      #   "question": "Question 7",
      #   "type": "Neither agree nor disagree",
      #   "value": 1,
      #   "percentage": 20,
      #   "percentage_start": -10,
      #   "percentage_end": 10
      # },
      # {
      #   "question": "Question 7",
      #   "type": "Agree",
      #   "value": 4,
      #   "percentage": 80,
      #   "percentage_start": 10,
      #   "percentage_end": 90
      # },
      # {
      #   "question": "Question 7",
      #   "type": "Strongly agree",
      #   "value": 0,
      #   "percentage": 0,
      #   "percentage_start": 90,
      #   "percentage_end": 90
      # },

      # {
      #   "question": "Question 8",
      #   "type": "Strongly disagree",
      #   "value": 0,
      #   "percentage": 0,
      #   "percentage_start": 0,
      #   "percentage_end": 0
      # },
      # {
      #   "question": "Question 8",
      #   "type": "Disagree",
      #   "value": 0,
      #   "percentage": 0,
      #   "percentage_start": 0,
      #   "percentage_end": 0
      # },
      # {
      #   "question": "Question 8",
      #   "type": "Neither agree nor disagree",
      #   "value": 0,
      #   "percentage": 0,
      #   "percentage_start": 0,
      #   "percentage_end": 0
      # },
      # {
      #   "question": "Question 8",
      #   "type": "Agree",
      #   "value": 0,
      #   "percentage": 0,
      #   "percentage_start": 0,
      #   "percentage_end": 0
      # },
      # {
      #   "question": "Question 8",
      #   "type": "Strongly agree",
      #   "value": 2,
      #   "percentage": 100,
      #   "percentage_start": 0,
      #   "percentage_end": 100
      # }
])

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
    range=["#c30d24", "#f3a583", "#f3c3a3", "#cccccc", "#c3c6f3", "#94c6da", "#1770ab"]
)

y_axis = alt.Axis(
    title='Question',
    offset=5,
    ticks=False,
    minExtent=60,
    domain=False
)

chart = alt.Chart(source).mark_bar().encode(
    x='percentage_start:Q',
    x2='percentage_end:Q',
    y=alt.Y('question:N', axis=y_axis),
    color=alt.Color(
        'type:N',
        legend=alt.Legend(title='Response'),
        scale=color_scale,
    )
)

chart.show()

# save(chart, 'example_chart.png')
