# election-analysis

## Project Overview
The purpose of this project is to perform an election audit on a Colorado State congressional election to ensure accuracy and see the distribution of votes among counties and candidates. We'll do this by:

1. Calculating the total number of votes cast.
2. Getting a complete list of all candidates who received votes
3. Calculating the total number of votes each candidate received.
4. Calculating the percentage of the vote each candidate received.
5. Determining the winner based off the above 2 data points. 

## Resources and Tools
- Data Source -  election_results.csv
- Software - Python 3.9.7, Visual Studio Code 1.60.1

## Summary 
The analysis of the election data shows that there were 369,711 votes cast. 

 - The counties focused on for this analysis, and the number of votes that were cast in them are listed below.
  - Denver County saw 82.8% of the vote and 305,055 votes. 
  - Jefferson County saw 10.5% of the vote and 38,855 votes.
  - Arapahoe County saw 6.7% of the vote and 24,801 votes.
 - Denver County saw the vast majority of the votes at 82.8%,

- The candidates were
  - Diana DeGette - received 73.8% of the vote and 272,892 votes. 
  - Charles Casper Stockham - received 23.0% of the vote and 85,213 votes. 
  - Raymon Anthony Doane - received 3.1% of the vote and 11,606 votes.
  
 - The winner of the election was Diana DeGette who received 73.8% of the vote and 272,892 votes. 
 
 # Election Audit Summary
 
 It seems the key takeaway here is that any prospective candidate should only run with their first and last names on the ballot, as middle names seemed to have a significant negative impact on electability.
 
 This script can easily be scaled to the rest of the 64 counties of Colorado to provide a broader analysis on the popularity of candidates among voters. With some small modifications, we can use this script to see a breakdown of votes within each county by candidate. This can be used to determine the viability of middle names within each individual county. 

With some small changes we can also use this to display the first and second runners up in an election that features more candidates. 
