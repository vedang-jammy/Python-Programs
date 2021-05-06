#main file

import scrape
import pandas as pd

total_list, state_list, confirmed_list, recovered_list, death_list = scrape.scrape_now()

state_stats=pd.DataFrame(
     list(zip(state_list,confirmed_list,death_list,recovered_list)),
     columns=['State','Confirmed','Deaths','Recovered']
)

state_stats = state_stats.sort_values(
    by='Confirmed', ascending=False
).reset_index(drop=True)

top_state_stats = state_stats.head(10)

state_list = top_state_stats['State'].values.tolist()
confirmed_list = top_state_stats['Confirmed'].values.tolist()
death_list = top_state_stats['Deaths'].values.tolist()
recovered_list = top_state_stats['Recovered'].values.tolist()

