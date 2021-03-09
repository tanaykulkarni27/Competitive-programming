#include<iostream>
#include<bits/stdc++.h>
#include<math.h>
#include<string>
#define FOR(start,end) for(int i=start;i<end;i++)
#define lli long long int 
#define read(a) cin>>a;
#define readr(b,n) for(int i=0;i<n;i++){cin>>b[i];}
#define pass ;
#define printarr(arr,n) FOR(0,n){cout<<arr[i]<<" "; }cout<<endl;
using namespace std;
//reverse
void reverse(lli arr[],lli n){
	lli mid = (lli)((n-1)/2);
	lli last = n-1;
	FOR(0,mid+1){
	lli temp = arr[last-i];
	arr[last-i] = arr[i];
	arr[i] = temp;	
	}
}
// deletion
int del(int arr[],int n,int index){
	if(n==0)
	return 0;
	FOR(index,n){
		arr[i] = arr[i+1];
	}
	return n-1;
}
int remove(int arr[],int n,int element){
	int temp = 0;
	int index;
	FOR(0,n){
	if(arr[i] == element){
		temp = i;
		break;
	}	
	}
	if(temp == 0)
	return n;
	else
	del(arr,n,temp);	
}

// A^N
lli power(lli a,lli n){
	if(n==0)
	return 1;
	lli half_power = power(a,(lli)n/2);
	if(n%2==0)
	return half_power*half_power;
	else
	return half_power*half_power*a;
}
// linear search
bool linear_search(long long int arr[],long long int n,long long int find){
	FOR(0,n){
		if(arr[i] == find)
		return 0;
	}
	return 1;
}
// binary search
bool binary_search(int arr[],int l,int r,int find){
int mid = l+(r-1)/2;
cout<<mid<<"\n";  
if(arr[l] == find || arr[r] == find || arr[mid] == find)
return 0;
if(l>r)
	return 1;
if(arr[l]<find)
return binary_search(arr,mid+1,r,find);
return binary_search(arr,l,mid-1,find);
}
// insertion
lli append(lli arr[],lli n,lli element){
	arr[n] = element;
	return n+1;
}
// Start Area to write solution

void solve(){
int n;
read(n)
vector<int>mat(n);
for(int i = 0;i<n;i++){
	int k;
	read(k)
	int bnf = 0;
	for(int j = 0;j<k;j++){
		int temp;
		read(temp)
		bnf+=(int)1<<(temp);
	}
	mat[i] = bnf;

}
int ans = 0;
for(int i = 0;i<n;i++){
	for(int j= i+1;j<n;j++){
		ans = max((int)__builtin_popcount((mat[i]&mat[j])),ans);
		
	}
//	cout<<endl;
}
cout<<ans<<"\n";
}
// End Area to write solution
int main(){
	int t;
	read(t)
	FOR(1,t+1){
		cout<<"Case #"<<i<<": ";
		solve();
	}
	return 0;
}
/* 
1
3
5
2 3 5 6 8
4
2 4 5 8
6
1 2 10 12 14 16

*/
