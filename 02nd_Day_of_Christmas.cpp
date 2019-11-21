#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>
#include <iterator>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

int main()
{
    string InputFileName;
    cout << "Input file name?";
    cin >> InputFileName;

    // read input line per line
	ifstream InputFile(InputFileName);
    vector<int> ListOfNumbers{ istream_iterator<int>{InputFile},{} };

    int rows = 16; // i have no idea how to read the number of lines in a file without declaring a new ifstream!
    int columns = ListOfNumbers.size()/rows;
    int Checksum = 0;

    int ChecksumDivision = 0;

    for ( int counter = 0; counter < rows; counter ++)
    {
        auto max = max_element(ListOfNumbers.begin()+counter*columns,ListOfNumbers.begin()+columns+counter*columns);
        auto min = min_element(ListOfNumbers.begin()+counter*columns,ListOfNumbers.begin()+columns+counter*columns);
        int diff = *max - *min;
        Checksum += diff;
        vector<int> temp(columns,0);
        sort (ListOfNumbers.begin()+counter*columns,ListOfNumbers.begin()+columns+counter*columns);
        copy ( ListOfNumbers.begin()+counter*columns,ListOfNumbers.begin()+columns+counter*columns, temp.begin() );
        int pos = 0 ;
        bool found = false;
        while( !found )
        {
            int divisor = temp[pos];
            auto it = find_if(temp.begin()+temp.size()/2-1,temp.end(),[divisor](int compare){return compare%divisor == 0;});
            if ( it < temp.end() )
            {
                found = true;
                ChecksumDivision += *it / divisor;
            }
            else
            {
                pos++;
            }
        }


    }

    cout << "First part solution is: " << Checksum << "\n";
    cout << "First part solution is: " << ChecksumDivision << "\n";


    return 0;
}