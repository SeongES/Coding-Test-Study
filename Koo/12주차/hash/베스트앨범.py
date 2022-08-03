def solution(genres, plays):
    answer = []
    g_dict = {}
    p_dict = {}
    
    for i in range(len(genres)) :
        g_dict[genres[i]] = g_dict.get(genres[i], 0) + plays[i]
        p_dict[genres[i]] = p_dict.get(genres[i], []) + [(plays[i], i)]
    
    sorted_total = sorted(g_dict.items(), key = lambda x : x[1], reverse=True)
    
    for g, tp in sorted_total :
        p_dict[g] = sorted(p_dict[g], key = lambda x : (-x[0], x[1]))
        answer += [i for (p, idx) in p_dict[g][:2]]
    return answer
