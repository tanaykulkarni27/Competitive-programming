#include<iostream>
#include<bits/stdc++.h>
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
struct node{
	struct node* arr[26];
	bool isend ;
};
struct node* getnode(){
	struct node* child = new node;
	child->isend = false;
	for(int i=0;i<26;i++)
	child->arr[i] = NULL;
	return child;
}
void insert(struct node* root ,string key){
	struct node* temp = root;
	for(int i=0;i<key.length();i++){
		int index = (int)key[i]-97;
		if(!temp->arr[index])
			temp->arr[index] = getnode();
		temp = temp->arr[index];
	}
	temp->isend = true;
}
bool search(struct node* root,string st){
	struct node* t = root;
	int pnt = 0;
	for(pnt=0;pnt<st.length();pnt++){
		int index = (int)st[pnt]-'a';	
		if(!t->arr[index])
			return false;
		else
		t = t->arr[index];
	}
	return (t!=NULL && t->isend);
}
// End Area to write solution
int main(){
	string a[5];
	string sear[5];
	readr(a,5);
	readr(sear,5);
	struct node* obj = getnode();
	for(auto v : a){
		insert(obj,v);
	}
	for(auto v : sear){
		cout<<search(obj,v)<<endl;
	
	}
	return 0;
}
/*
tanay tanhaji reshma sanika dhananjay
taay tanhaji reshma sanika dhananjay
*/
