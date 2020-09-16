import pandas as pd
import numpy as np
from numpy import random
from pandas.io.data import DataReader
from datetime import datetime

#tickers
tickers=['ABT', 'ABBV', 'ACN', 'ACE', 'ADBE', 'ADT', 'AAP', 'AES', 'AET', 'AFL', 'AMG', 'A', 'GAS', 'APD', 'ARG', 'AKAM', 'AA', 'AGN', 'ALXN', 'ALLE', 'ADS', 'ALL', 'ALTR', 'MO', 'AMZN', 'AEE', 'AAL', 'AEP', 'AXP', 'AIG', 'AMT', 'AMP', 'ABC', 'AME', 'AMGN', 'APH', 'APC', 'ADI', 'AON', 'APA', 'AIV', 'AMAT', 'ADM', 'AIZ', 'T', 'ADSK', 'ADP', 'AN', 'AZO', 'AVGO', 'AVB', 'AVY', 'BHI', 'BLL', 'BAC', 'BK', 'BCR', 'BXLT', 'BAX', 'BBT', 'BDX', 'BBBY', 'BRK-B', 'BBY', 'BLX', 'HRB', 'BA', 'BWA', 'BXP', 'BSK', 'BMY', 'BRCM', 'BF-B', 'CHRW', 'CA', 'CVC', 'COG', 'CAM', 'CPB', 'COF', 'CAH', 'HSIC', 'KMX', 'CCL', 'CAT', 'CBG', 'CBS', 'CELG', 'CNP', 'CTL', 'CERN', 'CF', 'SCHW', 'CHK', 'CVX', 'CMG', 'CB', 'CI', 'XEC', 'CINF', 'CTAS', 'CSCO', 'C', 'CTXS', 'CLX', 'CME', 'CMS', 'COH', 'KO', 'CCE', 'CTSH', 'CL', 'CMCSA', 'CMA', 'CSC', 'CAG', 'COP', 'CNX', 'ED', 'STZ', 'GLW', 'COST', 'CCI', 'CSX', 'CMI', 'CVS', 'DHI', 'DHR', 'DRI', 'DVA', 'DE', 'DLPH', 'DAL', 'XRAY', 'DVN', 'DO', 'DTV', 'DFS', 'DISCA', 'DISCK', 'DG', 'DLTR', 'D', 'DOV', 'DOW', 'DPS', 'DTE', 'DD', 'DUK', 'DNB', 'ETFC', 'EMN', 'ETN', 'EBAY', 'ECL', 'EIX', 'EW', 'EA', 'EMC', 'EMR', 'ENDP', 'ESV', 'ETR', 'EOG', 'EQT', 'EFX', 'EQIX', 'EQR', 'ESS', 'EL', 'ES', 'EXC', 'EXPE', 'EXPD', 'ESRX', 'XOM', 'FFIV', 'FB', 'FAST', 'FDX', 'FIS', 'FITB', 'FSLR', 'FE', 'FSIV', 'FLIR', 'FLS', 'FLR', 'FMC', 'FTI', 'F', 'FOSL', 'BEN', 'FCX', 'FTR', 'GME', 'GPS', 'GRMN', 'GD', 'GE', 'GGP', 'GIS', 'GM', 'GPC', 'GNW', 'GILD', 'GS', 'GT', 'GOOGL', 'GOOG', 'GWW', 'HAL', 'HBI', 'HOG', 'HAR', 'HRS', 'HIG', 'HAS', 'HCA', 'HCP', 'HCN', 'HP', 'HES', 'HPQ', 'HD', 'HON', 'HRL', 'HSP', 'HST', 'HCBK', 'HUM', 'HBAN', 'ITW', 'IR', 'INTC', 'ICE', 'IBM', 'IP', 'IPG', 'IFF', 'INTU', 'ISRG', 'IVZ', 'IRM', 'JEC', 'JBHT', 'JNJ', 'JCI', 'JOY', 'JPM', 'JNPR', 'KSU', 'K', 'KEY', 'GMCR', 'KMB', 'KIM', 'KMI', 'KLAC', 'KSS', 'KRFT', 'KR', 'LB', 'LLL', 'LH', 'LRCX', 'LM', 'LEG', 'LEN', 'LVLT', 'LUK', 'LLY', 'LNC', 'LLTC', 'LMT', 'L', 'LOW', 'LYB', 'MTB', 'MAC', 'M', 'MNK', 'MRO', 'MPC', 'MAR', 'MMC', 'MLM', 'MAS', 'MA', 'MAT', 'MKC', 'MCD', 'MHFI', 'MCK', 'MJN', 'MMV', 'MDT', 'MRK', 'MET', 'KORS', 'MCHP', 'MU', 'MSFT', 'MHK', 'TAP', 'MDLZ', 'MON', 'MNST', 'MCO', 'MS', 'MOS', 'MSI', 'MUR', 'MYL', 'NDAQ', 'NOV', 'NAVI', 'NTAP', 'NFLX', 'NWL', 'NFX', 'NEM', 'NWSA', 'NEE', 'NLSN', 'NKE', 'NI', 'NE', 'NBL', 'JWN', 'NSC', 'NTRS', 'NOC', 'NRG', 'NUE', 'NVDA', 'ORLY', 'OXY', 'OMC', 'OKE', 'ORCL', 'OI', 'PCAR', 'PLL', 'PH', 'PDCO', 'PAYX', 'PNR', 'PBCT', 'POM', 'PEP', 'PKI', 'PRGO', 'PFE', 'PCG', 'PM', 'PSX', 'PNW', 'PXD', 'PBI', 'PCL', 'PNC', 'RL', 'PPG', 'PPL', 'PX', 'PCP', 'PCLN', 'PFG', 'PG', 'PGR', 'PLD', 'PRU', 'PEG', 'PSA', 'PHM', 'PVH', 'QRVO', 'PWR', 'QCOM', 'DGX', 'RRC', 'RTN', 'O', 'RHT', 'REGN', 'RF', 'RSG', 'RAI', 'RHI', 'ROK', 'COL', 'ROP', 'ROST', 'RLC', 'R', 'CRM', 'SNDK', 'SCG', 'SLB', 'SNI', 'STX', 'SEE', 'SRE', 'SHW', 'SIAL', 'SPG', 'SWKS', 'SLG', 'SJM', 'SNA', 'SO', 'LUV', 'SWN', 'SE', 'STJ', 'SWK', 'SPLS', 'SBUX', 'HOT', 'STT', 'SRCL', 'SYK', 'STI', 'SYMC', 'SYY', 'TROW', 'TGT', 'TEL', 'TE', 'TGNA', 'THC', 'TDC', 'TSO', 'TXN', 'TXT', 'HSY', 'TRV', 'TMO', 'TIF', 'TWX', 'TWC', 'TJK', 'TMK', 'TSS', 'TSCO', 'RIG', 'TRIP', 'FOXA', 'TSN', 'TYC', 'UA', 'UNP', 'UNH', 'UPS', 'URI', 'UTX', 'UHS', 'UNM', 'URBN', 'VFC', 'VLO', 'VAR', 'VTR', 'VRSN', 'VZ', 'VRTX', 'VIAB', 'V', 'VNO', 'VMC', 'WMT', 'WBA', 'DIS', 'WM', 'WAT', 'ANTM', 'WFC', 'WDC', 'WU', 'WY', 'WHR', 'WFM', 'WMB', 'WEC', 'WYN', 'WYNN', 'XEL', 'XRX', 'XLNX', 'XL', 'XYL', 'YHOO', 'YUM', 'ZBH', 'ZION', 'ZTS']

