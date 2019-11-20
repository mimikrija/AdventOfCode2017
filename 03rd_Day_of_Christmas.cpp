#include <algorithm>
#include <vector>
#include <iostream>

using namespace std;

int SquareCircumference(int SquareNo)
{
	return 8 * (SquareNo - 1);
}

int main()
{
	int input;
	cin >> input;
	int SpiralDistance = 1;
	int RadialDistance = 1;
	vector<int> CrossPositions = { 1 };

	while (SpiralDistance < input)
	{
		RadialDistance++;
		SpiralDistance += SquareCircumference(RadialDistance);
		CrossPositions.push_back(CrossPositions.back() + 2 * RadialDistance - 3);
		for (int i = 2; i <= 4; i++)
		{
			CrossPositions.push_back(CrossPositions.back() + 2 * (RadialDistance - 1));
		}

	}

	// calculate lateral distance - there is an error here
	int LateralDistance = input;
	vector<int> LateralsInTheSquare(4, 0);
	copy(CrossPositions.end() - 4, CrossPositions.end(), LateralsInTheSquare.begin());
	LateralsInTheSquare.push_back(input);
	sort(LateralsInTheSquare.begin(), LateralsInTheSquare.end());
	unique(LateralsInTheSquare.begin(), LateralsInTheSquare.end());
	if (LateralsInTheSquare.size() == 4 ) LateralDistance = 0;
	auto pos = find(LateralsInTheSquare.begin(), LateralsInTheSquare.end(), input);

	int neighbor1, neighbor2;

	if (pos == LateralsInTheSquare.begin())
	{
		LateralDistance =  *(pos + 1) - input;
	}
	else
	{
		if (pos == LateralsInTheSquare.end() - 1 )
		{
			LateralDistance = input - *(pos - 1);
		}
		else
		{
			neighbor1 = *(pos - 1);
			neighbor2 = *(pos + 1);
			LateralDistance = min(abs(input-neighbor1), abs(input - neighbor2));
		}
	}





	RadialDistance--; // because we are measuring from 1.

	int ManhattanDistance = RadialDistance + LateralDistance;
	// Radial Distance is CurrentSquare (once I get it right)

	cout << "Manhattan distance is: " << ManhattanDistance << "\n";

	return 0;
}