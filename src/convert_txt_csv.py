# importing panda library
import pandas as pd
  
# readinag given csv file
# and creating dataframe
dataframe1 = pd.read_csv("data/row/AmesHousing.txt")
  
# storing this dataframe in a csv file
dataframe1.to_csv('data/row/AmesHousing.csv', 
                  index = None)