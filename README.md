# Election Analysis

## Overview of Election Audit 
The Colorado Board of Elections has assigned the task to complete an election audit of a recent local congression election. The following steps conducted to process the analysis:  
1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes. 
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: [election_results.csv](Resources/election_results.csv)
- Software: Python 3.10.3, Visual Studio Code 1.65.2

## Election-Audit Results
The following information has been gathered from conducting the analysis on the congressional election:

- There were 369,711 votes cast in the election.

- The voter turnout for each county was:

    - Jefferson produced 10.5% of voters, for a total of 38,855 voters.
    - Denver produced 82.8% of voters, for a total of 306,055 voters.
    - Arapahoe produced 6.7% of voters, for a total of 24,801 voters.

- The county with the largest voter turnout was:
    - Denver, which produced 82.8% of voters, for a total of 306,055 voters.

- The candidates were:

    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane

- The candidate results were:

    - Charles Casper Stockham received 23.0% of the vote, for a total of 85,213 votes.
    - Diana DeGette received 73.8% of the vote, for a total of 272,892 votes.
    - Raymon Anthony Doane received 3.1% of the vote, for a total of 11,606 votes.

- The winner of the election was:
    - Diana DeGette, who received 73.8% of the vote for a total of 272,892 votes.

Please see below for a snapshot of the congressional election results. The text version of the election results summary can be found [here](Analysis/election_results.txt).

![Election Results Summary](images/Election_results.png)

## Election-Audit Summary

As requested by the Colorado Board of Elections, an analysis was conducted for the congressional election. The analysis initially included only each candidate's voting counts. It was extended to also reflect the result by county. Analysing the data by county was a great addition, seeing as it provided a more detailed insight on the voters. 

The election script used in this analysis can easily be modified to reflect furhter insight. With some modifications, it can also be used to retrieve data for any future elections. The Colorado Board of Elections can greatly benefit from having an election anaylsis script, seeing as it can be reused for future elections and provide desired results. 

As an example, the script can be modified to include not only the separate results by county and candidates, but instead it can be interrelated to show what percentage of each county voted for each candidate. Similarily, with more information regarding the total population of each county, the script can be adjusted to reflect the total amount of voters per county and their participation rate. 

The script can add immense value to the Colorado Board of Elections. It provides essential information which can be used to conduct future election decisions. The script can easily be adjusted to showcase desired results which will aid in conducting election analysis. 

If you are interested in learning more about the benefits of utilizing the script in your election analysis and how it can be used to optimize your results, please feel free to reach out.
