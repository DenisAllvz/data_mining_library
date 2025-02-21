def setup_plot_style():
    import matplotlib.pyplot as plt
    import seaborn as sns

    # Set the aesthetic style of the plots
    sns.set_style("whitegrid")

    # Set the color palette
    sns.set_palette("colorblind")

    # Set the font size for the plots
    plt.rcParams.update({'font.size': 12})

    # Set the figure size
    plt.figure(figsize=(10, 6))