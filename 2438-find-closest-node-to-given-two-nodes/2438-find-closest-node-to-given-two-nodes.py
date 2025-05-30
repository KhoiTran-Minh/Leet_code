class Solution(object):
    def closestMeetingNode(self, edges, node1, node2):
        def get_distances(start):
            dist = {}
            current = start
            d = 0
            while current != -1 and current not in dist:
                dist[current] = d
                current = edges[current]
                d += 1
            return dist

        dist1 = get_distances(node1)
        dist2 = get_distances(node2)

        result = -1
        min_dist = float('inf')

        for node in range(len(edges)):
            if node in dist1 and node in dist2:
                max_d = max(dist1[node], dist2[node])
                if max_d < min_dist or (max_d == min_dist and node < result):
                    min_dist = max_d
                    result = node

        return result
        