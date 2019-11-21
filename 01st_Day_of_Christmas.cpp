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
    ifstream InputFile(InputFileName);

    char inputDigit;
    vector<int> CaptchaList, CaptchaListShifted;

    // read digits one by one into a vector
    while (InputFile>>inputDigit)
    {
        CaptchaList.push_back( inputDigit - 48 );
    }


    CaptchaListShifted = CaptchaList;
    rotate(CaptchaListShifted.begin(),CaptchaListShifted.begin()+1,CaptchaListShifted.end());

    int SumOfDigits = 0;

    for (int i = 0; i < CaptchaList.size(); i++)
    {
        if (CaptchaList[i] == CaptchaListShifted[i])
        {
            SumOfDigits += CaptchaList[i];
        }
    }

    cout << "First part solution is: " << SumOfDigits << "\n";

// part 2
    vector<int> CaptchaListExtended, CaptchaListShiftedExtended;
    rotate(CaptchaListShifted.begin(),CaptchaListShifted.begin()+CaptchaListShifted.size()/2-1,CaptchaListShifted.end());

    CaptchaListExtended = CaptchaList;
    CaptchaListShiftedExtended = CaptchaListShifted;

    CaptchaListExtended.insert(CaptchaListExtended.end(),CaptchaList.begin(),CaptchaList.begin()+CaptchaList.size()/2);
    CaptchaListShiftedExtended.insert(CaptchaListShiftedExtended.end(),CaptchaListShifted.begin(),CaptchaListShifted.begin()+CaptchaListShifted.size()/2);


    int SumOfDigitsHalfway = 0;

    for (int i = 0; i < CaptchaList.size(); i++)
    {
        if (CaptchaList[i] == CaptchaListShifted[i])
        {
            SumOfDigitsHalfway += CaptchaList[i];
        }
    }

    cout << "Second part solution is: " << SumOfDigitsHalfway << "\n";

    return 0;
}