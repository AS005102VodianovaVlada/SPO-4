from gpio import *
from time import *

def main():  
    pinMode(1, IN)  
    pinMode(2, OUT)  
    pinMode(3, OUT)  
    
    print("Blinking")  
    while True:   
        TEMP = analogRead(1);  
        TEMP_CEL = ((float(TEMP)/1023)*200-100);   
        if TEMP_CEL < 20:    
            digitalWrite(2, LOW); 
            print("Low temperature, turn on the heating element");    
            digitalWrite(3, HIGH);    
            print("Heating element finished");    
            print("Temp now = ");
            print(TEMP_CEL); 
            delay(500);   
        elif TEMP_CEL > 25:    
            digitalWrite(3, LOW);   
            print("High temperature, turn on the air cooler");    
            digitalWrite(2, HIGH);    
            print("Air cooler finished");    
            print("Temp now = ");    
            print(TEMP_CEL);    
            delay(500);   
        else:   
            print("The temp is normal");    
            print("Temp now = ");    
            print(TEMP_CEL);    
            delay(500); 
 
if __name__ == "__main__":  
    main() 
