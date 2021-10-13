#include <iostream>

using namespace std;

int MinMaxInTwoArray(int arr1[], int arr2[], int len1, int len2, int k){
    int m=0,n=0;
    for(int i=0,j=0;i<len1,j<len2;i++,j++){
        if(arr1[i]>k)
        m++;
        if(arr2[j]<k)
        n++;
    }
    cout<<m<<n;
    return m>n?m:n;   
}

int main()
{
    int arr1[]={9,16,12,5,15};
    int arr2[]={14,7,22,5,32,77};
    int len1=5;
    int len2=6;
    int k=9;
    cout<<MinMaxInTwoArray(arr1,arr2,len1,len2,k);
}
