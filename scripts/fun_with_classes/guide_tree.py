

def upgma( graph_list, align_algo ):

    if len( graph_list ) == 1:
        return graph_list[0]

    for g1 in graph_list:
        for g2 in graph_list:
            if g1.id == g2.id:
                continue

            if align_algo == "VF2":
                vf2 = VF2( g1, g2 )
                vf2.match

            if align_algo == "BK":
                
