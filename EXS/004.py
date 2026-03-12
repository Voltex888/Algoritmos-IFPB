real = int(input())
euro = real / 5
euro100 = euro//100
euro =euro%100
euro50 = euro //50
euro = euro%50
euro5 = euro//5
euro = euro%5
euro2 = euro//2
euro = euro%2
euro = euro//1
print(f"{euro100} $100,00")
print(f"{euro50} $50,00")
print(f"{euro5} $5,00")
print(f"{euro2} $100,00")