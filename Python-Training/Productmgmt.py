import mysql.connector

mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "rps@123", database = "kpmg")

mycursor = mydb.cursor()
#mycursor.execute("create table products_info(productId int(10),productName varchar(20),productPrice int,productDesc varchar(30),productCategory varchar(10))")

class KPMGProduct:
    
    print("---KPMG Product Management Application--- \n 1. Add Product \n 2. Update Product \n 3. Delete ProductById \n 4. Get ProductById \n 5. Get All Products ")
    option = int(input("Enter your option number : ")) 
    if option == 1:
        
        prodId = int(input("Product ID : "))
        prodName = input("Product Name : ")
        prodPrice = int(input("Product Price : "))
        prodDesc = input("Product Description : ")
        prodCategory = input ("Product Category : ")
        mycursor.execute(f"INSERT INTO  products_details VALUES({prodId},'{prodName}',{prodPrice},'{prodDesc}','{prodCategory}')")
        mydb.commit()
        print("Data inserted successfully")
    elif option == 2:
        
        pid = int(input("Enter product Id for updating price : "))
        pPrice = int(input("Enter updated Price : "))
        mycursor.execute(f"UPDATE products_details set productPrice = {pPrice}  where productId = {pid}" )
        mydb.commit()

    elif option ==3:
       
        pid = int(input("Enter product Id for deleting data : "))
        mycursor.execute(f"DELETE FROM products_details where productId = {pid}" )
        mydb.commit()

    elif option == 4:
       
        pid = int(input("Enter product Id to display data : "))
        mycursor.execute(f"SELECT * FROM  products_details where productId = {pid}" )
        myresult = mycursor.fetchone()
        print(myresult)
       
    elif option == 5:
        
        mycursor.execute("select * from products_details")
        data = mycursor.fetchall()

        for row in data:
            print("ProductID : ",row[0])
            print("Product Name : ",row[1])
            print("Product Price : ",row[2])
            print("Product Description : ",row[3])
            print("Product Category : ",row[4])