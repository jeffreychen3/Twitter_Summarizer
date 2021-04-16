# NETS213 Final Project - HASHTAG DICTIONARY - a Crowdsourced Hashtag Summarizer 

**Component 1: Selecting top-trending hashtags from Twitter’s trending page that have been active for more than 24 hrs.** *(2 points)*

For this component, we planned to select 10 hashtags from the Twitter trending page. We used newly created twitter accounts, that weren’t following anything, to view the trending page on Twitter, as we did not want accounts we followed to affect what we saw on the trending page. However, it was inevitable that our location affected what we saw on the trending page, which was okay, as we were more inclined to select English hashtags in general, rather than ones with tweets primarily in other languages. Note that Twitter states on their website that, “Trends are determined by an algorithm and, by default, are tailored for you based on who you follow, your interests, and your location.” Thus, it is possible that Twitter has collected data from sources besides just one’s location and what they follow on Twitter; thus, it may be impossible for us to truly see a generic Twitter trending page. We thought about using online data sites to track trending hashtags, but realized that the point of this project is not to select the top trending hashtags, but to simply select trending ones that may be obscure or unfamiliar to people, and thus require some sort of summary. 

We came up with selection criteria when choosing our 10 hashtags. Note that the hashtags are being chosen over a period of about 3 weeks (~3 hashtags per week), in order to create a timeline at the end of our project that displays crowdsourced summaries along with hashtags that were trending at points in our projects. The criteria we came up with was as follows. 1. Select hashtags that have been trending for more than 24 hrs. Once we spot a trending hashtag, we may check tweets in the hashtag to see if it has been very active for more than 24 hrs, or simply look up the news associated with that hashtag (example #Myanmar, related to the military coup in the country) and see how long ago the news came out.  2. Select hashtags with primarily English tweets. 3. Select hashtags that aren’t obvious as to what they are about. For example, #Biden2020 would be a bit too obvious as almost everyone knows what such a hashtag would be about. However, #dogecoin is not as obvious to many people, especially those not involved in cryptocurrency, finance, or part of gen-z. Selecting these types of hashtags makes the summarizing process more interesting, as we want to see varying results based on how much information/context (more/less/no tweets) we provide to workers to write their summaries.

Lastly, note that we aimed to select about 3-5 hashtags for which Twitter had a summary for. As will be seen in later components, one of the metrics we wanted to look at was quality ratings for these Twitter generated summaries (see #HobbyLobby below) versus the summaries generated by crowdsourcing.

<img width="613" alt="Screen Shot 2021-04-13 at 12 58 03 PM" src="https://user-images.githubusercontent.com/56012430/114591484-ed2a6b00-9c57-11eb-843e-359686b53991.png">



**Component 2: Online-bot tweet-to-CSV service: provides a file with ~400 tweets, specifically ones associated to a given hashtag and with a minimum of 100 likes.** *(2 points)*
	
We used the following Twitter bot to extract about 400 tweets from the hashtags that we had selected: https://seobots.io/bots/twitter-hashtag-scraper. This bot was cheap to use, and gave us the option to determine the number of tweets we wanted to scrape for in each hashtag, the language that the tweet needed to be in, and the minimum number of likes that a tweet needed to have. We selected a minimum of 100 likes so as to make sure that the tweets we were getting were representative of what most people interacting with the hashtag were actually interacting with. If we had set this barrier to zero, it is possible that we scraped tweets that were just “noise”—spam, or unrelated to the hashtag itself. This bot runs with a completion time of under two minutes. = It’s worth noting that the csv generated from this bot has columns for the following data: Username, User Handle, Date of Posting, Tweet Text, ReTweet Count, Like Count.

<img width="1369" alt="Screen Shot 2021-04-13 at 12 55 58 PM" src="https://user-images.githubusercontent.com/56012430/114591179-9e7cd100-9c57-11eb-970f-8bb802458d0e.png">

**Component 3: Generation 1 of HITs to generate summaries via crowdsourcing about why a particular hashtag is trending. Three different batches of HITs per hashtag for varying sources of information given to workers (No Tweets/Google News Only, 10 Tweets, 20 Tweets)** *(4 points)*

We will post three different HITs to mTurk. The purpose of such is to have varying amounts of information for the summary,  and to be eventually able to compare the quality of the summary based on how much further research is required from the information given. For one HIT we ask the workers to look up the hashtag on Google News only. To incorporate more information to help workers to explain the trendiness of some hashtag, the workers in other two HITs are given 10 tweets or 20 tweets pulled from the scraped tweets csv and allowed to look up on Google News. 

To create the HITs all in one csv (we have three CSVs, one with no tweets per HIT, one with 10 per HIT, one with 20 per HIT), we will first need to aggregate the tweets of different hashtags from our twitter-scraping bot. One HIT (one line of our CSVs) only contains tweets pertaining to one hashtag, however we do not want workers receiving HITs that pertain to the same hashtag. Thus, we will set a limit on the number of tasks workers can do (about 3-5) to ensure that we minimize the number of workers looking at the same hashtag twice. In addition, we will assign the tweets to HITs such that they are grouped with tweets that have a similar number of likes (so some HITs will have tweets with a lot of likes, while others may not be as many). This is such that we can later identify if there is correlation between popular tweets and the quality of the summary. 
In all HITs, workers will be informed about the hashtag. The result of each HIT will be aggregated into one file, and manipulated with python to create the generation 2 HITS.

**Component 4a: QC: Generation 2 of HITs to use crowdsourcing as quality control, where three workers workers give ratings to each summary, allowing for averaged ratings to be generated** *(4 points)*

We will implement another three separate HITs each containing summaries from No tweet, 10 Tweets and 20 Tweets groups. Each summary will be given to three workers for rating between 1-5 along with the associated hashtags. We will give criteria for each rating in our instruction to avoid some noise due to different people’s standards (see the mockup hits for the criteria). After each HIT being completed, we will average out the score for each summary using python. 

**Component 4b: Generation 3 of HITs using Twitter generated summaries about some of the hashtags (only one per hashtag). Yet again multiple workers will give ratings to each of these summaries and averaged ratings will be generated** *(2 points)*’

We will post one another HIT which asks multiple workers to rate each Twitter -generated tweet summary between 1-5 with the same criteria for 4a. This is to act as a control to see if the crowd gives a more satisfying, thorough summary than Twitter itself. Our group will manually aggregate the Twitter generated summaries into a CSV as preparation. This HIT will result in one CSV and the average ratings for the summaries will again be calculated using python. 

**Component 5: Aggregation Module where various graphs comparing ratings in our 4 different categories (Google News, 10 tweets, 20 tweets, Twitter generated) of summaries will be generated.** *(4 points)*

We will now be left with 4 CSVs. Each CSV will contain averaged ratings for summaries, and each CSV will pertain to one of the following categories: workers given no tweets and solely told to use Google News, workers given 10 tweets, workers given 20 tweets, and Twitter generated summaries. We want to now aggregate these 4 CSVs and use them to present some summarized data. The first set of data we want to present is a line graph of average summary rating vs information given, where we consider the least information -> most information given to workers to be in the following order: Google News, workers given 10 tweets, workers given 20 tweets, and Twitter generated summaries. We also want to present a graphic that shows the highest rated summary for each hashtag, along with which of our 4 categories the summary was in. Lastly, we want to analyze if giving workers more popular tweets in the 10 tweet/20 tweet category actually helped generate better summaries or not. We will thus create a graph of average likes versus summary rating, where average likes is the averaged like count for the tweets given to a worker that generated a given summary (recall that our bot collects data on likes for each tweet). 

**Component 6: Aggregation Module Part 2, where the best summaries are selected from each hashtag based on ratings from workers.** *(1 point)*

The requesters will take the top scoring summary for each hashtag among the three crowdsourced generated categories (no tweets, 10 tweets, 20 tweets), and display the best summary for each of the 10 hashtags; this will show the final results of the crowdworkers work in generating a summary about why a hashtag is trending.

Point Total: 19 points
