# Spark Empirical
This is the repository containing Stack Overflow manual study results for paper "An Empirical Study on the Challenges that Developers Encounter When Developing Apache Spark Applications".
 - `data` contains the a `csv` file that is the manual analysis result for the Stack Overflow posts. In the file, it contains information on the classification of the data, the reasons and the number of views, etc. 
 
 - `scripts` contains the python and sql files that are used for data collection and data analysis.
    - `query_data.sql` is used to collect data from the Stack Exchange website.
    - `sample.py` is used to sample data for manual analysis.
    - `common_issue.py` is used to study the percentage of common issues in rq1. 
    - `popularity.py` is used to calculate the average of normalized view counts in rq2.
    - `popularity_difficulty.py` is used to calculate the average of raw view counts and the median hours to receive an answer in rq2.
    - `root_cuase.py` is used to study the percentage of root causes in rq3. 
