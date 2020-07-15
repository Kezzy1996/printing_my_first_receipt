# created a variable for the product names and their prices
p1_name="books"
p2_name = "Computer"
p1_price=49.95
p2_price= 579.99
p3_name= "Monitor"
p3_price=124.89
# created the company name and its address
company_name = "coding temple, inc."
company_address = "283 Franklin St."
company_city = "Boston, MA"
 # declared ending message
message = "Thanks for shopping with us today!"
 # created the top border
print( "*" * 50 )
# printed company information first, using format
print( "\t\t{}" .format(company_name .title()))
print( "\t\t{}".format(company_address) ) 
print( "\t\t{}".format(company_city) )
# printed a line between sections
print( "=" * 50 )
# printed out header for section of items
print("\tProduct Name\tProduct Price")
# createed a print statement for each product
print( "\t{}\t\t${}".format(p1_name.title( ), p1_price) )
print( "\t{}\t${}".format(p2_name.title( ), p2_price) ) 
print( "\t{}\t\t${}".format(p3_name.title( ), p3_price) )
# printed a line between sections
print('=' * 50)
# printed out header for section of total
print("\t\t\tTotal")
 # calculated total price and print out
total = p1_price + p2_price + p3_price
print( "\t\t\t${}".format(total) )
# printed a line between sections
print( "=" * 50)
# output thank you message
print( "\n\t{}\n".format(message) )
# create a bottom border
print( "*" * 50 )

