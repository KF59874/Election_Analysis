# Election Analysis

## Overview of Election Audit 
The Colorado Board of Elections has assigned the task to complete an election audit of a recent local congression election. The following steps were included to process the analysis:  
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

As requested by the Colorado Board of Elections, an analysis was concluded for the congressional election. 

The analysis was extended to give a more detailed insight on which county had a higher vote turnout. It also included each candidates separate voting counts. 

Analysing the data by county and by candidate was a great addition, seeing as it provided a more detailed insight on the voters. The election script can furhtermore  easily be modified, so that it can be used to retrieve important data for any future election. 

The Colorado Board of Elections can greatly benefit from having a simple script which can be reused for future elections, as with a few simple modifications, it can reflect the desired results which can then be used to run successful future elections. 

The script can be modified to include not only the separate results by county and candidates, but also be interrelated to show what percentage of each county voted for each candidate. This, as an example, can aid in investing time in running campaigns in counties that have a higher turnout per candidate. 

Additionally, with more information regarding the total population of each county, the script can be modified to reflect the total amount of voters per county and their participation rate. Campaigns can be run to inform more voters of when elections are occuring, to increase the population of each county's participation rate and so the number of votes cast. 

The script can add immense value to the Colorado Board of Elections. It provides essential information which can be used to conduct analysis. The results can easily be achieved by modifying the script in a few steps to showcase desired results. 

Please feel free to reach out if you would like to discuss how the election analysis script can be used to optimize the results in future elections. 
