# -*- coding: utf-8 -*-
"""Delivers 2 QC control.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1r0Xtg71vCrhWxKp_QeAbbU9kAvoCXMFk
"""

#build a new dataframe with similar heads,for each file, for each avg like, save twitters, save sumar

def pullAvg10(input_10):
  #return datafrom type
  out_put = pd.DataFrame(columns=['Hashtag', 'Tweet1','Tweet2','Tweet3','Tweet4'
  ,'Tweet5','Tweet6','Tweet7','Tweet8','Tweet9','Tweet10','Average Likes','Summary','Rating'])
  ct = 0;
  avg = 0;
  for index,row in input_10.iterrows():
    avg = avg + int(row['Rating'])
    ct = ct + 1
    if ct == 3:
      avg = avg / 3;
      x = row.copy()
      x['Rating'] = avg
      to_append = pd.Series(x, index = out_put.columns)
      out_put = out_put.append(to_append)
      out_put.append(x)
      avg = 0
      ct = 0
  out_put.rename(columns={'Rating': 'Average Rating'},inplace=True)
  return out_put

def pullAvg20(input_20):
  #return datafrom type
  out_put = pd.DataFrame(columns=['Hashtag', 'Tweet1','Tweet2','Tweet3','Tweet4'
  ,'Tweet5','Tweet6','Tweet7','Tweet8','Tweet9','Tweet10','Tweet11', 'Tweet12', 
  'Tweet13', 'Tweet14', 'Tweet15', 'Tweet16', 'Tweet17', 'Tweet18', 'Tweet19', 
  'Tweet20','Average Likes','Summary','Rating'])
  ct = 0;
  avg = 0;
  for index,row in input_20.iterrows():
    avg = avg + int(row['Rating'])
    ct = ct + 1
    if ct == 3:
      avg = avg / 3;
      x = row.copy()
      x['Rating'] = avg
      to_append = pd.Series(x, index = out_put.columns)
      out_put = out_put.append(to_append)
      out_put.append(x)
      avg = 0
      ct = 0
  out_put.rename(columns={'Rating': 'Average Rating'},inplace=True)
  return out_put

def pullAvg0(input_0):
  #return datafrom type
  out_put = pd.DataFrame(columns=['Hashtag','Summary','Rating'])
  ct = 0;
  avg = 0;
  for index,row in input_0.iterrows():
    avg = avg + int(row['Rating'])
    ct = ct + 1
    if ct == 3:
      avg = avg / 3;
      x = row.copy()
      x['Rating'] = avg
      to_append = pd.Series(x, index = out_put.columns)
      out_put = out_put.append(to_append)
      out_put.append(x)
      avg = 0
      ct = 0
  out_put.rename(columns={'Rating': 'Average Rating'},inplace=True)
  return out_put

# Your main function
import pandas as pd
def main():
    # Read in CVS result file with pandas
    # PLEASE DO NOT CHANGE
    input_0 = pd.read_csv('0TweetsQCOutput.csv')
    input_10 = pd.read_csv('10TweetsQCOutput.csv')
    input_20 = pd.read_csv('20TweetsQCOutput.csv')

    #Call functions and output required CSV files
    avgR_10 = pullAvg10(input_10)
    avgR_10.to_csv("10TweetsAggregationPrep.csv", index=False)
    
    avgR_0 = pullAvg0(input_0)
    avgR_0.to_csv("0TweetsAggregationPrep.csv", index=False)

    avgR_20 = pullAvg20(input_20)
    avgR_20.to_csv("20TweetsAggregationPrep.csv", index=False)

    #now write a function which generates the highest avg rate for each hashtag
    dic = {}
    for index,row in avgR_20.iterrows():
      if row['Hashtag'] in dic:
        if dic[row['Hashtag']][0] < float(row['Average Rating']):
          dic[row['Hashtag']] = (float(row['Average Rating']),row['Summary'],'20Tweets')
      else:
        dic[row['Hashtag']] = (float(row['Average Rating']),row['Summary'],'20Tweets')
  
    for index,row in avgR_0.iterrows():
      if row['Hashtag'] in dic:
        if dic[row['Hashtag']][0] < float(row['Average Rating']):
          dic[row['Hashtag']] = (float(row['Average Rating']),row['Summary'],'0Tweets')
      else:
        dic[row['Hashtag']] = (float(row['Average Rating']),row['Summary'],'0Tweets')
    
    for index,row in avgR_10.iterrows():
      if row['Hashtag'] in dic:
        if dic[row['Hashtag']][0] < float(row['Average Rating']):
          dic[row['Hashtag']] = (float(row['Average Rating']),row['Summary'],'10Tweets')
      else:
        dic[row['Hashtag']] = (float(row['Average Rating']),row['Summary'],'10Tweets')

    l = []
    for key, value in dic.items():
      l.append((key,value[1],value[2],value[0]))
    print(l)

if __name__ == '__main__':
    main()