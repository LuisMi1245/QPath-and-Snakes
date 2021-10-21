from PIL import Image

def plot_qc(quantum_circuit):
    from qiskit import Aer, execute
    import numpy as np
    import matplotlib.pyplot as plt    
    bk = Aer.get_backend('qasm_simulator') #backend
    job = execute(quantum_circuit, bk, shots=10000) 
    result = job.result()
    count = result.get_counts(quantum_circuit)
    label = list(count.keys()) #x axis
    values = list(count.values())
    percentage = [round(i/sum(values),2) for i in values] #y axis
    x = np.arange(len(label))  # the label locations x
    width = 0.35  # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(x, percentage, width)
    #ax.set_ylabel('Probabilities')
    ax.set_xticks(x)
    ax.set_xticklabels(label, fontsize=30)
    ax.bar_label(rects1, padding=15, fontsize=30)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.get_yaxis().set_ticks([])
    #plt.title('Probabilities', fontsize=30)
    fig.tight_layout()
    plt.savefig("__stored_img__/plot_qcc.png")

img = Image.open('__stored_img__/plot_qcc.png')
new_img = img.resize((200,200))
new_img.save('__stored_img__/plot_qcc.png','png')