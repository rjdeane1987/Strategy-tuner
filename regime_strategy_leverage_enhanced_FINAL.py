import yfinance as yf
import pandas as pd
import numpy as np
import streamlit as st

def load_data(ticker, start, end):
    df = yf.download(ticker, start=start, end=end)
    if isinstance(df.columns, pd.MultiIndex):
        df = df['Close']
    else:
        df = df['Close']
    return df.to_frame(name='price').assign(returns=lambda x: x['price'].pct_change()).dropna()



           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                



           names=['Price', 'Ticker'])
           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                

                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                




           names=['Price', 'Ticker'])
           names=['Price', 'Ticker'])
           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                

                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                

                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                


           names=['Price', 'Ticker'])
                                                                                
    3803       casted_key = self._maybe_cast_indexer(key)                     
                                                                                
                                                                                
                                                                                
                                                                                



                                                                                
                                                                                
                                                                                
     28    df["returns"] = df["price"].pct_change()                            
    31 data = load_data(asset, start_date, end_date)                           
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
     25    df = yf.download(ticker, start=start, end=end)                      
    27    df = df["Adj Close"].to_frame(name="price")                         
     28    df["returns"] = df["price"].pct_change()                            
                                                                                
                                                                                
     4102          indexer = self.columns.get_loc(key)                       
     4104             indexer = [indexer]                                   
                                                                                
                                                                                
    4159       loc = self.columns.get_loc(key)                               
     4161          new_columns = self.columns[loc]                           
     4162          result_columns = maybe_droplevels(new_columns, key)       
                                                                                
                                                                                
   3040          loc = self._get_level_indexer(key, level=0)                
    3043       keylen = len(key)                                              
                                                                                
                                                                                
   3391          idx = self._get_loc_single_level_index(level_index, key)   
    3393          if level > 0 or self._lexsort_depth == 0:                  
                                                                                
                                                                                
                                                                                
                                                                                

