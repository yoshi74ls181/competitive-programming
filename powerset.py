def powerset(A):
    if not A:
        yield []
    else:
        a = A[0]
        
        for tail in powerset(A[1:]):
            yield tail
            yield [a] + tail

def powerset_c(A):
    if not A:
        yield [], []
    else:
        a = A[0]
        
        for tail, tail_c in powerset_c(A[1:]):
            yield tail, [a] + tail_c
            yield [a] + tail, tail_c
