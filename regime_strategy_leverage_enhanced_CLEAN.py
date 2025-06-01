import yfinance as yf
import pandas as pd
import numpy as np

def load_data(ticker, start, end):
    df = yf.download(ticker, start=start, end=end)
    if isinstance(df.columns, pd.MultiIndex):
        df = df['Close']  # Select the 'Close' column across tickers
    else:
        df = df['Close']
    return df.to_frame(name='price').assign(returns=lambda x: x['price'].pct_change()).dropna()

  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 06:56:05.143 503 GET /script-health-check (127.0.0.1) 1919.31ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 06:56:10.097 503 GET /script-health-check (127.0.0.1) 1858.36ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 06:56:14.821 503 GET /script-health-check (127.0.0.1) 1601.80ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 06:56:20.364 503 GET /script-health-check (127.0.0.1) 2053.22ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 06:56:25.289 503 GET /script-health-check (127.0.0.1) 2011.91ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 06:56:30.224 503 GET /script-health-check (127.0.0.1) 1908.06ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 06:56:35.132 503 GET /script-health-check (127.0.0.1) 1899.50ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 06:56:40.134 503 GET /script-health-check (127.0.0.1) 1876.02ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 06:56:45.106 503 GET /script-health-check (127.0.0.1) 1834.25ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 06:56:49.984 503 GET /script-health-check (127.0.0.1) 1760.67ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 06:56:55.188 503 GET /script-health-check (127.0.0.1) 1925.36ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 06:57:00.325 503 GET /script-health-check (127.0.0.1) 2031.04ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 06:57:05.167 503 GET /script-health-check (127.0.0.1) 1886.44ms

[*********************100%***********************]  1 of 1 completed[2025-06-01 06:57:08.366855] 
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 06:57:10.234 503 GET /script-health-check (127.0.0.1) 1917.71ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 06:57:15.176 503 GET /script-health-check (127.0.0.1) 1953.14ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 06:57:20.314 503 GET /script-health-check (127.0.0.1) 2084.22ms

[*********************100%***********************]  1 of 1 completed[2025-06-01 06:57:23.263896] 
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 06:57:25.174 503 GET /script-health-check (127.0.0.1) 1957.60ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 06:57:30.315 503 GET /script-health-check (127.0.0.1) 2066.91ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 06:57:35.066 503 GET /script-health-check (127.0.0.1) 1849.24ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 06:57:40.162 503 GET /script-health-check (127.0.0.1) 1920.99ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 06:57:45.056 503 GET /script-health-check (127.0.0.1) 1835.06ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 06:57:50.123 503 GET /script-health-check (127.0.0.1) 1896.80ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 06:57:55.300 503 GET /script-health-check (127.0.0.1) 2051.05ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 06:57:59.844 503 GET /script-health-check (127.0.0.1) 1625.93ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 06:58:05.434 503 GET /script-health-check (127.0.0.1) 2193.10ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 06:58:10.242 503 GET /script-health-check (127.0.0.1) 1919.01ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 06:58:15.311 503 GET /script-health-check (127.0.0.1) 2070.63ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 06:58:20.020 503 GET /script-health-check (127.0.0.1) 1792.15ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 06:58:25.061 503 GET /script-health-check (127.0.0.1) 1829.61ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 06:58:30.111 503 GET /script-health-check (127.0.0.1) 1875.20ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 06:58:35.269 503 GET /script-health-check (127.0.0.1) 2046.19ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 06:58:40.067 503 GET /script-health-check (127.0.0.1) 1823.91ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 06:58:45.037 503 GET /script-health-check (127.0.0.1) 1802.32ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 06:58:50.200 503 GET /script-health-check (127.0.0.1) 1938.46ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 06:58:55.068 503 GET /script-health-check (127.0.0.1) 1846.93ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 06:59:00.464 503 GET /script-health-check (127.0.0.1) 2191.36ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 06:59:05.250 503 GET /script-health-check (127.0.0.1) 2011.78ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 06:59:10.399 503 GET /script-health-check (127.0.0.1) 2156.40ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 06:59:15.466 503 GET /script-health-check (127.0.0.1) 2127.33ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 06:59:20.450 503 GET /script-health-check (127.0.0.1) 2160.27ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 06:59:25.384 503 GET /script-health-check (127.0.0.1) 2123.40ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 06:59:30.183 503 GET /script-health-check (127.0.0.1) 1850.98ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 06:59:35.170 503 GET /script-health-check (127.0.0.1) 1923.21ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 06:59:40.345 503 GET /script-health-check (127.0.0.1) 2034.73ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 06:59:45.044 503 GET /script-health-check (127.0.0.1) 1775.94ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 06:59:50.219 503 GET /script-health-check (127.0.0.1) 1990.09ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 06:59:54.968 503 GET /script-health-check (127.0.0.1) 1734.66ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 07:00:00.259 503 GET /script-health-check (127.0.0.1) 2027.03ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 07:00:05.152 503 GET /script-health-check (127.0.0.1) 1892.43ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 07:00:10.088 503 GET /script-health-check (127.0.0.1) 1866.09ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 07:00:15.482 503 GET /script-health-check (127.0.0.1) 2196.50ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 07:00:20.272 503 GET /script-health-check (127.0.0.1) 2047.25ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 07:00:24.916 503 GET /script-health-check (127.0.0.1) 1686.63ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 07:00:30.303 503 GET /script-health-check (127.0.0.1) 2077.22ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 07:00:34.983 503 GET /script-health-check (127.0.0.1) 1797.41ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 07:00:40.235 503 GET /script-health-check (127.0.0.1) 1935.77ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 07:00:45.168 503 GET /script-health-check (127.0.0.1) 1934.98ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 07:00:50.041 503 GET /script-health-check (127.0.0.1) 1819.06ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 07:00:55.250 503 GET /script-health-check (127.0.0.1) 2019.73ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 07:01:00.093 503 GET /script-health-check (127.0.0.1) 1856.52ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 07:01:05.311 503 GET /script-health-check (127.0.0.1) 2085.09ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 07:01:10.304 503 GET /script-health-check (127.0.0.1) 2011.77ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 07:01:15.161 503 GET /script-health-check (127.0.0.1) 1931.44ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 07:01:20.919 503 GET /script-health-check (127.0.0.1) 2554.90ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 07:01:25.012 503 GET /script-health-check (127.0.0.1) 1771.65ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 07:01:29.901 503 GET /script-health-check (127.0.0.1) 1665.09ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 07:01:35.249 503 GET /script-health-check (127.0.0.1) 2019.72ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 07:01:39.908 503 GET /script-health-check (127.0.0.1) 1688.47ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 07:01:45.515 503 GET /script-health-check (127.0.0.1) 2185.12ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 07:01:50.168 503 GET /script-health-check (127.0.0.1) 1930.54ms

