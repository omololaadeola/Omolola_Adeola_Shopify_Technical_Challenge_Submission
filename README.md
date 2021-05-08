# Omolola_Adeola_Shopify_Technical_Challenge_Submission

https://docs.google.com/document/d/1-R1738GaUW1EJcneTxRE6gXO2RANA-ykGCpinu--bY8/edit

Answer To Question 2;

Orders shipped by Speedy Express in total.

3.    SELECT * FROM [Orders] a
4.    JOIN Shippers b
5.    on b.ShipperID = a.ShipperID 
6.    WHERE b.ShipperName = "Speedy Express"
Answer = 54

Name of Employee With The Most Orders.

7.with b AS
(
8.SELECT Orders.EmployeeID, Employees.LastName, Orders.OrderID
9.FROM Orders
10.JOIN Employees
11.ON Employees.EmployeeID=Orders.EmployeeID
)
11.SELECT b.LastName, COUNT(*)
12.FROM b
13.GROUP BY b.LastName
14.ORDER BY COUNT(*) desc
15.limit 1

Answer     COUNT(*)
Peacock    40

Products that was ordered the most by customers in Germany.

16with Products_Ordered AS
(
17.SELECT Orders.OrderID, Customers.Country, OrderDetails.Quantity, Products.ProductName
18.FROM Orders, OrderDetails
19.JOIN Customers ON Orders.CustomerID=Customers.CustomerID
20.JOIN Products ON OrderDetails.ProductID=Products.ProductID
21.WHERE Country='Germany'
),
22.Product_Orders AS
(
23.SELECT ProductName, Quantity, COUNT(*) as 'Orders'
24.FROM Products_Ordered
25.GROUP BY ProductName
)
26.SELECT ProductName, Quantity, Orders, (Quantity * Orders) AS TotalOrdered
27.FROM Product_Orders
28.ORDER BY TotalOrdered desc
29.LIMIT 1;

ProductName        Quantity    Orders    TotalOrdered
Camembert Pierrot    40        300    12000
