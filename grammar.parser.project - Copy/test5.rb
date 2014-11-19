MODULE z ;
BEGIN
  y := 8 ;
  z := + y 13 ;
  IF < y z THEN
    WHILE < y z DO
      y := + y 1 ;
      WriteInt ( y ) ;
    END ;
  ELSE
    WriteInt ( 0 ) ;
  END ;
REPEAT IF == y z THEN WriteInt ( 100 ) ;
ELSE WriteInt ( 199 ) ; END ; UNTIL == y z ;

 END
y .

