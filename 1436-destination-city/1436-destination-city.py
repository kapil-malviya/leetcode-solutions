class Solution:
    def destCity(self, paths: List[List[str]]) -> str:

        outgoing = set()
        incoming = set()

        # record outgoing and incoming cities
        for path in paths:
            outgoing.add(path[0])
            incoming.add(path[1])

        # find destination city with no outgoing path
        destination_city = incoming.difference(outgoing).pop()

        return destination_city