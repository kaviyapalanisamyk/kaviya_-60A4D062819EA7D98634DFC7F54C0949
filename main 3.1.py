def linearSearchProduct(ProductList, targetProduct):
  indices = []
  for index,Product in enumerate(ProductList):
    if Product == targetProduct:
      indices . append (index)
  return indices
#Examble usage:
Product = ["shoes","boot","loafer","shoes","sandal","shoes"]
target = "shoes"
result = linearSearchProduct (Product,target)
print(result)