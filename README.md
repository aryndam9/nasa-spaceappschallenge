<p align="center">
  <img src="https://sa-2019.s3.amazonaws.com/media/images/Space_Apps_Default_Logo_-_2-Color_White.width-352.png" alt="NASA Space Apps Challenge 2022">
</p>
<p align="center">
  <a href="https://2022.spaceappschallenge.org/challenges/2022-challenges/measuring-open-science/teams/the-open-metric/project">Nasa Space apps project page</a>
</p>

# April TOPS Community Forum #

**Date:** Thursday April 13, 2023 1-2 PM ET

[Video Recording](https://www.youtube.com/watch?v=PSeKlCl7YLs)

[Slides](https://zenodo.org/record/7826161#.ZEBHunbMKUk)

[Certificate](https://docs.google.com/viewer?url=https://raw.githubusercontent.com/aryndam9/nasa-spaceappschallenge/03d16d1db67157a57ac11f287be0aa99d1268048/NASA_TOPS_Forum_Participation_Metrics.pdf)


# The Open Metric

With the introduction of Open Science and the increase of scientific research accessibility, the current metrics to measure relevance or success within the research community are rapidly becoming obsolete. These academic metrics aim to represent the dissemination of knowledge among scientists rather than the impact of the research on the wider world. There is, therefore, a lack of metrics to measure the effectiveness and impact of science. 

The Open Metric is a new measurement system that allows scientists to assess the effectiveness of their open science activities, such as journal articles, social media or news appearances, and outreach activities. It also allows independent researchers, especially those from developing countries, to identify the reproducibility of a specific research project and plan for future research. The Open Metric takes different input factors to compute a final value that effectively identifies the openness, engagement, and impact of any journal article, data repository, or scientific outreach activity.

## Input factors and weights

The Open Metric takes the following input factors and weights into account:

- **Credibility (50%)**: Measured using the citation index, which takes into account the number of times this specific content has been cited in scientific articles or scientific media. This value has a weight of 50%, since it is highly effective to measure the impact on new scientific projects and outcomes.
- **Accessibility (25%)**: Considers if it has been published under a pay-per-view format or it is open access and free. This factor has a weight of 25%, which highlights the importance of the parameter when measuring the potentially social impact of scientific work, especially towards developing countries.
- **Societal engagement (25%)**: Divided between social media interaction and online reader behavior, incorporates the social impact of the content. This factor has a weight of 25%, divided into 15% for social media interaction, considering both the post numbers and the reactions, and a 10% for online reader behavior, which is characterized by the time spent by readers on the content.

All these factors play a key role in the social impact and effectiveness of open science activities, and are therefore included in the Open Metric.

## Improvements

There are still a lot of things that could be improved in the Open Metric, such as:

- For the accessibility factor, it will be more holistic to include the proportion of referenced content that is open and free aside from only scoring between paid and free content. This will make it more comprehensive since it will allow independent researchers to check whether resources to reproduce the work are accessible.
- The inclusion of citations in patents for the credibility factor. This will show how a research work is solid enough to encourage technological transfer and scientifically support inventions.
- For societal engagement, it will be ideal to gather data on online reader behavior, such as the time spent by readers on the content.


# Open Metric

Open Metric is a web app developed as part of the [NASA Space Apps Challenge 2022]([https://2021.spaceappschallenge.org/challenges/statements/open-metric/details](https://2022.spaceappschallenge.org/challenges/2022-challenges/measuring-open-science/teams/the-open-metric/project)). It allows users to explore different metrics for evaluating the openness of scientific papers. The app is built using python on flask.

## Features

-  Credibility score: Measures the number of times the content has been cited in scientific articles or media, providing a weight of 50% in the overall score calculation.
- Accessibility score: Determines if the content is available as open access or under a pay-per-view format, providing a weight of 25% in the overall score calculation.
- Societal engagement score: Evaluates the social impact of the content, taking into account social media interaction and online reader behavior, with a total weight of 25% in the overall score calculation.
- Weighted score calculation: Combines the three input factors into a weighted score calculation, providing an overall score between 0 and 100.

<div align="center">
    <img src="https://github.com/aryndam9/nasa-spaceappschallenge/blob/main/v1-old/Screenshot_1.png" alt="Open Metric Web App Screenshot">
</div>

## How to use

To use Open Metric, simply visit the [web app](https://nasa-spaceapps.vercel.app/) and follow these steps:

1. Enter the DOI of the paper you want to score.
2. Click the "Submit" button.
3. The Open Metric score will be displayed.

For more details on the metric, please refer to the "About" section of the web app.


## Contributing

Contributions to the Open Metric project are always welcome! If you have any ideas or suggestions for improving the Open Metric, feel free to open an issue or submit a pull request.
If you want to run the app locally or contribute to its development, follow these steps:

1. Clone this repository to your local machine using Git.
2. Install the required dependencies by running `flask run app.py` in the project directory.
3. This will launch the app in your default browser at Localhost.
4. Make any changes you want and submit a pull request.

## Credits

Open Metric was developed by a team of four participants as part of the NASA International Space Apps Challenge 2021. The team members are:

- [Arindam](https://github.com/aryndam9)
- [Jaume Puig](https://github.com/JaumePuig98)
- [Florence Pauline Basubas]()

## License

The Open Metric is released under the MIT License.
