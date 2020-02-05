// Puzzle found here: https://www.codingame.com/ide/puzzle/chuck-norris
#include <iostream>
#include <string>
#include <bitset>

using namespace std;

// Method Prototypes
string convertToBits (string message, string bits);
string norrisify (string bits);

int main()
{
    string MESSAGE;
    getline(cin, MESSAGE);
    
    // Create a string of bits from the sent Message
    string bitString = convertToBits(MESSAGE, bitString);
    
    // Convert the string of bits to the Norris Encoded String
    bitString = norrisify(bitString);

    // output the converted string
    cout << bitString << endl;
}

// Takes in a string and iterates through it character by character converting them to 7 bit bitsets.
// Returns a new string containing the bitString
string convertToBits (string message, string bitsConverted){
    for (auto i : message){
        bitset<7>bits(i);
        bitsConverted += bits.to_string();
    }
    return bitsConverted;
}

// Converts a string of bits into Norris code
string norrisify (string bits){
    // Declare a string to hold final output
    string output = "";
    cerr << bits << endl;
    
    // Declare comparison variable
    char prev = '2'; // init to a junk, value to fail check;
    for(auto i : bits){
        // Check for the length to see if we are starting the conversion
        if(output.length() != 0){
            //cerr << prev << endl;
            if(i == prev){
                // The same bit has repeated append a 0
                output += "0";
            }else if(i == '0'){
                // The output has changed to 0
                output += " 00 0";
            }else{
                // The output bit has changed to 1 
                output += " 0 0";
            }
            prev = i;
        }else{
            // this is the first digit of the string
            output += (i == '0') ? "00 0" : "0 0";
            prev = i;
        }
    }
    cerr << endl;
    return output;
}