#stock tickers list
s=np.empty(0)
#5 day return for each of the stocks
#v=np.empty(0)
#matrix result of  477 stock (5day return) that are shifted by each day (for 400 rows)
compmatrix=np.zeros((400,477))

#calculate 5 day return for the 477 stocks for 400 times 
#then places it in a matrix with each column being a stock
col=0
for t in tickers:
    try:
        #read 477 stocks, do for about 500 days 2015/4/4-2017/4/9
        tickerresults = DataReader(t, "yahoo", datetime(2015,4,1), datetime(2017,4,14))
        #get adj close
        prices=tickerresults['Adj Close']
        #get prices vector length
        v=np.empty(0)
        fday=len(prices)-4
        #calculate 5 day return shifted by each day (400 rows)
        for b in np.arange(fday):
            #shifts each time tickerresults['adjclose'][4]-tickerresults['adjclose'][0] nexttime adjclose[5]-adjclose[1]...
            growthvalue = (tickerresults['Adj Close'][b+4] - tickerresults['Adj Close'][b+0])
            growthrate = (growthvalue/(tickerresults['Adj Close'][b+0]))*100
            #Append to v array
            v=np.append(v,growthrate)
        #Append to s array
        s=np.append(s,t)
        #add the 5 day return that is shifted each time
        for z in range(0,400):
            compmatrix[z,col]=v[z]
        col=col+1
    except:
        exit=0

