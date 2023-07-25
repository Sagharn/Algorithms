#include<iostream>
using namespace std;
int main()
{
    int len, i, arr[50], num, first, last, middle;
    cin>>len;
    for(i=0; i<len; i++)
        cin>>arr[i];
    cin>>num;
    first = 0;
    last = (len-1);
    middle = (first+last)/2;
    while(first <= last)
    {
        if(arr[middle]<num)
            first = middle+1;
        else if(arr[middle]==num)
        {
            cout<<middle+1;
            break;
        }
        else
            last = middle-1;
        middle = (first+last)/2;
    }
    return 0;
}
