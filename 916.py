class Solution(object):
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        if not B or len(B) == 0:
            return A
        lookup = collections.Counter(B[0])
        for word in B[1:]:
            tmp = collections.Counter(word)
            for key in tmp.keys():
                if key not in lookup:
                    lookup[key] = tmp[key]
                else:
                    lookup[key] = max(lookup[key], tmp[key])
        def uni(tmp_a, tmp_b):
            if len(tmp_a.keys()) < len(tmp_b.keys()):
                return False
            for key in tmp_b.keys():
                if key not in tmp_a:
                    return False
                else:
                    if tmp_a[key] < tmp_b[key]:
                        return False
            return True
        res = []
        for word in A:
            if uni(collections.Counter(word), lookup):
                res.append(word)
        return res