#Shape of the matrix containing 477 stocks and 400 5 day returns for each
ro,n=compmatrix.shape
#create the data train matrix
stockmatrix = np.zeros((ro,n))

#stores 5 day returns for apple
av=np.empty(0)

#creats a 5 day return vector for apple (400 rows)
for p in np.arange(ro):
    try:
        #get apple stock data
        tickerresults2 = DataReader("AAPL", "yahoo", datetime(2015,4,1), datetime(2017,4,14))
        #shift each day to get 400 rows of data
        growthvalue2 = (tickerresults2['Adj Close'][p+4] - tickerresults2['Adj Close'][p+0])
        growthrate2 = (growthvalue2/(tickerresults2['Adj Close'][p+0]))*100
        #add each 5 day return
        av=np.append(av,growthrate2)
    except:
        exit2=0

app = len(av)


# Write a logic to compare each of the growthrate and assign -1, 0 or 1, the comparison matrix
for i in range(0,app):
    #fetch the column containing all the 5 days returns for one stock
    stock=compmatrix[i,:]
    for j in range(0,n):
        #row value the 5 day returns for apple (400 items)
        rowval = av[i]
        #col value the 5 days returns for a stock (one of 477)
        colval = stock[j]
        if (rowval > 0):
            if colval > rowval or colval == rowval:
                stockmatrix[i,j] = 1
            elif colval < -rowval or colval == -rowval:
                stockmatrix[i,j] = -1
            else:
                stockmatrix[i,j] = 0
        elif (rowval < 0):
            if colval < rowval or colval == rowval:
                stockmatrix[i,j] = 1
            elif colval > -rowval or colval == -rowval:
                stockmatrix[i,j] = -1
            else:
                stockmatrix[i,j] = 0
                

#Training data output
out=np.empty(0)

#Write training data output matrix based on apple 5 day return
#if >0 append 1 <0 append 0
for ou in av:
    if(ou>0):
        out=np.append(out,1)  
    
    if(ou<0):
        out=np.append(out,0)



#uses the comparison matrix as input
training_set_inputs = stockmatrix
#output results comparing apple 5 day return to see if>0 or if<0
training_set_outputs = out.reshape(400,1)


#randomly makes a input array of 400
nums3 = np.random.choice([0, 1], size=n)
numlist2=nums3
#Sample data to test input (transposed because orginially it was inputted as a row but it is supposed to be 1 column (400 rows X 1 col)
input_req=numlist2.T



#We seed the random number generator so that we get the same number
#of runs every time
np.random.seed(1)

#weights, 477
weights = 2*np.random.random((477,1))-1

y=0
u=0
#Neural network, u is a counter that prevents while loop from executing infinitely
while(y!=400 and u<600):
    predict_outputs = 1/(1+np.exp(-np.dot(training_set_inputs,weights)))
    #error subtracts training output-predicted output
    error = training_set_outputs-predict_outputs
    #takes derivative
    der = predict_outputs * (1-predict_outputs)
    #adjusts the inputs based on error*derivative
    adjust = np.dot(training_set_inputs.T,error*der)
    y=0
    #compares each error value to see if <0.01 (400 times because 400 rows of error) and keeps counts
    for i in error:
        if np.any(y<=0.01):
            #counter
            y=y+1

    weights = weights + adjust
    #counter
    u=u+1

#predicted output
output_req=1/(1+np.exp(-np.dot(input_req,weights)))

print('Predicted value for input')
print(output_req)

print('The Weights')
print(weights)       


#data frame with weights and stocks
df4=pd.DataFrame(weights,s)

#rename column name to weights
df4.columns=['weights']

#top 5 of stocks based on weight`
print('top5')
print(df4['weights'].sort_values(ascending=False).head(5))

#bottom 5 stocks based on weight
print('bottom5')
print(df4['weights'].sort_values(ascending=False).tail(5))
