A basic flask app that accepts a POST request of operation type and two integers. 
{ “operation_type”: Enum <addition | subtraction | multiplication> , “x”: Integer, “y”: Integer }
Operation can either be addition, subtraction or mutiplication
x can be a number and Integer datatype
y can be a number and Integer datatype

A response with the result of the operation and your slack username is returned
{ “slackUsername”: String, "operation_type" : Enum. value, “result”: Integer }