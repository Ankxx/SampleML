# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 00:30:59 2018

@author: Ankit.Dhadse
"""
"""Bollinger Bands."""

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def symbol_to_path(symbol, base_dir="data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if 'TINPLATE' not in symbols:  # add TINPLATE for reference, if absent
        symbols.insert(0, 'TINPLATE')

    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol), index_col='Date',
                parse_dates=True, usecols=['Date', 'Close Price'], na_values=['nan'])
        df_temp = df_temp.rename(columns={'Close Price': symbol})
        df = df.join(df_temp)
        if symbol == 'TINPLATE':  # drop dates TINPLATE did not trade
            df = df.dropna(subset=["TINPLATE"])

    return df


def plot_data(df, title="Stock prices"):
    """Plot stock prices with a custom title and meaningful axis labels."""
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()
    df.hist(bins=50, label='TinPlate')
    

def compute_daily_returns(df):
    daily_returns = (df/df.shift(1)) - 1
    daily_returns.iloc[0, :] = 0
    return daily_returns


def compute_cumulative_returns(df):
    # (cumret[t] = price[t]/price[0]) - 1
    return df

def test_run():
    # Read data
    dates = pd.date_range('2017-03-01', '2017-10-01')
    symbols = ['TINPLATE', 'LTALLN']
    df = get_data(symbols, dates)
    daily_returns = compute_daily_returns(df)
    plot_data(daily_returns)
    #print(df)
    
    #scatterplot TINPLATE vs LTALLN
    daily_returns.plot(kind='scatter',x='TINPLATE', y='LTALLN')
    beta_LT, alpha_LT = np.polyfit(daily_returns['TINPLATE'], daily_returns['LTALLN'], 1)
    plt.plot(daily_returns['TINPLATE'], beta_LT*daily_returns['TINPLATE'] + alpha_LT, '-', color='r')
    plt.show()
    print(daily_returns.corr(method='pearson'))
    
    
if __name__ == "__main__":
    test_run()
