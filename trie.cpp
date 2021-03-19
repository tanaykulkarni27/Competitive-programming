#include<stdio.h>
#include<iostream>
#include<bits/stdc++.h>
#include<map>
#include <vector> 
#include<string>
using namespace std;
#define FOR(start,end) for(int i=start;i<end;i++)
#define lli long long int 
#define read(a) cin>>a;
#define readr(b,n) for(lli i=0;i<n;i++){cin>>b[i];}
#define printarr(arr,n) FOR(0,n){cout<<arr[i]<<" "; }cout<<endl;
const long int MOD = 1000000007;
struct lnode{
	bool is_end;
	struct lnode* chars[26];
};
struct lnode* new_node(){
		struct lnode* nw = new lnode();
		for (int i = 0; i < 26; ++i)
				{
					nw->chars[i] = NULL;
				}		
		nw->is_end = false;
		return nw;
	}
void del(struct lnode* root,string key){
	struct lnode* tmp = root;
	for (int i = 0; i < key.length() && tmp!= NULL; ++i)
	{
		int index = key[i]-'a';
		tmp = tmp->chars[index];
	}
	if(tmp!=NULL)
		tmp->is_end = false;
	return;
}
void insert(struct lnode* tmp,string data){
		//struct lnode* tmp = root;
		for(auto i : data){
			int index = i-'a';
			if(!tmp->chars[index])
				tmp->chars[index] = new_node();
			tmp = tmp->chars[index];
		}
		tmp->is_end = true;
}	
bool search(struct lnode* root,string key){
	struct lnode* tmp = root;
	for(auto i : key){
		int index = i-'a';
		if(tmp->chars[index] == NULL)
			return false;
		tmp = tmp->chars[index];
	}
	return tmp!=NULL && tmp->is_end ;
}
void dfs(struct lnode* root,string s){
	if(root->is_end == true)
		cout<<s<<" ";
	for (int i = 0; i < 26; ++i)
	{ 
		if(root->chars[i]!=NULL)
			dfs(root->chars[i],s+(char)(i+'a'));
	}
}
void solve(){
	struct lnode* root = new_node();
	string s[5] = {"tanay","abhinav","yashodhan","prashant","anupama"};
	for(auto i : s)
		insert(root,i);
	
	string res = search(root,"tanay")? "WORD FOUND ":"WORD NOT FOUND"; 
	cout<<res;

	//dfs(root,"");
}
int main(){
	solve();
	return 0;
}
