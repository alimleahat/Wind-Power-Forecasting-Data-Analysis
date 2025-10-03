import matplotlib.pyplot as plt

def plot(airlines, fuel, ticket, rows, cols, origin):
    # create the plot with two different y-axes
    fig, ax1 = plt.subplots(figsize=(10,5))
    ax2 = ax1.twinx()
    
    # get the names and values we need to plot
    names = []
    ticket_values = []
    fuel_values = []
    
    # loop to get all the data we need
    for i in range(len(rows)):
        names.append(airlines[rows[i]][0])
        ticket_values.append(ticket[rows[i]][cols[i]]) 
        fuel_values.append(fuel[rows[i]][cols[i]])
    
    # x positions
    x = range(len(names))
    
    # plot ticket bars slightly to the left
    ax1.bar([i-0.2 for i in x], ticket_values, width=0.4, label='Ticket')
    
    # plot fuel bars slightly to the right
    ax2.bar([i+0.2 for i in x], fuel_values, width=0.4, label='Fuel', color='orange')
    
    # x-axis labels and rotate them by 90 degrees
    ax1.set_xticks(x)
    ax1.set_xticklabels(names, rotation=90, ha='center')
    
    # add labels
    ax1.set_ylabel('Total Ticket Price')
    ax2.set_ylabel('Total Fuel Consumption')
    plt.title(f"Total Ticket Price and Fuel Consumption for Airport: {origin}")
    
    # add a legend
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')
    
    plt.tight_layout() 
    plt.show()
     