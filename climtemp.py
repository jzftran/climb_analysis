#group lead table by user_id, and grade, nth selects first ascent 
lead_analysis = lead.groupby(['user_id', 'grade'] )
lead_analysis = lead_analysis.nth(0, dropna=None).reset_index() # reset_index removes multiindex made by groupby
lead_pivot= lead_analysis.pivot_table(index = 'user_id', columns = ['grade'], values ='date')

%%time
#notnull returns dataframe with True/False information applymap with lambda function converts it to 0 and 1
sns.heatmap(lead_pivot.notnull().applymap(lambda x: int(x)), cbar=False, cmap='BuGn')

%%time
sns.heatmap(np.where( lead_pivot.notnull() == False, 0, 1 ), cbar=False, cmap='BuGn')


print("Green shows available data, blue missing data")
print(f"Number of all sends: {lead_pivot.notnull().sum().sum()}")
print(f"Number of climbers: {len(lead_pivot)}")


# calculate how much time spet at each grade with diff function, diff subtracts each column from previous

time_spent = lead_pivot.head().diff(axis = 1 ) # for some reason it may give negative result, why?
#time_spent = time_spent.applymap(lambda x: np.nan if x <0 else x ) # replaces negative values with NaN


time_spent= time_spent.where(time_spent <0 , np.nan) # replace negative values with NaN and convert remaining to months
time_spent= time_spent.where(time_spent !=np.nan , time_spent/3600*24*30) # replace negative values with NaN and convert remaining to months


