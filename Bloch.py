def BlochCircle(prob):
    y =  -1 + 2*prob
    x = np.sqrt(1-(y**2))

    circle1 = plt.Circle((0, 0), 1.07, color=(22/255, 182/255, 246/255,0.3))
    fig, ax = plt.subplots()
    
    ax.quiver(0,0,x,y, color=(0.8,.2,0.9), scale_units = 'xy',scale=1)
    ax.add_patch(circle1)
    

    plt.plot(np.zeros(10), np.linspace(-1.07, 1.07, 10) , "r--",alpha = 0.7)
    plt.plot(np.linspace(-1.07, 1.07, 10) ,np.zeros(10), "r--",alpha = 0.7)
    
    fig.text(0.5, 0.9, r'| 1 0 >', horizontalalignment='center', verticalalignment='center')
    fig.text(0.5, 0.1, r'| 0 1 >', horizontalalignment='center', verticalalignment='center')
    
    plt.xlim(-1.2,1.2)
    plt.ylim(-1.2,1.2)
    plt.axis('off')

    
    plt.savefig("__pycache__/bloch.jpg")
