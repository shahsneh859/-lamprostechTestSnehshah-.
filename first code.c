#include <stdio.h>
#include <conio.h>
//Creating main class
int getValue(const char * s){
    switch(*s) {
        case 'I': return 1;
        case 'V': return 5;
        case 'X': return 10;   
        case 'L': return 50;
        case 'c': return 100;
        case 'D': return 500;
        case 'M': return 1000;
    }
    return 0;
}
//Output
int romanToInt(char * s){
    int result = 0; 
    
    for(;*s != '\0'; ++s) {
        result += getValue(s);
    }
    return result;
}
