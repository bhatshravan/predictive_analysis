def plot_page_mpld3(df, columns, request):
    if request.method == 'POST':  # Something is being submitted
        x1 = str(request.form['x1'])
        x2 = str(request.form['x2'])
        y1 = str(request.form['y1'])
        y2 = str(request.form['y2'])
        z = str(request.form['z'])
        if (x1 not in columns) or (x2 not in columns):
            return redirect(url_for('mpld3_plot'))
        elif (y1 not in columns) or (y2 not in columns):
            return redirect(url_for('mpld3_plot'))
        elif (z not in columns):
            return redirect(url_for('mpld3_plot'))
    else:
        x1, x2, y1, y2, z = 'teff', 'vt', 'Vabs', 'feh', 'logg'
    # Does not work with NaN values!
    df = df.loc[:, list(set([x1, x2, y1, y2, z]))].dropna(axis=0)
    fig, ax = plt.subplots(2, 2, figsize=(14, 8), sharex='col', sharey='row')
    points = ax[0, 0].scatter(df[x1], df[y1], c=df[z], alpha=0.6)
    points = ax[1, 0].scatter(df[x1], df[y2], c=df[z], alpha=0.6)
    points = ax[0, 1].scatter(df[x2], df[y1], c=df[z], alpha=0.6)
    points = ax[1, 1].scatter(df[x2], df[y2], c=df[z], alpha=0.6)
    ax[1, 0].set_xlabel(x1)
    ax[1, 1].set_xlabel(x2)
    ax[0, 0].set_ylabel(y1)
    ax[1, 0].set_ylabel(y2)

    plugins.connect(fig, plugins.LinkedBrush(points))
    plot = fig_to_html(fig)
    return render_template('plot_mpld3.html', plot=plot, columns=columns,
                           x1=x1, x2=x2, y1=y1, y2=y2, z=z) 