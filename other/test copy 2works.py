import streamlit as st
from simple_salesforce import Salesforce
import json
from tavily import TavilyClient
import requests
import pandas as pd


class DraftKings2():
    def __init__(self):
        self.regionlower = "il"
        self.regionupper = "IL"
        self.sportid = "3"
        self.eventgroupid = "42133"
        self.headers = {'Accept': 'application/json','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36','Accept-Language': 'en-US,en;q=0.9','Accept-Encoding': 'gzip, deflate, br'}
        self.get_urls()
        self.set_initial_cache()
    
    def get_urls(self):
        self.odds_url = st.secrets.urlconfig.url_odds.format(regionlower=self.regionlower, regionupper=self.regionupper, eventgroupid=self.eventgroupid)
        self.events_url = st.secrets.urlconfig.url_events.format(regionupper=self.regionupper, sportid=self.sportid)
        self.standings_url = st.secrets.urlconfig.url_standings.format(regionupper=self.regionupper, sportid=self.sportid)
        self.seasons_url = st.secrets.urlconfig.url_seasons.format(regionupper=self.regionupper, sportid=self.sportid)

    def set_initial_cache(self):
        self.odds_data_retrieved = False
        self.events_data_retrieved = False
        self.standings_data_retrieved = False
        self.seasons_data_retrieved = False


    def get_data(self, odds: bool=False, events: bool=False, standings: bool=False, seasons: bool=False):
        if odds and not self.odds_data_retrieved:
            self.get_odds_data()
            self.odds_data_retrieved = True
        
        if events and not self.events_data_retrieved:
            self.get_events_data()
            self.events_data_retrieved = True

        if standings and not self.standings_data_retrieved:
            self.get_standings_data()
            self.standings_data_retrieved=True

        if seasons and not self.seasons_data_retrieved:
            self.get_seasons_data()
            self.seasons_data_retrieved=True

    def get_odds_data(self):
        self.odds_data_response = requests.get(url=self.odds_url, headers=self.headers)
        self.odds_data_json = self.odds_data_response.json()
        self.odds_offer_categories = self.odds_data_json.get('offerCategories', [])
    
    def get_events_data(self):
        self.events_data_response = requests.get(url=self.events_url, headers=self.headers)
        self.events_data_json = self.events_data_response.json()
    
    def get_standings_data(self):
        self.standings_data_response = requests.get(url=self.standings_url, headers=self.headers)
        self.standings_data_json = self.standings_data_response.json()
    
    def get_seasons_data(self):
        self.seasons_data_response = requests.get(url=self.seasons_url, headers=self.headers)
        self.seasons_data_json = self.seasons_data_response.json()

    def search_odds_data(self, search_terms):
        self.odds_search_terms = search_terms
        self.odds_search_results = []
        for category in self.odds_data_json['eventGroup']['offerCategories']:
            if category['name'] == "Futures":
                for descriptor in category['offerSubcategoryDescriptors']:
                    if descriptor.get('offerSubcategory'):
                        for offers in descriptor['offerSubcategory']['offers']:
                            for offer in offers:
                                for outcome in offer['outcomes']:
                                    if outcome['participant'] in search_terms:
                                        self.odds_search_results.append({
                                            'participant': outcome['participant'],
                                            'oddsAmerican': outcome['oddsAmerican'],
                                            'oddsDecimal': outcome['oddsDecimal']
                                        })







dkdata2 = DraftKings2()
dkdata2.get_data(odds=True, events=True)
# Example usage with the odds data
odds_data = dkdata2.odds_data_json
df_odds = pd.json_normalize(odds_data['eventGroup'])
print(df_odds)