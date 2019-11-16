import sys
import matplotlib.pyplot as plt
import statistics
def read_out_profile(file):
    res = dict()
    with open(file, 'r') as file:
        for line in file:
            if line.rstrip() == '':
                continue
            splitted = line.rstrip().split('\t')
            try:
                res[int(splitted[0])].append(float(splitted[1]))
            except:
                res[int(splitted[0])] = [float(splitted[1])]
    res2 = {k: statistics.mean(v) for k,v in res.items()}
    helper = sorted(res2.keys())
    res_sorted = dict()
    for i in helper:
        res_sorted[i] = res2[i]
    print(res_sorted)
    return res_sorted

if __name__ == '__main__':

    file = sys.argv[1]
    file_vf2 = sys.argv[2]
    title = sys.argv[3]
    result = read_out_profile(file)
    result_vf2 = read_out_profile(file_vf2)
    plt.plot(list(result.keys()), list(result.values()), label='BK')
    plt.plot(list(result.keys()), list(result_vf2.values()),label='VF2')
    plt.xlabel('#Nodes')
    plt.ylabel('Time / s')
    plt.title(title)
    plt.legend()#bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    plt.show()
