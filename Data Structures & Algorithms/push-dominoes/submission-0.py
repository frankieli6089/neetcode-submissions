class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        domin = list(dominoes)
        q = deque()

        for i, d in enumerate(domin):
            if d != ".":
                q.append((i, d))

        while q:
            size = len(q)
            forces = {}

            for _ in range(size):
                i, d = q.popleft()

                if d == "L":
                    if i > 0 and domin[i - 1] == ".":
                        forces.setdefault(i - 1, set()).add("L")

                elif d == "R":
                    if i + 1 < len(domin) and domin[i + 1] == ".":
                        forces.setdefault(i + 1, set()).add("R")

            for i, directions in forces.items():
                if len(directions) == 1:
                    direction = directions.pop()
                    domin[i] = direction
                    q.append((i, direction))

        return ''.join(domin)
