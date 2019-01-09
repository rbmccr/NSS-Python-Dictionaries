# block of publicly-traded stocks
stockDict = {
  'GM': 'General Motors',
  'CAT':'Caterpillar',
  'EK':'Eastman Kodak',
  'C':'Citigroup',
  'AAPL':'Apple Inc',
  'MSFT':'Microsoft',
  'INTC':'Intel',
  'LUV':'Southwest Airlines',
  'WMT':'Walmart',
  'TGT':'Target'
}

# simple list of blocks of stock (list of tuples)
# includes ticker symbol, num shares, date, price
purchases = [
 ( 'GM', 100, '10-sep-2010', 48 ),
 ( 'CAT', 50, '1-apr-2009', 24 ),
 ( 'CAT', 45, '1-jul-2009', 29 ),
 ( 'C', 1100, '10-sep-2008', 48 ),
 ( 'EK', 680, '1-apr-2004', 8 ),
 ( 'TGT', 200, '1-jul-2003', 56 ),
 ( 'AAPL', 50, '10-sep-2002', 480 ),
 ( 'WMT', 88, '1-apr-1997', 39 ),
 ( 'INTC', 200, '1-jul-1998', 77 )]

 # -----------------------------------------------------------------

 # Create a purchase history report that computes the full purchase price (shares times dollars) for each block of stock and uses the stockDict to look up the full company name.

purchase_history_report = []

for item in purchases:
  purchase_price = item[1] * item[3]
  stock_name = stockDict[item[0]]
  purchase_history_report.append((stock_name, "$" + str(purchase_price), item[2]))

print(purchase_history_report)

# PRINT RESULT:
# [('General Motors', '$4800', '10-sep-2010'),
#  ('Caterpillar', '$1200', '1-apr-2009'),
#  ('Caterpillar', '$1305', '1-jul-2009'),
#  ('Citigroup', '$52800', '10-sep-2008'),
#  ('Eastman Kodak', '$5440', '1-apr-2004'),
#  ('Target', '$11200', '1-jul-2003'),
#  ('Apple Inc', '$24000', '10-sep-2002'),
#  ('Walmart', '$3432', '1-apr-1997'),
#  ('Intel', '$15400', '1-jul-1998')]

# -----------------------------------------------------------------

 # Create a second purchase summary that accumulates total investment by ticker symbol.

 # Multiple blocks of the same stock can easily be combined by creating a dict where the key is the ticker and the value is the LIST OF BLOCKS purchased.

 # The program makes one pass through the data to create the dict.

 # A pass through the dict can then create a report showing each ticker symbol and all blocks of stock.

purchase_summary = {}

for item in purchases:
  stock_ticker = item[0]
  if stock_ticker in purchase_summary:
    purchase_summary[item[0]].append((item[1], item[2], item[3]))
  else:
    purchase_summary[item[0]] = []
    purchase_summary[item[0]].append((item[1], item[2], item[3]))

print(purchase_summary)

# PRINT RESULT (Dictionary -- See CAT: it's the only stock with more than one stock purchase listed):
# {'GM': [(100, '10-sep-2010', 48)],
# 'CAT': [(50, '1-apr-2009', 24), (45, '1-jul-2009', 29)],
# 'C': [(1100, '10-sep-2008', 48)],
# 'EK': [(680, '1-apr-2004', 8)],
# 'TGT': [(200, '1-jul-2003', 56)],
# 'AAPL': [(50, '10-sep-2002', 480)],
# 'WMT': [(88, '1-apr-1997', 39)],
# 'INTC': [(200, '1-jul-1998', 77)]}

# for each list of blocks, loop the list and accumulate purchase_price. Print the total investment once each block has been added to the total
for stock, purchases in purchase_summary.items():
  purchase_price = 0
  list_length = 0 # used to determine when the total is calculated completely
  print('-------- ' + stock + ' --------')
  for block in purchases:
    print(block)
    list_length += 1
    purchase_price += block[0] * block[2]
    if len(purchase_summary[stock]) == list_length:
      print("Total stock investment: " + "$" + str(purchase_price) + '\n')

# PRINT RESULT:

# -------- C --------
# (1100, '10-sep-2008', 48)
# Total stock investment: $

# -------- EK --------
# (680, '1-apr-2004', 8)
# Total stock investment: $5440

# -------- TGT --------
# (200, '1-jul-2003', 56)
# Total stock investment: $11200

# -------- AAPL --------
# (50, '10-sep-2002', 480)
# Total stock investment: $24000

# -------- CAT --------
# (50, '1-apr-2009', 24)
# (45, '1-jul-2009', 29)
# Total stock investment: $2505

# -------- INTC --------
# (200, '1-jul-1998', 77)
# Total stock investment: $15400

# -------- GM --------
# (100, '10-sep-2010', 48)
# Total stock investment: $4800

# -------- WMT --------
# (88, '1-apr-1997', 39)
# Total stock investment: $3432