def isValidSubsequence(array, sequence):
    seqIdx = 0

    for num in array:
        if seqIdx == len(sequence):
            break
        if num == sequence[seqIdx]:
            seqIdx += 1
            
    return seqIdx == len(sequence)

# O(n) time | O(1) space