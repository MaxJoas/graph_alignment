

def vf2 ( s, s0, ms ):
    if ms_in_g2(ms,g2):
        return ms

    ps = compute_ps()
    for n,m un  in ps :
        if feasibility( s, n, m ):
            s_ = compute_s_()
            vf2(s_,so, ms)
    restore_ds()



''' computung set ps for looping canditates '''
def compute_ps(s, g1, g2, n1, n2, ms1, ms2):
    pred_set1 = pred(g1, n1)
    succ_set1 = succ(g1, n1)
    t_in1 = t_in_out(ms1,pred_set, g1)
    t_out1 - t_in_out(ms1, succ_set, g1)

    pred_set2 = pred(g2, n2)
    succ_set2 = succ(g2, n2)
    t_in2 = t_in_out(ms2,pred_set, g2)
    t_out2 - t_in_out(ms2, succ_set, g2)

    if t_out1 and t_out2:
        # # TODO: # TODO:  ----------------------
        ps = t_out1 x min(t_out2)

    elif (not t_out1 and not t_out2)  and  ( t_in1 and t_in2 ):
        ps = t_in1 x min(t_in2) ## TODO:  ----------------------------

    elif not any(t_in1, t_in2, t_out1, t_out2):
        ps = (n1 - ms1 ) X min(n2 - ms2) # # TODO:  ----------------------

    else :
        state is not part of matching

''' feasbilit function a lo unclear here '''
def feasibility(s, n, m):
    bool = False
    # checks isomporphismus
    if  n.neighbours and m.neighbours inf ms1 ? ms2:
        check = check for corrsebonding branches # # TODO: ---------------------
        if  check:
            # # TODO: check semantic attributes
            if semantic_attributes:
                bool = True
                return bool

    # checks subgraph
    else :
        count how many nodes are in t_in_i, t_out_i ## TODO: ------------------
        and count how many nodes in (n_i - ms_i - t_in_i - t_out_i)
        if count_small_graph <- count_large_graph :
            # # TODO:  check semantic_attributes
            if semantic_attributes:
                bool = True
                return bool
    return bool


# helper functions --------------------------------------------------------

''' helper for finding cancelation criteria of vf2 '''
def ms_in_g2(ms, g2):
    bool = True
    for g in g2:
        if not g in ms:
            bool = False
            return bool

    return bool
''' find predecessors '''
def pred(g, n):
    pred_set = Set()
    ## TODO: FIND pred_set --------------------------------------


    return pred_set

''' find successors '''
def succ(g, n):
        succ_set = Set()
        ## TODO: FIND succ_set------------------------------

        return succ_set


 ''' find T out ot T in set based on the input '''
def t_in_out(ms, pred_succ_set, g1):
    t_out = Set()
    for g in g1:
        if not g in and in pred_succ_set:
            t_in_out.add(g)
    return t_in_out
''' MISSING HELPERS  ---------------------------------''''
core_1
core_2
in_1
out_1
in_2
out_2
