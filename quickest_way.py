d1, d2, d3 = int(input()), int(input()), int(input())
way1 = d1 + d3 + d2
way2 = (d1 + d2) * 2
way3 = (d2 + d3) * 2
way4 = (d1 + d3) * 2
print(min(way1, way2, way3, way4))
