import csv

########################################################################
class StockItem:
  def __init__(self, GTIN8_in, ProductDescription_in, UnitPrice_in):
	  self.GTIN8 = GTIN8_in
	  self.ProductDescription = ProductDescription_in
	  self.UnitPrice = UnitPrice_in
	  
  def displayAll(self):
    print self.GTIN8, self.ProductDescription, self.UnitPrice
########################################################################
class StockList:
	MyItems = []
	MyCount = 0
		
	def __init__(self):
		MyCount = 0
		

	def AddItem(self, StockItem):
		self.MyItems.append(StockItem)
		
		
	def GetItem(self, position):
		return self.MyItems[position]
		
			
	def FindGTIN8(self, GTIN8_in): 
		found= -1
		position=0
		#resultItem = StockItem()
		
		#print "Count=" , len(self.MyItems)
		#print "Looking for GTIN8", GTIN8_in
		
		while found==-1 and position < len(self.MyItems):
			#print "Testing:",self.MyItems[position].GTIN8,GTIN8_in
			if self.MyItems[position].GTIN8==GTIN8_in:
				found=position
			#print position
			position = position + 1
		### we need to figure out how to pass back the StockItem that was found!!!			
		return found
		
	def DisplayItems(self):
		print '{0:10}{1:30}{2:10}'.format("GTIN8", "ProductDescription", "UnitPrice")
		print '{0:10}{1:30}{2:10}'.format("-----", "------------------", "---------")
		for aStockItem in self.MyItems:
			print '{0:10}{1:30}{2:10}'.format(aStockItem.GTIN8, aStockItem.ProductDescription, aStockItem.UnitPrice)
			
		
########################################################################
class BasketItem:
  def __init__(self, StockItem_in, Quantity_in):
      self.StockItem= StockItem_in
      self.Quantity = Quantity_in
      self.SubTotal = float(self.StockItem.UnitPrice) * float(self.Quantity)
    
  def displayAll(self):
    print self.StockItem.GTIN8, self.StockItem.ProductDescription, self.StockItem.UnitPrice , self.Quantity	
InvalidItem = []
########################################################################
class BasketList:
	MyItems=[]

	def __init__(self):
		MyCount = 0
	def AddItem(self, BasketItem):
		self.MyItems.append(BasketItem)
			
	def Total(self):
		theTotal=float (0)
		for Basketitem in self.MyItems :
			#print "Here:",Basketitem.displayAll()
			#print "SubTotal", Basketitem.SubTotal
			theTotal = float(theTotal) + float(Basketitem.SubTotal)
			#print "Total ",theTotal
		return float(theTotal)
	
	def Receipt(self):
		print '{0:10}{1:30}{2:9}{3:8}{4:8}'.format("GTIN8 ", "ProductDescription ", "UnitPrice ", "Quantity ", "SubTotal ")
		print '{0:10}{1:30}{2:9}{3:8}{4:8}'.format("----- ", "------------------ ", "--------- ", "-------- ", "-------- ")
		for i in range (len(InvalidItem)):
			print '{0:30}{1:60}'.format(InvalidItem[i],"Product not found")
		for aBasketItem in self.MyItems:
			print '{0:10} {1:30} {2:9} {3:8} {4:8}'.format(aBasketItem.StockItem.GTIN8, aBasketItem.StockItem.ProductDescription, aBasketItem.StockItem.UnitPrice, aBasketItem.Quantity, aBasketItem.SubTotal)
		print '{0:61}{1:8}'.format ("Grand Total", self.Total())

########################################################################
########################################################################
########################################################################

#### Open the File
f = open('StockFile1.txt')
#### Read in the file 
csv_f = csv.reader(f)

#### Create a Stock List
TheStockList = StockList()

#### Create a Basket List
TheBasketList = BasketList()


#### go through each row and add to a new Stock Item Object, then Add to List
for row in csv_f:
  TheStockItem = StockItem( row[0], row[1], row[2] )
  TheStockList.AddItem(TheStockItem)
  
TheStockList.DisplayItems()
 
done=False

while done==False:
	UserInputGTIN8=raw_input("please enter a GTIN-8 code for a product you would like to buy")
	rtn = TheStockList.FindGTIN8(UserInputGTIN8)
	if rtn > -1:
		foundStockItem = TheStockList.GetItem(rtn)
		#foundStockItem.displayAll()
		
		UserInputQuantity=raw_input("Please Enter Quantity")
		if UserInputQuantity > 0 and UserInputQuantity.isdigit():
			#print '{0}, {1}, {2}'.format(foundStockItem.ProductDescription, foundStockItem.UnitPrice, UserInputQuantity, "the price")
			TheBasketItem=BasketItem(foundStockItem, int(UserInputQuantity))
			#TheBasketItem.displayAll()
			TheBasketList.AddItem(TheBasketItem)
		else:
			print "Invalid quantity"
	
	else:
		
		print "GTIN8 invalid or not found : ", UserInputGTIN8
		InvalidItem.append(UserInputGTIN8)
	
	UserInputQuit=raw_input('Are you finished shopping? (Y/N)')


	if UserInputQuit=="Y":
		done=True
		TheBasketList.Receipt()
		
print "All done!!!"