[*********************100%***********************]  1 of 1 completed[2025-06-01 07:01:53.267768] 
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 07:01:55.226 503 GET /script-health-check (127.0.0.1) 2001.38ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 07:02:00.342 503 GET /script-health-check (127.0.0.1) 2107.19ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 07:02:05.174 503 GET /script-health-check (127.0.0.1) 1952.55ms

[*********************100%***********************]  1 of 1 completed

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 07:02:12.599 503 GET /script-health-check (127.0.0.1) 4337.53ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 07:02:14.966 503 GET /script-health-check (127.0.0.1) 1770.98ms

[*********************100%***********************]  1 of 1 completed

[*********************100%***********************]  1 of 1 completed[2025-06-01 07:02:18.809749] 

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 07:02:24.375 503 GET /script-health-check (127.0.0.1) 6066.66ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 07:02:26.483 503 GET /script-health-check (127.0.0.1) 1700.41ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 07:02:30.119 503 GET /script-health-check (127.0.0.1) 1916.99ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 07:02:35.092 503 GET /script-health-check (127.0.0.1) 1855.82ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 07:02:40.089 503 GET /script-health-check (127.0.0.1) 1859.82ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 07:02:45.223 503 GET /script-health-check (127.0.0.1) 1995.02ms

[*********************100%***********************]  1 of 1 completed
DataFrame columns: MultiIndex([( 'Close', 'BTC-USD'),
            (  'High', 'BTC-USD'),
            (   'Low', 'BTC-USD'),
            (  'Open', 'BTC-USD'),
            ('Volume', 'BTC-USD')],
           names=['Price', 'Ticker'])
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3805 in get_loc                                                             
                                                                                
    3802 │   │   """                                                            
    3803 │   │   casted_key = self._maybe_cast_indexer(key)                     
    3804 │   │   try:                                                           
  ❱ 3805 │   │   │   return self._engine.get_loc(casted_key)                    
    3807 │   │   │   if isinstance(casted_key, slice) or (                      
    3808 │   │   │   │   isinstance(casted_key, abc.Iterable)                   
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:167                                 
                                                                                
  in pandas._libs.index.IndexEngine.get_loc:196                                 
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7081                     
                                                                                
  in pandas._libs.hashtable.PyObjectHashTable.get_item:7089                     
────────────────────────────────────────────────────────────────────────────────

The above exception was the direct cause of the following exception:

  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/exec_code.py:121 in exec_func_with_error_handling                        
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/scriptru  
  nner/script_runner.py:645 in code_to_exec                                     
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:31 in          
  <module>                                                                      
                                                                                
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
  ❱  31 data = load_data(asset, start_date, end_date)                           
     32                                                                         
     33 # Simulate regime logic (placeholder logic)                             
     34 np.random.seed(42)                                                      
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:219 in __call__                                                
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:261 in _get_or_create_cached_value                             
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/streamlit/runtime/caching/  
  cache_utils.py:320 in _handle_cache_miss                                      
                                                                                
  /mount/src/strategy-tuner/regime_strategy_leverage_enhanced.py:27 in          
  load_data                                                                     
                                                                                
     24 def load_data(ticker, start, end):                                      
     25 │   df = yf.download(ticker, start=start, end=end)                      
     26 │   print("DataFrame columns:", df.columns)                             
  ❱  27 │   df = df["Adj Close"].to_frame(name="price")                         
     28 │   df["returns"] = df["price"].pct_change()                            
     29 │   return df.dropna()                                                  
     30                                                                         
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4101   
  in __getitem__                                                                
                                                                                
     4098 │   │                                                                 
     4099 │   │   if is_single_key:                                             
     4100 │   │   │   if self.columns.nlevels > 1:                              
  ❱  4101 │   │   │   │   return self._getitem_multilevel(key)                  
     4102 │   │   │   indexer = self.columns.get_loc(key)                       
     4103 │   │   │   if is_integer(indexer):                                   
     4104 │   │   │   │   indexer = [indexer]                                   
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/frame.py:4159   
  in _getitem_multilevel                                                        
                                                                                
     4156 │                                                                     
     4157 │   def _getitem_multilevel(self, key):                               
     4158 │   │   # self.columns is a MultiIndex                                
  ❱  4159 │   │   loc = self.columns.get_loc(key)                               
     4160 │   │   if isinstance(loc, (slice, np.ndarray)):                      
     4161 │   │   │   new_columns = self.columns[loc]                           
     4162 │   │   │   result_columns = maybe_droplevels(new_columns, key)       
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3040 in get_loc                                                            
                                                                                
    3037 │   │   │   return mask                                                
    3038 │   │                                                                  
    3039 │   │   if not isinstance(key, tuple):                                 
  ❱ 3040 │   │   │   loc = self._get_level_indexer(key, level=0)                
    3041 │   │   │   return _maybe_to_slice(loc)                                
    3042 │   │                                                                  
    3043 │   │   keylen = len(key)                                              
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:3391 in _get_level_indexer                                                 
                                                                                
    3388 │   │   │   │   return slice(i, j, step)                               
    3389 │   │                                                                  
    3390 │   │   else:                                                          
  ❱ 3391 │   │   │   idx = self._get_loc_single_level_index(level_index, key)   
    3392 │   │   │                                                              
    3393 │   │   │   if level > 0 or self._lexsort_depth == 0:                  
    3394 │   │   │   │   # Desired level is not sorted                          
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/multi.  
  py:2980 in _get_loc_single_level_index                                        
                                                                                
    2977 │   │   │   # TODO: need is_valid_na_for_dtype(key, level_index.dtype  
    2978 │   │   │   return -1                                                  
    2979 │   │   else:                                                          
  ❱ 2980 │   │   │   return level_index.get_loc(key)                            
    2981 │                                                                      
    2982 │   def get_loc(self, key):                                            
    2983 │   │   """                                                            
                                                                                
  /home/adminuser/venv/lib/python3.13/site-packages/pandas/core/indexes/base.p  
  y:3812 in get_loc                                                             
                                                                                
    3809 │   │   │   │   and any(isinstance(x, slice) for x in casted_key)      
    3810 │   │   │   ):                                                         
    3811 │   │   │   │   raise InvalidIndexError(key)                           
    3813 │   │   except TypeError:                                              
    3814 │   │   │   # If we have a listlike key, _check_indexing_error will r  
    3815 │   │   │   #  InvalidIndexError. Otherwise we fall through and re-ra  
────────────────────────────────────────────────────────────────────────────────
2025-06-01 07:02:50.001 503 GET /script-health-check (127.0.0.1) 1776.00ms

[*********************100%***********************]  1 of 1 completed