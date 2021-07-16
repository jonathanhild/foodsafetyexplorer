# FoodSafetyExplorer

Data for food safety hazard analysis

## Summary

Analysis of historical and emerging hazards is critical to the development of an effective food safety system. Multiple regulatory agencies makes it difficult to stay aware of these hazards when sourcing from a global supply chain. A food safety professional can be diligent by checking multiple sources, or paying for a service to aggregate this information. But this approach is either time-consuming or expensive. Further, both approaches do not provide solutions in synthesizing this information for hazard analysis.

Data analytics and machine learning techniques can provide a solution to assist a food safety professional. In this project, I will create a solution that:

1. Collects recall data by API and/or web scraping from multiple sources.
1. Has a data pipeline that can be scaled for the addition of other sources.
1. Classify recalls using ML, NLP and text mining.
1. Utilize machine learning techniques for trending of emerging hazards.
1. Provides a data dashboard app for food safety professionals to explore historical recall information and emerging food safety hazards.

## The Data

![FDA Logo](./img/usfda.png)

[openFDA Recall Enforcement Endpoint](https://open.fda.gov/apis/food/enforcement/)

The FDA provides a convenient API endpoint of recall enforcement events.

![CFIA Logo](./img/cfia.png)

[CFIA Recalls & Safety Alerts API](https://open.canada.ca/data/en/dataset/d38de914-c94c-429b-8ab1-8776c31643e3)

![FSA Logo](./img/ukfsa.png)

[FSA Food Alerts API](https://data.food.gov.uk/food-alerts/ui/reference)

![EFSA Logo](./img/efsa.png)

[EFSA RASFF Portal](https://webgate.ec.europa.eu/rasff-window/portal/)

The RASFF portal does not provide a convenient API endpoint and I had to result to web scraping to collect using the Python BeautifulSoup library. Two stages were needed to collect this data. First, scraping URL links from the search results list. Then crawling the list of links and scraping data details.

## The Dashboard

{desciption pending}

## Recall Classification

{desciption pending}

## Emerging Trends

{description pending}

## Data Backend

I used a factory pattern of builder classes to perform collection and processing of data into a PostgreSQL database.
